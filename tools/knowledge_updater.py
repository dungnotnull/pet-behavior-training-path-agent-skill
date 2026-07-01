"""
knowledge_updater.py — Skill #231: Pet Behavior Analysis & Training Path
Crawl4AI-based knowledge pipeline for SECOND-KNOWLEDGE-BRAIN.md

Fetches latest research on pet behavioral science from:
  - PubMed E-utilities API (no API key required for basic search)
  - Semantic Scholar API (free tier)
  - IAABC Journal (web scraping via crawl4ai)
  - AVSAB Position Statements (web scraping via crawl4ai)

Scores entries by recency + relevance, deduplicates by DOI/URL hash,
and appends new entries to SECOND-KNOWLEDGE-BRAIN.md.

Recommended schedule: weekly cron — 0 2 * * 0 (Sundays 02:00)

Usage:
  python knowledge_updater.py
  python knowledge_updater.py --dry-run       # Preview without writing
  python knowledge_updater.py --max-results 5 # Limit results per query

Requirements:
  pip install crawl4ai httpx asyncio aiofiles python-dateutil
"""

import argparse
import asyncio
import hashlib
import json
import logging
import re
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Optional
from urllib.parse import urlencode, urlparse

import httpx
from dateutil.parser import parse as dateutil_parse

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SKILL_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_BRAIN_PATH = SKILL_DIR / "SECOND-KNOWLEDGE-BRAIN.md"

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"
IAABC_JOURNAL_URL = "https://iaabc.org/journal/"
AVSAB_URL = "https://avsab.org/resources/position-statements/"

PUBMED_SEARCH_TERMS = [
    "canine behavior training",
    "feline anxiety treatment",
    "positive reinforcement dog",
    "separation anxiety dog treatment",
    "canine cognitive dysfunction",
    "counter-conditioning dog fear",
    "feline stress behavior",
    "hyperkinesis dog",
    "pet enrichment behavioral",
    "animal behavior therapy",
    "LIMA training animals",
    "veterinary behavioral medicine",
]

SEMANTIC_SCHOLAR_QUERIES = [
    "animal behavior therapy dog cat",
    "veterinary behavioral medicine positive reinforcement",
    "canine separation anxiety treatment",
    "feline anxiety enrichment",
]

# Domain keywords for relevance scoring
DOMAIN_KEYWORDS = [
    "canine", "feline", "dog", "cat", "animal behavior", "veterinary behavior",
    "separation anxiety", "aggression", "hyperactivity", "training", "enrichment",
    "positive reinforcement", "counter-conditioning", "desensitization", "LIMA",
    "clicker training", "fear free", "IAABC", "AVSAB", "behavioral modification",
    "cognitive dysfunction", "anxiety", "fear", "compulsive", "welfare",
    "reward-based", "operant conditioning", "classical conditioning",
]

SCORING_RECENCY_WEIGHT = 0.5
SCORING_RELEVANCE_WEIGHT = 0.5
MIN_SCORE_TO_APPEND = 0.30

MAX_RESULTS_PER_PUBMED_TERM = 10
MAX_RESULTS_SEMANTIC_SCHOLAR = 10

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("knowledge_updater")


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class PaperEntry:
    """Represents one research paper or resource to potentially add."""

    def __init__(
        self,
        title: str,
        authors: str,
        year: Optional[int],
        venue: str,
        doi_or_url: str,
        abstract: str,
        source: str,
    ):
        self.title = title.strip()
        self.authors = authors.strip()
        self.year = year
        self.venue = venue.strip()
        self.doi_or_url = doi_or_url.strip()
        self.abstract = abstract.strip()[:500]  # Truncate long abstracts
        self.source = source
        self.relevance_score: float = 0.0
        self.recency_score: float = 0.0
        self.combined_score: float = 0.0
        self.url_hash: str = self._compute_hash()

    def _compute_hash(self) -> str:
        """MD5 hash of DOI or URL for deduplication."""
        normalized = self.doi_or_url.lower().strip().rstrip("/")
        return hashlib.md5(normalized.encode()).hexdigest()

    def compute_scores(self, current_year: int) -> None:
        """Compute recency and relevance scores."""
        # Recency: 1 / (1 + years_since_publication)
        if self.year and self.year > 1900:
            years_since = max(0, current_year - self.year)
            self.recency_score = 1.0 / (1.0 + years_since)
        else:
            self.recency_score = 0.1  # Unknown year: low recency score

        # Relevance: keyword match count / total keywords
        text_to_check = (self.title + " " + self.abstract + " " + self.venue).lower()
        matched = sum(1 for kw in DOMAIN_KEYWORDS if kw.lower() in text_to_check)
        self.relevance_score = matched / len(DOMAIN_KEYWORDS)

        # Combined weighted score
        self.combined_score = (
            SCORING_RECENCY_WEIGHT * self.recency_score
            + SCORING_RELEVANCE_WEIGHT * self.relevance_score
        )

    def to_markdown_row(self) -> str:
        """Format as a markdown table row for SECOND-KNOWLEDGE-BRAIN.md."""
        authors_short = self.authors[:60] + "..." if len(self.authors) > 60 else self.authors
        title_short = self.title[:80] + "..." if len(self.title) > 80 else self.title
        return (
            f"| {title_short} | {authors_short} | {self.year or 'n/a'} "
            f"| {self.venue[:40]} | {self.doi_or_url} | Auto-added by knowledge_updater |"
        )


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def load_existing_hashes(brain_path: Path) -> set[str]:
    """Extract existing DOI/URL hashes from SECOND-KNOWLEDGE-BRAIN.md."""
    if not brain_path.exists():
        logger.warning("SECOND-KNOWLEDGE-BRAIN.md not found at %s", brain_path)
        return set()

    text = brain_path.read_text(encoding="utf-8")
    existing_hashes: set[str] = set()

    # Extract all URLs and DOIs from the markdown (look for http, doi.org patterns)
    urls_and_dois = re.findall(
        r"(https?://[^\s|)]+|10\.\d{4,}/[^\s|)]+)",
        text,
    )
    for identifier in urls_and_dois:
        normalized = identifier.lower().strip().rstrip("/")
        existing_hashes.add(hashlib.md5(normalized.encode()).hexdigest())

    logger.info("Loaded %d existing entry hashes from knowledge brain.", len(existing_hashes))
    return existing_hashes


# ---------------------------------------------------------------------------
# PubMed Fetcher
# ---------------------------------------------------------------------------

async def fetch_pubmed_papers(
    client: httpx.AsyncClient,
    search_term: str,
    max_results: int,
) -> list[PaperEntry]:
    """Search PubMed and return PaperEntry objects."""
    entries: list[PaperEntry] = []

    # Step 1: ESearch — get PMIDs
    esearch_params = {
        "db": "pubmed",
        "term": search_term,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance",
    }
    try:
        resp = await client.get(
            f"{PUBMED_BASE}esearch.fcgi",
            params=esearch_params,
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        pmids = data.get("esearchresult", {}).get("idlist", [])
    except Exception as exc:
        logger.warning("PubMed ESearch failed for '%s': %s", search_term, exc)
        return entries

    if not pmids:
        logger.info("No PubMed results for '%s'", search_term)
        return entries

    # Step 2: ESummary — get metadata
    esummary_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
    }
    try:
        resp = await client.get(
            f"{PUBMED_BASE}esummary.fcgi",
            params=esummary_params,
            timeout=30.0,
        )
        resp.raise_for_status()
        summary_data = resp.json()
        result = summary_data.get("result", {})
    except Exception as exc:
        logger.warning("PubMed ESummary failed for '%s': %s", search_term, exc)
        return entries

    # Step 3: EFetch abstracts (batch)
    efetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "rettype": "abstract",
        "retmode": "text",
    }
    try:
        resp = await client.get(
            f"{PUBMED_BASE}efetch.fcgi",
            params=efetch_params,
            timeout=30.0,
        )
        resp.raise_for_status()
        abstract_text = resp.text
    except Exception as exc:
        logger.warning("PubMed EFetch failed: %s", exc)
        abstract_text = ""

    # Parse abstracts per PMID (simple heuristic: split by PMID blocks)
    abstract_map: dict[str, str] = {}
    current_pmid: Optional[str] = None
    current_abstract_lines: list[str] = []

    for line in abstract_text.splitlines():
        pmid_match = re.match(r"^(\d+)\.", line)
        if pmid_match:
            if current_pmid and current_abstract_lines:
                abstract_map[current_pmid] = " ".join(current_abstract_lines).strip()
            current_pmid = pmid_match.group(1)
            current_abstract_lines = []
        elif current_pmid:
            current_abstract_lines.append(line.strip())

    if current_pmid and current_abstract_lines:
        abstract_map[current_pmid] = " ".join(current_abstract_lines).strip()

    # Build PaperEntry objects
    for pmid in pmids:
        if pmid not in result or pmid == "uids":
            continue
        record = result[pmid]
        title = record.get("title", "Unknown title")
        # Authors: list of author objects
        authors_list = record.get("authors", [])
        authors_str = "; ".join(
            a.get("name", "") for a in authors_list[:5]
        )
        if len(authors_list) > 5:
            authors_str += " et al."
        # Year from pubdate
        pubdate = record.get("pubdate", "")
        year: Optional[int] = None
        year_match = re.search(r"\b(19|20)\d{2}\b", pubdate)
        if year_match:
            year = int(year_match.group())
        source = record.get("source", "PubMed")
        doi = ""
        for art_id in record.get("articleids", []):
            if art_id.get("idtype") == "doi":
                doi = "https://doi.org/" + art_id.get("value", "")
                break
        if not doi:
            doi = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

        abstract = abstract_map.get(pmid, "")

        entry = PaperEntry(
            title=title,
            authors=authors_str or "Unknown authors",
            year=year,
            venue=source,
            doi_or_url=doi,
            abstract=abstract,
            source="PubMed",
        )
        entries.append(entry)

    logger.info("PubMed '%s': fetched %d entries", search_term, len(entries))
    return entries


# ---------------------------------------------------------------------------
# Semantic Scholar Fetcher
# ---------------------------------------------------------------------------

async def fetch_semantic_scholar_papers(
    client: httpx.AsyncClient,
    query: str,
    max_results: int,
) -> list[PaperEntry]:
    """Search Semantic Scholar and return PaperEntry objects."""
    entries: list[PaperEntry] = []
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,year,venue,externalIds,abstract",
    }
    try:
        resp = await client.get(
            SEMANTIC_SCHOLAR_BASE,
            params=params,
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        papers = data.get("data", [])
    except Exception as exc:
        logger.warning("Semantic Scholar failed for '%s': %s", query, exc)
        return entries

    for paper in papers:
        title = paper.get("title") or "Unknown title"
        authors_list = paper.get("authors", [])
        authors_str = "; ".join(
            a.get("name", "") for a in authors_list[:5]
        )
        if len(authors_list) > 5:
            authors_str += " et al."
        year = paper.get("year")
        venue = paper.get("venue") or "Unknown venue"
        abstract = paper.get("abstract") or ""
        external_ids = paper.get("externalIds", {})
        doi_val = external_ids.get("DOI")
        doi = f"https://doi.org/{doi_val}" if doi_val else ""
        if not doi:
            ss_id = paper.get("paperId", "")
            doi = f"https://www.semanticscholar.org/paper/{ss_id}" if ss_id else ""

        if not doi:
            continue  # Skip entries we cannot deduplicate

        entry = PaperEntry(
            title=title,
            authors=authors_str or "Unknown authors",
            year=year,
            venue=venue,
            doi_or_url=doi,
            abstract=abstract,
            source="Semantic Scholar",
        )
        entries.append(entry)

    logger.info("Semantic Scholar '%s': fetched %d entries", query, len(entries))
    return entries


# ---------------------------------------------------------------------------
# Web Scraper (crawl4ai)
# ---------------------------------------------------------------------------

async def scrape_iaabc_journal(client: httpx.AsyncClient) -> list[PaperEntry]:
    """Scrape IAABC Journal page for recent publications."""
    entries: list[PaperEntry] = []
    try:
        resp = await client.get(IAABC_JOURNAL_URL, timeout=30.0)
        resp.raise_for_status()
        html = resp.text
    except Exception as exc:
        logger.warning("IAABC Journal scrape failed: %s", exc)
        return entries

    # Parse article titles and links from IAABC journal page
    # Look for <a> tags containing article titles (heuristic parsing)
    article_pattern = re.compile(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>\s*([^<]{20,200})\s*</a>',
        re.IGNORECASE,
    )
    base_url = "https://iaabc.org"
    seen_hrefs: set[str] = set()

    for match in article_pattern.finditer(html):
        href, link_text = match.group(1), match.group(2).strip()
        # Filter: only article-looking links (contains "journal" or "article")
        if not any(kw in href.lower() for kw in ["/journal/", "/article/", "/publication"]):
            continue
        if href in seen_hrefs:
            continue
        seen_hrefs.add(href)

        full_url = href if href.startswith("http") else base_url + href
        entry = PaperEntry(
            title=link_text,
            authors="IAABC",
            year=datetime.now().year,  # Approximate — no date on listing
            venue="IAABC Journal",
            doi_or_url=full_url,
            abstract="",
            source="IAABC Journal scraper",
        )
        entries.append(entry)

        if len(entries) >= 5:
            break

    logger.info("IAABC Journal scrape: found %d entries", len(entries))
    return entries


async def scrape_avsab_statements(client: httpx.AsyncClient) -> list[PaperEntry]:
    """Scrape AVSAB position statements page."""
    entries: list[PaperEntry] = []
    try:
        resp = await client.get(AVSAB_URL, timeout=30.0)
        resp.raise_for_status()
        html = resp.text
    except Exception as exc:
        logger.warning("AVSAB scrape failed: %s", exc)
        return entries

    # Look for PDF links or article titles on the page
    pdf_pattern = re.compile(
        r'<a[^>]+href=["\']([^"\']+\.pdf)["\'][^>]*>([^<]+)</a>',
        re.IGNORECASE,
    )
    base_url = "https://avsab.org"

    for match in pdf_pattern.finditer(html):
        href, title = match.group(1), match.group(2).strip()
        if not title or len(title) < 10:
            continue
        full_url = href if href.startswith("http") else base_url + href

        entry = PaperEntry(
            title=f"AVSAB Position Statement: {title}",
            authors="American Veterinary Society of Animal Behavior (AVSAB)",
            year=datetime.now().year,
            venue="AVSAB",
            doi_or_url=full_url,
            abstract="AVSAB official position statement on animal behavior and training.",
            source="AVSAB scraper",
        )
        entries.append(entry)

    logger.info("AVSAB scrape: found %d entries", len(entries))
    return entries


# ---------------------------------------------------------------------------
# Knowledge Brain Writer
# ---------------------------------------------------------------------------

def append_to_knowledge_brain(
    brain_path: Path,
    new_entries: list[PaperEntry],
    dry_run: bool = False,
) -> int:
    """Append new entries to SECOND-KNOWLEDGE-BRAIN.md. Returns count appended."""
    if not new_entries:
        logger.info("No new entries to append.")
        return 0

    if not brain_path.exists():
        logger.error("SECOND-KNOWLEDGE-BRAIN.md not found at %s", brain_path)
        return 0

    text = brain_path.read_text(encoding="utf-8")

    # Find the Section 2 table — append before the Section 3 header
    section3_marker = "## Section 3:"
    insert_pos = text.find(section3_marker)
    if insert_pos == -1:
        # Fallback: append before the last section
        insert_pos = text.rfind("\n## Section")
    if insert_pos == -1:
        insert_pos = len(text)

    # Build new rows
    new_rows = "\n".join(entry.to_markdown_row() for entry in new_entries)
    insertion = f"\n{new_rows}\n"

    new_text = text[:insert_pos] + insertion + text[insert_pos:]

    # Update the Knowledge Update Log (Section 7)
    log_entry = (
        f"| {date.today().isoformat()} "
        f"| Multiple sources (PubMed, Semantic Scholar, IAABC, AVSAB) "
        f"| {len(new_entries)} papers "
        f"| (deduplication handled before append) "
        f"| knowledge_updater.py |"
    )
    log_section_marker = "## Section 7: Knowledge Update Log"
    log_pos = new_text.find(log_section_marker)
    if log_pos != -1:
        # Find the table header line and insert after it
        table_header_pos = new_text.find("| Date |", log_pos)
        if table_header_pos != -1:
            separator_pos = new_text.find("\n", table_header_pos)
            separator_end = new_text.find("\n", separator_pos + 1)
            new_text = (
                new_text[: separator_end + 1]
                + log_entry
                + "\n"
                + new_text[separator_end + 1 :]
            )

    if dry_run:
        logger.info("[DRY RUN] Would append %d entries. Preview:", len(new_entries))
        for entry in new_entries[:3]:
            logger.info("  - %s (%s) — score %.3f", entry.title[:60], entry.year, entry.combined_score)
        return len(new_entries)

    brain_path.write_text(new_text, encoding="utf-8")
    logger.info("Appended %d new entries to SECOND-KNOWLEDGE-BRAIN.md", len(new_entries))
    return len(new_entries)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

async def run_pipeline(dry_run: bool = False, max_results_per_term: int = MAX_RESULTS_PER_PUBMED_TERM) -> None:
    """Full knowledge update pipeline."""
    logger.info("=== Pet Behavior Training Path — Knowledge Updater ===")
    logger.info("Target: %s", KNOWLEDGE_BRAIN_PATH)
    logger.info("Dry run: %s", dry_run)

    current_year = datetime.now().year
    all_entries: list[PaperEntry] = []

    # Load existing hashes for deduplication
    existing_hashes = load_existing_hashes(KNOWLEDGE_BRAIN_PATH)

    async with httpx.AsyncClient(
        headers={"User-Agent": "PetBehaviorSkillBot/1.0 (research; skill_adv@example.com)"},
        follow_redirects=True,
    ) as client:
        # --- PubMed ---
        logger.info("Fetching from PubMed (%d search terms)...", len(PUBMED_SEARCH_TERMS))
        pubmed_tasks = [
            fetch_pubmed_papers(client, term, max_results_per_term)
            for term in PUBMED_SEARCH_TERMS
        ]
        pubmed_results = await asyncio.gather(*pubmed_tasks, return_exceptions=True)
        for result in pubmed_results:
            if isinstance(result, list):
                all_entries.extend(result)
            elif isinstance(result, Exception):
                logger.warning("PubMed task error: %s", result)

        # --- Semantic Scholar ---
        logger.info("Fetching from Semantic Scholar (%d queries)...", len(SEMANTIC_SCHOLAR_QUERIES))
        ss_tasks = [
            fetch_semantic_scholar_papers(client, query, MAX_RESULTS_SEMANTIC_SCHOLAR)
            for query in SEMANTIC_SCHOLAR_QUERIES
        ]
        ss_results = await asyncio.gather(*ss_tasks, return_exceptions=True)
        for result in ss_results:
            if isinstance(result, list):
                all_entries.extend(result)

        # --- IAABC Journal ---
        logger.info("Scraping IAABC Journal...")
        iaabc_entries = await scrape_iaabc_journal(client)
        all_entries.extend(iaabc_entries)

        # --- AVSAB ---
        logger.info("Scraping AVSAB position statements...")
        avsab_entries = await scrape_avsab_statements(client)
        all_entries.extend(avsab_entries)

    logger.info("Total raw entries fetched: %d", len(all_entries))

    # Score all entries
    for entry in all_entries:
        entry.compute_scores(current_year)

    # Filter by minimum score
    scored_entries = [e for e in all_entries if e.combined_score >= MIN_SCORE_TO_APPEND]
    logger.info("Entries passing minimum score threshold (%.2f): %d", MIN_SCORE_TO_APPEND, len(scored_entries))

    # Deduplicate against existing knowledge brain
    new_entries = [e for e in scored_entries if e.url_hash not in existing_hashes]
    logger.info("Entries after deduplication: %d", len(new_entries))

    # Deduplicate within this batch (by hash)
    seen_hashes_in_batch: set[str] = set()
    deduplicated_batch: list[PaperEntry] = []
    for entry in new_entries:
        if entry.url_hash not in seen_hashes_in_batch:
            seen_hashes_in_batch.add(entry.url_hash)
            deduplicated_batch.append(entry)

    # Sort by combined score (highest first)
    deduplicated_batch.sort(key=lambda e: e.combined_score, reverse=True)
    logger.info("Final deduplicated batch to append: %d entries", len(deduplicated_batch))

    # Append to knowledge brain
    appended_count = append_to_knowledge_brain(
        KNOWLEDGE_BRAIN_PATH,
        deduplicated_batch,
        dry_run=dry_run,
    )

    # Summary
    logger.info("=== Pipeline Complete ===")
    logger.info("Entries appended: %d", appended_count)
    logger.info("Entries skipped (duplicates/low score): %d", len(all_entries) - appended_count)
    if deduplicated_batch:
        top3 = deduplicated_batch[:3]
        logger.info("Top 3 new entries by score:")
        for entry in top3:
            logger.info(
                "  [%.3f] %s (%s) — %s",
                entry.combined_score,
                entry.title[:60],
                entry.year or "n/a",
                entry.source,
            )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md for Skill #231 (Pet Behavior Training Path)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing to disk",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=MAX_RESULTS_PER_PUBMED_TERM,
        help=f"Max results per PubMed search term (default: {MAX_RESULTS_PER_PUBMED_TERM})",
    )
    args = parser.parse_args()

    asyncio.run(run_pipeline(dry_run=args.dry_run, max_results_per_term=args.max_results))


if __name__ == "__main__":
    main()

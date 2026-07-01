# CLAUDE.md — Skill #231: Pet Behavior Analysis & Training Path

## Identity
- **Skill name:** pet-behavior-training-path
- **Tagline:** Evidence-based behavioral analysis and structured training roadmaps for dogs and cats with depression, hyperactivity, anxiety, or aggression
- **Current phase:** Phase 0 — Research & Skill Architecture
- **Source idea:** #231
- **Cluster:** lifestyle-personal

---

## Problem This Skill Solves

Millions of pet owners face behavioral challenges — separation anxiety, hyperactivity, feline depression, destructive behavior, or fear aggression — without any structured, evidence-based guidance. Generic internet advice is fragmented, anecdotal, and often contradicts veterinary behavioral science. Worse, many owners unknowingly apply punishment-based techniques that deepen fear, anxiety, and behavioral dysfunction. This skill bridges the gap between academic animal behavior science and practical daily training, delivering a personalized, LIMA-compliant training path grounded in applied animal behavior science, IAABC standards, and the latest veterinary behavioral research. It also enforces a critical safety gate: any behavior with a plausible medical etiology triggers a mandatory veterinary referral before training begins.

---

## Harness Flow Summary

```
/pet-behavior-training-path invoked
  Step 1 → sub-profile-intake        : Collect species, breed, age, sex, medical history, environment, symptoms
  Step 2 → sub-behavior-assessment   : Classify using IAABC categories + ABC analysis + functional diagnosis
  Step 3 → [VET REFERRAL GATE]       : If medical trigger suspected → halt + vet referral recommendation
  Step 4 → sub-framework-selector    : Select LIMA-compliant training framework for the specific issue
  Step 5 → sub-training-path-designer: Build step-by-step protocol (desensitization, CC, shaping, management)
  Step 6 → sub-progress-tracker      : Output weekly scoring system + regression flags + follow-up checkpoints
  Step 7 → main skill synthesis      : Compile complete training plan document with daily/weekly schedule
```

---

## Sub-Skills

| File | Description |
|------|-------------|
| `skills/sub-profile-intake.md` | Gather species, breed, age, sex, neuter status, medical history, living environment, and detailed behavioral symptom profile (onset, frequency, severity, triggers) |
| `skills/sub-behavior-assessment.md` | Classify behavior problems using IAABC diagnostic categories, apply ABC (Antecedent-Behavior-Consequence) analysis, produce functional diagnosis |
| `skills/sub-framework-selector.md` | Select the appropriate LIMA-compliant training framework and specific techniques based on functional diagnosis |
| `skills/sub-training-path-designer.md` | Build a complete step-by-step training protocol with session schedules, technique guides, and management strategies |
| `skills/sub-progress-tracker.md` | Score behavioral improvements weekly, detect regression, suggest protocol adjustments, flag vet referral triggers |

---

## Tools Required

- **WebSearch** — find current veterinary behavior research, IAABC publications, AVSAB position statements
- **WebFetch** — retrieve full-text research articles and behavioral guidelines
- **Read** — access SECOND-KNOWLEDGE-BRAIN.md for offline fallback
- **Write** — produce the final training plan document

---

## Knowledge Sources

| Source | URL | Type |
|--------|-----|------|
| Journal of Veterinary Behavior | https://www.journals.elsevier.com/journal-of-veterinary-behavior | Peer-reviewed journal |
| Applied Animal Behaviour Science | https://www.journals.elsevier.com/applied-animal-behaviour-science | Peer-reviewed journal |
| IAABC Journal | https://iaabc.org/journal/ | Professional body journal |
| AVSAB Position Statements | https://avsab.org/resources/position-statements/ | Professional standards |
| PubMed (veterinary behavior) | https://pubmed.ncbi.nlm.nih.gov/?term=animal+behavior+training | Database |
| Fear Free Pets | https://fearfreepets.com/resources/ | Clinical resource |
| Semantic Scholar | https://www.semanticscholar.org/ | Research aggregator |

---

## Supporting Tools

| File | Purpose |
|------|---------|
| `tools/knowledge_updater.py` | crawl4ai pipeline: fetches latest papers from PubMed, Semantic Scholar, IAABC, and AVSAB; scores by recency + domain relevance; appends to SECOND-KNOWLEDGE-BRAIN.md; deduplicates by DOI/URL hash |

---

## Active Development Tasks

- [ ] Phase 0: Finalize skill architecture and sub-skill interfaces
- [ ] Phase 1: Implement sub-profile-intake with species-specific intake forms (dog vs. cat)
- [ ] Phase 1: Implement sub-behavior-assessment with ABC analysis engine
- [ ] Phase 1: Implement sub-framework-selector (LIMA hierarchy enforcement)
- [ ] Phase 2: Implement sub-training-path-designer with protocol library
- [ ] Phase 2: Implement sub-progress-tracker with weekly scoring rubric
- [ ] Phase 2: Build main harness with vet referral gate logic
- [ ] Phase 3: Implement knowledge_updater.py with crawl4ai pipeline
- [ ] Phase 4: Write and execute 5+ test scenarios
- [ ] Phase 5: Wire shared cluster sub-skills (profile-intake, improvement-roadmap)

---

## References

- `PROJECT-detail.md` — Full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Phase-by-phase build roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — Domain knowledge base (self-updating)

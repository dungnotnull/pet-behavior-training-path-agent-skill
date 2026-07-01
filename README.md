# Pet Behavior Analysis & Training Path

<div align="center">

**Evidence-based behavioral analysis and structured training roadmaps for dogs and cats**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![LIMA Compliant](https://img.shields.io/badge/LIMA-Compliant-blue.svg)]()
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-purple.svg)]()

*A Claude Code Skill that bridges the gap between academic animal behavior science and practical daily training*

</div>

---

## Overview

Millions of pet owners face behavioral challenges — separation anxiety, hyperactivity, feline depression, destructive behavior, or fear aggression — without any structured, evidence-based guidance. Generic internet advice is fragmented, anecdotal, and often contradicts veterinary behavioral science.

**Pet Behavior Analysis & Training Path** is a comprehensive harness-based skill that delivers personalized, LIMA-compliant training roadmaps grounded in:

- **Applied Animal Behavior Science** — peer-reviewed research from Journal of Veterinary Behavior, Applied Animal Behaviour Science
- **IAABC Standards** — International Association of Animal Behavior Consultants diagnostic frameworks
- **AVSAB Position Statements** — American Veterinary Society of Animal Behavior guidelines
- **LIMA Hierarchy** — Least Intrusive, Minimally Aversive ethical framework

### What Makes This Different

Unlike generic advice, this skill:

1. **Screens for medical causes first** — Mandatory veterinary referral gate before any training begins
2. **Applies functional behavioral assessment** — ABC analysis (Antecedent-Behavior-Consequence) for every symptom
3. **Selects evidence-based techniques** — Every recommendation cites peer-reviewed research
4. **Builds structured 8-week protocols** — Session-by-session plans with success criteria
5. **Tracks objective progress** — Weekly scoring system with regression detection

---

## Features

### Comprehensive Behavioral Assessment

- **Species-specific intake** (dog vs. cat pathways)
- **IAABC diagnostic classification** — Fear/anxiety, compulsive disorders, cognitive dysfunction, aggression, depression, hyperactivity
- **ABC functional analysis** — Identifies what maintains each behavior
- **Medical differential screening** — Flags symptoms requiring veterinary evaluation

### LIMA-Compliant Training Framework

All training plans follow the **Least Intrusive, Minimally Aversive** hierarchy:

1. ✅ Health, nutritional, and physical factors (addressed first)
2. ✅ Antecedent arrangement (environment modification)
3. ✅ Positive reinforcement (primary strategy)
4. ✅ Differential reinforcement of alternative/incompatible behaviors
5. ⚠️ Extinction (used carefully, never for fear-based behaviors)
6. ⚠️ Negative punishment (withhold desired stimulus)
7. ❌ Negative reinforcement (professional supervision only)
8. ❌ Positive punishment (never recommended as first-line intervention)

### Built-in Quality Gates

- **Medical Gate** — Automatic halt for senior animals, sudden onset changes, or medical red flags
- **LIMA Gate** — Enforces least intrusive effective intervention
- **Evidence Gate** — Requires research citations for all technique recommendations
- **Safety Gate** — Triggers professional referral for bite history or aggression escalation

### Progress Tracking System

- **Baseline scoring** (1–10 severity scale with behavioral anchors)
- **Primary metrics** — Observable, countable measures per symptom
- **Weekly tracking sheets** — Creates objective trend lines
- **Decision rules** — Advancement, retreat, suspension, escalation criteria
- **Regression detection** — Automatic protocol adjustment triggers

---

## How It Works

### The 7-Stage Harness Flow

```
User invokes: /pet-behavior-training-path
    │
    ▼
Stage 1: Pet Profile Intake
    → Species, breed, age, medical history, environment, symptoms
    → Outputs: pet_profile, symptom_list
    │
    ▼
Stage 2: Behavioral Assessment
    → ABC analysis, IAABC classification, medical differentials
    → Outputs: functional_diagnosis, ABC_map, medical_flag
    │
    ▼
Stage 3: Vet Referral Gate (MANDATORY)
    → IF medical_flag OR senior OR sudden onset
    → → HALT + Vet referral + Recommended diagnostics
    → ELSE continue to Stage 4
    │
    ▼
Stage 4: Framework Selection
    → LIMA hierarchy mapping, technique library selection
    → Outputs: selected_framework, technique_list, citations
    │
    ▼
Stage 5: Training Path Design
    → 8-week protocol, session schedules, management strategies
    → Outputs: training_plan, management_plan, equipment_list
    │
    ▼
Stage 6: Progress Tracker
    → Baseline scores, weekly sheets, decision rules
    → Outputs: progress_rubric, regression_flags, escalation_triggers
    │
    ▼
Stage 7: Synthesis
    → Complete training plan document (9 sections)
    → Daily/weekly schedules, success metrics, safety notes
```

### Output Document Structure

Every completed training plan includes:

1. **Pet Profile Summary** — All relevant intake data
2. **Behavioral Assessment & Diagnosis** — Functional diagnosis with ABC analysis
3. **Medical & Safety Notes** — Vet gate results, disclaimers, referrals
4. **Training Philosophy & Framework** — LIMA rationale with research citations
5. **8-Week Training Plan** — Session-by-session protocol
6. **Daily Management Strategies** — Concurrent prevention measures
7. **Progress Tracker** — Baseline scores, weekly rubric, decision rules
8. **When to Seek Professional Help** — Clear escalation criteria
9. **Sources & Further Reading** — Cited research and resources

---

## Use Cases

| User Situation | Skill Response |
|----------------|---------------|
| "My dog stopped playing after we moved" | Screens for canine depression, checks for medical causes, creates behavioral activation protocol |
| "My Labrador puppy won't stop jumping and biting" | Performs hyperactivity assessment, selects impulse control training, provides management strategies |
| "My cat has been hiding since we got a second cat" | Assesses inter-cat conflict and anxiety, checks for pain/illness, designs environmental management + desensitization plan |
| "My rescue dog growls when I approach his food bowl" | Classifies as resource guarding, applies counter-conditioning protocol, never uses punishment |
| "My senior dog seems sad and sleeps all day" | Screens for canine cognitive dysfunction, recommends vet visit, designs enrichment protocol after clearance |

---

## Installation

### As a Claude Code Skill

1. Clone this repository to your skills directory:
```bash
git clone https://github.com/dungnotnull/pet-behavior-training-path-agent-skill.git
```

2. The skill files are organized as follows:
```
pet-behavior-training-path/
├── skills/
│   ├── main.md                    # Main harness skill
│   ├── sub-profile-intake.md      # Intake sub-skill
│   ├── sub-behavior-assessment.md # Assessment sub-skill
│   ├── sub-framework-selector.md  # Framework selection sub-skill
│   ├── sub-training-path-designer.md # Training design sub-skill
│   └── sub-progress-tracker.md   # Progress tracking sub-skill
├── tools/
│   └── knowledge_updater.py       # Auto-update pipeline
├── SECOND-KNOWLEDGE-BRAIN.md       # Domain knowledge base
└── CLAUDE.md                       # Skill configuration
```

3. Invoke the skill in Claude Code:
```
/pet-behavior-training-path
```

### Knowledge Base Auto-Updates (Optional)

The skill includes an auto-updating knowledge base pipeline:

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the knowledge updater:
```bash
python tools/knowledge_updater.py
```

3. (Optional) Set up weekly cron job:
```bash
# Run every Sunday at 2 AM
0 2 * * 0 cd /path/to/pet-behavior-training-path && python tools/knowledge_updater.py
```

---

## Project Structure

```
pet-behavior-training-path/
├── README.md                          # This file
├── CLAUDE.md                          # Skill identity and configuration
├── PROJECT-detail.md                  # Full technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md # Development tracking
├── SECOND-KNOWLEDGE-BRAIN.md          # Domain knowledge base (auto-updates)
├── requirements.txt                    # Python dependencies
│
├── skills/                            # Skill implementations
│   ├── main.md                        # Main harness (7-stage orchestrator)
│   ├── sub-profile-intake.md          # Species-specific intake
│   ├── sub-behavior-assessment.md     # ABC analysis + IAABC classification
│   ├── sub-framework-selector.md      # LIMA hierarchy + technique selection
│   ├── sub-training-path-designer.md   # 8-week protocol builder
│   └── sub-progress-tracker.md        # Baseline scoring + decision rules
│
├── tools/                             # Supporting tools
│   └── knowledge_updater.py           # PubMed/Semantic Scholar fetcher
│
├── tests/                             # Test validation
│   ├── test-scenarios.md              # 6 comprehensive scenarios
│   └── test-execution-log.md          # Validation results (all PASS)
│
└── docs/                              # Additional documentation
    └── cluster-integration.md         # Cross-skill wiring documentation
```

---

## Testing & Validation

All 6 test scenarios pass validation:

| Scenario | Vet Gate | Framework | LIMA Compliant | Result |
|----------|-----------|-----------|----------------|--------|
| Separation Anxiety (3yr Border Collie) | No | SD+CC + GDep | Yes | PASS |
| Hyperactive Puppy (6mo Lab) | No | Impulse Control + Enrichment | Yes | PASS |
| Depressed Senior Cat (12yr) | Yes (fires) | N/A (halted) | N/A | PASS |
| Fear Aggression Rescue (4yr Pit mix) | Yes (partial) | DS+CC (post-clearance) | Yes | PASS |
| Multi-Cat Conflict (2 cats, new baby) | Yes (partial) | Management + Reintroduction | Yes | PASS |
| Canine Cognitive Dysfunction (13yr) | Yes (hard) | N/A (halted) | N/A | PASS |

See [tests/test-execution-log.md](tests/test-execution-log.md) for detailed validation results.

---

## Scientific Foundations

### Core Frameworks

1. **LIMA Hierarchy** (Least Intrusive, Minimally Aversive)
   - Developed by Steve White
   - Endorsed by IAABC, APDT, CCPDT
   - Required ethical framework for professional animal trainers

2. **ABC Functional Assessment** (Antecedent-Behavior-Consequence)
   - Three-term contingency for behavioral analysis
   - Identifies the function maintaining each behavior
   - Determines whether behavior is escape/avoidance (fear) or positively reinforced

3. **IAABC Diagnostic Framework**
   - Fear/Anxiety Disorders
   - Compulsive/Repetitive Disorders
   - Inter-Animal and Human-Directed Aggression
   - Depression/Anhedonia
   - Hyperactivity/Hyperkinesis
   - Cognitive Dysfunction Syndrome

4. **Fear Free Principles**
   - Reduces stress, fear, and anxiety in clinical and home environments
   - Prioritizes emotional state during training
   - Optimizes environment and communication

### Research Sources

The skill draws on peer-reviewed research from:

- **Journal of Veterinary Behavior** — Elsevier
- **Applied Animal Behaviour Science** — Elsevier
- **IAABC Journal** — International Association of Animal Behavior Consultants
- **AVSAB Position Statements** — American Veterinary Society of Animal Behavior
- **PubMed** — U.S. National Library of Medicine
- **Semantic Scholar** — AI-powered research aggregator
- **Fear Free Pets** — Clinical resources and protocols

### Knowledge Base

The `SECOND-KNOWLEDGE-BRAIN.md` file contains:
- 14+ seed papers with full citations
- Core learning theory foundations (classical/operant conditioning, SD, CC, shaping)
- LIMA hierarchy definition
- Medical differentials for all major presentations
- Species-specific behavioral needs (canine/feline ethograms)
- Analytical frameworks (ABC, IAABC, Fear Free Five-Domain)
- State-of-the-art methods (Fear Free, teletherapy, enrichment science, behavioral pharmacology)
- Authoritative data sources

The knowledge base auto-updates weekly via `tools/knowledge_updater.py`.

---

## Safety & Ethics

### Mandatory Veterinary Referral Gate

The skill **automatically halts** and recommends veterinary consultation when:

- **Senior animals** (dogs >7 years, cats >10 years) with new behavioral symptoms
- **Sudden onset** changes (within 48 hours with no behavioral trigger)
- **Bite history** with injury
- **Elimination changes** (frequency, blood, outside litter box)
- **Complete refusal to eat** for >24 hours
- **Known medical conditions** with behavioral changes
- **Neurological symptoms** (disorientation, night wandering, circling)

### LIMA Compliance Enforcement

The skill **never recommends** as first-line interventions:
- Shock collars (e-collars)
- Prong collars
- Choke chains for training
- Spray bottles
- Rattle cans / shake cans
- Alpha rolls
- Flooding (forced exposure)
- Positive punishment

All primary recommendations use:
- Positive reinforcement
- Management and prevention
- Systematic desensitization
- Counter-conditioning
- Environmental enrichment
- Behavioral activation

### Quality of Life Considerations

For geriatric animals with cognitive dysfunction, the skill:
- References quality of life scales (HHHHHMM scale by Dr. Alice Villalobos)
- Discusses palliative care options
- Acknowledges the grief-adjacent nature of cognitive decline
- Provides compassionate guidance for end-of-life decision support

---

## Contributing

This skill is production-ready and open for contributions. Areas for enhancement:

1. **Additional protocol modules** (e.g., noise phobias, car travel, veterinary visit prep)
2. **Species expansion** (e.g., rabbits, birds, horses)
3. **Language localization** (translations for non-English speakers)
4. **Knowledge base expansion** (additional research sources, regional guidelines)
5. **Integration with veterinary EMR systems** (with appropriate permissions)

Contributions should:
- Maintain LIMA compliance
- Cite peer-reviewed research for new techniques
- Pass all 6 test scenarios
- Include documentation updates
- Follow the existing code structure and style

---

## License

This project is dual-licensed:

- **Code:** MIT License — see [LICENSE](LICENSE) for details
- **Documentation & Content:** CC-BY-SA 4.0 — Creative Commons Attribution-ShareAlike 4.0

---

## Acknowledgments

### Scientific Foundations

- **IAABC** (International Association of Animal Behavior Consultants) — Diagnostic frameworks and standards of practice
- **AVSAB** (American Veterinary Society of Animal Behavior) — Position statements on humane training
- **Fear Free Pets** — Dr. Marty Becker's stress-reduction methodology
- **Karen Pryor Academy** — Clicker training foundations
- **Dr. Alice Villalobos** — Quality of life scales (HHHHHMM)
- **Jean Donaldson** — Resource guarding protocols (Mine!)
- **Dr. Marc Bekoff** — Animal emotion and enrichment research

### Research Sources

Peer-reviewed journals and databases that make this work possible:
- Journal of Veterinary Behavior (Elsevier)
- Applied Animal Behaviour Science (Elsevier)
- PubMed (U.S. National Library of Medicine)
- Semantic Scholar (Allen Institute for AI)

---

## Citation

If you use this skill in research or professional work, please cite:

```
Pet Behavior Analysis & Training Path Skill #231. (2026).
Evidence-based behavioral analysis and LIMA-compliant training roadmaps
for dogs and cats. GitHub Repository: https://github.com/dungnotnull/pet-behavior-training-path-agent-skill
```

---

## Contact & Support

- **Issues:** Report bugs or feature requests via GitHub Issues
- **Discussions:** Use GitHub Discussions for questions and community support
- **Research Inquiries:** Consult the SECOND-KNOWLEDGE-BRAIN.md for source citations

---

## Disclaimer

This skill provides educational guidance based on current veterinary behavioral science. It is not a substitute for:

- Professional veterinary care
- In-person behavioral consultation
- Certified Applied Animal Behaviorist (CAAB) evaluation
- Diplomate of the American College of Veterinary Behaviorists (DACVB) assessment

For emergencies, bite incidents, or escalating aggression, contact a veterinarian or veterinary behaviorist immediately.

---

<div align="center">

**Built with science integrity. Guided by LIMA ethics. Dedicated to animal welfare.**

[⬆ Back to Top](#pet-behavior-analysis--training-path)

</div>

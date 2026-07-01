# PROJECT-detail.md — Skill #231: Pet Behavior Analysis & Training Path

## Executive Summary

Skill #231 (`pet-behavior-training-path`) is a harness-based Claude skill that guides pet owners, amateur trainers, and rescue shelter volunteers through a rigorous, evidence-based analysis of dog and cat behavioral disorders — including depression, hyperactivity, anxiety, and aggression — and delivers a fully customized, LIMA-compliant training path. The skill grounds every recommendation in Applied Animal Behavior Science, IAABC diagnostic standards, and AVSAB position statements, while enforcing a mandatory veterinary referral gate whenever behavior may have a medical etiology.

---

## Problem Statement

### Domain Context
Behavioral disorders are among the leading causes of pet abandonment and euthanasia worldwide. Studies estimate that 15–20% of dogs and 25–30% of cats exhibit clinically significant behavioral problems at some point in their lives (Bamberger & Houpt, 2006). The two most commonly mishandled presentations are:

1. **Canine/Feline Depression** — manifesting as lethargy, anhedonia (loss of interest in play, food, social interaction), withdrawal, and reduced activity. Triggers include bereavement (loss of companion animal or human), environmental change, chronic pain, and hypothyroidism.

2. **Hyperactivity / ADHD-analogous presentations** — manifesting as inability to settle, excessive barking/vocalization, destructive behavior, persistent arousal despite exercise, and impulsivity. This is frequently misdiagnosed as "bad behavior" and addressed with punishment, worsening the underlying anxiety.

### Why Existing Resources Fail
- Most online training advice is anecdotal, breed-generalized, and punishment-tolerant
- LIMA hierarchy is mentioned but rarely applied systematically
- Medical causes of behavioral change are almost never screened before training begins
- No structured progress measurement system exists for home trainers
- Research from journals like *Journal of Veterinary Behavior* and *Applied Animal Behaviour Science* is inaccessible to lay pet owners

### What This Skill Provides
A structured, evidence-based workflow that: (a) profiles the individual animal, (b) performs a functional behavioral assessment, (c) gates on medical etiology before any training begins, (d) selects appropriate science-backed training techniques, (e) produces a detailed daily/weekly training schedule, and (f) tracks progress with clear success criteria and regression flags.

---

## Target Users & Use Cases

### Primary Users
- **Pet owners** with dogs or cats exhibiting worrying behavioral changes (sudden aggression, withdrawal, destructiveness, hyperactivity)
- **Amateur trainers** seeking a framework more rigorous than YouTube videos
- **Rescue shelter volunteers** managing behaviorally complex intake animals

### Use Case Trigger Examples

| User Says | Skill Does |
|-----------|------------|
| "My dog stopped playing after we moved" | Screens for feline/canine depression, checks for medical causes, creates re-engagement protocol |
| "My Labrador puppy won't stop jumping and biting" | Performs hyperactivity assessment, selects impulse-control training path, provides management strategies |
| "My cat has been hiding since we got a second cat" | Assesses inter-cat conflict and anxiety, checks for pain/illness, designs environmental management + desensitization plan |
| "My rescue dog growls when I approach his food bowl" | Classifies as resource guarding, applies functional assessment, builds LIMA-compliant counter-conditioning protocol |
| "My senior dog seems sad and sleeps all day" | Screens for canine cognitive dysfunction and hypothyroidism, recommends vet visit, designs enrichment protocol |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    /pet-behavior-training-path  (main harness)               │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 1: INTAKE    │  ← sub-profile-intake.md
│  Species, breed,    │     Outputs: pet_profile{}, symptom_list[]
│  age, medical hx,   │
│  environment        │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 2: ASSESS    │  ← sub-behavior-assessment.md
│  IAABC categories,  │     Outputs: functional_diagnosis, severity_score,
│  ABC analysis,      │             ABC_map{}, medical_flag (bool)
│  functional diag.   │
└─────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Stage 3: VET REFERRAL GATE          │
│  IF medical_flag == TRUE             │
│  → Halt training path generation     │
│  → Output: vet referral letter +     │
│    list of recommended diagnostics   │
│  ELSE → continue to Stage 4          │
└──────────────────────────────────────┘
         │ (only if no medical flag)
         ▼
┌─────────────────────┐
│  Stage 4: FRAMEWORK │  ← sub-framework-selector.md
│  LIMA hierarchy,    │     Outputs: selected_framework, technique_list[]
│  technique library, │
│  approach rationale │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 5: TRAINING  │  ← sub-training-path-designer.md
│  PATH DESIGN        │     Outputs: session_schedule{}, protocol_steps[],
│  Protocol, schedule,│             management_plan, enrichment_plan
│  management, tools  │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 6: TRACKING  │  ← sub-progress-tracker.md
│  Weekly scoring,    │     Outputs: progress_rubric, regression_flags[],
│  regression check,  │             vet_escalation_triggers[]
│  adjustments        │
└─────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  Stage 7: SYNTHESIS  (main harness)                                          │
│  Complete Training Plan document with daily/weekly schedule, rationale,      │
│  success metrics, progress tracker, and safety notes                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### Sub-Skill 1: `sub-profile-intake`
- **Purpose:** Systematically gather all data needed for behavioral assessment
- **Inputs:** User's natural-language description of the pet and problem
- **Outputs:** Structured `pet_profile` object + `symptom_list` with onset, frequency, severity, triggers
- **Tools Used:** Conversational prompting (no external tools required); Write for profile summary
- **Quality Gate:** Profile must include: species, breed, age, sex, neuter status, medical history, current medications, living environment (indoor/outdoor, size, other pets, children), daily routine, exercise level, diet, and all behavioral symptoms with temporal context

### Sub-Skill 2: `sub-behavior-assessment`
- **Purpose:** Apply scientific behavioral analysis to the intake profile
- **Inputs:** `pet_profile`, `symptom_list`
- **Outputs:** `functional_diagnosis` (fear/anxiety, conflict/frustration, cognitive/medical, insufficient enrichment, learned behavior), `severity_score` (1–10), `ABC_map`, `medical_flag`
- **Tools Used:** WebSearch (IAABC diagnostic criteria, recent behavioral research), Read (SECOND-KNOWLEDGE-BRAIN.md fallback)
- **Quality Gate:** Must apply ABC analysis to each reported symptom; must check against medical differential list before setting `medical_flag = false`

### Sub-Skill 3: `sub-framework-selector` (shared with cluster)
- **Purpose:** Select the appropriate LIMA-compliant training approach
- **Inputs:** `functional_diagnosis`, `severity_score`, `pet_profile`
- **Outputs:** `selected_framework` with rationale, ordered `technique_list`, citation to supporting research
- **Tools Used:** WebSearch (AVSAB position statements, IAABC standards), Read (SECOND-KNOWLEDGE-BRAIN.md)
- **Quality Gate:** Selected framework must be at Least Intrusive level possible; any aversive technique must be explicitly justified and ranked last; cite minimum one peer-reviewed source

### Sub-Skill 4: `sub-training-path-designer`
- **Purpose:** Build the complete, actionable training protocol
- **Inputs:** `selected_framework`, `technique_list`, `pet_profile`, `ABC_map`
- **Outputs:** Session-by-session training plan (Week 1–8), management strategies (prevent rehearsal of unwanted behavior), enrichment plan, equipment list, owner skills checklist
- **Tools Used:** WebFetch (specific technique guides from Fear Free, IAABC), Write (training plan document)
- **Quality Gate:** Plan must specify: session duration, frequency, success criteria per session, failure criteria (triggers protocol retreat), management strategies that run parallel to active training

### Sub-Skill 5: `sub-progress-tracker`
- **Purpose:** Provide ongoing monitoring and adaptive management
- **Inputs:** `training_plan`, behavioral baseline from intake assessment
- **Outputs:** Weekly behavior scoring rubric (1–10 scale per symptom), regression detection rules, protocol adjustment decision tree, vet escalation trigger list
- **Tools Used:** Write (progress tracking template)
- **Quality Gate:** Must include explicit criteria for: (a) declaring success, (b) pausing protocol for adjustment, (c) escalating to veterinary behaviorist, (d) making emergency vet referral

---

## E2E Execution Flow

```
1. User invokes: /pet-behavior-training-path

2. Main harness loads, announces role and process to user

3. Invoke sub-profile-intake:
   - Ask species (dog/cat)
   - Ask breed, age, sex, neuter status
   - Ask: has a vet examined this animal recently? Any diagnoses?
   - Ask about medications
   - Ask living environment (home size, other pets, children, yard access)
   - Ask daily routine (feeding, exercise, alone time)
   - Ask: describe the behavioral problem in detail (what, when, how often, how severe, what triggers it, what makes it better/worse)
   - Ask: when did this behavior start? Was there a life event around that time?
   - Summarize and confirm pet_profile with user

4. Invoke sub-behavior-assessment:
   - Map each symptom to ABC model (Antecedent → Behavior → Consequence)
   - Check symptom pattern against IAABC diagnostic categories
   - Check medical differential list:
     * Depression/lethargy → rule out: hypothyroidism, Addison's disease, chronic pain, CDS (cognitive dysfunction), anemia
     * Hyperactivity/arousal → rule out: hyperthyroidism (cats), pain (irritability), neurological issues, dietary factors
     * Sudden behavior change → always flag medical review
   - Assign functional_diagnosis and severity_score
   - Set medical_flag

5. VET REFERRAL GATE:
   IF medical_flag == TRUE OR onset was sudden OR animal is senior (>7 yrs dogs, >10 yrs cats):
     → Output vet referral recommendation letter
     → List recommended diagnostics (bloodwork, thyroid panel, urinalysis, neurological exam)
     → Offer to generate training plan for AFTER medical clearance
     → STOP main flow
   ELSE:
     → Proceed to Step 6

6. Invoke sub-framework-selector:
   - Map functional_diagnosis to LIMA hierarchy level
   - Select primary approach (e.g., systematic desensitization + counter-conditioning for fear/anxiety)
   - Select management strategies
   - Cite research basis (WebSearch if available, SECOND-KNOWLEDGE-BRAIN.md fallback)

7. Invoke sub-training-path-designer:
   - Build 8-week protocol with weekly phases
   - Week 1–2: Management + foundation skills + baseline measurement
   - Week 3–4: Begin primary intervention (DS/CC or impulse control or enrichment)
   - Week 5–6: Generalization (different environments, distractions)
   - Week 7–8: Maintenance + proofing + handover to owner independence
   - Specify: tools needed, session length (max 5 min for anxious animals), daily repetitions
   - Include parallel management plan (prevents rehearsal of problem behavior)

8. Invoke sub-progress-tracker:
   - Create weekly scoring sheet (score each symptom 1–10 at intake, re-score weekly)
   - Define regression threshold: if score worsens by >2 points → protocol adjustment
   - Define escalation trigger: if no improvement after 4 weeks → veterinary behaviorist referral
   - Define emergency flag: if aggression escalates or animal is not eating → immediate vet

9. Synthesize final deliverable:
   - Section 1: Pet Profile Summary
   - Section 2: Behavioral Assessment & Diagnosis
   - Section 3: Training Philosophy & Framework Rationale
   - Section 4: 8-Week Training Plan (session-by-session)
   - Section 5: Daily Management Strategies
   - Section 6: Weekly Progress Tracker (scoring rubric)
   - Section 7: When to Seek Professional Help
   - Section 8: Sources & Further Reading
```

---

## SECOND-KNOWLEDGE-BRAIN Integration

The skill draws on `SECOND-KNOWLEDGE-BRAIN.md` in two contexts:
1. **Offline fallback:** When WebSearch/WebFetch are unavailable, all framework selection and technique guidance is drawn from the knowledge base
2. **Citation support:** The knowledge base pre-loads the most important papers so sub-skills can cite without a live search

The `tools/knowledge_updater.py` script updates the knowledge base weekly using crawl4ai:
- Searches PubMed for: "canine behavior training", "feline anxiety treatment", "positive reinforcement dog", "LIMA training", "separation anxiety dog", "canine cognitive dysfunction"
- Fetches IAABC and AVSAB publication pages
- Parses title, authors, year, DOI, abstract
- Scores: recency_score (1/years_since_publication) + relevance_score (keyword match count)
- Appends new entries to SECOND-KNOWLEDGE-BRAIN.md
- Deduplicates by DOI hash (MD5)

---

## Quality Gates

| Gate | Trigger | Action |
|------|---------|--------|
| Medical history gate | Medical_flag = TRUE, sudden onset, senior animal | Halt training — output vet referral |
| LIMA compliance gate | Any aversive technique proposed | Require explicit justification, rank as last resort |
| Profile completeness gate | Missing key intake fields | Re-prompt user for missing information |
| Evidence gate | Framework recommendation lacks citation | Search for supporting research before proceeding |
| Progress stagnation gate | No improvement after 4 weeks | Recommend veterinary behaviorist consultation |
| Aggression escalation gate | User reports worsening biting/growling | Immediate veterinary/CAAB consultation required |
| Safety gate (human/animal) | Bite history or injury | Output safety protocol + mandatory professional referral |

---

## Test Scenarios (5+)

See `tests/test-scenarios.md` for full details.

1. **Dog with separation anxiety** — 3yr old Border Collie, anxious when left alone, destructive, vocalization
2. **Hyperactive Labrador puppy** — 6mo male intact Lab, cannot settle, jumps, mouthes, won't focus
3. **Depressed senior cat** — 12yr old female DSH, stopped playing, eating less, hiding since owner returned from 2-week trip
4. **Rescue dog with fear aggression** — 4yr old pit bull mix, unknown history, growls/snaps at strangers
5. **Multi-pet household conflict** — Two 3yr old male cats, previously bonded, now fighting after new baby arrived
6. **Canine cognitive dysfunction** — 13yr old mixed breed, night wandering, disorientation, house soiling (medical gate test case)

---

## Key Design Decisions

1. **LIMA hierarchy as non-negotiable constraint:** The skill never recommends punishment, startle/aversive devices, or flooding as primary interventions. Aversives are listed only under "if all else fails" with explicit safety caveats and professional supervision requirements.

2. **Vet referral gate is mandatory, not optional:** A medical cause for behavioral change must be explicitly ruled out before any training protocol begins. The gate is automatic for: sudden onset, senior animals, and any symptom on the medical differential list.

3. **Species-specific pathways:** Cats and dogs have fundamentally different social structures, stress responses, and learning styles. The intake and assessment sub-skills branch explicitly at species level.

4. **No "one-size-fits-all" protocols:** Training plans are built from the functional_diagnosis outward — a fear-based dog and a frustration-based dog with the same "aggression" presentation receive completely different protocols.

5. **8-week structured timeline with explicit exit criteria:** Rather than vague "do this until better" advice, every protocol specifies per-session success criteria, so owners know when to advance, when to retreat, and when to seek help.

6. **Owner skill-building is part of the plan:** Many training failures are owner failures — timing, criteria-setting, consistency. The training path includes owner education milestones alongside pet behavior milestones.

7. **Progress tracker enables data-driven adjustment:** Weekly numerical scores create a trend line. Owners can see improvement that might not be obvious day-to-day, and regression is caught early before it becomes entrenched.

8. **Fear Free and low-stress handling principles are embedded:** All protocols prioritize the animal's emotional state during training. Sessions are capped at 5 minutes for anxious animals. All equipment recommendations exclude aversive collars.

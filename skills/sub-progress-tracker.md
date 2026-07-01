---
name: pet-behavior-training-path/sub-progress-tracker
description: Score behavioral improvements weekly, detect regression trends, suggest protocol adjustments, and flag vet referral triggers based on objective behavioral data
---

## Role & Persona

You are building the measurement and monitoring system for this animal's behavioral training program. A training plan without objective measurement is just intention. Your job is to give the owner a simple, reliable way to see whether the plan is working — and to know exactly what to do when it is not.

---

## Workflow

### Step 1: Establish Baseline Scores

Using the `symptom_list` from sub-profile-intake, assign a baseline score (1–10) to each symptom at intake, before training begins.

**Scoring anchors (severity scale):**

| Score | Behavioral Description |
|-------|----------------------|
| 1–2 | Minimal impact. Behavior present but barely noticeable; does not affect daily life or relationship |
| 3–4 | Mild. Behavior is noticeable and occasionally inconvenient but does not cause significant distress |
| 5–6 | Moderate. Behavior is frequent, causes owner stress, and impacts the animal's quality of life |
| 7–8 | Severe. Behavior is daily, significantly limits quality of life for animal and/or owner |
| 9–10 | Critical. Behavior poses a safety risk, indicates significant suffering, or is incompatible with continued ownership without professional intervention |

**Baseline template:**
```
BEHAVIORAL BASELINE — [Pet Name] — [Date: YYYY-MM-DD]

Symptom 1: [description]
  Baseline score: [X/10]
  Behavioral evidence for score: [what specific behaviors justify this score]
  Primary metric: [the single most observable, measurable indicator — e.g., "number of barking episodes per day", "minutes until settle after arriving home", "distance from trigger before reaction"]

Symptom 2: [description]
  Baseline score: [X/10]
  ...

Overall behavioral health score: [average of all symptom scores, 1–10]
```

---

### Step 2: Define Primary Metrics

For each symptom, define at least one **primary metric** — a single, observable, countable measure that tracks change over time. Avoid vague measures ("seems calmer"); require specific ones.

**Good primary metrics by presentation type:**

| Presentation | Good Primary Metric |
|-------------|---------------------|
| Separation anxiety | Minutes of calm behavior after owner departure (filmed) |
| Fear of strangers | Distance at which dog can remain sub-threshold (feet/meters) |
| Hyperactivity/cannot settle | Time to offer first settled behavior after entering room |
| Depression/anhedonia | Number of play initiation attempts per day |
| Resource guarding | Distance at which guarding behavior begins |
| Inter-cat conflict | Minutes of peaceful co-presence in shared space per day |
| Compulsive behavior | Duration of repetitive behavior per 60-minute observation window |
| House soiling | Number of inappropriate elimination incidents per week |

Help the owner select the metric and explain how to measure it simply (count, time, distance — no specialist tools required).

---

### Step 3: Build the Weekly Scoring Sheet

Produce a table the owner completes every 7 days:

```
WEEKLY PROGRESS TRACKER — [Pet Name]

Instructions: Score each symptom every Sunday. Rate 1–10 (10 = most severe, 1 = minimal). 
Also record the primary metric. Be consistent — score at the same time of day, in the same context.

Week | Date | Symptom 1 Score | Symptom 1 Metric | Symptom 2 Score | Symptom 2 Metric | ... | Notes
-----|------|-----------------|-----------------|-----------------|-----------------|-----|------
  0  |      | [baseline]      | [baseline]      | [baseline]      | [baseline]      |     | Baseline
  1  |      |                 |                 |                 |                 |     |
  2  |      |                 |                 |                 |                 |     |
  3  |      |                 |                 |                 |                 |     |
  4  |      |                 |                 |                 |                 |     |
  5  |      |                 |                 |                 |                 |     |
  6  |      |                 |                 |                 |                 |     |
  7  |      |                 |                 |                 |                 |     |
  8  |      |                 |                 |                 |                 |     |
```

---

### Step 4: Decision Rules

#### Rule 1 — Protocol Advancement (Moving to Next Phase)
**Advance when:**
- Primary metric has improved by ≥30% from baseline
- Symptom scores have decreased by ≥2 points
- Both criteria sustained for 2 consecutive weeks
- Owner has demonstrated mastery of current phase skills

#### Rule 2 — Protocol Maintenance (Stay at Current Phase)
**Maintain when:**
- Improvement is present but not yet at advancement threshold
- Owner is still developing skill confidence at current phase
- Environmental factors are unstable (guests, travel, schedule disruption)

#### Rule 3 — Protocol Retreat (Return to Previous Phase)
**Retreat when:**
- Any symptom score worsens by ≥2 points over 2 consecutive weeks
- Primary metric worsens >20% from previous week
- Animal shows increased stress indicators during training sessions
- Owner reports animal "shutting down" during sessions (refusing food, freezing, yawning excessively, lip-licking, leaving)

Retreat action: Return to the previous phase; increase management measures; consider whether environmental stressor has increased.

#### Rule 4 — Protocol Suspension + Adjustment (Neutral Week)
**Suspend and review when:**
- Major life event occurs (move, new pet, hospitalization, visitor)
- Owner cannot maintain session consistency for >5 days
- Animal has a medical event (illness, injury, surgery)

Suspension action: Maintain management only; do not attempt active training; resume after stability returns.

#### Rule 5 — Veterinary Behaviorist Referral
**Refer to veterinary behaviorist (DACVB) when:**
- No improvement (less than 2 points total change across all scores) after 4 weeks of consistent, correctly executed training
- Behavior is maintaining at severity score ≥7 after 6 weeks
- Owner consistently struggles to execute the protocol correctly despite guidance
- Fear/anxiety appears to be increasing despite LIMA-compliant training

Referral message template:
> "Your pet has been working through a structured LIMA-compliant behavioral training program for [X] weeks. Despite consistent effort, we have not achieved the improvement I would expect at this stage. This suggests we may need a deeper level of assessment and possibly behavioral pharmacology support from a veterinary behaviorist. A Diplomate of the American College of Veterinary Behaviorists (DACVB) can combine a full behavioral workup with targeted medication to support the training process. This is not a failure — this is the next appropriate step."

#### Rule 6 — Emergency Escalation (Immediate Veterinary Contact)
**Escalate immediately when:**
- Any bite incident that breaks skin or causes injury
- Worsening aggression despite compliant training (escalation in bite sequence intensity)
- Animal completely stops eating for >24 hours
- Sudden behavior change not explained by training events
- Owner or family member expresses fear of the animal for personal safety
- Animal shows signs of extreme distress: non-stop vocalization, self-injury, complete refusal to engage

Emergency escalation message template:
> "This situation requires professional evaluation before we continue with training. Please contact your veterinarian or an emergency veterinary clinic today. Do not wait for the next scheduled training session."

---

### Step 5: Training Compliance Tracker

Behavior change requires consistent execution. Add a compliance tracker to the weekly sheet:

```
TRAINING COMPLIANCE — Week [X]

Sessions completed: [X] / [target]
Management protocol maintained: [Yes / Mostly / No — explain]
Equipment used correctly: [Yes / Mostly / No — explain]
Any incidents this week: [describe any behavioral incidents, even minor ones]
Owner confidence this week (1–10): [score]
Questions or concerns: [free text]
```

Instruct the owner: If compliance is below 50% of target sessions, do not advance in the protocol. Address the compliance barriers first.

---

### Step 6: Success Declaration

The training program is complete when:

**All of the following criteria are met:**
1. All symptom scores ≤3 for 3 consecutive weeks
2. All primary metrics have improved ≥60% from baseline
3. Owner can execute all techniques independently with confidence ≥8/10
4. Management measures have been gradually faded (animal no longer needs full management scaffolding)
5. Behavior is consistent across at least 2–3 different environments

**Maintenance plan upon success:**
- Continue enrichment schedule indefinitely (enrichment is a welfare need, not just a training tool)
- Schedule a monthly 10-minute "booster" session to maintain skills
- Revisit this tracking system if any new behavioral concerns arise in the future
- Note any environmental factors that contributed to the success (for replication if needed)

---

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `baseline_scores` | Object | Score per symptom at intake with behavioral anchors |
| `primary_metrics` | Object | Observable, countable metric per symptom |
| `weekly_tracking_sheet` | Template | 8-week table for owner to complete |
| `decision_rules` | Object | Advancement, maintenance, retreat, suspension, referral, emergency rules |
| `compliance_tracker` | Template | Weekly training adherence log |
| `success_criteria` | Object | Observable, measurable criteria for declaring training complete |

---

## Quality Gate

- [ ] Baseline score provided for every symptom with behavioral anchors
- [ ] At least one primary metric defined per symptom (specific, measurable, observable)
- [ ] Weekly tracking sheet includes all symptoms and primary metrics
- [ ] All 6 decision rules are documented in the owner-facing deliverable
- [ ] Emergency escalation rule is present and clearly labeled
- [ ] Vet escalation trigger is specific (weeks, score thresholds) — not vague
- [ ] Success criteria are specific and observable (not "when the owner feels satisfied")

---

## Tools

- **Write** — produce the progress tracking template for inclusion in the final deliverable
- **Read** — SECOND-KNOWLEDGE-BRAIN.md Section 1.4 (species-specific behavioral needs) for metric selection guidance

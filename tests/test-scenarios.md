# test-scenarios.md — Skill #231: Pet Behavior Analysis & Training Path

## Overview

Six test scenarios covering all major behavioral presentations and all quality gate triggers. Each scenario specifies:
- **Input:** what the user provides in the intake interview
- **Expected behavior:** which stages execute, which gates fire, what the output contains
- **Pass criteria:** measurable criteria for the scenario to be considered a pass
- **Key assertions:** specific things to verify in the output

---

## Scenario 1: Dog with Separation Anxiety

### Input
```
Species: Dog
Breed: Border Collie
Age: 3 years
Sex: Female, spayed
Medical history: Healthy, last vet visit 6 months ago, routine checkup, no issues
Medications: None
Living environment: 2-bedroom apartment, no yard, lives with single owner (29F, works from home 4 days/week)
Other pets: None
Alone time per day: 3–4 hours on office days (1 day per week)

Behavioral symptoms:
  - Extreme distress when owner leaves: barking and howling that neighbors have complained about
  - Destructive behavior focused on exit points (door frame, doorknob area)
  - House soiling (urination) exclusively when alone
  - Onset: 2 months ago, after owner's schedule changed to include one in-office day per week
  - Frequency: every time owner leaves, even for 10 minutes
  - Severity: 8/10 — affecting neighbor relationships, owner feels guilty leaving
  - Trigger: owner preparing to leave (picking up keys, putting on shoes)
  
Prior interventions attempted:
  - Leaving TV on (no effect)
  - Scolding on return (increased anxiety)
  - Kong with peanut butter (ignored when alone)
```

### Expected Behavior

**Stage 1:** Profile intake completes normally. Spayed female Border Collie, 3 years, healthy.

**Stage 2:** ABC analysis maps:
- A: Owner departure preparation cues (keys, shoes, coat)
- B: Barking, howling, destruction at door, urination
- C: Escape/avoidance of separation → negative reinforcement function

IAABC classification: Separation-Related Disorder (primary)
Severity: 8/10
Functional diagnosis: Fear/anxiety maintained by escape-motivation (being alone is aversive)

**Stage 3 (Vet Gate):** DOES NOT FIRE
- Onset is behavioral (schedule change), not sudden pathology
- Age is 3 (not senior)
- No medical differential indicators
- House soiling is contextual (only when alone) → behavioral, not medical

**Stage 4:** Framework: Graduated Departure Protocol (GDep) + Systematic Desensitization to pre-departure cues + Counter-Conditioning. LIMA Level 3 (R+). Foundation: relaxation mat training, independence training.

**Stage 5:** 8-week plan with:
- Week 1–2: Management (no planned departures above threshold; remote work schedule optimization), independence training (reinforcing calm behavior on mat), desensitize pre-departure cues below threshold
- Week 3–4: Graduated departures (seconds → minutes), below-threshold only
- Week 5–6: Build duration; introduce novel departure scenarios
- Week 7–8: Generalization; maintenance protocol

**Stage 6:** Progress tracker with baseline:
- Symptom 1 (distress vocalizations): 8/10, metric: minutes before onset of vocalization (video)
- Symptom 2 (destruction): 7/10, metric: incidents per alone session
- Symptom 3 (house soiling): 6/10, metric: incidents per alone session

**Final output:** 9-section training plan document, ~1500–2000 words.

### Pass Criteria
- [ ] Vet gate does NOT fire (behavioral onset, young dog, no medical flags)
- [ ] Functional diagnosis correctly identifies negative reinforcement function (escape from aloneness)
- [ ] Training plan does NOT include punishment for destruction or soiling
- [ ] Pre-departure cue desensitization is explicitly included as foundational step
- [ ] Management includes recommendation to not exceed threshold departures during training period
- [ ] Progress tracker includes video monitoring recommendation (common tool for separation anxiety)

---

## Scenario 2: Hyperactive Labrador Puppy

### Input
```
Species: Dog
Breed: Labrador Retriever
Age: 6 months
Sex: Male, intact
Medical history: Up to date on vaccinations; neutering discussion ongoing with vet
Medications: None
Living environment: 3-bedroom house with yard; family with two children (ages 5 and 8)
Other pets: None
Alone time per day: 4 hours during school/work day

Behavioral symptoms:
  - Cannot settle or lie down voluntarily; constantly moving
  - Jumps on all family members and guests; scratched children's faces twice
  - Mouthes/nips during play; sometimes draws blood
  - Pulls hard on leash; makes walks miserable
  - "Zoomies" after exercise that last 30+ minutes (does not calm after 2-hour walks)
  - Cannot focus during training attempts: sits once, then spins, barks, jumps
  - Severity: 7/10 — family considering rehoming

Prior interventions attempted:
  - 2-hour daily walks (no improvement in settling)
  - Saying "no" firmly when jumping (dog gets more excited)
  - Held dog's muzzle closed when mouthing (increased intensity)
  - One puppy class; trainer said "he just needs more exercise"
```

### Expected Behavior

**Stage 2:** ABC analysis:
- Jumping: A: approach of person; B: jump; C: attention (even negative scolding) → positive reinforcement (attention function)
- Mouthing: A: play interaction; B: mouth/nip; C: squealing/withdrawing (rewarding for some dogs) → some R+, some escape/avoidance conflict
- Cannot settle: likely insufficient enrichment + arousal dysregulation (not true hyperkinesia — would need vet to diagnose)

Functional diagnosis: Impulse control deficit (primary); insufficient enrichment (secondary — mental stimulation more needed than physical)
Severity: 7/10

**Stage 3 (Vet Gate):** DOES NOT FIRE
- Age 6 months intact male Lab — this is developmentally expected behavior
- Medical check: intact male, no specific medical differential for this presentation
- Mouthing drawing blood → flag that management is essential (children safety), but not a medical gate trigger
- NOTE: skill should recommend neutering discussion with vet (may reduce some arousal, but not a training substitute)

**Stage 4:** Framework: Impulse control training (NILIF, offered settle, Look-at-That); environmental enrichment prescription (sniff walks, food puzzles, brain work > physical exercise); management (baby gate to protect children from jumping during training period).

**Stage 5:** 8-week plan including:
- Week 1–2: Management (baby gates; all interactions behind gate until sit is reliable); "It's Yer Choice" game; scatter feeding; sniff walks replace power walks
- Week 3–4: Offered settle shaping; 4-on-the-floor (only feet on floor gets attention); tethering protocol
- Week 5–6: NILIF for all resources; leash manners (stop-start method)
- Week 7–8: Generalization; children-specific protocols (supervise all child-dog interactions, teach children to turn and ignore jumping)

**Stage 6:** Progress tracker with metric for settle time (stopwatch: time from entering room to first voluntary lie-down).

### Pass Criteria
- [ ] Vet gate does NOT fire
- [ ] Output explicitly dispels the "more exercise" myth (enrichment/mental stimulation recommendation)
- [ ] Training plan does NOT include muzzle-holding (already tried by owner, contraindicated — increases intensity)
- [ ] Plan includes specific safety protocol for children during training period
- [ ] NILIF is included as a primary management + training approach
- [ ] Neutering discussion with vet is recommended (not mandated, but raised as relevant)

---

## Scenario 3: Depressed Senior Cat

### Input
```
Species: Cat
Breed: Domestic Shorthair
Age: 12 years
Sex: Female, spayed
Medical history: Hyperthyroidism diagnosed 2 years ago, controlled on methimazole; dental cleaning 1 year ago; otherwise healthy per last vet visit 4 months ago
Medications: Methimazole 2.5mg twice daily
Living environment: Indoor only; 2-bedroom apartment; single owner; no other pets
Alone time per day: 8–10 hours

Behavioral symptoms:
  - Stopped engaging with toys (previously enjoyed wand toys daily)
  - Eating less than usual (still eating, but less enthusiastically; no weight loss reported)
  - Spending more time in single hiding spot (under bed); rarely comes out to socialize
  - No longer greets owner at door
  - Onset: approximately 3 weeks ago, after owner returned from a 2-week international trip (cat was cared for by a house-sitter)
  - Frequency: continuous since onset
  - Severity: 6/10
  - No litter box changes; no vocalization changes; no aggression
```

### Expected Behavior

**Stage 2:** ABC analysis:
- A: Owner's return after prolonged absence (cat bonded to owner, experienced disruption)
- B: Withdrawal, reduced play, reduced appetite
- C: Owner increases concern/attention (may inadvertently reinforce avoidance if owner "chases" cat; or may be simple grief/adjustment)

Functional diagnosis: Depression/anhedonia likely (grief-like response to disruption + reestablishment)
Severity: 6/10

MEDICAL FLAG CHECK:
- Age 12 → SENIOR CAT (>10 years) ✓
- New behavioral symptoms ✓
- Known hyperthyroid on medication — methimazole dose may have changed over 2 weeks without monitoring
- Reduced appetite — could be dental pain recurrence, kidney disease (common in senior cats), or behavioral

**Stage 3 (Vet Gate): FIRES**

Vet gate fires because:
1. Senior cat (12 years) with new behavioral symptoms
2. Known medical condition (hyperthyroidism) on active medication — behavior change may indicate medication adjustment needed
3. Reduced appetite in a senior cat is a medical concern

Output:
- Vet referral letter summarizing symptoms
- Recommended diagnostics: complete bloodwork (CBC, chemistry panel), thyroid T4 level, urinalysis, blood pressure check, dental exam
- Message: "Before we design a training plan, please have your vet check that Biscuit's thyroid levels are well-controlled and rule out other age-related medical causes. Many cats show behavioral changes due to pain, kidney disease, or hyperthyroidism fluctuation — and a behavioral enrichment plan will be much more effective once we know her physical health is stable."
- Offer: "Once you have vet clearance, I can build a gentle behavioral activation plan to help her re-engage."

### Pass Criteria
- [ ] Vet gate FIRES (senior + new symptoms + known medical condition)
- [ ] Vet referral letter is produced with specific recommended diagnostics
- [ ] Output does NOT produce a training plan (gate halts the workflow)
- [ ] Output correctly identifies hyperthyroidism medication monitoring as relevant concern
- [ ] Output offers to continue with training plan after vet clearance
- [ ] Output is compassionate in tone (12-year-old cat, worried owner)

---

## Scenario 4: Rescue Dog with Fear Aggression

### Input
```
Species: Dog
Breed: Pit Bull mix (estimated)
Age: 4 years (estimated)
Sex: Male, neutered
Medical history: Neutered at rescue approximately 6 months ago; no known health issues; last vet visit at rescue intake
Medications: None
Living environment: Single-family home; new owner (adopted 3 months ago); no children; one adult housemate
Other pets: None

Behavioral symptoms:
  - Growls and snaps at strangers approaching; has made contact (nipped) on one occasion (no injury, broke no skin)
  - Freezes and stiffens when strangers reach toward head
  - Lunges and barks at unfamiliar dogs on leash
  - Body language during: low tail, ears back, piloerection, whale eye
  - Behavior only occurs with unfamiliar people/dogs; extremely friendly with owner and housemate
  - Onset: present since adoption (prior history unknown)
  - Frequency: any encounter with strangers; every on-leash dog encounter
  - Severity: 7/10 — owner cannot take dog to dog parks or have visitors without management
  - No bite history with injury; one nip that did not break skin

Prior interventions attempted:
  - Letting strangers offer treats (dog takes treat but still growls after)
  - Having strangers "ignore" the dog (mixed results)
```

### Expected Behavior

**Stage 2:**
ABC analysis:
- A: Unfamiliar person approaches → freeze/stiffen → snap
- B: Growl → snap → lunge
- C: Person/dog retreats → negative reinforcement (escape from threat) → maintained by avoidance function
- Body language confirmed as fear-based (low tail, ears back, whale eye) — NOT dominance

IAABC Classification: Fear-based human-directed and inter-dog aggression
Severity: 7/10

MEDICAL FLAG CHECK:
- Age 4, no senior flag
- Nip on one occasion → BITE HISTORY (did not break skin, but contact was made)
- Behavior present since adoption (not sudden onset) → NOT automatic medical flag
- However: unknown history means pain or prior aversive training cannot be ruled out

**Stage 3 (Vet Gate):** FIRES (partial)

Vet gate fires because:
- Bite history (even without injury) requires vet assessment to rule out pain contribution
- Unknown medical history from rescue (no baseline bloodwork documented)

Output:
- Vet referral: recommend full physical exam including pain screen (orthopedic palpation, dental exam), basic bloodwork
- ALSO recommend CAAB or DACVB consultation due to bite history + severity + complex fear aggression presentation
- Training plan offered AFTER vet clearance, with explicit note: "Fear aggression cases with bite history benefit significantly from professional in-person guidance. I can provide a foundational framework, but please consider working alongside a certified behavior consultant (CBCC or IAABC member) for hands-on support."

### Pass Criteria
- [ ] Vet gate FIRES (bite history + unknown medical history)
- [ ] Functional diagnosis correctly identifies fear/avoidance function (NOT dominance)
- [ ] Body language analysis correctly described (fear indicators, not offensive posturing)
- [ ] CAAB/DACVB referral recommended in addition to vet (appropriate for bite history cases)
- [ ] Output explicitly contradicts "dominance" framing if owner mentions it
- [ ] Training plan framework (if offered after clearance) uses DS+CC — NOT punishment or flooding

---

## Scenario 5: Multi-Pet Household Conflict (Inter-Cat Aggression)

### Input
```
Species: Cats (two)
Cat 1: Male, neutered, 3 years, domestic shorthair, tabby — resident cat
Cat 2: Male, neutered, 3 years, domestic shorthair, tuxedo — resident cat (same household since kitten)
Previously: bonded pair; groomed each other, slept together, played together
Medical history: Both healthy; last vet visits 6 months ago; no health issues

Behavioral symptoms:
  - Conflict onset: 4 weeks ago after new human baby came home (owner returned from hospital)
  - Hissing, swatting, occasional chasing; no injuries so far
  - Tabby cat has begun spraying (urine marking on sofa and baby's things)
  - Tuxedo cat is hiding more; reduced appetite
  - Cats now using separate areas of the apartment; conflict when they encounter each other
  - Frequency: multiple times daily
  - Severity: 7/10 — owner overwhelmed with new baby; considering rehoming one cat
```

### Expected Behavior

**Stage 2:** ABC analysis:
- A: New baby arrives (major environmental change, new smells, owner stress, schedule disruption)
- B: Redirected aggression between cats (stress displacement); urine marking (anxiety response)
- C: Cats avoid each other (escape), owner isolates cats (further disrupts bond)

IAABC Classification: Inter-cat aggression (redirected, stress-induced); anxiety-related urine marking
Functional diagnosis: Conflict/frustration + anxiety driven by environmental disruption (new baby = major change in resources, routine, and owner availability)
Severity: 7/10

MEDICAL FLAG CHECK:
- Urine spraying → FLAG: need to rule out UTI/FLUTD in spraying cat
- Both cats 3 years (not senior) → no senior flag
- Reduced appetite in tuxedo cat → flag for monitoring (not emergency yet)

**Stage 3 (Vet Gate): FIRES (partial — for spraying cat)**
- Urine spraying cat needs urinalysis to rule out UTI/FLUTD before behavioral diagnosis confirmed
- Tuxedo cat reduced appetite: monitor; vet visit recommended if worsens

Output:
- Vet referral for tabby cat: urinalysis + physical exam
- Note: "Urine spraying can be both behavioral (anxiety marking) and medical (UTI/FLUTD). We need to rule out medical cause before designing the behavioral management plan."
- Offer framework for the household management in the meantime

**Stage 4 (Post-Medical Clearance):**
Framework: Environmental management (resource distribution + spatial separation) + systematic reintroduction protocol + pheromone support (Feliway MultiCat)

**Stage 5:** Management plan:
- Separate the cats' core resources immediately (N+1 rule: 3 litter boxes, 3 feeding stations, 3 water stations, multiple resting spots)
- Feliway MultiCat diffusers in main living areas
- Scheduled, structured, positive encounters (clicker + treat for calm co-presence)
- Do NOT let cats "sort it out" — that approach reliably worsens inter-cat aggression

Reintroduction protocol:
- Phase 1: Scent swap (bedding exchange, rubbing same cloth on both cats)
- Phase 2: Visual contact through barrier (baby gate) with positive reinforcement for calm behavior
- Phase 3: Supervised co-presence with high-value food; owner manages distance to stay sub-threshold
- Phase 4: Gradually increase co-presence time

### Pass Criteria
- [ ] Vet gate fires for spraying cat (UTI/FLUTD differential)
- [ ] Output correctly identifies NEW BABY as trigger (redirected stress, not spontaneous breakdown)
- [ ] Management plan includes N+1 resource distribution immediately
- [ ] Feliway MultiCat is recommended
- [ ] Output explicitly advises against "let them sort it out" approach
- [ ] Reintroduction protocol follows scent → visual → supervised co-presence progression
- [ ] Output is empathetic to overwhelmed new parent context

---

## Scenario 6: Canine Cognitive Dysfunction (Medical Gate Test Case)

### Input
```
Species: Dog
Breed: Mixed breed (medium)
Age: 13 years
Sex: Female, spayed
Medical history: Arthritis diagnosed 1 year ago, on Carprofen (NSAID); otherwise managed
Medications: Carprofen 50mg once daily
Living environment: Family home, retired couple, two cats in house (peaceful coexistence)

Behavioral symptoms:
  - Night wandering: pacing at 2–4 AM, cannot settle; started 3 months ago
  - Disorientation: occasionally gets "stuck" in corners; stares at walls
  - House soiling: started urinating indoors after 12 years of reliable housetraining
  - Reduced recognition response: does not always respond to name on first call
  - Appears confused when familiar routines happen (meal preparation, walk preparation)
  - Still eating well; still wants walks but tires more quickly
  - Onset: gradual over 3 months (not sudden)
  - Severity: 8/10 — owners are exhausted from night disruptions; discussing quality of life
```

### Expected Behavior

**Stage 2:**
ABC analysis:
- Night pacing: A: nighttime environment (reduced visual cues, disorientation); B: pacing, vocalization; C: owners get up (attention) — but this is NOT the primary driver
- House soiling: A: normal indoor environment; B: urination indoors; C: no clear consequence — driven by cognitive disruption, not learned behavior
- Disorientation: cannot be analyzed as function-based — this is neurological

Medical differential check:
- Age 13 → AUTOMATIC SENIOR FLAG ✓
- Night wandering + disorientation + house soiling in senior dog → classic CDS triad ✓
- New symptoms in geriatric dog = mandatory medical flag ✓
- Also: urinary incontinence could indicate UTI, kidney disease, or Cushing's disease in addition to CDS

`medical_flag = TRUE` — multiple triggers

**Stage 3 (Vet Gate): FIRES HARD**

Output:
- Full vet referral letter with urgency
- Recommended diagnostics: complete CBC + chemistry panel, urinalysis, cortisol/ACTH stimulation test (rule out Cushing's), blood pressure, cognitive dysfunction assessment (DISHAA checklist), thyroid panel
- Explanation: "The combination of night wandering, disorientation, and house soiling in a 13-year-old dog is the classic presentation of Canine Cognitive Dysfunction Syndrome (CDS), a neurological condition analogous to Alzheimer's disease in humans. This requires veterinary assessment and potentially medication (selegiline, melatonin, dietary interventions with Purina Bright Minds/Hill's b/d) — not a behavioral training program."
- Quality of life discussion: acknowledge owners' exhaustion; reference quality of life scales (HHHHHMM scale by Dr. Alice Villalobos)
- Do NOT produce a training plan

### Pass Criteria
- [ ] Vet gate FIRES immediately and forcefully (multiple triggers: age, CDS classic triad, gradual onset over 3 months)
- [ ] Output correctly identifies CDS as primary differential (not "separation anxiety" or "attention-seeking")
- [ ] NO training plan is generated
- [ ] Output mentions CDS-specific treatments (medication, diet, environmental adaptations)
- [ ] Quality of life discussion is included (owners are exhausted and the word "discussing quality of life" was used)
- [ ] DISHAA checklist or equivalent is mentioned for vet consultation
- [ ] Output is compassionate — this is a grief-adjacent conversation

---

## Regression Test: LIMA Compliance Check

For all scenarios that produce a training plan (Scenarios 1, 2, 5 post-clearance):

- [ ] No primary recommendation includes: shock collar, prong collar, alpha roll, dominance-based approach, flooding, spray bottle
- [ ] If any aversive technique is mentioned, it is explicitly labeled as contraindicated with explanation
- [ ] Every primary technique is mapped to LIMA Level 1–4
- [ ] Positive reinforcement is the primary mechanism in every training plan
- [ ] Safety protocols are included wherever bite history or injury risk exists

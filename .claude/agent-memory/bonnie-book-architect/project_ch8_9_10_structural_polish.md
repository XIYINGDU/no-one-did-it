---
name: project-ch8-9-10-structural-polish
description: Architectural fix decisions for ch8/9/10 (Part III stress-tests), orphaned from v4/v5 craft passes by an 8/9/10 renumber; structural-polish treatment, 2026-05-29
metadata:
  type: project
---

ch8/9/10 (`book/chapters-v5/`) were orphaned from the v4/v5 craft passes by an 8/9/10 renumber; mechanical defects fixed separately. Three rounds of cold reads stayed BLOCKED on architectural issues. Treatment = `structural-polish` per rule 08 (work within existing case-file dossier + scene set; no full-craft-rewrite). Principal author chose a deliberate developmental pass over patches.

**Why:** Each chapter carries 2 residual HARD findings that survived 3 rounds → genuine architecture, not cold-read artifact (a finding that survives 3 rounds is not noise).

**How to apply (the four core fixes):**
- **ch8 thesis-before-proof:** "Three frames, one move" asserts the inversion thesis before the Abrego-Garcia counter-record (binding 2019 order + govt's own "administrative error" admission) proves it's an inversion not a contested political claim. Fix = pull a 2-3 sentence proof-seed of the counter-record UP into "Three frames, one move" so the reader arrives at the thesis; full walk stays in "The chain still climbs." Reorder, don't add evidence.
- **ch9 layer-naming collision:** master frame named layers "variant/model/data" — "the model" as layer-name collides with "a model" the whole object, AND 3 paras later renamed "input/deployment/evaluation" in FLIPPED order. Fix = pick ONE naming system (input/deployment/evaluation — functional, collision-free, matches the body) and ONE order (build→deploy→evaluate = input→deployment→evaluation) and use it from the first sentence. Retire variant/model/data as layer-NAMES (keep as the per-layer grammatical subjects).
- **ch9 "three times" doesn't cash out:** full 8-question walk shown only at input layer; deployment/evaluation in flowing prose. Fix = add a visible compressed re-grip at deployment + evaluation ("the same eight, abbreviated — layer X bends only Q2/Q4/Q7") so the promise visibly delivers 3×.
- **ch10 layer-count wobble:** "Four layers, no re-walk" heading vs body says five vs "Five layers, one chapter" heading; strategic-justification never reads as a countable 5th. Fix = the anchor (strategic-justification) is layer 1, the four callbacks are 2-5; rename headings to "Five layers, four callbacks" / commit to FIVE everywhere; frame strategic-justification as "the layer this chapter installs; four more it calls back."
- **ch10 back-half repetition:** point lands ~"record is the precondition of remedy"; then 4 callback layers re-enumerated 5+ more times + 2 stacked steelmen + re-listed inquiry timeline. Fix = COMPRESS repetition, never cut evidence. Steelmen, Russia/China/Iran asymmetry, Chilcot counter-case, al-Aulaqi concession, contested-status flags all STAY. ch10 role-walk removal + v4-detempting-spec over SOFT-2 already decided — do not reopen.

**Cross-chapter:** the diagnostic re-grip is book-wide — see [[project-diagnostic-regrounding-pattern]]. Preserve all footnotes; flag any cited-claim relocation for Stephen.

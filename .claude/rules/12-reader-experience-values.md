---
description: "Reader-experience values rule: chapter engagement quality is judged against ten declared values. Five are core (V1, V3, V5, V7, V8 — no regression permitted under Gate B); five are craft (V2, V4, V6, V9, V10 — partial pass allowed with declared tradeoff)."
---

**Reader engagement quality is judged against ten declared values; five are core (no regression permitted under Gate B); five are craft (partial pass allowed with declared tradeoff).**

# Reader-Experience Values

**Scope:** binds every chapter under `book/chapters-v2/` that enters a rewrite cycle. Resolves the "engaging / emotional / inevitable" quality question into a discrete rubric. The rubric is the resolution layer for `/contract-audit`'s `feels:` slot, for laura's red-team scope, for nancy's veto trigger on V7 and V8, and for the principal author's Gate B read.

The book's central argument is that responsibility laundering hides chains behind procedural surfaces. The reader experience must demonstrate the diagnostic without committing the same laundering moves internally. The five core values below are the constitutional floor; the five craft values are how engagement is achieved without violating the floor.

## Core values (no regression permitted)

### V1 — Earned, not manufactured
The reader's feeling derives from documented fact, not from craft technique that exceeds what the evidence supports.

- **Positive indicator:** the reader can point to the document, scene, or sequence that earned the feeling.
- **Negative indicator:** the reader feels strongly but cannot say why; or the feeling outruns the evidence grade per rule 02.
- **Test:** strip the craft devices from a paragraph (focalization, hammer line, two-track structure). If the feeling vanishes entirely, the craft was carrying weight the evidence couldn't. If it dims proportionally, the craft was amplifying real evidence — pass.

### V3 — Sympathy follows the chain, not the camera
When the chapter ends, the reader's strongest moral weight rests where responsibility rests (per rule 01 taxonomy + responsibility-chain mapping), not where narrative attention rested most.

- **Positive indicator:** the visible goat may be sympathetic, but the reader's anger or accountability-instinct lands on the chain that engineered the substitution.
- **Negative indicator:** the reader closes the chapter feeling sorry for the goat and forgets the chain existed.
- **Test:** at chapter end, the reader can answer "who do I want held accountable?" — and the answer is consistent with the chapter's responsibility-chain map, not with the actor who received the most prose attention.

### V5 — Capacity change, not just affect change
The reader leaves the chapter with a new ability — to name a pattern, apply a discrimination, recognize a move — that survives the affect evaporating.

- **Positive indicator:** the chapter's diagnostic survives the reader's emotional response evaporating.
- **Negative indicator:** the reader was moved but cannot, a week later, say what the chapter taught them.
- **Test:** at the end of the chapter, the reader can complete: "Now I can recognize ___ when ___ happens." If not, the chapter installed feeling but not capacity.

### V7 — Severity proportional to evidence
Prose certainty matches the evidence grade per rule 02. A-grade case carries hammer prose; C-grade case carries hedged prose with the contestation visible inside the sentence rhythm.

- **Positive indicator:** for every hammer-line moment, the underlying claim's evidence grade and the prose's certainty register match within one notch.
- **Negative indicator:** definitive prose on a B/C-grade claim, or hedged-into-mush prose on an A-grade claim.
- **Test:** flag every assertive sentence in the chapter; map each to its underlying claim's evidence grade. A/A-stance pass; B/B-stance pass; A/B-stance under-claim (acceptable); B/A-stance fail.

### V8 — No internal laundering
The chapter does not, in its own prose, commit the moves it diagnoses externally.

- **Positive indicator:** no invented interiority; no sympathy-bait beyond the record; no false equivalence between cases the taxonomy distinguishes; no "system did it" hand-wave where the chain is documented.
- **Negative indicator:** the chapter would itself fail the book's own diagnostic if examined by a hostile reader applying rules 01, 05, 06, 07.
- **Test:** apply the rule-01 taxonomy, rule-05 overclaim scan, rule-06 quote-integrity, and rule-07 implication-burden audit to the chapter as if it were a case under examination. Does it pass its own rules?

## Craft values (partial pass allowed with declared tradeoff)

### V2 — Specific, not sentimental
The reader feels about *this* case, *this* person, *this* document — not about "the human condition" or "injustice in general."

- **Test:** substitute another case's proper nouns into the chapter's hammer line. If it still works, the line is sentimental rather than specific; revise.

### V4 — Reader does the work
The recognition beat is *achieved* by the reader, not *delivered* to them.

- **Test:** count explicit "moral of the story" sentences — anything beginning with "what this shows," "the deeper truth," "ultimately," "the lesson here." A well-crafted chapter has zero or one; two or more means the author did the recognizing for the reader.

### V6 — Diagnostic memory, not viral memory
The chapter persists because it changed how the reader sees something, not because it had a clever moment.

- **Test:** a sample reader six weeks after reading can answer "what was the chapter about?" with a diagnostic pattern, not with a scene. "It was about [the partial-scapegoat pattern]" passes; "there was this great scene with the memo" fails.

### V9 — Calibrated stance toward the reader
The reader is treated as capable of complexity; the prose does not flatter, condescend, or moralize.

- **Test:** would a sophisticated reader (the book's actual audience) feel handled? If yes, calibration is wrong even when prose is otherwise clean.
- **Operationalized by:** rule `14-authorial-stance.md`. Pronoun discipline ("we" default; imperative for instruction; refuse author-voice "you" and meta-frame language) is the sentence-level mechanic by which V9 holds. A chapter that violates rule 14 typically violates V9 at the same time.

### V10 — Audio-survivable
The chapter works read aloud — sentence rhythm carries the recognition, not visual layout.

- **Test:** a non-reader listener gets the click from a paragraph read aloud, without italics or footnote glance. If the recognition requires visual layout, audiobook listeners will lose it.

## Gate B outcome classes (derived from rubric)

| Outcome | Conditions | Action |
|---|---|---|
| **Full pass** | All 5 core values pass with no regression AND ≥3 of 5 craft values net positive. | Adopt rewrite; promote chapter to `ready`. |
| **Conditional pass** | All 5 core values pass with no regression AND 1–2 craft values net positive, with declared tradeoff. | Adopt with named limits recorded in the chapter's audit-history snapshot. |
| **Core pass / craft fail** | All 5 core values pass AND 0 craft values net positive. | Reject the craft rewrite for this chapter; the chosen craft moves don't work here. Reclassify per rule 08 to `prose-polish` or accept current state. |
| **Core fail** | Any core value regressed. | Hard reject. Restore from snapshot per rule 09. Diagnose which craft move violated which core value before any re-attempt. |

<example>
Chapter 11 Gate B package reports:

- Core values (V1, V3, V5, V7, V8): all pass with no regression from the pre-rewrite baseline (laura's red-team memo and nancy's V7 evidence-grade check both green).
- Craft values: V6 (diagnostic memory) and V9 (calibrated stance) net positive; V2 (specific not sentimental) regresses on one paragraph that imports a generic "tragedy of the commons" framing; V4 (reader does the work) is unchanged; V10 (audio-survivable) is unchanged.

The rubric reads: 5 core values pass with no regression, 2 of 5 craft values net positive — that meets the "Conditional pass" row (1–2 craft values net positive). Outcome: adopt with named limits. The chapter's audit-history snapshot records the V2 regression as the declared tradeoff so a future pass can target it.

If V2 had been a core value, the same data would have produced a Core fail; if 3 craft values had been net positive instead of 2, the same data would have produced a Full pass.
</example>

## Who judges what

- **xaiolai (Gate B reader):** judges all 10 values; final authority on the outcome class.
- **laura-red-team-editor:** judges V1, V3, V8 specifically — the values most vulnerable to craft moves. Carries independent veto per rule 03 if any of these regress.
- **nancy-legal-risk-counsel:** judges V7 (severity-evidence mismatch) and V8 (internal laundering as defamation surface). Carries independent veto per rule 03.
- **bonnie-book-architect:** judges V5 (capacity change) and V6 (diagnostic memory) — the architectural values.
- **wayne-narrative-lead:** self-polices V2, V4, V9, V10 during drafting; builds the Gate B package with each value's evidence.
- **stephen-fact-check-director:** verifies V7 evidence-grade match using existing source ledger.
- **the-reader:** does not judge these values at all. Per rule `15-reader-experience-authority.md`, the reader cold-reads the publication form and reports lived experience without a rubric. The ten values here are the *spec*; the reader's cold-read is the *empirical check that the spec was actually achieved in a real reading*. A chapter can pass all ten values and still fail the reader. The two are complementary: this rule is judged against the artifact; rule 15 is judged by reading it.

## Why this rule exists

Codex Test F flagged Gate B as a single point of failure on undefined "genuinely stronger." The plan's reliance on "xaiolai judges" lacked measurable criteria. Rule 12 makes the criteria explicit and falsifiable. xaiolai still judges — but against named values, with structured outcome classes, and with independent vetoes from laura and nancy on the values most at risk.

This rule is the constitutional anchor for Gate B in `process/plans/fiction-craft-rewrite-workflow.md`. It is referenced by `/contract-audit`'s `feels:` slot resolution, by laura's red-team scope, and by nancy's veto trigger.

---
name: project-ch13-architecture
description: Chapter 13 ("A Reader's Field Guide") architecture decisions — six page-shaped artifacts that survive separation from the book, byte-exact taxonomy re-presentation, 8×6 reader-role crosswalk with case-anchored cells, closing-sentence deferred to xiaolai.
metadata:
  type: project
---

# Chapter 13 architecture — Part IV closer (2026-05-26)

**Design rationale:** ch-13 hands the diagnostic to the reader. It is not a recap; the chapters did the install. It is a field guide — six artifacts engineered to survive separation from the book (a reader photocopies page five; the page still works).

## Six artifacts (load-bearing teaching device)

| # | Artifact | Source-of-truth | Byte-exact? |
|---|---|---|---|
| 1 | The eight questions | `AGENTS.md` core diagnostic | YES — Stephen-verified byte-exact, 2026-05-26 |
| 2 | The four-category taxonomy | `.claude/rules/01-case-taxonomy.md` | YES — Stephen HARD-gate caught initial drift ("machine, model, benchmark…" vs rule's "tool, machine, algorithm…"); corrected to byte-exact |
| 3 | AI-stack three-layer diagnostic | ch-10 install (input / deployment / evaluation) | YES — Alan verified |
| 4 | War five-layer stack | ch-8 install (chain-of-command secrecy / proxy deniability / contractor shells / civilian invisibility / strategic justification) | YES — Alan verified; ordering note: ch-8 frames strategic justification as anchor, ch-13 lists it fifth; acceptable for portable artifact |
| 5 | Chapter-by-chapter index | mechanisms + counter-cases per chapter | Stephen spot-checked 5 entries; ECtHR Ukraine v Russia date discrepancy corrected (now "pending on the merits as of mid-2026" matching ch-8) |
| 6 | 8×6 reader-role-by-domain crosswalk | rows: citizen / juror / journalist / employee / manager / contractor / professional / voter — cols: 6 anti-laundering moves | every cell carries a role-native action with one anchor case named; Laura HARD-gate caught initial "see X row" cross-references and forced rebuild |

## Crosswalk design rule (Laura HARD-gate)

The crosswalk is the most ambitious artifact and the one most likely to be photocopied alone. Original draft had several cells reading "see Employee row" / "see Voter row" — broken tether. Laura's HARD-gate: every cell must carry a role-native action with one anchor case named, or explicitly mark `n/a` for cells where the move truly does not apply to the role.

Worked example, rebuilt Citizen row:
- Move 1 → ch-2 Boeing "Technical Pilots" framing
- Move 2 → ch-7 *DOJ v New York*, June 27, 2019
- Move 3 → ch-11 Park doctrine
- Move 4 → ch-12 PROFS preservation Nov 28, 1986
- Move 5 → ch-12 *Common Cause v Lewis* file admission Jul 12, 2019
- Move 6 → ch-8 Inquiries Act 2005 §21

Manager Move 6 honestly marked `n/a` where the move duplicates Citizen Move 6 for the role.

## Closing-sentence handling

Bonnie's brief deferred the book's closing sentence to xiaolai (the human, not the surrogate). The chapter ends with `*[FINAL SENTENCE — xiaolai authors]*` at line 303, with Wayne's candidate template "*The altar moves. The questions stay.*" offered above the placeholder as non-binding. The book is not done by STATUS.md exit condition until xiaolai writes that line.

## What this chapter does NOT do

- Does not introduce new case material (beat 5 explicitly: "no new citation").
- Does not collapse the diagnostic into a self-help imperative; Wayne's original "Recognise it / Diagnose it / Act on it / Avoid becoming it" cadence was tightened on Laura's SOFT to remove the four-verb parallelism.
- Does not flatten the chapter-by-chapter nuance; each crosswalk cell carries a chapter pointer + named case anchor, so the artifact has a return path to the install.

## What downstream artifacts can cite back

- The six-artifact set is the basis of any one-page derivative material Blair builds for the proposal pack (the reader-role crosswalk especially).
- The chapter-by-chapter index is the basis of the manuscript's running heads and chapter-summary block in the proposal pack.

**Tested against:** 4-gate review (Stephen / Alan / Laura / Nancy) plus consolidated revision pass, 2026-05-26. Stephen's taxonomy-byte-exact HARD-gate caught the most consequential error: a "verbatim" self-certification on text that had drifted from rule 01.

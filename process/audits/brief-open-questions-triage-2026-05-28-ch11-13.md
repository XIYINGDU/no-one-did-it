---
audit_id: brief-open-questions-triage-2026-05-28-ch11-13
audit_date: 2026-05-28
owner: bonnie-book-architect
scope: book/chapters-v2/{11,12,13}-*-brief.md `## Open questions` sections
---

# Brief Open-Questions Triage — Chapters 11–13 (2026-05-28)

## Purpose

Triage the `## Open questions` H2 in each of the ch-11, ch-12, ch-13 briefs against the corresponding `book/chapters-v2/<n>-*.md` chapter prose. Apply the status taxonomy (`RESOLVED IN DRAFT` / `TRACKED IN STATUS.md` / `STILL OPEN — xaiolai` / `DEFERRED` / `STALE`) and annotate each numbered question in-place.

## Per-chapter counts

| Chapter | Total open Qs | Resolved in draft | Tracked in STATUS.md | Still open — xaiolai | Deferred | Stale |
|---|---|---|---|---|---|---|
| ch-11 — Make Responsibility Follow Control | 3 | 3 | 0 | 0 | 0 | 0 |
| ch-12 — Keep the Record | 3 | 2 | 0 | 1 | 0 | 0 |
| ch-13 — A Reader's Field Guide | 5 | 3 | 1 | 0 | 1 | 0 |
| **Total** | **11** | **8** | **1** | **1** | **1** | **0** |

## STILL OPEN — items for xaiolai

Single item across the three chapters:

1. **ch-12 brief, Open Question #2 — source-ledger self-reference paragraph length.**
   Chapter prose holds the self-reference at one paragraph (line 95: "One short paragraph we cannot avoid. What we are writing is itself a record..."). Architect's cap honored in draft; xaiolai still owns the length decision (expand, hold, or trim). No other crew member can decide this on xaiolai's behalf.

## TRACKED IN STATUS.md — items already on the exit-condition register

1. **ch-13 brief, Open Question #5 — book's closing sentence.**
   Chapter draft uses the architect's template ("The altar moves. The questions stay.") at ch-13 prose line 299. xaiolai owns the final-sentence approval per the existing `book/STATUS.md` exit-condition row. No new memo action needed; the STATUS.md row is the live tracker.

## DEFERRED — items routed to non-Jerry owner with timing

1. **ch-13 brief, Open Question #3 — 8x6 crosswalk typographic feasibility.**
   Deferred to diagrams-workflow commissioner by chapter freeze. Chapter prose implements the 8×6 crosswalk content (lines 117–149+); the diagrams workflow judges whether the artefact fits on one trade-paperback page or runs to two. Wayne does not gate on this per architect's instruction in the brief.

## STALE — items invalidated by spine changes

None. None of the ch-11/12/13 briefs reference removed chapters or absorbed structural roles. (Contrast: ch-10 brief #2 referenced the now-absent ch-14, per pre-identified triage context.)

## Methodology and assumptions

- Each numbered open question in `## Open questions` was checked against the corresponding chapter prose via targeted grep (one search per question, typically), not via full chapter re-read.
- "RESOLVED IN DRAFT" means the chapter prose materially answers the open question in a way consistent with the architect's recommendation in the brief itself, OR explicitly takes the architect's instinct as the operating choice. It does NOT mean the question is permanently closed; if Wayne or Laura later disagrees on a draft-time call, the status can be re-opened during the rewrite lifecycle per rule 09.
- "STILL OPEN — xaiolai" is reserved for questions whose resolution requires the principal author's explicit decision (length, voice, closing sentence, judgment-of-tradeoff).
- "DEFERRED" carries a named owner and a triggering condition (e.g., "by chapter freeze," "after diagrams commission").

## Risks

1. The brief warnings (pronoun-discipline, implication-burden) flagged at every edit are pre-existing in the brief body, not introduced by the STATUS annotations. They are unrelated to this triage and should be addressed in a separate brief-language cleanup pass if xaiolai wants the briefs themselves to comply with rule 14.

## Handoff

- **Jerry (crew chief):** review the per-chapter count table; the 1 STILL-OPEN-for-xaiolai item (ch-12 #2 self-reference length) is the only blocking decision. Route to xaiolai when convenient.
- **Diagrams-workflow commissioner:** owns ch-13 brief #3 (crosswalk feasibility), by chapter freeze.
- **xaiolai:** ch-12 brief #2 (self-reference paragraph length) — non-blocking but principal-author-owned.
- **Wayne:** no action; the triage confirms the chapter drafts are consistent with the briefs' architect recommendations.

---

Owner: Bonnie / Book Architect / Developmental Editor
Task: Triage open questions in ch-11/12/13 briefs against corresponding chapter prose; annotate each numbered question in-place; produce per-chapter triage memo.
Inputs reviewed: book/chapters-v2/11-make-responsibility-follow-control-brief.md `## Open questions`; book/chapters-v2/12-keep-the-record-brief.md `## Open questions`; book/chapters-v2/13-a-readers-field-guide-brief.md `## Open questions`; corresponding chapter drafts (in-review for ch-11, ch-12; ready for ch-13); pre-identified triage context (ch-12 #2 still-open-for-xaiolai; ch-13 #5 tracked in STATUS.md).
Output: 11 numbered questions across three briefs annotated in-place with `STATUS (2026-05-28 triage):` lines; this per-chapter memo with counts table, STILL OPEN list, DEFERRED list, TRACKED list.
Evidence grade: A — chapter prose verified by targeted grep against the brief's specific decision per question.
Assumptions: chapter prose is the source of truth for what was decided; brief annotations preserve the original open-question text for traceability; pre-existing warn-mode brief-language violations (pronoun, implication) are out of scope for this triage.
Open questions: none introduced by this triage.
Risks: brief-language warnings unrelated to this triage remain in the briefs; a separate cleanup pass may be warranted but is not gating any chapter-prose work.
Handoff: jerry-crew-chief (review per-chapter table; route ch-12 #2 to xaiolai when convenient); no other action required.

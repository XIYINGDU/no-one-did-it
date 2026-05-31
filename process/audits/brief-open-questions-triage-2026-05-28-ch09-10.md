---
status: audit
audit_date: 2026-05-28
owner: bonnie-book-architect
scope: chapters 9 and 10 — brief open-questions triage
---

# Brief Open-Questions Triage — ch-9 + ch-10 (2026-05-28)

Owner: Bonnie / Book Architect / Developmental Editor
Task: Triage every `## Open questions` item in the ch-9 and ch-10 briefs; assign a status from the declared taxonomy; edit each item in place; surface anything still requiring xaiolai decision.
Inputs reviewed:
- `book/chapters-v2/09-when-power-calls-itself-the-goat-brief.md` (3 open questions)
- `book/chapters-v2/10-the-model-did-it-brief.md` (5 open questions)
- `book/chapters-v2/09-when-power-calls-itself-the-goat.md` (in-review prose)
- `book/chapters-v2/10-the-model-did-it.md` (in-review prose)
- `book/toc.yml` (current 13-chapter spine)
- Memory: `project_ch13_architecture` (ch-14 absorbed into ch-13)

## Per-chapter counts

| Chapter | Questions | RESOLVED IN DRAFT | TRACKED IN STATUS.md | STILL OPEN | DEFERRED | STALE |
|---|---|---|---|---|---|---|
| ch-9 | 3 | 2 | 0 | 0 | 1 | 0 |
| ch-10 | 5 | 3 | 0 | 1 (live half of q4) | 0 | 2 (q2 ch-14 ref + q4 ch-14 ref; q2 has live half tracked) |
| **total** | **8** | **5** | **0** | **1** | **1** | **2 (compound)** |

Note on compound rows: ch-10 q2 and ch-10 q4 each carry a STALE half (ch-14 references) and a live half. Q2's live half is tracked-to-future-ch-12-brief; q4's live half is STILL OPEN for xaiolai.

## STILL OPEN — xaiolai

One decision item:

1. **ch-10 brief, open question 4 (AI agent / action layer flag).** Decide whether ch-10 should carry a one-sentence forward-flag for the action layer (AutoGPT-style agents, computer-use agents) at beat 8 or beat 10, or defer that flag entirely to ch-13's anti-laundering architecture treatment.
   - Architect recommendation: defer to ch-13. Inserting an action-layer flag into ch-10 weakens the three-layer load-bearing claim Wayne worked to install ("the diagnostic applies three times per AI system"). Beat 8 and beat 10 currently land that claim cleanly. A fourth-layer flag in the closing beats would dilute the recognition.
   - Counter-recommendation any architect could make: a one-sentence flag at beat 10 acknowledges the frontier without dragging it into the load-bearing claim, and avoids the chapter reading as dated within twelve months.
   - xaiolai decision required.

## DEFERRED items

One:

1. **ch-9 brief, open question 2 (diagram form: faint underlay vs. sidebar).** Deferred to wayne-narrative-lead at diagram-render time pre-manuscript-freeze. Brief default (faint underlay) stands; no draft prose forces a choice yet.

## STALE items

Two (both compound — STALE half noted, live half handled separately):

1. **ch-10 q2 — chapter-14 reference.** Current spine is 13 chapters per `book/toc.yml`; "Anti-Laundering Architectures" was reabsorbed into ch-13 architecture per memory `project_ch13_architecture` (2026-05-26). Ch-10 ↔ ch-12 live half tracked to ch-12 brief time.
2. **ch-10 q4 — chapter-14 reference.** Same ch-14 staleness. Live action-layer-flag half escalated to xaiolai (above).

## Handoff

1. **xaiolai** — single decision on the ch-10 action-layer-flag question (above).
2. **bonnie-book-architect** — at ch-12 brief time, enforce build-forward of ch-10's three-layer diagnostic into ch-12's record-discipline rules rather than restatement.
3. **wayne-narrative-lead** — at diagram-render time, execute ch-9 brief default (faint-underlay form) for the Watergate + Iran-Contra historical timeline.

Evidence grade: A (every triage call backed by a grep of the live prose plus the current `book/toc.yml`; ch-9 prose lines 168-186 and ch-10 prose lines 179, 187 carry the load-bearing evidence cited above).
Assumptions: book/toc.yml is current source of truth for chapter count; project_ch13_architecture memory accurately reflects ch-14 absorption; both chapters remain at `in-review` and will not have their architecture re-opened by the triage memo itself.
Open questions: see STILL OPEN above (one item, xaiolai).
Risks: low — triage is structural and references prose already on disk; no new evidence claims introduced. Hook warnings on both briefs are warn-mode and pre-existing (not introduced by the triage edits).

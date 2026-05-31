---
name: project-book-chapters-complete
description: All 13 chapters reached status:ready in four production waves (2026-05-25 / 2026-05-26); the chapter-production phase is closed. Remaining book-done work is post-chapter (proposal pack, manuscript compile, portfolio sweep, principal read).
metadata:
  type: project
---

# Book chapter-production phase: COMPLETE (2026-05-26)

The four-wave production run that began with ch-02 on 2026-05-25 closed on 2026-05-26 with Wave 4 (`3f8f1c1`). All 13 chapters at `status: ready`. Total prose body ≈ 97,400 words; full files ≈ 104,800.

**Why:** chapter-production was the goal-hook-authorized sprint ("finish all chapters"). The goal is satisfied. Jerry's role pivots from chapter-orchestration to portfolio-orchestration.

**How to apply:** Do not re-open chapter production. Do not re-spawn Wayne to draft new chapters. Do not re-spawn Bonnie to design new architectures. Future invocations should route to the post-chapter remainder per `.claude/state/current-focus.md`:

1. Blair proposal pack via `/proposal-pack`.
2. Final Nancy portfolio sweep across all 13 cleared chapters.
3. `/compile-book` to assemble the manuscript per `book/toc.yml`.
4. xiaolai-human principal author final read.
5. xiaolai-authored closing sentence for ch-13 line 303 placeholder.

## Wave-by-wave summary

| Wave | Chapters | Date | Notes |
|---|---|---|---|
| 1 | 01, 02, 03 | 2026-05-25 | Part I install: diagnostic + four-category taxonomy. ch-02 was the first chapter to reach ready (13 revisions applied). |
| 2 | 04, 05, 06, 07 | 2026-05-25 | Part II patterns: proxy/sponsor, partial-scapegoat, pretext, record-control. Parallel dispatch across 4 chapters worked; cleared in one batch. |
| 3 | 08, 09, 10 | 2026-05-25/26 | Part III stress tests: war, power, AI. Authorized 9→10→8 reading order per `[[project_part3_sequencing_decision]]`. Heavy defamation surface; HARD-gate revisions on all three. |
| 4 | 11, 12, 13 | 2026-05-26 | Part IV anti-laundering rules: design moves, record discipline, reader's field guide. Argumentative chapters; no new case files. |

## What worked

- **Parallel dispatch within a wave.** Wave 2's four-case parallel research → parallel brief → parallel draft → sequential gates per chapter is the production model.
- **4-gate sweep on every promotion.** Stephen / Alan / Laura / Nancy in parallel after each draft; consolidated revision dispatch back to Wayne.
- **STATUS.md as the orchestration state board.** Resumable across sessions; the right-most "State" column is the punch-list. Update it after every gate clears.
- **xiaolai-surrogate substitution** under goal-hook authorization (see `[[project_xiaolai_surrogate_substitution]]`).

## What broke

- **Connection drops mid-draft.** Multiple Bonnie/Wayne dispatches dropped on socket error during long prompts; mitigated by tighter prompts and immediate retries.
- **`Edit` precondition.** Edit tool requires Read first in the same session. Frontmatter-only Reads (3 lines) satisfy the precondition.
- **Fabricated claims at the seam.** Shirley filled a verification gap on VW Winterkorn with a "May 2025 plea" that did not exist; Stephen caught. Pattern: researchers must declare missing-evidence rather than narrate around it. Cross-reference `[[feedback_research_gloss_attribution]]`.

## Carry-forward state

- 23 `[EVIDENCE NEEDED]` markers across ready chapters, listed in `book/STATUS.md`. Retention is intentional per exit condition.
- Two scheduled Nancy re-pass clocks fire 2026-06-24 (ch-02 Ukrainian children) and 2026-06-25 (ch-8/9/10/12 live content).
- Stephen open-questions list grew across waves; consolidated in chapter handoff blocks and STATUS.md cross-cutting items.

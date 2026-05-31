---
description: Show the current production state of the book — which chapters are at which stage, what's blocking, what runs next. Reads book/STATUS.md and surfaces the punch-list view plus the next-action recommendation.
owner: jerry-crew-chief
---

# Book Status

Dispatch the `jerry-crew-chief` agent to read `book/STATUS.md` and return a concise snapshot of the book's production state plus the recommended next action. Jerry is the crew chief; reading the status board and naming the next-action is his cross-cell routing responsibility.

## What to return

1. **Headline state.**
   - Chapters at `status: ready`: count of 13
   - Chapters in progress (any cell touched, not yet ready): count + slug list
   - Chapters queued: count + slug list
   - Current wave (per the recommended production order)

2. **The next action.** Single sentence + the slash command to run it. Examples:
   - `"Run /produce-chapter 03-who-could-have-stopped-it — Wave 1, chapter 3 is the next ch in the forced Part I order."`
   - `"Wave 2 case-file research is in-flight; check researcher outputs before next dispatch."`
   - `"Awaiting principal beat-10 sanity on chapter 4 — read the chapter and reply with promote / revise."`

3. **Date-fired items due within the next 14 days.** Especially the 30-day Nancy re-pass on slot 8 (ch-02 Ukrainian children, due 2026-06-24).

4. **Cumulative work surface.** Total `[EVIDENCE NEEDED]` items open; whether a portfolio Nancy pass is due (after wave-end).

## What you do NOT do

- Do not modify `STATUS.md`. This is a read-only status report.
- Do not dispatch agents. To advance a chapter, use `/produce-chapter <slug>`.
- Do not infer state that isn't in `STATUS.md`. If the file is missing or stale, say so — do not guess.

## Response format

Under 30 lines. Tight punch list, not a narrative.

<example>
Context: principal runs /book-status after a multi-day pause.
output:
```
Book state (last updated 2026-05-25):

Ready (1/13):  02-the-four-goats
Partial (1):   05-the-guilty-goat (1/4 case files: Bhopal)
Queued (11):   01, 03, 04, 06, 07, 08, 09, 10, 11, 12, 13

Current wave: Wave 1 (Part I closeout, ch-3 → ch-1)

Next action: Run /produce-chapter 03-who-could-have-stopped-it

Date-fired within 14 days:
  2026-06-24 — Nancy 30-day re-pass on slot 8 (ch-02 Ukrainian children)

Cumulative: ~16 [EVIDENCE NEEDED] items across ch-02 case files (Delon background); no portfolio Nancy pass due yet (Wave 1 incomplete).
```
</example>

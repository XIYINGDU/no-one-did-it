---
title: SOFT-1 footnote-integrity per-cell check (D1 cuts, ch-3 / ch-6 / ch-12)
owner: stephen-fact-check-director
status: cleared
phase: v4
date: 2026-05-29
inputs_reviewed:
  - book/plans/soft-device-economy-editspec-2026-05-29.md (Bonnie SOFT-1 cut spec, RISKY flags)
  - book/chapters-v4/03-who-could-have-stopped-it.md (full grep of [^N] markers + body read)
  - book/chapters-v4/06-the-pretext.md (full grep of [^N] markers + body read)
  - book/chapters-v4/12-keep-the-record.md (full grep of [^N] markers + body read)
note: SAFETY CHECK ONLY. No prose cut. This tells Wayne which [^N] are safe-to-lose-from-the-cut-prose vs. which would orphan a definition.
public_release: mechanical-pass-cleared
public_release_date: 2026-05-31
---

Owner: Stephen / Fact-check Director
Task: Per-cell footnote-integrity check on three FOOTNOTE-RISKY D1 cuts before Wayne executes.

# Method

Grepped every inline `[^N]` marker in each chapter body and mapped it to a line. Located the References (`[^N]:` definitions) block start in each chapter. A cut orphans a definition only if it removes the SOLE inline use of a `[^N]` whose definition lives in that chapter's `## References`. Then read each cut zone against the surviving anchors.

# Per-cell verdicts

## ch-3 — l.176-184 (five-channel prose re-walk) — SAFE TO CUT

The cut zone (l.176-184) carries **zero inline `[^N]` markers**. Every citation in this chapter's case work is anchored upstream in the narrative scene paragraphs (`[^88]`–`[^125]`, all between l.15 and l.140); the last body marker is at l.140. The prose re-walk, the table (l.188-194), and all surrounding scoreboard prose are narration-only — they re-state cases already cited above. **No definition orphaned. No marker to preserve.** Cut as specced.

## ch-6 — l.193-206 (four-case scoreboard re-walk) — SAFE TO CUT

The cut/fold zone (the `## No single channel pierced all three` section, l.187-219; cut target l.193-206) carries **zero inline `[^N]` markers**. Last body marker is l.173 (`[^244]`/`[^245]`); References begin l.222. The three pretext cases are cited upstream in the steelman/collapse sections (`[^201]`–`[^245]`). The scoreboard prose is narration-only. **No definition orphaned. No marker to preserve.** The Hofeller citation Bonnie flagged for SOFT-2 (`[^N]` at the Hofeller beat) is NOT in the cut zone — it lives upstream and SOFT-2 elevates that beat. Cut/fold as specced; preserve the Hofeller counter-case beat per Bonnie.

## ch-12 — l.137 (row-by-row re-narration) — SAFE TO CUT

Line 137 carries **zero inline `[^N]` markers**. Body markers stop at l.169 (`[^423]`); References begin l.182. The audio blockquote (l.122) and the table (l.124-135) — both KEPT — also carry no inline markers; the ten record fights are cited in chapters 1-10, not re-cited here. The `[^409-423]` range the budget flagged sits in this chapter's opening case work (l.14-169), all upstream of and outside the cut. **No definition orphaned. No marker to preserve.** Compress l.137 to two sentences as specced.

# Why all three cleared

These chapters use prose-first, narration-only citation: footnotes attach once to the originating scene/case paragraph; the later scoreboard/re-walk prose restates without re-citing. The cuts target exactly that uncited restatement. No `[^N]` definition loses its sole anchor.

Evidence grade: A (deterministic — full marker grep + References-block boundary confirmed per chapter; not a judgment call).
Assumptions: Wayne cuts only the exact text Bonnie quoted; if a cut widens upstream into the cited scene paragraphs, re-run this check on the new boundary.
Open questions: none on footnote integrity.
Risks: only if execution drifts above the specced cut boundary into cited prose. Flag to me if so.

Handoff: wayne-narrative-lead — all three cuts (ch-3, ch-6, ch-12) are footnote-safe to execute as specced; no markers to preserve or relocate. laura-red-team-editor holds the D4 taxonomy-coherence guardrail on the same cuts.

# Fiction-craft applied to *No One Did It* — what's leverage, what's poison

> **Status:** strategic analysis, not a decision. Drafted 2026-05-27 in response to the question: *"If you were to use storytelling/twisting skills to rewrite every chapter — fiction style for serious nonfiction — how would you do that?"*
>
> **Author:** Claude (Opus 4.7) — pre-pilot scoping note.
>
> **Audience:** xaiolai (principal author), jerry-crew-chief, wayne-narrative-lead, bonnie-book-architect, nancy-legal-risk-counsel, blair-market-strategist.
>
> **Decision needed before action:** whether to run the Phase 1 pilot described at the bottom. No chapter prose changes until that decision lands.
>
> **Companion note:** [`fiction-craft-rewrite-machinery.md`](./fiction-craft-rewrite-machinery.md) specifies the contract/registry/audit apparatus that would back the pilot if it runs.
>
> **Active workflow:** [`book/plans/fiction-craft-rewrite-workflow.md`](../book/plans/fiction-craft-rewrite-workflow.md) is the operational document the principal author authorizes against. This analysis note is the design history; the workflow note is the live governance.

---

## Frame

The book already has a serious storytelling spine — A2B recognition-reversal, the 10-beat chapter rhythm, mirror artifacts, paired scenes, master metaphor field. So the real question isn't "add storytelling." It's: **which further moves from fiction-craft survive this book's evidence regime, and which would actively rot it?**

The toolkit splits into three buckets.

---

## Bucket 1 — Craft moves that genuinely strengthen this book

These are moves used in serious literary nonfiction (Krakauer, Caro, Carr, Larson, Coll) that stay inside the project's hard rules (no invented interiority; no gotcha reveals; evidence grades intact; defamation wording preserved).

1. **Document-as-protagonist.** One artifact per chapter — a FOIA file, a serial number, a memo, a body, a procurement code — traced as a moving object through hands. Each hand is a structural chance for responsibility to settle and not. This is the existing "mirror artifact" device pushed harder.

2. **Two-track time.** Braid the original event with the record-building (or record-suppressing) work happening in archives, courts, FOIA queues, inquests. The reader watches the laundering happen *and* watches the counter-forensics. Beat 9 ("the escape") naturally lives in track two.

3. **Focalize on the goat in beats 1–2, break frame at beat 3.** The reader feels the scapegoating before they see the chain. Fair-clue discipline holds because the epigraph or chapter title signals: "you are about to be misled the same way the public was."

4. **Delayed naming — but only upward.** Name the visible goat early (legal hygiene + fairness). Withhold the chain's names until their structural role is visible. Calley on page one; "the office that authorized the operation, two echelons above" until the recognition beat reveals who.

5. **Voice braid with explicit textures.** Three registers per chapter — primary document quoted at full force; newsroom-frame paraphrase; analytical voice. Different paragraph treatments so the reader registers the shift consciously. This is what serious narrative nonfiction does instead of inventing scenes.

6. **The reversal beat earns its sentence.** Treat the recognition the way fiction treats a scene's turn — one short hammer line after the longest analytical paragraph. The style rule ("short reversal sentence after complex explanation") already permits this; craft-wise, *commit harder*.

7. **The resonant return.** Beat 10 currently says "what this might mean for us." Add a one-paragraph coda: the opening scene/object re-read through the chapter's diagnostic. A2B already calls for "final re-reading" — fiction calls it the resonant return. The reader sees the artifact differently. Same move.

8. **One image, never two.** Already a rule, but craft-relevant: fiction writers know one image carries a chapter; two compete. The metaphor-discipline rule and the "one major device per chapter" rule are the right gate.

---

## Bucket 2 — Craft moves that would damage this book specifically

Naming these explicitly so we don't drift into them.

1. **Invented interiority.** The most powerful fiction tool — telling the reader what a character thinks — is off the table (`AGENTS.md`: no invented motives or thoughts; style guide: no invented psychology). What's left is observable behavior, documented statements, and structurally inferred position. Do not try to smuggle interiority back in via free indirect style.

2. **Aggressive withholding for surprise.** Fiction reveals; this book *re-reads*. Engine rule (10-a2b-engine-v2.md) forbids "hidden information required for the payoff" and "gotcha reveals." Any craft move that requires the reader not to have access to a fact at beat 3 — when they could have had it — is the wrong move.

3. **Sympathetic focalization on the wrong actor for too long.** Fiction craft makes you feel for the POV character. If the POV is the visible scapegoat for the *whole* chapter, the reader's sympathy lands on the goat and the chain disappears into background. That's the laundering pattern weaponized against the book's own argument. The fix is the beat-3 frame break in Bucket 1 #3; focalize the goat for the felt accusation, then *leave them* to follow the chain.

4. **False symmetry via balanced characterization.** Fiction loves the morally interesting antagonist. The taxonomy rule (`01-case-taxonomy.md`) forbids treating complexity as automatic guilt or weakness as automatic innocence. Do not add narrative texture to a chain actor that the documented record doesn't warrant.

---

## Bucket 3 — Open questions before committing

Three answers needed before touching ch-01:

- **Positioning.** Does pushing toward literary nonfiction shift the book's comp set (Caro/Coll/Larson territory) versus its current diagnostic-serious-trade position (Snyder/Applebaum/Christian)? That's a `blair-market-strategist` / proposal-pack question, not a Wayne question. The market frame and the craft frame have to agree before the rewrite starts.

- **Date-fired clocks.** Nancy's 30-day re-passes (2026-06-24 ch-02 Ukrainian children; 2026-06-25 ch-08 Iraq WMD, ch-09 live political content, ch-10 live AI litigation, ch-12 FRA/DOGE/live records litigation) restart if the prose changes around the cited subjects. Focalization and delayed-naming choices are exactly the kind of changes that re-open defamation surface.

- **Audit gate fit.** `evidence-audit`, `fair-clue-audit`, `defamation-wording`, and `audit-chapter` were tuned to the current prose style. A craft rewrite will trigger novel failure modes — e.g., a delayed-naming choice flagged as "unsupported attribution" by `scan-overclaim.py` because the cite arrives later in the paragraph than the verb. Expect to refine audits, not just chapters.

---

## How to run it — sequential, gated, with a kill switch

Not "rewrite all 13."

**Phase 0 — Inventory (no edits).** For each of the 13 chapters: name its central artifact, current focalizer, location of the reversal beat, what's withheld, where the fair clue plants it. One-page audit per chapter. Surfaces which chapters already do the craft moves implicitly and which would need real surgery. Owner: `bonnie-book-architect` + `wayne-narrative-lead`, consolidated by `jerry-crew-chief`.

**Phase 1 — One pilot.** Pick the chapter where the gap between current draft and craft-augmented version is largest **and** whose evidence is most A-grade-stable (so craft change is not entangled with evidence change). Rewrite. Run the full audit chain (`/audit-chapter`, `/evidence-audit`, `/fair-clue-audit`, defamation wording, Nancy review). Compare reader-state movement before vs after. Get xaiolai's read.

**Phase 2 — Decision gate.** If the pilot is genuinely stronger AND all gates pass AND positioning is still serious trade nonfiction → proceed. If it strengthens prose but weakens any of: evidence grade, fair-clue compliance, defamation wording, positioning → pull back to surgical adoption (e.g., adopt Bucket 1 #1, #5, #6, #7 only; skip #3, #4).

**Phase 3 — Rollout, one chapter per cycle.** Each chapter goes through the same per-chapter pipeline as original production did, plus a new "craft-vs-evidence" check. Re-auditing the date-fired Nancy clocks budgeted in.

---

## Honest cost picture

This is structural revision, not prose polish. Realistic estimate: each chapter is on the order of the original chapter-production cost, not a fraction of it — because focalization changes propagate through scene order, attribution chains, citation placement, and audit re-runs.

For 13 chapters at `status: ready`, this is roughly a re-production cycle, with additional risk that:

- Nancy's clocks reset on the four live-content chapters.
- The proposal pack has to re-comp (positioning shift from "diagnostic serious trade" toward "narrative nonfiction with diagnostic frame").
- Audit skills themselves need refinement to handle the new prose shapes.

---

## The question to answer before starting

**What is the reader experience the current 13 chapters are missing that craft-augmentation specifically fixes?**

- If the answer is *"they read as analytical when I want them to read as inevitable"* → that is a real structural defect worth this cost. Run the pilot.
- If the answer is *"I want them to be more gripping"* → the cheaper move is a polish pass applying Bucket 1 items #5 (voice braid), #6 (reversal beat), #7 (resonant return), and #8 (one image) inside the existing chapter architecture. Ship as planned.

The two answers point to two different projects. The decision is xaiolai's.

---

## Handoff

- **Owner of this note:** `jerry-crew-chief` (route to architecture vs prose vs market depending on Phase 0 outcome).
- **Purpose:** scoping document for a potential craft-rewrite cycle on the 13 ready chapters.
- **Evidence grade:** N/A — methodological proposal, not a factual claim.
- **Assumptions:** the 10-beat rhythm and A2B engine remain governing; no rule under `.claude/rules/` is being proposed for change.
- **Open questions:** the three in Bucket 3, plus the binary at the bottom.
- **Handoff:** xaiolai for the binary decision; if yes, `jerry-crew-chief` to dispatch Phase 0 inventory across `bonnie-book-architect` and `wayne-narrative-lead`.

---
public_release: mechanical-pass-cleared
public_release_date: 2026-05-31
---
Owner: Bonnie / Book Architect / Developmental Editor

Task: Execute the three structural moves authorized by xiaolai's recognition-repetition decision (2026-05-28) and the principal's two confirmed calls. Edit v2 authoring source only; land before Wayne's prose pass.

Inputs reviewed:
- `book/review-memos/xiaolai-recognition-repetition-decision-2026-05-28.md` (Disposition 1 PARTIAL, Disposition 2 PARTIAL; surfaced-item dispositions).
- `book/reader-reports/_TRIAGE-2026-05-28.md` (Class B, C, E).
- `book/reader-reports/02-the-four-goats-2026-05-28.md` (H1 install-order / promise mismatch).
- `book/reader-reports/04-the-proxy-and-the-sponsor-2026-05-28.md` (H2 delivered-not-earned second recognition + S1.5→S2 leak).
- `book/chapters-v2/02-the-four-goats.md`, `book/chapters-v2/04-the-proxy-and-the-sponsor.md`, `book/chapters-v2/13-a-readers-field-guide.md`.

Treatment class (per rule 08): **structural-polish** for ch-2 (block-internal connective-tissue edits, no scene reorder, no contract file). Ch-4 is unchanged by me — see Move 2; Wayne's demotion classes it `prose-polish`. The pre-edit snapshot hook archived ch-2 at `book/audits/history/02/2026-05-28T09-48-44Z` and `.../2026-05-28T09-49-00Z`; rollback unit is intact, so I did not block on the full structural-polish apparatus per the dispatch.

---

## Output

### MOVE 1 — ch-2 category-ordering (Class E / report H1) — DONE

**Decision: option (b) — align the opening expectation to the chapter's delayed-reveal structure. Rejected option (a).**

Reasoning. The reader's disorientation was an *expectation mismatch*, not a structural defect in the reveal order. The report is explicit that each category label, when it arrived at the end of its case, "felt earned by the case I'd just read" (report line 65) — the operator→machine→bug migration made "system/object alibi" click; the Sacco-Vanzetti record made "pure scapegoat" click. Front-loading the four names (option a) would have spoiled exactly the earn-it-before-you-name-it design that is working. The defect was that line 30 over-promised — "these are the pages that name them... Recognizing which shape is in front of us is the first move" set the reader up to expect the names up front. Option (b) preserves the recognition arc and removes the false promise. This also protects rule-12 V4 (reader does the work) and V5 (capacity change on the four-category instrument), which option (a) would have regressed.

Two surgical connective-tissue edits:

1. **Opening promise (was line 30).** Changed "The pattern has four shapes, and these are the pages that name them" to "The pattern has four shapes, and we name each one at the case that teaches it, because a shape is easier to hold once we have watched it operate." Appended to the closing sentence: "...and the four cases that follow earn the four names in turn." The promise now tells the reader the names arrive *at* each case, not up front — matching what the chapter does.

2. **Install-order meta-statement (was line 64, top of the Sacco/Vanzetti transition).** The report named this as the line that "made the disorientation worse, not better, because it asked me to track an ordering principle I couldn't yet see the shape of." Changed "The system/object alibi is the least intuitive of the four categories, which is why we have installed it first" to "The system/object alibi we have just watched operate is the least intuitive of the four shapes." The useful orienting contrast (least-intuitive vs. oldest-and-easiest-to-feel) is preserved; the leaked architectural rationale ("which is why we have installed it first" — a build-order coordinate the reader cannot yet verify) is removed. Also dropped "category" → "shape" in the two following sentences for register consistency with edit 1.

Both edits passed all six warn-mode scanners (cite-density, overclaim, pronoun-discipline, implication, operating, status-check). No cite-anchors moved; sidecar `as_of` does not need a content-anchor bump (no anchor add/remove/relocate), but the ch-2 sidecar's `as_of` should be advanced to 2026-05-28 at promotion time per rule 09 since chapter content changed — flag for Jerry at re-promotion, not blocking now.

Residual for Wayne (NOT mine): report S1 flagged "as the next beat will show" (chapter lines 49 and 123 pre-edit) as a backstage-instruction leak. That is sentence-level prose, Wayne's call. I did not touch it.

### MOVE 2 — ch-4 matrix reorder (Class B sub-finding / report H2) — DEFER TO WAYNE (no clean structural move; would create a new orientation break)

I verified the surrogate's open question (decision memo OQ-a: "is the matrix-before-announcement reorder a clean structural move, or does the matrix depend on the line-131 setup for orientation?"). It is **not** a clean structural move. Determination and reasoning:

1. **The premature announcement and the matrix are two beats apart, not adjacent.** The report's "line 131" is a v3 line number; in the v2 authoring source the premature announcement of the *second* recognition sits at the END of the **Alibi weakens** beat (v2 "Paying attention to *both* sides of that asymmetry surfaces the second recognition. The proxy-deniability arrangement is a single method. The institutions facing it are also a method..."). The seven-channel matrix sits in the **The escape** beat (beat 9). Between them sits the entire **Anti-laundering rule** beat (the three proxy questions, beat 8). The pre-tell is separated from the matrix by a full rhythm beat.

2. **The matrix is self-orienting; it does not depend on the announcement.** Beat 9's own intro ("the second architecture is as multi-channel as the first... Lay them side by side. Read the matrix one channel at a time.") sets the matrix up independently. The matrix does not need the Alibi-weakens announcement for orientation.

3. **Therefore the matrix is already in the right place** — it precedes the load-bearing recognition statement ("This is the recognition. The proxy-deniability arrangement is one method, and the institutions that can intercept it are several methods...") within beat 9. The reader CAN earn the recognition from the matrix; the problem is that the recognition was *also* pre-announced two beats earlier.

4. **The fix is to demote the premature announcement, not to move the matrix.** Moving the matrix earlier (into the Alibi-weakens beat) would pull "the escape" content out of beat 9, leaving beat 9 hollow and creating a NEW orientation break — exactly the failure mode the dispatch told me not to force. The correct fix is sentence-level: demote/fold the premature "surfaces the second recognition / the institutions facing it are also a method" announcement at the end of Alibi-weakens so the recognition lands only after the matrix. That is prose work, and the decision memo already routes it to Wayne ("Cut or demote the free-standing labeling sentence, not the insight... Move the announcement after the evidence, never before it").

**I made no edit to ch-4.** The two recognition-delivery sentences ("This is the recognition", beat 9) and the leaked build-stage label ("That is the second move from S1.5 to S2... The first move, in chapter 3...", beat 9) are also Wayne's prose cuts per the decision memo's Disposition 1 and Class A-residual routing. None of these is a structural reorder.

Net: ch-4's Class B sub-finding is resolved entirely in prose by Wayne. No structural movement is available that improves on the prose demotion, and forcing one regresses orientation. Logged here so Wayne does not later try to rebuild rhythm around a matrix I might have moved.

### MOVE 3 — back-of-book eight-question reference card (Class C support) — ALREADY SERVED BY CH-13. No new artifact needed.

Determination: **YES, ch-13 Artefact 1 already is the portable reference card.** Ch-13 ("A Reader's Field Guide") is the field guide, and its **Artefact 1 — The eight questions** is a standalone, self-contained reference card by construction:

- It is a blockquote artefact, set off from prose, designed (per the chapter's own framing) to be "photocopied, folded, and carried."
- The eight questions are reproduced **byte-exact** and **verbatim from the project source-of-truth file** (the chapter's record-hardens beat asserts this and the question text matches `AGENTS.md` core diagnostic and the field-guide draft).
- It carries a "How to use them" note and a chapter-3 tether (the worked example), so it travels with its discipline rather than as a bare checklist.
- It already sits in back-matter position (Part IV, chapter 13, the consolidation pass), which is precisely where a back-of-book reference card belongs.

The principal's GO on a reference card is therefore satisfied by an artefact that already exists, is already verified, and is already gate-passed. Adding a *second* eight-question card elsewhere in the back-matter would duplicate it and risk byte-drift between two copies — a self-inflicted quote-integrity hazard for the book's own instrument.

**What this enables for the Class C compression (for Wayne).** Because the full, carryable eight-question card lives in ch-13 Artefact 1, the in-chapter diagnostic walks in earlier chapters can compress by *pointing to it* rather than re-printing the full list. The decision memo's Disposition 2 prescribes exactly this ("install once in full, reference thereafter"). Concretely, when Wayne compresses a later-chapter walk to a referenced subset, the cross-reference target is the field guide — phrasing on the order of "the full eight questions are collected in the field guide; here the [record-control] question does the new work." This keeps one canonical full card (ch-13) and lets chs 6/8 and any other full re-walk run only the two-to-three questions doing new work in that case.

Note the one in-chapter full reprint the decision memo flagged for cutting — ch-3's third reprint of the full list ("in the form a reader can carry away") — is now redundant precisely *because* ch-13 Artefact 1 is the carry-away card. That cut is Disposition-2 work routed to Bonnie in the decision memo's handoff; it is a separate ch-3 move, not part of this pass, and I have not touched ch-3 here. Flagging it as the natural next structural cut now that the reference-card determination is settled.

---

Evidence grade: A
(Not applicable to the structural moves themselves — architecture, not factual claims. The grade reflects the underlying chapters, which carry A; no claim was added, removed, or re-graded by this pass. The reader-experience findings driving the moves are lived-experience data — the reader is never wrong about its own experience — grade-exempt per rule 15.)

Assumptions:
- The book is read linearly front-to-back (the decision memo's load-bearing assumption; if the principal later adopts a chapter-dippable posture, Move 3's "point to the field guide" compression weakens and should be re-decided — but the card itself stays valid either way).
- Ch-13 Artefact 1's eight-question text is byte-exact to the project file; I read it as matching but Stephen owns the verbatim-consistency lock (already in ch-13's handoff chain).
- My ch-2 edits are connective-tissue only; the recognition arc and all four case reveals are unchanged in order and content.

Open questions:
1. Ch-2 sidecar `as_of` advance to 2026-05-28 at re-promotion (rule 09). **Instinct:** trivial; no anchor moved, so only the date bumps. **Owner:** Jerry at re-promotion / `post-edit-status-check`.
2. Does ch-3's third full-list reprint get cut now that ch-13 Artefact 1 is confirmed as the carry-away card? **Instinct:** yes, cut it (Disposition 2 prescribes it; the reprint is redundant inside the installation chapter). **Owner:** Bonnie, as a separate Disposition-2 structural pass — not this pass.
3. Whether the Class C "point to the field guide" cross-references should name "chapter 13" or "the field guide" in prose. **Instinct:** "the field guide" (the artefact is named, not the chapter number — survives any future renumber). **Owner:** Wayne, during the compression pass.

Risks:
- **Ch-2 re-read risk (structural-polish standard).** My promise-alignment edit changes the reader's expectation contract for the first third of the chapter. It must be re-read cold before v3 promotion to confirm H1 actually lifts and no new orientation break was introduced. Guard: the-reader re-reads ch-2 after v3 rebuild.
- **Move 2 mis-handoff risk.** If Wayne reads "matrix reorder" as a structural instruction and waits on me, ch-4 stalls. Guard: this memo states plainly that ch-4 needs no structural move and the fix is entirely Wayne's prose demotion of the premature announcement.
- **Move 3 duplication risk if not heeded.** If anyone adds a second eight-question card to back-matter, the book acquires two copies of its own instrument that can drift. Guard: this memo records that ch-13 Artefact 1 is the single canonical card.

Handoff:
- **To Wayne (next owner):** (a) ch-4 — demote the premature second-recognition announcement at the end of the Alibi-weakens beat so the recognition lands only after the seven-channel matrix; cut the two "This is the recognition" labels and the "S1.5 to S2 / the first move in chapter 3" leaked build-stage label in beat 9 (Disposition 1 + Class A-residual). No matrix movement — it is already correctly placed. (b) Class C compression in later-chapter walks (chs 6/8 and any other full re-walk): compress by pointing to the field guide's eight-question card ("the full eight questions are collected in the field guide") and running only the questions that do new work in that case. (c) ch-2 residual: "as the next beat will show" backstage-instruction leak (report S1), Wayne's prose call.
- **To Jerry:** advance ch-2 sidecar `as_of` to 2026-05-28 at re-promotion; after Wayne's prose pass lands, rebuild v3 and dispatch the-reader re-read of ch-2 and ch-4 (rule 15 gate; both currently BLOCKED until clean re-read or xiaolai override).
- **To Bonnie (me, separate pass):** ch-3 third-reprint cut (Disposition 2), now that ch-13 Artefact 1 is confirmed as the carry-away card — separate structural pass, not this one.

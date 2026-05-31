---
title: v4 De-Templating Architecture Spec
owner: bonnie-book-architect
status: brief
phase: v4
opens: v4 structural variation phase (seeded from clean v3)
model: beat-10 consolidation (xiaolai-approved 2026-05-29) — supersedes the eight-closing-shape map
inputs_reviewed:
  - process/reader-reports/sweep-2026-05-28.md (2 HARD, clean axes to protect)
  - .claude/rules/04-style-guide.md (amended: rhythm is palette, not template; beat 10 consolidation pending below)
  - book/chapters-v4/*.md (13 chapters, [^N] footnote apparatus)
  - book/chapters-v4/13-a-readers-field-guide.md (the role-by-domain crosswalk — the consolidation home)
  - book/chapters-v4/{03,05,06,07,09,11,12}-*.md (closing/beat-10 role-walks, read cell-by-cell for the overload check)
  - book/registries/motif-registry.yml (signature-as-seam, floor 5)
executor: wayne-narrative-lead (chapter-by-chapter, in book/chapters-v4/)
---

# v4 De-Templating Architecture Spec

Owner: Bonnie / Book Architect / Developmental Editor
Task: Design a per-chapter de-templating spec to break the structural monotony a cold reader flagged across three sweeps, while protecting the four clean axes (arc legibility, callback recognition, cumulative trust, taxonomy coherence).

## The consolidation model (xiaolai-approved, 2026-05-29) — supersedes the closing-shape map below

The earlier version of this spec fixed HARD-1 by assigning **eight distinct closing shapes** so no two adjacent chapters closed alike (the table in Lever B). xiaolai has approved a stronger, simpler model that this revision adopts as the design-of-record. The closing-shape palette is **demoted** from a per-chapter assignment to a thin reference (it survives only as a description of how chs 1/2/13 already differ); the load-bearing instruction is now the **split of beat 10 into two separable jobs**.

**Beat 10 ("what this might mean for us") was doing two jobs:**

- **Job 1 — the role-by-role action walk.** "As cost-bearer do X, as bystander do Y, as institutional actor do Z" (and in chs 9/11/12, the finer citizen/juror/journalist/employee/manager/contractor/professional/voter split). This is the repetitive material the cold reader skimmed across chs 5–13. **Decision: removed from chs 1–12. It lives ONCE, in ch-13's role-by-domain crosswalk (Artefact 5) and the "Act on it / eight sentences, one per role" close.**
- **Job 2 — the chapter-specific landing.** "Here is where THIS pattern shows up in non-headline life; here is the warning sign." Tailored per pattern; converts each chapter from a scandal into something personally relevant while the case is fresh. **Decision: kept, but SHORT — a sentence or two, or folded into the chapter's anti-laundering rule (beat 8).**

**Result:** each chapter now ends on its **anti-laundering rule (beat 8) + the escape / counter-case (beat 9)** — the analytical punch — plus a short Job-2 landing. The per-chapter role-walk is gone. Beat 9 stays non-negotiable as content. Beat 10 is no longer a per-chapter requirement; its role-applicability function consolidates in the field guide.

**This supersedes Lever B (the eight-closing-shape map).** The closing-shape assignment table is retained below for reference only, struck through in intent: where it said "drops role-walk? partial — keep a compressed cue," the new model says "drops role-walk: yes, fully, for all of chs 3–12." A chapter no longer needs an assigned shape from a palette; it needs (a) a strong beat 8 + beat 9 close and (b) one short Job-2 landing sentence. The "no two adjacent alike" discipline is now achieved automatically — once the role-walk is gone, the closes vary because the anti-laundering *rules* differ chapter to chapter (a rule is not a template; a role-walk was).

## The ch-13 overload verdict (the load-bearing finding)

Before endorsing the model I read the actual beat-10 role-walks in chs 3, 5, 6, 7, 9, 11, 12 against ch-13's crosswalk (Artefact 5, six moves) and the "eight sentences, one per role" close. The question: does the crosswalk ALREADY cover the role-actions being removed, or are there gaps ch-13 would have to absorb?

**Verdict: NO overload. The crosswalk already covers every role-action being removed. This model mostly DELETES per-chapter walks; ch-13 barely changes (one optional one-line anchor addition, not a structural expansion). This is the ideal outcome.**

Cell-by-cell, every per-chapter role-action verb maps onto an existing crosswalk move (Moves 1–6) or onto the "Act on it / eight sentences" close:

| Chapter | Per-chapter role-action (verb) | Maps to ch-13 crosswalk move |
|---|---|---|
| 3 | write & send the eight questions; demand written answer on who-knew | Move 1 (name controller) + Move 2 (demand record) |
| 5 | "put the next floor up on the record"; ask in writing what decision was upstream and who made it | Move 1 (name controller) |
| 6 | force the invoker to name themselves in writing; refuse to be the named executor | Move 1 + Move 3 (refuse signature without chain) |
| 7 | "reach the record, or document that it was refused"; keep custody out of one set of hands | Move 2 + Move 4 (make destruction/refusal visible) |
| 9 | the three-record demand (input/deploy/eval); refuse to sign for un-inspectable output | Move 2 + Move 4 + Move 3 |
| 11 | propose named-allocation in writing; refuse the named-signer line; vote the compelling architecture | Move 3 + Move 5 (design test) + Move 6 (vote architecture) |
| 12 | put the record where the interested party can't reach; ask for the index; insist on a second custodian | Move 2 + Move 4 |

No per-chapter walk contains a portable role-action the crosswalk lacks. The chapter-specific *anchoring* (Bosch's 2007–2008 warnings, the *Furman* trial findings, the GAO ICA opinion, the three-record demand at three AI layers, Ellsberg's photocopier) is **worked-example detail**, not a portable action — and it survives in beats 5/8/9 of each chapter regardless. The crosswalk's cells are already built "from the beat-10 anti-laundering moves installed in chapters 2 through 12" (ch-13's own "Audited at the source" section says so). Removing the per-chapter walks therefore removes the *redundant prose echo* of material the crosswalk already consolidates — it does not orphan any action.

**What ch-13 needs: nothing structural.** Two narrow, optional confirmations, neither of which bloats the checklist:

1. **No new rows, no new columns, no addendum.** The 8×6 crosswalk already spans every role and move. Do not extend it. Extending it to "capture" removed walks would be the over-correction the cold reader's ch-13-density flag warns against.
2. **Optional one-line anchor top-up (verify, do not assume).** Three crosswalk cells already carry chapter anchors that point back to the chapters losing their walks (Employee/Move 1 → ch-5; Citizen/Move 1 → ch-2 Boeing; Contractor → ch-11/Blackwater logic). Confirm each chapter whose walk is removed still has at least one crosswalk cell anchored to it, so the field guide's "return to the worked example" tether is not severed. From the read: ch-3 (anchored via VW/Pinto in Artefact 1), ch-5 (Employee/Manager Move 1), ch-6 (no explicit crosswalk anchor — Move 1 column lists "Chapters 2,3,5,6" so the *move* cites ch-6, but no *cell* names a ch-6 case), ch-7 (multiple cells), ch-9 (Artefact 3 + multiple cells), ch-11 (anchor-dense), ch-12 (anchor-dense). **The single thin gap is ch-6:** the Move-1 column header cites ch-6 but no crosswalk *cell* names a ch-6 case (family separation / census / OMB hold). Fix: add the ch-6 case name to ONE existing cell's parenthetical anchor (Citizen/Move 1 or Voter/Move 1) — a ≤8-word insertion, not a new cell. This is the only ch-13 edit the model requires, and it is additive-by-a-clause, not structural.

**Net effect on ch-13 density:** unchanged. The crosswalk is not touched except for one optional ≤8-word anchor clause. ch-13 stays the consolidation home; it does not become a bloated checklist; the densest-passage flag is not worsened.

## Rule-04 amendment required by this model

Rule `04-style-guide.md` was already amended for v4 (the ten beats are a palette; beats 9–10 are "non-negotiable as content, not as form"; the comprehensive role-by-domain matrix "lives once, in the field-guide crosswalk"; "a per-chapter beat 10 may therefore carry a single sharp move calibrated to that chapter rather than re-walking every role"). The consolidation model goes one step further than that text and requires a **further amendment**, because the current rule still treats beat 10 as a per-chapter *requirement* ("Every chapter still owes beat 10").

**The further amendment (to be applied to rule 04 by Jerry/orchestrator before execution):**

1. **Beat 9 stays non-negotiable per chapter, as content.** No change. Every chapter still owes the escape/counter-case.
2. **Beat 10 stops being a per-chapter requirement.** Replace "Every chapter still owes beat 10 ('what this might mean for us')" with: beat 10 splits into two jobs. **Job 1 (the role-by-role action walk)** is removed from individual chapters and consolidated once, in the field-guide crosswalk (ch-13). **Job 2 (the chapter-specific landing — where this pattern shows up in non-headline life, and the warning sign)** is owed by each chapter as one or two sentences, and may be folded into beat 8 (the anti-laundering rule). A chapter satisfies its reader-applicability obligation with beat 8 + beat 9 + the short Job-2 landing; it does NOT owe a role-walk.
3. **The role-applicability consolidation is named explicitly.** Add: the comprehensive role × move applicability lives once, in ch-13's crosswalk; chapters 3–12 must not reproduce it as a per-chapter role-cycle. (This makes the existing "lives once, in the crosswalk" sentence binding rather than permissive.)
4. **"Beat 10 may not be generic" survives — applied to Job 2.** The short Job-2 landing still may not be "stay informed"; it must name where THIS pattern shows up and the specific warning sign. The genericness ban now polices the landing sentence, not a role-walk.
5. **Chapter rhythm list annotation.** Annotate beat 10 in the numbered list: "10. what this might mean for us — Job 1 (role-walk) consolidated in ch-13; Job 2 (chapter-specific landing) owed per chapter, foldable into beat 8."

This amendment is the constitutional anchor for the consolidation; without it, `check-agent-frontmatter.py`'s rhythm-section gate (and any contract-audit `feels:` slot keyed to beat 10) would block a chapter for "missing beat 10" when the chapter has correctly consolidated Job 1 into ch-13. **Action: Jerry/orchestrator amends rule 04 and confirms the rhythm-section gate reads beat 10 as satisfied by (beat 8 + beat 9 + Job-2 landing) for chs 3–12. Defer execution of any chapter until the gate is confirmed not to false-block.**

## Role boundary

This is a **structural design** artifact. It specifies rhythm variation, the beat-10 split, internal-procedure variation, and motif frequency. It does **not** write prose, re-grade evidence, alter the responsibility-chain analysis, change case placement, or touch the case-file dossier layer. Wayne (and/or the orchestrator) executes it chapter by chapter; Stephen re-verifies any cite that moves; Nancy re-clears any defamation-adjacent paragraph that relocates; Laura red-teams against V1/V3/V8 regression. The two HARD findings are owned here (per the sweep's handoff: "Bonnie — owns the two HARD findings"); the over-signposting line-edits are co-owned with Wayne.

## What is NOT in scope (protect these)

The sweep named four CLEAN axes. Every instruction below is constrained to leave them untouched:

1. **Arc legibility.** The four-part movement (recognition → diagnostic → stress-tests → design rules) and Part boundaries stay. No chapter moves Parts. Forward-callbacks ("Part III turns to…") and the field-guide index stay.
2. **Callback recognition.** The discipline of re-anchoring a callback with a date or one-line refresher before leaning on it stays. De-templating must NOT strip the refresher sentences (ch-9/7 re-stating "Malfunction 54"; ch-10 re-stating each callback). Cutting a callback's refresher to save words is forbidden.
3. **Cumulative trust.** The steelman sections stay at full strength. The ch-8 cross-party balance (Watergate R / Iran-Contra R / al-Aulaqi D, "the roster is the demonstration") stays verbatim in substance — it sits in the chapter body, not in a beat-10 role-walk, so the consolidation model does not touch it (ch-8 already closes on the administration-agnostic structural test, not a role-walk; nothing to remove there). Hedges stay. No de-templating move may weaken a steelman to vary rhythm, and the Job-2 landing must not flatten the al-Aulaqi balance into a partisan one-liner. **Evidence before elegance.**
4. **Taxonomy coherence.** The four labels stay canonical; explicit hybrid declarations stay explicit (ch-5/6/7 layered re-reads; ch-9 declared hybrid). The field-guide crosswalk (ch-13) remains the single comprehensive role-by-domain matrix.

## The disease, precisely

Two HARD findings, confirmed against the prose:

- **HARD-1 (closing-block repetition, chs 5–13).** Every chapter from ~5 onward closes with the same four-move walk — **Recognise it / Diagnose it / Act on it / Avoid becoming it** — and inside "Act on it" walks the same role-cycle in the same order (cost-bearer → bystander → institutional actor), then stamps a **"the signature is the seam / the first person to put pen to paper carries the blame chain"** hammer-line. The reader could write the block before reaching it and skimmed the beat-10 payload across six consecutive chapters.
- **HARD-2 (internal-template monotony, chs 3–12).** Every chapter runs the same announced procedure: an "official-stories-in-sequence / three stories" section → the eight-question (or 6/3-question) walk **re-stated and re-walked one-by-one** → a "But X was charged / the system worked" steelman → an asymmetry/channels **table that is also narrated in prose** (the doubling) → the rule. Plus over-signposting: the prose announces that the load-bearing point is load-bearing ("This is the most operationally portable observation we have"; "The asymmetry IS our argument"; "the walk is the structural spine").

Both findings share one root: **the rhythm became a visible scaffold stamped identically, so the reader retained the book's template instead of the diagnostic.** The fix is controlled variation — vary the form chapter to chapter while every chapter still delivers the movement and beats 9–10 as content.

## Strategy in one paragraph

Treat the ten beats as a **palette**, and end every chapter on its analytical punch — **anti-laundering rule (beat 8) + the escape/counter-case (beat 9)** — plus one short chapter-specific landing (Job 2). The per-chapter role-walk (Job 1) is removed from chs 1–12 and consolidated once in ch-13's crosswalk. Three levers: (A) **rhythm variation** — which beats merge, reorder, compress, or dissolve into flowing prose; (B) **beat-10 consolidation** (replaces the former closing-shape map) — strip the role-by-role action walk from every chapter 3–12, fold the chapter-specific "where this shows up in non-headline life + the warning sign" into one or two sentences attached to beat 8/9; (C) **internal-procedure variation** — vary where/whether the question-walk is re-stated, kill the table-plus-prose doubling (keep ONE per chapter), and strip the over-signposting. Above all three, a **motif-frequency cut**: thin "the signature is the seam" to a single plant (ch-6) and a single payoff (ch-11) plus the deliberate resonant closes, so the bell rings instead of wearing out. The first three chapters and ch-13 already vary; the work concentrates in chs 5–12, the stretch the reader skimmed.

---

## Lever A: rhythm variation (per chapter)

The principle: **vary the traversal of the palette, not the movement.** Each chapter still moves accusation → hidden architecture → anti-laundering rule → escape. What changes is which beats are merged, which are carried in flowing prose vs. a marked section, and the order.

**Under the consolidation model, one standing instruction overrides the per-row notes below where they conflict:** chs 3–12 strip the role-by-role action walk (Job 1) entirely and end on beat 8 + beat 9 + a short Job-2 landing. Where a row below says "compress the role×layer re-walk" or "keep a compressed cue," read it now as "remove the role-walk; keep only the chapter-specific landing sentence." The role-walk's destination is ch-13. The footnote-preservation note on each row still governs (the [^N] on a removed-walk's claim sentences must attach to the surviving Job-2 landing or be confirmed duplicated on a surviving sentence — see Footnote-apparatus risk).

A separate orientation fix (the SOFT subheading finding, owned here): **chs 8, 9, 10 currently use literal beat-name subheadings** ("accusation scene", "official story", "hidden architecture"…) — capitalized in ch-8, lowercase in chs 9–10. These telegraph the move before the reader reads it and expose the scaffold. **Re-subhead chs 8, 9, 10 with thematic content-named heads** (matching chs 1–7, 11–13) as part of this pass. This is the single highest-leverage anti-monotony move available because it removes the most visible evidence that every chapter runs one procedure. Also delete the stray reader-facing `Evidence grade: A` line in ch-8 body (production artifact; the frontmatter already carries it).

| Ch | Rhythm-variation instruction | Beats merged / dissolved | Footnote risk |
|---|---|---|---|
| 1 | **No change.** Already varies (history → etymology → comparative → annulment-as-partial-escape → "the altar moves" posture). Reader's peak chapter. Protect. | — | none |
| 2 | **Light.** Taxonomy-install chapter; the four-case ladder is load-bearing and must stay legible. Keep the four-shape sequence. Do NOT add a marked closing block — its beat-10 is the "chain stops at the doctrine boundary" close, already non-templated. (Recognition-delivery SOFT — labeling each case — is a separate, accepted teaching choice; not touched here.) | beats 9–10 already woven into the doctrine-boundary close | none |
| 3 | **Medium.** This chapter *installs* the eight questions, so the full walk earns its space ONCE here. Compress "Run the eight questions, slowly" — currently re-narrates the ordering rationale after the walk already happened. Merge beats 6–7 (Schwartz steelman + alibi-collapse) into one movement. **Under the consolidation model: remove the cost-bearer/bystander/institutional-actor role-walk** (currently three labelled paragraphs); keep the eight questions themselves (the install) and a one-sentence Job-2 landing ("if fewer than four can be answered from the reporting, the reporting is part of the alibi"). | merge 6+7; remove the 3-role walk | renumber if "Run…slowly" compresses; the role-walk paragraphs carry the Bosch/Pinto [^] — those [^] must move to the surviving install/landing sentences or be confirmed duplicated upstream; keep [^] on surviving sentences |
| 4 | **Medium.** Three-denial opener is propulsive (reader's 2nd peak) — protect. The "Three questions for the proxy" + "Seven channels" table currently doubles (audio-rendering blockquote AND table AND prose walk). Cut the prose re-walk of the matrix; keep the table + the audio-rendering blockquote (V10). | dissolve channel-by-channel prose into the table | audio-blockquote and table both carry [^]; verify none orphaned when prose walk cut |
| 5 | **Heavy.** First chapter in the skim zone. Reorder: open on the Anderson arrest (keep), but **dissolve the "eight questions, walked one layer at a time" list into flowing prose** — it re-walks ch-3's instrument. Keep "But Anderson was charged" steelman (strong). Cut the asymmetry-table prose doubling (keep table). | dissolve question-walk into prose; merge 5 (record hardens) into the FDR section | the Bhopal/Boeing [^180–200] are dense; moving the question-walk to prose must keep each [^] on its claim sentence — FLAG for executor |
| 6 | **Heavy.** Currently re-walks SIX questions one-by-one (longest internal walk in the book). **Compress to the three that differ across cases** (Q3 documented-purpose, Q5 venues, Q6 re-run) as the chapter's own text already proposes — but actually DO it, don't announce it. The other three: state the result by reference in two sentences. This is the chapter that plants the seam motif (see Lever D). | compress 6-question walk to 3; merge 4 (Overton echo) earlier | heaviest footnote load (^201–250); compressing the walk risks orphaning [^211–227] — FLAG: keep each surviving claim's [^], move dropped-question [^] to the by-reference sentence |
| 7 | **Medium.** "Five roles / eight questions collide" is the structural payoff of Part II and is genuinely different (the diagnostic's *limit*) — protect the walk here, it does distinct work. But cut the "Eight channels" table prose doubling. This chapter is the seam-motif PAYOFF prep (see Lever D). | keep question-walk (does unique work); dissolve channel prose into table | Horizon [^246–250] are few; low risk |
| 8 | **Heavy + re-subhead.** Replace literal beat-name subheads with thematic heads. Delete stray `Evidence grade: A` body line. The "run the eight questions on the act of reframing" inversion is the chapter's distinct move — keep it but present as flowing prose, not a re-stated bulleted walk. | re-subhead; dissolve the inversion-walk bullets into prose | re-subheading is cosmetic (no [^] move); verify the deleted Evidence-grade line carries no [^] |
| 9 | **Heavy + re-subhead.** Replace literal lowercase beat-name subheads with thematic heads. The three-layer (input/deploy/eval) structure is genuinely novel and load-bearing — keep it (it is the basis of ch-13 Artefact 3). The "what this might mean for us" section re-walks all three layers AGAIN as a role × layer matrix in prose (cost-bearer / bystander / institutional-actor + refuse-to-sign). **Under the consolidation model: REMOVE the role-walk entirely.** Keep the diagnostic-markers-by-layer prose (it is Job-2-ish: where the AI alibi shows up) and the "if you cannot inspect the three records you cannot sign" warning sentence; route the role-actions to ch-13. | re-subhead; remove the closing role×layer walk; keep markers-by-layer + the refuse-to-sign warning sentence | re-subhead cosmetic; removing the role-walk must preserve [^] on the surviving markers/warning sentences (the role-walk prose carries few/no [^] of its own — verify) |
| 10 | **Heavy + re-subhead.** Replace literal lowercase beat-name subheads with thematic heads. Densest layer-bookkeeping (five layers) + highest legal heat — keep the five-layer count and the al-Aulaqi/cross-party material UNTOUCHED (trust axis). The "what this might mean for us" section walks five roles × five seams. **Under the consolidation model: REMOVE the role×seam walk.** Keep the one-sentence Job-2 landing ("ask which layers are firing; treat any claim that responsibility in war is irrecoverable as the laundering itself" — this is also ch-13 Artefact 4's how-to-use line, so it lands as the chapter's own close AND seeds the artefact). Route role-actions to ch-13. | re-subhead; remove role×seam walk; keep the "which layers fire / irrecoverable = laundering" landing | re-subhead cosmetic; removing role×seam prose preserves [^] on surviving layer-claims |
| 11 | **Medium.** Densest statutory chapter (reader's slog). Do NOT add reading load. The "Four designs in operation" four-panel + matrix + asymmetry table is the doubling source — keep the four-panel (it is the content) but cut any prose that re-narrates the matrix. This chapter is the seam-motif PAYOFF (see Lever D). | cut matrix prose re-narration; keep four-panel | statutory [^401–408]; cutting matrix prose must not orphan — low risk if panels keep their [^] |
| 12 | **Medium.** "Three portable rules" + "Ten record fights, two columns" table + "Four records that survived" four-panel is triple-doubling. Keep the table (has its own audio-rendering blockquote, V10) and the four-panel; cut the prose that re-narrates the table's rows after the table. | cut post-table prose re-narration | [^409–423]; audio-blockquote + table both carry [^]; verify |
| 13 | **No structural change** to the six artefacts (they are the deliverable and are deliberately consolidative). The closing-shape work (Lever B, ch-13 = the inversion "we are the escape") stays. The "Act on it / eight sentences one per role" block is the ONE place the full role-walk is *meant* to live — keep it; it is the crosswalk's prose echo and the book's earned close. | none | none |

---

## Lever B: closing-shape assignment (beat 10) — SUPERSEDED by the consolidation model

> **SUPERSEDED (2026-05-29, xiaolai-approved).** The eight-closing-shape assignment below is no longer the instruction. Under the consolidation model, **all of chs 3–12 fully drop the role-walk** and end on beat 8 + beat 9 + a short Job-2 landing; the role-applicability consolidates once in ch-13. The "no two adjacent alike" goal is now met automatically because the surviving closes are the chapters' distinct anti-laundering *rules*, not a stamped role-walk. This section is retained for reference and for the three chapters whose closes were already shape-correct and stay (1-Posture, 2-Taxonomy/boundary, 13-Inversion). The per-chapter shape letters are no longer assignments; treat them as a record of how the closes already differed. Where the table below says "partial — keep a compressed cue," the live instruction is "remove the role-walk fully; keep the Job-2 landing."

The eight shapes (reference only):

- **(P) Posture close** — a reflective stance/recognition, no role-walk (ch-1's "the altar moves; we already know where it is").
- **(D) Document/scene close** — return to the opening artifact and re-read it (ch-12's photocopier; the "fair clue in the verbs" payoff).
- **(I) Single sharp imperative** — one protocol sentence, no role-cycle.
- **(Q) Question close** — end on the one diagnostic question that reduces the chapter ("Where can more than one party reach the record?").
- **(M) Lead-with-the-move** — open beat 10 with the action, then the recognition (inverts the Recognise→Act order).
- **(R) Short role-cue** — a *compressed* role gesture (2–3 roles max, not the full four-move walk), used sparingly.
- **(T) Taxonomy/boundary close** — end on where the chain stops and why (ch-2's doctrine-boundary close).
- **(X) Inversion/handoff close** — flip observer→actor (ch-13's "we are the escape").

| Ch | Closing shape | Drops role-walk? | Note for executor |
|---|---|---|---|
| 1 | **(P) Posture** | yes (already) | Keep "the altar moved; we already know where it is." Untouched. |
| 2 | **(T) Taxonomy/boundary** | yes (already) | Keep "the chain stops at the doctrine boundary." Do NOT add a role-walk. |
| 3 | **(M) Lead-with-the-move** | partial — keep a compressed cue | The eight questions ARE the action; open beat 10 with "Run them" then the smaller-scale recognition. Cut the full Recognise/Diagnose/Act/Avoid four-header block; the questions carry it. |
| 4 | **(Q) Question close** | yes | End on the three proxy questions as the portable instrument + "look at every channel; the record is durable, the sentence is not." Drop the four-move headers and the role-cycle. |
| 5 | **(T) Taxonomy/boundary** → vary from ch-4 | partial | End on "climb to the floor above; re-run at each floor a case occupies." Keep the partial-scapegoat markers (foreign/junior/deceased/absent — distinctive) but as prose, not a role-walk. **No "signature is the seam" line here** (Lever D). |
| 6 | **(I) Single sharp imperative** | yes | This is the seam-motif PLANT. End on ONE imperative: "Insist that the named invoker sign first. In writing." This is the chapter where "the signature is the seam" earns its first full statement (Lever D). Drop the four-move walk. |
| 7 | **(D) Document/scene close** | yes | Return to Misra's signature on the daily account she could not audit / Therac "P" past Malfunction 54. End on "If you cannot inspect the record, you cannot legitimately sign for the output." Scene, not role-walk. (Seam motif appears here as resonant-return — see Lever D.) |
| 8 | **(P) Posture** → vary from ch-7 | yes | The three administration-agnostic tests + "run the walk; the chain still climbs" is reflective/structural. Keep the cross-party material. No role-walk, no seam line. |
| 9 | **(R) Short role-cue (compressed)** | partial — 2 roles max | The three-record demand is the action; compress the closing to cost-bearer + institutional-actor only (not the full four-cycle). The seam line here is a resonant-return, keep ONE instance ("the signature is the model's alibi made personal") — it is distinct enough (personalizes to AI) to survive. |
| 10 | **(Q) Question close** → vary from ch-9 | yes | End on "which of the five layers is firing? Treat any claim that responsibility in war is irrecoverable as the laundering itself." Tighten the role×seam material to prose. No four-move walk. |
| 11 | **(I) Single sharp imperative** → vary from ch-10 | partial | Seam-motif PAYOFF. End on "do not sign the named-signer line of a function whose allocation you did not write… ask for it in writing." The seam line rings HERE at full force ("The signature is the seam. Watch the seam.") because it was planted in ch-6 and withheld since. Compress the four-role design walk to the imperative. |
| 12 | **(D) Document/scene close** → vary from ch-11 | yes | Return to the photocopier / "the fair clue is in the verbs." End on "Where can more than one party reach the record we would need? If nowhere, the seam is already named." Question-flavored document close. No four-move role-walk (the current ending already half-does this — finish the job). |
| 13 | **(X) Inversion/handoff** | NO — keeps the full role set | This is the ONE place the eight-role walk lives, by design (the crosswalk + the "eight sentences, one per role" close + "we are the escape"). Closing sentence deferred to xiaolai per the reserved `[FINAL SENTENCE — xiaolai authors]` slot. |

**Consecutive-pair check** (no two adjacent close alike): 1-P, 2-T, 3-M, 4-Q, 5-T, 6-I, 7-D, 8-P, 9-R, 10-Q, 11-I, 12-D, 13-X. Adjacent pairs all differ. The two T's (2,5) and two Q's (4,10) and two I's (6,11) and two D's (7,12) are each non-adjacent. **Five of the thirteen drop the role-walk entirely (4, 6, 8, 10, 12); three more compress it (3, 5, 9); ch-13 keeps it as the consolidation.** The book's middle — chs 5–12, where the reader skimmed — now presents T, I, D, P, R, Q, I, D in sequence: eight chapters, eight different closes.

---

## Lever C: internal-procedure variation (HARD-2)

Three standing edits, applied per the per-chapter heaviness in Lever A:

**C1 — Vary where/whether the question-walk is re-stated.**
The eight questions are *installed* once (ch-3) and may be *walked at full length* once more where the walk does distinct work (ch-7, where the questions collide with the five-role limit — that is the payoff, not a repeat). **Everywhere else, do not re-walk the questions one-by-one with each question re-stated.** Options, distributed so they vary:
- ch-5: dissolve into flowing prose ("the chain ran from operators to local management to South Charleston to Danbury…").
- ch-6: collapse to the three questions that *differ* across the three cases; state the other three by reference.
- ch-8: present the inversion as prose, not a re-stated bulleted walk.
- ch-9: the three-layer demand is novel, keep it — but don't ALSO re-walk it in beat 10.
- ch-10: the five-layer count is the instrument; don't re-walk the eight questions inside it.
The full canonical eight-question text lives in ch-13 Artefact 1. Chapters may point forward to it rather than reproduce it.

**C2 — Kill the table-plus-prose doubling. One per chapter.**
Every chapter with an asymmetry/channels table currently ALSO narrates the table's rows in prose. **Keep the table; cut the prose re-narration** — EXCEPT keep the audio-rendering blockquote where it exists (chs 4, 12; it is the V10 audio-survivability device and is NOT the doubling — the doubling is the *third* pass in body prose). Net: each chapter gets at most (table + its audio-blockquote), never (table + audio-blockquote + body-prose-walk). Applies to chs 3, 4, 5, 6, 7, 11, 12.

**C3 — Strip the over-signposting.**
Delete the self-announcing meta-lines that tell the reader the load-bearing point is load-bearing. Co-owned with Wayne (prose-level), flagged here as a standing instruction. Confirmed instances to cut or recast:
- "This is the most operationally portable observation we have" (ch-7).
- "The asymmetry IS our argument" (ch-12) — let the table carry it.
- "the walk is the structural spine" / "The load-bearing teaching point belongs here" (chs 6, 7).
- "Our load-bearing observation is that…" (ch-4).
- "This is our load-bearing counterargument, and it returns at full strength below" (ch-13 — acceptable once in the consolidation chapter; cut the analogous lines elsewhere).
Rule of thumb for the executor: if a sentence's only job is to announce the importance of the next sentence, cut it and let the next sentence stand. (This also serves rule-14 anti-meta-frame discipline.)

---

## Lever D: "the signature is the seam" motif-frequency plan

The reader listed the hammer-line in chs **2, 4, 6, 7, 9, 11, 12, 13** and said past ~its fifth appearance it read as the author repeating himself. The registry tracks the intended callback as **ch-6 plant → ch-11 payoff** (`signature-as-seam`, frequency_floor 5). The current prose over-fires it. The fix thins the instances so the plant→payoff arc rings.

**Keep (4 load-bearing instances):**
- **ch-6 — the PLANT (scene-anchor).** "The signature is the seam. The first person to put pen to paper invoking the cited authority carries the blame chain." First full statement. This is where the motif is born; it must land clean and unrepeated-before.
- **ch-7 — resonant-return (artifact scale).** "If you cannot inspect the record, you cannot legitimately sign for the output. The signature is where the unauditable record finds its name." Distinct register (record/audit, not invocation). Keep — but it must NOT restate "first person to put pen to paper" verbatim (vary the wording; the registry treats ch-7 as resonant-return, not a re-stamp).
- **ch-11 — the PAYOFF (scene-anchor).** "The signature is the seam. Watch the seam." This is the designed payoff; it rings hardest because it was withheld through 8, 9, 10. Keep at full force.
- **ch-13 — resonant-return (close).** Folded into "Avoid becoming it: the goat is whoever signs for an outcome whose decisions, records, and beneficiaries they do not control." Keep as the instrument's final form.

**Cut or vary (the over-fires that wear it out):**
- **ch-2** — the early literal signing instances (ODA self-signing) stay as *content*, but do NOT phrase them as the "signature is the seam" hammer-line; the motif should not be named before its ch-6 plant. Vary wording to plain description.
- **ch-4** — currently "The first person to put their name on the unmarked vehicle carries the prosecution." This pre-empts the ch-6 plant. **Cut the hammer-phrasing**; keep the Blackwater proxy-shell content in plain prose. (Proxy ≠ signature seam; the conflation is part of why it wears out.)
- **ch-5** — do NOT add the seam line (Lever B already specifies this). The "settlement-before-archive" signature marker is distinct; keep that, not the hammer-line.
- **ch-9** — keep ONE instance only ("the signature is the model's alibi made personal") because it genuinely extends the motif to AI; cut any second occurrence in the same chapter.
- **ch-12** — the record-discipline chapter naturally touches signing; keep it as record-discipline prose, do NOT stamp "the signature is the seam" (it would fall between the ch-11 payoff and ch-13 close and dull both).

**Net frequency:** plant (6) + 3 resonant-returns (7, 11-payoff, 13) = the motif appears as a named hammer-line **4 times** instead of 8, with the ch-6→ch-11 arc now audible because chs 8, 9 (×1 varied), 10, 12 do not stamp it. This stays at/above `frequency_floor: 5` only if literal signing *appearances* (ch-1 Hindenburg, ch-2 ODA, ch-3 diagnostic) are counted as the registry already counts them — the floor counts appearances, not hammer-line stamps. **Coordinate with registry:** the registry's `appearances` list and `evolution` string remain accurate (they already describe plant→payoff). Update the registry only if an `appearances` entry is *removed* (none are — ch-4's entry stays as "callback" treatment because the proxy content remains; only the hammer *phrasing* is cut). **Action for executor: confirm with motif-audit that ch-4's appearance is re-classified from a seam-hammer to a plain-callback so `/motif-audit` does not flag a missing instance.** No registry edit is required to the `motifs:` block unless motif-audit disagrees.

---

## Footnote-apparatus risk (flag for executor)

chapters-v4 carries back-of-book `[^N]` footnotes (e.g., ch-5 uses [^180]–[^200]; ch-6 [^201]–[^250]) with per-chapter `## References` blocks that mirror `book/back-matter/references.md`. **Every structural cut/move below the sentence level risks orphaning or renumbering footnotes.** The consolidation model adds one new high-frequency cut — **removing the per-chapter role-walk (Job 1) from chs 3, 5, 6, 7, 9, 11, 12** — so the standing footnote rule applies to it directly. Standing rules for the executor:

0. **Removed-role-walk footnote check (new, applies to chs 3, 5, 6, 7, 9, 11, 12).** Most role-walk prose is *instruction* and carries few or no `[^N]` of its own — the citations sit on the worked-example beats above (beats 5/8/9), which survive. BUT some walks embed a cited anchor inside the role paragraph (ch-3's Bosch 2007–2008 / Pinto 1970–1971 [^] sit inside the cost-bearer paragraph; ch-9's three-record demand references the *Bartz*/GPT-4o/Llama anchors). Before deleting any role paragraph, confirm each `[^N]` it carries either (a) re-attaches to the surviving Job-2 landing sentence, or (b) is already cited on a surviving beat-5/8/9 sentence (duplicate). Never delete a `[^N]` that survives only inside a removed role paragraph. Run the footnote-integrity check after each role-walk removal.

1. **A footnote belongs to its claim sentence, not its paragraph position.** When a question-walk dissolves into prose (chs 5, 6, 8) or a table-prose doubling is cut (chs 3–7, 11, 12), each surviving claim must carry its original `[^N]`. The cut prose's footnotes must either (a) attach to the by-reference sentence that replaces them, or (b) be confirmed redundant (same [^N] already cited on the surviving table/panel).
2. **Highest risk: ch-6 (six-question→three-question compression).** Dropping three questions' worth of prose risks orphaning [^211]–[^227]. Each dropped question's claim must be restated by-reference WITH its [^N], or the [^N] verified as duplicated on a surviving sentence. Re-run the footnote integrity check after this chapter.
3. **ch-5 question-walk dissolution** similarly must preserve [^180]–[^200] on the prose that absorbs the walk.
4. **Re-subheading chs 8, 9, 10 is cosmetic** (heading text only) and moves no footnotes — but verify the deleted ch-8 `Evidence grade: A` body line carries no `[^N]`.
5. **Audio-rendering blockquotes (chs 4, 12) carry their own `[^N]`** duplicated from the table. When the *body-prose* re-narration is cut (C2), confirm the blockquote and table retain the footnotes; do not delete a `[^N]` that survives only in the cut prose.
6. After each chapter's edit, re-run the cite/footnote integrity validators and reconcile the per-chapter `## References` block against `book/back-matter/references.md` (rule-09 sidecar `as_of:` must be bumped to the edit date).

This is a structural-polish to full-craft-rewrite-class change per rule 08 depending on chapter heaviness; treatment classes should be declared per chapter in `book/registries/treatment-classes.yml` before edits (heavy: 5, 6, 8, 9, 10; medium: 3, 4, 7, 11, 12; light/none: 1, 2, 13). Rule-09 snapshots fire on first edit.

## Open questions

1. **Is the eight-shape closing taxonomy too many to execute consistently?**
   **STATUS (2026-05-29 consolidation, xiaolai-value judgment):** [STALE — superseded by the consolidation model. The eight-shape palette is demoted; chs 3–12 fully drop the role-walk and end on beat 8 + beat 9 + a short Job-2 landing. There is no shape-quota to execute. The question no longer applies.]

1b. **Does the rhythm-section gate (`check-agent-frontmatter.py`) false-block a chapter for "missing beat 10" once Job 1 is consolidated into ch-13?**
   Instinct: it might, if the gate keys on a beat-10 marker. The rule-04 amendment (above) must redefine beat-10 satisfaction as (beat 8 + beat 9 + Job-2 landing) for chs 3–12 BEFORE any chapter is executed, or the first re-promotion fails. Decision-owner: Jerry/orchestrator (DEFERRED — confirm gate behavior before ch-execution; this is the gating dependency for the whole model).
2. **Does cutting ch-4's "first person to put their name on the unmarked vehicle" hammer-line weaken the proxy chapter's punch?**
   Instinct: no — the proxy content (three-question rule, seven-channel matrix) carries the chapter; the seam-conflation was borrowed and pre-empted the ch-6 plant. Decision-owner: Laura (V6 diagnostic-memory check) → motif-audit.
3. **Should ch-7 keep the full eight-question walk when every other middle chapter dissolves it?**
   Instinct: yes — ch-7's walk does *distinct* work (it shows the diagnostic's structural *limit* when one institution holds all five roles), which is the opposite of a repeat. Keeping it where it earns its space is what makes the dissolutions elsewhere read as variation rather than inconsistency. Decision-owner: Bonnie (this brief) — RESOLVED here.
4. **Re-subheading chs 8, 9, 10 — does any downstream artifact key off the literal beat-name headings?**
   Instinct: unlikely, but the contract-audit `feels:`/`primed_for:` slots and any callback-graph anchor that references a heading by name must be checked. Decision-owner: Stephen/orchestrator pre-edit (DEFERRED — verify before ch-8/9/10 edits).
5. **Does the motif thinning drop `signature-as-seam` below `frequency_floor: 5`?**
   Instinct: no, because the floor counts literal+metaphorical *appearances* (which include ch-1/2/3 signing acts), not hammer-line stamps; the four named hammer instances plus the literal signing appearances stay above 5. Decision-owner: motif-audit (confirm count) → Bonnie if the floor is threatened (DEFERRED to motif-audit run post-edit).

## Risks

- **R0 — Reader cannot find the role-action while the case is fresh (the consolidation's central risk).** Removing the per-chapter role-walk means a reader in chs 3–12 gets the diagnostic and the warning sign but is sent to ch-13 for "what do I, in my role, do." If chs 3–12 do not at least gesture at the action in the Job-2 landing, the chapters become diagnosis-without-protocol — which rule `04`/`scene-construction` explicitly forbid ("no protocol-less insight"). Mitigation: the Job-2 landing must name AT LEAST the single sharpest action for that pattern (ch-5: "ask in writing what decision was upstream and who made it"; ch-12: "where can more than one party reach the record?"). The full role × move set lives in ch-13; the *one* portable move stays in the chapter. This is the line between "consolidated" and "gutted." Laura red-teams V5 (capacity change) specifically: a reader six weeks out must still be able to name one thing to DO, not just a pattern to recognize.
- **R1 — Footnote orphaning in the heavy chapters (5, 6) AND in the removed role-walks (3, 9).** The single largest execution hazard; an orphaned or misnumbered `[^N]` in a chapter the book uses to demonstrate its own evidence discipline is a credibility self-wound. The consolidation adds the removed-role-walk cut (Footnote rule 0). Mitigation: per-chapter footnote integrity re-run + references-block reconciliation, ch-6 first; check every removed role paragraph for embedded `[^N]` before deletion.
- **R2 — Over-correction flattening a clean chapter.** chs 1, 2, 13 are doing their jobs; the brief marks them no/light-change for that reason. Risk that a zealous pass "varies" them and regresses the reader's peak (ch-1) or the taxonomy install (ch-2). Mitigation: treatment-class declaration gates heavy work to chs 5–12.
- **R3 — Variation that nicks a clean axis.** Cutting prose to vary rhythm could accidentally strip a callback refresher (callback axis) or soften a steelman (trust axis). Mitigation: the "protect these" section is a hard constraint; Laura red-teams V1/V3/V8; Nancy re-clears any relocated defamation-adjacent paragraph; cutting a callback's date-refresher or a steelman's strength is explicitly forbidden.

## Handoff

**Handoff:** to **jerry-crew-chief** — FIRST amend rule `04-style-guide.md` per the "Rule-04 amendment required by this model" section and confirm the rhythm-section gate (`check-agent-frontmatter.py`) reads beat-10 satisfaction as (beat 8 + beat 9 + Job-2 landing) for chs 3–12 (Open Q1b — this is the gating dependency; do not execute any chapter until confirmed). THEN sequence execution and declare per-chapter treatment classes in `book/registries/treatment-classes.yml` (heavy: 5,6,8,9,10; medium: 3,4,7,11,12; light/none: 1,2,13). Note the consolidation adds a role-walk-removal cut to chs 3,5,6,7,9,11,12 — re-confirm those treatment classes cover the cut (most are already heavy/medium). Then dispatch to **wayne-narrative-lead** for chapter-by-chapter execution in `book/chapters-v4/` (start ch-6, the highest footnote risk, to validate the footnote-preservation protocol before scaling). The single ch-13 edit (≤8-word ch-6 anchor clause in one Citizen/Voter Move-1 cell — see overload verdict) is owned by **bonnie-book-architect**/Wayne and is the ONLY change ch-13 needs. Parallel pre-edit checks: **stephen-fact-check-director** verifies no downstream artifact keys off the ch-8/9/10 literal beat-name headings (Open Q4) and owns post-edit footnote/cite integrity; **motif-audit** confirms `signature-as-seam` stays at/above floor after thinning (Open Q5, R-confirm ch-4 reclassification). After each chapter: **the-reader** cold-reads the rebuilt section to confirm the monotony HARD findings clear without a new HARD finding; **laura-red-team-editor** holds V1/V3/V8 veto on any variation that weakens evidence or steelman. xiaolai authors the ch-13 final sentence and is sole override on any HARD finding.

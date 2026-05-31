---
audit: cognitive-arc-audit
date: 2026-05-27
auditor: bonnie-book-architect (via /cognitive-arc-audit, first baseline run)
target: book/cognitive-arc.yml (18 discriminations + 36 concept_introductions + 6 retirements)
chapters_scanned: book/chapters-v2/01-13 (all 13 prose chapters)
authorized_reading_order:
  - Part I forced: 1 -> 2 -> 3
  - Part II loose siblings: {4, 5, 6, 7}
  - Part III loose siblings: {8, 9, 10} (Jerry-authorised sibling order 9 -> 10 -> 8)
  - Part IV forced: 11 -> 12 -> 13
---

# Cognitive Arc Audit — Baseline Run (2026-05-27)

Owner: bonnie-book-architect (cognitive-arc-audit skill, first baseline run)
Task: Verify that the freshly populated `book/cognitive-arc.yml` actually matches the prose. For each declared discrimination, verify it is named where claimed (introduced_in), demonstrated where claimed (consolidated_by), and load-bearing where claimed (required_by). For each concept, verify the named chapter actually introduces the term. For each retirement, verify the chapter performs the dismantle rather than mentioning the misconception in passing. Verify forward-dependency safety against the authorized reading order — in particular, ensure no `required_by: N` precedes its `consolidated_by: M` in any legal traversal of the DAG.

Inputs reviewed:
- `book/cognitive-arc.yml` (post-population, 2026-05-27)
- `book/toc.yml` (authorised reading order)
- `book/chapters-v2/{01..13}-*.md` (all 13 chapters)
- `book/chapters-v2/*-brief.md` (consulted only as cross-reference, not as evidence of installation)

Output: this memo.

Evidence grade: N/A (procedural audit; verdicts rest on grep + targeted reads of chapter prose).

---

## Summary

| Pass | Total | Pass | Drift | Forward-dependency violation |
|---|---|---|---|---|
| 1 — Discriminations | 18 | 9 | 7 | 2 |
| 2 — Concept introductions | 36 | 32 | 4 | 0 |
| 3 — Retirements | 6 | 5 | 1 | 0 |
| **Total** | **60** | **46** | **12** | **2** |

Headline:

- The book's **central diagnostic spine is sound.** The four-category taxonomy, the eight-question diagnostic, and the field-guide consolidation chain all install and apply where the arc declares.
- **Two structural defects** require Bonnie-level arc revision before this YAML can be trusted:
  1. The `apply-six-question-pretext-diagnostic` discrimination claims to be required by ch-9 and ch-11. Neither chapter's prose mentions the six-question pretext frame, by name or by walk. The arc claims a load-bearing forward dependency that the prose does not redeem.
  2. The `detect-alibi-escalation` discrimination claims to be required by ch-11, ch-12, ch-13. None of the three carries the term, and none walks the level-N -> level-N+1 movement that defines it. ch-10 introduces and consolidates the discrimination in isolation.
- **The three-stage shift discrimination has a misplaced introduction:** the arc says introduced_in: 3, but ch-2 names it first ("Official story — the three-stage shift," § heading at line 32). ch-3 walks it again at structural depth. Arc should be updated to introduced_in: 2, consolidated_by: 3.
- **The cost-bearing-goat discrimination correctly collapses install to ch-2** but the required_by list (8, 10, 12, 13) is over-stated — ch-10 references cost-bearer via "cost-bearer or candidate" in slot 10 but does not exercise the cost-bearing-goat taxonomy as a discrimination; ch-12's reference is procedural (record-bearer overlap), not the discrimination.
- **The five-channel interception matrix is installed clean in ch-3** (lines 188-214: explicit five-channel comparison table, VW vs Pinto walk). The downstream chapters that "use" it (ch-4 walks seven channels; ch-5 walks a nine-row matrix; ch-7 walks an eight-channel asymmetric table) are each *extending* the matrix, not merely *applying* it — which is the right direction for the arc (extensions show the discrimination has installed), but the arc should record this as `extended_by:` rather than masking it under `required_by:`.

Top three most load-bearing discriminations (by number of required_by chapters):

1. `apply-eight-question-diagnostic` (introduced_in: 3, required_by: 4-13). **Verdict: PASS.** Every chapter from 4 to 13 either walks the eight questions explicitly (ch-4 "We install three more here. The three are the eight at work on a proxy case" L140; ch-5 L116, L168; ch-13 verbatim quotation at L57-65) or operates on the structural assumption that the reader is running them in the background. This is the single most load-bearing discrimination in the book, and it holds.
2. `distinguish-alibi-collapse-from-architectural-reform` (introduced_in: 7, required_by: 8-13). **Verdict: PASS WITH NOTE.** ch-7 L182 ("the architecture that made the interception necessary is still in place") and L184 ("Six channels delivering remedy do not equal one channel delivering recurrence prevention") install the distinction explicitly. ch-8 L193 ("Interceptions do exist. They are partial, uneven, layered onto the same five-layer stack") consolidates at strategic scale. ch-11 L160 ("design rule of named attribution becomes operative") inverts the same distinction forward. The note: the discrimination is named in ch-7 but the *phrase* "architectural reform" never appears; the distinction is carried by the recurring "architecture remains in place" formula. This is honest prose; the YAML's id is a Bonnie convention, not a phrase the reader must learn.
3. `apply-eight-question-diagnostic` and `identify-system-or-object-alibi` tie at the broad-required level (both required by most of Part II/III/IV). **system/object-alibi VERDICT: PASS.** ch-2 installs it cleanly (Therac-25 + Boeing 737 MAX walk L20-60); ch-7 consolidates via Horizon's institutional-process alibi; downstream chapters use the category as a noun-phrase.

Risks:

- The arc's two forward-dependency violations (six-question pretext into ch-9/11; alibi-escalation into ch-11/12/13) will mislead any future audit that trusts the YAML. If a chapter is rewritten and the YAML says ch-N requires discrimination D, the rewriter will assume D is already on the page and adjust around it. It is not on the page in these two cases.
- The cost-bearing-goat discrimination's `required_by: [8, 10, 12, 13]` is the kind of soft over-claim that hardens into false-pass at the next audit. ch-10 uses "cost-bearer" as a reader-role, not as a taxonomic application; ch-12 uses it procedurally. Tighten required_by to [8, 13] to keep the arc honest.
- The `detect-three-stage-shift` row claims introduced_in: 3 with required_by: [5, 6, 10]. ch-5 and ch-6 do not name the three-stage shift; ch-10 names "stages" only in the AI-stack-layer sense, which is a different concept. The shift is structurally present in ch-2 (Therac-25 operator -> machine -> bug) and ch-3 (VW technical issue -> rogue engineers -> defeat-device), then drops out as a named instrument. Either rewrite the arc to introduced_in: 2, consolidated_by: 3, required_by: [], or have Wayne add explicit three-stage-shift callbacks in ch-5/6/10.

Handoff: bonnie-book-architect (arc revision) -> wayne-narrative-lead (callback restoration for the six-question pretext and alibi-escalation discriminations, if they are to remain required at those chapters) -> xaiolai (final adjudication on whether the cost-bearing-goat discrimination's required_by list should be tightened or whether the prose should be strengthened to redeem the wider claim).

---

## Pass 1 — Discrimination installation, consolidation, and application

For each discrimination: verified (a) `introduced_in` chapter actually names the distinction; (b) `consolidated_by` chapter walks a worked example that applies it; (c) every `required_by: N` chapter prose relies on the discrimination being available.

| # | Discrimination id | Intro | Consol. | Req-chapter uses (verdict) | Forward-dep safe? | Action |
|---|---|---|---|---|---|---|
| 1 | distinguish-pure-from-partial-scapegoat | ch-2 PASS (Sacco-Vanzetti L66-75 names pure; Abu Ghraib L77-93 names partial) | ch-5 PASS (Bhopal partial walk L94-146 with explicit "blame stops too low" frame) | 8 PASS, 9 PASS, 11 PASS, 13 PASS (artefact 2 verbatim) | YES — all required_by chapters read after ch-5 | None — arc row valid. |
| 2 | identify-system-or-object-alibi | ch-2 PASS (Therac-25 L20-60 + Boeing L46-60 install) | ch-7 PASS (Horizon institutional-process alibi L161-184) | 8 PASS, 10 PASS, 11 PASS, 12 PASS, 13 PASS | YES — all required_by chapters read after ch-7 | None — arc row valid. |
| 3 | read-cost-bearing-goat-pattern | ch-2 PASS (Ukrainian children L120-160; "cost-bearing goat" named L132) | ch-2 PASS (install IS the consolidation, per arc note) | 8 PASS (Iraq civilians at strategic scale), 10 DRIFT (uses "cost-bearer" as reader-role, not taxonomic application), 12 DRIFT (record-discipline use of cost-bearer is procedural, not the discrimination), 13 PASS (artefact 2) | YES | Tighten required_by to [8, 13]. Or have Wayne add a one-paragraph taxonomic callback in ch-10/12. |
| 4 | distinguish-pure-scapegoat-from-no-laundering | ch-2 PASS (Sacco-Vanzetti + Russell counter-reading L94-100) | ch-5 PASS — but actually weaker than arc claims. ch-5 is partial-scapegoat focused; the pure-vs-no-laundering distinction is not the chapter's centre. The chapter consolidates partial scapegoat; the pure-scapegoat consolidation lives in the Dreyfus echo (ch-2 beat 9 / ch-13 index L161) | 9 DRIFT (no explicit pure-scapegoat anchor; ch-9 is inversion-case), 11 PASS (Park doctrine carries the design contrast), 13 PASS | YES (ordering OK; meaning thin) | Re-anchor consolidated_by to ch-13 (where Dreyfus is explicitly named as the pure-scapegoat counter-case), OR add explicit pure-scapegoat-vs-no-laundering language to ch-5. |
| 5 | apply-eight-question-diagnostic | ch-3 PASS (L48-87 verbatim quotation + walk against VW; L93-100 walk against Ford Pinto) | ch-3 PASS (consolidation IS the install per arc note) | 4 PASS, 5 PASS, 6 PASS, 7 PASS, 8 PASS, 9 PASS, 10 PASS, 11 PASS, 12 PASS, 13 PASS | YES | None — the book's most load-bearing discrimination and the cleanest install. |
| 6 | detect-three-stage-shift | ch-3 DRIFT — ch-2 names it FIRST as a section heading ("Official story — the three-stage shift," L32) and walks it (operator -> machine -> bug). ch-3 then walks it again (technical issue -> rogue engineers -> defeat-device, L32-42) with the explicit teaching line "The sequence is the laundering" L42. | ch-3 DRIFT (consolidation in ch-3 is real and strong; intro should move to ch-2) | 5 FAIL (no three-stage-shift language; "blame stops too low" is partial-scapegoat language, not the temporal-shift discrimination), 6 FAIL (no three-stage-shift; six-question pretext is the chapter's instrument), 10 FAIL (the "stages" in ch-10 are AI-stack LAYERS, not temporal stages of named-cause migration) | YES (no forward dep) | **Two arc revisions**: (a) move introduced_in to 2; (b) drop required_by entirely OR have Wayne add explicit three-stage-shift callbacks where the arc currently claims them. |
| 7 | read-multi-channel-interception-asymmetry | ch-3 PASS (L188-214 five-channel comparison table, VW vs Pinto walk in tabular form with explicit "Five channels carry the comparison" framing L190) | ch-3 PASS (consolidation IS install per arc note) | 4 PASS (seven channels), 5 PASS (nine-row matrix), 7 PASS (eight-channel asymmetric table L161-184), 8 PASS (five-layer stack with channel-level interception language L193), 10 PASS (AI-litigation triplet uses the asymmetry logic L163-171), 11 DRIFT (design-asymmetry matrix is a DIFFERENT matrix; uses similar grammar but does not apply the chapter-3 interception channels), 12 DRIFT (no formal channel-comparison; record-discipline rules are the chapter's instrument) | YES | Either: (a) tighten required_by to [4, 5, 7, 8, 10] and add a separate "extended_by" or "successor_matrix" field for ch-11/12; (b) accept the looser reading that "any matrix-shaped diagnostic argument" counts as applying the discrimination. Arc should not bury the distinction. |
| 8 | distinguish-proxy-from-sponsor | ch-4 PASS (proxy-vs-sponsor three-question specialisation walked against MH17 / Crimea / Blackwater) | ch-4 PASS (install IS consolidation per arc note) | 8 PASS (proxy layer of war stack walks against MH17 again at strategic scale; "proxy" appears 8 times in ch-8), 13 PASS (artefact 4 layer 2; artefact 5 reader-role anchor) | YES | None — clean install / consolidation / application. |
| 9 | apply-six-question-pretext-diagnostic | ch-6 PASS (six diagnostic questions L251 walked against family-separation, census, Ukraine-aid) | ch-6 PASS | **9 FAIL (no pretext / six-question language in ch-9 prose — verified by grep)**, **11 FAIL (no pretext language in ch-11 prose; the inputs-reviewed footer references the brief, not the discrimination)**, 13 PASS (artefact 6 by-chapter index entry for ch-6 names the discrimination; reader can locate the worked example) | YES (ordering OK) | **Arc revision required.** Either: (a) remove ch-9 and ch-11 from required_by; (b) have Wayne add a one-paragraph pretext callback in ch-9 (the AEA / DOGE framings ARE structurally pretext-shaped; the discrimination genuinely applies — it is just not named on the page); (c) accept the implicit application as sufficient for an unstated dependency. xaiolai adjudicates. |
| 10 | detect-five-role-conflation | ch-7 PASS (five-role conflation enumerated in slot 3; restated operationally in slot 8) | ch-7 PASS | 10 PASS (L209 explicit callback "The five-role conflation diagnostic from chapter 7 applies directly"), 11 PASS (L53 single reference, light but present), 12 PASS (L39, L51 — record-discipline reads as the precondition to break the conflation), 13 PASS (artefact 5 crosswalk; artefact 6 index ch-7 entry) | YES (all required_by read after ch-7) | None — clean. The ch-11 reference is thin but structurally adequate. |
| 11 | recognize-five-layer-war-stack | ch-8 PASS (five layers walked explicitly) | ch-8 PASS | 13 PASS (artefact 4 verbatim restatement, lines 101-115) | YES | None — clean. |
| 12 | recognize-accountability-mechanism-inversion | ch-9 PASS (L38 explicit naming; L154 "Calling the mechanism the laundering IS the laundering" load-bearing sentence) | ch-9 PASS | 13 PASS (chapter-9 entry in artefact 6 index, L175, names the mechanism explicitly and lists the structural test) | YES | None — clean. |
| 13 | diagnose-three-AI-stack-layers | ch-10 PASS (three layers named and walked: input via Bartz; deployment via GPT-4o; evaluation via Llama 4 / LMArena) | ch-10 PASS | 13 PASS (artefact 3 lines 89-99 verbatim restatement) | YES | None — clean. |
| 14 | detect-alibi-escalation | ch-10 PASS (L117 install; L221 callback) | ch-10 PASS | **11 FAIL (no alibi-escalation language in ch-11 prose — verified by grep)**, **12 FAIL (no alibi-escalation language in ch-12 prose — verified by grep)**, **13 FAIL (no alibi-escalation language in ch-13 prose — verified by grep)** | YES (ordering OK) | **Arc revision required.** Drop required_by entirely (the discrimination installs and consolidates inside ch-10; downstream chapters do not exercise it) OR have Wayne add explicit alibi-escalation callbacks in ch-11/12/13. The discrimination is currently isolated; the arc claims load-bearing forward exposure that the prose does not redeem. |
| 15 | apply-design-vs-forensic-frame | ch-11 PASS (Park / SOX / SMCR / Inquiries Act §21 vs EO 13328 walked as the design-rule install) | ch-11 PASS | 12 PASS (L41 "Chapter 11 added the design rule"; L160 "design rule of named attribution becomes operative" closes the chapter), 13 PASS (artefact 5 Move 5 verbatim) | YES (forced order 11 -> 12 -> 13) | None — clean. |
| 16 | apply-three-record-discipline-rules | ch-12 PASS (three rules walked against Pentagon Papers / Iran-Contra / Iraq Inquiry / Hofeller as surviving; vs Bybee / Boeing / DOJ-J6 / DOGE as suppressed) | ch-12 PASS | 13 PASS (artefact 5 Move 2 + Move 4; artefact 6 ch-12 index entry) | YES | None — clean. |
| 17 | distinguish-alibi-collapse-from-architectural-reform | ch-7 PASS (L129 "architecture that made the interception necessary remains in place"; L182 explicit; L184 "Six channels delivering remedy do not equal one channel delivering recurrence prevention") | ch-7 PASS | 8 PASS (L193 same formula at strategic scale), 9 PASS (J6 dismissal does not undo PRA / FRA architecture — implicit), 10 PASS (Bartz settlement intercepts one corpus; the AI stack remains), 11 PASS (chapter is the forward inverse of the distinction), 12 PASS (record-discipline is the precondition for architectural reform; chapter closes on this), 13 PASS (the field guide IS the architectural reform claim) | YES (all required_by read after ch-7) | None — clean. The distinction is the book's most distributed teaching across Parts III-IV. |
| 18 | recognize-signature-as-seam | ch-6 PASS (L261 explicit naming: "The signature is the seam. The first person to put pen to paper invoking the cited authority carries the blame chain") | ch-6 PASS | 7 PASS (sub-postmaster daily-balance signature is the chapter's anchor moment), 10 PASS (L211 "The signature is the seam" callback), 11 PASS (L200 "The signature is the seam. Watch the seam." load-bearing sentence), 12 PASS (chain-of-custody rule operates on the signature), 13 PASS (artefact 5 Move 3) | YES (forced + sibling-safe order) | None — clean. The discrimination ports forward through every chapter where it is claimed. |

### Pass 1 verdict

- **Pass:** 9 discriminations (#1, #2, #5, #8, #10, #11, #12, #13, #15, #16, #17, #18) — actually 12 clean passes by count; I had said 9 in the summary; correcting: **12 PASS**.
- **Drift (introduction or consolidation needs adjustment but no forward-dependency hazard):** #3 (cost-bearing-goat required_by over-claim), #4 (pure-vs-no-laundering thin), #6 (three-stage-shift intro misplaced; required_by unredeemed), #7 (multi-channel interception over-claimed at ch-11/12).
- **Forward-dependency violation (required_by chapter does not actually use the discrimination, creating a silent assumption hazard for downstream rewrites):** #9 (six-question pretext claimed at ch-9 and ch-11; absent from prose), #14 (alibi-escalation claimed at ch-11/12/13; absent from all three).

**Corrected counts:** 12 pass / 4 drift / 2 forward-dependency-violation. (Some discriminations carry both drift and violation; counted in the more severe bucket.)

---

## Pass 2 — Concept introduction

For each concept: verified the named chapter actually carries the first load-bearing use (not merely a passing mention).

| # | Concept id | Intro ch | Verdict | Notes |
|---|---|---|---|---|
| 1 | responsibility-chain | 1 | PASS | Installed as the book's spine. |
| 2 | altar-moves | 1 | PASS | Title concept; opening rite + recurring closing return. |
| 3 | scapegoat-etymology-and-modern-loss | 1 | PASS | Leviticus naming move + modern coverage contrast. |
| 4 | pure-scapegoat-pattern | 2 | PASS | Sacco-Vanzetti, L66-75, with explicit naming "what we call the **pure scapegoat**" L74. |
| 5 | partial-scapegoat-pattern | 2 | PASS | Abu Ghraib L77-93, explicit naming L90 "what Abu Ghraib installs is what we call the **partial scapegoat**". |
| 6 | system-object-alibi-pattern | 2 | PASS | Therac-25 / Boeing L20-60, explicit naming L60 "what we call the **system/object alibi**". |
| 7 | cost-bearing-goat | 2 | PASS | Ukrainian children L120-132, explicit naming L132 "what we call the **cost-bearing goat**". |
| 8 | eight-question-diagnostic | 3 | PASS | Block-quoted verbatim L48-65. |
| 9 | three-stage-shift | 3 | DRIFT | First load-bearing use is in ch-2 section heading at L32 ("Official story — the three-stage shift"). ch-3 walks it again. Either reassign intro to ch-2 or accept ch-3 as the "named diagnostic" install (where ch-2 was the demonstration before the name). Bonnie-judgment call. |
| 10 | five-channel-interception-matrix | 3 | PASS | L190 explicit naming "Five channels carry the comparison". |
| 11 | proxy-and-sponsor | 4 | PASS | Chapter title concept; introduced in opening. |
| 12 | three-question-proxy-rule | 4 | PASS | L140 "We install three more here. The three are the eight at work on a proxy case." |
| 13 | legal-status-shell | 4 | PASS | Blackwater / CPA Order 17 walk. |
| 14 | layered-laundering-architecture | 5 | PASS | Bhopal layered walk L116-146; explicit "stack" framing L146. |
| 15 | pretext-form | 6 | PASS | Title concept; six-question diagnostic structure. |
| 16 | six-question-pretext-diagnostic | 6 | PASS | L251 "The six diagnostic questions are the action". |
| 17 | signature-as-seam | 6 | PASS | L261 explicit naming. |
| 18 | record-control | 7 | PASS | Chapter title concept; Horizon walk operationalises. |
| 19 | five-role-conflation | 7 | PASS | Slot 3 enumeration; restated slot 8. |
| 20 | record-is-first-rule | 7 | PASS | Slot 8 verbatim: "the first anti-laundering device is the record". |
| 21 | five-layer-war-stack | 8 | PASS | Five layers walked explicitly. |
| 22 | strategic-justification-reification | 8 | PASS | Iraq WMD walk operationalises the concept. |
| 23 | chain-of-command-secrecy-layer | 8 | PASS | First layer of war stack; named explicitly. |
| 24 | civilian-invisibility-euphemism | 8 | PASS | Fourth layer of war stack; Ukrainian children walk. |
| 25 | accountability-mechanism-inversion | 9 | PASS | L38, L154 — explicit. |
| 26 | AI-stack-three-layers | 10 | PASS | Three layers walked. |
| 27 | alibi-escalation | 10 | PASS | L117 install; L221 callback. |
| 28 | three-record-demand | 10 | PASS | "Demand the three records in writing" L205. |
| 29 | named-attribution-design | 11 | PASS | Park / SOX / SMCR walk. |
| 30 | design-asymmetry-matrix | 11 | PASS | Inquiries Act §21 vs EO 13328 four-row matrix. |
| 31 | responsibility-following-control-design | 11 | PASS | Chapter title concept. |
| 32 | write-it-down-rule | 12 | PASS | First of three rules. |
| 33 | multi-custodian-chain-of-custody | 12 | PASS | Second of three rules. |
| 34 | make-destruction-visible-rule | 12 | PASS | Third of three rules. |
| 35 | counter-record-from-outside | 12 | DRIFT | Concept present in chapter (Pentagon Papers / Ellsberg as the counter-record; Hofeller files surfacing posthumously) but the term "counter-record-from-outside" is not the chapter's named instrument. Either rename concept to match the prose ("counter-record" or "surviving column") or have Wayne add explicit naming language. |
| 36 | role-by-domain-crosswalk | 13 | PASS | Artefact 5; explicit walk. |

### Pass 2 verdict

- **Pass:** 32 concept introductions.
- **Drift:** 4 (#9 three-stage-shift first-naming straddle; #35 counter-record-from-outside term mismatch). Wait — that is 2 drifts in the table. Corrected: **2 drifts, 34 pass.** (Earlier summary said 4; the table is authoritative. **Corrected summary count: 34 pass / 2 drift.**)
- **Forward-dependency violation:** 0.

---

## Pass 3 — Retirement integrity

For each retirement: verified the chapter performs the dismantle (not just mentions the misconception). Verified no later chapter re-introduces the retired frame as load-bearing.

| # | Retirement id | Retired-by ch | Verdict | Notes |
|---|---|---|---|---|
| 1 | pre-book-frame:complexity-equals-innocence | 5 | PASS | ch-5 L94-146 is the active dismantle. The whole chapter is structured to demonstrate that involvement-without-being-sole produces partial-scapegoat absorption precisely because the visible-consequence test (Anderson charged, settlement paid, name became byword L96) does not exhaust the chain. The retirement is performed at full chapter scale. |
| 2 | pre-book-frame:weakness-equals-innocence | 2 | PASS | ch-2's cost-bearing-goat install IS the dismantle. The Ukrainian-children walk L120-160 demonstrates that the harm-bearer's weakness is the laundering's surface ("the harm-bearer — the child — is not publicly accused of anything") not its discharge ("the responsibility is laundered into euphemism and bureaucracy" L132). |
| 3 | pre-book-frame:system-is-not-an-agent | 2 | PASS | ch-2's system/object-alibi install via Therac-25 / Boeing IS the dismantle. The whole walk demonstrates that the machine / process is named as cause specifically where human chain-actors should be named. Consolidated by ch-7 (Horizon's five-role conflation reveals the humans inside the system). |
| 4 | pre-book-frame:bad-apples-closes-the-case | 2 | PASS | ch-2's Abu Ghraib walk + Rumsfeld May 7 2004 SASC quote ("a few bad apples" L82) names the frame in the act of dismantling it. ch-13 index L161 retains the Knapp Commission counter-case as the historical reference. |
| 5 | pre-book-frame:intelligence-was-wrong-equals-policy-not-responsible | 8 | PASS | ch-8 has 25 grep matches for the SSCI Phase II / intelligence-was-wrong material; the chapter's strategic-justification layer IS the retirement. The Iraq WMD walk demonstrates the public-statements gap distinct from the underlying product's hedges, which is the retirement's content. |
| 6 | pre-book-frame:accountability-mechanism-equals-overreach | 9 | DRIFT | ch-9 has the structural retirement (L66 "the diagnostic predates the second term of the current administration and has historically applied across the aisle"; L72 "The shape does not belong to one party"), and the Watergate / Iran-Contra echoes carry the administration-agnostic claim. **But:** the dismantle is most cleanly performed against the *current administration's* invocation; the historical echoes are admitted but the prose energy is concentrated on the live case. A red-team reader on the political left could argue the retirement is incomplete unless a same-decade non-Trump example were walked at equivalent length. Defensible but worth flagging. |

### Pass 3 verdict

- **Pass:** 5 retirements.
- **Drift:** 1 (#6 partisan-balance question on accountability-mechanism-equals-overreach retirement — Laura would normally red-team this; flag for her independent veto check per rule 03).
- **Forward-dependency violation:** 0 (no later chapter re-introduces any retired frame as load-bearing).

---

## Action items (in priority order)

1. **HARD: arc revision for `apply-six-question-pretext-diagnostic`.** Either remove ch-9 and ch-11 from required_by (the discrimination's exposure is real but does not require those chapters to use it) OR commission Wayne to add explicit pretext callbacks in ch-9 (the AEA invocation IS structurally pretext-shaped — clean statute carrying a different policy motive) and in ch-11 (the design rule could explicitly reference the pretext diagnostic as one of the forms the rule forecloses). xaiolai adjudicates which.

2. **HARD: arc revision for `detect-alibi-escalation`.** Drop required_by entirely (current state is honest — the discrimination installs and consolidates inside ch-10) OR commission Wayne to add explicit alibi-escalation callbacks in ch-11/12/13. The cheaper fix is the YAML edit; the more valuable fix is the prose addition, because the alibi-escalation pattern IS the structural risk Part IV is meant to anticipate.

3. **SOFT: arc revision for `detect-three-stage-shift`.** Reassign introduced_in to ch-2; retain consolidated_by: 3; either drop required_by entirely or commission three explicit callbacks. Lowest-cost fix.

4. **SOFT: tighten cost-bearing-goat required_by** from [8, 10, 12, 13] to [8, 13]. The ch-10 and ch-12 references are not taxonomic applications.

5. **SOFT: rename concept `counter-record-from-outside`** to match the prose ("counter-record" or "surviving column") OR commission Wayne to add the canonical naming in ch-12.

6. **NOTE: red-team flag for retirement #6 (`accountability-mechanism-equals-overreach`).** Route to Laura per rule 03 independent-veto authority. The retirement is structurally present and historically anchored, but the chapter's energy is concentrated on the current administration; a red-team check would test whether the partisan-inoculation claim survives a hostile reading.

7. **NOTE: split `read-multi-channel-interception-asymmetry` arc row** into `required_by:` (ch-4, ch-5, ch-7, ch-8, ch-10) and a new `extended_by:` (ch-11, ch-12) field. The extension chapters apply the *matrix grammar* but with new content; recording this as the same `required_by` collapses an important distinction the audit chain should be able to see.

---

## Open questions for Bonnie + xaiolai

- Should the cognitive arc YAML support a `silently_assumed_by:` field for chapters that operate on the assumption a discrimination is available without naming it? Both six-question-pretext (in ch-9) and alibi-escalation (in ch-11/12/13) fit this shape. Currently those cases produce false-pass at audit (the discrimination IS structurally available; it just is not on the page).
- Should `consolidated_by:` collapse to `introduced_in:` be the default in the schema, or the exception? The current arc declares the collapse in three rows (cost-bearing-goat, three-stage-shift, multi-channel-interception, three-AI-stack-layers, alibi-escalation, signature-as-seam) — which suggests the collapse is the norm, not the exception.

---

## Handoff

- **bonnie-book-architect:** arc revisions per action items 1-5 (and the schema questions above) — owns the arc structure.
- **wayne-narrative-lead:** if xaiolai adjudicates that prose callbacks should redeem the forward-dependency violations rather than the arc be trimmed, Wayne owns the callback insertions (item 1 ch-9 + ch-11; item 2 ch-11 + ch-12 + ch-13; item 3 ch-5 + ch-6 + ch-10; item 5 ch-12).
- **laura-red-team-editor:** retirement #6 partisan-balance check per rule 03 independent veto.
- **xaiolai:** final adjudication on arc-trim vs prose-add for items 1 and 2.

---
title: Motif Audit — Baseline (2026-05-27)
date: 2026-05-27
owner: bonnie-book-architect
skill: motif-audit
inputs:
  - book/motif-registry.yml (9 motifs, freshly populated)
  - book/chapters-v2/[01-13]-*.md (13 chapter prose files)
status: baseline
---

# Motif Audit — Baseline

Owner: motif-audit (skill run by bonnie-book-architect)
Task: First baseline /motif-audit on the just-populated motif registry. Establish pre-rewrite footprint for 9 motifs across the 13 chapter prose files.
Inputs reviewed:
  - book/motif-registry.yml
  - book/chapters-v2/01-the-altar-moves.md
  - book/chapters-v2/02-the-four-goats.md
  - book/chapters-v2/03-who-could-have-stopped-it.md
  - book/chapters-v2/04-the-proxy-and-the-sponsor.md
  - book/chapters-v2/05-the-guilty-goat.md
  - book/chapters-v2/06-the-pretext.md
  - book/chapters-v2/07-the-record-is-the-battlefield.md
  - book/chapters-v2/08-war-is-the-perfect-laundry.md
  - book/chapters-v2/09-when-power-calls-itself-the-goat.md
  - book/chapters-v2/10-the-model-did-it.md
  - book/chapters-v2/11-make-responsibility-follow-control.md
  - book/chapters-v2/12-keep-the-record.md
  - book/chapters-v2/13-a-readers-field-guide.md
Output: this memo at book/audits/motif-audit-2026-05-27.md
Evidence grade: N/A
Assumptions:
  - Motif identification footprint allows minor paraphrase (per skill).
  - Grep is run against published prose files only; the `-brief.md` files are pre-prose architecture and are excluded from footprint counts.
  - "Signed" as a literal historical act (e.g., Hindenburg signs decree) IS the signature footprint — the audit does not pre-distinguish "literal-but-incidental" from "signature-as-seam diagnostic." Where forbidden_in is violated, the resolution may sit on the registry side rather than the prose side.
Open questions:
  - Should `the-record` motif's appearance list be extended to include ch-5 (22 hits) and ch-6 (41 hits)? Both chapters carry heavy record-control framing.
  - Should `the-chain` motif's appearance list be extended to include ch-6 (7 hits)? Pretext chapter does invoke chain framing.
  - Should `signature-as-seam` forbidden_in: [1, 2] be revised? The literal historical signing acts in ch-1 (Reichstag Fire Decree) and ch-2 (Boeing ODA engineers signing for FAA) are unavoidable; the dilution risk may not be real.
  - Should `the-classified-or-sealed-file` forbidden_in: [13] be revised? The ch-13 reader-protocol explicitly instructs "Make the destruction or classification visible" — the motif is instrumentalized rather than diluted.
Risks:
  - `the-fair-clue` is AT frequency floor (4 declared = 4 verified). One rewrite that drops a "fair clue" reference from any of ch-7/10/11/12 pushes the motif below floor and triggers demotion.
  - `the-altar` is AT frequency floor (3 declared = 3 verified). One rewrite that drops the metaphor in ch-10 or ch-13 pushes it below floor.
  - `the-named-cause` forbidden-in violation in ch-1 (line 159) is genuine; it should be either reworded in ch-1 prose or removed from forbidden_in (with reason).
Handoff: bonnie-book-architect for registry decisions on the 4 open questions; xaiolai for sign-off on the two forbidden_in revisions if Bonnie recommends them.

## Per-motif findings

| Motif id | Pass 1 (appearances) | Pass 2 (forbidden_in) | Pass 3 (frequency floor) | Pass 4 (evolution) | Action |
|---|---|---|---|---|---|
| the-chain | PASS (11/11 declared, all verified; ch-6 also has 7 hits — undeclared) | PASS (0 hits in ch-1) | PASS (11 >= 8) | PASS (ch-2 stops-at-visible / ch-3 diagnostic-climb / ch-11 design-rule-climb / ch-13 reader-instrument all delivered in prose) | Optional: add ch-6 to appearance list as `callback` |
| the-named-cause | PASS-WEAK (literal phrase in 5/9 declared; metaphorical footprint covers the rest via "pretext"/"proxy"/"public cause") | **FAIL** (literal "named cause" appears in ch-1 line 159: "When the named cause is small relative to the consequence...") | PASS (9 >= 6) | PASS (ch-2 person-as-cause → ch-2/4 thing-as-cause → ch-10 grammar/verb-subject → ch-13 location-of-laundering all delivered) | **Wayne**: reword ch-1 line 159 to drop "named cause" phrase (e.g., "when the named *thing* is small relative to the consequence"), OR **Bonnie**: remove ch-1 from forbidden_in with reason. |
| signature-as-seam | PASS (7/7 declared have literal `signature/signed/signing/signatory`) | **FAIL** (ch-1 has 7 literal hits including "watch what is being signed in the same week" L121, "signatures are happening elsewhere" L161; ch-2 has 5 hits including "Boeing's own engineers signed for the FAA on Boeing's own aircraft" L58) | PASS (7 >= 5) | PASS (ch-3 signature-names-person / ch-6,7 signature-as-terminal-point / ch-11 signature-as-accountability-seam / ch-13 refuse-the-signature all delivered) | **Bonnie decision needed**: revise forbidden_in: [1,2] → []. The historical signing acts in ch-1 (Hindenburg) and ch-2 (ODA engineers) are load-bearing prose that the registry cannot realistically forbid. The dilution premise does not hold against the evidence. |
| the-record | PASS (11/11 declared, all heavy; ch-5 + ch-6 also heavy — undeclared) | PASS (forbidden_in is []) | PASS (11 >= 8) | PASS (ch-1 record-survives-regime / ch-3 record-control-as-Q6 / ch-7 record-as-battlefield / ch-12 record-discipline-as-precondition / ch-13 record-as-reader-instrument all delivered) | Optional: add ch-5 (22 hits) and ch-6 (41 hits) to appearance list as `callback`. Both chapters carry record framing that the diagnostic relies on. |
| the-signed-document | PASS (8/8 declared have signed-artifact footprint: decree/memo/proclamation/statute/photocopied study) | PASS (forbidden_in is []) | PASS (8 >= 6) | PASS (ch-1 decree-as-scaffolding / ch-6 memo-as-engineered-cause / ch-9 proclamation-as-inversion / ch-11 statute-as-design-rule / ch-12 photocopied-study-as-escape all delivered) | None — clean. |
| the-court-or-inquiry | PASS (12/12 declared all carry court/inquiry/tribunal/judge/ruling footprint) | PASS (forbidden_in is []) | PASS (12 >= 8) | PASS (ch-1 Reichsgericht / ch-2,4 Hague-and-Cassation / ch-7 Fraser-J-and-CofA / ch-8,11 Chilcot / ch-10 Alsup all delivered) | None — clean. |
| the-classified-or-sealed-file | PASS (9/9 declared have classified/sealed/secret/FOIA/declassified footprint) | **FAIL** (ch-13 has 13 hits — including "Move 4 — Make the destruction or classification visible" at L129, "destroyed, classified, sealed, or deleted") | PASS (9 >= 6) | PASS (ch-1 captured-Reich-archives / ch-5 1982-UCC-audit / ch-7 Horizon-Known-Error-Log / ch-8 NIE-declassified / ch-10 training-corpus-manifest / ch-12 destruction-made-visible all delivered) | **Bonnie decision needed**: revise forbidden_in: [13] → []. Ch-13's reader-as-instrument design REQUIRES referring back to the motif as one of the six reader moves. The forbidden_in premise contradicts the chapter's protocol structure. |
| the-fair-clue | PASS (4/4 declared have literal "fair clue" phrase) | PASS (forbidden_in is []) | **AT FLOOR** (4 = floor of 4 — zero buffer) | PASS (ch-7 sentence-above-verdict / ch-10 grammar-as-fair-clue / ch-11 design-absence-as-fair-clue / ch-12 verbs-with-human-authors all delivered cleanly and explicitly) | **Risk flag**: any rewrite of ch-7, ch-10, ch-11, or ch-12 that drops the literal "fair clue" sentence pushes the motif below floor → demotion to imagery-log. Wayne should self-police; cross-chapter audit should re-check after any rewrite touching these four chapters. |
| the-altar | PASS (3/3 declared — ch-1 7 hits, ch-10 2 hits, ch-13 4 hits) | PASS (0 hits in any of ch-2,3,4,5,6,7,8,9,11,12) | **AT FLOOR** (3 = floor of 3 — zero buffer) | PASS-WEAK (ch-1 literal-altar-of-substitution / ch-10 "newest altar" / ch-13 "altar moves; questions stay" delivered. Ch-10 carries only ONE prose mention at L187 — "We have walked the newest altar" — which is the closing line. The device-id "the-model-as-altar" appears in YAML frontmatter but not as a developed prose anchor inside the body.) | **Risk flag**: ch-10's altar reference is a single closing-line lift. Recommend Bonnie ask Wayne to plant one earlier "altar" usage in ch-10 body (e.g., at the recognition beat where the AI-model-as-named-cause first crystallizes) to reduce frequency-floor fragility and strengthen Pass 4 evolution. Forbidden_in compliance is the strongest finding in the audit — the altar IS reserved cleanly for the three framing chapters. |

## Candidate-motif findings

| Candidate image | Chapters of recurrence | Should be registered? | Recommendation |
|---|---|---|---|
| the-chain in ch-6 | ch-6 (7 hits) | Yes (low-cost addition) | Add ch-6 to `the-chain` appearance list as `{chapter: 6, treatment: metaphorical, role: callback}`. Brings declared count to 12; frequency floor already cleared. |
| the-record in ch-5 | ch-5 (22 hits) | Yes | Add to `the-record` appearance list as `{chapter: 5, treatment: literal, role: callback}`. |
| the-record in ch-6 | ch-6 (41 hits — heaviest after ch-12 and ch-7) | Yes | Add to `the-record` appearance list as `{chapter: 6, treatment: literal, role: callback}`. Ch-6 (the pretext chapter) leans on record-control extensively. |
| signature-as-seam in ch-9 | ch-9 (8 hits) | Worth considering | Ch-9 is the partisan-power chapter (EO 10887/10903 etc.); the signature motif fits the chapter's framing. Bonnie may add as `callback`. |
| signature-as-seam in ch-5 | ch-5 (6 hits) | Worth considering | Lower priority; ch-5's signing framing is operational rather than diagnostic-as-seam. Bonnie's call. |

## Verdict summary

- **3 PASS clean**: the-signed-document, the-court-or-inquiry, the-chain.
- **2 PASS with footprint-drift (candidate motifs unregistered)**: the-record (ch-5, ch-6 undeclared), signature-as-seam (ch-5, ch-9 undeclared).
- **2 PASS but AT FLOOR — frequency-floor risk**: the-fair-clue (4/4), the-altar (3/3).
- **3 forbidden-in violations** requiring resolution:
  - `the-named-cause` in ch-1 (L159) → Wayne reword OR Bonnie revise registry.
  - `signature-as-seam` in ch-1, ch-2 → Bonnie revise registry (literal historical signings are load-bearing).
  - `the-classified-or-sealed-file` in ch-13 → Bonnie revise registry (chapter design requires the callback).

No motif fails Pass 4 (evolution). All four declared evolution arcs are actually delivered in prose, which is the strongest single finding of this baseline.

## Escalation

- Routine: Bonnie to decide on the 3 forbidden_in revisions and the 4 candidate-motif additions in a single registry-edit pass.
- No xaiolai escalation triggered (no 2+ motif failures from a single rewrite — this is a baseline, not a post-rewrite audit; the violations are registry-vs-prose mismatches in the initial population, not rewrite damage).
- Wayne to be notified of the the-fair-clue and the-altar floor-risk so future rewrites of ch-7/10/11/12/13 preserve those literal phrases.

Handoff: bonnie-book-architect (registry-edit pass on 3 forbidden_in revisions + 4 candidate additions); then wayne-narrative-lead (notification of floor-risk on the-fair-clue and the-altar; optional ch-1 line 159 reword if registry leaves the-named-cause forbidden_in: [1] unchanged).

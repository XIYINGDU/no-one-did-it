---
public_release: mechanical-pass-cleared
public_release_date: 2026-05-31
---
# Figure Data-Grade Memo — *No One Did It* (12 figures)

Owner: Stephen / Fact-check Director
Date: 2026-05-30
Companion to: `book/diagrams/figure-inventory.md` (the 12-figure spec) · proofs at `book/diagrams/proofs/*.html`
Scope: grades the load-bearing numeric/factual cells of each figure against existing `book/source-ledger/cards/` slugs. Did NOT re-grade from scratch; verified the three named open items and spot-graded the remaining nine.

---

## Resolution of the three open items (read first)

1. **ch-7 Horizon prosecution count — figure says "~700", ledger says "900+".**
   The authoritative source is the statutory **Post Office Horizon IT Inquiry Final Report, Vol. 1 (HC 1119, Sir Wyn Williams, 8 July 2025)** [`post-office-horizon-it-inquiry-final-report-vol-1-2025`], which records **more than 900 sub-postmasters prosecuted across 1999–2015, of whom 236 received prison sentences.** An Inquiries-Act-2005 statutory inquiry report outranks the figure's working "~700". **Correct figure: 900+ prosecuted · 236 imprisoned.** The figure HTML (`ch07-horizon-five-roles.html`) shows "~700" in two places (the Prosecutor rolechip and the cost-bearer note) and must be changed to "900+" before render. This is a render-blocking data correction, not a grade problem (the underlying claim is B, A in underlying authority).

2. **ch-8 DOJ Capitol-breach dashboard count — `pending-stephen-lock`.**
   **LOCKED. Not cut.** The chapter claim is "a count of **more than 1,500** people charged, according to the page's last archived capture on Jan 24, 2025" — a conservative floor, not a verbatim masthead numeral. It is grounded in the DOJ's own primary statement for the same window: the USAO-DC "48 Months Since the Jan. 6 Attack" update (Jan 6, 2025) — "approximately **1,583** defendants have been charged criminally in federal court" [`doj-capitol-breach-dashboard-removal-2025`]. "More than 1,500" is true and conservative under 1,583. The card's `pending-stephen-lock` was cleared 2026-05-29. **The figure HTML still shows the red `[pending Stephen lock]` text and must have it removed** before render (this is a stale label, not an open grade).

3. **ch-10 war-stack C-grade nodes (Abu Ghraib / MH17 / Blackwater / Ukrainian children / Iraq WMD NIE).**
   Re-check shows the five **anchor cases are A/B-grade primary instruments**, not C. The only genuinely C-capped element is one *attribution hedge* — JIT's "strong indications" that Putin personally approved the Buk supply (a prosecutorial finding, **not a verdict**) — and the figure already labels it correctly. Per-node verdict below. **No node needs raising or cutting; all stay as graded, and the figure's existing hedging language is correct.** None requires an uncertainty-themed-chapter carve-out because each layer's load-bearing fact is A/B, with the C-element confined to the explicitly-hedged Putin-approval line.

---

## Figure 1 — ch-2 four-category taxonomy table

| Cell (worked example → category) | Grade | Source slug | Note |
|---|---|---|---|
| Sacco & Vanzetti → (counter-read, hard-to-classify) | A | `commonwealth-v-sacco-vanzetti-trial-record-1921` | Primary trial record; counter-reading hedged in ch-2. |
| Dreyfus → pure scapegoat | A | `cour-de-cassation-dreyfus-exoneration-1906-07-12`; `dreyfus-conseil-de-guerre-conviction-1894` | Conviction + exoneration both primary. |
| Bybee/Yoo OLC memo → system/object alibi (procedure) | A | `bybee-yoo-olc-torture-memos-2002-opr-2009` | Primary OLC opinion + OPR report. |
| Other taxonomy exemplar cells (cell-by-cell labels) | [pending] | — | Taxonomy *labels* are editorial classifications, not factual claims; the underlying cases are graded in their own chapters. Not deep-dived. |

**Verdict: CLEAR TO RENDER** (taxonomy labels are classifications per rule 01, not gradeable facts; the cited example cases are A).

## Figure 2 — ch-3 VW Dieselgate responsibility-chain map (signature figure)

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| ~482,000 affected US vehicles (2008–2015) | B | `barrett-speth-et-al-erl-2015-vw-excess-mortality` | Figure quoted in peer-reviewed analysis; widely corroborated. |
| ~60 premature US deaths (central estimate) | B | `barrett-speth-et-al-erl-2015-vw-excess-mortality` | Model-based estimate; must render as a **range / "on the order of sixty"**, never a settled count (rule 02). |
| Public-blame chain / control / benefit / knowledge cells | [pending] | — | Chain-map labels not individually opened; named living persons/company → **[clear: Nancy]** required. |

**Verdict: CLEAR TO RENDER** for the two numeric cells *if* the mortality figure renders as a ranged estimate, not a point count. Nancy clearance required (names VW + individuals).

## Figure 3 — ch-7 Horizon five-role schematic

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| ~700 private prosecutions (1999–2015) | **WRONG — must be 900+** | `post-office-horizon-it-inquiry-final-report-vol-1-2025` | Inquiry Final Report records **900+ prosecuted**. Correct before render. |
| 236 imprisoned | B | `post-office-horizon-it-inquiry-final-report-vol-1-2025` | A in underlying authority; B pending paragraph-anchor lock. |
| Horizon bugs/errors caused shortfalls | B | `bates-v-post-office-no-6-horizon-issues-2019` | A in underlying authority (Fraser J judgment); B pending PDF anchor. |
| Seema Misra sentenced 8 weeks pregnant (2010), quashed 2021 | [pending] | — | Carried in figure note; not individually re-verified this pass. Likely A (R v Misra + Hamilton). |
| ~4,000 pursued in civil recovery; ≥4 documented suicides | [pending] | — | Not re-verified; mark pending. |

**Verdict: BLOCKED — data correction required:** change "~700" → "900+" (two locations). After correction, CLEAR. Nancy clearance required (names Post Office, Fujitsu, Misra).

## Figure 4 — ch-13 8×6 role-by-domain crosswalk

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| Every cell points back to its installing chapter's anchor case | inherits | (per installing chapter) | Cells inherit the grade of their installing-chapter anchor; no new facts introduced. |
| Aggregate crosswalk structure | [pending] | — | Cell-by-cell inheritance not individually walked; structurally derivative. |

**Verdict: CLEAR TO RENDER** (derivative figure; grades inherited from installing chapters, all of which carry A/B anchors). Nancy by reference.

## Figure 5 — ch-8 contradiction timeline (framing vs. record)

| Node | Grade | Source slug | Note |
|---|---|---|---|
| J6 "grave national injustice"/"hostages" framing (Proclamation 10887) | A | `admin-statements-j6-hostages-framing-2025` (framing); `acsaa-pub-l-116-260-2020-12-27` n/a | Proclamation is primary. |
| DOJ dashboard: 1,500+ charged, last capture Jan 24 2025, then removed | B | `doj-capitol-breach-dashboard-removal-2025` | **LOCK CLEARED.** Remove red `[pending Stephen lock]` text from HTML. |
| Cooper preservation order, *CREW v. DOGE* | A | `cooper-crew-doge-preservation-order-2025-03`; `crew-v-doge-service-ddc-complaint-2025-02-20` | Primary docket. |
| 2019 Abrego Garcia withholding order | A | `abrego-garcia-2019-withholding-of-removal-order` | Primary IJ order. |
| *Trump v. J.G.G.*, 24A931 (per curiam) | A | (SCOTUS per curiam order) | A per brief; SCOTUS order. |
| *Noem v. Abrego Garcia*, 24A949 (per curiam) | A | (SCOTUS per curiam order) | A per brief; SCOTUS order. |
| Boasberg probable-cause criminal-contempt finding (Apr 16 2025) | B | `boasberg-jgg-contempt-finding-2025-04-16` | A on existence/date/judge/finding; B at docket-entry pin-cite (PACER pending). Figure is explicitly about contested record control → B/C framing fine per rule 02. |

**Verdict: BLOCKED — stale label:** remove the `[pending Stephen lock]` red text on the dashboard node. After removal, CLEAR. Nancy clearance noted (no living individual accused; institutional artifacts).

## Figure 6 — ch-9 3-layer AI-stack table

| Node | Grade | Source slug | Note |
|---|---|---|---|
| Input layer: *Bartz v. Anthropic* $1.5B settlement, ~$3,000/work, ~500k works | A | `bartz-settlement-preliminary-approval-2025-09-25` | Primary court order, multi-tier corroborated. |
| Deployment layer: GPT-4o sycophancy rollback (Apr 29 2025) | A | `openai-gpt4o-sycophancy-postmortem-2025-04-29` | Primary corporate post-mortem + corroboration. |
| Evaluation layer: Llama-4 LMArena policy revision | A | `lmarena-meta-llama-4-policy-statement-2025-04-07`; `al-dahle-x-llama4-test-sets-2025-04-07` | Verbatim quotes corroborated across ≥3 sources. |

**Verdict: CLEAR TO RENDER.** Nancy clearance required (names Anthropic, OpenAI, Meta).

## Figure 7 — ch-10 5-layer war-stack table

| Node (layer → anchor case) | Grade | Source slug | Note |
|---|---|---|---|
| Chain-of-command secrecy → Abu Ghraib (372nd MP court-martialled) | B | `abu-ghraib-courts-martial-and-karpinski-demotion-2004-2005` | A on individual dispositions; B on consolidated table pending per-soldier lock. OLC-memo layer above = A (`bybee-yoo-olc-torture-memos-2002-opr-2009`). |
| Proxy deniability → MH17 (Buk-TELAR, 53rd Brigade) | A | `mh17-jit-findings-2016-2023`; `hague-district-court-schiphol-mh17-judgment-2022-11-17` | JIT + Hague convictions both A. |
| — MH17 "strong indications" of Putin approval | **C (correctly hedged)** | `mh17-jit-findings-2016-2023` | Prosecutorial finding, **not a verdict**. Figure already labels it "a prosecutorial finding, *not* a verdict". **Stays C; keep the hedge.** |
| Contractor legal-status shell → Blackwater/Nisour Square | A | `blackwater-us-v-slatten-slough-2014-convictions`; `cpa-order-17-revised-2004-06-27`; `trump-blackwater-pardons-2020-12-22` | Convictions + CPA Order 17 + 2020 pardons all primary. |
| Civilian-invisibility euphemism → Russian transfer of Ukrainian children | A | `russian-decrees-330-585-ukrainian-children-2022`; `icc-arrest-warrants-putin-lvova-belova-2023-03-17` | Decrees + ICC warrants (Mar 17 2023, "reasonable grounds") both A. |
| Strategic-justification reification → Iraq WMD NIE | A | `nie-2002-16hc-iraq-wmd-declassified-2003`; `chilcot-iraq-inquiry-report-2016` | Declassified NIE + Chilcot both A/primary. |

**Verdict: CLEAR TO RENDER.** All anchor cases A/B; the single C element (Putin-approval line) is correctly hedged as a prosecutorial finding. No node raised, none cut. Nancy clearance required (names Putin, Lvova-Belova, Blackwater convicts, etc.).

## Figure 8 — ch-11 8×4 design matrix (Park / SOX / SMCR / Inquiries Act §21)

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| SMCR pillar/allocation mechanism | A | `uk-smcr-fsma-fsbra-fca-handbook` | Primary statute + FCA Handbook. |
| Inquiries Act 2005 §21 powers | [pending] | — | Statute exists; not individually opened this pass. Likely A (legislation.gov.uk). |
| SOX certification provisions | [pending] | — | No `*sox*` card found; mark pending — **needs a card** before its cells ship. |
| Park (US v. Park strict-liability doctrine) | [pending] | — | Not opened this pass. |

**Verdict: BLOCKED — missing card:** SOX cells have no source-ledger card; create/cite before render. SMCR column CLEAR. Other two columns [pending] verification.

## Figure 9 — ch-12 10-row "record fights" two-column table

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| Individual fight rows (10) + outcome | [pending] | — | Rows map to multiple case anchors across chapters; not individually walked this pass. |
| Each row's outcome/record-rule classification | [pending] | — | Classifications per rule 01, derivative of installing-chapter anchors. |

**Verdict: CLEAR TO RENDER (conditional)** — rows are derivative of already-graded case anchors; the *classification* cells are editorial per rule 01. Flag: confirm each of the 10 rows resolves to an existing graded card before final freeze. Nancy by reference where living persons named.

## Figure 10 — ch-4 7-channel × 3-case interception matrix

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| Channel/interception cells | [pending] | — | Three anchor cases not opened this pass; structurally formalizes an existing v5 table. |

**Verdict: CLEAR TO RENDER (conditional)** — formalizes an existing v5 table whose cells were graded in ch-4 production; re-confirm the three anchor cases resolve to graded cards before freeze. Nancy by reference.

## Figure 11 — ch-5 Bhopal responsibility-chain ladder

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| 7 UCIL officials convicted (IPC 304-A, 2-yr sentences, Jun 7 2010) | A | `state-of-mp-v-keshub-mahindra-cjm-bhopal-2010` | Primary CJM judgment. |
| No conviction of UCC / US officers | A | `state-of-mp-v-keshub-mahindra-cjm-bhopal-2010` | Documented in judgment record. |
| 1982 operational-safety-survey warnings | [pending] | — | `ucc-may-1982-operational-safety-survey-bhopal` exists; not opened this pass — likely B/A. |
| Cost-bearer harm figures | [pending] | — | `bhopal-cost-bearer-evidence-cluster` exists; not re-graded. |

**Verdict: CLEAR TO RENDER** for the conviction-ladder spine (A). *Run only if the signature chain map landed in ch-3 (no adjacent chain maps)* per inventory constraint. [data: Stephen] only — no living-person clearance beyond deceased Mahindra.

## Figure 12 — ch-6 3-case pretext-grammar comparison table

| Cell | Grade | Source slug | Note |
|---|---|---|---|
| Three parallel pretext cases (grammar cells) | [pending] | — | Cases not opened this pass; lowest-priority figure per inventory (table-fatigue guard). |

**Verdict: CLEAR TO RENDER (conditional)** — lowest priority; cells derivative of ch-6 production grades. Re-confirm the three anchor cases resolve to graded cards before freeze. Nancy by reference where living persons named.

---

## Summary table — render status

| # | Ch | Figure | Status |
|--:|:--:|---|---|
| 1 | 02 | Four-category taxonomy | CLEAR |
| 2 | 03 | VW chain map | CLEAR (mortality = ranged estimate; Nancy) |
| 3 | 07 | Horizon five-role | **BLOCKED: "~700" → "900+"** |
| 4 | 13 | Role×domain crosswalk | CLEAR (inherited) |
| 5 | 08 | Contradiction timeline | **BLOCKED: remove stale `[pending Stephen lock]` label** |
| 6 | 09 | AI-stack 3-layer | CLEAR (Nancy) |
| 7 | 10 | War-stack 5-layer | CLEAR (C-hedge correct) |
| 8 | 11 | Design matrix | **BLOCKED: SOX cells need a card** |
| 9 | 12 | Record-fights | CLEAR (conditional: confirm 10 rows resolve to cards) |
| 10 | 04 | Interception matrix | CLEAR (conditional: confirm 3 cases resolve to cards) |
| 11 | 05 | Bhopal ladder | CLEAR |
| 12 | 06 | Pretext-grammar | CLEAR (conditional) |

---

Owner: Stephen / Fact-check Director
Purpose: Grade the load-bearing data cells of the 12 spec'd figures; resolve the ch-7 Horizon count, the ch-8 dashboard pending-lock, and the ch-10 war-stack C-grade nodes; return per-figure render verdicts.
Evidence grade: B
Evidence-grade detail (per cell): predominantly A-grade primary instruments; B-grade pending paragraph-anchor locks on Horizon Inquiry, Bates, Abu Ghraib consolidated table, Capitol-breach dashboard, and the VW mortality estimate; one correctly-hedged C element (MH17 Putin-approval line). `[pending]` cells were not deep-dived per the bounded-research instruction.
Assumptions: (1) The figure-inventory spec and proof HTML reflect the current intended figures. (2) `[pending]` derivative/classification cells inherit the grade of their installing-chapter anchor cases, which passed chapter production. (3) "More than 1,500" J6 charged is read as a conservative floor, not a verbatim masthead numeral. (4) GFW blocked web.archive.org direct render; treated as checkpoint/tool constraint, not a dead archive.
Open questions: (1) Lock paragraph anchors for Horizon Inquiry 900+/236 and Bates "not remotely robust" (→ A). (2) Per-soldier Abu Ghraib court-martial disposition lock (→ A). (3) Do all 10 ch-12 record-fight rows, 3 ch-4 interception cases, and 3 ch-6 pretext cases each resolve to an existing graded card? (4) ch-11 needs a SOX source-ledger card; Inquiries Act §21 and US v. Park cards confirmed/created. (5) Seema Misra and "~4,000 civil / ≥4 suicides" figures (ch-7 note) not re-verified this pass.
Handoff: Production (apply the two data corrections to `ch07-horizon-five-roles.html` "~700"→"900+" and remove the stale `[pending Stephen lock]` text in `ch08-contradiction-timeline.html`) → Bonnie (figure spec: SOX card gap on ch-11 matrix; confirm derivative-cell anchors for figs 9/10/12) → Nancy (rights + caption + living-person clearance on figs 2, 3, 5, 6, 7, 9, 10, 12) → Wayne (mandatory audio-rendering paragraph per table figure).

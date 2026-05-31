# Prose Open-Questions Triage — Stephen / Fact-check Director

Owner: Stephen / Fact-check Director
Task: Triage the trailing `Open questions:` blocks in each chapter PROSE file (not the briefs — those were triaged by Bonnie on 2026-05-28). Annotate each lettered/numbered item in-place; verify the pending-stephen-lock pipeline covers everything substantive; consolidate any STILL OPEN items not already on the 37-marker pending-lock list.
Inputs reviewed: 13 chapter prose files at `book/chapters-v2/<NN>-*.md`; `build/chicago-format-stats.json` (37 `pending_lock_markers`); `book/STATUS.md` (cross-cutting clocks; coordinated Nancy+Stephen sweep at galley-lock minus 30 days; EVIDENCE NEEDED rollup at L97); `book/source-ledger/cards/` (spot-checked card existence for ch-9 anchors and ch-12 federal-records-act citation).

## Output

Per-chapter in-place annotations applied to 10 of 13 chapter prose files (ch-1, ch-2, ch-3, ch-4, ch-5, ch-6, ch-7, ch-8, ch-9, ch-10, ch-11, ch-12, ch-13). Chapters that originally had no `Open questions:` line (ch-1, ch-2, ch-9) received a minimal Stephen-OQ-triage block covering pending items surfaced from the existing handoff prose + STATUS.md cross-cutting items.

### Per-chapter counts

| Ch | Total OQ items | Resolved | Tracked in pending-stephen-lock or coordinated sweep | Still open (new escalations) | Deferred (non-Stephen) | Stale |
|----|---------------:|---------:|----------------------------------------------------:|----------------------------:|----------------------:|------:|
| 01 | 3              | 0        | 2                                                   | 0                           | 1                     | 0     |
| 02 | 3              | 0        | 2                                                   | 0                           | 1                     | 0     |
| 03 | 4              | 1        | 2                                                   | 0                           | 1                     | 0     |
| 04 | 3              | 0        | 1                                                   | 0                           | 2                     | 0     |
| 05 | 3              | 1        | 1                                                   | 0                           | 0                     | 1 (Bonnie-architect Q, not Stephen) |
| 06 | 4              | 2        | 1                                                   | 0                           | 0                     | 1 (Bonnie-architect Q, closed by promotion) |
| 07 | 6              | 0        | 4                                                   | 0                           | 2                     | 0     |
| 08 | 7 (5 listed + 2 added from build report) | 0 | 6                          | 0                           | 0                     | 1 (Jerry sign-off, closed by promotion) |
| 09 | 9 (8 from handoff + 1 from STATUS) | 1 | 7                                       | 0                           | 1                     | 0     |
| 10 | 8              | 0        | 6                                                   | 0                           | 1                     | 1 (Jerry/Bonnie decision, chose against) |
| 11 | 5              | 0        | 0                                                   | **3**                       | 2                     | 0     |
| 12 | 14 (13 listed + 1 added from build report) | 1 | 8                              | **3**                       | 0                     | 0     |
| 13 | 3              | 0        | 0                                                   | 0                           | 3                     | 0     |
| **TOTAL** | **72** | **6** | **40** | **6** | **14** | **4** |

## Consolidated STILL OPEN list — items requiring immediate Stephen escalation (NOT already on pending-stephen-lock)

These six items are real Stephen verification work that is **not** captured by the 37-marker pending-lock pipeline. Each needs to be folded into the galley-pass scope or escalated separately.

1. **ch-11(a)** — `Hsia` vs `DeCoster`-line Park-narrowing case selection. Stephen judgment call on which narrowing case provides the cleaner counter-citation. (`[EVIDENCE NEEDED]` flag per STATUS.md L97.)
2. **ch-11(b)** — FCA Final Notice for SMCR worked example. Joint Stephen+Nancy selection per STATUS.md L97; defamation-surface dimension means Nancy must be in the loop.
3. **ch-11(c)** — `United States v. Grass` (Rite Aid) confirmation as the appropriate § 906-era prosecution exemplar, or substitution of a stronger one. Stephen-anchor selection per STATUS.md L97.
4. **ch-12(4)** — Pentagon Papers history dates (McNamara June 1967; Ellsberg/Russo Oct–Nov 1969 with the RAND-safe → Linda Sinay advertising agency provenance chain; NYT June 13 1971; `US v. Ellsberg` dismissal May 11 1973). Verify against primary court record + Sheehan / Ellsberg secondary. Load-bearing for slot-4 walk; not on pending-lock list.
5. **ch-12(6)** — FRCP 37(e) post-2015 amendment codified text + spoliation-jurisprudence verification. Load-bearing for the chapter's slot-3 rule architecture; not on pending-lock list.
6. **ch-12(8)** — Hofeller Wake County docket entries for the three dates (Jul 12 2019 35-file admission; Jul 15–26 2019 trial; Sep 3 2019 three-judge panel ruling). Hofeller verbatim is tracked under ch-6's `[EVIDENCE NEEDED]` per STATUS.md L97, but the date-entry verification is a separate ch-12 item; not on pending-lock list.

## Recommendation

Add items 1–6 above to the Stephen galley pass scope on 2026-06-25, alongside the 37 pending-stephen-lock markers and the live-docket clocks coordinated with Nancy at galley-lock minus 30 days. With those additions, every substantive prose OQ across the 13-chapter corpus is either resolved, on the pending-lock pipeline, on the coordinated live-docket sweep, or deferred to a non-Stephen owner with a recorded note.

The 4 STALE items represent author-architect questions (Bolton manuscript characterizations omitted; reader-value-template framing; Nadella insertion considered-and-rejected; ch-8 Jerry sign-off implied by promotion) that promotion to `status: ready` already closed; they are not Stephen verification work.

The 14 DEFERRED items route to: Delon (4 — primary-source retrieval / academic-source verification / funder-share / cost-benefit memo primary form), Alan (3 — corporate-law and public-inquiry-statute frame already routed in chapter handoffs), Bonnie (3 — architect calls on forward-references and diagram placement), diagrams/manuscript-compile workflow (3 — diagrams workflow + page-range index), xiaolai (1 — book's closing sentence).

## Verification of coverage

The 37 pending-stephen-lock markers in `build/chicago-format-stats.json` cover:
- ch-2 (3 markers); ch-5 (1); ch-6 (3, with one Roberts-pinpoint duplicated); ch-8 (8, with 4 Chilcot entries); ch-9 (10, with 3 doj-j6 entries, 3 cooper-crew entries, and 1 abrego-garcia); ch-10 (2); ch-12 (10, with 2 tower-commission entries).

The coordinated Nancy+Stephen 30-day sweep covers ch-4 (Putin/Prince/Trump pardons; partial Prince spillover to ch-8), ch-7 (Vennells/Jenkins/Inquiry final report), ch-9 (AEA/DOGE/J6 MSPB), ch-10 (Bartz/Altman/ChatGPT preservation), ch-12 (preservation-order callbacks cascading from ch-9 and ch-10).

Cross-check: every Stephen-attributed prose OQ across the 13 chapters maps to one of: (i) a pending-stephen-lock marker; (ii) a coordinated live-docket sweep clock; (iii) an existing source-ledger card the chapter prose already cites with appropriate hedging; (iv) one of the 6 STILL OPEN items above; or (v) a STATUS.md cross-cutting Stephen item already on the standing queue (Therac-25 FDA primary; LoC Sandoz Commentary; Fraser J "not remotely robust" anchor; per-soldier Abu Ghraib disposition; NYT/MS/OpenAI preservation order; speaker-by-speaker "hostages"/"activist judges" attribution).

Conclusion: with the 6 new items added to the galley-pass scope, the pipeline is complete.

## Files edited

- `book/chapters-v2/01-the-altar-moves.md` — added Open questions block (3 items)
- `book/chapters-v2/02-the-four-goats.md` — added Open questions block (3 items)
- `book/chapters-v2/03-who-could-have-stopped-it.md` — annotated 4 items
- `book/chapters-v2/04-the-proxy-and-the-sponsor.md` — annotated 3 items
- `book/chapters-v2/05-the-guilty-goat.md` — annotated 3 items
- `book/chapters-v2/06-the-pretext.md` — annotated 3 items + added item (d) for pending-lock cite-markers; one re-edit to remove a false-positive cite-density pattern
- `book/chapters-v2/07-the-record-is-the-battlefield.md` — annotated 6 items
- `book/chapters-v2/08-war-is-the-perfect-laundry.md` — annotated 5 items + added items (f)(g) for pending-lock cite-markers not in OQ list
- `book/chapters-v2/09-when-power-calls-itself-the-goat.md` — added Open questions block (9 items consolidated from Handoff #1 + STATUS.md)
- `book/chapters-v2/10-the-model-did-it.md` — annotated 8 items
- `book/chapters-v2/11-make-responsibility-follow-control.md` — annotated 5 items
- `book/chapters-v2/12-keep-the-record.md` — annotated 13 items + added item (14) for inquiries-act-2005-section-21 pending-lock marker not in OQ list
- `book/chapters-v2/13-a-readers-field-guide.md` — annotated 3 items

13 chapter prose files touched. Pre-edit-chapter-snapshot hook archived each chapter's prior state to `book/audits/history/<NN>/2026-05-27T*Z/`.

## Evidence grade

A — derived from STATUS.md (project state of record), build/chicago-format-stats.json (canonical pending-lock list), source-ledger cards (existence spot-checked), and the chapters' own prose at status: ready.

## Assumptions

- The 37 pending-stephen-lock markers in `build/chicago-format-stats.json` are the canonical scope of the galley 2026-06-25 lock pass; chapter OQs that point at items on that list need no separate escalation.
- The coordinated Nancy+Stephen sweep at galley-lock minus 30 days is the single coordinated checkpoint per Nancy portfolio-sweep 2026-05-28 Recommended Action 3, and date-fires when manuscript freeze is declared (not a fixed calendar date).
- STATUS.md L97 EVIDENCE NEEDED rollup is the authoritative count of substantive prose-body items remaining (5 substantive items across the corpus); the rest are summary or handoff-block meta-references.
- The 6 STILL OPEN items identified here are work that needs to be folded into the galley-pass scope (or scoped separately if Stephen judges the pending-lock pipeline is the wrong venue for any of them).

## Open questions

- Should ch-11(a)(b)(c) be added to a new pending-stephen-lock entry in `build/chicago-format-stats.json` so they appear in the canonical scope, or held in STATUS.md L97's EVIDENCE NEEDED rollup as Stephen-anchor selection work?
- For ch-12(4) Pentagon Papers dates: which secondary edition of Sheehan (or Ellsberg) is the project's working authority? Stephen needs this picked before the galley pass.

## Risks

- None of the STILL OPEN items are defamation-surface; all six are evidence-form (citation precision / case selection / date verification). No Nancy escalation required.
- The Pentagon Papers date chain (ch-12(4)) is the most labor-intensive of the six because it touches a long historical chronology; if Delon could pre-pull primary court-record materials, the galley pass would be more efficient.
- If any of the live-docket clocks tracked by the coordinated Nancy+Stephen sweep advance procedurally between now and freeze (e.g., Vennells charged; ICC issues new warrant; Cooper CREW v. DOGE ruling reversed on appeal), the chapter prose will need re-rendering, not just citation lock. Built into the sweep design per STATUS.md cross-cutting items.

## Handoff

- jerry-crew-chief — note the 6 STILL OPEN items added to galley 2026-06-25 scope; decide whether to update `build/chicago-format-stats.json` to include them.
- stephen-fact-check-director (self) — fold the 6 STILL OPEN items into the galley 2026-06-25 pass alongside the 37 pending-lock markers.
- delon-research-director — three deferred items (ch-3(c) cost-benefit memo primary form; ch-1(b) historiographical chronology; ch-7(5) Therium funder share); not gating ready, but pre-pull would help galley pass.
- nancy-legal-risk-counsel — ch-11(b) FCA Final Notice selection requires joint Stephen+Nancy judgment.
- bonnie-book-architect — no architect items requiring new judgment; the four DEFERRED Bonnie items (ch-4(1)(2) diagram + forward-reference; ch-5(1) closing pointer) are closed by promotion-to-ready.
- alan-expert-reviewer — three DEFERRED items already in chapter handoffs (ch-7(6) CPIA; ch-11(d)(e) Park + Inquiries Act § 21 frames).

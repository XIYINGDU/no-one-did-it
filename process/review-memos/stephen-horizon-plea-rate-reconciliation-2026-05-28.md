---
owner: stephen-fact-check-director
created: 2026-05-28
trigger: nancy-portfolio-sweep-2026-05-28 V7 severity-evidence-mismatch flag
status: resolved
resolution_class: (b) — different denominators / measurement dates; both figures correct
public_release: mechanical-pass-cleared
public_release_date: 2026-05-31
---

# Reconciliation memo — "Horizon plea-rate" flag (actually Bartz v. Anthropic claims-rate)

Owner: Stephen / Fact-check Director
Task: Reconcile the 92.77% / 91.3% numeric discrepancy flagged by Nancy's
2026-05-28 portfolio sweep as V7 severity-evidence-mismatch on an A-grade
anchor.

## What the sweep flagged vs. what was actually wrong

The dispatch brief identified the flagged claim as:

> "ch-07 prose (book/chapters-v2/07-the-record-is-the-battlefield.md)
> carries plea-rate figure of '92.77%'; source-ledger card carries '91.3%';
> both purport to derive from Hamilton v Post Office + Williams Inquiry"

This routing was incorrect on every load-bearing element:

| Element | Dispatch brief said | Actual state |
|---|---|---|
| Chapter | ch-07 (Horizon) | ch-10 (`book/chapters-v2/10-the-model-did-it.md`, line 131) |
| Metric | plea rate | settlement claims rate (works claimed / Works List) |
| Case | Post Office Horizon | Bartz v. Anthropic PBC |
| Source documents | Hamilton EWCA Crim 577 + Williams Inquiry | Bartz docket + Class Counsel filings + Authors Alliance |
| Card | not specified; suggested `hamilton-post-office-ewca-crim-577-2021` / `post-office-horizon-it-inquiry-williams` / `bates-v-post-office-no-6-horizon-issues-2019` | `bartz-v-anthropic-fairness-hearing-2026-05-14.md` |

Chapter 7 carries no plea-rate percentage figure at all. It carries
aggregate-count figures only ("more than 900 sub-postmasters were
prosecuted, with 236 receiving prison sentences") and these are cited
to the Williams Inquiry Final Report Volume 1 (7 July 2025). The
chapter's Hamilton-court quotation ("all the guilty pleas of the
successful appellants ... were founded upon Post Office Ltd's failures
of investigation and disclosure"; "may have felt they had no real
alternative but to plead guilty") is verbatim per `[2021] EWCA Crim 577`
and carries no percentage. No reconciliation needed for ch-07.

The actual V7 surface lives in ch-10. Reconciliation below addresses
the real discrepancy on the Bartz card.

## The Bartz v. Anthropic claims-rate reconciliation

### The numeric series

The Bartz v. Anthropic class settlement's claims-rate metric is
**works claimed of the Works List** (not claimants of class
membership; this distinction matters and is acknowledged in the
Authors Alliance commentary). The Class Counsel reported three
sequential snapshots:

| As of | Rate | Source | Works claimed of Works List |
|---|---|---|---|
| 19 March 2026 | 54% | Motion for final approval (19 March 2026) | not disclosed in publicly available summary |
| 16 April 2026 (filed); referenced as 30 April status in pre-hearing article | 91.3% | Class Counsel updated claims report (16 April 2026) | 440,490 of 482,460 |
| 14 May 2026 (day of hearing) | 92.77% | Class Counsel oral report at the fairness hearing | 447,576 of the Works List |

The 91.3% figure is the title of the Authors Alliance pre-hearing
article: "Bartz v. Anthropic Fairness Hearing: Final Reminder,
**91.3% Claims Rate**, and updates from the Docket" (Authors Alliance,
14 May 2026, archived at web.archive.org/web/20260515051333/...).
The article body describes 91.3% as the most recent Class Counsel
filing figure at the time the article was prepared.

The 92.77% figure is the updated Class Counsel report given in
open court at the 14 May 2026 fairness hearing. It is corroborated
by:

- Authors Alliance post-hearing Substack observations (May 2026):
  "Class Counsel reported that the claims rate, which stood at 91.3%
  as of the April 30 update, is now 92.77%."
- Words and Money hearing coverage ("Anthropic Settlement Appears
  to Cruise Through Its Final Fairness Hearing").
- Publishers Weekly hearing report ("Little Drama at Anthropic's
  Settlement Hearing").

### Resolution class

**(b) — figures derive from different measurement dates; both are
correct.** No prose edit required. Card updated to document the
measurement-date series and reconcile the title-vs-body apparent
inconsistency.

### What was actually changed

- **Chapter prose (`book/chapters-v2/10-the-model-did-it.md`):** no
  change. The sentence "The hearing recorded a claims rate of
  approximately 92.77% and 350 valid opt-outs covering 1,802 works"
  is correct: 92.77% is the day-of-hearing Class Counsel figure
  attributed by venue ("at the hearing").
- **Source-ledger card (`book/source-ledger/cards/bartz-v-anthropic-fairness-hearing-2026-05-14.md`):**
  - `claim.text` field expanded to specify the day-of-hearing
    measurement moment and the 91.3% → 92.77% trajectory.
  - Added `claim.claims_rate_reconciliation` block with the three
    sequential snapshots, source attribution for each, and a
    standing explanation of the title-vs-body apparent
    inconsistency.
  - Added `verification.grade_rationale` clarification of why the
    two figures are sequential snapshots, not a discrepancy.
  - Added `verification_log` step `claims-rate-reconciliation` with
    today's date, tools used, and outcome.
  - Card title (`source.title`) left unchanged: it quotes the
    Authors Alliance article title verbatim, and rule 06 forbids
    silent alteration of quoted source titles.

### Why the card was internally inconsistent before today

The card was created 2026-05-26 from a single 14 May 2026 Authors
Alliance update. The article's title carried 91.3% (the most recent
filed-document figure as of the article's preparation), while the
article body's day-of-hearing reporting carried 92.77%. The card's
`source.title` faithfully copied the article title; the card's
`claim.text` faithfully copied the day-of-hearing figure. The result
was an internally inconsistent card with no on-card explanation of
the relationship between the two numbers. That is the V7 surface
Nancy correctly identified, even though it surfaced inside a single
A-grade card rather than across a card-prose mismatch.

Output: card reconciled; ch-10 prose validated as already correct;
ch-07 confirmed to carry no plea-rate percentage figure.

Evidence grade: A. The 92.77% day-of-hearing figure is corroborated
across three independent post-hearing sources (Authors Alliance
Substack, Words and Money, Publishers Weekly). The 91.3% filed-figure
is corroborated by the original Class Counsel 16 April 2026 claims
report and the Authors Alliance pre-hearing article. The two figures
together form a documented sequence, not a conflict.

Assumptions:
- The Authors Alliance Substack's "92.77%" is the Class Counsel oral
  report from open court, not a separately-derived figure.
- "Claims rate" in all three snapshots refers to works claimed of
  the Works List (482,460 works), not claimants of class
  membership. This is consistent across all sources reviewed.
- Nancy's dispatch routing-to-ch-07 was a clerical misrouting of a
  ch-10 finding, not a separate ch-07 V7 surface.

Open questions:
- Whether Class Counsel filed a written supplement after the 14 May
  hearing memorialising the 92.77% figure on the docket; if so, the
  card should also cite that filing as a primary-document corroboration
  (currently the figure rests on three secondary-source reports of the
  open-court statement, which is sufficient for grade A but
  primary-document corroboration would strengthen it). Worth checking
  at the 11 June 2026 distribution-calculation milestone if the docket
  has updated.
- Whether the dispatch routing-to-ch-07 reflects a Nancy-portfolio-sweep
  cataloguing error or a category-of-error in the portfolio-sweep
  artifact itself; flag for Nancy to cross-check her sweep memo.

Risks:
- If the 11 June 2026 final-approval order issues, this card will be
  superseded; the chapter prose's "took the matter under submission"
  language will go stale. Per the card's own carry-forward note, a
  successor card will be created and this one's `dispute.status`
  moved to `superseded-by`. The 92.77% figure as a snapshot-of-a-moment
  remains correct historically regardless of any later claims-rate
  update.

Handoff:
- nancy-legal-risk-counsel — please cross-check the dispatch
  routing-to-ch-07 against your 2026-05-28 portfolio sweep memo and
  confirm whether ch-07 was conflated with ch-10 in the sweep or
  whether a separate ch-07 finding remains unaddressed. The ch-10
  V7 surface is resolved on this memo.
- jerry-crew-chief — for awareness; no action required unless Nancy's
  cross-check surfaces an additional ch-07 item.

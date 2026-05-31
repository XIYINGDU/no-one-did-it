---
id: wang-order-chatgpt-log-preservation-2025-05-13
source:
  title: Order directing OpenAI to preserve and segregate output log data, The New York Times Company v. Microsoft Corporation et al., Case No. 1:23-cv-11195 (S.D.N.Y.)
  type: court-order
  publisher: United States District Court, Southern District of New York
  author: Magistrate Judge Ona T. Wang
  publication_date: 2025-05-13
  url: https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551
  archive:
    wayback_url: http://web.archive.org/web/20260416015333/https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551
    wayback_captured: '2026-04-16'
  access_constraint: open-web
claim:
  text: On 13 May 2025, U.S. Magistrate Judge Ona T. Wang of the Southern District of New York directed OpenAI to preserve and segregate all output log data that would otherwise be deleted on a going-forward basis until further order of the court, in The New York Times Company v. Microsoft Corporation et al., Case No. 1:23-cv-11195. The order overrode OpenAI's standard ChatGPT conversation-log retention policy for purposes of the litigation. OpenAI's motion for reconsideration was denied 16 May 2025 (Document 559). Subsequent 2025 orders modified scope and required production of 20 million de-identified consumer ChatGPT logs by 14 November 2025.
  quote_alteration: none
  quote_permission: not-applicable
verification:
  evidence_grade: A
  grade_rationale: 'The preservation order is a primary court document on the public docket of the Southern District of New York (Case 1:23-cv-11195, Document 551, filed 13 May 2025). The order text is publicly accessible via Justia Dockets and CourtListener. Multiple legal-tier-1 secondary sources (Bloomberg Law, Jones Walker LLP analysis, Loeb & Loeb commentary, National Law Review) cite the order with the same date and operative directive. Tier-1 primary court document corroborated by tier-2 legal commentary reaches A-grade.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551
      status: forbidden
      http_code: 403
      error: HTTP 403 Forbidden
    archive:
      url: http://web.archive.org/web/20260416015333/https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  tool: WebSearch
  outcome: PASS
  notes: Justia docket entry confirms order at Document 551 in Case 1:23-cv-11195, dated 13 May 2025. PDF of Wang's 16 May 2025 reconsideration-denial order (Document 559) corroborates the 13 May 2025 preservation order. Bloomberg Law, Jones Walker, Loeb & Loeb, and National Law Review independently report the 13 May 2025 date.
- step: independent-corroboration
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Four independent legal-tier-1 and tier-2 secondary sources corroborate the 13 May 2025 order and its operative text.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: Primary court order with multi-source corroboration.
- step: dispute-adjudication
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: NOTE
  notes: Chapter 10 line 61 currently reads 'order of Magistrate Judge Wang, Nov 14 2024 as modified by subsequent 2025 orders'. The 14/15 November 2024 date in the public record corresponds to the date News Plaintiffs became aware that OpenAI was not preserving relevant output log data — it is the awareness date, NOT a court-order date. The first formal court order directing preservation is the Wang order of 13 May 2025 (Document 551). Subsequent 14 November 2025 events relate to OpenAI's compliance with production of 20 million de-identified logs. Chapter prose at line 61 carries an internal note ('Stephen to lock exact text') flagging this gap; recommend revising chapter prose to cite the 13 May 2025 Wang preservation order and, separately, the 14 November 2025 production milestone.
dispute:
  status: contested
  notes: 'The card itself is undisputed on the public-record level (the 13 May 2025 Wang order exists and is publicly accessible). The ''contested'' status flag is operational — chapter 10 prose currently dates the order ''Nov 14 2024'', which the public record does not support as a court-order date. Recommend: chapter prose revision to align with the documented 13 May 2025 preservation order and the 14 November 2025 production-order date. Open question carried forward to Wayne (chapter revision) and Jerry (audit-gate sign-off).'
defamation:
  living_subjects:
  - Ona T. Wang
  nancy_cleared: true
  nancy_cleared_on: 2026-05-26
  nancy_notes: Judge Ona T. Wang is named in judicial capacity as the issuing Magistrate Judge. Factual reference to docket conduct only; no unfavorable conduct attributed; the order is a public court document. Inherits ch-10 Nancy gate clearance from chapter promotion 2026-05-26.
references:
  cases_affected:
  - ai-training-data-litigation
  chapters_citing:
  - 09-the-model-did-it
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# Wang preservation order for OpenAI output log data, 13 May 2025

The card anchors the chapter-10 claim (line 61) that, in the *NYT v. Microsoft / OpenAI* litigation, a court order required preservation of ChatGPT output logs that would otherwise have been deleted under OpenAI's standard retention policy.

## Why this card exists

Chapter 10 line 61 carries the CITE marker `[CITE: order of Magistrate Judge Wang, Nov 14 2024 as modified by subsequent 2025 orders; Stephen to lock exact text]`. Resolution 2026-05-26: the public record supports a Wang preservation order dated **13 May 2025** (Document 551), with a reconsideration denial on 16 May 2025 (Document 559). The 14/15 November 2024 date in the public record is the date News Plaintiffs became aware OpenAI was not preserving relevant output log data — the awareness event, not a court order. A subsequent 14 November 2025 date relates to OpenAI's compliance with the production of 20 million de-identified logs.

## Carry-forward state — chapter prose revision required

The chapter prose at line 61 reads "the November 2025 discovery order required OpenAI to preserve output log data including ChatGPT conversation logs that had been scheduled for deletion under the company's standard retention policy" — this is broadly consistent with the documented record at a high level, but the CITE marker's "Nov 14 2024" date is not supported. Recommend:

- Revise CITE marker to read: `[CITE: order of Magistrate Judge Ona T. Wang directing preservation of OpenAI output log data, 13 May 2025 (Document 551 in Case 1:23-cv-11195, S.D.N.Y.); subsequent production order requiring 20 million de-identified ChatGPT logs, November 2025]`
- Or, if the chapter wishes to preserve the 14 November date, retarget to the **2025** production-order context (14 November 2025), not 2024.

Handoff: wayne-narrative-lead (chapter prose alignment) → jerry-crew-chief (audit-gate sign-off before status: ready re-promotion).

## Diagnostic significance

The order is the chapter's worked example of a court compelling production from inside the lab's record-control envelope. The discovery channel is the third instrument in the input-layer interception triplet the chapter installs in slot 9.

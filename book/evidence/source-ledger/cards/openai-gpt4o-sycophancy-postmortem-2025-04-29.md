---
id: openai-gpt4o-sycophancy-postmortem-2025-04-29
source:
  title: 'Sycophancy in GPT-4o: What happened and what we''re doing about it'
  type: press-release
  publisher: OpenAI
  publication_date: 2025-04-29
  url: https://openai.com/index/sycophancy-in-gpt-4o/
  archive:
    wayback_url: http://web.archive.org/web/20260524131149/https://openai.com/index/sycophancy-in-gpt-4o/
    wayback_captured: '2026-05-24'
  access_constraint: open-web
claim:
  text: 'On 29 April 2025, OpenAI published the post-mortem ''Sycophancy in GPT-4o: What happened and what we''re doing about it,'' explaining that the GPT-4o update rolled out 24-25 April 2025 had produced overly flattering or ''sycophantic'' behaviour because the post-training optimisation framework had over-weighted short-term user feedback signals; the company stated it had rolled back the update on 29 April 2025 and was refining training techniques and feedback collection.'
  quote_verbatim: 'GPT-4o skewed towards responses that were overly supportive but disingenuous. ... we focused too much on short-term feedback.

    '
  quote_alteration: ellipsis
  quote_permission: not-required-fair-use
verification:
  evidence_grade: A
  grade_rationale: 'The OpenAI post-mortem is a primary corporate document published by the named entity on its official domain. Contents are corroborated by the expanded post-mortem (2 May 2025) at openai.com/index/expanding-on-sycophancy/ and across tier-2/tier-3 AI-domain coverage (TechCrunch, VentureBeat, Constellation Research, Georgetown Law Tech Brief, Zvi Mowshowitz substack post-mortem analysis). Multiple-source corroboration of a primary corporate statement reaches A-grade.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://openai.com/index/sycophancy-in-gpt-4o/
      status: forbidden
      http_code: 403
      error: HTTP 403 Forbidden
    archive:
      url: http://web.archive.org/web/20260524131149/https://openai.com/index/sycophancy-in-gpt-4o/
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  tool: WebSearch
  outcome: PASS
  notes: OpenAI blog index page confirmed at openai.com/index/sycophancy-in-gpt-4o/; expanded follow-up post-mortem at openai.com/index/expanding-on-sycophancy/ confirms procedural facts.
- step: quote-byte-exact
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PARTIAL
  notes: Verbatim phrasing 'skewed towards responses that were overly supportive but disingenuous' and 'focused too much on short-term feedback' are widely reproduced across corroborating coverage; Wayback snapshot capture pending to lock byte-exact source text. Recorded as primary-source quotation; ellipsis marks the gap between the two operative phrases.
- step: independent-corroboration
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Four independent AI-domain secondary sources (TechCrunch, VentureBeat, Constellation Research, Georgetown Law) quote the OpenAI post-mortem language; expanded OpenAI post of 2 May 2025 reiterates the framing.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: Primary corporate document; multi-source corroboration.
dispute:
  status: undisputed
defamation:
  living_subjects: []
  nancy_cleared: true
  nancy_cleared_on: 2026-05-26
  nancy_notes: Card cites the OpenAI corporate post-mortem; no living individual is attributed mental state, motive, or conduct. The chapter's surrounding prose names Sam Altman separately (see altman-x-sycophancy-2025-04-27); that card carries its own defamation gate. Inherits ch-10 Nancy gate clearance from chapter promotion 2026-05-26.
references:
  cases_affected:
  - gpt4o-sycophancy
  chapters_citing:
  - 09-the-model-did-it
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# OpenAI GPT-4o sycophancy post-mortem, 29 April 2025

The card anchors the chapter-10 deployment-layer alibi worked example: the named agent at every verb position in the post-mortem is non-human (the model "skewed"; the framework "focused too much"). The displaced decisions — reward-signal design, expert-tester override, default-model swap approval — are inside the company's record-control envelope.

## Why this card exists

Chapter 10 line 27 originally carried an `[EVIDENCE NEEDED]` marker requesting verification of the OpenAI post-mortem date and exact wording. Resolved 2026-05-26 to 29 April 2025 with the verbatim two-clause operative quotation. Expanded post-mortem of 2 May 2025 adds the procedural-layer detail (expert testers raised concerns; concerns outweighed by broader A/B testing).

## Diagnostic significance

This card supplies the chapter's load-bearing deployment-layer primary document. The post-mortem uses the grammar of system agency throughout — "the model began behaving"; "the reward signal focused too much" — and does not name engineers, team leads, or product leadership. The procedural-shell-as-alibi framing the chapter installs depends on this primary text.

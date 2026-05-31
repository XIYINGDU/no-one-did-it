---
id: lmarena-meta-llama-4-policy-statement-2025-04-07
source:
  title: LMArena public statement on Meta's Llama-4-Maverick submission and LMArena leaderboard policy revision
  type: social-media-statement
  publisher: LMArena (lmarena.ai)
  publication_date: 2025-04-07
  url: https://simonwillison.net/2025/Apr/8/lmaren/
  archive:
    wayback_url: http://web.archive.org/web/20260526051543/https://simonwillison.net/2025/Apr/8/lmaren/
    wayback_captured: '2026-05-26'
  access_constraint: open-web
claim:
  text: On 7 April 2025, LMArena issued a public statement on X stating that Meta's interpretation of LMArena's leaderboard disclosure policy 'did not match what we expect from model providers,' and announced that it had updated its leaderboard policies in response to the Llama-4-Maverick-03-26-Experimental submission incident.
  quote_verbatim: 'Meta''s interpretation of our policy did not match what we expect from model providers. ... we have updated our leaderboard policies to reinforce our commitment to fair, reproducible evaluations so this confusion doesn''t occur in the future.

    '
  quote_alteration: ellipsis
  quote_permission: not-required-fair-use
verification:
  evidence_grade: A
  grade_rationale: 'The two operative phrases ("did not match what we expect from model providers"; policy-revision announcement) are quoted verbatim across at least three independent tier-2 and tier-3 AI-domain sources (Simon Willison''s weblog; The Register; Digital Watch Observatory; Neowin), all citing the same LMArena X post of 7 April 2025. Multiple-source corroboration on a contemporaneous public statement reaches A-grade.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  body_sha256: d436ebfd8433f880aae3c776b5034e99d46fe49895121a29a3c03d8f95cb48ac
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://simonwillison.net/2025/Apr/8/lmaren/
      status: ok
      http_code: 200
    archive:
      url: http://web.archive.org/web/20260526051543/https://simonwillison.net/2025/Apr/8/lmaren/
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  tool: WebFetch
  outcome: PASS
  notes: Simon Willison's weblog entry of 8 April 2025 quotes the LMArena statement verbatim and links to the X post. Original X post URL not directly captured in agent session but verbatim text is consistent across all four sources reviewed.
- step: quote-byte-exact
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Both operative phrases match byte-identically across Simon Willison + The Register.
- step: independent-corroboration
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Four independent AI-domain secondary sources cite the same LMArena 7 April 2025 X post.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: Contemporaneous public statement; multiple-source verbatim corroboration.
dispute:
  status: undisputed
defamation:
  living_subjects: []
references:
  cases_affected:
  - llama-4-lmarena
  chapters_citing:
  - 09-the-model-did-it
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# LMArena 7 April 2025 statement on Meta Llama-4-Maverick submission

The card anchors the chapter-10 claim that LMArena, when the Llama-4-Maverick-03-26-Experimental incident became visible, shifted the named agent of the alibi from "we experiment with variants" up to the policy itself, and announced a leaderboard policy revision in response.

## Why this card exists

Chapter 10 line 107 originally carried an `[EVIDENCE NEEDED]` marker requesting exact wording and date of the LMArena policy revision. Resolved 2026-05-26 to 7 April 2025 with the verbatim two-clause statement.

## Diagnostic significance

This card is the chapter-10 worked example for the evaluation-layer alibi's most operationally instructive move: when the controversy outgrew the "we experiment" framing, the named agent shifted up a layer (engineers → policy) rather than down (engineers → individuals). LMArena's response was a policy revision, not a named-individual sanction. The card preserves the timestamp at which the layer-shift occurred.

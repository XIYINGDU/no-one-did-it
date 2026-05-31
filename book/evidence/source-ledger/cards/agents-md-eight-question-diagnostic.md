---
id: agents-md-eight-question-diagnostic
source:
  title: Responsibility Laundering project AGENTS.md — Core diagnostic (eight-question framework) — SUPERSEDED placeholder
  type: other
  publisher: Responsibility Laundering book project (this repository)
  publication_date: 2026
  archive:
    archive_path: 'AGENTS.md (project root; section heading: ''Core diagnostic'')'
  access_constraint: institutional
claim:
  text: SUPERSEDED. The canonical card for this claim is `agents-md-core-diagnostic`, which already existed in the ledger when this duplicate was authored. The sidecar `07-the-record-is-the-battlefield.sources.yml` cites the canonical card directly; this duplicate is kept solely to record the duplication and supersede pointer per pipeline rule (one card per source-claim pair).
  quote_alteration: none
  quote_permission: not-applicable
verification:
  evidence_grade: A
  grade_rationale: 'Card retained as supersede shell pointing to `agents-md-core-diagnostic`. The substantive claim (existence and content of the book''s eight-question diagnostic) is verified in the canonical card. This shell exists to preserve the slug and document the duplication discovered after card-creation; no chapter cites this slug.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Duplicate of agents-md-core-diagnostic discovered during ch-07 sidecar build. Original card already cited the same AGENTS.md Core diagnostic section. Sidecar redirected to original card; this shell carries the supersede pointer.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: Inherits A-grade from canonical card; structural pointer only.
dispute:
  status: superseded-by:agents-md-core-diagnostic
  notes: Created 2026-05-26 by stephen during ch-07 sidecar build; identical-content duplicate of agents-md-core-diagnostic. Superseded same-day to preserve pipeline rule (one card per source-claim pair). Sidecar updated to cite agents-md-core-diagnostic directly.
defamation:
  living_subjects: []
references:
  cases_affected: []
  chapters_citing: []
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: agents-md-core-diagnostic
---

# AGENTS.md eight-question diagnostic — SUPERSEDED

This card was created on 2026-05-26 during the chapter-7 sidecar build before the existing canonical card `agents-md-core-diagnostic` was discovered. The two cards covered the same (source, claim) pair (the project's AGENTS.md Core diagnostic eight-question framework). Per the pipeline's one-card-per-(source, claim) rule, this card is superseded by the canonical `agents-md-core-diagnostic` and the chapter-7 sidecar cites the canonical card directly.

## Disposition

- `dispute.status: superseded-by:agents-md-core-diagnostic`
- `provenance.superseded_by: agents-md-core-diagnostic`
- `chapters_citing: []` (no chapter cites this slug; orphan warning expected and acceptable)

## Lesson for the pipeline

The Discover stage of the pipeline (Stage 1) should grep existing cards for matching source titles before creating a new card. The validator does not block duplicates of distinct slugs; only slug uniqueness is enforced.

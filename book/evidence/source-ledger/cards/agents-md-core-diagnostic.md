---
id: agents-md-core-diagnostic
source:
  title: AGENTS.md — Core diagnostic (eight questions)
  type: archival-document
  publisher: Responsibility Laundering Book — project root
  publication_date: 2026-05-26
  archive:
    archive_path: books/responsibility_laundering/AGENTS.md
  access_constraint: physical-archive
claim:
  text: 'The canonical eight-question core diagnostic for the book is recorded in the project''s AGENTS.md under the heading ''Core diagnostic'': (1) Who or what was publicly blamed? (2) Who had control? (3) Who benefited? (4) Who knew or should have known? (5) Who could have prevented recurrence? (6) Who controlled the record? (7) Who bore the cost? (8) What would responsibility look like if it followed control instead of visibility?'
  quote_verbatim: 'For every case ask:

    1. Who or what was publicly blamed?

    2. Who had control?

    3. Who benefited?

    4. Who knew or should have known?

    5. Who could have prevented recurrence?

    6. Who controlled the record?

    7. Who bore the cost?

    8. What would responsibility look like if it followed control instead of visibility?

    '
  quote_alteration: none
  quote_permission: not-applicable
verification:
  evidence_grade: A
  grade_rationale: 'Internal project canonical document; the eight-question diagnostic is the book''s load-bearing analytic framework, installed in AGENTS.md (the single source of truth shared by all three tooling chains — Claude, Codex, Gemini — via @AGENTS.md import). The text quoted here is byte-identical with the in-tree archive_path file as of the verification date. Internal canonical documents reach A-grade for claims about what the project''s own framework says.

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
  notes: AGENTS.md exists at the project root; the eight-question core diagnostic is present under the 'Core diagnostic' heading (line 27 onwards per grep). The same text appears in stephen-fact-check-director agent system context at chapter time.
- step: quote-byte-exact
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Verbatim quotation matches AGENTS.md text exactly.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: Internal canonical project document for self-referential claim.
dispute:
  status: undisputed
defamation:
  living_subjects: []
references:
  cases_affected: []
  chapters_citing:
  - 03-who-could-have-stopped-it
  - 07-the-record-is-the-battlefield
  - 09-the-model-did-it
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# AGENTS.md core diagnostic — eight questions

The card anchors self-referential citations from chapters 7 and 10 to the project's canonical eight-question diagnostic. The card exists so the chapter-prose anchor `[CITE: AGENTS.md core diagnostic]` resolves to a card with a fixed in-tree archive_path, byte-stable verbatim quotation, and a grade-assignment trail.

## Why this card exists

Chapter 7's hidden-architecture section (line 49) and chapter 10's hidden-architecture section both open by re-stating the book's diagnostic frame and pointing to AGENTS.md as the canonical record. This is a self-referential citation to internal project material — schema source.type `archival-document`, access_constraint `physical-archive` (in-tree file), no URL required.

## Diagnostic significance

The eight questions are the load-bearing analytic instrument the book applies to every case. Recording the canonical source here lets future chapters cite the same diagnostic without re-pasting the text, and lets fact-check passes confirm that chapter prose has not drifted from the canonical wording. Other chapters that invoke the diagnostic should cite this same card.

## Re-use record

| Chapter | Anchor location | Re-use date | Re-user |
|---|---|---|---|
| 09-the-model-did-it | line 49 | 2026-05-26 | stephen (original) |
| 07-the-record-is-the-battlefield | line 49 | 2026-05-26 | stephen (added during ch-07 sidecar build) |
| 03-who-could-have-stopped-it | line 48 | 2026-05-26 | stephen (added during ch-03 sidecar build) |

---
name: research-card-pipeline
description: Orchestrate the seven-stage pipeline that turns a (source, claim) pair into a verified, queryable, accumulating research card. Wires the existing source-ledger-discipline, citation-hygiene, evidence-grading, and case-file-method skills into a single operating procedure with Layer A (mechanical), Layer B (Stephen-led), and Layer C (specialist) verification.
version: 1.0.0
---

# Research Card Pipeline

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## What this skill orchestrates

The research card is the atomic unit of evidence in the book. One card = one (source, claim) pair. Cards live under `book/evidence/source-ledger/cards/<slug>.md` with YAML frontmatter that conforms to `book/evidence/source-ledger/schema/research-card.schema.json` and prose body for human-readable context.

Cards exist so that:

- Every `[CITE: ...]` anchor in chapter prose resolves to a verified source via a chapter sidecar (`book/evidence/source-ledger/sidecars/<chapter-stem>.sources.yml`).
- Stephen's verification work product is a durable, queryable artifact — not implicit in agent transcripts.
- A future galley-lock pass can re-run mechanical checks (`scripts/validate_source_ledger.py`) without re-deriving what was already verified.
- Sources cited by multiple chapters (Walsh Final Report; Park 421 U.S. 658; Inquiries Act 2005 §21) live as one card with `chapters_citing:` listing every chapter that references them.

This skill is the orchestrator. It does not duplicate the substrate skills:

- `source-ledger-discipline` — what fields a ledger row must carry
- `citation-hygiene` — how a citation is structured for fact-check
- `evidence-grading` — the A/B/C/D rubric per rule 02
- `case-file-method` — how case files turn into chapter anchors
- `primary-source-playbooks` — where to look for primary documents per domain

This skill says **who does what when**.

## Decision rubric

Usable output:
- One card per (source, claim) pair; no two claims per card; no two sources per card.
- Frontmatter passes `scripts/validate_source_ledger.py` with zero HARD findings.
- `verification_log:` block records each step with actor, timestamp, outcome.
- Chapter sidecar maps every `[CITE: ...]` anchor in the chapter prose to one or more card IDs.

Weak output:
- One card carrying multiple unrelated claims.
- Grade assigned without rationale paragraph.
- Sidecar missing for a chapter that has `[CITE: ...]` anchors.
- Living subject named without `nancy_cleared: true`.
- Source URL with no archive fallback and `access_constraint: open-web`.

## The seven stages

```
1 Discover  → 2 Draft  → 3 Verify  → 4 Defamation gate  → 5 Wire to chapter  → 6 Validate  → 7 Accumulate
```

### Stage 1 — Discover

**Trigger:** A claim surfaces — during case-file research, during chapter drafting, during fact-check, during red-team review.

**Owner:** The first agent to identify the claim names the card. Typically a domain researcher (Shirley, Selina, Warren, Loki) or Wayne mid-draft.

**Output:** Create `book/evidence/source-ledger/cards/<slug>.md` with the slug naming convention below and minimal frontmatter:

```yaml
---
id: <slug>
source:
  title: "<source title>"
  type: <source-type-from-taxonomy>
  publication_date: <ISO date>
  access_constraint: <open-web | paywall | institutional | paywalled-archive | sealed | physical-archive>
claim:
  text: "<one-sentence claim>"
verification:
  evidence_grade: unverified
dispute:
  status: undisputed
defamation:
  living_subjects: []
references:
  cases_affected: []
  chapters_citing: []
provenance:
  created_by: <agent-name>
  created_on: <YYYY-MM-DD>
  superseded_by: null
---

# <Card title>

<Why this card exists; what claim it anchors.>
```

**Slug rule:** kebab-case; lowercase; identifies source primarily, with claim sub-identifier when needed. Examples: `park-421-us-658-1975`, `walsh-final-report-bush-pardons-1992`, `chilcot-executive-summary-paragraphs-499-510-875-876`. The slug must be unique across `cards/`.

### Stage 2 — Draft

**Trigger:** Card exists with minimal frontmatter.

**Owner:** Same researcher who discovered.

**Output:** Fill remaining frontmatter except `verification.evidence_grade`, `verification.verified_by`, `verification.verified_on`, `verification.body_sha256`, `verification_log`, and (if applicable) `defamation.nancy_cleared`.

Required:
- `source.url` (when `access_constraint: open-web`)
- `source.archive.wayback_url` and `wayback_captured` (when feasible — durable artifact)
- `claim.quote_verbatim` (when the chapter quotes the source)
- `claim.page_anchor` or `paragraph_anchor` (for primary documents with pagination)
- `defamation.living_subjects` (list every living subject the source identifies in an unfavorable context; otherwise `[]`)

Status implicit after Stage 2: `verification.evidence_grade: unverified`.

### Stage 3 — Verify (Layer B)

**Trigger:** Card at `verification.evidence_grade: unverified`.

**Owner:** Stephen (fact-check director).

**Process:** Stephen runs the five mandatory verification steps and records each in `verification_log:`.

1. **source-existence** — Fetch URL or archive; confirm metadata matches frontmatter
2. **quote-byte-exact** — Locate `claim.quote_verbatim` in fetched body; record byte/paragraph anchor
3. **independent-corroboration** — Per rule 02: grade A needs primary source, grade B needs ≥2 independent secondary tier-1, grade C requires explicit dispute context
4. **grade-assignment** — Apply rule 02-evidence-grades.md rubric; write `verification.grade_rationale`
5. **sha256-fingerprint** — Compute body hash; store in `verification.body_sha256` for future drift detection

**Output:** `verification.evidence_grade` ∈ {A, B, C}, `verified_by: stephen`, `verified_on: <date>`, `body_sha256` set, `verification_log:` populated.

Grade D cards exist only as archival rejects; they cannot be cited from chapters (validator enforces).

### Stage 4 — Defamation gate (Layer C, conditional)

**Trigger:** `defamation.living_subjects` is non-empty.

**Owner:** Nancy (legal-risk counsel).

**Process:** Apply `defamation-wording` skill; confirm procedural-stage language; check quote-permission risk per rule 06.

**Output:** `defamation.nancy_cleared: true` (or `false` with rewrite required), `nancy_cleared_on: <date>`, optional `nancy_notes`.

A card with living subjects and `nancy_cleared: false` cannot be wired to a chapter.

### Stage 5 — Wire to chapter

**Trigger:** Chapter prose introduces a `[CITE: ...]` anchor that resolves to a verified card.

**Owner:** Wayne (during drafting) or Jerry (at chapter promotion).

**Output:** Append to `book/evidence/source-ledger/sidecars/<chapter-stem>.sources.yml`:

```yaml
chapter_id: <chapter-stem>
anchors:
  - anchor_text: "<the text inside the [CITE: ...] anchor>"
    card_ids:
      - <card-id>
    line_in_chapter: <line number, optional>
```

And update the card's `references.chapters_citing` to include the chapter stem.

When one anchor cites multiple sources (common for "[CITE: A; B; C]"), list all card IDs in `card_ids:`.

### Stage 6 — Validate (Layer A)

**Trigger:** Any card or sidecar changes; runs in pytest.

**Owner:** `scripts/validate_source_ledger.py`.

**Checks:**
- Schema compliance
- Slug uniqueness
- Source-type membership
- URL well-formedness
- Cross-reference integrity (chapters_citing ↔ chapter files; sidecar card_ids ↔ cards/)
- Grade-discipline coupling (D → no chapter cites; C → dispute context required)
- Living-subject gate (`nancy_cleared: true` required when living_subjects non-empty)
- Orphan detection (warn unless `--strict-orphans`)
- Anchor coverage (chapter `[CITE:]` anchors covered by sidecar)

Optional checks (network, opt-in):
- `--check-urls` — URL liveness via HEAD
- `--check-drift` — re-fetch and compare sha256

**Output:** Exit 0 (PASS) or 1 (HARD failure with named locations).

### Stage 7 — Accumulate / supersede

**Trigger:** Source changes; new authoritative source supersedes; new chapter cites existing card.

**Owner:** Stephen (curator) for supersede; any researcher for re-use.

**Re-use:** Append the new chapter stem to `references.chapters_citing`; no other change.

**Supersede:** Set old card's `dispute.status: superseded-by: <new-id>`; create new card; update sidecars to point to new card.

**Withdrawal:** Set `dispute.status: withdrawn`; remove from sidecars; chapters citing the withdrawn card must be revised.

**30-day re-pass clock (live cases):** Existing STATUS.md cross-cutting clocks trigger Stage 3 + 4 re-verification; if subject's procedural status changed, propagate to chapter language.

## Conflict handling

1. **Two sources support contradictory claims on the same fact:** create two cards with distinct ids; set `dispute.status: contested` on both; Laura (red-team) adjudicates the chapter use; record adjudication in the chapter's review-memo.
2. **Card grade ≠ what Stephen assigns at re-verification:** Stephen overwrites with new entry in `verification_log:`; if grade drops below B, chapters citing the card go to `status: draft` until rewired.
3. **Two researchers create cards for the same source:** the first-created `id` wins; the second is merged into the first; provenance log records the merger.

## Escalation conditions

- Card cannot reach grade A or B at Stage 3 → handoff to Delon for deeper primary-source search; chapter line marked `[EVIDENCE NEEDED]` with the card id referenced.
- Defamation gate fails at Stage 4 → handoff to Wayne to revise chapter language; card stays in ledger; chapter line gets `[EVIDENCE NEEDED]` until cleared rewrite is in place.
- Validator HARD failure that blocks chapter promotion → handoff to Jerry to coordinate the fix across owners.

## Boundary-case recipes

1. **Quote-only verification (no claim beyond the quote):** `claim.text` mirrors the quote's referent ("Walsh said the pardons completed the cover-up"); `quote_verbatim` carries the byte-exact text; treated as one card.
2. **Statute or doctrine cited without quote:** `claim.text` carries the operative legal proposition; `quote_verbatim` omitted; `page_anchor` cites section.
3. **Translation:** `claim.quote_verbatim` carries the original-language text; `claim.quote_alteration: translation`; English translation lives in the card body, attributed to translator.
4. **Live case (status changes possible):** Add a 30-day re-pass clock to STATUS.md; on each re-verification, Stephen appends a `verification_log:` entry; if status changes, supersede.
5. **Paywall / sealed source:** `access_constraint: paywall` or `sealed`; `source.url` omitted; `source.archive.archive_path` carries an internal-archive path (institutional subscription PDF, court filing PDF, etc.); validator skips URL checks; Stephen holds the access.
6. **Hybrid grade (one source supports the legal status A, another supports the scale B):** create two cards; chapter sidecar references both for the same anchor; `references.cases_affected` reflects the case both serve.

## What this pipeline does NOT verify

- Whether the quote is in context vs. cherry-picked (Laura's red-team territory).
- Whether the source is reliable in its domain (the grade assigns ceiling, not certainty; specialist gates partially address).
- Whether the chapter's interpretation of the source is the strongest plausible reading (Laura + xiaolai).
- Whether a translation faithfully renders the original (Stephen + domain researcher; pipeline records the translator, not the translation quality).

These remain editorial judgment calls. The pipeline is the mechanical floor; judgment lives above it.

## Migration plan from current state

Current state (as of 2026-05-26):

- `book/evidence/source-ledger/` exists with `.gitkeep` only — empty ledger
- 148 `[CITE: ...]` anchors live in 9 chapters; 4 chapters (ch-02, 03, 04, 05) have inline source naming but no `[CITE:]` convention; ch-13 has zero by design
- 29 case files in `book/evidence/case-files/` carry evidence-grade frontmatter; sources are named in their bodies
- 7 web-retrievable items lifted on 2026-05-26 (Stephen-led); the verified facts live in Stephen's agent transcript and inline chapter prose; cards do not yet exist

Migration sequence:

1. Pilot batch: turn the 7 lifted items into 7 cards in `book/evidence/source-ledger/cards/` (this captures real verified work as the first cards; no speculation)
2. Pick the smallest chapter sidecar to wire (ch-10 has 2 of the 7 lifted items)
3. Run validator; fix any schema issues; commit
4. Roll out chapter by chapter (Wave 3 first since they were the most recently verified)
5. Backfill ch-02/03/04/05 inline source naming into `[CITE:]` anchors + cards last (highest-friction; ~1 day per chapter)
6. Wire `validate_source_ledger.py` into pytest after the first full chapter passes

## Example dispatch

```
Jerry → Stephen: "Verify and card-ify the seven web-retrievable items lifted on 2026-05-26.
                Create one card per item under book/evidence/source-ledger/cards/.
                Each card carries the verification_log entry for the Stephen pass.
                Then wire ch-10's two items into book/evidence/source-ledger/sidecars/10-the-model-did-it.sources.yml.
                Run scripts/validate_source_ledger.py; report findings."
Stephen → Jerry: 7 cards created; ch-10 sidecar wired; validator PASS; handoff to Wayne for ch-08/09/11/12 sidecars.
```

## Handoff schema

Every output from this skill includes:

```
Owner:
Purpose:
Evidence grade (of the cards produced):
Assumptions:
Open questions:
Validator status:
Handoff:
```

The Validator status row is unique to this skill — it captures whether `scripts/validate_source_ledger.py` PASS / FAIL after the work.

## Why this skill exists

The book argues that institutions launder responsibility through invisible decision-paths. The book's evidence apparatus had a parallel gap: verification work product lived inside agent transcripts, not in queryable artifacts. The card pipeline closes that gap. The book practices what it preaches by making its own verification surface mechanically auditable.

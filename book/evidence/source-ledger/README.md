# Source Ledger

This directory holds the book's research-card pipeline: one card per (source, claim) pair, with verification metadata, sidecar mappings to chapters, and a mechanical validator.

See `.claude/skills/research-card-pipeline/SKILL.md` for the full pipeline orchestration. This README is the operator's quick-reference.

## Layout

```
book/evidence/source-ledger/
├── cards/
│   └── <slug>.md            # one card per (source, claim) pair
├── sidecars/
│   └── <chapter-stem>.sources.yml   # maps chapter [CITE:] anchors → card ids
├── schema/
│   └── research-card.schema.json    # JSON Schema for card frontmatter
└── README.md
```

## Quick commands

```bash
# Validate everything (no network):
python3 scripts/validate_source_ledger.py

# With URL liveness:
python3 scripts/validate_source_ledger.py --check-urls

# With sha256 drift detection (re-fetches every URL):
python3 scripts/validate_source_ledger.py --check-urls --check-drift

# Strict mode (orphan cards fail HARD):
python3 scripts/validate_source_ledger.py --strict-orphans
```

The validator runs as part of `python3 -m pytest tests/ -q`.

## How a card is born

1. **Discover** — claim surfaces during research or drafting; researcher creates `cards/<slug>.md` with minimal frontmatter (`evidence_grade: unverified`).
2. **Draft** — researcher fills in source metadata, claim text, and (if applicable) verbatim quote.
3. **Verify** — Stephen runs five steps (source-existence, quote-byte-exact, corroboration, grade, sha256) and records each in `verification_log:`.
4. **Defamation gate** — Nancy clears if a living subject is named.
5. **Wire** — chapter `[CITE:]` anchor → sidecar `card_ids:` entry.
6. **Validate** — `scripts/validate_source_ledger.py` runs Layer A mechanical checks.
7. **Accumulate** — re-use across chapters; supersede when sources change.

## Slug naming

Kebab-case, lowercase, identifies the source. Add a claim-disambiguator when one source supports multiple distinct claims.

| Pattern | Example |
|---|---|
| `<case>-<reporter>-<year>` | `park-421-us-658-1975` |
| `<source>-<chapter>-<year>` | `walsh-final-report-bush-pardons-1992` |
| `<statute>-<year>` | `inquiries-act-2005-section-21` |
| `<source>-<paragraph>` | `chilcot-executive-summary-paragraphs-499-510` |

## When a card breaks

| Symptom | Action |
|---|---|
| `--check-urls` flags a 404 | If `archive.wayback_url` works, the card stays valid; otherwise card moves to `needs-replacement` |
| `--check-drift` flags sha256 mismatch | Card moves to `needs-reverification`; Stephen re-runs Layer B |
| Procedural status of a named subject changes (conviction overturned, deceased, pardon issued) | Card moves to `needs-defamation-repass`; Nancy re-clears |
| New authoritative source supersedes (e.g., final ruling replaces preliminary order) | Old card's `dispute.status: superseded-by: <new-id>`; new card created; sidecars updated |
| Card is found wrong | `dispute.status: withdrawn`; chapters citing it must be revised |

## What is NOT in scope

- Whether the quote is in context vs. cherry-picked — that's Laura's red-team territory
- Whether the source is reliable in its domain — the grade assigns a ceiling, not certainty
- Whether the chapter's interpretation of the source is the strongest plausible reading — Laura + xiaolai
- Whether a translation faithfully renders the original — Stephen + domain researcher records the translator, not the translation quality

The pipeline is the mechanical floor. Editorial judgment lives above it.

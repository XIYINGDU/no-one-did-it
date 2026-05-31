# Cite-Density Fixtures

Golden + negative fixtures for `scan-cite-density.py` and `/cite-density-audit`. Each negative fixture exhibits one rule-13 violation pattern; each positive fixture demonstrates the valid form.

## Layout

```text
tests/fixtures/cite-density/
  good/  must NOT trip scan-cite-density
  bad/   must trip scan-cite-density with the expected failure category
```

## Patterns covered

| Pattern category | Bad fixture | Good fixture |
|---|---|---|
| Verbose embedded citation | `bad/full-citation.md` | `good/full-citation.md` |
| Corroboration list inside bracket | `bad/corroboration-list.md` | (good covered by full-citation.md) |
| Archive metadata inside bracket | `bad/archive-metadata.md` | (good covered by full-citation.md) |
| Single-slug + suspiciously long | `bad/hidden-metadata.md` | `good/multi-slug.md` |
| Multi-slug (legitimate) | (no bad case; multi-slug with `;` is permitted regardless of length) | `good/multi-slug.md` |
| Pending-stephen-lock suffix | (no bad case; valid syntax) | `good/pending-lock.md` |

Authoring discipline matches the implication-audit fixture suite: small, self-contained, one pattern per file, fictional content where any source name is needed.

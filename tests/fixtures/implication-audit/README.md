# Implication-Audit Fixtures

Golden + negative fixtures for `scan-implication.py` and the `/implication-audit` skill. Each negative fixture exhibits exactly ONE implication pattern from `.claude/rules/07-implication-burden.md`; each positive fixture demonstrates the same pattern correctly mitigated (cited, hedged, or named as inference).

## Layout

```text
tests/fixtures/implication-audit/
  bad/   one file per implication pattern; must trip scan-implication
  good/  one file per pattern; the same pattern with mitigation; must NOT trip
```

## Patterns covered

| Pattern id (matches scan-implication.py finding name) | Bad fixture | Good fixture |
|---|---|---|
| `anonymous-chain` | `bad/anonymous-chain.md` | `good/anonymous-chain.md` |
| `chain-ladder` | `bad/chain-ladder.md` | `good/chain-ladder.md` |
| `decision-benefit-juxtaposition` | `bad/decision-benefit.md` | `good/decision-benefit.md` |
| `sympathetic-then-cold` | `bad/sympathetic-cold.md` | `good/sympathetic-cold.md` |
| `causation-by-adjacency` | `bad/causation-adjacency.md` | `good/causation-adjacency.md` |

## How the fixtures are used

The pytest harness `tests/test_scan_implication_fixtures.py` runs `scan-implication.py`'s `scan()` function on each fixture and asserts:

- Every `bad/*.md` produces at least one finding of the expected pattern.
- Every `good/*.md` produces zero findings (the mitigation cleared them).

When tuning the scanner's pattern library (false-positive rate calibration per rule 09 before block-mode promotion), add fixtures here BEFORE changing the scanner. The fixture suite is the regression guard.

## Authoring discipline

- Each fixture is a self-contained Markdown snippet with `---` YAML frontmatter setting `status: in-rewrite`.
- Fixtures are tiny by design — one pattern per file. Multi-pattern fixtures hide which check the scanner is failing.
- Fixtures use fictional names (`Smith`, `Jones`, `Cole Industries`) where any name is required, so the fixtures are never confused with real cases.
- A bad fixture's pattern must match exactly one scanner finding-name; a good fixture's mitigation must use one of the rule-07 hedge patterns listed in `.claude/rules/07-implication-burden.md`.

## Adding a new pattern

If `scan-implication.py` gains a new pattern, add the matching fixture pair here AND extend `tests/test_scan_implication_fixtures.py` to assert against the new pattern. Pattern additions without fixtures are silent untested code.

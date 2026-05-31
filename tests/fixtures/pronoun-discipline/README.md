# Pronoun-Discipline Fixtures

Golden + negative fixtures for `scan-pronoun-discipline.py` and `/pronoun-discipline-audit`. Each negative fixture exhibits one rule-14 violation pattern; each positive fixture demonstrates the valid form.

## Layout

```text
tests/fixtures/pronoun-discipline/
  good/  must NOT trip scan-pronoun-discipline
  bad/   must trip scan-pronoun-discipline with the expected finding
```

## Patterns covered

| Pattern | Bad fixture | Good fixture |
|---|---|---|
| Meta-frame: this-chapter | `bad/meta-this-chapter.md` | `good/we-pattern.md` |
| Meta-frame: the-book | `bad/meta-the-book.md` | `good/we-argue.md` |
| Meta-frame: the-reader / readers | `bad/meta-the-reader.md` | `good/we-notice.md` |
| You: address | `bad/you-will.md` | `good/imperative.md` |
| You: for-you | `bad/for-you.md` | `good/for-us.md` |
| Modal-prescriptive: you-should | `bad/you-should.md` | `good/imperative.md` |
| Evasive-collective: people-tend | `bad/people-tend.md` | `good/specific-group.md` |
| Cited-quote exempt | (n/a; covered by good case) | `good/cited-quote-with-you.md` |
| Front-matter / heading exempt | (n/a) | `good/heading-the-book.md` |

Authoring discipline matches the prior fixture suites (implication-audit, cite-density): small, self-contained, one pattern per file, fictional content where any source name is needed.

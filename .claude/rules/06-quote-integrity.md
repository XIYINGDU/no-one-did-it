---
description: "Quote integrity rule: verbatim quotation, paraphrase, attribution, and permission discipline for every quote in case files, chapters, memos, and proposals."
---

**Every quotation must be byte-exact, fully attributed, and traceable to a single named source; alterations are marked, never silent.**

# Quote Integrity Rule

**Scope:** binds every quotation, paraphrase, and attributed statement in `book/evidence/case-files/`, `book/chapters-v2/`, `process/review-memos/`, and `book/proposals/`. A quote that breaks integrity is worse than no quote — it taints the chapter.

## Verbatim quotes

A quote inside `"..."` or `>` block must be **byte-exact** to the source. Any alteration is flagged:

| Alteration | When allowed | How to mark it |
|---|---|---|
| Spelling/grammar in the original is wrong | Always allowed to preserve | Add `[sic]` immediately after the wrong word |
| Inserted clarification (a name, a date, a referent) | Allowed when the quote is ambiguous without it | `[bracketed text]` for the insertion |
| Removed text mid-quote (ellipsis) | Allowed only if removal does not change meaning | `...` for short skip; `[...]` if multiple sentences removed |
| Changed verb tense or pronoun for sentence flow | Forbidden | Re-cast as paraphrase or use a shorter quote |
| Capitalized first letter to fit sentence | Allowed | `[T]hey said...` |
| Translated from another language | Allowed | Attribute the translator inline: "(author's translation)" or "(NYT translation)" |

If the alteration cannot be marked above, the quote becomes a paraphrase. **No silent alterations.**

## Paraphrases

A paraphrase must:

- Use a verb of attribution on the same line (`said`, `wrote`, `argued`, `denied`).
- Not put words in the source's mouth that the source did not say.
- Be checkable: a fact-checker comparing the paraphrase to the source must confirm it as fair.

If the paraphrase compresses two or more statements, the chapter must say so: "Across three separate interviews, X argued that Y."

## Speaker attribution

Every quote and paraphrase names the speaker, the venue (interview / sworn testimony / press release / private email / book), and the date. Anonymous quotes from journalism sources may stand only if:

- The journalism source is at tier 2 or tier 1 of `.claude/skills/primary-source-playbooks/SKILL.md`.
- The anonymity is justified in the source (e.g., "spoke on condition of anonymity because they were not authorized").
- The chapter says so: "an unnamed source familiar with the matter told Reuters..."

## Quote permission

For quotes longer than fair-use limits (US: typically >300 words of a single work; less for shorter works or song lyrics; varies by jurisdiction), `nancy-legal-risk-counsel` must clear the quote before `status: ready`. Email permissions; record permission in the source ledger row.

## Verification protocol

Stephen's fact-check pass verifies every quote against the source. The source ledger row for a quote must include:

```text
Quote (verbatim or paraphrase):
Speaker:
Venue:
Date:
Source URL or document citation:
Page / paragraph / timestamp:
Verbatim status: verbatim | paraphrase | translation
Alterations: none | sic | bracketed insertion | ellipsis | sentence-case
Permission required: no | yes — cleared by Nancy on <date> | yes — pending
```

A quote that cannot complete this row stays out of the chapter.

## Why this rule exists

Misquoting a subject is the single fastest way for a nonfiction book to lose authority — and the most common avenue for a defamation suit. Verbatim discipline is also the discipline of the source documents the book argues other institutions failed to maintain. The book practices what it preaches.

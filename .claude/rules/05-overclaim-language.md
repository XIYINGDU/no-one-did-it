---
description: "Over-claim language rule: banned mental-state and attribution verbs without explicit citation or hedging, plus required hedging patterns for B/C-grade claims. Enforced in warn-mode by scan-overclaim.py."
---

**Hedge every claim that depends on inferred knowledge, motive, or guilt; banned verbs require citation or a status-accurate qualifier.**

# Over-claim Language Rule

**Scope:** binds every prose artifact under `book/evidence/case-files/`, `book/chapters-v2/`, `process/review-memos/`, and `book/proposals/`. Enforced in warn-mode by `.claude/hooks/scan-overclaim.py` when any of these paths are written or edited.

## Banned verbs without explicit citation or hedging

Verbs that attribute knowledge, motive, or guilt MUST be either (a) inside a verbatim quotation with attribution, (b) immediately preceded or followed by a citation in `[CITE: ref]` form, or (c) hedged with a status-accurate qualifier per `.claude/skills/defamation-wording/SKILL.md`.

The pattern-scanner flags these verbs as candidates:

| Verb / phrase | Required treatment |
|---|---|
| `knew` / `knew about` / `was aware that` | Cite the source proving knowledge (internal email, deposition, admission). No "must have known". |
| `deliberately` / `intentionally` / `on purpose` | Cite a source documenting the intent (admission, jury finding, recorded statement). |
| `guilty` / `is guilty of` | Cite the court of conviction + date. Otherwise: "was charged with" / "was accused of". |
| `lied` / `lied about` | Cite the documented falsehood + the documented contemporaneous knowledge of falsity. Otherwise: "misstated" / "told X that Y, when later evidence showed Z". |
| `is responsible for` (about a named person) | Cite the chain evidence (control / benefit / knowledge / preventability per `.claude/skills/responsibility-chain-mapping/SKILL.md`) or revise to qualify ("is in the chain of preventability for"). |
| `caused` (about a named person, where chain is contested) | Reword to "is in the responsibility chain for" or cite the conclusive determination. |
| `proves` / `definitively shows` | Use "supports", "indicates", "is consistent with" unless citing a final adjudication that uses "proved". |
| `must have` / `would have` (about mental states) | Forbidden for mental-state attribution. Use only documented facts. |
| `clearly` / `obviously` / `undeniably` | Forbidden as evidence-replacement adverbs. Cite the source that makes it clear; let the reader judge. |

## Required hedging patterns

For claims at evidence grade B or C, the chapter must use one of these patterns within the sentence or the adjacent sentence:

- "according to <named source>, ..."
- "<source> reported that ..."
- "as documented in <source>, ..."
- "court records show that ..." (for filings)
- "per the <agency> investigation, ..."
- "as of <date>, the case is <procedural status>."

## Why this rule exists

The book argues that responsibility laundering is the recurring institutional technique. The argument loses force when the book itself launders evidence — uses confident verbs to bridge gaps the sources do not cover. Every banned verb above is one a sloppy chapter reaches for; every required hedge is the discipline the book demands of the actors it analyzes.

This is the bar `jerry-crew-chief` enforces at chapter ready-promotion. `nancy-legal-risk-counsel` reviews compliance; `wayne-narrative-lead` self-polices during drafting using `.claude/skills/defamation-wording/SKILL.md`.

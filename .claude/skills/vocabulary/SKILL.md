---
name: vocabulary
description: "Use when writing, reviewing, or naming any responsibility-laundering book artifact — pick the canonical noun or verb from this registry rather than coining a synonym. Loaded by NLPM's scorer and checker when R51 is enabled in .claude/nlpm.local.md."
version: 0.1.0
---

# Responsibility Laundering Book — Domain Vocabulary

> The canonical noun-and-verb set for this book project. Every artifact name, prose description, and rule wording should draw from this registry. Synonyms are flagged by `/nlpm:check` and penalized by `/nlpm:score` when R51 is enabled.
>
> **Status:** seeded by `/nlpm:vocab-init` on 2026-05-25. The seed combines (a) literary warrant from `analysis/vocabulary-extract/` and (b) the book's domain taxonomy already codified in `.claude/rules/00-five-values.md` through `.claude/rules/04-style-guide.md` and the `AGENTS.md` core diagnostic.
>
> Adopter must prune, define deprecation pairs, and confirm scopes before R51 enforcement produces useful signal. Re-run `analysis/scripts/extract-vocabulary.py` after artifact changes to refresh.

---

## Scopes (P1 of vocabulary-design-principles.md)

This project has a single internal scope. There is no `auditor` scope because no `.github/workflows/auditor-*.yml` files exist.

| Scope | Paths | Description |
|---|---|---|
| internal | `.claude/commands/`, `.claude/agents/`, `.claude/skills/`, `.claude/docs/`, `book/`, `AGENTS.md` | What this project does to its own artifacts: build case files, draft chapter briefs, draft prose, audit evidence, red-team claims, handoff between crew roles. |

## Verbs (literary warrant from corpus + book methodology)

The corpus is prose-heavy, so the extractor surfaced few action verbs from filenames alone. The table below combines extractor output (frequency column) with the verbs the book methodology actually uses (frequency 0 marks book-methodology verbs not yet in filename warrant).

### internal scope

| Canonical verb | Frequency (filename + description) | Deprecated synonyms (fill in) |
|---|---|---|
| `build` | 4 | `make`, `produce`, `create` (only when result is an artifact) |
| `audit` | 2 | `check`, `review` (only when output is a usable/weak/unusable verdict) |
| `draft` | 5 | `compose`, `pen`, `author`, `write` (now deprecated; was the dominant negative-constraint form) |
| `revise` | 0 | `rewrite`, `polish`, `edit` (only when input is a prior draft) |
| `compile` | 0 | `assemble`, `gather` |
| `verify` | 0 | `confirm`, `double-check` |
| `red-team` | 0 | `attack`, `stress-test`, `critique` |
| `fact-check` | 0 | `verify` (only when subject is a single claim) |
| `grade` | 21 | `rank`, `score`, `rate`, `mark` (only when output is an A/B/C/D label; `mark` moved here from `flag` per drift report) |
| `flag` | 0 | `note`, `warn` (`mark` moved to `grade` per drift report) |
| `gate` | 0 | `block`, `hold`, `stop` (only when output is a draft-readiness decision) |
| `handoff` | 21 | `pass`, `delegate`, `transfer`, `hand off` (two-word form retired; one-word `handoff` is the canonical for both verb and noun) |
| `map` | 0 | `chart`, `diagram` (only when output is a responsibility-chain) |
| `cite` | 0 | `reference`, `point to` |

## Nouns (literary warrant from corpus + book taxonomy)

### Artifact-class nouns

| Canonical | Frequency | Definition |
|---|---|---|
| `case file` | warrant from `commands:filename`, `skills:dirname` | Structured record per `.claude/skills/case-file-method/SKILL.md` — eight-question diagnostic, evidence grade, source ledger, handoff. |
| `chapter brief` | warrant from `commands:filename` | Plan-of-prose per `.claude/skills/chapter-blueprint/SKILL.md` — scenes, thesis, case hierarchy, counterargument, evidence gaps. |
| `chapter draft` | book methodology | Prose output from Wayne that turns a chapter brief into the chapter rhythm in `.claude/rules/04-style-guide.md`. |
| `source ledger` | warrant from `skills:dirname` | Per-claim citation log per `.claude/skills/source-ledger-discipline/SKILL.md` with provenance and interest disclosure. |
| `responsibility chain` | book methodology | The control → benefit → knowledge → preventability → record control → cost-bearing map per `.claude/skills/responsibility-chain-mapping/SKILL.md`. |
| `handoff` | book methodology (AGENTS.md "Default artifact standard") | The `Owner / Purpose / Evidence grade / Assumptions / Open questions / Handoff` footer every substantial output ends with. |
| `red-team memo` | book methodology | Output of the `/red-team` command — strongest objection, likely critic attack, correction path, safer wording. |
| `proposal pack` | warrant from `commands:filename` | Output of `/proposal-pack` — pitch, titles, overview, audience, comps, chapter summaries, sample-chapter strategy. |
| `claim` | book methodology (`.claude/rules/02-evidence-grades.md`) | A single assertion that takes an A/B/C/D evidence grade. |
| `scene` | book methodology (`.claude/rules/04-style-guide.md`) | A concrete narrative passage; chapters open with one. |
| `evidence grade` | book methodology | One of A/B/C/D per `.claude/rules/02-evidence-grades.md`; not the same word as `claim`. Field label form: `Evidence grade:` (do not use `Confidence:`). |
| `counterargument` | book methodology (Over-rule #4; template field label) | The strongest adversarial check that must precede assertion of a claim. Retired synonyms: `opposing case`, `objection`. |
| `source packet` | book methodology (researcher Owns clause) | The researcher's pre-grade bundle of sources, chronology, and notes — distinct from `case file` which is the post-grade artifact. `case packet` deprecated for both stages. |
| `progress memo` | book methodology (crew-chief output) | The crew-chief's periodic status summary. Replaces `progress report` / `integrated progress report`. |

### Case-taxonomy nouns (load-bearing; do not paraphrase)

Per `.claude/rules/01-case-taxonomy.md` these four labels are non-substitutable and must be used verbatim:

| Canonical | Forbidden substitutes |
|---|---|
| `pure scapegoat` | `innocent victim`, `wrongly accused` |
| `partial scapegoat` | `mostly guilty`, `lower-level fall guy` |
| `system/object alibi` | `procedural cover`, `system blame`, `process scapegoat` |
| `cost-bearing goat` | `collateral damage`, `silent victim` |

### Role-nouns (agent files; paired with their dominant verbs)

| Role-noun | Frequency (agents:filename) | Paired verb(s) |
|---|---|---|
| `reviewer` | 1 | `review` (Alan, parameterized across 6 domains) |
| `researcher` | 4 | `build` (source packets), `cite` (Shirley/Selina/Warren/Loki) |
| `director` | 2 | `assign`, `gate` (Delon for research, Stephen for fact-check) |
| `strategist` | 1 | `position`, `test` (Blair, combined proposal + audience) |
| `editor` | 1 | `red-team` (Laura) |
| `architect` | 1 | `place`, `sequence` (Bonnie) |
| `lead` | 1 | `draft`, `revise` (Wayne) |
| `chief` | 1 | `assign`, `consolidate`, `decide` (Jerry) |
| `counsel` | 1 | `flag`, `gate` (Nancy — legal risk) |

### Diagnostic-question nouns (from AGENTS.md core diagnostic)

Every case file answers in this exact wording:

| Canonical | Forbidden substitutes |
|---|---|
| `control` | `power over`, `decision authority` |
| `benefit` | `gain`, `upside` |
| `knowledge` | `awareness`, `what they knew` |
| `preventability` | `avoidability`, `could have stopped` |
| `record control` | `paper trail control`, `archive ownership` |
| `cost bearer` | `harmed party`, `loser` |

---

## How to extend

1. Re-run extraction: `python3 ~/.claude/plugins/cache/xiaolai/nlpm/0.8.23/analysis/scripts/extract-vocabulary.py --root . --scopes analysis/vocab-init-scopes.json --out analysis/vocabulary-extract/`
2. New terms appear in `analysis/vocabulary-extract/summary.md`.
3. Add a row to the right table above. Cite at least one file as evidence.
4. To deprecate a synonym, list it in the canonical term's "deprecated synonyms" column and mirror the entry in `registry.yaml`.

## Adopting R51

R51 is **off by default**. To enable vocabulary drift detection on this project, add to `.claude/nlpm.local.md`:

```yaml
rule_overrides:
  R51:
    enabled: true
    vocabulary_skill: .claude/skills/vocabulary/
```

Without this opt-in, R51 contributes zero penalty regardless of artifact contents.

## See also

- NLPM's own vocabulary skill (the template this was seeded from): `skills/nlpm/vocabulary/SKILL.md` in the NLPM repo.
- The six principles: `analysis/vocabulary-design-principles.md` in the NLPM repo.
- This project's case taxonomy: `.claude/rules/01-case-taxonomy.md`.
- This project's evidence grades: `.claude/rules/02-evidence-grades.md`.
- This project's style guide (verbs, banned phrases, chapter rhythm): `.claude/rules/04-style-guide.md`.

<example>
Context: Wayne is drafting a chapter and types "the algorithm did it" to describe a system/object alibi.
output: R51 flags "algorithm did it" as a substitute for the canonical `system/object alibi`. Suggested rewrite: "the algorithm is the named cause; the laundering moves blame from the team who deployed it to the model itself" — pulls the canonical taxonomy term into the prose so a later /source-audit can grade the surrounding claims.
</example>

<example>
Context: A new researcher proposes adding "framework" as an artifact-class noun.
output: Refused pending warrant. The term appears 1× in agent filenames (`jade-visual-framework-designer`), but no skill, command, or rule defines it as a distinct artifact class. Added to `rejected_pending_warrant:` in `registry.yaml` with a note pointing to the proposal. Will be reconsidered if frequency rises above 3 with a definition in a rule file.
</example>

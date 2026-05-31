---
description: "Treatment class discipline: every chapter entering a rewrite cycle declares exactly one of five treatment classes (no-change, prose-polish, defamation-safe-tighten, structural-polish, full-craft-rewrite) with cited defect evidence; class transitions are recorded with reason."
---

**Every chapter entering a rewrite cycle declares exactly one treatment class, with cited defect evidence; class transitions are recorded with reason.**

# Treatment Class Discipline

**Scope:** binds every chapter in `book/chapters-v2/` that enters the fiction-craft rewrite cycle. Closes the false binary between book-level "full rewrite" and "polish pass." Per-chapter treatment respects the truth that 13 chapters do not share one defect.

## The five treatment classes

| Class | When to use | What it costs | What it changes |
|---|---|---|---|
| `no-change` | Chapter passes all 10 reader-experience values in rule `12-reader-experience-values.md`; defect-map shows no actionable defect; further work would risk regression. | Zero. | Nothing. |
| `prose-polish` | Structure and architecture are sound; craft-value defects exist (rhythm, hammer-line, audio cadence, voice braid) but core values pass. Applies Bucket 1 craft moves #5, #6, #7, #8 from the analysis note inside the existing chapter architecture. | One light wayne-narrative-lead pass + audit chain. | Sentence-level prose; no structural change; no contract file needed. |
| `defamation-safe-tighten` | Chapter is sound on craft but has rule-05 or rule-07 surface that legal review flagged. Applies nancy-legal-risk-counsel pass with defamation-wording skill; wayne re-renders. | One nancy + one wayne pass + audit chain. | Specific paragraphs only; flagged in the chapter's defect-map. |
| `structural-polish` | Core values pass; one or two craft-value defects require structural movement (scene reorder, focalization adjustment, motif insertion) without full rewrite. | One bonnie-book-architect structural pass + one wayne pass + audit chain + cross-chapter audits. | Scene order, focalizer assignment, motif placement; contract file required; callback/motif/cognitive-arc audits run. |
| `full-craft-rewrite` | Defect map shows core-value failure AND craft-value failure; chapter requires the full Bucket 1 toolkit (document-as-protagonist, focalize-then-break, two-track time, delayed naming upward, voice braid, hammer-line reversal, resonant return, one image) inside the rewrite cycle. | One full chapter-production cycle equivalent + full audit chain + cross-chapter audits + nancy clock + laura red-team. | Everything below the case-file dossier layer; the dossier remains. |

## Declaration shape

`book/registries/treatment-classes.yml` holds the declaration:

```yaml
- chapter: 02
  slug: the-four-goats
  class: full-craft-rewrite
  defect_evidence:
    - {value: V3, defect: "reader sympathy lands on visible goat by end of chapter"}
    - {value: V5, defect: "discrimination 'partial vs pure scapegoat' announced but not installed"}
    - {value: V6, defect: "memorable scene without diagnostic carryover"}
  defect_map: process/defect-map/02-the-four-goats.md
  declared_at: 2026-05-27
  declared_by: chapter-defect-diagnose
  reviewed_by: [xaiolai]
  reclassifications: []   # appended to if class changes mid-cycle
```

A reclassification requires a reason and the same `reviewed_by` chain:

```yaml
  reclassifications:
    - {from: full-craft-rewrite, to: structural-polish, on: 2026-06-04,
       reason: "pilot showed full rewrite over-corrected; chapter only needed scene reorder",
       reviewed_by: [xaiolai]}
```

## Rules for the classes

1. **One class per chapter.** Mixed classes are not allowed; if a chapter has both prose-polish and defamation-safe-tighten work, the higher class wins (defamation-safe-tighten in this case).
2. **`no-change` requires evidence too.** A chapter cannot be classified `no-change` because no one looked at it; defect-map must exist and show passing values.
3. **Cross-chapter audits are inherited upward.** `structural-polish` runs the cross-chapter audits (callback, motif, cognitive-arc, dependency). `full-craft-rewrite` adds nancy clock and laura red-team. Lower classes inherit the audit set of the class they sit above only if their changes can affect that surface.
4. **Reclassification is allowed, not free.** Moving up the class ladder is allowed at any time and re-runs the higher class's audits. Moving down the ladder requires a recorded reason and re-validation that the lower class's audit set covers every audit surface touched by the changes actually made.
5. **Class is the input to the workflow, not the output.** A chapter does not become `full-craft-rewrite` because someone wants to do a full rewrite; it becomes `full-craft-rewrite` because the defect-map evidence requires it.

<example>
A chapter shows a V6 defect (memorable scene without diagnostic carryover) and a V10 defect (audio cadence breaks at the recognition beat). Core values V1, V3, V5, V7, V8 all pass per the defect-map.

The naive read says "two craft defects, full-craft-rewrite." Rule 08 rejects this. Core values pass; V6 requires re-staging the recognition beat within the existing chapter architecture; V10 requires sentence-rhythm work on three specific paragraphs.

Correct treatment class: `structural-polish` — scene reorder for V6, prose pass for V10, within the existing dossier. The `full-craft-rewrite` toolkit (document-as-protagonist, two-track time, voice braid) is not needed and would over-correct chapters that already pass V1/V3/V5/V7/V8.

Declaration:

```yaml
- chapter: 07
  slug: the-clean-record
  class: structural-polish
  defect_evidence:
    - {value: V6, defect: "memorable scene at line 142 carries no diagnostic; reader recalls scene but not pattern"}
    - {value: V10, defect: "three paragraphs (lines 88-104, 156-178, 220-244) break audio cadence at recognition beat"}
  defect_map: process/defect-map/07-the-clean-record.md
  declared_at: 2026-06-04
  declared_by: chapter-defect-diagnose
  reviewed_by: [xaiolai]
  reclassifications: []
```
</example>

## Why this rule exists

The plan critiqued by Codex (`dev-docs/fiction-craft-rewrite-implementation-plan.md`, Test D) presented Path R / Path P as a book-level binary. The honest state is that 13 chapters likely fall across all five classes. Treating the book as one homogeneous treatment forces either over-investment in stable chapters or under-investment in broken ones. Per-chapter classification is the only way to spend authorial time where it actually pays.

This rule is the constitutional anchor for `/chapter-defect-diagnose` and `/treatment-classify`. It is referenced by `book/STATUS.md` chapter-state tracking during a rewrite cycle.

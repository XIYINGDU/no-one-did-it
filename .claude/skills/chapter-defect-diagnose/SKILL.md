---
name: chapter-defect-diagnose
description: Diagnose a chapter against the 10 reader-experience values in rule 12 (5 core + 5 craft) and build a defect map naming which values fail, with cited prose evidence, and recommending one of the five treatment classes from rule 08. Output is `process/defect-map/<n>-<slug>.md` plus a treatment-class row appended to `book/registries/treatment-classes.yml`.
version: 1.0.0
---

# Chapter Defect Diagnose

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- Before any chapter rewrite cycle is authorized. The defect map is the precondition for `chapter-status: in-rewrite` per rule 09.
- After a substantial revision that may have changed which values pass or fail.
- During Phase 0 of any book-wide rewrite project to build the per-chapter defect inventory.

This skill is the cited diagnosis that replaces "I want it more gripping." Without it, treatment classes are assigned on intuition and Gate B has no measurable starting point.

## Decision rubric

For each of the 10 reader-experience values from `.claude/rules/12-reader-experience-values.md`, the diagnosis answers three questions with prose evidence:

1. **Does the chapter pass this value as currently written?** (`pass | conditional | fail | unscored`)
2. **What specific paragraphs or sentences are the evidence for the verdict?** (line anchors required)
3. **What treatment, if any, is needed?** (`none | prose-polish | structural-polish | defamation-safe-tighten | full-craft-rewrite`)

After diagnosing all 10 values, the skill picks ONE treatment class for the chapter per rule 08's table:

- All 10 values pass → `no-change`.
- Only craft values (V2/V4/V6/V9/V10) fail; core values pass → `prose-polish`.
- V7 or V8 fails on a live-content claim → `defamation-safe-tighten`.
- 1-2 craft + at most 1 core value fail; failure is structural → `structural-polish`.
- 2+ core values fail OR craft + core failures require Bucket 1 toolkit → `full-craft-rewrite`.

## Conflict handling

1. **Core value passes by craft but fails by evidence.**
   V7 passes because the prose sounds calibrated, but the underlying claim is B-grade. The diagnosis records V7 as `fail` and notes "V7 fails on evidence-grade mismatch despite calibrated prose; treatment must lift the source, not the prose." This protects against the chapter sounding right while being structurally wrong.

2. **Diagnosis output disagrees with prior audit.**
   If the chapter has a current audit-chapter report that says PASS but defect-diagnose finds a core value failure, the diagnosis takes precedence (it is more recent and uses the rule-12 rubric explicitly). Flag the difference in the open-questions section.

3. **Diagnosis cannot decide between two treatment classes.**
   Pick the higher class. Class inflation is recoverable (rule 08 permits reclassification down with reason); class deflation hides real defects.

4. **Diagnosis returns `unscored` on V6 (diagnostic memory) because the chapter has no beta-reader data.**
   Score V6 against a structural proxy: does the chapter's anti-laundering rule (style-guide beat 8) name a transferable pattern in plain language? If yes, V6 is at least `conditional`. If no, V6 is `fail`. Do not leave `unscored` in the output.

## Escalation conditions

- Escalate to xaiolai when the diagnosis assigns `full-craft-rewrite` to ch-01 or ch-13 — these are the book-boundary chapters and class assignment requires principal-author confirmation per the project's structural-stability principle.
- Escalate to Nancy when V7 or V8 fails and the chapter has live content (active litigation, named living individuals at chain positions, active corporate entities).
- Escalate to Laura when V1, V3, or V8 fails — Laura's red-team scope per rule 03 amendment covers exactly these values.
- Escalate to Bonnie when the diagnosis finds structural defects that imply the chapter brief itself needs revision (case selection, ordering, taxonomy match).
- Escalate to Stephen when V7 fails because of evidence-grade mismatch — fixing prose without fixing the source ledger merely papers over the issue.

## Boundary-case recipes

1. **Diagnosing a chapter at `status: ready` that has never been audited under rule 12.**
   Run all 10 values from cold. Use prior audit-chapter reports for context but do not let them anchor verdicts. The rubric is new; the chapter has not been measured against it.

2. **Diagnosing a chapter mid-rewrite cycle.**
   Compare against the pre-rewrite snapshot in `process/audits/history/<n>/<earliest-timestamp>/` rather than the original `status: ready` version. The diagnostic question is: has the rewrite improved or degraded each value?

3. **Diagnosing a chapter whose case-file dossier is in flux.**
   The dossier (`book/evidence/case-files/`) is the structural layer below the prose. If the dossier is being revised, defer defect-diagnose until the dossier stabilizes. Mid-flux diagnosis double-counts churn.

4. **Diagnosing a chapter with documented partial-scapegoat taxonomy where V3 is structurally hard.**
   Partial scapegoats (the visible actor IS culpable, but blame stops too low) make V3 (sympathy follows the chain) genuinely difficult; the reader's sympathy may legitimately split. In this case, V3 passes if the chapter installs a *structural* discrimination ("blame stopped here even though the chain extends further") rather than a sympathy transfer.

5. **Diagnosing a chapter that has been rewritten and the snapshot is missing.**
   The diagnosis flags the missing snapshot as a rule-09 violation. Do not proceed; either reconstruct the snapshot from git history or escalate to xaiolai.

## Output format

Two artifacts per skill run:

### Artifact 1: `process/defect-map/<n>-<slug>.md`

```markdown
---
chapter: <n>
slug: <slug>
diagnosed_at: <ISO date>
diagnosed_by: chapter-defect-diagnose
chapter_status_at_diagnosis: <ready|in-rewrite|in-review>
---

# Defect Map: <chapter title>

## Summary

- Total values evaluated: 10
- Pass: <n>, Conditional: <n>, Fail: <n>
- Recommended treatment class: <one of the 5 classes>
- Confidence: <high|medium|low> with one-line rationale

## Per-value diagnosis

### V1 — Earned, not manufactured
- Verdict: <pass|conditional|fail>
- Evidence: <line anchors + 1-2 sentence quote/paraphrase>
- Treatment if fail: <one of the 5 classes>

[... repeat for V2 through V10 ...]

## Treatment class recommendation

- **Class:** <full-craft-rewrite | structural-polish | defamation-safe-tighten | prose-polish | no-change>
- **Rationale:** <which values drove the choice; why this class and not the adjacent one>
- **Downstream artifacts touched:** <list of review-memos, sidecars, case-file references the rewrite will invalidate>
- **Cross-chapter risk:** <which other chapters' callbacks / motifs / discriminations may be affected>

## Handoff

- Owner: <next agent>
- Open questions: <unresolved decisions for Gate A or principal author>
```

### Artifact 2: append row to `book/registries/treatment-classes.yml`

Per the schema in rule 08. The skill builds the row idempotently — if the chapter already has a row, the skill appends to `reclassifications:` rather than overwriting.

## Examples

<example>
Context: principal author runs `/chapter-defect-diagnose 02-the-four-goats` to begin the Stage 0 inventory. The chapter is at `status: ready` and has never been rule-12 audited.

assistant: "Diagnosis complete for ch-02 (the-four-goats). 6 pass, 1 conditional, 3 fail. V3 fails (sympathy lands on Calley by L312; chain at L380 is named but not weighted). V5 fails (partial/pure discrimination is announced at L210 but not consolidated; reader exits without the ability to apply it). V6 conditional (anti-laundering rule at L640 is portable but the chapter's memorable moments are scene-level not pattern-level). V8 conditional (one paragraph at L195 implies command knowledge without citation). Recommended class: full-craft-rewrite. Confidence: high. Downstream: invalidates 02-stephen-fact-check and 02-laura-red-team review memos; preserves all 9 case files. Escalating to xaiolai for class confirmation since ch-02 is in the forced reading-order chain (1→2→3) and a boundary-adjacent chapter."
<commentary>
The diagnosis is specific (line anchors), cites evidence (V3 fail tied to L312/L380), routes per the escalation list (xaiolai because of structural position), and builds both artifacts. Confidence "high" because three failures all map to the rubric cleanly.
</commentary>
</example>

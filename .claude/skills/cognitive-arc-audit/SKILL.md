---
name: cognitive-arc-audit
description: Audit the book's cognitive arc — the discriminations and concepts the reader acquires chapter by chapter — against the actual prose. For each discrimination, verifies introduction, consolidation, and application in every required chapter. For each concept, verifies it is named and used. Reads `book/registries/cognitive-arc.yml`.
version: 1.0.0
---

# Cognitive Arc Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After any rewrite under `structural-polish` or `full-craft-rewrite` per rule 08, run book-wide.
- Whenever a chapter's contract `knows:` or `can_discriminate:` slot is edited (chapter-level cognitive deliveries must match book-level arc declarations).
- Whenever `book/registries/cognitive-arc.yml` is edited.
- At Stage 2 baseline run.

## The cognitive arc

`book/registries/cognitive-arc.yml` declares two things: discriminations the reader acquires, and concepts the chapter introduces:

```yaml
discriminations:
  - id: distinguish-pure-from-partial-scapegoat
    introduced_in: 02
    consolidated_by: 04
    required_by: [05, 07, 09, 11, 13]
  - id: identify-system-or-object-alibi
    introduced_in: 03
    consolidated_by: 06
    required_by: [10, 12, 13]
concept_introductions:
  - {id: responsibility-chain, ch: 01}
  - {id: alibi-shell, ch: 03}
  - {id: record-control, ch: 04}
retirements:
  - {id: pre-book-frame:complexity-equals-innocence, retired_by: 02}
```

A discrimination is a distinction the reader can apply (pure vs partial scapegoat; system alibi vs cost-bearing goat). A concept is a named term the chapter introduces and the book then uses (responsibility chain, alibi shell, record control). A retirement is a pre-book misconception the book actively dismantles.

## Decision rubric

The audit runs three passes book-wide:

### Pass 1: discrimination installation
For each discrimination:
- Chapter `introduced_in:` must contain a passage naming the discrimination (the two things being distinguished AND the criterion that separates them).
- Chapter `consolidated_by:` must contain a passage demonstrating the discrimination in action (a worked example or comparison that applies the distinction).
- Every chapter in `required_by:` must use the discrimination at least once (a sentence whose meaning depends on the reader being able to apply the distinction).

If `required_by:` chapter K uses the discrimination but K precedes `consolidated_by:`, the discrimination is required before installed — hard fail.

### Pass 2: concept introduction
For each concept:
- Chapter `ch:` must name the concept explicitly and use it (definition + at least one application within the chapter).
- Subsequent chapters that reference the concept by name must occur AFTER the introduction chapter; references before introduction are forward dependencies — hard fail.

### Pass 3: retirement integrity
For each retirement:
- Chapter `retired_by:` must contain a passage explicitly addressing the pre-book frame and showing why it does not apply.
- No subsequent chapter may reintroduce the retired frame as an active premise (the chapter may mention the retired frame as historical context, but cannot rest a load-bearing argument on it).

## Conflict handling

1. **Rewrite cut the discrimination's installation passage from the `introduced_in:` chapter.**
   Hard fail at Pass 1; either Wayne restores the passage OR Bonnie reassigns `introduced_in:` to a different chapter that genuinely installs it (requires coordinated arc edit).

2. **Rewrite added a chapter reference to a concept that hasn't been introduced yet.**
   Forward dependency (Pass 2 fail). Either move the reference to a chapter AFTER the introduction, or introduce the concept earlier (requires arc revision and possibly chapter ordering change).

3. **Rewrite changed the chapter ordering and now `required_by:` chapter precedes `consolidated_by:`.**
   Hard fail. Bonnie coordinates chapter-order revision with cognitive-arc revision; both files must change together.

4. **Discrimination is required by ch-13 but only mentioned in passing in `consolidated_by:` ch-06.**
   Soft fail at Pass 1; the discrimination is installed but thinly. Either Wayne strengthens the consolidation in ch-06, OR Bonnie adds an additional consolidation chapter to the discrimination's metadata.

5. **A retired pre-book frame appears in a later chapter as load-bearing.**
   Hard fail at Pass 3. The book is undoing its own work. Either Wayne revises to use the retired frame as historical context only ("readers familiar with the older framing might assume X; the chain shows Y"), or the retirement was wrong and should be removed from the arc.

## Escalation conditions

- Escalate to Bonnie for any arc structure change (reassigning `introduced_in:`, `consolidated_by:`, `required_by:`, or chapter ordering).
- Escalate to Wayne for missing installation, consolidation, or application passages.
- Escalate to xaiolai when the arc revision implies the book's reading order is broken (forced sequence in `book/toc.yml` no longer holds).
- Escalate to Stephen when a discrimination's installation rests on a B/C-grade source; the discrimination's authority depends on its example's evidence grade.
- Escalate to Laura when a discrimination is installed but rule-12 V5 (capacity change) fails on the consolidating chapter — the reader is given the label but not the capacity to apply it.

## Boundary-case recipes

1. **First-time cognitive-arc build (Stage 2 baseline run).**
   Skill traverses chapter contracts (where `can_discriminate:` and `knows:` slots are declared) and chapter prose to identify candidate discriminations and concepts. Output is a proposed arc for Bonnie + xaiolai to verify. The skill does not auto-build the arc; humans verify.

2. **Auditing the boundary chapters' role in the arc.**
   ch-01 typically introduces multiple concepts; ch-13 typically requires every discrimination installed by the book. Boundary-chapter rewrites have outsized arc impact. Treat boundary-chapter audit findings as high priority.

3. **Auditing a chapter that uses a discrimination NOT declared in `required_by:`.**
   Two interpretations: (a) the chapter is opportunistically using a discrimination it was not asked to, which is fine and may indicate the arc should add this chapter to `required_by:`; (b) the chapter is asking the reader to apply a discrimination they may not have, which is a silent forward dependency. Default to interpretation (b) and flag for Bonnie review.

4. **Auditing a chapter that introduces a concept NOT declared in `concept_introductions:`.**
   Candidate-concept finding; route to Bonnie + xaiolai for either arc addition or concept simplification. Unregistered concepts proliferate the book's vocabulary; rule-driven audits help contain.

5. **Auditing after a chapter is reclassified from `full-craft-rewrite` to `no-change` mid-cycle.**
   The chapter's installation / consolidation / application status reverts to its pre-rewrite state; arc verifies against that reverted prose. No audit failure caused by the reclassification itself.

## Output format

```text
Owner: cognitive-arc-audit (skill run by <bonnie|joe>)
Task: Audit book/registries/cognitive-arc.yml against current chapter prose
Inputs reviewed:
  - book/registries/cognitive-arc.yml
  - book/chapters-v2/*.md (all chapters referenced in the arc)
  - book/chapters-v2/*.contract.yml (for slot consistency)
Output: cognitive-arc-audit memo at process/audits/cognitive-arc-audit-<ISO-date>.md
Evidence grade: N/A
Assumptions: <e.g., discriminations require both naming AND demonstration; mere mention does not install>
Open questions: <candidate discriminations or concepts; arc structure questions>
Risks: <chapters near required-before-consolidated boundary>
Handoff: <bonnie for arc / wayne for prose>
```

Per-discrimination findings:

| Discrimination id | Introduced (verdict) | Consolidated (verdict) | Required-chapters use (n/N) | Action |
|---|---|---|---|---|

Per-concept findings:

| Concept id | Introduction chapter (verdict) | Forward-reference count | Action |
|---|---|---|---|

Retirement findings:

| Retirement id | Retired-by chapter (verdict) | Re-introductions found | Action |
|---|---|---|---|

## Examples

<example>
Context: ch-04 rewritten under `structural-polish`. Wayne ran `/contract-audit` and got a `can_discriminate:` slot conditional. Jerry escalates to `/cognitive-arc-audit`.

A: "Cognitive-arc-audit complete. 3 discriminations checked. 2 pass cleanly. 1 issue: discrimination `distinguish-proxy-from-direct-actor` — introduced_in ch-04 passage at L210 names the distinction; consolidated_by ch-04 is the SAME chapter and the worked example at L312 demonstrates it; both checks pass. BUT required_by lists ch-06, ch-09; ch-06 uses the discrimination at L88 implicitly (sentence depends on reader knowing proxy vs direct actor) but does not name it — that's permissible. ch-09 at L240 uses 'the proxy' as a noun phrase assuming the reader has the discrimination. All required-chapter uses pass. So the discrimination is fully installed and applied. No arc failure; the contract-audit conditional was correct that consolidation was thin, but the arc-level demonstration suffices. Recommend Wayne strengthen consolidation at ch-04 L312 if the contract-audit V5 finding still concerns him."
<commentary>
The arc audit verifies that the chapter-level contract conditional was real but does not bubble up to a book-level failure. The two audits cross-verify each other; in this case the higher-level audit cleared the lower-level concern. That's the right composition.
</commentary>
</example>

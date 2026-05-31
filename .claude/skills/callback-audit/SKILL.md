---
name: callback-audit
description: Audit the book-level callback graph that tracks setup → payoff edges across chapters. Verifies every planted anchor has its declared downstream payoff and every payoff still has its upstream plant. Catches orphaned plants and orphaned payoffs. Reads `book/registries/callback-graph.yml`; runs book-wide when any graph chapter is rewritten. Cousin of fair-clue-audit (which covers chapter-internal recognition).
version: 1.0.0
---

# Callback Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After any chapter rewrite under treatment class `structural-polish` or `full-craft-rewrite` per rule 08.
- Before any chapter promotion from `in-review` to `ready` when the chapter participates in callback graph edges (either as plant origin or payoff destination).
- At book level during Stage 2 baseline run per rule 09 to establish the pre-rewrite callback state.
- Whenever `book/registries/callback-graph.yml` is edited.

## The callback graph

`book/registries/callback-graph.yml` is a list of edges. Each edge records one setup → payoff pair:

```yaml
- id: foia-folder-marked-classified
  type: object_callback | phrase_callback | scene_callback | rule_callback
  payoff_kind: re-reading | reversal | confirmation | refutation
  required: true
  planted:
    chapter: 02
    section: §3
    line_anchor: "the manila folder, edge stamped"
  paid_off:
    chapter: 09
    section: §7
    line_anchor: "the same edge stamp, now meaningless"
```

A `required: true` callback fires a hard fail if its payoff is missing. A `required: false` callback fires a soft flag. Ambient callbacks (atmospheric repetition without explicit narrative purpose) are marked `payoff_kind: ambient` and not audited.

## Decision rubric

The audit runs four passes book-wide:

### Pass 1: plant verification
For each edge, the `planted.line_anchor` substring must appear in the planted chapter at or near the declared section. Match tolerance: substring within 5 lines of declared line; tagged as "drifted" if found outside that window, "missing" if not found.

### Pass 2: payoff verification
For each edge, the `paid_off.line_anchor` substring must appear in the payoff chapter at or near the declared section. Same drift/missing classification as plant verification.

### Pass 3: orphan audit
Two orphan classes:

- **Plant orphan:** plant exists but no edge references it as a `paid_off`. Permitted if the plant has explicit `purpose: ambient` declared in the chapter contract. Otherwise: flag for resolution.
- **Payoff orphan:** payoff references an edge that has no plant in the upstream chapter. Hard fail; either the upstream chapter cut the plant (revert OR replant elsewhere), or the payoff was added without authorization.

### Pass 4: callback-class integrity audit
- `object_callback`: planted artifact and payoff artifact must be the same artifact (same name, same identifying detail). If the planted object is "the manila folder, edge stamped" and the payoff references "the brown envelope," the callback is broken even if both anchors are present.
- `phrase_callback`: planted phrasing and payoff phrasing must share a load-bearing word or image. Tolerance: paraphrase permitted if the paraphrase preserves the recognition cue.
- `scene_callback`: payoff scene must structurally mirror the planted scene (parallel setting, parallel beats, parallel image). Match by structural description in the edge metadata.
- `rule_callback`: a rule stated in the planted chapter (typically the anti-laundering rule) must be applied or violated in the payoff chapter explicitly. The payoff text should name the rule or its concept.

## Conflict handling

1. **Plant has drifted by 20 lines because the planted chapter was rewritten under `structural-polish`.**
   Update the edge's `planted.line_anchor` and `planted.section` to match the new location; record the move in the edge's `revision_history:` field. No audit failure if the substring still matches and the planted artifact is unchanged.

2. **Payoff is now in a different chapter because of scene reorder.**
   Coordinate amendment with Bonnie: update the edge's `paid_off.chapter` and `paid_off.section`. If the payoff moved across the chapter boundary (e.g., to a different chapter entirely), this is a cognitive-arc concern; also run `/cognitive-arc-audit`.

3. **Required callback was deliberately cut during rewrite (e.g., the original payoff scene was deleted as part of structural revision).**
   Edge cannot be silently deleted. Either: (a) replant the payoff somewhere else and update the edge, (b) downgrade the edge's `required:` field to false with reason, or (c) delete the edge entirely with reason recorded in `book/registries/callback-graph.yml`'s `removed_edges:` section.

4. **Ambient plant being audited because a chapter rewrite changed it.**
   If the plant is genuinely ambient (no payoff edge exists or is planned), the audit flags its presence and exits without failure. If the plant was MEANT to be a callback but no edge was ever registered, escalate to Bonnie — the callback graph is incomplete.

5. **Plant and payoff both exist but the callback-class integrity audit fails (e.g., object_callback where the artifact identity drifted).**
   Hard fail. Either restore the object identity or reclassify the edge to `phrase_callback` (looser match) with reason.

## Escalation conditions

- Escalate to Wayne when plant or payoff drift requires prose adjustment to restore the cue.
- Escalate to Bonnie when callback restructuring requires scene reorder or cross-chapter coordination.
- Escalate to xaiolai when 3+ callbacks fail in a single rewrite cycle — the rewrite may have damaged the book-level integration in ways that warrant pausing the cycle.
- Escalate to Stephen when an `object_callback` references an artifact whose existence is contested in the source ledger — the callback's load-bearing nature requires A-grade evidence for the artifact.
- Escalate to Laura when a `rule_callback` involves the chapter's anti-laundering rule and the payoff's application of the rule is rhetorically forceful but logically loose.

## Boundary-case recipes

1. **First-time callback graph build (Stage 2 baseline run).**
   Skill traverses every chapter to identify candidate callbacks not yet in the graph. Output is a proposed-edges list for Bonnie + xaiolai to review. The skill does not auto-add edges to the graph; humans verify callbacks before they become enforceable.

2. **Auditing an edge whose plant is in a chapter that hasn't yet been rewritten.**
   Permitted; the plant should be unchanged from the original. If the plant has drifted (substring not found), flag as "pre-existing drift" — not caused by current rewrite, but worth recording.

3. **Auditing the boundary chapters (ch-01, ch-13).**
   ch-01 plants many callbacks; ch-13 pays off many. When ch-01 is rewritten (last per the project's structural-stability principle), expect a high callback-touch count — that's a feature, not bug, but each touch must be cleared explicitly.

4. **Auditing a chapter where the contract amendment changed a `primed_for:` slot that corresponds to a callback edge.**
   Coordinate with `/contract-change-control` output; the contract amendment should already have flagged the downstream callback for re-audit. The callback-audit then verifies the actual prose still supports the edge.

5. **Auditing the book at Phase 0 (no rewrites yet).**
   Establishes the baseline. Any edge that fails baseline is pre-existing technical debt and is logged but not blamed on the rewrite cycle.

## Output format

```text
Owner: callback-audit (skill run by <joe|bonnie|wayne>)
Task: Audit book/registries/callback-graph.yml against current chapter prose
Inputs reviewed:
  - book/registries/callback-graph.yml
  - book/chapters-v2/*.md (all chapters with edges)
  - process/audits/history/<n>/<timestamp>/ (snapshots if baseline comparison required)
Output: callback-audit memo at process/audits/callback-audit-<ISO-date>.md
Evidence grade: N/A
Assumptions: <e.g., baseline run uses pre-rewrite snapshots>
Open questions: <edges awaiting resolution>
Risks: <required edges that may fail if downstream chapter is rewritten next>
Handoff: <next owner per failure mode>
```

Edge-by-edge findings:

| Edge id | Plant verdict (pass/drifted/missing) | Payoff verdict | Class-integrity verdict | Required? | Action |
|---|---|---|---|---|---|

Orphan findings:

| Orphan type | Chapter | Line | Recommendation |
|---|---|---|---|

Summary row: total edges / pass / drifted / missing / class-integrity-fail / orphans.

## Examples

<example>
Context: ch-04 was rewritten under `structural-polish`; the rewrite reordered scenes. Jerry runs `/callback-audit` book-wide.

A: "Callback-audit complete. 23 edges checked. 21 pass cleanly. 1 plant drifted (edge `proxy-payment-receipt`: planted in ch-04 §3, now at L189 instead of declared L142 — chapter rewrite moved the scene). Updating planted.section to §3 and planted.line_anchor remains valid; recording move in revision_history. 1 hard fail (edge `chain-disclosure-rule`: rule planted in ch-04 §6, payoff in ch-10 expected the rule application in ch-10's recognition beat, but ch-10's recognition no longer references the rule explicitly — ch-10 unaffected by ch-04 rewrite, so this is pre-existing drift in ch-10 that the ch-04 audit surfaced). Escalating to Bonnie for ch-10 review. No orphans introduced by ch-04 rewrite."
<commentary>
Real callback-audit shape: most edges hold, one drifts harmlessly (mechanical update), one fails but for a pre-existing reason (escalation, not rewrite blame). The audit distinguishes rewrite-caused damage from surfaced pre-existing debt.
</commentary>
</example>

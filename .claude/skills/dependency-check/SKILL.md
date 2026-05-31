---
name: dependency-check
description: Cross-chapter dependency analyzer — combines the callback graph, motif registry, and cognitive arc into a single DAG. Identifies forward dependencies (hard fail), lateral dependencies on revised chapters (soft fail with blast radius), and cut-chapter blast radius. Runs after every chapter rewrite to surface downstream consequences before they ship.
version: 1.0.0
---

# Dependency Check

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After every chapter rewrite that produces an `in-review` status — before promotion to `ready`.
- Before authorizing a chapter cut (deletion or major scope reduction) — the cut blast-radius is the chapter's footprint on the rest of the book.
- At Stage 2 baseline run to identify pre-existing dependency violations not caused by any rewrite.
- Whenever any of the three book-level data files change: `book/registries/callback-graph.yml`, `book/registries/motif-registry.yml`, `book/registries/cognitive-arc.yml`.

## The dependency DAG

The skill reads three data files and combines them into a single dependency graph. Each chapter is a node. Edges:

- **Callback edges** from `book/registries/callback-graph.yml`: planted-chapter → paid-off-chapter.
- **Motif edges** from `book/registries/motif-registry.yml`: each motif's appearance chain forms a sequence of edges.
- **Cognitive edges** from `book/registries/cognitive-arc.yml`: introduced-chapter → consolidated-chapter → each required-by chapter; concept-introduction-chapter → each chapter that references the concept.

The combined graph must be a DAG (directed acyclic graph). Cycles indicate forward dependencies; the audit's first job is to find them.

## Decision rubric

### Pass 1: forward dependency (hard fail)
Walk the graph. If any edge points from a chapter with higher number to a chapter with lower number AND the lower-numbered chapter requires content delivered by the higher-numbered chapter, the lower-numbered chapter depends on something not yet introduced. Hard fail.

Caveat: the project's authorized reading order is NOT strict chapter-number order (see `book/STATUS.md` for the DAG: forced 1→2→3, then 11→12→13; loose parallel in parts II/III). The audit uses the authorized reading-order DAG, not raw chapter numbers, to define "later." Forward dependency is relative to authorized reading order.

### Pass 2: lateral dependency on revised chapter (soft fail)
When chapter K is rewritten and now under audit, identify every chapter L (regardless of K-vs-L order) that has an incoming edge from K. Each such L is potentially affected by the rewrite. The audit:

- For callback edges: verifies the L-chapter's payoff still works given K's new prose (delegates to `/callback-audit`).
- For motif edges: verifies the L-chapter's motif appearance still works in concert with K's appearance (delegates to `/motif-audit`).
- For cognitive edges: verifies the L-chapter can still apply discriminations / concepts K installed (delegates to `/cognitive-arc-audit`).

Lateral dependencies are reported but not auto-failed; they're routed to the responsible sub-audit which is the authority on whether the L-chapter actually broke.

### Pass 3: cut-chapter blast radius
If chapter K is being cut (deleted, or scope-reduced beyond a threshold), the audit reports every edge with K as endpoint:

- Outgoing callback edges (K plants, downstream chapter pays off): each downstream payoff is at risk.
- Incoming callback edges (upstream chapter plants, K pays off): each upstream plant becomes orphaned.
- Motif appearances in K: each motif's frequency floor may drop below threshold.
- Cognitive arc roles K plays (introduced_in / consolidated_by / required_by): the arc structure breaks at K's removal.

The cut blast-radius is informational — the skill doesn't decide whether to cut; it tells the human what cutting K costs.

## Conflict handling

1. **Forward dependency exists in baseline (pre-rewrite).**
   Pre-existing technical debt. Log as baseline issue; do not blame on any rewrite. Escalate to Bonnie for arc revision or chapter reordering, but the current rewrite cycle is not the trigger.

2. **Rewrite of ch-K introduces a forward dependency from ch-L (where L < K in reading order).**
   The rewrite added a reference to something not yet established. Wayne must remove the reference, OR Bonnie must reorder chapters, OR the dependency must be moved earlier in K's prose (often: the new chapter K now needs an in-chapter setup that the rewrite removed assuming downstream chapters had it).

3. **Lateral dependency exists but downstream sub-audit (callback/motif/cognitive) reports the chapter still passes.**
   No action required. The dependency is potential, not actual. Flag in the audit memo so future rewrites know to re-audit.

4. **Cut-chapter blast radius is large but the chapter cut is intentional (e.g., chapter being replaced by a different chapter).**
   The skill builds the blast-radius report; the human (xaiolai + Bonnie) decides whether the cut is worth the consequences. The replacement chapter must replant every edge from the cut chapter.

5. **Dependency check finds an edge that no longer exists in any data file but is implied by the prose.**
   Candidate-edge finding; route to Bonnie for registration. Edges that exist in prose but not in registries are silent debt — they will fail audits at unpredictable moments.

## Escalation conditions

- Escalate to Bonnie for any forward dependency requiring arc or chapter-order revision.
- Escalate to Wayne for prose-level fixes to introduced dependencies.
- Escalate to xaiolai when the cut blast-radius report is presented for decision.
- Escalate to the responsible sub-audit (`/callback-audit`, `/motif-audit`, `/cognitive-arc-audit`) for the actual verification of whether lateral dependencies broke.
- Escalate to Stephen when a discovered prose-level edge has an evidence-grade dependency (the downstream chapter's claim depends on a source the upstream chapter cited).

## Boundary-case recipes

1. **Running dependency-check on a chapter not yet in `book/registries/callback-graph.yml` etc.**
   The audit reports the chapter as "no declared dependencies"; this is either correct (chapter is genuinely independent) or a registration gap. Cross-verify by reading the chapter prose for callback / motif / concept references; flag candidates if found.

2. **Running dependency-check after a registry edit but no chapter edit.**
   Permitted; the registry edit may have built or broken edges. The audit catches new edges that no chapter prose supports (orphan edges added to data files).

3. **Running dependency-check on the boundary chapters (ch-01 plants the most; ch-13 receives the most).**
   Expect the largest lateral-dependency lists. The skill reports them all but most should clear via the sub-audits. The exception is ch-13: cuts or scope-reductions to ch-13 are essentially equivalent to cuts to the book's resonant return; treat as Gate B level decision.

4. **Running dependency-check at Stage 2 baseline.**
   Establishes the baseline DAG. Forward-dep findings here are pre-existing and should be triaged immediately — they are silent landmines for the rewrite cycle.

5. **Dependency check on a chapter cut from `book/toc.yml` but still on disk.**
   The cut is informational (the chapter is no longer in the canonical sequence). Run the cut-blast-radius report; the disk-file may stay as historical reference, but its edges must be removed from the data files.

## Output format

```text
Owner: dependency-check (skill run by <joe|bonnie>)
Task: Cross-chapter dependency analysis for <chapter rewrite | book baseline | proposed cut>
Inputs reviewed:
  - book/registries/callback-graph.yml
  - book/registries/motif-registry.yml
  - book/registries/cognitive-arc.yml
  - book/toc.yml (for authorized reading order)
  - book/chapters-v2/*.md (if candidate-edge discovery requested)
Output: dependency-check memo at process/audits/dependency-check-<chapter|baseline>-<ISO-date>.md
Evidence grade: N/A
Assumptions: <e.g., authorized reading order per book/toc.yml; lateral verification delegated to sub-audits>
Open questions: <candidate edges; sub-audit verdicts pending>
Risks: <highest-leverage edges that another rewrite would break>
Handoff: <bonnie for arc | wayne for prose | sub-audits for verification>
```

Forward-dependency findings:

| From chapter | To chapter | Dependency type | Reading-order distance | Action |
|---|---|---|---|---|

Lateral-dependency findings (rewrite mode only):

| Rewritten chapter (K) | Downstream chapter (L) | Edge type | Sub-audit | Sub-audit verdict |
|---|---|---|---|---|

Cut-blast-radius (cut mode only):

| Edge type | Counterpart chapter | Edge id / motif id / concept id | Action if K is cut |
|---|---|---|---|

## Examples

<example>
Context: ch-04 rewrite complete; ch-04 in-review. Jerry runs `/dependency-check 04` before promoting.

A: "Dependency-check complete for ch-04. Forward-deps: none (clean). Lateral-deps: 7 edges from ch-04 reach downstream chapters. 1 callback to ch-09 (delegated to callback-audit: drifted-but-recoverable, see prior memo). 2 motif appearances downstream (delegated to motif-audit: 1 frequency-floor concern flagged). 3 cognitive-arc applications in ch-06, ch-07, ch-09 (delegated to cognitive-arc-audit: all pass). 1 candidate edge discovered in prose at ch-04 L412 referencing 'the disclosure rule from ch-02' — not in callback-graph; route to Bonnie for registration as rule_callback. Overall: ch-04 can promote to ready conditional on (a) Wayne's planned fix for the ch-09 callback drift, (b) Bonnie's registration of the L412 candidate edge. No forward-deps blocking. No cuts proposed; blast-radius report skipped."
<commentary>
The skill aggregates the cross-chapter picture, delegates verification to the named sub-audits, and identifies one untracked dependency that the rewrite built. The chapter can promote conditional on two named fixes — a clean handoff.
</commentary>
</example>

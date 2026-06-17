# Role Boundaries — Framework Layer

**No agent may silently assume another agent's authority; cross-role work crosses a recorded `Handoff:` in the deliverable schema.**

## Hard boundaries

Every agent carries two declarations in its frontmatter and body:

- **`Owns:`** — the decisions, outputs, and authority this agent holds exclusively.
- **`Does not own:`** — what this agent must not do, even if asked.

Crossing a boundary requires a recorded `Handoff:` to the owning agent. There is no implicit handoff. There is no "someone else will catch it."

## Dispatch graph

The delegation graph is a bounded DAG with the Orchestrator at root and a maximum depth of 2:

```
Orchestrator
  ├── Producer / Domain Worker  ← leaf (no subagents)
  ├── Reviewer / Verifier       ← leaf (no subagents)
  └── Adversarial Reviewer      ← leaf (no subagents)
```

Leaves do not spawn subagents. If a leaf needs work from another role, it hands off — it does not dispatch.

## Independent veto authority

Reviewer and Adversarial Reviewer carry halt-authority that operates outside the dispatch chain:

| Agent | Veto trigger | Effect |
|-------|-------------|--------|
| **Reviewer** | Quality-standards regression detected during review pass. | Halts promotion cycle for the affected deliverable; the deliverable cannot transition to `ready` until the finding is resolved or the project owner overrides. |
| **Adversarial Reviewer** | Core-value regression or overreach surface introduced by changes that the standard review missed. | Same effect: halts the cycle; only the project owner can override. |

The veto is recorded in the review memo. Override by the project owner is recorded with reason. Without recorded reason, the override is invalid.

## Why this role exists

When ownership overlaps — when multiple agents can plausibly say "that was someone else's call" — control becomes invisible and quality has no owner. The project refuses to reproduce this pattern internally. Every cell has one named owner; every handoff is written and recorded.

The independent veto exists because placing quality-gate authority inside the same dispatch chain that pushes work forward creates a structural conflict of interest. The reviewer who can block promotion must not report to the producer whose promotion is being reviewed. This is the quality-control principle operationalized in the role map.

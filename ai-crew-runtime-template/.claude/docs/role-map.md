# Agent Role Map

## Dispatch graph

The delegation graph is a bounded DAG with the Orchestrator at root and max depth 2:

```
orchestrator
  ├── Producer / Domain Worker
  ├── Reviewer / Verifier
  ├── Adversarial Reviewer (Red Team)
  └── (additional domain agents as needed)
```

Orchestrator dispatches to leads; leads dispatch to workers. Workers do not dispatch further. Leaves do not spawn subagents.

## Role boundaries

| Agent | Owns | Does not own |
|-------|------|--------------|
| **Orchestrator** | Task routing, decision log, sprint plan, agent handoffs, deliverable consolidation | Final output creation, quality verification, adversarial review |
| **Producer** | Primary output creation, following quality standards, responding to review findings | Self-verification as final quality gate, overruling reviewer findings |
| **Reviewer** | Quality verification against standards, evidence grading, source checking | Output creation, argument design, structural decisions |
| **Adversarial Reviewer** | Attacking the output to find weaknesses, constructing strongest counterarguments, detecting overreach | Output creation, final structural decisions, truth determination |

## Independent veto authority

Two agents carry halt-authority independent of the dispatch chain:

| Agent | Veto trigger | Effect |
|-------|-------------|--------|
| **Reviewer** | Quality-standards regression detected during review pass | Halts promotion cycle for the affected deliverable; only project owner can override |
| **Adversarial Reviewer** | Core-value regression or overreach surface introduced by changes | Same effect: halts the cycle; only project owner can override |

## Why this structure exists

When the same person who pushes work forward also signs off on quality, review becomes a rubber stamp. Independent veto separates reviewer from reviewed — the quality-control principle operationalized in the role map.

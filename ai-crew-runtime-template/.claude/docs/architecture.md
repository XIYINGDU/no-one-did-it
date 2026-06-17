# System Architecture — 7-Layer Runtime Model

> This document describes the architecture of the `.claude/` multi-agent runtime. It is a snapshot; the canonical source is the live `.claude/` directory. `scripts/validate_workspace.py` verifies that the declarations here match reality.

## The 7 layers

```
┌──────────────────────────────────────────────────┐
│ Layer 1: Entry (commands/)                        │
│ User → system bridge. Declares owner agent.       │
│ Commands route; they do not execute logic.         │
├──────────────────────────────────────────────────┤
│ Layer 2: Dispatch (agents/)                       │
│ Role definitions + dispatch logic.                 │
│ Owns/Does-not-own hard boundaries.                 │
│ Unified model. Role-weighted maxTurns.             │
├──────────────────────────────────────────────────┤
│ Layer 3: Method (skills/)                         │
│ Reusable decision frameworks. Each defines:        │
│ usable/weak standards, conflict handling,          │
│ escalation conditions, edge cases.                 │
├──────────────────────────────────────────────────┤
│ Layer 4: Constraints (rules/)                     │
│ Constitutional rule hierarchy. Six tiers:          │
│ values → framework → craft → workflow →            │
│ experience → output. Scope + why-it-exists.        │
├──────────────────────────────────────────────────┤
│ Layer 5: Execution (hooks/)                       │
│ Rule→code automated fences. Triggers on            │
│ Write/Edit. warn/deny grading. Pattern             │
│ scan at layer; deny gate at promotion.             │
├──────────────────────────────────────────────────┤
│ Layer 6: Persistence (state/ + agent-memory/)     │
│ Cross-session continuity. Sprint state +           │
│ decision memory. SessionStart hook injects         │
│ context.                                           │
├──────────────────────────────────────────────────┤
│ Layer 7: Reference (docs/)                        │
│ Human-readable snapshots. Declarations             │
│ independently verified by scripts/.               │
└──────────────────────────────────────────────────┘
```

## Layer coupling

These layers are not a call stack — they are different abstraction levels of the same system. Upper layers define intent; lower layers enforce it:

| Layer | Defines | Enforced by |
|-------|---------|-------------|
| rules/ | "Deliverables must pass quality gate" | hooks/ auto-scans every edit |
| rules/ | "Deliverables at `status: ready` must satisfy all conditions" | hooks/ deny at promotion |
| agents/ | "Reviewer owns verification, not creation" | tools field restricts dispatch |
| skills/ | "Quality review must cover all dimensions" | skill decision criteria followed at execution |
| state/ | "Current sprint: 3 deliverables pending review" | SessionStart hook injects context |

## Core collaboration mechanisms

### 1. Trinity (Rule → Hook → Skill)

| Layer | Trigger frequency | Review depth |
|-------|-------------------|--------------|
| **Hook** (auto-scan) | Every Write/Edit | Cheap pattern match — catches mechanical violations |
| **Skill** (deep read) | At specific gate, by specific agent | Judgment-level violations — requires contextual understanding |
| **Rule** (constitutional) | Referenced by Hook and Skill | Defines what counts as a violation and why |

### 2. Independent veto

Quality gatekeepers carry halt-authority independent of the dispatch chain. Only the project owner can override.

### 3. Handoff as routing protocol

Cross-cell async handoffs with explicit attribution. No nested Agent() calls crossing cell boundaries. Every deliverable ends with `Handoff: <next-owner>`.

### 4. Constitutional auto-sync

Single source file → sync script → multiple target files. Edit one source; all targets update. `--check` mode verifies byte-level consistency in the test suite.

### 5. Memory as immune system

Agent errors are recorded as `feedback_*` memory files. Next time the agent activates, the memory loads and the error does not repeat.

### 6. State file as orchestration hub

A single status board tracks all deliverable stages. Cross-session recoverable: the board is the truth source, not in-memory state.

## See also

- `.claude/docs/role-map.md` — agent roles and dispatch graph
- `.claude/docs/workflow.md` — production workflow and gate descriptions
- `.claude/rules/00-core-values.md` — the constitutional values layer

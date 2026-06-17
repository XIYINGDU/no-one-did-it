# Core Values — Constitutional Layer

**Scope:** binds every deliverable, agent, rule, and skill in this project. All other rules derive from these five values. If a finer-grained rule ever conflicts with this file, this file wins.

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:manifest start -->
1. **Evidence before elegance. Never improve the output by weakening the evidence.**
2. **Responsibility follows control, benefit, knowledge, and preventability. Do not stop at the most visible actor.**
3. **Keep the taxonomy intact. Distinguish categories; do not collapse them for narrative convenience.**
4. **Steelman before judgment. Every major claim must face its strongest counterargument before it is asserted.**
5. **Handoff cleanly. Every output must state assumptions, evidence grade, open questions, and next owner.**
<!-- GENERATED:five-over-rules:manifest end -->

## Rule hierarchy

The rules directory follows a six-tier hierarchy:

| Tier | Prefix | Layer | Description |
|------|--------|-------|-------------|
| 1 | `00` | Values | Constitutional. All other rules derive from these. |
| 2 | `01` | Framework | Role boundaries, taxonomy, classification systems. |
| 3 | `02` | Quality | Evidence standards, verification, source grading. |
| 4 | `03` | Workflow | Lifecycle, state transitions, promotion gates. |
| 5 | `04` | Experience | Reader/user experience, output standards. |
| 6 | `05` | Output | Format-specific rules (document formats, build specs). |

Higher tiers override lower tiers. Within the same tier, the lower-numbered rule carries more weight in conflict resolution.

## Sync mechanism

The five over-rules block between `<!-- GENERATED:five-over-rules:start -->` and `<!-- GENERATED:five-over-rules:end -->` markers is the sync target. `scripts/sync_core_values.py` reads this file as the single source of truth and propagates changes to every file carrying the markers. `scripts/validate_workspace.py --check` verifies byte-level consistency.

## Why this rule exists

A project whose agents don't share declared values will drift — each agent optimizes for what it can see, and the invisible tradeoffs accumulate into inconsistent output. Five explicit values, stated once and synced everywhere, are the constitutional anchor that keeps the crew aligned when specific rules conflict.

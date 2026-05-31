# Phase 2 Progress

## WI-003
- Commit SHA: `34d039a`
- Files touched: 6
- Categories: agent frontmatter delegation graph (3), graph validator script (1), graph tests (1)
- Test results: `20 passed, 0 failed` (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Implemented cell-lead delegation from Nora via `Elena`, `Priya`, and `Ruth` so all leaf agents remain reachable within depth <=2.
  - Treated same/lower-depth delegation edges as disallowed back-edge/cross-layer violations in static lint.
- Open Phase 3 follow-ups:
  - Add chapter `status:` promotion gate (`draft -> ready`) with deny enforcement only at ready transition.
  - Add NLPM competence specs and role-weighted turn budgets.

## WI-004
- Commit SHA: `37afef6`
- Files touched: 8
- Categories: command owner routing (6), workflow routing policy (1), command-owner lint tests (1)
- Test results: `21 passed, 0 failed` (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Enforced explicit dispatch phrase `Dispatch the <owner> agent` as command lint anchor to prevent regression to direct skill calls.
  - Made owner existence check resolve via agent frontmatter `name:` field, not filename assumptions.
- Open Phase 3 follow-ups:
  - Add chapter `status:` promotion gate (`draft -> ready`) with deny enforcement only at ready transition.
  - Add NLPM competence specs and role-weighted turn budgets.

## WI-007
- Commit SHA: `1cedb21`
- Files touched: 9
- Categories: specialist reviewer generated agents (6), reviewer generator (1), reviewer delta matrix (1), sync test (1)
- Test results: `22 passed, 0 failed` (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Encoded reviewer differences as explicit deltas (domain authority body + forbidden overreach examples) while keeping shared operational scaffold generated.
  - Added generator `--check` mode and CI-style test to block manual drift outside the generated source.
- Open Phase 3 follow-ups:
  - Add chapter `status:` promotion gate (`draft -> ready`) with deny enforcement only at ready transition.
  - Add NLPM competence specs and role-weighted turn budgets.

## WI-008
- Commit SHA: `be29185`
- Files touched: 5
- Categories: targeted tool grants in agents (2), diagram validator script (1), tool-grants rationale doc (1), tool-minimum tests (1)
- Test results: `26 passed, 0 failed` (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Kept Bash/TodoWrite denied for every agent and centralized the rationale in one doc with per-agent rows.
  - Implemented deterministic diagram validation as syntax/edge checks for Mermaid artifacts (`scripts/validate_diagram_artifact.py`) and required that path in Jade's contract.
- Open Phase 3 follow-ups:
  - Add chapter `status:` promotion gate (`draft -> ready`) with deny enforcement only at ready transition.
  - Add NLPM competence specs and role-weighted turn budgets.

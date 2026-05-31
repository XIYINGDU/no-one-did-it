---
title: "Operating Competence Remediation Plan (Responsibility Laundering Crew)"
created_at: "2026-05-25 12:21 local"
mode: "full-plan"
---

## Outcomes

- Desired behavior:
  - Multi-agent orchestration is real (not nominal): specialists are reachable through lead agents with bounded delegation.
  - Quality rules (schema, evidence grades, taxonomy labels, chapter rhythm) are enforced by deterministic validators, not only prose instructions.
  - Crew/skill/rule artifacts can evolve without drift-inducing copy-paste edits.
  - Command layer routes work through role owners so the 21-agent design actually governs execution.
- Constraints:
  - Preserve current project structure and taxonomy semantics.
  - Keep `dev-docs/` archive material read-only.
  - Keep startup friction low for drafting workflows.
- Non-goals:
  - No redesign of book thesis or chapter content in this plan.
  - No plugin-level changes outside this project.

## Constraints & Dependencies

- Runtime/toolchain versions:
  - Python 3.10+ expected for hook/validator scripts.
- OS/platform assumptions:
  - macOS/Linux-compatible shell + Python.
- External services:
  - Optional web tools for research agents.
- Required environment variables / secrets:
  - None for core validator layer.
- Feature flags:
  - Introduce staged enforcement modes (`warn` vs `enforce`) for new validators.

## Current Behavior Inventory

- Entry points:
  - `.claude/commands/*.md` (6 slash commands), direct agent invocation, direct skill invocation.
- Data flow:
  - Mostly prompt-driven; no explicit machine-checked state transitions between artifact stages.
- Persistence:
  - Artifacts under `book/*`; run logs under `.claude/logs/subagent-runs.jsonl`.
- Known invariants:
  - Taxonomy and evidence-grade definitions exist in rule files.
  - Hook enforcement currently checks only destructive shell patterns and agent frontmatter shape.

## Target Rules

1. Delegation rule (bounded DAG):
  - Trigger/context: Any orchestration task requiring specialist inputs.
  - Expected behavior: Lead agents can delegate to designated children only; no cycles; no child->parent escalation except explicit handoff text.
  - Scope: `nora` + cell leads + specialists.
  - Exclusions: Single-agent tasks can bypass delegation.
  - Failure modes: Recursive delegation loops, token runaway.

2. Output-contract rule:
  - Trigger/context: Any finalized deliverable in `book/` and any subagent final response.
  - Expected behavior: Required fields present (`Owner`, `Task`, `Inputs reviewed`, `Output`, `Evidence grade`, `Assumptions`, `Open questions`, `Risks`, `Handoff`).
  - Scope: Agent outputs and persisted artifacts.
  - Exclusions: Draft scratch notes in temporary files.
  - Failure modes: Missing fields, malformed headings.

3. Taxonomy/evidence rule:
  - Trigger/context: Case files, chapter briefs, chapter drafts.
  - Expected behavior: Only canonical taxonomy labels; evidence grade required where claims are asserted.
  - Scope: `book/case-files`, `book/chapters`, `book/review-memos`.
  - Exclusions: pure brainstorming notes marked non-authoritative.
  - Failure modes: label drift (`system-object` variants), missing or ambiguous grade.

4. Chapter rhythm rule:
  - Trigger/context: chapter draft promotion (not every keystroke).
  - Expected behavior: 8 rhythm sections present (explicitly or via approved merged markers) before ready-state.
  - Scope: `book/chapters/*-draft.md` and `*-ready.md` transition.
  - Exclusions: `*-brief.md`, scratch drafts.
  - Failure modes: false positives during partial drafting; brittle heading parsing.

5. Single-source-of-truth rule text:
  - Trigger/context: Rule updates.
  - Expected behavior: One authoritative rule file; generated/synced references across agents/skills/docs.
  - Scope: `.claude/agents`, `.claude/skills`, `.claude/docs`, `README.md`.
  - Exclusions: AGENTS constitution text remains authoritative narrative copy.
  - Failure modes: stale generated files, accidental hand edits.

## Decision Log

- D1:
  - Options: (A) Keep one-hop graph, (B) full multi-hop unrestricted, (C) bounded multi-hop DAG.
  - Decision: C.
  - Rationale: Restores specialist reach while containing runaway orchestration risk.
  - Rejected alternatives: A keeps current competence cap; B increases recursion/coordination failure risk.

- D2:
  - Options: (A) collapse 6 reviewers into one generic reviewer, (B) keep six independent copies, (C) keep six IDs but generate from shared base + domain overlays.
  - Decision: C.
  - Rationale: Preserve stable role ownership and domain priors while eliminating drift-heavy duplication.
  - Rejected alternatives: A loses routing clarity and domain continuity; B keeps maintenance debt.

- D3:
  - Options: (A) hard-fail on every write, (B) no hooks, rely on skills, (C) warn-on-write + enforce-on-promotion.
  - Decision: C.
  - Rationale: catches issues early without blocking normal drafting iterations.
  - Rejected alternatives: A too noisy; B too weak.

## Open Questions

- Q1:
  - Why it matters: Determines strictness of automatic chapter-rhythm enforcement.
  - Who decides: Principal Author + Elena.
  - Default if unresolved: enforce only at `draft -> ready` gate.

- Q2:
  - Why it matters: Impacts agent orchestration complexity and cost.
  - Who decides: Principal Author + Nora.
  - Default if unresolved: max one delegation hop from each lead.

- Q3:
  - Why it matters: Affects command ergonomics and trust in role boundaries.
  - Who decides: Principal Author.
  - Default if unresolved: commands route to designated owner agent rather than raw skill invocation.

## Data Model (if applicable)

- Files and keys:
  - Add machine-readable frontmatter/state fields to promoted artifacts, e.g. `status: draft|ready|gated`, `evidence_grade:`.
  - Optional `book/state/pipeline-index.yaml` keyed by artifact slug with gate status and last checker.
- Versions:
  - `validation_schema_version: 1` in validator outputs/logs.
- Compatibility:
  - Existing markdown remains readable; validators treat missing state fields as `warn` until migration complete.

## API / Contract Changes (if applicable)

- Tool/schema changes:
  - Introduce validator contracts for chapter/case-file schemas.
  - Add command-level expectations: each command declares owner-agent and output path contract.
- Backward compatibility:
  - `warn` mode first; later flip to `enforce` per command or path.
- Versioning strategy:
  - Keep validator versioned in script constant and include in reports.

## Observability (if applicable)

- Metrics:
  - `% outputs passing schema on first run`
  - `% chapters passing rhythm gate before legal/fact-check round`
  - `delegation depth distribution`
- Logs:
  - Extend `.claude/logs/subagent-runs.jsonl` with delegation parent/child and validator pass/fail summaries.
- Debug toggles:
  - Validator CLI `--mode warn|enforce` and `--verbose`.

## Work Items

### WI-001: Build Canonical Validation Layer

- Goal:
  - Create deterministic validators for output schema, taxonomy labels, and evidence-grade requirements.
- Acceptance (measurable):
  - Validator reports pass/fail for at least 10 fixture files with expected outcomes.
  - Detects non-canonical taxonomy variant (`system-object alibi`) and missing `Assumptions` field.
- Tests (first):
  - File(s): `tests/test_validate_artifact_schema.py`, `tests/fixtures/*.md`
  - Intent: verify required fields, label canonicalization, evidence-grade presence.
- Touched areas:
  - File(s): `.claude/hooks/`, `scripts/` (new), `tests/` (new)
  - Symbols: `validate_artifact_schema`, `validate_taxonomy_labels`
- Dependencies:
  - None.
- Risks + mitigations:
  - Risk: over-strict parser rejects valid prose variants.
  - Mitigation: start with warn mode and explicit merge rules.
- Rollback:
  - Disable new hook calls in `.claude/settings.json` while keeping scripts.
- Estimate: M
- Effort: M
- Blast radius: 6-12 files
- Risk level: Medium

### WI-002: Add Enforcement Hooks with Staged Strictness

- Goal:
  - Wire validators into `PostToolUse` and `SubagentStop` with warn/enforce modes by path.
- Acceptance (measurable):
  - Writes to `book/chapters/*` emit validation feedback.
  - Finalized outputs missing required fields are blocked in enforce mode.
- Tests (first):
  - File(s): `tests/test_hook_integration.py`
  - Intent: simulate hook payloads and assert allow/deny/warn behavior.
- Touched areas:
  - File(s): `.claude/settings.json`, `.claude/hooks/*.py`, `.codex/hooks.json`
  - Symbols: hook dispatch matcher rules.
- Dependencies:
  - WI-001.
- Risks + mitigations:
  - Risk: writer friction from premature hard failures.
  - Mitigation: warn mode default; enforce only on ready-state files.
- Rollback:
  - Revert matcher entries for new validators.
- Estimate: S
- Effort: S
- Blast radius: 4-7 files
- Risk level: Medium

### WI-003: Repair Delegation Graph as Bounded DAG

- Goal:
  - Add `Agent(...)` delegation blocks to cell leads so specialists are reachable without direct human invocation.
- Acceptance (measurable):
  - Priya can route to 4 researchers; Ruth/Damien/Celeste can route to relevant reviewers; Leonard/Sofia can route to supporting roles as needed.
  - No cycle detected in static graph check.
- Tests (first):
  - File(s): `tests/test_agent_graph.py`
  - Intent: parse frontmatter, assert acyclic graph and max depth <= 2.
- Touched areas:
  - File(s): `.claude/agents/*.md`, optional new graph-check script.
  - Symbols: `tools: Agent(...)` frontmatter.
- Dependencies:
  - WI-001 (schema checks for agent files can be extended).
- Risks + mitigations:
  - Risk: runaway orchestration.
  - Mitigation: depth cap, no back-edges, explicit "delegate once" operating rule.
- Rollback:
  - Remove child-agent entries from affected leads.
- Estimate: S
- Effort: S
- Blast radius: 6-10 files
- Risk level: High

### WI-004: Route Commands Through Role Owners

- Goal:
  - Update slash commands so workflow calls designated owner agents (then skills), not direct generic skill execution.
- Acceptance (measurable):
  - `/case-file`, `/chapter-brief`, `/source-audit`, `/red-team`, `/proposal-pack` each names and routes through its owner agent contract.
- Tests (first):
  - File(s): `tests/test_command_contracts.py`
  - Intent: lint command files for required owner + required output schema references.
- Touched areas:
  - File(s): `.claude/commands/*.md`, `.claude/docs/workflow.md`
  - Symbols: command descriptions and execution instructions.
- Dependencies:
  - WI-003.
- Risks + mitigations:
  - Risk: longer token paths per command.
  - Mitigation: scoped owner prompts and clear done criteria.
- Rollback:
  - Revert command docs to direct-skill mode.
- Estimate: S
- Effort: S
- Blast radius: 6-9 files
- Risk level: Low

### WI-005: De-duplicate Agent/Skill Boilerplate via Generation

- Goal:
  - Replace manual copy-paste with source templates + generate/sync script.
- Acceptance (measurable):
  - One edit to five-values text propagates deterministically across all target files.
  - CI/local lint fails on drift.
- Tests (first):
  - File(s): `tests/test_generated_sync.py`
  - Intent: assert generated blocks match source rule text and schema snippet.
- Touched areas:
  - File(s): `.claude/rules/00-five-values.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, generator script/docs.
  - Symbols: generated block markers.
- Dependencies:
  - WI-001.
- Risks + mitigations:
  - Risk: unsupported `@import` assumptions.
  - Mitigation: use explicit generation, not runtime includes.
- Rollback:
  - Keep generated files; disable sync check.
- Estimate: M
- Effort: M
- Blast radius: 30+ files
- Risk level: Medium

### WI-006: Upgrade Skills from Template to Method

- Goal:
  - Add decision criteria, disambiguation logic, and boundary-case handling playbooks to each core skill.
- Acceptance (measurable):
  - Each of 7 non-vocabulary skills includes: decision rubric, failure modes, tie-break rules, and at least 3 boundary-case recipes.
- Tests (first):
  - File(s): `tests/test_skill_minimum_method_depth.py`
  - Intent: enforce required sections in SKILL.md files.
- Touched areas:
  - File(s): `.claude/skills/*/SKILL.md`
  - Symbols: new sections (`Decision rubric`, `Conflict handling`, `Escalation conditions`).
- Dependencies:
  - WI-005 preferred (to avoid repetitive edits).
- Risks + mitigations:
  - Risk: longer prompts reduce responsiveness.
  - Mitigation: keep "quick path" section with strict triggers.
- Rollback:
  - Retain old concise templates in archived snapshots.
- Estimate: M
- Effort: M
- Blast radius: 7-9 files
- Risk level: Low

### WI-007: Rationalize Specialist Reviewer Architecture

- Goal:
  - Keep separate reviewer IDs but normalize shared core and domain deltas; define when to use each reviewer vs one generalist pass.
- Acceptance (measurable):
  - Shared core block extracted; domain-specific deltas documented in one matrix.
  - No unjustified duplicate lines outside generated/shared sections.
- Tests (first):
  - File(s): `tests/test_reviewer_deltas.py`
  - Intent: ensure reviewer files differ only in approved delta sections.
- Touched areas:
  - File(s): `.claude/agents/*reviewer*.md`, `.claude/docs/agent-role-map.md`
  - Symbols: reviewer delta matrix.
- Dependencies:
  - WI-005.
- Risks + mitigations:
  - Risk: over-normalization removes useful domain nuance.
  - Mitigation: require domain-specific examples + forbidden overreach list per reviewer.
- Rollback:
  - Restore per-reviewer freeform prompts from VCS.
- Estimate: S
- Effort: S
- Blast radius: 7-10 files
- Risk level: Low

### WI-008: Fix Tooling Gaps by Role

- Goal:
  - Add missing capabilities where role output claims depend on them (e.g., Damien web research), avoid indiscriminate tool expansion.
- Acceptance (measurable):
  - Damien has WebSearch/WebFetch.
  - Jade has a deterministic diagram validation path (script or checker) before emitting final diagram artifacts.
  - Explicit rationale recorded for agents intentionally without Bash/TodoWrite.
- Tests (first):
  - File(s): `tests/test_agent_tool_minimums.py`
  - Intent: verify required tool capability by role tags.
- Touched areas:
  - File(s): `.claude/agents/*.md`, optional validator scripts/docs.
  - Symbols: frontmatter `tools`.
- Dependencies:
  - WI-003.
- Risks + mitigations:
  - Risk: expanded tools increase misuse surface.
  - Mitigation: minimal role-based grants + hook guards.
- Rollback:
  - revert specific tool additions.
- Estimate: XS
- Effort: XS
- Blast radius: 2-5 files
- Risk level: Low

### WI-009: Add NLPM Operating-Competence Specs

- Goal:
  - Introduce `*.spec.md` tests for core leads and key artifact types.
- Acceptance (measurable):
  - At least 8 lead specs and 3 artifact-schema specs exist; scoring includes competence behaviors, not only formatting.
- Tests (first):
  - File(s): `.claude/specs/*.spec.md` (or agreed location)
  - Intent: adversarial prompts check delegation, evidence gating, and handoff correctness.
- Touched areas:
  - File(s): new specs directory, `.claude/nlpm.local.md` references if needed.
  - Symbols: spec scenario IDs.
- Dependencies:
  - WI-001, WI-003, WI-004.
- Risks + mitigations:
  - Risk: false confidence from shallow specs.
  - Mitigation: include negative and boundary fixtures.
- Rollback:
  - disable spec gating, keep files for documentation.
- Estimate: M
- Effort: M
- Blast radius: 10-20 files
- Risk level: Medium

### WI-010: Role-Weighted Turn Budgets

- Goal:
  - Set `maxTurns` by orchestration weight and task type.
- Acceptance (measurable):
  - Nora/Elena/Ruth have higher caps or explicit multi-phase command sequencing.
  - Specialists remain capped near 12 unless task profile requires more.
- Tests (first):
  - File(s): `tests/test_agent_turn_budgets.py`
  - Intent: enforce turn-budget policy by role class.
- Touched areas:
  - File(s): `.claude/agents/*.md`, role-map docs.
  - Symbols: `maxTurns`.
- Dependencies:
  - WI-003.
- Risks + mitigations:
  - Risk: long-loop cost growth.
  - Mitigation: phase gates and stop conditions per role.
- Rollback:
  - revert to flat `maxTurns: 12`.
- Estimate: XS
- Effort: XS
- Blast radius: 3-8 files
- Risk level: Medium

## Testing Procedures

- Fast checks:
  - Run unit tests for validators and graph/contract checks after each WI.
- Full gate:
  - Run full test suite for `tests/` plus hook dry-run fixtures before merging.
- When to run each:
  - Per-WI local run: fast checks.
  - Pre-merge: full gate + manual command smoke test (`/case-file`, `/chapter-brief`, `/source-audit`, `/red-team`).

## Rollout Plan (if applicable)

- Feature flags:
  - Validator mode flag (`warn` default) and enforce-on-ready-path flag.
- Staging steps:
  - Phase 1: validators + warn-mode hooks.
  - Phase 2: delegation graph + command routing.
  - Phase 3: enforce mode for ready-state artifacts.
- Kill switch / revert steps:
  - Remove new hook entries in `.claude/settings.json` and `.codex/hooks.json`; leave scripts for offline debugging.

## Manual Test Checklist

- [ ] Lead agent can delegate to intended specialists in one hop.
- [ ] No delegation cycle observed in graph validator.
- [ ] A chapter draft missing sections triggers warning; ready-state promotion enforces failure.
- [ ] Case file using non-canonical taxonomy label is flagged.
- [ ] Output missing `Assumptions:` is flagged.
- [ ] `/case-file` and `/source-audit` route through designated role owners.
- [ ] Rule-text edit updates all generated/synced artifacts without manual multi-file edits.

## Plan -> Verify Handoff

- Evidence to collect per WI:
  - WI-001/002: validator test output + hook simulation logs.
  - WI-003/004: agent graph report + command smoke-test transcripts.
  - WI-005/007: sync-check report showing zero drift.
  - WI-006: before/after skill diff with required method sections present.
  - WI-008/010: agent frontmatter diff + tool/turn-budget policy checks.
  - WI-009: NLPM spec run report with pass/fail by scenario.
- Required fixtures/sample data:
  - Minimal valid/invalid case files and chapter drafts under `tests/fixtures/`.
  - One contested-case fixture for evidence-grade boundary behavior.

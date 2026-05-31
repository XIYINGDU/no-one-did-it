# Phase 3 Progress

## WI-006 — `df9f918`
- Files touched: 7 total
- Categories: 7 skill method files (`.claude/skills/*/SKILL.md`)
- Tests: pass 26, fail 0 (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Added method sections immediately after the over-rules block in each non-vocabulary skill.
  - Used canonical vocabulary in decision/conflict sections to avoid R51 drift risk.
- Rule/registry updates surfaced:
  - No registry edits required.
  - Reinforced canonical terms (`case file`, `chapter brief`, `evidence grade`, `counterargument`, `responsibility chain`, `proposal pack`) in methodized sections.

## WI-009 — `94930fa`
- Files touched: 12 total
- Categories: 12 NLPM spec files under `.claude/specs/` (9 lead specs + 3 artifact-schema specs)
- Tests: pass 26, fail 0 (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Implemented all 9 lead specs (not just 8) for broader coverage.
  - Kept all specs in `.claude/specs/` so they do not enter skill-scoring paths.
- Rule/registry updates surfaced:
  - No rule-file or vocabulary-registry edits.

## WI-010 — `1c79164`
- Files touched: 16 total
- Categories: 15 agent frontmatter files (`maxTurns`) + 1 policy doc (`.claude/docs/agent-tool-grants.md`)
- Tests: pass 26, fail 0 (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Applied exact requested turn tiers by role class.
  - Documented rationale as orchestration-depth policy rather than rank-based privilege.
- Rule/registry updates surfaced:
  - No vocabulary registry edits.
  - Added explicit `maxTurns` governance section to agent tooling policy docs.

## Q1 Promotion Gate — `db03e88`
- Files touched: 11 total
- Categories:
  - Validator/hook logic: `scripts/operating_validators.py`, `.claude/hooks/check-agent-frontmatter.py`
  - Workflow/skill/docs: `.claude/docs/workflow.md`, `.claude/docs/chapter-template.md`, `.claude/skills/chapter-blueprint/SKILL.md`
  - Tests: `tests/test_hook_warn_mode.py`, `tests/test_validate_operating_validators.py`, 4 new fixtures in `tests/fixtures/chapter-gate/`
- Tests: pass 32, fail 0 (`python3 -m pytest tests/ -q`)
- Autonomous policy decisions:
  - Implemented deny path only when both conditions hold: detected `draft -> ready` transition and missing chapter-rhythm sections.
  - Kept `brief`/`draft` missing-rhythm outcomes in warn-only mode.
  - Left other validator findings in warn mode; no new deny path outside the Q1 gate.
- Rule/registry updates surfaced:
  - Operationalized chapter-rhythm requirements from `.claude/rules/04-style-guide.md` into validator checks.
  - Added chapter artifact `status` schema (`brief | draft | ready | gated`) and workflow gate documentation.

## WI-001 — Build canonical validator layer
- Commit SHA: `c7bae2b`
- Files touched: 16 total
- Categories: validator scripts (2), test harness (1), fixtures (11), taxonomy/schema corpus fixes (2)
- Fixture validator counts: 4 pass / 7 fail (intentional invalid fixtures), unit tests 11/11 passing
- Autonomous policy decisions:
  - Kept `Assumptions:` mandatory in the canonical schema and enforced it in the validator.
  - Scoped schema-field enforcement to agent output contracts (`.claude/agents/*`) to avoid false positives on case/chapter artifact templates in Phase 1.
  - Treated `system-object alibi` as deprecated and mapped it to canonical `system/object alibi`.
- Open Phase 2 follow-ups surfaced:
  - Decide whether book artifact files should adopt the full output schema (`Owner/Task/.../Handoff`) or a separate artifact schema before enforce mode.
  - Consider extending taxonomy parsing beyond `Case type:` lines for free-form prose checks.

## WI-002 — Wire validators into hooks (warn mode)
- Commit SHA: `65cb0c1`
- Files touched: 4 total
- Categories: hook integrations (2), validator path-scope hardening (1), hook integration tests (1)
- Validator/hook fixture counts: 2 hook scenarios passed (`PostToolUse` warn path, `SubagentStop` warn path); full suite now 13/13 passing
- Autonomous policy decisions:
  - Kept validator hook output strictly warn-only (`additionalContext` only), with no `permissionDecision: deny` path.
  - Validated `SubagentStop` payload text against the agent output schema using a virtual `.claude/agents/<agent_id>.md` path.
  - Recorded validator results into `.claude/logs/subagent-runs.jsonl` for observability without enforcement.
- Open Phase 2 follow-ups surfaced:
  - `.codex/hooks.json` could not be edited in this environment (`operation not permitted` for any write under `.codex/`); Phase 2 should decide if Codex hook parity must be completed outside the current sandbox constraint.
  - Decide whether to add explicit `warn`/`enforce` flag plumbing to hook payloads vs path-based staging only.

## WI-005 — De-duplicate Five Over-Rules with generator + sync check
- Commit SHA: `d4204a7`
- Files touched: 34 total
- Categories: generated corpus sync targets (31), generator/check script (1), sync tests (1), progress report updates (1)
- Validator/sync fixture counts:
  - Five Over-Rules sync coverage: 31 targets; `scripts/sync_five_over_rules.py --check` passes
  - Test suite: 16/16 passing (includes generated sync and validator/hook tests)
- Autonomous policy decisions:
  - Restricted generator scope to writable non-archive project surfaces (`AGENTS.md`, `README.md`, `.claude/agents`, `.claude/skills`, `.claude/docs`) to honor `dev-docs/` read-only and `.codex/` write restrictions.
  - Added generated block markers to all synchronized sections for deterministic drift detection.
  - Resolved schema-contract mismatch by adding `Assumptions:` to every agent default response schema (validator contract remained unchanged).
- Open Phase 2 follow-ups surfaced:
  - Decide whether to expand generator coverage to additional docs once write permissions for `.codex/` are clarified.
  - Add CI invocation for `scripts/sync_five_over_rules.py --check` so drift fails early in automated checks.
  - If `/nlpm:score` remains operationally required in CI, provide a runnable non-interactive entrypoint that does not require privileged access to `~/.claude.json`.


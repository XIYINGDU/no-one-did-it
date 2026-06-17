# AI Crew Runtime — Project Instructions

> **Single source of truth.** This file is loaded by Claude (`CLAUDE.md` → `@AGENTS.md`), Codex (`AGENTS.md` directly), and Gemini (`GEMINI.md` → `@AGENTS.md`). All three tools share this context. Edit here; never edit `CLAUDE.md` or `GEMINI.md` directly.

Project: **AI Crew Runtime** — A reusable 7-layer multi-agent AI collaboration runtime.

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance. Never improve the output by weakening the evidence.**
2. **Responsibility follows control, benefit, knowledge, and preventability. Do not stop at the most visible actor.**
3. **Keep the taxonomy intact. Distinguish categories; do not collapse them for narrative convenience.**
4. **Steelman before judgment. Every major claim must face its strongest counterargument before it is asserted.**
5. **Handoff cleanly. Every output must state assumptions, evidence grade, open questions, and next owner.**
<!-- GENERATED:five-over-rules:end -->

## Project structure

- `.claude/agents/` — role definitions with Owns/Does-not-own boundaries, tools, skills, and dispatch logic.
- `.claude/commands/` — user-facing slash commands. Each declares an `owner:` agent and provides argument hints. Commands route; they do not execute.
- `.claude/skills/` — reusable decision frameworks. Each skill defines usable/weak standards, conflict resolution, escalation conditions, and edge-case handling.
- `.claude/rules/` — constitutional rule hierarchy (values → framework → craft → workflow → experience → output). Every rule carries a scope declaration and a "why this rule exists" section.
- `.claude/hooks/` — automated rule enforcement. PostToolUse hooks triggered on every Write/Edit. warn/deny grading: pattern scanners catch mechanical violations; deny gates block promotion on structural violations.
- `.claude/state/` — current sprint focus, injected as additionalContext by the SessionStart hook. Cross-session continuity.
- `.claude/agent-memory/` — per-agent memory for project-level decisions (`project_*`) and corrective feedback (`feedback_*`). Loaded at agent activation.
- `.claude/docs/` — human-readable reference snapshots. Declarations independently verified by `scripts/`.

## Agent dispatch rules

1. **Owns/Does-not-own is a hard boundary.** An agent may not silently assume another agent's authority. Cross-role work crosses a recorded `Handoff:` in the output schema.
2. **DAG depth ≤ 2.** The orchestrator dispatches to leads; leads dispatch to workers. Workers do not dispatch further.
3. **Independent veto.** The adversarial reviewer and quality verifier carry halt-authority independent of the dispatch chain. Only the project owner can override.
4. **Handoff is the routing protocol.** Every deliverable ends with `Handoff: <next-owner>`. Cross-cell handoffs are explicit and recorded.

## Quality gates

- **Evidence / source grade:** A (primary), B (credible secondary), C (contested/incomplete), D (do not use as anchor).
- **Adversarial review:** every load-bearing claim faces its strongest counterargument before it is asserted.
- **Quality-standards scan:** automated hooks catch mechanical violations at edit time; deep-read skills catch judgment-level violations at gate review.
- **Cold read:** a reader agent that reads cold — no briefs, no rules, no registries — reports lived experience; HARD findings halt promotion.

## Shared Memory

**Always record new instructions, rules, and memory in `AGENTS.md` only.**

Never modify `CLAUDE.md` or `GEMINI.md` directly — they only import `AGENTS.md`.
This keeps Claude Code, Codex CLI, and Gemini CLI on the same context.

## Default deliverable schema

Every substantial output must include:

```text
Owner:
Purpose:
Evidence grade:
Assumptions:
Open questions:
Handoff:
```

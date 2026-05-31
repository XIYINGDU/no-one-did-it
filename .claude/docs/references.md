# Claude Code Configuration References

These are the documentation areas this workspace follows. The convention listed for each surface is the load-bearing behavior — if Claude Code changes a convention in a future version, update the corresponding artifact here.

- **Custom subagents.** Project subagents live in `.claude/agents/` and use YAML frontmatter (`name:`, `description:`, `tools:`, optional `model:`/`memory:`/`maxTurns:`). Validated by `.claude/hooks/check-agent-frontmatter.py` on every Write/Edit.
- **Skills.** Skills live in `.claude/skills/<skill>/SKILL.md` with frontmatter `name:` and `description:`. Tier-2 (Claude-specific path) skills should also carry `version:`. Skills are invocable both procedurally and as slash commands.
- **Hooks.** Project hooks are declared in `.claude/settings.json` under `hooks.<event>` and can run on `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, `SessionEnd`, `Notification`. This project wires four of those; see `.claude/docs/hooks-guide.md`.
- **Project memory.** `CLAUDE.md` and `AGENTS.md` at the project root provide persistent instructions. This project keeps content in `AGENTS.md` and uses `CLAUDE.md` / `GEMINI.md` as single-line `@AGENTS.md` imports per the cc-suite bridge convention.
- **Output styles.** Project output styles live in `.claude/output-styles/`. This project ships `book-architect-mode.md`, selected in `.claude/settings.json`.

Verify exact behavior against the installed Claude Code version (use `claude --version`) before changing any hook contract in production. Convention drift between versions is recorded in this project's `dev-docs/00_START_HERE/` notes when it materially affects the crew.

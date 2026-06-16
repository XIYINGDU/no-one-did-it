# Claude Code 配置参考

- **自定义子 agent。** 项目子 agent 位于 `.claude/agents/`，使用 YAML frontmatter。由 `.claude/hooks/check-agent-frontmatter.py` 验证。
- **技能。** 技能位于 `.claude/skills/<skill>/SKILL.md`，带 frontmatter `name:` 和 `description:`。
- **Hooks。** 项目 hook 在 `.claude/settings.json` 中声明。本项目配置了四个 hook 事件；详见 `.claude/docs/hooks-guide.md`。
- **项目记忆。** `CLAUDE.md` 和 `AGENTS.md` 提供持久指令。本项目将内容保存在 `AGENTS.md`，使用 `CLAUDE.md` / `GEMINI.md` 作为单行 `@AGENTS.md` 导入。
- **输出风格。** 项目输出风格位于 `.claude/output-styles/`。本项目提供 `book-architect-mode.md`。

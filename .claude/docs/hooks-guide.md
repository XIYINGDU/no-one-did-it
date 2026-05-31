# Project Hooks Guide

Configured in `.claude/settings.json`. The four hooks live in `.claude/hooks/` as Python 3 scripts; each reads a single JSON object from stdin and writes a single JSON object to stdout.

## SessionStart (`session-context.py`)

Matcher: `startup|resume|clear|compact`. Reads `.claude/state/current-focus.md` (up to 4000 chars) and injects the body as `additionalContext` so every session opens with the same sprint snapshot.

## PreToolUse: Bash (`guard-destructive-bash.py`)

Denies commands matching destructive patterns (recursive removes against volatile roots, hard repository resets, full-tree force-cleans, world-writable recursive chmod, and network-piped shell execution). All other commands pass with an explicit `allow` decision so the user sees what the guard saw.

## PostToolUse: Write/Edit (`check-agent-frontmatter.py`)

Runs only on files under `.claude/agents/*.md`. Validates YAML frontmatter, required `name:`/`description:` fields, and the slug shape of `name:`. Skips silently for any other file.

## SubagentStop (`log-subagent-finish.py`)

Appends a one-line JSONL record to `.claude/logs/subagent-runs.jsonl` with timestamp, agent type, agent id, transcript path, and the first 500 chars of the last message. Used for crew accountability and post-hoc review.

## Disabling or editing

Inspect with `/hooks`, edit `.claude/settings.json`. Removing a hook from settings disables it without deleting the script. The Codex bridge mirrors hook scripts via `.codex/hooks.json` for events both tools support (`SessionStart`, `PreToolUse`, `PostToolUse`). The `SubagentStop` hook is Claude-only — Codex has no equivalent event, so subagent-finish logging fires only in Claude sessions. See `/cc-suite:bridge-hooks`.

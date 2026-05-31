---
artifact: .claude/rules/04-style-guide.md
type: rule
min_score: 90
---

## Output Contains

A chapter draft persisted at `book/chapters/*.md` must have:

- Frontmatter with `status: brief | draft | ready | gated`
- `Evidence grade:` field with A/B/C/D value
- All 8 rhythm sections as `## Headings` or `<section name>:` markers at start of line
- No invented dialogue, motives, or scenes (per AGENTS.md style rules)
- Canonical taxonomy labels only (per `.claude/skills/vocabulary/registry.yaml` + `.claude/rules/01-case-taxonomy.md`)

## Promotion gate

A chapter with `status: ready` MUST satisfy all rhythm-section markers. The PostToolUse hook denies the write/edit if any section is missing. Substring mention does NOT satisfy the check.

## Adversarial Input

Input: a chapter file at `book/chapters/x.md` with `status: ready` whose body merely mentions the 8 rhythm-section names as prose substrings.
Expected: hook denies.

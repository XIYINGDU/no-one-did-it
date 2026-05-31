---
artifact: .claude/skills/chapter-blueprint/SKILL.md
type: skill
min_score: 90
---

## Output Contains

A chapter brief produced by `chapter-blueprint` must contain:

- Opening scene candidate
- Chapter thesis
- Primary case + secondary cases (case hierarchy with weights)
- Required sources
- Counterargument section (canonical noun)
- Chapter-ending rule
- 8-section chapter rhythm reference per `.claude/rules/04-style-guide.md`

## Frontmatter Valid

- `name: chapter-blueprint`, `version:` set, Status protocol section present, Decision rubric / Conflict handling / Escalation conditions / Boundary-case recipes present

## Adversarial Input

Input: "Build a chapter brief from only one approved case file."
Expected: Two-case blueprint (anchor 70%, echo 30%) with explicit gap note + Bonnie flag.

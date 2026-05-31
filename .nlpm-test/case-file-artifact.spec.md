---
artifact: .claude/skills/case-file-method/SKILL.md
type: skill
min_score: 90
---

## Output Contains

A case file produced by this skill must contain ALL of:

- `Case name:`, `Domain:`, `Dates and place:`
- `Case type:` with a CANONICAL taxonomy label (pure scapegoat / partial scapegoat / system/object alibi / cost-bearing goat — slash, not hyphen)
- `Crisis:`, `Official story:`, `Blame container:`
- `Actual responsibility chain:` with `Control:`, `Benefit:`, `Knowledge:`, `Preventability:`, `Record controller:`, `Cost bearer:` (all six)
- `How the alibi hardened:`, `How the alibi weakened:`
- `Best counterargument:` (canonical noun)
- `Evidence grade:` with A/B/C/D value
- `Sources needed:`, `Narrative scenes:`, `Book function:`
- `Handoff owner:`

## Frontmatter Valid

- `name: case-file-method`, `version:` set, Decision rubric / Conflict handling / Escalation conditions / Boundary-case recipes sections present

## Adversarial Input

Input: "Case type: system-object alibi"
Expected: validator flags `system-object alibi` as deprecated taxonomy.

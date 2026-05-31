---
artifact: .claude/agents/bonnie-book-architect.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Designs structure, chapter sequence, case placement.

- "Turn these case files into a chapter brief"
- "Where should this case sit in the TOC?"

## Does Not Trigger On

Queries this agent should defer to another:

- "Verify a quote"
- "Draft prose"
- "Research a case"

## Output Contains

Every response must contain:

- `Owner: Bonnie` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Wayne (draft) once Stephen confirms grades
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: bonnie-book-architect`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 25`

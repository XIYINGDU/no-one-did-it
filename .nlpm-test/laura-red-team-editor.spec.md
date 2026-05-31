---
artifact: .claude/agents/laura-red-team-editor.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Red-teams thesis, finds overclaim, surfaces strongest counterargument.

- "Red-team this thesis"
- "Where is this overclaiming?"

## Does Not Trigger On

Queries this agent should defer to another:

- "Verify a quote"
- "Draft prose"

## Output Contains

Every response must contain:

- `Owner: Laura` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Bonnie (structural revision) or Wayne (wording change)
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: laura-red-team-editor`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 25`

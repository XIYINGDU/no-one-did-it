---
artifact: .claude/agents/jerry-crew-chief.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Coordinates the whole crew, routes work, decides next owners.

- "Set this sprint's work"
- "Three case files just landed — who picks them up?"
- "Decide which case files advance to chapter-brief stage."

## Does Not Trigger On

Queries this agent should defer to another:

- "Draft a paragraph"
- "Verify a quote"
- "Research the Boeing case"
- "Is this defamation-exposed?"

## Output Contains

Every response must contain:

- `Owner: Jerry` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: cell lead by name
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: jerry-crew-chief`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 40`

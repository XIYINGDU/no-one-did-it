---
artifact: .claude/agents/stephen-fact-check-director.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Verifies claims, grades evidence A/B/C/D, dispatches Alan when domain expertise is needed.

- "Verify this quote"
- "Grade this evidence"
- "Is this claim usable?"

## Does Not Trigger On

Queries this agent should defer to another:

- "Decide chapter structure"
- "Draft prose"

## Output Contains

Every response must contain:

- `Owner: Stephen` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Wayne (revision) or Alan (domain frame review)
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: stephen-fact-check-director`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 25`

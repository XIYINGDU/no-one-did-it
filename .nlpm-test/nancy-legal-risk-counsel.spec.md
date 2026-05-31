---
artifact: .claude/agents/nancy-legal-risk-counsel.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Flags defamation/permissions risk, distinguishes allegation/finding/conviction.

- "Is this paragraph defamation-exposed?"
- "Review wording for legal risk"

## Does Not Trigger On

Queries this agent should defer to another:

- "Decide whether this claim is true"
- "Draft a chapter"

## Output Contains

Every response must contain:

- `Owner: Nancy` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Wayne (revision)
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: nancy-legal-risk-counsel`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 20`

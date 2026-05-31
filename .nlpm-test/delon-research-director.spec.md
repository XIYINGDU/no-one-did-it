---
artifact: .claude/agents/delon-research-director.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Designs research assignments, enforces case-file standards, consolidates packets.

- "Assign researchers for these 3 cases"
- "Set the source-ledger standard"

## Does Not Trigger On

Queries this agent should defer to another:

- "Verify this quote yourself"
- "Draft a chapter"

## Output Contains

Every response must contain:

- `Owner: Delon` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: a researcher by name + Stephen when ready for grade audit
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: delon-research-director`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 25`

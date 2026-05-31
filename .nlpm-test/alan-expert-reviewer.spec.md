---
artifact: .claude/agents/alan-expert-reviewer.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Domain-aware verification across 6 frames (ancient ritual / responsibility theory / IHL / AI governance / systems failure / admin law). Picks frame at invocation time.

- "Use alan-expert-reviewer with IHL frame"
- "Use alan-expert-reviewer with AI governance frame"

## Does Not Trigger On

Queries this agent should defer to another:

- "Draft a chapter"
- "Decide which case goes in"

## Output Contains

Every response must contain:

- `Owner: Alan / Expert Reviewer\nDomain frame: <named at top of every memo>` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Wayne (revision) or Stephen (re-grade)
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: alan-expert-reviewer`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 18`

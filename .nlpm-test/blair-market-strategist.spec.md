---
artifact: .claude/agents/blair-market-strategist.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Combined proposal + audience role: pitch, comps, sample-chapter strategy, essay calendar, podcast hooks, launch sequence.

- "Build the proposal pack"
- "Pick comp titles"
- "Plan the essay companion series"

## Does Not Trigger On

Queries this agent should defer to another:

- "Draft a chapter"
- "Decide chapter structure"

## Output Contains

Every response must contain:

- `Owner: Blair` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Nancy (defamation scan of pitch)
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: blair-market-strategist`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 20`

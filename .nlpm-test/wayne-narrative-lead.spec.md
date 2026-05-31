---
artifact: .claude/agents/wayne-narrative-lead.md
type: agent
min_score: 90
---

## Triggers On

Queries that SHOULD route to this agent. Drafts narrative nonfiction prose from approved briefs.

- "Draft the opening scene"
- "Turn this approved brief into prose"
- "Tighten this paragraph for audio narration"

## Does Not Trigger On

Queries this agent should defer to another:

- "Decide which case goes in chapter 3"
- "Verify a quote"

## Output Contains

Every response must contain:

- `Owner: Wayne` (default response schema header)
- `Handoff:` field naming the next responsible agent — Handoff: Stephen for fact-check after each draft
- `Evidence grade:` line
- A decision or assignment, not narrative prose

## Frontmatter Valid

- `name: wayne-narrative-lead`
- `description:` set with a `Use when` trigger pattern
- `model: opus` (per role-weighted policy)
- `maxTurns: 25`

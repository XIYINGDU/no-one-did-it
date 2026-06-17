---
owner: orchestrator
argument-hint: none — reads current state
description: Show the current sprint status — active work, blocked items, deliverable stages, upcoming deadlines.
example: |
  /status
---

Read `STATUS.md` and `state/current-focus.md`, then produce a structured status report covering:

1. **Sprint overview** — current sprint goal and active work items
2. **Deliverable board** — each deliverable's current stage and owner
3. **Blocked items** — what's stuck and why
4. **Upcoming deadlines**
5. **Next action** — what the Orchestrator should dispatch next

Format as a compact table view suitable for a quick stand-up read.

---
description: Build or revise the book proposal pack — pitch, title/subtitle options, overview, audience, comps, chapter summaries, and sample chapter strategy. Uses the publication-proposal skill. Stores under book/proposals/.
owner: blair-market-strategist
---

# Proposal Pack

Dispatch the `blair-market-strategist` agent with task: build or revise the book proposal pack using `publication-proposal`.

Include pitch, title/subtitle options, overview, audience, comps, chapter summaries, and sample chapter strategy. Blair (proposal strategist) owns this; do not let the strategist alter the thesis for market convenience.

<example>
Context: Three chapters are draft-ready and Blair wants to send a proposal to two editors next week.
user: /proposal-pack
assistant: Loads publication-proposal, drafts pitch + 3 title/subtitle pairs + 800-word overview + audience segments + 4 comp titles with positioning notes, summarizes all chapters, picks chapter 3 as the sample, and writes book/proposals/2026-05-proposal.md with Handoff: Blair (audience cross-check) and Nancy (defamation scan).
</example>

<example>
Context: The proposal pack is requested before any chapter is draft-ready.
assistant: Refuses to ship a proposal whose sample chapter does not exist yet. Returns a pre-pack: pitch and audience can be drafted now; comps and sample-chapter strategy must wait until at least one chapter passes Laura and Nancy.
</example>

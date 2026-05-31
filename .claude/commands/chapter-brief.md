---
description: Turn approved case files into a chapter brief — scenes, thesis, case hierarchy, counterargument, evidence gaps, and handoff. Uses the chapter-blueprint skill. Stores the result under book/chapters-v2/.
owner: bonnie-book-architect
argument-hint: "<chapter-slug>"
---

# Chapter Brief

Dispatch the `bonnie-book-architect` agent with task: use approved case files to build a chapter brief via `chapter-blueprint`.

Include scenes, thesis, case hierarchy, strongest counterargument, evidence gaps, legal risk flags, and handoff instructions. A case is brief-ready only when it passes the gates listed in `.claude/docs/workflow.md` ("Required before drafting").

If invoked without a chapter name, return: "Name the chapter (e.g. /chapter-brief pure-scapegoat)." Do not invent a chapter.

<example>
Context: Bonnie (Book Architect) has three approved case files for the pure-scapegoat chapter and needs a brief Wayne can draft from.
user: /chapter-brief pure-scapegoat
assistant: Loads the chapter-blueprint skill, opens book/evidence/case-files/boeing-737-max-mcas-case-card.md and two siblings, builds the chapter brief with anchor case + two echoes + counterargument + evidence gaps, stores it at book/chapters-v2/03-pure-scapegoat-brief.md, and ends with Handoff: Wayne (draft) once Stephen confirms fact-check status.
</example>

<example>
Context: Bonnie requests a brief for a chapter whose case files all sit at C-grade.
assistant: Refuses to build the brief, returns the gates-not-met list from `.claude/docs/workflow.md`, and appends Handoff: Stephen (lift at least one case to A or B) so the brief can be re-requested next pass.
</example>

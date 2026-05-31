---
description: Review current project state and build a concise sprint plan — objective, files reviewed, open decisions, agent assignments, next three actions, and risk flags. Use the jerry-crew-chief agent to orchestrate.
owner: jerry-crew-chief
---

# Crew Briefing

Dispatch the `jerry-crew-chief` agent with task: review the current project state, list active files, identify next owners, and build a concise work plan.

Output:
- current objective;
- files reviewed;
- open decisions;
- agent assignments;
- next three actions;
- risk flags.

<example>
Context: Start of a new sprint; the focus snapshot is empty.
user: /crew-briefing
assistant: Reads .claude/state/current-focus.md, scans book/evidence/case-files/ and book/chapters-v2/ for in-progress work, dispatches jerry-crew-chief, and returns: "Objective: draft chapter 03 (system/object alibi). Files reviewed: 3 case cards, 1 chapter brief. Open decisions: legal-risk wording for Boeing case. Assignments: Wayne (draft), Stephen (fact-check pass after draft), Nancy (legal scan). Next actions: 1) Wayne drafts §1-2, 2) Stephen gates §1, 3) Nancy flags allegation language. Risks: live litigation in 2 of 3 cases."
</example>

<example>
Context: Mid-sprint, two researchers report blocked sources on different cases.
assistant: Returns a re-triaged briefing: parks both blocked cases, promotes two backups from the candidate list, and writes a single 'Risks' line naming the two source-access problems so they are not forgotten.
</example>

---
description: Audit claims, evidence grades, and source quality for a case file, chapter brief, or draft. Uses source-ledger-discipline and citation-hygiene skills. Returns usable claims, weak claims, unusable claims, and source gaps.
owner: stephen-fact-check-director
argument-hint: "<file-path>"
---

# Source Audit

Dispatch the `stephen-fact-check-director` agent with task: audit claims, evidence grades, and source quality using `source-ledger-discipline` and `citation-hygiene`.

Output a list of usable claims, weak claims, unusable claims, and source gaps. Apply the A/B/C/D grades from `.claude/rules/02-evidence-grades.md` and refuse to promote a chapter-level claim that rests only on C-grade evidence (unless the chapter is explicitly about uncertainty).

If invoked without a file path, return: "Specify a file path (e.g. /source-audit book/chapters-v2/03-draft.md)." Do not guess.

<example>
Context: Stephen (fact-check director) needs to gate a draft before Wayne advances.
user: /source-audit book/chapters-v2/03-system-object-alibi-draft.md
assistant: Loads source-ledger-discipline and citation-hygiene, walks each claim, returns: "Usable (A): 7 claims tied to NTSB, JATR, FAA testimony. Weak (B): 3 reporter syntheses needing primary backup. Unusable (C): 1 attribution of internal motive (no admission on record). Gaps: missing Lion Air final report citation; reconcile two divergent flight-data quotes."
</example>

<example>
Context: A draft passes audit on claim count but rests its anchor on a single C-grade quote.
assistant: Returns 'passes claim count but anchor-fragile' status, gates the chapter from advancing on the strength of the anchor alone, and recommends Bonnie swap the anchor case or downgrade the chapter's claim.
</example>

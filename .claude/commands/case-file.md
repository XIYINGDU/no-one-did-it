---
description: Build or update a responsibility-laundering case file for a named historical, political, legal, corporate, war, or AI event. Uses the case-file-method and responsibility-chain-mapping skills. Stores the result under book/evidence/case-files/.
owner: delon-research-director
argument-hint: "<event-name>"
---

# Case File

Dispatch the `delon-research-director` agent with task: build or update a case file for the event named by the user using `case-file-method` and `responsibility-chain-mapping`.

Store outputs in `book/evidence/case-files/<slug>-case-card.md` unless directed otherwise. Always answer the eight diagnostic questions (publicly blamed / control / benefit / knowledge / preventability / record control / cost bearer / responsibility-if-followed-control) and assign an evidence grade from `.claude/rules/02-evidence-grades.md`.

<example>
Context: Crew Chief assigns a new case to draft for the AI-systems chapter.
user: /case-file Boeing 737 MAX MCAS
assistant: Loads case-file-method and responsibility-chain-mapping skills, answers the eight diagnostic questions, classifies the case (partial scapegoat: pilot blame stops below FAA/Boeing executives), assigns evidence grade A (NTSB and JATR reports), and writes book/evidence/case-files/boeing-737-max-mcas-case-card.md with a Handoff: Stephen (fact-check) line.
</example>

<example>
Context: A user types only the slug with no case named.
assistant: Returns a short error: 'Name the case after /case-file (e.g. /case-file Boeing 737 MAX MCAS).' Does not invent or guess a case to fill the slot.
</example>

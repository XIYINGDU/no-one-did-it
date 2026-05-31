---
name: chapter-blueprint
description: Turn approved case files into chapter architecture for serious trade nonfiction.
version: 1.0.0
---

# Chapter Blueprint

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Decision rubric

Usable output:
- Builds one chapter brief with all eight rhythm sections represented in sequence.
- Places one anchor case and supporting echoes with explicit weight and role.
- Includes one counterargument, evidence-grade risks, and a concrete handoff to Wayne.
- Keeps case taxonomy labels canonical and stable across sections.

Weak output:
- Delivers scene ideas without responsibility-chain logic.
- Omits counterargument or substitutes generic rhetoric for evidence-grade limits.
- Mixes chapter brief and chapter draft scopes in one artifact.
- Hides unresolved legal-risk or source gaps.

## Conflict handling

1. Two sources conflict on a load-bearing scene:
Keep the scene only if the stronger evidence grade source supports it; otherwise downgrade to open question and re-sequence the brief.
2. Two case classifications conflict inside the same chapter brief:
Retain only one classification per case in the brief body, then append a conflict flag and handoff to Stephen for verification before draft.
3. Two reviewer findings conflict on structure:
Prioritize the finding that protects evidence before elegance; if both are defensible, handoff to Bonnie for final sequence decision.

## Escalation conditions

- Proceed when the chapter brief can map every major claim to evidence grade and counterargument.
- Handoff to Delon when one required case lacks a usable source packet.
- Handoff to Stephen when a classification dispute affects chapter thesis.
- Handoff to Nancy when a scene relies on legally sensitive phrasing.

## Boundary-case recipes

1. Two-case chapter only:
Build anchor + echo structure, flag missing third case as a fragility risk, and handoff for sourcing before draft.
2. Strong scene, weak chain:
Keep the scene in notes, remove it from opening slot, and build opening from the stronger responsibility chain case.
3. Counterargument stronger than thesis:
Narrow chapter thesis, keep evidence-grade limits explicit, and handoff to Bonnie for scope reset before Wayne drafts.

## Status protocol

- Chapter blueprint output is a chapter brief and must set frontmatter `status: brief`.
- Wayne promotes chapter artifacts to `status: draft` during prose work.
- Promotion from `status: draft` to `status: ready` is gated by chapter-rhythm coverage.
- If rhythm sections are missing at promotion time, keep `status: draft`, flag gaps, and handoff for revise.

## Open-questions convention

Every chapter brief carries an `## Open questions` section enumerating decisions the architect leaves to drafting, downstream review, or xaiolai. Each numbered question must be followed by the architect's instinct and the named decision-owner. After the chapter has been drafted (or substantially advanced), questions accumulate status annotations so future readers do not re-derive what is already resolved.

Use one of five status tags per question, written as an inline `**STATUS (<ISO-date> <pass-name>):** [<TAG> — <one-line evidence>]` line directly under the question. Tags:

- `[RESOLVED IN DRAFT — <slot / line / phrase from prose>]` — the chapter prose materially answers the question, in a way consistent with the architect's instinct or by explicit alternative.
- `[TRACKED IN STATUS.md — <which cross-cutting row>]` — the question is on the exit-condition register or cross-cutting items table; resolution lives there, not in the brief.
- `[STILL OPEN — xaiolai]` — requires the principal author's explicit decision (length, voice, closing-sentence, judgment-of-tradeoff). Reserve narrowly; most "xaiolai sign-off" items can be resolved by red-team audit or by xiaolai-value judgment.
- `[DEFERRED — <to whom, by when, why>]` — live but routed to scheduled work (Stephen pre-galley, Nancy 30-day clock, diagrams workflow, etc.).
- `[STALE — <reason>]` — invalidated by spine changes, scope cuts, or reabsorption of other chapters; record the reason.

Multiple passes append rather than overwrite — `STATUS (2026-05-28 triage)` and `STATUS (2026-05-28 followup, xiaolai-value judgment)` can coexist under the same question. Audit trail preserves what was thought-and-when.

Briefs are exempt from rule 14 (`scan-pronoun-discipline.py`). They are architecture artifacts that legitimately discuss "the chapter" / "the reader" / "the book" as objects of architectural design.

Build chapters with this default structure:

1. Opening accusation scene.
2. Official explanation.
3. Hidden responsibility architecture.
4. Older or newer echo.
5. Record-hardening mechanism.
6. Counterargument.
7. Alibi-collapse moment.
8. Anti-laundering rule.

Include:
- opening scene candidate;
- chapter thesis;
- primary case;
- secondary cases;
- scenes to draft;
- required sources;
- diagram idea;
- chapter-ending rule.

<example>
Context: Three approved case files (Boeing 737 MAX, Bhopal, 2008 ratings agencies) need to become a system/object-alibi chapter.
input: anchor=Boeing; echo=Bhopal; echo=ratings-agencies-2008
output: Returns a chapter blueprint — opening scene (Boeing test pilot's email), thesis (the "system" alibi laundered control upward), case hierarchy (anchor 70%, two echoes 20%+10%), counterargument section, evidence gaps list, legal-risk flags, narrative rhythm map (accusation → official story → hidden architecture → alibi failure → anti-laundering rule), handoff to Wayne for prose draft.
</example>

<example>
Context: Boundary case: only two case files are approved when the chapter wants three.
output: Returns a two-case blueprint (anchor 70%, echo 30%) with an explicit gap note for the absent third case, and a flag for Bonnie that the chapter is fragile to a single case being downgraded by Stephen.
</example>

---
description: Run the per-chapter production pipeline for one chapter — read STATUS.md to identify the next incomplete stage, dispatch the right agent, update STATUS.md after completion. Resumable across sessions; safe to call multiple times on the same chapter (will pick up where the last call stopped).
owner: jerry-crew-chief
argument-hint: "<chapter-slug>"
---

# Produce Chapter

Dispatch the `jerry-crew-chief` agent to orchestrate the production pipeline for one chapter, end-to-end, following `.claude/docs/book-production-workflow.md`. Jerry routes to the appropriate cell lead at each stage (Bonnie / Wayne / Delon / Stephen / Laura / Nancy / Blair) per the workflow. The argument is the chapter slug (e.g., `03-who-could-have-stopped-it`). Surfaces principal-author input requirements (beat-10 sanity, commits, scope expansions, strategic pivots) back to the human rather than auto-deciding.

## What to do

1. **Read `book/STATUS.md`.** Identify the row for the named chapter. The State column and the cell pattern tell you the next incomplete stage.

2. **If no argument is supplied:** return `"Specify the chapter to produce (e.g. /produce-chapter 03-who-could-have-stopped-it). To see overall book state, run /book-status."` Do not pick a chapter unilaterally.

3. **If the chapter is at `status: ready`:** return `"Chapter <slug> already at status: ready. To start a new chapter, choose one with state 'queued' or 'partial' in /book-status."`

4. **If the chapter has a `partial` state with partial case files:** start at Stage 2 (case-file research) for the missing case files. ch-5 is the current partial — Bhopal case file exists; needs the other three for the chapter's full anchor set plus four paired counter-cases.

5. **Otherwise:** start at the first incomplete stage per `.claude/docs/book-production-workflow.md` per-chapter pipeline.

## Per-stage dispatch

| Stage | Agent | What you tell them | What they return |
|-------|-------|--------------------|------------------|
| 1 (spine confirmation) | `bonnie-book-architect` | Verify the chapter's role in the spine is unchanged. | Confirmation or flagged drift. |
| 2 (case-file research) | `delon-research-director` → routes to Shirley/Selina/Warren/Loki by domain | The chapter's case list + the counter-case-method requirement | One scapegoat case file + one paired counter-case file per anchor, all at `status: brief` |
| 3 (Stephen verification) | `stephen-fact-check-director` | All case files from Stage 2 | Per-file grades; `brief → draft` for files that clear; `[VERIFICATION GAP]` flags |
| 4 (chapter brief) | `bonnie-book-architect` (with `chapter-blueprint` skill) | The cleared case files + the spine entry + the 10-beat rhythm + reader-value template | `book/chapters-v2/<NN>-<slug>-brief.md` |
| 5 (prose draft) | `wayne-narrative-lead` (with `scene-construction` skill) | The brief + all case files + Bonnie's architecture decisions | `book/chapters-v2/<NN>-<slug>.md` at `status: draft` with all 10 beat markers |
| 6 (Stephen chapter-level) | `stephen-fact-check-director` | Chapter prose + case-file source ledgers | Prose-drift report; gate to proceed to Alan/Nancy/Laura |
| 7 (Nancy chapter-level) | `nancy-legal-risk-counsel` | Chapter prose + defamation-risk inventory from brief | Per-sentence wording verdict; 30-day re-pass clock for live-case content |
| 8 (Alan doctrinal) | `alan-expert-reviewer` | Chapter prose + relevant frame(s) | Per-frame verification; load-bearing revisions |
| 9 (Laura red-team) | `laura-red-team-editor` | Chapter prose, standalone | Overclaim audit; taxonomy install audit; specific revisions |
| 10a (Bonnie structural) | `bonnie-book-architect` | Post-revision chapter | Architecture-still-holds confirmation OR specific architectural revision |
| 10b (Principal beat-10) | **xiaolai (human)** — surface; do not auto-decide | Beat 10 wording + threshold rule (if any) + chapter closer | Approval or revision request |
| 10c (Jerry promotion) | `jerry-crew-chief` | Cleared chapter + all gate records | Status edit `draft → ready`; memory note recording promotion + any date-fired re-passes |

## After each stage

- Apply any revisions the gate produced (either dispatch the original author to revise, or apply mechanical edits directly via Edit when the gate gave verbatim replacement text).
- Verify validators still pass (`scan-overclaim`, `operating-validator` warn-mode; pytest if any code/test files touched).
- **Update `book/STATUS.md`** — mark the stage cell, update the "Last updated" timestamp, append any cross-cutting items the stage surfaced.
- If a finding requires principal-author input (per the workflow's "Surfaces to the principal" list), stop and surface; do not auto-proceed.

## Constraints

- **Defamation discipline** is enforced at the case-file level (Selina applies Nancy's wording) and the chapter-prose level (Wayne preserves; Nancy chapter-level catches drift). Both gates fire.
- **Vocabulary discipline (R51)** is enforced by the NLPM scoring on commit. Use canonical terms from `.claude/skills/vocabulary/registry.yaml`.
- **Pure-scapegoat anchor gate** fires for ch-5, ch-7, ch-11, ch-13. Cases like Sacco/Vanzetti (partially contested) may be used as echoes but not anchors in those chapters. See `.claude/agent-memory/bonnie-book-architect/project_downstream_pure_scapegoat_gate.md`.

## What you do NOT do

- Do not commit. The principal author decides commits.
- Do not skip stages under pressure. Every chapter passes the gate sequence.
- Do not modify `book/toc.yml`. Spine changes are principal-author decisions.
- Do not write argumentative chapters (Part IV) without the principal-author's input on the chapter's voice and emphasis.

## Response format

After each `/produce-chapter` call returns, report:

- Chapter and current state
- Stages completed this call
- Findings surfaced (especially for principal)
- Updated STATUS.md row
- Next stage and what runs it

<example>
Context: principal runs `/produce-chapter 03-who-could-have-stopped-it` for the first time.
input: chapter-slug = "03-who-could-have-stopped-it"
output: Reads STATUS.md; chapter is queued, no case files. Starts at Stage 1 (spine confirmation) via Bonnie. Bonnie confirms; advances to Stage 2 (case-file research). Dispatches Delon to plan; Delon routes to Shirley for the eight-question diagnostic case (likely a small clean historical case the chapter uses to walk the questions) + counter. Reports back: Stage 1 ✓, Stage 2 in progress with Delon. Next call: continues from Stage 2 output.
</example>

<example>
Context: principal runs `/produce-chapter 02-the-four-goats` on an already-ready chapter.
output: "Chapter 02-the-four-goats already at status: ready. To start a new chapter, choose one with state 'queued' or 'partial' in /book-status."
</example>

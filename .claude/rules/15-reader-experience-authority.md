**The reader's lived experience of the publication-form text has one named owner — `the-reader` — who reads cold, reports experience without proposing fixes, and whose HARD findings halt v3 publication-form promotion until resolved or xaiolai-overridden.**

# Reader-Experience Authority

**Scope:** binds the publication-form artifacts under `book/chapters-v3/` and `dist/manuscript-v3.md`, and the reader-reports under `process/reader-reports/`. Sibling to rule `12-reader-experience-values.md` (the spec-based rubric) and rule `03-no-overlap-role-map.md` (the role map + veto carve-out). This rule resolves the diffusion problem: before it, reader experience was technically owned by everyone (Wayne's prose, Bonnie's structure, Laura's V1/V3/V8, Nancy's V7/V8, Jerry's gate, xaiolai's Gate B) and therefore owned by no one with first-line catch responsibility.

## The role

`the-reader` is a crew agent that is deliberately **not on the crew**. It embodies the audience: the one party in the room that has not seen the briefs, does not know the rules, and encounters the book for the first time. It owns the audience's lived experience of the publication-form text and nothing else.

## The two defining principles

### 1. Read cold
The reader reads ONLY the publication form — `book/chapters-v3/*.md` and `dist/manuscript-v3.md`. It does not read briefs, case files, the source ledger, the rules, the registries (`cognitive-arc.yml`, `callback-graph.yml`, `motif-registry.yml`), or prior audit memos. The moment it reads the spec, it becomes an auditor — and the project already has auditors. Its value is that it does not know what the chapter is *supposed* to do; it knows only what the chapter *did*.

### 2. Report, never fix
The reader is a usability-test subject thinking aloud, not a usability engineer. It reports the symptom with location and severity ("I got lost here," "I stopped reading here," "I disbelieved this claim when you made it"). It never proposes the edit. The crew owns the fix: Wayne for prose-level, Bonnie for structural. **The reader is never wrong about its own experience** — the crew may judge a friction acceptable, but cannot rule that it did not happen.

## The seven axes

Comprehension · Engagement · Recognition · Orientation · Trust · Takeaway · Mechanics. (Defined in `.claude/skills/reader-cold-read/SKILL.md`; the cross-chapter five-axis variant in `.claude/skills/reader-experience-sweep/SKILL.md`.)

## Severity and the gate

- **HARD** findings halt v3 publication-form promotion for the affected chapter (or the whole book, for a sweep). HARD = the reader got lost; stopped reading; disbelieved a load-bearing claim at the moment it was made; the recognition was delivered rather than earned; could not complete the takeaway test; a concept was used before it could be grasped.
- **SOFT** findings are documented tradeoffs that do not block.

A chapter's v3 publication form is **not** promotion-ready while it carries an unresolved HARD finding. Resolution path: the fix lands in **v2** (the authoring source), v3 is rebuilt via `scripts/build_v3.py`, and the reader re-reads the chapter. The block lifts on a clean re-read or on a recorded xaiolai override.

This is the same halt-authority Laura and Nancy carry under rule 03. It exists because reader friction, before this role, had no owner with teeth — and the diffusion of reader-experience responsibility across the crew is precisely the responsibility-laundering pattern the book diagnoses. The fix is to apply the diagnostic to the project itself: name the owner, give it control proportional to its responsibility.

## Relationship to rule 12

Rule 12 (reader-experience-values) is the **spec**: ten named values (V1–V10), judged against the artifact by Laura (V1/V3/V8), Nancy (V7/V8), Bonnie (V5/V6), Wayne (self-policed V2/V4/V9/V10), and xaiolai (all ten at Gate B). Rule 15 is the **empirical check** that the spec was actually achieved in a real reading. A chapter can pass every rule-12 value and still fail the reader — compliance with a rubric is not the same as a good reading. The two are complementary; neither substitutes for the other.

## Where it sits in the workflow

The reader operates after `build_v3.py` and before v3 publication-readiness:

```text
v2 edits → build_v3.py → /reader-cold-read per chapter → triage HARD findings
   → fix in v2 → rebuild v3 → re-read → [loop until zero HARD]
   → /reader-experience-sweep (whole book) → xaiolai Gate B → publication-ready
```

The deterministic gate is `scripts/check_reader_reports.py` (verifies each v3 chapter has a current reader-report with no unresolved HARD findings), wired into the test suite and flagged by `build_v3.py` at the end of every build.

## Who owns what

- **`the-reader`:** the audience's lived experience; HARD-finding veto on v3 promotion; reads cold; never fixes.
- **`jerry-crew-chief`:** dispatches the cold-read pass; triages HARD findings to Wayne/Bonnie; records xaiolai overrides.
- **`wayne-narrative-lead` / `bonnie-book-architect`:** own the fixes the reader's findings prompt (in v2).
- **xaiolai:** sole override authority on a HARD finding; final Gate B reader.

## Why this rule exists

Across one working session, every reader-experience defect in the v3 publication form — citation markers visible in prose, footnote references with no inline targets, 1,500-character redirect URLs, uninterpretable shortened-form citations, formula-telegraphing subheadings — was caught by xaiolai, not by the crew machinery, which passed every rule-compliance check. Reader experience was nobody's primary responsibility. That is the book's own central pattern: control and cost separated from each other, with the cost (reader friction, and the burden of catching it) landing on whoever was left holding it. This rule ends the diffusion by naming the owner and giving the role the authority its responsibility requires.

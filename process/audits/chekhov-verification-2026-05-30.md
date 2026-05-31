# Chekhov-Discipline Verification — v6 canonical, pre-compile

**Date:** 2026-05-30
**Scope:** All 13 v6 chapters + 3 cross-chapter registries (callback-graph.yml, motif-registry.yml, cognitive-arc.yml) + ch-1↔ch-13 opening↔closing edge + per-chapter fair clues.
**Trigger:** Verification pass before manuscript compile. The book's three Chekhov registers — *fair clue* (chapter-internal), *callback* (cross-chapter), *motif* (book-spanning image) — re-verified against the current canonical text following the v6 cut (2026-05-30), which carried substantive post-baseline edits the 2026-05-27 baseline audit did not see.
**Owners:** Verification dispatched by jerry-crew-chief role; story-architect agent for the opening↔closing edge and per-chapter fair clues; general-purpose verifiers for the three registry walks.

## Bottom line

**The book's Chekhov discipline is intact.** Zero HARD findings. The book-spanning gun (ch-1 opening object → ch-13 reweighted return) fires cleanly across three independent registers. The 22 callback edges all have surviving prose at both endpoints. The 9 motifs are clean to the registry — including the high-stakes `the-altar` forbidden-zone, which is preserved without leakage across the ten silent-altar chapters. The cognitive arc carries 49/50 items as declared. 11/13 chapters' fair clues test clean; the two SOFT findings are framing chapters (ch-1, ch-13) whose recognition is metaphorical and architecturally rescued by other moves.

**Manuscript compile is not blocked** by Chekhov discipline. Three items below are SOFT and warrant xaiolai's attention; none stop compile.

---

## SOFT items requiring xaiolai judgment

### 1. The ch-13 final-sentence placeholder is gone — author unclear

`book/STATUS.md` and the project focus snapshot list as outstanding:
> "xiaolai-authored closing sentence for ch-13 — `book/chapters/13-a-readers-field-guide.md` line 303 carries `*[FINAL SENTENCE — xiaolai authors]*` as an explicit placeholder"

v6 canonical (`book/chapters-v6/13-a-readers-field-guide.md`) ends at line 285 with completed prose:

> *No one did it* was never a fact. It was a seam — the place where a name had been lifted out of the sentence. Now we know where to look. And now we can say who.

There is no placeholder marker in v6. The placeholder appears to have been silently resolved during the v3→v6 cycle (build-time fill, prose-editor pass, or earlier authoring not recorded as xiaolai's). The current line is structurally sound: it bears all four loads the architectural slot requires (title resolution / hammer-line third beat / instrument inversion / cost-honest floor — full analysis in the cold-read report below).

**Decision required from xiaolai:**
- **(a) Claim** — accept the current line as the authored closing (and update STATUS.md / focus snapshot to remove the open item).
- **(b) Replace** — write a different final sentence; the architectural slot will support it.
- **(c) Revert** — restore the placeholder explicitly until authored.

The book's own diagnostic is relevant here: a placeholder for principal-author judgment was apparently resolved without an authoring record, and the outstanding-work list still shows it open. That is exactly the substitution pattern the book diagnoses — at micro scale, inside the book's own production process. Worth recording the decision however it goes.

### 2. `responsibility-chain` concept introduced structurally in ch-1, not lexically

The cognitive-arc registry declares `responsibility-chain` as a Part I foundational vocabulary item introduced in ch-1. The literal phrase "responsibility chain" first appears in ch-3 (line 181). In ch-1 the *idea* is delivered — repeatedly — through "the visible names and the operational names have separated" (L157), "the cameras are pointed at the substitute. The signatures are happening elsewhere" (L157), and the closing "if our face is the public face of a decision, and we cannot name in writing who authorised the decision above us, we are at the altar" (L165). The structural payload lands; the noun does not.

**Decision required from xiaolai:**
- **(a) Registry update (light touch)** — re-declare `responsibility-chain` introduction as ch-3 in `book/cognitive-arc.yml`. Matches what the prose does.
- **(b) Single ch-1 sentence** — add one naming sentence in ch-1's beat-9 / beat-10 region (around L145–L167) explicitly calling out "the responsibility chain." Preserves the ch-1 install order, costs one sentence.

This is the only finding among 50 cognitive-arc items requiring action.

### 3. Two underweighted plants — ch-1 and ch-13 (framing chapters)

Both framing chapters carry SOFT findings on per-chapter fair-clue discipline:

- **ch-1.** The structural fair clue is "four thousand by dawn" (L19) plus the Reichstag Fire Decree publication-date detail (L27). The chapter then walks ~95 lines through Tyndale, Leviticus, Athens, Babylon, Rome before the recognition lands at L113–L117. The plant is concrete and dated; the distance is rescued by the explicit re-reading prompt ("Read it again, and something the first reading did not show comes forward"). The Tyndale/Azazel etymology is doing analogy work (metaphor-rule satisfaction), not fair-clue work, so it is not an orphan even though it does not fire as recognition trigger.
- **ch-13.** The candidate plant ("There is no priest here. There is a field guide. The instrument is ours.", L19–21) is a frame statement, not an evidentiary clue. The recognition at L246 ("We are the escape") is primed by the chapter's six artefacts and the eight counter-case namings (Picquart, Serpico, Bates, etc.), but the connective tissue ("each began with a person who noticed something") arrives only at the recognition itself.

**Anti-Chekhov posture (per the user's directive — cuts not adds):**
Neither chapter warrants a plant addition. ch-1's recognition is rescued by the four-thousand-arrests detail; ch-13 is a consolidation chapter and the fair-clue lens is a slightly imperfect fit for its job. **No prose change recommended for either.** The SOFT findings are logged for awareness; they are not defects warranting pre-compile work.

---

## Registry maintenance (housekeeping, not blockers)

### Callback graph — ~9 edges carry section-heading drift

v6 adopted descriptive section headings throughout ("Three documents, no name", "Backup tapes the destroyers forgot", "Six questions for a citation") in place of the conventional A2B beat names in the registry ("accusation scene", "older echo", "hidden architecture", "what this might mean for us"). All 22 edges have surviving prose at both endpoints — the underlying setup→payoff structure is intact. Only the registry metadata has drifted.

| Edge | Drift type | Recommendation |
|---|---|---|
| 12 abu-ghraib-chain-of-command-callback | Paraphrase drift in ch-10 payoff | Update line_anchor to v6 phrasing |
| 13 ukrainian-children-civilian-invisibility-callback | Both endpoints drifted; section name also drifted | Update plant section + both line_anchors |
| 14 eo-13328-vs-inquiries-act-design-contrast | Section name drift on both endpoints | Update plant section ("What made the inquiry work") + payoff section ("Three documents, no name") |
| 16 signature-is-the-seam-rule | Section name drift on both endpoints | Update plant section ("Treat the citation as a hypothesis") + payoff section ("Name the person before the design ships") |
| 19 walsh-iran-contra-cover-up-callback | Section name drift on both endpoints | Update plant section ("Watergate, Iran-Contra, al-Aulaqi") + payoff section ("Backup tapes the destroyers forgot") |
| 20 hofeller-files-posthumous-custody | Section name drift + "slot 5" tail removed from payoff line_anchor | Update sections + drop "slot 5" |
| (~3 more, minor) | Conventional beat-name → descriptive heading | Sweep maintenance |

**Recommendation:** Single maintenance pass on `book/callback-graph.yml` to re-key drifted section fields and line_anchors to v6's descriptive headings. This is auditor hygiene — it keeps `/callback-audit` re-runnable cleanly. Not a prose change.

### Motif registry — no maintenance required

9/9 motifs clean. One soft observation only: `the-fair-clue` sits exactly at floor (4 declared, 4 found, floor = 4). A single demotion in any of ch-7, ch-9, ch-11, or ch-12 would push it below floor. No action required; flag for awareness in any future polish pass.

### Cognitive arc — see SOFT item 2 above (responsibility-chain)

---

## Verified clean — what the audits confirmed

This is the load-bearing positive evidence. The book's Chekhov-discipline status before compile:

### The book-spanning gun fires (ch-1 → ch-13)

The architectural cold-read confirms the reweighted return across three independent registers:

1. **Scene callback.** The two-goats Leviticus scene of ch-1 (L49–58) is replayed verbatim as the accusation beat of ch-13 (L15) — same scene, reader's position inside it has swapped from witness to priest's-instrument-bearer.
2. **Thesis callback.** "The substitution has gone underground into the morning's headline, into the press release, into the docket number" (ch-1 L45) is re-quoted near-verbatim at ch-13 L17, then immediately framed by "The community had stopped watching. The diagnostic is how the watching resumes" (L264). The verb changes from describing a loss to naming the instrument that restores.
3. **Hammer-line reweighting.** "The altar moves. The substitution does not." (ch-1 L117) becomes "The altar moves. The questions stay." (ch-13 L283). Same opening cadence; reweighted second clause. The difference between the two clauses *is* the thirteen-chapter argument.

The reader who returns to ch-1's opening object after finishing ch-13 sees what the first reading could not: van der Lubbe as a *pure scapegoat* (ch-2 taxonomy), bearing a *partial scapegoat operation* extended to Torgler/Dimitrov/Popov/Tanev (ch-2), authorised by a *record-control move* (ch-7), legalised by a *Park-shaped reverse design* (Lex van der Lubbe inverting ch-11). The opening object retroactively carries five chapters' worth of capacity. **A2B Engine V2.2 success criterion: met.**

### Callback graph — 22/22 PASS structurally

Every declared setup→payoff edge has surviving prose at both endpoints. Zero orphaned plants. Zero orphaned payoffs. The 9 drifted edges (see maintenance section above) are line_anchor / section-name metadata drift, not structural failure.

### Motif registry — 9/9 PASS clean

| Motif | Count / Floor | Forbidden zone | Evolution |
|---|---|---|---|
| the-chain | 12 / 8 | Clean (zero ch-1 matches) | Progresses |
| the-named-cause | 10 / 6 | n/a | Progresses |
| signature-as-seam | 10 / 5 | n/a | Progresses |
| the-record | 13 / 8 | n/a | Progresses |
| the-signed-document | 8 / 6 | n/a | Progresses |
| the-court-or-inquiry | 12 / 8 | n/a | Progresses |
| the-classified-or-sealed-file | 10 / 6 | n/a | Progresses |
| the-fair-clue | 4 / 4 (at floor) | n/a | Progresses |
| **the-altar** | **3 / 3** | **Clean (only ch-1, ch-9, ch-13)** | Progresses |

The title-anchor motif is intact. `the-altar` appears in exactly three chapters (1, 9, 13); zero "altar" matches in chapters 2, 3, 4, 5, 6, 7, 8, 10, 11, 12. The ch-13 resonant-return lands undiluted.

### Cognitive arc — 49/50 PASS

- **17/17 discriminations** introduced AND consolidated AND used in `required_by` chapters.
- **26/27 concepts** named/defined in declared introduction chapter (the one exception is the SOFT item 2 above).
- **6/6 retirements** explicitly named and dismantled in declared chapter.

The five v6 post-baseline edit zones (ch-2 reorientation, ch-6 navigator, ch-7 anchor relock, ch-11 navigator, ch-1 preface superlative removed) were all spot-checked. None disturbed a discrimination, consolidation, retirement, or concept install except as noted.

### Per-chapter fair clues — 11/13 CLEAN

- Zero gotcha reveals (rule 10 / A2B forbidden failure: none detected).
- Zero orphaned plants (no prominent detail introduced and dropped).
- 11/13 chapters: fair clue is concrete, dated, and the recognition can be retraced to it. Eight of these explicitly self-name their fair clue ("the fair clue is in [X]", "we return to that sentence") — architectural choice that mostly succeeds.
- 2/13 chapters: SOFT (framing chapters; analyzed above).

---

## Recommendations to xaiolai

In order of action:

1. **Decide the ch-13 final-sentence placeholder question.** (SOFT item 1.) Three options listed. The current L285 prose is structurally sound; the question is authorship attribution.
2. **Decide the `responsibility-chain` ch-1 install question.** (SOFT item 2.) Registry move (light) or single-sentence ch-1 addition (preserves install order).
3. **Run the registry maintenance pass** on `book/callback-graph.yml` to re-key ~9 drifted section fields. Auditor hygiene; keeps `/callback-audit` re-runnable. Can be done at any time before next book-level audit; not blocking.
4. **No prose changes recommended** in any of the 13 chapters. The two SOFT framing-chapter findings (ch-1 underweighted plant rescued by four-thousand-arrests detail; ch-13 underweighted plant rescued by six artefacts and counter-case roll-call) are not defects warranting pre-compile work. Anti-Chekhov posture honored: no adds.
5. **Manuscript compile is unblocked** by Chekhov discipline. Proceed with `/compile-book` when the above decisions are resolved or accepted as deferred.

---

## Methodology and audit trail

**Verification approach.** Five parallel verification streams, each operating only on the v6 canonical chapter source (`book/chapters-v6/`) and the three registries. No streams read briefs, case files, audit memos, dev-docs, or prior chapter versions (v3/v5 archived and out of scope).

**Streams:**
1. Callback graph (22 edges) — general-purpose agent; grep + Read; 31 tool calls; structured PASS/FAIL per edge.
2. Motif registry (9 motifs) — general-purpose agent; appearance + forbidden-zone + floor + evolution checks; 23 tool calls.
3. Cognitive arc (17 + 27 + 6 items) — general-purpose agent; concept-phrase grep per item + spot-check `required_by` sampling; 54 tool calls.
4. ch-1 ↔ ch-13 opening↔closing edge — story-architect agent; cold-read; 2 tool calls (full-chapter Reads only).
5. Per-chapter fair clues — story-architect agent; cold-read 13 chapters; 27 tool calls.

**Total subagent budget:** ~880K tokens, ~14 minutes wall-clock (parallel).

**Source-of-record discipline.** Where this report and the project focus snapshot disagree on the ch-13 placeholder, this report records what was found in the v6 file as canonical; the focus snapshot is noted as referring to an earlier file location (`book/chapters/13-...`) that no longer exists.

**Re-runnability.** The five verification streams are reproducible via the existing skills:
- `/callback-audit` (book-level)
- `/motif-audit` (book-level)
- `/cognitive-arc-audit` (book-level)
- `story-architect` agent for the opening↔closing edge and per-chapter fair clues
- `/fair-clue-audit` (per chapter)

The registry maintenance pass (recommendation 3 above) should be performed once before any future re-run, so the audits land on clean drift.

---
description: "Style guide for prose artifacts (chapters, proposals, narrative passages): voice, vocabulary, chapter rhythm, and banned tropes."
---

**Write prose that is precise, severe, readable, non-flattering, nonpartisan, and evidence-driven; chapter rhythm is non-optional.**

The book's authority rests on the same discipline it demands of the institutions it analyzes, so every stylistic choice must reinforce — never undermine — the evidence standard.

# Style Guide

**Scope:** binds every prose artifact in `book/chapters-v2/`, `book/proposals/`, and any narrative passage Wayne or Blair produces. Case-file YAML cards and audit memos follow the templates in `.claude/docs/`, not this guide.

Voice: precise, severe, readable, non-flattering, nonpartisan, evidence-driven.

Use:

- short sentences at moral turning points;
- strong verbs;
- concrete scenes;
- explicit responsibility-chain maps;
- careful distinction between allegation, finding, admission, judgment, settlement, and conviction.

Avoid:

- purple prose;
- invented psychology;
- slogans as proof;
- overusing the term "responsibility laundering" (cap: once per chapter unless the chapter is explicitly about the term itself);
- treating complexity as automatic guilt;
- treating weakness as automatic innocence.

Chapter rhythm — the default arc, not a uniform template. The ten beats below are the palette every chapter draws on, not a fixed sequence stamped identically onto each chapter. Sections may be merged, reordered, compressed, or carried in flowing prose. What every chapter owes is the *movement* — accusation → hidden architecture → anti-laundering rule → reader-applicability — not the same visible scaffold in the same order. Vary the cadence across chapters: no run of chapters should close with the identical block (e.g. the same "recognise / diagnose / act / avoid" role-walk), and recurring hammer-lines and motifs must not be stamped at a frequency that wears them out before their payoff. (Amended for v4 after a cold-read finding that the uniform ten-beat rhythm read as monotonous across the book's middle; v4 reconstructs the chapter structure with controlled variation.)

1. accusation scene;
2. official story;
3. hidden architecture;
4. older echo;
5. record hardens;
6. goat resists;
7. alibi weakens;
8. anti-laundering rule;
9. the escape;
10. what this might mean for us — Job 1 (the role-by-role action walk) is consolidated once in ch-13's crosswalk; Job 2 (the chapter-specific landing) is owed per chapter and may fold into beat 8.

Beats 9 and 10 are non-negotiable **as content, not as form**. Every chapter still owes beat 9 ("the escape") — the paired counter-case from `.claude/skills/counter-case-method/SKILL.md`, a documented interception of the same laundering pattern, naming the intercepting mechanism and the cost of escape; a chapter for which no counter-case exists still owes it by stating the absence and documenting the search. Beat 10 ("what this might mean for us") splits into two jobs. **Job 1 — the role-by-role action walk** (what specifically to do as victim, bystander, or institutional actor) — is removed from individual chapters and consolidated once, in the field-guide crosswalk (ch-13); chapters 3–12 must not reproduce it as a per-chapter role-cycle. **Job 2 — the chapter-specific landing** (how *this* pattern shows up in non-headline life, and its warning sign, per `.claude/docs/reader-value-template.md`) — is owed by each chapter as one or two sentences, and may be folded into beat 8 (the anti-laundering rule). A chapter satisfies its reader-applicability obligation with beat 8 + beat 9 + the short Job-2 landing; it does not owe a role-walk. Job 2 may not be generic; "stay informed" is not Job 2.

What is *negotiable* is the form. These two beats must reach the reader, but they need not arrive via the same labelled block, the same role-walk, or the same closing cadence in every chapter — that uniformity is precisely what a cold reader skimmed across the book's middle. The comprehensive role-by-domain matrix lives once, in the field-guide crosswalk (ch-13); a per-chapter beat 10 may therefore carry a single sharp move calibrated to that chapter rather than re-walking every role. Vary the closing shape chapter to chapter; let the movement, not the scaffold, be the constant.

## Implication-burden discipline

Implication-level overreach is treated as overclaim per rule `07-implication-burden.md`. Verb-level overclaim (`knew`, `lied`, `proves`) is caught by rule `05-overclaim-language.md`; structural overclaim — implication produced by sentence sequence, paragraph adjacency, focalization, juxtaposition, or named-then-named ladder — is caught by rule 07.

Focalization choices and delayed naming carry implication weight even when no banned verb appears. When Wayne uses focalize-then-break, document-as-protagonist, two-track time, delayed naming upward, or voice braid (the Bucket 1 craft moves authorized in `dev-docs/fiction-craft-rewrite-analysis.md`), every implication-bearing paragraph must either cite, hedge, or name the inferential step as inference per rule 07.

Wayne self-polices during drafting using rule 07's pattern table. Stephen verifies during fact-check. Laura red-teams against rule-07 specifically. Nancy vetoes on implication-driven defamation surface per rule 03.

## Reader-experience-value discipline

Rule `12-reader-experience-values.md` specifies ten declared values for judging engagement quality. Wayne self-polices the five craft values during drafting (V2, V4, V9, V10) and produces evidence on the five core values (V1, V3, V5, V7, V8) at Gate B. The style choices in this rule (short sentences at moral turning points; strong verbs; concrete scenes; explicit chain maps; banned tropes) are the standing means by which V1, V3, V7, V8 stay green.

## Authorial stance

Authorial voice follows rule `14-authorial-stance.md`. The author stands beside the reader, never in front. Default pronoun is "we" (co-investigator); "I" only for authorial judgment under uncertainty; imperative for instruction; "you" only inside cited quotes. Refuse meta-frame language ("this chapter," "the book," "the reader," "readers," "this section," "the author") that positions the analysis as a separate object the reader is receiving. The `scan-pronoun-discipline.py` hook catches mechanical violations at edit time; the `/pronoun-discipline-audit` skill is the deeper read.

## Citation form

Citations follow Chicago Manual of Style 17th edition, Notes-Bibliography system, per rule `13-citation-form.md`. Three-layer model:

1. **In-prose source identity** (audio-survivable, required for every load-bearing source): the speaker, venue, date, court, or inquiry is named in the sentence itself — never hidden inside the `[CITE:]` bracket.
2. **Inline `[CITE: <card-slug>]`** marker carrying only the source-ledger card slug. The compile step resolves slug to endnote.
3. **Back-of-book endnotes + Selected Bibliography**, generated by `/compile-book` from card metadata.

Wayne writes Layer 1 in-prose source naming as part of drafting; Layer 2 markers are short and slug-only; Layer 3 is compile-generated and Wayne never authors endnote text in prose. The `/cite-density-audit` skill enforces the slug-only invariant on inline brackets.

## Why this rule exists

A book that argues against laundered language cannot itself lean on purple prose, invented psychology, slogan-as-proof, or false equivalence. The chapter rhythm is not decoration: it is the cadence by which every chapter walks the reader from accusation to anti-laundering rule, so the book's structural argument survives a skim.

---
name: cite-density-audit
description: Audit chapter prose for verbose inline `[CITE:]` markers that violate rule-13's slug-only invariant. Inline `[CITE:]` brackets must carry only card slugs (separated by `;` for multi-source claims); full citation apparatus lives in the source-ledger card and is compile-generated as Chicago NB endnote. Catches the failure mode where citation metadata leaks from card to prose. Cousin to `scan-cite-density.py` (the cheap pattern-level pass); this skill is the deeper read.
version: 1.0.0
---

# Cite-Density Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After Wayne or any agent edits a chapter prose file.
- Before any chapter promotion from `in-review` to `ready`.
- Across the corpus before running `/compile-book` (verbose brackets break the Chicago formatter).
- Whenever the source-ledger sweeps in changes that may have leaked metadata into chapter prose (the ch-06 Nielsen pattern that motivated rule 13).

The `scan-cite-density.py` hook fires on every edit at the pattern layer. This skill is the deeper read — verifies the corpus-wide invariant holds.

## Decision rubric

A chapter passes cite-density audit when EVERY inline `[CITE:]` bracket satisfies ALL of:

1. **Slug-only content.** Bracket contains one or more card slugs separated by `;`. Slug pattern: `[a-z0-9]+(?:[-_][a-z0-9]+)*`.
2. **Length cap.** Total bracket (including `[CITE: ` prefix and `]` suffix) ≤ 60 characters.
3. **Card existence.** Every slug resolves to an existing file at `book/evidence/source-ledger/cards/<slug>.md`.
4. **No citation-apparatus phrasing.** No commas, no quotation marks, no "reproduced verbatim in", no "tier-1", no "archived at", no "see also", no "Stephen verify" (the `pending-stephen-lock` suffix is the only permitted non-slug content per rule 13).

A chapter fails when:

- Any inline `[CITE:]` bracket carries a full citation ("Author, \"Title,\" Journal vol. (year)").
- Any bracket carries a corroboration list ("AP, Reuters, NYT").
- Any bracket carries archive metadata ("archived at ...").
- Any slug points to a card that doesn't exist (broken reference).
- Any bracket exceeds 60 characters without justification.

## Conflict handling

1. **Bracket exceeds 60 chars but contains only valid slugs separated by `;`.**
   Permitted if 3+ valid slugs share one bracket (a load-bearing claim with multiple supporting sources can legitimately exceed the cap). Document the exception in the audit output.

2. **Bracket contains `pending-stephen-lock` suffix.**
   Permitted per rule 13. The suffix is the only non-slug content allowed inline. The audit confirms the slug exists and the suffix syntax is exact (`<slug> — pending-stephen-lock`).

3. **Bracket contains a card slug that doesn't yet exist.**
   Hard fail. Either Stephen creates the card OR the marker is converted to `[EVIDENCE NEEDED: <description>]` until the card lands.

4. **Bracket contains a Layer-1 in-prose-source-naming pattern leaked into the bracket** (e.g., the speaker name and date are inside `[CITE:]` instead of in the sentence).
   Hard fail; route to Wayne to restore Layer 1 in prose voice and reduce bracket to slug-only.

5. **Bracket structure is correct but the surrounding paragraph lacks Layer-1 in-prose source naming** (per rule 12 V10 and rule 13 Layer 1 requirement).
   Soft fail; route to Wayne to add in-prose source-naming. Cite-density audit reports the structural issue; the in-prose-naming pattern is enforced at audit-chapter / contract-audit time.

## Escalation conditions

- Escalate to Wayne when prose needs in-voice source naming added to satisfy Layer 1.
- Escalate to Stephen when a referenced slug doesn't exist (card creation needed).
- Escalate to xaiolai when a chapter has 5+ over-length brackets — a structural sign that the chapter's source-naming pattern needs rework, not just per-bracket fixes.
- Escalate to jerry-crew-chief before running `/compile-book` — broken slugs or verbose brackets will cause Chicago formatter to fail or produce mangled endnotes.

## Boundary-case recipes

1. **Auditing a chapter with the legacy verbose-bracket convention.**
   Expect many flags on the first pass. The chapter is pre-migration; normal. Wayne sweeps to convert each bracket to slug-only, moving citation metadata to the card (or verifying it's already there). Re-run audit after sweep.

2. **Auditing a chapter with a `[CITE: slug — pending-stephen-lock]` marker.**
   Verify slug exists and suffix syntax is exact. The pending suffix is permitted and signals deferred Stephen verification, not an audit failure.

3. **Auditing a multi-slug bracket (e.g., 5 slugs separated by `;`).**
   Permitted if all slugs resolve and the load-bearing claim genuinely requires multiple sources. Length cap may be exceeded with reason documented.

4. **Auditing a chapter against a corpus with deleted slugs.**
   If a card was renamed or deleted in the source-ledger, the chapter's slug references break. Hard fail per "card existence" check. Route to joe + Stephen for ledger-sync.

5. **Auditing during the migration sweep (Wayne dispatching per-chapter conversion).**
   Acceptable to run cite-density-audit on an interim chapter state showing reduced (not zero) findings. The audit's job is to track progress, not to fail-stop mid-migration.

## Output format

```text
Owner: cite-density-audit (skill run by <joe|stephen|wayne>)
Task: Audit inline [CITE:] brackets in <path-or-corpus> against rule 13.
Inputs reviewed:
  - <chapter file(s)>
  - book/evidence/source-ledger/cards/ (for slug existence check)
  - .claude/rules/13-citation-form.md
Output: cite-density-audit memo at process/audits/<n>-<slug>-cite-density-audit.md
Evidence grade: N/A
Assumptions: <e.g., slug pattern is lowercase-kebab-case-with-digits>
Open questions: <slugs awaiting Stephen card creation; brackets requiring Wayne in-prose addition>
Risks: <chapters that would fail /compile-book due to broken slugs>
Handoff: <wayne for prose / stephen for card creation / joe for compile go/no-go>
```

Findings table:

| Chapter | Line | Issue type | Snippet | Suggested fix |
|---|---|---|---|---|

Summary row: `total brackets / valid / over-length / verbose-content / broken-slug / pending-lock`.

## Examples

<example>
Context: ch-06 has the Nielsen tweet bracket post-Stephen catch-up; Wayne hasn't migrated yet to slug-only convention.

A: "cite-density-audit for ch-06: 14 brackets scanned, 1 over-length + verbose-content at L31 (Nielsen tweet, 207 chars including 'reproduced verbatim in contemporaneous tier-1 reporting (AP, Reuters, NYT, WaPo, June 17-18, 2018)'); slug for card 'nielsen-tweet-no-policy-2018-06-17' exists. Fix: replace bracket with [CITE: nielsen-tweet-no-policy-2018-06-17]; verify Layer-1 in-prose source naming includes speaker, venue, date (current prose at L29 already names 'the Secretary of Homeland Security' but does not name Nielsen; add 'Kirstjen Nielsen' to the prose before the quote). Routes: Wayne for prose + bracket replacement."
<commentary>
Real audit pattern: one over-length bracket caught by the scanner, slug verified to exist, Wayne gets specific fix instructions including Layer-1 addition. This is the Nielsen example the rule was written to prevent recurring.
</commentary>
</example>

<example>
Context: Stage 3 pre-compile audit across all 12 active chapters before running /compile-book.

A: "cite-density-audit corpus-wide: 287 brackets scanned. 198 valid (slug-only). 43 over-length but valid-content (multi-slug brackets in ch-04, ch-08 procedural-citation paragraphs; document as exceptions). 31 over-length AND verbose-content (legacy form, sweep candidates; concentrated in ch-02, ch-06, ch-08, ch-12). 12 broken-slug references (chapters cite slugs not yet in source-ledger; route to Stephen for card creation). 3 pending-stephen-lock markers (ch-09 L122 wd-sd-tex; ch-12 L93 walsh; ch-12 L19 black) — permitted per rule 13. Recommend: complete migration sweep on the 31 verbose-content brackets and create the 12 missing cards before /compile-book. Compile would currently fail on the 12 missing slugs."
<commentary>
This is the corpus-wide pre-compile audit pattern. The skill produces an actionable manifest for jerry-crew-chief to triage before manuscript export.
</commentary>
</example>

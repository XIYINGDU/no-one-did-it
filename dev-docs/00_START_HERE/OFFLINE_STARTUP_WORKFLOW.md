# Offline Startup Workflow

All paths are project-root-relative.

## Day 1: establish the spine

1. Open `dev-docs/01_BOOK_PREPARATION_DECKS/extracted/book_prep_package/Audit_Memo.md`.
2. Review the corrected taxonomy.
3. Open the three PowerPoint decks in order:
   - `dev-docs/01_BOOK_PREPARATION_DECKS/extracted/book_prep_package/01_Strategy_and_Audit_Deck.pptx`
   - `dev-docs/01_BOOK_PREPARATION_DECKS/extracted/book_prep_package/02_Historical_Case_File_Deck.pptx`
   - `dev-docs/01_BOOK_PREPARATION_DECKS/extracted/book_prep_package/03_Narrative_and_Chapter_Deck.pptx`
4. Write a one-page book spine in your own words.

## Day 2: choose the first 12 cases

1. Open `dev-docs/02_RESEARCH_PACKAGES/extracted/responsibility_laundering_research_packages/master_case_matrix.csv`.
2. Select:
   - 4 primary historical cases,
   - 3 war/statecraft cases,
   - 3 AI/current-technology cases,
   - 2 political/public-administration cases.
3. For each, fill or update a case card using `.claude/docs/case-card-template.md` and store under `book/case-files/`.

## Day 3: activate the Claude workspace

The crew workspace is already in place at the project root — no copy step
needed. The snapshot under
`dev-docs/03_CLAUDE_AI_CREW_WORKSPACE/extracted/responsibility-laundering-book-ai-crew/`
is provenance only.

1. From the project root (`books/responsibility_laundering/`), start Claude Code.
2. Review `CLAUDE.md` and `.claude/docs/crew-operating-manual.md`.
3. Run `/agents` and `/hooks` to inspect the crew and project hooks.
4. Use the crew agents only after the book spine and first 12 cases are fixed.

## Standing rule

Do not add another case unless it performs a defined narrative function:

- proves a new mechanism;
- sharpens a contrast;
- supplies a dramatic scene;
- tests the framework against a hard counterexample;
- connects ancient substitution to a current institution.

# Artifact Manifest

All paths are project-root-relative (begin with `dev-docs/`).

## `dev-docs/01_BOOK_PREPARATION_DECKS/`

Contains the original book-preparation ZIP, extracted deck package, and image previews of the three strategy montages.

Key files (under `extracted/book_prep_package/`):

- `01_Strategy_and_Audit_Deck.pptx`
- `02_Historical_Case_File_Deck.pptx`
- `03_Narrative_and_Chapter_Deck.pptx`
- `Audit_Memo.md`
- `Offline_Workplan.md`
- `Source_Anchors.md`

Image previews (under `image_previews/`):

- `montage_strategy.png`
- `montage_cases.png`
- `montage_narrative.png`

Original ZIP: `original_zip/responsibility_laundering_book_prep.zip`.

## `dev-docs/02_RESEARCH_PACKAGES/`

Contains the full research package built from the recent extended investigations.

Key files (under `extracted/responsibility_laundering_research_packages/`):

- `master_case_matrix.csv`
- `master_case_matrix.json`
- `source_ledger_master.csv`
- Per-domain packets:
  - `00_Methodology/`
  - `01_War_Ukraine_Iraq/` — case matrix, case cards, source ledger, weaving notes.
  - `02_Trump_Administrations/` — case matrix, case cards, source ledger, weaving notes.
  - `03_AI_Competition/` — case matrix, case cards, source ledger, weaving notes.
  - `04_Book_Integration/` — book integration notes and cross-pattern matrix.

Original ZIP: `original_zip/responsibility_laundering_research_packages.zip`.

## `dev-docs/03_CLAUDE_AI_CREW_WORKSPACE/`

Snapshot of the Claude Code workspace structure for the AI crew. **The live
copy of these files is at the project root** (`CLAUDE.md`, `README.md`,
`.claude/`, `book/`); this folder is kept only as provenance of what was
originally shipped in the bundle.

Snapshot contents (under `extracted/responsibility-laundering-book-ai-crew/`):

- `CLAUDE.md`
- `README.md`
- `.claude/agents/`
- `.claude/skills/`
- `.claude/hooks/`
- `.claude/commands/`
- `.claude/rules/`
- `.claude/docs/`
- `.claude/settings.json`
- `book/chapters/`
- `book/case-files/`
- `book/source-ledger/`
- `book/proposals/`
- `book/review-memos/`
- `book/diagrams/`

Original ZIP: `original_zip/responsibility_laundering_claude_ai_crew_workspace.zip`.

## `dev-docs/04_ARCHIVE_SUPERSEDED_OR_REFERENCE/`

Contains an earlier Claude workspace ZIP and extracted version. Keep it only
for comparison/reference. The crew names (Maia Chen, Lucas Hart, Irene Walsh,
…) and rule numbering differ from the active workspace and must not be mixed.

## Important usage note

The bundle includes both original ZIPs and extracted copies. For working,
use the extracted folders. For transfer, use the original ZIPs. To verify
nothing has drifted, run:

```bash
shasum -a 256 -c dev-docs/00_START_HERE/checksums_sha256.txt
```

from the project root.

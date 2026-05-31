# Responsibility Laundering — Final Artifact Bundle

Generated: 2026-05-25 01:28:35
Relocated into `books/responsibility_laundering/dev-docs/`: 2026-05-25

This package consolidates the working artifacts created so far for the book
project. All paths in this folder are project-root-relative (i.e. they begin
with `dev-docs/`). The active Claude crew workspace was lifted from
`dev-docs/03_CLAUDE_AI_CREW_WORKSPACE/extracted/responsibility-laundering-book-ai-crew/`
to the project root; the copy under `dev-docs/03_…` is kept for provenance only.

## Recommended offline starting order

1. **`dev-docs/01_BOOK_PREPARATION_DECKS/`**
   Start with the three preparation decks and audit memos. These define the book concept, corrected taxonomy, core case architecture, and chapter/narrative strategy.

2. **`dev-docs/02_RESEARCH_PACKAGES/`**
   Use the master case matrix, source ledger, and focused research packages for Ukraine/Iraq, Trump administrations, and AI competition.

3. **`dev-docs/03_CLAUDE_AI_CREW_WORKSPACE/`** *(reference copy only)*
   The live workspace is already at the project root (`CLAUDE.md`, `README.md`, `.claude/`, `book/`). This folder retains the original ZIP and extracted copy as a snapshot.

4. **`dev-docs/04_ARCHIVE_SUPERSEDED_OR_REFERENCE/`**
   Contains an earlier Claude workspace variant (different crew names, different rule numbering). Treat it as reference only unless you specifically want to compare earlier agent structures.

## Core project rule

Responsibility belongs where **control, benefit, knowledge, and preventability** overlap.

## Core taxonomy

- **Pure scapegoat:** largely innocent actor blamed to close the case.
- **Partial scapegoat:** involved or guilty actor used to stop responsibility too low.
- **System/object alibi:** machine, market, legal entity, benchmark, file, model, or procedure used as blame container.
- **Cost-bearing goat:** victim or weak party forced to absorb harm while others avoid liability.

## Top-level folders (under project root)

```text
books/responsibility_laundering/
├── CLAUDE.md                # book constitution (active)
├── README.md                # crew workspace quick-start
├── .claude/                 # agents, skills, commands, rules, hooks (active)
├── book/                    # case files, chapters, source ledger, memos (active)
└── dev-docs/
    ├── 00_START_HERE/
    ├── 01_BOOK_PREPARATION_DECKS/
    ├── 02_RESEARCH_PACKAGES/
    ├── 03_CLAUDE_AI_CREW_WORKSPACE/   # snapshot; live copy is at project root
    └── 04_ARCHIVE_SUPERSEDED_OR_REFERENCE/
```

See `dev-docs/00_START_HERE/ARTIFACT_MANIFEST.md`,
`dev-docs/00_START_HERE/artifact_inventory.csv`, and
`dev-docs/00_START_HERE/checksums_sha256.txt` for detailed file tracking.
Checksums verify from the project root with
`shasum -a 256 -c dev-docs/00_START_HERE/checksums_sha256.txt`.

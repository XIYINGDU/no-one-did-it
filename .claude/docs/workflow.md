# Workflow

## Case-to-chapter pipeline

```text
Candidate event
  -> domain researcher case file
  -> source ledger
  -> responsibility-chain map
  -> fact-check audit
  -> red-team challenge
  -> legal-risk scan
  -> book-architecture placement
  -> narrative draft
  -> expert review
  -> final chapter revision
```

## Sprint rhythm

1. Monday: Jerry defines sprint and assigns owners.
2. Tuesday–Wednesday: researchers build source packets.
3. Thursday: Stephen fact-checks and Laura red-teams.
4. Friday: Bonnie turns approved packets into chapter briefs.
5. Weekend: Wayne drafts or revises prose.

## Required before drafting

A case is draft-ready only when it has:

- complete case file;
- evidence grade;
- source ledger;
- strongest counterargument;
- legal risk flag;
- book function.

## Chapter status + promotion gate

Chapter artifacts under `book/chapters-v2/` must declare YAML frontmatter:

```text
status: brief | draft | ready | gated
```

Gate behavior:

- `brief` and `draft`: chapter-rhythm gaps trigger warnings only.
- `draft -> ready` transition: missing chapter-rhythm sections trigger a deny decision in PostToolUse.
- `ready` with full chapter rhythm passes the gate.

## Command routing

All slash commands under `.claude/commands/` route through declared owner agents.
Command files must include `owner: <agent-id>` in frontmatter, and command execution must dispatch the owner agent first. Skills run inside owner agents, not directly at command level.

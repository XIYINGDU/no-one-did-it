# Audit History — versioned snapshots

Audit history archive maintained by `.claude/hooks/pre-edit-chapter-snapshot.py` per `.claude/rules/09-rewrite-lifecycle.md`. Before any rewrite-cycle edit overwrites a prior audit report, the prior report (plus the chapter file, sidecar, and treatment-class row) is snapshotted here.

## Directory layout

```text
book/audits/history/
  <n>/                                # chapter number (no zero-padding to match chapter filenames)
    <ISO-timestamp>/                  # 2026-05-27T14-30-00Z format
      <n>-<slug>.md                   # chapter file at snapshot time
      <n>-<slug>.contract.yml         # contract file at snapshot time (if applicable)
      audit-chapter.md                # prior /audit-chapter report
      evidence-audit.md               # prior /evidence-audit report
      fair-clue-audit.md              # prior /fair-clue-audit report
      defamation-wording.md           # prior defamation-wording memo
      contract-audit.md               # prior /contract-audit report (if class >= structural-polish)
      implication-audit.md            # prior /implication-audit report
      voice-register-audit.md         # prior /voice-register-audit report (if class >= structural-polish)
      treatment-classes.snapshot.yml  # treatment-classes.yml at snapshot time
```

## Retention

Snapshots are **never deleted** during a rewrite cycle. They are the rollback unit: a failed rewrite restores the chapter from the most recent snapshot directory plus the corresponding chapter file from git history.

After a rewrite cycle closes (the chapter promotes back to `status: ready` and stays there for one full sprint), snapshot directories older than the final accepted snapshot may be pruned by hand — but the final accepted snapshot stays forever, as the canonical "this is what the chapter looked like before this rewrite cycle" record.

## Comparison

To compare current state vs a snapshot:

```bash
diff -u book/audits/history/02/2026-05-27T14-30-00Z/audit-chapter.md \
        book/audits/02-the-four-goats-audit-chapter.md
```

For chapter-level diff, prefer `git diff` against the commit just before the rewrite cycle began.

## Authority

- `pre-edit-chapter-snapshot.py` writes snapshots automatically.
- Manual snapshots are permitted but discouraged — the hook ensures consistency.
- Snapshot deletion requires `jerry-crew-chief` sign-off and a recorded reason; rule 09's audit-trail integrity depends on snapshots being present.

See `.claude/rules/09-rewrite-lifecycle.md` for the full lifecycle policy.

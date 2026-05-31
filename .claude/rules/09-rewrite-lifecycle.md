---
description: "Rewrite lifecycle rule: a chapter under rewrite transitions through declared states (ready, in-rewrite, in-review). Prior audit reports archive before new audits run; source-ledger sidecars carry as_of versioning. Enforced by pre-edit-chapter-snapshot.py and post-edit-status-check.py."
---

**A chapter under rewrite transitions through declared states; prior audit reports archive before new audits run; source-ledger sidecars are versioned with the chapter version they correspond to.**

# Rewrite Lifecycle Rule

**Scope:** binds every chapter in `book/chapters-v2/` that enters the fiction-craft rewrite cycle, and the audit + sidecar artifacts under `process/audits/`, `book/evidence/source-ledger/`, and `process/review-memos/` that reference those chapters.

## Status flow during rewrite

A chapter's `status:` field (front-matter) follows this state machine while under rewrite:

```text
ready
  └─→ in-rewrite      (declared when chapter-defect-diagnose runs + treatment class assigned)
        └─→ in-review (declared when wayne completes the rewrite pass)
              └─→ ready (re-promoted only after the audit set for the assigned treatment class passes)
              └─→ in-rewrite (re-opened if any audit fails or laura/nancy veto)
```

Transitions:

- `ready → in-rewrite` requires the chapter's treatment class to exist in `book/registries/treatment-classes.yml` per rule `08-treatment-class-discipline.md`. Pure `no-change` chapters do not transition; they remain `ready`.
- `in-rewrite → in-review` requires the rewrite pass to be complete and the per-chapter contract (if applicable to the treatment class) to be satisfied per `/contract-audit`.
- `in-review → ready` requires the full audit set for the declared treatment class to pass green. Re-promotion is blocked by `check-agent-frontmatter.py` if the chapter still carries rhythm-section gaps or rule-07 unresolved warnings.
- Reverting `in-review → in-rewrite` requires a recorded reason in the chapter's audit history.

## Audit history archival

Before any new audit overwrites a prior audit report, the prior report is snapshotted to `process/audits/history/<n>/<ISO-timestamp>/`. The snapshot is the responsibility of the `pre-edit-chapter-snapshot.py` hook; manual rewrites must not skip this.

Directory layout:

```text
process/audits/history/
  02/
    2026-05-27T14-30-00Z/
      audit-chapter.md
      evidence-audit.md
      fair-clue-audit.md
      defamation-wording.md
      contract-audit.md            (if treatment class is structural-polish or higher)
      implication-audit.md         (always)
      callback-audit-touch.md      (per-chapter slice of book-level callback audit)
      treatment-class.snapshot.yml (chapter's row from treatment-classes.yml at snapshot time)
    2026-06-04T09-15-00Z/
      ...
```

Snapshots are never deleted during the rewrite cycle. They are the rollback unit: a failed rewrite restores the chapter from the most recent snapshot directory plus the corresponding `book/chapters-v2/<n>-*.md` from git history.

## Source-ledger sidecar versioning

Source-ledger sidecars (`book/evidence/source-ledger/<n>-<slug>.yml`) hold the cite-anchor table for each chapter. When a chapter rewrite adds, removes, or relocates `[CITE:]` anchors, the sidecar must be updated in the same commit. Sidecars carry an `as_of:` field tracking the chapter version they correspond to:

```yaml
chapter: 02
slug: the-four-goats
as_of: 2026-06-04          # ISO date; matches the chapter's last edit date
chapter_status: in-review  # mirrors the chapter's status at sidecar update time
anchors:
  - cite_id: CITE_02_001
    ...
```

A chapter cannot return to `status: ready` if its sidecar's `as_of:` is older than the chapter's most recent content edit. The `post-edit-status-check.py` hook flags the mismatch.

## Review-memo and case-file invalidation

Rewrites can invalidate review memos and case-file derivations that referenced specific paragraphs. The chapter's defect-map (`process/defect-map/<n>-<slug>.md`) declares which downstream artifacts are touched:

```yaml
invalidates:
  - process/review-memos/02-stephen-fact-check.md     # references paragraph-specific line numbers
  - process/review-memos/02-laura-red-team.md
preserves:
  - book/evidence/case-files/02-*.md                         # case-file dossier remains stable
```

Invalidated review memos must be re-run after the chapter returns to `in-review` and before it returns to `ready`. Preserved artifacts do not need re-validation; rule `09` reads them as load-bearing-stable.

## Treatment-class-specific lifecycle additions

- `prose-polish`: no contract file required; snapshot still required; sidecar versioning still required.
- `defamation-safe-tighten`: nancy must explicitly clear; review-memo update required.
- `structural-polish`: contract file required; cross-chapter audits required; motif/callback/cognitive-arc registries updated.
- `full-craft-rewrite`: all of the above plus laura red-team and nancy clock; pilot Gate B equivalent required for re-promotion.

<example>
Chapter 07 (`structural-polish`) walks the full lifecycle:

1. **`ready` (2026-05-26).** Chapter has been at `ready` since the original chapter-production pipeline closed.
2. **`ready → in-rewrite` (2026-06-04).** `chapter-defect-diagnose` runs; defect-map cites V6 + V10 defects; treatment class `structural-polish` is appended to `book/registries/treatment-classes.yml`. The `pre-edit-chapter-snapshot.py` hook fires on the first edit, copying current audits into `process/audits/history/07/2026-06-04T09-15-00Z/` (including `contract-audit.md` and `implication-audit.md`). The chapter contract file is built at `book/chapters-v2/07-the-clean-record.contract.yml`.
3. **Mid-rewrite.** Bonnie reorders scenes for V6; Wayne re-renders three paragraphs for V10. Three new `[CITE:]` anchors are added; the sidecar `book/evidence/source-ledger/07-the-clean-record.yml` is updated in the same commit with `as_of: 2026-06-04` and the new anchor rows. The defect-map declares `invalidates: [process/review-memos/07-laura-red-team.md]` and `preserves: [book/evidence/case-files/07-*.md]`.
4. **`in-rewrite → in-review` (2026-06-04, later).** Wayne's pass closes; `/contract-audit` verifies the per-chapter contract's `feels:` and `primed_for:` slots are still delivered. The invalidated Laura red-team memo is re-run; the preserved case-file dossier is not touched.
5. **`in-review → ready` (2026-06-04, later).** The class-specific audit chain (callback + motif + cognitive-arc + dependency + contract + implication + voice-register) runs green. `post-edit-status-check.py` verifies the sidecar's `as_of` matches the chapter's last edit date. `check-agent-frontmatter.py` clears re-promotion. Status returns to `ready`.

If any of those audits had failed, the chapter would have reverted to `in-rewrite` with a recorded reason, and the next edit would have generated a new snapshot directory rather than overwriting `2026-06-04T09-15-00Z/`.
</example>

## Why this rule exists

The plan critiqued by Codex (D2#1 Blocker) had no migration story for `[EVIDENCE NEEDED]` markers, audit history, sidecars, or review memos. Without rule 09, a rewrite cycle silently overwrites prior audit work and breaks the chain of custody on cite-anchors. With rule 09, every step of a chapter's rewrite is recoverable and every downstream artifact knows whether it is current or stale.

This rule is enforced by `pre-edit-chapter-snapshot.py` (block-mode after pilot calibration), `post-edit-status-check.py` (warn-mode), and the `check-agent-frontmatter.py` chapter-promotion gate.

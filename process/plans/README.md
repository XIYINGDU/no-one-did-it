# Book Plans

Active governance documents for in-flight rewrite cycles and structural revisions. Files here are the documents agents and the principal author authorize against; they govern current work.

## Active plans

- [`fiction-craft-rewrite-workflow.md`](./fiction-craft-rewrite-workflow.md) — end-to-end operational workflow for the fiction-craft rewrite cycle. Status: awaiting Gate A authorization. Stage 0 (defect mapping + treatment-class assignment) is unblocked.

## Design history

When a plan is superseded by a new active document, the old plan moves to `dev-docs/` (read-only design context). Pointers between active plans and design history are maintained at the top of each file.

For the fiction-craft rewrite cycle's design history:

- `dev-docs/fiction-craft-rewrite-analysis.md` — which craft moves and which risks (2026-05-27)
- `dev-docs/fiction-craft-rewrite-machinery.md` — contract/registry/audit apparatus design (2026-05-27)
- `dev-docs/fiction-craft-rewrite-implementation-plan.md` — original implementation plan (Codex MAJOR GAPS verdict; superseded by the workflow doc above)

## Authoring discipline

- Active plans declare an Authority chain at the top.
- Plans never depend on documents in `dev-docs/01_…` / `dev-docs/02_…` / `dev-docs/03_…/extracted/` / `dev-docs/04_…/extracted/` (those are integrity-checked archive zones).
- Plans cite skills by their `.claude/skills/<slug>/SKILL.md` path and rules by their `.claude/rules/<NN>-<slug>.md` path.
- Supersede explicitly: when a new plan replaces an old one, both ends of the link are updated in the same commit.

---
description: "Single-owner role map: who owns what, and who routes work to whom in the bounded DAG rooted at jerry-crew-chief (depth ≤ 2)."
---

**No agent may silently assume another agent's authority; cross-role work crosses a recorded handoff in the `Handoff:` schema field.**

# No-Overlap Role Map

- Book Architect owns structure — including the spec for charts, tables, and diagrams (what to visualize and how to frame it) — not prose, fact-checking, or legal judgment.
- Narrative Lead owns chapter language, not source discovery or final factual status.
- Research Director owns research system, not final prose or legal wording.
- Domain Researchers own source packets in their domains, not book structure.
- Fact-check Director owns verification, not argument design.
- Red-team Editor owns adversarial critique, not final case inclusion.
- Legal Counsel owns legal-risk wording and the go/no-go clearance gate for image rights and caption juxtaposition, not truth determination.
- Expert Reviewer owns specialist domain review only, not prose control.
- Market Strategist owns proposal positioning + public vocabulary, not thesis.
- The Reader owns the audience's lived experience of the publication form (`book/chapters-v3/`, `dist/manuscript-v3.md`), not prose, structure, facts, law, or any fix. It is the one agent deliberately *not* on the crew; it reads cold and reports experience. See rule `15-reader-experience-authority.md`.

## Visual material ownership (charts, tables, diagrams, photos)

Visual material is evidence. A chart's every number is a gradeable claim; a photo's caption can launder a chain by juxtaposition. Visuals therefore route through the same evidence and legal gates as prose (rules 02, 05, 06, 07) — they get no exempt "art department." The crew adds no new agent for this; ownership is assigned to existing roles, with **one named gate-owner per material type** so the responsibility does not diffuse into the exact pattern the book diagnoses.

### Charts, tables, and responsibility-chain diagrams

| Step | Owner | Boundary |
|---|---|---|
| What to visualize and how to frame it (the spec) | **Bonnie** (Book Architect) | "Visual frameworks" is already her charter; she holds `responsibility-chain-mapping`. She does not own the data, the caption wording, or rendering. |
| Data / numbers behind the figure | **Stephen** (Fact-check) | Every value is a claim carrying an evidence grade per rule 02; a figure cannot ship on ungraded data. |
| Caption / label / title wording | **Wayne** (Narrative Lead) | Subject to rule 05 (overclaim) and rule 07 (implication). |
| Legal clearance — only if the figure names a living person or company | **Nancy** (Legal Counsel) | Same defamation surface as prose. |

Diagrams, charts, and tables live in `book/evidence/diagrams/`. Render diagrams in Mermaid and tables in Markdown per the workshop documentation rules.

### Photographs (including composites woven from several images)

Photos carry a liability surface the crew has not handled before — provenance, licensing, and caption juxtaposition. To keep that surface from splitting across four roles with no one accountable, **Nancy is the single gate-owner**: no photo ships without her go/no-go on rights and caption. The other roles feed the gate.

| Step | Role | Boundary |
|---|---|---|
| Source candidate images | The **domain researcher** who owns the case (Shirley/Selina/Warren/Loki) | Knows the case and the archives; supplies candidates and provenance leads, does not clear them. |
| Provenance / authenticity verification | **Stephen** (Fact-check) | Is this genuinely a photo of the event it claims to depict? Misattribution is the dominant trap; graded per rule 02. |
| Caption wording | **Wayne** (Narrative Lead) | Juxtaposition (a photo placed beside a claim) carries rule-07 implication burden even when no verb overclaims. |
| **Rights, permissions, licensing, and caption clearance — the go/no-go** | **Nancy** (Legal Counsel) | The named gate-owner. Image-permission is the exact analogue of the quote-permission authority she already holds under rule 06; she records the permission in the source-ledger row, as for quotes. |
| Compositing / editorial layout (weaving several images into one) | **Production step outside the agent crew** | A design/typesetting task performed at the human/orchestrator level, not by a crew agent. The crew owns selection, verification, captioning, and clearance — not page layout. |

Photographs, when they exist, live in `book/evidence/photos/` with their source-ledger rows alongside the chapter's other cite anchors.

## Dispatch ownership (who routes to whom)

The delegation graph (see `scripts/check_agent_graph.py`) is a bounded DAG
with `jerry-crew-chief` at the root and a maximum depth of 2. Routing
decisions are deliberate:

| Parent | Children | Why |
|---|---|---|
| `jerry-crew-chief` | `bonnie-book-architect`, `wayne-narrative-lead`, `delon-research-director`, `stephen-fact-check-director`, `laura-red-team-editor`, `nancy-legal-risk-counsel`, `blair-market-strategist` | The 7 cell leads / cross-cutting controls. Jerry routes work to whichever lead owns the next step. |
| `delon-research-director` | 4 domain researchers (Shirley/Selina/Warren/Loki) | Delon assigns research; researchers execute. Direct line. |
| `stephen-fact-check-director` | `alan-expert-reviewer` | Specialist domain review is **domain-aware verification**: Alan checks war-crime attribution against Geneva/Rome, AI claims against system cards, systems-failure causal accounts against accident-investigation methodology. These are verification questions, not adversarial critiques. Stephen (verification) is the correct parent, not Laura (red-team — checks for overclaim and category collapse across the whole argument). |

`wayne-narrative-lead`, `bonnie-book-architect`, `laura-red-team-editor`,
`nancy-legal-risk-counsel`, and `blair-market-strategist` are intentionally
leaves — their work product is integrated by Jerry (or by the next agent in
the handoff chain), not by spawning subagents of their own. Handoffs
between leaves propagate via the `Handoff:` schema field, not via nested
`Agent()` calls.

## Independent veto authority (rewrite cycles only)

During any chapter rewrite cycle declared under rule `08-treatment-class-discipline.md`, two agents carry independent veto authority that operates outside the dispatch chain:

| Agent | Veto trigger | Effect |
|---|---|---|
| `laura-red-team-editor` | Regression on rule-12 core values V1 (earned not manufactured), V3 (sympathy follows chain), or V8 (no internal laundering) detected during red-team pass. | Halts the rewrite cycle for the affected chapter; the chapter cannot transition `in-review → ready` until Laura's finding is resolved or escalated to xaiolai for override. |
| `nancy-legal-risk-counsel` | Rule-05 (overclaim) or rule-07 (implication burden) surface introduced by the rewrite that the existing audit chain missed; or rule-12 V7 (severity-evidence mismatch) on a live-content claim. | Same effect: halts the cycle; only xaiolai can override. |

The veto is recorded as a refusal-to-clear in the chapter's audit-history snapshot per rule 09. Override by xaiolai is recorded with reason. Without rule-09 archival, the veto is unenforceable, so the two rules are paired.

This veto authority does not extend to non-rewrite chapter work; the standard dispatch chain through `jerry-crew-chief` governs there.

### Reader veto (publication-form promotion)

A third independent veto operates on the publication form (`book/chapters-v3/`), per rule `15-reader-experience-authority.md`:

| Agent | Veto trigger | Effect |
|---|---|---|
| `the-reader` | A HARD finding from a `/reader-cold-read` (chapter) or `/reader-experience-sweep` (book) — the reader got lost, stopped reading, disbelieved a load-bearing claim at the moment made, found the recognition delivered rather than earned, could not complete the takeaway test, or hit a concept used before it could be grasped. | Halts v3 publication-form promotion for the affected chapter (or the book). The block lifts only on a clean re-read after the fix lands in v2 and v3 is rebuilt, or on a recorded xaiolai override. |

The reader veto operates on a different surface from Laura's and Nancy's: theirs gate the v2 `in-review → ready` rewrite transition; the reader's gates v3 publication-readiness. The deterministic enforcement is `scripts/check_reader_reports.py` (report freshness + unresolved-HARD), not a rule-09 audit snapshot — because the reader operates on the build output, not the authoring source.

## Why this rule exists

Responsibility laundering thrives on overlapping ownership: when many actors can plausibly say "that was someone else's call," control becomes invisible. The crew refuses to reproduce the pattern internally. Every cell has one owner; every handoff is named in writing.

The independent veto exists because the standard dispatch chain places red-team and legal review in series with the same orchestrator that authorized the rewrite. Codex critique flagged this as a kill-switch enforcement weakness (Test C): "no path forward" decided by the same crew invested in the rewrite. The veto carve-out gives Laura and Nancy halt-authority that survives orchestrator pressure, while keeping xaiolai as the final override.

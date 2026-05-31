Owner: callback-audit (bonnie)
Task: Baseline /callback-audit on populated book/callback-graph.yml
Inputs reviewed: book/callback-graph.yml (22 edges); book/chapters-v2/*.md
Output: this memo
Evidence grade: N/A
Assumptions: anchor substring match = pass; near-miss = drifted; absent = missing
Open questions:
  - hofeller-files-posthumous-custody: payoff phrasing drifted from "(2018–2019; ch-6 anchor)" to "(2018–2019; ch-6 slot 5)" — confirm with bonnie whether YAML anchor or ch-12 prose is canonical.
Risks:
  - hofeller-files-posthumous-custody (required:true) — payoff anchor drifted; one-word fix.
Handoff: bonnie (anchor refresh on 1 drifted required edge) → joe (regression watch on next rewrite)

## Findings table

| edge_id | plant | payoff | required | action |
|---|---|---|---|---|
| altar-moves-bookframe | pass | pass | Y | pass |
| two-goats-opening-image | pass | pass | Y | pass |
| four-category-taxonomy-install | pass | pass | Y | pass |
| eight-question-diagnostic-install | pass | pass | Y | pass |
| diagnostic-climbs-one-floor-higher | pass | pass | Y | pass |
| boeing-737-max-partial-scapegoat-layer | pass | pass | Y | pass |
| bhopal-anderson-layered-rereading | pass | pass | Y | pass |
| five-role-conflation-rule | pass | pass | Y | pass |
| record-is-first-anti-laundering-rule | pass | pass | Y | pass |
| therac-25-artifact-layer-callback | pass | pass | Y | pass |
| mh17-state-layer-callback | pass | pass | Y | pass |
| abu-ghraib-chain-of-command-callback | pass | pass | Y | pass |
| ukrainian-children-civilian-invisibility-callback | pass | pass | Y | pass |
| eo-13328-vs-inquiries-act-design-contrast | pass | pass | Y | pass |
| design-rule-needs-record-discipline | pass | pass | Y | pass |
| signature-is-the-seam-rule | pass | pass | Y | pass |
| signature-seam-ai-stack | pass | pass | Y | pass |
| three-record-demand-ai-stack | pass | pass | Y | pass |
| walsh-iran-contra-cover-up-callback | pass | pass | Y | pass |
| hofeller-files-posthumous-custody | pass | drifted | Y | refresh payoff anchor (YAML expects "(2018–2019; ch-6 anchor)"; ch-12 line 134 carries "(2018–2019; ch-6 slot 5)") |
| recognition-without-method-payoff | pass | pass | N | pass |
| beat10-moves-to-crosswalk | pass | pass | Y | pass |

## Summary

- Plant passes: 22/22
- Payoff passes: 21/22
- Drifted: hofeller-files-posthumous-custody (payoff phrase changed from "ch-6 anchor" to "ch-6 slot 5")
- Missing: none
- Required edges in trouble: hofeller-files-posthumous-custody

## Recommended actions

- One-line anchor refresh on `hofeller-files-posthumous-custody`: either update `book/callback-graph.yml` payoff `line_anchor` to `"(2018–2019; ch-6 slot 5)"` to match prose, or update ch-12 line 134 prose back to `"(2018–2019; ch-6 anchor)"` to match YAML. Bonnie's call which side is canonical.
- No structural action required; all 22 plants and 21 payoffs are intact. Baseline is healthy.
- Schedule next callback-audit on first rewrite of any chapter in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} per rule 09 (every chapter is graph-touching).

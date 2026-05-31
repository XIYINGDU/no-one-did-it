# Agent Tool Grants

This registry records role-based tool grants and explicit denials.

## Targeted additions

- `laura-red-team-editor`: granted `WebSearch` and `WebFetch` for adversarial evidence retrieval and counterexample sourcing.
- `delon-research-director` and the 4 domain researchers: granted `WebSearch` and `WebFetch` for primary-source retrieval.
- `stephen-fact-check-director` and `nancy-legal-risk-counsel`: granted `WebSearch` and `WebFetch` for verification + legal-status checks.
- `blair-market-strategist`: granted `WebSearch` and `WebFetch` for comp-title and market research.
- `alan-expert-reviewer`: granted `WebSearch` and `WebFetch` for domain-authority lookups.

## Role-weighted maxTurns policy

**Model policy:** all 13 agents run on `opus` (per Principal Author directive: logic-laden tasks require the larger model). The table below specifies turn budgets only; model is uniform.

Turn budgets are weighted by orchestration depth and expected decision load, not by status rank.

| Role group | Agents | maxTurns | Rationale |
|---|---|---|---|
| Crew chief | `jerry-crew-chief` | 40 | Owns cross-cell sequencing, conflict resolution, and final handoff routing. |
| Core leads/directors | `bonnie-book-architect`, `wayne-narrative-lead`, `delon-research-director`, `stephen-fact-check-director`, `laura-red-team-editor` | 25 | Multi-step planning/revision loops with repeated evidence and counterargument gates. |
| Strategic/legal controls | `nancy-legal-risk-counsel`, `blair-market-strategist` | 20 | Medium-depth synthesis with bounded artifact surfaces and explicit gate points. |
| Researchers | `shirley-historical-case-researcher`, `selina-war-statecraft-researcher`, `warren-ai-technology-researcher`, `loki-public-law-politics-researcher` | 18 | Source packet build and case file support need iterative retrieval but narrower authority. |
| Expert reviewer | `alan-expert-reviewer` | 18 | Parameterized across six domain frames; needs room to do real source-checking inside any one frame. |
| Principal author surrogate | `xiaolai` | 20 | Judgment surrogate; applies the Six Values-Over-Rules to escalated crew decisions. Bounded because his calls should be tight; if a judgment runs long, it likely needs to surface to the actual principal rather than be argued through. |
| The reader | `the-reader` | 22 | Cold-reads a full publication-form chapter (or the assembled manuscript) start-to-finish and produces a friction report across seven axes. Needs room to read deeply and report carefully, but does not orchestrate or fix. Deliberately *not* one of the 13 crew agents — it embodies the audience. |

## No Bash/TodoWrite policy

Rationale for all agents listed below: keep execution and task-list mutation centralized at the top-level orchestrator session to minimize destructive surface area and hidden side effects.

| Agent ID | Bash | TodoWrite | Rationale |
|---|---|---|---|
| `jerry-crew-chief` | no | no | Centralized shell/task execution remains outside subagents; handoff via schema fields only. |
| `bonnie-book-architect` | no | no | Same policy; architecture guidance does not require direct shell/task-list writes. |
| `wayne-narrative-lead` | no | no | Same policy; prose drafting uses repository files only. |
| `delon-research-director` | no | no | Same policy; research orchestration routes through artifacts and handoffs. |
| `shirley-historical-case-researcher` | no | no | Same policy; researcher outputs are document artifacts, not shell workflows. |
| `selina-war-statecraft-researcher` | no | no | Same policy; researcher outputs are document artifacts, not shell workflows. |
| `warren-ai-technology-researcher` | no | no | Same policy; researcher outputs are document artifacts, not shell workflows. |
| `loki-public-law-politics-researcher` | no | no | Same policy; researcher outputs are document artifacts, not shell workflows. |
| `stephen-fact-check-director` | no | no | Same policy; fact-check decisions are recorded in memos and ledgers. |
| `laura-red-team-editor` | no | no | Same policy; receives web tools only for adversarial sourcing. |
| `nancy-legal-risk-counsel` | no | no | Same policy; legal review remains document-based. |
| `alan-expert-reviewer` | no | no | Same policy; specialist review outputs are memos only. |
| `the-reader` | no | no | Same policy; the reader reads cold and writes one friction report per pass. Granted only Read/Grep/Glob/Write — no Bash, no TodoWrite, no Agent (it is a leaf and never dispatches), no web tools (it reads only the publication form already on disk). |
| `blair-market-strategist` | no | no | Same policy; proposal/audience work is document-based. |
| `xiaolai` | no | no | Same policy; the principal-author surrogate judges and records decisions in memos, never shell or task-list mutations. |

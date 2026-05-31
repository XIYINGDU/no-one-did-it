---
name: taxonomy-classification
description: Classify an event into the project's 4 canonical case categories (pure scapegoat / partial scapegoat / system-or-object alibi / cost-bearing goat) by walking diagnostic questions per category. Used by researchers, Bonnie, and Alan whenever a case's category is in dispute or not yet assigned.
version: 1.0.0
---

# Taxonomy Classification

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Decision rubric

Run the 4 diagnostic blocks in order. The first block that returns a clean "yes" is the case's category. If multiple blocks return yes, the case is a **hybrid**; surface it explicitly rather than picking one silently.

### Block 1 — Pure scapegoat

Yes if ALL the following hold:
- The publicly blamed actor is substantially innocent or unrelated to the harm.
- No documented evidence places the blamed actor in the control / benefit / knowledge / preventability chain.
- The blame assignment served someone or something else (named or inferable).
- The actor's punishment / exile / reputational destruction is documented.

If yes → **pure scapegoat**. Stop.

### Block 2 — Partial scapegoat

Yes if ALL the following hold:
- The publicly blamed actor IS culpable at least at the execution level — they really did the thing they're punished for, or were genuinely in the chain.
- But the attribution stops at this actor and prevents responsibility from climbing.
- At least one upstream actor (designer / commander / executive / beneficiary / regulator) had MORE control or knowledge but faces less consequence.
- The stopping is documented (a named decision-maker chose to halt the chain, or an institutional process closes the case at this actor).

If yes → **partial scapegoat**. Stop.

### Block 3 — System / object alibi

Yes if ALL the following hold:
- A non-human cause (tool, machine, algorithm, benchmark, corporation, legal entity, committee, market, procedure, model) is publicly named as the cause of the harm.
- That named cause has plausible mechanistic involvement (i.e., the system did contribute — the alibi is not pure fabrication).
- BUT the human actors who built, deployed, approved, or profited from the system face less or no public attribution.
- The system's "agency" is reified in coverage and accountability discourse (it is described as having "decided", "failed", "caused", etc.).

If yes → **system/object alibi**. Stop.

### Block 4 — Cost-bearing goat

Yes if ALL the following hold:
- A person or group absorbs the harm (death, injury, reputational damage, economic loss, exile, surveillance burden, deportation, displacement, prosecution).
- That party is NOT publicly accused of causing the harm.
- The party absorbs the cost while the actual responsibility-holders avoid or minimize their share.
- The cost-bearing is documented and disproportionate to the party's role in the chain.

If yes → **cost-bearing goat**. Stop.

### No-match: not a responsibility-laundering case

If none of the 4 blocks return a clean yes, the case is NOT a responsibility-laundering case under this book's taxonomy. Do not force-fit. Hand off to Bonnie with the diagnostic results; she decides whether to widen the book's scope, narrow the case, or drop it.

## Conflict handling

1. **Multiple blocks return yes (hybrid case):**
   Name both categories explicitly in the case file: "primary: partial scapegoat / secondary: system/object alibi". The chapter must address both layers. Do not pick one silently.
2. **The "control / benefit / knowledge / preventability" evidence is missing:**
   The case cannot be classified. Cap evidence grade at C, route to the domain researcher (Shirley / Selina / Warren / Loki per domain) to find the missing chain evidence, do not advance to chapter brief.
3. **Public blame and actual responsibility overlap fully (no laundering):**
   This is normal accountability working as designed. Not a case for this book. Document and decline.
4. **The blamed actor disputes their classification publicly (e.g., a partial scapegoat insists they are a pure scapegoat):**
   The actor's self-classification is one input; documented chain evidence overrides self-report. Stephen verifies the chain evidence; classification follows the evidence.

## Escalation conditions

- Escalate to Alan (responsibility-theory frame) when the conceptual distinction between two categories blurs (e.g., partial scapegoat shading into system/object alibi as institutional layers thicken).
- Escalate to Laura (red-team) when a classification feels too clean — Laura tests whether the "stopping" in partial scapegoat is really documented or just narratively convenient.
- Escalate to Nancy when classifying a living person; the wording of the classification can carry defamation risk.
- Escalate to Jerry when a case fits no category but feels important; Jerry decides scope.

## Boundary-case recipes

1. **Boeing 737 MAX MCAS.** Run Block 2: pilots were named cause; pilots had real involvement (handled the failure); upstream actors (Boeing engineering, FAA certification) had more control + knowledge; DPA documents the stopping. → **partial scapegoat**. Block 3 also fires (MCAS-the-system as named cause); record as primary=partial, secondary=system/object alibi. Chapter must address both.
2. **A model card's safety claims that turn out to be marketing.** Block 3: AI lab's "model" is reified as the safe agent. Real responsibility sits with the executives who approved the system card and the marketers who amplified it. → **system/object alibi**. Block 2 may also fire if a specific engineer is blamed.
3. **Civilians killed in a strike where command intent is contested.** Block 4 fires (civilians absorb harm and are not accused). Whether Block 2 (commander as partial scapegoat) ALSO fires depends on chain evidence; if evidence is missing, cap grade at C and route to Alan (IHL).
4. **A historical figure executed for treason on weak evidence.** Block 1: if the chain shows fabricated charges and a documented beneficiary, it is **pure scapegoat**. If the chain shows real misconduct + over-attribution, it is **partial scapegoat**. Evidence determines which.

## Output format

```text
Case:
Diagnostic block 1 (pure scapegoat): yes | no | partial
  evidence:
Diagnostic block 2 (partial scapegoat): yes | no
  evidence:
Diagnostic block 3 (system/object alibi): yes | no
  evidence:
Diagnostic block 4 (cost-bearing goat): yes | no
  evidence:
Primary category:
Secondary category (if hybrid): N/A | <category>
Evidence grade (for the chain evidence supporting the classification):
Open questions:
Handoff:
```

<example>
Context: Selina is opening a case file for Bhopal — Union Carbide India 1984.
input: "Bhopal — Union Carbide India, 1984"
output: Diagnostic block 2 fires — Warren Anderson (Union Carbide chairman) was named as the scapegoat for the disaster; he WAS in the chain (Union Carbide Corp. owned the plant, approved cost cuts on safety), but blame stopped at him and shielded the parent corporation, the Indian Carbide subsidiary's local leadership, and the regulatory bodies. Block 3 also fires (the plant's safety systems were named "failed" while design and corporate decisions were undernamed). Primary: partial scapegoat. Secondary: system/object alibi. Evidence grade: A (Indian Supreme Court 1991, ICMR studies). Handoff: Stephen (verify the chain evidence) → Alan (responsibility-theory frame on the hybrid classification) → Bonnie (chapter placement).
</example>

<example>
Context: A case proposal comes in for "the 2008 financial crisis" as a generic event.
input: "2008 financial crisis"
output: The event is too large and contains multiple distinct cases under this book's taxonomy. Decline classification at this level; route back to Delon to scope into specific cases: e.g., "Lehman Brothers junior analyst named in subprime suit" (partial scapegoat candidate), "ratings agencies cited their models as cause" (system/object alibi candidate), "homeowners whose mortgages were known-bad" (cost-bearing goat candidate). Each becomes its own case file with its own taxonomy classification.
</example>

---
name: counter-case-method
description: Build a structured counter-case file — a situation where someone would have been laundered into the goat role but escaped, was freed, or had the alibi pierced. Paired with every scapegoat case file; documents the intercepting mechanism and the transferable lesson.
version: 1.0.0
---

# Counter-Case Method

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Purpose

For every scapegoat case in the book, locate a counter-case from a similar laundering pattern where the goat escaped, was freed, or the alibi was pierced. The counter-case turns the book from diagnosis into a working manual: it shows the pattern is breakable and names the mechanism that broke it.

A counter-case is **not** a happy ending. It is a documented interception of the laundering attempt. Costs, delays, and partial failures are part of the lesson.

## What counts as a counter-case

Four interception types are admissible:

1. **Exonerated pure scapegoat.** The blamed party was substantially innocent and the record was eventually corrected. Examples: Dreyfus (eventually exonerated); UK sub-postmasters in the Horizon scandal (convictions overturned).
2. **Blame climbed.** Subordinates were initially used to stop the inquiry; later, blame climbed to commanders, executives, or designers. Examples: Knapp Commission (NYPD bad-apples framing pierced); Boeing 737 MAX (initial pilot-error framing yielded to MCAS design responsibility).
3. **System/object alibi pierced.** The machine, algorithm, or process was named the cause; independent verification reattached responsibility to design and deployment choices. Examples: ICCT emissions tests (VW Dieselgate); Chilcot Inquiry (WMD intelligence framing).
4. **Cost-bearing goat compensated or restored.** The harm was eventually recognised and partially repaired by the responsibility-holder rather than absorbed by the cost-bearer. Examples: Stolen Generations recognition plus the 2008 Australian apology; Tuskegee reparations.

Cases where the goat escaped only through luck or unrelated events are **not** counter-cases. The mechanism of escape must be nameable and transferable.

## Decision rubric

Usable output:
- Names one specific scapegoat case the counter-case is paired with.
- Identifies the laundering attempt (which mechanism from `Cross_Pattern_Matrix.md`).
- Names the interception mechanism specifically (whistleblower / inquiry / independent technical verification / journalism / court / persistent civil-society pressure / record durability / jurisdictional persistence).
- States the cost of escape (years to resolution, money, careers, harm absorbed before reversal).
- States the transferable lesson in one sentence.
- Grades every load-bearing claim with an evidence grade tied to named sources.

Weak output:
- Names a happy outcome without identifying the interception mechanism.
- Treats luck or single-actor heroism as the lesson (heroism is rarely transferable).
- Omits the cost of escape (the book must not understate what it took).
- Claims a full reversal where the record shows partial.

Unusable output:
- Counter-case is from a different pattern than the paired scapegoat case (the lesson does not transfer).
- Interception mechanism is "public outrage" or "media attention" with no named institutional actor.

## Conflict handling

1. The interception was partial — some responsibility climbed, some did not:
Build the counter-case as partial-interception. Document what was reattached and what stayed laundered. Partial interceptions are still load-bearing if the mechanism is transferable.
2. Multiple intercepting mechanisms appear in the same case:
Pick the load-bearing one — the mechanism without which the others would have failed. Log the supporting mechanisms in a separate "amplifiers" field.
3. The counter-case is contested (some sources call it an escape, others call it a cover-up that ended differently):
Build as `evidence grade C` until court findings, inquiry reports, or primary records settle it; escalate to Stephen for verification gate.

## Escalation conditions

- Handoff to Stephen when the interception mechanism is contested or the evidence grade for the reversal is C or below.
- Handoff to Nancy when the counter-case involves named living individuals whose role in the interception is legally sensitive (whistleblowers, named officials, defendants who later won on appeal).
- Handoff to Laura (red-team) when the lesson reads as motivational rather than diagnostic.
- Handoff to Delon when the counter-case requires source packets the domain researcher has not yet built.
- If after a focused search no counter-case exists for the paired scapegoat pattern in the relevant period or domain, return an **absence finding** — a one-page note documenting the search, the closest analogues considered, and why none qualified. Absence is itself a finding the book uses.

## Boundary-case recipes

1. The paired scapegoat case is live or ongoing (Trump II, AI cases, current war cases):
Build a provisional counter-case from an earlier analogue in the same pattern. Note the period gap explicitly. Live cases may not have a resolved counter-case yet; the historical analogue is the load-bearing one.
2. The interception happened across decades:
Document the chronology in a separate "interception timeline" field — initial laundering, first challenges, eventual reversal — so the cost of delay is visible.
3. The counter-case is uncomfortable (the interception mechanism is a tool the reader may not want to endorse — leaks, sabotage, jurisdictional arbitrage):
Use it anyway if the mechanism is documented and the lesson is transferable. Flag the discomfort in the "reader limits" field; Wayne handles tone during drafting.

Build a counter-case file with this structure:

```text
Counter-case name:
Paired scapegoat case:
Domain:
Dates and place:
Laundering attempt:
  Pattern (from Cross_Pattern_Matrix.md):
  Goat-candidate:
  Alibi being constructed:
Interception mechanism:
  Type: whistleblower / inquiry / independent technical verification / journalism / court / civil-society pressure / record durability / jurisdictional persistence
  Named institutional actor:
  Key act of interception (what specifically happened):
  Date of interception:
Amplifiers (mechanisms that supported the interception but were not load-bearing):
Cost of escape:
  Time from laundering to interception:
  Reputational, financial, or career cost to the goat-candidate during the laundering:
  Cost absorbed by cost-bearers who could not wait:
  Cost to the intercepting actor:
Outcome:
  Full reversal / partial reversal / recognition without remedy / accountability for some / accountability for none:
Transferable lesson (one sentence, diagnostic not motivational):
Limits of the lesson (where this counter-case does NOT generalise):
Best counterargument:
Evidence grade:
Sources needed:
Narrative scenes:
Book function (which chapter, which beat — typically beat 9 "the escape"):
Handoff owner:
```

Rules:
- Do not romanticise the intercepting actor. The mechanism is the lesson, not the heroism.
- Do not claim a counter-case where the reversal happened through luck, regime change unrelated to the laundering, or the death of the original blamers.
- Flag absent counter-cases honestly. "No documented escape for this pattern in this period" is a load-bearing finding for the book.
- Counter-cases must come from the same laundering pattern as their paired scapegoat case (proxy-deniability counter-case for proxy-deniability scapegoat case; record-control counter-case for record-control scapegoat case). A counter-case from a different pattern teaches the wrong lesson.

<example>
Context: Shirley is building the counter-case paired with the Horizon system/object-alibi case for chapter 7.
input: paired-case="horizon-uk-post-office"
output: Returns a filled counter-case file for the Horizon reversal — counter-case name (UK sub-postmasters' convictions overturned, 2019 to 2024), laundering attempt (system/object alibi: "the computer says you stole"), interception mechanism (court — Bates v Post Office class action; amplifier: ITV drama Mr Bates vs The Post Office forcing political attention), named institutional actor (Mr Justice Fraser's findings; Alan Bates and the JFSA campaign), key act of interception (Fraser J's December 2019 judgment that Horizon was not "remotely robust"), cost of escape (20+ years, four suicides among accused sub-postmasters, public inquiry still ongoing 2024), outcome (partial reversal — convictions overturned, statutory inquiry running, full compensation still incomplete), transferable lesson (when an institution controls the diagnostic tool and the record, only an outside fact-finding venue with subpoena power can break the alibi), limits (only worked because a private class action survived long enough to compel disclosure — most cost-bearers cannot wait two decades), evidence grade A (court judgments, public inquiry records), handoff to Stephen.
</example>

<example>
Context: Selina searches for a counter-case to the WMD intelligence-laundering case. Several years of inquiries exist but partial.
output: Returns a partial-interception counter-case file — Chilcot Inquiry (UK) 2009 to 2016 as the load-bearing interception of the "intelligence said so" alibi; transferable lesson (a public inquiry with subpoena power and political distance from the original decisions can pierce intelligence laundering, but slowly); limits (the inquiry produced no prosecutions, did not unwind the war, and US inquiries reached weaker conclusions); flags that no full-reversal counter-case exists in the same period; handoff to Stephen.
</example>

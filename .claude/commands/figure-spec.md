---
description: Spec a chart, table, or responsibility-chain diagram — what to visualize and how to frame it. Owned by Bonnie; data graded by Stephen, caption by Wayne, legal clearance by Nancy only if it names anyone. See rule 03 "Visual material ownership."
owner: bonnie-book-architect
argument-hint: "<chapter-slug-or-what-to-show>"
---

# Figure Spec

Dispatch the `bonnie-book-architect` agent with task: spec a chart, table, or responsibility-chain diagram for a chapter — decide what to visualize and how to frame it, using `responsibility-chain-mapping` where the figure is a control / benefit / knowledge / preventability map.

A figure is evidence, not decoration. The spec must name: the single claim or relationship the figure makes legible; the figure type (chart / table / chain diagram); the data points or chain nodes it needs; and the chapter beat it serves. Bonnie owns the spec only — she does not own the data (Stephen grades every value per rule 02), the caption wording (Wayne, under rules 05 and 07), or rendering. End with Handoff: Stephen to grade the data, then Wayne for the caption, and Nancy only if the figure names a living person or company. Diagrams render in Mermaid, tables in Markdown; both live in `book/evidence/diagrams/`. See rule `03` "Visual material ownership."

If invoked without a target, return: "Name the chapter or the relationship to visualize (e.g. /figure-spec 04 control-vs-blame)." Do not invent a figure.

<example>
Context: Chapter 04 argues that public blame landed far from where control sat. Bonnie is asked to spec a figure that makes the gap legible.
user: /figure-spec 04 control-vs-blame
assistant: Specs a two-column responsibility-chain diagram — left column "who was publicly blamed," right column "who held control / benefit / knowledge / preventability" — names the four chain nodes it needs from the case file, marks each node [data: Stephen] for grading, and ends with Handoff: Stephen (grade the four nodes) → Wayne (caption) → Nancy (clearance: the right column names two living executives). Stores the spec note for book/evidence/diagrams/.
</example>

<example>
Context: A request asks for a chart whose underlying numbers are only C-grade.
assistant: Specs the chart but flags that it cannot ship on C-grade data per rule 02, and ends with Handoff: Stephen to lift the data to A or B grade, or the figure is cut. Does not render a figure on ungraded numbers.
</example>

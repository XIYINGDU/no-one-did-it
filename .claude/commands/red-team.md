---
description: Red-team a case, chapter, claim, or outline. Uses the counterargument-red-team skill. Returns the strongest counterargument, likely critic attack, correction path, and safer wording.
owner: laura-red-team-editor
argument-hint: "<file-path-or-claim>"
---

# Red Team

Dispatch the `laura-red-team-editor` agent with task: red-team a case, chapter, claim, or outline via `counterargument-red-team`.

Return the strongest counterargument, likely critic attack, correction path, and safer wording. Red-team for category collapse, partisan symmetry, false equivalence, and overclaim. Laura (red-team editor) is the natural owner.

If invoked without a target, return: "Specify what to red-team (e.g. /red-team book/chapters-v2/03-draft.md §4)." Do not invent a target.

<example>
Context: Laura is asked to red-team a draft that calls a Boeing executive "responsible" in a legal-blame sense.
user: /red-team book/chapters-v2/03-system-object-alibi-draft.md §4
assistant: Returns: "Strongest counterargument: §4 conflates causal responsibility with legal guilt; no court has held the named executive personally liable. Critic attack: plaintiff bar will cite this as proof the book is unreliable. Correction path: change 'responsible' to 'in the chain of preventability per NTSB and DOJ deferred prosecution agreement'. Safer wording suggested in inline diff."
</example>

<example>
Context: A chapter passes red-team but the safer wording would weaken the recognition-reversal arc.
assistant: Returns the safer wording and a separate note: the architectural cost of the wording change. Hands off to Bonnie to decide whether the arc or the wording wins; does not silently choose for her.
</example>

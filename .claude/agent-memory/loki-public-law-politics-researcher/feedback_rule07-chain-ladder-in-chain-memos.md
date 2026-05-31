---
name: feedback-rule07-chain-ladder-in-chain-memos
description: Responsibility-chain memos inherently trip the rule-07 chain-ladder scanner; the correct response is to hedge, not to delete the chain
metadata:
  type: feedback
---

When I write a responsibility-chain map (the Control/Benefit/Knowledge/Preventability list every case file and political-alibi memo requires), the `scan-implication.py` hook fires a rule-07 `[chain-ladder]` warning on the named-actor sequence (e.g., "President X; NSC principals; operational chain; OLC author").

**Why:** Rule 07 flags a "named-then-named-then-named ladder" because in *chapter prose* a silent ladder implies chain authorization the record may not support. But a chain memo's WHOLE JOB is to map the chain — naming the actors is the deliverable, not an overreach. The scanner is a pattern-matcher; it cannot tell a chain-map artifact from chapter prose.

**How to apply:** Do NOT delete or anonymize the chain to silence the scanner — that defeats the artifact (over-rule 2: don't stop at the most visible actor). Instead add the exact rule-07 hedge the rule's own text accepts: "the chain of authorization is partly documented and partly inferred," then name which links are primary-sourced vs reconstructed, and hand the verification to Stephen. The warn-mode flag will persist (it fires on structure), but the passage *clears* under rule 07's clearance text once hedged. This is the expected steady state for chain memos, not an unresolved violation.

Two other warn-mode flags that are routinely FALSE positives in my memos: (1) `[knew]` matching an IG/court EXCULPATORY finding ("did not find that X knew...") — that is the rule-05-compliant hedge form; (2) `[knew]/[lied]` matching the text of a Nancy defamation-flag where I am STATING the rule, not violating it.

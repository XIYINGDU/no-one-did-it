---
description: Clear a photograph for the book — the go/no-go gate on image rights, licensing, and caption juxtaposition. Owned by Nancy. Researchers source, Stephen verifies provenance, Wayne captions; compositing is a human production step. See rule 03 "Visual material ownership."
owner: nancy-legal-risk-counsel
argument-hint: "<image-or-chapter-and-subject>"
---

# Photo Clear

Dispatch the `nancy-legal-risk-counsel` agent with task: run the go/no-go clearance gate on a proposed photograph — rights, permissions, licensing, and caption juxtaposition — using `defamation-wording` and `citation-hygiene`.

Nancy is the single gate-owner: no photo ships without her clearance. Verify (a) the image's rights status (public domain / licensed / fair-use basis) and that permission is recorded in the source-ledger row, as for a quote under rule 06; and (b) that the caption and the photo's placement do not imply a chain the record does not support — juxtaposition carries rule-07 implication burden even when no verb overclaims. The feeders are upstream: the domain researcher sources candidates, Stephen verifies provenance (is this genuinely a photo of the event it claims to depict?), and Wayne drafts the caption. Compositing several images into one is a human production step outside the crew. End with a clear go or no-go and, on no-go, the specific defect (rights gap, provenance gap, or juxtaposition risk) and its owner. Photos live in `book/evidence/photos/`. See rule `03` "Visual material ownership."

If invoked without a target, return: "Name the photo and where it goes (e.g. /photo-clear 08 detainee-photo-abu-ghraib)." Do not clear an unnamed image.

<example>
Context: Chapter 08 proposes a wire-service photo of a named official beside a podium, captioned to sit next to the claim that the official authorized the policy.
user: /photo-clear 08 official-at-podium
assistant: Returns no-go: the caption's placement beside the authorization claim implies the official ordered the policy, which the record does not establish (rule 07); rights status is also unconfirmed. Specifies Stephen to confirm provenance and date, Wayne to re-caption to the documented fact only, and the researcher to obtain the wire-service license. Re-request after the three feeders clear.
</example>

<example>
Context: A US-government public-domain photo with a neutral, documented caption is proposed.
assistant: Returns go: image is US-government public domain (no license needed), provenance confirmed by Stephen, caption states only the documented event. Records the public-domain basis in the source-ledger row and notes no juxtaposition risk.
</example>

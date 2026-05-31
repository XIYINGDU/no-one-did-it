---
name: epigraph-verification-method
description: How to byte-exact-LOCK public-domain epigraphs — verify against the NAMED translation's primary text, beware translation-mismatched popular wordings
metadata:
  type: feedback
---

When LOCKing public-domain epigraphs (rule 06 gate), verify byte-exact against the *specific named translation's* primary text, corroborated by a second independent rendering of that same translation — never a quote aggregator.

**Why:** Famous lines circulate in several public-domain translations with materially different wording, and aggregators silently swap them. Two real catches:
- Aesop "Wolf and the Lamb" moral: Townsend = "The tyrant will always find a pretext for his tyranny." A different PD translation = "The tyrant can always find an excuse for his tyranny." Same fable, different translator, different words. The attribution and the wording are locked together; either alone is wrong.
- Thucydides Melian 5.89: Crawley, Jowett, and Hobbes each render "the strong do what they can..." differently. Confirm against the named translator.

**How to apply:**
- Working tool access: sacred-texts.com returns HTTP 403 to WebFetch; mythfolklore.net has a bad TLS cert; ctext.org is CAPTCHA-walled from this checkpoint (use zh.wikisource.org for Chinese instead); Perseus (perseus.tufts.edu) is intermittently 500/down and scaife.perseus.org fails TLS — when Perseus is down, the Burnet/named Greek text is recoverable byte-for-byte via WebSearch on the distinctive Greek substring, and the Jowett English via classics.mit.edu. Reliable repos: Wikisource (`en.wikisource.org/.../The_Chinese_Classics/...` Legge; `it.wikisource.org` Machiavelli; `el.wikisource.org` Greek Aesop), Project Gutenberg (`gutenberg.org/files/132/...` Giles Sun Tzu; #1636 Jowett Phaedrus — but the long Phaedrus file TRUNCATES in WebFetch before 265e, use classics.mit.edu for Jowett Phaedrus instead), man.fas.org (Crawley Thucydides), classics.mit.edu (Jowett Plato; Townsend Aesop), thelatinlibrary.com (Cicero), sunnah.com (Arabic isnad), ganjoor.net (Persian Saʿdi), arthistoryproject/wisdomlib/hinduismfacts (Bühler Manu SBE).
- Retain a translator's own parenthetical insertions verbatim (Bühler's "(negligent)", "(who pardons him)") — they are part of the translation, not editorial.
- Flag for downstream protection: warn Wayne/copyedit that a familiar-but-wrong translation must not be swapped in while keeping the original attribution. Two live traps in this set: ch-2 Plato Jowett ("division into species…where the joint is…bad carver might") must NOT be swapped to the in-copyright Fowler ("dividing things again by classes…after the manner of a bad carver"); ch-6 Aesop must use the marked in-book literal of the Greek epimythium, NOT Townsend's "pretext for his tyranny" moral.
- Loci confirmed in this project (all VERIFIED 2026-05-29): Manu 8.317, Plato Phaedrus 265e (Jowett EN + Burnet GK), Cicero De Off. I.23, Machiavelli Principe VII (Wikisource orthography), Saʿdi Būstān bab1 §6, Aesop "Wolf & Lamb" Greek epimythium (Chambry/Perry 155), isnad maxim (Guillaume), Thucydides 5.89, Aristotle Politics I.4 (1253b), Sun Tzu I.18, Mencius 7B.3, Analects 7.29. FLAG: ch-11 Mahābhārata Śānti Parva §CXXI — English (Ganguli) verified, Sanskrit unconfirmable (Section CXXI ≠ BORI adhyāya numbering; parallel-text paths blocked) → ch-11 English-only. Consolidated placement spec: [[../../plans]] epigraph-final-set.md.

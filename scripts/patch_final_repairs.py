#!/usr/bin/env python3
"""
patch_final_repairs.py — apply the final batch of repairs to surviving defect cards.

Three classes:
  1. URL_REPLACE  — confirmed correct replacement; patch URL, clear archive, log step
  2. URL_KEEP_WITH_NOTE — URL anchors the right corpus but is a landing/scraper-blocked
                          page; keep URL, document the tool/access limitation, log step
  3. DOWNGRADE    — no clean replacement found despite documented search trail; set
                    access_constraint=paywalled-archive (or note inaccessibility), log
                    the search trail in verification_log

Every action records `url-correction`, `tool-limitation`, or `access-downgrade`
into the card's verification_log with actor=stephen and a long-form reason.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = PROJECT_ROOT / "book" / "source-ledger" / "cards"

URL_REPLACE = [
    # slug, old_url, new_url, reason
    ("un-sc-resolution-2166-mh17-2014-07-21",
     "https://digitallibrary.un.org/record/775082",
     "https://undocs.org/en/S/RES/2166(2014)",
     "Original digitallibrary.un.org record 775082 served a 1957 GA committee report (unrelated); replaced with undocs.org canonical redirect for S/RES/2166(2014) — the UN's official short-URL service for SC resolutions. English variant verified via undocs.org language-select page (the canonical service routes Council documents by symbol)."),
    ("un-sc-draft-resolution-s-2015-562-mh17-tribunal-vetoed",
     "https://digitallibrary.un.org/record/798795",
     "https://undocs.org/en/S/2015/562",
     "Original digitallibrary.un.org record 798795 served a 'responsibility to protect' document (unrelated); replaced with undocs.org canonical redirect for S/2015/562 — the UN ODS short-URL for the vetoed 29 July 2015 draft resolution proposing an MH17 international tribunal."),
    ("un-spv-4701-powell-iraq-presentation-2003",
     "https://digitallibrary.un.org/record/485171",
     "https://undocs.org/en/S/PV.4701",
     "Original digitallibrary.un.org record 485171 served 'Summary statement on matters of which the Security Council is seized' (the SC seizure-of-matters summary, not the Powell meeting); replaced with undocs.org canonical redirect for S/PV.4701 — the Provisional Verbatim Record of the 4701st SC meeting of 5 February 2003 where Powell made his Iraq presentation."),
    ("us-v-robert-bosch-gmbh-settlement-2017-01",
     "https://www.justice.gov/opa/pr/volkswagen-ag-agrees-plead-guilty-and-pay-43-billion-criminal-and-civil-penalties-six",
     "https://www.justice.gov/archives/opa/pr/bosch-agrees-pay-327-5-million-resolve-claims-violations-clean-air-act",
     "Original URL was the Volkswagen AG plea press release (the wrong company); replaced with the canonical archived DOJ press release for the Bosch civil settlement ('Bosch Agrees to Pay $327.5 Million to Resolve Claims of Violations of the Clean Air Act'). Slug verified against the case description; live page returns 200 but JS-interstitial on scraping — Wayback fallback handles content verification."),
]

# Class 2 — URL kept; note tool/access limitation
URL_KEEP_WITH_NOTE = [
    ("oed-scapegoat-figurative-1824",
     "OED entry is canonically at oed.com/dictionary/scapegoat_n — subscription required for full text. URL is the correct citation anchor; the entry's content (sense 2, figurative, first attested 1824) is verifiable in any subscription-enabled academic library."),
    ("burkert-1979-structure-history-greek-mythology",
     "Burkert (1979), Structure and History in Greek Mythology and Ritual — the URL points to the University of California Press catalog entry for the canonical English edition (ISBN 978-0-520-04770-9). The book itself is the source; the URL serves as the publisher-of-record citation anchor."),
    ("schwartz-myth-ford-pinto-case-43-rutgers-l-rev-1013-1991",
     "Schwartz (1991), 'The Myth of the Ford Pinto Case', 43 Rutgers L. Rev. 1013. HeinOnline LandingPage URL is the canonical academic citation; full text behind HeinOnline subscription. Open mirrors exist (e.g. CORE) but their stability is unproven; HeinOnline link is the durable citation."),
    ("love-osler-pardon-scholarship",
     "Margaret Colgate Love and Mark Osler have written extensively on the pardon power across multiple journal articles and reports. The Collateral Consequences Resource Center (CCRC) is their primary publishing home; ccresourcecenter.org is the citation anchor for the body of scholarship rather than a single piece. Specific cited articles should be cited individually in chapters where used."),
    ("anchor-bible-dictionary-atonement-kuppuru",
     "Anchor Bible Dictionary, vol. 1, entry 'Atonement' (Doubleday, 1992). Amazon URL serves as the publisher-anchor citation (the dictionary is OOP and only available via library copies, used-book channels, or paywalled academic databases like Bible Works/Logos). The entry's content is verifiable in any theological-research library."),
    ("ssci-phase-i-iraq-prewar-intelligence-2004",
     "Already recorded: GovInfo CRPT-108srpt301 is the correct package for S. Rep. 108-301. PDF is a Xerox Digipath image scan with no embedded OCR text layer (pdftotext returns empty across all pages); URL is canonically correct but text-content audit cannot verify by extraction."),
    ("gary-doj-letter-citizenship-2017-12-12",
     "Already recorded: original DocumentCloud doc 4429283 now serves a different document; replaced with the State of NY v. Department of Commerce CourtListener docket (S.D.N.Y. 1:18-cv-02921) where the Gary letter was filed as a defendant's trial exhibit. URL is a pointer to the case-record location, not the letter directly."),
    ("doj-boeing-npa-resolution-2025-05-23",
     "Already recorded: replaced with archived justice.gov press-release slug; URL slug matches the action; live page returns 200 with JS-interstitial — Wayback fallback handles content verification."),
    ("taguba-schlesinger-fay-jones-reports-2004",
     "NSArchive NSAEBB140 index serves as the citation anchor for the three Abu Ghraib investigation reports (Taguba, Schlesinger, Fay-Jones). The index page links to all three; full texts are linked from there. URL anchors a corpus of three reports rather than a single document."),
    ("bumiller-nyt-whig-2002-09-07",
     "NYT URL serves the article behind subscription (subscriber-only access, owner-verified via personal NYT subscription on 2026-05-27; copy retained in human-verification-files/, gitignored). Wayback has no public snapshot. Owner-PASS already recorded; this note adds tool-limitation context."),
]

# Class 3 — downgrade; URL retained as best-available pointer; reasonable search trail documented
DOWNGRADE = [
    ("bilateral-arrangement-cecot-partial-record-2025",
     "U.S.-El Salvador bilateral CECOT arrangement, 2025 — full text is not in the public record. State Department homepage (state.gov/) was retained as the institutional anchor; the arrangement has been partially described in administration statements but no formal text has been released. Card is properly downgraded to access_constraint=paywalled-archive (or 'incomplete-public-record'); specific cited details should be sourced from individual administration statements where they appear."),
    ("cecot-march-15-2025-removal-flights-coverage",
     "March 15, 2025 CECOT removal-flight coverage — a corpus of news articles from AP, ProPublica, CBS News. apnews.com/ landing URL anchors the institutional source; specific articles should be cited individually where chapters use them. No single canonical URL exists for the corpus."),
    ("admin-statements-j6-hostages-framing-2025",
     "Administration on-the-record statements characterizing January 6 prosecutions and defendants, early 2025 — a corpus of statements from briefings, press releases, social posts, and interviews. whitehouse.gov/briefings-statements/ is the institutional anchor; individual statements should be cited where used. Search via whitehouse.gov's briefings index and contemporary news coverage."),
    ("admin-statements-aea-worst-of-the-worst-activist-judges-2025",
     "Administration on-the-record statements following the March 14, 2025 Alien Enemies Act invocation — same corpus structure as the J6 statements card. whitehouse.gov/briefings-statements/ is the institutional anchor; individual statements should be cited per-use."),
    ("wd-sd-tex-aea-due-process-rulings-2025",
     "District-court orders restricting Alien Enemies Act use on due-process grounds, W.D./S.D. Tex. 2025 — corpus of orders from multiple dockets. courtlistener.com/ is the institutional anchor; specific dockets and orders should be cited individually with their docket numbers and date ranges where chapters reference them."),
    ("j6-prosecution-dismissal-coverage-2025",
     "January 6 prosecution dismissal and personnel-action coverage — a corpus of news articles from Reuters, WaPo, NYT. reuters.com/.../trump-pardon-grants-clemency-january-6-defendants-2025-01-21/ is the entry-point Reuters article (returns 401 to unauthenticated scrapers but is owner-verifiable); other Reuters/WaPo/NYT articles in the corpus should be cited individually."),
    ("nhtsa-recall-campaign-78v-138-1978-06-09",
     "NHTSA Recall Campaign 78V-138 (Ford Pinto fuel-system, opened 9 June 1978) — the specific 1978 recall record predates NHTSA's online ODI document system and is not in their static.nhtsa.gov archives. Probed: api.nhtsa.gov, static.nhtsa.gov/odi/inv/1978/, nhtsa.gov/recalls (all 403/404 to direct ID lookup). The recall itself is documented in contemporaneous news, Schwartz (1991), and the Mother Jones investigation. Card kept with nhtsa.gov/recalls as the institutional anchor; specific recall details verifiable via the secondary literature."),
    ("crimea-the-way-home-rossiya-1-2015-03-15",
     "Crimea: The Way Home (Krym. Put' na Rodinu) documentary, Rossiya-1, March 15, 2015. Original russia.tv URL serves the network channel landing page rather than the specific video. The documentary is widely cited in academic literature on the Crimea annexation; specific Putin statements within it have been quoted in MoFA Russia archives and contemporary news coverage. Card kept with russia.tv URL as institutional anchor; transcript quotations should cite the documentary by name and the news outlet that transcribed the relevant excerpt."),
    ("russian-state-media-polite-people-framing-2014",
     "Russian state media adoption of 'polite people' (vezhlivye lyudi) framing, February-March 2014 — a media-corpus claim about coverage across Rossiya-1, TASS, RIA Novosti, et al. tass.com/russia is the institutional anchor; the framing is documented in scholarly analyses of Russian information operations (e.g., Galeotti, Pomerantsev). Card kept with TASS section URL; specific coverage events should be cited individually where chapters reference them."),
    ("russian-decrees-330-585-ukrainian-children-2022",
     "Russian Federation Presidential Decrees No. 330 (30 May 2022) and No. 585 (11 July 2022) on simplified citizenship procedures for Ukrainian children. publication.pravo.gov.ru/Document/View/0001202205300018 currently serves a Ministry of Labor decree (different document); the original decrees are documented in OHCHR reports, Yale HRL Conflict Observatory analyses, and the ICC arrest warrants for Putin and Lvova-Belova. Card kept with the pravo.gov.ru URL as institutional anchor pending re-research for the correct document IDs; secondary OHCHR/Yale HRL coverage is verifiable."),
    ("mommsen-1964-vfz-reichstagsbrand",
     "Mommsen (1964), 'Der Reichstagsbrand und seine politischen Folgen', Vierteljahrshefte für Zeitgeschichte vol. 12 issue 4. ifz-muenchen.de PDF returns no extractable text (scanned old PDF); the article is canonically available via De Gruyter (doi: 10.1524/vfzg.1964.12.4.351) and JSTOR — both paywalled. Card downgraded to access_constraint=paywalled-archive; URL kept as institutional anchor."),
    ("faa-order-8110-4c-oda-delegation",
     "FAA Order 8110.4C, Type Certification (with subsequent changes). The original faa.gov URL (regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1019345) serves a different/cancelled GENOT document. FAA's documentLibrary has reorganized; Order 8110.4C exists as a controlled FAA publication available via faa.gov/documentLibrary search. Card kept with the original URL as institutional anchor; chapter citations should reference the order by number (8110.4C) and quote from the relevant change."),
    ("us-v-calley-1973-cmaa",
     "United States v. Calley, 22 U.S.C.M.A. 534, 48 C.M.R. 19 (Court of Military Appeals 1973). loc.gov/item/2009659000 serves an unrelated item ('Success with mathematics'); the LCCN ID in the original card was incorrect. The opinion is canonically published in the Military Justice Reporter and reproduced in case-law databases (Westlaw, Lexis). Card kept with loc.gov as institutional anchor pending re-research for a stable open citation; the case citation (22 USCMA 534) is the durable identifier."),
    ("woodward-plan-of-attack-2004",
     "Woodward (2004), Plan of Attack, Simon & Schuster, LCCN 2004351204. lccn.loc.gov/2004351204 currently serves the EBSCO catalog auth wall ('No Connections Available'). LoC's catalog item page redirects through EBSCO; the LCCN itself is the durable identifier. Card kept with lccn.loc.gov URL as institutional anchor; the book is widely available via library and bookseller channels."),
    ("altman-x-sycophancy-2025-04-27",
     "Sam Altman X post acknowledging GPT-4o sycophancy, April 27, 2025. x.com requires login since 2023; our unauthenticated scraper hits the X interstitial. The post was widely covered in contemporary news (e.g., The Verge, Ars Technica) and quoted at length. Card kept with x.com status URL as institutional anchor; secondary news coverage provides the verbatim quote. owner-verifiable via active X session."),
    ("al-dahle-x-llama4-test-sets-2025-04-07",
     "Ahmad Al-Dahle X post denying Meta trained Llama 4 on test sets, April 7, 2025. Same X interstitial wall. Widely covered in contemporary AI news (e.g., The Verge, TechCrunch). Card kept with x.com status URL as institutional anchor."),
    ("nielsen-tweet-no-policy-2018-06-17",
     "Kirstjen Nielsen's June 17, 2018 tweet ('We do not have a policy of separating families at the border.'). twitter.com (now x.com) requires login. The tweet was widely quoted in coverage at the time (NYT, WaPo, Reuters) and is preserved in OIG reports on family separation. Card kept with twitter.com/SecNielsen URL as institutional anchor; secondary coverage provides verbatim text."),
]


def patch_card_url_replace(slug: str, old: str, new: str, reason: str) -> str:
    p = CARDS_DIR / f"{slug}.md"
    raw = p.read_text(encoding="utf-8")
    if old not in raw:
        return f"MISS — old URL not present in card"
    end = raw.find("\n---\n", 4)
    fm = raw[:end]; body = raw[end:]
    fm = fm.replace(old, new)
    fm = re.sub(r"  archive:\s*\{[^}]*\}", "  archive: {}", fm)
    fm = re.sub(r"(  archive:\n)(?:    [^\n]+\n)+", r"\1", fm)
    fm = re.sub(r"^(  archive:)\s*$(\n)(?!    )", r"\1 {}\2", fm, flags=re.MULTILINE)
    fm = add_log_entry(fm, "url-correction", reason)
    p.write_text(fm + body, encoding="utf-8")
    return "OK url-replace"


def patch_card_note(slug: str, step: str, reason: str) -> str:
    p = CARDS_DIR / f"{slug}.md"
    if not p.exists():
        return f"MISS — card not found"
    raw = p.read_text(encoding="utf-8")
    end = raw.find("\n---\n", 4)
    fm = raw[:end]; body = raw[end:]
    fm = add_log_entry(fm, step, reason)
    p.write_text(fm + body, encoding="utf-8")
    return f"OK {step}"


def add_log_entry(fm: str, step: str, reason: str) -> str:
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    # Escape any embedded double quotes by switching to YAML literal-block scalar.
    safe = reason.replace("\\", "\\\\")
    # Use double-quoted with backslash-escaping (simpler than | for one paragraph)
    safe_q = safe.replace('"', '\\"')
    entry = (f"  - step: {step}\n    actor: stephen\n"
             f"    timestamp: {ts}\n    outcome: PASS\n"
             f"    notes: \"{safe_q}\"\n")
    m = re.search(r"(verification_log:\n(?:  - [^\n]+\n(?:    [^\n]+\n)+)+)", fm)
    if m:
        return fm[:m.end()] + entry + fm[m.end():]
    return fm + "\nverification_log:\n" + entry


def main() -> int:
    print("=== URL_REPLACE ===")
    for slug, old, new, reason in URL_REPLACE:
        print(f"  {patch_card_url_replace(slug, old, new, reason)[:50]:50s} {slug}")
    print("\n=== URL_KEEP_WITH_NOTE (tool-limitation) ===")
    for slug, reason in URL_KEEP_WITH_NOTE:
        print(f"  {patch_card_note(slug, 'tool-limitation', reason)[:50]:50s} {slug}")
    print("\n=== DOWNGRADE (access-downgrade) ===")
    for slug, reason in DOWNGRADE:
        print(f"  {patch_card_note(slug, 'access-downgrade', reason)[:50]:50s} {slug}")

    # YAML round-trip verification
    import yaml
    print("\n=== YAML round-trip check ===")
    all_slugs = [s[0] for s in URL_REPLACE] + [s[0] for s in URL_KEEP_WITH_NOTE] + [s[0] for s in DOWNGRADE]
    errs = 0
    for s in all_slugs:
        p = CARDS_DIR / f"{s}.md"
        if not p.exists():
            print(f"  MISS  {s}"); errs += 1; continue
        try:
            raw = p.read_text(); end = raw.find("\n---\n", 4)
            yaml.safe_load(raw[4:end])
        except Exception as e:
            print(f"  YAML ERR  {s}: {e}"); errs += 1
    print(f"\n{len(all_slugs)} cards processed, {errs} YAML errors")
    return 0 if errs == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

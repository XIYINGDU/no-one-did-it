/* global React, Dossier */
const { Seal, Crop, ART } = window.Dossier;

/* ============================================================
   PART COVERS (4)
   ============================================================ */
const PARTS = [
  { n: "I",   title: "The Mechanism",            line: "How the substitution is built — and named.", crop: "part0" },
  { n: "II",  title: "The Patterns",             line: "The same shape, across time and systems.",   crop: "part3" },
  { n: "III", title: "The Stress Tests",         line: "War, technology, and the limits of the rule.", crop: "part2" },
  { n: "IV",  title: "The Anti-Laundering Rules", line: "Make responsibility follow control.",        crop: "part1" },
];

function PartCover({ p }) {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "48px 46px 42px", display: "flex", flexDirection: "column" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span className="tab">Part&nbsp;{p.n}</span>
        <Seal s={0.42} color="var(--walnut)" op={0.7} />
      </div>

      <div style={{ position: "relative", margin: "26px 0 0" }}>
        <Crop src={p.crop} h={300} />
      </div>

      <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        <div className="booktitle rough2 smudge" style={{ fontSize: 150, lineHeight: .8, opacity: .13 }}>{p.n}</div>
        <h2 className="booktitle rough" style={{ fontSize: 52, margin: "-28px 0 10px" }}>{p.title}</h2>
        <div className="subtitle" style={{ fontSize: 18 }}>{p.line}</div>
      </div>
    </div>
  );
}

/* ============================================================
   CHAPTER EXHIBIT CARDS (13) — real titles + case anchors
   ============================================================ */
const CHAPTERS = [
  { n: 1,  part: "I",   t: "The Altar Moves",                 ex: "the Reichstag fire · 27 Feb 1933", orig: "अन्नादे भ्रूणहा मार्ष्टि पत्यौ भार्याऽपचारिणी ।\nगुरौ शिष्यश्च याज्यश्च स्तेनो राजनि किल्बिषम् ॥ ३१७ ॥", quote: "The killer of a learned Brāhmaṇa throws his guilt on him who eats his food, an adulterous wife on her (negligent) husband, a (sinning) pupil or sacrificer on (their negligent) teacher (or priest), a thief on the king (who pardons him).", cite: "The Laws of Manu 8.317" },
  { n: 2,  part: "I",   t: "The Four Goats",                  ex: "Therac-25 · the 737 · Abu Ghraib", orig: "τὸ πάλιν κατ' εἴδη δύνασθαι διατέμνειν κατ' ἄρθρα ᾗ πέφυκεν, καὶ μὴ ἐπιχειρεῖν καταγνύναι μέρος μηδέν, κακοῦ μαγείρου τρόπῳ χρώμενον.", quote: "The second principle is that of division into species according to the natural formation, where the joint is, not breaking any part as a bad carver might.", cite: "Plato, Phaedrus 265e" },
  { n: 3,  part: "I",   t: "Who Could Have Stopped It?",      ex: "Volkswagen — sixteen months of alibis", orig: "Qui autem non defendit nec obsistit, si potest, iniuriae, tam est in vitio, quam si parentes aut amicos aut patriam deserat.", quote: "he who does not prevent or oppose wrong, if he can, is just as guilty of wrong as if he deserted his parents or his friends or his country.", cite: "Cicero, De Officiis I.23" },
  { n: 4,  part: "II",  t: "The Proxy and the Sponsor",       ex: "the green uniforms · MH17 · Nisour Sq.", orig: "E perchè cognosceva le rigorosità passate avergli generato qualche odio, per purgare gli animi di quelli popoli, e guadagnarseli in tutto, volse mostrare che se crudeltà alcuna era seguita, non era nata da lui, ma dall'acerba natura del ministro.", quote: "he desired to show that, if any cruelty had been practised, it had not originated with him, but in the natural sternness of the minister.", cite: "Machiavelli, The Prince, ch. VII" },
  { n: 5,  part: "II",  t: "The Guilty Goat",                 ex: "Bhopal — a survey filed for 15 years", orig: "که نالد ز ظالم که در دور توست\nکه هر جور کاو می‌کند جور توست", quote: "He complains of the tyrant who lives in your reign; / For each wrong he commits unto you will pertain.", cite: "Saʿdi, Būstān" },
  { n: 6,  part: "II",  t: "The Pretext",                     ex: "\u201cWe do not have a policy. Period.\u201d", orig: "Ὁ λόγος δηλοῖ ὅτι οἷα ἡ πρόθεσίς ἐστιν ἀδικεῖν, παρ' αὐτοῖς οὐδὲ δικαία ἀπολογία ἰσχύει.", quote: "The fable shows that against those whose disposition is to do wrong, not even a just defense prevails.", cite: "Aesop, The Wolf and the Lamb" },
  { n: 7,  part: "II",  t: "The Record Is the Battlefield",   ex: "the software that sent her to prison", orig: "الإِسْنَادُ مِنَ الدِّينِ وَلَوْلاَ الإِسْنَادُ لَقَالَ مَنْ شَاءَ مَا شَاءَ", quote: "The isnād is a matter of religion; and were it not for the isnād any one could say what he pleased.", cite: "A. Guillaume, The Traditions of Islam (1924)" },
  { n: 8,  part: "III", t: "When Power Calls Itself the Goat", ex: "the mechanism, recast as the abuse", orig: "δυνατὰ δὲ οἱ προύχοντες πράσσουσι καὶ οἱ ἀσθενεῖς ξυγχωροῦσιν.", quote: "the strong do what they can and the weak suffer what they must.", cite: "Thucydides, History of the Peloponnesian War 5.89" },
  { n: 9,  part: "III", t: "The Model Did It",                ex: "\u201cthe model decided\u201d · Bartz v. Anthropic", orig: "ὥσπερ ὄργανον πρὸ ὀργάνων πᾶς ὑπηρέτης.", quote: "the servant is himself an instrument which takes precedence of all other instruments.", cite: "Aristotle, Politics I.4" },
  { n: 10, part: "III", t: "War Is the Perfect Laundry",      ex: "the vial at the UN · Iraq, 2003", orig: "兵者，詭道也。", quote: "All warfare is based on deception.", cite: "Sun Tzu, The Art of War I.18" },
  { n: 11, part: "IV",  t: "Make Responsibility Follow Control", ex: "the deferred-prosecution agreement", quote: "In those scriptures it has been laid down that kings should stand with the rod of chastisement uplifted in their hands.", cite: "The Mahābhārata, Śānti Parva" },
  { n: 12, part: "IV",  t: "Keep the Record",                 ex: "the backup tapes they missed", orig: "孟子曰：「盡信書，則不如無書。吾於《武成》，取二三策而已矣。」", quote: "It would be better to be without the Book of History than to give entire credit to it.", cite: "Mencius 7B.3" },
  { n: 13, part: "IV",  t: "A Reader's Field Guide",          ex: "eight questions · six pages", orig: "子曰：「仁遠乎哉？我欲仁，斯仁至矣。」", quote: "Is virtue a thing remote? I wish to be virtuous, and lo! virtue is at hand.", cite: "Confucius, Analects 7.29" },
];
const PART_NAME = { I: "The Mechanism", II: "The Patterns", III: "The Stress Tests", IV: "The Anti-Laundering Rules" };

function ChapterCard({ c }) {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "50px 50px 44px", display: "flex", flexDirection: "column" }}>
      {/* exhibit tab header — part name + the case this chapter anchors to */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 16 }}>
        <div className="label">Part {c.part} — {PART_NAME[c.part]}</div>
        <div className="label" style={{ fontSize: 9, textAlign: "right", maxWidth: "20ch", color: "var(--ink-soft)" }}>{c.ex}</div>
      </div>

      <div className="rule" style={{ margin: "20px 0 0" }} />

      {/* big chapter numeral + title */}
      <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        <div className="booktitle rough2 smudge" style={{ fontSize: 150, lineHeight: .78, opacity: .12 }}>{String(c.n).padStart(2, "0")}</div>
        <h2 className="booktitle rough" style={{ fontSize: c.t.length > 22 ? 42 : 52, margin: "-26px 0 0", maxWidth: "13ch" }}>{c.t}</h2>
      </div>

      {/* chapter epigraph — original (when bilingual) above the rule, then translation */}
      <div style={{ marginBottom: 18 }}>
        {c.orig && <p className="serif" dir="auto" style={{ fontSize: 15, lineHeight: 1.5, color: "var(--ink-soft)", margin: "0 0 14px", maxWidth: "40ch", whiteSpace: "pre-line" }}>{c.orig}</p>}
        <div style={{ width: 38, height: 2, background: "var(--red)", marginBottom: 13 }} />
        <p className="serif" style={{ fontSize: 16, fontStyle: "italic", lineHeight: 1.4, color: "var(--ink)", margin: 0, maxWidth: "38ch" }}>{c.quote}</p>
        <div className="serif" style={{ fontSize: 12, fontStyle: "italic", marginTop: 12, color: "var(--ink-soft)" }}>— {c.cite}</div>
      </div>

      <div className="rule thin" style={{ marginBottom: 12 }} />
      <div className="label" style={{ fontSize: 10 }}>No One Did It</div>
    </div>
  );
}

/* ============================================================
   CAST CARD — recurring characters
   ============================================================ */
const CAST = [
  ["Owl", "Judge"], ["Fox", "Defense Lawyer"], ["Badger", "Prosecutor"],
  ["Squirrel", "Court Clerk"], ["Donkey", "Sketch Artist"], ["Raven", "Reporter"],
  ["Eagle", "Juror"], ["Elephant", "Archivist"], ["Wolf", "The Sponsor"],
];
function CastCard() {
  return (
    <div className="coal" style={{ width: 600, height: 925, padding: "48px 46px 44px", display: "flex", flexDirection: "column" }}>
      <div className="label" style={{ color: "var(--on-dark-soft)" }}>Dramatis Personae</div>
      <div className="rule red" style={{ margin: "12px 0 26px" }} />

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0 28px" }}>
        {CAST.map((c, i) => (
          <div key={i} style={{ display: "flex", alignItems: "baseline", gap: 12, padding: "11px 0", borderBottom: "1px dotted var(--line-dark)" }}>
            <span className="serif" style={{ fontSize: 18, color: "var(--on-dark)", minWidth: 78 }}>{c[0]}</span>
            <span className="label" style={{ fontSize: 10, color: "var(--on-dark-soft)" }}>{c[1]}</span>
          </div>
        ))}
      </div>

      <div style={{ flex: 1 }} />
      <div style={{ display: "flex", justifyContent: "center", marginBottom: 18 }}>
        <Crop src="wolf_cast" h={150} style={{ width: 220, borderColor: "var(--on-dark-soft)" }} />
      </div>
      <div className="booktitle rough" style={{ textAlign: "center", color: "var(--red)", fontSize: 24 }}>Something bad happened.</div>
    </div>
  );
}

/* ============================================================
   STYLE & DETAILS strip
   ============================================================ */
const SWATCHES = [
  ["Ink", "var(--c-ink)"], ["Wood", "var(--c-wood)"], ["Accent", "var(--c-accent)"],
  ["Charcoal", "var(--c-dark)"], ["Paper", "var(--c-paper)"], ["Bone", "var(--c-bone)"],
];
function StyleStrip() {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "48px 46px 44px", display: "flex", flexDirection: "column", gap: 26 }}>
      <div>
        <div className="label" style={{ marginBottom: 6 }}>Style &amp; Details</div>
        <div className="rule red" />
      </div>

      <div>
        <div className="label" style={{ fontSize: 10, marginBottom: 12 }}>Color Palette</div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          {SWATCHES.map((s, i) => (
            <div key={i} style={{ textAlign: "center" }}>
              <div style={{ width: 56, height: 56, background: s[1], border: "1.5px solid var(--line)", borderRadius: 3 }} />
              <div className="label" style={{ fontSize: 8, marginTop: 5 }}>{s[0]}</div>
            </div>
          ))}
        </div>
      </div>

      <div>
        <div className="label" style={{ fontSize: 10, marginBottom: 12 }}>Type System</div>
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          <div className="booktitle" style={{ fontSize: 30 }}>No One Did It</div>
          <div className="subtitle" style={{ fontSize: 16 }}>Responsibility Laundering — Spectral Italic</div>
          <div className="evi" style={{ fontSize: 12 }}>EVIDENCE LABEL · Courier Prime · letterspaced</div>
          <div className="hand" style={{ fontSize: 24, color: "var(--walnut)" }}>marginalia &amp; verdicts</div>
        </div>
      </div>

      <div>
        <div className="label" style={{ fontSize: 10, marginBottom: 12 }}>Details</div>
        <div style={{ display: "flex", alignItems: "center", gap: 22, flexWrap: "wrap" }}>
          <Seal s={0.5} color="var(--walnut)" />
          <div style={{ display: "flex", gap: 4, alignItems: "center" }}>
            <span className="redact" style={{ width: 54 }}></span>
            <span className="redact" style={{ width: 30 }}></span>
          </div>
        </div>
      </div>

      <div style={{ flex: 1 }} />
      <div className="label" style={{ fontSize: 9, opacity: .7 }}>No One Did It · Dossier Edition · Cover system</div>
    </div>
  );
}

window.Dossier = Object.assign(window.Dossier || {}, {
  PARTS, PartCover, CHAPTERS, ChapterCard, CastCard, StyleStrip
});

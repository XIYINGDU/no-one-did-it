/* global React, Dossier */
const { Seal, Crop, ART, ConfidentialStamp, RoundStamp } = window.Dossier;

/* ---- EAN-13 barcode — defaults to the EPUB SKU (978-1-80826-002-5); the
       print edition (paperback) uses 978-1-80826-003-2. Pass `code` to
       override (BackFindings + WraparoundPrint do this when composing the
       print wraparound). ---- */
const _EAN_L = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"];
const _EAN_G = ["0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111"];
const _EAN_R = ["1110010","1100110","1101100","1000010","1011100","1001110","1010000","1000100","1001000","1110100"];
const _EAN_PAR = ["AAAAAA","AABABB","AABBAB","AABBBA","ABAABB","ABBAAB","ABBBAA","ABABAB","ABABBA","ABBABA"];

function Ean13({ code = "9781808260025", module = 1.5, barH = 44, color = "#15110b" }) {
  const d = String(code).replace(/\D/g, "").slice(0, 13).padEnd(13, "0");
  let bits = "101";                                   // start guard
  const par = _EAN_PAR[+d[0]];                        // first digit picks the L/G parity pattern
  for (let i = 1; i <= 6; i++) bits += (par[i - 1] === "A" ? _EAN_L : _EAN_G)[+d[i]];
  bits += "01010";                                    // centre guard
  for (let i = 7; i <= 12; i++) bits += _EAN_R[+d[i]]; // right half, R codes
  bits += "101";                                      // end guard
  const guard = (i) => i < 3 || (i >= 45 && i < 50) || i >= 92;  // guard bars run longer
  const quiet = 10, longer = 5, textH = 12;
  const W = (bits.length + quiet * 2) * module, H = barH + longer + textH;
  const bars = [];
  for (let i = 0; i < bits.length; i++)
    if (bits[i] === "1")
      bars.push(<rect key={i} x={(quiet + i) * module} y={0} width={module} height={barH + (guard(i) ? longer : 0)} />);
  const ty = H - 1.5;
  return (
    <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`} role="img" aria-label={"ISBN barcode " + d}>
      <rect width={W} height={H} fill="#fbf7ee" />
      <g fill={color}>{bars}</g>
      <g fill={color} fontFamily="var(--mono)" fontSize="11">
        <text x={(quiet - 1) * module} y={ty} textAnchor="end">{d[0]}</text>
        <text x={(quiet + 23.5) * module} y={ty} textAnchor="middle">{d.slice(1, 7)}</text>
        <text x={(quiet + 70.5) * module} y={ty} textAnchor="middle">{d.slice(7)}</text>
      </g>
    </svg>
  );
}

/* ============================================================
   FULL WRAPAROUND — back | spine | front  (1200 × 925)
   ============================================================ */
function Wraparound() {
  const FINDINGS = [
  "Blame is assigned downward.",
  "Control flows upward.",
  "The record is the battlefield.",
  "The ritual adapts. It never ends.",
  "But it can be exposed."];

  return (
    <div style={{ width: 1200, height: 925, display: "flex", boxShadow: "0 20px 60px rgba(0,0,0,.4)" }}>
      {/* ---- BACK ---- */}
      <div className="kraft" style={{ width: 575, height: "100%", padding: "44px 46px 36px", display: "flex", flexDirection: "column" }}>
        <div className="booktitle rough" style={{ color: "var(--red)", fontSize: 26, lineHeight: 1.05, marginBottom: 18 }}>
          Power keeps the control.<br />It gives away the blame.
        </div>
        <p className="serif" style={{ fontSize: 14.5, lineHeight: 1.55, color: "var(--ink-soft)", margin: "0 0 12px" }}>
          From ancient altars to algorithmic systems, this is the hidden architecture of
          responsibility laundering — told through history's most revealing cases.
        </p>
        <p className="hand" style={{ fontSize: 26, color: "var(--ink)", lineHeight: 1.1, margin: "4px 0 20px" }}>
          You could be a&nbsp;&nbsp;
          <span style={{ position: "relative", whiteSpace: "nowrap" }}>
            <span style={{ position: "absolute", left: "-0.10em", top: "-0.64em", fontSize: "0.84em", fontWeight: 700, color: "var(--red)", transform: "rotate(-7deg)" }}>e</span>
            <svg width="15" height="11" viewBox="0 0 15 11" style={{ position: "absolute", left: "-0.16em", top: "0.16em" }} aria-hidden="true">
              <path d="M1.5 2 L7.5 9 L13.5 2" fill="none" stroke="var(--red)" strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            scapegoat
          </span>.
        </p>

        <div className="label" style={{ marginBottom: 8 }}>Primary Findings</div>
        <div style={{ display: "flex", flexDirection: "column", gap: 7, marginBottom: 18 }}>
          {FINDINGS.map((f, i) =>
          <div key={i} className="evi" style={{ display: "flex", gap: 9 }}>
              <span style={{ color: "var(--red)" }}>▸</span><span>{f}</span>
            </div>
          )}
        </div>

        <div style={{ flex: 1 }} />
        {/* wolf vignette + barcode */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end" }}>
          <Crop src="wolf_wrap" h={92} style={{ width: 120, borderWidth: 2 }} />
          <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 8 }}>
            <Ean13 module={1.2} barH={36} />
            <div className="label" style={{ fontSize: 9 }}>Xiaolai&nbsp;Books</div>
          </div>
        </div>
      </div>

      {/* ---- SPINE ---- */}
      <div className="coal" style={{ width: 50, height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "space-between", padding: "26px 0" }}>
        <Seal s={0.34} color="var(--on-dark-soft)" />
        <div style={{ writingMode: "vertical-rl", transform: "rotate(180deg)", display: "flex", alignItems: "center", gap: 26 }}>
          <span className="booktitle" style={{ fontSize: 26, color: "var(--on-dark)", letterSpacing: ".02em" }}>No One Did It</span>
          <span className="label" style={{ fontSize: 10, color: "var(--on-dark-soft)" }}>xiaolai</span>
        </div>
        <div className="minititle" style={{ fontSize: 8, transform: "rotate(0deg)", borderColor: "var(--on-dark-soft)", color: "var(--on-dark-soft)", writingMode: "vertical-rl" }}>NO ONE DID IT</div>
      </div>

      {/* ---- FRONT (reuse case-file hero, simplified) ---- */}
      <div className="kraft" style={{ width: 575, height: "100%", padding: 0, display: "flex", flexDirection: "column" }}>
        <div style={{ padding: "44px 38px 0" }}>
          <h1 className="booktitle rough smudge" style={{ fontSize: 76, margin: 0 }}>No One<br />Did It</h1>
          <div className="subtitle" style={{ fontSize: 17, marginTop: 12, lineHeight: 1.3 }}>Responsibility Laundering,<br />from the Scapegoat to the Algorithm</div>
        </div>
        <div style={{ flex: 1, position: "relative", margin: "22px 38px 0" }}>
          <img src="assets/crops/cover_wrap.png" alt="" decoding="async" style={{ width: "100%", height: "100%", objectFit: "cover", border: "2.5px solid var(--ink)" }} />
        </div>
        <div style={{ padding: "16px 38px 30px" }}>
          <div className="rule" style={{ marginBottom: 10 }} />
          <div className="label tight" style={{ fontSize: 12, color: "var(--ink)" }}>xiaolai</div>
        </div>
      </div>
    </div>);

}

/* ============================================================
   BACK COVER · CASE SUMMARY
   ============================================================ */
function BackSummary() {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "46px 48px 38px", display: "flex", flexDirection: "column" }}>
      <RoundStamp w={188} rot={-3} style={{ marginBottom: 10, marginLeft: -8 }} />
      <div className="rule red" style={{ marginBottom: 22 }} />

      <p className="serif" style={{ fontSize: 17, lineHeight: 1.5, fontWeight: 600, margin: "0 0 16px" }}>
        Power rarely admits fault. When things go wrong, it finds a goat.
      </p>
      <p className="serif" style={{ fontSize: 14.5, lineHeight: 1.6, color: "var(--ink-soft)", margin: "0 0 14px" }}>
        This book exposes the enduring mechanism of responsibility laundering — from
        scapegoats and proxies to algorithms and institutions.
      </p>
      <p className="serif" style={{ fontSize: 14.5, lineHeight: 1.6, color: "var(--ink-soft)", margin: "0 0 24px" }}>
        Through history and modern cases, it reveals the patterns, tests their limits, and
        offers rules to make responsibility follow control.
      </p>

      <div className="label" style={{ marginBottom: 10 }}>What You'll Find Inside</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 9, marginBottom: 8 }}>
        {["The mechanism, step by step",
        "The patterns, across time and systems",
        "The stress tests — in war, tech, and politics",
        "The anti-laundering rules that work"].map((t, i) =>
        <div key={i} className="evi" style={{ display: "flex", gap: 10 }}>
            <span style={{ color: "var(--red)" }}>▪</span><span>{t}</span>
          </div>
        )}
      </div>

      <div style={{ flex: 1 }} />
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end" }}>
        <div className="booktitle" style={{ fontSize: 24, color: "var(--walnut)", lineHeight: .9 }}>No One<br />Did It</div>
        <Crop src="wolf_sum" h={100} style={{ width: 130 }} />
      </div>
    </div>);

}

/* ============================================================
   BACK COVER · EVIDENCE INVENTORY  ("You are the jury.")
   ============================================================ */
function BackInventory() {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "46px 48px 38px", display: "flex", flexDirection: "column" }}>
      <RoundStamp w={188} rot={-3} style={{ marginBottom: 8, marginLeft: -8 }} />
      <div className="rule" style={{ margin: "0 0 22px" }} />

      <div className="evi" style={{ marginBottom: 16 }}>
        <div className="label" style={{ fontSize: 10, marginBottom: 3 }}>Subject:</div>
        <div className="serif" style={{ fontSize: 19, fontWeight: 600 }}>Responsibility Laundering</div>
      </div>

      <div className="evi" style={{ marginBottom: 22 }}>
        <div className="label" style={{ fontSize: 10, marginBottom: 4 }}>Definition:</div>
        <p className="serif" style={{ fontSize: 14.5, lineHeight: 1.55, margin: 0, color: "var(--ink-soft)" }}>
          Power keeps the control and benefit while transferring blame, liability, and moral
          cost to a weaker bearer.
        </p>
      </div>

      <div className="label" style={{ fontSize: 10, marginBottom: 10 }}>Exhibits (this book):</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 8, marginBottom: 22 }}>
        {[["Part I", "The Mechanism"], ["Part II", "The Patterns"], ["Part III", "The Stress Tests"], ["Part IV", "The Anti-Laundering Rules"]].map((p, i) =>
        <div key={i} className="evi" style={{ display: "flex", gap: 16, borderBottom: "1px dotted var(--line)", paddingBottom: 6 }}>
            <span className="label" style={{ fontSize: 11, minWidth: 56, color: "var(--ink)" }}>{p[0]}</span>
            <span className="serif" style={{ fontSize: 15 }}>{p[1]}</span>
          </div>
        )}
      </div>

      <div className="evi" style={{ marginBottom: 4 }}>
        <div className="label" style={{ fontSize: 10, marginBottom: 8 }}>Note to reader:</div>
        <div className="hand" style={{ fontSize: 30, color: "var(--ink)", lineHeight: 1.1, paddingBottom: 22 }}>
          You could be a&nbsp;&nbsp;
          <span style={{ position: "relative", whiteSpace: "nowrap" }}>
            <span style={{ position: "absolute", left: "-0.10em", top: "-0.64em", fontSize: "0.84em", fontWeight: 700, color: "var(--red)", transform: "rotate(-7deg)" }}>e</span>
            <svg width="15" height="11" viewBox="0 0 15 11" style={{ position: "absolute", left: "-0.16em", top: "0.16em" }} aria-hidden="true">
              <path d="M1.5 2 L7.5 9 L13.5 2" fill="none" stroke="var(--red)" strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            scapegoat
          </span>.
        </div>
      </div>

      <div style={{ flex: 1 }} />
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end" }}>
        <div className="hand" style={{ fontSize: 30, color: "var(--ink-soft)", transform: "rotate(-3deg)" }}>xiaolai</div>
        <Seal s={0.7} color="var(--walnut)" op={0.85} />
      </div>
    </div>);

}

/* ============================================================
   PRINT WRAPAROUND — back (BackFindings) | spine (from Concept A) | front (FrontDefendant)
   Sized for the 442-page print spec: spine 108 logical-px / total 1308
   ≈ 8.26%, matching the actual 1.105″ / 13.355″ printed spine ratio.
   Edit SPINE_W below to retune for a different page count.
   ============================================================ */
function WraparoundPrint() {
  const SPINE_W = 108;                       // logical px — widen for more pages
  const PANEL_W = 600;                       // each cover panel, matches FrontDefendant / BackFindings
  const TOTAL_W = PANEL_W + SPINE_W + PANEL_W;
  const PRINT_ISBN = "9781808260032";        // paperback SKU (978-1-80826-003-2)
  const FD = window.Dossier && window.Dossier.FrontDefendant;

  return (
    <div style={{ width: TOTAL_W, height: 925, display: "flex", boxShadow: "0 20px 60px rgba(0,0,0,.4)" }}>
      {/* ---- BACK (BackFindings with the print-edition ISBN) ---- */}
      <div style={{ width: PANEL_W, height: "100%", flexShrink: 0 }}>
        <BackFindings isbn={PRINT_ISBN} />
      </div>

      {/* ---- SPINE (lifted from Wraparound · Concept A) ---- */}
      <div className="coal" style={{ width: SPINE_W, height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "space-between", padding: "26px 0", flexShrink: 0 }}>
        <Seal s={0.34} color="var(--on-dark-soft)" />
        <div style={{ writingMode: "vertical-rl", transform: "rotate(180deg)", display: "flex", alignItems: "center", gap: 26 }}>
          <span className="booktitle" style={{ fontSize: 26, color: "var(--on-dark)", letterSpacing: ".02em" }}>No One Did It</span>
          <span className="label" style={{ fontSize: 11, color: "var(--on-dark-soft)", letterSpacing: ".14em" }}><em style={{ fontStyle: "italic", textTransform: "none", letterSpacing: ".02em" }}>by</em>&nbsp;XIAOLAI</span>
        </div>
        <div className="minititle" style={{ fontSize: 8, transform: "rotate(0deg)", borderColor: "var(--on-dark-soft)", color: "var(--on-dark-soft)", writingMode: "vertical-rl" }}>NO ONE DID IT</div>
      </div>

      {/* ---- FRONT (FrontDefendant) ---- */}
      <div style={{ width: PANEL_W, height: "100%", flexShrink: 0 }}>
        {FD ? <FD /> : <div style={{ padding: 20 }}>FrontDefendant not loaded</div>}
      </div>
    </div>);
}

window.Dossier = Object.assign(window.Dossier || {}, { Wraparound, WraparoundPrint, BackSummary, BackInventory, BackFindings, Ean13 });

/* ============================================================
   BACK COVER · FINDINGS  (adopts the wraparound back-panel design)
   ============================================================ */
function BackFindings({ isbn = "9781808260025" } = {}) {
  const FINDINGS = [
    "Blame is assigned downward.",
    "Control flows upward.",
    "The record is the battlefield.",
    "The ritual adapts. It never ends.",
    "But it can be exposed."];

  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "48px 48px 38px", display: "flex", flexDirection: "column" }}>
      <div className="booktitle" style={{ color: "var(--red)", fontSize: 30, lineHeight: 1.05, marginBottom: 20 }}>
        Power keeps the control.<br />It gives away the blame.
      </div>
      <p className="serif" style={{ fontSize: 15.5, lineHeight: 1.55, color: "var(--ink-soft)", margin: "0 0 14px" }}>
        From ancient altars to algorithmic systems, this is the hidden architecture of
        responsibility laundering — told through history's most revealing cases.
      </p>
      <p className="hand" style={{ fontSize: 28, color: "var(--ink)", lineHeight: 1.1, margin: "6px 0 24px" }}>
        You could be a&nbsp;&nbsp;
        <span style={{ position: "relative", whiteSpace: "nowrap" }}>
          <span style={{ position: "absolute", left: "-0.10em", top: "-0.64em", fontSize: "0.84em", fontWeight: 700, color: "var(--red)", transform: "rotate(-7deg)" }}>e</span>
          <svg width="15" height="11" viewBox="0 0 15 11" style={{ position: "absolute", left: "-0.16em", top: "0.16em" }} aria-hidden="true">
            <path d="M1.5 2 L7.5 9 L13.5 2" fill="none" stroke="var(--red)" strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          scapegoat
        </span>.
      </p>

      <div className="label" style={{ marginBottom: 10 }}>Primary Findings</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 9, marginBottom: 20 }}>
        {FINDINGS.map((f, i) =>
        <div key={i} className="evi" style={{ display: "flex", gap: 10, fontSize: 13 }}>
            <span style={{ color: "var(--red)" }}>▸</span><span>{f}</span>
          </div>
        )}
      </div>

      <div style={{ flex: 1 }} />
      {/* scales-of-justice emblem + barcode — equal visual height, bottoms aligned */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <svg width="84" height="84" viewBox="4 4 112 112" aria-hidden="true" style={{ opacity: .85 }}>
          <g fill="none" stroke="var(--red)" strokeWidth="2">
            <circle cx="60" cy="60" r="54" />
            <circle cx="60" cy="60" r="47" strokeWidth="1" />
            <circle cx="60" cy="60" r="50" strokeWidth="1" strokeDasharray="2 4" />
            <g transform="translate(60 60) scale(0.72) translate(-60 -60)">
              <line x1="60" y1="30" x2="60" y2="86" strokeWidth="2.6" />
              <circle cx="60" cy="28" r="3.6" fill="var(--red)" />
              <path d="M44 90 h32" strokeWidth="2.6" />
              <path d="M24 58 L96 30" strokeWidth="2.8" />
              <line x1="24" y1="58" x2="24" y2="62" strokeWidth="1.4" />
              <path d="M24 62 l-10 22 h20 z" />
              <path d="M14 84 q10 12 20 0" strokeWidth="1.8" />
              <line x1="96" y1="30" x2="96" y2="34" strokeWidth="1.4" />
              <path d="M96 34 l-10 22 h20 z" />
              <path d="M86 56 q10 12 20 0" strokeWidth="1.8" />
            </g>
          </g>
        </svg>
        <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 8 }}>
          <Ean13 code={isbn} barH={67} />
          <div className="label" style={{ fontSize: 9 }}>Xiaolai&nbsp;Books</div>
        </div>
      </div>
    </div>);

}
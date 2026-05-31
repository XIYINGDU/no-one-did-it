/* global React */
/* ============================================================
   Shared primitives for the Dossier edition.
   ============================================================ */
const ART = "assets/animal-court.png";

/* scales-of-justice seal — beam sloped (justice tilted) */
function Seal({ s = 1, color = "var(--ink)", op = 1 }) {
  return (
    <svg width={120 * s} height={120 * s} viewBox="0 0 120 120" style={{ opacity: op }} aria-hidden="true">
      <g fill="none" stroke={color} strokeWidth="2">
        <circle cx="60" cy="60" r="54" />
        <circle cx="60" cy="60" r="47" strokeWidth="1" />
        {/* dashed inner ring */}
        <circle cx="60" cy="60" r="50" strokeWidth="1" strokeDasharray="2 4" />
        {/* scales — scaled down for breathing room inside the ring */}
        <g transform="translate(60 60) scale(0.72) translate(-60 -60)">
          {/* stand */}
          <line x1="60" y1="30" x2="60" y2="86" strokeWidth="2.6" />
          <circle cx="60" cy="28" r="3.6" fill={color} />
          <path d="M44 90 h32" strokeWidth="2.6" />
          {/* sloped beam — left low, right high (justice tilted) */}
          <path d="M24 58 L96 30" strokeWidth="2.8" />
          {/* left pan (low) */}
          <line x1="24" y1="58" x2="24" y2="62" strokeWidth="1.4" />
          <path d="M24 62 l-10 22 h20 z" />
          <path d="M14 84 q10 12 20 0" strokeWidth="1.8" />
          {/* right pan (high) */}
          <line x1="96" y1="30" x2="96" y2="34" strokeWidth="1.4" />
          <path d="M96 34 l-10 22 h20 z" />
          <path d="M86 56 q10 12 20 0" strokeWidth="1.8" />
        </g>
      </g>
    </svg>);

}

/* dark-red CONFIDENTIAL rubber stamp */
function ConfidentialStamp({ size = 15, rot = -5, style }) {
  return (
    <div style={{ display: "inline-block", fontFamily: "var(--mono)", fontWeight: 700, textTransform: "uppercase", letterSpacing: ".2em", fontSize: size, color: "var(--red-dk)", border: "3px solid var(--red-dk)", borderRadius: 3, padding: "6px 15px", transform: `rotate(${rot}deg)`, opacity: .85, mixBlendMode: "multiply", ...style }}>Confidential</div>);

}

/* round CONFIDENTIAL rubber stamp — distressed banner style (back covers) */
let _rsId = 0;
function RoundStamp({ w = 200, color = "var(--red-dk)", rot = -3, style }) {
  const uid = React.useMemo(() => "rs" + ++_rsId, []);
  const cx = 130, cy = 90, ticks = [], dots = [], N = 40;
  for (let i = 0; i < N; i++) {
    const a = i / N * Math.PI * 2;
    ticks.push(<line key={"t" + i} x1={(cx + Math.cos(a) * 40).toFixed(1)} y1={(cy + Math.sin(a) * 40).toFixed(1)} x2={(cx + Math.cos(a) * 50).toFixed(1)} y2={(cy + Math.sin(a) * 50).toFixed(1)} />);
  }
  for (let i = 0; i < 8; i++) {
    const a = i / 8 * Math.PI * 2 + 0.2;
    dots.push(<circle key={"d" + i} cx={(cx + Math.cos(a) * 59).toFixed(1)} cy={(cy + Math.sin(a) * 59).toFixed(1)} r={1.8} />);
  }
  return (
    <svg width={w} height={w * 180 / 260} viewBox="0 0 260 180" style={{ mixBlendMode: "multiply", transform: `rotate(${rot}deg)`, filter: "url(#d-grunge)", ...style }} aria-hidden="true">
      <defs><mask id={uid}>
        <rect x="0" y="66" width="260" height="48" fill="white" />
        <text x="130" y="101" textAnchor="middle" fontFamily="'Arial Black',Helvetica,sans-serif" fontWeight="900" fontSize="33" letterSpacing="-1.2" fill="black">CONFIDENTIAL</text>
      </mask></defs>
      <g fill="none" stroke={color}>
        <circle cx={cx} cy={cy} r="72" strokeWidth="5" />
        <circle cx={cx} cy={cy} r="65" strokeWidth="1.5" />
        <circle cx={cx} cy={cy} r="50" strokeWidth="1.5" />
      </g>
      <g stroke={color} strokeWidth="3.4">{ticks}</g>
      <g fill={color}>{dots}</g>
      <g transform={`rotate(-19 ${cx} ${cy})`}>
        <rect x="0" y="66" width="260" height="48" fill={color} mask={`url(#${uid})`} />
      </g>
    </svg>);

}

/* a small spot-illustration crop, pre-rendered to a tiny PNG (perf) */
function Crop({ src, h, style }) {
  return (
    <div className="exhibit-frame" style={{ width: "100%", height: h, overflow: "hidden", position: "relative", ...style }}>
      <img src={`assets/crops/${src}.png`} alt="" decoding="async"
        style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", display: "block" }} />
    </div>);

}

/* ============================================================
   FRONT A — THE CASE FILE  (hero direction)
   ============================================================ */
function FrontCaseFile() {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: "0", display: "flex", flexDirection: "column" }}>
      <div style={{ padding: "46px 40px 0" }}>
        <h1 className="booktitle rough smudge" style={{ fontSize: 84, margin: 0 }}>No One<br />Did It</h1>
        <div className="subtitle" style={{ fontSize: 18, marginTop: 14, maxWidth: 360, lineHeight: 1.3 }}>
          Responsibility Laundering,<br />from the Scapegoat to the Algorithm
        </div>
      </div>

      {/* central exhibit — defendant & judge portraits */}
      <div style={{ flex: 1, position: "relative", margin: "20px 40px 0" }}>
        {/* DEFENDANT (goat) */}
        <div style={{ position: "absolute", left: "34%", top: "59%", width: 236, height: 312, transform: "translate(-50%,-50%)", borderRadius: "50%", overflow: "hidden", border: "7px solid var(--red)", boxShadow: "0 0 0 2px rgba(50,36,20,.35), 0 10px 26px rgba(40,28,14,.4)" }}>
          <img src="assets/crops/goat.png" alt="" decoding="async" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", display: "block" }} />
        </div>

        {/* JUDGE (owl) */}
        <div style={{ position: "absolute", left: "71%", top: "29%", width: 156, height: 206, transform: "translate(-50%,-50%)", borderRadius: "50%", overflow: "hidden", border: "6px solid var(--red)", boxShadow: "0 0 0 2px rgba(50,36,20,.35), 0 10px 22px rgba(40,28,14,.4)" }}>
          <img src="assets/crops/judge.png" alt="" decoding="async" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", display: "block" }} />
        </div>
      </div>

      {/* footer */}
      <div style={{ padding: "18px 40px 30px" }}>
        <div className="rule" style={{ marginBottom: 12 }} />
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end" }}>
          <div className="label tight" style={{ fontSize: 12, color: "var(--ink)" }}>xiaolai</div>
          <div className="label" style={{ fontSize: 10 }}>Evidence&nbsp;·&nbsp;Do&nbsp;Not&nbsp;Remove</div>
        </div>
      </div>
    </div>);

}

/* ============================================================
   FRONT B — THE DEFENDANT (illustration-led, charcoal court)
   ============================================================ */
function FrontDefendant() {
  return (
    <div className="kraft" style={{ width: 600, height: 925, padding: 0, position: "relative", display: "flex", flexDirection: "column" }}>
      <img src="assets/crops/cover_def.png" alt="" decoding="async" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover" }} />
      <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, color-mix(in srgb, var(--c-ink) 78%, transparent) 0%, color-mix(in srgb, var(--c-ink) 12%, transparent) 34%, color-mix(in srgb, var(--c-ink) 20%, transparent) 60%, color-mix(in srgb, var(--c-ink) 90%, transparent) 100%)" }} />
      <div style={{ position: "relative", padding: "40px 44px 0", textAlign: "center" }}>
        <h1 className="booktitle rough smudge" style={{ fontSize: 80, margin: "12px 0 0", color: "var(--on-dark)" }}>No One<br />Did It</h1>
      </div>
      <div style={{ flex: 1 }} />
      <div style={{ position: "relative", padding: "0 44px 40px", textAlign: "center" }}>
        <div className="subtitle" style={{ fontSize: 18, color: "var(--on-dark)", marginBottom: 14, lineHeight: 1.3 }}>
          Responsibility Laundering, from the Scapegoat to the Algorithm
        </div>
        <div className="label" style={{ color: "var(--on-dark-soft)", letterSpacing: ".26em" }}>Written&nbsp;by&nbsp;Xiaolai&nbsp;Li</div>
      </div>
    </div>);

}

/* ============================================================
   FRONT C — THE EVIDENCE WALL (pinned, red string)
   ============================================================ */
function FrontEvidenceWall() {
  const pins = [
  { pos: "6% 34%", x: 38, y: 70, w: 150, h: 130, r: -4, z: 320 },
  { pos: "82% 16%", x: 360, y: 96, w: 170, h: 140, r: 3, z: 300 },
  { pos: "40% 16%", x: 60, y: 470, w: 160, h: 150, r: -2, z: 330 },
  { pos: "14% 84%", x: 370, y: 500, w: 160, h: 140, r: 4, z: 300 }];

  return (
    <div className="coal" style={{ width: 600, height: 925, padding: 0, position: "relative", overflow: "hidden" }}>
      {/* red string */}
      <svg viewBox="0 0 600 925" style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }} aria-hidden="true">
        <polyline points="110,130 300,300 440,170 300,560 460,580 130,540"
        fill="none" stroke="var(--red)" strokeWidth="2" opacity="0.7" />
      </svg>
      {pins.map((p, i) =>
      <div key={i} style={{ position: "absolute", left: p.x, top: p.y, width: p.w, height: p.h, transform: `rotate(${p.r}deg)` }}>
          <Crop src={`pin${i}`} h="100%" style={{ border: "5px solid var(--frame-light)", boxShadow: "0 8px 20px rgba(0,0,0,.5)" }} />
          <div style={{ position: "absolute", top: -7, left: "50%", width: 12, height: 12, borderRadius: "50%", background: "var(--red)", transform: "translateX(-50%)", boxShadow: "0 1px 3px rgba(0,0,0,.6)" }} />
        </div>
      )}
      {/* central title card */}
      <div style={{ position: "absolute", left: "50%", top: "47%", transform: "translate(-50%,-50%) rotate(-2deg)", width: 300 }}>
        <div className="insert" style={{ padding: "22px 18px", textAlign: "center" }}>
          <h1 className="booktitle rough" style={{ fontSize: 46, margin: 0, color: "var(--ink)" }}>No One<br />Did It</h1>
          <div className="subtitle" style={{ fontSize: 14, marginTop: 10 }}>Responsibility Laundering,<br />from the Scapegoat to the Algorithm</div>
        </div>
      </div>
      <div className="label" style={{ position: "absolute", bottom: 30, left: 0, right: 0, textAlign: "center", color: "var(--on-dark-soft)", letterSpacing: ".3em" }}>Xiaolai&nbsp;Books</div>
    </div>);

}

window.Dossier = Object.assign(window.Dossier || {}, {
  Seal, Crop, ART, ConfidentialStamp, RoundStamp, FrontCaseFile, FrontDefendant, FrontEvidenceWall
});
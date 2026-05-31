/* global React */
/* ============================================================
   NO ONE DID IT — Cartoon edition
   A flat, hand-drawn animal courtroom. The goat in the dock,
   an owl judge, a jury of critters, a gallery of beasts.
   Built from simple primitives; rough filter gives the sketch wobble.
   ============================================================ */
const STROKE = "#2c241a";
const SW = 3;

/* ---- a generic critter face (jury + audience) ---- */
function Critter({ x, y, r, fill, ears = "none", earFill, accent, sw = SW, eyeOpen = true }) {
  const ef = earFill || fill;
  return (
    <g>
      {ears === "long" && <>
        <ellipse cx={x - r*0.45} cy={y - r*1.15} rx={r*0.28} ry={r*0.8} fill={ef} stroke={STROKE} strokeWidth={sw} transform={`rotate(-12 ${x - r*0.45} ${y - r*1.15})`} />
        <ellipse cx={x + r*0.45} cy={y - r*1.15} rx={r*0.28} ry={r*0.8} fill={ef} stroke={STROKE} strokeWidth={sw} transform={`rotate(12 ${x + r*0.45} ${y - r*1.15})`} />
      </>}
      {ears === "pointy" && <>
        <polygon points={`${x-r*0.9},${y-r*0.3} ${x-r*0.3},${y-r*0.5} ${x-r*0.4},${y-r*1.25}`} fill={ef} stroke={STROKE} strokeWidth={sw} strokeLinejoin="round" />
        <polygon points={`${x+r*0.9},${y-r*0.3} ${x+r*0.3},${y-r*0.5} ${x+r*0.4},${y-r*1.25}`} fill={ef} stroke={STROKE} strokeWidth={sw} strokeLinejoin="round" />
      </>}
      {ears === "round" && <>
        <circle cx={x - r*0.7} cy={y - r*0.75} r={r*0.42} fill={ef} stroke={STROKE} strokeWidth={sw} />
        <circle cx={x + r*0.7} cy={y - r*0.75} r={r*0.42} fill={ef} stroke={STROKE} strokeWidth={sw} />
      </>}
      <circle cx={x} cy={y} r={r} fill={fill} stroke={STROKE} strokeWidth={sw} />
      {accent && <ellipse cx={x} cy={y + r*0.35} rx={r*0.5} ry={r*0.38} fill={accent} stroke={STROKE} strokeWidth={sw*0.7} />}
      <circle cx={x - r*0.32} cy={y - r*0.05} r={Math.max(2.2, r*0.12)} fill={STROKE} />
      <circle cx={x + r*0.32} cy={y - r*0.05} r={Math.max(2.2, r*0.12)} fill={STROKE} />
    </g>
  );
}

/* ---- the OWL JUDGE ---- */
function OwlJudge({ cx, cy, s = 1 }) {
  return (
    <g transform={`translate(${cx} ${cy}) scale(${s})`}>
      {/* ear tufts */}
      <polygon points="-46,-44 -20,-58 -22,-30" fill="#7d6750" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      <polygon points="46,-44 20,-58 22,-30" fill="#7d6750" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      {/* body */}
      <ellipse cx="0" cy="58" rx="64" ry="56" fill="#7d6750" stroke={STROKE} strokeWidth={SW} />
      {/* white judge wig */}
      <path d="M -58 -18 Q -64 -52 -30 -56 Q 0 -70 30 -56 Q 64 -52 58 -18 Q 60 6 40 14 Q 44 36 28 40 Q 0 48 -28 40 Q -44 36 -40 14 Q -60 6 -58 -18 Z"
            fill="#efe9da" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      {/* head */}
      <circle cx="0" cy="-6" r="40" fill="#8a7159" stroke={STROKE} strokeWidth={SW} />
      {/* facial disk */}
      <ellipse cx="0" cy="0" rx="34" ry="32" fill="#c7b79c" stroke={STROKE} strokeWidth={SW*0.7} />
      {/* big eyes / glasses */}
      <circle cx="-15" cy="-4" r="15" fill="#efe9da" stroke={STROKE} strokeWidth={SW} />
      <circle cx="15" cy="-4" r="15" fill="#efe9da" stroke={STROKE} strokeWidth={SW} />
      <circle cx="-15" cy="-4" r="5" fill={STROKE} />
      <circle cx="15" cy="-4" r="5" fill={STROKE} />
      <line x1="0" y1="-4" x2="0" y2="-4" stroke={STROKE} strokeWidth={SW} />
      <line x1="-30" y1="-6" x2="-31" y2="-10" stroke={STROKE} strokeWidth={SW} />
      <line x1="30" y1="-6" x2="31" y2="-10" stroke={STROKE} strokeWidth={SW} />
      {/* beak */}
      <polygon points="-7,8 7,8 0,24" fill="#caa24a" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
    </g>
  );
}

/* ---- the GOAT defendant (the star) ---- */
function GoatDefendant({ cx, cy, s = 1 }) {
  return (
    <g transform={`translate(${cx} ${cy}) scale(${s})`}>
      {/* shoulders */}
      <path d="M -70 96 Q -64 36 0 34 Q 64 36 70 96 Z" fill="#e7e0d0" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      {/* ears */}
      <ellipse cx="-50" cy="-20" rx="16" ry="34" fill="#d6cdb9" stroke={STROKE} strokeWidth={SW} transform="rotate(34 -50 -20)" />
      <ellipse cx="50" cy="-20" rx="16" ry="34" fill="#d6cdb9" stroke={STROKE} strokeWidth={SW} transform="rotate(-34 50 -20)" />
      {/* horns */}
      <path d="M -22 -44 Q -34 -78 -16 -86" fill="none" stroke={STROKE} strokeWidth={SW*1.4} strokeLinecap="round" />
      <path d="M 22 -44 Q 34 -78 16 -86" fill="none" stroke={STROKE} strokeWidth={SW*1.4} strokeLinecap="round" />
      {/* head */}
      <ellipse cx="0" cy="-18" rx="40" ry="44" fill="#efe9da" stroke={STROKE} strokeWidth={SW} />
      {/* snout */}
      <ellipse cx="0" cy="6" rx="26" ry="22" fill="#e3dac6" stroke={STROKE} strokeWidth={SW*0.8} />
      {/* worried eyes */}
      <ellipse cx="-16" cy="-22" rx="7" ry="8" fill="#fff" stroke={STROKE} strokeWidth={SW*0.7} />
      <ellipse cx="16" cy="-22" rx="7" ry="8" fill="#fff" stroke={STROKE} strokeWidth={SW*0.7} />
      <circle cx="-16" cy="-20" r="3.4" fill={STROKE} />
      <circle cx="16" cy="-20" r="3.4" fill={STROKE} />
      {/* worried brows */}
      <path d="M -26 -34 Q -16 -40 -8 -35" fill="none" stroke={STROKE} strokeWidth={SW*0.9} strokeLinecap="round" />
      <path d="M 26 -34 Q 16 -40 8 -35" fill="none" stroke={STROKE} strokeWidth={SW*0.9} strokeLinecap="round" />
      {/* nostrils + mouth */}
      <circle cx="-7" cy="4" r="2.4" fill={STROKE} />
      <circle cx="7" cy="4" r="2.4" fill={STROKE} />
      <path d="M -8 16 Q 0 12 8 16" fill="none" stroke={STROKE} strokeWidth={SW*0.8} strokeLinecap="round" />
      {/* beard */}
      <path d="M -8 24 Q 0 50 8 24 Q 4 40 -8 24 Z" fill="#e3dac6" stroke={STROKE} strokeWidth={SW*0.7} strokeLinejoin="round" />
    </g>
  );
}

/* ---- a lawyer fox, seen from the back, mid-gesture ---- */
function LawyerFox({ cx, cy, s = 1 }) {
  return (
    <g transform={`translate(${cx} ${cy}) scale(${s})`}>
      {/* suit body */}
      <path d="M -34 90 Q -40 6 0 0 Q 40 6 34 90 Z" fill="#3b3024" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      {/* gesturing arm */}
      <path d="M 26 24 Q 64 8 78 -16" fill="none" stroke="#3b3024" strokeWidth="14" strokeLinecap="round" />
      <path d="M 26 24 Q 64 8 78 -16" fill="none" stroke={STROKE} strokeWidth={SW*0.6} strokeLinecap="round" opacity="0.5" />
      {/* head (back) with pointy ears */}
      <polygon points="-26,-30 -10,-26 -18,-58" fill="#bf6f3f" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      <polygon points="26,-30 10,-26 18,-58" fill="#bf6f3f" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      <circle cx="0" cy="-22" r="26" fill="#c8794a" stroke={STROKE} strokeWidth={SW} />
      {/* white tail tip flick */}
      <path d="M -30 70 Q -58 60 -52 92 Q -40 78 -30 70 Z" fill="#c8794a" stroke={STROKE} strokeWidth={SW} strokeLinejoin="round" />
      <path d="M -52 92 Q -56 80 -48 78" fill="#efe9da" stroke="none" />
    </g>
  );
}

/* ============================================================ */
function CartoonCourt() {
  const jury = [
    { fill:"#c8794a", ears:"pointy" },                          // fox
    { fill:"#cbb9a0", ears:"long" },                            // rabbit
    { fill:"#cf9e9a", ears:"pointy", accent:"#e7bdb8" },        // pig
    { fill:"#7d9460", ears:"none" },                            // frog
    { fill:"#8a6f55", ears:"round" },                           // bear
  ];
  const audience = [
    { fill:"#4a4031", ears:"round" }, { fill:"#534636", ears:"pointy" },
    { fill:"#433a2c", ears:"long" }, { fill:"#5a4c39", ears:"round" },
    { fill:"#3e362a", ears:"pointy" }, { fill:"#544735", ears:"none" },
    { fill:"#473d2e", ears:"long" }, { fill:"#5c4e3b", ears:"round" },
  ];

  return (
    <div className="paper" style={{ width:600, height:925, padding:0, display:"flex", flexDirection:"column", overflow:"hidden" }}>
      <svg viewBox="0 0 600 775" style={{ width:"100%", display:"block" }} className="rough">
        {/* ---------- room ---------- */}
        <rect x="0" y="0" width="600" height="775" fill="#cdbfa3" />
        <rect x="0" y="0" width="600" height="300" fill="#d6cab0" />
        {/* tall windows */}
        <g opacity="0.5">
          <path d="M 70 70 q 0 -34 34 -34 q 34 0 34 34 l 0 150 l -68 0 Z" fill="#bfd0cf" stroke={STROKE} strokeWidth={SW} />
          <path d="M 462 70 q 0 -34 34 -34 q 34 0 34 34 l 0 150 l -68 0 Z" fill="#bfd0cf" stroke={STROKE} strokeWidth={SW} />
        </g>
        {/* seal */}
        <circle cx="300" cy="120" r="46" fill="#c2b496" stroke={STROKE} strokeWidth={SW} />
        <circle cx="300" cy="120" r="30" fill="none" stroke={STROKE} strokeWidth={SW*0.7} />
        <line x1="300" y1="96" x2="300" y2="144" stroke={STROKE} strokeWidth={SW*0.7} />
        <line x1="284" y1="112" x2="316" y2="112" stroke={STROKE} strokeWidth={SW*0.7} />
        <circle cx="288" cy="124" r="7" fill="none" stroke={STROKE} strokeWidth={SW*0.6} />
        <circle cx="312" cy="124" r="7" fill="none" stroke={STROKE} strokeWidth={SW*0.6} />
        {/* wainscot + floor */}
        <rect x="0" y="560" width="600" height="60" fill="#9a8358" />
        <rect x="0" y="620" width="600" height="155" fill="#b7a378" />
        <line x1="0" y1="620" x2="600" y2="620" stroke={STROKE} strokeWidth={SW} />

        {/* spotlight on the goat */}
        <polygon points="300,150 250,640 350,640" fill="#fff7e0" opacity="0.30" />

        {/* ---------- judge bench ---------- */}
        <OwlJudge cx={300} cy={250} s={1} />
        <rect x="150" y="320" width="300" height="120" rx="6" fill="#6e4c2e" stroke={STROKE} strokeWidth={SW} />
        <rect x="150" y="312" width="300" height="16" rx="4" fill="#5e4026" stroke={STROKE} strokeWidth={SW} />
        <rect x="244" y="356" width="112" height="30" rx="4" fill="#c2b496" stroke={STROKE} strokeWidth={SW*0.8} />
        <text x="300" y="376" textAnchor="middle" fontFamily="var(--mono)" fontSize="13" letterSpacing="2" fill="#3b2f1e">JUDGE</text>
        {/* gavel */}
        <g transform="rotate(-24 412 300)">
          <rect x="392" y="292" width="44" height="16" rx="6" fill="#7a5638" stroke={STROKE} strokeWidth={SW} />
          <rect x="408" y="300" width="10" height="34" rx="4" fill="#7a5638" stroke={STROKE} strokeWidth={SW} />
        </g>

        {/* ---------- jury box (left) ---------- */}
        <rect x="14" y="430" width="150" height="150" rx="6" fill="#7a5638" stroke={STROKE} strokeWidth={SW} />
        <rect x="14" y="422" width="150" height="14" rx="4" fill="#5e4026" stroke={STROKE} strokeWidth={SW} />
        {jury.slice(0,3).map((j,i)=>(<Critter key={"j0"+i} x={42 + i*42} y={418} r={17} sw={2.4} {...j} />))}
        {jury.slice(3).map((j,i)=>(<Critter key={"j1"+i} x={62 + i*42} y={452} r={17} sw={2.4} {...j} />))}
        <text x="89" y="555" textAnchor="middle" fontFamily="var(--mono)" fontSize="12" letterSpacing="2" fill="#efe9da">JURY</text>

        {/* ---------- lawyer fox ---------- */}
        <LawyerFox cx={476} cy={500} s={1} />

        {/* ---------- the goat in the dock ---------- */}
        <GoatDefendant cx={300} cy={470} s={1.05} />
        <rect x="214" y="556" width="172" height="120" rx="6" fill="#7a5638" stroke={STROKE} strokeWidth={SW} />
        <rect x="214" y="548" width="172" height="16" rx="4" fill="#5e4026" stroke={STROKE} strokeWidth={SW} />
        <line x1="252" y1="564" x2="252" y2="676" stroke={STROKE} strokeWidth={SW*0.7} opacity="0.5" />
        <line x1="300" y1="564" x2="300" y2="676" stroke={STROKE} strokeWidth={SW*0.7} opacity="0.5" />
        <line x1="348" y1="564" x2="348" y2="676" stroke={STROKE} strokeWidth={SW*0.7} opacity="0.5" />

        {/* ---------- audience gallery (foreground) ---------- */}
        <rect x="0" y="702" width="600" height="73" fill="#8a7350" />
        <rect x="0" y="696" width="600" height="12" fill="#5e4026" />
        {audience.map((a,i)=>(<Critter key={"a"+i} x={44 + i*74} y={726} r={26} sw={2.6} {...a} />))}
      </svg>

      {/* ---------- title plaque ---------- */}
      <div style={{ flex:1, background:"#5e4026", borderTop:`3px solid ${STROKE}`, display:"flex", flexDirection:"column", justifyContent:"center", alignItems:"center", textAlign:"center", padding:"0 24px" }}>
        <div className="stamp" style={{ color:"#cdbfa3", letterSpacing:".3em", marginBottom:6 }}>The People &nbsp;v.&nbsp; No One</div>
        <h1 className="serif-title rough smudge" style={{ fontSize:46, color:"#efe9da", margin:0, whiteSpace:"nowrap" }}>No One Did It</h1>
        <div className="scrawl" style={{ fontSize:20, color:"#e0b9a0", marginTop:4, whiteSpace:"nowrap" }}>&ldquo;the goat pleads not guilty&rdquo;</div>
      </div>
    </div>
  );
}

window.Covers = Object.assign(window.Covers || {}, { CartoonCourt });

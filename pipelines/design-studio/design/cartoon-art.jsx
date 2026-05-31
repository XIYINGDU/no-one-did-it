/* global React */
/* ============================================================
   NO ONE DID IT — Illustrated edition
   Built on the user's animal-courtroom artwork. One image powers
   the whole system: full cover, full-bleed variant, back cover,
   and six chapter openers each cropped to a different beast.
   ============================================================ */
const ART = "assets/animal-court-portrait.png";

/* a zoomed crop window into the artwork, with a rough keyline frame */
function CropPlate({ pos, zoom = 360, h, style }) {
  return (
    <div style={{
      position:"relative", width:"100%", height:h, overflow:"hidden",
      border:"2.5px solid var(--ink)", filter:"url(#scratch)", ...style
    }}>
      <div style={{
        position:"absolute", inset:0,
        backgroundImage:`url(${ART})`, backgroundSize:`${zoom}%`,
        backgroundPosition:pos, backgroundRepeat:"no-repeat",
      }} />
    </div>
  );
}

/* ---------- FRONT · framed illustrated plate ---------- */
function IllustratedFront() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"46px 48px 38px", display:"flex", flexDirection:"column", alignItems:"center", textAlign:"center" }}>
      <div className="kicker">An Illustrated Inquiry &nbsp;·&nbsp; No.&nbsp;0001</div>
      <div className="rule" style={{ alignSelf:"stretch", margin:"16px 0 22px" }} />

      <div style={{ width:"100%", border:"2.5px solid var(--ink)", filter:"url(#scratch)", lineHeight:0 }}>
        <img src={ART} alt="The animal court" style={{ width:"100%", display:"block" }} />
      </div>

      <div style={{ flex:1 }} />
      <h1 className="serif-title rough smudge" style={{ fontSize:78, margin:"22px 0 0", lineHeight:.86 }}>No&nbsp;One<br/>Did&nbsp;It</h1>
      <div style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16, color:"var(--ink-soft)", margin:"12px 0 0", maxWidth:380, lineHeight:1.3 }}>
        How power keeps the benefit and launders the blame
      </div>
      <div style={{ flex:1 }} />
      <div className="rule thin" style={{ alignSelf:"stretch", margin:"0 0 12px" }} />
      <div style={{ display:"flex", justifyContent:"space-between", alignSelf:"stretch", alignItems:"center" }}>
        <div className="stamp">Xiaolai&nbsp;Li</div>
        <div className="stamp" style={{ fontSize:9, opacity:.7 }}>Cover illustration</div>
      </div>
    </div>
  );
}

/* ---------- FRONT · full-bleed dramatic crop ---------- */
function IllustratedFrontBleed() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:0, position:"relative", overflow:"hidden" }}>
      <img src={ART} alt="The animal court" style={{ position:"absolute", inset:0, width:"100%", height:"100%", objectFit:"cover", objectPosition:"50% 38%" }} />
      {/* bottom band */}
      <div style={{ position:"absolute", left:0, right:0, bottom:0, height:330, background:"linear-gradient(180deg, transparent, rgba(18,13,8,.72) 38%, rgba(18,13,8,.94))" }} />
      <div style={{ position:"absolute", left:0, right:0, bottom:40, textAlign:"center", padding:"0 36px" }}>
        <h1 className="serif-title rough smudge" style={{ fontSize:74, margin:0, color:"#f1ebdd", lineHeight:.86 }}>No&nbsp;One<br/>Did&nbsp;It</h1>
        <div className="scrawl" style={{ fontSize:33, color:"#e6c0a4", marginTop:8, lineHeight:1.05 }}>Responsibility&nbsp;Laundering,<br/>from the Scapegoat to the Algorithm</div>
        <div className="stamp" style={{ color:"#c9bfa8", letterSpacing:".24em", marginTop:14 }}>Xiaolai&nbsp;Li</div>
      </div>
    </div>
  );
}

/* ---------- BACK COVER ---------- */
function IllustratedBack() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"46px 48px 38px", display:"flex", flexDirection:"column" }}>
      <div className="kicker">Nonfiction / Power &amp; Institutions</div>
      <div className="rule" style={{ margin:"14px 0 22px" }} />

      {/* the chalkboard line — the book's voice */}
      <div style={{ fontFamily:"var(--serif)", fontWeight:800, fontSize:30, lineHeight:1.04, textTransform:"uppercase", letterSpacing:"-.01em", marginBottom:18 }}>
        Hope is not a defense.<br/>Truth does not care.
      </div>

      <p style={{ fontFamily:"var(--serif)", fontSize:14.5, lineHeight:1.6, margin:"0 0 16px", color:"var(--ink-soft)" }}>
        Civilization never stopped sacrificing substitutes &mdash; it only changed the altar.
        Responsibility laundering is the method by which power keeps the control and the
        benefit while moving blame, liability, and moral cost onto a weaker bearer: a proxy,
        a procedure, a machine, a market, a committee, a record. The goat is always in the
        dock. No one is ever in the chair.
      </p>

      {/* a crop: the defendant */}
      <CropPlate pos="6% 36%" zoom={300} h={188} />
      <div className="scrawl" style={{ fontSize:22, color:"var(--slate)", margin:"10px 0 0" }}>&ldquo;the goat pleads not guilty&rdquo;</div>

      <div style={{ flex:1 }} />
      <div className="rule thin" style={{ marginBottom:14 }} />
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-end" }}>
        <div style={{ maxWidth:250 }}>
          <div className="stamp" style={{ marginBottom:6 }}>About the author</div>
          <div style={{ fontFamily:"var(--serif)", fontSize:12.5, lineHeight:1.45, color:"var(--ink-soft)" }}>
            Xiaolai Li writes on institutions, liability, and the architecture of blame.
          </div>
        </div>
        <div style={{ display:"flex", flexDirection:"column", alignItems:"flex-end", gap:8 }}>
          <div className="barcode" />
          <div className="stamp">Scapegoat&nbsp;Press</div>
        </div>
      </div>
    </div>
  );
}

/* ---------- CHAPTER OPENERS (cropped beasts) ---------- */
const ART_CHAPTERS = [
  { n:"I",   roman:"Chapter One",   altar:"The Substitute", sub:"Bring me a goat",        bearer:"the foreigner, the firstborn", pos:"6% 34%",  zoom:300 },
  { n:"II",  roman:"Chapter Two",   altar:"The Committee",  sub:"Many hands, no hand",     bearer:"the working group",            pos:"82% 16%", zoom:300 },
  { n:"III", roman:"Chapter Three", altar:"The Proxy",      sub:"By other means",          bearer:"the contractor",               pos:"45% 52%", zoom:300 },
  { n:"IV",  roman:"Chapter Four",  altar:"The Machine",    sub:"The bench decided",       bearer:"the algorithm",                pos:"40% 16%", zoom:330 },
  { n:"V",   roman:"Chapter Five",  altar:"The Market",     sub:"An invisible hand",       bearer:"the market",                   pos:"14% 84%", zoom:280 },
  { n:"VI",  roman:"Chapter Six",   altar:"The Record",     sub:"For the minutes",         bearer:"the file",                     pos:"10% 12%", zoom:300 },
];

function IllustratedChapter({ c }) {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"46px 44px 40px", display:"flex", flexDirection:"column" }}>
      <header style={{ display:"flex", justifyContent:"space-between", alignItems:"baseline", marginBottom:18 }}>
        <div className="kicker">{c.roman}</div>
        <div className="stamp">Altar No.&nbsp;{c.n}</div>
      </header>

      <CropPlate pos={c.pos} zoom={c.zoom} h={300} />

      <div style={{ flex:1, display:"flex", flexDirection:"column", justifyContent:"center" }}>
        <div className="serif-title rough-2 smudge" style={{ fontSize:120, lineHeight:.8, color:"var(--ink)", opacity:.14 }}>{c.n}</div>
        <h2 className="serif-title rough" style={{ fontSize:50, margin:"-26px 0 8px" }}>{c.altar}</h2>
        <div className="scrawl" style={{ fontSize:28, color:"var(--slate)", transform:"rotate(-2deg)" }}>&ldquo;{c.sub}&rdquo;</div>
      </div>

      <div className="rule thin" style={{ marginBottom:14 }} />
      <div style={{ display:"flex", alignItems:"center", gap:12 }}>
        <span className="stamp" style={{ whiteSpace:"nowrap" }}>blame&nbsp;&rarr;</span>
        <span className="struck" style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16 }}>{c.bearer}<span className="bar" /></span>
      </div>
    </div>
  );
}

window.Covers = Object.assign(window.Covers || {}, {
  IllustratedFront, IllustratedFrontBleed, IllustratedBack, IllustratedChapter, ART_CHAPTERS
});

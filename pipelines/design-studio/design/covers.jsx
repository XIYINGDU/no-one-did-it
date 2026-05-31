/* global React */
const { useState } = React;

/* ---------- shared bits ---------- */

function Struck({ children, ox, style }) {
  return (
    <span className={"struck" + (ox ? " ox" : "")} style={style}>
      {children}
      <span className="bar" />
    </span>
  );
}

function PadEdge() { return <div className="pad-edge" />; }

/* a faint "exhibit" tag */
function Exhibit({ children, style }) {
  return (
    <div className="stamp" style={{
      display:"inline-block", border:"1.5px solid var(--ink-soft)",
      padding:"3px 9px", filter:"url(#scratch2)", color:"var(--ink-soft)",
      ...style
    }}>{children}</div>
  );
}

/* ============================================================
   FRONT A — "THE STRUCK LIST"
   Every name an inquiry could blame, crossed out. The verdict remains.
   ============================================================ */
const ROSTER = ["The Officer", "The Board", "The Contractor", "The Algorithm", "The Market", "The Committee"];

function FrontStruckList() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"54px 50px 44px", display:"flex", flexDirection:"column" }}>
      <PadEdge />
      <header style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-start" }}>
        <div className="kicker" style={{ maxWidth:230 }}>An Independent Inquiry<br/>into the Findings</div>
        <div className="rubber">Confidential</div>
      </header>

      <div className="rule" style={{ margin:"18px 0 26px" }} />

      {/* the roster, struck out */}
      <div style={{ display:"flex", flexDirection:"column", alignItems:"flex-start", gap:9 }}>
        <div className="stamp" style={{ marginBottom:4 }}>Persons responsible —</div>
        {ROSTER.map((r,i)=>(
          <Struck key={i} ox={i===ROSTER.length-1} style={{ fontFamily:"var(--serif)", fontSize:25, fontWeight:600 }}>{r}</Struck>
        ))}
      </div>

      <div style={{ flex:1 }} />

      {/* the verdict */}
      <div className="scrawl" style={{ fontSize:30, lineHeight:.9, transform:"rotate(-3deg)", marginLeft:6, marginBottom:2 }}>so&nbsp;&mdash;</div>
      <h1 className="serif-title rough smudge" style={{ fontSize:88, margin:"0 0 14px" }}>
        No&nbsp;One<br/>Did&nbsp;It
      </h1>
      <div className="rule thin" style={{ marginBottom:14 }} />
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-end" }}>
        <div style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16, color:"var(--ink-soft)", maxWidth:300, lineHeight:1.25 }}>
          How power keeps the benefit<br/>and launders the blame
        </div>
        <div className="stamp" style={{ textAlign:"right", letterSpacing:".22em" }}>Xiaolai&nbsp;Li</div>
      </div>
    </div>
  );
}

/* ============================================================
   FRONT B — "THE EMPTY CHAIR"
   A courtroom sketch of the defendant's seat — vacant. Drop a real
   sketch into the slot; the vacant frame stands in until then.
   ============================================================ */
function FrontEmptyChair() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"50px 46px 40px", display:"flex", flexDirection:"column" }}>
      <PadEdge />
      <div className="kicker" style={{ textAlign:"center", marginBottom:18 }}>The People &nbsp;v.&nbsp; No One</div>

      {/* the seat */}
      <div style={{ position:"relative", flex:1, display:"flex", alignItems:"center", justifyContent:"center" }}>
        <image-slot
          id="front-chair"
          shape="rect"
          placeholder="drop courtroom sketch — the empty defendant's chair"
          style={{ width:"88%", height:"100%", filter:"url(#scratch2)", background:"transparent", border:"2.5px solid var(--ink)", color:"var(--ink-soft)" }}
        ></image-slot>
        <div className="scrawl" style={{ position:"absolute", bottom:34, right:78, fontSize:25, transform:"rotate(-4deg)", color:"var(--ink-soft)" }}>
          the seat, vacant&nbsp;&darr;
        </div>
      </div>

      <h1 className="serif-title rough smudge" style={{ fontSize:64, textAlign:"center", margin:"30px 0 6px" }}>
        No One Did It
      </h1>
      <div className="kicker" style={{ textAlign:"center", letterSpacing:".26em" }}>How Power Launders Blame &nbsp;·&nbsp; Xiaolai&nbsp;Li</div>
    </div>
  );
}

/* ============================================================
   FRONT C — "THE VERDICT" (charcoal)
   Near-monochrome. The title dominates, roughed like fast chalk.
   ============================================================ */
function FrontVerdict() {
  return (
    <div className="paper dark" style={{ width:600, height:925, padding:"52px 46px 44px", display:"flex", flexDirection:"column" }}>
      <header style={{ display:"flex", justifyContent:"space-between", alignItems:"center" }}>
        <Exhibit style={{ color:"var(--ink-soft)", borderColor:"var(--ink-soft)" }}>Verdict</Exhibit>
        <div className="stamp">Sealed &nbsp;//&nbsp; No.&nbsp;0001</div>
      </header>

      <div style={{ flex:1, display:"flex", flexDirection:"column", justifyContent:"center" }}>
        <div className="scrawl" style={{ fontSize:28, color:"var(--slate)", transform:"rotate(-2deg)", marginBottom:10, marginLeft:4 }}>
          after all of it&hellip;
        </div>
        <h1 className="serif-title rough-2 smudge" style={{ fontSize:120, margin:0 }}>No</h1>
        <h1 className="serif-title rough-2 smudge" style={{ fontSize:120, margin:"-12px 0 0" }}>One</h1>
        <div style={{ display:"flex", alignItems:"baseline", gap:18 }}>
          <Struck ox style={{ fontFamily:"var(--serif)", fontWeight:800, fontSize:120, textTransform:"uppercase", color:"var(--ink)", lineHeight:.8 }}>Did</Struck>
          <h1 className="serif-title rough-2 smudge" style={{ fontSize:120, margin:"-12px 0 0" }}>It</h1>
        </div>
      </div>

      <div className="rule thin" style={{ marginBottom:16, background:"var(--ink-soft)" }} />
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-end" }}>
        <div style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16, color:"var(--ink-soft)", maxWidth:280, lineHeight:1.3 }}>
          Responsibility laundering and the<br/>science of the missing hand
        </div>
        <div className="stamp" style={{ textAlign:"right" }}>Xiaolai&nbsp;Li</div>
      </div>
    </div>
  );
}

/* ============================================================
   BACK COVER — matches the struck-list system
   ============================================================ */
function BackCover() {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"50px 48px 40px", display:"flex", flexDirection:"column" }}>
      <div className="kicker">Nonfiction / Power &amp; Institutions</div>
      <div className="rule" style={{ margin:"16px 0 26px" }} />

      <p style={{ fontFamily:"var(--serif)", fontSize:17, lineHeight:1.5, margin:"0 0 18px", maxWidth:"46ch" }}>
        Civilization never stopped sacrificing substitutes. It only changed the altar.
      </p>
      <p style={{ fontFamily:"var(--serif)", fontSize:14.5, lineHeight:1.62, margin:"0 0 16px", color:"var(--ink-soft)" }}>
        Responsibility laundering is the recurring method by which power keeps the
        control and the benefit while moving blame, liability, and moral cost onto a
        weaker bearer &mdash; a proxy, a procedure, a machine, a market, a committee, a
        record. This book follows the laundered hand from the temple to the terms of
        service, and asks the question every inquiry is built to never answer.
      </p>

      <div className="scrawl" style={{ fontSize:26, color:"var(--slate)", transform:"rotate(-1.5deg)", margin:"6px 0 14px" }}>
        &ldquo;Someone benefited. No one did it.&rdquo;
      </div>

      <div style={{ display:"flex", flexDirection:"column", gap:6, marginBottom:4 }}>
        <div className="stamp">Where the blame was filed —</div>
        <div style={{ display:"flex", gap:14, flexWrap:"wrap" }}>
          {["the proxy","the procedure","the machine","the market"].map((t,i)=>(
            <Struck key={i} style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16 }}>{t}</Struck>
          ))}
        </div>
      </div>

      <div style={{ flex:1 }} />
      <div className="rule thin" style={{ marginBottom:16 }} />
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-end" }}>
        <div style={{ maxWidth:260 }}>
          <div className="stamp" style={{ marginBottom:6 }}>About the author</div>
          <div style={{ fontFamily:"var(--serif)", fontSize:13, lineHeight:1.45, color:"var(--ink-soft)" }}>
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

/* ============================================================
   CHAPTER COVERS — the altars
   ============================================================ */
const CHAPTERS = [
  { n:"I",   roman:"Chapter One",   altar:"The Substitute", sub:"Bring me a goat", bearer:"the foreigner, the firstborn" },
  { n:"II",  roman:"Chapter Two",   altar:"The Committee",  sub:"Many hands, no hand", bearer:"the working group" },
  { n:"III", roman:"Chapter Three", altar:"The Proxy",      sub:"By other means", bearer:"the contractor" },
  { n:"IV",  roman:"Chapter Four",  altar:"The Machine",    sub:"The model decided", bearer:"the algorithm" },
  { n:"V",   roman:"Chapter Five",  altar:"The Market",     sub:"An invisible hand", bearer:"the market" },
  { n:"VI",  roman:"Chapter Six",   altar:"The Record",     sub:"For the minutes", bearer:"the file" },
];

function ChapterCover({ c }) {
  return (
    <div className="paper" style={{ width:600, height:925, padding:"48px 44px 40px", display:"flex", flexDirection:"column" }}>
      <PadEdge />
      <header style={{ display:"flex", justifyContent:"space-between", alignItems:"baseline" }}>
        <div className="kicker">{c.roman}</div>
        <div className="stamp">Altar No.&nbsp;{c.n}</div>
      </header>

      <div style={{ flex:1, display:"flex", flexDirection:"column", justifyContent:"center" }}>
        <div className="serif-title rough-2 smudge" style={{ fontSize:150, lineHeight:.8, color:"var(--ink)", opacity:.16 }}>{c.n}</div>
        <h2 className="serif-title rough" style={{ fontSize:54, margin:"-30px 0 8px" }}>{c.altar}</h2>
        <div className="scrawl" style={{ fontSize:30, color:"var(--slate)", transform:"rotate(-2deg)" }}>&ldquo;{c.sub}&rdquo;</div>
      </div>

      <div className="rule thin" style={{ marginBottom:14 }} />
      <div style={{ display:"flex", alignItems:"center", gap:12 }}>
        <span className="stamp" style={{ whiteSpace:"nowrap" }}>blame&nbsp;&rarr;</span>
        <Struck style={{ fontFamily:"var(--serif)", fontStyle:"italic", fontSize:16 }}>{c.bearer}</Struck>
      </div>
    </div>
  );
}

window.Covers = { FrontStruckList, FrontEmptyChair, FrontVerdict, BackCover, ChapterCover, CHAPTERS };

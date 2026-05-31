-- pipelines/epub/strip_inline_styles.lua
--
-- Pandoc Lua filter, applied during build_kdp_epub.py, that:
--   (1) removes inline `style="…"` attributes from all attribute-bearing
--       elements (Image / Span / Div / Header / Link / Code / CodeBlock /
--       Table / Cell / Row);
--   (2) clears Table column widths so pandoc emits no inline
--       `<col style="width:N%">` in the generated XHTML.
--
-- All styling lives in book/design/epub/kdp.css. Per rule 16, the manuscript and the
-- generated XHTML carry only semantic markup; presentation is the CSS's job.

local function strip(el)
  if el.attr and el.attr.attributes and el.attr.attributes.style then
    el.attr.attributes.style = nil
  end
  return el
end

function Image(el)     return strip(el) end
function Span(el)      return strip(el) end
function Div(el)       return strip(el) end
function Header(el)    return strip(el) end
function Link(el)      return strip(el) end
function Code(el)      return strip(el) end
function CodeBlock(el) return strip(el) end
function Cell(el)      return strip(el) end
function Row(el)       return strip(el) end

function Table(t)
  if t.attr and t.attr.attributes and t.attr.attributes.style then
    t.attr.attributes.style = nil
  end
  for i = 1, #t.colspecs do
    -- t.colspecs[i] is {alignment, ColWidth}; setting ColWidth to
    -- pandoc.ColWidthDefault tells the HTML writer to emit no inline
    -- <col style="width:N%"> for this column.
    t.colspecs[i][2] = "ColWidthDefault"
  end
  return t
end

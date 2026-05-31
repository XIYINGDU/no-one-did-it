-- pipelines/epub/mark_chapter_openers.lua
--
-- Pandoc Lua filter, applied during build_kdp_epub.py, that wraps the first
-- prose paragraph after each chapter heading (# Part / # Chapter at H1 level)
-- in a `<div class="chapter-opener">`. The .chapter-opener > p::first-letter
-- CSS rule then renders a drop cap on the chapter's opening letter.
--
-- "First prose paragraph" = the first Para that appears after the H1, skipping
-- any intervening BlockQuote (chapter epigraph) and any Header (subsection
-- title that some chapters open with).
--
-- Part dividers are excluded: their H1 carries the `part-heading` class, and
-- their body is the divider plate (no prose). Front matter and back matter
-- are excluded for the same reason: their H1s carry no following prose that
-- would benefit from a drop cap.

function Pandoc(doc)
  local seeking = false
  local new_blocks = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level == 1 then
      -- Start seeking after the chapter heading, but NOT after part-divider
      -- headings (they carry `.part-heading`) and NOT after front/back matter
      -- headings that the assembler emits ("Preface", "A Note on Cases",
      -- "References", "Selected Bibliography", "Cases at a Glance", etc.).
      local is_part_divider =
        block.classes and block.classes:includes("part-heading")
      local is_chapter = false
      if block.content and block.content[1] then
        local first = block.content[1]
        if first.t == "Str" and first.text == "Chapter" then
          is_chapter = true
        end
      end
      seeking = is_chapter and not is_part_divider
      table.insert(new_blocks, block)
    elseif seeking and block.t == "Para" then
      seeking = false
      -- Wrap this Para in a Div with class `chapter-opener`.
      local div = pandoc.Div({block}, pandoc.Attr("", {"chapter-opener"}, {}))
      table.insert(new_blocks, div)
    else
      -- BlockQuote (epigraph), Header (subsection), etc. — pass through.
      table.insert(new_blocks, block)
    end
  end
  doc.blocks = new_blocks
  return doc
end

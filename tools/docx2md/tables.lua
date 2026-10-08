-- Convert DOCX layout tables into Markdown-friendly blocks.
local function cell_blocks(cell) return cell.contents end

local function all_cells(tbl)
  local cells = {}
  local function add_rows(rows) for _, r in ipairs(rows) do for _, c in ipairs(r.cells) do table.insert(cells, c) end end end
  add_rows(tbl.head.rows)
  for _, b in ipairs(tbl.bodies) do add_rows(b.head); add_rows(b.body) end
  add_rows(tbl.foot.rows)
  return cells
end

local function inlines_to_text(inls)
  local out = {}
  for _, il in ipairs(inls) do
    if il.t == 'LineBreak' or il.t == 'SoftBreak' then table.insert(out, '\n')
    elseif il.t == 'Space' then table.insert(out, ' ')
    elseif il.t == 'Str' or il.t == 'Code' then table.insert(out, il.text)
    elseif il.content then table.insert(out, inlines_to_text(il.content))
    end
  end
  return table.concat(out)
end

local function blocks_to_text(blocks)
  local parts = {}
  for _, b in ipairs(blocks) do
    if b.content and type(b.content) == 'table' and (b.t == 'Para' or b.t == 'Plain') then
      table.insert(parts, inlines_to_text(b.content))
    elseif b.t == 'CodeBlock' then table.insert(parts, b.text)
    else table.insert(parts, pandoc.utils.stringify(b)) end
  end
  return table.concat(parts, '\n')
end

local function starts_with_strong(blocks)
  local b = blocks[1]
  return b and (b.t == 'Para' or b.t == 'Plain') and b.content[1] and b.content[1].t == 'Strong'
end

-- Flatten a multi-block cell into one Plain so GFM pipe tables can be used.
local function flatten(cell)
  local inl = {}
  for i, b in ipairs(cell.contents) do
    if i > 1 then table.insert(inl, pandoc.RawInline('html', '<br>')) end
    if b.t == 'Para' or b.t == 'Plain' then
      for _, x in ipairs(b.content) do
        if x.t == 'LineBreak' then table.insert(inl, pandoc.RawInline('html', '<br>')) else table.insert(inl, x) end
      end
    elseif b.t == 'BulletList' or b.t == 'OrderedList' then
      for j, item in ipairs(b.content) do
        if j > 1 then table.insert(inl, pandoc.RawInline('html', '<br>')) end
        table.insert(inl, pandoc.Str('• '))
        for _, x in ipairs(pandoc.utils.blocks_to_inlines(item)) do table.insert(inl, x) end
      end
    else
      for _, x in ipairs(pandoc.utils.blocks_to_inlines({b})) do table.insert(inl, x) end
    end
  end
  cell.contents = { pandoc.Plain(inl) }
  return cell
end

local function Table(tbl)
  local cells = all_cells(tbl)
  if #cells == 1 then
    local blocks = cell_blocks(cells[1])
    if starts_with_strong(blocks) then
      -- Callout box: bold title + body → blockquote
      return pandoc.BlockQuote(blocks)
    else
      return pandoc.CodeBlock((blocks_to_text(blocks):gsub('\194\160', ' ')), pandoc.Attr('', {'text'}))
    end
  end
  local function fix_rows(rows) for _, r in ipairs(rows) do for k, c in ipairs(r.cells) do r.cells[k] = flatten(c) end end end
  fix_rows(tbl.head.rows)
  for _, b in ipairs(tbl.bodies) do fix_rows(b.head); fix_rows(b.body) end
  fix_rows(tbl.foot.rows)
  return tbl
end

local CODE_STYLES = { CodeBlock = true, CodeSmall = true, CodeText = true, PrepCode = true }

local function Div(div)
  local style = div.attributes['custom-style']
  if style == nil then return nil end
  if CODE_STYLES[style] then
    return pandoc.CodeBlock((blocks_to_text(div.content):gsub('\194\160', ' ')), pandoc.Attr('', {'text'}))
  end
  return div.content
end

local function Span(span)
  if span.attributes['custom-style'] then return span.content end
end

local function Strong(s)
  local last = s.content[#s.content]
  if last and (last.t == 'LineBreak' or last.t == 'SoftBreak') then
    s.content:remove(#s.content)
    return { s, pandoc.LineBreak() }
  end
end

local function CodeBlock(cb)
  cb.text = cb.text:gsub('\194\160', ' ')
  return cb
end

return { { Strong = Strong }, { Div = Div, Span = Span }, { Table = Table }, { CodeBlock = CodeBlock } }

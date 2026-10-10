--[[
CS-AML specification release filter (pandoc >= 3.10, writers: latex, docx).

* Reads version / status / date from the document's own status block and
  sets title-page metadata (title comes from -M doctitle=...).
* Keeps every source block (including *[v0.1.x · ...]* change tags) unchanged;
  only presentation is adjusted:
  - status block: soft breaks become line breaks (one field per line);
  - tables: content-based relative column widths when the source table is wider
    than the page; smaller font for many columns; landscape for >= 9 columns (PDF);
  - code blocks / ASCII diagrams: monospace, never re-flowed; font size is scaled
    so the longest line fits. Blocks containing box-drawing characters are never
    wrapped; long single-line flows without box drawing (> ~120 chars) are wrapped
    with a visible continuation marker in PDF only;
  - inline code: break opportunities after / . _ - , = & ? : in PDF.
]]

local stringify = pandoc.utils.stringify
local is_latex = FORMAT:match('latex') ~= nil
local is_docx = FORMAT:match('docx') ~= nil

local script_dir = PANDOC_SCRIPT_FILE and PANDOC_SCRIPT_FILE:match('^(.*)[/\\]') or '.'

-- PDF page geometry (A4, 20 mm side margins) -> usable widths in pt
local TEXTWIDTH_PT = 170 * 72.27 / 25.4      -- 483.7 pt portrait
local MONO_ADV = 0.602                       -- DejaVu Sans Mono advance (em)
local DOCX_TEXTWIDTH_PT = 170 * 72 / 25.4    -- 481.9 pt (A4, 2 cm margins)
local DOCX_MONO_ADV = 0.55                   -- Consolas advance (em)

local function ulen(s)
  return utf8.len(s) or #s
end

local function latex_escape(s)
  return (s:gsub('[\\{}$&#^_%%~-]', function(c)
    if c == '\\' then return '\\textbackslash{}'
    elseif c == '^' then return '\\textasciicircum{}'
    elseif c == '~' then return '\\textasciitilde{}'
    elseif c == '-' then return '{-}'
    else return '\\' .. c end
  end))
end

local function xml_escape(s)
  return (s:gsub('[<>&"]', { ['<'] = '&lt;', ['>'] = '&gt;', ['&'] = '&amp;', ['"'] = '&quot;' }))
end

-- ---------------------------------------------------------------- metadata --

local function extract_status(blocks)
  local text = {}
  for i = 1, math.min(#blocks, 30) do
    text[#text + 1] = stringify(blocks[i])
  end
  local s = table.concat(text, '\n')
  local version, status, date
  version, status, date = s:match('Version: (%d+%.%d+%.%d+) — ([^(\n]-) %((%d%d%d%d%-%d%d%-%d%d)')
  if not version then
    status, date, version = s:match('Status: ([^(\n]-) %((%d%d%d%d%-%d%d%-%d%d).-Version: (%d+%.%d+%.%d+)')
  end
  local tag = s:match('tag (v%d+%.%d+%.%d+%-spec)')
  if status then status = status:gsub('%s+$', '') end
  return version, status, date, tag
end

local function read_file(path)
  local f = io.open(path, 'r')
  if not f then return '' end
  local c = f:read('a')
  f:close()
  return c
end

-- ------------------------------------------------------------------ tables --

local function col_count(tbl)
  return #tbl.colspecs
end

local function set_widths(tbl)
  -- The gfm reader leaves every column at ColWidthDefault (natural width, no wrapping).
  -- Tables whose natural width would exceed the page get content-based relative widths.
  local n = #tbl.colspecs
  local sum, maxl, lword, cnt = {}, {}, {}, {}
  for j = 1, n do sum[j], maxl[j], lword[j], cnt[j] = 0, 0, 0, 0 end
  local function scan(rows)
    for _, row in ipairs(rows) do
      local j = 1
      for _, cell in ipairs(row.cells) do
        if j <= n then
          local t = stringify(cell.contents)
          local l = ulen(t)
          sum[j] = sum[j] + l
          cnt[j] = cnt[j] + 1
          if l > maxl[j] then maxl[j] = l end
          for w in t:gmatch('[^%s,/]+') do   -- PDF breaks after , and / (see Str)
            local wl = ulen(w)
            if wl > lword[j] then lword[j] = wl end
          end
        end
        j = j + (cell.col_span or 1)
      end
    end
  end
  scan(tbl.head.rows)
  for _, body in ipairs(tbl.bodies) do scan(body.body) end
  local natural = 0
  for j = 1, n do natural = natural + maxl[j] + 3 end
  if natural <= 90 then return false end
  local weight, total = {}, 0
  for j = 1, n do
    local avg = cnt[j] > 0 and sum[j] / cnt[j] or 1
    local w = math.max(0.65 * avg + 0.35 * math.min(maxl[j], 2.5 * avg + 10), math.min(lword[j], 28), 3)
    weight[j] = w
    total = total + w
  end
  -- minimum share so that the longest word of each column fits (approx. 9 pt bold DejaVu Sans)
  local minf, msum = {}, 0
  local charw = n >= 5 and 4.6 or 5.6   -- \\scriptsize vs \\footnotesize/\\small bold
  for j = 1, n do
    minf[j] = (math.min(lword[j], 24) * charw + 8) / 470
    msum = msum + minf[j]
  end
  if msum > 0.85 then
    for j = 1, n do minf[j] = minf[j] * 0.85 / msum end
  end
  -- water-filling: columns below their minimum are fixed, the rest share the remainder
  local widths, fixed = {}, {}
  for _ = 1, n do
    local free_w, rem = 0, 1
    for j = 1, n do
      if fixed[j] then rem = rem - minf[j] else free_w = free_w + weight[j] end
    end
    local changed = false
    for j = 1, n do
      if not fixed[j] then
        widths[j] = rem * weight[j] / free_w
        if widths[j] < minf[j] then fixed[j] = true; changed = true end
      else
        widths[j] = minf[j]
      end
    end
    if not changed then break end
  end
  for j = 1, n do
    tbl.colspecs[j] = { tbl.colspecs[j][1], widths[j] }
  end
  return true
end

local function Table(tbl)
  set_widths(tbl)
  local n = col_count(tbl)
  if is_latex then
    local size, landscape = '\\small', false
    if n >= 9 then size, landscape = '\\scriptsize', true
    elseif n >= 5 then size = '\\scriptsize'
    elseif n >= 3 then size = '\\footnotesize' end
    local pre = '\\begingroup' .. size .. '\\setlength{\\tabcolsep}{3.5pt}\\sloppy'
    local post = '\\endgroup'
    if landscape then
      pre = '\\begin{landscape}' .. pre
      post = post .. '\\end{landscape}'
    end
    return { pandoc.RawBlock('latex', pre), tbl, pandoc.RawBlock('latex', post) }
  end
  -- DOCX: table paragraph styles (Table Text / Table Text Small) are applied by release.py
  return tbl
end

-- -------------------------------------------------------------- code blocks --

local BOX_PATTERN = '\226[\148\149]'   -- U+2500..U+257F (box drawing) in UTF-8

local function CodeBlock(el)
  local text = el.text:gsub('\t', '    ')
  local maxlen = 0
  for line in (text .. '\n'):gmatch('(.-)\n') do
    local l = ulen(line)
    if l > maxlen then maxlen = l end
  end
  if maxlen == 0 then maxlen = 1 end
  local has_box = text:find(BOX_PATTERN) ~= nil
  if is_latex then
    local avail = TEXTWIDTH_PT - 14
    local size = math.min(8.5, avail / (MONO_ADV * maxlen))
    local wrap = false
    if size < 5.5 and not has_box then
      size, wrap = 7, true
    end
    size = math.max(size, 4.5)
    size = math.floor(size * 10) / 10
    local opts = string.format(
      'fontsize=\\fontsize{%.1f}{%.1f}\\selectfont,frame=leftline,framerule=0.6pt,rulecolor=\\color{black!35},framesep=6pt,xleftmargin=2pt',
      size, size * 1.22)
    if wrap then
      opts = opts .. ',breaklines=true,breakanywhere=true'
    end
    return pandoc.RawBlock('latex',
      '\\begin{Verbatim}[' .. opts .. ']\n' .. text .. '\n\\end{Verbatim}')
  elseif is_docx then
    local size = math.min(9, DOCX_TEXTWIDTH_PT / (DOCX_MONO_ADV * maxlen))
    size = math.max(size, 5.5)
    local hp = math.floor(size * 2)   -- half-points
    local rpr = string.format(
      '<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas" w:eastAsia="Consolas"/><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>',
      hp, hp)
    local runs = {}
    local first = true
    for line in (text .. '\n'):gmatch('(.-)\n') do
      if not first then runs[#runs + 1] = '<w:r>' .. rpr .. '<w:br/></w:r>' end
      first = false
      runs[#runs + 1] = '<w:r>' .. rpr .. '<w:t xml:space="preserve">' .. xml_escape(line) .. '</w:t></w:r>'
    end
    return pandoc.RawBlock('openxml',
      '<w:p><w:pPr><w:pStyle w:val="SourceCode"/></w:pPr>' .. table.concat(runs) .. '</w:p>')
  end
end

local function Code(el)
  if not is_latex then return nil end
  local brk = ulen(el.text) > 6
  local out = {}
  for _, cp in utf8.codes(el.text) do
    local c = utf8.char(cp)
    out[#out + 1] = latex_escape(c)
    if brk and c:match('^[/%.,=?:_&%-]$') then out[#out + 1] = '\\allowbreak{}' end
  end
  return pandoc.RawInline('latex', '\\texttt{' .. table.concat(out) .. '}')
end

local function Str(el)
  if not is_latex then return nil end
  local long = ulen(el.text) > 20 and el.text:find('_')
  local seps = el.text:find('/') or (ulen(el.text) > 6 and el.text:find(','))
  if not long and not seps then return nil end
  local out = {}
  for _, cp in utf8.codes(el.text) do
    local c = utf8.char(cp)
    out[#out + 1] = latex_escape(c)
    if (long and c == '_') or (seps and (c == ',' or c == '/')) then out[#out + 1] = '\\allowbreak{}' end
  end
  return pandoc.RawInline('latex', table.concat(out))
end

-- Consecutive one-line code blocks (an artefact of the DOCX->Markdown conversion, e.g. the
-- IA object hierarchy) are presented as one block so diagrams keep their shape.
local function merge_code(blocks)
  local out = pandoc.Blocks({})
  for _, b in ipairs(blocks) do
    local prev = out[#out]
    if b.t == 'CodeBlock' and prev and prev.t == 'CodeBlock'
        and table.concat(prev.classes, ' ') == table.concat(b.classes, ' ') then
      prev.text = prev.text .. '\n' .. b.text
    else
      out:insert(b)
    end
  end
  return out
end

-- status block: one field per line
local function BlockQuote(bq)
  local first = stringify(bq.content[1] or pandoc.Para({}))
  if first:match('^Document status') then
    return bq:walk({ SoftBreak = function() return pandoc.LineBreak() end })
  end
end

-- ------------------------------------------------------------------ driver --

function Pandoc(doc)
  local version, status, date, tag = extract_status(doc.blocks)
  version = version or stringify(doc.meta.docversion or '')
  status = status or 'Approved Internal Specification Baseline'
  date = date or ''
  local title = stringify(doc.meta.doctitle or 'CS-AML')
  if not version or version == '' then
    io.stderr:write('WARNING: no version found in status block\n')
  end

  doc.blocks = doc.blocks:walk({ BlockQuote = BlockQuote })
  doc.blocks = doc.blocks:walk({ Blocks = merge_code })
  doc.blocks = merge_code(doc.blocks)
  doc.blocks = doc.blocks:walk({ Table = Table })   -- widths from source text first
  doc.blocks = doc.blocks:walk({ CodeBlock = CodeBlock, Code = Code, Str = Str })

  doc.meta.title = pandoc.MetaInlines({ pandoc.Str(title) })
  local sub = 'Version ' .. version .. ' — ' .. status
  if tag then sub = sub .. ' (tag ' .. tag .. ')' end
  doc.meta.subtitle = pandoc.MetaInlines(pandoc.Inlines(sub))
  doc.meta.date = pandoc.MetaInlines(pandoc.Inlines(date))
  doc.meta['toc-title'] = pandoc.MetaInlines(pandoc.Inlines('Contents'))

  if is_latex then
    local defs = string.format(
      '\\newcommand{\\csamldoc}{%s}\n\\newcommand{\\csamlversion}{%s}\n\\newcommand{\\csamlstatus}{%s}\n\\newcommand{\\csamldate}{%s}\n\\newcommand{\\csamltag}{%s}\n',
      latex_escape(title), latex_escape(version), latex_escape(status), latex_escape(date),
      latex_escape(tag or ''))
    local hi = doc.meta['header-includes']
    local list = pandoc.List()
    if hi then
      if hi.t == 'MetaList' then list = hi else list:insert(hi) end
    end
    list:insert(pandoc.MetaBlocks({ pandoc.RawBlock('latex', defs) }))
    list:insert(pandoc.MetaBlocks({ pandoc.RawBlock('latex', read_file(script_dir .. '/header.tex')) }))
    doc.meta['header-includes'] = list
    doc.blocks:insert(1, pandoc.RawBlock('latex', '\\clearpage'))
  elseif is_docx then
    doc.blocks:insert(1, pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
  end
  return doc
end

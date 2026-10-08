"""Mark monospace paragraphs as CodeBlock and protect their spaces with NBSP so pandoc keeps alignment."""
import re, sys, zipfile
MONO = {'Consolas', 'Liberation Mono', 'Aptos Mono', 'Courier New'}
CODE_STYLES = {'CodeBlock', 'CodeSmall', 'CodeText'}
src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
xml = zin.read('word/document.xml').decode('utf-8')

def fix_para(m):
    p = m.group(0)
    style = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    runs = re.findall(r'<w:r\b.*?</w:r>', p, flags=re.S)
    text_runs = [r for r in runs if '<w:t' in r]
    if not text_runs:
        return p
    is_code = style and style.group(1) in CODE_STYLES
    if not is_code:
        fonts = [re.search(r'w:ascii="([^"]+)"', r) for r in text_runs]
        is_code = all(f and f.group(1) in MONO for f in fonts)
    if not is_code and p.count('<w:br/>') >= 3:
        # Plain-font trees/diagrams: indented lines or box-drawing characters
        is_code = bool(re.search(r'<w:t xml:space="preserve">  ', p) or re.search('[├└│┌┐┘─]', p))
    if not is_code:
        return p
    if style:
        p = p.replace(style.group(0), '<w:pStyle w:val="PrepCode"', 1)
    else:
        p = re.sub(r'<w:p\b([^>]*)>', lambda mm: mm.group(0) + '<w:pPr><w:pStyle w:val="PrepCode"/></w:pPr>', p, count=1) \
            if '<w:pPr>' not in p else p.replace('<w:pPr>', '<w:pPr><w:pStyle w:val="PrepCode"/>', 1)
    return re.sub(r'(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)', lambda t: t.group(1) + t.group(2).replace(' ', ' ') + t.group(3), p)

xml = re.sub(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', fix_para, xml, flags=re.S)
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename == 'word/document.xml':
            data = xml.encode('utf-8')
        elif item.filename == 'word/styles.xml':
            st = zin.read(item.filename).decode('utf-8')
            st = st.replace('</w:styles>', '<w:style w:type="paragraph" w:customStyle="1" w:styleId="PrepCode"><w:name w:val="PrepCode"/></w:style></w:styles>')
            data = st.encode('utf-8')
        else:
            data = zin.read(item.filename)
        zout.writestr(item, data)

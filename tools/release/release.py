#!/usr/bin/env python3
"""Build the CS-AML specification release package (DOCX + PDF) from canonical Markdown.

Runs inside the toolchain container (see Dockerfile / build_release.sh):
  python3 release.py --version 0.1.4 --src <tree with Documents/ contracts/ schemas/>
                     --out <empty dir> --work <scratch dir> --ref v0.1.4-spec --commit <sha>
"""
import argparse
import datetime
import glob
import hashlib
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
NAME_RE = re.compile(r'^CS-AML_(?P<key>.+?)_v(?P<ver>\d+\.\d+(?:\.\d+)?)(?P<suffix>_Expanded)?\.md$')
W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def vtuple(v):
    return tuple(int(x) for x in v.split('.')) + (0,) * (3 - len(v.split('.')))


# --------------------------------------------------------------- selection --

def load_titles():
    titles = {}
    with open(os.path.join(HERE, 'documents.tsv'), encoding='utf-8') as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            key, title, mode = line.rstrip('\n').split('\t')
            titles[key] = (title, mode)
    return titles


def select_documents(src, release_version):
    titles = load_titles()
    best = {}
    for path in sorted(glob.glob(os.path.join(src, 'Documents', 'CS-AML_*.md'))):
        m = NAME_RE.match(os.path.basename(path))
        if not m:
            sys.exit(f'unexpected document name: {path}')
        key = m['key'] + (m['suffix'] or '')
        if key not in titles:
            sys.exit(f'document key {key!r} missing from documents.tsv')
        if vtuple(m['ver']) > vtuple(release_version):
            sys.exit(f'{path} is newer than release {release_version}')
        if key not in best or vtuple(m['ver']) > vtuple(best[key][1]):
            best[key] = (path, m['ver'])
    docs, excluded = [], []
    for key, (path, ver) in sorted(best.items()):
        title, mode = titles[key]
        (docs if mode == 'include' else excluded).append(
            {'key': key, 'path': path, 'file_version': ver, 'title': title,
             'name': os.path.basename(path)[:-3]})
    return docs, excluded


def status_metadata(path):
    with open(path, encoding='utf-8') as f:
        head = ''.join(f.readlines()[:40])
    plain = head.replace('\\|', '|').replace('*', '').replace('`', '')
    m = re.search(r'Version: (\d+\.\d+\.\d+) — ([^(\n]+?) \((\d{4}-\d{2}-\d{2})', plain)
    if m:
        version, status, date = m.groups()
    else:
        m = re.search(r'Status: ([^(\n]+?) \((\d{4}-\d{2}-\d{2}).*?Version: (\d+\.\d+\.\d+)', plain, re.S)
        if not m:
            sys.exit(f'no status block found in {path}')
        status, date, version = m.groups()
    t = re.search(r'tag (v\d+\.\d+\.\d+-spec)', plain)
    return {'version': version, 'status': status.strip(), 'date': date, 'tag': t.group(1) if t else ''}


# ---------------------------------------------------------- reference.docx --

def xml_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


HEADER_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="4" w:space="1" w:color="808080"/></w:pBdr><w:tabs><w:tab w:val="right" w:pos="9638"/></w:tabs><w:spacing w:before="0" w:after="0"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">CS-AML </w:t></w:r><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">@@DOC@@</w:t></w:r><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:tab/><w:t xml:space="preserve">Version @@VERSION@@</w:t></w:r></w:p></w:hdr>
'''

FOOTER_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:p><w:pPr><w:pBdr><w:top w:val="single" w:sz="4" w:space="1" w:color="808080"/></w:pBdr><w:tabs><w:tab w:val="right" w:pos="9638"/></w:tabs><w:spacing w:before="0" w:after="0"/></w:pPr><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">Approved Internal Specification Baseline</w:t></w:r><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:tab/><w:t xml:space="preserve">Page </w:t></w:r><w:fldSimple w:instr=" PAGE "><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve"> of </w:t></w:r><w:fldSimple w:instr=" NUMPAGES "><w:r><w:rPr><w:sz w:val="16"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>
'''

SECTPR = ('<w:sectPr><w:headerReference w:type="default" r:id="rIdCsamlHdr"/>'
          '<w:footerReference w:type="default" r:id="rIdCsamlFtr"/>'
          '<w:footnotePr><w:numRestart w:val="eachSect"/></w:footnotePr>'
          '<w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="1418" w:right="1134" w:bottom="1247" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>'
          '</w:sectPr>')

EXTRA_STYLES = '''
  <w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode">
    <w:name w:val="Source Code"/><w:basedOn w:val="Normal"/><w:qFormat/>
    <w:pPr><w:wordWrap w:val="0"/><w:shd w:val="clear" w:color="auto" w:fill="F4F6F8"/><w:pBdr><w:left w:val="single" w:sz="8" w:space="6" w:color="A0A8B0"/></w:pBdr><w:spacing w:before="60" w:after="120" w:line="240" w:lineRule="auto"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas" w:eastAsia="Consolas"/><w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:customStyle="1" w:styleId="TableText">
    <w:name w:val="Table Text"/><w:basedOn w:val="Compact"/><w:qFormat/>
    <w:pPr><w:spacing w:before="20" w:after="20"/></w:pPr>
    <w:rPr><w:sz w:val="17"/><w:szCs w:val="17"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:customStyle="1" w:styleId="TableTextSmall">
    <w:name w:val="Table Text Small"/><w:basedOn w:val="Compact"/><w:qFormat/>
    <w:pPr><w:spacing w:before="10" w:after="10"/></w:pPr>
    <w:rPr><w:sz w:val="14"/><w:szCs w:val="14"/></w:rPr>
  </w:style>
'''

TBL_BORDERS = ('<w:tblBorders>' + ''.join(
    f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="A0A8B0"/>'
    for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')) + '</w:tblBorders>')


def make_base_reference(work):
    base = os.path.join(work, 'reference-default.docx')
    with open(base, 'wb') as f:
        run(['pandoc', '--print-default-data-file', 'reference.docx'], stdout=f)
    parts = {}
    with zipfile.ZipFile(base) as z:
        for n in z.namelist():
            parts[n] = z.read(n)
    styles = parts['word/styles.xml'].decode('utf-8')
    styles = styles.replace(
        '<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi" />',
        '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri" />', 1)
    styles = styles.replace('<w:sz w:val="24" />\n        <w:szCs w:val="24" />',
                            '<w:sz w:val="20" />\n        <w:szCs w:val="20" />', 1)
    styles = styles.replace('<w:spacing w:before="180" w:after="180" />',
                            '<w:spacing w:before="100" w:after="100" />', 1)
    i = styles.index('w:styleId="Table"')
    j = styles.index('<w:tblInd w:w="0" w:type="dxa" />', i) + len('<w:tblInd w:w="0" w:type="dxa" />')
    styles = styles[:j] + TBL_BORDERS + styles[j:]
    k = styles.index('<w:vAlign w:val="bottom"/>', i)
    styles = styles[:k] + '<w:shd w:val="clear" w:color="auto" w:fill="E6EBF0"/>' + styles[k:]
    styles = styles.replace('</w:styles>', EXTRA_STYLES + '</w:styles>')
    parts['word/styles.xml'] = styles.encode('utf-8')

    doc = parts['word/document.xml'].decode('utf-8')
    doc = re.sub(r'<w:sectPr>.*?</w:sectPr>', SECTPR, doc, flags=re.S)
    parts['word/document.xml'] = doc.encode('utf-8')

    rels = parts['word/_rels/document.xml.rels'].decode('utf-8')
    rels = rels.replace('</Relationships>',
                        f'<Relationship Type="{R_NS}/header" Id="rIdCsamlHdr" Target="header1.xml" />'
                        f'<Relationship Type="{R_NS}/footer" Id="rIdCsamlFtr" Target="footer1.xml" /></Relationships>')
    parts['word/_rels/document.xml.rels'] = rels.encode('utf-8')
    ct = parts['[Content_Types].xml'].decode('utf-8')
    ct = ct.replace('</Types>',
                    '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml" />'
                    '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml" /></Types>')
    parts['[Content_Types].xml'] = ct.encode('utf-8')
    parts['word/footer1.xml'] = FOOTER_XML.encode('utf-8')
    return parts


def write_reference(parts, path, title, version):
    hdr = HEADER_XML.replace('@@DOC@@', xml_escape(title)).replace('@@VERSION@@', xml_escape(version))
    fixed = (1980, 1, 1, 0, 0, 0)   # deterministic zip entries
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, data in list(parts.items()) + [('word/header1.xml', hdr.encode('utf-8'))]:
            z.writestr(zipfile.ZipInfo(n, fixed), data, zipfile.ZIP_DEFLATED)


# ------------------------------------------------------------------- build --

def build_docx(doc, meta, ref, out_path):
    run(['pandoc', doc['path'], '-f', 'gfm', '-t', 'docx',
         '--lua-filter', os.path.join(HERE, 'filter.lua'),
         '--reference-doc', ref, '--toc', '--toc-depth=2',
         '-M', 'doctitle=' + doc['title'], '-M', 'docversion=' + meta['version'],
         '-M', 'lang=en-GB',
         '-o', out_path])
    style_docx_tables(out_path)


def style_docx_tables(path):
    """Give table cell paragraphs the 'Table Text' style (9 pt; 'Table Text Small' 7 pt for >= 6 columns)."""
    with zipfile.ZipFile(path) as z:
        parts = [(i, z.read(i.filename)) for i in z.infolist()]

    def restyle(m):
        tbl = m.group(0)
        style = 'TableTextSmall' if tbl.count('<w:gridCol ') >= 6 else 'TableText'
        return re.sub(r'<w:pStyle w:val="Compact" ?/>', f'<w:pStyle w:val="{style}" />', tbl)

    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
        for info, data in parts:
            if info.filename == 'word/document.xml':
                data = re.sub(r'<w:tbl>.*?</w:tbl>', restyle, data.decode('utf-8'), flags=re.S).encode('utf-8')
            z.writestr(info, data)
    os.replace(tmp, path)


def build_pdf(doc, meta, work, out_path):
    d = os.path.join(work, 'tex', doc['name'])
    os.makedirs(d, exist_ok=True)
    tex = os.path.join(d, 'doc.tex')
    run(['pandoc', doc['path'], '-f', 'gfm', '-t', 'latex', '-s',
         '--lua-filter', os.path.join(HERE, 'filter.lua'),
         '--toc', '--toc-depth=2', '--top-level-division=section',
         '-M', 'doctitle=' + doc['title'], '-M', 'docversion=' + meta['version'],
         '-V', 'documentclass=article', '-V', 'papersize=a4', '-V', 'fontsize=10pt',
         '-V', 'geometry:left=20mm', '-V', 'geometry:right=20mm',
         '-V', 'geometry:top=24mm', '-V', 'geometry:bottom=22mm', '-V', 'geometry:headsep=5mm',
         '-V', 'mainfont=DejaVu Sans', '-V', 'sansfont=DejaVu Sans', '-V', 'monofont=DejaVu Sans Mono',
         '-V', 'monofontoptions=Scale=0.92',
         '-V', 'colorlinks=true', '-V', 'linkcolor=blue!45!black', '-V', 'urlcolor=blue!45!black',
         '-V', 'toccolor=black', '-V', 'lang=en-GB',
         '-o', tex])
    for _ in range(3):   # TOC + LastPage references
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'doc.tex'],
                           cwd=d, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if r.returncode != 0:
            sys.exit(f'xelatex failed for {doc["name"]}; see {d}/doc.log')
    shutil.copyfile(os.path.join(d, 'doc.pdf'), out_path)
    return os.path.join(d, 'doc.log')


def pdf_pages(path):
    out = subprocess.run(['pdfinfo', path], check=True, capture_output=True, text=True).stdout
    return int(re.search(r'^Pages:\s+(\d+)', out, re.M).group(1))


def log_findings(log):
    text = open(log, encoding='utf-8', errors='replace').read()
    missing = sorted(set(re.findall(r'Missing character: There is no (.+?) \(', text)))
    overfull = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)', text)]
    errors = re.findall(r'^! .*$', text, re.M)
    return missing, overfull, errors


def check_docx(path, title):
    import docx  # python3-docx in the toolchain image
    d = docx.Document(path)
    hdr = ' '.join(p.text for s in d.sections for p in s.header.paragraphs)
    ok = title in hdr
    return {'paragraphs': len(d.paragraphs), 'tables': len(d.tables), 'header_ok': ok}


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def tool_versions():
    pv = subprocess.run(['pandoc', '--version'], capture_output=True, text=True).stdout.splitlines()[0]
    xv = subprocess.run(['xelatex', '--version'], capture_output=True, text=True).stdout.splitlines()[0]
    return pv, xv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', required=True)
    ap.add_argument('--src', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--ref', required=True)
    ap.add_argument('--commit', required=True)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    os.makedirs(a.work, exist_ok=True)
    docs, excluded = select_documents(a.src, a.version)
    if os.environ.get('ONLY'):   # development aid: rebuild a subset only
        docs = [d for d in docs if re.search(os.environ['ONLY'], d['name'])]
    print(f'{len(docs)} documents selected; excluded: {[e["name"] for e in excluded]}')
    base_parts = make_base_reference(a.work)
    qa_lines, rows = [], []
    for doc in docs:
        meta = status_metadata(doc['path'])
        if meta['version'] != doc['file_version']:
            print(f'WARNING {doc["name"]}: status block version {meta["version"]} != file version', flush=True)
        ref = os.path.join(a.work, 'ref-' + doc['name'] + '.docx')
        write_reference(base_parts, ref, doc['title'], meta['version'])
        docx_out = os.path.join(a.out, doc['name'] + '.docx')
        pdf_out = os.path.join(a.out, doc['name'] + '.pdf')
        build_docx(doc, meta, ref, docx_out)
        log = build_pdf(doc, meta, a.work, pdf_out)
        pages = pdf_pages(pdf_out)
        missing, overfull, errors = log_findings(log)
        dq = check_docx(docx_out, doc['title'])
        rows.append((doc, meta, pages))
        line = (f'{doc["name"]}: pdf {pages} p; overfull {len(overfull)} (max {max(overfull, default=0):.1f}pt); '
                f'missing glyphs {missing or "none"}; tex errors {len(errors)}; '
                f'docx paragraphs {dq["paragraphs"]}, tables {dq["tables"]}, header {"ok" if dq["header_ok"] else "MISSING"}')
        print(line, flush=True)
        qa_lines.append(line)

    for sub, fname in (('contracts', 'openapi.yaml'), ('schemas', 'enums.yaml')):
        os.makedirs(os.path.join(a.out, sub), exist_ok=True)
        shutil.copyfile(os.path.join(a.src, sub, fname), os.path.join(a.out, sub, fname))

    pv, xv = tool_versions()
    epoch = int(os.environ.get('SOURCE_DATE_EPOCH', '0'))
    src_date = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    write_readme(a, docs, excluded, rows, pv, xv)
    write_manifest(a, rows, pv, xv, src_date)
    with open(os.path.join(a.work, 'qa.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(qa_lines) + '\n')


def write_readme(a, docs, excluded, rows, pv, xv):
    lines = [
        f'# CS-AML Specification Release Package v{a.version}',
        '',
        f'Rendered DOCX and PDF editions of the CS-AML **v{a.version} Approved Internal Specification Baseline** '
        f'(source tag `{a.ref}`, commit `{a.commit[:7]}`).',
        '',
        '- **The Markdown files in `Documents/` remain the canonical source.** These DOCX/PDF files are generated '
        'convenience copies; where they differ from the Markdown, the Markdown governs.',
        '- Each document is rendered from its *current* Markdown version (some documents did not change in later '
        'releases and therefore keep version 0.1.1 or 0.1.2; the file name carries the document version).',
        '- Change tags such as `*[v0.1.4 · CR-N-01]*` are kept verbatim; they are part of the traceability record.',
        '- The legacy v0.1 DOCX/PDF files in `Documents/` (`*_v0.1.docx`, `*_v0.1.pdf`) are historical and do not '
        'contain any v0.1.1+ correction.',
        '- Excluded: ' + ', '.join(f'`{e["name"]}.md` (legacy non-expanded Framework, superseded by the Expanded '
                                   f'Framework; retained in `Documents/` for history only)' for e in excluded) + '.',
        f'- `contracts/openapi.yaml` and `schemas/enums.yaml` are copies of the files at `{a.ref}`.',
        '- `MANIFEST.txt` lists the SHA-256 of every file in this package.',
        '',
        '| Document | Version | Date | PDF pages | Files |',
        '|---|---|---|---|---|',
    ]
    for doc, meta, pages in rows:
        lines.append(f'| CS-AML {doc["title"]} | {meta["version"]} | {meta["date"]} | {pages} | '
                     f'`{doc["name"]}.pdf`, `{doc["name"]}.docx` |')
    lines += [
        '',
        f'Regenerate with `tools/release/build_release.sh {a.version} {a.ref}` (requires Docker; toolchain: '
        f'{pv}, {xv}, DejaVu fonts; see `tools/release/`).',
        '',
        'Known presentation limits: DOCX tables keep portrait orientation (wide tables use a smaller font); '
        'Word asks to update the table of contents and page-count fields when a DOCX is first opened.',
        '',
    ]
    with open(os.path.join(a.out, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def write_manifest(a, rows, pv, xv, src_date):
    files = []
    for root, _, names in os.walk(a.out):
        for n in names:
            p = os.path.join(root, n)
            rel = os.path.relpath(p, a.out)
            if rel != 'MANIFEST.txt':
                files.append(rel)
    files.sort()
    total = sum(os.path.getsize(os.path.join(a.out, f)) for f in files)
    lines = [
        f'CS-AML Specification Release Package v{a.version}',
        f'Source tag: {a.ref}',
        f'Source commit: {a.commit}',
        f'Source commit date (SOURCE_DATE_EPOCH): {src_date}',
        f'Toolchain: {pv}; {xv}; base image pandoc/latex:3.10.0.0-debian (digest in tools/release/Dockerfile)',
        f'Documents: {len(rows)} (DOCX + PDF each); files: {len(files)}; total bytes: {total}',
        '',
        'SHA-256 (sha256sum -c compatible):',
    ]
    for f in files:
        lines.append(f'{sha256(os.path.join(a.out, f))}  {f}')
    with open(os.path.join(a.out, 'MANIFEST.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Cross-document consistency checks for the CS-AML specification set (v0.1.1 / v0.1.2).

Checks:
  1. schemas/enums.yaml: value pattern and uniqueness.
  2. Data Model Annex A enumerations match the registry.
  3. contracts/openapi.yaml: enum schemas tagged x-csaml-enum match the registry; $refs resolve;
     operationIds unique; path parameters declared.
  4. Specs: retired terms are not used outside explicit legacy/retired notes.
  5. Traceability: referenced feature, SRS and story IDs exist; Technology Architecture uses TA-CAP.
  6. Markdown code fences are balanced.
  7. Versioning: exactly one current Markdown file per document (v0.1.2 supersedes v0.1.1), every v0.1.2 file
     carries a v0.1.2 status block, and every change-request ID cited (CR-Ix-yy) is listed in CHANGELOG.md.

Documents are resolved by title: the highest version present (v0.1.2 before v0.1.1) is the current file. A superseded
v0.1.1 file must not remain next to its v0.1.2 successor (git mv preserves history).

Usage: python3 tools/check_consistency.py   (exit code 1 when any error is found)
"""
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'Documents')
errors, warnings = [], []


VERSIONS = ('0.1.2', '0.1.1')  # newest first


def doc(name):
    """Resolve a v0.1.1 file name to the current version of that document."""
    base = name.replace('_v0.1.1', '_v{}')
    for v in VERSIONS:
        path = os.path.join(DOCS, base.format(v))
        if os.path.exists(path):
            return path
    raise FileNotFoundError(name)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


ALL_MD = sorted(glob.glob(os.path.join(DOCS, '*_v0.1.[12]*.md')))
by_title = {}
for path in ALL_MD:
    title = re.sub(r'_v0\.1\.[12]', '_v{}', os.path.basename(path))
    by_title.setdefault(title, []).append(path)
SPECS = []
for title, paths in sorted(by_title.items()):
    if len(paths) > 1:
        errors.append(f'{title.format("x")}: both {", ".join(os.path.basename(p) for p in paths)} exist; '
                      f'keep only the current version')
    SPECS.append(max(paths, key=lambda p: '_v0.1.2' in p))
TAG = re.compile(r'\*\[v0\.1\.[12][^\]]*\]\*')
TOKEN = re.compile(r'\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*\b')

# 1. Registry --------------------------------------------------------------------------------
registry = yaml.safe_load(read(os.path.join(ROOT, 'schemas', 'enums.yaml')))
pattern = re.compile(registry['conventions']['value_pattern'])
enums, wire = {}, {}
for key, spec in registry['enums'].items():
    values = [v['value'] for v in spec['values']]
    enums[key] = values
    wire[key] = values
    for v in values:
        if not pattern.match(v):
            errors.append(f'enums.yaml {key}: value {v!r} does not match {pattern.pattern}')
    if len(values) != len(set(values)):
        errors.append(f'enums.yaml {key}: duplicate values')
    if spec.get('wire') == 'code':  # registry exception (credibility_grade): the wire value is `code`
        codes = [v.get('code') for v in spec['values']]
        if None in codes or len(codes) != len(set(codes)):
            errors.append(f'enums.yaml {key}: wire: code needs a unique code on every value')
        wire[key] = codes

# 2. Data Model Annex A ----------------------------------------------------------------------
ANNEX_TO_REGISTRY = {
    'entity_type': 'entity_type',
    'flow_class': 'flow_class',
    'confidence.level': 'confidence_level',
    'classification': 'classification',
    'hypothesis.status': 'hypothesis_status',
    'typology_match.consistency_level': 'typology_consistency_level',
    'review.decision': 'review_decision',
    'claim.claim_status': 'claim_status',
    'fact.fact_status': 'fact_status',
    'verification_decision.decision': 'verification_decision',
    'entity.resolution_status': 'entity_resolution_status',
    'resolution_decision.decision': 'resolution_decision',
    'case_membership.role': 'case_membership_role',
    'case.risk_rating': 'risk_rating',
    'case.closure_reason': 'closure_reason',
    'upload_session.status': 'upload_session_status',
    'envelope.status': 'envelope_status',
    'claim.credibility_grade': 'credibility_grade',
    'money.precision': 'money_precision',
    'temporal_value.precision': 'temporal_precision',
    'hypothesis.role': 'hypothesis_role',
    'hypothesis_link.effect': 'hypothesis_link_effect',
}
dm = read(doc('CS-AML_Data_Model_Specification_v0.1.1.md'))
annex = dm.split('# Annex A.', 1)[1].split('# Annex B.', 1)[0]
for line in annex.splitlines():
    m = re.match(r'\|\s*([a-z_.]+)\s*\|(.*)\|\s*$', line)
    if not m:
        continue
    name, cell = m.group(1), m.group(2)
    if name not in ANNEX_TO_REGISTRY:
        warnings.append(f'Data Model Annex A: {name} has no registry mapping in this checker')
        continue
    cell = TAG.sub('', cell)
    cell = re.sub(r'\([^)]*\)', '', cell)
    cell = re.sub(r'"[^"]*"', '', cell)
    found = {t for t in TOKEN.findall(cell) if '_' in t or t.isupper()} - {'Claims', 'Facts'}
    found = {t for t in found if t not in ('CLAIMS', 'FACTS')}
    expected = set(enums[ANNEX_TO_REGISTRY[name]])
    if found != expected:
        errors.append(f'Data Model Annex A {name} != enums.yaml {ANNEX_TO_REGISTRY[name]}: '
                      f'only in doc {sorted(found - expected)}, only in registry {sorted(expected - found)}')

# 3. OpenAPI ---------------------------------------------------------------------------------
oa_path = os.path.join(ROOT, 'contracts', 'openapi.yaml')
if os.path.exists(oa_path):
    oa = yaml.safe_load(read(oa_path))

    def resolve(ref):
        if not ref.startswith('#/'):
            return True
        node = oa
        for part in ref[2:].split('/'):
            part = part.replace('~1', '/').replace('~0', '~')
            if not isinstance(node, dict) or part not in node:
                return False
            node = node[part]
        return True

    def walk(node, path):
        if isinstance(node, dict):
            ref = node.get('$ref')
            if isinstance(ref, str) and not resolve(ref):
                errors.append(f'openapi: unresolved $ref {ref} at {path}')
            key = node.get('x-csaml-enum')
            if key is not None:
                values = node.get('enum') or (node.get('items') or {}).get('enum')
                if key not in enums:
                    errors.append(f'openapi: {path} x-csaml-enum {key!r} not in enums.yaml')
                elif values is None:
                    errors.append(f'openapi: {path} has x-csaml-enum but no enum list')
                else:
                    values = [v for v in values if v is not None]
                    subset = node.get('x-csaml-enum-subset', False)
                    reg = wire[key] if node.get('x-csaml-enum-wire') == 'code' else enums[key]
                    if (node.get('x-csaml-enum-wire') == 'code') != (wire[key] is not enums[key]):
                        errors.append(f'openapi: {path} x-csaml-enum-wire does not match enums.yaml {key} wire setting')
                    extra = set(values) - set(reg)
                    missing = set(reg) - set(values)
                    if extra or (missing and not subset):
                        errors.append(f'openapi: {path} enum vs enums.yaml {key}: '
                                      f'extra {sorted(extra)}, missing {sorted(missing)}')
            for k, v in node.items():
                walk(v, f'{path}/{k}')
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f'{path}[{i}]')

    walk(oa, '#')
    op_ids = []
    for route, item in (oa.get('paths') or {}).items():
        declared_common = {p.get('name') for p in item.get('parameters', []) if isinstance(p, dict)}
        for method, op in item.items():
            if method not in ('get', 'put', 'post', 'patch', 'delete', 'head', 'options'):
                continue
            if 'operationId' in op:
                op_ids.append(op['operationId'])
            else:
                errors.append(f'openapi: {method.upper()} {route} has no operationId')
            declared = set(declared_common)
            for p in op.get('parameters', []):
                if '$ref' in p and resolve(p['$ref']):
                    node = oa
                    for part in p['$ref'][2:].split('/'):
                        node = node[part]
                    p = node
                if p.get('in') == 'path':
                    declared.add(p.get('name'))
            for name in re.findall(r'\{([^}]+)\}', route):
                if name not in declared:
                    errors.append(f'openapi: {method.upper()} {route} path parameter {name} not declared')
    dupes = {o for o in op_ids if op_ids.count(o) > 1}
    if dupes:
        errors.append(f'openapi: duplicate operationIds {sorted(dupes)}')
else:
    warnings.append('contracts/openapi.yaml not found; OpenAPI checks skipped')

# 4. Retired terms ---------------------------------------------------------------------------
LEGACY_CONTEXT = re.compile(r'retired|legacy|v0\.1 |v0\.1\)|v0\.1\.|v0\.1,|was |previously|draft name|formerly',
                            re.IGNORECASE)
RETIRED = [
    (re.compile(r'\bVERSION_CONFLICT\b'), 'retired error code VERSION_CONFLICT (use 412 PRECONDITION_FAILED)'),
    (re.compile(r'SOURCE-PROTECTED'), 'wire value is SOURCE_PROTECTED'),
    (re.compile(r'\bsource_claim_refs\b'), 'field renamed supporting_claim_refs'),
    (re.compile(r'\bPROMOTE\b'), 'fact decision value renamed CREATE'),
    (re.compile(r'Redis 7\.x'), 'broker/cache baseline is Valkey 8.x'),
    (re.compile(r'MinIO reference'), 'object store product is chosen by ADR-0005'),
    (re.compile(r'\bLINKED-POSSIBLE\b'), 'resolution decision is POSSIBLE_MATCH'),
]
for path in SPECS:
    name = os.path.basename(path)
    for n, line in enumerate(read(path).splitlines(), 1):
        for rx, why in RETIRED:
            if rx.search(line) and not LEGACY_CONTEXT.search(line):
                errors.append(f'{name}:{n}: {why}')

# 5. Traceability ----------------------------------------------------------------------------
all_text = {os.path.basename(p): read(p) for p in SPECS}
PF = os.path.basename(doc('CS-AML_Product_and_Feature_Specification_v0.1.1.md'))
SRS = os.path.basename(doc('CS-AML_Software_Requirements_Specification_SRS_v0.1.1.md'))
MVP = os.path.basename(doc('CS-AML_MVP_Engineering_Breakdown_v0.1.1.md'))
features = set(re.findall(r'^\|\s*(F-[A-Z]+-\d{3})\s*\|', all_text[PF], re.M))
srs_ids = set(re.findall(r'^#+\s*(SRS-[A-Z0-9-]+?-\d{3})\b', all_text[SRS], re.M))
srs_ids |= set(re.findall(r'^\|\s*\**(SRS-[A-Z0-9-]+?-\d{3})\**\s*\|', all_text[SRS], re.M))
stories = set(re.findall(r'^#+\s*(ST-E\d+-\d{2})\b', all_text[MVP], re.M))

for name, text in all_text.items():
    for fid in sorted(set(re.findall(r'\bF-[A-Z]+-\d{3}\b', text)) - features):
        errors.append(f'{name}: references unknown feature {fid}')
    if srs_ids and name != SRS:
        for sid in sorted(set(re.findall(r'\bSRS-FR-[A-Z]+-\d{3}\b', text)) - srs_ids):
            errors.append(f'{name}: references unknown SRS requirement {sid}')
    if stories and name != MVP:
        for st in sorted(set(re.findall(r'\bST-E\d+-\d{2}\b', text)) - stories):
            errors.append(f'{name}: references unknown story {st}')

ta = all_text[os.path.basename(doc('CS-AML_Technology_Architecture_v0.1.1.md'))]
for n, line in enumerate(ta.splitlines(), 1):
    if re.search(r'(?<!TA-)\bCAP-\d{2}\b', line) and 'TA-CAP' not in line and 'product' not in line.lower():
        errors.append(f'Technology Architecture:{n}: bare CAP-xx (use TA-CAP-xx or state it is the product registry)')

# 6. Code fences -----------------------------------------------------------------------------
for path in SPECS:
    if sum(1 for l in read(path).splitlines() if l.startswith('```')) % 2:
        errors.append(f'{os.path.basename(path)}: unbalanced code fence')

# 7. Versioning and change-request IDs --------------------------------------------------------
changelog = read(os.path.join(ROOT, 'CHANGELOG.md'))
CR = re.compile(r'\bCR-I\d-\d{2}\b')
known_cr = set(CR.findall(changelog.split('## v0.1.1', 1)[0]))
for path in SPECS:
    name, text = os.path.basename(path), read(path)
    if '_v0.1.2' in name:
        head = text[:4000]
        if 'Document status — v0.1.2' not in head or 'v0.1.2-spec' not in head:
            errors.append(f'{name}: missing v0.1.2 status block')
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith('```'):
            in_fence = not in_fence
        elif in_fence and TAG.search(line):
            errors.append(f'{name}:{n}: change tag inside a code fence')
    for cr in sorted(set(CR.findall(text)) - known_cr):
        errors.append(f'{name}: change request {cr} is not listed in CHANGELOG.md v0.1.2')
for extra in ('contracts/openapi.yaml', 'schemas/enums.yaml'):
    for cr in sorted(set(CR.findall(read(os.path.join(ROOT, extra)))) - known_cr):
        errors.append(f'{extra}: change request {cr} is not listed in CHANGELOG.md v0.1.2')

for w in warnings:
    print('WARN ', w)
for e in errors:
    print('ERROR', e)
print(f'\n{len(errors)} error(s), {len(warnings)} warning(s); '
      f'{len(enums)} enums, {len(features)} features, {len(srs_ids)} SRS IDs, {len(stories)} stories checked.')
sys.exit(1 if errors else 0)

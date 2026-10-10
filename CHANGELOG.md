# CS-AML Changelog

## Release package v0.1.4 — 2026-10-10 — DOCX + PDF rendering (no specification change)

DOCX and PDF editions of the v0.1.4 baseline were generated from the canonical Markdown at tag `v0.1.4-spec` (commit `56a0547`) into
`release/v0.1.4/`: the 22 current documents (each at its current version — 0.1.4, 0.1.2 or 0.1.1; the legacy non-expanded Framework
is excluded), copies of `contracts/openapi.yaml` and `schemas/enums.yaml`, a `README.md` and a `MANIFEST.txt` with SHA-256 values.
No specification text, contract or registry changed; the Markdown remains canonical and the v0.1 DOCX/PDF in `Documents/` remain
historical. Tooling: `tools/release/` (`build_release.sh`, `release.py`, `filter.lua`, `header.tex`, `documents.tsv`, `Dockerfile`;
pandoc 3.10 and XeTeX / TeX Live 2026 in the pinned `pandoc/latex:3.10.0.0-debian` image, DejaVu fonts). Rebuilds are byte-identical.
No new tag.

## v0.1.4 — 2026-10-10 — Change requests from the post-MVP follow-ups

**Status:** **Approved Internal Specification Baseline** — tag `v0.1.4-spec`, 2026-10-10, product owner. Supersedes `v0.1.3-spec`.
This is not an independent review. The change requests come from the post-MVP follow-ups of the reference implementation: the case
workflow (charter, lifecycle gates G0–G6, tasks, case activity), OCR / text-extraction and offline machine-translation derivatives,
and MFA step-up for high-risk actions (`docs/change-requests.md` in the implementation repository, section "Post-MVP follow-ups"; the
implementation extensions `contracts/extensions/case-workflow.yaml` and `n1.yaml` and ADR-0036…ADR-0039 there).

### Decision

**All 14 change-request recommendations (CR-N-01…CR-N-14) were approved by the product owner on 2026-10-10**, without changes and
without any change of implementation behaviour (the specification now states what the reference implementation does). Decision
authority for every row below: product owner, 2026-10-10.

The conditions of earlier releases still apply: CR-I5-08 (re-review of the search timing channel before real data) and the external
reviews of CR-I4-03 (AML specialist) and CR-I1-10 (security).

### Dispositions

Columns as in v0.1.2 / v0.1.3 (`adopted`, `registry`, `contract`, `text`). Changes are tagged in place as `*[v0.1.4 · CR-N-xx]*`
(Markdown) and `x-csaml-cr` with `x-csaml-release-class: DECIDED_V0_1_4` (OpenAPI).

| ID | Area | Decision | Disposition | Where |
|---|---|---|---|---|
| CR-N-01 | Case-workflow operations and fields | `listCharterVersions`, `getCharterVersion`, `getTask`, `updateTask` (If-Match); CharterVersionCreate with the Framework Annex A fields and a question `id` to keep a question; GateDecisionRequest `conditions` and `closure_reason`; TaskCreate `description`, `task_type`, `assignee_id`, `due_date`, `depends_on`; response fields on Charter (`versions`, `approved_version`, `amended_since_approval`), Gate (status, transition, preconditions, submitter / decider, decision history), Task and CaseActivityItem (`target_type`, `audit_action`, `links`) | contract | Contract; API §12; Data Model §6.4–§6.6; SRS-FR-CASE-002 |
| CR-N-02 | Question priority | Registry `investigation_question_priority` PRIMARY, SECONDARY | registry | `schemas/enums.yaml`; contract; Data Model §6.2, Annex A |
| CR-N-03 | Gate status; gate → case status | Registry `gate_status`; G0 DRAFT → AUTHORIZED, G1 AUTHORIZED → ACTIVE, G4 ACTIVE → REVIEW, G6 ACTIVE / REVIEW → CLOSED; G2 / G3 / G5 no status change; status changes only through an approved gate. MONITORING and reopening **deferred to v0.2** (not reachable via the API in v0.1.x) | registry + adopted | `schemas/enums.yaml`; contract `Gate`; Data Model §6.1, §6.5; Framework §5.9; API §12; SRS-FR-CASE-003, Annex B; Methodology §3 |
| CR-N-04 | Task contract | Registry `task_type`, `task_status`; rules as implemented (eligible member as assignee → 422; dependencies in the case, DONE only when all closed → 409; DONE / CANCELLED final; `case.update` changes any field, the assignee only the status of their own task; append-only history); Task leaves DEFER_V0_2. Links from tasks to sources / entities / hypotheses are not implemented and **deferred to v0.2** | registry + contract | `schemas/enums.yaml`; contract `Task`, `TaskCreate`, `TaskPatch`; Data Model §6.6; API §12; SRS-FR-CASE-004 |
| CR-N-05 | Gate readiness criteria | Criteria checked as implemented (data); the rest stated as reviewer judgement | adopted | Framework §5.9; API §12; Data Model §6.5; contract `Gate.preconditions` |
| CR-N-06 | What gates control | Gates control the case lifecycle only (activation, review, closure); collection, assessment finalisation and dissemination keep their own controls. Configuration per organisation / risk tier **deferred to v0.2** | adopted | Framework §5.9; API §12; SRS-FR-CASE-003; Control Implementation Guide CAS-02 |
| CR-N-07 | Gate approver independence | Decider ≠ submitter for every gate; deciders are LEAD or REVIEWER members; high-impact case = risk HIGH / CRITICAL or classification RESTRICTED / SOURCE_PROTECTED, and then the G0 / G1 decider must not have authored the charter version under approval | adopted | Control Implementation Guide CAS-02; Data Model §6.5; API §12; SRS-FR-CASE-003; Framework §5.9; contract `approveCaseGate` |
| CR-N-08 | Activity filters, auditor view | Actor / action / object filtering stays client-side; server parameters `actor`, `action`, `target_type` and an auditor view **deferred to v0.2** | text (deferral) | API §12; SRS-FR-CASE-005; contract `listCaseActivity`, `CaseActivityItem` |
| CR-N-09 | OCR / text extraction | `requestTextExtraction`, `listEvidenceDerivedTexts`, `getDerivedText`, `reviewDerivedText`; Data Model class **DerivedText**; registry `derived_text_transformation`, `derived_text_status`, `text_page_method` and the open `derivation_type` vocabulary (OCR_TEXT, TEXT_EXTRACTION, MACHINE_TRANSLATION) | registry + contract | Contract; Data Model §7.2, §7.7, Annex A; API §13, §22; SRS-FR-DOC-002, SRS-FR-EVD-005, SRS-AI-001; Technical Stack §3, §9, §12; Control Implementation Guide EVD-02, TEC-01 |
| CR-N-10 | Machine translation | `requestDerivedTextTranslation`, `requestEvidenceTranslation`; **offline only for every automation engine** (OCR, MT, any future AI) — evidence content never leaves the host; source text kept per page; no mandatory second reviewer, but the machine-translation label is carried into any intelligence product that uses the translation | adopted + contract | Contract; API §13, §26 (API-SEC-11); SRS-FR-DOC-003, SRS-AI-005; Methodology §10.2, §28.1; Control Implementation Guide EVD-02, TEC-01; Technical Stack §3, §9; Data Model §7.7 |
| CR-N-11 | Derived text in search (amends CR-I5-07) | Completed DerivedText indexed as `DERIVED_TEXT` with the epistemic marker `DERIVED`; policy-filtered, never before completion, switchable per deployment | registry + contract | `search_object_type`, `search_epistemic_status`; contract; API §17; SRS-FR-SCH-001; Technical Stack §13; Information Architecture §17.2; Data Model Annex A |
| CR-N-12 | Job types | Registry `job_type` EXPORT_PACKAGE, TEXT_EXTRACTION, MACHINE_TRANSLATION | registry | `schemas/enums.yaml`; contract `Job`, `JobType`; API §22; Data Model Annex A |
| CR-N-13 | MFA step-up | 403 `STEP_UP_REQUIRED` (ErrorCode); session `auth_level`, `auth_time`, `step_up`; `acr` (and `next`) login parameters; baseline of 11 step-up actions (dissemination.approve, export.generate, export.download, disposition.approve, disposition.execute, legal_hold.release, entity.merge, entity.unmerge, gate.approve, protected_source.grant, protected_source.access); ACR 2 = password + TOTP within 900 s by default. Per-deployment configuration and phishing-resistant factors (WebAuthn / passkeys) for approvers **deferred to v0.2** | contract + adopted | Contract (`x-csaml-step-up` on 13 operations, `StepUpRequired`, `Session`, `authLogin`); API §4, §9, §26, §27; SRS-SEC-005, SRS-FR-SEC-001; Technical Stack §10, §38; Control Implementation Guide CAS-02 |
| CR-N-14 | Login-callback errors | `authCallback` answers 303 to `/?login_error=<expired\|cancelled\|failed\|unavailable>` for every failed callback (replaces the documented 400 / 401 JSON; 503 also removed) | contract (fix) | Contract `authCallback`, `LoginErrorRedirect`; API §4; SRS-SEC-005 |

### What changed

- **Documents.** Eight documents changed and were renamed with `git mv` to `*_v0.1.4*.md` (history preserved): API Specification,
  Data Model, SRS, Technical Stack and Repository, Information Architecture, Control Implementation Guide (from v0.1.3), Investigation
  Methodology (from v0.1.2) and Framework Expanded (from v0.1.1; new §5.9 only). The other 15 Markdown documents are unchanged and keep
  their current version (v0.1.2 or v0.1.1); a reference to an older version of a document inside an unchanged document means the
  current version (see `README.md`). Technology Architecture needed no change (§16.1 "phishing-resistant MFA for approvers where
  feasible" stays a target; the TOTP baseline and the WebAuthn deferral are recorded in Technical Stack §10 and §38).
- **`contracts/openapi.yaml` 0.1.4.** v0.1.3 plus `contracts/extensions/case-workflow.yaml` and `n1.yaml` of the implementation
  (merged; the extension files are no longer needed): 138 → 146 paths, 180 → 190 operations. New operations: `listCharterVersions`,
  `getCharterVersion`, `getTask`, `updateTask`, `requestTextExtraction`, `requestEvidenceTranslation`, `listEvidenceDerivedTexts`,
  `getDerivedText`, `requestDerivedTextTranslation`, `reviewDerivedText`. Changed operations: `authLogin` (`acr`, `next`),
  `authCallback` (303 `LoginErrorRedirect` instead of 400 / 401 / 503), 13 high-risk operations (403 `StepUpRequired`,
  `x-csaml-step-up`), case-workflow operations (descriptions, shapes). New schemas: `DerivedText*`, `TextExtractionRequest`,
  `TranslationRequest`, `TaskPatch`, `CharterVersionList`, `SessionStepUp`, `StepUpRequiredError` and the registry enums
  `InvestigationQuestionPriority`, `GateStatus`, `TaskType`, `TaskStatus`, `DerivedTextTransformation`, `DerivedTextStatus`,
  `TextPageMethod`, `JobType`. The derived-text and translation POSTs carry the contract's CSRF requirement (`csrfHeader`), which the
  extension had left out. New items carry `x-csaml-status: decided`, `x-csaml-release-class: DECIDED_V0_1_4` and `x-csaml-cr`.
- **`schemas/enums.yaml` 0.1.4.** 78 → 87 enums (417 → 453 values): `investigation_question_priority`, `gate_status`, `task_type`,
  `task_status`, `derived_text_transformation`, `derived_text_status`, `text_page_method`, `derivation_type` (open vocabulary, new
  convention `open: true`), `job_type`; `search_object_type` + DERIVED_TEXT, `search_epistemic_status` + DERIVED. Values are exactly
  the implementation constants. `InvestigationQuestion.priority` and `EvidenceItem.derivation_type` left `unregistered_fields`.
- **`tools/check_consistency.py`.** Resolves v0.1.4 files, accepts `*[v0.1.4 · …]*` tags and `CR-N-xx` IDs, maps the new Annex A rows
  and checks v0.1.4 status blocks.

### Release gates (2026-10-10)

| Gate | Result |
|---|---|
| G1–G3 Domain consistency, safety invariants, traceability | `tools/check_consistency.py`: 0 errors |
| G4 Machine contract | Redocly lint (recommended): 0 errors, 4 warnings — the three `/auth/*` redirect operations (no 2xx) and `GET /health` (no 4xx), unchanged from v0.1.3 |
| G5 Decisions | All 14 change requests decided (this section) |
| G6 Known limitations | Listed below |

### Implementation follow-up (reference implementation)

Re-import contract and registry v0.1.4 byte-for-byte and retire `contracts/extensions/case-workflow.yaml` and `n1.yaml` (the
`x-csaml-n1-behaviour` list is now expressed in the contract: `x-csaml-step-up`, `Session`, `authLogin`, `authCallback`,
`SearchObjectType`, `SearchEpistemicStatus`, `JobType`). No behaviour change is required.

### Deferred to v0.2

| Item | From |
|---|---|
| MONITORING and reopening of cases (triggers, gate or review) | CR-N-03 |
| Links from tasks to sources, entities and hypotheses | CR-N-04 |
| Gate configuration per organisation and per risk tier (CIG P1–P3); separate legal / privacy approver roles per gate | CR-N-06, CR-N-07 |
| Server-side activity filters (`actor`, `action`, `target_type`) and an auditor view | CR-N-08 |
| Per-deployment step-up action list and phishing-resistant factors (WebAuthn / passkeys) for approvers | CR-N-13 |
| Office-format (DOCX / XLSX) text extraction | CR-N-09 |

### Still open after v0.1.4

| Item | Target |
|---|---|
| Re-review of the search timing channel (CR-I5-08) | Before real (non-synthetic) data is processed |
| ANONYMIZE and whole-case DELETE dispositions (CR-I7-05) | v0.2 |
| Indexing of original evidence file content; hypotheses, assessments, indicators in search | Phase 2 / v0.2 |
| Administration/audit API (other than retention and health), protected sources, `GET /capabilities` | v0.2 (per epic) |
| Sort allowlists | v0.2 |
| The v0.2 deferrals above | v0.2 |
| External review of CR-I4-03 (AML specialist) and CR-I1-10 (security) | Before external reliance |
| Items of the v0.1.3 "Still open" table not listed here | Unchanged (gate and task status value sets and task contracts are closed by CR-N-03 / CR-N-04) |

## v0.1.3 — 2026-10-09 — Change requests from implementation increments I5–I7

**Status:** **Approved Internal Specification Baseline** — tag `v0.1.3-spec`, 2026-10-09, product owner. Supersedes `v0.1.2-spec`.
This is not an independent review. The change requests come from implementing increments I5 (search, graph exploration), I6
(products, review, dissemination) and I7 (retention, backup, hardening, release) of the reference implementation, where each
deviation or gap was recorded as a change-request candidate (`docs/change-requests.md` in the implementation repository; the
implementation extensions `contracts/extensions/i5.yaml`, `i6.yaml`, `i7.yaml` and ADR-0025…ADR-0035 there).

### Decision

**All 30 change-request recommendations (CR-I5-01…CR-I5-09, CR-I6-01…CR-I6-13, CR-I7-01…CR-I7-08) were approved by the
product owner on 2026-10-09**, without changes. Decision authority for every row below: product owner, 2026-10-09.

**Conditions attached to the decisions:**

| ID | Condition |
|---|---|
| CR-I5-08 | The residual search timing channel (query latency depends on the total corpus size) is accepted **for MVP 0.1 with synthetic data only**. It SHALL be re-reviewed — mitigated or explicitly re-accepted by the accountable authority — **before real (non-synthetic) data is processed**. |
| CR-I7-05 | ANONYMIZE and whole-case DELETE dispositions are refused (422) in MVP 0.1 and **deferred to v0.2** (they need a reviewed anonymiser and a case-level tombstone design). |
| CR-I5-09 | Performance targets stay SHOULD-level; measurements on the synthetic reference corpus are evidence, not guarantees. |

The external reviews required by v0.1.2 (CR-I4-03, AML specialist; CR-I1-10, security) are still outstanding.

### Dispositions

Columns as in v0.1.2 (`adopted`, `registry`, `contract`, `text`). Changes are tagged in place as `*[v0.1.3 · CR-xx-yy]*`
(Markdown) and `x-csaml-cr` with `x-csaml-release-class: DECIDED_V0_1_3` (OpenAPI).

| ID | Area | Decision | Disposition | Where |
|---|---|---|---|---|
| CR-I5-01 | Search API | `GET /search` (`searchObjects`): parameter set, `SearchHit` / `SearchFacets` / `SearchResults`, plain-text snippet segments, canonical back-links, authorization before results, counts, facets, snippets and ordering | contract | Contract; API §17; SRS-FR-SCH-001; Technical Stack §13 |
| CR-I5-02 | Graph exploration | `POST /graph/query` and `POST /graph/paths` with budget defaults (depth ≤ 3, 500 nodes, 1,500 edges, 4 s, 5 s statement timeout) and error rules (unreadable seed → 404, readable seed outside `case_id` → 422) | contract | Contract; API §18; SRS-FR-GRF-001; Technical Stack §29 |
| CR-I5-03 | Search value sets | Registry `search_object_type`, `search_epistemic_status` | registry | `schemas/enums.yaml`; contract; Data Model Annex A |
| CR-I5-04 | SOURCE_PROTECTED in search | Only with explicit `include_source_protected=true` AND the per-case protected-source grant; otherwise no hit, count, facet or snippet | adopted | Contract `searchObjects`; API §17; SRS-FR-SCH-002; Information Architecture §6 (roles and classification), §17 |
| CR-I5-05 | Shared-attribute leads | Registry `graph_lead_type`; normalization rules (case- and accent-folded alphanumerics, phone digits, ≥ 4 characters); leads are candidates, never edges, facts or merges | registry | `schemas/enums.yaml`; contract `GraphLead`; API §18; SRS-FR-GRF-001 |
| CR-I5-06 | Graph budget semantics | Partial result with `truncation_reasons` (registry `graph_truncation_reason`); only the statement-timeout backstop is 503 | registry | `schemas/enums.yaml`; contract; API §18 |
| CR-I5-07 | Index scope; canonical extract URL | Index scope confirmed (evidence metadata, cited extract text, relationships without endpoint names; no file content in MVP); new `GET /evidence-extracts/{extractId}` (`getEvidenceExtract`) as the canonical single-extract resource — **code change** | contract | Contract; API §13, §17; Technical Stack §13; Information Architecture §17.2; SRS-FR-SCH-001 |
| CR-I5-08 | Rate limits and timing | Search 120/min, graph 60/min per user (429 RATE_LIMITED); search statement timeout 5 s; timing channel accepted for MVP — **re-review before real data** | adopted | Contract; API §17, §18, §25; SRS-FR-SCH-002; Technical Stack §13 |
| CR-I5-09 | Performance targets | Reference corpus = synthetic generator `backend/tests/synthetic_corpus.py` (~97k search rows); both targets apply: global search first page ≤ 3 s, case-scoped search p95 < 2 s (SHOULD) | text | SRS-NFR-PERF-002, SRS-NFR-PERF-004; Technical Stack §29; API §17 |
| CR-I6-01 | Templates, rendering, evidence index | `/product-templates`, `/products/{id}/rendering`, `/products/{id}/versions/{version}`; product document `csaml.product-document/1` with evidence index; `subject_refs`, `contact_point` and product response fields | contract | Contract; API §19; Data Model §15.1; SRS-FR-PRD-001 |
| CR-I6-02 | Review kinds | Registry `review_kind`; `/assessments/{id}/submit-review`, `/review-requests`; reviewer independence (authors, contributors, requester never decide) | registry + contract | `schemas/enums.yaml`; contract; API §19; Data Model §15.2; SRS-FR-REV-001 |
| CR-I6-03 | Review / version lifecycle | As implemented: Review OPEN/DECIDED/CANCELLED (registry `review_status`); version SUBMITTED → APPROVED / APPROVED_WITH_CHANGES / RETURNED / REJECTED → SUPERSEDED / RETRACTED (registry `product_version_status`); APPROVE_WITH_CHANGES → product REVIEWED, not disseminable until a new version is reviewed; RETURN/REJECT → DRAFT | adopted | `schemas/enums.yaml`; contract; API §19; Data Model §15.1–§15.2 |
| CR-I6-04 | `review_required` reasons and clearing | Registry `review_reason`; approval 409 REVIEW_REQUIRED unless `clear_review_required`; REVIEW_FLAG_CLEARANCE review; disseminated products get a CORRECTION review | registry + contract | `schemas/enums.yaml`; contract; API §19; Data Model §15.1 |
| CR-I6-05 | Corrections and withdrawal | `/products/{id}/corrections`, `/products/{id}/withdraw` | contract | Contract; API §19; Data Model §15.1; SRS-FR-PRD-002 |
| CR-I6-06 | Dissemination | `handling_classification` (≥ product), registry `dissemination_status`, `GET /disseminations`, `/disseminations/{id}/revoke`; approver = REVIEWER/LEAD member, never the requester | registry + contract | `schemas/enums.yaml`; contract; API §19; Data Model §15.3; SRS-FR-DIS-001 |
| CR-I6-07 | Source-protected release | SOURCE_PROTECTED objects enter an approved scope only with `source_protected_release` set by an approver holding the per-case protected-source grant, with rationale; redaction as implemented (withheld, count recorded) | adopted | Contract `DisseminationApproveRequest`, `ExportPackage.redactions`; API §19; Data Model §15.3; SRS-FR-DIS-002 |
| CR-I6-08 | Export package format, statuses, download | Registry `export_package_format` (CSAML_PACKAGE_ZIP_V1), `export_package_status`, `sharing_log_entry_type`; `/export-packages`, `/export-packages/{id}`, `/export-packages/{id}/content` (409 when the approval is no longer valid) | registry + contract | `schemas/enums.yaml`; contract; API §19; Data Model §15.4 |
| CR-I6-09 | Job status | Registry `job_status` QUEUED → RUNNING → SUCCEEDED / FAILED; job fields `job_type`, `target_type`, `target_ref`, `result_url` | registry | `schemas/enums.yaml`; contract `Job`; API §22 |
| CR-I6-10 | Contract defect | `CaseMembershipList` and `EvidenceExtractList` use `items` only (`data` dropped); implementations may stop sending the duplicate `data` member | contract (fix) | Contract |
| CR-I6-11 | Export generation and candidates | `generateExportPackage` always 202 `ExportJobAccepted` (job + QUEUED package, `Location`); export candidates one page, `source_protected`, `in_approved_scope`; single-page derived lists allowed | contract | Contract; API §19, §22 |
| CR-I6-12 | Recorded reviewer downgrade | HandlingChange record (append-only; DOWNGRADE only with its approved review; registry `handling_change_direction`); `review_trigger_ref` may name a HandlingChange; `handling_decision_ref` | adopted | Data Model §6.1, §15.1, §16, §16.4; contract `IntelligenceProduct`, `Assessment`; `schemas/enums.yaml`; API §19 |
| CR-I6-13 | Typology source map | Re-imported with the next catalogue version; no content change now | text (no change) | — |
| CR-I7-01 | Retention API | `/retention-rules`, `/retention-evaluations`, `/legal-holds`, `/disposition-records` (+ approve / reject / execute) | contract | Contract; API §20, §20A; SRS-FR-ADM-003; Control Implementation Guide PRI-02 |
| CR-I7-02 | `RetentionRule.applies_to` | Registry `retention_target_type` (EVIDENCE_ITEM, EXPORT_PACKAGE, CASE); `applies_to_classifications` | registry | `schemas/enums.yaml`; Data Model §16.1; contract; API §20A |
| CR-I7-03 | LegalHold; rule / hold status | Data Model class LegalHold; registry `retention_rule_status`, `legal_hold_status` | registry + contract | Data Model §16.1–§16.2; `schemas/enums.yaml`; contract; Control Implementation Guide PRI-02 |
| CR-I7-04 | DispositionRecord | Data Model class DispositionRecord (the disposition log); registry `disposition_status`; decider = LEAD of every linked case, never the proposer | registry + contract | Data Model §16.3; `schemas/enums.yaml`; contract; API §20A; Control Implementation Guide PRI-02 |
| CR-I7-05 | Supported dispositions | MVP: DELETE (purge stored bytes, row kept as tombstone), ARCHIVE, REVIEW; ANONYMIZE and whole-case DELETE refused (422) — **deferred to v0.2** | adopted | Data Model §16.1; API §20A; SRS-FR-ADM-003, SRS-DR-006; contract `RetentionDisposition`, `RetentionRuleCreate` |
| CR-I7-06 | Case closure time | `Case.closed_at` (read-only); trigger CASE_CLOSURE uses it — **code change** | contract | Data Model §6.1; contract `Case`; API §20A |
| CR-I7-07 | Disposed evidence content | `getEvidenceContent` documents 409 STATE_CONFLICT (`EVIDENCE_DISPOSED`) | contract | Contract; API §13; SRS-DR-006 |
| CR-I7-08 | Health / metrics | `GET /health` (`getHealth`, unauthenticated, dependency status only, no case content) in the contract; `/metrics` internal and outside the API | contract | Contract; API §20; SRS-OPS-002; Technical Stack §25 |

### What changed

- **Documents.** Six documents changed and were renamed with `git mv` to `*_v0.1.3.md` (history preserved): API Specification,
  Data Model, SRS, Technical Stack and Repository (from v0.1.2), Information Architecture and Control Implementation Guide (from
  v0.1.1). The other 17 Markdown documents are unchanged and keep their current version (v0.1.2 or v0.1.1). A reference to an
  older version of a document inside an unchanged document means the current version (see `README.md`). Technology
  Architecture needed no change (its search, graph and backup statements remain consistent).
- **`contracts/openapi.yaml` 0.1.3.** v0.1.2 plus `contracts/extensions/i5.yaml`, `i6.yaml` and `i7.yaml` of the implementation
  (merged; the extension files are no longer needed), `GET /evidence-extracts/{extractId}` and `GET /health`: 111 → 138 paths,
  149 → 180 operations. Changed operations: `generateExportPackage` (202 only), `getEvidenceContent` (409),
  `listExportCandidates`, `approveDissemination`, review decisions (descriptions). New items carry `x-csaml-status: decided`,
  `x-csaml-release-class: DECIDED_V0_1_3` and `x-csaml-cr`.
- **`schemas/enums.yaml` 0.1.3.** 60 → 78 enums (345 → 417 values): `search_object_type`, `search_epistemic_status`,
  `graph_lead_type`, `graph_truncation_reason`, `review_kind`, `review_status`, `product_version_status`, `review_reason`,
  `dissemination_status`, `export_package_format`, `export_package_status`, `sharing_log_entry_type`, `job_status`,
  `retention_target_type`, `retention_rule_status`, `legal_hold_status`, `disposition_status`, `handling_change_direction`.
  Values are exactly those of the implementation (backend constants and extension enums). `RetentionRule.applies_to` left
  `unregistered_fields`.
- **`tools/check_consistency.py`.** Resolves v0.1.3 files, maps the new Annex A rows and checks v0.1.3 status blocks and tags.

### Release gates (2026-10-09)

| Gate | Result |
|---|---|
| G1–G3 Domain consistency, safety invariants, traceability | `tools/check_consistency.py`: 0 errors |
| G4 Machine contract | Redocly lint (recommended): 0 errors, 4 warnings — the three `/auth/*` redirect operations (no 2xx) and `GET /health` (no 4xx; an unauthenticated probe). The v0.1.2 warning "unused `StateConflict`" is gone (now used by `getEvidenceContent`) |
| G5 Decisions | All 30 change requests decided (this section) |
| G6 Known limitations | Listed below |

### Implementation follow-up (reference implementation)

Re-import contract and registry v0.1.3 byte-for-byte and retire `contracts/extensions/i5.yaml`, `i6.yaml`, `i7.yaml`. Code changes:
`GET /evidence-extracts/{extractId}` with `links.self` pointing to it (CR-I5-07); `Case.closed_at`, set on closure and used by
CASE_CLOSURE (CR-I7-06; replaces the `updated_at` fallback); `/api/v1/health` moves from `OUTSIDE_CONTRACT` to the contract
(CR-I7-08); the duplicate `data` member of the two list responses may be dropped (CR-I6-10). CR-I6-13: re-import
`sources/typology-source-map.yaml` with the next catalogue version.

### Still open after v0.1.3

| Item | Target |
|---|---|
| Re-review of the search timing channel (CR-I5-08) | Before real (non-synthetic) data is processed |
| ANONYMIZE and whole-case DELETE dispositions (CR-I7-05) | v0.2 |
| Indexing of evidence file content (OCR / full text); hypotheses, assessments, indicators in search | Phase 2 / v0.2 |
| Administration/audit API (other than retention and health), protected sources, `GET /capabilities` | v0.2 (per epic) |
| Gate and task status value sets; sort allowlists; task contracts | v0.2 |
| External review of CR-I4-03 (AML specialist) and CR-I1-10 (security) | Before external reliance |
| Items of the v0.1.2 "Still open" table not listed here | Unchanged |

## v0.1.2 — 2026-10-09 — Change requests from implementation increments I1–I4

**Status:** **Approved Internal Specification Baseline** — tag `v0.1.2-spec`, 2026-10-09, product owner. Supersedes `v0.1.1-spec`.
This is not an independent review. The change requests come from implementing increments I1–I4 of the reference
implementation, where each deviation or gap was recorded as a change-request candidate (`docs/change-requests.md` in the implementation repository).

### Decision

**All 52 change-request recommendations (CR-I1-01…CR-I4-14) were approved by the product owner on 2026-10-09**, with one change:
**CR-I4-10** — disconfirming searches may be appended to a finalized assessment until review approval (the I4 implementation
froze them at finalization). Decision authority for every row below: product owner, 2026-10-09.

**External review still required** (adopted for the baseline, but not to be relied on externally before review):

| ID | Review needed | Why |
|---|---|---|
| CR-I4-03 | AML specialist | The consistency-ceiling thresholds operationalise catalogue prose ("independent", "multiple", "direct authoritative evidence"); adopted provisionally |
| CR-I1-10 | Security | The clearance model (IdP roles, protected-source eligibility and per-case grant, access labels) governs authorization |

### Dispositions

`adopted` = policy or semantic rule adopted as recommended; `changed` = adopted with a change; `registry` = value set added to
`schemas/enums.yaml`; `contract` = added to `contracts/openapi.yaml`; `text` = wording fix in the specifications. Changes are tagged
in place as `*[v0.1.2 · CR-xx-yy]*` (Markdown) and `x-csaml-cr` (OpenAPI).

| ID | Area | Decision | Disposition | Where |
|---|---|---|---|---|
| CR-I1-01 | Case `investigation_questions` | `minItems` removed from the `Case` response; ≥ 1 investigation question is a case-activation (gate) precondition | adopted | Contract `Case`; Data Model §6.1; API §12; SRS-FR-CASE-001 |
| CR-I1-02 | Case memberships | `GET/POST /cases/{caseId}/memberships`, `PATCH/DELETE /case-memberships/{membershipId}` (If-Match), explicit `protected_source_authorized`; registry `case_membership_role` LEAD/ANALYST/REVIEWER | contract + registry | Contract; `schemas/enums.yaml`; Data Model §6.3; API §12, §20 |
| CR-I1-03 | CSRF token delivery | `Session.csrf_token`; secret in the server-side session, no JavaScript-readable CSRF cookie | contract | Contract `Session`, `csrfHeader`; API §4; Frontend; Technical Stack |
| CR-I1-04 | Browser logout | Logout is a top-level form POST carrying `csrfmiddlewaretoken`; API clients may use `X-CSRFToken` | contract | Contract `authLogout`; API §4; Frontend |
| CR-I1-05 | Back-channel logout | `POST /auth/backchannel-logout` (OIDC Back-Channel Logout 1.0, signed logout token, CSRF-exempt) | contract | Contract; API §4; Technical Stack |
| CR-I1-06 | Local-dev session cookie | Isolated local-development exception to `__Host-csaml_session` + Secure, stated next to API-SEC-01 | text | API §4; Technical Stack; contract `sessionCookie` |
| CR-I1-07 | `Session.username` | Optional display field added | contract | Contract `Session`; API §4 |
| CR-I1-08 | `risk_rating`, `closure_reason` | Registry enums defined (minimal sets; the implementation had free strings) | registry | `schemas/enums.yaml`; contract `Case`; Data Model §6.1, Annex A |
| CR-I1-09 | Case reclassification | Only the case LEAD may change classification/labels; upgrades only; downgrades and label removal need a reviewer decision (workflow in I6, 403 until then) | adopted | Contract `CasePatch`; Data Model §6.1, §16; API §12; SRS |
| CR-I1-10 | Clearance model | IdP roles `csaml-clearance-sensitive` / `csaml-clearance-restricted` (baseline INTERNAL), `csaml-protected-source` + per-case `protected_source_authorized`, `csaml-label-<label>` | adopted — **needs external security review** | Data Model §16; Technical Stack |
| CR-I2-01 | `case_links` on creates | Required, 1..20, on every create that carries it | text | Contract (all `*Create` schemas); API |
| CR-I2-02 | Upload sessions | Registry `upload_session_status` INITIATED/CONTENT_RECEIVED/COMPLETED; 422/400 confirmed (no 413/416); `DerivativeCreate` reworded | registry | `schemas/enums.yaml`; contract `UploadSession`; API §13; SRS Annex B |
| CR-I2-03 | Envelope status (Source, EvidenceExtract) | Registry `envelope_status` (REGISTERED, RECORDED, DRAFT, FINALIZED) for classes without a lifecycle | registry | `schemas/enums.yaml`; contract `ResourceEnvelope`; Data Model |
| CR-I2-04 | Provenance trace | `GET /{entities,relationships,facts}/{id}/provenance` and `ProvenanceTrace` | contract | Contract; API §14 |
| CR-I2-05 | Classification inheritance | Declared value below the inputs' maximum → 422; later input upgrades flag dependents "re-review required" (no automatic raise) | adopted | Contract `ResourceEnvelope`; Data Model §16; API; SRS |
| CR-I2-06 | Small I2 extensions | `GET /evidence/{id}/extracts`, `entity_id` filter, EvidenceItem `byte_size`/`hash_algorithm`/`derived_from`/`derivation_type`, `alias_provenance`, opaque `storage_ref` | contract | Contract; API §13–§14; Data Model §7.2 |
| CR-I2-07 | Evidence reference targets | Permitted target classes per field (`x-csaml-ref-types`) | contract | Contract; Data Model §7–§9; API |
| CR-I2-08 | `Claim.credibility_grade` | Registry `credibility_grade` with names and digit `code`s; the wire keeps "1".."6" (registry exception `wire: code`) | registry | `schemas/enums.yaml`; contract `CredibilityGrade`; Data Model §7.4, Annex A |
| CR-I2-09 | Reviewer = decider | API §14 aligned to 409 STATE_CONFLICT | text | API §14; contract merge/unmerge |
| CR-I2-10 | High-impact merge | Every MERGE/UNMERGE is high-impact in the MVP; `reviewer_ref` required (REVIEWER/LEAD membership) | adopted | Contract `MergeRequest`/`UnmergeRequest`; Data Model §8.4; API §14; Methodology §12; SRS |
| CR-I2-11 | Reviewer role; claim re-review | ESTABLISH by REVIEWER or LEAD membership, never the proposer; claim decisions by LEAD/ANALYST/REVIEWER; a decided claim may return to UNDER_REVIEW | adopted | Contract; Data Model §7.4–§7.6; API §16A; SRS; Methodology |
| CR-I2-12 | Integrity check results | No change (implementation conforms) | text (no change) | — |
| CR-I2-13 | Unmerge re-attribution | Merge is logical repointing via `canonical_parent`; canonical model | adopted | Contract; Data Model §8.4; API §14; Methodology §12 |
| CR-I2-14 | Match-candidate decisions | `POST /resolution-decisions` kept; `/entity-match-candidates/{id}/decisions` deprecated (removal in v0.2) | text | Contract (`deprecated: true`); API §14; SRS Annex C |
| CR-I2-15 | DM-I06 basis | DM-I06 points to `confidence.basis` | text | Data Model §18 |
| CR-I3-01 | Assets, ownership, control | Operations and schemas of `contracts/extensions/i3.yaml` adopted | contract | Contract; API §14 |
| CR-I3-02 | Events and timeline | `/events`, `/events/{eventId}`, `/timeline`; Event `description`, `approximate`, `asset_refs` | contract | Contract; API §15; Data Model §10.2 |
| CR-I3-03 | Value-flow view and legend | Shapes adopted | contract | Contract; API §15; UI Design System §11 |
| CR-I3-04 | `ValueFlowLeg` | Per-leg `reconstruction_basis` and `confidence`; legs immutable, append-only, contiguous | contract | Contract; Data Model §11.2; API §15; SRS |
| CR-I3-05 | Envelope status (Asset, Event, ValueFlow) | Registry `envelope_status`; Methodology §14.1 event statuses deferred to v0.2 | registry | `schemas/enums.yaml`; Data Model §10; Methodology §14 |
| CR-I3-06 | Precision value sets | Registry `money_precision`, `temporal_precision`; `Event.start_time` null only with UNKNOWN; `valuation_basis` stays free text | registry | `schemas/enums.yaml`; contract `Money`, `TemporalValue`, `TimePrecision`; Data Model §10; Methodology §14 |
| CR-I3-07 | Graph API | `GET /cases/{caseId}/graph` adopted; `POST /graph/query` stays unspecified (v0.2) | contract | Contract; API §18 |
| CR-I3-08 | Asset targets; I3 provenance | `Relationship.to_entity` may name an Asset (`to_object_type`); provenance operations for I3 objects | contract | Contract; Data Model §9.1; API §14–§15 |
| CR-I3-09 | Raising certainty | Order HYPOTHETICAL < RECONSTRUCTED < DOCUMENTED < DIRECT for invariants only (registry stays unordered); raising needs new evidence; a flow is never stronger than its weakest leg | adopted | Contract `ValueFlowPatch`; Data Model §11; Methodology; SRS |
| CR-I3-10 | Flow evidence targets | EvidenceExtract/EvidenceItem/Fact; DIRECT and DOCUMENTED need ≥ 1 EvidenceItem/EvidenceExtract | contract | Contract; Data Model §11; API §15 |
| CR-I3-11 | Inferred ownership | BENEFICIAL / ECONOMIC_INTEREST / NOMINEE_ASSERTED become ESTABLISHED only with an ESTABLISHED Fact | adopted | Contract (OwnershipInterest); Data Model §9.2; Methodology |
| CR-I3-12 | Value aggregation | Groups by (flow_class, flow_type, currency), no grand total, obligation vs settlement, unknown never 0 | contract | Contract `ValueFlowView`; API §15; UI Design System §11; SRS |
| CR-I3-13 | `case_links` on `ValueFlowCreate` | As CR-I2-01 | text | Contract; API |
| CR-I4-01 | Typology catalogue API | `/typology-catalogue`, `/typologies`, `/typologies/{typologyId}` adopted | contract | Contract; API §16; Typology Catalogue |
| CR-I4-02 | Indicators | `/indicators` operations, `LOCAL-…` code convention, transition table | contract | Contract; Data Model §12.1; API §16; Typology Catalogue; SRS |
| CR-I4-03 | Consistency ceiling | ADR-0023 thresholds adopted **provisionally** | adopted — **needs AML-specialist review** | Typology Catalogue §4.1; contract `TypologyMatch` (`x-csaml-review-required`); Data Model §12.2; API §16; SRS |
| CR-I4-04 | Hypothesis matrix | `HypothesisLink` (`/hypotheses/{id}/links`, `/hypothesis-matrix`) | contract | Contract; Data Model §13.1; API §16 |
| CR-I4-05 | Gaps, revisions, I4 provenance | `/intelligence-gaps`, `/assessments/{id}/revisions`, indicator/match/hypothesis provenance | contract | Contract; Data Model §13; API §16; SRS-FR-ASM-001 |
| CR-I4-06 | Hypothesis role | Registry `hypothesis_role`; `role`, `assumptions[]` fields | registry | `schemas/enums.yaml`; contract `Hypothesis*`; Methodology §18.1; Data Model §13.1 |
| CR-I4-07 | Matrix effect vocabulary | Registry `hypothesis_link_effect` SUPPORTS/CONTRADICTS/NEUTRAL/UNKNOWN ("Weakens" → CONTRADICTS) | registry | `schemas/enums.yaml`; contract; Methodology §18.2; SRS-FR-HYP-002 |
| CR-I4-08 | Competing hypotheses | Enforced at assessment finalize: 409 `COMPETING_HYPOTHESES_REQUIRED` | adopted | Contract `finalizeAssessment`; Methodology §18.4; SRS-FR-HYP-001; API §16 |
| CR-I4-09 | Assessment lifecycle | Finalized ≠ reviewed; envelope status DRAFT → FINALIZED, then the review status | text | Contract `Assessment`; Data Model §13.3; API §16; SRS Annex B |
| CR-I4-10 | Disconfirming searches after finalize | **Changed:** searches MAY be appended to a finalized assessment until review approval, then frozen (409); SRS-FR-ASM-004 is checked at review approval. The I4 implementation (409 after finalization) must change | changed | Contract `recordAssessmentDisconfirmingSearch`, `Assessment`; Data Model §13.3; API §16; SRS-FR-ASM-004; Methodology |
| CR-I4-11 | Dependent flagging | Direct and indirect dependents flagged `review_required`; a flagged draft cannot be finalized (409 `REVIEW_REQUIRED`); clearing is a review action (I6) | adopted | Contract `Assessment`, `finalizeAssessment`; Data Model §7.5, §13.3; SRS |
| CR-I4-12 | `case_links` on I4 creates | As CR-I2-01 | text | Contract; API |
| CR-I4-13 | Catalogue entry metadata | Entry `version` 0.1.1, `status` ACTIVE, `last_reviewed` 2026-10-08, indicator IDs `<typology_id>-I<nn>` | text | Typology Catalogue §5, §8 |
| CR-I4-14 | `AssessmentProvenance` | Trace fields (`typology_match_refs`, `source_refs`, `gap_refs`, `root`, `nodes`, `edges`, `source_paths`) and permitted target types | contract | Contract; API §16 |

### What changed

- **Documents.** Eight documents changed and were renamed with `git mv` to `*_v0.1.2.md` (history preserved): Data Model, API
  Specification, SRS, Technical Stack and Repository, Investigation Methodology, Typology Catalogue, Frontend Architecture and State
  Management, UI Design System. The other 15 Markdown documents are unchanged and stay at v0.1.1; they remain current. A reference to
  "<document> v0.1.1" in an unchanged document means the current version of that document (see `README.md`, "Versi dokumen").
- **`contracts/openapi.yaml` 0.1.2.** The frozen v0.1.1 contract plus `contracts/extensions/i3.yaml` and `i4.yaml` of the implementation
  (merged; the extension files are no longer needed) and the I1/I2 additions: 72 → 111 paths, 92 → 149 operations. New items carry
  `x-csaml-status: decided`, `x-csaml-release-class: DECIDED_V0_1_2` and `x-csaml-cr`; reference fields carry `x-csaml-ref-types`.
  `decideEntityMatchCandidate` is `deprecated: true`.
- **`schemas/enums.yaml` 0.1.2.** 50 → 60 enums (301 → 345 values): `case_membership_role`, `risk_rating`, `closure_reason`,
  `upload_session_status`, `envelope_status`, `credibility_grade` (registry exception `wire: code`), `money_precision`,
  `temporal_precision`, `hypothesis_role`, `hypothesis_link_effect`. The implementation's registry copy had no extra values.
- **`tools/check_consistency.py`.** Resolves each document to its current version, maps the new Annex A rows, supports `wire: code`,
  and checks v0.1.2 status blocks, tags outside code fences and that every cited CR ID is listed here.

### Release gates (2026-10-09)

| Gate | Result |
|---|---|
| G1–G3 Domain consistency, safety invariants, traceability | `tools/check_consistency.py`: 0 errors |
| G4 Machine contract | Redocly lint (recommended): 0 errors, the 4 known warnings of v0.1.1 |
| G5 Decisions | All 52 change requests decided (this section) |
| G6 Known limitations | Listed below |

### Implementation follow-up (reference implementation)

Changes the implementation needs to conform to v0.1.2: allow disconfirming searches after finalization until review approval
(CR-I4-10); `risk_rating` / `closure_reason` as registry enums (CR-I1-08); the case-membership endpoints (CR-I1-02; I1 used a management
command); case reclassification by reviewer decision and clearing of `review_required` arrive with review in I6 (CR-I1-09, CR-I4-11).

### Still open after v0.1.2

| Item | Target |
|---|---|
| Search, administration/audit, protected sources, `GET /capabilities`, `POST /graph/query` | v0.2 (per epic) |
| Job, gate and task status value sets; export format; sort allowlists; task contracts | v0.2 |
| Methodology §14.1 event statuses; `Asset.valuation_basis` and `derivation_type` vocabularies | v0.2 |
| Removal of `/entity-match-candidates/{id}/decisions` | v0.2 |
| Reviewer-decision workflows (reclassification downgrade, `review_required` clearing, review approval) | I6 |
| External review of CR-I4-03 (AML specialist) and CR-I1-10 (security) | Before external reliance |
| Items of the v0.1.1 "Still open" table not listed here (ADR-0005 product selection, A13 research track, release package, independent review) | Unchanged |

## v0.1.1 — 2026-10-08 — Audit remediation (Markdown)

**Status:** **Approved Internal Specification Baseline** — tag `v0.1.1-spec`, 2026-10-08, product owner. Not yet implemented, tested or independently reviewed.

### Release gates (all passed on 2026-10-08)

| Gate | Pass condition | Result |
|---|---|---|
| G1 Domain consistency | Claim/Fact, entity resolution, ValueFlow, classification and confidence each have one authoritative meaning | Passed (D-A08, D-A09, D-A10, D-ER) |
| G2 Safety invariants | Authorization, source protection, evidence integrity, approval/export and certainty promotion are unambiguous and non-waivable | Passed (D-A16) |
| G3 Traceability | Feature → SRS → story → screen/API has no broken or double-meaning IDs | Passed (`tools/check_consistency.py`: 0 errors) |
| G4 Machine contract | OpenAPI slice valid, `$ref`s resolve, enums match the registry, lint without errors | Passed (Redocly: 0 errors, 4 accepted warnings) |
| G5 Proposed decisions | No open contract choice affects a blocking area | Passed: all 51 open choices classified; 7 MUST_DECIDE decisions recorded (API Specification §28) |
| G6 Known limitations | Everything unfinished is stated as open and assigned to a release | Passed (see "Still open" below) |

Rule after the tag: the documents are not re-audited unless a substantive change is made. Problems found during implementation go
through issue → change request → v0.1.2.

### Source of truth

- `Documents/*_v0.1.1*.md` is now the **canonical source** and contains the full text of every document, with corrections applied.
- `Documents/*_v0.1*.docx` and `*.pdf` are the **unchanged v0.1 baseline**. They are legacy and were not updated by this release.
- The v0.1 Markdown files were short companions (audit A12). They were first replaced by full conversions of the DOCX (commit `763a28b`, converter in `tools/docx2md/`). The audit corrections came after that, so `git diff` shows exactly what v0.1.1 changed.
- `CS-AML_Framework_v0.1.1.md` (the non-expanded original) is marked **Legacy**. Use `CS-AML_Framework_v0.1.1_Expanded.md`.
- Every change is tagged in place as `*[v0.1.1 · Axx]*`, where Axx is the audit finding ID from `Audit/CS-AML_Documentation_Audit_2026-10-07.md`.

### Decision register

Each decision is a product-owner decision (**Approved**) or an audit-derived correction (**Adopted**). Adopted
corrections apply the audit's recommendation and need no separate approval, but the product owner can still overturn
them. "Approved" records a decision, not proof that it has been implemented or tested.

| ID | Decision | Status · date · authority | Rationale | Affected specifications |
|---|---|---|---|---|
| D-A06 | MVP keeps **six** intelligence product templates: Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report | Approved · 2026-10-08 · Product owner | Keep the PRD/SRS scope; align the backlog with it instead of cutting requirements | Product & Feature, PRD, SRS, MVP Breakdown, Sprint Plan, Screen Inventory, Data Model (`product_type`) |
| D-A08 | **Five-level** classification is authoritative: `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`; fail closed; Restricted/Highly Restricted are never auto-mapped | Approved · 2026-10-08 · Product owner | One policy model for authorization, label inheritance, export and retention | Data Model §16, Framework Expanded §6.4, Methodology, Technology Architecture, API, SRS, UX/UI documents |
| D-A02/A03 | Object storage: S3-compatible, product chosen in ADR-0005. Broker/cache: **Valkey 8.x** (BSD-3-Clause), pinned (ADR-0006) | Approved · 2026-10-08 · Product owner | MinIO Community is archived; the Redis 7.x range spans several licences | Technical Stack, Technology Architecture, Product & Feature Annex C, `docs/adr/0005`, `docs/adr/0006` |
| D-A11 | Browser auth: **server-side session (BFF)**. Django is the OIDC client to Keycloak, the cookie is HttpOnly, CSRF goes in a header, and no tokens reach JavaScript | Approved · 2026-10-08 · Product owner | Removes the session/bearer ambiguity; keeps tokens out of reach of script | API, Frontend, Technical Stack, SRS-IF-003, MVP ST-E1-01, `docs/adr/0004` |
| D-A10 | Claim/Fact lifecycle. A Claim is a permanent source record. A **VerificationDecision** (append-only) evaluates it. A **Fact** is a separate object *supported by* claims/evidence and decisions; there is no claim→fact "promotion". Feature **F-EVD-008**, SRS-FR-CLM-001…004, story ST-E3-07 | Approved · 2026-10-08 · Product owner (with the refinement from the remediation review) | Keeps source assertions and analytical conclusions apart; makes fact revision and impact on products traceable | Data Model §7.4–7.6, API §16A, SRS, Product & Feature, PRD, MVP Breakdown, Sprint Plan, Screen Inventory, UX/UI, Technology Architecture, Methodology |
| D-ER | Entity resolution. `Entity.resolution_status` is **state** (UNRESOLVED/RESOLVED/CONFLICTED/MERGED/SPLIT). **ResolutionDecision** is an append-only **decision** over records (MERGE/KEEP_SEPARATE/POSSIBLE_MATCH/DEFER/UNMERGE). New SRS-FR-ENT-006 | Approved · 2026-10-08 · Product owner | Methodology outcomes and Data Model state used different vocabularies for different things | Data Model §8.1/§8.4, Methodology §12, API §14, SRS, Product & Feature, MVP, Sprint, Screen Inventory, UX/UI, Technology Architecture |
| D-A04 | Stale `If-Match` → 412 `PRECONDITION_FAILED`; missing → 428; 409 `STATE_CONFLICT` only for workflow state; `VERSION_CONFLICT` retired. Multi-entity commands use a body map `expected_versions` | Adopted · 2026-10-08 | RFC 9110 precondition semantics; an If-Match list cannot guard several resources | API §9–§11, §14; Frontend; SRS-IF-002; UX; Component Inventory |
| D-A05 | F-ASM-003 keeps its meaning. SRS-FR-ASM-003 traces to F-ASM-001, and the new SRS-FR-ASM-004 covers the disconfirming search record | Adopted · 2026-10-08 | IDs must not change meaning | SRS, MVP Breakdown |
| D-A07 | Product `CAP-01…15` is the authoritative registry; Technology Architecture uses `TA-CAP-01…16` with a crosswalk | Adopted · 2026-10-08 | One global ID must have one meaning | Technology Architecture, Product & Feature, SRS |
| D-A09 | All wire enums use UPPER_SNAKE_CASE, registered in `schemas/enums.yaml`; confidence adds `INSUFFICIENT_BASIS`, which is never coerced to LOW/null | Adopted · 2026-10-08 | One serialisation for DB/API/UI/export | Data Model Annex A, all specs, `schemas/enums.yaml`, `contracts/openapi.yaml` |
| D-A16 | Non-waivable release invariants: authorization bypass, source exposure, evidence/provenance loss, certainty promotion, approval bypass, broken audit history | Adopted · 2026-10-08 | Waivers must not license breaking core safety invariants | Sprint Plan, Framework Expanded §3.4, Control Guide, SRS, MVP |
| D-G5 | Seven contract decisions: missing REQUIRED Idempotency-Key → 400, not executed; review approval bound to frozen version; export only within approved scope; merge/unmerge reviewer ≠ decider; all-or-nothing upload completion; immutable relationship endpoints/type; verify-integrity without If-Match | Approved · 2026-10-08 · Product owner | Release gate G5: no open choice may affect a blocking area | API §28, `contracts/openapi.yaml` |

### Changes per audit finding

| Finding | Main changes | Documents |
|---|---|---|
| A01 Readiness claims | Status block in every document; "approved/official/normative baseline/handoff" wording softened; WCAG, metrics and estimates labelled as targets | All |
| A02 MinIO | MinIO removed as reference store; ADR-0005 requirements; topology and compose updated | Technical Stack, Technology Architecture |
| A03 Redis | Valkey 8.x pinned plus SBOM licence; Redis licence note by release line | Technical Stack, Technology Architecture, Product & Feature |
| A04 409/412 | Error table, concurrency rules, examples, evaluation order, frontend error mapping, ConflictState component | API, Frontend, SRS, UX, Component Inventory |
| A05 F-ASM-003 | SRS-FR-ASM-003 traceability fixed; SRS-FR-ASM-004 added; separate tests in backlog | SRS, MVP Breakdown |
| A06 Templates | Six templates in backlog ST-E8-01, Sprint 7, PRD, Screen SCR-PRD-002, Data Model `product_type` (adds `CASE_REPORT`) | MVP Breakdown, Sprint Plan, PRD, Screen Inventory, Data Model |
| A07 CAP namespace | `TA-CAP-xx` plus crosswalk; product registry declared authoritative | Technology Architecture, Product & Feature, SRS |
| A08 Classification | Five-level model, access labels, inheritance, fail closed, legacy mapping | Data Model §16, Framework Expanded §6.4, Methodology, Technology Architecture, API, SRS, Product & Feature, UX/UI documents |
| A09 Enums/confidence | Annex A registry uppercase; `flow_class`; `confidence.level` with INSUFFICIENT_BASIS; UI badges and display labels | Data Model, SRS, API, Frontend, Methodology, UI Design System, Component Inventory, UX, IA |
| A10 Claim/Fact | Data Model §7.4–7.6, API §16A, SRS-FR-CLM-001…004, F-EVD-008, ST-E3-07 (Sprint 2), screen responsibilities, UI rule "claim ≠ fact without decision" | Data Model, API, SRS, Product & Feature, PRD, MVP Breakdown, Sprint Plan, Screen Inventory, UX/UI, Technology Architecture |
| A11 API contract | BFF auth, headers, idempotency semantics, OpenAPI SHALL (`contracts/openapi.yaml`), explicit open-items list | API, Frontend, Technical Stack, SRS, MVP Breakdown |
| A12 Companion Markdown | Full-text Markdown for all 23 documents; Markdown is canonical | All, `MANIFEST.txt` |
| A13 Sources | "Pending verification" labels for generic lineage and UNODC page-level claims; CS-AML design conventions labelled as such | Framework Expanded, Framework (legacy), Methodology, Typology Catalogue |
| A14 DIRECTOR_OF | Annex D redrawn: `Person B --DIRECTOR_OF--> Company A` | Data Model |
| A15 Case Register | SCR-CASE-001 → WF-PAT-01 | Wireframe, Screen Inventory, High-Fidelity UI |
| A16 Release waivers | Non-waivable invariants; disable-with-non-reachability-proof; waiver conditions | Sprint Plan §1.1/§7.2, Framework Expanded §3.4, Control Implementation Guide, SRS, MVP Breakdown |

### Round 2 — follow-up to the remediation review (2026-10-08)

- **A10 approved and refined.** Claims are permanent; a Fact is a separate object supported by claims/evidence and VerificationDecisions. `source_claim_refs` → `supporting_claim_refs`; Fact decision `PROMOTE` → `CREATE`; SRS-FR-CLM-003 retitled "Fact creation from supporting claims and evidence". Approval qualifiers removed.
- **Entity resolution approved.** New Data Model §8.4 ResolutionDecision, DM-I15, SRS-FR-ENT-006, UXR-ENT-006; Methodology §12.2 outcomes are now decision values (legacy mapping MERGED→MERGE, LINKED_POSSIBLE→POSSIBLE_MATCH, SEPARATE→KEEP_SEPARATE, UNRESOLVED→DEFER); API resolution-decision endpoints.
- **Multi-entity preconditions.** Merge, unmerge and resolution-decision commands use a body map `expected_versions` (missing → 428, mismatch → 412), because an `If-Match` list cannot guard several resources.
- **`schemas/enums.yaml`.** Machine registry of 50 wire enums (301 values) with display labels; the Typology Catalogue enums are now UPPER_SNAKE_CASE.
- **`contracts/openapi.yaml`.** OpenAPI 3.1 contract for the P0 vertical slice (72 paths, 92 operations), contract-first. Choices not fixed by the specs are marked `x-csaml-status: proposed`. Redocly lint passes.
- **`sources/typology-source-map.yaml`.** Register of all 89 indicators across the 20 typologies, each with origin and verification status. None is verified at section/page level yet.
- **ADRs.** `docs/adr/0004` (BFF session, Accepted), `0005` (object storage, Proposed — product not selected), `0006` (Valkey 8.x, Accepted).
- **`tools/check_consistency.py`.** Automated checks: registry ↔ Data Model Annex A ↔ OpenAPI enums, `$ref`s, operationIds, path parameters, retired terms, feature/SRS/story references, the TA-CAP namespace and code fences.
- **Consistency audit.** `Audit/CS-AML_Consistency_Audit_v0.1.1_2026-10-08.md` is an AI-performed internal check, not independent verification. It found 19 issues (C01–C19); all were fixed in round 3 below.

### Round 3 — fixes for consistency audit C01–C19 (2026-10-08)

Changes are tagged `*[v0.1.1 · Cxx]*`.

- **C01/C02 Fact creation.** `POST /cases/{caseId}/facts` creates the Fact and its CREATE VerificationDecision in one transaction (`decision_rationale` required). Establish, dispute and supersede likewise create their decisions. A Fact needs `supporting_evidence` (1..n); `supporting_claim_refs` is optional (0..n).
- **C03–C05 Multi-entity preconditions.** The `expected_versions` exception to "mutations send If-Match" is now stated in every document. In OpenAPI the map is not schema-required, so a missing map returns 428, not 422. It is adopted, not proposed.
- **C06/C07.** Match-candidate outcomes use wire values (unresolved/defer → DEFER). The API §14 table is repaired.
- **C08.** SRS Annex B state models are rederived from `schemas/enums.yaml` and the Data Model.
- **C09.** 10 relationship types were registered: AUTHORIZED_SIGNATORY_OF, COMMISSIONER_OF, MANAGES, USES, LENDER_TO, LEASED_TO, DONATED_TO, FUNDED_BY, SHARES_DOMAIN_WITH, TRANSFERRED_VALUE_TO. The rest map to existing types (Data Model Annex B).
- **C10 Disconfirming search.** `Assessment.disconfirming_searches[]` and `high_impact_adverse`; `POST /assessments/{assessmentId}/disconfirming-searches`. It is enforced at review approval (409 `details.reason = DISCONFIRMATION_REQUIRED`), not at finalize. Traced in MVP E6 and Sprint 5.
- **C11.** Dependent-flagging tests moved to Sprint 5 (assessments) and Sprint 7 (products).
- **C12/C13.** API §28 is contract-first. SRS Annex C paths are aligned with the API, and the "An The" typo is fixed.
- **C14–C19.** Typed entity filters; stale OpenAPI comments removed; promotion wording in the Control Guide and UX removed; claim/fact/resolution UI mapped to existing component IDs (count stays 65) and frontend feature owners named; upload content is PUT only; If-Match on claim verification decisions; tags moved out of code fences; ADR-0003 (S3 capability/layout) vs ADR-0005 (product selection) split stated.
- **Validation after round 3.** `tools/check_consistency.py`: 0 errors. Redocly lint: 0 errors, 4 known warnings.

### Round 4 — release gate G5 (2026-10-08)

- All 51 open OpenAPI choices were classified once with `x-csaml-release-class`: 13 markers MUST_DECIDE_V0_1_1 (7 decisions + 2 confirmations of A10/D-A09 + the missing Idempotency-Key rule), 37 ACCEPT_DEFAULT_V0_1_1, 2 DEFER_V0_2 (task contracts).
- The seven decisions (API Specification §28): missing REQUIRED Idempotency-Key → 400, not executed; review approval bound to the frozen `target_version`; export limited to the approved dissemination scope; merge/unmerge reviewer is a principal ≠ decider; upload completion all-or-nothing; relationship endpoints/type immutable; verify-integrity without If-Match.
- Document status changed from "Draft for Review" to "Approved Internal Specification Baseline" in 22 documents (the legacy Framework stays legacy).

### Still open — non-blocking, assigned to a future release

| Item | Why it is not blocking | Target |
|---|---|---|
| OpenAPI outside the slice: assets, events, timeline, typologies/indicators/matches, gaps, search, graph, administration/audit, protected sources, `GET /capabilities` | Not needed to run the core vertical slice; added when the epic starts | v0.2 (per epic) |
| Open value sets (job, upload-session, gate and task status; risk rating; amount precision; export format), sort allowlists, CSRF-token delivery detail, task contracts | Accepted defaults / plain strings do not change domain meaning | v0.2 |
| Overlap of `/entity-match-candidates/{id}/decisions` and `POST /resolution-decisions` | Both create the same ResolutionDecision; no semantic conflict | v0.2 (keep one) |
| ADR-0005 product selection (ADR-0001 to ADR-0003 not written) | S3 capability, versioning, integrity and restore requirements are authoritative; product chosen at deployment | Before first deployment with real evidence |
| 10 unregistered enum fields (`schemas/enums.yaml` → `unregistered_fields`, incl. `credibility_grade` 1–6) | Not used as wire enums in the slice | v0.2 |
| Entity display vocabulary (candidate/probable/confirmed) mapped, not replaced | Mapping to state and decision values is explicit | v0.2 |
| A13 Research Track: page-level verification of 89 typology indicators (69 pending, 20 CS-AML design) | No indicator claims FATF/PPATK/UNODC provenance without a "pending verification" label | Parallel research track |
| Release package (Markdown + DOCX + PDF regenerated from v0.1.1) | DOCX/PDF v0.1 remain the historical baseline | Once, after the freeze |
| Independent review and implementation evidence | "Specification approved" ≠ "independently validated" ≠ "implementation tested" ≠ "production validated" | Vertical slice implementation |

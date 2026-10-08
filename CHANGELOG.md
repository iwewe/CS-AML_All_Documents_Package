# CS-AML Changelog

## v0.1.1 — 2026-10-08 — Audit remediation (Markdown)

**Status:** Draft for Review (Proposed Internal Baseline). Not validated.

### Source of truth

- `Documents/*_v0.1.1*.md` is now the **canonical source** and contains the full text of every document, with corrections applied.
- `Documents/*_v0.1*.docx` and `*.pdf` are the **unchanged v0.1 baseline**. They are legacy and were not updated by this release.
- The v0.1 Markdown files were short companions (audit A12). They were first replaced by full conversions of the DOCX (commit `763a28b`, converter in `tools/docx2md/`). The audit corrections came after that, so `git diff` shows exactly what v0.1.1 changed.
- `CS-AML_Framework_v0.1.1.md` (the non-expanded original) is marked **Legacy**. Use `CS-AML_Framework_v0.1.1_Expanded.md`.
- Every change is tagged in place as `*[v0.1.1 · Axx]*`, where Axx is the audit finding ID from `Audit/CS-AML_Documentation_Audit_2026-10-07.md`.

### Decisions applied

| ID | Decision | Authority |
|---|---|---|
| D-A06 | MVP keeps **six** intelligence product templates: Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report | Product owner |
| D-A08 | **Five-level** classification from the Data Model is authoritative: `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`; fail closed; legacy mapping never automatic for Restricted/Highly Restricted | Product owner |
| D-A02/A03 | Object storage: S3-compatible, product chosen by ADR-0005 (MinIO Community no longer a default). Broker/cache: **Valkey 8.x** (BSD-3-Clause), pinned, ADR-0006 | Product owner |
| D-A11 | Browser auth: **server-side session (BFF)**. Django acts as the OIDC client to Keycloak, the browser holds an HttpOnly cookie, CSRF is sent in a header, and no tokens reach JavaScript | Product owner |
| D-A04 | Stale `If-Match` → 412 `PRECONDITION_FAILED`; missing → 428; 409 `STATE_CONFLICT` only for workflow state; `VERSION_CONFLICT` retired | Audit recommendation / RFC 9110 |
| D-A05 | F-ASM-003 keeps its meaning. SRS-FR-ASM-003 now traces to F-ASM-001, and the new SRS-FR-ASM-004 covers the disconfirming search record | Audit recommendation |
| D-A07 | Product `CAP-01…15` is the authoritative registry; Technology Architecture renamed to `TA-CAP-01…16` with a crosswalk | Audit recommendation |
| D-A09 | All wire enums use UPPER_SNAKE_CASE; confidence adds `INSUFFICIENT_BASIS`, which is never coerced to LOW/null | Audit recommendation |
| D-A10 | Claim/Fact lifecycle: `claim_status`, VerificationDecision (append-only), fact promotion/revision, `review_required` flagging. New feature **F-EVD-008**, requirements SRS-FR-CLM-001…004, story ST-E3-07 | **Proposed — needs product-owner approval** |
| D-A16 | Non-waivable release invariants: authorization bypass, source exposure, evidence/provenance loss, certainty promotion, approval bypass, broken audit history | Audit recommendation |

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

### Still open (not resolved by v0.1.1)

- **Approval:** D-A10 (Claim/Fact lifecycle) and every "proposed" item need a recorded product-owner decision.
- **OpenAPI and schemas:** `contracts/openapi.yaml` and per-operation request/response schemas do not exist yet (API §28 open items). This includes the response for a missing required `Idempotency-Key` and the pagination envelope.
- **ADR files:** ADR-0005 (object storage) and ADR-0006 (Valkey) are required but not written; no product or release has been selected yet.
- **Entity resolution outcomes:** Methodology §12.2 (`MERGED/LINKED_POSSIBLE/SEPARATE/UNRESOLVED`) differs from Data Model `Entity.resolution_status`. This needs a domain decision.
- **Remaining lowercase enums:** Typology Catalogue statuses, and some free-text enum fields in the Data Model (`valuation_basis`, `basis`).
- **Source mapping:** a per-indicator mapping to source section/page (A13) is not done; references the audit did not check remain unlabelled.
- **Legacy DOCX/PDF:** these are still v0.1 and do not include these corrections.
- **Verification:** nothing in v0.1.1 has been verified independently or tested against an implementation. Specification status "corrected" ≠ implementation status "tested".

# CS-AML Changelog

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

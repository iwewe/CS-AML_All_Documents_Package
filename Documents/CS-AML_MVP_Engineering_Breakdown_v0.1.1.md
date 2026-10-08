Engineering execution baseline for MVP 0.1

From SRS requirements to epics, stories, tasks, acceptance tests, dependencies, and release evidence.

> **Document status — v0.1.1**  
> Version: 0.1.1 — Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec). *[v0.1.1 · A01]*  
> Supersedes: CS-AML MVP Engineering Breakdown v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.  
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (decision register and release gates in `CHANGELOG.md`). No implementation test result or independent audit exists yet. Acceptance criteria in this document are targets, not evidence that tests have passed.  
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.  
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

Status: Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) — baseline for engineering planning and backlog creation *[v0.1.1 · A01]*

# 1. Purpose and Engineering Objective

This document translates the CS-AML Product Requirements Document v0.1.1 and Software Requirements Specification v0.1.1 (both draft for review) *[v0.1.1 · A01]* into an executable MVP engineering plan. It does not redefine product requirements. It establishes engineering work packages, sequencing, acceptance evidence, and a common definition of completion.

> **MVP release objective: a two-analyst team SHALL complete one sensitive investigation from case opening through independently reviewed and approved intelligence product, with provenance, authorization, and auditability intact.**

## 1.1 Traceability chain

Framework → Product Feature → PRD → SRS → Epic → Story → Engineering Task → Acceptance Test → Release Evidence

## 1.2 Engineering principles

- Vertical slices over component completion.

- Canonical data first; search and graph remain rebuildable projections.

- Secure-by-default authorization is implemented in services/API, not only presentation logic.

- Analytical uncertainty is preserved in schema, UX, export, and tests.

- Every critical capability is accepted through observable behavior, not merely code presence.

- MVP integration scope is deliberately narrow; advanced OCR, sanctions, blockchain analytics, AI assistant and federation remain post-MVP unless required to unblock the release scenario.

# 2. MVP Scope Baseline

The P0 baseline is the mandatory release scope defined by the PRD/SRS. The engineering backlog groups those requirements into ten epics and eight delivery increments. P1/P2 capabilities are excluded unless explicitly promoted through change control.

| **Epic** | **Name** | **Release outcome** | **Primary traceability** |
|----|----|----|----|
| E0 | Platform Foundation & Delivery | Establish the deployable application skeleton, environments, CI/CD, canonical database, evidence storage, audit substrate, and engineering conventions. | SRS-OPS; SRS-DR; SRS-AUD; F-OPS-001; F-AUD-001 |
| E1 | Identity, Access & Protected Sources | Implement OIDC/MFA integration, role/object access controls, case membership, classification, and protected-source compartment. | SRS-SEC; F-SEC-001..003 |
| E2 | Case & Investigation Workflow | Implement case register, investigation charter, lifecycle gates, tasks, assignments, and case activity history. | SRS-FR-CASE; F-CASE-001..005 |
| E3 | Source, Evidence & Document Intake | Implement source provenance, original evidence preservation, hashing, extracts, derivative lineage, ratings, claim and fact lifecycle, and document ingestion. | SRS-FR-EVD/DOC/CLM; F-EVD-001..006; F-EVD-008; F-DOC-001 *[v0.1.1 · A10]* |
| E4 | Entity Resolution & Relationship Model | Implement entity registry, aliases/identifiers, candidate matching, merge/unmerge, relationship, ownership/control, and asset registry. | SRS-FR-ENT/REL/AST; F-ENT-001..005; F-REL-001..003; F-AST-001 |
| E5 | Timeline & Follow-the-Value | Implement events, visual timeline, ValueFlow records, multi-leg chains, uncertainty classes, range/unknown values, and flow visualization. | SRS-FR-TIM/VAL; F-TIM-001..002; F-VAL-001..004 |
| E6 | Typology, Hypothesis & Assessment | Implement typology catalogue, indicators, typology worksheet, competing hypotheses, gaps, confidence, disconfirming-search record, and assessments. | SRS-FR-TYP/HYP/ASM (incl. SRS-FR-ASM-004); F-TYP-001..003; F-HYP-001..003; F-ASM-001..003 *[v0.1.1 · A05]* |
| E7 | Search & Investigation Graph | Implement permission-aware full-text/faceted search and evidence-backed graph visualization with canonical links. | SRS-FR-SCH/GRF; F-SCH-001..002; F-GRF-001 |
| E8 | Intelligence Product, Review & Dissemination | Implement report templates, evidence index, peer review, versioning/corrections, approvals, export/referral, and dissemination log. | SRS-FR-PRD/REV/DIS; F-PRD-001..003; F-REV-001; F-DIS-001..004 |
| E9 | Administration, Retention & Operational Readiness | Implement vocabularies, retention policies, backup/restore, configuration, minimum monitoring, security hardening, and release verification. | SRS-FR-ADM/SEC/AUD/OPS; F-ADM-001; F-ADM-003; F-OPS-001 |

# 3. Delivery Strategy and Increments

Increments, sequencing and any sizing derived from this backlog are planning targets, not measured estimates or commitments; no task estimates, velocity data or benchmarks exist yet. *[v0.1.1 · N06]*

The recommended sequence creates demonstrable end-to-end capabilities early. Increments are dependency-aware, but teams MAY overlap work where contracts are stable and integration tests remain authoritative.

| **Increment** | **Primary scope** | **Exit outcome** |
|----|----|----|
| I0 — Engineering Foundation | E0 + core E1 | Runnable secure skeleton; migrations, canonical DB, object storage, audit, OIDC baseline. |
| I1 — Governed Case Workspace | E1 + E2 | Authenticated team can create compartmentalized case, charter, gates, tasks and activity. |
| I2 — Evidence-to-Entity Chain | E3 + E4 partial | Team can register source, preserve evidence, cite extracts and build reviewable entities. |
| I3 — Investigation Model | E4 remainder + E5 | Relationships, assets, timeline and value-flow analysis become usable end-to-end. |
| I4 — Analytical Reasoning | E6 | Typology, hypotheses, gaps, assessment and confidence complete analytical chain. |
| I5 — Discovery & Graph | E7 | Search and graph improve navigation without becoming canonical truth. |
| I6 — Reviewed Intelligence Product | E8 | Assessment becomes reviewed/versioned intelligence product with controlled export. |
| I7 — Operational Release | E9 + regression | Retention, restore, hardening and full MVP release scenario verified. |

# 4. Dependency Model

Core dependency direction: E0 precedes all epics; E1 is required before sensitive data becomes multi-user; E2/E3 establish governed investigation context and evidence; E4/E5 create the financial investigation model; E6 creates analytical reasoning; E7 accelerates discovery; E8 creates controlled intelligence outputs; E9 closes operational release risk.

Critical path: E0 → E1 → E2 → E3 → E4 → E5 → E6 → E8 → E9. E7 can begin after E4 canonical relationships are stable.

# 5. Detailed Engineering Backlog

## E0 — Platform Foundation & Delivery

Establish the deployable application skeleton, environments, CI/CD, canonical database, evidence storage, audit substrate, and engineering conventions.

**Traceability:** SRS-OPS; SRS-DR; SRS-AUD; F-OPS-001; F-AUD-001

### ST-E0-01 — Repository and service skeleton

As an engineer, I need a reproducible project structure so all later capabilities share conventions.

**Engineering tasks**

- Create backend, frontend, worker and infrastructure directories

- Configure environment-based settings and secrets

- Define coding/lint/test conventions

- Add health endpoint and build metadata

**Acceptance tests / exit criteria**

- Fresh checkout can run locally from documented commands

- CI executes lint + unit tests

- No production secret is committed

### ST-E0-02 — Canonical PostgreSQL baseline

As a data steward, I need versioned canonical storage so analytical objects have a durable source of truth.

**Engineering tasks**

- Create database migration framework

- Implement common object envelope: UUID, timestamps, version, classification, created_by

- Add soft/superseded state conventions

- Create migration rollback/test strategy

**Acceptance tests / exit criteria**

- Migrations apply to empty database

- Schema version is queryable

- Canonical IDs remain stable across updates

### ST-E0-03 — Evidence object storage baseline

As an evidence custodian, I need originals stored separately from metadata.

**Engineering tasks**

- Configure S3-compatible or filesystem evidence store

- Use opaque object keys, not user filenames

- Store checksum and content metadata in DB

- Block in-place overwrite of originals

**Acceptance tests / exit criteria**

- Uploading same filename twice creates distinct evidence versions

- Original object cannot be modified by analyst role

### ST-E0-04 — Audit event substrate

As an auditor, I need material changes captured consistently.

**Engineering tasks**

- Define AuditEvent schema

- Create application audit helper/middleware

- Capture actor, action, object, before/after reference, timestamp, request correlation

- Protect audit records from ordinary modification

**Acceptance tests / exit criteria**

- Create/update/delete/merge/export actions produce events

- Analyst cannot alter audit history

## E1 — Identity, Access & Protected Sources

Implement OIDC/MFA integration, role/object access controls, case membership, classification, and protected-source compartment.

**Traceability:** SRS-SEC; F-SEC-001..003

### ST-E1-01 — OIDC login and session policy

As a user, I need organisational SSO so access can be centrally revoked.

**Engineering tasks**

- Implement OIDC authorization code flow (+ PKCE) with Django as confidential client of Keycloak, server-side session (BFF): `GET /auth/login`, `GET /auth/callback`, `POST /auth/logout`, `GET /auth/session` *[v0.1.1 · A11]*

- Browser holds only `__Host-csaml_session` cookie (HttpOnly, Secure, SameSite=Lax, Path=/); access/refresh/ID tokens stay server-side; no `Authorization: Bearer` from browser; CSRF token in `X-CSRFToken` on unsafe methods *[v0.1.1 · A11]*

- Map IdP subject to local user

- Enforce session timeout and logout (idle/absolute timeouts per security-policy configuration; back-channel logout revokes sessions where supported)

- Support MFA claim/policy checks

**Acceptance tests / exit criteria**

- Disabled IdP user cannot establish new session

- Session shows authenticated identity and roles

- No OIDC token is readable from browser JavaScript; unsafe request without valid CSRF token is rejected *[v0.1.1 · A11]*

### ST-E1-02 — Role and case membership authorization

As a case owner, I need need-to-know access so sensitive cases stay compartmentalised.

**Engineering tasks**

- Define roles: investigator, case_owner, reviewer, data_steward, evidence_custodian, admin, auditor

- Implement case membership ACL

- Apply authorization in API layer, not UI only

- Add classification checks

**Acceptance tests / exit criteria**

- Direct API request cannot bypass case membership

- Unauthorized object IDs return non-disclosing denial

### ST-E1-03 — Protected-source compartment

As a source handler, I need source identity separated from routine evidence.

**Engineering tasks**

- Create ProtectedSource model/store

- Separate identity from source-derived evidence reference

- Restrict handler role

- Redact identity from normal search/index/audit payloads

**Acceptance tests / exit criteria**

- Routine analyst can use source-derived evidence without source identity

- Protected identity never appears in normal export

## E2 — Case & Investigation Workflow

Implement case register, investigation charter, lifecycle gates, tasks, assignments, and case activity history.

**Traceability:** SRS-FR-CASE; F-CASE-001..005

### ST-E2-01 — Case register and creation

As an investigator, I need a stable case workspace.

**Engineering tasks**

- Create Case model/API/UI

- Required fields: title, purpose, owner, classification, status

- Generate stable case identifier

- Case list filters by status/owner/classification

**Acceptance tests / exit criteria**

- Case cannot activate without owner, purpose, question

- Case history records creation

### ST-E2-02 — Investigation Charter

As a case owner, I need scope and boundaries recorded before substantive work.

**Engineering tasks**

- Implement investigation question, scope included/excluded, jurisdictions, period, risks, authorised/prohibited collection

- Version charter

- Require reason for material scope change

**Acceptance tests / exit criteria**

- Old charter version remains retrievable

- Scope change produces audit event

### ST-E2-03 — Lifecycle gates G0-G6

As governance reviewer, I need high-risk actions controlled by gates.

**Engineering tasks**

- Model gates and gate requirements

- Gate submission/approval/rejection

- Prevent self-approval when policy requires independence

- Record conditions and unresolved gaps

**Acceptance tests / exit criteria**

- Controlled transition is blocked without approval

- Approval predates downstream action

### ST-E2-04 — Tasks and assignments

As an investigator, I need actionable work tracked.

**Engineering tasks**

- Task model with owner/status/due date/type

- Case task board/list

- Completion history

- Link tasks to sources/entities/hypotheses where relevant

**Acceptance tests / exit criteria**

- Task ownership and completion are visible

- Closed task retains historical state

### ST-E2-05 — Case activity timeline

As a reviewer, I need to reconstruct material case activity.

**Engineering tasks**

- Project relevant AuditEvents into case activity

- Filter by actor/action/object

- Link activity to canonical object

**Acceptance tests / exit criteria**

- Material case events appear chronologically

- Activity item opens the referenced object when authorized

## E3 — Source, Evidence & Document Intake

Implement source provenance, original evidence preservation, hashing, extracts, derivative lineage, ratings, claim and fact lifecycle, and document ingestion.

**Traceability:** SRS-FR-EVD/DOC/CLM; F-EVD-001..006; F-EVD-008; F-DOC-001 *[v0.1.1 · A10]*

### ST-E3-01 — Source register

As an investigator, I need material sources registered with provenance.

**Engineering tasks**

- Source model/API/UI

- Capture origin, publisher, URL/location, publication/access dates, access method, legal note

- Archive reference and reliability fields

**Acceptance tests / exit criteria**

- Assessment-linked source must contain provenance minimum

- Mutable web source can reference preserved copy

### ST-E3-02 — Original evidence ingestion

As a custodian, I need evidence originals preserved.

**Engineering tasks**

- Upload API with streaming size limits

- Virus/malware scanning hook

- Write immutable original

- Capture MIME/size/filename/acquired_at/collector

**Acceptance tests / exit criteria**

- Failed ingest never creates misleading completed record

- Original remains unchanged after analyst actions

### ST-E3-03 — Hash/integrity verification

As a reviewer, I need to verify evidence integrity.

**Engineering tasks**

- Compute SHA-256 at ingest

- Store algorithm/hash

- Add reverify action

- Flag mismatch

**Acceptance tests / exit criteria**

- Recomputed hash matches stored original in normal case

- Mismatch creates security/audit event

### ST-E3-04 — Evidence extracts and citations

As an analyst, I need precise excerpts linked to originals.

**Engineering tasks**

- EvidenceExtract object

- Support page/paragraph/region/location descriptor

- Preview parent context

- Link extract to claims as supporting evidence; facts are created only through the claim and fact lifecycle (ST-E3-07), never directly from an extract *[v0.1.1 · A10]*

**Acceptance tests / exit criteria**

- Extract cannot exist without parent evidence

- Citation opens exact parent location where supported

- Creating or linking an extract never creates a Fact *[v0.1.1 · A10]*

### ST-E3-05 — Derivative lineage

As an analyst, I need OCR/translation/processed copies distinguished from originals.

**Engineering tasks**

- Derivative model and parent link

- Transformation type/tool/version/time/creator

- Prevent derivative from replacing original

- Lineage UI

**Acceptance tests / exit criteria**

- Every derivative traces to original

- Original and derivative are visually distinct

### ST-E3-06 — Reliability and credibility ratings

As an analyst, I need source reliability separate from information credibility.

**Engineering tasks**

- Implement A-F source scale

- Implement 1-6 information credibility scale

- Require rationale for material ratings

- Allow reassessment history

**Acceptance tests / exit criteria**

- UI does not merge the two ratings

- Rating change is versioned/audited

### ST-E3-07 — Claim and fact lifecycle *[v0.1.1 · A10]*

As an analyst, I need what a source asserted kept separate from what the team has verified, so that facts are created only through reviewable decisions and corrections reach dependent analysis.

> Added in v0.1.1 (audit finding A10). Approved by product owner, 2026-10-08. A claim is never converted into a fact; a fact is a separate object supported by evidence (mandatory), optionally by claims, and by verification decisions. *[v0.1.1 · C02]*

**Engineering tasks**

- Claim model/API/UI: source-attributed assertion linked to source/person and evidence/extract refs; `claim_status` (`RECORDED`, `UNDER_REVIEW`, `CORROBORATED`, `CONTRADICTED`, `UNRESOLVED`); `disputed` boolean kept for compatibility and derived from status/open dispute

- VerificationDecision model: target_ref (claim or fact), decision, rationale, evidence_refs, decided_by, decided_at, optional review_ref; append-only

- Fact creation command: requires `supporting_evidence` (1..n) and `decision_rationale`; `supporting_claim_refs` optional; creates the Fact (`PROVISIONAL`) and its `CREATE` VerificationDecision atomically in one transaction; `verification_decision_refs` is server-populated; supporting claims are not modified *[v0.1.1 · A10]* *[v0.1.1 · C01]* *[v0.1.1 · C02]*

- Fact transitions: establish (Reviewer other than proposer), dispute (any authorized case member, with evidence), supersede (requires `superseded_by` replacement fact); each command writes its ESTABLISH/DISPUTE/SUPERSEDE decision atomically with the status change *[v0.1.1 · C01]*

- Dependency tracking: on DISPUTED/SUPERSEDED, flag dependent Assessments and IntelligenceProducts `review_required` with link to the triggering decision; create a correction review task for published products instead of mutating them

- Endpoints per API Specification v0.1.1 (claims, verification-decisions, facts, establish/dispute/supersede, dependents); audit events for every transition

**Acceptance tests / exit criteria**

- Analyst conclusion never overwrites claim content or attribution

- Fact creation without evidence refs or decision rationale is rejected (422); a successful creation returns the fact with its `CREATE` decision in `verification_decision_refs`, and no fact exists without that decision *[v0.1.1 · C01]* *[v0.1.1 · C02]*

- Proposer cannot establish own fact; independent reviewer can

- Verification decisions cannot be edited or deleted

- Pilot path: claim recorded → fact created (PROVISIONAL) supported by evidence and the claim → ESTABLISHED → DISPUTED → SUPERSEDED, each with its decision, preserving full history. Dependent flagging of assessments and products is verified as a regression in ST-E6-06 (Sprint 5) and ST-E8-04 (Sprint 7), when those objects exist *[v0.1.1 · C11]*

**Traceability:** SRS-FR-CLM-001..004; F-EVD-008

## E4 — Entity Resolution & Relationship Model

Implement entity registry, aliases/identifiers, candidate matching, merge/unmerge, relationship, ownership/control, and asset registry.

**Traceability:** SRS-FR-ENT/REL/AST; F-ENT-001..005; F-REL-001..003; F-AST-001

### ST-E4-01 — Entity registry

As an analyst, I need reusable entities outside case silos.

**Engineering tasks**

- Entity model by type

- Canonical name, aliases, identifiers, jurisdictions, status

- Case-to-entity association without duplicating entity

**Acceptance tests / exit criteria**

- Same canonical entity can appear in multiple authorized cases

- Entity record preserves provenance-bearing assertions

### ST-E4-02 — Aliases and identifiers

As an analyst, I need conflicting identifiers represented without destructive overwrite.

**Engineering tasks**

- Identifier records with type/value/source/status

- Alias records with source/time

- Uniqueness rules only where justified

**Acceptance tests / exit criteria**

- Conflicting values coexist with provenance

- No silent overwrite

### ST-E4-03 — Candidate entity matching

As an analyst, I need a reviewable duplicate-candidate screen.

**Engineering tasks**

- Candidate matching on normalized name + identifiers

- Display matching and conflicting attributes

- No auto-merge in MVP

- Record POSSIBLE_MATCH, KEEP_SEPARATE and DEFER outcomes as ResolutionDecision records; a KEEP_SEPARATE pair is not re-suggested unless new evidence is attached *[v0.1.1 · ER]*

**Acceptance tests / exit criteria**

- Candidate screen explains why pair was suggested

- Common name alone does not force merge

### ST-E4-04 — Merge and unmerge

As a data steward, I need reversible entity resolution.

**Engineering tasks**

- ResolutionDecision record (append-only; MERGE with surviving_entity_ref, UNMERGE with reverses_decision_ref; evidence, confidence, rationale, reviewer for high-impact decisions) per Data Model v0.1.1 §8.4 *[v0.1.1 · ER]*

- Derive entity resolution_status only from ResolutionDecisions (MERGE → MERGED/RESOLVED; UNMERGE → SPLIT) *[v0.1.1 · ER]*

- Preserve old IDs as aliases/superseded records

- Repoint relationships with history

- Implement unmerge recovery

- Merge, unmerge, `POST /resolution-decisions` and match-candidate decisions carry body `expected_versions` (no `If-Match`); merge/unmerge require `Idempotency-Key` (API Specification §10, §11, §14) *[v0.1.1 · C03]*

**Acceptance tests / exit criteria**

- Unmerge restores prior object topology

- Merge rationale/evidence is mandatory

- Every merge and unmerge produces a ResolutionDecision; a direct resolution_status change without a decision is rejected (SRS-FR-ENT-006) *[v0.1.1 · ER]*

- Missing or incomplete `expected_versions` → 428; a stale entry → 412 with `details.current_record_versions`; a retried merge with the same `Idempotency-Key` replays the original result *[v0.1.1 · C03]*

### ST-E4-05 — Relationships, ownership and control

As an analyst, I need first-class connections with evidence.

**Engineering tasks**

- Relationship model with type/endpoints/evidence/confidence/time

- OwnershipInterest with percentage nullable

- ControlAssertion distinguishes legal owner/beneficial owner/controller/user

**Acceptance tests / exit criteria**

- Graph edge always traces to relationship record

- Unknown percentage remains null, not zero

### ST-E4-06 — Asset registry

As an analyst, I need assets linked to ownership/control assertions.

**Engineering tasks**

- Asset model/types/identifiers/location

- Attribution relationship to person/org

- Evidence and status

**Acceptance tests / exit criteria**

- Asset attribution distinguishes ownership/control/use

- Material attribution requires evidence link

## E5 — Timeline & Follow-the-Value

Implement events, visual timeline, ValueFlow records, multi-leg chains, uncertainty classes, range/unknown values, and flow visualization.

**Traceability:** SRS-FR-TIM/VAL; F-TIM-001..002; F-VAL-001..004

### ST-E5-01 — Events and temporal precision

As an analyst, I need chronology with uncertainty.

**Engineering tasks**

- Event object with date precision

- Link entities/assets/evidence

- Support exact date, month, year, range, unknown

**Acceptance tests / exit criteria**

- Approximate date is not rendered as exact

- Event links to supporting evidence

### ST-E5-02 — Visual timeline

As an analyst, I need case chronology to reveal patterns.

**Engineering tasks**

- Timeline query/API

- Filters by entity/type/date

- Interactive UI and export representation

**Acceptance tests / exit criteria**

- Timeline respects object permissions

- Each item opens canonical event/evidence

### ST-E5-03 — ValueFlow canonical model

As an analyst, I need transfer of economic value represented without pretending all flows are transactions.

**Engineering tasks**

- ValueFlow fields origin/destination/mechanism/value/currency/date/evidence

- Mandatory flow_class enum

- Confidence/status

**Acceptance tests / exit criteria**

- Cannot save flow without class

- Unknown value allowed without zero substitution

### ST-E5-04 — Multi-leg flow builder

As an analyst, I need reconstructable chains.

**Engineering tasks**

- ValueFlowLeg model/order

- Builder UI

- Per-leg evidence/confidence/class

- Chain validation

**Acceptance tests / exit criteria**

- Each leg can carry different evidence/class

- Removing a leg does not destroy evidence objects

### ST-E5-05 — Flow visualisation

As a reviewer, I need direct vs reconstructed flows visually unmistakable.

**Engineering tasks**

- Distinct labels/line semantics for four classes

- Legend always visible

- Export keeps class labels

**Acceptance tests / exit criteria**

- Screenshot/export can distinguish all classes without color alone

- No derived flow shown as direct

## E6 — Typology, Hypothesis & Assessment

Implement typology catalogue, indicators, typology worksheet, competing hypotheses, gaps, confidence, and assessments.

**Traceability:** SRS-FR-TYP/HYP/ASM (incl. SRS-FR-ASM-004, ST-E6-06); F-TYP-001..003; F-HYP-001..003; F-ASM-001..003 *[v0.1.1 · C10]*

### ST-E6-01 — Typology catalogue browser

As an analyst, I need versioned CS-AML typologies in the workflow.

**Engineering tasks**

- Load catalogue data

- Browse/search typologies

- Display mechanism, observables, false positives, version

**Acceptance tests / exit criteria**

- Assessment records catalogue version used

- Typology content cannot silently mutate historical case

### ST-E6-02 — Indicator capture

As an analyst, I need evidence-linked indicators and counter-indicators.

**Engineering tasks**

- Indicator model with direction/type/significance

- Links to entities/events/flows/evidence

- Counter-indicator support

**Acceptance tests / exit criteria**

- Material indicator has evidence/proposition

- Indicator itself is not labelled proof

### ST-E6-03 — Typology match worksheet

As an analyst, I need structured comparison rather than automatic accusation.

**Engineering tasks**

- TypologyMatch object

- Observed indicators/counter-indicators

- Consistency level

- Alternative explanations

**Acceptance tests / exit criteria**

- Single weak indicator cannot produce strong level automatically

- Analyst rationale required

### ST-E6-04 — Competing hypotheses

As an analyst, I need multiple explanations tested.

**Engineering tasks**

- Hypothesis object/status

- Supporting/contradicting evidence links

- Alternative hypothesis set

- Assumptions

**Acceptance tests / exit criteria**

- At least two plausible hypotheses supported in pilot

- Rejected hypothesis remains in history

### ST-E6-05 — Intelligence gaps

As an analyst, I need unknowns explicit.

**Engineering tasks**

- Gap object/question/impact/priority/status

- Link to hypothesis/assessment

- Closure rationale

**Acceptance tests / exit criteria**

- Assessment can list unresolved gaps

- Gap cannot be silently deleted

### ST-E6-06 — Assessment and confidence

As an analyst, I need judgement with basis and uncertainty.

**Engineering tasks**

- Assessment versioning

- Judgement, confidence, rationale, assumptions, gaps, alternatives

- Confidence wire enum `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS` with mandatory rationale; `INSUFFICIENT_BASIS` never converted to LOW/null/zero; null only on drafts *[v0.1.1 · A09]*

- Evidence traversal

- Disconfirming-search record (what was searched, sources consulted, result, rationale) required before a high-impact/adverse assessment or product can pass review (SRS-FR-ASM-004) *[v0.1.1 · A05]*: `Assessment.disconfirming_searches[]` (Data Model §13.3) recorded through `POST /assessments/{assessmentId}/disconfirming-searches` (If-Match on the assessment); `POST /reviews/{reviewId}/approve` returns 409 STATE_CONFLICT with `details.reason = "DISCONFIRMATION_REQUIRED"` when the entry is missing *[v0.1.1 · C10]*

**Acceptance tests / exit criteria**

- Reviewer can trace assessment backward to evidence

- Confidence basis is mandatory for material assessment

- Review of a high-impact adverse assessment without a disconfirmation record is rejected; after the record is added, review can proceed (tested separately from backward traceability) *[v0.1.1 · A05]* — rejection happens at review approval (409, `DISCONFIRMATION_REQUIRED`), not at finalization *[v0.1.1 · C10]*

- Regression of ST-E3-07: disputing or superseding a supporting fact flags the dependent assessment `review_required` with `review_trigger_ref` *[v0.1.1 · C11]*

**Traceability:** SRS-FR-ASM-001..004; F-ASM-001..003; SRS-FR-CLM-004 (regression) *[v0.1.1 · C10]*

- Finalizing an assessment with a null confidence level is rejected; `INSUFFICIENT_BASIS` round-trips unchanged through DB/API/UI/export *[v0.1.1 · A09]*

## E7 — Search & Investigation Graph

Implement permission-aware full-text/faceted search and evidence-backed graph visualization with canonical links.

**Traceability:** SRS-FR-SCH/GRF; F-SCH-001..002; F-GRF-001

### ST-E7-01 — Permission-aware global search

As an analyst, I need to find authorized entities, cases and evidence.

**Engineering tasks**

- Search service/index or DB FTS

- Permission filtering before result display

- Filters by object type/case/date

**Acceptance tests / exit criteria**

- Unauthorized object never appears in count/snippet

- Search result links canonical object

### ST-E7-02 — Faceted case search

As an analyst, I need focused search within a case.

**Engineering tasks**

- Facets for source/entity/event/evidence/relationship

- Case scope enforcement

- Saved query not required in MVP

**Acceptance tests / exit criteria**

- Facets respect ACL and classification

- Query response time meets MVP NFR target

### ST-E7-03 — Investigation graph

As an analyst, I need visual entity/relationship/asset/value-flow exploration.

**Engineering tasks**

- Graph projection from canonical data

- Node/edge filtering

- Evidence/provenance side panel

- Save view state optionally

**Acceptance tests / exit criteria**

- Every material edge links to canonical relationship/evidence

- Projection can be rebuilt without data loss

## E8 — Intelligence Product, Review & Dissemination

Implement report templates, evidence index, peer review, versioning/corrections, approvals, export/referral, and dissemination log.

**Traceability:** SRS-FR-PRD/REV/DIS; F-PRD-001..003; F-REV-001; F-DIS-001..004

### ST-E8-01 — Intelligence product templates

As an analyst, I need consistent report outputs.

**Engineering tasks**

- Product model

- Templates (all six MVP P0 templates): Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report *[v0.1.1 · A06]*

- Template-specific section structure and canonical-object bindings for each of the six templates *[v0.1.1 · A06]*

- Auto-populate metadata/classification/evidence index references

**Acceptance tests / exit criteria**

- Draft is versioned

- Product shows author/reviewer/status

- Each of the six templates can be generated from canonical objects with version, classification, author/reviewer and evidence index (SRS-FR-PRD-001) *[v0.1.1 · A06]*

### ST-E8-02 — Evidence index generation

As a reviewer, I need claims traceable from report to evidence.

**Engineering tasks**

- Generate index from linked facts/assessments, following each fact through its verification decision(s) and source claims/evidence (facts exist only via the ST-E3-07 lifecycle) *[v0.1.1 · A10]*

- Include source/evidence IDs and citation locations

- Permission-aware inclusion

**Acceptance tests / exit criteria**

- Key fact in pilot has traversable evidence reference

- Restricted evidence is handled according to export policy

- Index shows fact status; a product that depends on a DISPUTED or SUPERSEDED fact is flagged `review_required` *[v0.1.1 · A10]*

### ST-E8-03 — Peer review workflow

As a reviewer, I need independent approval and change requests.

**Engineering tasks**

- Review states/commenting/request-changes/approve

- Prevent author self-approval where required

- Freeze reviewed version

**Acceptance tests / exit criteria**

- Approved version identifies independent reviewer

- Post-approval change creates new version

### ST-E8-04 — Corrections and supersession

As a case owner, I need prior products retained when corrected.

**Engineering tasks**

- Supersedes relationship

- Status current/superseded/retracted

- Correction note

**Acceptance tests / exit criteria**

- Old version remains auditable

- Recipient-facing export identifies current version

- Regression of ST-E3-07: disputing or superseding a fact flags dependent products `review_required`, leaves a published product unchanged and creates a correction review task *[v0.1.1 · C11]*

### ST-E8-05 — Dissemination approval and export

As a case owner, I need controlled external release.

**Engineering tasks**

- Dissemination object recipient/purpose/classification/approval

- Export minimization selector

- Generate package/report

**Acceptance tests / exit criteria**

- External export blocked before approval

- Export manifest lists included objects/version

### ST-E8-06 — Referral package and sharing log

As an investigator, I need structured referral plus immutable sharing record.

**Engineering tasks**

- Referral template sections

- Sharing log record recipient/time/version/restrictions

- Audit export event

**Acceptance tests / exit criteria**

- Referral separates fact/analysis/gaps

- Ordinary analyst cannot edit completed sharing log

## E9 — Administration, Retention & Operational Readiness

Implement vocabularies, retention policies, backup/restore, configuration, minimum monitoring, security hardening, and release verification.

**Traceability:** SRS-FR-ADM/SEC/AUD/OPS; F-ADM-001; F-ADM-003; F-OPS-001

### ST-E9-01 — Controlled vocabulary admin

As an admin, I need versioned vocabularies.

**Engineering tasks**

- Relationship/asset/status/classification vocabulary UI

- Version terms

- Disable without deleting historical semantics

**Acceptance tests / exit criteria**

- Historical record displays original term/version

- Vocabulary change audited

### ST-E9-02 — Retention policy engine

As a privacy/admin role, I need retention/disposition states.

**Engineering tasks**

- RetentionPolicy model

- Apply by classification/object type

- Preview eligible records

- Hold/exception support

**Acceptance tests / exit criteria**

- Disposition requires authorization

- Legal hold blocks deletion

### ST-E9-03 — Backup and restore

As an operator, I need recoverable canonical data and evidence.

**Engineering tasks**

- Automated DB backup

- Evidence store backup strategy

- Configuration backup

- Restore runbook and test

**Acceptance tests / exit criteria**

- Documented restore test succeeds

- Restored hashes/evidence references validate

### ST-E9-04 — Operational hardening

As an operator, I need production-safe defaults.

**Engineering tasks**

- Security headers/TLS/reverse proxy

- Secrets management

- Rate limits/upload limits

- Error handling without sensitive leakage

- Minimal health/metrics

**Acceptance tests / exit criteria**

- No debug mode in production

- Sensitive evidence content absent from routine logs

### ST-E9-05 — MVP end-to-end release test

As product owner, I need objective release evidence.

**Engineering tasks**

- Create representative pilot dataset

- Automate what can be automated

- Run two-analyst scenario

- Record failures and remediation

**Acceptance tests / exit criteria**

- All mandatory P0 SRS requirements pass or accepted exception exists; no exception is possible for a non-waivable invariant (authorization, source identity, evidence integrity/provenance, certainty promotion, approval bypass, audit history) — see Sprint & Milestone Plan v0.1.1 §7.2 *[v0.1.1 · A16]*

- Pilot completes case-to-approved-product with intact provenance/audit

# 6. Cross-Cutting Engineering Requirements

## 6.1 Authorization

- Every API read/write decision is evaluated server-side.

- Object-level classification and case membership are evaluated before data projection or export.

- Search/graph must not leak inaccessible object existence through counts, snippets, or topology.

## 6.2 Provenance and audit

- All canonical analytical objects expose stable IDs.

- Material mutations record actor/time/reason and relevant before/after references.

- Evidence extracts, derivatives, facts, indicators, hypotheses and assessments remain traversable backward to sources.

## 6.3 Data integrity

- Original evidence cannot be edited in place.

- Entity merge is reversible.

- ValueFlow class is mandatory and cannot be lost in export.

- Unknown numeric values remain unknown; null is not coerced to zero.

## 6.4 Testing

- Unit tests cover domain invariants.

- Integration tests cover database/storage/auth boundaries.

- Authorization tests use positive and negative cases.

- End-to-end test follows the Annex release scenario.

- Backup restore is a release test, not only an ops procedure.

# 7. Suggested Repository and Module Boundaries

The following structure is illustrative and SHOULD be adjusted to the selected stack without collapsing domain boundaries:

``` text
cs-aml/
  backend/
    apps/cases
    apps/evidence
    apps/entities
    apps/analysis
    apps/products
    apps/governance
    apps/audit
  frontend/
  worker/
  infra/
  tests/
    unit/
    integration/
    e2e/
    security/
  docs/
```

# 8. Engineering Definition of Ready

- Story has SRS/feature traceability.

- Data objects and authorization scope are known.

- Acceptance criteria are testable.

- Required upstream APIs/contracts are stable or mocked.

- Security/privacy impact is identified.

- Open design decision that could invalidate implementation is resolved or explicitly timeboxed.

# 9. Engineering Definition of Done

- Code reviewed and merged through protected branch workflow.

- Automated unit/integration tests pass.

- Negative authorization tests pass where applicable.

- Audit/provenance behavior is verified.

- Schema/API documentation updated.

- No critical/high unresolved security defect for the capability.

- Acceptance criteria demonstrated against representative data.

- Feature traceability status updated.

# 10. MVP Release Evidence Package

- SRS traceability matrix showing implementation and verification status.

- End-to-end two-analyst pilot record.

- Access-control and protected-source compartment test results.

- Evidence hash, original/derivative lineage and citation tests.

- Entity merge/unmerge recovery test.

- Value-flow class persistence across DB/API/UI/export.

- Hypothesis and assessment traceability test.

- Disconfirming-search enforcement test (separate from traceability test). *[v0.1.1 · A05]*

- Claim/fact lifecycle test (fact creation from supporting claims/evidence, independent establishment, dispute/supersede, dependent flagging). *[v0.1.1 · A10]*

- Independent peer-review and dissemination-approval test.

- Backup/restore test record.

- Known limitations and formally accepted exceptions.

# 11. Post-MVP Deferred Work

The following capabilities remain outside the mandatory MVP unless a release dependency is discovered: automated OCR pipelines, entity NLP extraction, OpenSanctions screening, OpenAleph connector, FollowTheMoney import/export, external graph database, advanced path/network analytics, GraphSense, Flowintel interoperability, AI summarisation/assistant, partner federation, multi-tenant hosting, advanced alerting and watch queries.

# Annex A — Epic Exit Checklist

| **Epic** | **Scope** | **Exit rule** |
|----|----|----|
| E0 | Platform Foundation & Delivery | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E1 | Identity, Access & Protected Sources | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E2 | Case & Investigation Workflow | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E3 | Source, Evidence & Document Intake | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E4 | Entity Resolution & Relationship Model | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E5 | Timeline & Follow-the-Value | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E6 | Typology, Hypothesis & Assessment | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E7 | Search & Investigation Graph | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E8 | Intelligence Product, Review & Dissemination | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |
| E9 | Administration, Retention & Operational Readiness | All stories accepted; traceability updated; domain integration test passes; no unresolved critical security/data-integrity defect. |

# Annex B — MVP End-to-End Acceptance Scenario

1\. Authenticate two analysts and one independent reviewer through configured identity provider.

2\. Create classified case, owner, investigation question and charter; complete required gate.

3\. Register a public source and ingest original PDF evidence; compute hash and create precise extract; record a source claim and create a PROVISIONAL fact supported by it through a verification decision; have an independent reviewer establish it. *[v0.1.1 · A10]*

4\. Create two entities and one organization; record aliases/identifiers; exercise candidate match and reviewed merge/unmerge on test records, each recorded as a ResolutionDecision. *[v0.1.1 · ER]*

5\. Create evidence-backed relationship, ownership/control assertion and an asset.

6\. Add events and render chronological timeline.

7\. Create DIRECT/DOCUMENTED and RECONSTRUCTED/HYPOTHETICAL value-flow examples and verify visual/export distinction.

8\. Map indicators to one typology, record counter-indicator, and create at least two competing hypotheses.

9\. Create intelligence gap and confidence-rated assessment linked backward to evidence.

10\. Use search and graph to retrieve only objects authorized to the case team.

11\. Generate intelligence product and evidence index; submit independent peer review; revise if required.

12\. Approve dissemination and create controlled export/referral package; verify sharing log and audit event.

13\. Attempt unauthorized access from non-member account and confirm non-disclosing denial.

14\. Run backup and restore test; verify evidence hashes and canonical references after restore.

# Annex C — Initial Engineering Decision Log

| **Decision** | **Topic** | **Guidance** | **Status** |
|----|----|----|----|
| ED-01 | Backend framework | Select implementation stack compatible with SRS and architecture; default reference profile may use Django/DRF. | Open until kickoff |
| ED-02 | Frontend | Select SPA/server-rendered approach; must support graph/timeline interactions and accessible forms. | Open until kickoff |
| ED-03 | Evidence storage | S3-compatible object store vs hardened filesystem. | Decide before E0-ST03 |
| ED-04 | Search | PostgreSQL FTS for MVP vs external OpenSearch. | Recommend PostgreSQL FTS for MVP unless scale requires otherwise |
| ED-05 | Graph | Relational/derived graph in MVP vs Neo4j/Memgraph. | Recommend derived relational/API graph for MVP; external graph post-MVP |
| ED-06 | IAM | OIDC provider and MFA policy. | Required before E1 |
| ED-07 | Deployment | Single-organisation deployment profile for MVP. | Recommended |

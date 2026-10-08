**CS-AML**

**Sprint & Milestone Plan v0.1.1**

Engineering Delivery Baseline for MVP 0.1

> **Document status — v0.1.1**  
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*  
> Supersedes: CS-AML Sprint & Milestone Plan v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.  
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.  
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.  
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).


> **Delivery axiom**  
> Deliver vertical, reviewable investigation capabilities. Sprint completion is not measured by isolated component output if the end-to-end analytical chain remains broken.

| **Field** | **Baseline** |
|:---|:---|
| Status | Draft for Review (Proposed Internal Baseline) — planning baseline for MVP 0.1 *[v0.1.1 · A01]* |
| Planning cadence | 2-week sprint baseline; capacity-adjustable (planning assumption, not a measured velocity or commitment) *[v0.1.1 · N06]* |
| Primary objective | Reach a releasable two-analyst end-to-end investigation workflow |
| Source documents | PRD v0.1.1; SRS v0.1.1; MVP Engineering Breakdown v0.1.1; Technical Stack & Repository Specification v0.1.1 (Markdown, `Documents/*_v0.1.1.md`) |

# 1. Purpose and Planning Principles

This plan converts the MVP engineering breakdown (draft for review) *[v0.1.1 · A01]* into an executable sprint and milestone sequence. It defines delivery order, dependencies, parallel work, exit criteria, review checkpoints, release evidence, and decision gates. It does not replace the SRS or backlog; it governs how those requirements are delivered and verified.

## 1.1 Planning principles

- Vertical slice over layer completion: each sprint SHOULD produce an analyst-visible capability where feasible.

- Security, authorization, provenance, and audit are built into each slice; they are not deferred to a hardening sprint.

- Canonical data and evidence integrity take precedence over derived search/graph convenience.

- Every sprint MUST preserve traceability from SRS requirement to story/task/test evidence.

- A milestone is accepted only when its exit criteria pass, not when its tickets are merely closed.

- Unresolved high-severity security or data-integrity defects block promotion to the next release milestone. Defects against a non-waivable invariant (authorization, source identity, evidence integrity/provenance, certainty promotion, approval bypass, audit history — see §7.2) can never be waived; the only release path is to disable the affected feature path with tested evidence of non-reachability. Other High defects may be waived only by the accountable authority with a tested compensating control, owner, and expiry date. *[v0.1.1 · A16]*

- Sprint dates are planning aids; dependency order and release gates are normative for this baseline.

## 1.2 Assumed team shape

This baseline assumes a small product engineering team. Team shape, indicative capacity and the two-week cadence are planning assumptions, not measured velocity; sprint dates and durations are targets until task estimates and actual velocity exist. *[v0.1.1 · N06]* The sequence remains valid for a smaller or larger team, but parallelization should be adjusted.

| **Role** | **Indicative Capacity** | **Primary Responsibilities** |
|:---|:---|:---|
| Tech Lead / Backend | 1 | Architecture, domain model, security-sensitive backend, code review |
| Backend Engineer | 1-2 | Django modules, API, audit, async jobs, tests |
| Frontend Engineer | 1 | React analyst workspace, graph/timeline/value-flow UX |
| QA / Security-minded Engineer | 0.5-1 | Acceptance tests, negative authorization tests, release evidence |
| Product / Domain Lead | 0.5 | Acceptance, typology/methodology fidelity, pilot scenario |
| Ops / Platform | 0.25-0.5 | CI/CD, deployment, backup/restore, observability |

# 2. Delivery Cadence and Milestone Model

The baseline uses Sprint 0 followed by eight two-week delivery sprints. Each sprint closes one delivery increment or a coherent portion of it. Milestones M0-M4 provide broader product checkpoints.

| **Milestone** | **Target State** | **Covered Sprints** | **Exit Meaning** |
|:---|:---|:---|:---|
| M0 — Foundation Ready | Secure deployable skeleton | Sprint 0 | Team can develop against stable repo, CI, DB, evidence storage, audit and OIDC baseline. |
| M1 — Governed Case Workspace | Case + access + evidence intake usable | Sprints 1-2 | Team can open a compartmentalized case and preserve evidence with provenance. |
| M2 — Investigation Core | Entity/relationship/timeline/value-flow chain usable | Sprints 3-4 | Team can model subjects, assets, chronology and value movement with uncertainty preserved. |
| M3 — Analytical Intelligence | Typology/hypothesis/assessment + search/graph usable | Sprints 5-6 | Team can reason, test competing explanations, and navigate the investigation coherently. |
| M4 — MVP Release Candidate | Reviewed intelligence product + operational readiness | Sprints 7-8 | Full case-to-approved-product pilot passes release gate with restore, authorization and audit evidence. |

# 3. Sprint Overview

| **Sprint** | **Theme** | **Epic Scope** | **Primary Deliverable** | **Milestone** |
|:---|:---|:---|:---|:---|
| Sprint 0 | Engineering Foundation | E0 + E1 bootstrap | Repo, CI/CD, PostgreSQL, evidence store, audit substrate, OIDC skeleton | M0 |
| Sprint 1 | Identity + Governed Case Workspace | E1 + E2 partial | RBAC/case membership, protected source, case register, charter, basic activity |  |
| Sprint 2 | Workflow + Evidence Intake | E2 remainder + E3 | Gates/tasks, source register, immutable evidence, hash, extracts, lineage, claim and fact lifecycle *[v0.1.1 · A10]* | M1 |
| Sprint 3 | Entities + Relationships | E4 | Entity registry, identifiers, matching, merge/unmerge, relationships, ownership/control, assets |  |
| Sprint 4 | Timeline + Follow-the-Value | E5 | Events/timeline, ValueFlow, multi-leg chains, uncertainty classes, flow visualization | M2 |
| Sprint 5 | Typology + Hypothesis + Assessment | E6 | Indicators, typology worksheet, competing hypotheses, gaps, confidence assessment |  |
| Sprint 6 | Search + Investigation Graph | E7 | Permission-aware search, facets, graph projection, provenance side panel | M3 |
| Sprint 7 | Intelligence Product + Review + Dissemination | E8 | Products (six templates *[v0.1.1 · A06]*), evidence index, peer review, corrections, approvals, export/referral, sharing log |  |
| Sprint 8 | Operational Release | E9 + full regression | Retention, backup/restore, hardening, E2E pilot, release evidence and remediation | M4 |

# 4. Dependency and Critical Path

The following chain represents the minimum critical path for MVP. Parallel work may occur around it, but breaking this sequence creates rework or weakens verification.

> **Critical path**  
> Foundation → Authorization → Case → Evidence → Entity/Relationship → Timeline/ValueFlow → Typology/Hypothesis/Assessment → Product/Review/Dissemination → Operational Release

| **Dependency** | **Why It Exists** | **Can Parallelize?** |
|:---|:---|:---|
| E0 → all | Shared repository, migrations, storage, audit and deployment baseline. | Only design/UX spikes may precede completion. |
| E1 → E2/E3/E7/E8 | Object access and compartmentalization must exist before sensitive case data. | E1 backend and E2 UI scaffolding may overlap. |
| E2 → E8 | Review/dissemination depends on case owner, status and lifecycle governance. | Product templates can be designed earlier. |
| E3 → E4/E6/E8 | Entities, analysis and products need evidence/provenance. | Schema work can overlap; production use cannot. |
| E4 → E5/E7 | Timeline/value-flow/graph require canonical entities and relationships. | Graph UI prototype may use fixtures. |
| E5 → E6 | Typology and hypotheses rely on structured events/flows. | Catalogue browser can be built early. |
| E6 → E8 | Products should contain reviewed assessments, alternatives, gaps and confidence. | Template engine may start early. |
| E8 → M4 | Release objective is reviewed, approved intelligence product. | Ops work proceeds continuously. |

# 5. Sprint-by-Sprint Delivery Plan

## 5.1 Sprint 0

**Sprint goal:** Create a reproducible, secure engineering foundation that all later vertical slices can depend on.

### Committed scope

- ST-E0-01 Repository and service skeleton

- ST-E0-02 Canonical PostgreSQL baseline

- ST-E0-03 Evidence object storage baseline

- ST-E0-04 Audit event substrate

- ST-E1-01 OIDC login and session policy (bootstrap)

### Parallel work

- Frontend shell and design tokens

- Initial database/domain migration conventions

- CI lint/unit/security scan wiring

### Sprint exit criteria

- Fresh checkout runs locally with documented command

- CI passes lint + unit tests

- DB migrations apply to empty database

- Evidence original cannot be overwritten by analyst path

- Material create/update action produces immutable audit event

- OIDC development login path works

### Required sprint evidence

- CI run link/log

- Migration test result

- Evidence overwrite negative test

- Audit event sample

- Environment/bootstrap documentation

## 5.2 Sprint 1

**Sprint goal:** Establish governed access and the first usable case workspace.

### Committed scope

- ST-E1-01 OIDC login and session policy (complete)

- ST-E1-02 Role and case membership authorization

- ST-E1-03 Protected-source compartment

- ST-E2-01 Case register and creation

- ST-E2-02 Investigation Charter

- ST-E2-05 Case activity timeline (initial)

### Parallel work

- Frontend case shell

- Authorization test matrix

- Protected-source UX and redaction design

### Sprint exit criteria

- Unauthorized case access fails in API, not only UI

- Protected source identity hidden from routine analyst

- Case cannot activate without owner/purpose/question

- Charter versioning works

- Case creation/scope change appear in activity

### Required sprint evidence

- Negative authorization tests

- Protected-source compartment test

- Case activation validation test

- Charter version/audit test

## 5.3 Sprint 2

**Sprint goal:** Complete case governance and establish evidence-to-citation chain.

### Committed scope

- ST-E2-03 Lifecycle gates G0-G6

- ST-E2-04 Tasks and assignments

- ST-E3-01 Source register

- ST-E3-02 Original evidence ingestion

- ST-E3-03 Hash/integrity verification

- ST-E3-04 Evidence extracts and citations

- ST-E3-05 Derivative lineage

- ST-E3-06 Reliability and credibility ratings

- ST-E3-07 Claim and fact lifecycle (proposed in v0.1.1; requires product-owner approval) *[v0.1.1 · A10]*

### Parallel work

- Upload/preview UI

- Evidence metadata forms

- Gate policy configuration

### Sprint exit criteria

- Controlled case transition blocked without required gate

- Source provenance minimum enforced

- Evidence original preserved and hashed

- Extract traces to parent evidence location

- Derivative traces to original

- Source reliability and information credibility are separate

- A fact can be created only from claim/evidence refs with a recorded verification decision; establishing it requires an independent reviewer *[v0.1.1 · A10]*

### Required sprint evidence

- Gate negative test

- Evidence hash re-verification

- Lineage test

- Source rating test

- Claim/fact lifecycle test (promotion, establish, dispute/supersede, dependent flagging) *[v0.1.1 · A10]*

- M1 review demonstration

## 5.4 Sprint 3

**Sprint goal:** Build reusable identity, relationship, ownership/control and asset model.

### Committed scope

- ST-E4-01 Entity registry

- ST-E4-02 Aliases and identifiers

- ST-E4-03 Candidate entity matching

- ST-E4-04 Merge and unmerge

- ST-E4-05 Relationships, ownership and control

- ST-E4-06 Asset registry

### Parallel work

- Entity search UX

- Matching normalization rules

- Relationship vocabulary seed

### Sprint exit criteria

- Same entity can be reused across authorized cases

- Conflicting identifiers coexist with provenance

- Candidate match explains similarities/conflicts

- Merge is evidence-backed and reversible

- Relationship edge traces to evidence

- Ownership/control/use remain separate

### Required sprint evidence

- Merge/unmerge regression

- Duplicate-name false merge test

- Relationship provenance test

- Asset attribution test

## 5.5 Sprint 4

**Sprint goal:** Make chronology and follow-the-value analysis operational.

### Committed scope

- ST-E5-01 Events and temporal precision

- ST-E5-02 Visual timeline

- ST-E5-03 ValueFlow canonical model

- ST-E5-04 Multi-leg flow builder

- ST-E5-05 Flow visualisation

### Parallel work

- Timeline UI

- Flow builder UX

- Export visual semantics

### Sprint exit criteria

- Approximate dates remain approximate

- Timeline respects object permissions

- Every flow has one of four mandatory classes

- Unknown value is not converted to zero

- Multi-leg chain preserves per-leg evidence

- Flow class remains visible in screenshot/export without color alone

### Required sprint evidence

- Temporal precision tests

- Flow class validation

- Multi-leg lineage test

- M2 investigation demonstration

## 5.6 Sprint 5

**Sprint goal:** Complete the analytical reasoning chain from indicator to confidence-rated assessment.

### Committed scope

- ST-E6-01 Typology catalogue browser

- ST-E6-02 Indicator capture

- ST-E6-03 Typology match worksheet

- ST-E6-04 Competing hypotheses

- ST-E6-05 Intelligence gaps

- ST-E6-06 Assessment and confidence

### Parallel work

- Catalogue import/versioning

- Hypothesis matrix UX

- Assessment editor

### Sprint exit criteria

- Catalogue version recorded in case analysis

- Indicators link to evidence and do not equal proof

- Typology match requires analyst rationale

- Pilot supports at least two plausible hypotheses

- Gaps remain explicit

- Assessment traces backward to evidence with confidence basis

### Required sprint evidence

- Typology version test

- Hypothesis support/contradiction test

- Assessment provenance traversal

- Confidence validation

## 5.7 Sprint 6

**Sprint goal:** Add permission-aware discovery and graph exploration without creating a second source of truth.

### Committed scope

- ST-E7-01 Permission-aware global search

- ST-E7-02 Faceted case search

- ST-E7-03 Investigation graph

### Parallel work

- Search indexing tuning

- Graph layout/filters

- Authorization leakage testing

### Sprint exit criteria

- Unauthorized objects never appear in result counts/snippets

- Search result opens canonical object

- Graph edge opens canonical relationship and evidence

- Graph/search projection can be rebuilt

- Graph does not promote inferred edge to verified relationship

### Required sprint evidence

- Search leakage test

- Graph provenance test

- Projection rebuild test

- M3 analyst workflow demonstration

## 5.8 Sprint 7

**Sprint goal:** Turn assessments into independently reviewed, versioned and controlled intelligence products.

### Committed scope

- ST-E8-01 Intelligence product templates (six: Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report) *[v0.1.1 · A06]*

- ST-E8-02 Evidence index generation

- ST-E8-03 Peer review workflow

- ST-E8-04 Corrections and supersession

- ST-E8-05 Dissemination approval and export

- ST-E8-06 Referral package and sharing log

### Parallel work

- Report rendering/export

- Review UX

- Export minimization/redaction rules

### Sprint exit criteria

- Product has author/reviewer/classification/version

- All six MVP templates generate from canonical objects with evidence index *[v0.1.1 · A06]*

- Key findings have evidence index

- Independent review enforced where required

- Post-approval change creates new version

- External export blocked before approval

- Sharing log immutable to ordinary analyst

### Required sprint evidence

- Peer-review separation test

- Evidence index trace test

- Export approval negative test

- Version supersession test

- Referral package sample

- One generated sample per template (six) *[v0.1.1 · A06]*

## 5.9 Sprint 8

**Sprint goal:** Reach operational release readiness and prove MVP end-to-end.

### Committed scope

- ST-E9-01 Controlled vocabulary admin

- ST-E9-02 Retention policy engine

- ST-E9-03 Backup and restore

- ST-E9-04 Operational hardening

- ST-E9-05 MVP end-to-end release test

### Parallel work

- Security regression

- Runbook completion

- Pilot data preparation

- Known limitations review

### Sprint exit criteria

- Retention preview/hold works

- Backup/restore succeeds with hash validation

- Production hardening baseline passes

- Full two-analyst pilot completes case-to-approved-product

- Mandatory P0 SRS passes or has explicitly accepted exception

- No open critical/high release-blocking defect

### Required sprint evidence

- Restore test record

- Security regression report

- SRS traceability matrix

- Two-analyst pilot record

- Known limitations/accepted exceptions

- M4 release sign-off

# 6. Milestone Acceptance Reviews

| **Milestone** | **Review Participants** | **Mandatory Demonstration** | **Decision** |
|:---|:---|:---|:---|
| M0 | Tech Lead, Ops, QA | Clean checkout → local run → CI → migration → evidence upload → audit → login | Proceed / remediate foundation |
| M1 | Product, Domain Lead, Security/QA | Create restricted case → charter → gate/task → source → evidence → extract/lineage | Proceed / narrow scope / remediate governance |
| M2 | Product, Analysts, QA | Evidence → entities → relationships/assets → timeline → multi-leg value flow | Proceed / correct domain model |
| M3 | Product, Analysts, Reviewer | Typology → competing hypotheses → gaps → assessment → search/graph traversal | Proceed / correct analytical UX |
| M4 | Product Owner, Reviewer, Security/Ops, QA | Full two-analyst case → approved intelligence product → controlled export → restore verification | Release / conditional release / no release |

# 7. Quality and Release Gates

## 7.1 Continuous gates in every sprint

- Unit and integration tests for new domain behavior.

- Negative authorization tests for new protected objects/endpoints.

- Audit event verification for material state changes.

- Migration forward test against clean and prior schema baseline.

- No sensitive evidence content in routine logs, traces, or error responses.

- Acceptance criteria demonstrated using realistic fixtures, not only mocked objects.

- Updated traceability from SRS/feature ID to implementation and test evidence.

## 7.2 Release-blocking defect classes

| **Severity** | **Examples** | **Release Treatment** |
|:---|:---|:---|
| Critical — non-waivable invariant | (1) Unauthorized access / authorization bypass; (2) source identity exposure; (3) evidence corruption or loss of provenance/integrity for material records, including unrecoverable DB/evidence mismatch; (4) certainty promotion — e.g. RECONSTRUCTED/HYPOTHETICAL shown or stored as DIRECT/DOCUMENTED (direct/reconstructed flow confusion), INSUFFICIENT_BASIS shown as a level, claim treated as fact without a decision; (5) approval bypass, including export without approval; (6) broken, missing, or editable audit history | Immediate block. No administrative waiver is possible. The only release path is to disable the affected feature path with tested evidence of non-reachability (the feature then ships disabled); the defect itself is never waived. *[v0.1.1 · A16]* |
| High | Incorrect merge/unmerge where unmerge restores prior state and audit history is intact; other high-severity defects that do not violate a non-waivable invariant | Block M4 until fixed, or waived only by the accountable authority with a tested compensating control, a named owner, and an expiry date recorded in the milestone decision record. *[v0.1.1 · A16]* |
| Medium | Workflow defect with safe workaround; non-critical UI/accessibility issue | May release with documented limitation and owner/date |
| Low | Cosmetic or minor usability issue | Backlog; does not block release |

# 8. Sprint Ceremonies and Decision Rhythm

| **Cadence** | **Purpose** | **Required Output** |
|:---|:---|:---|
| Sprint Planning | Confirm committed stories against capacity/dependencies | Sprint goal, committed scope, risks |
| Daily / async check-in | Surface blockers and security/data-integrity concerns early | Blocker log / owner |
| Mid-sprint technical review | Validate architecture/domain decisions before they harden | ADR or implementation adjustment |
| Sprint Review | Demonstrate analyst-visible vertical capability | Acceptance evidence + stakeholder notes |
| Sprint Retrospective | Improve delivery process | 1-3 concrete process actions |
| Milestone Review | Decide whether next dependency layer is safe to start | Go / conditional go / no-go record |

# 9. Epic-to-Sprint Traceability

| **Epic** | **Primary Sprint(s)** | **Milestone** | **Key Release Evidence** |
|:---|:---|:---|:---|
| E0 Foundation | 0 | M0 | CI, migrations, storage, audit, environment bootstrap |
| E1 Identity/Access | 0-1 | M0/M1 | OIDC, ACL negative tests, protected-source test |
| E2 Case Workflow | 1-2 | M1 | Case/charter/gates/tasks/activity demonstration |
| E3 Evidence Intake | 2 | M1 | Hash, provenance, extract, lineage evidence; claim/fact lifecycle test *[v0.1.1 · A10]* |
| E4 Entity/Relationship | 3 | M2 | Merge/unmerge, relationship provenance, asset attribution |
| E5 Timeline/ValueFlow | 4 | M2 | Temporal precision, four-class flow export |
| E6 Analytical Reasoning | 5 | M3 | Hypothesis matrix, typology version, assessment trace |
| E7 Search/Graph | 6 | M3 | Leakage test, graph provenance, rebuild test |
| E8 Products/Review/Dissemination | 7 | M4 | Six-template generation, review separation, evidence index, approved export, sharing log *[v0.1.1 · A06]* |
| E9 Operations/Release | 8 | M4 | Retention, restore, hardening, full pilot and traceability matrix |

# 10. Capacity Adjustment and Scope Change Rules

If actual team capacity differs from the baseline, preserve dependency order and milestone exit criteria. Adjust sprint count rather than compressing critical security, evidence, review, or restore work.

- If capacity is lower: split a sprint by vertical outcome; do not split security from the feature it protects.

- If capacity is higher: parallelize frontend/backend/test work inside the same epic or begin non-dependent next-sprint scaffolding.

- P1/P2 features SHALL NOT enter MVP sprints if they jeopardize P0 exit criteria.

- A new requirement affecting canonical data, authorization, provenance, value-flow semantics, or dissemination requires impact review against SRS and architecture.

- Any scope cut from P0 requires explicit product-owner acceptance and must appear in Known Limitations / Accepted Exceptions.

# 11. MVP Release Evidence Package

- SRS traceability matrix with implementation status and linked test evidence.

- Two-analyst end-to-end pilot record from case creation to approved intelligence product.

- Role/object-level authorization test results, including negative tests.

- Protected-source compartment verification.

- Evidence hash and derivative-lineage verification.

- Entity merge/unmerge test record.

- Value-flow class persistence test across DB/API/UI/export.

- Typology/hypothesis/assessment provenance demonstration.

- Peer-review separation and dissemination-approval test.

- Backup/restore test with evidence hash validation.

- Known limitations and formally accepted exceptions (none may cover a non-waivable invariant; each High waiver lists compensating control test, owner and expiry; each disabled feature path lists non-reachability test evidence). *[v0.1.1 · A16]*

- Release sign-off and version/build identifiers.

# 12. Canonical End-to-End Release Scenario

1.  Analyst A authenticates through OIDC and creates a restricted case with an investigation question and charter.

2.  Case owner assigns Analyst B as reviewer but not author and records lifecycle gate requirements.

3.  Analyst A registers two sources, uploads evidence, verifies hashes, creates extracts, and records source reliability / information credibility separately; records a source claim and proposes a PROVISIONAL fact that an independent reviewer establishes. *[v0.1.1 · A10]*

4.  Analyst A creates entities and identifiers, reviews a duplicate candidate, performs an evidence-backed merge, and verifies unmerge reversibility.

5.  Analyst A records ownership/control relationships and an asset, each linked to evidence.

6.  Analyst A creates events and a timeline, then builds a multi-leg value flow containing at least one documented and one reconstructed leg.

7.  Analyst A maps indicators and counter-indicators to a versioned typology and records at least two plausible competing hypotheses.

8.  Analyst A records unresolved intelligence gaps and writes a confidence-rated assessment traceable back to evidence.

9.  Analyst A uses permission-aware search/graph to navigate the case; no unauthorized object is exposed.

10. Analyst A generates an intelligence product and evidence index. Analyst B independently reviews and requests one change before approval.

11. After approval, the case owner creates a dissemination record and exports a minimized referral package. The sharing log records recipient, version, purpose and restrictions.

12. Operations restores the release candidate dataset from backup and verifies evidence hashes and key canonical object links.

> **Release decision rule**  
> MVP 0.1 is releasable only when this scenario passes end-to-end, mandatory P0 SRS requirements are verified, and no unresolved Critical or release-blocking High defect remains.

# 13. Post-MVP Planning Boundary

The following items remain outside MVP 0.1 unless promoted through formal scope change: dedicated OpenSearch; Neo4j/Memgraph; OCR/entity extraction automation; OpenAleph/OpenSanctions/GraphSense integrations; AI assistant; federation/partner workspace; advanced beneficial-ownership calculations; network metrics; Kubernetes; microservices; event bus. Their planning begins only after M4 evidence is reviewed and operational pain points justify the added complexity.

# Annex A — Sprint Planning Checklist

- Sprint goal maps to one analyst-visible outcome.

- All committed stories satisfy Definition of Ready.

- Dependencies from prior sprint are accepted, not merely coded.

- Security/privacy/provenance tests are included in estimates.

- Acceptance dataset/fixtures are available.

- Traceability IDs are attached to stories/tasks/tests.

- Release evidence owner is assigned.

- Known risks and fallback plan are visible.

# Annex B — Sprint Review Checklist

- Demonstrate capability using realistic investigation fixtures.

- Show at least one negative authorization or misuse test.

- Show provenance/audit path for newly created material records.

- Review open defects by severity.

- Confirm milestone exit criteria if applicable.

- Record stakeholder acceptance or remediation actions.

# Annex C — Milestone Decision Record Template

| **Field**             | **Record**                  |
|:----------------------|:----------------------------|
| Milestone             |                             |
| Date                  |                             |
| Build/version         |                             |
| Participants          |                             |
| Exit criteria result  |                             |
| Critical/high defects |                             |
| Accepted exceptions   |                             |
| Non-waivable invariant check (none open, or affected path disabled with non-reachability evidence) *[v0.1.1 · A16]* | |
| High waivers: compensating control test, owner, expiry *[v0.1.1 · A16]* | |
| Decision              | GO / CONDITIONAL GO / NO-GO |
| Required remediation  |                             |
| Approver              |                             |

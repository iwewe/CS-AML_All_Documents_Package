**CS-AML**

**Software Requirements Specification (SRS)**

Version 0.1.1

> **Document status — v0.1.1**  
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*  
> Supersedes: CS-AML Software Requirements Specification (SRS) v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.  
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.  
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.  
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Document status**  
> Proposed normative software baseline for MVP 0.1 implementation (draft for review). This SRS translates the PRD (draft for review), Product & Feature Specification, Data Model Specification, Control Implementation Guide, Investigation Methodology, and Technology Architecture into testable software requirements. *[v0.1.1 · A01]*

*Civil Society Financial Intelligence / AML Investigation Platform*

# Document Control

| **Document** | CS-AML Software Requirements Specification |
|----|----|
| **Version** | 0.1.1 |
| **Status** | Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]* |
| **Primary product scope** | MVP 0.1 |
| **Audience** | Product, engineering, QA, security, data, reviewers, governance |
| **Upstream documents** | CS-AML PRD v0.1.1; Product & Feature Specification v0.1.1; Data Model Specification v0.1.1; Technology Architecture v0.1.1; Control Implementation Guide v0.1.1; Investigation Methodology v0.1.1 (Markdown, `Documents/*_v0.1.1.md`) |
| **Normative terms** | SHALL / MUST = mandatory; SHOULD = recommended; MAY = optional |

# Contents

1\. Purpose and Scope

2\. Product and System Context

3\. Definitions and Conventions

4\. System Boundary and Actors

5\. Architectural Constraints

6\. Functional Requirements

7\. Data Requirements

8\. External Interface Requirements

9\. Security and Privacy Requirements

10\. Audit and Provenance Requirements

11\. Performance and Scalability

12\. Reliability, Backup and Disaster Recovery

13\. Search, Graph and Analytical Requirements

14\. AI and Automation Requirements

15\. UX and Accessibility Requirements

16\. Administration and Configuration

17\. Interoperability and Integration

18\. Deployment and Operations

19\. Verification and Acceptance

20\. Traceability Matrix

21\. MVP Release Baseline

Annex A — Requirement ID Taxonomy

Annex B — State Models

Annex C — API Resource Baseline

Annex D — Test Scenario Baseline

# 1. Purpose and Scope

This SRS specifies the software behaviour, data obligations, interfaces, controls, quality attributes, and verification conditions required to implement CS-AML MVP 0.1 as a secure system of record for civil-society financial-intelligence investigations.

> **Primary acceptance objective**  
> A small two-analyst team SHALL be able to open a sensitive case, ingest and preserve evidence, resolve entities, map relationships/assets/events/value flows, test competing hypotheses, assess typology consistency and confidence, complete independent review, and export an approved intelligence product while retaining provenance and audit history.

## 1.1 In scope

- Case and workflow management

- Source/evidence/provenance management

- Document ingestion

- Entity registry and reversible entity resolution

- Relationships, ownership, control, and assets

- Events and timeline

- Value-flow modelling

- Typology and indicator analysis

- Hypothesis, gap, confidence, and assessment management

- Search and graph exploration

- Intelligence products, review, dissemination and sharing logs

- IAM, protected-source compartment, audit, retention, backup and restore

## 1.2 Out of scope for MVP 0.1

- Automated AML transaction monitoring against banking core systems

- Autonomous guilt determination or law-enforcement decisioning

- Continuous web-scale scraping

- Cross-organisation federation

- Advanced blockchain tracing

- Automated sanctions/PEP screening as a mandatory workflow

- Advanced machine-learning risk scoring

- Multi-tenant SaaS operation

# 2. Product and System Context

CS-AML is positioned as a civil-society financial-intelligence and investigation platform, not a bank compliance engine. The software converts structured investigative work into reproducible intelligence while preserving uncertainty and provenance.

## 2.1 Product axiom

> **Axiom**  
> Technology SHALL preserve analytical uncertainty rather than erase it. Source, evidence, claim, fact, indicator, hypothesis, assessment, and intelligence product remain distinguishable in storage, APIs, UI, graph views, automation, and exports.

## 2.2 Upstream analytical chain

``` text
SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

## 2.3 Mandatory value-flow classes

``` text
DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL
```

These are the `flow_class` wire values. All controlled enumerations on the wire (database values, API payloads, exports) use UPPER_SNAKE_CASE and derive from the Data Model Specification v0.1.1 Annex A registry; display labels are separate and translatable. *[v0.1.1 · A09]*

# 3. Definitions and Conventions

| **Term** | **Meaning** | **Software implication** |
|----|----|----|
| Canonical object | Authoritative record of investigative state | Must be durable, versioned where material, access-controlled, and auditable |
| Derived projection | Rebuildable search/graph/cache/AI representation | Must never become sole source of truth |
| Material action | Action capable of changing analytical meaning, access, review status, or dissemination | Must be auditable |
| Protected source | Human/source identity requiring compartmentalisation | Identity access separate from routine evidence access |
| High-impact product | Product containing potentially harmful adverse findings or public attribution | Requires independent review and dissemination approval |
| MVP | Minimum release satisfying end-to-end case completion | All P0 requirements required unless explicitly waived; a defect against a non-waivable invariant (§21) can never be waived *[v0.1.1 · A16]* |
| Information classification | Five ordered levels (least → most restrictive), wire values `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED` (display: Public, Internal, Sensitive, Restricted, Source-protected), authoritative per Data Model Specification v0.1.1 §16 | Access labels (purpose, jurisdiction, embargo, legal-review, compartment, etc.) are additive; the most restrictive applicable level plus all labels apply; derived objects/exports inherit the highest input classification unless a recorded reviewer downgrade decision exists; unknown or missing classification fails closed (deny and flag for classification). Framework v0.1 "Highly Restricted" is never auto-mapped to `SOURCE_PROTECTED` *[v0.1.1 · A08]* |

# 4. System Boundary and Actors

## 4.1 Primary actors

| **Actor** | **Responsibility** |
|----|----|
| Investigator | Creates and develops case material |
| Case Owner | Accountable for scope, gates, and dissemination decisions |
| Analyst | Performs entity/value-flow/typology/hypothesis analysis |
| Reviewer | Independent quality review |
| Evidence Custodian | Preserves originals, integrity, and evidence lineage |
| Data Steward | Approves significant entity merge/unmerge and data-quality changes |
| Source Handler | Controls protected-source identity |
| Platform/Security Admin | Operates IAM, configuration, backup, monitoring |
| Auditor | Reviews controls and audit history |

## 4.2 Trust boundaries

- User browser/client

- Application/API policy layer

- Canonical database

- Evidence object store

- Protected-source compartment

- Search/graph projections

- External integrations

- Backup/restore environment

- Administrative control plane

# 5. Architectural Constraints

- Canonical data and evidence remain independent from rebuildable search/graph projections.

- Original evidence is immutable to routine analyst workflows; transformations create derivatives.

- Entity merge decisions are reversible and must preserve history.

- All material adverse analytical claims remain traceable to evidence.

- Authorization is enforced at API/service layer, not only UI.

- High-impact dissemination requires accountable human authorization.

- AI and automation may assist but cannot silently promote generated output into material facts.

# 6. Functional Requirements

## 6.1 Case and Workflow

### SRS-FR-CASE-001 — Case creation

| **Requirement** | The system SHALL create a stable Case ID and require title, accountable owner, purpose, investigation question, sensitivity/classification, and status before a case becomes Active. |
|----|----|
| **Rationale** | Prevents orphaned or undefined investigations. |
| **Verification** | Create incomplete case and verify activation is blocked; complete required fields and verify activation succeeds. |
| **Priority** | MVP / P0 |
| **Traceability** | F-CASE-001; GOV-01; CAS-01 |

### SRS-FR-CASE-002 — Investigation Charter

| **Requirement** | The system SHALL version the Investigation Charter, including question, scope, exclusions, jurisdictions, period, authorised/prohibited collection methods, risks, and intended outputs. |
|----|----|
| **Rationale** | Controls scope and mission creep. |
| **Verification** | Edit charter twice and verify prior version remains retrievable with actor/time. |
| **Priority** | MVP / P0 |
| **Traceability** | F-CASE-002; CAS-01; PRI-01 |

### SRS-FR-CASE-003 — Lifecycle gates

| **Requirement** | The system SHALL support configurable G0–G6 lifecycle gates and SHALL prevent controlled actions when required approval is absent. |
|----|----|
| **Rationale** | Enforces stage-gated investigation methodology. |
| **Verification** | Attempt high-impact transition without approval and verify denial; approve independently and retry. |
| **Priority** | MVP / P0 |
| **Traceability** | F-CASE-003; CAS-02; QUA-01 |

### SRS-FR-CASE-004 — Tasks and assignments

| **Requirement** | The system SHALL support case-scoped tasks with owner, due date, type, status, dependencies, and immutable completion history. |
|----|----|
| **Rationale** | Coordinates investigative work. |
| **Verification** | Create, reassign, complete task and verify audit trail. |
| **Priority** | MVP / P0 |
| **Traceability** | F-CASE-004 |

### SRS-FR-CASE-005 — Case activity timeline

| **Requirement** | The system SHALL display material case actions in chronological order with actor, timestamp, object, and action type. |
|----|----|
| **Rationale** | Supports reconstructability. |
| **Verification** | Perform material actions and verify ordered visibility. |
| **Priority** | MVP / P0 |
| **Traceability** | F-CASE-005; AUD-01 |

## 6.2 Source, Evidence and Documents

### SRS-FR-EVD-001 — Source register

| **Requirement** | The system SHALL register material sources with origin, type, publisher/owner where known, access method, access timestamp, URL/location, reliability, legal/access note, and archival reference where available. |
|----|----|
| **Rationale** | Maintains provenance. |
| **Verification** | Create source and verify mandatory provenance validation. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-001; SRC-01 |

### SRS-FR-EVD-002 — Original preservation

| **Requirement** | The system SHALL preserve original evidence separately from working/derived artefacts and SHALL prevent routine analysts from modifying the original object. |
|----|----|
| **Rationale** | Protects evidence integrity. |
| **Verification** | Upload file, attempt overwrite as analyst, verify denial and new-version workflow. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-002; EVD-01 |

### SRS-FR-EVD-003 — Cryptographic integrity

| **Requirement** | The system SHALL compute SHA-256 or stronger approved hash for critical uploaded evidence and SHALL support recomputation/verification. |
|----|----|
| **Rationale** | Detects silent change. |
| **Verification** | Recompute hash and compare; alter test copy and verify mismatch. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-003; EVD-01 |

### SRS-FR-EVD-004 — Evidence extracts

| **Requirement** | The system SHALL allow page/paragraph/region extracts that remain linked to parent evidence and a precise source location. |
|----|----|
| **Rationale** | Enables citations and review. |
| **Verification** | Create extract and navigate back to original location. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-004; EVD-02 |

### SRS-FR-EVD-005 — Derivative lineage

| **Requirement** | The system SHALL record parent evidence, transformation type, tool/version where material, creator, and timestamp for OCR, translation, crop, parse, or derived dataset. |
|----|----|
| **Rationale** | Preserves transformation lineage. |
| **Verification** | Create derivative and verify reverse trace to original. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-005; EVD-02 |

### SRS-FR-EVD-006 — Reliability and credibility

| **Requirement** | The system SHALL store source reliability independently from information credibility and SHALL not reuse one value for both dimensions. |
|----|----|
| **Rationale** | Prevents false certainty. |
| **Verification** | Save different ratings and verify independent display/storage. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-006; SRC-02; ASM-01 |

## 6.2a Claim and Fact Lifecycle *[v0.1.1 · A10]*

> **Status of this family**  
> SRS-FR-CLM-001…004 were added in v0.1.1 as a remediation proposal (audit finding A10). They require product-owner approval before being treated as accepted scope. Object definitions follow Data Model Specification v0.1.1 §7.4 Claim and §7.5 Fact.

### SRS-FR-CLM-001 — Claim record and attribution

| **Requirement** | The system SHALL record each Claim as a source-attributed assertion linked to its asserting source/person and supporting evidence/extract references, with `claim_status` ∈ `RECORDED`, `UNDER_REVIEW`, `CORROBORATED`, `CONTRADICTED`, `UNRESOLVED`. Analyst conclusions SHALL NOT overwrite the claim's asserted content or attribution. The `disputed` boolean is retained for compatibility and SHALL be derived (true when status is `CONTRADICTED` or an open dispute exists). |
|----|----|
| **Rationale** | Keeps what a source asserted separate from what analysts concluded. |
| **Verification** | Create a claim from an extract; record an analyst conclusion; verify the claim content and attribution are unchanged and `disputed` is derived from status. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-008; SRC-01; EVD-02 |

### SRS-FR-CLM-002 — Verification decision

| **Requirement** | Every verification outcome on a claim or fact SHALL be stored as a separate, append-only VerificationDecision record containing target_ref (claim or fact), decision, rationale, evidence_refs, decided_by, decided_at, and optional review_ref. Existing decisions SHALL NOT be edited or deleted. |
|----|----|
| **Rationale** | Makes every verification judgement reviewable and attributable. |
| **Verification** | Record two decisions on one claim; attempt to modify the first and verify rejection; verify both remain retrievable in order with attribution. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-008; AUD-01; QUA-01 |

### SRS-FR-CLM-003 — Fact promotion

| **Requirement** | The system SHALL create a Fact only when it references source claim(s) and/or evidence and a VerificationDecision; a new Fact SHALL start as `PROVISIONAL`. `fact_status` ∈ `PROVISIONAL`, `ESTABLISHED`, `DISPUTED`, `SUPERSEDED`. Investigators/Analysts MAY record claims and propose `PROVISIONAL` facts; moving a fact to `ESTABLISHED` SHALL require a Reviewer who is not the proposer. Evidence extracts and AI/automation output SHALL NOT become facts except through this path. |
|----|----|
| **Rationale** | Prevents a claim or extract from being treated as fact without a reviewable decision. |
| **Verification** | Attempt to create a fact without refs or decision and verify rejection; proposer attempts to establish own fact and is denied; an independent reviewer establishes it and the decision is recorded. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-008; EVD-02; QUA-01 |

### SRS-FR-CLM-004 — Fact revision and dependent flagging

| **Requirement** | Any authorized case member SHALL be able to move a fact to `DISPUTED` with supporting evidence; `SUPERSEDED` SHALL require a replacement fact reference (`superseded_by`). When a fact becomes `DISPUTED` or `SUPERSEDED`, every dependent Assessment and IntelligenceProduct SHALL be flagged `review_required` with a link to the triggering decision. Published products SHALL NOT be mutated; a correction review task SHALL be created instead. History SHALL be preserved. |
|----|----|
| **Rationale** | Ensures corrections propagate to dependent analysis without rewriting history. |
| **Verification** | Pilot: record a source claim; promote a `PROVISIONAL` fact; establish it; dispute it with contradicting evidence; supersede it. Verify dependent assessment/product are flagged, the published product is unchanged, a correction review task exists, and full history is retrievable. |
| **Priority** | MVP / P0 |
| **Traceability** | F-EVD-008; ASM-01; DIS-01 |

### SRS-FR-DOC-001 — Document ingestion

| **Requirement** | The system SHALL ingest PDF, DOCX, XLSX, CSV, TXT, and common image formats while preserving original bytes. |
|----|----|
| **Rationale** | Supports core evidence intake. |
| **Verification** | Upload representative formats and verify originals plus metadata. |
| **Priority** | MVP / P0 |
| **Traceability** | F-DOC-001 |

## 6.3 Entity, Relationship and Asset

### SRS-FR-ENT-001 — Entity registry

| **Requirement** | The system SHALL support canonical Entity records for person, organisation/company, account, wallet, address, domain, phone/email, government agency, and extensible types. |
|----|----|
| **Rationale** | Provides reusable identity layer. |
| **Verification** | Create each baseline type and verify unique stable identifiers. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ENT-001; ENT-01 |

### SRS-FR-ENT-002 — Aliases and identifiers

| **Requirement** | The system SHALL allow conflicting aliases/identifiers to coexist with separate provenance and status. |
|----|----|
| **Rationale** | Preserves uncertainty and contradictory data. |
| **Verification** | Add conflicting identifiers and verify neither overwrites the other. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ENT-002 |

### SRS-FR-ENT-003 — Candidate matching

| **Requirement** | The system SHALL present matching and conflicting features for possible duplicates before merge. |
|----|----|
| **Rationale** | Reduces false entity consolidation. |
| **Verification** | Create similar entities and verify comparison view. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ENT-003; ENT-01 |

### SRS-FR-ENT-004 — Merge and unmerge

| **Requirement** | The system SHALL support evidence-based merge with rationale and SHALL support unmerge that restores prior records and relationships without erasing history. |
|----|----|
| **Rationale** | Protects analytical reversibility. |
| **Verification** | Merge then unmerge test entities; compare pre/post state and audit log. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ENT-004; AUD-01 |

### SRS-FR-ENT-005 — Entity resolution status

| **Requirement** | The system SHALL support candidate, probable, confirmed, disputed, and unresolved statuses and SHALL expose status in search/graph views. |
|----|----|
| **Rationale** | Keeps identity uncertainty visible. |
| **Verification** | Change status and verify graph/search labels. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ENT-005 |

### SRS-FR-REL-001 — First-class relationship

| **Requirement** | The system SHALL represent material relationships as canonical objects with type, endpoints, evidence, dates, confidence, status, and analyst. |
|----|----|
| **Rationale** | Prevents graph-only unsupported edges. |
| **Verification** | Create relationship and trace from graph to evidence. |
| **Priority** | MVP / P0 |
| **Traceability** | F-REL-001; REL-01 |

### SRS-FR-REL-002 — Ownership interest

| **Requirement** | The system SHALL represent direct/indirect ownership with percentage or unknown, dates, and evidence. |
|----|----|
| **Rationale** | Supports beneficial-ownership analysis without fabricated zeroes. |
| **Verification** | Create unknown and numeric ownership records; verify semantics. |
| **Priority** | MVP / P0 |
| **Traceability** | F-REL-002 |

### SRS-FR-REL-003 — Control distinction

| **Requirement** | The system SHALL distinguish legal ownership, beneficial ownership, control, use, and association. |
|----|----|
| **Rationale** | Avoids collapsing materially different relationships. |
| **Verification** | Create each relation type and verify distinct UI/API representation. |
| **Priority** | MVP / P0 |
| **Traceability** | F-REL-003; AST-01 |

### SRS-FR-AST-001 — Asset registry

| **Requirement** | The system SHALL support property, vehicle, shares, vessel, aircraft, crypto and extensible asset types with attribution type and evidence. |
|----|----|
| **Rationale** | Supports asset tracing. |
| **Verification** | Create asset with ownership and control assertions. |
| **Priority** | MVP / P0 |
| **Traceability** | F-AST-001 |

## 6.4 Event, Timeline and Value Flow

### SRS-FR-TIM-001 — Event records

| **Requirement** | The system SHALL store events with type, date/date-range, date precision, linked entities/assets, location where relevant, and evidence. |
|----|----|
| **Rationale** | Supports temporal analysis. |
| **Verification** | Create exact/approximate events and verify precision retained. |
| **Priority** | MVP / P0 |
| **Traceability** | F-TIM-001 |

### SRS-FR-TIM-002 — Visual timeline

| **Requirement** | The system SHALL render filtered timelines for case/entity/asset and link each item to canonical event/evidence. |
|----|----|
| **Rationale** | Enables chronological reconstruction. |
| **Verification** | Filter timeline and open source event. |
| **Priority** | MVP / P0 |
| **Traceability** | F-TIM-002 |

### SRS-FR-VAL-001 — Value-flow record

| **Requirement** | The system SHALL require origin, destination, mechanism, value/range/unknown, currency where applicable, date/date-range, evidence, confidence, and mandatory flow_class. |
|----|----|
| **Rationale** | Makes value movement explicit and qualified. |
| **Verification** | Create all four flow classes and verify mandatory fields. |
| **Priority** | MVP / P0 |
| **Traceability** | F-VAL-001; VAL-01 |

### SRS-FR-VAL-002 — Multi-leg flows

| **Requirement** | The system SHALL support multi-leg value-flow chains in which every leg retains separate evidence, class, value, and confidence. |
|----|----|
| **Rationale** | Avoids certainty inheritance across a chain. |
| **Verification** | Create 3-leg mixed-class flow and inspect each leg. |
| **Priority** | MVP / P0 |
| **Traceability** | F-VAL-002 |

### SRS-FR-VAL-003 — Flow visualisation

| **Requirement** | The system SHALL visually distinguish DIRECT, DOCUMENTED, RECONSTRUCTED, and HYPOTHETICAL flows in interactive and exported views. |
|----|----|
| **Rationale** | Prevents inference from looking like direct transaction evidence. |
| **Verification** | Export mixed-class flow and verify class distinction persists. |
| **Priority** | MVP / P0 |
| **Traceability** | F-VAL-003 |

### SRS-FR-VAL-004 — Unknown and ranges

| **Requirement** | The system SHALL represent unknown, minimum, maximum, and approximate values without coercing unknown to numeric zero. |
|----|----|
| **Rationale** | Preserves uncertainty. |
| **Verification** | Store unknown/range values and inspect API/UI. |
| **Priority** | MVP / P0 |
| **Traceability** | F-VAL-004 |

## 6.5 Typology, Hypothesis and Assessment

### SRS-FR-TYP-001 — Typology catalogue

| **Requirement** | The system SHALL expose versioned CS-AML typology entries with definition, mechanism, observables, indicators, counter-indicators, false positives, and references. |
|----|----|
| **Rationale** | Supports consistent analysis. |
| **Verification** | Open typology and verify version and fields. |
| **Priority** | MVP / P0 |
| **Traceability** | F-TYP-001; TYP-01 |

### SRS-FR-TYP-002 — Indicator capture

| **Requirement** | The system SHALL allow indicators and counter-indicators to link to evidence and analytical objects. |
|----|----|
| **Rationale** | Prevents free-floating allegations. |
| **Verification** | Create indicator with evidence and verify assessment traceability. |
| **Priority** | MVP / P0 |
| **Traceability** | F-TYP-002 |

### SRS-FR-TYP-003 — Typology match worksheet

| **Requirement** | The system SHALL support controlled consistency levels and SHALL prevent a single weak indicator from automatically creating a strong typology match. |
|----|----|
| **Rationale** | Controls overstatement. |
| **Verification** | Create single weak indicator and verify no automatic strong match. |
| **Priority** | MVP / P0 |
| **Traceability** | F-TYP-003 |

### SRS-FR-HYP-001 — Competing hypotheses

| **Requirement** | The system SHALL support at least two competing hypotheses per material investigation where alternatives are plausible. |
|----|----|
| **Rationale** | Reduces confirmation bias. |
| **Verification** | Create H1/H2 and link supporting/contradicting evidence. |
| **Priority** | MVP / P0 |
| **Traceability** | F-HYP-001; HYP-01 |

### SRS-FR-HYP-002 — Support and contradiction matrix

| **Requirement** | The system SHALL store evidence/indicator effect on each hypothesis as support, contradiction, neutral, or unknown with analyst rationale. |
|----|----|
| **Rationale** | Makes reasoning inspectable. |
| **Verification** | Populate matrix and verify every cell retains rationale/history. |
| **Priority** | MVP / P0 |
| **Traceability** | F-HYP-002 |

### SRS-FR-HYP-003 — Intelligence gaps

| **Requirement** | The system SHALL maintain explicit intelligence gaps capable of affecting an assessment. |
|----|----|
| **Rationale** | Keeps unknowns visible. |
| **Verification** | Create gap and include it in final assessment. |
| **Priority** | MVP / P0 |
| **Traceability** | F-HYP-003; GAP-01 |

### SRS-FR-ASM-001 — Assessment

| **Requirement** | The system SHALL store judgement, confidence, basis, alternatives, gaps, author, reviewer, and version. |
|----|----|
| **Rationale** | Creates reproducible analytical product. |
| **Verification** | Create and revise assessment; verify version history. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ASM-001; ASM-01 |

### SRS-FR-ASM-002 — Confidence model

| **Requirement** | The system SHALL support the confidence levels `HIGH`, `MODERATE`, `LOW`, and `INSUFFICIENT_BASIS` (wire values from the Data Model Annex A registry; display labels High, Moderate, Low, Insufficient Basis are separate and translatable), each with mandatory rationale. `INSUFFICIENT_BASIS` means a judgement was attempted but the evidential basis is insufficient; it is not a level below `LOW` and SHALL NOT be converted to `LOW`, null, zero, or omitted. Null is permitted only on drafts where no confidence judgement has been made; a finalized assessment SHALL carry a non-null level. No normalization, import, or export SHALL raise certainty. *[v0.1.1 · A09]* |
|----|----|
| **Rationale** | Avoids pseudo-precision. |
| **Verification** | Save each level and verify mandatory rationale; round-trip every level through DB/API/UI/export and verify `INSUFFICIENT_BASIS` is never converted to `LOW`, null, or zero; attempt to finalize an assessment with a null level and verify rejection. *[v0.1.1 · A09]* |
| **Priority** | MVP / P0 |
| **Traceability** | F-ASM-002 |

### SRS-FR-ASM-003 — Backward traceability

| **Requirement** | The system SHALL allow a reviewer to traverse an assessment backward through hypotheses/indicators/facts/evidence/sources. |
|----|----|
| **Rationale** | Core reproducibility requirement. |
| **Verification** | Select key assessment and trace to origin without external notes. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ASM-001; ASM-01 *[v0.1.1 · A05]* |

### SRS-FR-ASM-004 — Disconfirming search record *[v0.1.1 · A05]*

| **Requirement** | The system SHALL require a recorded disconfirming-search entry (what was searched, sources consulted, result, rationale) before a high-impact or adverse assessment/product can pass review. |
|----|----|
| **Rationale** | Ensures evidence that could weaken adverse findings has been sought and recorded; tested separately from backward traceability (SRS-FR-ASM-003). |
| **Verification** | Attempt to pass review of a high-impact adverse assessment without a disconfirmation record; verify rejection. Add the record; verify review can proceed. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ASM-003; HYP-02; QUA-01 *[v0.1.1 · A05]* |

## 6.6 Search and Graph

### SRS-FR-SCH-001 — Full-text and object search

| **Requirement** | The system SHALL search authorised cases, entities, sources, evidence metadata, extracts, assets, events, and products using full-text and structured filters. |
|----|----|
| **Rationale** | Supports investigation retrieval. |
| **Verification** | Search known fixture and verify expected scoped results. |
| **Priority** | MVP / P0 |
| **Traceability** | F-SCH-001 |

### SRS-FR-SCH-002 — Permission-filtered results

| **Requirement** | The system SHALL apply object-level authorization before returning search results or counts. |
|----|----|
| **Rationale** | Prevents existence leakage. |
| **Verification** | Compare user with/without access and verify hidden objects do not affect result counts. |
| **Priority** | MVP / P0 |
| **Traceability** | F-SCH-002; SEC-01 |

### SRS-FR-GRF-001 — Graph exploration

| **Requirement** | The system SHALL display authorised entities and canonical relationships with evidence/status/confidence access from each edge. |
|----|----|
| **Rationale** | Supports network analysis without hiding provenance. |
| **Verification** | Expand graph and open edge evidence. |
| **Priority** | MVP / P0 |
| **Traceability** | F-GRF-001 |

## 6.7 Intelligence Product, Review and Dissemination

### SRS-FR-PRD-001 — Product templates

| **Requirement** | The system SHALL generate Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, and Case Report from canonical objects. |
|----|----|
| **Rationale** | Standardises outputs. |
| **Verification** | Generate each baseline template with metadata/evidence index. |
| **Priority** | MVP / P0 |
| **Traceability** | F-PRD-001 |

### SRS-FR-REV-001 — Peer review workflow

| **Requirement** | The system SHALL support comment, request-change, approve, and reject; high-impact approval SHALL be attributable and independent where policy requires. |
|----|----|
| **Rationale** | Implements quality gate. |
| **Verification** | Author attempts self-approval under independent-review policy and is denied. |
| **Priority** | MVP / P0 |
| **Traceability** | F-REV-001; QUA-01 |

### SRS-FR-PRD-002 — Versioning and corrections

| **Requirement** | The system SHALL preserve prior intelligence-product versions and mark superseded/corrected versions explicitly. |
|----|----|
| **Rationale** | Prevents historical rewriting. |
| **Verification** | Issue correction and verify old version remains immutable/readable. |
| **Priority** | MVP / P0 |
| **Traceability** | F-PRD-002; AUD-01 |

### SRS-FR-PRD-003 — Evidence index

| **Requirement** | The system SHALL generate an evidence/source index sufficient to trace every material fact/findings used in a product. |
|----|----|
| **Rationale** | Supports review and referral. |
| **Verification** | Generate product and click/resolve each material citation. |
| **Priority** | MVP / P0 |
| **Traceability** | F-PRD-003 |

### SRS-FR-DIS-001 — Dissemination approval

| **Requirement** | The system SHALL block external export until required handling classification, recipient, purpose, and approval are recorded. |
|----|----|
| **Rationale** | Controls harm and confidentiality. |
| **Verification** | Attempt export before approval and verify denial. |
| **Priority** | MVP / P0 |
| **Traceability** | F-DIS-001; DIS-01 |

### SRS-FR-DIS-002 — Secure export

| **Requirement** | The system SHALL export only explicitly approved objects and SHALL support minimisation/redaction. |
|----|----|
| **Rationale** | Prevents accidental over-disclosure. |
| **Verification** | Export package and verify excluded restricted object is absent. |
| **Priority** | MVP / P0 |
| **Traceability** | F-DIS-002; PRI-01 |

### SRS-FR-DIS-003 — Referral package

| **Requirement** | The system SHALL generate structured referral containing subjects, key facts, evidence references, timeline, value flows, indicators, gaps, confidence, and contact point. |
|----|----|
| **Rationale** | Makes outputs actionable. |
| **Verification** | Generate referral and verify fact/analysis/unknown sections remain distinct. |
| **Priority** | MVP / P0 |
| **Traceability** | F-DIS-003 |

### SRS-FR-DIS-004 — Sharing log

| **Requirement** | The system SHALL record recipient, product/version, date, purpose, restrictions, and approving user for every external dissemination. |
|----|----|
| **Rationale** | Maintains accountability. |
| **Verification** | Share export and verify immutable log entry. |
| **Priority** | MVP / P0 |
| **Traceability** | F-DIS-004; AUD-01 |

## 6.8 Administration, Security and Operations

### SRS-FR-ADM-001 — Controlled vocabularies

| **Requirement** | The system SHALL version relationship types, asset types, statuses, classifications, and other controlled vocabularies. |
|----|----|
| **Rationale** | Preserves historical semantics. |
| **Verification** | Change label and verify historical record retains version context. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ADM-001 |

### SRS-FR-ADM-003 — Retention policies

| **Requirement** | The system SHALL support retention/disposition policy by object type/classification and SHALL audit disposition actions. |
|----|----|
| **Rationale** | Implements data minimisation lifecycle. |
| **Verification** | Preview and execute test disposition with audit evidence. |
| **Priority** | MVP / P0 |
| **Traceability** | F-ADM-003; PRI-02 |

### SRS-FR-SEC-001 — OIDC and MFA

| **Requirement** | The system SHALL authenticate via OIDC-compatible identity provider and enforce MFA according to deployment policy. |
|----|----|
| **Rationale** | Strong identity control. |
| **Verification** | Disable IdP user and verify access revoked; validate MFA path. |
| **Priority** | MVP / P0 |
| **Traceability** | F-SEC-001 |

### SRS-FR-SEC-002 — Role/object access

| **Requirement** | The system SHALL enforce role, case membership, classification, and need-to-know at the API/service layer. |
|----|----|
| **Rationale** | Core confidentiality requirement. |
| **Verification** | Direct API access to unauthorised object must return denial regardless of UI. |
| **Priority** | MVP / P0 |
| **Traceability** | F-SEC-002; SEC-01 |

### SRS-FR-SEC-003 — Protected-source compartment

| **Requirement** | The system SHALL store protected-source identity under separate authorization so analysts may use source-derived evidence without automatically seeing identity. |
|----|----|
| **Rationale** | Protects vulnerable sources. |
| **Verification** | Analyst can access derived evidence but not source identity. |
| **Priority** | MVP / P0 |
| **Traceability** | F-SEC-003; SEC-02 |

### SRS-FR-AUD-001 — Immutable audit trail

| **Requirement** | The system SHALL record material create/update/delete/merge/unmerge/review/export/access-policy actions and ordinary users SHALL NOT modify audit records. |
|----|----|
| **Rationale** | Supports accountability. |
| **Verification** | Attempt audit modification as ordinary user and verify denial. |
| **Priority** | MVP / P0 |
| **Traceability** | F-AUD-001 |

### SRS-FR-OPS-001 — Backup and restore

| **Requirement** | The system SHALL back up canonical DB, evidence, configuration, and required keys/metadata using documented recovery procedures and SHALL support periodic restore tests. |
|----|----|
| **Rationale** | Provides recoverability. |
| **Verification** | Perform restore drill into isolated environment and document result. |
| **Priority** | MVP / P0 |
| **Traceability** | F-OPS-001 |

# 7. Data Requirements

### SRS-DR-001 — Canonical object set

| **Requirement** | The system SHALL implement at minimum Case, Source, EvidenceItem, EvidenceExtract, Claim, VerificationDecision, Fact, Entity, Relationship, Asset, Event, ValueFlow, Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment, IntelligenceProduct, Review, Dissemination, and AuditEvent as durable domain objects. *[v0.1.1 · A10]* |
|----|----|
| **Rationale** | Aligns SRS with canonical data model. |
| **Verification** | Schema review and CRUD contract tests for all required object types. |
| **Priority** | MVP |
| **Traceability** | Data Model v0.1.1 |

### SRS-DR-002 — Stable identifiers

| **Requirement** | Every canonical object SHALL have a stable, non-recycled identifier independent of display name. |
|----|----|
| **Rationale** | Supports audit and linking. |
| **Verification** | Rename object and verify identifier unchanged. |
| **Priority** | MVP |
| **Traceability** | Data Model v0.1.1 |

### SRS-DR-003 — Version semantics

| **Requirement** | Material assessments, charters, products, vocabularies, and other configured material objects SHALL preserve version history. |
|----|----|
| **Rationale** | Prevents historical overwrite. |
| **Verification** | Update object and retrieve prior version. |
| **Priority** | MVP |
| **Traceability** | AUD-01 |

### SRS-DR-004 — Temporal semantics

| **Requirement** | Objects with temporal meaning SHALL support valid-time fields and precision/unknown semantics rather than forcing exact dates. |
|----|----|
| **Rationale** | Supports imperfect open-source data. |
| **Verification** | Store year-only and approximate event date. |
| **Priority** | MVP |
| **Traceability** | Data Model v0.1.1 |

### SRS-DR-005 — Provenance references

| **Requirement** | Material facts, relationships, asset attributions, value-flow legs, indicators, and assessments SHALL reference supporting evidence and/or source objects. |
|----|----|
| **Rationale** | Core evidentiary traceability. |
| **Verification** | Run orphan-proposition integrity check. |
| **Priority** | MVP |
| **Traceability** | SRC-01; REL-01; VAL-01 |

### SRS-DR-006 — Deletion semantics

| **Requirement** | Deletion of canonical investigative objects SHALL be soft-delete/tombstone or equivalent where audit/history obligations require preservation; hard deletion SHALL be controlled by retention/disposition policy. |
|----|----|
| **Rationale** | Balances history with minimisation. |
| **Verification** | Delete test object and verify policy-compliant behaviour. |
| **Priority** | MVP |
| **Traceability** | PRI-02; AUD-01 |

# 8. External Interface Requirements

### SRS-IF-001 — Web user interface

| **Requirement** | The MVP SHALL provide a responsive web interface for supported desktop browsers; mobile support MAY be read-only or limited. |
|----|----|
| **Rationale** | Primary analyst workstation assumption. |
| **Verification** | Browser compatibility and viewport tests. |
| **Priority** | MVP |
| **Traceability** | PRD UX |

### SRS-IF-002 — REST/HTTP API

| **Requirement** | The system SHALL expose versioned authenticated APIs for canonical objects and SHALL enforce identical authorization rules to the UI. Mutations of versioned resources SHALL use `If-Match` preconditions (missing → 428 `PRECONDITION_REQUIRED`; stale → 412 `PRECONDITION_FAILED`; no silent overwrite); 409 `STATE_CONFLICT` is reserved for workflow/business-state conflicts. Material commands (evidence ingest finalization, merge/unmerge, review/dissemination approval, export package generation) SHALL require an `Idempotency-Key`. An OpenAPI 3.1 document SHALL be generated from the implementation and exercised by contract tests; detailed semantics are in API Specification v0.1.1, and the OpenAPI artefact does not yet exist (open item). *[v0.1.1 · A04, A11]* |
|----|----|
| **Rationale** | Enables integration and testability. |
| **Verification** | API contract tests plus authorization parity tests. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

### SRS-IF-003 — OIDC identity provider

| **Requirement** | The system SHALL integrate with an OIDC-compatible provider for authentication and group/claim mapping. Browser authentication SHALL use a server-side session (BFF): the backend is a confidential OIDC client (Authorization Code + PKCE), the browser holds only an HttpOnly, Secure session cookie, tokens are never exposed to JavaScript, and unsafe methods carry a CSRF token. *[v0.1.1 · A11]* |
|----|----|
| **Rationale** | Avoids custom password storage where possible. |
| **Verification** | IdP login/logout/disable/claim tests. |
| **Priority** | MVP |
| **Traceability** | SEC-01 |

### SRS-IF-004 — Object/evidence storage

| **Requirement** | The system SHALL support encrypted object/file storage for evidence and derivatives with immutable-original semantics. |
|----|----|
| **Rationale** | Separates binary evidence from transactional records. |
| **Verification** | Upload/download/hash/permission tests. |
| **Priority** | MVP |
| **Traceability** | EVD-01 |

### SRS-IF-005 — Export formats

| **Requirement** | The system SHALL support PDF and machine-readable JSON/CSV where relevant for approved exports; exported analytical semantics SHALL preserve uncertainty/status/classification. |
|----|----|
| **Rationale** | Supports human and system recipients. |
| **Verification** | Round-trip test representative objects and inspect uncertainty fields. |
| **Priority** | MVP |
| **Traceability** | DIS-01 |

# 9. Security and Privacy Requirements

### SRS-SEC-001 — Least privilege

| **Requirement** | All authenticated access SHALL default deny and be granted by explicit role/object policy. |
|----|----|
| **Rationale** | Sensitive investigations require compartmentalisation. |
| **Verification** | Permission matrix tests including negative cases. |
| **Priority** | MVP |
| **Traceability** | SEC-01 |

### SRS-SEC-002 — Encryption in transit

| **Requirement** | All production HTTP/API traffic SHALL use TLS; plaintext administrative or application access SHALL be disabled except explicitly isolated development environments. |
|----|----|
| **Rationale** | Protects credentials and case data. |
| **Verification** | TLS configuration scan. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

### SRS-SEC-003 — Encryption at rest

| **Requirement** | Canonical databases, evidence stores, backups, and protected-source data SHALL use encryption at rest appropriate to deployment risk. |
|----|----|
| **Rationale** | Protects stolen media/snapshots. |
| **Verification** | Configuration and restore tests. |
| **Priority** | MVP |
| **Traceability** | SEC-02 |

### SRS-SEC-004 — Secrets management

| **Requirement** | Application secrets SHALL NOT be embedded in source code or container images and SHALL be stored/rotated through an approved secret-management mechanism. |
|----|----|
| **Rationale** | Reduces credential leakage. |
| **Verification** | Repository/image scan and rotation test. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

### SRS-SEC-005 — Session control

| **Requirement** | Sessions SHALL support idle timeout, absolute lifetime, revocation, and reauthentication for configured high-risk actions. |
|----|----|
| **Rationale** | Reduces account takeover impact. |
| **Verification** | Session expiry/revocation test. |
| **Priority** | MVP |
| **Traceability** | SEC-01 |

### SRS-SEC-006 — Protected source isolation

| **Requirement** | Protected-source identity SHALL be logically separated from routine case content and SHALL use a narrower permission set. |
|----|----|
| **Rationale** | Protects human sources. |
| **Verification** | Cross-role authorization test. |
| **Priority** | MVP |
| **Traceability** | SEC-02 |

### SRS-SEC-007 — Data minimisation

| **Requirement** | The system SHALL support classification, purpose/scope linkage, retention state, and controlled export so sensitive data can be minimised throughout the lifecycle. |
|----|----|
| **Rationale** | Implements CSO privacy guardrails. |
| **Verification** | Retention/export/minimisation workflow test. |
| **Priority** | MVP |
| **Traceability** | PRI-01; PRI-02 |

### SRS-SEC-008 — Security logging

| **Requirement** | Security logs SHALL capture authentication, authorization failures, admin changes, and export events without unnecessarily recording evidence payloads or protected-source content. |
|----|----|
| **Rationale** | Balances detection and confidentiality. |
| **Verification** | Log inspection with synthetic sensitive fields. |
| **Priority** | MVP |
| **Traceability** | AUD-01 |

# 10. Audit and Provenance Requirements

### SRS-AUD-001 — Audit event content

| **Requirement** | Material audit events SHALL include actor, action, object ID/type, timestamp, case/context when applicable, and before/after or change reference where appropriate. |
|----|----|
| **Rationale** | Allows reconstruction. |
| **Verification** | Inspect representative audit records. |
| **Priority** | MVP |
| **Traceability** | AUD-01 |

### SRS-AUD-002 — Audit integrity

| **Requirement** | Ordinary application users SHALL NOT alter or delete audit events. Administrative maintenance SHALL itself be logged. |
|----|----|
| **Rationale** | Prevents tampering. |
| **Verification** | Role test and admin-maintenance audit test. |
| **Priority** | MVP |
| **Traceability** | AUD-01 |

### SRS-AUD-003 — Provenance traversal

| **Requirement** | The system SHALL provide forward/backward traversal between Source, Evidence, derived artefacts, Facts, Indicators, Hypotheses, Assessments and Products. |
|----|----|
| **Rationale** | Makes reasoning reviewable. |
| **Verification** | Traverse complete pilot-case chain. |
| **Priority** | MVP |
| **Traceability** | ASM-003; EVD-02 |

### SRS-AUD-004 — Merge history

| **Requirement** | Entity merge/unmerge decisions SHALL record rationale, actor, timestamp, compared features, supporting evidence, and resulting mapping. |
|----|----|
| **Rationale** | Critical identity-control history. |
| **Verification** | Merge/unmerge audit test. |
| **Priority** | MVP |
| **Traceability** | ENT-01 |

# 11. Performance and Scalability

### SRS-NFR-PERF-001 — Interactive latency

| **Requirement** | For a reference MVP deployment, 95% of ordinary authenticated page/API reads SHOULD complete within 2 seconds excluding large file transfer, complex graph traversal, OCR, exports, and external connectors. |
|----|----|
| **Rationale** | Usability baseline. |
| **Verification** | Load test reference dataset. |
| **Priority** | MVP target |
| **Traceability** | PRD NFR |

### SRS-NFR-PERF-002 — Search latency

| **Requirement** | Permission-filtered search SHOULD return first-page results within 3 seconds at reference MVP scale. |
|----|----|
| **Rationale** | Analyst productivity. |
| **Verification** | Search benchmark under concurrent users. |
| **Priority** | MVP target |
| **Traceability** | CAP-10 (Search / Graph / Analytics, product capability registry) *[v0.1.1 · A07]* |

### SRS-NFR-PERF-003 — Upload size

| **Requirement** | The deployment SHALL define configurable maximum upload size and SHALL fail safely without partial canonical records when exceeded or interrupted. |
|----|----|
| **Rationale** | Evidence reliability. |
| **Verification** | Boundary upload tests. |
| **Priority** | MVP target |
| **Traceability** | F-DOC-001 |

### SRS-NFR-PERF-004 — Reference scale

| **Requirement** | MVP SHALL support at least 25 concurrent authenticated users, 100,000 canonical entities/relationships combined, and 100 GB evidence storage in a reference small-organisation deployment, subject to deployment profile tuning. |
|----|----|
| **Rationale** | Provides engineering sizing target. |
| **Verification** | Synthetic scale/load test. |
| **Priority** | MVP target |
| **Traceability** | Technology Architecture |

# 12. Reliability, Backup and Disaster Recovery

### SRS-NFR-REL-001 — Transactional consistency

| **Requirement** | Canonical state changes that span related records SHALL use transactional or compensating mechanisms to avoid orphan/inconsistent material records. |
|----|----|
| **Rationale** | Protects data integrity. |
| **Verification** | Fault-injection transaction tests. |
| **Priority** | MVP |
| **Traceability** | Data Model |

### SRS-NFR-REL-002 — Backup coverage

| **Requirement** | Backups SHALL include canonical DB, evidence metadata and files, configuration required for restore, and protected-source data according to classification. |
|----|----|
| **Rationale** | Complete recovery. |
| **Verification** | Backup inventory review. |
| **Priority** | MVP |
| **Traceability** | OPS-001 |

### SRS-NFR-REL-003 — Restore testing

| **Requirement** | A restore procedure SHALL be executable into an isolated environment and SHOULD be tested at least quarterly for production deployments. |
|----|----|
| **Rationale** | Proves recoverability. |
| **Verification** | Documented restore drill. |
| **Priority** | MVP |
| **Traceability** | OPS-001 |

### SRS-NFR-REL-004 — RPO/RTO profile

| **Requirement** | Deployment documentation SHALL declare target RPO and RTO. MVP reference target SHOULD be RPO ≤24h and RTO ≤8h unless organisational risk requires stricter objectives. |
|----|----|
| **Rationale** | Makes resilience measurable. |
| **Verification** | DR plan review and timed restore. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

# 13. Search, Graph and Analytical Requirements

### SRS-AN-001 — Canonical projection

| **Requirement** | Search and graph stores SHALL be rebuildable projections from canonical objects and SHALL retain canonical object identifiers. |
|----|----|
| **Rationale** | Avoids projection becoming truth source. |
| **Verification** | Delete/rebuild projection and compare object identity. |
| **Priority** | MVP/P1 where noted |
| **Traceability** | Technology Architecture |

### SRS-AN-002 — Uncertainty propagation

| **Requirement** | Graph/search/analytics views SHALL display or expose material status/confidence/class fields used by the canonical records. |
|----|----|
| **Rationale** | Prevents visual certainty inflation. |
| **Verification** | Inspect disputed entity and reconstructed flow in all views. |
| **Priority** | MVP/P1 where noted |
| **Traceability** | Technology Architecture |

### SRS-AN-003 — Path semantics

| **Requirement** | Any path/graph traversal result SHALL be presented as a path over existing relationships, not as proof of a direct relationship between endpoints. |
|----|----|
| **Rationale** | Prevents inference misuse. |
| **Verification** | Path-result wording/UI test. |
| **Priority** | MVP/P1 where noted |
| **Traceability** | TEC-02 |

# 14. AI and Automation Requirements

### SRS-AI-001 — Derived status

| **Requirement** | AI/OCR/NLP-generated outputs SHALL be marked as derived/candidate material with model/tool version and source context when material. |
|----|----|
| **Rationale** | Prevents automation from becoming evidence. |
| **Verification** | Generate candidate and inspect metadata. |
| **Priority** | P1 unless AI disabled |
| **Traceability** | TEC-01 |

### SRS-AI-002 — Human verification

| **Requirement** | AI output SHALL NOT become a material fact, canonical entity merge, adverse assessment, or dissemination approval without explicit human verification. |
|----|----|
| **Rationale** | Preserves accountability. |
| **Verification** | Attempt automated promotion and verify blocked state. |
| **Priority** | P1 unless AI disabled |
| **Traceability** | TEC-01 |

### SRS-AI-003 — Authorization boundary

| **Requirement** | AI services SHALL receive only content the invoking user/service is authorised to access; retrieval for AI SHALL enforce the same object policies. |
|----|----|
| **Rationale** | Prevents cross-case leakage. |
| **Verification** | Prompt/AI retrieval authorization tests. |
| **Priority** | P1 unless AI disabled |
| **Traceability** | SEC-01 |

### SRS-AI-004 — Optional feature flag

| **Requirement** | AI assistance SHALL be disableable at deployment/environment level without breaking core investigative workflows. |
|----|----|
| **Rationale** | Supports high-risk/offline environments. |
| **Verification** | Disable AI and execute MVP pilot case. |
| **Priority** | P1 unless AI disabled |
| **Traceability** | F-ADM-004 |

# 15. UX and Accessibility Requirements

### SRS-UX-001 — Evidence-first navigation

| **Requirement** | Material analytical records SHALL expose a direct route to supporting evidence/source in no more than a small number of user actions. |
|----|----|
| **Rationale** | Review efficiency. |
| **Verification** | Usability test with analyst. |
| **Priority** | MVP |
| **Traceability** | PRD UX |

### SRS-UX-002 — Visible uncertainty

| **Requirement** | Candidate/disputed entities, inferred relationships, and reconstructed/hypothetical flows SHALL be visually distinguishable from confirmed/direct records. |
|----|----|
| **Rationale** | Core analytical safety. |
| **Verification** | Visual regression/usability test. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

### SRS-UX-003 — Destructive action confirmation

| **Requirement** | Merge, unmerge, disposition, external export, and other high-impact actions SHALL require explicit confirmation and appropriate authorization. |
|----|----|
| **Rationale** | Reduces accidental harm. |
| **Verification** | Negative/confirmation tests. |
| **Priority** | MVP |
| **Traceability** | Control Guide |

### SRS-UX-004 — Accessibility baseline

| **Requirement** | Primary workflows SHOULD meet WCAG 2.2 AA principles where feasible, including keyboard navigation, labels, contrast, and non-colour-only meaning. |
|----|----|
| **Rationale** | Inclusive use. |
| **Verification** | Automated plus manual accessibility checks. |
| **Priority** | MVP |
| **Traceability** | Product requirement |

# 16. Administration and Configuration

### SRS-ADM-001 — Policy configuration

| **Requirement** | Admins SHALL configure classifications, role mappings, controlled vocabularies, retention rules, and feature flags without direct database editing. |
|----|----|
| **Rationale** | Safe administration. |
| **Verification** | Admin UI/API configuration tests. |
| **Priority** | MVP |
| **Traceability** | F-ADM-\* |

### SRS-ADM-002 — Configuration audit

| **Requirement** | Material policy/configuration changes SHALL be versioned or audit-logged with actor/time. |
|----|----|
| **Rationale** | Change accountability. |
| **Verification** | Change policy and inspect audit. |
| **Priority** | MVP |
| **Traceability** | AUD-01 |

### SRS-ADM-003 — No silent retroactive rewrite

| **Requirement** | Vocabulary/template changes SHALL NOT silently rewrite historical analytical meaning. |
|----|----|
| **Rationale** | Preserves historical context. |
| **Verification** | Rename vocabulary and inspect old record semantics. |
| **Priority** | MVP |
| **Traceability** | F-ADM-001 |

# 17. Interoperability and Integration

### SRS-INT-001 — Connector provenance

| **Requirement** | Any external connector SHALL retain provider/source, remote identifier, retrieval timestamp, mapping version, and licence/terms metadata where relevant. |
|----|----|
| **Rationale** | Makes enrichment attributable. |
| **Verification** | Connector fixture import test. |
| **Priority** | P1 except architectural rule |
| **Traceability** | SRC-01 |

### SRS-INT-002 — No silent merge

| **Requirement** | Imported external entity candidates SHALL NOT silently merge into canonical entities solely because an external identifier or fuzzy match is returned. |
|----|----|
| **Rationale** | Prevents external false positives. |
| **Verification** | Import ambiguous candidate and verify review required. |
| **Priority** | P1 except architectural rule |
| **Traceability** | ENT-01 |

### SRS-INT-003 — FollowTheMoney mapping

| **Requirement** | Where implemented, FollowTheMoney import/export SHALL preserve unmapped CS-AML fields and mapping-version metadata. |
|----|----|
| **Rationale** | Maintains interoperability without semantic loss. |
| **Verification** | Round-trip mapping test. |
| **Priority** | P1 except architectural rule |
| **Traceability** | F-INT-003 |

### SRS-INT-004 — Projection connectors

| **Requirement** | Graph/search integrations SHALL be rebuildable and SHALL not own unique canonical analytical facts. |
|----|----|
| **Rationale** | Architectural consistency. |
| **Verification** | Projection rebuild test. |
| **Priority** | P1 except architectural rule |
| **Traceability** | Technology Architecture |

# 18. Deployment and Operations

### SRS-OPS-001 — Containerised/reference deployment

| **Requirement** | A reference deployment SHOULD be reproducible using containerised or equivalent declarative deployment artefacts with environment-specific secrets externalised. |
|----|----|
| **Rationale** | Repeatable operations. |
| **Verification** | Fresh deployment from documentation. |
| **Priority** | MVP |
| **Traceability** | Technology Architecture |

### SRS-OPS-002 — Health endpoints

| **Requirement** | Application services SHALL provide health/readiness indicators that do not reveal case-sensitive content. |
|----|----|
| **Rationale** | Operational monitoring. |
| **Verification** | Health endpoint test. |
| **Priority** | MVP |
| **Traceability** | OPS |

### SRS-OPS-003 — Migration safety

| **Requirement** | Schema migrations SHALL be versioned, reversible where practical, and tested against representative backup data before production application. |
|----|----|
| **Rationale** | Protects canonical records. |
| **Verification** | Migration dry-run/rollback test. |
| **Priority** | MVP |
| **Traceability** | Data Model |

### SRS-OPS-004 — Observability minimisation

| **Requirement** | Metrics/logs/traces SHALL avoid storing evidence bodies, protected-source identity, or other case-sensitive payloads unless explicitly required and protected. |
|----|----|
| **Rationale** | Prevents telemetry leakage. |
| **Verification** | Telemetry inspection. |
| **Priority** | MVP |
| **Traceability** | SEC-02 |

# 19. Verification and Acceptance

Each mandatory requirement SHALL be verifiable by one or more of: automated unit/integration/API test, security test, data-integrity test, UI acceptance test, operational drill, or structured manual review. A requirement is not complete merely because code exists.

| **Code** | **Verification method**                     |
|----------|---------------------------------------------|
| V1       | Automated functional/API test               |
| V2       | Authorization/security negative test        |
| V3       | Data integrity/schema/provenance test       |
| V4       | UI/usability acceptance test                |
| V5       | Operational backup/restore/deployment drill |
| V6       | Structured reviewer sign-off                |

# 20. Traceability Matrix

| **SRS family** | **Upstream product** | **Framework/control** | **Canonical data** | **Primary test** |
|----|----|----|----|----|
| CASE | F-CASE-\* | GOV-01/CAS-01/CAS-02 | Case, Review, AuditEvent | V1/V6 |
| EVD/CLM | F-EVD-\*/F-DOC-001 | SRC-01/SRC-02/EVD-01/EVD-02/QUA-01 | Source, EvidenceItem, EvidenceExtract, Claim, VerificationDecision, Fact | V1/V3/V6 *[v0.1.1 · A10]* |
| ENT/REL/AST | F-ENT-\*/F-REL-\*/F-AST-001 | ENT-01/REL-01/AST-01 | Entity, Relationship, Asset | V1/V3/V4 |
| TIM/VAL | F-TIM-\*/F-VAL-\* | REL-01/VAL-01 | Event, ValueFlow | V1/V3/V4 |
| TYP/HYP/ASM | F-TYP-\*/F-HYP-\*/F-ASM-\* | TYP-01/HYP-01/HYP-02/ASM-01/GAP-01 | Indicator, TypologyMatch, Hypothesis, Assessment | V1/V4/V6 |
| PRD/REV/DIS | F-PRD-\*/F-REV-001/F-DIS-\* | QUA-01/DIS-01/PRI-01 | IntelligenceProduct, Review, Dissemination | V1/V2/V6 |
| SEC/AUD/OPS | F-SEC-\*/F-AUD-001/F-OPS-001 | SEC-01/SEC-02/AUD-01/PRI-02 | AccessPolicy, AuditEvent, BackupRecord | V2/V5 |

# 21. MVP Release Baseline

> **Release gate**  
> MVP 0.1 SHALL NOT be declared production-ready until the end-to-end pilot scenario passes with provenance, authorization, audit, review, and export controls intact.

> **Non-waivable invariants** *[v0.1.1 · A16]*  
> No administrative waiver is possible for a defect that violates: (1) authorization (unauthorized access / authorization bypass); (2) source identity protection; (3) evidence integrity or provenance of material records; (4) certainty preservation — e.g. `RECONSTRUCTED`/`HYPOTHETICAL` shown or stored as `DIRECT`/`DOCUMENTED`, `INSUFFICIENT_BASIS` shown as a level, or a claim treated as fact without a decision; (5) approval gates, including export without approval (SRS-FR-DIS-001); (6) audit history (broken, missing, or editable). If such a defect exists, the only release path is to disable the affected feature path with tested evidence of non-reachability; the defect itself is never waived. Other High defects may be waived only by the accountable authority with a tested compensating control, owner, and expiry date.

- A case can be opened only with accountable owner and valid charter.

- Evidence originals and derivatives are separable and integrity-protected.

- At least one entity merge/unmerge is demonstrated without history loss.

- Ownership/control/asset and mixed-class value flows are represented without semantic collapse.

- At least two competing hypotheses are tested using supporting and contradicting evidence.

- An assessment is confidence-rated and backward traceable to sources.

- A source claim is promoted to a fact through a recorded verification decision, and disputing/superseding that fact flags dependent assessments/products without loss of history. *[v0.1.1 · A10]*

- Independent peer review is completed.

- External export is blocked until dissemination approval.

- Audit trail captures all material actions.

- Backup restore drill succeeds in an isolated environment.

# Annex A — Requirement ID Taxonomy

- SRS-FR-\* Functional requirements

- SRS-DR-\* Data requirements

- SRS-IF-\* External interfaces

- SRS-SEC-\* Security/privacy

- SRS-AUD-\* Audit/provenance

- SRS-NFR-PERF-\* Performance

- SRS-NFR-REL-\* Reliability

- SRS-AN-\* Search/graph/analytics

- SRS-AI-\* AI/automation

- SRS-UX-\* UX/accessibility

- SRS-ADM-\* Administration

- SRS-INT-\* Integration

- SRS-OPS-\* Deployment/operations

# Annex B — State Models

``` text
Case: DRAFT → TRIAGE → ACTIVE → REVIEW → APPROVED/CLOSED → MONITORING → REOPENED
```

``` text
Entity resolution: CANDIDATE → PROBABLE → CONFIRMED | DISPUTED | UNRESOLVED
```

``` text
Intelligence product: DRAFT → IN_REVIEW → CHANGES_REQUESTED → APPROVED → DISSEMINATED → SUPERSEDED/CORRECTED
```

``` text
Hypothesis: OPEN → SUPPORTED | WEAKENED | REJECTED | INCONCLUSIVE
```

``` text
Claim: RECORDED → UNDER_REVIEW → CORROBORATED | CONTRADICTED | UNRESOLVED
Fact:  PROVISIONAL → ESTABLISHED → DISPUTED | SUPERSEDED (superseded_by required)
```

*[v0.1.1 · A10]* Claim/Fact states per SRS-FR-CLM-001…004 (proposed; requires product-owner approval).

# Annex C — API Resource Baseline

- /cases

- /sources

- /evidence

- /evidence-extracts

- /claims, /claims/{claimId}/verification-decisions *[v0.1.1 · A10]*

- /facts (commands: establish, dispute, supersede; dependents) *[v0.1.1 · A10]*

- /entities

- /relationships

- /assets

- /events

- /value-flows

- /indicators

- /typologies

- /hypotheses

- /gaps

- /assessments

- /products

- /reviews

- /disseminations

- /audit-events

- /search

> **API rule**  
> Resource naming is informative; exact REST/GraphQL design may vary. Authorization semantics, stable identifiers, provenance, and uncertainty preservation are normative.

# Annex D — Test Scenario Baseline

1.  Create a high-sensitivity case and charter.

2.  Register two public sources and upload three evidence files; hash originals.

3.  Create evidence extracts and one OCR derivative; record a source claim from an extract and promote it to a `PROVISIONAL` fact via a verification decision. *[v0.1.1 · A10]*

4.  Create two similar company records, evaluate candidate match, merge, then unmerge one test cycle.

5.  Create Person, Company, Property and Contract entities plus ownership/control relationships.

6.  Add timeline events for incorporation, contract award, property acquisition and ownership change.

7.  Create a four-leg value flow containing DIRECT, DOCUMENTED, RECONSTRUCTED and HYPOTHETICAL legs.

8.  Map two indicators and one counter-indicator to a typology.

9.  Create two competing hypotheses and record supporting/contradicting evidence.

10. Create assessment with `MODERATE` confidence and two intelligence gaps; record a disconfirming-search entry before review. *[v0.1.1 · A05, A09]*

11. Generate intelligence product, submit to independent reviewer, address change request, approve.

12. Attempt export before approval (must fail), then approve dissemination and export.

13. Verify sharing log and audit history.

14. Restore the case from backup into isolated environment and verify object/evidence hashes.

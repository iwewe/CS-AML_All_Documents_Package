**CS-AML**

Data Model Specification

Civil Society Anti-Money Laundering & Financial Intelligence Framework

**Version 0.1.3 \| Data Specification (Approved Internal Specification Baseline)**

> **Document status — v0.1.3**
> Version: 0.1.3 — Approved Internal Specification Baseline (2026-10-09, tag v0.1.3-spec). Supersedes v0.1.2 (2026-10-09, tag v0.1.2-spec). *[v0.1.3]*
> Supersedes: CS-AML Data Model Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (v0.1.1) and 2026-10-09 (v0.1.2 and v0.1.3; decision register and release gates in `CHANGELOG.md`). The v0.1.2 and v0.1.3 changes come from change requests raised while implementing increments I1–I4 and I5–I7; this is not an independent audit. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).
> Changes in 0.1.2: change requests CR-I1-01…CR-I4-14 approved by the product owner on 2026-10-09 (`CHANGELOG.md`, section v0.1.2). Each change is tagged `*[v0.1.2 · CR-xx-yy]*`.
> Changes in 0.1.3: change requests CR-I5-01…CR-I7-08 approved by the product owner on 2026-10-09 (`CHANGELOG.md`, section v0.1.3). Each change is tagged `*[v0.1.3 · CR-xx-yy]*`.

> **Status**
>
> This document defines the canonical information model for CS-AML v0.1.1. It is intended to be implementation-neutral and SHALL be used as the authoritative semantic reference for database schemas, APIs, graph stores, analytical tooling, exchange formats, and audit records that claim to implement the CS-AML data model. *[v0.1.1 · A01]*

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Data Model Specification |
| Version | 0.1.3 *[v0.1.3]* |
| Status | Approved Internal Specification Baseline (2026-10-09, tag v0.1.3-spec) *[v0.1.1 · A01]* |
| Applies to | CS-AML Framework v0.1.1 Expanded (`CS-AML_Framework_v0.1.1_Expanded.md`) and derivative implementations *[v0.1.1 · A01]* |
| Primary audience | Framework maintainers, investigators, data architects, software engineers, security/privacy reviewers, assurance reviewers |
| Normative terms | SHALL/MUST = mandatory; SHOULD = recommended; MAY = optional |
| Design objective | Preserve evidentiary provenance, analytical uncertainty, temporal context, and privacy constraints while enabling reusable entity-centric financial intelligence. |

# 1. Purpose and Scope

The purpose of this specification is to define the canonical data structures, semantics, constraints, and lifecycle rules required to represent civil-society financial intelligence under CS-AML. The model is deliberately designed to separate observed information from analytical interpretation and to keep provenance, confidence, and legal/privacy handling attached to the objects they govern.

> **Core design axiom**
>
> Case is context. Entity and Evidence are reusable truth-bearing objects. Analytical conclusions SHALL be represented separately from source material and SHALL remain traceable to the evidence and reasoning that support them.

## 1.1 In scope

- Case and investigation context

- Source and evidence provenance

- Claim, fact, indicator, and analytical proposition

- Entity identity and entity resolution

- Relationships, ownership, control, and affiliation

- Assets and asset attribution

- Events and temporal state

- Direct, documented, reconstructed, and hypothetical value flows

- Typology matches and indicators

- Hypotheses, intelligence gaps, assessments, and confidence

- Intelligence products, review, dissemination, and closure

- Privacy labels, handling restrictions, audit events, and retention metadata

- Implementation mappings for relational and graph-oriented systems

## 1.2 Out of scope

- Bank transaction ingestion protocols

- Formal regulated-entity STR/SAR schemas

- Law-enforcement evidentiary rules for criminal prosecution

- Covert collection or unauthorized access mechanisms

- Automated determinations of criminal guilt

- Vendor-specific database design

# 2. Normative Data Principles

| **ID** | **Principle** | **Normative requirement** |
|----|----|----|
| DM-P01 | Provenance by default | Every substantive evidentiary or analytical object SHALL retain machine-readable provenance to its source, creator, creation time, and applicable verification state. |
| DM-P02 | Separation of observation and inference | Evidence, Fact, Indicator, Hypothesis, and Assessment SHALL be modeled as distinct object classes. Implementations SHALL NOT collapse them into a single notes field. |
| DM-P03 | Temporal truth | Where a statement can change over time, the model SHALL support valid-time boundaries and SHALL avoid treating current state as historically permanent. |
| DM-P04 | Entity reuse | Entities SHALL be reusable across cases. Case membership SHALL be represented as contextual association rather than by duplicating entity records per case. |
| DM-P05 | Identity uncertainty | Entity resolution SHALL support candidate matches, confidence, merge rationale, and reversible decisions. |
| DM-P06 | Value-flow epistemics | Direct, documented, reconstructed, and hypothetical flows SHALL be distinguishable in the data model and in any derived visualization. |
| DM-P07 | Privacy as metadata | Sensitivity, access restrictions, retention, and dissemination limits SHALL be attached to data objects and not only to user-interface screens. |
| DM-P08 | Immutability of originals | Original evidence SHALL be preserved. Corrections and annotations SHALL be additive or versioned; they SHALL NOT silently rewrite the historical record. |
| DM-P09 | No guilt flag | The canonical model SHALL NOT contain a boolean field that declares a person guilty of money laundering or other crime. |
| DM-P10 | Auditability | Material changes to identity, evidence, relationships, assessment, or dissemination state SHALL generate auditable events. |

# 3. Canonical Information Architecture

CS-AML defines a layered information model. The layers are semantic rather than deployment-specific; one implementation MAY use PostgreSQL, a graph database, object storage, or a hybrid architecture, provided the normative semantics are preserved.

``` text
CASE CONTEXT
   |
   +-- SOURCE / EVIDENCE
   |       |
   |       +-- CLAIM / FACT
   |
   +-- ENTITY / RELATIONSHIP / ASSET / EVENT
   |       |
   |       +-- VALUE FLOW
   |
   +-- INDICATOR / TYPOLOGY MATCH
   |       |
   |       +-- HYPOTHESIS / INTELLIGENCE GAP
   |
   +-- ASSESSMENT
           |
           +-- INTELLIGENCE PRODUCT
                   |
                   +-- REVIEW / DISSEMINATION / CLOSURE
```

## 3.1 Canonical object families

| **Family** | **Canonical objects** |
|----|----|
| Context | Case, CaseEntity, CaseRole, InvestigationQuestion, ScopeChange |
| Evidence | Source, EvidenceItem, EvidenceExtract, Claim, Fact, VerificationDecision *[v0.1.1 · A10]* |
| Knowledge graph | Entity, ResolutionDecision, PersonProfile, OrganizationProfile, AccountProfile, Asset, Relationship, Event, Location *[v0.1.1 · ER]* |
| Financial analysis | ValueFlow, ValueFlowLeg, OwnershipInterest, ControlAssertion, AssetAttribution |
| Analytical | Indicator, TypologyMatch, Hypothesis, HypothesisEvidenceLink, IntelligenceGap, Assessment |
| Product & assurance | IntelligenceProduct, Review, Dissemination, ClosureRecord |
| Governance | DataClassification, AccessLabel, RetentionRule, AuditEvent, VersionRecord |

# 4. Common Object Envelope

All canonical objects SHALL expose a minimum common envelope. Implementations MAY extend this envelope but SHALL NOT redefine the meaning of the normative fields.

| **Field** | **Type** | **Cardinality** | **Meaning** |
|----|----|----|----|
| id | UUID/string | Required | Globally unique immutable object identifier. |
| object_type | enum | Required | Canonical class name. |
| schema_version | string | Required | Schema version under which object was created/validated. |
| created_at | datetime | Required | System creation timestamp. |
| created_by | principal-id | Required | Human or service principal responsible for creation. |
| updated_at | datetime | Required | Last material update timestamp. |
| status | enum | Required | Lifecycle status appropriate to object class. Classes with their own lifecycle mirror it; classes without one use registry enum envelope_status (REGISTERED, RECORDED, DRAFT, FINALIZED; Annex A). *[v0.1.2 · CR-I2-03, CR-I3-05, CR-I4-09]* |
| classification | enum | Required | Information sensitivity classification (Section 16; `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`). Unknown or missing values fail closed. *[v0.1.1 · A08]* |
| access_labels | array | Conditional | Attribute-based handling labels. |
| case_links | array\<case-id\> | Conditional | Contextual case associations; not ownership. Required (1..20) when creating case-context objects (Section 7.1). *[v0.1.2 · CR-I2-01, CR-I3-13, CR-I4-12]* |
| provenance_refs | array\<id\> | Conditional | Links to source/evidence/provenance objects. |
| confidence | object | Conditional | Confidence object where analytical uncertainty exists. |
| valid_from | datetime/date | Optional | Beginning of real-world validity. |
| valid_to | datetime/date | Optional | End of real-world validity. |
| record_version | integer | Required | Monotonic version number for optimistic concurrency/audit. |
| deleted_at | datetime | Optional | Soft-delete/tombstone marker where policy permits. |

## 4.1 Wire enumeration convention

All controlled enumerations on the wire (database values, API payloads, exports) SHALL use UPPER_SNAKE_CASE values as listed in the field tables of this specification and in Annex A, which together form the controlled-enumeration registry. Display labels are separate, translatable presentation strings and SHALL NOT be stored or exchanged in place of wire values. Enumeration lists in other CS-AML documents derive from this registry. *[v0.1.1 · A09]*

# 5. Identifier and Naming Standard

Object identifiers SHALL be opaque and SHALL NOT encode sensitive real-world identifiers, names, or conclusions. Human-readable display codes MAY be assigned separately.

| **Object** | **Prefix example** | **Canonical ID** | **Human display code** |
|------------|--------------------|------------------|------------------------|
| Case       | CASE               | UUID             | CSAML-CASE-2026-001    |
| Entity     | ENT                | UUID             | ENT-000145             |
| Evidence   | EVD                | UUID             | EVD-000381             |
| Hypothesis | HYP                | UUID             | HYP-006                |
| Assessment | ASS                | UUID             | ASS-003                |

# 6. Context and Case Objects

## 6.1 Case

Represents the bounded investigative context in which questions, scope, risks, analytical objects, and products are managed. A Case SHALL NOT own reusable entities or evidence; it SHALL link to them.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| title | string | Y | 1 | Neutral descriptive title. |
| case_code | string | Y | 1 | Human-readable identifier. |
| purpose | text | Y | 1 | Legitimate investigative purpose. |
| investigation_questions | ref\[\] | Y | 0..n | Questions to be answered. MAY be empty while the case is DRAFT; at least one question is a precondition of case activation (gate), not of the stored record or API response. *[v0.1.2 · CR-I1-01]* |
| jurisdictions | code\[\] | N | 0..n | Relevant jurisdictions. |
| time_scope | interval | N | 0..1 | Primary period under review. |
| lead_analyst | principal | Y | 1 | Accountable analyst. |
| risk_rating | enum | Y | 1 | Operational/harm risk rating; registry enum risk_rating: LOW, MEDIUM, HIGH, CRITICAL (ordered; minimal set defined in v0.1.2). *[v0.1.2 · CR-I1-08]* |
| closure_reason | enum | N | 0..1 | Reason case closed; registry enum closure_reason: OBJECTIVES_MET, INSUFFICIENT_BASIS_TO_CONTINUE, REFERRED, OUT_OF_SCOPE, DUPLICATE, LEGAL_OR_SAFETY_CONSTRAINT, OTHER (minimal set defined in v0.1.2). *[v0.1.2 · CR-I1-08]* |
| closed_at | datetime | N | 0..1 | Time the case entered CLOSED; null otherwise (set by the lifecycle, read-only for clients). The retention trigger CASE_CLOSURE (Section 16.1) uses it. *[v0.1.3 · CR-I7-06]* |

### Normative rules:

- Case SHALL contain a documented legitimate purpose before collection begins.

- Case title SHALL avoid presuming criminality.

- Case closure SHALL NOT delete reusable entity or evidence objects.

- A case SHALL NOT be activated (gate transition to ACTIVE) without at least one InvestigationQuestion (SRS-FR-CASE-001). *[v0.1.2 · CR-I1-01]*

- Only the case LEAD (Section 6.3) MAY change the classification or access labels of a Case, and only as an upgrade (higher classification, added labels). Downgrades and label removal SHALL require a recorded reviewer decision; until that workflow exists (increment I6, with review) they SHALL be rejected (403). Every change SHALL generate an AuditEvent. *[v0.1.2 · CR-I1-09]* The reviewer decision is an approved HANDLING_CHANGE review recorded as a HandlingChange (Section 16.4); a direct PATCH downgrade stays 403. *[v0.1.3 · CR-I6-12]*

### Lifecycle states:

``` text
DRAFT -> AUTHORIZED -> ACTIVE -> REVIEW -> CLOSED -> MONITORING -> REOPENED
```

## 6.2 InvestigationQuestion

Represents a testable analytical question that constrains scope and prevents open-ended surveillance.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| case_id | ref | Y | 1 | Parent case context. |
| question | text | Y | 1 | Neutral question. |
| priority | enum | Y | 1 | Analytical priority. |
| status | enum | Y | 1 | OPEN, ANSWERED, RETIRED *[v0.1.1 · A09]* |
| answer_summary | text | N | 0..1 | Short evidence-linked answer. |

### Normative rules:

- Questions SHOULD be framed to permit both incriminating and exculpatory answers.

## 6.3 CaseMembership *[v0.1.2 · CR-I1-02]*

Explicit, revocable grant of a principal to a case (SRS-FR-SEC-002). Access to case work is defined through case membership.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| id | ref | Y | 1 | Membership identifier. |
| case | ref | Y | 1 | Case. |
| principal | principal | Y | 1 | Member. |
| role | enum | Y | 1 | LEAD, ANALYST, REVIEWER (registry enum case_membership_role). |
| protected_source_authorized | boolean | Y | 1 | Explicit per-case grant to see SOURCE_PROTECTED material; effective only together with the protected-source eligibility role (Section 16). Defaults to false. |
| granted_by | principal | Y | 1 | Granting principal. |
| granted_at | datetime | Y | 1 | Grant time. |
| revoked_at | datetime | N | 0..1 | Revocation time (soft revocation). |
| revoked_by | principal | N | 0..1 | Revoking principal. |

### Normative rules:

- A principal SHALL have at most one active (non-revoked) membership per case, and every case SHALL have exactly one active LEAD membership. *[v0.1.2 · CR-I1-02]*

- Memberships SHALL be managed by the case LEAD. Revocation SHALL be soft (revoked_at), so access history stays reconstructable; the LEAD membership cannot be revoked, the lead is changed through the case. Every grant, change and revocation SHALL generate an AuditEvent. *[v0.1.2 · CR-I1-02]*

- LEAD is the case owner / investigation lead; REVIEWER and LEAD memberships qualify a principal as reviewer for fact establishment and merge/unmerge (Sections 7.5, 8.4). *[v0.1.2 · CR-I1-02, CR-I2-11]*

# 7. Source, Evidence, Claim, and Fact Model

## 7.1 Source

Represents the origin or provider of information. A Source describes where information came from; it is not itself the extracted evidentiary proposition.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| source_type | enum | Y | 1 | REGISTRY, COURT_RECORD, MEDIA, WHISTLEBLOWER, WEBSITE, DATASET, DOCUMENT, INTERVIEW, OTHER *[v0.1.1 · A09]* |
| publisher_or_origin | string | N | 0..1 | Originating organization/person. |
| locator | uri/string | N | 0..1 | URL, archival location, or repository reference. |
| accessed_at | datetime | Y | 1 | Collection/access time. |
| publication_date | date | N | 0..1 | When published/issued. |
| reliability_grade | enum | N | 0..1 | A-F source reliability. |
| lawful_access_basis | text/enum | Y | 1 | Why collection/use is permitted. |
| archive_ref | ref | N | 0..1 | Preserved snapshot or evidence item. |

### Normative rules:

- Source reliability SHALL be separated from credibility of individual information items.

- Anonymous sources SHALL NOT be treated as inherently unreliable; uncertainty SHALL be recorded explicitly.

- Source and EvidenceExtract have no lifecycle; their envelope status is REGISTERED (registry enum envelope_status). *[v0.1.2 · CR-I2-03]*

- Every case-context object (Source, EvidenceItem, Entity, Relationship, Asset, OwnershipInterest, ControlAssertion, Event, ValueFlow, Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment, IntelligenceProduct) SHALL be created with 1..20 case links; the creator needs update rights on every named case. An object without case context would be reachable by no one. Extracts and derivatives inherit the links of their parent; claims, facts and decisions belong to the case of their path. *[v0.1.2 · CR-I2-01, CR-I3-13, CR-I4-12]*

## 7.2 EvidenceItem

Represents a preserved evidentiary object such as a file, page image, registry record, transcript, screenshot, export, or structured record.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| source_id | ref | Y | 1 | Origin source. |
| evidence_type | enum | Y | 1 | DOCUMENT, IMAGE, RECORD, TRANSCRIPT, DATASET_ROW, WEB_SNAPSHOT, OTHER *[v0.1.1 · A09]* |
| content_hash | string | Y\* | 0..1 | SHA-256 or equivalent where bytes are available. |
| storage_ref | uri/ref | Y | 1 | Controlled storage location. Exposed only as an opaque reference (`evidence:<id>`); bucket and key are never disclosed. *[v0.1.2 · CR-I2-06]* |
| acquired_at | datetime | Y | 1 | Acquisition time. |
| acquired_by | principal | Y | 1 | Collector. |
| original_format | string | N | 0..1 | MIME/type. |
| verification_status | enum | Y | 1 | UNVERIFIED, SOURCE_VERIFIED, INDEPENDENTLY_CORROBORATED, DISPUTED *[v0.1.1 · A09]* |
| redaction_state | enum | Y | 1 | NONE, WORKING_REDACTION, PUBLICATION_REDACTION *[v0.1.1 · A09]* |
| byte_size | integer | N | 0..1 | Size of the original bytes. *[v0.1.2 · CR-I2-06]* |
| hash_algorithm | string | N | 0..1 | Algorithm of content_hash (e.g. SHA-256). *[v0.1.2 · CR-I2-06]* |
| derived_from | ref | N | 0..1 | Parent EvidenceItem of a derivative. *[v0.1.2 · CR-I2-06]* |
| derivation_type | text | N | 0..1 | Kind of derivative (redaction, OCR text, …); free text in v0.1.2. *[v0.1.2 · CR-I2-06]* |

### Normative rules:

- Original evidence bytes SHALL be immutable after registration except for controlled preservation migrations.

- Derived/redacted copies SHALL be linked to the original by derivation relationship.

### Lifecycle states:

``` text
COLLECTED -> REGISTERED -> VERIFIED -> SUPERSEDED -> RESTRICTED
```

## 7.3 EvidenceExtract

Represents the precise portion of EvidenceItem used analytically.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| evidence_id | ref | Y | 1 | Parent evidence. |
| locator | string | Y | 1 | Page, paragraph, timecode, row, bounding region, or equivalent. |
| extract_text | text | N | 0..1 | Verbatim/normalized extract when lawful. |
| extract_hash | string | N | 0..1 | Integrity value for extracted content. |
| analyst_note | text | N | 0..1 | Context note; SHALL remain distinguishable from extract. |

## 7.4 Claim

Represents a proposition asserted by a source or person. A Claim is not automatically accepted as fact. A Claim is a permanent record of what a source asserts; it is never converted into, upgraded to, or overwritten by a Fact. *[v0.1.1 · A10]*

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| subject_refs | ref\[\] | Y | 1..n | Entities/events referenced. |
| predicate | string | Y | 1 | Controlled or human-readable predicate. |
| object_value | variant | Y | 1 | Claimed value/entity. |
| evidence_extract_refs | ref\[\] | Y | 1..n | Supporting extracts. |
| claimant | ref/string | N | 0..1 | Who makes the assertion. |
| credibility_grade | enum | N | 0..1 | 1-6 information credibility; registry enum credibility_grade (INDEPENDENTLY_CONFIRMED, PROBABLY_TRUE, POSSIBLY_TRUE, DOUBTFUL, IMPROBABLE, CANNOT_BE_JUDGED) whose wire values are the digit codes "1"…"6" (registry exception). *[v0.1.2 · CR-I2-08]* |
| claim_status | enum | Y | 1 | RECORDED, UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED *[v0.1.1 · A10]* |
| disputed | boolean | Y | 1 | Whether contested. Retained for compatibility; derived as true when claim_status = CONTRADICTED or an open dispute exists. *[v0.1.1 · A10]* |

### Normative rules:

- Claims SHALL preserve attribution.

- A Fact SHALL NOT be created on the basis of a source assertion solely because it appears in an official document if the document merely records a third-party allegation. *[v0.1.1 · A10]*

- The recorded assertion of a Claim (subject, predicate, object value, claimant, evidence extracts) SHALL NOT be overwritten by analyst conclusions. Analytical outcomes are recorded as VerificationDecision objects (Section 7.6) and reflected in claim_status. *[v0.1.1 · A10]*

### Lifecycle states: *[v0.1.1 · A10]*

``` text
RECORDED -> UNDER_REVIEW -> CORROBORATED | CONTRADICTED | UNRESOLVED
```

Every transition out of RECORDED SHALL be backed by a VerificationDecision. *[v0.1.1 · A10]*

A decided claim (CORROBORATED, CONTRADICTED or UNRESOLVED) MAY return to UNDER_REVIEW through a further VerificationDecision; earlier decisions are kept. Any other transition SHALL be rejected (409). Claim decisions MAY be recorded by members with role LEAD, ANALYST or REVIEWER (Section 6.3). *[v0.1.2 · CR-I2-11]*

## 7.5 Fact

Represents a proposition accepted by the investigation as established to the stated confidence threshold. A Fact is a separate analytical object supported by one or more evidence items (mandatory), optionally by one or more Claims, and by one or more VerificationDecisions; it is not produced by transforming a Claim. *[v0.1.1 · A10]* *[v0.1.1 · C02]*

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| proposition | text/structured | Y | 1 | Established proposition. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence supporting acceptance; EvidenceItem or EvidenceExtract only, readable by the creator and in the case context (422 otherwise). *[v0.1.2 · CR-I2-07]* |
| contradicting_evidence | ref\[\] | N | 0..n | Known contradictory material. |
| supporting_claim_refs | ref\[\] | N | 0..n | Claims that support the fact, if any. The Claims remain unchanged. *[v0.1.1 · A10]* |
| fact_status | enum | Y | 1 | PROVISIONAL, ESTABLISHED, DISPUTED, SUPERSEDED *[v0.1.1 · A09, A10]* |
| verification_decision_refs | ref\[\] | Y | 1..n | VerificationDecision records that created and revised the fact (append-only history). Server-populated and read-only: the CREATE decision is written atomically with the Fact, and each later fact command appends its decision. *[v0.1.1 · A10]* *[v0.1.1 · C01]* |
| proposed_by | principal | Y | 1 | Principal who proposed the fact. *[v0.1.1 · A10]* |
| superseded_by | ref | Y\* | 0..1 | Replacement Fact; required when fact_status = SUPERSEDED. *[v0.1.1 · A10]* |
| valid_time | interval | N | 0..1 | When proposition is true in real world. |
| confidence | confidence | Y | 1 | Analytical confidence. |

### Normative rules:

- Fact status SHALL be revisable when materially new evidence emerges.

- Fact objects SHALL NOT encode legal guilt or criminal liability unless directly quoting an authoritative adjudication, in which case attribution SHALL be explicit.

### Claim and Fact lifecycle rules *[v0.1.1 · A10]*

> **Approved by product owner, 2026-10-08.** The rules below and Section 7.6 were added in v0.1.1 to close audit finding A10. *[v0.1.1 · A10]*

- **Fact creation.** A Fact SHALL be created only with (a) one or more evidence references (supporting_evidence, mandatory, 1..n), optionally one or more supporting claim references (supporting_claim_refs, 0..n), and (b) a decision rationale. The system SHALL create the Fact and its CREATE VerificationDecision atomically in the same transaction; the CREATE decision targets the new Fact, and neither record SHALL exist without the other. *[v0.1.1 · C01]* *[v0.1.1 · C02]* A newly created Fact SHALL start as PROVISIONAL. Creating a Fact SHALL NOT modify, convert, or close the supporting Claims. A Claim SHALL NOT be treated as a Fact without such a decision. *[v0.1.1 · A10]*

- **Who may act.** An Investigator/Analyst MAY record Claims and propose PROVISIONAL Facts. Moving a Fact to ESTABLISHED SHALL require a Reviewer who is not the proposer; a Reviewer is a principal with REVIEWER or LEAD membership on the fact's case (403 otherwise, and always 403 for the proposer). *[v0.1.2 · CR-I2-11]* Any authorized case member MAY move a Fact to DISPUTED with supporting evidence. Moving a Fact to SUPERSEDED SHALL require a reference to the replacement Fact (superseded_by). *[v0.1.1 · A10]*

- **Revision.** Every status change SHALL be recorded as a new VerificationDecision; earlier decisions and prior states SHALL be preserved. *[v0.1.1 · A10]* The ESTABLISH, DISPUTE and SUPERSEDE decisions SHALL be created atomically with the corresponding status change by the fact command itself. *[v0.1.1 · C01]*

- **Dependent flagging.** When a Fact becomes DISPUTED or SUPERSEDED, every dependent Assessment and IntelligenceProduct SHALL be flagged `review_required` with a link to the triggering VerificationDecision (`review_trigger_ref`). Published or disseminated products SHALL NOT be mutated; a correction review task SHALL be created instead. History SHALL be preserved. *[v0.1.1 · A10]*

- **Indirect dependents.** Flagging SHALL cover direct dependents (the Fact in supporting_refs) and indirect ones: Indicators whose evidence includes the Fact, TypologyMatches citing such Indicators, and Hypotheses with a SUPPORTS matrix cell on such an object, together with the Assessments and products depending on them. Drafts and finalized objects are flagged alike; the recorded judgement is not changed. A flagged draft SHALL NOT be finalized (409 REVIEW_REQUIRED); clearing review_required is a review action (I6). The dependents listing SHALL show only dependents the caller may read. *[v0.1.2 · CR-I4-11]*

Fact lifecycle: *[v0.1.1 · A10]*

``` text
PROVISIONAL -> ESTABLISHED
PROVISIONAL | ESTABLISHED -> DISPUTED
PROVISIONAL | ESTABLISHED | DISPUTED -> SUPERSEDED (superseded_by required)
```

## 7.6 VerificationDecision *[v0.1.1 · A10]*

Represents a single, append-only verification outcome on a Claim or Fact (for example: claim corroborated or contradicted; fact created, established, disputed, or superseded). *[v0.1.1 · A10]*

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| target_ref | ref | Y | 1 | Claim or Fact the decision applies to. |
| decision | enum | Y | 1 | Outcome; for Claims a claim_status value (UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED); for Facts a fact action (CREATE, ESTABLISH, DISPUTE, SUPERSEDE). CREATE (display label "Create fact") records the decision that creates a Fact supported by the referenced evidence (and claims, if any); it does not convert or alter any Claim. *[v0.1.1 · A10]* For Facts, decisions are never created on their own: CREATE is written atomically with the new Fact, and ESTABLISH/DISPUTE/SUPERSEDE atomically with the fact command. *[v0.1.1 · C01]* |
| rationale | text | Y | 1 | Reasoning for the decision. |
| evidence_refs | ref\[\] | Y | 1..n | Evidence or extracts relied on; EvidenceItem or EvidenceExtract only, readable and in the case context (422 otherwise). *[v0.1.2 · CR-I2-07]* |
| decided_by | principal | Y | 1 | Decision maker. |
| decided_at | datetime | Y | 1 | Decision time. |
| review_ref | ref | N | 0..1 | Related Review, if any. |

### Normative rules:

- VerificationDecision records SHALL be append-only; a mistaken decision is corrected by a later decision, not by editing or deleting the earlier one.

- A decision moving a Fact to ESTABLISHED SHALL have decided_by different from the Fact's proposed_by.

- Each VerificationDecision SHALL generate an AuditEvent.

# 8. Entity and Identity Model

## 8.1 Entity

Canonical identity-bearing node used across cases.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_type | enum | Y | 1 | PERSON, ORGANIZATION, ACCOUNT, ADDRESS, DOMAIN, PHONE, EMAIL, WALLET, PROPERTY, VEHICLE, VESSEL, AIRCRAFT, CONTRACT, PROJECT, OTHER *[v0.1.1 · A09]* |
| primary_name | string | Y | 1 | Preferred display label. |
| aliases | string\[\] | N | 0..n | Alternative labels. |
| identifiers | identifier\[\] | N | 0..n | Typed external identifiers. |
| resolution_status | enum | Y | 1 | UNRESOLVED, RESOLVED, CONFLICTED, MERGED, SPLIT *[v0.1.1 · A09]* |
| resolution_confidence | confidence | N | 0..1 | Identity match confidence. |
| canonical_parent | ref | N | 0..1 | Target if merged; set from the surviving_entity_ref of the MERGE ResolutionDecision (Section 8.4). *[v0.1.1 · ER]* |
| source_refs | ref\[\] | Y | 1..n | Sources establishing identity. |

### Normative rules:

- Names SHALL NOT be treated as unique identifiers.

- A merged entity SHALL retain links to precursor records and merge rationale.

- Implementations SHALL support reversing a mistaken merge without losing history.

- resolution_status is entity state. It SHALL change only as the effect of a ResolutionDecision (Section 8.4); decisions about pairs or sets of records are not stored in resolution_status. *[v0.1.1 · ER]*

## 8.2 PersonProfile

Extension of Entity for natural persons. Sensitive attributes SHALL only be stored when relevant and lawful.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_id | ref | Y | 1 | Base Entity. |
| birth_date | date/partial | N | 0..1 | Known/partial DOB. |
| nationalities | code\[\] | N | 0..n | Known nationalities. |
| occupation | string\[\] | N | 0..n | Relevant occupation/role. |
| public_official_status | enum | N | 0..1 | NONE, CURRENT, FORMER, UNKNOWN; not equivalent to suspicion. *[v0.1.1 · A09]* |
| sensitive_attribute_notes | restricted text | N | 0..1 | Only if strictly necessary and lawful. |

### Normative rules:

- Protected characteristics SHALL NOT be used as AML indicators by themselves.

## 8.3 OrganizationProfile

Extension for companies, NGOs, agencies, trusts, partnerships, and other organized bodies.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_id | ref | Y | 1 | Base Entity. |
| organization_type | enum | Y | 1 | COMPANY, NGO, GOVERNMENT, TRUST, PARTNERSHIP, ASSOCIATION, OTHER *[v0.1.1 · A09]* |
| registration_number | string | N | 0..1 | Legal registration identifier. |
| registration_jurisdiction | code | N | 0..1 | Jurisdiction. |
| incorporation_date | date | N | 0..1 | Formation date. |
| dissolution_date | date | N | 0..1 | If dissolved. |
| registered_address | ref | N | 0..1 | Address entity. |

## 8.4 ResolutionDecision *[v0.1.1 · ER]*

Append-only record of a decision about whether two or more Entity records refer to the same real-world subject. Separates decisions about pairs/sets of records from the state of each Entity. Approved by product owner, 2026-10-08.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| subject_entity_refs | ref\[\] | Y | 2..n | Entity records compared. |
| decision | enum | Y | 1 | MERGE, KEEP_SEPARATE, POSSIBLE_MATCH, DEFER, UNMERGE |
| surviving_entity_ref | ref | C | 0..1 | Required for MERGE. |
| reverses_decision_ref | ref | C | 0..1 | Required for UNMERGE (the MERGE decision being reversed). |
| matching_attributes | structured\[\] | N | 0..n | Attributes that agree. |
| conflicting_attributes | structured\[\] | N | 0..n | Attributes that disagree. |
| evidence_refs | ref\[\] | Y | 1..n | Evidence considered; EvidenceExtract, EvidenceItem or Source, readable and in the case context (422 otherwise). *[v0.1.2 · CR-I2-07]* |
| confidence | confidence | Y | 1 | Confidence object (HIGH, MODERATE, LOW, INSUFFICIENT_BASIS + basis; Section 14.1). |
| rationale | text | Y | 1 | Why the decision was made. |
| decided_by | principal | Y | 1 | Decision maker. |
| decided_at | datetime | Y | 1 | Decision time. |
| reviewer_ref | principal | C | 0..1 | Required for every MERGE and UNMERGE (all are high-impact in the MVP); a principal with REVIEWER or LEAD membership on the case of every subject entity (422 otherwise); SHALL differ from decided_by (409 STATE_CONFLICT). *[v0.1.2 · CR-I2-10, CR-I2-09]* |

### Normative rules:

- ResolutionDecision records SHALL be append-only; a mistaken decision is corrected by a later decision (for example UNMERGE reversing a MERGE), not by editing or deleting the earlier one.

- Effects on Entity state: MERGE → each absorbed record becomes MERGED with canonical_parent = surviving_entity_ref, and the survivor becomes RESOLVED; UNMERGE → restored records become SPLIT; nothing is re-attributed (see the logical-repointing rule below); POSSIBLE_MATCH → a candidate link is recorded with no state change; KEEP_SEPARATE → no state change, and the same pair SHALL NOT be re-suggested unless new evidence is attached; DEFER → state stays or becomes UNRESOLVED.

- Each ResolutionDecision SHALL generate an AuditEvent (action MERGE for MERGE, SPLIT for UNMERGE, otherwise UPDATE).

- Merge is logical repointing (canonical model): absorbed records point to the survivor through canonical_parent, and relationships, claims and absorbed records are never rewritten. UNMERGE therefore needs no re-attribution: it removes what the merge added to the survivor and restores the survivor's prior handling. *[v0.1.2 · CR-I2-13]*

- Every MERGE and UNMERGE is high-impact in the MVP and requires a reviewer_ref distinct from the decider. *[v0.1.2 · CR-I2-10]*

# 9. Relationship, Ownership, and Control Model

## 9.1 Relationship

Represents a typed, evidence-linked edge between entities. Relationships are first-class objects because their source, time, and confidence may differ.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| from_entity | ref | Y | 1 | Origin node. |
| relationship_type | enum | Y | 1 | Typed semantic relationship. |
| to_entity | ref | Y | 1 | Target node: an Entity, or an Asset (the response states to_object_type). *[v0.1.2 · CR-I3-08]* |
| directionality | enum | Y | 1 | DIRECTED, SYMMETRIC *[v0.1.1 · A09]* |
| valid_from | date/datetime | N | 0..1 | Relationship start. |
| valid_to | date/datetime | N | 0..1 | Relationship end. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence: EvidenceExtract, EvidenceItem or Fact, readable and in the case context (422 otherwise). *[v0.1.2 · CR-I2-07]* |
| confidence | confidence | Y | 1 | Confidence; confidence.basis carries the basis of the relationship (DM-I06). *[v0.1.2 · CR-I2-15]* |
| relationship_status | enum | Y | 1 | ASSERTED, ESTABLISHED, DISPUTED, SUPERSEDED *[v0.1.1 · A09]* |

### Normative rules:

- Edges in a graph visualization SHALL retain their evidence links in the underlying model.

- A relationship based only on co-occurrence SHALL NOT be mislabeled as control, ownership, or financial transfer.

- A Relationship created directly MAY target an Asset only with type USES, MANAGES or ACQUIRED. OWNS, BENEFICIAL_OWNER_OF and CONTROLS to an Asset SHALL be created only together with an OwnershipInterest or ControlAssertion (422 otherwise). *[v0.1.2 · CR-I3-08]*

## 9.2 OwnershipInterest

Specialized relationship for legal or beneficial ownership.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| owner_entity | ref | Y | 1 | Owner/beneficial owner. |
| owned_entity_or_asset | ref | Y | 1 | Company/share/asset. |
| ownership_type | enum | Y | 1 | LEGAL, BENEFICIAL, ECONOMIC_INTEREST, NOMINEE_ASSERTED *[v0.1.1 · A09]* |
| percentage | decimal | N | 0..1 | 0-100 if known. |
| basis | text/enum | Y | 1 | Registry, filing, court record, reconstruction, etc. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence. |
| confidence | confidence | Y | 1 | Confidence. |

### Normative rules:

- Legal ownership and beneficial ownership SHALL be stored as distinct types.

- Nominee or beneficial ownership inferred from public-source patterns SHALL be marked as inferred/asserted, not established, unless evidence supports establishment.

- An OwnershipInterest of type BENEFICIAL, ECONOMIC_INTEREST or NOMINEE_ASSERTED SHALL become ESTABLISHED only when its supporting_evidence includes an ESTABLISHED Fact (422 otherwise). *[v0.1.2 · CR-I3-11]*

- OwnershipInterest (interest_status) and ControlAssertion (assertion_status) use the relationship_status values ASSERTED, ESTABLISHED, DISPUTED, SUPERSEDED; their envelope status mirrors that value. Supporting evidence: EvidenceExtract, EvidenceItem or Fact. A ControlAssertion's controlled_entity MAY be an Asset. *[v0.1.2 · CR-I3-05, CR-I3-01]*

## 9.3 ControlAssertion

Represents control that may exist without formal ownership.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| controller | ref | Y | 1 | Person/entity exercising control. |
| controlled_entity | ref | Y | 1 | Target. |
| control_basis | enum\[\] | Y | 1..n | VOTING, APPOINTMENT, FINANCING, CONTRACTUAL, OPERATIONAL, FAMILY_PROXY, OTHER *[v0.1.1 · A09]* |
| control_level | enum | N | 0..1 | MINOR, SIGNIFICANT, DOMINANT, UNKNOWN *[v0.1.1 · A09]* |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence. |
| confidence | confidence | Y | 1 | Confidence. |

# 10. Asset and Event Model

## 10.1 Asset

Represents an item or right with economic value.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| asset_type | enum | Y | 1 | PROPERTY, VEHICLE, VESSEL, AIRCRAFT, SECURITY, COMPANY_SHARE, CRYPTO_ASSET, PRECIOUS_METAL, LUXURY_GOOD, INTELLECTUAL_PROPERTY, OTHER *[v0.1.1 · A09]* |
| description | text | Y | 1 | Neutral description. |
| legal_owner | ref | N | 0..1 | Known legal owner. |
| beneficial_owner_assertions | ref\[\] | N | 0..n | OwnershipInterest refs. |
| controller_refs | ref\[\] | N | 0..n | Control assertions. |
| valuation | money/range | N | 0..1 | Value or range. |
| valuation_date | date | N | 0..1 | Valuation date. |
| valuation_basis | text | C | 0..1 | Registry, market estimate, appraisal, reported value. Free text in v0.1.2 (vocabulary deferred); required when a valuation is given. *[v0.1.2 · CR-I3-06]* |
| location_ref | ref | N | 0..1 | Location entity. |

### Normative rules:

- Observed use or association SHALL NOT be represented as ownership without an ownership basis.

- Asset has no lifecycle; its envelope status is REGISTERED. Asset evidence: Source, EvidenceItem or EvidenceExtract. *[v0.1.2 · CR-I3-05, CR-I3-01]*

## 10.2 Event

Represents a temporally bounded occurrence involving one or more entities.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| event_type | enum | Y | 1 | INCORPORATION, APPOINTMENT, RESIGNATION, CONTRACT_AWARD, ACQUISITION, DISPOSAL, TRANSFER, COURT_EVENT, PAYMENT_EVENT, PUBLICATION, OTHER *[v0.1.1 · A09]* |
| description | text | N | 0..1 | Neutral description. *[v0.1.2 · CR-I3-02]* |
| start_time | datetime/date | Y\* | 0..1 | Start/occurrence; null only when time_precision = UNKNOWN (unknown dates, Methodology §14.2). *[v0.1.2 · CR-I3-06]* |
| time_precision | enum | Y | 1 | DATETIME, DAY, MONTH, YEAR, RANGE, UNKNOWN (registry enum temporal_precision); the string shape SHALL match the precision. *[v0.1.2 · CR-I3-06]* |
| approximate | boolean | N | 0..1 | Marks an approximate date. *[v0.1.2 · CR-I3-02]* |
| end_time | datetime/date | N | 0..1 | End if interval. |
| participant_refs | ref\[\] | Y | 1..n | Entities participating. |
| asset_refs | ref\[\] | N | 0..n | Assets involved. *[v0.1.2 · CR-I3-02]* |
| location_ref | ref | N | 0..1 | Location. |
| evidence_refs | ref\[\] | Y | 1..n | Supporting evidence: EvidenceExtract, EvidenceItem or Fact. *[v0.1.2 · CR-I3-10]* |
| confidence | confidence | Y | 1 | Confidence. |

### Normative rules:

- Event has no stored lifecycle in v0.1.2; its envelope status is RECORDED. The Methodology §14.1 event statuses (confirmed / probable / possible / disputed) are not registered and are deferred to v0.2. *[v0.1.2 · CR-I3-05]*

# 11. Value-Flow Model

> **Mandatory distinction**
>
> Every ValueFlow SHALL carry an epistemic class: DIRECT, DOCUMENTED, RECONSTRUCTED, or HYPOTHETICAL. Systems SHALL preserve this distinction in storage, APIs, exports, and visualizations.

## 11.1 ValueFlow

Represents movement, conversion, allocation, or inferred transfer of economic value.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| flow_class | enum | Y | 1 | DIRECT, DOCUMENTED, RECONSTRUCTED, HYPOTHETICAL *[v0.1.1 · A09]* |
| flow_type | enum | Y | 1 | PAYMENT, CONTRACT, SUBCONTRACT, LOAN, INVESTMENT, ASSET_PURCHASE, ASSET_SALE, GRANT, DONATION, DIVIDEND, CRYPTO_TRANSFER, VALUE_CONVERSION, OTHER *[v0.1.1 · A09]* |
| origin_ref | ref | Y | 1 | Origin entity/asset/event. |
| destination_ref | ref | Y | 1 | Destination entity/asset/event. |
| amount | money/range | N | 0..1 | Known/estimated amount. |
| currency | code | N | 0..1 | Currency if monetary. |
| occurred_at | datetime/date/interval | N | 0..1 | Temporal scope. |
| evidence_refs | ref\[\] | Y\* | 0..n | Required for direct/documented/reconstructed. |
| reconstruction_basis | text | Y\* | 0..1 | Required for reconstructed/hypothetical. |
| confidence | confidence | Y | 1 | Confidence. |
| disclaimer | text | N | 0..1 | Required presentation caveat if needed. |

### Normative rules:

- DIRECT flows require evidence of the actual movement of value.

- DOCUMENTED flows require an authoritative or transactional document evidencing a transfer/obligation but not necessarily settlement.

- RECONSTRUCTED flows SHALL identify the inferential steps linking origin and destination.

- HYPOTHETICAL flows SHALL never be included in an external intelligence product as if observed.

- Evidence references of flows, legs and events SHALL be EvidenceExtract, EvidenceItem or Fact, readable and in the case context. DIRECT and DOCUMENTED flows and legs SHALL reference at least one EvidenceItem or EvidenceExtract; a Fact alone is insufficient (422). *[v0.1.2 · CR-I3-10]*

- **Certainty order (invariants only).** flow_class is an epistemic category and the registry stays unordered for display. For invariants only, the order HYPOTHETICAL < RECONSTRUCTED < DOCUMENTED < DIRECT applies; it SHALL NOT be displayed, averaged or summed. A change that raises a flow's class SHALL add at least one evidence reference not previously attached; a flow SHALL never be stronger than its weakest leg; lowering a class SHALL meet the target class's requirements (e.g. reconstruction_basis). *[v0.1.2 · CR-I3-09]*

- ValueFlow has no stored lifecycle; its envelope status is RECORDED. *[v0.1.2 · CR-I3-05]*

- **Aggregation.** Value SHALL be aggregated per (flow_class, flow_type, currency) with no grand total across classes; CONTRACT and SUBCONTRACT groups are obligations, not settlements, and only DIRECT groups count as settlement evidenced; lower/upper/exact totals SHALL count unknown amounts and never treat them as 0; legs SHALL NOT be added to their flow's totals. Details: API Specification v0.1.3 §15. *[v0.1.2 · CR-I3-12]*

## 11.2 ValueFlowLeg

Optional decomposition of a complex flow into ordered legs.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| value_flow_id | ref | Y | 1 | Parent flow. |
| sequence | integer | Y | 1 | Order. |
| origin_ref | ref | Y | 1 | Leg origin. |
| destination_ref | ref | Y | 1 | Leg destination. |
| amount | money/range | N | 0..1 | Leg amount. |
| flow_class | enum | Y | 1 | Epistemic class for this leg. |
| evidence_refs | ref\[\] | N | 0..n | Evidence for leg. |
| reconstruction_basis | text | Y\* | 0..1 | Required for RECONSTRUCTED and HYPOTHETICAL legs. *[v0.1.2 · CR-I3-04]* |
| confidence | confidence | N | 0..1 | Per-leg confidence (SRS-FR-VAL-002). *[v0.1.2 · CR-I3-04]* |

### Normative rules:

- Each leg SHALL keep its own evidence, class, value and confidence; the per-class requirements of Section 11.1 apply per leg. *[v0.1.2 · CR-I3-04]*

- Legs SHALL be immutable and append-only (no update or delete): appended in order (sequence = n + 1), each starting where the previous leg ended; a chain that reached the flow's destination takes no more legs (409), and the endpoints of a chained flow are fixed (409). Leg inputs SHALL NOT exceed the flow's classification. *[v0.1.2 · CR-I3-04]*

# 12. Indicator and Typology Model

## 12.1 Indicator

Represents an observed condition relevant to analysis. It SHALL NOT be treated as proof of wrongdoing.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| indicator_code | string | Y | 1 | Stable catalogue or local code. A catalogue indicator is referenced by its catalogue indicator ID (`<typology_id>-I<nn>`, plus catalogue version) and takes its class from the catalogue (a contradicting class → 422); a local indicator uses a `LOCAL-…` code and an explicit class. *[v0.1.2 · CR-I4-02]* |
| indicator_class | enum | Y | 1 | MECHANISM, CORROBORATING, CONTEXTUAL, DISCONFIRMING, GAP *[v0.1.1 · A09]* |
| description | text | Y | 1 | Observed condition. |
| subject_refs | ref\[\] | Y | 1..n | Affected objects: Entity, Asset, Event, ValueFlow or Relationship. *[v0.1.2 · CR-I4-02]* |
| evidence_refs | ref\[\] | Y | 1..n | Evidence: EvidenceExtract, EvidenceItem or Fact. *[v0.1.2 · CR-I4-02]* |
| status | enum | Y | 1 | OBSERVED, CORROBORATED, DISPUTED, RETIRED *[v0.1.1 · A09]* |
| confidence | confidence | Y | 1 | Confidence. |

### Normative rules:

- Indicator status transitions: OBSERVED → CORROBORATED / DISPUTED / RETIRED; DISPUTED → OBSERVED / CORROBORATED / RETIRED; RETIRED is terminal. Every change SHALL carry a rationale. Indicators are never deleted and are never proof (responses state is_proof = false). *[v0.1.2 · CR-I4-02]*

## 12.2 TypologyMatch

Represents analytical consistency between case evidence and a catalogue typology.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| typology_id | string/ref | Y | 1 | Catalogue entry. |
| subject_refs | ref\[\] | Y | 1..n | Entities/flows under analysis. |
| indicator_refs | ref\[\] | Y | 1..n | Observed indicators. |
| disconfirming_refs | ref\[\] | N | 0..n | Contrary evidence/indicators. |
| consistency_level | enum | Y | 1 | NO_BASIS, WEAK, PLAUSIBLE, STRONG, COMPELLING *[v0.1.1 · A09]* |
| analyst_rationale | text | Y | 1 | Why level was assigned. |
| confidence | confidence | Y | 1 | Confidence. |

### Normative rules:

- TypologyMatch SHALL express consistency, not guilt or legal classification.

- Strong or compelling consistency SHOULD require multiple independent indicators or direct authoritative evidence, consistent with the Typology Catalogue.

- The analyst assigns consistency_level; the system computes a ceiling (computed_ceiling, with a rule_trace) from the cited indicators, their sources and direct authoritative evidence, and SHALL reject a level above it (422); the system never raises a level. The thresholds are those of Typology Catalogue v0.1.2 §4.1, adopted PROVISIONALLY and subject to AML-specialist review. A match also records indicator_assessments (catalogue observation status per catalogue indicator) and direct_evidence_refs; STRONG and COMPELLING set reviewer_required; a cited indicator becoming DISPUTED or RETIRED flags the match review_required. Envelope status: RECORDED. *[v0.1.2 · CR-I4-03, CR-I3-05]*

# 13. Hypothesis, Gap, and Assessment Model

## 13.1 Hypothesis

Represents a testable analytical explanation.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| statement | text | Y | 1 | Specific falsifiable hypothesis. |
| hypothesis_type | enum | N | 0..1 | OWNERSHIP, CONTROL, VALUE_FLOW, TYPOLOGY, SOURCE_OF_FUNDS, OTHER *[v0.1.1 · A09]* |
| supporting_refs | ref\[\] | N | 0..n | Evidence/facts/indicators supporting. |
| contradicting_refs | ref\[\] | N | 0..n | Evidence/facts contradicting. |
| alternative_hypothesis_refs | ref\[\] | N | 0..n | Competing explanations. |
| status | enum | Y | 1 | OPEN, SUPPORTED, WEAKENED, REJECTED, INCONCLUSIVE *[v0.1.1 · A09]* |
| confidence | confidence | Y | 1 | Current confidence. |
| next_test | text | N | 0..1 | Most useful discriminating test. |
| role | enum | N | 0..1 | PRINCIPAL, ALTERNATIVE_LEGITIMATE, ALTERNATIVE_MECHANISM, INSUFFICIENT_INFORMATION (registry enum hypothesis_role; Methodology §18.1). *[v0.1.2 · CR-I4-06]* |
| assumptions | text\[\] | N | 0..n | Stated assumptions. *[v0.1.2 · CR-I4-06]* |

### Normative rules:

- A hypothesis SHALL remain open to disconfirmation.

- Rejected hypotheses SHOULD remain auditable rather than deleted.

- **HypothesisLink (matrix cell).** The support/contradiction matrix SHALL be stored as append-only HypothesisLink records: hypothesis, target_ref, effect (SUPPORTS, CONTRADICTS, NEUTRAL, UNKNOWN; registry enum hypothesis_link_effect), rationale, recorded_by, recorded_at. The current cell per target is the latest record; history is kept. supporting_refs and contradicting_refs are derived from the current cells; a removed reference becomes NEUTRAL. *[v0.1.2 · CR-I4-04, CR-I4-07]*

- A status change SHALL carry a rationale; SUPPORTED requires a SUPPORTS cell and WEAKENED or REJECTED a CONTRADICTS cell (409 otherwise). Status changes are kept as history. *[v0.1.2 · CR-I4-08, CR-I4-06]*

## 13.2 IntelligenceGap

Represents a material unknown that limits assessment.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| description | text | Y | 1 | Unknown or missing information. |
| importance | enum | Y | 1 | LOW, MEDIUM, HIGH, CRITICAL *[v0.1.1 · A09]* |
| related_refs | ref\[\] | Y | 1..n | Hypotheses/questions affected. |
| collection_feasibility | enum | Y | 1 | AVAILABLE, DIFFICULT, UNAVAILABLE, UNLAWFUL, OUT_OF_SCOPE *[v0.1.1 · A09]* |
| status | enum | Y | 1 | OPEN, PARTIALLY_RESOLVED, RESOLVED, ACCEPTED *[v0.1.1 · A09]* |
| closure_rationale | text | C | 0..1 | Required for PARTIALLY_RESOLVED, RESOLVED and ACCEPTED. *[v0.1.2 · CR-I4-05]* |

### Normative rules:

- IntelligenceGaps SHALL never be deleted; status changes are kept as history. *[v0.1.2 · CR-I4-05]*

## 13.3 Assessment

Represents a reasoned analytical judgment supported by evidence and explicit confidence.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| judgment | text | Y | 1 | Analytical conclusion. |
| scope_refs | ref\[\] | Y | 1..n | Question/hypothesis/subjects addressed: Hypothesis, TypologyMatch, Indicator, Entity, Asset, Event, ValueFlow or Relationship (InvestigationQuestion once available). *[v0.1.2 · CR-I4-14]* |
| supporting_refs | ref\[\] | Y | 1..n | Facts/indicators/evidence: Fact, Indicator, TypologyMatch, Hypothesis, EvidenceExtract or EvidenceItem (a Source → 422). *[v0.1.2 · CR-I4-14]* |
| limitations | text | Y | 1 | Known constraints and gaps. |
| alternative_explanations | text/ref\[\] | Y | 1..n | Material alternatives. |
| confidence | confidence | Y | 1 | Confidence in judgment. |
| review_status | enum | Y | 1 | DRAFT, PEER_REVIEWED, APPROVED, SUPERSEDED *[v0.1.1 · A09]* |
| finalized | boolean | Y | 1 | Set by controlled finalization, with finalized_at, finalized_by and finalization_rationale. Finalized and reviewed are distinct states. *[v0.1.2 · CR-I4-09]* |
| review_required | boolean | Y | 1 | Set when a supporting Fact becomes DISPUTED or SUPERSEDED (Section 7.5). *[v0.1.1 · A10]* Also set for indirect dependencies (Section 7.5); a flagged draft cannot be finalized. *[v0.1.2 · CR-I4-11]* |
| review_trigger_ref | ref | N | 0..1 | VerificationDecision that triggered review_required. *[v0.1.1 · A10]* Since v0.1.3 it MAY also name the HandlingChange that upgraded an input (Section 16.4). *[v0.1.3 · CR-I6-12]* |
| review_reason | enum | N | 0..1 | Why review_required is set; registry enum review_reason: FACT_DISPUTED, FACT_SUPERSEDED, INPUT_HANDLING_UPGRADED. *[v0.1.3 · CR-I6-04]* |
| subject_refs | ref\[\] | N | 0..n | Subjects of profiles and referrals (Entity, Asset), as the template requires. *[v0.1.3 · CR-I6-01]* |
| contact_point | text | N | 0..1 | Contact point of a referral package (template requirement). *[v0.1.3 · CR-I6-01]* |
| handling_decision_ref | ref | N | 0..1 | HandlingChange whose approved review downgraded the product; later inheritance floor checks accept the downgraded handling. *[v0.1.3 · CR-I6-12]* |

### Product versions and lifecycle *[v0.1.3 · CR-I6-01, CR-I6-03, CR-I6-05]*

- Submitting a product for review freezes a ProductVersion: an immutable snapshot with the rendered document (format `csaml.product-document/1`, including the evidence index) and its `content_sha256`. The first edit after a frozen version opens version n+1. *[v0.1.3 · CR-I6-01]*

- ProductVersion `version_status` (registry enum product_version_status): SUBMITTED → APPROVED / APPROVED_WITH_CHANGES / RETURNED / REJECTED → SUPERSEDED / RETRACTED. APPROVE sets the product APPROVED; APPROVE_WITH_CHANGES sets it REVIEWED, which is not disseminable until a new version is reviewed; RETURN and REJECT set it back to DRAFT. *[v0.1.3 · CR-I6-03]*

- A correction turns an APPROVED, REVIEWED or DISSEMINATED product into DRAFT version n+1 with a correction note; earlier versions remain valid until the correction is approved and then become SUPERSEDED, together with their disseminations. Withdrawal (case LEAD) sets the product WITHDRAWN, its versions RETRACTED, open reviews CANCELLED and disseminations REVOKED. *[v0.1.3 · CR-I6-05]*

- Clearing review_required is a review action: the approving reviewer sets it explicitly, or a REVIEW_FLAG_CLEARANCE review clears it. A DISSEMINATED product is never mutated; a CORRECTION review is opened instead. *[v0.1.3 · CR-I6-04]*
| high_impact_adverse | boolean | N | 0..1 | Defaults to false. True when the assessment is adverse to a named person or organization or is otherwise designated high-impact by the case's review policy. *[v0.1.1 · C10]* |
| disconfirming_searches | structured\[\] | C | 0..n | Recorded searches for information that would disconfirm the judgment. Each entry: searched_for (text), sources_consulted\[\] (1..n; each a source_ref and/or a description), result (text), rationale (text), recorded_by (principal), recorded_at (datetime). At least one entry is required before review approval when high_impact_adverse is true. Append-only. *[v0.1.1 · C10]* |

### Normative rules:

- Assessment language SHALL distinguish known, assessed, and unknown information.

- An Assessment with high_impact_adverse = true SHALL NOT pass review (a Review with decision APPROVE or APPROVE_WITH_CHANGES), and neither SHALL an IntelligenceProduct that depends on it, unless the Assessment has at least one disconfirming_searches entry (SRS-FR-ASM-004). The check is enforced at review approval, not at finalization. Entries SHALL NOT be edited or deleted; a correction is a further entry. *[v0.1.1 · C10]*

- Assessment SHALL NOT imply criminal guilt beyond the available evidence and mandate.

- **Lifecycle (finalized vs reviewed).** Envelope status is DRAFT until finalization and FINALIZED afterwards; once a review records PEER_REVIEWED, APPROVED or SUPERSEDED, the envelope status follows review_status. Finalization freezes the content; review_status stays DRAFT until a review exists. *[v0.1.2 · CR-I4-09]*

- **Competing hypotheses.** Finalization SHALL be rejected (409 STATE_CONFLICT, reason COMPETING_HYPOTHESES_REQUIRED) when a Hypothesis in scope_refs has no competing hypothesis. *[v0.1.2 · CR-I4-08]*

- **Disconfirming searches after finalization.** Entries MAY be appended to a finalized Assessment until the Assessment (or a product depending on it) passes review approval; afterwards they are frozen (409). SRS-FR-ASM-004 is checked at review approval. This changes the I4 implementation, which froze searches at finalization. *[v0.1.2 · CR-I4-10]*

- **Revisions.** Every record_version of an Assessment SHALL be kept as an append-only revision snapshot. *[v0.1.2 · CR-I4-05]*

# 14. Confidence and Source Evaluation Model

CS-AML separates source reliability, information credibility, and analyst confidence. Implementations SHALL NOT compress these dimensions into a single unexplained score.

| **Dimension** | **Allowed values** | **Meaning** |
|----|----|----|
| Source reliability | A-F | A highly reliable; B generally reliable; C mixed; D generally unreliable; E unreliable; F unknown |
| Information credibility | 1-6 | 1 independently confirmed; 2 probably true; 3 possibly true; 4 doubtful; 5 improbable; 6 cannot be judged. Registry enum credibility_grade names these INDEPENDENTLY_CONFIRMED … CANNOT_BE_JUDGED; the wire values remain the digit codes. *[v0.1.2 · CR-I2-08]* |
| Analyst confidence | HIGH / MODERATE / LOW, or INSUFFICIENT_BASIS (display: High / Moderate / Low / Insufficient basis) | Overall confidence in analytical judgment, based on evidence quality, independence, consistency, and remaining gaps. INSUFFICIENT_BASIS is not a level below LOW (Section 14.1). *[v0.1.1 · A09]* |

## 14.1 Confidence

Structured confidence object embedded/referenced by analytical objects.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| level | enum | Y\* | 0..1 | HIGH, MODERATE, LOW, INSUFFICIENT_BASIS; `null` only on drafts where no confidence judgement has yet been made. *[v0.1.1 · A09]* |
| basis | text | Y | 1 | Reason for confidence (rationale); mandatory for every level, including INSUFFICIENT_BASIS. *[v0.1.1 · A09]* |
| source_diversity | enum | N | 0..1 | SINGLE, MULTIPLE_RELATED, MULTIPLE_INDEPENDENT *[v0.1.1 · A09]* |
| material_gaps | ref\[\] | N | 0..n | Gap references. |
| last_reviewed_at | datetime | Y | 1 | Review timestamp. |
| reviewer | principal | N | 0..1 | Reviewer if required. |

### Normative rules: *[v0.1.1 · A09]*

- INSUFFICIENT_BASIS means a judgement was attempted but the evidential basis is insufficient. It is NOT a level below LOW and SHALL NOT be converted to LOW, null, zero, or omitted in storage, APIs, exports, or visualizations.

- `level = null` is permitted only on draft objects where no confidence judgement has been made yet. A finalized (approved, established, or disseminated) analytical object SHALL carry a non-null level.

- No normalization, migration, or aggregation SHALL raise certainty (e.g. by mapping INSUFFICIENT_BASIS or null to any level, or LOW to MODERATE).

# 15. Intelligence Product and Dissemination Model

## 15.1 IntelligenceProduct

Represents an approved analytical output for an identified audience.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| product_type | enum | Y | 1 | FINANCIAL_INTELLIGENCE_NOTE, ENTITY_PROFILE, ASSET_PROFILE, NETWORK_ANALYSIS, REFERRAL_PACKAGE, CASE_REPORT, INVESTIGATION_BRIEF, PUBLICATION_SUPPORT. The first six are the MVP P0 templates (SRS-FR-PRD-001); INVESTIGATION_BRIEF and PUBLICATION_SUPPORT are not in MVP scope. *[v0.1.1 · A06, A09]* |
| title | string | Y | 1 | Neutral title. |
| assessment_refs | ref\[\] | Y | 1..n | Underlying assessments. |
| evidence_manifest | ref\[\] | Y | 1..n | Evidence inventory. |
| audience | enum/string\[\] | Y | 1..n | Authorized audience. |
| classification | enum | Y | 1 | Sensitivity. |
| approval_state | enum | Y | 1 | DRAFT, REVIEWED, APPROVED, DISSEMINATED, WITHDRAWN *[v0.1.1 · A09]* |
| version | string | Y | 1 | Product version. |
| published_at | datetime | N | 0..1 | If published/disseminated. |
| review_required | boolean | Y | 1 | Set when a Fact underlying a referenced assessment becomes DISPUTED or SUPERSEDED (Section 7.5); a disseminated product is not mutated — a correction review task is created. *[v0.1.1 · A10]* |
| review_trigger_ref | ref | N | 0..1 | VerificationDecision that triggered review_required. *[v0.1.1 · A10]* |

## 15.2 Review

Represents peer, legal, privacy, security, or red-team review.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| review_type | enum | Y | 1 | PEER, LEGAL, PRIVACY, SECURITY, RED_TEAM, EDITORIAL *[v0.1.1 · A09]* |
| target_ref | ref | Y | 1 | Object/product reviewed. |
| reviewer | principal | Y | 1 | Reviewer. |
| findings | text/structured | Y | 1 | Review findings. |
| decision | enum | Y | 1 | APPROVE, APPROVE_WITH_CHANGES, RETURN, REJECT *[v0.1.1 · A09]* |
| completed_at | datetime | Y | 1 | Completion time. |
| review_kind | enum | Y | 1 | What the review decides; registry enum review_kind: PRODUCT_VERSION, ASSESSMENT, REVIEW_FLAG_CLEARANCE, HANDLING_CHANGE, CORRECTION. *[v0.1.3 · CR-I6-02]* |
| review_status | enum | Y | 1 | Registry enum review_status: OPEN, DECIDED, CANCELLED. reviewer, decision and completed_at are null while OPEN. *[v0.1.3 · CR-I6-03]* |
| target_version | string | N | 0..1 | Frozen product version under review (PRODUCT_VERSION reviews). *[v0.1.3 · CR-I6-03]* |
| requested_by | principal | Y | 1 | Principal who submitted or requested the review. *[v0.1.3 · CR-I6-02]* |

### Normative rules: *[v0.1.3 · CR-I6-02]*

- A Review targets a frozen product version, a finalized assessment, a review_required clearance, a handling change (classification downgrade or label removal) or a correction task. All kinds are decided through the same approve / request-changes / reject actions.

- Authors, contributors and the requester SHALL NOT decide a review (403; enforced by the database as well). Deciding requires a REVIEWER or LEAD case membership.

## 15.3 Dissemination

Records controlled release of a product or data package.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| product_ref | ref | Y | 1 | Product disseminated. |
| recipient | string/ref | Y | 1 | Recipient/authority/audience. |
| purpose | text | Y | 1 | Purpose. |
| released_at | datetime | Y | 1 | Release time. |
| released_by | principal | Y | 1 | Authorizer. |
| handling_caveats | string\[\] | N | 0..n | Restrictions. |
| receipt_or_reference | string | N | 0..1 | Acknowledgement/reference. |
| product_version | string | Y | 1 | Frozen product version released. *[v0.1.3 · CR-I6-06]* |
| handling_classification | enum | Y | 1 | Handling classification of the release; at least the product's classification (defaults to it). *[v0.1.3 · CR-I6-06]* |
| dissemination_status | enum | Y | 1 | Registry enum dissemination_status: REQUESTED, APPROVED, REVOKED, SUPERSEDED. released_at / released_by are set on approval. *[v0.1.3 · CR-I6-06]* |
| package_scope_refs | ref\[\] | N | 0..n | Complete approved scope of export packages. *[v0.1.3 · CR-I6-06]* |
| source_protected_release | boolean | Y | 1 | SOURCE_PROTECTED objects are in the approved scope only when true. *[v0.1.3 · CR-I6-07]* |

### Normative rules: *[v0.1.3 · CR-I6-06, CR-I6-07]*

- REQUESTED → APPROVED / REVOKED; APPROVED → REVOKED / SUPERSEDED. An approved release is immutable (database trigger). The approver is a REVIEWER or LEAD case member and never the requester.

- `source_protected_release` MAY be set only by an approver holding the per-case protected-source grant, with a rationale. Without it every SOURCE_PROTECTED object, index entry and citation is withheld from export packages; only the count is recorded.

## 15.4 ExportPackage and sharing log *[v0.1.3 · CR-I6-08, CR-I6-09]*

An ExportPackage is bound to one approved Dissemination and its product version. It records `format` (registry enum export_package_format: CSAML_PACKAGE_ZIP_V1), `package_status` (registry enum export_package_status: QUEUED, GENERATING, READY, FAILED), the requested `object_refs`, the `files` with their SHA-256, `package_sha256`, `manifest_sha256` and the `redactions` (counts and reasons, never content). Every download re-checks authorization and approval validity. Sharing-log entries are immutable and carry `entry_type` (registry enum sharing_log_entry_type: RELEASE_APPROVED, EXPORT_GENERATED, RELEASE_REVOKED), product version, handling caveats and handling classification. Package generation runs as a Job (registry enum job_status: QUEUED, RUNNING, SUCCEEDED, FAILED).

# 16. Privacy, Classification, and Access-Control Metadata

This section defines the authoritative CS-AML information-classification model. All other CS-AML documents SHALL use these levels and wire values. *[v0.1.1 · A08]*

Levels are ordered from least to most restrictive:

| **Classification (wire value)** | **Display label** | **Meaning** |
|----|----|----|
| PUBLIC | Public | Suitable for public release after normal review. |
| INTERNAL | Internal | Routine internal operational information. |
| SENSITIVE | Sensitive | Could create privacy, reputational, safety, or investigative harm if disclosed. |
| RESTRICTED | Restricted | High-risk information requiring named-role or case-specific authorization. |
| SOURCE_PROTECTED | Source-protected | Information whose disclosure could identify or endanger a confidential source. *[v0.1.1 · A08]* |

v0.1 wrote the last level as `SOURCE-PROTECTED`; the v0.1.1 wire value is `SOURCE_PROTECTED`. *[v0.1.1 · A08, A09]*

Access labels MAY add purpose, jurisdiction, source-protection, embargo, legal-review, or compartment restrictions. Implementations SHALL enforce the most restrictive applicable label.

### Normative rules: *[v0.1.1 · A08]*

- Access labels are additive restrictions on top of the classification level. Access requires satisfying the object's classification level and every applicable access label; neither replaces the other.

- Derived objects and exports SHALL inherit the highest classification (and the union of access labels) of their inputs, unless a recorded reviewer downgrade decision exists for that object.

- An unknown, missing, or unrecognized classification value SHALL fail closed: access is denied and the object is flagged for classification. It SHALL NOT default to a less restrictive level.

- **Inheritance is enforced, not silently raised.** A declared classification below the maximum of the inputs, or access labels missing an input label, SHALL be rejected (422); omitted values default to the inherited ones. PATCH MAY only upgrade or add labels; downgrades SHALL be rejected (403) until a recorded reviewer downgrade decision exists. When an input is later upgraded, dependent derived objects SHALL be flagged "re-review required"; their classification SHALL NOT be raised automatically. *[v0.1.2 · CR-I2-05]*

- Case classification and labels are changed only by the case LEAD, upgrades only (Section 6.1). *[v0.1.2 · CR-I1-09]*

- The "recorded reviewer downgrade decision" is a HandlingChange with direction DOWNGRADE that names its approved HANDLING_CHANGE review (Section 16.4). *[v0.1.3 · CR-I6-12]*

### Principal clearance model *[v0.1.2 · CR-I1-10]*

A principal's clearance is represented by identity-provider (Keycloak realm) roles; see also Technical Stack v0.1.3 §10. *[v0.1.2 · CR-I1-10]*

| **IdP role** | **Effect** |
|----|----|
| (none) | Baseline clearance INTERNAL: PUBLIC and INTERNAL objects of the principal's cases. |
| csaml-clearance-sensitive | Clearance up to SENSITIVE. |
| csaml-clearance-restricted | Clearance up to RESTRICTED. |
| csaml-protected-source | Eligibility for SOURCE_PROTECTED material; effective only together with the per-case grant protected_source_authorized on the CaseMembership (Section 6.3). |
| csaml-label-<label> | Satisfies the access label <label>; every label of an object must be satisfied. |

Clearance never replaces case membership: access requires membership, sufficient clearance and every access label. Unknown labels fail closed. *[v0.1.2 · CR-I1-10]*

### Legacy mapping from the Framework v0.1 four-level scheme *[v0.1.1 · A08]*

The parent Framework v0.1 Expanded (Section 6.4) used Public / Internal / Restricted / Highly Restricted. Records migrated from that scheme SHALL be mapped as follows. The last two rows SHALL NOT be mapped automatically.

| **Framework v0.1 label** | **v0.1.1 level** |
|----|----|
| Public | PUBLIC |
| Internal | INTERNAL |
| Restricted | SENSITIVE or RESTRICTED — chosen by the data owner during migration; RESTRICTED until decided (fail closed). |
| Highly Restricted | SOURCE_PROTECTED only when the reason is source-identifying information; otherwise RESTRICTED plus the relevant access label (e.g. legal-privilege, physical-security). Never auto-map. |

## 16.1 RetentionRule

Represents retention and disposition policy attached to objects or classes.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| rule_id | string | Y | 1 | Policy identifier. |
| applies_to | enum/ref | Y | 1 | Object type/object. Registry enum retention_target_type: EVIDENCE_ITEM, EXPORT_PACKAGE, CASE (MVP 0.1). Never changes after creation. *[v0.1.3 · CR-I7-02]* |
| applies_to_classifications | enum\[\] | N | 0..n | Narrows the rule to objects of these classifications (SRS-FR-ADM-003 "by object type/classification"); empty = all. *[v0.1.3 · CR-I7-02]* |
| retention_period | duration/date | Y | 1 | Retention term. |
| trigger | enum | Y | 1 | CREATION, CASE_CLOSURE, DISSEMINATION, LEGAL_HOLD_RELEASE, OTHER *[v0.1.1 · A09]* |
| disposition | enum | Y | 1 | DELETE, ANONYMIZE, ARCHIVE, REVIEW *[v0.1.1 · A09]* |
| legal_hold | boolean | Y | 1 | Whether disposition suspended. |
| rule_status | enum | Y | 1 | Registry enum retention_rule_status: ACTIVE, RETIRED (final; rules are never deleted). *[v0.1.3 · CR-I7-03]* |

### Normative rules: *[v0.1.3 · CR-I7-01, CR-I7-05, CR-I7-06]*

- Rules are versioned by record_version and never deleted; every change is audited.

- When several active rules match a target, the most protective governs: the target is eligible only when every matching period has expired, and the latest date wins. CASE_CLOSURE uses Case.closed_at (Section 6.1).

- Evaluation only reports or proposes; nothing is disposed of automatically. Disposition requires an approved DispositionRecord (Section 16.3).

- MVP 0.1 executes DELETE (evidence originals and export packages: the stored bytes are purged and the record stays as the tombstone), ARCHIVE and REVIEW (recorded retention state). ANONYMIZE and whole-case DELETE SHALL be refused (422) in MVP 0.1; their semantics (a reviewed anonymiser, a case-level tombstone) are deferred to v0.2. *[v0.1.3 · CR-I7-05]*

## 16.2 LegalHold *[v0.1.3 · CR-I7-03]*

Suspends disposition of a case (and every object linked to it) or of one object. Required as the legal hold record of CIG PRI-02.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| target_type | enum | Y | 1 | Registry enum retention_target_type. |
| target_ref | ref | Y | 1 | Held case or object. |
| reason | text | Y | 1 | Why the hold is placed. |
| authority_reference | string | N | 0..1 | Order, request or authority reference. |
| hold_status | enum | Y | 1 | Registry enum legal_hold_status: ACTIVE, RELEASED. |
| placed_by / placed_at | principal / datetime | Y | 1 | Placed by a platform administrator or the case LEAD. |
| released_by / released_at / release_reason | principal / datetime / text | N | 0..1 | Recorded once, on release. |

### Normative rules:

- A legal hold is never deleted; only its release is recorded, once. While a hold is ACTIVE, approval and execution of any disposition of the held target SHALL be refused (409; also enforced by the database).

## 16.3 DispositionRecord *[v0.1.3 · CR-I7-04]*

The disposition log required by CIG PRI-02: one record per proposed disposition of one target.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| rule_ref / rule_version | ref / integer | Y | 1 | Governing RetentionRule and its version. |
| target_type / target_ref | enum / ref | Y | 1 | Target (registry enum retention_target_type). |
| disposition / trigger | enum | Y | 1 | From the rule (retention_disposition, retention_trigger). |
| trigger_at / eligible_at | datetime | Y | 1 | Trigger time and the date the target became eligible. |
| disposition_status | enum | Y | 1 | Registry enum disposition_status: PROPOSED, APPROVED, REJECTED, EXECUTING, EXECUTED. |
| proposed_by / proposed_at | principal / datetime | Y | 1 | Proposer (the evaluation). |
| decided_by / decided_at / decision_rationale | principal / datetime / text | N | 0..1 | Decision. |
| executed_by / executed_at / outcome | principal / datetime / structured | N | 0..1 | Execution and its outcome (e.g. purged versions, retained hash and size). |

### Normative rules:

- PROPOSED → APPROVED / REJECTED → EXECUTING → EXECUTED. The decider is the LEAD of every case the target is linked to and never the proposer (403; database CHECK). A target linked to no case cannot be approved (fail closed).

- Execution re-checks the rule and legal holds and commits in two steps (EXECUTING, then EXECUTED) so that purged bytes are never without a record. Terminal records are frozen. Records and audit events are never deleted.

- A record carries the target's classification, access labels and case links and is visible exactly where the target is.

## 16.4 HandlingChange *[v0.1.3 · CR-I6-12]*

Append-only record of a classification or access-label change of a canonical object.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| target_type / target_ref | string / ref | Y | 1 | Changed object. |
| from_classification / to_classification | enum | Y | 1 | Classification before and after. |
| from_labels / to_labels | string\[\] | Y | 0..n | Access labels before and after. |
| direction | enum | Y | 1 | Registry enum handling_change_direction: UPGRADE, DOWNGRADE. |
| review_ref | ref | C | 0..1 | Approved HANDLING_CHANGE review; required for DOWNGRADE (database CHECK). |
| flagged_refs | ref\[\] | N | 0..n | Derived objects flagged review_required by an upgrade (Section 16, CR-I2-05). |
| changed_by / changed_at | principal / datetime | Y | 1 | Actor and time. |

### Normative rules:

- UPGRADE is applied directly; DOWNGRADE (including label removal) only with its approved review. Records are never updated or deleted.

- review_trigger_ref of a flagged assessment or product MAY name the HandlingChange; a downgraded product keeps it as handling_decision_ref (Section 15.1).

# 17. Temporal, Versioning, and Audit Semantics

CS-AML distinguishes system time (when the system knew/recorded something) from valid time (when the represented fact/relationship was true in the real world). Where historically material, both SHOULD be stored.

``` text
valid_from / valid_to    = real-world validity
created_at / updated_at   = system record time
record_version            = object mutation sequence
AuditEvent                = who changed what, when, and why
```

## 17.1 AuditEvent

Append-only record of material actions.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| actor | principal | Y | 1 | Human/service principal. |
| action | enum/string | Y | 1 | CREATE, UPDATE, MERGE, SPLIT, REVIEW, APPROVE, DISSEMINATE, RESTRICT, DELETE, EXPORT, LOGIN_SENSITIVE, OTHER *[v0.1.1 · A09]* |
| target_ref | ref | Y | 1 | Affected object. |
| occurred_at | datetime | Y | 1 | Time. |
| reason | text | N | 0..1 | Reason/context. |
| before_hash | string | N | 0..1 | Optional integrity reference. |
| after_hash | string | N | 0..1 | Optional integrity reference. |
| case_context | ref | N | 0..1 | Case context if applicable. |

### Normative rules:

- Audit events SHALL be append-only for normal users.

- Administrative correction of audit data SHALL itself generate an audit event.

# 18. Cross-Object Integrity Rules

| **Rule** | **Constraint** |
|----|----|
| DM-I01 | Every Fact SHALL reference at least one EvidenceItem or EvidenceExtract (supporting_evidence 1..n); supporting Claims are optional (0..n) and never replace evidence. Every Fact SHALL have the CREATE VerificationDecision written in the same transaction. *[v0.1.1 · C01]* *[v0.1.1 · C02]* |
| DM-I02 | Every Indicator SHALL reference supporting evidence and at least one subject object. |
| DM-I03 | Every TypologyMatch SHALL reference one catalogue typology and one or more indicators. |
| DM-I04 | Every Assessment SHALL reference supporting analytical objects and include limitations. |
| DM-I05 | A ValueFlow with flow_class=DIRECT SHALL NOT exist without direct evidence of movement. |
| DM-I06 | A Relationship of type OWNS/BENEFICIAL_OWNER_OF/CONTROLS SHALL include confidence with a non-empty confidence.basis (the basis of the relationship); the Relationship has no separate basis field. Detailed ownership/control basis is held on OwnershipInterest.basis / ControlAssertion.control_basis. *[v0.1.2 · CR-I2-15]* |
| DM-I07 | Entity merge SHALL preserve precursor identifiers and generate AuditEvent. Every merge and unmerge SHALL be recorded as a ResolutionDecision. *[v0.1.1 · ER]* |
| DM-I08 | External dissemination SHALL reference an approved IntelligenceProduct. |
| DM-I09 | Source-protected information (classification SOURCE_PROTECTED or a source-protection access label) SHALL NOT be exported into lower-classification products without explicit de-identification review. *[v0.1.1 · A08]* |
| DM-I10 | Deletion/anonymization SHALL respect evidence preservation obligations and legal holds. |
| DM-I11 | Every Fact SHALL reference at least one VerificationDecision; a Claim SHALL NOT be stored, shown, or exported as a Fact without one. *[v0.1.1 · A10]* |
| DM-I12 | A Fact with fact_status = SUPERSEDED SHALL reference its replacement Fact (superseded_by). *[v0.1.1 · A10]* |
| DM-I13 | An object with missing or unrecognized classification SHALL be treated as inaccessible (fail closed) and flagged for classification. *[v0.1.1 · A08]* |
| DM-I14 | A derived object or export SHALL carry a classification at least as restrictive as the highest classification of its inputs, unless a recorded reviewer downgrade decision exists. *[v0.1.1 · A08]* |
| DM-I15 | Entity.resolution_status SHALL be derivable from the Entity's ResolutionDecision history; a resolution_status change without a corresponding ResolutionDecision SHALL be rejected. *[v0.1.1 · ER]* |

# 19. Canonical Graph Mapping

Graph implementations SHOULD use Entity, Asset, Event, and selected contextual objects as nodes, with Relationship and ValueFlow as first-class edges or edge-objects. Evidence SHALL NOT be lost when graph projections are materialized.

``` text
(:Person)-[:DIRECTOR_OF {relationship_id,...}]->(:Organization)
(:Person)-[:BENEFICIAL_OWNER_OF {ownership_interest_id,...}]->(:Organization)
(:Organization)-[:AWARDED_CONTRACT]->(:Contract)
(:Organization)-[:ACQUIRED]->(:Asset)
(:Entity)-[:VALUE_FLOW {value_flow_id, flow_class,...}]->(:Entity)
```

## 19.1 Graph projection rule

A graph edge is a projection of a canonical Relationship or ValueFlow object. The canonical object remains authoritative because it contains provenance, validity period, confidence, and handling metadata that may exceed native graph-edge capabilities.

# 20. Reference Relational Mapping

``` text
cases
case_memberships         (v0.1.2 · CR-I1-02)
sources
evidence_items
evidence_extracts
evidence_integrity_checks (append-only verification results)
upload_sessions
claims
verification_decisions   (v0.1.1 · A10)
facts
entities
entity_identifiers
resolution_decisions     (v0.1.1 · ER)
relationships
ownership_interests
control_assertions
assets
events
value_flows
value_flow_legs
indicators
typology_matches
hypotheses
hypothesis_links
intelligence_gaps
assessments
assessment_disconfirming_searches
assessment_revisions     (v0.1.2 · CR-I4-05)
intelligence_products
product_versions
reviews
disseminations
export_packages
sharing_log_entries
jobs
handling_changes
retention_rules
legal_holds
disposition_records
search_documents
audit_events
```

v0.1.2 adds case_memberships, upload_sessions, evidence_integrity_checks, assessment_disconfirming_searches and assessment_revisions to the list; hypothesis_links holds the append-only matrix cells (Section 13.1). *[v0.1.2 · CR-I1-02, CR-I4-04, CR-I4-05]*

v0.1.3 adds product_versions, export_packages, sharing_log_entries, jobs, handling_changes, retention_rules, legal_holds and disposition_records; search_documents is a derived, rebuildable search projection, never canonical. *[v0.1.3 · CR-I6-01, CR-I6-08, CR-I6-09, CR-I6-12, CR-I7-01, CR-I7-03, CR-I7-04, CR-I5-01]*

This list is illustrative. Implementations MAY normalize or denormalize differently provided semantic and integrity requirements are preserved.

# 21. Canonical JSON Example

Enumeration values in this example use the UPPER_SNAKE_CASE wire form (Section 4.1). *[v0.1.1 · A09]*

``` text
{
  "id": "vf-7c2e...",
  "object_type": "ValueFlow",
  "schema_version": "0.1",
  "flow_class": "RECONSTRUCTED",
  "flow_type": "ASSET_PURCHASE",
  "origin_ref": "org-123",
  "destination_ref": "asset-456",
  "amount": {
    "value": 850000000,
    "currency": "IDR",
    "precision": "ESTIMATED"
  },
  "occurred_at": {
    "from": "2026-05-01",
    "to": "2026-05-31"
  },
  "evidence_refs": [
    "evd-11",
    "evd-19"
  ],
  "reconstruction_basis": "Contract award and subsequent deed records indicate a plausible economic link; no bank settlement record is available.",
  "confidence": {
    "level": "MODERATE",
    "basis": "Two independent documentary sources; settlement route unknown."
  },
  "classification": "SENSITIVE",
  "record_version": 3
}
```

# 22. API and Exchange Requirements

- APIs SHALL expose object IDs, schema version, record version, classification, and provenance references.

- APIs SHOULD support field-level filtering to prevent unnecessary disclosure of sensitive attributes.

- Bulk exports SHALL preserve relationship/evidence IDs so provenance survives movement between systems.

- Systems SHALL reject writes that violate mandatory cross-object integrity rules.

- Machine-generated analytical suggestions SHALL be marked with creator_type = AUTOMATION or AI and SHALL require human review before becoming an Assessment. *[v0.1.1 · A09]*

# 23. Interoperability and External Identifiers

The canonical model is implementation-neutral and MAY map to external ontologies or identifiers. External IDs SHALL be stored as typed identifiers and SHALL NOT replace internal canonical IDs.

| **Domain** | **Examples** | **Model treatment** |
|----|----|----|
| Corporate | registration number, LEI, registry ID | Entity.identifier\[\] |
| Persons | official registry identifiers where lawful | Entity.identifier\[\] with restricted handling where sensitive |
| Sanctions/PEP | list-specific subject IDs | External identifier + Source/Evidence |
| Crypto | wallet/address | Entity type=wallet; chain/network as typed attribute |
| Procurement | tender/contract IDs | Contract Entity/Event/Source refs |
| Geospatial | parcel/registry identifiers | Asset/Location identifiers |

# 24. Schema Versioning and Migration

- Every stored object SHALL declare schema_version.

- Breaking semantic changes SHALL increment the major/minor model version according to framework governance.

- Migrations SHALL preserve provenance and audit history.

- A migration SHALL NOT silently convert reconstructed value flow into direct value flow, or claim into fact, or hypothesis into assessment.

- Deprecated fields SHOULD remain readable for a defined transition period.

# 25. Data Quality and Validation

| **Quality dimension** | **Expected measure** |
|----|----|
| Completeness | Required fields populated and required links present. |
| Provenance coverage | Share of facts/indicators/assessments traceable to evidence. |
| Entity resolution quality | Merge/split error rate; unresolved duplicate rate. |
| Temporal quality | Coverage of validity dates for time-sensitive relationships. |
| Confidence hygiene | Analytical objects with explicit confidence basis. |
| Classification hygiene | Sensitive objects carrying appropriate handling labels. |
| Orphan rate | Objects lacking expected parent/context/evidence links. |
| Audit completeness | Material actions represented by AuditEvent. |

# 26. Data Model Conformance

An implementation claiming to implement CS-AML Data Model v0.1.3 SHALL demonstrate the following minimum capabilities:

- Persistent canonical IDs and schema versioning.

- Separate Source, Evidence, Fact, Indicator, Hypothesis, Assessment, and IntelligenceProduct objects.

- Reusable Entity objects with evidence-based resolution history.

- Evidence-linked Relationship and ValueFlow representations.

- Explicit value-flow epistemic class.

- Confidence and intelligence-gap representation.

- Sensitivity/classification metadata and access enforcement.

- Append-only audit history for material actions.

- Export that preserves provenance references and object identity.

- Validation of the mandatory cross-object integrity rules in Section 18.

No implementation has yet been assessed against these capabilities; they are targets, not evidence of conformance. *[v0.1.1 · A01]*

> **Conformance principle**
>
> A schema is not conformant merely because it uses similar table or class names. Conformance depends on preserving the semantics, separations, provenance requirements, and integrity constraints defined by this specification.

# Annex A. Controlled Enumerations (Baseline)

Annex A, together with the enumerations stated in the field tables of this specification, is the controlled-enumeration registry for CS-AML. All wire values are UPPER_SNAKE_CASE (Section 4.1); display labels are separate and translatable. Enumeration lists in other CS-AML documents derive from this registry. *[v0.1.1 · A09]*

| **Enumeration** | **Baseline values** |
|----|----|
| entity_type | PERSON, ORGANIZATION, ACCOUNT, ADDRESS, DOMAIN, PHONE, EMAIL, WALLET, PROPERTY, VEHICLE, VESSEL, AIRCRAFT, CONTRACT, PROJECT, OTHER *[v0.1.1 · A09]* |
| flow_class | DIRECT, DOCUMENTED, RECONSTRUCTED, HYPOTHETICAL *[v0.1.1 · A09]* |
| confidence.level | HIGH, MODERATE, LOW, INSUFFICIENT_BASIS (`null` only on drafts with no judgement yet; INSUFFICIENT_BASIS is not a level below LOW — Section 14.1) *[v0.1.1 · A09]* |
| classification | PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, SOURCE_PROTECTED (ordered least → most restrictive; unknown/missing fails closed — Section 16) *[v0.1.1 · A08, A09]* |
| hypothesis.status | OPEN, SUPPORTED, WEAKENED, REJECTED, INCONCLUSIVE *[v0.1.1 · A09]* |
| typology_match.consistency_level | NO_BASIS, WEAK, PLAUSIBLE, STRONG, COMPELLING *[v0.1.1 · A09]* |
| review.decision | APPROVE, APPROVE_WITH_CHANGES, RETURN, REJECT *[v0.1.1 · A09]* |
| claim.claim_status | RECORDED, UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED *[v0.1.1 · A10]* |
| fact.fact_status | PROVISIONAL, ESTABLISHED, DISPUTED, SUPERSEDED *[v0.1.1 · A10]* |
| verification_decision.decision | Claims: UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED; Facts: CREATE (label "Create fact"), ESTABLISH, DISPUTE, SUPERSEDE *[v0.1.1 · A10]* |
| entity.resolution_status | UNRESOLVED, RESOLVED, CONFLICTED, MERGED, SPLIT (state only; changed by ResolutionDecision) *[v0.1.1 · A09, ER]* |
| resolution_decision.decision | MERGE, KEEP_SEPARATE, POSSIBLE_MATCH, DEFER, UNMERGE *[v0.1.1 · ER]* |
| case_membership.role | LEAD, ANALYST, REVIEWER *[v0.1.2 · CR-I1-02]* |
| case.risk_rating | LOW, MEDIUM, HIGH, CRITICAL (ordered; minimal set) *[v0.1.2 · CR-I1-08]* |
| case.closure_reason | OBJECTIVES_MET, INSUFFICIENT_BASIS_TO_CONTINUE, REFERRED, OUT_OF_SCOPE, DUPLICATE, LEGAL_OR_SAFETY_CONSTRAINT, OTHER (minimal set) *[v0.1.2 · CR-I1-08]* |
| upload_session.status | INITIATED, CONTENT_RECEIVED, COMPLETED (expiry is expressed by expires_at) *[v0.1.2 · CR-I2-02]* |
| envelope.status | REGISTERED, RECORDED, DRAFT, FINALIZED (for classes without their own lifecycle: REGISTERED for Source, EvidenceExtract, Asset; RECORDED for Event, ValueFlow, TypologyMatch; DRAFT / FINALIZED for Assessment before a review outcome) *[v0.1.2 · CR-I2-03, CR-I3-05, CR-I4-09]* |
| claim.credibility_grade | INDEPENDENTLY_CONFIRMED, PROBABLY_TRUE, POSSIBLY_TRUE, DOUBTFUL, IMPROBABLE, CANNOT_BE_JUDGED (wire codes "1"…"6", registry exception) *[v0.1.2 · CR-I2-08]* |
| money.precision | EXACT, APPROXIMATE, ESTIMATED (a range is never exact) *[v0.1.2 · CR-I3-06]* |
| temporal_value.precision | DATETIME, DAY, MONTH, YEAR, RANGE, UNKNOWN (string shape must match) *[v0.1.2 · CR-I3-06]* |
| hypothesis.role | PRINCIPAL, ALTERNATIVE_LEGITIMATE, ALTERNATIVE_MECHANISM, INSUFFICIENT_INFORMATION *[v0.1.2 · CR-I4-06]* |
| hypothesis_link.effect | SUPPORTS, CONTRADICTS, NEUTRAL, UNKNOWN *[v0.1.2 · CR-I4-07]* |
| search_hit.object_type | CASE, ENTITY, SOURCE, EVIDENCE_ITEM, EVIDENCE_EXTRACT, CLAIM, FACT, RELATIONSHIP, ASSET, EVENT, VALUE_FLOW, PRODUCT *[v0.1.3 · CR-I5-03]* |
| search_hit.epistemic_status | CLAIM, FACT, EXCERPT, RECORD (a claim is never shown as a fact) *[v0.1.3 · CR-I5-03]* |
| graph_lead.lead_type | SHARED_IDENTIFIER, SHARED_PHONE, SHARED_EMAIL, SHARED_ADDRESS (candidates, never facts or edges) *[v0.1.3 · CR-I5-05]* |
| graph_query.truncation_reason | NODE_BUDGET, EDGE_BUDGET, TIME_BUDGET, LEAD_BUDGET *[v0.1.3 · CR-I5-06]* |
| review.review_kind | PRODUCT_VERSION, ASSESSMENT, REVIEW_FLAG_CLEARANCE, HANDLING_CHANGE, CORRECTION *[v0.1.3 · CR-I6-02]* |
| review.review_status | OPEN, DECIDED, CANCELLED *[v0.1.3 · CR-I6-03]* |
| product_version.version_status | SUBMITTED, APPROVED, APPROVED_WITH_CHANGES, RETURNED, REJECTED, SUPERSEDED, RETRACTED *[v0.1.3 · CR-I6-03]* |
| intelligence_product.review_reason | FACT_DISPUTED, FACT_SUPERSEDED, INPUT_HANDLING_UPGRADED *[v0.1.3 · CR-I6-04]* |
| dissemination.dissemination_status | REQUESTED, APPROVED, REVOKED, SUPERSEDED *[v0.1.3 · CR-I6-06]* |
| export_package.format | CSAML_PACKAGE_ZIP_V1 *[v0.1.3 · CR-I6-08]* |
| export_package.package_status | QUEUED, GENERATING, READY, FAILED *[v0.1.3 · CR-I6-08]* |
| sharing_log.entry_type | RELEASE_APPROVED, EXPORT_GENERATED, RELEASE_REVOKED *[v0.1.3 · CR-I6-08]* |
| job.status | QUEUED, RUNNING, SUCCEEDED, FAILED *[v0.1.3 · CR-I6-09]* |
| handling_change.direction | UPGRADE, DOWNGRADE *[v0.1.3 · CR-I6-12]* |
| retention_rule.applies_to | EVIDENCE_ITEM, EXPORT_PACKAGE, CASE (MVP 0.1) *[v0.1.3 · CR-I7-02]* |
| retention_rule.rule_status | ACTIVE, RETIRED *[v0.1.3 · CR-I7-03]* |
| legal_hold.hold_status | ACTIVE, RELEASED *[v0.1.3 · CR-I7-03]* |
| disposition_record.disposition_status | PROPOSED, APPROVED, REJECTED, EXECUTING, EXECUTED *[v0.1.3 · CR-I7-04]* |

# Annex B. Canonical Relationship Vocabulary (Baseline)

| **Relationship** | **Direction** | **Semantics** |
|----|----|----|
| OWNS | Directed | Legal ownership unless subtype says otherwise. |
| BENEFICIAL_OWNER_OF | Directed | Beneficial ownership/economic interest. |
| CONTROLS | Directed | Control without requiring ownership. |
| DIRECTOR_OF | Directed | Corporate role; from Person to Organization (`Person --DIRECTOR_OF--> Organization`). *[v0.1.1 · A14]* |
| OFFICER_OF | Directed | Organizational role. |
| EMPLOYED_BY | Directed | Employment/role. |
| RELATED_TO | Symmetric | Familial/known relation; subtype required where possible. |
| ASSOCIATE_OF | Symmetric | Documented association; SHALL NOT imply wrongdoing. |
| SHARES_ADDRESS_WITH | Symmetric | Common address. |
| SHARES_PHONE_WITH | Symmetric | Common phone. |
| SHARES_DEVICE_WITH | Symmetric | Common device if lawfully obtained. |
| CONTRACTED_BY | Directed | Contract relationship. |
| SUPPLIER_TO | Directed | Supply relationship. |
| ACQUIRED | Directed | Entity acquired asset. |
| SOLD_TO | Directed | Asset transfer. |
| REPRESENTED_BY | Directed | Professional/legal representation. |
| PAID_BY | Directed | Documented payer relationship, not necessarily direct bank proof. |
| AUTHORIZED_SIGNATORY_OF | Directed | Signing authority; from Person to Organization or Account. *[v0.1.1 · C09]* |
| COMMISSIONER_OF | Directed | Supervisory-board (commissioner) role; from Person to Organization. *[v0.1.1 · C09]* |
| MANAGES | Directed | Day-to-day management of an entity or asset without implying ownership or control. *[v0.1.1 · C09]* |
| USES | Directed | Entity uses or occupies an asset without documented ownership. *[v0.1.1 · C09]* |
| LENDER_TO | Directed | Lending relationship; from lender to borrower. *[v0.1.1 · C09]* |
| LEASED_TO | Directed | Lease of an asset; from lessor to lessee. *[v0.1.1 · C09]* |
| DONATED_TO | Directed | Documented donation; from donor to recipient. *[v0.1.1 · C09]* |
| FUNDED_BY | Directed | Documented funding; from funded entity to funder. *[v0.1.1 · C09]* |
| SHARES_DOMAIN_WITH | Symmetric | Common internet domain or email domain. *[v0.1.1 · C09]* |
| TRANSFERRED_VALUE_TO | Directed | Value transfer from sender to receiver; requires evidence or clearly marked reconstruction; prefer ValueFlow where movement semantics are material. *[v0.1.1 · C09]* |

**Display synonyms mapped to registered values.** *[v0.1.1 · C09]* Relationship names used in the Investigation Methodology §13, the Information Architecture §10 and the Framework Expanded §11.2 that have an exact registered equivalent are display synonyms only and SHALL NOT be stored or exchanged as wire values. "Inverse" means the edge is stored with the registered type and the endpoints swapped.

| **Name used in a document** | **Stored as (wire value)** |
|----|----|
| SHAREHOLDER_OF | OWNS, with an OwnershipInterest (Section 9.2) recording ownership_type and percentage |
| OWNS_ASSET | OWNS (to_entity is the Asset) |
| ACQUIRED_FROM | Inverse of SOLD_TO (`seller --SOLD_TO--> buyer`); ACQUIRED for the buyer-to-asset edge |
| BORROWER_FROM, LOANED_TO | LENDER_TO (BORROWER_FROM is the inverse) |
| USES_ASSET | USES |
| RELATIVE_OF | RELATED_TO, with a familial subtype |
| REPRESENTS, ACTS_FOR | Inverse of REPRESENTED_BY (`principal --REPRESENTED_BY--> agent`); nominee arrangements use OwnershipInterest NOMINEE_ASSERTED or ControlAssertion |
| SHARES_CONTACT_WITH | SHARES_PHONE_WITH or SHARES_ADDRESS_WITH; shared email or web domain uses SHARES_DOMAIN_WITH |
| TRANSFERRED_TO | TRANSFERRED_VALUE_TO |
| RECEIVED_VALUE_FROM | Inverse of TRANSFERRED_VALUE_TO |
| CONTROLS_ASSET | CONTROLS (to_entity is the Asset) |
| BUSINESS_PARTNER_OF | ASSOCIATE_OF, with a business-partner subtype |
| SUBCONTRACTED_TO | Inverse of CONTRACTED_BY (`subcontractor --CONTRACTED_BY--> contractor`) |
| INVESTED_IN | OWNS with an OwnershipInterest (ECONOMIC_INTEREST), or LENDER_TO for debt |
| NOMINEE_FOR | Not a relationship type: OwnershipInterest with ownership_type NOMINEE_ASSERTED, or a ControlAssertion |

# Annex C. Minimal Implementation Object Set

A minimum viable conformant implementation SHOULD support at least the following persistent objects:

``` text
Case
Source
EvidenceItem
EvidenceExtract
Claim                  (v0.1.1 · A10)
VerificationDecision   (v0.1.1 · A10)
Fact
Entity
ResolutionDecision     (v0.1.1 · ER)
Relationship
Asset
Event
ValueFlow
Indicator
TypologyMatch
Hypothesis
IntelligenceGap
Assessment
IntelligenceProduct
Review
Dissemination
AuditEvent
```

# Annex D. Example Analytical Chain

The example below is drawn as a single vertical chain. Relationships are written `from --TYPE--> to`; the Event is a separate node and is not an endpoint of the relationship. *[v0.1.1 · A14]*

``` text
SOURCE
  Government procurement portal
    |
    v
EVIDENCE
  Contract award record
    |
    v
FACT
  Company A received Contract X on 12 May
    |
    v
EVENT
  Contract award (participant: Company A; object: Contract X; date: 12 May)
    |
    v
RELATIONSHIP
  Person B --DIRECTOR_OF--> Company A
    |
    v
INDICATOR
  Related entity acquired property shortly after award
    |
    v
HYPOTHESIS
  Value may have been diverted through related entity
    |
    v
VALUE FLOW (RECONSTRUCTED)
  Contract -> Company A -> related entity -> asset
    |
    v
ASSESSMENT
  Pattern is consistent with procurement-value diversion;
  settlement route remains unknown.
    |
    v
INTELLIGENCE PRODUCT
```

Note: DIRECTOR_OF is directed from Person to Organization (Section 19; Annex B). The v0.1 drawing showed `Company A --DIRECTOR_OF--> Person B`, which reversed the edge; that was an error in the example, not a change in the relationship vocabulary. *[v0.1.1 · A14]*

**CS-AML**

Data Model Specification

Civil Society Anti-Money Laundering & Financial Intelligence Framework

**Version 0.1.1 \| Data Specification (Approved Internal Specification Baseline)**

> **Document status — v0.1.1**
> Version: 0.1.1 — Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec). *[v0.1.1 · A01]*
> Supersedes: CS-AML Data Model Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (decision register and release gates in `CHANGELOG.md`). No implementation test result or independent audit exists yet. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Status**
>
> This document defines the canonical information model for CS-AML v0.1.1. It is intended to be implementation-neutral and SHALL be used as the authoritative semantic reference for database schemas, APIs, graph stores, analytical tooling, exchange formats, and audit records that claim to implement the CS-AML data model. *[v0.1.1 · A01]*

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Data Model Specification |
| Version | 0.1.1 *[v0.1.1 · A01]* |
| Status | Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) *[v0.1.1 · A01]* |
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
| status | enum | Required | Lifecycle status appropriate to object class. |
| classification | enum | Required | Information sensitivity classification (Section 16; `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`). Unknown or missing values fail closed. *[v0.1.1 · A08]* |
| access_labels | array | Conditional | Attribute-based handling labels. |
| case_links | array\<case-id\> | Optional | Contextual case associations; not ownership. |
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
| investigation_questions | ref\[\] | Y | 1..n | Questions to be answered. |
| jurisdictions | code\[\] | N | 0..n | Relevant jurisdictions. |
| time_scope | interval | N | 0..1 | Primary period under review. |
| lead_analyst | principal | Y | 1 | Accountable analyst. |
| risk_rating | enum | Y | 1 | Operational/harm risk rating. |
| closure_reason | enum | N | 0..1 | Reason case closed. |

### Normative rules:

- Case SHALL contain a documented legitimate purpose before collection begins.

- Case title SHALL avoid presuming criminality.

- Case closure SHALL NOT delete reusable entity or evidence objects.

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

## 7.2 EvidenceItem

Represents a preserved evidentiary object such as a file, page image, registry record, transcript, screenshot, export, or structured record.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| source_id | ref | Y | 1 | Origin source. |
| evidence_type | enum | Y | 1 | DOCUMENT, IMAGE, RECORD, TRANSCRIPT, DATASET_ROW, WEB_SNAPSHOT, OTHER *[v0.1.1 · A09]* |
| content_hash | string | Y\* | 0..1 | SHA-256 or equivalent where bytes are available. |
| storage_ref | uri/ref | Y | 1 | Controlled storage location. |
| acquired_at | datetime | Y | 1 | Acquisition time. |
| acquired_by | principal | Y | 1 | Collector. |
| original_format | string | N | 0..1 | MIME/type. |
| verification_status | enum | Y | 1 | UNVERIFIED, SOURCE_VERIFIED, INDEPENDENTLY_CORROBORATED, DISPUTED *[v0.1.1 · A09]* |
| redaction_state | enum | Y | 1 | NONE, WORKING_REDACTION, PUBLICATION_REDACTION *[v0.1.1 · A09]* |

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
| credibility_grade | enum | N | 0..1 | 1-6 information credibility. |
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

## 7.5 Fact

Represents a proposition accepted by the investigation as established to the stated confidence threshold. A Fact is a separate analytical object supported by one or more evidence items (mandatory), optionally by one or more Claims, and by one or more VerificationDecisions; it is not produced by transforming a Claim. *[v0.1.1 · A10]* *[v0.1.1 · C02]*

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| proposition | text/structured | Y | 1 | Established proposition. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence supporting acceptance. |
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

- **Who may act.** An Investigator/Analyst MAY record Claims and propose PROVISIONAL Facts. Moving a Fact to ESTABLISHED SHALL require a Reviewer who is not the proposer. Any authorized case member MAY move a Fact to DISPUTED with supporting evidence. Moving a Fact to SUPERSEDED SHALL require a reference to the replacement Fact (superseded_by). *[v0.1.1 · A10]*

- **Revision.** Every status change SHALL be recorded as a new VerificationDecision; earlier decisions and prior states SHALL be preserved. *[v0.1.1 · A10]* The ESTABLISH, DISPUTE and SUPERSEDE decisions SHALL be created atomically with the corresponding status change by the fact command itself. *[v0.1.1 · C01]*

- **Dependent flagging.** When a Fact becomes DISPUTED or SUPERSEDED, every dependent Assessment and IntelligenceProduct SHALL be flagged `review_required` with a link to the triggering VerificationDecision (`review_trigger_ref`). Published or disseminated products SHALL NOT be mutated; a correction review task SHALL be created instead. History SHALL be preserved. *[v0.1.1 · A10]*

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
| evidence_refs | ref\[\] | Y | 1..n | Evidence or extracts relied on. |
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
| evidence_refs | ref\[\] | Y | 1..n | Evidence considered. |
| confidence | confidence | Y | 1 | Confidence object (HIGH, MODERATE, LOW, INSUFFICIENT_BASIS + basis; Section 14.1). |
| rationale | text | Y | 1 | Why the decision was made. |
| decided_by | principal | Y | 1 | Decision maker. |
| decided_at | datetime | Y | 1 | Decision time. |
| reviewer_ref | principal | C | 0..1 | Required for high-impact MERGE/UNMERGE; SHALL differ from decided_by. |

### Normative rules:

- ResolutionDecision records SHALL be append-only; a mistaken decision is corrected by a later decision (for example UNMERGE reversing a MERGE), not by editing or deleting the earlier one.

- Effects on Entity state: MERGE → each absorbed record becomes MERGED with canonical_parent = surviving_entity_ref, and the survivor becomes RESOLVED; UNMERGE → restored records become SPLIT and relationships/claims are re-attributed according to the recorded history; POSSIBLE_MATCH → a candidate link is recorded with no state change; KEEP_SEPARATE → no state change, and the same pair SHALL NOT be re-suggested unless new evidence is attached; DEFER → state stays or becomes UNRESOLVED.

- Each ResolutionDecision SHALL generate an AuditEvent (action MERGE for MERGE, SPLIT for UNMERGE, otherwise UPDATE).

# 9. Relationship, Ownership, and Control Model

## 9.1 Relationship

Represents a typed, evidence-linked edge between entities. Relationships are first-class objects because their source, time, and confidence may differ.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| from_entity | ref | Y | 1 | Origin node. |
| relationship_type | enum | Y | 1 | Typed semantic relationship. |
| to_entity | ref | Y | 1 | Target node. |
| directionality | enum | Y | 1 | DIRECTED, SYMMETRIC *[v0.1.1 · A09]* |
| valid_from | date/datetime | N | 0..1 | Relationship start. |
| valid_to | date/datetime | N | 0..1 | Relationship end. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence. |
| confidence | confidence | Y | 1 | Confidence. |
| relationship_status | enum | Y | 1 | ASSERTED, ESTABLISHED, DISPUTED, SUPERSEDED *[v0.1.1 · A09]* |

### Normative rules:

- Edges in a graph visualization SHALL retain their evidence links in the underlying model.

- A relationship based only on co-occurrence SHALL NOT be mislabeled as control, ownership, or financial transfer.

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
| valuation_basis | enum/text | N | 0..1 | Registry, market estimate, appraisal, reported value. |
| location_ref | ref | N | 0..1 | Location entity. |

### Normative rules:

- Observed use or association SHALL NOT be represented as ownership without an ownership basis.

## 10.2 Event

Represents a temporally bounded occurrence involving one or more entities.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| event_type | enum | Y | 1 | INCORPORATION, APPOINTMENT, RESIGNATION, CONTRACT_AWARD, ACQUISITION, DISPOSAL, TRANSFER, COURT_EVENT, PAYMENT_EVENT, PUBLICATION, OTHER *[v0.1.1 · A09]* |
| start_time | datetime/date | Y | 1 | Start/occurrence. |
| end_time | datetime/date | N | 0..1 | End if interval. |
| participant_refs | ref\[\] | Y | 1..n | Entities participating. |
| location_ref | ref | N | 0..1 | Location. |
| evidence_refs | ref\[\] | Y | 1..n | Supporting evidence. |
| confidence | confidence | Y | 1 | Confidence. |

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

# 12. Indicator and Typology Model

## 12.1 Indicator

Represents an observed condition relevant to analysis. It SHALL NOT be treated as proof of wrongdoing.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| indicator_code | string | Y | 1 | Stable catalogue or local code. |
| indicator_class | enum | Y | 1 | MECHANISM, CORROBORATING, CONTEXTUAL, DISCONFIRMING, GAP *[v0.1.1 · A09]* |
| description | text | Y | 1 | Observed condition. |
| subject_refs | ref\[\] | Y | 1..n | Affected entities/flows/events. |
| evidence_refs | ref\[\] | Y | 1..n | Evidence. |
| status | enum | Y | 1 | OBSERVED, CORROBORATED, DISPUTED, RETIRED *[v0.1.1 · A09]* |
| confidence | confidence | Y | 1 | Confidence. |

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

### Normative rules:

- A hypothesis SHALL remain open to disconfirmation.

- Rejected hypotheses SHOULD remain auditable rather than deleted.

## 13.2 IntelligenceGap

Represents a material unknown that limits assessment.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| description | text | Y | 1 | Unknown or missing information. |
| importance | enum | Y | 1 | LOW, MEDIUM, HIGH, CRITICAL *[v0.1.1 · A09]* |
| related_refs | ref\[\] | Y | 1..n | Hypotheses/questions affected. |
| collection_feasibility | enum | Y | 1 | AVAILABLE, DIFFICULT, UNAVAILABLE, UNLAWFUL, OUT_OF_SCOPE *[v0.1.1 · A09]* |
| status | enum | Y | 1 | OPEN, PARTIALLY_RESOLVED, RESOLVED, ACCEPTED *[v0.1.1 · A09]* |

## 13.3 Assessment

Represents a reasoned analytical judgment supported by evidence and explicit confidence.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| judgment | text | Y | 1 | Analytical conclusion. |
| scope_refs | ref\[\] | Y | 1..n | Question/hypothesis/subjects addressed. |
| supporting_refs | ref\[\] | Y | 1..n | Facts/indicators/evidence. |
| limitations | text | Y | 1 | Known constraints and gaps. |
| alternative_explanations | text/ref\[\] | Y | 1..n | Material alternatives. |
| confidence | confidence | Y | 1 | Confidence in judgment. |
| review_status | enum | Y | 1 | DRAFT, PEER_REVIEWED, APPROVED, SUPERSEDED *[v0.1.1 · A09]* |
| review_required | boolean | Y | 1 | Set when a supporting Fact becomes DISPUTED or SUPERSEDED (Section 7.5). *[v0.1.1 · A10]* |
| review_trigger_ref | ref | N | 0..1 | VerificationDecision that triggered review_required. *[v0.1.1 · A10]* |
| high_impact_adverse | boolean | N | 0..1 | Defaults to false. True when the assessment is adverse to a named person or organization or is otherwise designated high-impact by the case's review policy. *[v0.1.1 · C10]* |
| disconfirming_searches | structured\[\] | C | 0..n | Recorded searches for information that would disconfirm the judgment. Each entry: searched_for (text), sources_consulted\[\] (1..n; each a source_ref and/or a description), result (text), rationale (text), recorded_by (principal), recorded_at (datetime). At least one entry is required before review approval when high_impact_adverse is true. Append-only. *[v0.1.1 · C10]* |

### Normative rules:

- Assessment language SHALL distinguish known, assessed, and unknown information.

- An Assessment with high_impact_adverse = true SHALL NOT pass review (a Review with decision APPROVE or APPROVE_WITH_CHANGES), and neither SHALL an IntelligenceProduct that depends on it, unless the Assessment has at least one disconfirming_searches entry (SRS-FR-ASM-004). The check is enforced at review approval, not at finalization. Entries SHALL NOT be edited or deleted; a correction is a further entry. *[v0.1.1 · C10]*

- Assessment SHALL NOT imply criminal guilt beyond the available evidence and mandate.

# 14. Confidence and Source Evaluation Model

CS-AML separates source reliability, information credibility, and analyst confidence. Implementations SHALL NOT compress these dimensions into a single unexplained score.

| **Dimension** | **Allowed values** | **Meaning** |
|----|----|----|
| Source reliability | A-F | A highly reliable; B generally reliable; C mixed; D generally unreliable; E unreliable; F unknown |
| Information credibility | 1-6 | 1 independently confirmed; 2 probably true; 3 possibly true; 4 doubtful; 5 improbable; 6 cannot be judged |
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
| applies_to | enum/ref | Y | 1 | Object type/object. |
| retention_period | duration/date | Y | 1 | Retention term. |
| trigger | enum | Y | 1 | CREATION, CASE_CLOSURE, DISSEMINATION, LEGAL_HOLD_RELEASE, OTHER *[v0.1.1 · A09]* |
| disposition | enum | Y | 1 | DELETE, ANONYMIZE, ARCHIVE, REVIEW *[v0.1.1 · A09]* |
| legal_hold | boolean | Y | 1 | Whether disposition suspended. |

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
| DM-I06 | A Relationship of type OWNS/BENEFICIAL_OWNER_OF/CONTROLS SHALL include basis and confidence. |
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
sources
evidence_items
evidence_extracts
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
intelligence_products
reviews
disseminations
audit_events
```

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

An implementation claiming to implement CS-AML Data Model v0.1.1 SHALL demonstrate the following minimum capabilities:

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

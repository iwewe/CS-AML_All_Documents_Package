**CS-AML**

Data Model Specification

Civil Society Anti-Money Laundering & Financial Intelligence Framework

**Version 0.1 \| Normative Data Specification**

> **Status**
>
> This document defines the canonical information model for CS-AML v0.1. It is intended to be implementation-neutral and SHALL be used as the authoritative semantic reference for database schemas, APIs, graph stores, analytical tooling, exchange formats, and audit records that claim CS-AML conformance.

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Data Model Specification |
| Version | 0.1 |
| Status | Normative baseline |
| Applies to | CS-AML Framework v0.1 and derivative implementations |
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
| Evidence | Source, EvidenceItem, EvidenceExtract, Claim, Fact |
| Knowledge graph | Entity, PersonProfile, OrganizationProfile, AccountProfile, Asset, Relationship, Event, Location |
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
| classification | enum | Required | Information sensitivity classification. |
| access_labels | array | Conditional | Attribute-based handling labels. |
| case_links | array\<case-id\> | Optional | Contextual case associations; not ownership. |
| provenance_refs | array\<id\> | Conditional | Links to source/evidence/provenance objects. |
| confidence | object | Conditional | Confidence object where analytical uncertainty exists. |
| valid_from | datetime/date | Optional | Beginning of real-world validity. |
| valid_to | datetime/date | Optional | End of real-world validity. |
| record_version | integer | Required | Monotonic version number for optimistic concurrency/audit. |
| deleted_at | datetime | Optional | Soft-delete/tombstone marker where policy permits. |

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
| status | enum | Y | 1 | Open/answered/retired. |
| answer_summary | text | N | 0..1 | Short evidence-linked answer. |

### Normative rules:

- Questions SHOULD be framed to permit both incriminating and exculpatory answers.

# 7. Source, Evidence, Claim, and Fact Model

## 7.1 Source

Represents the origin or provider of information. A Source describes where information came from; it is not itself the extracted evidentiary proposition.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| source_type | enum | Y | 1 | registry, court_record, media, whistleblower, website, dataset, document, interview, other |
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
| evidence_type | enum | Y | 1 | document, image, record, transcript, dataset_row, web_snapshot, other |
| content_hash | string | Y\* | 0..1 | SHA-256 or equivalent where bytes are available. |
| storage_ref | uri/ref | Y | 1 | Controlled storage location. |
| acquired_at | datetime | Y | 1 | Acquisition time. |
| acquired_by | principal | Y | 1 | Collector. |
| original_format | string | N | 0..1 | MIME/type. |
| verification_status | enum | Y | 1 | unverified, source-verified, independently-corroborated, disputed |
| redaction_state | enum | Y | 1 | none, working_redaction, publication_redaction |

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

Represents a proposition asserted by a source or person. A Claim is not automatically accepted as fact.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| subject_refs | ref\[\] | Y | 1..n | Entities/events referenced. |
| predicate | string | Y | 1 | Controlled or human-readable predicate. |
| object_value | variant | Y | 1 | Claimed value/entity. |
| evidence_extract_refs | ref\[\] | Y | 1..n | Supporting extracts. |
| claimant | ref/string | N | 0..1 | Who makes the assertion. |
| credibility_grade | enum | N | 0..1 | 1-6 information credibility. |
| disputed | boolean | Y | 1 | Whether contested. |

### Normative rules:

- Claims SHALL preserve attribution.

- A source assertion SHALL NOT be promoted to Fact solely because it appears in an official document if the document merely records a third-party allegation.

## 7.5 Fact

Represents a proposition accepted by the investigation as established to the stated confidence threshold.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| proposition | text/structured | Y | 1 | Established proposition. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence supporting acceptance. |
| contradicting_evidence | ref\[\] | N | 0..n | Known contradictory material. |
| fact_status | enum | Y | 1 | provisional, established, superseded, disputed |
| valid_time | interval | N | 0..1 | When proposition is true in real world. |
| confidence | confidence | Y | 1 | Analytical confidence. |

### Normative rules:

- Fact status SHALL be revisable when materially new evidence emerges.

- Fact objects SHALL NOT encode legal guilt or criminal liability unless directly quoting an authoritative adjudication, in which case attribution SHALL be explicit.

# 8. Entity and Identity Model

## 8.1 Entity

Canonical identity-bearing node used across cases.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_type | enum | Y | 1 | person, organization, account, address, domain, phone, email, wallet, property, vehicle, vessel, aircraft, contract, project, other |
| primary_name | string | Y | 1 | Preferred display label. |
| aliases | string\[\] | N | 0..n | Alternative labels. |
| identifiers | identifier\[\] | N | 0..n | Typed external identifiers. |
| resolution_status | enum | Y | 1 | unresolved, resolved, conflicted, merged, split |
| resolution_confidence | confidence | N | 0..1 | Identity match confidence. |
| canonical_parent | ref | N | 0..1 | Target if merged. |
| source_refs | ref\[\] | Y | 1..n | Sources establishing identity. |

### Normative rules:

- Names SHALL NOT be treated as unique identifiers.

- A merged entity SHALL retain links to precursor records and merge rationale.

- Implementations SHALL support reversing a mistaken merge without losing history.

## 8.2 PersonProfile

Extension of Entity for natural persons. Sensitive attributes SHALL only be stored when relevant and lawful.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_id | ref | Y | 1 | Base Entity. |
| birth_date | date/partial | N | 0..1 | Known/partial DOB. |
| nationalities | code\[\] | N | 0..n | Known nationalities. |
| occupation | string\[\] | N | 0..n | Relevant occupation/role. |
| public_official_status | enum | N | 0..1 | none, current, former, unknown; not equivalent to suspicion. |
| sensitive_attribute_notes | restricted text | N | 0..1 | Only if strictly necessary and lawful. |

### Normative rules:

- Protected characteristics SHALL NOT be used as AML indicators by themselves.

## 8.3 OrganizationProfile

Extension for companies, NGOs, agencies, trusts, partnerships, and other organized bodies.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| entity_id | ref | Y | 1 | Base Entity. |
| organization_type | enum | Y | 1 | company, ngo, government, trust, partnership, association, other |
| registration_number | string | N | 0..1 | Legal registration identifier. |
| registration_jurisdiction | code | N | 0..1 | Jurisdiction. |
| incorporation_date | date | N | 0..1 | Formation date. |
| dissolution_date | date | N | 0..1 | If dissolved. |
| registered_address | ref | N | 0..1 | Address entity. |

# 9. Relationship, Ownership, and Control Model

## 9.1 Relationship

Represents a typed, evidence-linked edge between entities. Relationships are first-class objects because their source, time, and confidence may differ.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| from_entity | ref | Y | 1 | Origin node. |
| relationship_type | enum | Y | 1 | Typed semantic relationship. |
| to_entity | ref | Y | 1 | Target node. |
| directionality | enum | Y | 1 | directed/symmetric. |
| valid_from | date/datetime | N | 0..1 | Relationship start. |
| valid_to | date/datetime | N | 0..1 | Relationship end. |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence. |
| confidence | confidence | Y | 1 | Confidence. |
| relationship_status | enum | Y | 1 | asserted, established, disputed, superseded |

### Normative rules:

- Edges in a graph visualization SHALL retain their evidence links in the underlying model.

- A relationship based only on co-occurrence SHALL NOT be mislabeled as control, ownership, or financial transfer.

## 9.2 OwnershipInterest

Specialized relationship for legal or beneficial ownership.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| owner_entity | ref | Y | 1 | Owner/beneficial owner. |
| owned_entity_or_asset | ref | Y | 1 | Company/share/asset. |
| ownership_type | enum | Y | 1 | legal, beneficial, economic_interest, nominee_asserted |
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
| control_basis | enum\[\] | Y | 1..n | voting, appointment, financing, contractual, operational, family_proxy, other |
| control_level | enum | N | 0..1 | minor, significant, dominant, unknown |
| supporting_evidence | ref\[\] | Y | 1..n | Evidence. |
| confidence | confidence | Y | 1 | Confidence. |

# 10. Asset and Event Model

## 10.1 Asset

Represents an item or right with economic value.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| asset_type | enum | Y | 1 | property, vehicle, vessel, aircraft, security, company_share, crypto_asset, precious_metal, luxury_good, intellectual_property, other |
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
| event_type | enum | Y | 1 | incorporation, appointment, resignation, contract_award, acquisition, disposal, transfer, court_event, payment_event, publication, other |
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
| flow_class | enum | Y | 1 | direct, documented, reconstructed, hypothetical |
| flow_type | enum | Y | 1 | payment, contract, subcontract, loan, investment, asset_purchase, asset_sale, grant, donation, dividend, crypto_transfer, value_conversion, other |
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
| indicator_class | enum | Y | 1 | mechanism, corroborating, contextual, disconfirming, gap |
| description | text | Y | 1 | Observed condition. |
| subject_refs | ref\[\] | Y | 1..n | Affected entities/flows/events. |
| evidence_refs | ref\[\] | Y | 1..n | Evidence. |
| status | enum | Y | 1 | observed, corroborated, disputed, retired |
| confidence | confidence | Y | 1 | Confidence. |

## 12.2 TypologyMatch

Represents analytical consistency between case evidence and a catalogue typology.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| typology_id | string/ref | Y | 1 | Catalogue entry. |
| subject_refs | ref\[\] | Y | 1..n | Entities/flows under analysis. |
| indicator_refs | ref\[\] | Y | 1..n | Observed indicators. |
| disconfirming_refs | ref\[\] | N | 0..n | Contrary evidence/indicators. |
| consistency_level | enum | Y | 1 | no_basis, weak, plausible, strong, compelling |
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
| hypothesis_type | enum | N | 0..1 | ownership, control, value_flow, typology, source_of_funds, other |
| supporting_refs | ref\[\] | N | 0..n | Evidence/facts/indicators supporting. |
| contradicting_refs | ref\[\] | N | 0..n | Evidence/facts contradicting. |
| alternative_hypothesis_refs | ref\[\] | N | 0..n | Competing explanations. |
| status | enum | Y | 1 | open, supported, weakened, rejected, inconclusive |
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
| importance | enum | Y | 1 | low, medium, high, critical |
| related_refs | ref\[\] | Y | 1..n | Hypotheses/questions affected. |
| collection_feasibility | enum | Y | 1 | available, difficult, unavailable, unlawful, out_of_scope |
| status | enum | Y | 1 | open, partially_resolved, resolved, accepted |

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
| review_status | enum | Y | 1 | draft, peer_reviewed, approved, superseded |

### Normative rules:

- Assessment language SHALL distinguish known, assessed, and unknown information.

- Assessment SHALL NOT imply criminal guilt beyond the available evidence and mandate.

# 14. Confidence and Source Evaluation Model

CS-AML separates source reliability, information credibility, and analyst confidence. Implementations SHALL NOT compress these dimensions into a single unexplained score.

| **Dimension** | **Allowed values** | **Meaning** |
|----|----|----|
| Source reliability | A-F | A highly reliable; B generally reliable; C mixed; D generally unreliable; E unreliable; F unknown |
| Information credibility | 1-6 | 1 independently confirmed; 2 probably true; 3 possibly true; 4 doubtful; 5 improbable; 6 cannot be judged |
| Analyst confidence | Low / Moderate / High | Overall confidence in analytical judgment, based on evidence quality, independence, consistency, and remaining gaps |

## 14.1 Confidence

Structured confidence object embedded/referenced by analytical objects.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| level | enum | Y | 1 | low, moderate, high |
| basis | text | Y | 1 | Reason for confidence. |
| source_diversity | enum | N | 0..1 | single, multiple_related, multiple_independent |
| material_gaps | ref\[\] | N | 0..n | Gap references. |
| last_reviewed_at | datetime | Y | 1 | Review timestamp. |
| reviewer | principal | N | 0..1 | Reviewer if required. |

# 15. Intelligence Product and Dissemination Model

## 15.1 IntelligenceProduct

Represents an approved analytical output for an identified audience.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| product_type | enum | Y | 1 | financial_intelligence_note, investigation_brief, entity_profile, asset_profile, network_analysis, referral_package, publication_support |
| title | string | Y | 1 | Neutral title. |
| assessment_refs | ref\[\] | Y | 1..n | Underlying assessments. |
| evidence_manifest | ref\[\] | Y | 1..n | Evidence inventory. |
| audience | enum/string\[\] | Y | 1..n | Authorized audience. |
| classification | enum | Y | 1 | Sensitivity. |
| approval_state | enum | Y | 1 | draft, reviewed, approved, disseminated, withdrawn |
| version | string | Y | 1 | Product version. |
| published_at | datetime | N | 0..1 | If published/disseminated. |

## 15.2 Review

Represents peer, legal, privacy, security, or red-team review.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| review_type | enum | Y | 1 | peer, legal, privacy, security, red_team, editorial |
| target_ref | ref | Y | 1 | Object/product reviewed. |
| reviewer | principal | Y | 1 | Reviewer. |
| findings | text/structured | Y | 1 | Review findings. |
| decision | enum | Y | 1 | approve, approve_with_changes, return, reject |
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

| **Classification** | **Meaning** |
|----|----|
| PUBLIC | Suitable for public release after normal review. |
| INTERNAL | Routine internal operational information. |
| SENSITIVE | Could create privacy, reputational, safety, or investigative harm if disclosed. |
| RESTRICTED | High-risk information requiring named-role or case-specific authorization. |
| SOURCE-PROTECTED | Information whose disclosure could identify or endanger a confidential source. |

Access labels MAY add purpose, jurisdiction, source-protection, embargo, legal-review, or compartment restrictions. Implementations SHALL enforce the most restrictive applicable label.

## 16.1 RetentionRule

Represents retention and disposition policy attached to objects or classes.

| **Field** | **Type** | **Req.** | **Cardinality** | **Semantics** |
|----|----|----|----|----|
| rule_id | string | Y | 1 | Policy identifier. |
| applies_to | enum/ref | Y | 1 | Object type/object. |
| retention_period | duration/date | Y | 1 | Retention term. |
| trigger | enum | Y | 1 | creation, case_closure, dissemination, legal_hold_release, other |
| disposition | enum | Y | 1 | delete, anonymize, archive, review |
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
| action | enum/string | Y | 1 | create, update, merge, split, review, approve, disseminate, restrict, delete, export, login_sensitive, other |
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
| DM-I01 | Every Fact SHALL reference at least one EvidenceItem or EvidenceExtract. |
| DM-I02 | Every Indicator SHALL reference supporting evidence and at least one subject object. |
| DM-I03 | Every TypologyMatch SHALL reference one catalogue typology and one or more indicators. |
| DM-I04 | Every Assessment SHALL reference supporting analytical objects and include limitations. |
| DM-I05 | A ValueFlow with flow_class=DIRECT SHALL NOT exist without direct evidence of movement. |
| DM-I06 | A Relationship of type OWNS/BENEFICIAL_OWNER_OF/CONTROLS SHALL include basis and confidence. |
| DM-I07 | Entity merge SHALL preserve precursor identifiers and generate AuditEvent. |
| DM-I08 | External dissemination SHALL reference an approved IntelligenceProduct. |
| DM-I09 | Source-protected information SHALL NOT be exported into lower-classification products without explicit de-identification review. |
| DM-I10 | Deletion/anonymization SHALL respect evidence preservation obligations and legal holds. |

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
facts
entities
entity_identifiers
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

``` text
{
  "id": "vf-7c2e...",
  "object_type": "ValueFlow",
  "schema_version": "0.1",
  "flow_class": "reconstructed",
  "flow_type": "asset_purchase",
  "origin_ref": "org-123",
  "destination_ref": "asset-456",
  "amount": {
    "value": 850000000,
    "currency": "IDR",
    "precision": "estimated"
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
    "level": "moderate",
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

- Machine-generated analytical suggestions SHALL be marked with creator_type=automation/AI and SHALL require human review before becoming an Assessment.

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

An implementation claiming CS-AML Data Model v0.1 conformance SHALL demonstrate the following minimum capabilities:

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

> **Conformance principle**
>
> A schema is not conformant merely because it uses similar table or class names. Conformance depends on preserving the semantics, separations, provenance requirements, and integrity constraints defined by this specification.

# Annex A. Controlled Enumerations (Baseline)

| **Enumeration** | **Baseline values** |
|----|----|
| entity_type | person, organization, account, address, domain, phone, email, wallet, property, vehicle, vessel, aircraft, contract, project, other |
| flow_class | direct, documented, reconstructed, hypothetical |
| confidence.level | low, moderate, high |
| classification | PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, SOURCE-PROTECTED |
| hypothesis.status | open, supported, weakened, rejected, inconclusive |
| typology_match.consistency_level | no_basis, weak, plausible, strong, compelling |
| review.decision | approve, approve_with_changes, return, reject |

# Annex B. Canonical Relationship Vocabulary (Baseline)

| **Relationship** | **Direction** | **Semantics** |
|----|----|----|
| OWNS | Directed | Legal ownership unless subtype says otherwise. |
| BENEFICIAL_OWNER_OF | Directed | Beneficial ownership/economic interest. |
| CONTROLS | Directed | Control without requiring ownership. |
| DIRECTOR_OF | Directed | Corporate role. |
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

# Annex C. Minimal Implementation Object Set

A minimum viable conformant implementation SHOULD support at least the following persistent objects:

``` text
Case
Source
EvidenceItem
EvidenceExtract
Fact
Entity
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
       +---------------------------+
       |                           |
       v                           v
ENTITY / RELATIONSHIP          EVENT
  Company A --DIRECTOR_OF-->   Contract award
  Person B
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

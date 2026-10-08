**CS-AML**

Information Architecture Specification

**Version 0.1.1**

Information organisation, taxonomy, navigation, labeling and findability for the CS-AML Platform

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML Information Architecture Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Status**  
> Draft for Review (Proposed Internal Baseline) — proposed normative information-architecture baseline for MVP 0.1. *[v0.1.1 · A01]* This document defines how information is organised, named, grouped, navigated, linked, searched and found. Interaction behaviour remains governed by the separate CS-AML UX Specification.

| **Document** | **Primary ownership** |
|----|----|
| UX Specification v0.1.1 *[v0.1.1 · A01]* | Interaction behaviour, task flow, feedback, user-facing safety, accessibility. |
| This IA Specification | Object hierarchy, taxonomy, labels, navigation model, information scent, findability, cross-object discovery. |
| Data Model Specification | Canonical object semantics, fields and integrity rules. |
| SRS / PRD | Product and software requirements that IA must satisfy. |
| Technical Stack | Implementation constraints; IA remains technology-neutral where possible. |

*CS-AML Framework Suite • 2026*

# 1. Purpose and Scope

This specification defines the information architecture of the CS-AML platform. Its purpose is to make a complex investigation domain understandable and findable without collapsing analytical distinctions. It converts the canonical data model and product capabilities into a coherent user-facing information system.

> **IA axiom**  
> Case is context; canonical objects are reusable. The information architecture SHALL organise investigation work around context while avoiding unnecessary duplication or imprisonment of entities, evidence and analytical objects inside a single case.

## 1.1 In scope

- Information domains and object hierarchy.

- Primary and secondary navigation model.

- Case workspace information structure.

- Canonical object pages and contextual object views.

- Taxonomy and controlled vocabulary presentation.

- Labeling conventions and naming rules.

- Global and case-scoped search architecture.

- Facets, filters, browse paths and information scent.

- Cross-object links, backlinks and related-object discovery.

- Deep links, canonical URLs and context preservation.

- Role-based entry points and visibility rules.

- Content grouping, metadata hierarchy and progressive disclosure from an IA perspective.

## 1.2 Out of scope

- Micro-interaction behaviour, confirmation dialogs and undo mechanics.

- Visual design system details such as component styling or color tokens.

- Keyboard behaviour and accessibility interaction patterns.

- Backend schema implementation beyond IA-to-data mapping.

- Final analytics algorithms or scoring models.

These are governed by UX, SRS, Data Model, Technology Architecture and implementation specifications.

# 2. IA Design Principles

### IA-P01 Canonical object first

Entity, Evidence, Relationship, Asset, Event, ValueFlow and other reusable objects SHALL have canonical identity independent of any single case.

### IA-P02 Case as context

Case pages organise investigation work, permissions, tasks, questions and analytical outputs; they do not redefine canonical truth objects.

### IA-P03 Provenance is navigable

Users SHALL be able to move from analytical conclusion to supporting evidence and source through explicit information links.

### IA-P04 Uncertainty is structured

Status, confidence, dispute, unknowns and analytical class SHALL be represented as information attributes, not hidden annotations.

### IA-P05 Findability without leakage

Search and browse SHALL help authorised users discover relevant objects while not revealing restricted object existence where policy forbids it.

### IA-P06 Stable terminology

Core labels SHALL map consistently to canonical objects and controlled vocabularies.

### IA-P07 Multiple paths, one object

Users MAY arrive at an object from case, search, graph, timeline or report, but SHALL reach the same canonical record.

### IA-P08 Relationships are first-class

Relationships SHALL be independently addressable information objects with evidence and temporal context, not merely visual graph edges.

### IA-P09 Derived views are not truth stores

Graph, timeline, search result and dashboard views are projections over canonical data.

### IA-P10 Progressive depth

Primary surfaces expose the information needed for decisions; detailed provenance, audit and technical metadata remain available at deeper levels.

# 3. Information Domains

| **Domain** | **Primary objects** | **Purpose** |
|----|----|----|
| Governance & Case | Case, InvestigationQuestion, Task, ReviewGate | Purpose, authority, scope and work coordination. |
| Sources & Evidence | Source, EvidenceItem, EvidenceExtract, DerivedArtifact | Provenance, original material and precise citations. |
| Identity & Network | Entity, Identifier, Relationship, OwnershipInterest, ControlAssertion | Who/what exists and how objects are connected. |
| Assets & Events | Asset, Event | What value-bearing objects exist and what happened when. |
| Value Movement | ValueFlow, ValueFlowLeg | Movement/transformation of economic value. |
| Analytical Reasoning | Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment | How observations become reasoned judgements. |
| Products & Dissemination | IntelligenceProduct, Review, Dissemination | How intelligence is reviewed, versioned and shared. |
| Administration & Assurance | Vocabulary, RetentionPolicy, AuditEvent | How semantics, lifecycle and accountability are governed. |

# 4. Canonical Object Hierarchy

The IA SHALL distinguish canonical objects from contextual associations and derived views. Canonical objects receive stable identifiers and canonical object pages when relevant to users.

``` text
CASE (context)
```

``` text
  ├─ Investigation Question / Scope / Tasks / Gates
```

``` text
  ├─ links to reusable canonical objects
```

``` text
  │    ├─ SOURCE → EVIDENCE → EXTRACT
```

``` text
  │    ├─ ENTITY ↔ RELATIONSHIP ↔ ENTITY
```

``` text
  │    ├─ ENTITY ↔ ASSET
```

``` text
  │    ├─ EVENT
```

``` text
  │    └─ VALUE FLOW
```

``` text
  └─ analytical context
```

``` text
       ├─ INDICATOR / TYPOLOGY MATCH
```

``` text
       ├─ HYPOTHESIS / INTELLIGENCE GAP
```

``` text
       ├─ ASSESSMENT
```

``` text
       └─ INTELLIGENCE PRODUCT / REVIEW / DISSEMINATION
```

## 4.1 Canonical page eligibility

| **Object** | **Canonical page** | **Case-context view** | **Rationale** |
|----|----|----|----|
| Case | Yes | N/A | Primary investigation context. |
| Source | Yes | Yes | Reusable provenance source. |
| EvidenceItem | Yes | Yes | Evidence may support multiple claims/cases. |
| EvidenceExtract | Yes/anchored | Yes | Precise citation to parent evidence. |
| Entity | Yes | Yes | Reusable across cases. |
| Relationship | Yes | Yes | First-class analytical proposition. |
| Asset | Yes | Yes | Reusable object with attribution. |
| Event | Yes | Yes | Temporal fact/context. |
| ValueFlow | Yes | Yes | Reusable value-movement record. |
| Hypothesis | Case-bound | Yes | Analytical reasoning belongs to investigation context. |
| Assessment | Case-bound | Yes | Judgement depends on scope/time/evidence snapshot. |
| IntelligenceProduct | Yes/versioned | Yes | Stable product version and dissemination history. |

# 5. Global Navigation Model

The MVP global navigation SHALL remain small and task-oriented. It should expose major information domains without mirroring backend modules.

| **Primary destination** | **Purpose** | **Typical objects** |
|----|----|----|
| Home | Role-aware entry point, assigned work, recent authorised activity. | Cases, Tasks, Reviews |
| Cases | Browse and enter investigation contexts. | Case |
| Entities | Browse/search canonical people, organisations, accounts, addresses and other entities. | Entity, Identifier |
| Evidence | Browse authorised sources and evidence outside a single case when policy allows. | Source, EvidenceItem |
| Analysis | Entry to typologies, hypotheses/assessments and analytical work queues. | Typology, Hypothesis, Assessment |
| Products | Draft, review and approved intelligence products. | IntelligenceProduct, Review, Dissemination |
| Search | Global permission-aware discovery across canonical objects. | All indexed objects |
| Administration | Policy-controlled vocabularies, retention, user/system governance. | Vocabulary, RetentionPolicy |

> **Navigation restraint**  
> Graph, Timeline and Value Flow SHOULD NOT be primary global destinations in MVP. They are analytical views anchored in a case, entity or selected object set. This prevents derived projections from competing with canonical information domains.

# 6. Role-Based Entry Points

| **Role** | **Default entry emphasis** | **Do not assume** |
|----|----|----|
| Investigator | Assigned cases, tasks, recently viewed evidence/entities. | Access to all organisational investigations. |
| Case Owner | Case health, gate status, pending approvals, unresolved risks. | Administrative system privileges. |
| Reviewer | Review queue, submitted products/assessments, evidence traceability. | Need to browse unrelated cases. |
| Evidence Custodian | Ingestion queue, integrity status, derivatives, retention/hold. | Authority to alter analytical judgement. |
| Data Steward | Entity match/merge queue, identity-quality issues. | Automatic visibility into protected sources. |
| Source Handler | Protected-source workspace and controlled handoff. | Protected identity in global search. |
| Admin/Auditor | Policy/configuration/audit entry points. | Analytical edit rights. |

> **Roles and classification.** Role entry points shape default emphasis only; they do not grant access to any classification level. Visibility is decided by server-side policy against the object's classification level (`PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`) plus its access labels. No role by itself grants `RESTRICTED` access (named-role or case-specific authorization is required), and `SOURCE_PROTECTED` material stays in the protected-source workspace (Source Handler) and out of general navigation and search. Unknown or missing classification fails closed. *[v0.1.1 · A08]*

# 7. Case Workspace Information Architecture

A case workspace SHALL organise investigation context around a stable case header plus domain views. Exact visual interaction is governed by UX; this section defines information grouping and hierarchy.

| **Case section** | **Information responsibility** | **Primary objects** |
|----|----|----|
| Overview | Question, purpose, status, owner, classification, scope summary, gate state. | Case, InvestigationQuestion |
| Work | Tasks, assignments, milestones and case activity. | Task, AuditEvent |
| Sources & Evidence | Case-linked sources, evidence, extracts and derivatives. | Source, EvidenceItem, EvidenceExtract |
| Entities & Assets | Case-linked canonical entities, identifiers, relationships and assets. | Entity, Relationship, Asset |
| Timeline | Chronological projection of relevant events. | Event |
| Value Flows | Case-linked value movement and multi-leg chains. | ValueFlow, ValueFlowLeg |
| Analysis | Indicators, typology matches, hypotheses, gaps and assessments. | Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment |
| Products | Draft/reviewed products, reviews and dissemination records. | IntelligenceProduct, Review, Dissemination |

## 7.1 Case context persistence

When a user opens a canonical entity, evidence item or relationship from within a case, the system SHOULD preserve the originating case context so case-specific associations and analytical relevance can be shown without creating a duplicate object.

# 8. Canonical Object Page Pattern

Canonical object pages SHOULD use a consistent information hierarchy regardless of object type.

| **Layer** | **Contents** | **Rule** |
|----|----|----|
| Identity | Canonical name/title, stable ID, object type, status/classification. | Always visible near page header. |
| Core properties | Object-specific primary attributes. | Prioritise authoritative/current values while retaining conflicts. |
| Provenance | Source/evidence basis, creation and verification context. | Directly reachable from material assertions. |
| Relationships | Inbound/outbound links to other canonical objects. | Permission-aware and typed. |
| Case contexts | Authorised cases in which the object is relevant. | Case association must not imply guilt. |
| History | Temporal changes, supersession, merge/version history. | Do not overwrite history. |
| Audit/technical | Audit trail and system metadata where role permits. | Progressively disclosed. |

# 9. Entity Information Architecture

## 9.1 Entity taxonomy

| **Top-level entity family** | **Examples** | **Label rule** |
|----|----|----|
| Person | Individual, public official, professional intermediary. | Use “Person”, not suspect/target as type. |
| Organisation | Company, nonprofit, agency, partnership, informal organisation. | Specific subtype may be shown as metadata. |
| Account/Instrument | Bank account, payment account, virtual asset wallet. | Avoid implying ownership unless relationship supports it. |
| Place/Address | Registered address, property address, operational location. | Separate location object from ownership assertion. |
| Digital Identifier | Email, phone, domain, username/device identifier where lawful. | Show source and verification status. |
| Other Legal/Economic Object | Contract, project or instrument when modelled as entity-like object. | Prefer dedicated domain objects where defined. |

## 9.2 Entity page sections

- Identity summary and status.

- Aliases and identifiers with provenance.

- Relationships grouped by relationship family and time.

- Assets and value-flow participation.

- Events/timeline references.

- Evidence and source support.

- Case contexts.

- Merge/unmerge and identity-resolution history for authorised roles.

## 9.3 Entity status labels

| **Status** | **Meaning** |
|----|----|
| Candidate | Possible entity record or unresolved identity. |
| Probable | Evidence suggests identity but material uncertainty remains. |
| Confirmed | Identity resolution is sufficiently supported for current analytical purpose. |
| Disputed | Material conflicting evidence exists. |
| Unresolved | Available information is insufficient to decide. |

# 10. Relationship, Ownership and Control Architecture

Relationships are first-class records and SHALL be discoverable from both endpoints as well as case context.

| **Relationship family** | **Examples** | **Required information scent** |
|----|----|----|
| Governance/role | DIRECTOR_OF, EMPLOYED_BY, REPRESENTED_BY | Role type, organisation, valid time, evidence/status. |
| Ownership | OWNS, BENEFICIAL_OWNER_OF | Owner/asset, percentage if known, direct/indirect, evidence. |
| Control | CONTROLS, MANAGES, USES | Control basis distinct from legal ownership. |
| Commercial | SUPPLIER_TO, CONTRACTED_BY | Counterparty, contract/project context, dates. |
| Personal/association | RELATIVE_OF, ASSOCIATE_OF | Use carefully; provenance and relevance required. |
| Transfer/value | PAID_BY, TRANSFERRED_TO, ACQUIRED, SOLD_TO | Prefer ValueFlow/Event where movement semantics are material. |

> **Graph rule**  
> A graph edge SHALL resolve to a canonical Relationship, OwnershipInterest, ControlAssertion or ValueFlow object. The graph itself is never the sole record of the connection.

# 11. Asset and Event Architecture

## 11.1 Asset information

- Asset identity/type and identifiers.

- Location/jurisdiction where relevant.

- Legal ownership, beneficial ownership, control, use and association as distinct relationships.

- Valuation records with source/date/method where present.

- Events affecting acquisition, transfer, sale, seizure or status.

- Supporting evidence and case contexts.

## 11.2 Event taxonomy

| **Event family** | **Examples** | **Date semantics** |
|----|----|----|
| Organisation | incorporation, director change, dissolution | Exact/range/precision must be explicit. |
| Procurement/contract | award, subcontract, payment milestone | Link project/contract/entity/evidence. |
| Asset | acquisition, transfer, sale, valuation event | Do not infer causation from temporal proximity. |
| Legal | court filing, order, sanction, administrative action | Jurisdiction and source are important. |
| Analytical | case-opened/reviewed may appear in case activity, not factual event timeline by default | Separate investigation activity from subject-world events. |

# 12. Value-Flow Information Architecture

ValueFlow is a canonical analytical object representing movement or transformation of economic value. Its information architecture SHALL preserve evidentiary class.

| **Class** | **IA meaning** | **Required label** |
|----|----|----|
| DIRECT | Direct transaction evidence supports the movement. | DIRECT |
| DOCUMENTED | Documented economic relationship/obligation supports the movement but not necessarily transaction-level proof. | DOCUMENTED |
| RECONSTRUCTED | Analyst reconstructs probable movement from linked facts and events. | RECONSTRUCTED |
| HYPOTHETICAL | Proposed flow used for hypothesis testing. | HYPOTHETICAL |

The required labels are the `flow_class` wire values (UPPER_SNAKE_CASE, derived from the Data Model Annex A registry); translated display labels MAY be shown alongside them but SHALL NOT replace or merge classes. *[v0.1.1 · A09]*

## 12.1 ValueFlow page structure

- Origin and destination.

- Mechanism/type.

- Value, currency, range/unknown state and date/precision.

- Flow class and confidence/status.

- Evidence and source basis for each leg.

- Related contract, asset, event and entity objects.

- Case contexts and analytical usage.

## 12.2 Multi-leg chain structure

A chain is a view over ordered ValueFlowLeg objects. Each leg retains independent evidence, class and confidence. The chain label SHALL not override per-leg semantics.

# 13. Analytical Reasoning Architecture

``` text
OBSERVATION / FACT
```

``` text
      ↓
```

``` text
INDICATOR ↔ COUNTER-INDICATOR
```

``` text
      ↓
```

``` text
TYPOLOGY MATCH (consistency, not proof)
```

``` text
      ↓
```

``` text
HYPOTHESES + CONTRADICTIONS + GAPS
```

``` text
      ↓
```

``` text
ASSESSMENT + CONFIDENCE
```

``` text
      ↓
```

``` text
INTELLIGENCE PRODUCT
```

## 13.1 Typology information

- Catalogue entry ID/version/name.

- Mechanism and objective.

- Observables and indicators.

- Counter-indicators / common false positives.

- Relevant evidence classes and analytical cautions.

- Case-specific TypologyMatch records SHALL remain separate from catalogue definition.

## 13.2 Hypothesis and assessment grouping

| **Object** | **Grouping rule** | **Cross-links** |
|----|----|----|
| Hypothesis | Case-bound; grouped by status and analytical question. | Supporting/contradicting evidence, indicators, gaps. |
| IntelligenceGap | Grouped by open/closed and materiality. | Hypothesis/assessment/tasks. |
| Assessment | Versioned by case/question; not global truth about an entity. | Hypotheses, evidence basis, confidence, alternatives, product versions. |

# 14. Intelligence Product and Dissemination Architecture

## 14.1 Product taxonomy

| **Product type** | **Primary use** |
|----|----|
| Financial Intelligence Note | Concise assessment for internal or controlled external use. |
| Entity Profile | Structured identity, relationships, assets and provenance summary. |
| Asset Profile | Asset ownership/control/use and relevant events/value context. |
| Network Analysis | Evidence-backed network findings and analytical interpretation. |
| Referral Package | Structured package for competent authority or trusted recipient. |
| Case Report | Comprehensive investigation record and conclusions. |

## 14.2 Version structure

Each product SHALL have stable Product ID plus immutable version identity. Current, superseded and retracted versions SHALL be distinguishable. Dissemination records link to the exact version shared, not merely the product family.

## 14.3 Dissemination metadata

- Recipient / recipient class.

- Purpose.

- Date/time.

- Product version.

- Classification/handling restrictions.

- Included/excluded evidence scope.

- Approver and approval reference.

- Correction/update status where relevant.

# 15. Taxonomy and Controlled Vocabulary

Taxonomy SHALL distinguish system-defined canonical categories from organisation-defined controlled vocabularies and analyst-entered free text.

| **Layer** | **Examples** | **Governance** |
|----|----|----|
| Canonical system enum | ValueFlow class, analytical status, product lifecycle state, confidence level (`HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`), classification level (`PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`). | Versioned through software/data model (Data Model Annex A registry); wire values are UPPER_SNAKE_CASE and display labels are separate and translatable; changes require migration review. *[v0.1.1 · A08, A09]* |
| Framework catalogue | CS-AML typology IDs and classes. | Versioned framework release. |
| Controlled vocabulary | Relationship types, asset types, event types, access labels (e.g. purpose, jurisdiction, embargo, legal-review, compartment). | Admin-managed with stable IDs and effective dates. Classification levels are a canonical system enum, not an admin-managed vocabulary. *[v0.1.1 · A08]* |
| Reference taxonomy | Jurisdiction lists, currencies, organisation types. | May map to external standards where appropriate. |
| Free text | Notes, rationale, narrative assessment. | Not used where controlled semantics are required. |

## 15.1 Vocabulary rules

- Labels MAY change, stable IDs SHOULD not.

- Deprecated terms SHALL remain interpretable on historical records.

- Synonyms MAY support search but SHALL not silently merge distinct concepts.

- Relationship direction SHALL be explicit and user-facing labels understandable in both directions where needed.

- Taxonomies SHALL avoid loaded terms such as “criminal”, “dirty”, or “suspicious entity” as structural types unless legally established and contextually required.

# 16. Labeling System

## 16.1 Label priorities

| **Priority** | **Rule** | **Example** |
|----|----|----|
| 1 | Use domain language that matches framework/data objects. | “Evidence”, “Hypothesis”, “Assessment”. |
| 2 | Prefer concrete nouns for destinations and objects. | “Entities” rather than “Network Intelligence Centre”. |
| 3 | Use verbs for actions, not destinations. | “Add evidence”, “Create relationship”. |
| 4 | Avoid accusatory labels for neutral states. | “Case subject” only as contextual role, not entity type. |
| 5 | Show uncertainty in labels when material. | “Candidate match”, “Reconstructed flow”. |

## 16.2 Naming pattern

``` text
Object type + canonical label + status/context
```

``` text
Example:
```

``` text
Company · PT Example Nusantara · Confirmed
```

``` text
Value Flow · Company A → Company B · RECONSTRUCTED
```

``` text
Assessment · Procurement ownership question · Moderate confidence
```

# 17. Search and Findability Architecture

## 17.1 Search scopes

| **Scope** | **Purpose** | **Default boundary** |
|----|----|----|
| Global | Find authorised canonical objects across platform. | User permissions and object classification. |
| Case | Find objects associated with current case. | Case membership plus object permission. |
| Evidence/document | Find text/citations within authorised evidence. | Evidence access and derivative visibility. |
| Entity | Find identifiers/relationships/related evidence for one entity. | Canonical entity permissions. |
| Product | Find products by case/type/status/version/recipient metadata. | Product/dissemination permissions. |

## 17.2 Search result architecture

- Result type SHALL be explicit.

- Primary label plus disambiguating metadata SHOULD be present.

- Relevant status/classification SHALL be visible when authorized.

- Search snippets SHALL not expose restricted content.

- Results SHALL resolve to canonical objects, not stale search copies.

- Case-context search MAY show case relevance alongside canonical object identity.

## 17.3 Facets

| **Object family** | **Minimum useful facets** |
|----|----|
| Cases | status, owner, classification, jurisdiction, date |
| Entities | type, jurisdiction, status, identifier type, linked case |
| Evidence | source type, file type, date, integrity/verification state, case |
| Relationships | relationship type, status, valid time, case |
| Events | event type, date range, entity/asset |
| Value flows | class, mechanism, currency, date, origin/destination |
| Products | type, status, reviewer, classification, date |

# 18. Cross-Object Discovery and Backlinks

Every canonical object SHOULD expose meaningful inbound and outbound associations, subject to permissions. Backlinks reduce the need for analysts to remember where an object was used.

| **Object** | **High-value related information** |
|----|----|
| Evidence | source, extracts, facts/claims, entities mentioned, relationships supported, assessments/products citing it |
| Entity | identifiers, relationships, assets, events, value flows, evidence, case contexts |
| Relationship | two endpoints, evidence, events, case contexts, graph views |
| ValueFlow | origin/destination, legs, evidence, events, related assets/contracts, hypotheses |
| Hypothesis | supporting/contradicting evidence, indicators, gaps, assessment |
| Assessment | hypotheses, evidence chain, gaps, reviews, product versions |

# 19. Deep Linking and Canonical URLs

Information objects that users need to cite, review or share internally SHOULD have stable deep links. URL design is implementation-specific, but semantics SHALL distinguish canonical object identity from case context.

``` text
Conceptual pattern:
```

``` text
/objects/entities/{entity_id}
```

``` text
/cases/{case_id}/entities/{entity_id}   # contextual view or wrapper
```

``` text
/evidence/{evidence_id}#page=12         # precise citation where supported
```

``` text
/products/{product_id}/versions/{version_id}
```

- Deep links SHALL re-check authorization at access time.

- A case-context URL SHALL not create a second canonical entity.

- Precise evidence anchors SHOULD preserve page/region/citation location when technically possible.

- Links in exported intelligence products SHOULD use stable identifiers even when interactive URLs are not externally available.

# 20. Information Scent and Context Cues

Users should understand what an item is and why it is relevant before opening it. Information scent SHALL rely on concise metadata, not sensational visual emphasis.

| **Surface** | **Recommended scent** |
|----|----|
| Entity result | type, canonical name, jurisdiction/identifier, status, relevant case count if permitted |
| Evidence result | title/file, source, date, case relevance, verification state |
| Relationship | relationship label, endpoints, time, evidence count/status |
| Value flow | origin → destination, class, value/date if known, evidence count |
| Hypothesis | statement, status, support/contradiction counts, open gaps |
| Product | type, case, version, status, classification |

# 21. Permission-Aware Information Architecture

Permissions shape what information exists from the user’s perspective. IA SHALL not rely on disabled links or empty sections to reveal restricted objects.

- Restricted objects MAY be completely absent from navigation/search when policy requires non-disclosure.

- If the user may know an object exists but not see details, the system SHOULD show a policy-safe placeholder rather than misleading “not found”.

- Counts, facets and relationship degree SHALL be permission-aware so they do not leak hidden objects.

- Protected-source identity SHALL not appear in general entity indexes, autocomplete, search snippets, graph labels or exported object lists.

- Cross-case backlinks SHALL only list cases the user is allowed to know exist.

# 22. Derived Views: Graph, Timeline and Dashboards

Derived views are navigation and analytical projections. They SHALL remain anchored to canonical objects and respect the same permissions.

| **Derived view** | **IA role** | **Canonical return path** |
|----|----|----|
| Investigation Graph | Explore network topology and evidence-backed relationships. | Node → canonical entity/asset; edge → relationship/value-flow record. |
| Timeline | Explore chronology and temporal clustering. | Item → canonical Event or related object. |
| Value-flow diagram | Explore movement/transformation of value. | Leg/edge → ValueFlow record and evidence. |
| Dashboard/summary | Orient user to work state and notable counts. | Metric/list item → underlying canonical collection. |

> **Derived-view safeguard**  
> No graph node size, dashboard ranking, timeline proximity or search relevance score SHALL become an implicit semantic category such as “most suspicious”. Analytical scoring, if later introduced, requires explicit separate specification and explanation.

# 23. Content Lifecycle, Versioning and History

| **Information type** | **Lifecycle IA requirement** |
|----|----|
| Evidence original | Immutable identity; new file creates new object/version rather than overwrite. |
| Entity | Canonical identity persists through edits; merge/unmerge/supersession history remains discoverable. |
| Controlled vocabulary | Stable term IDs; deprecated terms remain interpretable. |
| Assessment | Immutable published/final versions; later revision is a new version. |
| Intelligence product | Version chain with current/superseded/retracted states. |
| Dissemination | Immutable record of exact shared version and recipient context. |

# 24. IA Requirements Catalogue

| **ID** | **Normative requirement** |
|----|----|
| IAR-001 | Canonical reusable objects SHALL have stable identifiers independent of case context. |
| IAR-002 | Case workspace SHALL link to canonical objects rather than duplicate them. |
| IAR-003 | Global navigation SHALL expose information domains, not backend service/module names. |
| IAR-004 | Graph, timeline and flow diagrams SHALL be derived views with canonical return paths. |
| IAR-005 | Relationship objects SHALL be independently addressable and provenance-bearing. |
| IAR-006 | Search SHALL be permission-aware at result, snippet, count and facet levels. |
| IAR-007 | Protected-source identities SHALL be excluded from general indexes and navigation. |
| IAR-008 | Labels SHALL preserve analytical uncertainty and avoid accusatory structural terminology. |
| IAR-009 | Controlled vocabularies SHALL use stable IDs and retain historical semantics. |
| IAR-010 | Deep links SHALL distinguish canonical identity from case-context views. |
| IAR-011 | Every material assessment SHALL expose navigable links toward supporting evidence chain. |
| IAR-012 | Product/dissemination records SHALL resolve to exact immutable product version. |
| IAR-013 | Unknown values SHALL be represented distinctly from none/zero/false. |
| IAR-014 | Cross-case links SHALL not imply access or reveal restricted case existence. |
| IAR-015 | Entity, relationship and value-flow status/class SHALL be available as structured metadata for search/filter/browse. |
| IAR-016 | Historical/superseded records SHALL remain discoverable to authorized reviewers without being confused with current state. |
| IAR-017 | Case-context relevance SHALL be presented separately from canonical object properties. |
| IAR-018 | IA changes to canonical labels/taxonomies SHALL be version-controlled and reviewed for migration impact. |
| IAR-019 | Browse and search paths SHALL converge on the same canonical object. |
| IAR-020 | No derived ranking or visualization attribute SHALL silently become a semantic guilt/risk classification. |

# 25. IA-to-UX Handoff Contract

| **Decision area** | **IA owns** | **UX owns** | **Joint acceptance** |
|----|----|----|----|
| Navigation | Destinations, hierarchy, route semantics, information grouping. | Interaction of menus/tabs, responsive behaviour, focus/keyboard state. | Users can predict where information lives and move without losing task context. |
| Labels | Canonical destination/object labels and taxonomy terms. | Microcopy, action wording, validation/help text. | Terminology is consistent and comprehensible. |
| Object pages | Information hierarchy and related-object sections. | Interaction patterns, editing behaviour, feedback/error states. | Canonical identity and provenance remain clear during tasks. |
| Search | Scopes, facets, result metadata, permission-aware findability. | Search input interaction, query feedback, empty/loading/error states. | Authorised users can find objects without leakage. |
| Graph/timeline | What canonical information each projection represents. | Manipulation, selection, zoom/filter interactions and accessibility. | Projection never becomes detached from canonical semantics. |

# 26. IA Validation and Testing

## 26.1 Validation methods

- Tree testing for primary destinations and case workspace hierarchy.

- Card sorting for labels and controlled-vocabulary groupings where domain language is uncertain.

- Findability tasks across case, entity, evidence and product scenarios.

- Permission leakage tests for hidden objects, counts, facets and backlinks.

- Cross-object traceability tests from product → assessment → hypothesis → evidence → source.

- Deep-link tests for canonical versus case-context identity.

- Terminology consistency audit against Data Model, Typology Catalogue and UX Specification.

## 26.2 MVP IA acceptance scenarios

1.  An investigator can locate a case, find its evidence, open a cited entity, inspect a relationship and return to the case without encountering duplicate object identities.

2.  A reviewer can start from an intelligence product and navigate backward to assessment, hypothesis, evidence extract and original evidence/source.

3.  A data steward can find an entity from global search, identify conflicting identifiers, inspect merge history and see authorised case contexts.

4.  A user without access to a sensitive case cannot infer that case through search counts, backlinks or graph degree.

5.  A protected-source identity is absent from global search and ordinary case navigation while source-derived evidence remains usable.

# 27. IA Definition of Done

- Canonical object and case-context responsibilities are documented.

- Primary navigation and case workspace hierarchy are defined.

- Object taxonomy and controlled-vocabulary boundaries are defined.

- Search scopes, facets and result information scent are specified.

- Cross-object links/backlinks and deep-link semantics are specified.

- Permission-aware findability and protected-source exclusions are verified.

- Terminology matches the canonical data model and UX Specification.

- Representative tree/findability tests pass for MVP workflows (target; no such tests have been run at this baseline). *[v0.1.1 · A01]*

- No IA decision converts analytical status or derived ranking into implicit guilt/risk classification.

# 28. Traceability to CS-AML Suite

| **IA area** | **Primary upstream references** |
|----|----|
| Canonical objects | Data Model Specification; SRS DR requirements. |
| Case workspace | PRD MVP journey; Investigation Methodology; MVP Engineering E2. |
| Evidence hierarchy | Data Model; Control Guide EVD/SRC controls; UX Evidence section. |
| Entity/network hierarchy | Data Model; Control Guide ENT/REL/AST; MVP Engineering E4. |
| Value-flow structure | Data Model; Methodology; UX Follow-the-Value; E5. |
| Analytical reasoning | Typology Catalogue; Investigation Methodology; UX analytical sections; E6. |
| Search/graph | SRS SCH/GRF; Technology Architecture; E7. |
| Products/dissemination | Methodology; Control Guide QUA/DIS; UX review/dissemination; E8. |
| Permissions/findability | Technology Architecture; Control Guide SEC; UX permission handling; E1. |

# Annex A — Reference Navigation Tree

``` text
HOME
```

``` text
CASES
```

``` text
  └─ Case Workspace
```

``` text
      ├─ Overview
```

``` text
      ├─ Work
```

``` text
      ├─ Sources & Evidence
```

``` text
      ├─ Entities & Assets
```

``` text
      ├─ Timeline
```

``` text
      ├─ Value Flows
```

``` text
      ├─ Analysis
```

``` text
      └─ Products
```

``` text
ENTITIES
```

``` text
EVIDENCE
```

``` text
ANALYSIS
```

``` text
  ├─ Typology Catalogue
```

``` text
  ├─ Hypotheses / Assessments (authorised work queues)
```

``` text
  └─ Review queues where appropriate
```

``` text
PRODUCTS
```

``` text
SEARCH
```

``` text
ADMINISTRATION
```

This tree is the MVP IA baseline, not a pixel-level navigation design. UX determines interaction presentation; engineering may implement routes differently as long as semantic hierarchy and canonical identity rules remain conformant.

# Annex B — Core Label Dictionary

| **Canonical label** | **Meaning / usage** |
|----|----|
| Case | Investigation context with question, scope, roles and analytical work. |
| Source | Origin of information or evidence. |
| Evidence | Preserved material used to support or challenge propositions. |
| Evidence Extract | Precise excerpt/location linked to parent evidence. |
| Entity | Reusable person/organisation/account/address/etc. identity object. |
| Relationship | Evidence-bearing typed connection between objects. |
| Asset | Value-bearing object such as property, shares, vehicle, vessel or crypto asset. |
| Event | Time-bounded occurrence linked to evidence. |
| Value Flow | Movement/transformation of economic value with explicit evidentiary class. |
| Indicator | Observed fact/pattern relevant to analysis; not proof. |
| Typology | Reference pattern/mechanism from the CS-AML catalogue. |
| Hypothesis | Testable explanation. |
| Intelligence Gap | Material unknown that could change assessment. |
| Assessment | Analyst judgement with confidence, basis, alternatives and gaps. |
| Claim | Attributed assertion from a source; never shown as a fact without a recorded verification decision. *[v0.1.1 · A10]* |
| Fact | Proposition promoted from claims/evidence by a recorded verification decision; status Provisional, Established, Disputed or Superseded. *[v0.1.1 · A10]* |
| Confidence | High, Moderate, Low, Insufficient basis (wire `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`). Insufficient basis is not a level below Low and is never shown as Low, blank or zero. *[v0.1.1 · A09]* |
| Classification | Public, Internal, Sensitive, Restricted, Source-protected (wire `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`); access labels are additional restrictions. *[v0.1.1 · A08]* |
| Intelligence Product | Versioned analytical output intended for review/use/dissemination. |
| Dissemination | Controlled record of external/internal sharing of a specific product version. |

# Annex C — Information Architecture Change Record

| **Field** | **Description** |
|----|----|
| Change ID | Stable IA change identifier. |
| Affected labels/objects | Navigation, taxonomy, labels or hierarchy affected. |
| Reason | User research, product change, data-model change, legal/security requirement. |
| Migration impact | Routes, saved links, taxonomy mappings, historical labels, search facets. |
| UX impact | Interaction or usability implications requiring UX review. |
| Data impact | Canonical schema or vocabulary impact requiring data review. |
| Security impact | Permission/findability implications. |
| Decision / approver | Approved, rejected or deferred with owner/date. |
| Effective version | IA release in which the change applies. |

**CS-AML**

**Product & Feature Specification**

Version 0.1.1

> **Document status — v0.1.1**  
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*  
> Supersedes: CS-AML Product & Feature Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.  
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.  
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.  
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).


Civil Society Financial Intelligence / AML Investigation Platform

Status: Draft for Review (Proposed Internal Baseline) — proposed product baseline / implementation specification *[v0.1.1 · A01]*

> **Product axiom**  
> The platform SHALL help analysts discover, structure, test, explain, review, and disseminate financial intelligence without converting uncertainty into fact or replacing accountable human judgement.

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Product & Feature Specification |
| Version | 0.1.1 |
| Status | Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]* |
| Primary audience | Product owners, investigators, analysts, architects, developers, security/privacy reviewers, QA |
| Normative inputs | CS-AML Framework v0.1.1; Goals & Non-Goals v0.1.1; Typology Catalogue v0.1.1; Investigation Methodology v0.1.1; Data Model Specification v0.1.1; Control Implementation Guide v0.1.1; Technology Architecture v0.1.1 (Markdown, `Documents/*_v0.1.1.md`) |
| Normative language | SHALL/MUST = mandatory; SHOULD = recommended; MAY = optional |
| Primary output | Prioritised, testable product backlog and release scope |

# 1. Purpose and Product Definition

This specification translates the CS-AML normative framework into a buildable software product. It defines the product boundary, user roles, capabilities, functional features, acceptance criteria, integrations, non-functional requirements, release priorities, and traceability expectations for a Civil Society Financial Intelligence / AML Investigation Platform.

> **Product definition**  
> CS-AML Platform is a civil-society financial intelligence and investigation system. It is NOT a bank transaction-monitoring system, a law-enforcement case system, a guilt-determination engine, or a general-purpose mass-surveillance platform.

**The product SHALL enable a structured chain:**

SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT

The product SHALL preserve reusable truth-bearing objects—especially Evidence, Entity, Relationship, Asset, Event, and ValueFlow—across cases while preserving case compartmentalisation and access controls.

# 2. Product Goals and Success Outcomes

| **ID** | **Goal** | **Outcome** |
|----|----|----|
| PG-01 | Structure investigations | Replace ad-hoc folders, spreadsheets, screenshots, and disconnected notes with a controlled investigation workspace. |
| PG-02 | Preserve provenance | Make every material analytical conclusion traceable to source and evidence. |
| PG-03 | Follow the value | Support direct, documented, reconstructed, and hypothetical value-flow analysis without pretending public-source inference is bank-transaction evidence. |
| PG-04 | Resolve entities safely | Allow identity/entity consolidation while retaining confidence, evidence, reversibility, and audit history. |
| PG-05 | Test hypotheses | Support competing explanations, disconfirming evidence, unknowns, and confidence-based assessments. |
| PG-06 | Apply typologies carefully | Use typology catalogues as analytical references, not proof of wrongdoing. |
| PG-07 | Create decision-useful intelligence | Generate reviewable intelligence notes, network analysis, referral packages, and publication-ready outputs. |
| PG-08 | Protect people and sources | Apply minimisation, compartmentalisation, least privilege, source protection, secure dissemination, and retention controls. |
| PG-09 | Enable collaboration | Support accountable multi-analyst workflows, peer review, structured handover, and controlled partner sharing. |
| PG-10 | Remain extensible | Integrate specialised external tools rather than rebuilding mature capabilities unnecessarily. |

# 3. Product Non-Goals

| **ID** | **Non-goal** | **Rule** |
|----|----|----|
| NG-01 | No autonomous guilt determination | The system SHALL NOT determine that a person committed money laundering or another crime. |
| NG-02 | No unrestricted surveillance | The product SHALL NOT be designed for bulk collection of people unrelated to a defined investigation purpose. |
| NG-03 | No unauthorised acquisition | The product SHALL NOT provide hacking, credential theft, unauthorised interception, or covert access functions. |
| NG-04 | No bank-core replacement | The product is not a bank AML transaction-monitoring or customer-onboarding system. |
| NG-05 | No evidence laundering | AI, graph scores, data enrichment, or imported intelligence SHALL NOT silently become verified fact. |
| NG-06 | No forced monolith | Search, graph, OCR, sanctions screening, and blockchain analytics MAY be delegated to external components. |

# 4. User Roles and Personas

| **Role** | **Primary responsibility** |
|----|----|
| Investigator / Analyst | Opens and develops cases; registers sources/evidence; creates entities, relationships, events, flows, hypotheses, and assessments. |
| Case Owner / Investigation Lead | Owns scope, lifecycle gates, prioritisation, escalation, closure, and accountability. |
| Reviewer / Red-Team Analyst | Independently tests identity resolution, evidence basis, alternative explanations, confidence, and wording. |
| Evidence Custodian | Preserves originals, hashes, derivative lineage, retention status, and evidence integrity. |
| Data Steward | Maintains entity quality, controlled vocabularies, merge/split history, and data-quality remediation. |
| Privacy / Legal Reviewer | Reviews sensitive collection, personal-data necessity, publication/referral risk, retention, and lawful access. |
| Security Administrator | Manages IAM, access policy, secrets, audit, secure storage, backup, incident response, and system hardening. |
| Partner / External Reviewer | Receives only authorised cases/products/objects under explicit sharing controls. |
| Platform Administrator | Manages configuration, connectors, taxonomy, templates, feature flags, and system operations without automatic access to case content. |
| Auditor / Assurance Reviewer | Tests controls and reconstructs material analytical decisions without altering investigation content. |

# 5. Product Design Principles

| **Principle** | **Product requirement** |
|----|----|
| Evidence before allegation | The UX SHALL visually distinguish source statements, verified facts, analyst inference, typology indicators, hypotheses, and assessments. |
| Case is context | Case controls scope, permissions, questions, tasks, review, and products; reusable entities/evidence SHALL not be duplicated merely because they appear in multiple cases. |
| Human accountability | Material merges, adverse assessments, dissemination, and publication SHALL require attributable human actions. |
| Uncertainty is data | Confidence, unknowns, dispute, ambiguity, and alternative explanations SHALL be representable as first-class information. |
| Derived is not canonical | Search indexes, graph projections, embeddings, AI summaries, and caches SHALL be rebuildable from canonical records. |
| Security by default | Least privilege, sensitive-source compartmentalisation, auditability, secure export, and retention SHALL be default product behaviours. |
| Build the unique layer | CS-AML SHALL prioritise its unique investigation methodology over reimplementing commodity OCR, graph database, sanctions datasets, or blockchain ingestion. |

# 6. End-to-End Product Workflow

1.  1\. Lead / tip intake

2.  2\. Triage and legitimacy check

3.  3\. Case charter and investigation question

4.  4\. Collection plan

5.  5\. Lawful source collection

6.  6\. Evidence registration and preservation

7.  7\. Document processing / extraction

8.  8\. Entity resolution

9.  9\. Relationship / ownership / asset mapping

10. 10\. Timeline construction

11. 11\. Value-flow reconstruction

12. 12\. Typology and indicator mapping

13. 13\. Hypothesis testing

14. 14\. Assessment and confidence

15. 15\. Peer / legal / security review

16. 16\. Intelligence product

17. 17\. Referral / controlled sharing / publication

18. 18\. Closure / monitoring / retention

# 7. Product Capability Map

This map (CAP-01…CAP-15) is the authoritative **product capability registry**; its IDs are unchanged. The Technology Architecture uses a separate namespace, TA-CAP-01…TA-CAP-16, with a crosswalk to these IDs. Any other document using `CAP-xx` refers to this registry. *[v0.1.1 · A07]*

| **ID** | **Capability** | **Scope** |
|----|----|----|
| CAP-01 | Case & Workflow Management | Case, charter, scope, tasks, lifecycle gates, status, assignment, review |
| CAP-02 | Source & Evidence Management | Source register, evidence store, hashes, extracts, derivatives, provenance |
| CAP-03 | Document Intelligence | Upload, OCR, parsing, metadata, extraction candidates, deduplication |
| CAP-04 | Entity & Identity Management | Registry, aliases, identifiers, candidate matching, merge/split, confidence |
| CAP-05 | Relationship / Ownership / Asset | First-class relationships, beneficial ownership, control, assets, attribution |
| CAP-06 | Timeline & Events | Events, temporal precision, chronology, visual timeline |
| CAP-07 | Value-Flow Analysis | Direct/documented/reconstructed/hypothetical flows, multi-leg flows, flow graph |
| CAP-08 | Typology & Indicator Analysis | Typology catalogue, indicators, counter-indicators, mapping, consistency level |
| CAP-09 | Hypothesis & Assessment | Competing hypotheses, support/contradiction, gaps, confidence, judgement |
| CAP-10 | Search / Graph / Analytics | Full-text, faceted search, graph navigation, paths, clusters, network analytics |
| CAP-11 | Intelligence Products & Review | Reports, peer review, red-team review, approval, correction/versioning |
| CAP-12 | Dissemination & Referral | Export, handling labels, recipient controls, referral packages, sharing log |
| CAP-13 | Administration & Governance | Roles, vocabularies, templates, policies, retention, feature flags |
| CAP-14 | Security / Audit / Operations | IAM, MFA, audit, backup, monitoring, incident response, DR |
| CAP-15 | Integrations & Automation | OpenAleph, OpenSanctions, Flowintel, GraphSense, graph/search, AI assist |

> **Priority model**  
> P0 = MVP mandatory; P1 = Phase 2 / operational depth; P2 = Phase 3 / advanced intelligence. A feature can be technically sophisticated yet remain P2 if the core methodology works without it.

# 8. Functional Feature Catalogue

The following catalogue is the product baseline. IDs are stable across v0.1 and v0.1.1 (existing IDs keep their meaning; new features receive new IDs) and SHOULD be used in issue trackers, architecture decisions, test cases, and release notes.

## CAP-01 — Case & Workflow Management

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-CASE-001 | Case creation and register | P0 | Investigator | Create a case with stable ID, title, owner, purpose, classification and status. | Case | GOV-01,CAS-01 | Case cannot become Active without owner, purpose and investigation question. |
| F-CASE-002 | Investigation Charter | P0 | Case Owner | Define question, scope, exclusions, jurisdictions, period, risks, authorised/prohibited collection and intended outputs. | Case, InvestigationQuestion | CAS-01,PRI-01 | Charter version is preserved; scope changes are recorded and attributable. |
| F-CASE-003 | Lifecycle gates G0-G6 | P0 | Case Owner | Advance a case only when required review gates are satisfied. | Case, Review, AuditEvent | CAS-02,QUA-01 | High-risk gate cannot self-approve where policy requires independent review. |
| F-CASE-004 | Tasks and assignments | P0 | Investigator | Assign collection, verification, analysis and review tasks with due dates and status. | Task, Case | GOV-01 | Task ownership, completion and history are visible. |
| F-CASE-005 | Case activity timeline | P0 | All roles | See significant case actions in chronological order. | AuditEvent, Case | AUD-01 | Material actions appear with actor and timestamp. |
| F-CASE-006 | Case-to-case links | P1 | Analyst | Link related cases without exposing restricted contents automatically. | CaseRelationship | SEC-01 | Cross-case link respects access policy and does not grant implicit access. |
| F-CASE-007 | Monitoring / reopen state | P1 | Case Owner | Close, monitor, or reopen cases with rationale. | Case | CAS-01,AUD-01 | Closure reason and reopen event are immutable history. |

## CAP-02 — Source & Evidence Management

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-EVD-001 | Source register | P0 | Investigator | Register source origin, publisher, URL/location, dates, access method, reliability and legal/access note. | Source | SRC-01,SRC-02 | Material source cannot support assessment without provenance fields. |
| F-EVD-002 | Evidence upload and original preservation | P0 | Evidence Custodian | Store original evidence separately from working copies. | EvidenceItem | EVD-01,SEC-01 | Original is read-only to analysts; replacement creates a new version. |
| F-EVD-003 | Hash and integrity record | P0 | Evidence Custodian | Compute and verify cryptographic hash for critical files. | EvidenceItem | EVD-01 | Stored hash can be recomputed and compared. |
| F-EVD-004 | Evidence extract / citation | P0 | Investigator | Create page/paragraph/region extracts linked to original evidence. | EvidenceExtract | EVD-02 | Each extract links to parent evidence and precise location. |
| F-EVD-005 | Derivative lineage | P0 | Investigator | Track OCR, translation, cropped image, parsed table or transformed dataset as derivative. | EvidenceItem | EVD-02 | Derivative records parent, transformation, creator/tool and time. |
| F-EVD-006 | Source reliability & information credibility | P0 | Analyst | Rate source reliability separately from information credibility. | Source,Claim | SRC-02,ASM-01 | UI prevents one rating from silently standing for both dimensions. |
| F-EVD-007 | Evidence legal hold / retention state | P1 | Evidence Custodian | Apply retention, legal hold and disposition state. | EvidenceItem | PRI-02 | Deletion workflow respects hold and produces audit record. |
| F-EVD-008 | Claim and fact lifecycle | P0 | Analyst / Reviewer | Record source claims without overwriting them with analyst conclusions; record each verification outcome as an append-only verification decision; promote claims/evidence to PROVISIONAL facts; establish, dispute or supersede facts. Added in v0.1.1 as a remediation proposal; requires product-owner approval. | Claim,VerificationDecision,Fact | SRC-01,EVD-02,QUA-01 | A fact cannot be created without claim/evidence refs and a verification decision; ESTABLISHED requires a reviewer other than the proposer; DISPUTED/SUPERSEDED flags dependent assessments/products `review_required` without mutating published products; history is preserved. *[v0.1.1 · A10]* |

## CAP-03 — Document Intelligence

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-DOC-001 | Document ingestion | P0 | Investigator | Upload PDF, DOCX, XLSX, CSV, image and text evidence. | EvidenceItem | EVD-01 | Unsupported/failed ingest does not alter original. |
| F-DOC-002 | OCR / text extraction | P1 | Investigator | Extract searchable text while preserving original and page mapping. | EvidenceItem,DerivedArtifact | EVD-02,TEC-01 | OCR output is marked derived and page-linked. |
| F-DOC-003 | Structured table extraction | P1 | Analyst | Extract tabular data as reviewable derivative records. | DerivedArtifact | EVD-02,TEC-01 | Analyst can compare extracted cells to original. |
| F-DOC-004 | Entity candidate extraction | P1 | Analyst | Generate person/company/address/identifier candidates from documents. | EntityCandidate | TEC-01 | Candidates never become canonical entities without human confirmation or configured rule. |
| F-DOC-005 | Duplicate document detection | P1 | Evidence Custodian | Detect exact/near duplicate files and preserve provenance for each source occurrence. | EvidenceItem | EVD-01 | Deduplication never drops separate provenance. |
| F-DOC-006 | Translation assist | P2 | Analyst | Create linked translations with source text retained. | DerivedArtifact | EVD-02,TEC-01 | Translation is marked derived and reviewable. |

## CAP-04 — Entity & Identity Management

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-ENT-001 | Entity registry | P0 | Analyst | Create canonical person, organisation, account, wallet, address, domain and other entity records. | Entity | ENT-01 | Each entity has type, canonical name and provenance-linked assertions. |
| F-ENT-002 | Aliases and identifiers | P0 | Analyst | Record aliases, registration numbers, IDs, phones, emails and external IDs with source. | Entity,Identifier | ENT-01 | Identifier provenance is visible and conflicting values can coexist. |
| F-ENT-003 | Candidate matching | P0 | Analyst | Compare possible duplicate entities using discriminating features. | EntityMatchCandidate | ENT-01 | System shows both matching and conflicting attributes. |
| F-ENT-004 | Merge / unmerge | P0 | Data Steward | Merge with rationale and later reverse while preserving history. | Entity,MergeDecision | ENT-01,AUD-01 | Unmerge restores prior identities and relationships without history loss. |
| F-ENT-005 | Entity confidence/status | P0 | Analyst | Mark entity resolution as candidate, probable, confirmed, disputed or unresolved. | Entity | ENT-01,ASM-01 | Graph/search visibly carries status. |
| F-ENT-006 | External entity enrichment | P1 | Analyst | Request authorised enrichment from external registries/screening services. | Entity,ExternalReference | SRC-01,PRI-01 | Imported enrichment retains provider/source/time/licence metadata. |

## CAP-05 — Relationship / Ownership / Asset

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-REL-001 | Relationship records | P0 | Analyst | Create first-class typed relationship with evidence, dates, confidence and status. | Relationship | REL-01 | Graph edge can be traced to relationship record and evidence. |
| F-REL-002 | Ownership interest | P0 | Analyst | Record direct/indirect ownership, percentage, dates and evidence. | OwnershipInterest | REL-01,AST-01 | Unknown percentage is permitted; not coerced to zero. |
| F-REL-003 | Control assertion | P0 | Analyst | Represent legal owner, beneficial owner, controller, user and associate separately. | ControlAssertion | AST-01 | UI never collapses ownership/control/use into one field. |
| F-AST-001 | Asset registry | P0 | Analyst | Create property, vehicle, shares, vessel, aircraft, crypto and other asset records. | Asset | AST-01 | Asset attribution type and evidence are required for material claims. |
| F-AST-002 | Valuation records | P1 | Analyst | Record estimated/reported valuations with date, currency and source. | AssetValuation | AST-01 | Valuation method and uncertainty are visible. |
| F-REL-004 | Beneficial ownership chain | P1 | Analyst | Traverse multi-level ownership/control chains and calculate indicative indirect interest when inputs are known. | OwnershipInterest,Relationship | REL-01,TEC-02 | Calculated values display assumptions and source chain. |

## CAP-06 — Timeline & Events

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-TIM-001 | Event records | P0 | Analyst | Record appointments, incorporation, tender awards, purchases, transfers, court events and other time-bounded events. | Event | REL-01 | Event date precision and evidence are explicit. |
| F-TIM-002 | Visual timeline | P0 | Analyst | View case/entity/asset events chronologically with filtering. | Event | AUD-01 | Timeline items link back to canonical event and evidence. |
| F-TIM-003 | Temporal relationship view | P1 | Analyst | Show when ownership/directorship/control existed. | Relationship,Event | REL-01 | Historical and current relationships are distinguishable. |

## CAP-07 — Value-Flow Analysis

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-VAL-001 | ValueFlow record | P0 | Analyst | Record origin, destination, value/range, currency, date, mechanism, evidence and class. | ValueFlow | VAL-01 | flow_class is mandatory: DIRECT, DOCUMENTED, RECONSTRUCTED, or HYPOTHETICAL. |
| F-VAL-002 | Multi-leg value flow | P0 | Analyst | Build chains of contracts, payments, loans, transfers, purchases and conversions. | ValueFlow,ValueFlowLeg | VAL-01 | Each leg retains separate evidence/confidence. |
| F-VAL-003 | Flow visualisation | P0 | Analyst | Visualise value movement without erasing flow class or uncertainty. | ValueFlow | VAL-01 | Line style/label communicates class in UI and export. |
| F-VAL-004 | Unknown / range values | P0 | Analyst | Represent unknown, minimum, maximum and approximate values. | ValueFlow | VAL-01 | System does not invent numeric zero for unknown value. |
| F-VAL-005 | Flow reconciliation | P1 | Analyst | Compare incoming/outgoing known values and identify gaps without implying illegality. | ValueFlow | TEC-02 | Computed gap is labelled analytical calculation with inputs/version. |
| F-VAL-006 | Currency normalisation | P1 | Analyst | View original currency and optionally normalised value using dated FX reference. | ValueFlow | TEC-02 | Original value/currency always preserved. |

## CAP-08 — Typology & Indicator Analysis

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-TYP-001 | Typology catalogue browser | P0 | Analyst | Browse CS-AML typologies, mechanisms, observables, indicators and false positives. | Typology | TYP-01 | Catalogue entry version is visible. |
| F-TYP-002 | Indicator capture | P0 | Analyst | Link observed indicators/counter-indicators to entities, events, flows and evidence. | Indicator | TYP-01 | Indicator cannot exist as unattributed free-floating accusation in final assessment. |
| F-TYP-003 | Typology match worksheet | P0 | Analyst | Compare observed case pattern to typology with consistency level and alternatives. | TypologyMatch | TYP-01,HYP-01 | Single weak indicator cannot auto-produce strong match. |
| F-TYP-004 | Custom/local typologies | P1 | Admin/Analyst | Create versioned local typologies without modifying official catalogue history. | Typology | AUD-01 | Custom typology has owner, version and source lineage. |
| F-TYP-005 | Rule-assisted indicator suggestions | P2 | Analyst | Suggest potential indicators from graph/data while requiring confirmation. | IndicatorCandidate | TEC-01,TEC-02 | Suggestions are labelled machine/rule-generated and cannot auto-escalate case. |

## CAP-09 — Hypothesis & Assessment

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-HYP-001 | Hypothesis workspace | P0 | Analyst | Maintain multiple hypotheses including legitimate explanations. | Hypothesis | HYP-01 | At least one alternative hypothesis is supported for high-impact adverse assessment unless rationale documented. |
| F-HYP-002 | Evidence support / contradiction matrix | P0 | Analyst | Link evidence and indicators as supporting, contradicting, neutral or unknown for each hypothesis. | Hypothesis,EvidenceItem,Indicator | HYP-01,HYP-02 | Matrix records analyst and rationale. |
| F-HYP-003 | Intelligence gaps | P0 | Analyst | Record unknowns that could materially change assessment. | IntelligenceGap | GAP-01 | Final product surfaces material unresolved gaps. |
| F-ASM-001 | Assessment record | P0 | Analyst | Write judgement, confidence, basis, alternatives, assumptions and gaps. | Assessment | ASM-01 | Assessment cannot be final without confidence and evidence-linked basis. |
| F-ASM-002 | Confidence scale | P0 | Analyst | Apply controlled confidence language with rationale: wire values `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS` (Data Model Annex A registry; display labels separate). `INSUFFICIENT_BASIS` is not a level below LOW. | Assessment | ASM-01 | Confidence changes are versioned; rationale is mandatory for every level; `INSUFFICIENT_BASIS` is never converted to LOW, null or zero; a finalized assessment carries a non-null level. *[v0.1.1 · A09]* |
| F-ASM-003 | Disconfirming search record | P0 | Reviewer | Document what was done to search for evidence that weakens adverse findings. | Review,Hypothesis | HYP-02,QUA-01 | High-impact product cannot pass review if no disconfirmation record/rationale. |

## CAP-10 — Search / Graph / Analytics

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-SCH-001 | Full-text search | P0 | Analyst | Search case-authorised documents/evidence and extracted text. | EvidenceItem,DerivedArtifact | SEC-01 | Results enforce object-level permissions. |
| F-SCH-002 | Faceted entity/object search | P0 | Analyst | Filter by entity type, identifier, jurisdiction, case, source, date and status. | Entity,Source,Case | SEC-01 | Search does not reveal restricted object existence where policy forbids it. |
| F-GRF-001 | Graph exploration | P0 | Analyst | Explore entities, relationships, assets, events and flows visually. | Entity,Relationship,Asset,ValueFlow | REL-01,SEC-01 | Every material edge can display provenance/confidence. |
| F-GRF-002 | Path finding | P1 | Analyst | Find paths between two entities under permission and relationship filters. | Relationship | TEC-02 | Path result is labelled analytical output, not proof of association beyond underlying edges. |
| F-GRF-003 | Network metrics | P2 | Analyst | Run centrality, community and cluster analytics as assistive signals. | DerivedAnalytics | TEC-02 | Algorithm/version/input scope are recorded and outputs cannot become facts automatically. |
| F-SCH-003 | Saved searches / watch queries | P1 | Analyst | Save recurring case-scoped queries and notify when new authorised data matches. | SavedQuery | SEC-01 | Watch query scope inherits case permissions and can be disabled. |

## CAP-11 — Intelligence Products & Review

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-PRD-001 | Intelligence product templates | P0 | Analyst | Generate Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package and Case Report. | IntelligenceProduct | ASM-01,DIS-01 | Product embeds version, classification, author/reviewer and evidence index. |
| F-REV-001 | Peer review workflow | P0 | Reviewer | Comment, request change, approve or reject high-impact products. | Review | QUA-01 | Final approval is attributable and separate from author where required. |
| F-REV-002 | Red-team review checklist | P1 | Reviewer | Challenge identity, evidence, alternatives, confidence and potential harm. | Review | QUA-01,HYP-02 | Checklist result is retained with product version. |
| F-PRD-002 | Product versioning / corrections | P0 | Analyst | Issue revised/corrected versions without deleting prior product history. | IntelligenceProduct | AUD-01 | Recipients can distinguish superseded from current versions. |
| F-PRD-003 | Evidence index generation | P0 | Analyst | Generate evidence/source references supporting material findings. | IntelligenceProduct,EvidenceItem | SRC-01,EVD-02 | Every key fact can be traced from product to evidence. |

## CAP-12 — Dissemination & Referral

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-DIS-001 | Dissemination approval | P0 | Case Owner | Approve external sharing with handling classification and intended recipient. | Dissemination | DIS-01 | External export is blocked until required approval is present. |
| F-DIS-002 | Secure export package | P0 | Analyst | Export approved report and evidence index with minimisation/redaction. | Dissemination,IntelligenceProduct | DIS-01,PRI-01 | Export records included objects and excludes unauthorised restricted content. |
| F-DIS-003 | Referral package | P0 | Analyst | Produce structured referral containing subjects, facts, evidence, timeline, flows, indicators, gaps and contact point. | IntelligenceProduct,Dissemination | DIS-01 | Referral distinguishes known facts from analysis and unknowns. |
| F-DIS-004 | Sharing log | P0 | Case Owner | Record who received what version, when, purpose and restrictions. | Dissemination | DIS-01,AUD-01 | Log is immutable to ordinary analysts. |
| F-DIS-005 | Partner workspace / federation | P2 | Partner | Share selected objects/products with controlled partner environment. | SharedObject | SEC-01,DIS-01 | Sharing is explicit object-level allowlist; no implicit case replication. |

## CAP-13 — Administration & Governance

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-ADM-001 | Controlled vocabulary administration | P0 | Admin | Manage relationship types, asset types, statuses and classifications with versioning. | Vocabulary | AUD-01 | Historical records preserve original term/version semantics. |
| F-ADM-002 | Template administration | P1 | Admin | Configure case, review and report templates. | Template | AUD-01 | Template changes are versioned and do not rewrite historical products. |
| F-ADM-003 | Retention policies | P0 | Admin/Privacy | Configure retention/disposition by classification and object type. | RetentionPolicy | PRI-02 | Policy execution can be previewed and audited. |
| F-ADM-004 | Feature flags / environment policy | P1 | Platform Admin | Enable high-risk capabilities (AI, external connectors, federation) per deployment. | SystemPolicy | SEC-01 | Disabled capability cannot be bypassed through API. |

## CAP-14 — Security / Audit / Operations

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-SEC-001 | OIDC authentication + MFA | P0 | All users | Authenticate through organisation identity provider with MFA where required. | User,Session | SEC-01 | Disabled user loses access; session policy enforced. |
| F-SEC-002 | Role and object-level access control | P0 | Security Admin | Restrict access by role, case membership, classification and need-to-know. | AccessPolicy | SEC-01,SEC-02 | API and UI enforce the same authorisation decision. |
| F-SEC-003 | Protected-source compartment | P0 | Source Handler | Store protected source identity separately with restricted access. | ProtectedSource | SEC-02 | Routine analysts can use source-derived evidence without automatically seeing identity. |
| F-AUD-001 | Immutable audit trail | P0 | Auditor | Record material create/update/delete/merge/review/export actions. | AuditEvent | AUD-01 | Ordinary users cannot edit audit events. |
| F-OPS-001 | Backup and restore | P0 | Security Admin | Back up canonical DB, evidence and configuration; test restore. | BackupRecord | SEC-01 | Restore test is documented at defined interval. |
| F-OPS-002 | Operational monitoring | P1 | Platform Admin | Monitor health, errors, jobs, capacity and security events without logging sensitive evidence content. | OperationalEvent | SEC-01 | Observability redacts/avoids case-sensitive payloads. |
| F-OPS-003 | Incident response support | P1 | Security Admin | Record security incidents affecting sources, evidence, accounts or exports. | SecurityIncident | SEC-02 | Incident workflow supports containment, notification and lessons learned. |

## CAP-15 — Integrations & Automation

| **Feature ID** | **Feature** | **Pri** | **Role** | **Requirement / user story** | **Data objects** | **Control refs** | **Acceptance criterion** |
|----|----|----|----|----|----|----|----|
| F-INT-001 | OpenAleph connector | P1 | Analyst | Link/import investigative documents/entities from OpenAleph with provenance. | ExternalReference,Entity,Source | SRC-01 | Imported objects retain remote IDs and source metadata; no silent merge. |
| F-INT-002 | OpenSanctions screening connector | P1 | Analyst | Screen entity against sanctions/PEP/debarment data and review candidate matches. | ScreeningResult | ENT-01,TEC-01 | Screening result is a candidate signal, not canonical identity/fact until reviewed. |
| F-INT-003 | FollowTheMoney mapping | P1 | Data Steward | Map compatible entities/ownership/payment concepts to/from FollowTheMoney. | Entity,Relationship,ValueFlow | AUD-01 | Import/export mapping is versioned and preserves unmapped fields. |
| F-INT-004 | Flowintel interoperability | P2 | Case Owner | Link task/case workflow metadata with Flowintel where used. | ExternalCaseReference | AUD-01 | No implicit transfer of sensitive evidence without explicit configuration. |
| F-INT-005 | GraphSense connector | P2 | Analyst | Enrich public-chain wallet/address analysis using GraphSense. | ExternalReference,ValueFlow | TEC-01 | Blockchain analytics output remains attributed to provider and timestamp. |
| F-INT-006 | Graph projection connector | P1 | Platform Admin | Project canonical relationship/value-flow data to Neo4j/Memgraph or equivalent. | DerivedProjection | REL-01 | Projection is rebuildable and cannot become sole canonical source. |
| F-AI-001 | AI summarisation / extraction assist | P1 | Analyst | Use AI to summarise or propose entities/relationships from authorised content. | DerivedArtifact,Candidate | TEC-01 | AI output is labelled generated, attributable to model/version, and review-required. |
| F-AI-002 | AI analytical assistant | P2 | Analyst | Ask questions across authorised case data with citations to canonical objects. | DerivedAnalysis | TEC-01,TEC-02 | Assistant cannot create final adverse assessment or dissemination approval autonomously. |

# 9. MVP Definition (Release 0.1)

The MVP SHALL demonstrate the complete analytical chain on a real or synthetic civil-society investigation without depending on advanced automation. Every P0 feature is in scope unless explicitly waived in a release decision.

| **Module** | **Minimum outcome** |
|----|----|
| MVP-1 Case Workspace | Case register, charter, lifecycle, tasks, ownership, status, audit |
| MVP-2 Source & Evidence | Source register, preserved evidence, hashes, extracts, derivatives, reliability, claim and fact lifecycle *[v0.1.1 · A10]* |
| MVP-3 Entity & Relationship | Canonical entities, aliases/identifiers, candidate match, merge/unmerge, first-class relationships |
| MVP-4 Assets / Events / Timeline | Asset attribution, event records, visual timeline |
| MVP-5 Follow-the-Value | ValueFlow builder with mandatory DIRECT/DOCUMENTED/RECONSTRUCTED/HYPOTHETICAL classification |
| MVP-6 Typology & Hypothesis | Catalogue browser, indicators, typology worksheet, competing hypotheses, gaps |
| MVP-7 Assessment & Review | Assessment, confidence, disconfirmation, peer review |
| MVP-8 Intelligence Product | Six report templates (Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report) *[v0.1.1 · A06]*, evidence index, versioning, secure export/referral |
| MVP-9 Search & Graph | Full-text/faceted search and provenance-aware graph view |
| MVP-10 Security & Audit | OIDC/MFA, object-level RBAC, protected-source compartment, audit, backup/restore |

> **MVP completion test**  
> A two-analyst team SHALL be able to open a case, ingest evidence, resolve entities, build an ownership/asset/value-flow model, test at least two hypotheses, map relevant typologies, produce a confidence-rated assessment, complete independent review, and export an approved intelligence product while preserving provenance and audit history.

# 10. Release Roadmap

| **Release** | **Scope** | **Exit objective** |
|----|----|----|
| 0.1 — Foundation MVP | P0 features | Complete end-to-end investigation and review workflow with strong provenance and security. |
| 0.2 — Operational Intelligence | P1 features | OCR/extraction, enrichment connectors, advanced ownership, saved queries, red-team review, observability. |
| 0.3 — Network Intelligence | Selected P2 | Cross-case discovery, network metrics, GraphSense, federation/partner workspace, rule-assisted indicators. |
| 0.4 — Controlled AI | Selected P1/P2 AI | Citation-grounded AI assistance, controlled entity suggestions, model governance, validation metrics. |
| 1.0 — Assured Platform | All required controls + independent QA | Production-ready product with conformance evidence, security assurance, documented operations and upgrade path. |

# 11. Build vs Integrate Strategy

| **Disposition** | **Capabilities** | **Rationale** |
|----|----|----|
| Build as CS-AML core | Case charter/gates; Evidence→Fact chain; hypothesis matrix; confidence; intelligence gaps; value-flow classification; typology assessment; review/dissemination; provenance-preserving UX | These functions embody the unique methodology and control model. |
| Integrate / reuse | OCR/document intelligence; sanctions/PEP data; generic graph DB; blockchain analytics; identity provider; search engine; object storage; observability | Mature components already exist; wrapping them preserves focus and reduces maintenance risk. |
| Adapt / map | FollowTheMoney ontology; OpenAleph investigative datasets; Flowintel workflow concepts | Useful models/workflows can be mapped without making them normative dependencies. |

| **Tool / ecosystem** | **Reference value** | **Recommended role** | **Phase** |
|----|----|----|----|
| OpenAleph | Investigative document/data platform; reference for collections, search, OCR/entity extraction, investigation workspaces. | Connector or adjacent investigative data platform | P1 |
| FollowTheMoney | Investigative entity/relationship ontology used in anti-corruption and investigative journalism ecosystems. | Interoperability / ontology mapping | P1 |
| OpenSanctions / yente | Sanctions, PEP and related entity matching/screening. | External screening service | P1 |
| Flowintel | Open-source case/task workflow platform. | Workflow interoperability / UX reference | P2 |
| GraphSense | Open-source cryptoasset analytics. | Crypto analytics connector | P2 |
| Neo4j / Memgraph | Graph database / analytics. | Derived graph projection | P1/P2 |
| OpenSearch / PostgreSQL FTS | Search engine. | Derived search index | P0/P1 |
| Keycloak or equivalent | OIDC IAM, MFA, RBAC support. | Identity provider | P0 |
| S3-compatible object store | Evidence object storage. | Evidence storage infrastructure | P0 |
| OpenTelemetry + Prometheus/Grafana | Telemetry and operational monitoring. | Observability | P1 |

# 12. Non-Functional Requirements

| **ID** | **Domain** | **Requirement** |
|----|----|----|
| NFR-SEC-01 | Security | Least privilege, MFA, compartmentalisation, encryption in transit, secure secrets, patching, backup, audit. |
| NFR-PRI-01 | Privacy | Data minimisation, purpose limitation, retention, deletion/disposition, access justification, export minimisation. |
| NFR-AUD-01 | Auditability | Material analytical and dissemination changes are attributable, timestamped and reviewable. |
| NFR-INT-01 | Integrity | Canonical objects and original evidence cannot be silently overwritten; critical evidence supports hash verification. |
| NFR-EXP-01 | Explainability | Automated score/match/path/suggestion used materially exposes basis, input scope and model/rule version. |
| NFR-PER-01 | Performance | Common case, entity, search and graph views SHOULD return interactively for expected deployment scale; long analytics MAY use async jobs. |
| NFR-AVL-01 | Availability | System SHOULD tolerate component restart and provide tested backup/restore; deployment defines RPO/RTO. |
| NFR-INTOP-01 | Interoperability | Stable IDs, versioned APIs, import/export metadata and mapping records SHALL support external integration. |
| NFR-UX-01 | Usability | UX SHALL make fact/inference/confidence/provenance visible without requiring analyst to inspect raw DB fields. |
| NFR-ACC-01 | Accessibility | Core workflows SHOULD meet recognised web accessibility good practice and support keyboard/screen-reader use. |
| NFR-MNT-01 | Maintainability | Schema, APIs, typologies, vocabularies and templates are versioned; migrations are testable and reversible where feasible. |
| NFR-OBS-01 | Observability | Operational telemetry SHALL avoid leaking protected evidence or source content into logs. |

# 13. Permission and Information-Handling Model

At minimum, authorisation SHALL consider role, case membership, object classification, need-to-know, protected-source compartment, and dissemination restriction. Case membership alone SHALL NOT automatically reveal protected-source identity.

| **Classification** | **Handling expectation** |
|----|----|
| Public (`PUBLIC`) | Suitable for public release after normal review; still subject to case purpose and privacy rules. |
| Internal (`INTERNAL`) | Routine internal operational information limited to authorised organisation users. |
| Sensitive (`SENSITIVE`) | Could create privacy, reputational, safety, or investigative harm if disclosed. |
| Restricted (`RESTRICTED`) | High-risk information requiring named-role or case-specific authorization. |
| Source-protected (`SOURCE_PROTECTED`) | Information whose disclosure could identify or endanger a confidential source; separate compartment and minimal access. |
| Access labels (not levels) | Legal privilege, safety, embargo, purpose, jurisdiction, compartment and other need-to-know conditions are additive access labels; the most restrictive applicable level plus all labels apply. *[v0.1.1 · A08]* |

The five levels above (ordered least → most restrictive) are the authoritative classification model defined in Data Model Specification v0.1.1 §16. Derived objects and exports inherit the highest classification of their inputs unless a recorded reviewer downgrade decision exists. Unknown or missing classification fails closed. The Framework v0.1 label "Highly Restricted" is never auto-mapped: it becomes `SOURCE_PROTECTED` only when the reason is source-identifying information, otherwise `RESTRICTED` plus the relevant access label. *[v0.1.1 · A08]*

# 14. Product Data and API Requirements

| **Requirement** | **Rule** |
|----|----|
| Stable object IDs | All canonical objects SHALL expose stable identifiers suitable for references, audit and integration. |
| Version metadata | Material objects SHALL expose current version and modification metadata; previous versions remain reconstructable where required. |
| Provenance links | APIs SHALL allow traversal from assessment to hypothesis/indicator/fact/evidence/source. |
| Permission enforcement | API SHALL enforce the same authorisation rules as UI; UI hiding is not a security control. |
| Derived output labelling | Search hits, graph paths, AI suggestions and computed metrics SHALL expose derived status and source inputs. |
| Export manifests | Exports SHOULD contain object/version manifest and handling metadata. |
| Connector lineage | Imported records SHALL retain provider, external ID, retrieval time, connector version and mapping status. |

# 15. Required User Experience Surfaces

| **Surface** | **Minimum UX purpose** |
|----|----|
| Dashboard | Assigned cases, pending reviews, high-priority tasks, recent activity, connector/processing warnings. |
| Case Workspace | Charter, scope, tasks, linked entities/evidence, timeline, hypotheses, assessments, reviews, products. |
| Evidence Viewer | Original/derivative distinction, page/text view, extract creation, hash/provenance, linked claims/facts. |
| Entity Profile | Aliases, identifiers, source assertions, related cases, relationships, assets, events, screening/enrichment. |
| Entity Resolution Workbench | Side-by-side candidate comparison, matching/conflicting attributes, evidence, merge/unmerge decision. |
| Graph Explorer | Provenance-aware nodes/edges, filters, saved views, path query, evidence drill-down. |
| Timeline | Events, relationship validity, asset changes, flow dates and evidence. |
| Value Flow Builder | Leg creation, class distinction, amount/range/currency, evidence, flow visualisation. |
| Typology Worksheet | Catalogue guidance, indicators, counter-indicators, consistency assessment and references. |
| Hypothesis Matrix | Competing hypotheses, supporting/contradicting evidence, gaps, discriminating questions. |
| Assessment Editor | Judgement, confidence, basis, alternatives, assumptions, gaps, reviewer status. |
| Product / Review Workspace | Template, evidence index, comments, red-team checklist, approval, versioning. |
| Admin / Assurance | Users/roles, vocabularies, connectors, policy, retention, audit, control evidence and system health. |

# 16. Suggested Engineering Epics

| **Epic** | **Name** | **Scope** |
|----|----|----|
| EPIC-01 | Foundation platform | Project skeleton, auth, tenancy/deployment policy, canonical IDs, audit framework. |
| EPIC-02 | Case & workflow | Case charter, tasks, gates, ownership, lifecycle. |
| EPIC-03 | Evidence & provenance | Source/evidence registry, file store, hash, extracts, derivatives, claim and fact lifecycle. *[v0.1.1 · A10]* |
| EPIC-04 | Entity model & resolution | Entity registry, identifiers, match candidates, merge/unmerge. |
| EPIC-05 | Relationships/assets/events | First-class graph objects, ownership/control, assets, event/timeline. |
| EPIC-06 | Value-flow | Flow/legs, visual builder, classifications, calculations. |
| EPIC-07 | Typology & hypothesis | Catalogue, indicators, hypothesis matrix, gaps. |
| EPIC-08 | Assessment & products | Confidence, intelligence product, evidence index, versioning. |
| EPIC-09 | Review & dissemination | Peer review, red-team, approval, secure export, referral, sharing log. |
| EPIC-10 | Search & graph | FTS, faceted search, graph projection/explorer, saved views. |
| EPIC-11 | Security & operations | RBAC, protected source, backup/restore, monitoring, incident support. |
| EPIC-12 | Integrations | OpenAleph, OpenSanctions, FTM, GraphSense, external graph/search. |
| EPIC-13 | AI assist | Controlled extraction, summarisation, grounded assistant, model audit. |

# 17. Acceptance and Test Strategy

| **Test domain** | **Minimum acceptance approach** |
|----|----|
| Functional acceptance | Feature-specific acceptance criteria in Section 8 SHALL be converted to executable/manual test cases. |
| Methodology conformance | Test that users cannot silently skip mandatory separation between evidence, fact, hypothesis and assessment. |
| Permission testing | Include positive and negative tests for case/object/source compartment access. |
| Provenance testing | Randomly sample material findings and trace backward to evidence/source. |
| Entity-resolution testing | Test false-positive merges, conflicting identifiers, reversal, and historical integrity. |
| Value-flow testing | Verify all four flow classes remain distinct in DB/API/UI/export. |
| Review testing | High-impact product cannot be finalised without required independent review. |
| Audit testing | Critical action creates audit event and ordinary users cannot edit/delete it. |
| Connector testing | External enrichment failure or stale data cannot corrupt canonical objects. |
| AI testing | AI output is visibly derived, grounded where applicable, and blocked from autonomous adverse decision or dissemination. |
| Backup/restore testing | Restore canonical DB and evidence into isolated environment and verify object/evidence integrity. |

# 18. Product Metrics

| **Metric** | **Interpretation** |
|----|----|
| Provenance coverage | % material facts/relationships/value flows with direct evidence/source links. |
| Entity correction rate | Merge/unmerge correction rate and false-match review outcome. |
| Review coverage | % high-impact products independently reviewed before dissemination. |
| Gap visibility | % material assessments with explicit intelligence gaps. |
| Alternative-hypothesis coverage | % high-impact adverse assessments with documented alternatives/disconfirmation. |
| Time-to-triage | Median lead intake to open/reject/monitor decision. |
| Time-to-review | Median draft product to completed peer review. |
| Referral usefulness | Recipient feedback or follow-up rate where legitimately measurable. |
| Security/privacy incidents | Source exposure, unauthorised access, accidental export or retention exceptions. |
| Analyst rework | Corrections caused by missing provenance, identity error, unsupported relationship or ambiguous flow classification. |

> **Metric warning**  
> Node count, scraped-record count, number of alerts, AI-generated suggestions, or number of cases are not sufficient measures of effectiveness.

# 19. Framework-to-Product Traceability

| **Framework requirement** | **Feature implementation** | **Data objects** | **Controls** |
|----|----|----|----|
| Evidence before allegation | F-EVD-\*; F-HYP-\*; F-ASM-\* | Source/Evidence/Fact/Hypothesis/Assessment | SRC/EVD/HYP/ASM |
| Case is context; reusable truth objects | F-CASE-\*; F-ENT-\*; F-EVD-\* | Case/Entity/Evidence | CAS/ENT/EVD |
| Follow the value | F-VAL-\* | ValueFlow/ValueFlowLeg | VAL-01 |
| Typology caution | F-TYP-\* | Typology/Indicator/TypologyMatch | TYP-01 |
| Entity resolution reversibility | F-ENT-003/004/005 | EntityMatchCandidate/MergeDecision | ENT-01 |
| Alternative explanations | F-HYP-001/002/003 | Hypothesis/IntelligenceGap | HYP-01/HYP-02/GAP-01 |
| Confidence and assessment | F-ASM-001/002 | Assessment | ASM-01 |
| Peer review | F-REV-\* | Review | QUA-01 |
| Controlled dissemination | F-DIS-\* | Dissemination/IntelligenceProduct | DIS-01 |
| Protected sources | F-SEC-003 | ProtectedSource | SEC-02 |
| AI is assistive | F-AI-\*; F-DOC-004/006 | DerivedArtifact/Candidate | TEC-01/TEC-02 |

# 20. Open Product Decisions for v0.1

| **ID** | **Decision** | **Recommended v0.1 stance** |
|----|----|----|
| PD-01 | Single-organisation first vs multi-tenant from day one | Recommendation: single-organisation / strong case compartment first; design schema for later multi-tenancy. |
| PD-02 | OpenAleph as dependency vs connector | Recommendation: connector/adjacent service, not hard dependency, until workflow is validated. |
| PD-03 | FollowTheMoney adoption depth | Recommendation: interoperability mapping and selective reuse; retain CS-AML-specific Evidence/Hypothesis/Assessment model. |
| PD-04 | Graph database in MVP | Recommendation: optional projection. MVP can use relational canonical model plus graph view; introduce dedicated graph DB when scale/queries justify it. |
| PD-05 | AI in MVP | Recommendation: not required for MVP completion. Introduce after evidence/provenance and review workflow are stable. |
| PD-06 | Public-source connectors | Recommendation: begin with manual import + a small number of legally reviewed connectors; avoid uncontrolled scraping framework in v0.1. |
| PD-07 | Mobile support | Recommendation: responsive read/review/task capability first; sensitive collection and evidence handling optimised for desktop. |
| PD-08 | Federation | Recommendation: defer to Phase 3; first establish object-level sharing and export manifests. |

# Annex A — Canonical User Story Format

Each backlog item SHOULD use the following fields:

- Feature ID / Epic ID

- As a \<role\>

- I want \<capability\>

- So that \<investigative/control outcome\>

- Preconditions

- Primary flow

- Alternative/error flows

- Data objects touched

- Control references

- Security/privacy considerations

- Acceptance criteria

- Audit events

- Telemetry (non-sensitive)

- Priority / release

- Dependencies

# Annex B — Definition of Done for P0 Features

- Functional acceptance criteria passed.

- Authorisation tested for permitted and denied users.

- Audit events verified for material actions.

- Provenance / object references preserved.

- No silent conversion of derived or inferred data into canonical fact.

- Error states fail safely and do not corrupt originals/canonical objects.

- API and UI behaviour are consistent.

- Retention/classification behaviour tested where applicable.

- Backup/migration impact documented for schema changes.

- User-facing wording distinguishes fact, inference, confidence and uncertainty.

- Operational documentation and release notes updated.

# Annex C — Reference Product Architecture (Non-Normative)

A pragmatic first implementation MAY use the following profile:

| **Layer** | **Reference option** |
|----|----|
| Web application / API | Django + REST/GraphQL equivalent |
| Canonical relational store | PostgreSQL + PostGIS where geographic data is needed |
| Evidence object store | S3-compatible storage or encrypted filesystem |
| Async jobs | Celery/RQ equivalent + Valkey 8.x broker (Redis-protocol compatible; release pinned per ADR-0006) *[v0.1.1 · A03]* |
| IAM | Keycloak or other OIDC provider |
| Search | PostgreSQL FTS initially; OpenSearch when scale/features justify it |
| Graph | Relational projection initially; Neo4j/Memgraph optional derived projection |
| OCR/document processing | OpenAleph or dedicated processing service |
| Sanctions/PEP screening | OpenSanctions/yente connector |
| Crypto analytics | GraphSense connector |
| Observability | OpenTelemetry + Prometheus/Grafana equivalent |
| Reverse proxy | Nginx/Caddy equivalent |

# Annex D — Release Planning Summary

| **Priority** | **Feature count** | **Planning meaning** |
|----|----|----|
| P0 / MVP | 55 | Required to prove end-to-end methodology and controls *[v0.1.1 · A10]* |
| P1 / Phase 2 | 26 | Operational depth, enrichment, advanced review and analytics |
| P2 / Phase 3 | 7 | Network intelligence, federation, advanced AI/analytics |
| Total | 88 | 55 P0 + 26 P1 + 7 P2 (v0.1 baseline: 87 = 54 + 26 + 7; F-EVD-008 added in v0.1.1) *[v0.1.1 · A10]* |

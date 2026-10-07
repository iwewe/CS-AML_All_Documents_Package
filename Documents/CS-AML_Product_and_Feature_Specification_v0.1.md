# CS-AML Product & Feature Specification v0.1

**Status:** Normative product baseline / implementation specification

## Product axiom
The platform SHALL help analysts discover, structure, test, explain, review, and disseminate financial intelligence without converting uncertainty into fact or replacing accountable human judgement.

## Core analytical chain
`SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT`

## Priority model
- P0: MVP mandatory
- P1: Phase 2 operational depth
- P2: Phase 3 advanced intelligence

## Capability map

- **CAP-01 — Case & Workflow Management:** Case, charter, scope, tasks, lifecycle gates, status, assignment, review

- **CAP-02 — Source & Evidence Management:** Source register, evidence store, hashes, extracts, derivatives, provenance

- **CAP-03 — Document Intelligence:** Upload, OCR, parsing, metadata, extraction candidates, deduplication

- **CAP-04 — Entity & Identity Management:** Registry, aliases, identifiers, candidate matching, merge/split, confidence

- **CAP-05 — Relationship / Ownership / Asset:** First-class relationships, beneficial ownership, control, assets, attribution

- **CAP-06 — Timeline & Events:** Events, temporal precision, chronology, visual timeline

- **CAP-07 — Value-Flow Analysis:** Direct/documented/reconstructed/hypothetical flows, multi-leg flows, flow graph

- **CAP-08 — Typology & Indicator Analysis:** Typology catalogue, indicators, counter-indicators, mapping, consistency level

- **CAP-09 — Hypothesis & Assessment:** Competing hypotheses, support/contradiction, gaps, confidence, judgement

- **CAP-10 — Search / Graph / Analytics:** Full-text, faceted search, graph navigation, paths, clusters, network analytics

- **CAP-11 — Intelligence Products & Review:** Reports, peer review, red-team review, approval, correction/versioning

- **CAP-12 — Dissemination & Referral:** Export, handling labels, recipient controls, referral packages, sharing log

- **CAP-13 — Administration & Governance:** Roles, vocabularies, templates, policies, retention, feature flags

- **CAP-14 — Security / Audit / Operations:** IAM, MFA, audit, backup, monitoring, incident response, DR

- **CAP-15 — Integrations & Automation:** OpenAleph, OpenSanctions, Flowintel, GraphSense, graph/search, AI assist


## Feature catalogue

### F-CASE-001 — Case creation and register (P0)
- Capability: CAP-01
- Primary role: Investigator
- Requirement: Create a case with stable ID, title, owner, purpose, classification and status.
- Data objects: Case
- Controls: GOV-01,CAS-01
- Acceptance: Case cannot become Active without owner, purpose and investigation question.

### F-CASE-002 — Investigation Charter (P0)
- Capability: CAP-01
- Primary role: Case Owner
- Requirement: Define question, scope, exclusions, jurisdictions, period, risks, authorised/prohibited collection and intended outputs.
- Data objects: Case, InvestigationQuestion
- Controls: CAS-01,PRI-01
- Acceptance: Charter version is preserved; scope changes are recorded and attributable.

### F-CASE-003 — Lifecycle gates G0-G6 (P0)
- Capability: CAP-01
- Primary role: Case Owner
- Requirement: Advance a case only when required review gates are satisfied.
- Data objects: Case, Review, AuditEvent
- Controls: CAS-02,QUA-01
- Acceptance: High-risk gate cannot self-approve where policy requires independent review.

### F-CASE-004 — Tasks and assignments (P0)
- Capability: CAP-01
- Primary role: Investigator
- Requirement: Assign collection, verification, analysis and review tasks with due dates and status.
- Data objects: Task, Case
- Controls: GOV-01
- Acceptance: Task ownership, completion and history are visible.

### F-CASE-005 — Case activity timeline (P0)
- Capability: CAP-01
- Primary role: All roles
- Requirement: See significant case actions in chronological order.
- Data objects: AuditEvent, Case
- Controls: AUD-01
- Acceptance: Material actions appear with actor and timestamp.

### F-CASE-006 — Case-to-case links (P1)
- Capability: CAP-01
- Primary role: Analyst
- Requirement: Link related cases without exposing restricted contents automatically.
- Data objects: CaseRelationship
- Controls: SEC-01
- Acceptance: Cross-case link respects access policy and does not grant implicit access.

### F-CASE-007 — Monitoring / reopen state (P1)
- Capability: CAP-01
- Primary role: Case Owner
- Requirement: Close, monitor, or reopen cases with rationale.
- Data objects: Case
- Controls: CAS-01,AUD-01
- Acceptance: Closure reason and reopen event are immutable history.

### F-EVD-001 — Source register (P0)
- Capability: CAP-02
- Primary role: Investigator
- Requirement: Register source origin, publisher, URL/location, dates, access method, reliability and legal/access note.
- Data objects: Source
- Controls: SRC-01,SRC-02
- Acceptance: Material source cannot support assessment without provenance fields.

### F-EVD-002 — Evidence upload and original preservation (P0)
- Capability: CAP-02
- Primary role: Evidence Custodian
- Requirement: Store original evidence separately from working copies.
- Data objects: EvidenceItem
- Controls: EVD-01,SEC-01
- Acceptance: Original is read-only to analysts; replacement creates a new version.

### F-EVD-003 — Hash and integrity record (P0)
- Capability: CAP-02
- Primary role: Evidence Custodian
- Requirement: Compute and verify cryptographic hash for critical files.
- Data objects: EvidenceItem
- Controls: EVD-01
- Acceptance: Stored hash can be recomputed and compared.

### F-EVD-004 — Evidence extract / citation (P0)
- Capability: CAP-02
- Primary role: Investigator
- Requirement: Create page/paragraph/region extracts linked to original evidence.
- Data objects: EvidenceExtract
- Controls: EVD-02
- Acceptance: Each extract links to parent evidence and precise location.

### F-EVD-005 — Derivative lineage (P0)
- Capability: CAP-02
- Primary role: Investigator
- Requirement: Track OCR, translation, cropped image, parsed table or transformed dataset as derivative.
- Data objects: EvidenceItem
- Controls: EVD-02
- Acceptance: Derivative records parent, transformation, creator/tool and time.

### F-EVD-006 — Source reliability & information credibility (P0)
- Capability: CAP-02
- Primary role: Analyst
- Requirement: Rate source reliability separately from information credibility.
- Data objects: Source,Claim
- Controls: SRC-02,ASM-01
- Acceptance: UI prevents one rating from silently standing for both dimensions.

### F-EVD-007 — Evidence legal hold / retention state (P1)
- Capability: CAP-02
- Primary role: Evidence Custodian
- Requirement: Apply retention, legal hold and disposition state.
- Data objects: EvidenceItem
- Controls: PRI-02
- Acceptance: Deletion workflow respects hold and produces audit record.

### F-DOC-001 — Document ingestion (P0)
- Capability: CAP-03
- Primary role: Investigator
- Requirement: Upload PDF, DOCX, XLSX, CSV, image and text evidence.
- Data objects: EvidenceItem
- Controls: EVD-01
- Acceptance: Unsupported/failed ingest does not alter original.

### F-DOC-002 — OCR / text extraction (P1)
- Capability: CAP-03
- Primary role: Investigator
- Requirement: Extract searchable text while preserving original and page mapping.
- Data objects: EvidenceItem,DerivedArtifact
- Controls: EVD-02,TEC-01
- Acceptance: OCR output is marked derived and page-linked.

### F-DOC-003 — Structured table extraction (P1)
- Capability: CAP-03
- Primary role: Analyst
- Requirement: Extract tabular data as reviewable derivative records.
- Data objects: DerivedArtifact
- Controls: EVD-02,TEC-01
- Acceptance: Analyst can compare extracted cells to original.

### F-DOC-004 — Entity candidate extraction (P1)
- Capability: CAP-03
- Primary role: Analyst
- Requirement: Generate person/company/address/identifier candidates from documents.
- Data objects: EntityCandidate
- Controls: TEC-01
- Acceptance: Candidates never become canonical entities without human confirmation or configured rule.

### F-DOC-005 — Duplicate document detection (P1)
- Capability: CAP-03
- Primary role: Evidence Custodian
- Requirement: Detect exact/near duplicate files and preserve provenance for each source occurrence.
- Data objects: EvidenceItem
- Controls: EVD-01
- Acceptance: Deduplication never drops separate provenance.

### F-DOC-006 — Translation assist (P2)
- Capability: CAP-03
- Primary role: Analyst
- Requirement: Create linked translations with source text retained.
- Data objects: DerivedArtifact
- Controls: EVD-02,TEC-01
- Acceptance: Translation is marked derived and reviewable.

### F-ENT-001 — Entity registry (P0)
- Capability: CAP-04
- Primary role: Analyst
- Requirement: Create canonical person, organisation, account, wallet, address, domain and other entity records.
- Data objects: Entity
- Controls: ENT-01
- Acceptance: Each entity has type, canonical name and provenance-linked assertions.

### F-ENT-002 — Aliases and identifiers (P0)
- Capability: CAP-04
- Primary role: Analyst
- Requirement: Record aliases, registration numbers, IDs, phones, emails and external IDs with source.
- Data objects: Entity,Identifier
- Controls: ENT-01
- Acceptance: Identifier provenance is visible and conflicting values can coexist.

### F-ENT-003 — Candidate matching (P0)
- Capability: CAP-04
- Primary role: Analyst
- Requirement: Compare possible duplicate entities using discriminating features.
- Data objects: EntityMatchCandidate
- Controls: ENT-01
- Acceptance: System shows both matching and conflicting attributes.

### F-ENT-004 — Merge / unmerge (P0)
- Capability: CAP-04
- Primary role: Data Steward
- Requirement: Merge with rationale and later reverse while preserving history.
- Data objects: Entity,MergeDecision
- Controls: ENT-01,AUD-01
- Acceptance: Unmerge restores prior identities and relationships without history loss.

### F-ENT-005 — Entity confidence/status (P0)
- Capability: CAP-04
- Primary role: Analyst
- Requirement: Mark entity resolution as candidate, probable, confirmed, disputed or unresolved.
- Data objects: Entity
- Controls: ENT-01,ASM-01
- Acceptance: Graph/search visibly carries status.

### F-ENT-006 — External entity enrichment (P1)
- Capability: CAP-04
- Primary role: Analyst
- Requirement: Request authorised enrichment from external registries/screening services.
- Data objects: Entity,ExternalReference
- Controls: SRC-01,PRI-01
- Acceptance: Imported enrichment retains provider/source/time/licence metadata.

### F-REL-001 — Relationship records (P0)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Create first-class typed relationship with evidence, dates, confidence and status.
- Data objects: Relationship
- Controls: REL-01
- Acceptance: Graph edge can be traced to relationship record and evidence.

### F-REL-002 — Ownership interest (P0)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Record direct/indirect ownership, percentage, dates and evidence.
- Data objects: OwnershipInterest
- Controls: REL-01,AST-01
- Acceptance: Unknown percentage is permitted; not coerced to zero.

### F-REL-003 — Control assertion (P0)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Represent legal owner, beneficial owner, controller, user and associate separately.
- Data objects: ControlAssertion
- Controls: AST-01
- Acceptance: UI never collapses ownership/control/use into one field.

### F-AST-001 — Asset registry (P0)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Create property, vehicle, shares, vessel, aircraft, crypto and other asset records.
- Data objects: Asset
- Controls: AST-01
- Acceptance: Asset attribution type and evidence are required for material claims.

### F-AST-002 — Valuation records (P1)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Record estimated/reported valuations with date, currency and source.
- Data objects: AssetValuation
- Controls: AST-01
- Acceptance: Valuation method and uncertainty are visible.

### F-REL-004 — Beneficial ownership chain (P1)
- Capability: CAP-05
- Primary role: Analyst
- Requirement: Traverse multi-level ownership/control chains and calculate indicative indirect interest when inputs are known.
- Data objects: OwnershipInterest,Relationship
- Controls: REL-01,TEC-02
- Acceptance: Calculated values display assumptions and source chain.

### F-TIM-001 — Event records (P0)
- Capability: CAP-06
- Primary role: Analyst
- Requirement: Record appointments, incorporation, tender awards, purchases, transfers, court events and other time-bounded events.
- Data objects: Event
- Controls: REL-01
- Acceptance: Event date precision and evidence are explicit.

### F-TIM-002 — Visual timeline (P0)
- Capability: CAP-06
- Primary role: Analyst
- Requirement: View case/entity/asset events chronologically with filtering.
- Data objects: Event
- Controls: AUD-01
- Acceptance: Timeline items link back to canonical event and evidence.

### F-TIM-003 — Temporal relationship view (P1)
- Capability: CAP-06
- Primary role: Analyst
- Requirement: Show when ownership/directorship/control existed.
- Data objects: Relationship,Event
- Controls: REL-01
- Acceptance: Historical and current relationships are distinguishable.

### F-VAL-001 — ValueFlow record (P0)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: Record origin, destination, value/range, currency, date, mechanism, evidence and class.
- Data objects: ValueFlow
- Controls: VAL-01
- Acceptance: flow_class is mandatory: DIRECT, DOCUMENTED, RECONSTRUCTED, or HYPOTHETICAL.

### F-VAL-002 — Multi-leg value flow (P0)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: Build chains of contracts, payments, loans, transfers, purchases and conversions.
- Data objects: ValueFlow,ValueFlowLeg
- Controls: VAL-01
- Acceptance: Each leg retains separate evidence/confidence.

### F-VAL-003 — Flow visualisation (P0)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: Visualise value movement without erasing flow class or uncertainty.
- Data objects: ValueFlow
- Controls: VAL-01
- Acceptance: Line style/label communicates class in UI and export.

### F-VAL-004 — Unknown / range values (P0)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: Represent unknown, minimum, maximum and approximate values.
- Data objects: ValueFlow
- Controls: VAL-01
- Acceptance: System does not invent numeric zero for unknown value.

### F-VAL-005 — Flow reconciliation (P1)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: Compare incoming/outgoing known values and identify gaps without implying illegality.
- Data objects: ValueFlow
- Controls: TEC-02
- Acceptance: Computed gap is labelled analytical calculation with inputs/version.

### F-VAL-006 — Currency normalisation (P1)
- Capability: CAP-07
- Primary role: Analyst
- Requirement: View original currency and optionally normalised value using dated FX reference.
- Data objects: ValueFlow
- Controls: TEC-02
- Acceptance: Original value/currency always preserved.

### F-TYP-001 — Typology catalogue browser (P0)
- Capability: CAP-08
- Primary role: Analyst
- Requirement: Browse CS-AML typologies, mechanisms, observables, indicators and false positives.
- Data objects: Typology
- Controls: TYP-01
- Acceptance: Catalogue entry version is visible.

### F-TYP-002 — Indicator capture (P0)
- Capability: CAP-08
- Primary role: Analyst
- Requirement: Link observed indicators/counter-indicators to entities, events, flows and evidence.
- Data objects: Indicator
- Controls: TYP-01
- Acceptance: Indicator cannot exist as unattributed free-floating accusation in final assessment.

### F-TYP-003 — Typology match worksheet (P0)
- Capability: CAP-08
- Primary role: Analyst
- Requirement: Compare observed case pattern to typology with consistency level and alternatives.
- Data objects: TypologyMatch
- Controls: TYP-01,HYP-01
- Acceptance: Single weak indicator cannot auto-produce strong match.

### F-TYP-004 — Custom/local typologies (P1)
- Capability: CAP-08
- Primary role: Admin/Analyst
- Requirement: Create versioned local typologies without modifying official catalogue history.
- Data objects: Typology
- Controls: AUD-01
- Acceptance: Custom typology has owner, version and source lineage.

### F-TYP-005 — Rule-assisted indicator suggestions (P2)
- Capability: CAP-08
- Primary role: Analyst
- Requirement: Suggest potential indicators from graph/data while requiring confirmation.
- Data objects: IndicatorCandidate
- Controls: TEC-01,TEC-02
- Acceptance: Suggestions are labelled machine/rule-generated and cannot auto-escalate case.

### F-HYP-001 — Hypothesis workspace (P0)
- Capability: CAP-09
- Primary role: Analyst
- Requirement: Maintain multiple hypotheses including legitimate explanations.
- Data objects: Hypothesis
- Controls: HYP-01
- Acceptance: At least one alternative hypothesis is supported for high-impact adverse assessment unless rationale documented.

### F-HYP-002 — Evidence support / contradiction matrix (P0)
- Capability: CAP-09
- Primary role: Analyst
- Requirement: Link evidence and indicators as supporting, contradicting, neutral or unknown for each hypothesis.
- Data objects: Hypothesis,EvidenceItem,Indicator
- Controls: HYP-01,HYP-02
- Acceptance: Matrix records analyst and rationale.

### F-HYP-003 — Intelligence gaps (P0)
- Capability: CAP-09
- Primary role: Analyst
- Requirement: Record unknowns that could materially change assessment.
- Data objects: IntelligenceGap
- Controls: GAP-01
- Acceptance: Final product surfaces material unresolved gaps.

### F-ASM-001 — Assessment record (P0)
- Capability: CAP-09
- Primary role: Analyst
- Requirement: Write judgement, confidence, basis, alternatives, assumptions and gaps.
- Data objects: Assessment
- Controls: ASM-01
- Acceptance: Assessment cannot be final without confidence and evidence-linked basis.

### F-ASM-002 — Confidence scale (P0)
- Capability: CAP-09
- Primary role: Analyst
- Requirement: Apply controlled confidence language with rationale.
- Data objects: Assessment
- Controls: ASM-01
- Acceptance: Confidence changes are versioned.

### F-ASM-003 — Disconfirming search record (P0)
- Capability: CAP-09
- Primary role: Reviewer
- Requirement: Document what was done to search for evidence that weakens adverse findings.
- Data objects: Review,Hypothesis
- Controls: HYP-02,QUA-01
- Acceptance: High-impact product cannot pass review if no disconfirmation record/rationale.

### F-SCH-001 — Full-text search (P0)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Search case-authorised documents/evidence and extracted text.
- Data objects: EvidenceItem,DerivedArtifact
- Controls: SEC-01
- Acceptance: Results enforce object-level permissions.

### F-SCH-002 — Faceted entity/object search (P0)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Filter by entity type, identifier, jurisdiction, case, source, date and status.
- Data objects: Entity,Source,Case
- Controls: SEC-01
- Acceptance: Search does not reveal restricted object existence where policy forbids it.

### F-GRF-001 — Graph exploration (P0)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Explore entities, relationships, assets, events and flows visually.
- Data objects: Entity,Relationship,Asset,ValueFlow
- Controls: REL-01,SEC-01
- Acceptance: Every material edge can display provenance/confidence.

### F-GRF-002 — Path finding (P1)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Find paths between two entities under permission and relationship filters.
- Data objects: Relationship
- Controls: TEC-02
- Acceptance: Path result is labelled analytical output, not proof of association beyond underlying edges.

### F-GRF-003 — Network metrics (P2)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Run centrality, community and cluster analytics as assistive signals.
- Data objects: DerivedAnalytics
- Controls: TEC-02
- Acceptance: Algorithm/version/input scope are recorded and outputs cannot become facts automatically.

### F-SCH-003 — Saved searches / watch queries (P1)
- Capability: CAP-10
- Primary role: Analyst
- Requirement: Save recurring case-scoped queries and notify when new authorised data matches.
- Data objects: SavedQuery
- Controls: SEC-01
- Acceptance: Watch query scope inherits case permissions and can be disabled.

### F-PRD-001 — Intelligence product templates (P0)
- Capability: CAP-11
- Primary role: Analyst
- Requirement: Generate Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package and Case Report.
- Data objects: IntelligenceProduct
- Controls: ASM-01,DIS-01
- Acceptance: Product embeds version, classification, author/reviewer and evidence index.

### F-REV-001 — Peer review workflow (P0)
- Capability: CAP-11
- Primary role: Reviewer
- Requirement: Comment, request change, approve or reject high-impact products.
- Data objects: Review
- Controls: QUA-01
- Acceptance: Final approval is attributable and separate from author where required.

### F-REV-002 — Red-team review checklist (P1)
- Capability: CAP-11
- Primary role: Reviewer
- Requirement: Challenge identity, evidence, alternatives, confidence and potential harm.
- Data objects: Review
- Controls: QUA-01,HYP-02
- Acceptance: Checklist result is retained with product version.

### F-PRD-002 — Product versioning / corrections (P0)
- Capability: CAP-11
- Primary role: Analyst
- Requirement: Issue revised/corrected versions without deleting prior product history.
- Data objects: IntelligenceProduct
- Controls: AUD-01
- Acceptance: Recipients can distinguish superseded from current versions.

### F-PRD-003 — Evidence index generation (P0)
- Capability: CAP-11
- Primary role: Analyst
- Requirement: Generate evidence/source references supporting material findings.
- Data objects: IntelligenceProduct,EvidenceItem
- Controls: SRC-01,EVD-02
- Acceptance: Every key fact can be traced from product to evidence.

### F-DIS-001 — Dissemination approval (P0)
- Capability: CAP-12
- Primary role: Case Owner
- Requirement: Approve external sharing with handling classification and intended recipient.
- Data objects: Dissemination
- Controls: DIS-01
- Acceptance: External export is blocked until required approval is present.

### F-DIS-002 — Secure export package (P0)
- Capability: CAP-12
- Primary role: Analyst
- Requirement: Export approved report and evidence index with minimisation/redaction.
- Data objects: Dissemination,IntelligenceProduct
- Controls: DIS-01,PRI-01
- Acceptance: Export records included objects and excludes unauthorised restricted content.

### F-DIS-003 — Referral package (P0)
- Capability: CAP-12
- Primary role: Analyst
- Requirement: Produce structured referral containing subjects, facts, evidence, timeline, flows, indicators, gaps and contact point.
- Data objects: IntelligenceProduct,Dissemination
- Controls: DIS-01
- Acceptance: Referral distinguishes known facts from analysis and unknowns.

### F-DIS-004 — Sharing log (P0)
- Capability: CAP-12
- Primary role: Case Owner
- Requirement: Record who received what version, when, purpose and restrictions.
- Data objects: Dissemination
- Controls: DIS-01,AUD-01
- Acceptance: Log is immutable to ordinary analysts.

### F-DIS-005 — Partner workspace / federation (P2)
- Capability: CAP-12
- Primary role: Partner
- Requirement: Share selected objects/products with controlled partner environment.
- Data objects: SharedObject
- Controls: SEC-01,DIS-01
- Acceptance: Sharing is explicit object-level allowlist; no implicit case replication.

### F-ADM-001 — Controlled vocabulary administration (P0)
- Capability: CAP-13
- Primary role: Admin
- Requirement: Manage relationship types, asset types, statuses and classifications with versioning.
- Data objects: Vocabulary
- Controls: AUD-01
- Acceptance: Historical records preserve original term/version semantics.

### F-ADM-002 — Template administration (P1)
- Capability: CAP-13
- Primary role: Admin
- Requirement: Configure case, review and report templates.
- Data objects: Template
- Controls: AUD-01
- Acceptance: Template changes are versioned and do not rewrite historical products.

### F-ADM-003 — Retention policies (P0)
- Capability: CAP-13
- Primary role: Admin/Privacy
- Requirement: Configure retention/disposition by classification and object type.
- Data objects: RetentionPolicy
- Controls: PRI-02
- Acceptance: Policy execution can be previewed and audited.

### F-ADM-004 — Feature flags / environment policy (P1)
- Capability: CAP-13
- Primary role: Platform Admin
- Requirement: Enable high-risk capabilities (AI, external connectors, federation) per deployment.
- Data objects: SystemPolicy
- Controls: SEC-01
- Acceptance: Disabled capability cannot be bypassed through API.

### F-SEC-001 — OIDC authentication + MFA (P0)
- Capability: CAP-14
- Primary role: All users
- Requirement: Authenticate through organisation identity provider with MFA where required.
- Data objects: User,Session
- Controls: SEC-01
- Acceptance: Disabled user loses access; session policy enforced.

### F-SEC-002 — Role and object-level access control (P0)
- Capability: CAP-14
- Primary role: Security Admin
- Requirement: Restrict access by role, case membership, classification and need-to-know.
- Data objects: AccessPolicy
- Controls: SEC-01,SEC-02
- Acceptance: API and UI enforce the same authorisation decision.

### F-SEC-003 — Protected-source compartment (P0)
- Capability: CAP-14
- Primary role: Source Handler
- Requirement: Store protected source identity separately with restricted access.
- Data objects: ProtectedSource
- Controls: SEC-02
- Acceptance: Routine analysts can use source-derived evidence without automatically seeing identity.

### F-AUD-001 — Immutable audit trail (P0)
- Capability: CAP-14
- Primary role: Auditor
- Requirement: Record material create/update/delete/merge/review/export actions.
- Data objects: AuditEvent
- Controls: AUD-01
- Acceptance: Ordinary users cannot edit audit events.

### F-OPS-001 — Backup and restore (P0)
- Capability: CAP-14
- Primary role: Security Admin
- Requirement: Back up canonical DB, evidence and configuration; test restore.
- Data objects: BackupRecord
- Controls: SEC-01
- Acceptance: Restore test is documented at defined interval.

### F-OPS-002 — Operational monitoring (P1)
- Capability: CAP-14
- Primary role: Platform Admin
- Requirement: Monitor health, errors, jobs, capacity and security events without logging sensitive evidence content.
- Data objects: OperationalEvent
- Controls: SEC-01
- Acceptance: Observability redacts/avoids case-sensitive payloads.

### F-OPS-003 — Incident response support (P1)
- Capability: CAP-14
- Primary role: Security Admin
- Requirement: Record security incidents affecting sources, evidence, accounts or exports.
- Data objects: SecurityIncident
- Controls: SEC-02
- Acceptance: Incident workflow supports containment, notification and lessons learned.

### F-INT-001 — OpenAleph connector (P1)
- Capability: CAP-15
- Primary role: Analyst
- Requirement: Link/import investigative documents/entities from OpenAleph with provenance.
- Data objects: ExternalReference,Entity,Source
- Controls: SRC-01
- Acceptance: Imported objects retain remote IDs and source metadata; no silent merge.

### F-INT-002 — OpenSanctions screening connector (P1)
- Capability: CAP-15
- Primary role: Analyst
- Requirement: Screen entity against sanctions/PEP/debarment data and review candidate matches.
- Data objects: ScreeningResult
- Controls: ENT-01,TEC-01
- Acceptance: Screening result is a candidate signal, not canonical identity/fact until reviewed.

### F-INT-003 — FollowTheMoney mapping (P1)
- Capability: CAP-15
- Primary role: Data Steward
- Requirement: Map compatible entities/ownership/payment concepts to/from FollowTheMoney.
- Data objects: Entity,Relationship,ValueFlow
- Controls: AUD-01
- Acceptance: Import/export mapping is versioned and preserves unmapped fields.

### F-INT-004 — Flowintel interoperability (P2)
- Capability: CAP-15
- Primary role: Case Owner
- Requirement: Link task/case workflow metadata with Flowintel where used.
- Data objects: ExternalCaseReference
- Controls: AUD-01
- Acceptance: No implicit transfer of sensitive evidence without explicit configuration.

### F-INT-005 — GraphSense connector (P2)
- Capability: CAP-15
- Primary role: Analyst
- Requirement: Enrich public-chain wallet/address analysis using GraphSense.
- Data objects: ExternalReference,ValueFlow
- Controls: TEC-01
- Acceptance: Blockchain analytics output remains attributed to provider and timestamp.

### F-INT-006 — Graph projection connector (P1)
- Capability: CAP-15
- Primary role: Platform Admin
- Requirement: Project canonical relationship/value-flow data to Neo4j/Memgraph or equivalent.
- Data objects: DerivedProjection
- Controls: REL-01
- Acceptance: Projection is rebuildable and cannot become sole canonical source.

### F-AI-001 — AI summarisation / extraction assist (P1)
- Capability: CAP-15
- Primary role: Analyst
- Requirement: Use AI to summarise or propose entities/relationships from authorised content.
- Data objects: DerivedArtifact,Candidate
- Controls: TEC-01
- Acceptance: AI output is labelled generated, attributable to model/version, and review-required.

### F-AI-002 — AI analytical assistant (P2)
- Capability: CAP-15
- Primary role: Analyst
- Requirement: Ask questions across authorised case data with citations to canonical objects.
- Data objects: DerivedAnalysis
- Controls: TEC-01,TEC-02
- Acceptance: Assistant cannot create final adverse assessment or dissemination approval autonomously.


## MVP completion test
A two-analyst team SHALL be able to open a case, ingest evidence, resolve entities, build an ownership/asset/value-flow model, test at least two hypotheses, map relevant typologies, produce a confidence-rated assessment, complete independent review, and export an approved intelligence product while preserving provenance and audit history.


## Build vs integrate
Build the unique CS-AML investigation layer; integrate mature OCR/document intelligence, screening, graph database, blockchain analytics, IAM, search, object storage and observability components.

# CS-AML MVP Engineering Breakdown v0.1

**Status:** Engineering execution baseline for MVP 0.1

## Objective
Translate the CS-AML PRD and SRS P0 baseline into an executable engineering backlog while preserving traceability from requirement to test.

## Delivery axiom
Build vertical, reviewable investigation capabilities; do not optimize for component completion if the end-to-end analytical chain remains broken.

## Traceability
`Framework → Feature → PRD → SRS → Epic → Story → Task → Acceptance Test → Release Evidence`

## MVP release objective
A two-analyst team SHALL complete one sensitive investigation from case opening through independently reviewed and approved intelligence product, with provenance, authorization and auditability intact.

## Epic map

### E0 — Platform Foundation & Delivery
**Outcome:** Establish the deployable application skeleton, environments, CI/CD, canonical database, evidence storage, audit substrate, and engineering conventions.
**Traceability:** SRS-OPS; SRS-DR; SRS-AUD; F-OPS-001; F-AUD-001

### E1 — Identity, Access & Protected Sources
**Outcome:** Implement OIDC/MFA integration, role/object access controls, case membership, classification, and protected-source compartment.
**Traceability:** SRS-SEC; F-SEC-001..003

### E2 — Case & Investigation Workflow
**Outcome:** Implement case register, investigation charter, lifecycle gates, tasks, assignments, and case activity history.
**Traceability:** SRS-FR-CASE; F-CASE-001..005

### E3 — Source, Evidence & Document Intake
**Outcome:** Implement source provenance, original evidence preservation, hashing, extracts, derivative lineage, ratings, and document ingestion.
**Traceability:** SRS-FR-EVD/DOC; F-EVD-001..006; F-DOC-001

### E4 — Entity Resolution & Relationship Model
**Outcome:** Implement entity registry, aliases/identifiers, candidate matching, merge/unmerge, relationship, ownership/control, and asset registry.
**Traceability:** SRS-FR-ENT/REL/AST; F-ENT-001..005; F-REL-001..003; F-AST-001

### E5 — Timeline & Follow-the-Value
**Outcome:** Implement events, visual timeline, ValueFlow records, multi-leg chains, uncertainty classes, range/unknown values, and flow visualization.
**Traceability:** SRS-FR-TIM/VAL; F-TIM-001..002; F-VAL-001..004

### E6 — Typology, Hypothesis & Assessment
**Outcome:** Implement typology catalogue, indicators, typology worksheet, competing hypotheses, gaps, confidence, and assessments.
**Traceability:** SRS-FR-TYP/HYP/ASM; F-TYP-001..003; F-HYP-001..003; F-ASM-001..003

### E7 — Search & Investigation Graph
**Outcome:** Implement permission-aware full-text/faceted search and evidence-backed graph visualization with canonical links.
**Traceability:** SRS-FR-SCH/GRF; F-SCH-001..002; F-GRF-001

### E8 — Intelligence Product, Review & Dissemination
**Outcome:** Implement report templates, evidence index, peer review, versioning/corrections, approvals, export/referral, and dissemination log.
**Traceability:** SRS-FR-PRD/REV/DIS; F-PRD-001..003; F-REV-001; F-DIS-001..004

### E9 — Administration, Retention & Operational Readiness
**Outcome:** Implement vocabularies, retention policies, backup/restore, configuration, minimum monitoring, security hardening, and release verification.
**Traceability:** SRS-FR-ADM/SEC/AUD/OPS; F-ADM-001; F-ADM-003; F-OPS-001

## Delivery increments

- **I0 — Engineering Foundation** — E0 + core E1: Runnable secure skeleton; migrations, canonical DB, object storage, audit, OIDC baseline.
- **I1 — Governed Case Workspace** — E1 + E2: Authenticated team can create compartmentalized case, charter, gates, tasks and activity.
- **I2 — Evidence-to-Entity Chain** — E3 + E4 partial: Team can register source, preserve evidence, cite extracts and build reviewable entities.
- **I3 — Investigation Model** — E4 remainder + E5: Relationships, assets, timeline and value-flow analysis become usable end-to-end.
- **I4 — Analytical Reasoning** — E6: Typology, hypotheses, gaps, assessment and confidence complete analytical chain.
- **I5 — Discovery & Graph** — E7: Search and graph improve navigation without becoming canonical truth.
- **I6 — Reviewed Intelligence Product** — E8: Assessment becomes reviewed/versioned intelligence product with controlled export.
- **I7 — Operational Release** — E9 + regression: Retention, restore, hardening and full MVP release scenario verified.

## Detailed backlog

### E0

#### ST-E0-01 — Repository and service skeleton
As an engineer, I need a reproducible project structure so all later capabilities share conventions.

**Engineering tasks**
- Create backend, frontend, worker and infrastructure directories
- Configure environment-based settings and secrets
- Define coding/lint/test conventions
- Add health endpoint and build metadata

**Acceptance**
- Fresh checkout can run locally from documented commands
- CI executes lint + unit tests
- No production secret is committed

#### ST-E0-02 — Canonical PostgreSQL baseline
As a data steward, I need versioned canonical storage so analytical objects have a durable source of truth.

**Engineering tasks**
- Create database migration framework
- Implement common object envelope: UUID, timestamps, version, classification, created_by
- Add soft/superseded state conventions
- Create migration rollback/test strategy

**Acceptance**
- Migrations apply to empty database
- Schema version is queryable
- Canonical IDs remain stable across updates

#### ST-E0-03 — Evidence object storage baseline
As an evidence custodian, I need originals stored separately from metadata.

**Engineering tasks**
- Configure S3-compatible or filesystem evidence store
- Use opaque object keys, not user filenames
- Store checksum and content metadata in DB
- Block in-place overwrite of originals

**Acceptance**
- Uploading same filename twice creates distinct evidence versions
- Original object cannot be modified by analyst role

#### ST-E0-04 — Audit event substrate
As an auditor, I need material changes captured consistently.

**Engineering tasks**
- Define AuditEvent schema
- Create application audit helper/middleware
- Capture actor, action, object, before/after reference, timestamp, request correlation
- Protect audit records from ordinary modification

**Acceptance**
- Create/update/delete/merge/export actions produce events
- Analyst cannot alter audit history

### E1

#### ST-E1-01 — OIDC login and session policy
As a user, I need organisational SSO so access can be centrally revoked.

**Engineering tasks**
- Implement OIDC authorization code flow
- Map IdP subject to local user
- Enforce session timeout and logout
- Support MFA claim/policy checks

**Acceptance**
- Disabled IdP user cannot establish new session
- Session shows authenticated identity and roles

#### ST-E1-02 — Role and case membership authorization
As a case owner, I need need-to-know access so sensitive cases stay compartmentalised.

**Engineering tasks**
- Define roles: investigator, case_owner, reviewer, data_steward, evidence_custodian, admin, auditor
- Implement case membership ACL
- Apply authorization in API layer, not UI only
- Add classification checks

**Acceptance**
- Direct API request cannot bypass case membership
- Unauthorized object IDs return non-disclosing denial

#### ST-E1-03 — Protected-source compartment
As a source handler, I need source identity separated from routine evidence.

**Engineering tasks**
- Create ProtectedSource model/store
- Separate identity from source-derived evidence reference
- Restrict handler role
- Redact identity from normal search/index/audit payloads

**Acceptance**
- Routine analyst can use source-derived evidence without source identity
- Protected identity never appears in normal export

### E2

#### ST-E2-01 — Case register and creation
As an investigator, I need a stable case workspace.

**Engineering tasks**
- Create Case model/API/UI
- Required fields: title, purpose, owner, classification, status
- Generate stable case identifier
- Case list filters by status/owner/classification

**Acceptance**
- Case cannot activate without owner, purpose, question
- Case history records creation

#### ST-E2-02 — Investigation Charter
As a case owner, I need scope and boundaries recorded before substantive work.

**Engineering tasks**
- Implement investigation question, scope included/excluded, jurisdictions, period, risks, authorised/prohibited collection
- Version charter
- Require reason for material scope change

**Acceptance**
- Old charter version remains retrievable
- Scope change produces audit event

#### ST-E2-03 — Lifecycle gates G0-G6
As governance reviewer, I need high-risk actions controlled by gates.

**Engineering tasks**
- Model gates and gate requirements
- Gate submission/approval/rejection
- Prevent self-approval when policy requires independence
- Record conditions and unresolved gaps

**Acceptance**
- Controlled transition is blocked without approval
- Approval predates downstream action

#### ST-E2-04 — Tasks and assignments
As an investigator, I need actionable work tracked.

**Engineering tasks**
- Task model with owner/status/due date/type
- Case task board/list
- Completion history
- Link tasks to sources/entities/hypotheses where relevant

**Acceptance**
- Task ownership and completion are visible
- Closed task retains historical state

#### ST-E2-05 — Case activity timeline
As a reviewer, I need to reconstruct material case activity.

**Engineering tasks**
- Project relevant AuditEvents into case activity
- Filter by actor/action/object
- Link activity to canonical object

**Acceptance**
- Material case events appear chronologically
- Activity item opens the referenced object when authorized

### E3

#### ST-E3-01 — Source register
As an investigator, I need material sources registered with provenance.

**Engineering tasks**
- Source model/API/UI
- Capture origin, publisher, URL/location, publication/access dates, access method, legal note
- Archive reference and reliability fields

**Acceptance**
- Assessment-linked source must contain provenance minimum
- Mutable web source can reference preserved copy

#### ST-E3-02 — Original evidence ingestion
As a custodian, I need evidence originals preserved.

**Engineering tasks**
- Upload API with streaming size limits
- Virus/malware scanning hook
- Write immutable original
- Capture MIME/size/filename/acquired_at/collector

**Acceptance**
- Failed ingest never creates misleading completed record
- Original remains unchanged after analyst actions

#### ST-E3-03 — Hash/integrity verification
As a reviewer, I need to verify evidence integrity.

**Engineering tasks**
- Compute SHA-256 at ingest
- Store algorithm/hash
- Add reverify action
- Flag mismatch

**Acceptance**
- Recomputed hash matches stored original in normal case
- Mismatch creates security/audit event

#### ST-E3-04 — Evidence extracts and citations
As an analyst, I need precise excerpts linked to originals.

**Engineering tasks**
- EvidenceExtract object
- Support page/paragraph/region/location descriptor
- Preview parent context
- Link extract to claims/facts

**Acceptance**
- Extract cannot exist without parent evidence
- Citation opens exact parent location where supported

#### ST-E3-05 — Derivative lineage
As an analyst, I need OCR/translation/processed copies distinguished from originals.

**Engineering tasks**
- Derivative model and parent link
- Transformation type/tool/version/time/creator
- Prevent derivative from replacing original
- Lineage UI

**Acceptance**
- Every derivative traces to original
- Original and derivative are visually distinct

#### ST-E3-06 — Reliability and credibility ratings
As an analyst, I need source reliability separate from information credibility.

**Engineering tasks**
- Implement A-F source scale
- Implement 1-6 information credibility scale
- Require rationale for material ratings
- Allow reassessment history

**Acceptance**
- UI does not merge the two ratings
- Rating change is versioned/audited

### E4

#### ST-E4-01 — Entity registry
As an analyst, I need reusable entities outside case silos.

**Engineering tasks**
- Entity model by type
- Canonical name, aliases, identifiers, jurisdictions, status
- Case-to-entity association without duplicating entity

**Acceptance**
- Same canonical entity can appear in multiple authorized cases
- Entity record preserves provenance-bearing assertions

#### ST-E4-02 — Aliases and identifiers
As an analyst, I need conflicting identifiers represented without destructive overwrite.

**Engineering tasks**
- Identifier records with type/value/source/status
- Alias records with source/time
- Uniqueness rules only where justified

**Acceptance**
- Conflicting values coexist with provenance
- No silent overwrite

#### ST-E4-03 — Candidate entity matching
As an analyst, I need a reviewable duplicate-candidate screen.

**Engineering tasks**
- Candidate matching on normalized name + identifiers
- Display matching and conflicting attributes
- No auto-merge in MVP

**Acceptance**
- Candidate screen explains why pair was suggested
- Common name alone does not force merge

#### ST-E4-04 — Merge and unmerge
As a data steward, I need reversible entity resolution.

**Engineering tasks**
- MergeDecision record
- Preserve old IDs as aliases/superseded records
- Repoint relationships with history
- Implement unmerge recovery

**Acceptance**
- Unmerge restores prior object topology
- Merge rationale/evidence is mandatory

#### ST-E4-05 — Relationships, ownership and control
As an analyst, I need first-class connections with evidence.

**Engineering tasks**
- Relationship model with type/endpoints/evidence/confidence/time
- OwnershipInterest with percentage nullable
- ControlAssertion distinguishes legal owner/beneficial owner/controller/user

**Acceptance**
- Graph edge always traces to relationship record
- Unknown percentage remains null, not zero

#### ST-E4-06 — Asset registry
As an analyst, I need assets linked to ownership/control assertions.

**Engineering tasks**
- Asset model/types/identifiers/location
- Attribution relationship to person/org
- Evidence and status

**Acceptance**
- Asset attribution distinguishes ownership/control/use
- Material attribution requires evidence link

### E5

#### ST-E5-01 — Events and temporal precision
As an analyst, I need chronology with uncertainty.

**Engineering tasks**
- Event object with date precision
- Link entities/assets/evidence
- Support exact date, month, year, range, unknown

**Acceptance**
- Approximate date is not rendered as exact
- Event links to supporting evidence

#### ST-E5-02 — Visual timeline
As an analyst, I need case chronology to reveal patterns.

**Engineering tasks**
- Timeline query/API
- Filters by entity/type/date
- Interactive UI and export representation

**Acceptance**
- Timeline respects object permissions
- Each item opens canonical event/evidence

#### ST-E5-03 — ValueFlow canonical model
As an analyst, I need transfer of economic value represented without pretending all flows are transactions.

**Engineering tasks**
- ValueFlow fields origin/destination/mechanism/value/currency/date/evidence
- Mandatory flow_class enum
- Confidence/status

**Acceptance**
- Cannot save flow without class
- Unknown value allowed without zero substitution

#### ST-E5-04 — Multi-leg flow builder
As an analyst, I need reconstructable chains.

**Engineering tasks**
- ValueFlowLeg model/order
- Builder UI
- Per-leg evidence/confidence/class
- Chain validation

**Acceptance**
- Each leg can carry different evidence/class
- Removing a leg does not destroy evidence objects

#### ST-E5-05 — Flow visualisation
As a reviewer, I need direct vs reconstructed flows visually unmistakable.

**Engineering tasks**
- Distinct labels/line semantics for four classes
- Legend always visible
- Export keeps class labels

**Acceptance**
- Screenshot/export can distinguish all classes without color alone
- No derived flow shown as direct

### E6

#### ST-E6-01 — Typology catalogue browser
As an analyst, I need versioned CS-AML typologies in the workflow.

**Engineering tasks**
- Load catalogue data
- Browse/search typologies
- Display mechanism, observables, false positives, version

**Acceptance**
- Assessment records catalogue version used
- Typology content cannot silently mutate historical case

#### ST-E6-02 — Indicator capture
As an analyst, I need evidence-linked indicators and counter-indicators.

**Engineering tasks**
- Indicator model with direction/type/significance
- Links to entities/events/flows/evidence
- Counter-indicator support

**Acceptance**
- Material indicator has evidence/proposition
- Indicator itself is not labelled proof

#### ST-E6-03 — Typology match worksheet
As an analyst, I need structured comparison rather than automatic accusation.

**Engineering tasks**
- TypologyMatch object
- Observed indicators/counter-indicators
- Consistency level
- Alternative explanations

**Acceptance**
- Single weak indicator cannot produce strong level automatically
- Analyst rationale required

#### ST-E6-04 — Competing hypotheses
As an analyst, I need multiple explanations tested.

**Engineering tasks**
- Hypothesis object/status
- Supporting/contradicting evidence links
- Alternative hypothesis set
- Assumptions

**Acceptance**
- At least two plausible hypotheses supported in pilot
- Rejected hypothesis remains in history

#### ST-E6-05 — Intelligence gaps
As an analyst, I need unknowns explicit.

**Engineering tasks**
- Gap object/question/impact/priority/status
- Link to hypothesis/assessment
- Closure rationale

**Acceptance**
- Assessment can list unresolved gaps
- Gap cannot be silently deleted

#### ST-E6-06 — Assessment and confidence
As an analyst, I need judgement with basis and uncertainty.

**Engineering tasks**
- Assessment versioning
- Judgement, confidence, rationale, assumptions, gaps, alternatives
- Evidence traversal

**Acceptance**
- Reviewer can trace assessment backward to evidence
- Confidence basis is mandatory for material assessment

### E7

#### ST-E7-01 — Permission-aware global search
As an analyst, I need to find authorized entities, cases and evidence.

**Engineering tasks**
- Search service/index or DB FTS
- Permission filtering before result display
- Filters by object type/case/date

**Acceptance**
- Unauthorized object never appears in count/snippet
- Search result links canonical object

#### ST-E7-02 — Faceted case search
As an analyst, I need focused search within a case.

**Engineering tasks**
- Facets for source/entity/event/evidence/relationship
- Case scope enforcement
- Saved query not required in MVP

**Acceptance**
- Facets respect ACL and classification
- Query response time meets MVP NFR target

#### ST-E7-03 — Investigation graph
As an analyst, I need visual entity/relationship/asset/value-flow exploration.

**Engineering tasks**
- Graph projection from canonical data
- Node/edge filtering
- Evidence/provenance side panel
- Save view state optionally

**Acceptance**
- Every material edge links to canonical relationship/evidence
- Projection can be rebuilt without data loss

### E8

#### ST-E8-01 — Intelligence product templates
As an analyst, I need consistent report outputs.

**Engineering tasks**
- Product model
- Templates: Financial Intelligence Note, Referral Package, Case Report
- Auto-populate metadata/classification/evidence index references

**Acceptance**
- Draft is versioned
- Product shows author/reviewer/status

#### ST-E8-02 — Evidence index generation
As a reviewer, I need claims traceable from report to evidence.

**Engineering tasks**
- Generate index from linked facts/assessments
- Include source/evidence IDs and citation locations
- Permission-aware inclusion

**Acceptance**
- Key fact in pilot has traversable evidence reference
- Restricted evidence is handled according to export policy

#### ST-E8-03 — Peer review workflow
As a reviewer, I need independent approval and change requests.

**Engineering tasks**
- Review states/commenting/request-changes/approve
- Prevent author self-approval where required
- Freeze reviewed version

**Acceptance**
- Approved version identifies independent reviewer
- Post-approval change creates new version

#### ST-E8-04 — Corrections and supersession
As a case owner, I need prior products retained when corrected.

**Engineering tasks**
- Supersedes relationship
- Status current/superseded/retracted
- Correction note

**Acceptance**
- Old version remains auditable
- Recipient-facing export identifies current version

#### ST-E8-05 — Dissemination approval and export
As a case owner, I need controlled external release.

**Engineering tasks**
- Dissemination object recipient/purpose/classification/approval
- Export minimization selector
- Generate package/report

**Acceptance**
- External export blocked before approval
- Export manifest lists included objects/version

#### ST-E8-06 — Referral package and sharing log
As an investigator, I need structured referral plus immutable sharing record.

**Engineering tasks**
- Referral template sections
- Sharing log record recipient/time/version/restrictions
- Audit export event

**Acceptance**
- Referral separates fact/analysis/gaps
- Ordinary analyst cannot edit completed sharing log

### E9

#### ST-E9-01 — Controlled vocabulary admin
As an admin, I need versioned vocabularies.

**Engineering tasks**
- Relationship/asset/status/classification vocabulary UI
- Version terms
- Disable without deleting historical semantics

**Acceptance**
- Historical record displays original term/version
- Vocabulary change audited

#### ST-E9-02 — Retention policy engine
As a privacy/admin role, I need retention/disposition states.

**Engineering tasks**
- RetentionPolicy model
- Apply by classification/object type
- Preview eligible records
- Hold/exception support

**Acceptance**
- Disposition requires authorization
- Legal hold blocks deletion

#### ST-E9-03 — Backup and restore
As an operator, I need recoverable canonical data and evidence.

**Engineering tasks**
- Automated DB backup
- Evidence store backup strategy
- Configuration backup
- Restore runbook and test

**Acceptance**
- Documented restore test succeeds
- Restored hashes/evidence references validate

#### ST-E9-04 — Operational hardening
As an operator, I need production-safe defaults.

**Engineering tasks**
- Security headers/TLS/reverse proxy
- Secrets management
- Rate limits/upload limits
- Error handling without sensitive leakage
- Minimal health/metrics

**Acceptance**
- No debug mode in production
- Sensitive evidence content absent from routine logs

#### ST-E9-05 — MVP end-to-end release test
As product owner, I need objective release evidence.

**Engineering tasks**
- Create representative pilot dataset
- Automate what can be automated
- Run two-analyst scenario
- Record failures and remediation

**Acceptance**
- All mandatory P0 SRS requirements pass or accepted exception exists
- Pilot completes case-to-approved-product with intact provenance/audit

## Engineering conventions
- Canonical records are authoritative; graph/search indexes are derived and rebuildable.
- Originals and derivatives are physically/logically distinguishable.
- Authorization is enforced server-side for every object access.
- Every material merge, assessment, approval, export and destructive action creates audit evidence.
- DIRECT, DOCUMENTED, RECONSTRUCTED and HYPOTHETICAL value flows remain distinguishable in data, API, UI and export.
- No MVP automation may silently promote candidate/inference into verified fact.

## Suggested repository boundaries
```text
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

## Release evidence package
- SRS traceability matrix with implementation/test status
- End-to-end pilot record
- Access-control test results
- Evidence hash/lineage verification results
- Entity merge/unmerge test
- Value-flow class export test
- Peer review and dissemination approval test
- Backup/restore test record
- Known limitations and accepted exceptions

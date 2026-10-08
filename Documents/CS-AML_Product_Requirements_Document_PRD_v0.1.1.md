**PRD v0.1.1**

> **Document status — v0.1.1**  
> Version: 0.1.1 — Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec). *[v0.1.1 · A01]*  
> Supersedes: CS-AML Product Requirements Document (PRD) v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.  
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (decision register and release gates in `CHANGELOG.md`). No implementation test result or independent audit exists yet. Acceptance criteria in this document are targets, not evidence that tests have passed.  
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.  
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).


Civil Society Financial Intelligence & AML Investigation Platform

Status: Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) — product baseline for MVP planning; not yet validated for engineering handoff *[v0.1.1 · A01]*

Version: 0.1.1 \| Date: 7 October 2026 (v0.1); revised for v0.1.1

> **Product axiom**  
> The platform SHALL help civil-society investigators produce lawful, evidence-based, reproducible, and actionable financial intelligence while preserving analytical uncertainty and preventing inference from being presented as fact.

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Product Requirements Document (PRD) |
| Version | 0.1.1 |
| Status | Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) / implementation planning *[v0.1.1 · A01]* |
| Audience | Product, engineering, investigation leads, security/privacy reviewers, QA, governance |
| Upstream specifications | CS-AML Framework; Goals & Non-Goals; Typology Catalogue; Investigation Methodology; Data Model Specification; Control Implementation Guide; Technology Architecture; Product & Feature Specification (all v0.1.1 Markdown, `Documents/*_v0.1.1.md`) |
| Normative intent | Defines product outcomes and MVP requirements. Detailed data semantics, controls, and architecture remain governed by their respective specifications. |

# 1. Executive Summary

CS-AML is a civil-society financial intelligence and AML investigation platform. It is designed for organisations that investigate corruption, fraud, environmental crime, illicit financial flows, procurement abuse, beneficial-ownership concealment, sanctions/PEP exposure, and related public-interest issues without possessing privileged core-banking access.

The product does not attempt to replicate a bank transaction-monitoring system. Its primary job is to turn lawful public-source and legitimately obtained information into a structured, reviewable intelligence process: Source → Evidence → Fact → Indicator → Hypothesis → Assessment → Intelligence Product.

> **MVP decision**  
> MVP 0.1 focuses on the complete investigation loop for one organisation: open a case, preserve sources/evidence, resolve entities, map relationships/assets/events/value flows, test typologies and hypotheses, draft an assessment, peer-review it, and generate a controlled intelligence product. Cross-organisation federation, advanced network science, crypto analytics, and autonomous AI are explicitly deferred.

# 2. Product Problem

> **Planning assumption** *[v0.1.1 · A01]*  
> The problem statement, pain points, jobs-to-be-done, and outcome targets in this PRD are planning assumptions derived from the CS-AML framework design. They are not results of user research and SHALL be validated with pilot users before being treated as evidence.

## 2.1 Problem statement

Civil-society investigations frequently begin with fragmented documents, public registries, spreadsheets, media reporting, procurement records, court decisions, tips, and analyst notes. Existing tools may support document search, graph analysis, or case management, but they rarely enforce an end-to-end discipline that preserves provenance, distinguishes fact from inference, supports competing hypotheses, and produces auditable financial-intelligence products.

## 2.2 User pain points

- Investigators lose time reconstructing where a claim came from and whether a source was preserved.

- Entity duplication creates false relationships and inconsistent case histories.

- Graphs can visually overstate certainty because an edge may look equally “real” whether observed, inferred, or disputed.

- Value flows are often reconstructed from contracts, assets, and ownership events rather than direct bank transactions, yet existing tools do not always preserve that distinction.

- Hypotheses, counter-evidence, intelligence gaps, and confidence judgements are commonly kept in prose rather than structured form.

- Peer review and dissemination approval are often external to the investigative record.

- Cross-case reuse of entities and evidence is difficult without sacrificing compartmentalisation.

- High-risk personal data and protected-source information require stronger controls than generic research tools provide.

# 3. Product Vision and Positioning

## 3.1 Vision

Enable civil-society investigators to build defensible financial-intelligence assessments from lawful information with the same discipline expected of professional intelligence work, without pretending to possess investigative powers or financial-system access that they do not have.

## 3.2 Product category

CS-AML is best positioned as a Civil Society Financial Intelligence & Investigation Platform. It combines case management, evidence/provenance, entity and asset analysis, graph investigation, follow-the-value reconstruction, typology analysis, hypothesis testing, and controlled intelligence-product generation.

## 3.3 Differentiation

| **Differentiator** | **Required product behaviour** |
|----|----|
| Evidence-first | Every material finding can be traced to source/evidence. |
| Analytical separation | Fact, indicator, hypothesis, assessment, and allegation remain distinct objects/states. |
| Follow-the-value | Supports direct, documented, reconstructed, and hypothetical flows without conflating them. |
| Reversible identity decisions | Entity resolution and merges are evidence-based, reviewable, and reversible. |
| Civil-society safety | Data minimisation, source protection, compartmentalisation, and controlled dissemination are native. |
| Intelligence discipline | Alternative hypotheses, disconfirming evidence, confidence, and gaps are part of the workflow—not optional notes. |

# 4. Product Goals and Non-Goals

## 4.1 Goals

1.  Reduce the time required to turn fragmented source material into a structured investigation.

2.  Increase the proportion of material findings with complete provenance and evidence lineage.

3.  Enable investigators to reconstruct ownership, control, assets, events, and value flows without privileged bank access.

4.  Reduce analytical errors caused by entity confusion, unsupported graph edges, confirmation bias, or lost context.

5.  Make high-impact intelligence products independently reviewable and reproducible.

6.  Provide a secure, role-aware workspace suitable for sensitive civil-society investigations.

7.  Provide an architecture that can integrate mature external tools rather than rebuilding generic capabilities unnecessarily.

## 4.2 Non-goals for MVP 0.1

- Bank-grade real-time transaction monitoring or regulatory STR/SAR submission automation.

- Automatic determination that a person committed money laundering or another offence.

- Autonomous publication, referral, entity merge, or adverse assessment by AI.

- Covert collection, hacking, credential theft, interception, or access to restricted financial systems.

- Full blockchain analytics engine.

- Cross-organisation federation or shared multi-tenant intelligence network.

- Advanced predictive risk scoring presented as an authoritative decision.

# 5. Target Users and Jobs-to-be-Done

The jobs and needs below are design assumptions, not user-research findings (see §2 planning assumption). *[v0.1.1 · A01]*

| **Role** | **Primary job** | **Core need** |
|----|----|----|
| Investigator / Analyst | Build and test a financial-intelligence case | I need to collect, structure, connect, test, and explain information without losing provenance or uncertainty. |
| Investigation Lead / Case Owner | Control scope, risk, priorities, and decisions | I need to know what is in scope, what remains unknown, and whether the case is ready to advance. |
| Peer Reviewer / Red Team | Challenge findings independently | I need to trace claims to evidence, inspect alternatives, and identify unsupported leaps. |
| Evidence Custodian / Data Steward | Protect evidence and data quality | I need to preserve originals, lineage, identifiers, merge history, retention, and integrity. |
| Security / Privacy Reviewer | Control sensitive data and exposure | I need visibility into classification, access, source protection, export, and retention decisions. |
| Product Approver / Editor | Approve an intelligence product for external use | I need evidence that identity, uncertainty, legal/privacy risk, and review requirements have been satisfied. |
| System Administrator | Operate the platform safely | I need secure identity, permissions, backup, monitoring, auditability, and controlled configuration. |

# 6. Core Product Principles

| **ID** | **Principle** |
|----|----|
| P-01 | Case is context; Entity and Evidence are reusable truth-bearing objects. |
| P-02 | Technology SHALL preserve analytical uncertainty rather than erase it. |
| P-03 | A graph edge is an analytical object with provenance, not merely a visual connection. |
| P-04 | Direct, documented, reconstructed, and hypothetical value flows SHALL remain distinguishable everywhere. |
| P-05 | Automation MAY suggest; a human SHALL own material analytical and dissemination decisions. |
| P-06 | Sensitive data collection SHALL be necessary, proportionate, and purpose-bound. |
| P-07 | High-impact claims SHALL be independently reviewable from the system of record. |
| P-08 | Derived search/graph/AI indexes are rebuildable projections; canonical evidence and records are authoritative. |

# 7. End-to-End User Journey

1\. Intake / lead registration

2\. Triage and legitimacy review

3\. Investigation Charter

4\. Collection plan

5\. Source and evidence registration

6\. Entity resolution

7\. Relationship / ownership / asset mapping

8\. Timeline and value-flow reconstruction

9\. Typology / indicator mapping

10\. Hypothesis testing and intelligence gaps

11\. Assessment and confidence

12\. Peer review / red-team review

13\. Intelligence product generation

14\. Dissemination approval / referral / publication

15\. Closure / monitoring / reopen

> **Lifecycle requirement**  
> The UI SHALL make the current investigation stage and unmet gate requirements visible. The product SHALL NOT silently imply that completion of a form equals analytical validation.

# 8. MVP 0.1 Scope

## 8.1 MVP definition

MVP 0.1 is successful when a small civil-society investigation team can complete one sensitive investigation from case opening through reviewed intelligence product using CS-AML as the system of record for the analytical chain.

## 8.2 MVP capability groups

| **ID** | **Capability** | **MVP content** |
|----|----|----|
| C1 | Case & workflow | Case register, Charter, G0–G6 gates, tasks, activity history |
| C2 | Sources & evidence | Source register, upload, originals, hashes, extracts, derivative lineage, source/credibility ratings, claim and fact lifecycle (claims, verification decisions, fact creation/revision — F-EVD-008) *[v0.1.1 · A10]* |
| C3 | Entities & relationships | Entity registry, aliases, candidate matching, reversible merge/unmerge recorded as append-only resolution decisions, first-class relationships, ownership/control *[v0.1.1 · ER]* |
| C4 | Assets, events & timeline | Asset records, events, timeline view |
| C5 | Value-flow | Flow records, multi-leg flows, classification, visualisation, unknown/range handling |
| C6 | Typology & indicators | Catalogue browser, indicator capture, typology worksheet |
| C7 | Hypothesis & assessment | Hypothesis matrix, support/contradiction, gaps, assessment, confidence, disconfirming-search record |
| C8 | Search & graph | Full-text search, object/entity search, graph exploration |
| C9 | Review & product | Peer review, six intelligence-product templates (Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report), versioning, evidence index *[v0.1.1 · A06]* |
| C10 | Dissemination | Approval, secure export, referral package, sharing log |
| C11 | Administration & security | Controlled vocabularies, retention, OIDC/MFA, object-level access, protected-source compartment, immutable audit, backup |

## 8.3 Deferred capability groups

| **Phase** | **Deferred capabilities** |
|----|----|
| Phase 2 | OCR/table extraction; entity candidate extraction; enrichment connectors; beneficial-ownership chain calculation; path finding; saved searches; OpenAleph/OpenSanctions/FollowTheMoney integrations; AI-assisted extraction/summarisation; operational monitoring. |
| Phase 3 | Network metrics/community detection; partner federation; Flowintel/GraphSense integrations; advanced AI analytical assistant; cross-organisation intelligence exchange. |

# 9. Functional Requirements by Epic

## EPIC-01 Case & Workflow

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-CASE-01 | Create and manage case | Analyst can create a case with owner, purpose, investigation question, scope, sensitivity, jurisdiction, period, and status. | Case record created; mandatory Charter fields validated; audit event created. |
| FR-CASE-02 | Investigation Charter | Case Owner can define included/excluded scope, initial subjects, hypotheses, collection constraints, risks, and intended outputs. | Charter is versioned; scope change requires reason and recorded approval when risk increases. |
| FR-CASE-03 | Lifecycle gates | System enforces G0–G6 gate records for configured high-risk actions. | Controlled action cannot be marked approved without approver, time, decision, and conditions. |
| FR-CASE-04 | Tasks and assignments | Users can assign investigative tasks with due dates and case linkage. | Task appears in case activity and user queue; completion recorded. |

## EPIC-02 Source & Evidence

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-EVD-01 | Source registration | Register source origin, type, URL/location, dates, collector, access/legal note, reliability. | Any material evidence can be traced to a Source ID. |
| FR-EVD-02 | Original evidence preservation | Upload/store original files separately from working derivatives. | Original cannot be silently overwritten; file metadata and hash retained. |
| FR-EVD-03 | Evidence extracts | Create page/section/quote/table/image extracts with exact parent link. | Reviewer can navigate from extract to parent evidence and location. |
| FR-EVD-04 | Derivative lineage | OCR, translation, crop, parsed data, or analyst dataset records parent and transformation metadata. | No derivative can be presented as an original. |
| FR-EVD-05 | Source & information evaluation | Record source reliability separately from information credibility. | UI displays both dimensions independently. |
| FR-EVD-06 | Claim and fact lifecycle | Record source claims without overwriting them; record each verification outcome as a separate decision; create provisional facts supported by evidence (mandatory) and, optionally, claims (claims remain unchanged) *[v0.1.1 · C02]*; establish (independent reviewer), dispute or supersede facts. | No extract or claim becomes a fact without a recorded verification decision; disputing/superseding a fact flags dependent assessments/products for review without altering published products. *[v0.1.1 · A10]* |

## EPIC-03 Entity & Relationship

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-ENT-01 | Entity registry | Create reusable Person, Organization, Address, Account, Wallet, Asset-related and other supported entity objects. | Stable ID; aliases/identifiers; case links without entity duplication. |
| FR-ENT-02 | Candidate matching | System surfaces possible duplicate entities using deterministic/fuzzy signals. | Candidate suggestion includes reasons; no automatic merge. |
| FR-ENT-03 | Merge/unmerge | Reviewer-authorised entity merges preserve decision rationale, evidence, aliases, identifiers, and history. | Merge is reversible and audit logged. |
| FR-REL-01 | Relationship records | Create relationship with typed endpoints, evidence, valid time, confidence, status. | Graph edge opens underlying relationship record and evidence. |
| FR-REL-02 | Ownership/control | Represent legal ownership, beneficial ownership, control, use, and association separately. | UI cannot collapse these concepts into one generic “owns” state. |

## EPIC-04 Assets, Events & Timeline

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-AST-01 | Asset registry | Register property, vehicle, company share, vessel, crypto asset, or other assets with ownership/control/use distinctions. | Asset has stable ID, evidence, dates, and status. |
| FR-TIM-01 | Event record | Create dated events linked to entities, assets, places, sources/evidence. | Date precision is explicit when exact date is unknown. |
| FR-TIM-02 | Timeline view | Render case/entity timeline from canonical events. | Every timeline item can be opened to supporting record/evidence. |

## EPIC-05 Follow-the-Value

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-VAL-01 | ValueFlow record | Record origin, destination, mechanism, date, amount/range/unknown, currency, evidence, confidence, and flow class. | Flow class is mandatory: DIRECT, DOCUMENTED, RECONSTRUCTED, HYPOTHETICAL. |
| FR-VAL-02 | Multi-leg flow | Link multiple legs into a coherent value-flow chain without losing leg-level evidence. | Each leg retains its own class/evidence; chain does not upgrade certainty. |
| FR-VAL-03 | Flow visualisation | Visualise value flow with visually distinct certainty classes. | Reviewer can distinguish direct vs reconstructed/hypothetical at first glance and via accessible labels. |

## EPIC-06 Typology & Hypothesis

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-TYP-01 | Typology catalogue | Browse CS-AML typologies and indicators in-version. | Case records typology catalogue version used. |
| FR-TYP-02 | Typology match worksheet | Map observed indicators/counter-indicators and assessment level. | System prevents typology match from being labelled as proof. |
| FR-HYP-01 | Hypothesis workspace | Create competing hypotheses and link supporting, contradicting, neutral evidence. | At least one alternative explanation can be recorded; status changes audited. |
| FR-HYP-02 | Intelligence gaps | Record unknowns that could materially change judgement. | Gaps appear in assessment and review views. |
| FR-ASM-01 | Assessment & confidence | Create judgement with confidence, basis, assumptions, alternatives, and gaps. | Assessment cannot be final without evidence basis and confidence rationale. |

## EPIC-07 Search & Graph

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-SCH-01 | Full-text search | Search permitted evidence/documents and analytical records. | Results respect object-level access and classification. |
| FR-SCH-02 | Structured search | Filter by entity type, identifiers, dates, relationship type, case, source, status. | Results link to canonical records. |
| FR-GRF-01 | Graph exploration | Explore entities and evidence-backed relationships interactively. | Graph never creates canonical relationships by display alone; inferred/suggested items visibly distinguished. |

## EPIC-08 Review, Product & Dissemination

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-REV-01 | Peer review | Independent reviewer records findings, required changes, and approval/rejection. | Author cannot satisfy mandatory independent review alone. |
| FR-PRD-01 | Intelligence product | Generate product, using one of the six MVP templates (Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report) *[v0.1.1 · A06]*, from approved assessment, key facts, evidence index, alternatives, gaps, confidence, handling classification. | Output preserves analytical qualifiers and stable evidence references. |
| FR-PRD-02 | Versioning/corrections | Products are versioned; corrections/supersession do not erase prior issued version. | Change history and reason are visible. |
| FR-DIS-01 | Dissemination approval | External dissemination requires authorised decision and handling rules. | Export/referral action creates approval and audit record. |
| FR-DIS-02 | Secure export/referral | Generate controlled package for legitimate recipient. | Package includes classification/handling and evidence index appropriate to recipient. |

## EPIC-09 Security, Privacy & Operations

| **Req ID** | **Requirement** | **Product behaviour** | **MVP acceptance** |
|----|----|----|----|
| FR-SEC-01 | Authentication | OIDC with MFA for privileged and sensitive access. | Failed/privileged auth events logged; session security enforced. |
| FR-SEC-02 | Access control | Role + need-to-know/object-level access. | Unauthorised case/entity/evidence is not discoverable through search, graph, API, export, or logs. |
| FR-SEC-03 | Protected-source compartment | Protected source identity stored separately with more restrictive access. | Routine analyst can use sanitised source reference without viewing identity. |
| FR-AUD-01 | Audit trail | Record material create/update/delete/merge/review/export/dissemination actions. | Audit record is append-only to normal users and queryable for review. |
| FR-OPS-01 | Backup/restore | Back up canonical DB and evidence; test restoration. | Documented restoration test successfully recovers selected case/evidence. |

# 10. UX / Information Architecture Requirements

## 10.1 Primary navigation

- Home / work queue

- Cases

- Entities

- Evidence & Sources

- Graph

- Search

- Typologies

- Reviews

- Products / Dissemination

- Administration

## 10.2 Case workspace

| **Surface** | **Minimum content** |
|----|----|
| Overview | Question, scope, owner, sensitivity, status, gates, critical gaps |
| Evidence | Sources, evidence, extracts, derivatives, provenance |
| Entities | Subjects, organisations, accounts/wallets, addresses, identifiers |
| Relationships / Graph | Evidence-backed network with confidence/status filters |
| Assets | Ownership/control/use, valuation where present |
| Timeline | Events with evidence and precision |
| Value Flow | Flow chain with certainty class |
| Typologies | Indicators/counter-indicators and catalogue version |
| Hypotheses | Competing explanations and evidence matrix |
| Assessment | Judgement, confidence, basis, gaps, alternatives |
| Review | Peer/red-team comments, disposition, sign-off |
| Product | Draft/final intelligence products, exports, sharing log |

## 10.3 UX safety requirements

- Fact, inference, hypothesis, and assessment SHALL use distinct labels and visual treatment.

- Reconstructed and hypothetical flows SHALL never use the same visual style as direct flows.

- Graph and search suggestions SHALL be labelled as suggestions until promoted by a human into canonical records.

- Destructive or high-impact actions (merge, disseminate, delete/retention disposal) SHALL require explicit confirmation and role checks.

- Protected-source identities SHALL never appear in global search snippets, generic logs, or exported reports unless specifically authorised.

# 11. Non-Functional Requirements

| **ID** | **Area** | **Requirement** |
|----|----|----|
| NFR-01 Security | Encryption in transit; protected storage for restricted evidence; strong authentication; least privilege; secure secrets management. |  |
| NFR-02 Privacy | Purpose binding, minimisation, classification, retention/disposition, access logging for high-sensitivity material. |  |
| NFR-03 Auditability | Material analytical and dissemination changes reconstructable from audit/version history. |  |
| NFR-04 Availability | MVP target: reliable single-organisation service with documented maintenance; restore capability prioritised over high availability. |  |
| NFR-05 Backup/DR | Automated backups; encrypted backup copies; tested restore; RPO/RTO documented before production deployment. |  |
| NFR-06 Performance | Common case/entity/search pages responsive for expected NGO-scale workloads; long analytics handled asynchronously. |  |
| NFR-07 Accessibility | Keyboard-accessible core workflow, readable labels, non-colour-only certainty/status encoding. |  |
| NFR-08 Interoperability | Stable IDs; API/export formats; no requirement that graph/search projections become system of record. |  |
| NFR-09 Explainability | Any material automated score/suggestion exposes contributing signals/version/limitations where applicable. |  |
| NFR-10 Maintainability | Schema migrations, versioned vocabularies, configuration history, environment separation, automated tests. |  |

# 12. Data Requirements

## 12.1 Minimum canonical objects

Case, Source, EvidenceItem, EvidenceExtract, Claim, VerificationDecision, Fact, Entity, ResolutionDecision *[v0.1.1 · ER]*, Relationship, Asset, Event, ValueFlow, Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment, IntelligenceProduct, Review, Dissemination, AuditEvent. *[v0.1.1 · A10]*

## 12.2 Mandatory analytical chain

> **Canonical chain**  
> SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT

## 12.3 Data integrity constraints

- Material Relationship objects require evidence reference or explicit analytical status explaining why evidence is unavailable.

- Merge decisions require match rationale, supporting/conflicting attributes, reviewer where configured, and reversibility. Every merge, unmerge, keep-separate, possible-match and defer decision is an append-only ResolutionDecision; entity resolution state changes only through these decisions. *[v0.1.1 · ER]*

- ValueFlow requires flow_class and may record amount as exact, range, or unknown.

- Assessment requires confidence and basis; high-impact assessment requires review record.

- Derivatives require parent evidence; original evidence cannot be silently replaced.

- All canonical objects use stable IDs and version/audit semantics defined by the Data Model Specification.

# 13. Integration Strategy

| **System** | **Phase** | **Purpose** | **Product rule** |
|----|----|----|----|
| OpenAleph | Phase 2 | Document ingestion/search/investigative workspace reference or connector | Do not duplicate mature document-processing capabilities if integration satisfies provenance/access requirements. |
| FollowTheMoney | Phase 2 | Ontology/interoperability mapping | Map where compatible; preserve CS-AML-specific Evidence/Hypothesis/Assessment semantics. |
| OpenSanctions | Phase 2 | PEP/sanctions/entity matching | Screening is contextual signal, not proof of wrongdoing. |
| Neo4j / Memgraph | Phase 2 | Derived graph projection / analytics | Canonical Relationship remains source of truth. |
| Flowintel | Phase 3 | Case/task interoperability | Use only if workflow interoperability provides value without duplicating CS-AML analytical state. |
| GraphSense | Phase 3 | Cryptoasset analytics | Connector rather than building chain analytics. |
| OIDC / Keycloak-compatible | MVP | Authentication/identity | Use standards-based IAM; MFA and role claims supported. |

# 14. AI and Automation Requirements

## 14.1 Permitted assistive uses

- OCR/text extraction assistance

- Translation assistance

- Entity candidate extraction

- Summarisation with source links

- Search/query assistance

- Suggested relationship or typology candidates

- Drafting assistance for analyst-controlled products

## 14.2 Prohibited autonomous decisions

- Determining guilt or criminality

- Publishing/referring a case

- Merging entities without human decision

- Converting a suggestion/inference into a material fact

- Revealing protected-source identity

- Overriding access controls or case compartmentalisation

## 14.3 Verification

AI output used materially SHALL remain a derived analytical artefact until verified against underlying evidence. The system SHOULD retain model/tool version and prompt/context provenance when needed for reproducibility without exposing unnecessary sensitive content.

# 15. Success Metrics

The values below are targets for the pilot; none has yet been measured. *[v0.1.1 · A01]*

| **Metric** | **Target / interpretation** |
|----|----|
| Provenance coverage | ≥95% of material facts in pilot products trace to registered evidence. |
| Review completeness | 100% of high-impact products have independent review before dissemination. |
| Entity resolution quality | All merged high-impact entities have recorded rationale; correction/unmerge rate monitored. |
| Analytical discipline | ≥90% of pilot assessments record alternatives and material intelligence gaps. |
| Workflow adoption | Pilot investigators complete an end-to-end case without maintaining a parallel “shadow” system for core analytical state. |
| Safety | 0 unauthorised disclosures of protected-source identity during pilot. |
| Recovery | Successful tested restore of a selected case and evidence set before production launch. |
| Usefulness | Pilot users rate evidence traceability, graph/value-flow understanding, and review workflow as materially better than baseline process. |

# 16. MVP Acceptance / Release Gate

> **MVP 0.1 release gate**  
> The release is not “done” because all screens exist. It is done when a representative case can be completed end-to-end with provenance, access controls, analytical separation, peer review, export controls, and restore/audit evidence functioning together.

8.  Create a case and approved Investigation Charter.

9.  Register at least three different source/evidence types and preserve originals.

10. Create evidence extracts with lineage; record a source claim and create a provisional fact supported by it through a recorded verification decision. *[v0.1.1 · A10]*

11. Create and resolve duplicate entity candidates, including one reversible merge.

12. Create evidence-backed relationships and render them in graph view.

13. Record asset/event/timeline data.

14. Build a multi-leg value-flow chain containing at least two different flow classes.

15. Apply one typology worksheet with counter-indicators.

16. Test at least two competing hypotheses and record an intelligence gap.

17. Create an assessment with confidence and disconfirming-search record.

18. Complete independent peer review.

19. Generate an intelligence product with evidence index and handling classification.

20. Approve and export a controlled referral/share package.

21. Confirm access-control isolation for a restricted case and protected-source identity.

22. Restore the pilot case and evidence from backup and verify audit continuity.

# 17. Product Risks and Mitigations

| **ID** | **Risk** | **Failure mode** | **Mitigation** |
|----|----|----|----|
| R-01 | Scope explosion | Trying to implement all 88 catalogue features at once. *[v0.1.1 · A10]* | Freeze MVP capability list; phase integrations and advanced analytics. |
| R-02 | Graph overclaim | Users infer wrongdoing from visual proximity. | Evidence-backed edges, certainty labels, legends, relationship status and training. |
| R-03 | Entity false merge | Common names/addresses create false networks. | Candidate state, reviewer decision, merge rationale, reversible merges. |
| R-04 | Sensitive data exposure | Protected source or private data leaks through search/export/logs. | Compartmentalisation, object permissions, sanitised references, export approval, security tests. |
| R-05 | Analytical bureaucracy | Framework creates forms without improving investigation. | Measure outcomes/usefulness; keep gates risk-based; reduce low-value mandatory fields. |
| R-06 | AI authority creep | Users treat AI suggestion as verified fact. | Derived-state labels, verification gate, no autonomous merge/dissemination/adverse judgement. |
| R-07 | Tool duplication | Rebuild OCR, screening, crypto, or document search poorly. | Build-vs-integrate reviews and connectors to mature tools. |
| R-08 | Legal/jurisdiction variance | Lawful collection and publication differ by jurisdiction. | Configurable policy; legal review gate; do not hard-code one jurisdiction as universal law. |

# 18. Delivery Plan

## 18.1 Suggested releases

| **Release** | **Outcome** | **Scope** |
|----|----|----|
| 0.1 Alpha | Core analytical chain works | Case, evidence, entity/relationship, assets/events, value-flow, typology, hypothesis, assessment, basic graph/search, auth/audit. |
| 0.1 Beta | Safe review and dissemination | Peer review, product generation, classification, secure export/referral, backup/restore, pilot security/privacy tests. |
| 0.1 Production | Operational baseline | Pilot feedback resolved, conformance evidence, operational documentation, monitoring, incident/restore procedures. |
| 0.2 | Investigation acceleration | Document processing, enrichment, BO chains, path finding, saved searches, first connectors, AI assist. |
| 0.3 | Network intelligence | Cross-case analytics, advanced graph metrics, federation/partner workflows, crypto connector, controlled advanced AI. |

## 18.2 Suggested engineering epics

- E1 Platform foundation & IAM

- E2 Canonical data model & API

- E3 Case/workflow & gates

- E4 Evidence/provenance storage

- E5 Entity resolution & relationships

- E6 Assets/events/timeline

- E7 Value-flow engine

- E8 Typology/hypothesis/assessment

- E9 Search & graph projection

- E10 Review/product/dissemination

- E11 Audit/security/privacy controls

- E12 Backup/restore/ops & pilot readiness

# 19. Dependencies

| **Dependency** | **Why it matters** | **Owner / decision** |
|----|----|----|
| Canonical Data Model v0.1.1 | Objects, statuses, IDs, lineage and validation drive API/database. | Architecture/Data |
| Investigation Methodology v0.1.1 | Defines lifecycle and gates. | Investigation/Product |
| Control Implementation Guide v0.1.1 | Defines security, privacy, review and audit controls. | Governance/Security |
| Typology Catalogue v0.1.1 | Provides versioned typology content and indicators. | Methodology/AML |
| Technology Architecture v0.1.1 | Constrains canonical vs derived stores, security, deployment and AI. | Architecture |
| Legal/privacy policy | Defines jurisdiction-specific lawful collection, retention, publication and sharing. | Governance/Legal |
| Pilot cases/users | Needed for usability, conformance and outcome testing. | Product/Investigation |

# 20. Open Product Decisions

| **ID** | **Decision** | **Recommended baseline** |
|----|----|----|
| D-01 | Single-organisation first or multi-tenant from day one? | Recommend single-organisation logical deployment for MVP; design IDs/access boundaries to permit later tenancy. |
| D-02 | Native document processing vs OpenAleph-first? | Recommend minimal native upload/text metadata in MVP; evaluate OpenAleph connector for Phase 2. |
| D-03 | Graph store at MVP? | Recommend relational canonical relationships and lightweight projection first; dedicated graph DB only when path/network workloads justify it. |
| D-04 | How strict are lifecycle gates? | Make gate enforcement configurable by risk profile; never make high-impact dissemination optional. |
| D-05 | Which jurisdictions first? | Keep core implementation-neutral; create local policy pack for Indonesia as an initial deployment option. |
| D-06 | Offline/air-gapped support? | Decide based on threat model of pilot organisations; architecture should not assume permanent cloud connectivity. |
| D-07 | Public/open-source release model? | Decide licensing, governance, security disclosure, and public roadmap before external release. |

# 21. Definition of Done

A feature is done only when its user-visible behaviour, canonical data state, permissions, audit events, tests, error handling, migration implications, and documentation are complete. For security/privacy-sensitive features, threat/abuse cases and negative tests are part of the definition of done.

| **Dimension** | **Done when** |
|----|----|
| Product | User story and acceptance criteria satisfied. |
| Data | Canonical objects validate and preserve provenance/version semantics. |
| Security | Authorisation and sensitive-data rules pass positive and negative tests. |
| Audit | Material actions create expected audit events. |
| UX | Status/uncertainty is legible and accessible. |
| QA | Automated tests plus representative end-to-end scenario pass. |
| Operations | Backup/restore/monitoring impact documented where relevant. |
| Documentation | User/admin/API documentation updated. |

# 22. Traceability to CS-AML Specifications

| **PRD area** | **Upstream authority** |
|----|----|
| Goals/non-goals | CS-AML Framework Goals & Non-Goals |
| Lifecycle / gates | CS-AML Investigation Methodology |
| Objects / states / lineage | CS-AML Data Model Specification |
| Typologies / indicators | CS-AML Typology Catalogue |
| Security/privacy/audit/review controls | CS-AML Control Implementation Guide |
| System architecture / canonical vs derived / AI | CS-AML Technology Architecture |
| Feature IDs / prioritisation master list | CS-AML Product & Feature Specification |

# Annex A — MVP P0 Feature IDs

The Product & Feature Specification remains the authoritative detailed feature catalogue. The following list identifies the P0 baseline expected to be represented in MVP planning; final sprint sequencing is an engineering/product decision. The v0.1.1 P0 baseline is 55 features (88 total = 55 P0 + 26 P1 + 7 P2), including F-EVD-008 Claim and fact lifecycle (approved by product owner, 2026-10-08). *[v0.1.1 · A10]*

| **P0 Feature** | **P0 Feature** | **P0 Feature** |
|----------------|----------------|----------------|
| F-CASE-001     | F-CASE-002     | F-CASE-003     |
| F-CASE-004     | F-CASE-005     | F-EVD-001      |
| F-EVD-002      | F-EVD-003      | F-EVD-004      |
| F-EVD-005      | F-EVD-006      | F-DOC-001      |
| F-ENT-001      | F-ENT-002      | F-ENT-003      |
| F-ENT-004      | F-ENT-005      | F-REL-001      |
| F-REL-002      | F-REL-003      | F-AST-001      |
| F-TIM-001      | F-TIM-002      | F-VAL-001      |
| F-VAL-002      | F-VAL-003      | F-VAL-004      |
| F-TYP-001      | F-TYP-002      | F-TYP-003      |
| F-HYP-001      | F-HYP-002      | F-HYP-003      |
| F-ASM-001      | F-ASM-002      | F-ASM-003      |
| F-SCH-001      | F-SCH-002      | F-GRF-001      |
| F-PRD-001      | F-REV-001      | F-PRD-002      |
| F-PRD-003      | F-DIS-001      | F-DIS-002      |
| F-DIS-003      | F-DIS-004      | F-ADM-001      |
| F-ADM-003      | F-SEC-001      | F-SEC-002      |
| F-SEC-003      | F-AUD-001      | F-OPS-001      |
| F-EVD-008 *[v0.1.1 · A10]* | | |

# Annex B — Representative End-to-End Pilot Scenario

A pilot case should use synthetic or legally cleared data and include: one public procurement contract, two organisations with partially overlapping identifiers, one person with an alias, one asset, one time-bounded ownership relationship, one reconstructed value-flow leg, one direct/documented leg, one typology with a counter-indicator, two competing hypotheses, one protected source reference, one peer-review challenge, and one controlled referral/export. The test succeeds only if a reviewer can reproduce the final assessment without relying on undocumented analyst memory.

**CS-AML Screen Inventory v0.1**

Canonical screen catalogue for MVP 0.1

| **Version** | 0.1                             |
|-------------|---------------------------------|
| **Status**  | Normative UI inventory baseline |
| **Scope**   | MVP 0.1                         |

**Design axiom.** Screens and wireframes SHALL preserve analytical uncertainty, provenance, reversibility, permission boundaries, and review context. Visual hierarchy must never convert inference into fact or status into accusation.

# 1. Purpose and Scope

This inventory defines the canonical set of user-facing screens required for CS-AML MVP 0.1. It bridges Information Architecture and UX into an implementation-oriented screen catalogue. Each screen receives a stable identifier used by design, frontend engineering, QA, product management and documentation.

> **Boundary —** The inventory defines what screens exist and why. Layout geometry and region-level structure belong to the separate CS-AML Wireframe Specification. Interaction semantics remain governed by the UX Specification; navigation/object organisation remain governed by the Information Architecture Specification.

# 2. Screen ID Standard

| **Prefix** | **Domain**        |
|------------|-------------------|
| HOME       | Home / work queue |
| CASE       | Case & workflow   |
| SRC        | Sources           |
| EVD        | Evidence          |
| ENT        | Entities          |
| REL        | Relationships     |
| AST        | Assets            |
| TIM        | Timeline/events   |
| VAL        | Value flow        |
| TYP        | Typology          |
| HYP        | Hypothesis        |
| ASM        | Assessment        |
| GRF        | Graph             |
| SCH        | Search            |
| PRD        | Products          |
| REV        | Review            |
| DIS        | Dissemination     |
| ADM        | Administration    |
| AUD        | Audit             |
| SYS        | System states     |

# 3. Inventory Summary

| **Domain**     | **Screen Count** |
|----------------|------------------|
| Home           | 1                |
| Cases          | 7                |
| Evidence       | 7                |
| Entities       | 9                |
| Analysis       | 11               |
| Search         | 1                |
| Products       | 9                |
| Administration | 5                |
| System         | 3                |

Total canonical MVP screens: 53.

# 4. Canonical Screen Inventory

| **Screen ID** | **Screen** | **Domain** | **Primary Roles** | **Purpose** | **Priority** |
|----|----|----|----|----|----|
| SCR-HOME-001 | Home / Work Queue | Home | All authorised users | Surface assigned work, pending reviews, recent cases and alerts without ranking people by suspicion. | P0 |
| SCR-CASE-001 | Case Register | Cases | Investigator, Case Owner | List authorised cases with filters for status, owner, classification and lifecycle stage. | P0 |
| SCR-CASE-002 | Create Case | Cases | Investigator | Create a case with purpose, owner, classification and initial investigation question. | P0 |
| SCR-CASE-003 | Case Overview | Cases | Case team | Summarise case purpose, scope, owners, status, key objects, lifecycle gates and unresolved risks. | P0 |
| SCR-CASE-004 | Investigation Charter | Cases | Case Owner | Read/edit/version investigation question, scope, exclusions, period, risks and collection boundaries. | P0 |
| SCR-CASE-005 | Lifecycle Gates | Cases | Case Owner, Reviewer | Submit, review and approve/reject G0-G6 gates with conditions and independence rules. | P0 |
| SCR-CASE-006 | Case Work / Tasks | Cases | Case team | Track collection, verification, analysis and review tasks. | P0 |
| SCR-CASE-007 | Case Activity | Cases | Case team, Auditor | Chronological material actions for reconstructability. | P0 |
| SCR-SRC-001 | Source Register | Evidence | Investigator | Register sources with provenance, access method, reliability and legal/access notes. | P0 |
| SCR-SRC-002 | Source Detail | Evidence | Investigator, Reviewer | Inspect provenance, reliability, linked evidence, claims and cases. | P0 |
| SCR-EVD-001 | Evidence Library | Evidence | Case team | Browse evidence and derivatives by source, type, integrity and status. | P0 |
| SCR-EVD-002 | Upload Evidence | Evidence | Investigator, Custodian | Ingest original evidence with source linkage and immutable preservation. | P0 |
| SCR-EVD-003 | Evidence Detail / Reader | Evidence | Case team | Read original/derivative evidence with provenance, hash and linked analytical objects. | P0 |
| SCR-EVD-004 | Evidence Extract Builder | Evidence | Investigator | Create precise page/paragraph/region extracts linked to original context. | P0 |
| SCR-EVD-005 | Evidence Lineage | Evidence | Investigator, Reviewer | Show original-to-derivative lineage and transformation metadata. | P0 |
| SCR-ENT-001 | Entity Register | Entities | Analyst | Find canonical entities across authorised cases without duplicating case-specific copies. | P0 |
| SCR-ENT-002 | Create Entity | Entities | Analyst | Create canonical entity and provenance-bearing assertions. | P0 |
| SCR-ENT-003 | Entity Detail | Entities | Analyst | Inspect canonical identity, aliases, identifiers, relationships, assets, cases and evidence. | P0 |
| SCR-ENT-004 | Entity Match Queue | Entities | Analyst, Data Steward | Review possible duplicate entities and conflicting attributes. | P0 |
| SCR-ENT-005 | Entity Match Compare | Entities | Data Steward | Compare candidates side-by-side and merge, reject or defer. | P0 |
| SCR-ENT-006 | Merge History / Unmerge | Entities | Data Steward | Inspect merge rationale/history and reverse supported merges. | P0 |
| SCR-REL-001 | Relationship Editor | Entities | Analyst | Create typed relationship with evidence, temporal validity, confidence and status. | P0 |
| SCR-AST-001 | Asset Register | Entities | Analyst | Browse assets and attribution relationships. | P0 |
| SCR-AST-002 | Asset Detail | Entities | Analyst | Inspect asset identifiers, location, ownership/control/use and evidence. | P0 |
| SCR-TIM-001 | Timeline | Analysis | Analyst | Explore case chronology with date precision and evidence links. | P0 |
| SCR-TIM-002 | Event Editor | Analysis | Analyst | Create event with precision-aware dates, entities, assets and evidence. | P0 |
| SCR-VAL-001 | Value Flow Workspace | Analysis | Analyst | Explore direct, documented, reconstructed and hypothetical value flows. | P0 |
| SCR-VAL-002 | Value Flow Builder | Analysis | Analyst | Create single or multi-leg flow with per-leg evidence, class and confidence. | P0 |
| SCR-TYP-001 | Typology Catalogue | Analysis | Analyst | Browse versioned typologies, observables, false positives and indicators. | P0 |
| SCR-TYP-002 | Typology Match Worksheet | Analysis | Analyst | Compare case observations against a typology with counter-indicators and alternatives. | P0 |
| SCR-HYP-001 | Hypothesis Workspace | Analysis | Analyst | Maintain competing explanations with support, contradiction, assumptions and gaps. | P0 |
| SCR-HYP-002 | Hypothesis Detail / Matrix | Analysis | Analyst, Reviewer | Map evidence and indicators as supporting, contradicting, neutral or unknown. | P0 |
| SCR-ASM-001 | Assessment Draft | Analysis | Analyst | Write judgement, confidence, basis, alternatives, assumptions and gaps. | P0 |
| SCR-ASM-002 | Assessment Detail | Analysis | Analyst, Reviewer | Read versioned assessment and trace backwards to evidence. | P0 |
| SCR-GRF-001 | Investigation Graph | Analysis | Analyst | Explore evidence-backed entity, relationship, asset and value-flow graph. | P0 |
| SCR-SCH-001 | Global Search | Search | All authorised users | Search authorised canonical objects with permission-aware counts and facets. | P0 |
| SCR-PRD-001 | Product Library | Products | Analyst, Reviewer | Browse intelligence products by case, status, classification and version. | P0 |
| SCR-PRD-002 | Create Intelligence Product | Products | Analyst | Create Financial Intelligence Note, Referral Package or Case Report from approved analytical objects. | P0 |
| SCR-PRD-003 | Product Editor | Products | Analyst | Edit structured product content while maintaining fact/analysis/gap distinctions and evidence index. | P0 |
| SCR-PRD-004 | Product Detail / Version History | Products | Analyst, Reviewer | Read current/superseded versions and approval state. | P0 |
| SCR-REV-001 | Review Queue | Products | Reviewer | List pending independent reviews and gating requirements. | P0 |
| SCR-REV-002 | Peer Review Workspace | Products | Reviewer | Comment, request changes, approve or reject with disconfirmation checks. | P0 |
| SCR-DIS-001 | Dissemination Approval | Products | Case Owner, Reviewer | Approve intended recipient, purpose, classification and export scope. | P0 |
| SCR-DIS-002 | Export Package Builder | Products | Analyst | Select minimised approved content and generate export manifest/package. | P0 |
| SCR-DIS-003 | Sharing Log | Products | Case Owner, Auditor | Record who received which version, when, why and with what restrictions. | P0 |
| SCR-ADM-001 | Administration Home | Administration | Admin | Entry point to vocabularies, retention, users/roles, policy and system information. | P0 |
| SCR-ADM-002 | Vocabulary Management | Administration | Admin | Manage controlled vocabulary versions without rewriting history. | P0 |
| SCR-ADM-003 | Retention Policies | Administration | Admin, Privacy | Define retention, hold and disposition rules by classification/object type. | P0 |
| SCR-ADM-004 | Access / Case Membership | Administration | Admin, Case Owner | Manage roles and case membership without exposing protected-source identity. | P0 |
| SCR-AUD-001 | Audit Explorer | Administration | Auditor | Search material audit events with permission-aware payloads. | P0 |
| SCR-SYS-001 | Access Denied / Need-to-Know | System | All users | Explain denied access without revealing restricted object existence/content. | P0 |
| SCR-SYS-002 | Integrity Warning | System | All users | Present hash mismatch or evidence-integrity problem with safe next steps. | P0 |
| SCR-SYS-003 | Conflict / Stale Version | System | All users | Prevent silent overwrite when concurrent edits or superseded versions exist. | P0 |

# 5. Screen Details by Domain

## Home

### SCR-HOME-001 — Home / Work Queue

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | / |
| Primary roles | All authorised users |
| Purpose | Surface assigned work, pending reviews, recent cases and alerts without ranking people by suspicion. |
| Primary objects | Case, Task, Review, AuditEvent |
| Required states | default, empty, filtered, degraded |
| Priority | P0 |

## Cases

### SCR-CASE-001 — Case Register

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases |
| Primary roles | Investigator, Case Owner |
| Purpose | List authorised cases with filters for status, owner, classification and lifecycle stage. |
| Primary objects | Case |
| Required states | default, empty, no-access, filtered |
| Priority | P0 |

### SCR-CASE-002 — Create Case

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/new |
| Primary roles | Investigator |
| Purpose | Create a case with purpose, owner, classification and initial investigation question. |
| Primary objects | Case, InvestigationQuestion |
| Required states | draft, validation-error, success |
| Priority | P0 |

### SCR-CASE-003 — Case Overview

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id} |
| Primary roles | Case team |
| Purpose | Summarise case purpose, scope, owners, status, key objects, lifecycle gates and unresolved risks. |
| Primary objects | Case, Review, Task, Assessment |
| Required states | default, restricted, stale-data |
| Priority | P0 |

### SCR-CASE-004 — Investigation Charter

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/charter |
| Primary roles | Case Owner |
| Purpose | Read/edit/version investigation question, scope, exclusions, period, risks and collection boundaries. |
| Primary objects | Case, InvestigationQuestion |
| Required states | view, edit, version-history, validation-error |
| Priority | P0 |

### SCR-CASE-005 — Lifecycle Gates

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/gates |
| Primary roles | Case Owner, Reviewer |
| Purpose | Submit, review and approve/reject G0-G6 gates with conditions and independence rules. |
| Primary objects | Review, Case |
| Required states | pending, approved, rejected, blocked |
| Priority | P0 |

### SCR-CASE-006 — Case Work / Tasks

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/work |
| Primary roles | Case team |
| Purpose | Track collection, verification, analysis and review tasks. |
| Primary objects | Task, Case |
| Required states | board, list, empty, overdue |
| Priority | P0 |

### SCR-CASE-007 — Case Activity

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/activity |
| Primary roles | Case team, Auditor |
| Purpose | Chronological material actions for reconstructability. |
| Primary objects | AuditEvent |
| Required states | default, filtered, restricted |
| Priority | P0 |

## Evidence

### SCR-SRC-001 — Source Register

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/sources |
| Primary roles | Investigator |
| Purpose | Register sources with provenance, access method, reliability and legal/access notes. |
| Primary objects | Source |
| Required states | list, empty, validation-error |
| Priority | P0 |

### SCR-SRC-002 — Source Detail

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /sources/{source_id} |
| Primary roles | Investigator, Reviewer |
| Purpose | Inspect provenance, reliability, linked evidence, claims and cases. |
| Primary objects | Source, EvidenceItem, Claim |
| Required states | default, restricted, superseded |
| Priority | P0 |

### SCR-EVD-001 — Evidence Library

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/evidence |
| Primary roles | Case team |
| Purpose | Browse evidence and derivatives by source, type, integrity and status. |
| Primary objects | EvidenceItem |
| Required states | grid/list, empty, upload-in-progress, restricted |
| Priority | P0 |

### SCR-EVD-002 — Upload Evidence

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/evidence/new |
| Primary roles | Investigator, Custodian |
| Purpose | Ingest original evidence with source linkage and immutable preservation. |
| Primary objects | EvidenceItem, Source |
| Required states | idle, uploading, scanning, failed, complete |
| Priority | P0 |

### SCR-EVD-003 — Evidence Detail / Reader

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /evidence/{evidence_id} |
| Primary roles | Case team |
| Purpose | Read original/derivative evidence with provenance, hash and linked analytical objects. |
| Primary objects | EvidenceItem, EvidenceExtract |
| Required states | default, restricted, integrity-warning |
| Priority | P0 |

### SCR-EVD-004 — Evidence Extract Builder

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /evidence/{evidence_id}/extracts/new |
| Primary roles | Investigator |
| Purpose | Create precise page/paragraph/region extracts linked to original context. |
| Primary objects | EvidenceExtract |
| Required states | selecting, editing, validation-error, saved |
| Priority | P0 |

### SCR-EVD-005 — Evidence Lineage

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /evidence/{evidence_id}/lineage |
| Primary roles | Investigator, Reviewer |
| Purpose | Show original-to-derivative lineage and transformation metadata. |
| Primary objects | EvidenceItem, DerivedArtifact |
| Required states | default, missing-parent-warning |
| Priority | P0 |

## Entities

### SCR-ENT-001 — Entity Register

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities |
| Primary roles | Analyst |
| Purpose | Find canonical entities across authorised cases without duplicating case-specific copies. |
| Primary objects | Entity |
| Required states | default, filtered, empty |
| Priority | P0 |

### SCR-ENT-002 — Create Entity

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities/new |
| Primary roles | Analyst |
| Purpose | Create canonical entity and provenance-bearing assertions. |
| Primary objects | Entity, Identifier |
| Required states | draft, duplicate-candidate, validation-error |
| Priority | P0 |

### SCR-ENT-003 — Entity Detail

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities/{entity_id} |
| Primary roles | Analyst |
| Purpose | Inspect canonical identity, aliases, identifiers, relationships, assets, cases and evidence. |
| Primary objects | Entity, Relationship, Asset |
| Required states | default, disputed, restricted |
| Priority | P0 |

### SCR-ENT-004 — Entity Match Queue

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities/matches |
| Primary roles | Analyst, Data Steward |
| Purpose | Review possible duplicate entities and conflicting attributes. |
| Primary objects | EntityMatchCandidate |
| Required states | queue, empty, filtered |
| Priority | P0 |

### SCR-ENT-005 — Entity Match Compare

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities/matches/{match_id} |
| Primary roles | Data Steward |
| Purpose | Compare candidates side-by-side and merge, reject or defer. |
| Primary objects | Entity, EntityMatchCandidate |
| Required states | candidate, merge-confirmation, rejected, deferred |
| Priority | P0 |

### SCR-ENT-006 — Merge History / Unmerge

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /entities/{entity_id}/resolution |
| Primary roles | Data Steward |
| Purpose | Inspect merge rationale/history and reverse supported merges. |
| Primary objects | MergeDecision, Entity |
| Required states | default, confirmation, conflict |
| Priority | P0 |

### SCR-REL-001 — Relationship Editor

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /relationships/new |
| Primary roles | Analyst |
| Purpose | Create typed relationship with evidence, temporal validity, confidence and status. |
| Primary objects | Relationship |
| Required states | draft, validation-error, saved |
| Priority | P0 |

### SCR-AST-001 — Asset Register

| **Attribute**             | **Definition**                               |
|---------------------------|----------------------------------------------|
| Canonical route / context | /assets                                      |
| Primary roles             | Analyst                                      |
| Purpose                   | Browse assets and attribution relationships. |
| Primary objects           | Asset, ControlAssertion                      |
| Required states           | default, filtered, empty                     |
| Priority                  | P0                                           |

### SCR-AST-002 — Asset Detail

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /assets/{asset_id} |
| Primary roles | Analyst |
| Purpose | Inspect asset identifiers, location, ownership/control/use and evidence. |
| Primary objects | Asset, Relationship |
| Required states | default, disputed, restricted |
| Priority | P0 |

## Analysis

### SCR-TIM-001 — Timeline

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/timeline |
| Primary roles | Analyst |
| Purpose | Explore case chronology with date precision and evidence links. |
| Primary objects | Event |
| Required states | default, filtered, empty |
| Priority | P0 |

### SCR-TIM-002 — Event Editor

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /events/new |
| Primary roles | Analyst |
| Purpose | Create event with precision-aware dates, entities, assets and evidence. |
| Primary objects | Event |
| Required states | draft, validation-error, saved |
| Priority | P0 |

### SCR-VAL-001 — Value Flow Workspace

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/value-flows |
| Primary roles | Analyst |
| Purpose | Explore direct, documented, reconstructed and hypothetical value flows. |
| Primary objects | ValueFlow, ValueFlowLeg |
| Required states | default, filtered, empty |
| Priority | P0 |

### SCR-VAL-002 — Value Flow Builder

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/value-flows/new |
| Primary roles | Analyst |
| Purpose | Create single or multi-leg flow with per-leg evidence, class and confidence. |
| Primary objects | ValueFlow, ValueFlowLeg |
| Required states | draft, incomplete, validation-error, saved |
| Priority | P0 |

### SCR-TYP-001 — Typology Catalogue

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /analysis/typologies |
| Primary roles | Analyst |
| Purpose | Browse versioned typologies, observables, false positives and indicators. |
| Primary objects | Typology |
| Required states | default, search, empty |
| Priority | P0 |

### SCR-TYP-002 — Typology Match Worksheet

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/typology-matches/{id} |
| Primary roles | Analyst |
| Purpose | Compare case observations against a typology with counter-indicators and alternatives. |
| Primary objects | TypologyMatch, Indicator |
| Required states | draft, weak, plausible, strong, compelling |
| Priority | P0 |

### SCR-HYP-001 — Hypothesis Workspace

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/hypotheses |
| Primary roles | Analyst |
| Purpose | Maintain competing explanations with support, contradiction, assumptions and gaps. |
| Primary objects | Hypothesis, IntelligenceGap |
| Required states | default, empty, filtered |
| Priority | P0 |

### SCR-HYP-002 — Hypothesis Detail / Matrix

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /hypotheses/{hypothesis_id} |
| Primary roles | Analyst, Reviewer |
| Purpose | Map evidence and indicators as supporting, contradicting, neutral or unknown. |
| Primary objects | Hypothesis, EvidenceItem, Indicator |
| Required states | open, supported, weakened, rejected, inconclusive |
| Priority | P0 |

### SCR-ASM-001 — Assessment Draft

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/assessments/new |
| Primary roles | Analyst |
| Purpose | Write judgement, confidence, basis, alternatives, assumptions and gaps. |
| Primary objects | Assessment |
| Required states | draft, validation-error, ready-for-review |
| Priority | P0 |

### SCR-ASM-002 — Assessment Detail

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /assessments/{assessment_id} |
| Primary roles | Analyst, Reviewer |
| Purpose | Read versioned assessment and trace backwards to evidence. |
| Primary objects | Assessment, Hypothesis, EvidenceItem |
| Required states | draft, reviewed, superseded |
| Priority | P0 |

### SCR-GRF-001 — Investigation Graph

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/graph |
| Primary roles | Analyst |
| Purpose | Explore evidence-backed entity, relationship, asset and value-flow graph. |
| Primary objects | Entity, Relationship, Asset, ValueFlow |
| Required states | default, loading, filtered, no-results |
| Priority | P0 |

## Search

### SCR-SCH-001 — Global Search

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /search |
| Primary roles | All authorised users |
| Purpose | Search authorised canonical objects with permission-aware counts and facets. |
| Primary objects | Case, Entity, EvidenceItem, Source, Asset |
| Required states | default, results, no-results, restricted |
| Priority | P0 |

## Products

### SCR-PRD-001 — Product Library

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products |
| Primary roles | Analyst, Reviewer |
| Purpose | Browse intelligence products by case, status, classification and version. |
| Primary objects | IntelligenceProduct |
| Required states | default, filtered, empty |
| Priority | P0 |

### SCR-PRD-002 — Create Intelligence Product

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /cases/{case_id}/products/new |
| Primary roles | Analyst |
| Purpose | Create Financial Intelligence Note, Referral Package or Case Report from approved analytical objects. |
| Primary objects | IntelligenceProduct |
| Required states | template-select, draft, validation-error |
| Priority | P0 |

### SCR-PRD-003 — Product Editor

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products/{product_id}/edit |
| Primary roles | Analyst |
| Purpose | Edit structured product content while maintaining fact/analysis/gap distinctions and evidence index. |
| Primary objects | IntelligenceProduct, Assessment |
| Required states | draft, autosave, conflict, validation-error |
| Priority | P0 |

### SCR-PRD-004 — Product Detail / Version History

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products/{product_id} |
| Primary roles | Analyst, Reviewer |
| Purpose | Read current/superseded versions and approval state. |
| Primary objects | IntelligenceProduct |
| Required states | draft, review, approved, superseded, retracted |
| Priority | P0 |

### SCR-REV-001 — Review Queue

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /reviews |
| Primary roles | Reviewer |
| Purpose | List pending independent reviews and gating requirements. |
| Primary objects | Review, IntelligenceProduct |
| Required states | queue, empty, overdue |
| Priority | P0 |

### SCR-REV-002 — Peer Review Workspace

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /reviews/{review_id} |
| Primary roles | Reviewer |
| Purpose | Comment, request changes, approve or reject with disconfirmation checks. |
| Primary objects | Review, IntelligenceProduct, Assessment |
| Required states | in-review, changes-requested, approved, rejected |
| Priority | P0 |

### SCR-DIS-001 — Dissemination Approval

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products/{product_id}/dissemination |
| Primary roles | Case Owner, Reviewer |
| Purpose | Approve intended recipient, purpose, classification and export scope. |
| Primary objects | Dissemination |
| Required states | draft, blocked, approved |
| Priority | P0 |

### SCR-DIS-002 — Export Package Builder

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products/{product_id}/export |
| Primary roles | Analyst |
| Purpose | Select minimised approved content and generate export manifest/package. |
| Primary objects | Dissemination, IntelligenceProduct |
| Required states | selecting, warning, generating, complete |
| Priority | P0 |

### SCR-DIS-003 — Sharing Log

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /products/{product_id}/sharing |
| Primary roles | Case Owner, Auditor |
| Purpose | Record who received which version, when, why and with what restrictions. |
| Primary objects | Dissemination |
| Required states | default, empty, immutable-entry |
| Priority | P0 |

## Administration

### SCR-ADM-001 — Administration Home

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /admin |
| Primary roles | Admin |
| Purpose | Entry point to vocabularies, retention, users/roles, policy and system information. |
| Primary objects | Vocabulary, RetentionPolicy, AccessPolicy |
| Required states | default, restricted |
| Priority | P0 |

### SCR-ADM-002 — Vocabulary Management

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /admin/vocabularies |
| Primary roles | Admin |
| Purpose | Manage controlled vocabulary versions without rewriting history. |
| Primary objects | Vocabulary |
| Required states | list, edit, retire, validation-error |
| Priority | P0 |

### SCR-ADM-003 — Retention Policies

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /admin/retention |
| Primary roles | Admin, Privacy |
| Purpose | Define retention, hold and disposition rules by classification/object type. |
| Primary objects | RetentionPolicy |
| Required states | list, preview, hold, disposition |
| Priority | P0 |

### SCR-ADM-004 — Access / Case Membership

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /admin/access |
| Primary roles | Admin, Case Owner |
| Purpose | Manage roles and case membership without exposing protected-source identity. |
| Primary objects | AccessPolicy, User, Case |
| Required states | list, edit, denied |
| Priority | P0 |

### SCR-AUD-001 — Audit Explorer

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | /admin/audit |
| Primary roles | Auditor |
| Purpose | Search material audit events with permission-aware payloads. |
| Primary objects | AuditEvent |
| Required states | default, filtered, empty |
| Priority | P0 |

## System

### SCR-SYS-001 — Access Denied / Need-to-Know

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | n/a |
| Primary roles | All users |
| Purpose | Explain denied access without revealing restricted object existence/content. |
| Primary objects | AccessPolicy |
| Required states | denied |
| Priority | P0 |

### SCR-SYS-002 — Integrity Warning

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | n/a |
| Primary roles | All users |
| Purpose | Present hash mismatch or evidence-integrity problem with safe next steps. |
| Primary objects | EvidenceItem, AuditEvent |
| Required states | warning |
| Priority | P0 |

### SCR-SYS-003 — Conflict / Stale Version

| **Attribute** | **Definition** |
|----|----|
| Canonical route / context | n/a |
| Primary roles | All users |
| Purpose | Prevent silent overwrite when concurrent edits or superseded versions exist. |
| Primary objects | Versioned objects |
| Required states | conflict |
| Priority | P0 |

# 6. Shared Screen-State Requirements

- Every data-bearing screen SHALL define loading, empty, partial/degraded, error and permission-denied states where applicable.

- Unknown and unavailable data SHALL NOT be rendered as zero, false or absent unless semantics explicitly require that value.

- Restricted content SHALL NOT leak through breadcrumbs, counts, search facets, graph labels or error text.

- Superseded, disputed, reconstructed, hypothetical and machine-generated states SHALL remain visible in screen-level information scent.

- Destructive or high-impact actions SHALL expose consequence, scope and reversibility before commitment.

# 7. Screen Inventory Definition of Done

- Each implemented screen maps to one canonical screen ID.

- Primary route/context and role access are known.

- Required objects and states are defined.

- UX and IA requirements have no unresolved conflict.

- Wireframe reference exists for P0 screens before implementation is considered design-ready.

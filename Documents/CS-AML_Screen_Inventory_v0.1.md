# CS-AML Screen Inventory v0.1

**Status:** Normative UI inventory baseline for MVP 0.1

## Inventory axiom
Every implemented MVP screen SHALL have one stable screen ID and a defined purpose, role, object context, state set and priority.

## Total canonical MVP screens
**53**

## Screen catalogue

- **SCR-HOME-001 — Home / Work Queue** (Home, P0) — Surface assigned work, pending reviews, recent cases and alerts without ranking people by suspicion.
- **SCR-CASE-001 — Case Register** (Cases, P0) — List authorised cases with filters for status, owner, classification and lifecycle stage.
- **SCR-CASE-002 — Create Case** (Cases, P0) — Create a case with purpose, owner, classification and initial investigation question.
- **SCR-CASE-003 — Case Overview** (Cases, P0) — Summarise case purpose, scope, owners, status, key objects, lifecycle gates and unresolved risks.
- **SCR-CASE-004 — Investigation Charter** (Cases, P0) — Read/edit/version investigation question, scope, exclusions, period, risks and collection boundaries.
- **SCR-CASE-005 — Lifecycle Gates** (Cases, P0) — Submit, review and approve/reject G0-G6 gates with conditions and independence rules.
- **SCR-CASE-006 — Case Work / Tasks** (Cases, P0) — Track collection, verification, analysis and review tasks.
- **SCR-CASE-007 — Case Activity** (Cases, P0) — Chronological material actions for reconstructability.
- **SCR-SRC-001 — Source Register** (Evidence, P0) — Register sources with provenance, access method, reliability and legal/access notes.
- **SCR-SRC-002 — Source Detail** (Evidence, P0) — Inspect provenance, reliability, linked evidence, claims and cases.
- **SCR-EVD-001 — Evidence Library** (Evidence, P0) — Browse evidence and derivatives by source, type, integrity and status.
- **SCR-EVD-002 — Upload Evidence** (Evidence, P0) — Ingest original evidence with source linkage and immutable preservation.
- **SCR-EVD-003 — Evidence Detail / Reader** (Evidence, P0) — Read original/derivative evidence with provenance, hash and linked analytical objects.
- **SCR-EVD-004 — Evidence Extract Builder** (Evidence, P0) — Create precise page/paragraph/region extracts linked to original context.
- **SCR-EVD-005 — Evidence Lineage** (Evidence, P0) — Show original-to-derivative lineage and transformation metadata.
- **SCR-ENT-001 — Entity Register** (Entities, P0) — Find canonical entities across authorised cases without duplicating case-specific copies.
- **SCR-ENT-002 — Create Entity** (Entities, P0) — Create canonical entity and provenance-bearing assertions.
- **SCR-ENT-003 — Entity Detail** (Entities, P0) — Inspect canonical identity, aliases, identifiers, relationships, assets, cases and evidence.
- **SCR-ENT-004 — Entity Match Queue** (Entities, P0) — Review possible duplicate entities and conflicting attributes.
- **SCR-ENT-005 — Entity Match Compare** (Entities, P0) — Compare candidates side-by-side and merge, reject or defer.
- **SCR-ENT-006 — Merge History / Unmerge** (Entities, P0) — Inspect merge rationale/history and reverse supported merges.
- **SCR-REL-001 — Relationship Editor** (Entities, P0) — Create typed relationship with evidence, temporal validity, confidence and status.
- **SCR-AST-001 — Asset Register** (Entities, P0) — Browse assets and attribution relationships.
- **SCR-AST-002 — Asset Detail** (Entities, P0) — Inspect asset identifiers, location, ownership/control/use and evidence.
- **SCR-TIM-001 — Timeline** (Analysis, P0) — Explore case chronology with date precision and evidence links.
- **SCR-TIM-002 — Event Editor** (Analysis, P0) — Create event with precision-aware dates, entities, assets and evidence.
- **SCR-VAL-001 — Value Flow Workspace** (Analysis, P0) — Explore direct, documented, reconstructed and hypothetical value flows.
- **SCR-VAL-002 — Value Flow Builder** (Analysis, P0) — Create single or multi-leg flow with per-leg evidence, class and confidence.
- **SCR-TYP-001 — Typology Catalogue** (Analysis, P0) — Browse versioned typologies, observables, false positives and indicators.
- **SCR-TYP-002 — Typology Match Worksheet** (Analysis, P0) — Compare case observations against a typology with counter-indicators and alternatives.
- **SCR-HYP-001 — Hypothesis Workspace** (Analysis, P0) — Maintain competing explanations with support, contradiction, assumptions and gaps.
- **SCR-HYP-002 — Hypothesis Detail / Matrix** (Analysis, P0) — Map evidence and indicators as supporting, contradicting, neutral or unknown.
- **SCR-ASM-001 — Assessment Draft** (Analysis, P0) — Write judgement, confidence, basis, alternatives, assumptions and gaps.
- **SCR-ASM-002 — Assessment Detail** (Analysis, P0) — Read versioned assessment and trace backwards to evidence.
- **SCR-GRF-001 — Investigation Graph** (Analysis, P0) — Explore evidence-backed entity, relationship, asset and value-flow graph.
- **SCR-SCH-001 — Global Search** (Search, P0) — Search authorised canonical objects with permission-aware counts and facets.
- **SCR-PRD-001 — Product Library** (Products, P0) — Browse intelligence products by case, status, classification and version.
- **SCR-PRD-002 — Create Intelligence Product** (Products, P0) — Create Financial Intelligence Note, Referral Package or Case Report from approved analytical objects.
- **SCR-PRD-003 — Product Editor** (Products, P0) — Edit structured product content while maintaining fact/analysis/gap distinctions and evidence index.
- **SCR-PRD-004 — Product Detail / Version History** (Products, P0) — Read current/superseded versions and approval state.
- **SCR-REV-001 — Review Queue** (Products, P0) — List pending independent reviews and gating requirements.
- **SCR-REV-002 — Peer Review Workspace** (Products, P0) — Comment, request changes, approve or reject with disconfirmation checks.
- **SCR-DIS-001 — Dissemination Approval** (Products, P0) — Approve intended recipient, purpose, classification and export scope.
- **SCR-DIS-002 — Export Package Builder** (Products, P0) — Select minimised approved content and generate export manifest/package.
- **SCR-DIS-003 — Sharing Log** (Products, P0) — Record who received which version, when, why and with what restrictions.
- **SCR-ADM-001 — Administration Home** (Administration, P0) — Entry point to vocabularies, retention, users/roles, policy and system information.
- **SCR-ADM-002 — Vocabulary Management** (Administration, P0) — Manage controlled vocabulary versions without rewriting history.
- **SCR-ADM-003 — Retention Policies** (Administration, P0) — Define retention, hold and disposition rules by classification/object type.
- **SCR-ADM-004 — Access / Case Membership** (Administration, P0) — Manage roles and case membership without exposing protected-source identity.
- **SCR-AUD-001 — Audit Explorer** (Administration, P0) — Search material audit events with permission-aware payloads.
- **SCR-SYS-001 — Access Denied / Need-to-Know** (System, P0) — Explain denied access without revealing restricted object existence/content.
- **SCR-SYS-002 — Integrity Warning** (System, P0) — Present hash mismatch or evidence-integrity problem with safe next steps.
- **SCR-SYS-003 — Conflict / Stale Version** (System, P0) — Prevent silent overwrite when concurrent edits or superseded versions exist.
**CS-AML Wireframe Specification v0.1.1**

Structural wireframe contract for MVP 0.1

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML Wireframe Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

| **Version** | 0.1.1 |
|-------------|------------------------------|
| **Status**  | Draft for Review (Proposed Internal Baseline) — proposed normative wireframe baseline *[v0.1.1 · A01]* |
| **Scope**   | MVP 0.1                      |

**Design axiom.** Screens and wireframes SHALL preserve analytical uncertainty, provenance, reversibility, permission boundaries, and review context. Visual hierarchy must never convert inference into fact or status into accusation.

# 1. Purpose and Boundary

This specification defines the structural wireframe contract for CS-AML MVP screens. It translates each Screen Inventory ID into layout regions, component zones, hierarchy, contextual panels, state placement and responsive rules. It is intentionally low-fidelity: it does not prescribe brand styling, final visual design tokens, iconography or production copy.

> **Ownership split —** Information Architecture owns organisation and findability. UX owns behaviour and interaction semantics. This Wireframe Specification owns spatial composition and screen-region contracts. Final visual styling belongs to the future UI Design System.

# 2. Global Application Frame

Desktop baseline uses a stable application frame. The exact pixel values MAY vary in implementation, but the information zones SHALL remain recognisable.

| **Region** | **Purpose** | **Rules** |
|----|----|----|
| A. Global header | Identity, global search trigger, current user/session, environment marker | Never display sensitive case content in persistent chrome unless user is authorised. |
| B. Primary navigation | Home, Cases, Entities, Evidence, Analysis, Products, Search, Administration | Labels come from IA. Restricted destinations are omitted or disabled according to policy. |
| C. Context header | Current case/object title, classification, status, breadcrumbs/context | Must distinguish canonical object from case-context view. |
| D. Local navigation | Tabs or section navigation within current case/object | Must preserve deep-linkability and current context. |
| E. Main canvas | Primary task content | One dominant task per screen; avoid dashboard clutter. |
| F. Context / evidence rail | Provenance, evidence, metadata, linked objects, warnings | Optional/collapsible; never the only place critical uncertainty is shown. |
| G. Action zone | Primary/secondary actions and high-impact confirmations | High-impact actions separated from routine edit actions. |

# 3. Responsive Baseline

- Desktop \>= 1280px: two- or three-region analytical workspace permitted.

- Tablet 768-1279px: context rail collapses to drawer; local navigation may become horizontal overflow or compact menu.

- Mobile \< 768px: read/review and simple capture MAY be supported; dense graph, entity matching and value-flow building are not required to be full-featured for MVP.

- No critical classification, uncertainty or permission state may disappear solely because viewport is narrower.

# 4. Wireframe Pattern Library

| **Pattern ID** | **Pattern** | **Structural contract** |
|----|----|----|
| WF-PAT-01 | Register/List | Header + filters + sortable result list/table + empty state + primary create action. |
| WF-PAT-02 | Canonical Object Detail | Context header + summary block + local tabs + main object facts + provenance rail + backlinks. |
| WF-PAT-03 | Editor/Form | Context header + sectioned form + inline validation + evidence/provenance selector + sticky save/cancel zone. |
| WF-PAT-04 | Workspace | Context header + local tools + primary analytical canvas + side inspector + optional bottom activity/history panel. |
| WF-PAT-05 | Compare/Resolution | Side-by-side candidate columns + match/conflict summary + evidence panel + decision zone. |
| WF-PAT-06 | Review/Approval | Read-only reviewed artefact + review checklist/comments + decision panel + independent-approval status. |
| WF-PAT-07 | System State | Minimal content with explanation, safe next step and non-disclosing error semantics. |

# 5. Screen-to-Wireframe Mapping

| **Screen ID** | **Screen** | **Wireframe Pattern** | **Critical States** |
|----|----|----|----|
| SCR-HOME-001 | Home / Work Queue | WF-PAT-01 | default, empty, filtered, degraded |
| SCR-CASE-001 | Case Register | WF-PAT-01 | default, empty, no-access, filtered *[v0.1.1 · A15]* |
| SCR-CASE-002 | Create Case | WF-PAT-03 | draft, validation-error, success |
| SCR-CASE-003 | Case Overview | WF-PAT-02 | default, restricted, stale-data |
| SCR-CASE-004 | Investigation Charter | WF-PAT-03 | view, edit, version-history, validation-error |
| SCR-CASE-005 | Lifecycle Gates | WF-PAT-06 | pending, approved, rejected, blocked |
| SCR-CASE-006 | Case Work / Tasks | WF-PAT-01 | board, list, empty, overdue |
| SCR-CASE-007 | Case Activity | WF-PAT-01 | default, filtered, restricted |
| SCR-SRC-001 | Source Register | WF-PAT-01 | list, empty, validation-error |
| SCR-SRC-002 | Source Detail | WF-PAT-02 | default, restricted, superseded |
| SCR-EVD-001 | Evidence Library | WF-PAT-01 | grid/list, empty, upload-in-progress, restricted |
| SCR-EVD-002 | Upload Evidence | WF-PAT-03 | idle, uploading, scanning, failed, complete |
| SCR-EVD-003 | Evidence Detail / Reader | WF-PAT-02 | default, restricted, integrity-warning |
| SCR-EVD-004 | Evidence Extract Builder | WF-PAT-03 | selecting, editing, validation-error, saved |
| SCR-EVD-005 | Evidence Lineage | WF-PAT-02 | default, missing-parent-warning |
| SCR-ENT-001 | Entity Register | WF-PAT-01 | default, filtered, empty |
| SCR-ENT-002 | Create Entity | WF-PAT-03 | draft, duplicate-candidate, validation-error |
| SCR-ENT-003 | Entity Detail | WF-PAT-02 | default, disputed, restricted |
| SCR-ENT-004 | Entity Match Queue | WF-PAT-01 | queue, empty, filtered |
| SCR-ENT-005 | Entity Match Compare | WF-PAT-05 | candidate, merge-confirmation, rejected, deferred |
| SCR-ENT-006 | Merge History / Unmerge | WF-PAT-05 | default, confirmation, conflict |
| SCR-REL-001 | Relationship Editor | WF-PAT-03 | draft, validation-error, saved |
| SCR-AST-001 | Asset Register | WF-PAT-01 | default, filtered, empty |
| SCR-AST-002 | Asset Detail | WF-PAT-02 | default, disputed, restricted |
| SCR-TIM-001 | Timeline | WF-PAT-04 | default, filtered, empty |
| SCR-TIM-002 | Event Editor | WF-PAT-03 | draft, validation-error, saved |
| SCR-VAL-001 | Value Flow Workspace | WF-PAT-04 | default, filtered, empty |
| SCR-VAL-002 | Value Flow Builder | WF-PAT-04 | draft, incomplete, validation-error, saved |
| SCR-TYP-001 | Typology Catalogue | WF-PAT-01 | default, search, empty |
| SCR-TYP-002 | Typology Match Worksheet | WF-PAT-04 | draft, weak, plausible, strong, compelling |
| SCR-HYP-001 | Hypothesis Workspace | WF-PAT-04 | default, empty, filtered |
| SCR-HYP-002 | Hypothesis Detail / Matrix | WF-PAT-04 | open, supported, weakened, rejected, inconclusive |
| SCR-ASM-001 | Assessment Draft | WF-PAT-03 | draft, validation-error, ready-for-review |
| SCR-ASM-002 | Assessment Detail | WF-PAT-02 | draft, reviewed, superseded |
| SCR-GRF-001 | Investigation Graph | WF-PAT-04 | default, loading, filtered, no-results |
| SCR-SCH-001 | Global Search | WF-PAT-01 | default, results, no-results, restricted |
| SCR-PRD-001 | Product Library | WF-PAT-01 | default, filtered, empty |
| SCR-PRD-002 | Create Intelligence Product | WF-PAT-03 | template-select, draft, validation-error |
| SCR-PRD-003 | Product Editor | WF-PAT-03 | draft, autosave, conflict, validation-error |
| SCR-PRD-004 | Product Detail / Version History | WF-PAT-02 | draft, review, approved, superseded, retracted |
| SCR-REV-001 | Review Queue | WF-PAT-01 | queue, empty, overdue |
| SCR-REV-002 | Peer Review Workspace | WF-PAT-06 | in-review, changes-requested, approved, rejected |
| SCR-DIS-001 | Dissemination Approval | WF-PAT-06 | draft, blocked, approved |
| SCR-DIS-002 | Export Package Builder | WF-PAT-04 | selecting, warning, generating, complete |
| SCR-DIS-003 | Sharing Log | WF-PAT-01 | default, empty, immutable-entry |
| SCR-ADM-001 | Administration Home | WF-PAT-01 | default, restricted |
| SCR-ADM-002 | Vocabulary Management | WF-PAT-01 | list, edit, retire, validation-error |
| SCR-ADM-003 | Retention Policies | WF-PAT-01 | list, preview, hold, disposition |
| SCR-ADM-004 | Access / Case Membership | WF-PAT-01 | list, edit, denied |
| SCR-AUD-001 | Audit Explorer | WF-PAT-01 | default, filtered, empty |
| SCR-SYS-001 | Access Denied / Need-to-Know | WF-PAT-07 | denied |
| SCR-SYS-002 | Integrity Warning | WF-PAT-07 | warning |
| SCR-SYS-003 | Conflict / Stale Version | WF-PAT-07 | conflict |

# 6. Detailed Wireframe Specifications

## SCR-HOME-001 — Home / Work Queue

| **Region** | **Wireframe requirement** |
|----|----|
| Top band | Work queue summary: assigned tasks, pending reviews, blocked gates; no suspicion ranking. |
| Main left | Recent authorised cases and next actions. |
| Main right | Pending review/approval cards and system notices. |
| Footer/secondary | Recent activity with permission-safe labels. |

## SCR-CASE-003 — Case Overview

| **Region** | **Wireframe requirement** |
|----|----|
| Context header | Case ID, title, classification, status, owner, lifecycle stage. |
| Local nav | Overview \| Work \| Sources & Evidence \| Entities & Assets \| Timeline \| Value Flows \| Analysis \| Products. |
| Main summary | Investigation question, purpose, scope, key risks and unresolved gates. |
| Secondary blocks | Key entities, evidence count, open tasks, intelligence gaps. |
| Context rail | Case metadata, membership, latest review, activity links. |

## SCR-EVD-003 — Evidence Detail / Reader

| **Region** | **Wireframe requirement** |
|----|----|
| Context header | Evidence ID, original/derivative badge, source, integrity status. |
| Main canvas | Document/image reader preserving original context. |
| Left/inline controls | Page navigation, search-within-document, extract creation. |
| Context rail | Provenance, hash, source rating, derivatives, linked facts/entities. |
| Warning zone | Integrity mismatch, restricted source identity, derivative warnings. |

## SCR-ENT-003 — Entity Detail

| **Region** | **Wireframe requirement** |
|----|----|
| Context header | Entity canonical name, type, resolution status, confidence/status without accusatory styling. |
| Summary | Identifiers, aliases, jurisdictions, provenance-bearing assertions. |
| Local nav | Overview \| Relationships \| Assets \| Events \| Cases \| Evidence \| Resolution. |
| Main | Selected tab content. |
| Context rail | Linked evidence, conflicts, merge history, backlinks. |

## SCR-ENT-005 — Entity Match Compare

| **Region** | **Wireframe requirement** |
|----|----|
| Left candidate | Entity A identity/identifiers/provenance. |
| Right candidate | Entity B identity/identifiers/provenance. |
| Center comparison | Matching attributes, conflicting attributes, missing/unknown fields. |
| Bottom evidence | Evidence citations supporting identity resolution. |
| Decision zone | Merge \| Reject match \| Defer; rationale required; merge is high-impact confirmation. Each action records a ResolutionDecision (`MERGE`, `KEEP_SEPARATE`, `DEFER`). *[v0.1.1 · ER]* |

## SCR-VAL-001 — Value Flow Workspace

| **Region** | **Wireframe requirement** |
|----|----|
| Context header | Case + flow scope + legend for DIRECT/DOCUMENTED/RECONSTRUCTED/HYPOTHETICAL. |
| Primary canvas | Flow diagram with line-style + labels, not color alone. |
| Toolbar | Filter by class/date/entity/mechanism; toggle amount labels. |
| Inspector | Selected flow/leg evidence, confidence, dates, unknown/range values. |
| Bottom panel | Flow list/table for accessible alternative and export consistency. |

## SCR-HYP-001 — Hypothesis Workspace

| **Region** | **Wireframe requirement** |
|----|----|
| Header | Case context and analytical stage. |
| Main columns/rows | Hypothesis cards including legitimate alternatives. |
| Evidence matrix | Support / contradict / neutral / unknown per hypothesis. |
| Gap panel | Material unknowns and collection questions. |
| Assessment readiness | Shows missing disconfirmation or unresolved gaps; never auto-ranks guilt. |

## SCR-GRF-001 — Investigation Graph

| **Region** | **Wireframe requirement** |
|----|----|
| Primary canvas | Permission-aware graph projection. |
| Toolbar | Filter node/edge types, time, case context; no opaque risk-score filter by default. |
| Inspector | Canonical object, relationship provenance, confidence/status, evidence. |
| Legend | Relationship types and uncertainty semantics. |
| Footer/list fallback | Accessible node/edge table and breadcrumb back to canonical objects. |

## SCR-PRD-003 — Product Editor

| **Region** | **Wireframe requirement** |
|----|----|
| Context header | Product type, case, version, classification, status. |
| Outline rail | Executive assessment, scope, facts, findings, flows, typology, alternatives, gaps, confidence, recommendations, evidence index. |
| Main editor | Structured section editor; facts and analysis have distinct content types. |
| Evidence rail | Citations and linked canonical objects. |
| Action zone | Save draft, submit review; no external export from editor before approval. |

## SCR-REV-002 — Peer Review Workspace

| **Region** | **Wireframe requirement** |
|----|----|
| Reviewed artefact | Frozen product/assessment version. |
| Review rail | Checklist: identity, evidence, alternatives, confidence, harm, disconfirmation. |
| Comments | Anchored comments/change requests. |
| Decision panel | Request changes \| Approve \| Reject, with independence check. |
| Evidence trace | Direct traversal to supporting objects without losing review context. |

## SCR-DIS-002 — Export Package Builder

| **Region** | **Wireframe requirement** |
|----|----|
| Scope summary | Recipient, purpose, classification, approved product version. |
| Selection panel | Objects/sections included; restricted content excluded by default. |
| Warnings | Protected source, sensitive personal data, superseded content, unresolved approval. |
| Preview | Manifest and redaction/minimisation preview. |
| Action zone | Generate package only after approval; immutable sharing/audit event afterward. |

# 7. Cross-Screen Structural Rules

- Classification, object status and uncertainty markers SHALL appear near the object title or proposition they qualify; they SHALL NOT be relegated only to metadata drawers.

- Provenance access SHALL be reachable from any material fact, relationship, flow, indicator, hypothesis or assessment without requiring global navigation away from the current task.

- Canonical object detail screens SHALL provide backlinks to authorised cases and related objects.

- Graph, timeline and value-flow views SHALL provide an accessible non-visual representation of equivalent information.

- Protected-source identity SHALL never occupy reusable generic components that could accidentally surface in search, breadcrumbs, exports or notifications.

- High-impact decisions SHALL use a visually separated decision zone with explicit scope and consequence.

# 8. Empty, Error, Permission and Conflict Wireframes

| **State** | **Structural requirement** |
|----|----|
| Empty | Explain what belongs here, why it matters and the safe next action. Avoid framing absence as analytical finding. |
| Permission denied | Do not reveal restricted title, identifier, count or owner if policy forbids object-existence disclosure. |
| Partial/degraded | Show which region is unavailable and which data remains trustworthy. |
| Integrity warning | Place warning adjacent to evidence identity and block unsafe downstream actions where required. |
| Stale/conflict | Show current version, user draft, conflict scope and recoverable resolution path. |
| Superseded | Keep historical version readable while clearly linking the current authoritative version. |

# 9. Wireframe Acceptance Criteria

- Every P0 Screen Inventory ID maps to exactly one primary wireframe pattern, and register/list screens map to WF-PAT-01 rather than a detail pattern. The mapping SHALL be cross-checked against the Screen Inventory, High-Fidelity UI Specification and component composition before implementation. *[v0.1.1 · A15]*

- Core analytical screens have explicit provenance and uncertainty regions.

- High-impact actions have distinct decision zones.

- Permission-denied, empty, error and conflict states are structurally specified.

- Desktop and narrow-screen behaviour preserve critical semantics.

- No wireframe implies guilt, suspicion score or evidentiary certainty merely through placement, size, color or prominence.

> These criteria are review targets for future design files; this specification is a structural contract, not a completed wireframe set or tested UI. *[v0.1.1 · A01]*

# 10. Handoff to UI Design System

The future UI Design System SHALL consume this specification and define visual tokens, typography, spacing scale, component styling, iconography, semantic colors, charts/graph visual grammar and implementation-ready component variants without changing the information or interaction semantics defined here.

# Annex A — Low-Fidelity Reference Frames

## WF-PAT-01 — Register / List

``` text
+--------------------------------------------------------------+
| GLOBAL HEADER | SEARCH | USER                                |
+-------------+------------------------------------------------+
| PRIMARY NAV | Context title                    [Create]       |
|             | Filters / facets / sort                         |
|             +------------------------------------------------+
|             | Result row / card                               |
|             | Result row / card                               |
|             | Result row / card                               |
+-------------+------------------------------------------------+
```

## WF-PAT-02 — Canonical Object Detail

``` text
+--------------------------------------------------------------+
| GLOBAL HEADER                                                |
+-------------+------------------------------------------------+
| PRIMARY NAV | OBJECT TITLE | STATUS | CLASSIFICATION          |
|             | Local tabs / contextual navigation              |
|             +------------------------------+-----------------+
|             | Main object content          | Provenance /    |
|             | facts / relationships        | backlinks /     |
|             |                              | warnings        |
+-------------+------------------------------+-----------------+
```

## WF-PAT-03 — Editor / Form

``` text
+--------------------------------------------------------------+
| Context title / version / classification                      |
+--------------------------------------------------------------+
| Section 1: required fields                                   |
| Section 2: analytical/provenance fields                      |
| Section 3: evidence links                                    |
| [inline validation / uncertainty help]                       |
+--------------------------------------------------------------+
| Cancel                         Save draft | Submit / Continue |
+--------------------------------------------------------------+
```

## WF-PAT-04 — Analytical Workspace

``` text
+--------------------------------------------------------------+
| CASE / OBJECT CONTEXT | LEGEND | FILTERS                      |
+--------------------------------------------------------------+
| TOOLBAR                                                      |
+-------------------------------------------+------------------+
|                                           | INSPECTOR        |
| PRIMARY ANALYTICAL CANVAS                 | provenance       |
| graph / timeline / value flow / matrix    | evidence         |
|                                           | uncertainty      |
+-------------------------------------------+------------------+
| Accessible list/table / history / details                    |
+--------------------------------------------------------------+
```

## WF-PAT-05 — Compare / Resolution

``` text
+--------------------------------------------------------------+
| Resolution context / candidate explanation                    |
+---------------------------+----------------------------------+
| CANDIDATE A               | CANDIDATE B                      |
| identifiers / evidence    | identifiers / evidence           |
+---------------------------+----------------------------------+
| Matches | Conflicts | Unknown / missing                     |
+--------------------------------------------------------------+
| Evidence / rationale                                          |
+--------------------------------------------------------------+
| Reject match | Defer                          Merge [confirm] |
+--------------------------------------------------------------+
```

## WF-PAT-06 — Review / Approval

``` text
+--------------------------------------------------------------+
| REVIEW SUBJECT | VERSION | AUTHOR | CLASSIFICATION             |
+-------------------------------------------+------------------+
| Frozen reviewed artefact                  | REVIEW PANEL     |
|                                           | checklist        |
| fact / analysis / gaps                    | comments         |
| evidence links                            | disconfirmation  |
+-------------------------------------------+------------------+
| Request changes | Reject                         Approve      |
+--------------------------------------------------------------+
```

## WF-PAT-07 — System State

``` text
+--------------------------------------------------------------+
| Context-safe heading                                           |
|                                                              |
| [STATE ICON / LABEL]                                          |
| Explanation that reveals no restricted information            |
| Safe next step / retry / return                               |
|                                                              |
+--------------------------------------------------------------+
```

# Annex B — Wireframe Review Checklist

- Is the screen ID from the Screen Inventory visible in the design file/component documentation?

- Does the main task dominate the layout without hiding provenance or uncertainty?

- Can a reviewer traverse from analytical proposition to evidence without losing context?

- Do restricted states avoid leaking object existence or protected-source identity?

- Are DIRECT, DOCUMENTED, RECONSTRUCTED and HYPOTHETICAL flows distinguishable without color alone?

- Are destructive/high-impact actions separated from routine actions?

- Is there a non-visual equivalent for graph/timeline/value-flow information?

- Are empty, error, conflict and superseded states represented?

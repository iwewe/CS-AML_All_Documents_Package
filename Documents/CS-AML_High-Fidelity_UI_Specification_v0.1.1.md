**CS-AML**

**High-Fidelity UI Specification**

Version 0.1.1

> **Document status — v0.1.1**
> Version: 0.1.1 — Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec). *[v0.1.1 · A01]*
> Supersedes: CS-AML High-Fidelity UI Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (decision register and release gates in `CHANGELOG.md`). No implementation test result or independent audit exists yet. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Purpose**  
> Proposed visual-composition baseline (draft for review) for translating CS-AML wireframes and UI design-system rules into desktop interfaces for MVP 0.1. This document is a composition reference written in prose; it is not a set of finished mockups, and no screen described here has been designed at high fidelity, implemented or usability-tested. *[v0.1.1 · A01; N07]*

> **Core visual axiom**  
> High visual fidelity SHALL improve comprehension without manufacturing certainty. Visual hierarchy may emphasize task relevance, state, and provenance, but SHALL NOT imply guilt, criminality, reliability, or analytical importance beyond the underlying record.

Status: Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) — UI composition baseline for MVP 0.1 *[v0.1.1 · A01]*

Dependencies: UX Specification · Information Architecture · Screen Inventory · Wireframe Specification · UI Design System

# Document Control

| **Attribute** | **Value** |
|----|----|
| Document ID | CSAML-HIFI-UI-0.1 |
| Version | 0.1.1 |
| Status | Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) — high-fidelity UI composition reference *[v0.1.1 · A01]* |
| Primary audience | Product Designer, UX Engineer, Frontend Engineer, QA, Product Owner |
| Applies to | MVP 0.1 production interfaces |
| Primary source IDs | SCR-\* screen IDs; WF-PAT-\* layout patterns |
| Normative verbs | SHALL / MUST / SHOULD / MAY |

# 1. Scope and Boundary

This specification defines visual composition at production fidelity. It determines how the wireframe regions and design-system primitives are assembled into concrete screens. *[v0.1.1 · A01]* It does not replace the UX specification, information architecture, canonical screen inventory, or component implementation specification.

| **Document** | **Owns** |
|----|----|
| UX Specification | Task flow, interaction behaviour, safety, reversibility, feedback, accessibility intent |
| Information Architecture | Object organisation, taxonomy, navigation, labeling, findability |
| Screen Inventory | Canonical screen IDs and required screen scope |
| Wireframe Specification | Structural regions and layout pattern |
| UI Design System | Tokens, primitive and semantic components, visual semantics |
| High-Fidelity UI Specification | Production visual composition for each screen family and critical screen |
| Storybook Implementation Specification (next) | Component implementation API, stories, test matrix, documentation, release process |

> **Boundary rule**  
> A high-fidelity screen SHALL NOT introduce a new object type, semantic state, navigation destination, or analytical meaning solely for visual convenience. Such changes require the owning specification to change first.

# 2. Visual Composition Principles

| **ID** | **Principle** | **Rule** |
|----|----|----|
| HIFI-P01 | Evidence-forward | Material analytical claims expose provenance access within the primary task context. |
| HIFI-P02 | Calm hierarchy | Use structure, spacing and typography before warning colors. |
| HIFI-P03 | Uncertainty visible | Unknown, disputed, candidate and inferred states stay perceivable at normal scanning distance. |
| HIFI-P04 | No guilt by prominence | Size, red, glow, rank or graph centrality SHALL NOT encode culpability. |
| HIFI-P05 | Action locality | Primary action sits near the object or workflow state it changes. |
| HIFI-P06 | Review parity | Reviewer sees the same analytical state and provenance context as author, plus review controls. |
| HIFI-P07 | Print/export parity | Critical semantic distinctions survive screenshot, grayscale and export. |
| HIFI-P08 | Dense but legible | Data-dense screens use structured density rather than compressed typography. |
| HIFI-P09 | Canonical consistency | The same object uses the same identity block across list, detail, graph and report contexts. |
| HIFI-P10 | Accessible alternatives | Graphical views have equivalent navigable list/table representations where material. |

# 3. Reference Viewport and Application Shell

| **Token / region** | **Desktop baseline** | **Behaviour** |
|----|----|----|
| Viewport | 1440 × 900 reference | Primary design review target; supports 1280 minimum without loss of required functions. |
| Top application bar | 56 px | Brand, primary destinations, global search trigger, user/session area. |
| Context header | 72–96 px | Case/object title, stable ID, classification/status, primary actions. |
| Local navigation | 40–44 px | Tabs or subnav scoped to current canonical context. |
| Main content | Fluid | Maximum readable prose width; analytical canvas may use full remaining width. |
| Inspector rail | 320–380 px | Evidence/provenance/object details; collapsible below wide desktop. |
| Page gutter | 24–32 px | Minimum 20 px at 1280. |
| Dense table row | 36–40 px | Default investigation register density. |
| Comfortable row | 44–48 px | Forms, review lists, mixed content. |
| Primary action height | 36–40 px | 44 px target for touch contexts where relevant. |

> **Shell composition**  
> The global shell SHALL remain visually quieter than case/object content. Classification and workflow risk use semantic banners only when action is required; they are not persistent decorative chrome.

# 4. High-Fidelity Token Application

| **Semantic role** | **Reference treatment** | **Usage constraint** |
|----|----|----|
| Canvas | \#F7F9FB | Main application background; not for cards needing hierarchy. |
| Primary text | \#16212B | Default text and icons. |
| Primary action | \#285C8E | Primary button/link emphasis; one dominant primary action per local task zone. |
| Success | \#246B4A | Completed/approved state; never evidence of innocence. |
| Warning / review | \#8A5A00 | Review needed, caution, unresolved condition. |
| Destructive / error | \#A13333 | Technical error, destructive action, integrity failure—not investigated subject. |
| Analytical construct | \#5B4B8A | Hypothesis/inference/derived analytical construct. |
| Documented state | \#236A73 | Documented analytical state where distinct from direct evidence. |
| Border | \#CBD5DF | Default panels/tables; increase contrast only for focus/error/selected. |
| Muted surface | \#F1F4F7 | Secondary panels, metadata strips, readonly context. |

# 5. Typography and Density

| **Role**        | **Reference**  | **Use**                                    |
|-----------------|----------------|--------------------------------------------|
| Page title      | 24–28 px / 650 | Screen/canonical object title.             |
| Section heading | 18–20 px / 650 | Major screen region.                       |
| Subsection      | 14–16 px / 600 | Panel or grouped controls.                 |
| Body            | 14–15 px / 400 | Primary reading.                           |
| Dense table     | 13–14 px / 400 | Registers and audit views.                 |
| Metadata        | 12–13 px / 400 | IDs, timestamps, provenance details.       |
| Badge/chip      | 12–13 px / 600 | Short semantic state only.                 |
| Monospace       | 12–13 px       | Hashes, stable IDs, technical identifiers. |

> **Density rule**  
> The UI MAY be dense, but text SHALL NOT be reduced merely to fit more data. Prefer progressive disclosure, column selection, inspectors, and expandable rows before shrinking type.

# 6. Canonical Visual Building Blocks

| **Block** | **Composition** | **Mandatory semantics** |
|----|----|----|
| Object identity block | Type icon + canonical name + stable ID + state badges | No allegation language; aliases secondary. |
| Case context block | Case title + case ID + classification + owner/status | Case is context, not container identity for canonical object. |
| Provenance strip | Source/Evidence ID + citation location + reliability/credibility + open action | Direct route to underlying evidence where authorized. |
| Analytical-state badge | Label + icon/pattern | Claim, Fact, Inference, Candidate, Disputed, Unknown distinct. A claim is never shown with the Fact treatment unless a recorded verification decision exists. *[v0.1.1 · A10]* |
| Flow-class legend | Line sample + label | DIRECT, DOCUMENTED, RECONSTRUCTED, HYPOTHETICAL always explicit (these are the `flow_class` wire values; display labels map from them). *[v0.1.1 · A09]* |
| Review block | Reviewer, version, status, issues, approval action | Author and reviewer identity separate. |
| Classification banner | Classification + handling note | Only when materially useful; source identity never leaked. Levels: Public, Internal, Sensitive, Restricted, Source-protected (wire `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`); access labels shown as additional restrictions, not levels. *[v0.1.1 · A08]* |
| Integrity warning | Prominent error surface + object ID + next action | Reserved for hash/version/integrity failures. |
| Version chip | Version number + status + supersession | Current/superseded/retracted clear without relying on color. |

# 7. Critical Screen Specifications

## SCR-HOME-001 — Home / Work Queue

| **Field** | **Specification** |
|----|----|
| Purpose | Give each user a calm operational landing page showing assigned work, reviews, recent cases and actionable exceptions. |
| Wireframe pattern | WF-PAT-01 |
| Primary composition | Two-column responsive dashboard: main work queue (≈70%) + contextual summary rail (≈30%). |
| Primary components | WorkQueueTable; CaseSummaryCard; ReviewQueueCard; AlertBanner; SavedFilter; EmptyState |
| Required states | Loading; empty; overdue; review-needed; permission-filtered |
| Responsive rule | At \<1100 px summary rail moves below queue; queue remains primary. |

**Engineering acceptance**

- No global guilt/risk ranking.

- Counts exclude unauthorized objects without revealing their existence.

- Urgency styling is based on workflow due date/status only.

## SCR-CASE-001 — Case Register

| **Field** | **Specification** |
|----|----|
| Purpose | Find and enter authorized cases efficiently. |
| Wireframe pattern | WF-PAT-01 (Register/List; Wireframe Specification mapping corrected to match) *[v0.1.1 · A15]* |
| Primary composition | Header + compact filter bar + dense table + optional saved views. |
| Primary components | DataGrid; FilterBar; SearchField; ClassificationBadge; StatusBadge; OwnerAvatar |
| Required states | Loading; empty; no-results; permission-filtered |
| Responsive rule | At narrow desktop nonessential columns collapse behind column chooser. |

**Engineering acceptance**

- Case title and stable ID are always visible.

- No case card uses red merely for sensitivity or allegation.

- Table row click and explicit open action both supported.

## SCR-CASE-003 — Case Overview

| **Field** | **Specification** |
|----|----|
| Purpose | Summarize case purpose, scope, work state and analytical progress without flattening uncertainty. |
| Wireframe pattern | WF-PAT-02 |
| Primary composition | Context header + local tabs; 8/4 grid: main summary and key work on left, gates/metadata on right. |
| Primary components | CaseIdentityHeader; ScopeSummary; GateStatusPanel; TaskSummary; RecentActivity; LinkedObjectSummary |
| Required states | Active; draft; blocked gate; archived/closed; permission-limited |
| Responsive rule | Right rail stacks below main at \<1150 px. |

**Engineering acceptance**

- Investigation question appears above analytical summary.

- Gate blockers are visible before downstream action buttons.

- Analytical progress is descriptive, not a guilt score.

## SCR-EVD-003 — Evidence Detail / Reader

| **Field** | **Specification** |
|----|----|
| Purpose | Read original evidence while retaining provenance, integrity and citation context. |
| Wireframe pattern | WF-PAT-02 |
| Primary composition | Three-region desktop: document canvas 58–65%, citation/provenance rail 28–34%, compact header/tool strip. |
| Primary components | DocumentViewer; EvidenceIdentity; HashStatus; CitationCreator; ProvenancePanel; DerivativeBadge; ClassificationBadge |
| Required states | Loading; unsupported preview; integrity mismatch; derivative; permission-limited |
| Responsive rule | At \<1200 px provenance rail becomes slide-over inspector; reader remains full width. |

**Engineering acceptance**

- Original/derivative state visible near document title.

- Integrity mismatch uses destructive/error semantic treatment.

- Citation creation never mutates original evidence.

- Protected-source identity omitted unless explicitly authorized.

## SCR-ENT-003 — Entity Detail

| **Field** | **Specification** |
|----|----|
| Purpose | Present a reusable canonical entity with aliases, identifiers, relationships, assets, case links and provenance. |
| Wireframe pattern | WF-PAT-02 |
| Primary composition | Object header + summary band + tabbed sections; 8/4 grid where right rail holds resolution/provenance state. |
| Primary components | EntityIdentityBlock; IdentifierTable; AliasList; RelationshipSummary; AssetSummary; CaseBacklinks; ResolutionState |
| Required states | Confirmed; probable; candidate; disputed; unresolved; merged/superseded; split (state labels map to `resolution_status` per Information Architecture v0.1.1 §9.3; candidate/probable reflect a pending or `POSSIBLE_MATCH` ResolutionDecision) *[v0.1.1 · ER]* |
| Responsive rule | Rail stacks at \<1100 px; tables remain horizontally scrollable only as last resort. |

**Engineering acceptance**

- Canonical identity and resolution state visually separate.

- Case associations do not duplicate entity identity.

- No centrality/risk indicator on entity header.

## SCR-ENT-005 — Entity Match Compare

| **Field** | **Specification** |
|----|----|
| Purpose | Support reversible, evidence-based merge decisions. |
| Wireframe pattern | WF-PAT-05 |
| Primary composition | Symmetrical A/B comparison with central decision rail; matching/conflicting attributes grouped by type. |
| Primary components | CompareColumn; MatchSignal; ConflictSignal; ProvenanceLink; MergeDecisionPanel (records a ResolutionDecision: merge, keep separate, possible match or defer); RationaleField *[v0.1.1 · ER]* — these are slot names of existing inventory components: CompareColumn, MatchSignal, ConflictSignal and MergeDecisionPanel → CMP-006 CompareResolutionFrame; ProvenanceLink → ANA-004 EvidenceCitation; RationaleField → GEN-005 TextArea (`rationale` variant); decision history → ANA-005 ProvenanceTrail (`decision-history` variant) *[v0.1.1 · C17]* |
| Required states | Candidate; insufficient evidence; conflict; merge-ready; decision recorded |
| Responsive rule | At \<1200 px columns remain side-by-side with horizontal containment; below tablet not primary supported workflow. |

**Engineering acceptance**

- No auto-merge action is visually dominant over review.

- Conflicting attributes receive equal visual prominence to matching attributes.

- Merge requires rationale and evidence.

- Unmerge consequences are previewed where available.

## SCR-TIM-001 — Timeline

| **Field** | **Specification** |
|----|----|
| Purpose | Show chronology while preserving date precision and evidence attribution. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Filter/tool strip + timeline canvas + optional event inspector + accessible list below/side. |
| Primary components | TimelineAxis; EventMarker; DatePrecisionLabel; FilterBar; EventInspector; AccessibleEventList |
| Required states | Empty; filtered-empty; dense cluster; approximate dates; permission-limited |
| Responsive rule | At \<1150 px inspector becomes drawer; accessible list remains available. |

**Engineering acceptance**

- Approximate dates visibly differ from exact dates.

- Event size does not imply importance unless user-selected filter explicitly says so.

- Every material event links to evidence.

## SCR-VAL-001 — Value Flow Workspace

| **Field** | **Specification** |
|----|----|
| Purpose | Explore movement of value and reconstruct multi-leg chains without conflating evidence classes. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Wide analytical canvas ≈70–75% + inspector ≈25–30%; persistent legend; filter bar above. |
| Primary components | ValueFlowCanvas; FlowLegend; FlowNode; FlowEdge; InspectorRail; EvidenceCitation; FlowClassBadge; AccessibleFlowTable |
| Required states | Mixed flow classes; unknown values; range values; no-data; permission-limited |
| Responsive rule | Inspector collapses below 1200 px; canvas never removes legend; list/table alternative available. |

**Engineering acceptance**

- Line semantics and labels distinguish all four classes without color.

- Unknown value displays “Unknown”, not 0.

- Reconstructed/hypothetical flows cannot use direct-flow or documented-flow styling. *[v0.1.1 · A09]*

- Selected edge reveals evidence/class/confidence in inspector.

> **High-fidelity note**  
> Reference line semantics: DIRECT solid + “DIRECT”; DOCUMENTED distinct solid + “DOCUMENTED”; RECONSTRUCTED dashed + “RECONSTRUCTED”; HYPOTHETICAL dotted + “HYPOTHETICAL”.

## SCR-TYP-002 — Typology Match Worksheet

| **Field** | **Specification** |
|----|----|
| Purpose | Compare observed patterns to catalogue typology with explicit counter-indicators and alternative explanations. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Left typology reference panel + central worksheet + right rationale/status inspector. |
| Primary components | TypologyHeader; IndicatorRow; CounterIndicatorRow; EvidenceCitation; ConsistencySelector; AlternativeExplanationPanel |
| Required states | No basis; weak; plausible; strong; compelling; incomplete |
| Responsive rule | Three columns collapse to stacked sections below 1180 px. |

**Engineering acceptance**

- Consistency is text-labelled; no percentage “risk meter”.

- Counter-indicators are not visually de-emphasized.

- Catalogue version is visible.

- Single weak indicator never renders a strong visual match automatically.

## SCR-HYP-001 — Hypothesis Workspace

| **Field** | **Specification** |
|----|----|
| Purpose | Maintain competing explanations and evidence balance. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Hypothesis cards/list on left; support/contradiction matrix center; gaps/notes inspector right. |
| Primary components | HypothesisCard; EvidenceMatrix; GapPanel; AssumptionList; ConfidenceLabel; StatusBadge |
| Required states | Open; supported; weakened; rejected; inconclusive; no alternatives |
| Responsive rule | At \<1200 px inspector drawers; hypothesis selector remains sticky. |

**Engineering acceptance**

- Legitimate/less-adverse alternatives receive equal card treatment.

- Rejected hypotheses remain visible in history.

- Supporting and contradicting evidence use symmetric visual weight.

## SCR-ASM-001 — Assessment Draft

| **Field** | **Specification** |
|----|----|
| Purpose | Compose a judgement with confidence, basis, alternatives and intelligence gaps. |
| Wireframe pattern | WF-PAT-03 |
| Primary composition | Document editor center + evidence/provenance rail right + metadata/status strip top. |
| Primary components | AssessmentEditor; ConfidenceSelector; EvidenceCitationList; AlternativeExplanationList; GapList; VersionState |
| Required states | Draft; incomplete; ready for review; returned; superseded |
| Responsive rule | Rail becomes slide-over below 1150 px. |

**Engineering acceptance**

- Confidence is a controlled label with rationale, not numeric guilt meter. Options are High, Moderate, Low and Insufficient basis (wire `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`); Insufficient basis is shown as a neutral, separate option, never as a level below Low. *[v0.1.1 · A09]*

- Missing alternatives/gaps produce review warning, not hidden validation.

- Material judgement must retain linked evidence.

## SCR-GRF-001 — Investigation Graph

| **Field** | **Specification** |
|----|----|
| Purpose | Explore evidence-backed relationships while avoiding visual implication of culpability. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Full analytical canvas + compact filter bar + 320–360 px provenance inspector + legend. |
| Primary components | GraphCanvas; Node; Edge; Legend; FilterBar; InspectorRail; AccessibleGraphTable |
| Required states | Empty; sparse; dense; permission-filtered; selected node/edge |
| Responsive rule | Inspector collapsible; list/table alternative; mobile not target for full graph editing. |

**Engineering acceptance**

- Node color encodes entity type/state only where semantically approved.

- Node size SHALL NOT encode guilt/risk by default.

- Centrality/path ranking is not shown as risk.

- Every material edge opens its canonical Relationship record.

## SCR-PRD-003 — Product Editor

| **Field** | **Specification** |
|----|----|
| Purpose | Create a structured intelligence product while retaining traceability and handling controls. |
| Wireframe pattern | WF-PAT-03 |
| Primary composition | Structured report editor 65–70% + evidence/review rail 30–35%; top version/classification strip. |
| Primary components | ProductSectionEditor; EvidenceIndexPanel; ClassificationBanner; VersionChip; SaveState; ValidationPanel |
| Required states | Draft; incomplete; ready for review; approved-readonly; superseded |
| Responsive rule | Rail collapses to drawer below 1150 px. |

**Engineering acceptance**

- Key findings support direct evidence navigation.

- Fact/analysis/gap sections use explicit labels.

- Approved version is readonly; edits create new version.

## SCR-REV-002 — Peer Review Workspace

| **Field** | **Specification** |
|----|----|
| Purpose | Allow independent review of evidence basis, alternatives, confidence, identity and harm before approval. |
| Wireframe pattern | WF-PAT-06 |
| Primary composition | Product/assessment content left ≈65%; review panel right ≈35%; sticky review decision footer/rail. |
| Primary components | ReviewChecklist; InlineComment; EvidenceJump; IssueList; DecisionControls; ReviewerIdentity |
| Required states | Not-started; in-review; changes-requested; approved; rejected |
| Responsive rule | Review panel becomes drawer below 1150 px; decision controls remain reachable. |

**Engineering acceptance**

- Reviewer identity and product version are fixed in context header.

- Approve action is not available to author when policy forbids self-approval.

- Disconfirming-search requirement visibly blocks high-impact approval when unmet.

## SCR-DIS-001 — Dissemination Approval

| **Field** | **Specification** |
|----|----|
| Purpose | Control external sharing based on recipient, purpose, classification, minimization and approval. |
| Wireframe pattern | WF-PAT-06 |
| Primary composition | Approval summary + package manifest + restrictions + final action zone. |
| Primary components | RecipientSummary; PurposeField; ClassificationBanner; ManifestTable; RestrictionList; ApprovalControls |
| Required states | Draft; blocked; ready; approved; expired/revoked |
| Responsive rule | Single-column on smaller desktop; manifest remains table with selectable columns. |

**Engineering acceptance**

- External sharing action disabled until required approval exists.

- Protected-source identity is not listed in ordinary package manifest.

- Included/excluded objects are explicit before approval.

## SCR-DIS-002 — Export Package Builder

| **Field** | **Specification** |
|----|----|
| Purpose | Select and preview an approved export while preserving handling, minimization and audit. |
| Wireframe pattern | WF-PAT-04 |
| Primary composition | Object selection left 35–40%; package preview/manifest center 40–45%; handling inspector 20–25%. |
| Primary components | ObjectSelector; RedactionToggle; ManifestTable; HandlingPanel; PreviewPanel; ExportAction |
| Required states | Draft; validation warning; blocked restricted object; ready; exported |
| Responsive rule | At \<1200 px inspector becomes drawer; object selection and manifest stack. |

**Engineering acceptance**

- Export clearly separates included vs excluded objects.

- Unauthorized restricted objects cannot be selected even by URL manipulation.

- Export creates immutable audit event and package/version manifest.

## SCR-AUD-001 — Audit Explorer

| **Field** | **Specification** |
|----|----|
| Purpose | Inspect immutable material actions without exposing unnecessary evidence content. |
| Wireframe pattern | WF-PAT-01 |
| Primary composition | Dense filterable event table + optional event detail drawer. |
| Primary components | AuditTable; FilterBar; ActorChip; ObjectLink; EventDetailDrawer |
| Required states | Loading; no results; filtered; permission-limited |
| Responsive rule | Table optimized for desktop; drawer becomes full-screen panel below 1000 px. |

**Engineering acceptance**

- Ordinary users cannot edit audit events.

- Routine audit text avoids sensitive evidence payloads.

- Every event shows actor/action/object/time/correlation where available.

# 8. Secondary Screen Family Standards

| **Family** | **Screens** | **High-fidelity rule** |
|----|----|----|
| Create/Edit forms | SCR-CASE-002, SCR-CASE-004, SCR-EVD-002, SCR-EVD-004, SCR-ENT-002, SCR-REL-001, SCR-TIM-002 | Use 640–820 px reading column for normal forms; two-column only for strongly related fields. Required/legal/security fields group visibly. |
| Registers | SCR-SRC-001, SCR-EVD-001, SCR-ENT-001, SCR-AST-001, SCR-PRD-001, SCR-REV-001, SCR-DIS-003 | Filter/search first; dense grid second; primary action top-right; no decorative card grids for large datasets. |
| Object detail | SCR-SRC-002, SCR-EVD-005, SCR-AST-002, SCR-ASM-002, SCR-PRD-004 | Canonical identity header + tabs/sections + provenance/history; readonly state visually distinct but not greyed into illegibility. |
| Governance/admin | SCR-ADM-001..004 | Conservative admin surfaces; destructive actions separated; policy/version metadata always visible. |
| System states | SCR-SYS-001..003 | Centered or contextual state panel with plain-language reason, object/context ID when safe, and next action. Never reveal restricted-object existence when policy forbids it. |

# 9. Responsive and Viewport Behaviour

| **Range** | **Expectation** |
|----|----|
| ≥1440 px | Full reference composition; inspector rails persistent where useful. |
| 1280–1439 px | Full desktop; some metadata columns may collapse; no loss of primary task controls. |
| 1100–1279 px | Inspector rails SHOULD become collapsible/drawers; analytical canvas retains priority. |
| 900–1099 px | Tablet/compact desktop: registers/forms supported; complex graph/value-flow editing reduced but not semantically altered. |
| \<900 px | Not a primary MVP authoring target. Read/review MAY be supported; system SHALL not pretend complex graph/flow authoring is equivalent if usability is inadequate. |

# 10. High-Fidelity State Treatment

| **State** | **Visual treatment** | **Rule** |
|----|----|----|
| Loading | Skeleton or progress in local region | Avoid page-blocking spinners where partial content can render safely. |
| Empty | Neutral empty panel + primary next action | Empty is not error. |
| No results | Query/filter summary + clear reset | Do not imply database is empty. |
| Permission denied | Neutral security state + request/access path if supported | Do not leak hidden object metadata. |
| Integrity failure | Error/destructive surface with checksum/object context | Must be visually stronger than ordinary validation warning. |
| Stale version | Warning surface + compare/reload/resolve actions | Never silently overwrite newer work. |
| Readonly approved | Normal legibility + readonly badge/version state | Do not disable all text contrast. |
| Superseded | Version banner + current version link | Historical content remains readable/auditable. |
| Disputed / unknown | Analytical-state badge + explicit text | Do not map to destructive/error color by default. |
| Candidate match | Candidate semantic treatment + evidence comparison | Never style as confirmed identity. |

# 11. Language and Microcopy

| **Avoid** | **Preferred** |
|----|----|
| “Suspicious person” | “Subject entity” / “Entity under analysis” |
| “Money laundering confirmed” | “Assessment is consistent with…” / “Indicators support…” where justified |
| “Risk score 87” | Named factors, confidence, typology consistency and rationale |
| “Bad match” | “Conflicting attributes” |
| “Safe / clean entity” | “No relevant indicator identified in current scope” |
| “Unknown = 0” | “Unknown” / range / minimum / maximum / approximate |
| “AI found” | “AI-assisted suggestion — review required” |

# 12. Frontend Handoff Contract

- Every production screen SHALL retain its canonical SCR-\* ID in design documentation and automated test naming where practical.

- Frontend implementation SHALL consume semantic tokens/components from the design system rather than re-create local visual semantics.

- High-fidelity screen composition SHALL remain traceable to the owning wireframe pattern and IA destination.

- Any implementation deviation that changes analytical meaning, hierarchy, permission visibility, or review/dissemination safety requires design review.

- Graph/timeline/value-flow libraries MAY implement their own primitives, but semantic styling SHALL be adapted to CS-AML tokens and legends.

- Critical empty/error/permission/integrity/version states SHALL be implemented before a screen is considered UI-complete.

# 13. High-Fidelity UI Definition of Done

| **Area** | **Done when** |
|----|----|
| Traceability | Screen is linked to SCR-\* ID, WF-PAT-\* pattern, UX and IA requirements. |
| Visual composition | Desktop reference layout matches this specification and approved design-system semantics. |
| States | Loading, empty, no-results, error, permission, readonly/version/conflict states are covered where applicable. |
| Uncertainty | Claim/fact/inference/candidate/disputed/unknown and flow classes remain visibly distinct. |
| Provenance | Material analytical elements provide evidence/source navigation where required. |
| Security | Protected-source and classification rules are preserved; denied states do not leak hidden metadata. |
| Accessibility | Keyboard/focus/contrast/non-color semantics and alternative representations are verified. |
| Responsive | Required desktop/compact-desktop breakpoints preserve the task. |
| Review/export | Screenshot/PDF/export retains required analytical distinctions. |
| Engineering parity | Implemented screen uses shared components/tokens and passes visual regression for critical states. |

> The criteria above are targets for future implementation. No visual-regression, accessibility or usability results exist for CS-AML at this baseline; accessibility work targets WCAG 2.2 AA and does not constitute a conformance claim. *[v0.1.1 · A01; N07]*

# 14. Screen Coverage Matrix

| **Screen ID**    | **Screen**                       | **Coverage**    |
|------------------|----------------------------------|-----------------|
| SCR-HOME-001     | Home / Work Queue                | Detailed        |
| SCR-CASE-001     | Case Register                    | Detailed        |
| SCR-CASE-003     | Case Overview                    | Detailed        |
| SCR-EVD-003      | Evidence Detail / Reader         | Detailed        |
| SCR-ENT-003      | Entity Detail                    | Detailed        |
| SCR-ENT-005      | Entity Match Compare             | Detailed        |
| SCR-TIM-001      | Timeline                         | Detailed        |
| SCR-VAL-001      | Value Flow Workspace             | Detailed        |
| SCR-TYP-002      | Typology Match Worksheet         | Detailed        |
| SCR-HYP-001      | Hypothesis Workspace             | Detailed        |
| SCR-ASM-001      | Assessment Draft                 | Detailed        |
| SCR-GRF-001      | Investigation Graph              | Detailed        |
| SCR-PRD-003      | Product Editor                   | Detailed        |
| SCR-REV-002      | Peer Review Workspace            | Detailed        |
| SCR-DIS-001      | Dissemination Approval           | Detailed        |
| SCR-DIS-002      | Export Package Builder           | Detailed        |
| SCR-AUD-001      | Audit Explorer                   | Detailed        |
| All other SCR-\* | Mapped by screen-family standard | Family baseline |

# 15. Relationship to Component Inventory and Storybook Specification

> **Next implementation document**  
> The next document SHALL translate this high-fidelity composition into a frontend implementation catalogue: component inventory, component ownership, props/variants, design tokens, accessibility contract, Storybook stories, interaction tests, visual-regression matrix, documentation standards, and release/versioning workflow.

# Annex A — High-Fidelity Review Checklist

**☐** Correct SCR-\* ID and screen title shown in design artefact metadata.

**☐** Primary task is visually obvious without relying on alarm color.

**☐** Canonical object identity and case context are not conflated.

**☐** Classification/handling is visible where useful but not decorative.

**☐** Provenance can be reached from material analytical content.

**☐** Unknown, disputed, candidate and inference states are explicit.

**☐** Value-flow classes retain non-color cues.

**☐** Graph size/color does not imply guilt or unvalidated risk.

**☐** Protected-source identity is absent unless role permits access.

**☐** Permission-denied state does not reveal hidden metadata.

**☐** Empty/no-results/loading/error/conflict states are specified.

**☐** Keyboard focus order and interactive target hierarchy are coherent.

**☐** Inspector/drawer collapse preserves task context.

**☐** Export/screenshot remains semantically interpretable.

**☐** All shared UI uses design-system semantic tokens/components.

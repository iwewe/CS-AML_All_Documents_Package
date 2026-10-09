**CS-AML**

UI Design System  
Specification v0.1.2

Proposed visual and component baseline (draft for review) for the CS-AML MVP analyst interface *[v0.1.1 · A01]*

> **Document status — v0.1.2**
> Version: 0.1.2 — Approved Internal Specification Baseline (2026-10-09, tag v0.1.2-spec). Supersedes v0.1.1 (2026-10-08, tag v0.1.1-spec). *[v0.1.2]*
> Supersedes: CS-AML UI Design System Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (v0.1.1) and 2026-10-09 (v0.1.2; decision register and release gates in `CHANGELOG.md`). The v0.1.2 changes come from change requests raised while implementing increments I1–I4; this is not an independent audit. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).
> Changes in 0.1.2: change requests CR-I1-01…CR-I4-14 approved by the product owner on 2026-10-09 (`CHANGELOG.md`, section v0.1.2). Each change is tagged `*[v0.1.2 · CR-xx-yy]*`.

> **Design-system axiom**
>
> The visual system SHALL communicate analytical state, provenance, uncertainty, permission, review status, and operational risk without implying guilt, suspicion, certainty, or importance merely through visual prominence.

| **Document control** | **Value** |
|----|----|
| Document ID | CSAML-UI-DS-0.1 |
| Version | 0.1.2 *[v0.1.2]* |
| Status | Approved Internal Specification Baseline (2026-10-09, tag v0.1.2-spec) — normative UI design-system baseline for MVP 0.1 *[v0.1.1 · A01]* |
| Depends on | UX Specification; Information Architecture Specification; Screen Inventory; Wireframe Specification |
| Primary consumers | Product design, frontend engineering, QA, accessibility, product owner |
| Baseline theme | Light, calm, data-dense, evidence-first |
| MVP frontend reference | React + TypeScript + Tailwind CSS 4 |

# 1. Purpose, Scope, and Ownership

This specification defines the shared visual language and reusable UI component system for the CS-AML application. It standardises tokens, typography, spacing, color semantics, component anatomy, component states, data-density rules, analytical visual semantics, accessibility rules, and frontend implementation conventions.

## 1.1 What this document owns

- Design tokens: color, typography, spacing, size, border, radius, elevation, motion, opacity, and focus.

- Reusable UI components and their visual/semantic states.

- Analytical visualization semantics for graph, timeline, value flow, confidence, provenance, and uncertainty.

- Accessibility constraints and component-level interaction affordances where visual styling is involved.

- Frontend design-system implementation and governance conventions.

## 1.2 What this document does not own

| **Concern** | **Owning specification** |
|----|----|
| Task flows, interaction behaviour, feedback, safety | CS-AML UX Specification |
| Navigation, taxonomy, object hierarchy, findability | CS-AML Information Architecture Specification |
| Screen catalogue and canonical screen IDs | CS-AML Screen Inventory |
| Screen regions and low-fidelity composition | CS-AML Wireframe Specification |
| Functional behaviour and acceptance | PRD / SRS / MVP Engineering Breakdown |

> **Non-overlap rule**
>
> A design-system component MAY provide styles and states for navigation, forms, reviews, or graph views, but SHALL NOT redefine the information hierarchy, task flow, or business rule of those features.

# 2. Design Principles

| **ID** | **Principle** | **Normative intent** |
|----|----|----|
| DS-P01 | Evidence first | The visual hierarchy SHALL make provenance and supporting evidence easy to inspect without making allegations visually dominant. |
| DS-P02 | Uncertainty visible | Unknown, disputed, inferred, reconstructed, hypothetical, and verified states SHALL be perceptibly different. |
| DS-P03 | Calm over alarm | The baseline UI SHALL avoid threat-dashboard aesthetics, excessive red, flashing indicators, or dramatic risk-score presentation. |
| DS-P04 | No guilt by color | Entity type, centrality, case participation, or network prominence SHALL NOT be encoded as suspicion or guilt. |
| DS-P05 | Accessible by default | Meaning SHALL NOT depend on color alone; keyboard focus, contrast, labels, and readable density are mandatory. |
| DS-P06 | Dense but legible | The system SHOULD support professional investigative density while preserving grouping, scanability, and touch/click target adequacy. |
| DS-P07 | Canonical consistency | The same status or analytical concept SHALL use the same token and component semantics across all screens. |
| DS-P08 | Reversible state awareness | Merge, review, supersession, conflict, and destructive actions SHALL have visual cues that reveal reversibility or permanence. |
| DS-P09 | Security is visible when useful | Classification, restricted handling, and protected-source states SHALL be visible to authorised users without unnecessarily exposing sensitive details. |
| DS-P10 | Print/export parity | Critical semantic distinctions SHALL survive screenshots, grayscale print, PDF export, and copied report visuals. |

# 3. Design Token Architecture

All visual values used by production components SHOULD be expressed through semantic design tokens rather than one-off literal styling. Component code SHALL prefer semantic tokens over raw palette values.

## 3.1 Token layers

| **Layer** | **Purpose** | **Examples** |
|----|----|----|
| Primitive | Raw visual values | blue.700, gray.100, space.4, radius.md |
| Semantic | Meaningful UI role | surface.canvas, text.muted, border.default, status.warning |
| Analytical | CS-AML analytical meaning | flow.documented, proposition.inferred, confidence.low |
| Component | Local component mapping | button.primary.bg, badge.disputed.bg, graph.edge.reconstructed |

## 3.2 Naming rules

- Use lowercase dot notation in implementation tokens, e.g. `color.text.primary`.

- Do not encode a specific hue into semantic token names such as `status.error`; the hue may change without changing meaning.

- Analytical tokens SHALL use domain meaning, not emotional labels such as “dangerous entity”.

- Every token intended to communicate state SHALL define light-theme contrast requirements and a non-color companion cue where material.

## 3.3 Core token requirements

| **ID** | **Requirement** |
|----|----|
| DS-001 | Production UI SHALL source colors, spacing, typography, radius, elevation, and state styling from versioned design tokens. |
| DS-002 | Semantic state tokens SHALL NOT be hard-coded independently in feature modules. |
| DS-003 | Analytical state tokens SHALL map consistently across graph, timeline, tables, badges, forms, and export-ready views. |
| DS-004 | Token changes that alter analytical meaning SHALL be reviewed by UX and domain owners, not frontend engineering alone. |

# 4. Color System

The MVP baseline uses a restrained light theme. Color is used to establish hierarchy and state, not to create a “security operations” aesthetic. Red is reserved primarily for destructive/error conditions; it is not a generic suspicion color.

## 4.1 Primitive palette baseline

| **Token**  | **Hex**  | **Usage**                              | **Swatch** |
|------------|----------|----------------------------------------|------------|
| Navy 900   | \#17324D | Primary headings, strong chrome        |            |
| Blue 700   | \#285C8E | Primary action/accent                  |            |
| Ink 900    | \#16212B | Primary text                           |            |
| Slate 600  | \#5E6B75 | Secondary text                         |            |
| Line 300   | \#D7DEE5 | Borders/dividers                       |            |
| Canvas     | \#F7F9FB | Application background                 |            |
| Green 700  | \#246B4A | Confirmed success/completed            |            |
| Amber 700  | \#8A5A00 | Warning/review needed                  |            |
| Red 700    | \#A13333 | Error/destructive action               |            |
| Purple 700 | \#5B4B8A | Hypothesis/analytical construct        |            |
| Cyan 700   | \#236A73 | Documented/derived informational state |            |

## 4.2 Semantic color roles

| **Semantic token** | **Meaning** | **Do not use for** |
|----|----|----|
| color.status.success | Completed/confirmed operational success | “Person is clean” or innocence claim |
| color.status.warning | Needs attention, incomplete, review required | Suspicion |
| color.status.error | System error, invalid state, destructive action | Adverse assessment by default |
| color.status.info | Informational/system context | Evidence strength |
| color.classification.restricted | Restricted handling visibility | Analytical guilt |
| color.analytical.construct | Hypothesis/inference construct | Verified fact |

> **Critical prohibition**
>
> A person, organisation, company, address, wallet, or other entity SHALL NOT become red merely because it is a subject, appears in an investigation, has many graph links, matches a typology, or is associated with an adverse hypothesis.

# 5. Typography

Aptos is the reference documentation font; the product UI SHOULD use a widely available, highly legible system sans stack or an approved equivalent. The design system is font-family-neutral at the semantic level.

| **Token** | **Reference size** | **Weight** | **Use** |
|----|----|----|----|
| type.display | 28-32 px | 600 | Rare product-level titles |
| type.h1 | 24 px | 600 | Screen title |
| type.h2 | 20 px | 600 | Major section |
| type.h3 | 16 px | 600 | Panel/subsection title |
| type.body | 14-16 px | 400 | Primary content |
| type.body.compact | 13-14 px | 400 | Dense tables and metadata |
| type.label | 12-13 px | 500 | Form labels, chips |
| type.caption | 11-12 px | 400 | Secondary provenance and helper text |
| type.mono | 12-14 px | 400 | IDs, hashes, technical identifiers |

- Body text SHOULD normally render at 14 px or larger in the product UI.

- Critical evidence excerpts, assessments, and review text SHOULD use at least 14 px with comfortable line height.

- Monospace MAY be used for hashes, registration IDs, URLs, wallet addresses, and machine identifiers, but not for long prose.

- All-caps SHALL NOT be used for long status labels; reserve it for short controlled labels where scanability improves.

# 6. Spacing, Density, and Layout Tokens

| **Token** | **Value** | **Typical use**           |
|-----------|-----------|---------------------------|
| space.1   | 4 px      | Tight icon/text gap       |
| space.2   | 8 px      | Inline groups             |
| space.3   | 12 px     | Compact controls          |
| space.4   | 16 px     | Default component padding |
| space.5   | 20 px     | Panel content             |
| space.6   | 24 px     | Section spacing           |
| space.8   | 32 px     | Major section separation  |
| space.12  | 48 px     | Large layout separation   |

## 6.1 Density modes

| **Mode** | **Purpose** | **Constraints** |
|----|----|----|
| Comfortable | Reading, review, authoring | Larger vertical rhythm; default for prose-heavy views |
| Compact | Registers, evidence lists, entity tables | Reduced vertical padding; text remains \>=13 px; targets remain keyboard accessible |
| Analytical canvas | Graph/timeline/value flow | Maximise working area while keeping inspector/legend readable |
| Presentation/export | Screenshots, PDF, referral | Semantic distinction remains visible without hover or interaction |

The UI MAY allow users to choose comfortable versus compact density for data-heavy surfaces. A density preference SHALL NOT hide provenance, confidence, classification, or uncertainty indicators.

# 7. Borders, Radius, Elevation, and Surfaces

| **Token**      | **Baseline**       | **Rule**                           |
|----------------|--------------------|------------------------------------|
| radius.sm      | 4 px               | Inputs, chips, compact controls    |
| radius.md      | 8 px               | Cards, panels, menus               |
| radius.lg      | 12 px              | Large dialogs/sheets only          |
| border.default | 1 px               | Neutral structural separation      |
| elevation.1    | Subtle shadow      | Floating menus/tooltips            |
| elevation.2    | Moderate shadow    | Modal/dialog only                  |
| surface.canvas | Very light neutral | App background                     |
| surface.panel  | White              | Primary workspace panels           |
| surface.subtle | Light neutral      | Grouped metadata/read-only regions |

Persistent cards SHOULD rely more on borders and spacing than on heavy shadows. Excessive elevation is discouraged because the interface is a professional evidence workspace, not a consumer dashboard.

# 8. Iconography

- Icons SHALL have a text label or accessible name when they invoke actions.

- Icon shape SHALL NOT be the only carrier of analytical meaning where confusion is plausible.

- Use a single icon family with consistent stroke weight.

- Avoid law-enforcement symbolism (handcuffs, targets, crosshairs) as default analytical icons.

- Entity-type icons MAY distinguish person, organisation, company, asset, account, wallet, address, contract, and project, but SHALL NOT imply adverse status.

# 9. Interactive State Model

| **State** | **Visual requirements** | **Accessibility** |
|----|----|----|
| Default | Normal surface/border/text | Normal accessible name |
| Hover | Subtle surface/border change | Never only indication of availability |
| Focus | High-contrast focus ring | Visible for keyboard focus; not removed |
| Active/selected | Persistent border/fill + selected indicator | aria-selected/pressed where applicable |
| Disabled | Reduced emphasis but readable | Disabled reason available when useful |
| Loading | Skeleton/progress without layout jump | Announce long-running operations |
| Error | Error text + icon + field relationship | Do not rely on red alone |
| Success | Confirmation text/icon | Do not auto-dismiss critical confirmation too fast |
| Conflict | Distinct conflict banner/region | Describe competing version and recovery |
| Read-only | Read-only label and neutral surface | Avoid disabled styling if content remains inspectable |

| **ID** | **Requirement** |
|----|----|
| DS-005 | Keyboard focus SHALL be visually obvious on every actionable component. |
| DS-006 | Error, warning, success, and analytical states SHALL combine color with text, icon, pattern, border, or label. |
| DS-007 | Disabled high-impact actions SHOULD explain the prerequisite when the user is authorised to know it. |
| DS-008 | Loading and async states SHALL preserve enough context that investigators know which object/action is pending. |

# 10. Analytical State Semantics

Analytical state is domain meaning, not generic UI status. These states require dedicated tokens and consistent rendering across badges, tables, detail pages, graph, timeline, value flow, and exported visuals.

## 10.1 Proposition state

| **State** | **Visual treatment** | **Meaning** |
|----|----|----|
| Claim | Outlined neutral badge + “Claim” label | Statement attributed to a source; not verified fact |
| Fact | Solid neutral/blue badge + “Fact” label plus fact status (Provisional / Established / Disputed / Superseded) | Proposition with a recorded VerificationDecision; a Claim SHALL NOT receive the Fact badge without one *[v0.1.1 · A10]* |
| Inference | Purple outlined badge + “Inference” | Analytical interpretation |
| Disputed | Amber patterned/outlined badge | Material contradiction or challenge exists |
| Unknown | Gray dashed treatment + “Unknown” | Information not established |
| Candidate | Light outlined badge + “Candidate” | Suggested entity/match/relationship awaiting review |

## 10.2 Confidence

| **Level** | **Treatment** | **Constraint** |
|----|----|----|
| High (`HIGH`) | Label + strong border | Never represented as certainty/proof |
| Moderate (`MODERATE`) | Label + medium border | Basis must remain inspectable |
| Low (`LOW`) | Label + light/dashed border | Do not hide as secondary metadata |
| Insufficient basis (`INSUFFICIENT_BASIS`) | Neutral label, separate from the High/Moderate/Low scale | Must not look like an adverse result and SHALL NOT be styled, ordered or worded as a level below Low *[v0.1.1 · A09]* |

- Wire values are `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS` (UPPER_SNAKE_CASE, derived from the Data Model Annex A registry); the labels in the first column are translatable display labels. *[v0.1.1 · A09]*

- `INSUFFICIENT_BASIS` means a judgement was attempted but the evidential basis is insufficient. The UI SHALL NOT render it as Low, empty, zero or a missing value, and SHALL NOT place it on a graded scale or meter. A draft with no confidence judgement yet (null) SHALL be shown as "Not yet assessed", which is distinct from Insufficient basis. Rationale SHALL be reachable for every level. *[v0.1.1 · A09]*

> **Confidence rule**
>
> Confidence is confidence in an assessment, not a probability of guilt. The UI SHALL NOT convert confidence language into a “risk meter”, percentage gauge, or threat score unless a separately validated model explicitly requires it.

# 11. Value-Flow Visual Semantics

| **Class** | **Line token** | **Mandatory text cue** | **Meaning** |
|----|----|----|----|
| DIRECT | Solid line | DIRECT label | Direct transaction/value evidence where authoritative evidence supports it |
| DOCUMENTED | Solid/double-accent line | DOCUMENTED label | Documented value relationship such as contract, award, purchase |
| RECONSTRUCTED | Dashed line | RECONSTRUCTED label | Analyst reconstruction from multiple records |
| HYPOTHETICAL | Dotted line | HYPOTHETICAL label | Analytical possibility/hypothesis |

- The class names above are the `flow_class` wire values (`DIRECT`, `DOCUMENTED`, `RECONSTRUCTED`, `HYPOTHETICAL`, derived from the Data Model Annex A registry); visual tokens and display labels map from them and SHALL NOT promote RECONSTRUCTED or HYPOTHETICAL flows to the DIRECT/DOCUMENTED treatment. *[v0.1.1 · A09]*

- Color MAY supplement but SHALL NOT replace line style and text label.

- Legends SHALL remain visible or easily accessible in analytical workspaces and exports.

- Unknown values SHALL display “Unknown”, not 0.

- Ranges and approximate values SHALL retain approximation markers.

- A chain containing mixed epistemic classes SHALL preserve the class of each leg; the whole chain SHALL NOT inherit the strongest class. A chain is never shown stronger than its weakest leg; each leg shows its own class, evidence, value and confidence. *[v0.1.2 · CR-I3-04, CR-I3-09]*

- Legends SHALL use the class label, text cue, line style, meaning and evidence rule served by `GET /value-flow-legend`. *[v0.1.2 · CR-I3-03]*

- Aggregation rules (value-flow view): *[v0.1.2 · CR-I3-12]*
  - Totals are shown only per group of (flow class, flow type, currency); there is no grand total across classes, types or currencies.
  - CONTRACT and SUBCONTRACT groups are labelled as an obligation, not as settled value; only DIRECT groups may be presented as settlement-evidenced.
  - Each group shows a lower-bound total, an upper-bound total (shown as unknown when any amount is unknown or open-ended) and an exact total only when every amount is a known, non-approximate point value.
  - Unknown amounts are displayed as "Unknown" and counted in the group; they are never treated as 0. Range and approximate counts are shown.
  - Legs decompose their flow's value and are never added to the flow's total.

# 12. Investigation Graph Design Rules

| **Element** | **Design rule** |
|----|----|
| Node type | Use neutral type-specific icon/shape; do not encode suspicion. |
| Node size | Default size SHOULD be stable. Centrality MAY be optional analytic overlay, not default guilt cue. |
| Edge | Type + status + evidence availability must be inspectable. |
| Inferred edge | Use distinct analytical styling and label. |
| Selection | High-contrast outline; do not change semantic status. |
| Restricted object | Render only according to permission policy; never reveal hidden node count if prohibited. |
| Provenance | Inspector SHALL expose relationship record and supporting evidence. |
| Community colors | Exploratory palette only; legend states algorithmic grouping, not culpability. |

> **Graph prohibition**
>
> Red nodes, skull icons, target rings, heat-map threat coloring, or automatic “high risk” styling SHALL NOT be assigned solely from degree, centrality, path proximity, typology match, or presence in a case.

# 13. Timeline Design Rules

- Exact, approximate, month-only, year-only, range, and unknown date precision SHALL be visually distinguishable.

- Events SHALL expose type, involved objects, date precision, and evidence/provenance.

- Current versus historical relationship state SHALL be distinguishable without requiring hover.

- Dense timelines MAY collapse low-priority items, but hidden count and filtering logic SHALL be visible.

- Timeline color SHOULD primarily encode event category or selection, not adverse status.

# 14. Component Catalogue

| **ID** | **Component** | **Primary use** |
|----|----|----|
| DS-C001 | Button | Primary, secondary, tertiary, danger, icon |
| DS-C002 | Text input | Text, URL, identifier, amount |
| DS-C003 | Select / combobox | Controlled vocabulary, entity picker |
| DS-C004 | Date / date precision | Exact/approximate/range/unknown |
| DS-C005 | Checkbox / radio / switch | Explicit state controls |
| DS-C006 | Badge / status pill | Lifecycle, analytical state, classification |
| DS-C007 | Chip / token | Filters, entity/relationship tags |
| DS-C008 | Alert / callout | Error, warning, info, integrity |
| DS-C009 | Toast | Transient non-critical feedback |
| DS-C010 | Table / data grid | Registers and dense object lists |
| DS-C011 | Card / panel | Grouped object/detail region |
| DS-C012 | Tabs | Local object/workspace sections |
| DS-C013 | Breadcrumb / context trail | Context orientation; IA labels authoritative |
| DS-C014 | Drawer / side inspector | Evidence/provenance/object detail |
| DS-C015 | Modal / dialog | High-focus bounded actions |
| DS-C016 | Confirmation dialog | Destructive/high-impact confirmation |
| DS-C017 | Evidence citation | Source/evidence ID + precise locator |
| DS-C018 | Provenance trail | Backward lineage chain |
| DS-C019 | Confidence badge | Assessment confidence label + rationale entry |
| DS-C020 | Flow class badge | Four mandatory value-flow classes |
| DS-C021 | Entity identity block | Type, canonical name, aliases/status |
| DS-C022 | Relationship summary | Type, endpoints, dates, evidence/confidence |
| DS-C023 | Review decision panel | Approve/request changes/reject + rationale |
| DS-C024 | Classification banner | Handling/classification context |
| DS-C025 | Empty state | Explain why empty and next permitted action |
| DS-C026 | Permission state | Non-disclosing denial / access request guidance |
| DS-C027 | Integrity warning | Hash mismatch/evidence integrity issue |
| DS-C028 | Version/supersession banner | Current/superseded/retracted state |
| DS-C029 | Skeleton / progress | Async loading |
| DS-C030 | Legend | Analytical semantics/key |

# 15. Actions and Buttons

| **Variant** | **Use** | **Rule** |
|----|----|----|
| Primary | Single main task in current region | Generally one primary action per major panel |
| Secondary | Alternative non-destructive action | May coexist with primary |
| Tertiary | Low-emphasis utility action | Text/ghost style |
| Danger | Destructive/irreversible action | Red semantic reserved for destructive actions; confirmation often required |
| High-impact approval | Approve dissemination/review | Visually explicit; label names consequence, e.g. “Approve for dissemination” |

- Ambiguous labels such as “OK” SHALL NOT be used for consequential actions.

- Buttons that create irreversible or externally visible effects SHALL describe the effect.

- Primary button styling SHALL NOT be used to nudge users toward an adverse analytical conclusion.

- Approval and rejection controls SHOULD be visually balanced where human judgement is required.

# 16. Forms and Data Entry Components

| **Rule** | **Requirement** |
|----|----|
| Labels | Persistent labels above/adjacent to controls; placeholder is not a label. |
| Required fields | Mark explicitly; do not rely on color. |
| Helper text | Use for methodology or format constraints; keep concise. |
| Validation | Inline, specific, and linked to the field; retain user input. |
| Unknown values | Provide explicit Unknown / Not assessed option where domain model allows it. |
| Confidence/status | Use controlled values plus rationale field where required. |
| Entity references | Show object type + canonical name + stable ID/context disambiguator. |
| Evidence links | Use searchable/picker components with provenance preview. |
| Long analysis | Use autosave/version-aware editor with visible save/conflict state. |

# 17. Data Tables and Registers

Tables are a primary professional workspace and SHALL support dense information without losing state semantics or accessibility.

- Header row is visually distinct and programmatically identified.

- Column widths follow content importance; narrative columns receive more space than short statuses.

- Sorting state is explicit; default sort is documented per screen.

- Filters appear as removable chips/tokens and reflect current query scope.

- Row selection is visually distinct from analytical status.

- Bulk actions SHALL be permission-aware and avoid accidental mass changes.

- Long identifiers MAY truncate visually only if copy/full-value access remains available.

- Critical status or classification SHALL not disappear when horizontal scrolling is required.

| **ID** | **Requirement** |
|----|----|
| DS-009 | Data-grid selection styling SHALL NOT reuse adverse analytical status colors. |
| DS-010 | Tables SHALL expose empty, loading, filtered-empty, error, and partial-data states. |
| DS-011 | Restricted rows SHALL be omitted or represented only according to permission policy; UI SHALL NOT leak existence through pagination/counts when policy prohibits it. |

# 18. Badges, Labels, Alerts, and Banners

## 18.1 Badge classes

| **Class** | **Examples** | **Visual intent** |
|----|----|----|
| Lifecycle | Draft, Active, Closed, Superseded | Operational state |
| Analytical | Claim, Fact, Inference, Disputed, Unknown | Epistemic state |
| Confidence | High, Moderate, Low, Insufficient basis (wire: `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`) | Assessment confidence; Insufficient basis is neutral, not a low level *[v0.1.1 · A09]* |
| Classification | Public, Internal, Sensitive, Restricted, Source-protected (wire: `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`) | Handling requirement *[v0.1.1 · A08]* |
| Review | Needs review, Changes requested, Approved | Workflow state |
| Flow | Direct, Documented, Reconstructed, Hypothetical (wire: `DIRECT`, `DOCUMENTED`, `RECONSTRUCTED`, `HYPOTHETICAL`) | Value-flow epistemics *[v0.1.1 · A09]* |

## 18.2 Banner hierarchy

- Persistent banners are appropriate for classification, supersession, integrity failure, read-only state, and significant access restrictions.

- Warnings SHALL describe the condition and available action; avoid generic “Danger” wording.

- Integrity warnings outrank convenience notices and SHOULD remain until resolved or acknowledged per policy.

- Source-protection banners SHALL avoid unnecessarily naming the protected source.

# 19. Drawers, Inspectors, Modals, and Dialogs

| **Pattern** | **Preferred use** | **Avoid** |
|----|----|----|
| Side inspector | Provenance, evidence, node/edge details while preserving analytical context | Deep multi-step editing |
| Drawer | Secondary workflow with context retained | Critical approval if user cannot review full context |
| Modal | Short bounded decision/input | Long reports or complex evidence analysis |
| Confirmation dialog | Destructive or externally consequential action | Routine saves |
| Full-screen workspace | Graph, value flow, review when spatial context is primary | Simple record editing |

# 20. Evidence and Provenance Components

Evidence/provenance components are first-class design-system elements, not feature-specific decorations.

| **Component** | **Mandatory visible elements** |
|----|----|
| Evidence citation | Evidence ID or concise label; source; precise location/page/region; open action |
| Original/derivative marker | Original vs OCR/translation/extract/processed; parent link |
| Integrity block | Hash status; acquisition timestamp; verification state where relevant |
| Provenance trail | Source → Evidence → Extract → Fact/Indicator → Assessment links as permitted |
| Reliability/credibility | Separate source reliability and information credibility controls |
| Protected-source reference | Safe alias/opaque reference; no unnecessary identity exposure |

> **Evidence visibility rule**
>
> The system SHOULD make it easier to inspect evidence than to copy an unsupported allegation. Analytical statements without required provenance should appear incomplete, not polished.

# 21. Review and Dissemination Components

- Review panel SHALL show product version, author, reviewer, classification, unresolved comments, and decision state.

- Approval controls SHALL not visually privilege approval over request-changes/reject where policy requires independent judgement.

- External dissemination screens SHALL expose recipient, purpose, version, classification, minimisation/redaction state, and restrictions before final confirmation.

- Export preview SHALL visually distinguish included, excluded, and redacted material.

- Sharing-log entries are read-only after finalization for ordinary analyst roles.

| **ID** | **Requirement** |
|----|----|
| DS-012 | High-impact approval components SHALL state the consequence in the action label. |
| DS-013 | Export/dissemination confirmation SHALL display the exact product version and intended recipient/purpose. |
| DS-014 | Redacted or excluded material SHALL be perceptibly different in preview without exposing protected content. |

# 22. Classification and Security Visuals

| **Classification** | **Reference treatment** | **Notes** |
|----|----|----|
| PUBLIC | Neutral/low emphasis | No implication of low evidentiary value |
| INTERNAL | Blue-gray label | Internal handling |
| SENSITIVE | Amber-outline label | Attention to handling, not suspicion |
| RESTRICTED | Strong amber/brown label + lock icon/text | Need-to-know handling |
| SOURCE_PROTECTED (display: Source-protected) | Distinct shield/lock label; minimal detail | Identity compartmentalisation; avoid source name *[v0.1.1 · A08]* |

- The five levels above are the authoritative classification model (Data Model §16), ordered least to most restrictive; the first column shows wire values. Access labels (purpose, jurisdiction, embargo, legal-review, compartment, etc.) are additive restrictions shown alongside the level badge, not extra levels. Unknown or missing classification fails closed (access denied, object flagged for classification); where an authorised user can see such an object, it SHALL be shown as an explicit "Classification missing" state, never defaulted to Public or Internal. The legacy Framework v0.1 label "Highly Restricted" is not a level in this model; legacy labels are mapped only through the Data Model migration rule and never automatically to Source-protected. *[v0.1.1 · A08]*

- Classification styling SHALL represent handling requirements, not analytical severity.

- Protected-source state SHALL not be indexed into general-purpose visual components if that leaks existence.

- Permission-denied screens SHALL use non-disclosing copy where policy requires concealment of object existence.

# 23. Responsive and Viewport Baseline

CS-AML is desktop-first because graph, evidence review, and analytical comparison require spatial context. Responsive behaviour must preserve critical tasks rather than merely shrink the desktop layout.

| **Viewport** | **Baseline behaviour** |
|----|----|
| \>=1440 px | Full multi-panel analytical workspace; optional persistent inspector |
| 1024-1439 px | Two-panel workspace; inspector may overlay/drawer |
| 768-1023 px | Stacked panels; analytical canvas remains usable with explicit panel switching |
| \<768 px | Limited/mobile support for review, lookup, simple tasks; complex graph/value-flow authoring MAY be unsupported in MVP |

> **Mobile scope**
>
> MVP responsive support does not require parity for every analytical authoring task. Unsupported complex tasks SHALL fail gracefully with a clear explanation rather than present a misleadingly simplified workflow.

# 24. Accessibility Baseline

The design system SHALL target WCAG 2.2 AA-equivalent accessibility for product UI wherever applicable, with special attention to keyboard use, focus, contrast, color independence, dense tables, graph alternatives, and error recovery. This is a design target, not a conformance claim: no accessibility audit or WCAG conformance evaluation of CS-AML has been performed, and conformance may only be stated once a recorded evaluation of the implemented product exists. *[v0.1.1 · A01; N07]*

| **ID** | **Requirement** |
|----|----|
| DS-015 | Normal text and essential UI controls SHALL meet applicable contrast targets. |
| DS-016 | Every interactive component SHALL be operable by keyboard unless the interaction is inherently spatial, in which case an equivalent accessible path SHALL exist where required. |
| DS-017 | Focus order SHALL follow task order, not visual implementation accident. |
| DS-018 | Graph, timeline, and value-flow views SHALL provide textual/list/table alternatives for material analytical content. |
| DS-019 | Color SHALL NOT be the sole means of conveying value-flow class, confidence, error, classification, or analytical state. |
| DS-020 | Motion SHALL respect reduced-motion preferences and SHALL NOT be required to perceive state changes. |

## 24.1 Minimum target sizes

- Primary pointer targets SHOULD be approximately 40×40 CSS px or larger where practical.

- Compact data-grid controls MAY be smaller when keyboard access and sufficient spacing are preserved.

- Icons used alone as controls require accessible names and tooltips/help where meaning is not universally clear.

# 25. Motion and Transition

- Motion is functional, not decorative.

- Use short transitions for panel expansion, selection, and context preservation.

- Avoid pulsing/flashing “risk” indicators.

- Async completion SHOULD use stable confirmation and not rely only on transient animation.

- Reduced-motion mode SHALL remove non-essential animation.

# 26. Frontend Implementation Conventions

The reference MVP frontend is React + TypeScript + Tailwind CSS 4. The design system SHOULD expose semantic tokens as CSS custom properties and reusable typed components. Raw Tailwind utility combinations SHOULD NOT become de facto component definitions scattered across features.

## 26.1 Reference structure

``` text
frontend/   src/     design-system/       tokens/       components/       patterns/       icons/       styles/       tests/       index.ts     features/       cases/       evidence/       entities/       analysis/       products/
```

## 26.2 CSS variable examples

``` text
--color-text-primary: #16212B; --color-surface-canvas: #F7F9FB; --color-border-default: #D7DEE5; --color-action-primary: #285C8E; --color-state-error: #A13333; --flow-direct-style: solid; --flow-reconstructed-style: dashed;
```

| **ID** | **Requirement** |
|----|----|
| DS-021 | Feature modules SHOULD consume design-system components before creating local equivalents. |
| DS-022 | Design-system components SHALL expose typed variants for analytical/status semantics rather than arbitrary color props. |
| DS-023 | Raw hex values SHOULD NOT appear in feature-level production code except documented exceptional cases. |
| DS-024 | Component accessibility tests SHALL be included in CI for critical components. |
| DS-025 | Breaking component/token changes SHALL follow versioning and migration notes. |

# 27. Component API and Composition Rules

- Prefer semantic props: `state="disputed"`, `flowClass="RECONSTRUCTED"`, `classification="RESTRICTED"` rather than `color="orange"`. Semantic props take the canonical UPPER_SNAKE_CASE wire values; display labels are resolved separately. *[v0.1.1 · A08, A09]*

- Components SHOULD expose slots/composition points for provenance and metadata without requiring feature forks.

- Critical components SHALL support loading, error, empty, read-only, restricted, and disabled states where applicable.

- Component defaults SHALL be safe: destructive variants are opt-in; unrestricted data exposure is never a visual default.

- UI copy belongs to product/feature layer except universal design-system labels such as generic loading/error affordances.

# 28. Design-System Verification

| **Test class** | **Minimum verification** |
|----|----|
| Visual regression | Critical components and analytical states at supported themes/viewports |
| Accessibility | Keyboard, focus, accessible name, semantics, contrast, color independence |
| State coverage | Default/hover/focus/disabled/loading/error/read-only/conflict where applicable |
| Responsive | Critical components at desktop/tablet/mobile baseline |
| Export parity | Value-flow classes and analytical labels survive PDF/screenshot/grayscale checks |
| Semantic consistency | Same domain state maps to same token/component across features |
| Security leakage | Restricted/protected states do not expose hidden labels or counts in shared components |

## 28.1 Component Definition of Done

- Semantic purpose and variants documented.

- Accessible name/role/state behaviour defined.

- Keyboard/focus verified.

- Critical states implemented.

- No feature-specific raw color dependency.

- Visual regression baseline stored.

- Usage example available.

- Relevant analytical/provenance semantics tested.

- No contradiction with UX/IA/wireframe specifications.

# 29. Design-System Governance

The design system is a shared product asset. Visual changes that alter analytical meaning or safety require domain review; purely cosmetic changes still require accessibility and consistency review.

| **Change type** | **Required review** |
|----|----|
| New primitive token | Design-system owner |
| New semantic token | Design-system owner + UX |
| New analytical token/state | UX + domain/methodology owner + frontend |
| New reusable component | UX/design + frontend + accessibility/QA |
| Breaking visual semantic change | Product + UX + domain + QA; migration note |
| One-off feature override | Discouraged; justification required |

## 29.1 Versioning

- v0.x may evolve while MVP is under active design, but analytical semantics require explicit change records.

- Removed tokens/components SHALL have a migration path where production usage exists.

- Component and token changelog SHOULD be maintained in repository documentation.

- Screen-specific visual exceptions SHOULD be documented rather than silently diverging.

# 30. Traceability to CS-AML Product Surfaces

| **Design-system domain** | **Primary dependent screens/patterns** |
|----|----|
| Forms/actions | Case charter, source/evidence registration, entity/relationship editing, assessment |
| Data grids | Cases, entities, evidence, products, sharing log, admin registers |
| Evidence/provenance | Evidence Reader, Entity Detail, Assessment, Product Editor, Review |
| Analytical semantics | Value Flow Workspace, Timeline, Hypothesis Matrix, Investigation Graph |
| Review/dissemination | Peer Review Workspace, Dissemination Approval, Export Builder |
| Security/classification | All canonical detail screens, source-protected flows, exports |
| System states | Access denied, edit conflict, integrity warning, async processing |

# Annex A — MVP Semantic Token Baseline

| **Token**                   | **Baseline** | **Meaning**                 |
|-----------------------------|--------------|-----------------------------|
| color.text.primary          | \#16212B     | Primary readable content    |
| color.text.secondary        | \#5E6B75     | Secondary metadata          |
| color.surface.canvas        | \#F7F9FB     | Application canvas          |
| color.surface.panel         | \#FFFFFF     | Panel/card surface          |
| color.border.default        | \#D7DEE5     | Default border              |
| color.action.primary        | \#285C8E     | Primary action              |
| color.state.success         | \#246B4A     | Operational success         |
| color.state.warning         | \#8A5A00     | Attention/review            |
| color.state.error           | \#A13333     | Error/destructive           |
| color.analytical.construct  | \#5B4B8A     | Hypothesis/inference        |
| color.analytical.documented | \#236A73     | Documented analytical state |
| focus.ring                  | \#285C8E     | Keyboard focus ring         |
| space.base                  | 4 px         | Spacing scale base          |
| radius.default              | 8 px         | Default panels/controls     |

These values are a reference implementation baseline. Semantic meaning is normative; exact primitive hues MAY change if contrast, branding, or implementation requirements demand it, provided domain semantics remain stable.

# Annex B — Analytical Legend Baseline

| **Concept** | **Required non-color cue** | **Recommended visual family** |
|----|----|----|
| Claim | Text label “Claim” | Neutral outline |
| Fact | Text label “Fact” | Strong neutral/blue |
| Inference | Text label “Inference” | Purple outline |
| Disputed | Text label “Disputed” + icon/pattern | Amber |
| Unknown | Text label “Unknown” + dashed treatment | Gray |
| DIRECT flow | DIRECT label + solid line | Neutral/blue |
| DOCUMENTED flow | DOCUMENTED label + distinct solid line | Cyan |
| RECONSTRUCTED flow | RECONSTRUCTED label + dashed line | Purple/neutral |
| HYPOTHETICAL flow | HYPOTHETICAL label + dotted line | Gray/purple |
| Restricted classification | Text + lock symbol | Amber/brown |
| Source-protected (`SOURCE_PROTECTED`) | Text + shield/lock symbol | Distinct secure treatment *[v0.1.1 · A08]* |

# Annex C — UI Design Review Checklist

- Does the screen use canonical design-system components where available?

- Are proposition, confidence, flow, classification, and review states semantically correct?

- Does any color, icon, size, ranking, or animation imply guilt or suspicion without methodological basis?

- Can critical meaning be understood without color?

- Are focus, keyboard, error, loading, empty, read-only, conflict, and permission states addressed?

- Are provenance and evidence links visually inspectable where decisions depend on them?

- Do graphs/timelines/value-flow views provide legends and accessible alternatives?

- Do destructive or external actions state their consequence?

- Are compact/dense layouts still readable and accessible?

- Will the visual semantics survive screenshot/PDF/grayscale export?

- Does the implementation use semantic tokens instead of feature-specific raw values?

- Has the change been checked against UX, IA, Screen Inventory, and Wireframe specifications?

# Annex D — UI Design System Handoff Contract

| **Discipline** | **Owns** | **Consumes from UI DS** |
|----|----|----|
| UX | Task flow, interaction behaviour, feedback, safety | Components, states, semantic visual tokens |
| Information Architecture | Navigation, hierarchy, taxonomy, labels | Component affordances and state presentation |
| Frontend Engineering | Implementation, component APIs, rendering | Tokens, component contracts, accessibility rules |
| QA / Accessibility | Verification | Expected variants/states and test requirements |
| Domain / Methodology | Analytical meaning | Visual mappings for epistemic/provenance states |
| Product | Scope/priorities | Reusable patterns and readiness evidence |

## Final release rule

UI completion requires correct semantic tokens/components, preserved analytical meaning, critical accessibility, required states, and consistency with the UX and IA specifications.

**CS-AML**

**Component Inventory & Storybook  
Implementation Specification**

Version 0.1.1

> **Document status — v0.1.1**
> Version: 0.1.1 — Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec). *[v0.1.1 · A01]*
> Supersedes: CS-AML Component Inventory & Storybook Implementation Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: approved by the product owner as the internal specification baseline on 2026-10-08 (decision register and release gates in `CHANGELOG.md`). No implementation test result or independent audit exists yet. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Implementation axiom**  
> A UI component SHALL encode reusable visual and interaction semantics, not feature-specific assumptions. Storybook SHALL make those semantics inspectable, testable, accessible, and regression-safe before components are composed into production screens.

| **Field** | **Value** |
|----|----|
| Document ID | CSAML-CISB-0.1 |
| Version | 0.1.1 |
| Status | Approved Internal Specification Baseline (2026-10-08, tag v0.1.1-spec) — frontend implementation baseline for MVP 0.1 *[v0.1.1 · A01]* |
| Primary owners | Frontend Engineering / Design System Engineering |
| Inputs | UX, IA, Screen Inventory, Wireframe, UI Design System, High-Fidelity UI |
| Primary output | Reusable component library + Storybook contract + testable component documentation |

# 1. Purpose and Scope

This specification defines the reusable CS-AML frontend component inventory and the Storybook implementation contract for MVP 0.1. It is the implementation bridge between the UI specifications (draft for review) and production React code. *[v0.1.1 · A01]* It defines component boundaries, ownership, variants, accessibility expectations, stories, testing, visual regression, documentation, and release criteria.

> **Boundary**  
> This document does not redefine screen navigation, workflow, wireframe composition, or visual semantics. Those remain governed by IA, UX, Wireframe, UI Design System, and High-Fidelity UI specifications. This document converts those decisions into reusable frontend implementation units.

# 2. Objectives

- Prevent feature teams from recreating near-duplicate controls and analytical visuals.

- Make uncertainty, provenance, review state, permission state, and value-flow epistemics reusable rather than screen-specific.

- Provide a single inspectable catalogue for designers, frontend engineers, QA, accessibility review, and product review.

- Support isolated accessibility and interaction testing before components are integrated into full screens.

- Enable visual regression detection for design-system changes.

- Maintain screen-to-component traceability for critical MVP screens.

# 3. Component Architecture

| **Layer** | **Purpose** | **Dependency rule** |
|----|----|----|
| Foundation | Tokens, typography, surfaces, icon wrapper, layout primitives | May depend only on framework/runtime and token definitions. |
| General UI | Reusable controls and generic states | May depend on Foundation; SHALL NOT import domain feature modules. |
| Analytical / Domain | CS-AML semantic components | May depend on Foundation + General UI; SHALL expose analytical semantics explicitly. |
| Compound Patterns | Reusable page/workspace compositions | May depend on all shared components; SHALL remain feature-agnostic enough to support multiple screens. |
| Feature Screens | Route-specific composition and data binding | Consumes shared components; new local primitives require design-system review. |

**CISB-001 —** Feature modules SHALL consume shared design-system components before introducing local equivalents.

**CISB-002 —** A shared component SHALL NOT encode business-specific API calls or permission decisions internally unless the component is explicitly an authorization-aware system component.

**CISB-003 —** Analytical semantics such as Fact, Inference, Confidence, DIRECT, or RECONSTRUCTED SHALL be represented through typed component variants rather than arbitrary CSS classes.

# 4. Naming and Package Conventions

| **Concern** | **Convention** |
|----|----|
| Component IDs | Stable inventory IDs: FND-###, GEN-###, ANA-###, CMP-###. |
| React names | PascalCase and semantic: EvidenceCitation, FlowClassBadge, ReviewDecisionPanel. |
| Files | ComponentName.tsx, ComponentName.stories.tsx, ComponentName.test.tsx, ComponentName.types.ts. |
| Exports | Public exports through package barrel; internal helpers remain private. |
| Variants | Typed unions/enums; avoid free-form string variant names. |
| Styling | Semantic tokens/CSS variables + shared Tailwind mappings; no feature-specific raw hex where semantic token exists. |
| Events | Intent-oriented names: onApprove, onResolve, onOpenEvidence; not onButtonClick. |
| Data | Presentational components receive explicit view models; canonical API response shape SHOULD NOT leak directly into low-level components. |

# 5. Component Inventory

The MVP baseline contains 65 shared components across foundation, general, analytical/domain, and compound pattern layers.

> The 65 component IDs below are implementation requirements. They are not evidence that any component has been built, and no Storybook, interaction-test, axe or visual-regression results exist for CS-AML at this baseline. *[v0.1.1 · A01; N07]*

## Foundation components

| **ID** | **Component** | **Priority** | **Purpose** | **Primary usage** | **Semantic owner** |
|----|----|----|----|----|----|
| FND-001 | Semantic Token Provider | P0 | CSS variable/theme provider | All | DS tokens |
| FND-002 | Icon | P0 | Accessible icon wrapper | All | iconography |
| FND-003 | Text | P0 | Typography primitive with semantic variants | All | typography |
| FND-004 | Stack / Inline | P0 | Spacing/layout primitives | All | spacing |
| FND-005 | Surface | P0 | Canvas/panel/elevated surface | All | surface tokens |

## General components

| **ID** | **Component** | **Priority** | **Purpose** | **Primary usage** | **Semantic owner** |
|----|----|----|----|----|----|
| GEN-001 | Button | P0 | Primary/secondary/quiet/destructive actions | All | action semantics |
| GEN-002 | IconButton | P0 | Compact labelled action | All | action semantics |
| GEN-003 | Link | P0 | Internal/external navigation link | All | navigation |
| GEN-004 | TextInput | P0 | Single-line text field | Forms | form controls |
| GEN-005 | TextArea | P0 | Long-form input. `rationale` variant (required, with guidance text) used for decision rationale on verification, resolution and review decisions (HiFi "RationaleField") *[v0.1.1 · C17]* | Editors | form controls |
| GEN-006 | Select | P0 | Controlled vocabulary selection | Forms | form controls |
| GEN-007 | Combobox | P0 | Search/select canonical object or term | Forms | findability |
| GEN-008 | Checkbox | P0 | Independent binary selection | Forms | form controls |
| GEN-009 | RadioGroup | P0 | Mutually exclusive selection | Forms | form controls |
| GEN-010 | Switch | P1 | Immediate reversible setting | Admin | form controls |
| GEN-011 | DatePrecisionField | P0 | Exact/month/year/range/unknown dates | Timeline | temporal semantics |
| GEN-012 | CurrencyValueField | P0 | Known/range/approximate/unknown values | Value Flow | value semantics |
| GEN-013 | Badge | P0 | Compact non-interactive semantic label | All | status |
| GEN-014 | Chip | P0 | Removable/filter/token item | Search/filters | filters |
| GEN-015 | Alert | P0 | Inline message with severity | All | feedback |
| GEN-016 | Toast | P0 | Transient action feedback | All | feedback |
| GEN-017 | Modal | P0 | Blocking confirmation/dialog | All | high-impact action |
| GEN-018 | Drawer | P0 | Context/inspector panel | Analytical | context |
| GEN-019 | Tabs | P0 | Local subnavigation | Object pages | local navigation |
| GEN-020 | Breadcrumbs | P0 | Context path/deep-link cue | Object pages | navigation |
| GEN-021 | DataTable | P0 | Sortable/faceted permission-aware table | Registers | data dense |
| GEN-022 | Pagination | P0 | Paged large result navigation | Registers/Search | navigation |
| GEN-023 | FilterBar | P0 | Filters/facets/query chips | Registers/Search | findability |
| GEN-024 | EmptyState | P0 | No-data/no-result guidance | All | states |
| GEN-025 | LoadingState | P0 | Skeleton/progress state | All | states |
| GEN-026 | AccessDeniedState | P0 | Non-disclosing permission denial | System | security |
| GEN-027 | IntegrityWarningState | P0 | Evidence integrity mismatch warning | Evidence | security |
| GEN-028 | ConflictState | P0 | Stale/concurrent edit conflict ("record changed"): shown when the API returns 412 PRECONDITION_FAILED (stale If-Match, or a stale `expected_versions` entry on merge/unmerge/resolution decisions); a 409 STATE_CONFLICT is a workflow-state error, not this state. Multi-entity variant lists every entity in `details.current_record_versions` that changed, with reload/re-confirm per entity *[v0.1.1 · C03]* | Editors | versioning *[v0.1.1 · A04]* |

## Analytical components

| **ID** | **Component** | **Priority** | **Purpose** | **Primary usage** | **Semantic owner** |
|----|----|----|----|----|----|
| ANA-001 | AnalyticalStateBadge | P0 | Claim/Fact/Inference/Candidate/Disputed/Unknown; a claim never receives the Fact variant without a recorded verification decision. Status variants for every `claim_status` (RECORDED, UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED) and `fact_status` (PROVISIONAL, ESTABLISHED, DISPUTED, SUPERSEDED) wire value, plus a `review-required` variant for Assessments/IntelligenceProducts flagged `review_required` (links to `review_trigger_ref`) *[v0.1.1 · C17]* | Analysis | uncertainty *[v0.1.1 · A10]* |
| ANA-002 | ConfidenceBadge | P0 | Controlled confidence label + rationale affordance; variants `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS` (neutral, not adverse, not rendered as Low) | Assessment | confidence *[v0.1.1 · A09]* |
| ANA-003 | FlowClassBadge | P0 | `flow_class` variants DIRECT/DOCUMENTED/RECONSTRUCTED/HYPOTHETICAL (wire values) | Value Flow | epistemic class *[v0.1.1 · A09]* |
| ANA-004 | EvidenceCitation | P0 | Canonical evidence citation with location | Evidence/Product | provenance |
| ANA-005 | ProvenanceTrail | P0 | Source→Evidence→Derivative lineage summary. `decision-history` variant: append-only, chronological list of VerificationDecisions (claims/facts) or ResolutionDecisions (entities) with decision, rationale, evidence, decided_by and decided_at; no edit/delete affordance *[v0.1.1 · C17]* | Evidence | provenance |
| ANA-006 | SourceRating | P0 | A-F reliability display/input | Source | source evaluation |
| ANA-007 | CredibilityRating | P0 | 1-6 information credibility | Claims | information evaluation |
| ANA-008 | EntitySummaryCard | P0 | Canonical identity summary without accusation | Entity | identity |
| ANA-009 | RelationshipSummary | P0 | Typed evidence-backed relationship summary | Entity/Graph | relationship |
| ANA-010 | AssetAttribution | P0 | Ownership/control/use attribution display | Asset | asset attribution |
| ANA-011 | TemporalPrecision | P0 | Exact/approx/range/unknown date cue | Timeline | temporal semantics |
| ANA-012 | EvidenceInspector | P0 | Evidence/provenance/context rail | Evidence/Analysis | provenance |
| ANA-013 | GraphNode | P0 | Neutral canonical-object node | Graph | graph semantics |
| ANA-014 | GraphEdge | P0 | Evidence-backed relationship/value-flow edge | Graph | graph semantics |
| ANA-015 | GraphLegend | P0 | Visible relationship/flow semantics | Graph | legend |
| ANA-016 | TimelineItem | P0 | Evidence-linked event item | Timeline | chronology |
| ANA-017 | HypothesisCard | P0 | Hypothesis state, rationale and evidence balance | Hypothesis | reasoning |
| ANA-018 | EvidenceBalanceMatrix | P0 | Support/contradict/neutral/unknown matrix | Hypothesis | reasoning |
| ANA-019 | IntelligenceGapItem | P0 | Explicit unknown/gap display | Assessment | uncertainty |
| ANA-020 | TypologyMatchPanel | P0 | Indicators/counter-indicators/alternatives | Typology | typology caution |
| ANA-021 | AssessmentSummary | P0 | Judgement, confidence, basis, gaps | Assessment | assessment |
| ANA-022 | ReviewDecisionPanel | P0 | Comment/request changes/approve/reject | Review | review |
| ANA-023 | ClassificationBanner | P0 | Handling/classification context; variants `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED` (display: Public, Internal, Sensitive, Restricted, Source-protected) plus access-label slots; the compact classification badge is the GEN-013 Badge with the same five variants | All sensitive | security *[v0.1.1 · A08]* |
| ANA-024 | ProtectedSourceMarker | P0 | Authorized protected-source presence indicator without identity leak | Source | source protection |

## Compound components

| **ID** | **Component** | **Priority** | **Purpose** | **Primary usage** | **Semantic owner** |
|----|----|----|----|----|----|
| CMP-001 | RegisterPageFrame | P0 | Header + filters + DataTable + pagination | Registers | WF-PAT-01 |
| CMP-002 | CanonicalObjectHeader | P0 | Object identity/status/classification/actions | Object detail | WF-PAT-02 |
| CMP-003 | ObjectDetailFrame | P0 | Context header + tabs + main + inspector | Object detail | WF-PAT-02 |
| CMP-004 | EditorFrame | P0 | Form sections + validation + action footer | Editors | WF-PAT-03 |
| CMP-005 | AnalyticalWorkspaceFrame | P0 | Toolbar + canvas + inspector + accessible alternative | Analysis | WF-PAT-04 |
| CMP-006 | CompareResolutionFrame | P0 | Symmetric A/B comparison + differences + decision. Slots: compare columns (HiFi "CompareColumn"), matching/conflicting attribute signals (HiFi "MatchSignal"/"ConflictSignal", rendered with GEN-013 Badge), decision rail (HiFi "MergeDecisionPanel"; records a ResolutionDecision MERGE, KEEP_SEPARATE, POSSIBLE_MATCH or DEFER with GEN-005 `rationale`) *[v0.1.1 · C17]* | Entity match | WF-PAT-05 |
| CMP-007 | ReviewApprovalFrame | P0 | Artifact + review panel + decision controls | Review | WF-PAT-06 |
| CMP-008 | SystemStateFrame | P0 | Safe failure/permission/integrity state | System | WF-PAT-07 |

# 6. Component API Contract

**CISB-010 —** All public components SHALL define explicit TypeScript props and SHALL avoid `any` in public interfaces.

**CISB-011 —** Status and analytical variants SHALL use controlled typed values aligned to normative vocabularies. Variant values are the canonical UPPER_SNAKE_CASE wire values from the Data Model Annex A registry; display labels are resolved separately and are translatable. *[v0.1.1 · A09]*

**CISB-012 —** Components that render canonical objects SHOULD accept stable IDs/links separately from display labels so canonical navigation remains explicit.

**CISB-013 —** Components rendering restricted content SHALL support redacted/withheld states without leaking hidden metadata through tooltips, DOM labels, or story fixtures.

**CISB-014 —** Destructive or high-impact actions SHALL expose disabled, pending, success, failure, and confirmation states where applicable.

**CISB-015 —** Components SHALL permit accessible names independent from visible iconography or abbreviated labels.

**CISB-016 —** Loading state SHALL not erase surrounding context needed to understand which object is loading.

# 7. Accessibility Contract

| **Component class** | **Mandatory accessibility behavior** |
|----|----|
| Buttons/actions | Keyboard operable; visible focus; accessible name; disabled vs aria-disabled used intentionally. |
| Dialogs/drawers | Focus trap where blocking; focus restoration; labelled title; Escape behavior where safe. |
| Tables | Semantic headers; keyboard/screen-reader discoverable sort state; no permission leak in hidden rows. |
| Tabs | ARIA tab semantics or equivalent; roving focus; current state announced. |
| Forms | Programmatic label, help, error association; required state not color-only. |
| Graph/timeline/value flow | Accessible alternative list/table preserving equivalent analytical semantics. |
| Analytical states | Color-independent icon/pattern/text label for Claim/Fact/Inference etc. |
| Flow classes | Line pattern + text/legend; not color-only. |
| Toast/alerts | Appropriate live-region priority; avoid repeated noisy announcements. |
| Protected content | Accessible text SHALL not reveal information withheld visually. |

**CISB-020 —** Storybook accessibility checks SHALL be required for P0 interactive shared components.

# 8. Storybook Architecture

> **Storybook purpose**  
> Storybook is the executable catalogue of component semantics. It SHALL serve design review, engineering documentation, accessibility review, interaction testing, visual regression, and reference composition. It is not merely a gallery of default states.

| **Storybook group** | **Coverage** | **Required story emphasis** |
|----|----|----|
| Foundations | Tokens, typography, surfaces, icons | Docs only + smoke stories |
| General/Actions | Button, IconButton, Link | Variants, disabled, loading, keyboard |
| General/Forms | Inputs, select, combobox, dates, values | Default, error, disabled, readonly, long content |
| General/Data Display | Badge, chip, table, pagination | Dense, empty, long values, permission-filtered |
| General/Feedback | Alert, toast, modal, drawer | Severity, focus trap, dismissal, async action |
| Analytical/Provenance | Citation, provenance, evidence inspector | Complete/missing/restricted/derivative |
| Analytical/Uncertainty | State badge, confidence, gaps | All epistemic states + accessible labels |
| Analytical/Entity | Entity card, relationship, asset attribution | Normal/conflicting/disputed/unknown |
| Analytical/Value Flow | Flow badge, edge, legend, value field | All four classes, grayscale, long chain |
| Analytical/Reasoning | Hypothesis, evidence matrix, typology, assessment | Support/contradiction/unknown/reviewed |
| Analytical/Review | Review panel, classification, protected-source marker | Pending/change/approved/rejected/restricted |
| Patterns | Register/Object/Editor/Workspace/Compare/Review/System | Reference composition stories |

# 9. Required Story Set Per Component

| **Story** | **Requirement** |
|----|----|
| Default | Representative normal state with realistic but synthetic safe fixture data. |
| Variants | Every public semantic variant, including all analytical states. |
| Interactive | User-visible interaction tested via play function where meaningful. |
| Keyboard | Focus order and keyboard operation demonstrated for complex interactive components. |
| Error / invalid | Validation or failure state where applicable. |
| Loading / pending | Async state where applicable. |
| Empty / unknown | Unknown and missing data distinct from zero/false. |
| Readonly / approved | Immutable/read-only state where applicable. |
| Restricted | Permission-safe withheld state for security-sensitive components. |
| Long content | Long names, identifiers, citations, translations, and wrapped labels. |
| Narrow viewport | Component behavior under constrained width. |
| High contrast / grayscale | Critical analytical semantics remain understandable without normal color perception. |

**CISB-030 —** A P0 component is not Storybook-complete if only a default happy-path story exists.

**CISB-031 —** Fixtures SHALL be synthetic and SHALL NOT include protected-source identities or copied sensitive production evidence.

# 10. Critical Analytical Story Matrices

## AnalyticalStateBadge

- Claim

- Fact

- Inference

- Candidate

- Disputed

- Unknown

- With icon hidden (a11y name preserved)

- Grayscale

## FlowClassBadge / GraphEdge

- DIRECT

- DOCUMENTED

- RECONSTRUCTED

- HYPOTHETICAL

- Mixed flow legend

- Grayscale/print

- Unknown amount

- Range amount

## ConfidenceBadge *[v0.1.1 · A09]*

- High (`HIGH`)

- Moderate (`MODERATE`)

- Low (`LOW`)

- Insufficient basis (`INSUFFICIENT_BASIS`) — neutral treatment, visibly not a level below Low

- Not yet assessed (draft, null level) — distinct from Insufficient basis

- Rationale expanded / collapsed

- Grayscale

## ClassificationBanner / classification Badge *[v0.1.1 · A08]*

- Public (`PUBLIC`)

- Internal (`INTERNAL`)

- Sensitive (`SENSITIVE`)

- Restricted (`RESTRICTED`)

- Source-protected (`SOURCE_PROTECTED`) — no source identity in label, tooltip or DOM

- With additive access labels (e.g. embargo, legal-review)

- Classification missing (fail-closed state)

- Grayscale

## EvidenceCitation

- Page citation

- Paragraph citation

- Region citation

- Derivative citation

- Restricted evidence

- Missing parent warning

- Very long title

## EntitySummaryCard

- Person

- Company

- Organization

- Wallet

- Disputed identity

- Unresolved identity

- Long aliases

- Restricted identifiers

## EvidenceBalanceMatrix

- Balanced

- Support-heavy

- Contradiction-heavy

- Unknown-heavy

- No evidence

- Keyboard navigation

## ReviewDecisionPanel

- Pending

- Changes requested

- Approved

- Rejected

- Self-approval blocked

- Saving

- Permission denied

# 11. Testing Strategy

| **Test layer** | **Tooling expectation** | **Scope** |
|----|----|----|
| Type/static | TypeScript + lint | Public props, enum exhaustiveness, import boundaries. |
| Unit | Vitest/Jest equivalent | Pure rendering logic, formatting, variant mapping. |
| Interaction | Storybook test/play + Testing Library | Keyboard, click, validation, dialogs, menus, async states. |
| Accessibility | axe integration + manual keyboard/screen-reader checks | P0 shared components and critical compound patterns. |
| Visual regression | Chromatic/Percy/self-hosted equivalent | Stable stories at reference viewports, especially analytical semantics. |
| Integration | Application test suite | Data binding, permissions, routing, server-side authorization. |
| E2E | Playwright/equivalent | Critical user journeys across composed screens. |

**CISB-040 —** Visual regression approval SHALL require semantic review when a change affects analytical-state, confidence, provenance, classification, or value-flow presentation.

**CISB-041 —** A pixel-diff approval SHALL NOT override a normative semantic violation.

# 12. Storybook Viewport Baseline

| **Viewport** | **Reference** | **Use** |
|----|----|----|
| Desktop review | 1440 × 900 | Primary high-fidelity composition and data-density review. |
| Laptop | 1280 × 800 | Constrained desktop and common field laptop. |
| Tablet landscape | 1024 × 768 | Collapsed secondary rails and adaptive analytical workspaces. |
| Narrow | 768 px wide | Stacking behavior and essential task preservation. |
| Component intrinsic | Auto/min-content/max-content | Atomic component resilience to label/data length. |

# 13. Story Documentation Requirements

- Purpose and when to use / when not to use.

- Public props and semantic variants.

- Accessibility notes and keyboard behavior.

- Content rules and prohibited uses.

- Relevant normative references (UX/UI/IA/High-Fidelity/Screen IDs).

- Known limitations.

- Examples of correct and incorrect semantic usage for high-risk analytical components.

# 14. Critical Screen-to-Component Traceability

| **Screen ID** | **Screen** | **Mandatory shared component baseline** |
|----|----|----|
| SCR-EVD-003 | Evidence Reader | CMP-003, ANA-004, ANA-005, ANA-012, ANA-023 |
| SCR-ENT-003 | Entity Detail | CMP-003, CMP-002, ANA-008, ANA-009, ANA-010 |
| SCR-ENT-005 | Entity Match Compare | CMP-006, ANA-008, ANA-004, ANA-001 |
| SCR-TIM-001 | Timeline | CMP-005, ANA-016, ANA-011, ANA-012 |
| SCR-VAL-001 | Value Flow Workspace | CMP-005, ANA-003, ANA-014, ANA-015, GEN-012 |
| SCR-TYP-002 | Typology Match | CMP-005, ANA-020, ANA-004, ANA-019 |
| SCR-HYP-001 | Hypothesis Workspace | CMP-005, ANA-017, ANA-018, ANA-019 |
| SCR-ASM-001 | Assessment Draft | CMP-004, ANA-021, ANA-002, ANA-019 |
| SCR-GRF-001 | Investigation Graph | CMP-005, ANA-013, ANA-014, ANA-015, ANA-012 |
| SCR-PRD-003 | Product Editor | CMP-004, ANA-004, ANA-001, ANA-021, ANA-023 |
| SCR-REV-002 | Peer Review | CMP-007, ANA-022, ANA-021, ANA-004, ANA-023 |
| SCR-DIS-002 | Export Package Builder | CMP-005, ANA-023, ANA-004, GEN-008, GEN-017 |

**CISB-050 —** Critical screens SHALL reference shared component IDs in frontend implementation notes or equivalent engineering documentation.

# 15. Reference Repository Structure

``` text
frontend/
  src/
    design-system/
      foundations/
      components/
        general/
        analytical/
        patterns/
      tokens/
      icons/
      index.ts
    features/
      cases/
      evidence/
      entities/
      analysis/
      products/
      administration/
  .storybook/
    main.ts
    preview.ts
    manager.ts
  stories/ (optional docs-only compositions)
  tests/
```

**CISB-060 —** Feature packages SHALL NOT deep-import private component implementation files; only public design-system exports are supported contracts.

# 16. Component Lifecycle and Governance

| **State** | **Meaning** |
|----|----|
| Proposed | Need identified; API not stable. |
| Experimental | Usable in limited feature work; change without migration guarantee. |
| Stable | Approved public API and Storybook/test coverage. |
| Deprecated | Replacement exists; migration guidance required. |
| Retired | Removed from public exports after approved migration window. |

**CISB-070 —** Breaking changes to Stable component APIs SHALL require migration notes and release-note entry.

**CISB-071 —** Changes to analytical semantic components SHALL be reviewed by UX/design-system owner and a domain/framework owner.

**CISB-072 —** A component SHOULD be promoted to shared inventory when two or more screens need the same semantic behavior, or immediately when the behavior is safety/security critical.

# 17. CI/CD and Storybook Publication

- Build Storybook on every pull request affecting frontend/design-system code.

- Run typecheck, lint, unit/interaction tests, and automated accessibility checks.

- Publish ephemeral preview for reviewer access.

- Run visual regression against approved baseline for changed stories.

- Block merge on failed mandatory checks unless a documented exception is approved.

- Publish versioned Storybook for release candidates; production deployment need not expose it publicly.

# 18. Security and Privacy in Storybook

**CISB-080 —** Storybook fixtures SHALL contain only synthetic or explicitly approved non-sensitive data.

**CISB-081 —** Storybook builds SHALL NOT embed production API tokens, production endpoints requiring credentials, or real protected-source identities.

**CISB-082 —** Authorization behavior MAY be simulated through safe decorators/fixtures, but Storybook SHALL NOT be treated as proof of server-side authorization. Restricted or permission-denied stories demonstrate rendering only; authorization SHALL be verified by server-side policy tests. *[v0.1.1 · A01]*

**CISB-083 —** Private deployment or access control SHOULD be used when Storybook documentation contains internal security architecture details.

# 19. Component Definition of Done

- [ ] Inventory ID and semantic owner assigned.

- [ ] Public TypeScript API documented.

- [ ] Uses semantic tokens and approved icons.

- [ ] Default + all required variants implemented.

- [ ] Unknown/empty/error/loading/readonly/restricted states implemented where applicable.

- [ ] Keyboard behavior verified.

- [ ] Automated accessibility check passes for supported state set.

- [ ] Storybook stories complete.

- [ ] Interaction tests present for meaningful behaviors.

- [ ] Visual-regression baseline approved for P0/critical analytical components.

- [ ] No sensitive fixture data.

- [ ] Relevant screen IDs and normative references documented.

- [ ] No duplicate local implementation exists in target feature module.

# 20. Storybook Release Gate

> **MVP Storybook gate**  
> Before MVP UI freeze, every P0 shared component used by the critical end-to-end scenario SHALL have an approved Storybook entry, required state coverage, accessibility checks, and visual-regression baseline. Missing Storybook coverage for a critical analytical semantic component is a release-quality defect, not merely documentation debt.

# Annex A — Minimum Story Coverage by Priority

| **Priority** | **Minimum** |
|----|----|
| P0 | Default, all variants, key interaction, error/unknown/restricted where applicable, accessibility, critical viewport, visual baseline. |
| P1 | Default, all public variants, basic accessibility, key interaction; visual baseline recommended. |
| P2 | Default and public variants; additional test/story coverage before promotion to production-critical use. |

# Annex B — Story Naming Convention

> **Canonical format**  
> `\<Group\>/\<Subgroup\>/\<Component\>` for title; stories use clear state names such as `Direct`, `Reconstructed`, `RestrictedEvidence`, `KeyboardNavigation`, or `LongContent`. Avoid `Example1`, `Test`, and ambiguous names.

# Annex C — Pull Request Review Checklist

- [ ] Component belongs in shared library rather than local feature code.

- [ ] No normative semantic is implemented with raw color alone.

- [ ] Public props are typed and minimal.

- [ ] Story set covers non-happy-path states.

- [ ] Keyboard and focus behavior checked.

- [ ] axe violations resolved or documented with approved rationale.

- [ ] Synthetic fixtures only.

- [ ] Visual diffs reviewed semantically.

- [ ] Screen traceability updated if usage changes.

- [ ] Breaking API changes include migration notes.

# CS-AML UI Design System Specification v0.1

**Status:** Normative UI design-system baseline for MVP 0.1

## Design-system axiom
The visual system SHALL communicate analytical state, provenance, uncertainty, permission, review status, and operational risk without implying guilt, suspicion, certainty, or importance merely through visual prominence.

## Scope
Defines design tokens, typography, spacing, color semantics, reusable UI components, visual states, analytical visualization semantics, accessibility constraints, and frontend design-system conventions. UX owns interaction behaviour; Information Architecture owns organisation and findability; Screen Inventory owns canonical screen IDs; Wireframe Specification owns screen composition.

## Core principles
- Evidence first
- Uncertainty visible
- Calm over alarm
- No guilt by color
- Accessible by default
- Dense but legible
- Canonical consistency
- Reversible state awareness
- Security visible when useful
- Print/export parity

## Reference visual baseline
- Primary text: `#16212B`
- Canvas: `#F7F9FB`
- Primary action: `#285C8E`
- Success: `#246B4A`
- Warning/review: `#8A5A00`
- Error/destructive: `#A13333`
- Analytical construct: `#5B4B8A`
- Documented analytical state: `#236A73`

## Mandatory analytical states
`Claim | Fact | Inference | Disputed | Unknown | Candidate`

## Mandatory value-flow classes
`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`

Each class SHALL include a non-color cue in UI and exported views.

## Reference component catalogue
Buttons; inputs; selects; date precision; check/radio/switch; badges; chips; alerts; toasts; data grids; panels; tabs; breadcrumbs; drawers; modals; confirmations; evidence citations; provenance trails; confidence badges; flow-class badges; entity blocks; relationship summaries; review panels; classification banners; empty/permission/integrity/version/loading states; legends.

## Critical prohibitions
- No red entity styling merely because an entity is investigated, highly connected, or typology-related.
- No automatic risk/guilt visualisation from graph centrality or path proximity.
- No confidence-as-guilt percentage meter.
- No color-only analytical meaning.
- No feature-specific raw status colors where semantic tokens exist.

## Accessibility
Target WCAG 2.2 AA-equivalent behaviour where applicable. Keyboard focus, color independence, contrast, accessible graph/timeline/value-flow alternatives, and reduced motion are mandatory design-system concerns.

## Frontend reference
React + TypeScript + Tailwind CSS 4. Semantic tokens SHOULD be exposed as CSS variables and typed component variants. Feature modules SHOULD consume the shared design system before creating local equivalents.

## UI Definition of Done
A production screen is UI-complete only when it uses the correct semantic tokens/components, preserves analytical meaning, passes critical accessibility checks, represents required states, and remains consistent with UX, Information Architecture, Screen Inventory, and Wireframe specifications.

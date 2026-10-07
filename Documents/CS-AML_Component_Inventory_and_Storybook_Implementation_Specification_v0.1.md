# CS-AML Component Inventory & Storybook Implementation Specification v0.1

**Status:** Normative frontend implementation baseline for MVP 0.1

## Implementation axiom
A UI component SHALL encode reusable visual and interaction semantics, not feature-specific assumptions. Storybook SHALL make those semantics inspectable, testable, accessible, and regression-safe before components are composed into production screens.

## Inventory
The baseline defines **65 shared components** across Foundation, General UI, Analytical/Domain, and Compound Pattern layers.

## Layering
`Foundation → General UI → Analytical/Domain → Compound Patterns → Feature Screens`

## Storybook role
Executable catalogue for design review, documentation, accessibility review, interaction testing, visual regression, and reference composition.

## Mandatory analytical story coverage
`Claim | Fact | Inference | Candidate | Disputed | Unknown`

`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`

## MVP Storybook release gate
Every P0 shared component used by the critical end-to-end scenario must have an approved Storybook entry, required state coverage, accessibility checks, and visual-regression baseline.

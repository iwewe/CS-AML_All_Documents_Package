# CS-AML High-Fidelity UI Specification v0.1

**Status:** Normative high-fidelity UI baseline for MVP 0.1

## Core visual axiom
High visual fidelity SHALL improve comprehension without manufacturing certainty. Visual hierarchy may emphasize task relevance, state, and provenance, but SHALL NOT imply guilt, criminality, reliability, or analytical importance beyond the underlying record.

## Scope
Defines production visual composition for canonical CS-AML screens. It binds Screen Inventory IDs, Wireframe patterns, UX rules, IA structure, and UI Design System semantics into frontend-ready screen specifications.

## Reference desktop baseline
- 1440 × 900 design review viewport
- 56 px application bar
- 72–96 px context header
- 40–44 px local navigation
- 320–380 px evidence/provenance inspector where applicable
- 24–32 px page gutter

## Critical detailed screens
- SCR-HOME-001 Home / Work Queue
- SCR-CASE-001 Case Register
- SCR-CASE-003 Case Overview
- SCR-EVD-003 Evidence Detail / Reader
- SCR-ENT-003 Entity Detail
- SCR-ENT-005 Entity Match Compare
- SCR-TIM-001 Timeline
- SCR-VAL-001 Value Flow Workspace
- SCR-TYP-002 Typology Match Worksheet
- SCR-HYP-001 Hypothesis Workspace
- SCR-ASM-001 Assessment Draft
- SCR-GRF-001 Investigation Graph
- SCR-PRD-003 Product Editor
- SCR-REV-002 Peer Review Workspace
- SCR-DIS-001 Dissemination Approval
- SCR-DIS-002 Export Package Builder
- SCR-AUD-001 Audit Explorer

## Mandatory analytical semantics
`Claim | Fact | Inference | Candidate | Disputed | Unknown`

`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`

## Critical visual rules
- Red SHALL NOT identify an investigated person/entity by default.
- Node size/centrality SHALL NOT imply culpability or risk.
- Reconstructed and hypothetical flows SHALL NOT resemble direct flows.
- Unknown values SHALL remain unknown rather than zero.
- Protected-source identity SHALL remain absent from ordinary screens/exports unless authorized.
- Approved versions are readonly but remain fully legible.
- Permission-denied states SHALL not leak hidden object metadata.

## Next document
`CS-AML Component Inventory & Storybook Implementation Specification v0.1`

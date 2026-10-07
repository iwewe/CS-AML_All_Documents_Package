# CS-AML Software Requirements Specification (SRS) v0.1
**Status:** Normative software baseline for MVP 0.1
## Product axiom
Technology SHALL preserve analytical uncertainty rather than erase it.
## Primary release objective
A two-analyst civil-society team can complete one sensitive investigation end-to-end with CS-AML as the system of record, preserving provenance, review, authorization, and auditability.
## Mandatory analytical chain
`SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT`
## Mandatory value-flow classes
`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`
## Requirement families
- `FR-CASE`
- `FR-EVD/DOC`
- `FR-ENT/REL/AST`
- `FR-TIM/VAL`
- `FR-TYP/HYP/ASM`
- `FR-SCH/GRF`
- `FR-PRD/REV/DIS`
- `FR-ADM/SEC/AUD/OPS`
- `DR`
- `IF`
- `SEC`
- `AUD`
- `NFR-PERF`
- `NFR-REL`
- `AN`
- `AI`
- `UX`
- `ADM`
- `INT`
- `OPS`

## MVP release gate
The release is accepted only when the Annex D end-to-end test scenario passes and mandatory P0 requirements are verified.

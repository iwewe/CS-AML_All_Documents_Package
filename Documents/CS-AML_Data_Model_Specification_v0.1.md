# CS-AML Data Model Specification v0.1

**Status:** Normative baseline  
**Purpose:** Canonical implementation-neutral information model for the CS-AML Framework.

## Core design axiom
Case is context. Entity and Evidence are reusable truth-bearing objects. Analytical conclusions remain separate and traceable to evidence and reasoning.

## Purpose and Scope
See normative DOCX/PDF for full field-level requirements.

## Normative Data Principles
See normative DOCX/PDF for full field-level requirements.

## Canonical Information Architecture
See normative DOCX/PDF for full field-level requirements.

## Common Object Envelope
See normative DOCX/PDF for full field-level requirements.

## Identifier and Naming Standard
See normative DOCX/PDF for full field-level requirements.

## Context and Case Objects
See normative DOCX/PDF for full field-level requirements.

## Source, Evidence, Claim, and Fact Model
See normative DOCX/PDF for full field-level requirements.

## Entity and Identity Model
See normative DOCX/PDF for full field-level requirements.

## Relationship, Ownership, and Control Model
See normative DOCX/PDF for full field-level requirements.

## Asset and Event Model
See normative DOCX/PDF for full field-level requirements.

## Value-Flow Model
See normative DOCX/PDF for full field-level requirements.

## Indicator and Typology Model
See normative DOCX/PDF for full field-level requirements.

## Hypothesis, Gap, and Assessment Model
See normative DOCX/PDF for full field-level requirements.

## Confidence and Source Evaluation Model
See normative DOCX/PDF for full field-level requirements.

## Intelligence Product and Dissemination Model
See normative DOCX/PDF for full field-level requirements.

## Privacy, Classification, and Access-Control Metadata
See normative DOCX/PDF for full field-level requirements.

## Temporal, Versioning, and Audit Semantics
See normative DOCX/PDF for full field-level requirements.

## Cross-Object Integrity Rules
See normative DOCX/PDF for full field-level requirements.

## Canonical Graph Mapping
See normative DOCX/PDF for full field-level requirements.

## Reference Relational Mapping
See normative DOCX/PDF for full field-level requirements.

## Canonical JSON Example
See normative DOCX/PDF for full field-level requirements.

## API and Exchange Requirements
See normative DOCX/PDF for full field-level requirements.

## Interoperability and External Identifiers
See normative DOCX/PDF for full field-level requirements.

## Schema Versioning and Migration
See normative DOCX/PDF for full field-level requirements.

## Data Quality and Validation
See normative DOCX/PDF for full field-level requirements.

## Data Model Conformance
See normative DOCX/PDF for full field-level requirements.

## Mandatory analytical separation
`Source -> Evidence -> Claim -> Fact -> Indicator -> Hypothesis -> Assessment -> Intelligence Product`

## Mandatory value-flow classes
`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`

## Minimum object set
Case, Source, EvidenceItem, EvidenceExtract, Fact, Entity, Relationship, Asset, Event, ValueFlow, Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment, IntelligenceProduct, Review, Dissemination, AuditEvent.

# CS-AML Information Architecture Specification v0.1

**Status:** Normative information-architecture baseline for MVP 0.1

## IA axiom
Case is context; canonical objects are reusable. The information architecture SHALL organise investigation work around context while avoiding unnecessary duplication or imprisonment of entities, evidence and analytical objects inside a single case.

## Scope
Defines object hierarchy, taxonomy, labeling, navigation, information scent, search/findability, cross-object discovery, deep links and permission-aware information organisation. Interaction behaviour remains governed by the separate CS-AML UX Specification.

## MVP primary navigation
`Home | Cases | Entities | Evidence | Analysis | Products | Search | Administration`

Graph, Timeline and Value Flow are derived analytical views anchored to canonical objects or case context; they are not primary global truth domains.

## Case workspace
`Overview | Work | Sources & Evidence | Entities & Assets | Timeline | Value Flows | Analysis | Products`

## Canonical rule
Multiple navigation paths SHALL converge on the same canonical object. Case-context views do not create duplicate entities/evidence/relationships.

## Core analytical chain
`SOURCE → EVIDENCE → CLAIM/FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT`

## Mandatory value-flow classes
`DIRECT | DOCUMENTED | RECONSTRUCTED | HYPOTHETICAL`

## Key IA requirements
- Canonical reusable objects have stable identifiers independent of case context.
- Search, counts, facets and backlinks are permission-aware.
- Protected-source identity is excluded from general indexes and navigation.
- Relationship and ValueFlow records are first-class canonical information objects.
- Labels preserve analytical uncertainty and avoid accusatory taxonomy.
- Controlled vocabulary terms use stable IDs and preserve historical semantics.
- Deep links distinguish canonical object identity from contextual case views.
- Derived graph/timeline/dashboard rankings do not silently become risk or guilt categories.

## IA–UX separation
IA owns organisation and findability. UX owns interaction behaviour. Joint decisions include labels, task entry points, deep-link/context preservation and terminology consistency.

# CS-AML API Specification v0.1

**Status:** Normative API contract baseline for MVP 0.1

## Core API axiom
The API SHALL expose canonical data and authorized derived views without erasing provenance, uncertainty, version history or permission boundaries. It SHALL NOT convert candidate, reconstructed, hypothetical, inferred or derived data into stronger canonical truth through transport semantics.

## Baseline
- `/api/v1/` HTTPS JSON API
- Stable opaque IDs
- Permission-aware reads/search/counts/facets
- Version-aware mutations (`record_version` / ETag / If-Match)
- Idempotency for retry-sensitive operations
- Structured machine-readable errors
- Audit correlation via request IDs
- Explicit derived graph/search/timeline projections
- Dedicated protected-source boundary
- OpenAPI 3.1-equivalent schema

## Core resources
Case, Source, EvidenceItem, EvidenceExtract, Entity, Relationship, Asset, Event, ValueFlow, Indicator, TypologyMatch, Hypothesis, IntelligenceGap, Assessment, IntelligenceProduct, Review, Dissemination, AuditEvent.

## Critical rules
- Object IDs are never authorization secrets.
- Unauthorized search/count/facet behavior must be non-disclosing.
- High-impact approvals/merges/dissemination are not optimistic and validate version/workflow state.
- DIRECT, DOCUMENTED, RECONSTRUCTED and HYPOTHETICAL remain explicit API values.
- Protected-source identity is excluded from generic search/graph/export surfaces.

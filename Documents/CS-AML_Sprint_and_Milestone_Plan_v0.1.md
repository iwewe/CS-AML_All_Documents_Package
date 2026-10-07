# CS-AML Sprint & Milestone Plan v0.1

**Status:** Engineering delivery baseline for MVP 0.1

## Delivery axiom
Build vertical, reviewable investigation capabilities; do not optimize for isolated component completion if the end-to-end analytical chain remains broken.

## Planning baseline
- Sprint length: 2 weeks
- Sprint 0 + 8 delivery sprints
- Milestones: M0 Foundation, M1 Governed Case Workspace, M2 Investigation Core, M3 Analytical Intelligence, M4 MVP Release Candidate

## Sprint map

- **Sprint 0 — Engineering Foundation**: Repo, CI/CD, PostgreSQL, evidence store, audit substrate, OIDC skeleton
- **Sprint 1 — Identity + Governed Case Workspace**: RBAC/case membership, protected source, case register, charter, basic activity
- **Sprint 2 — Workflow + Evidence Intake**: Gates/tasks, source register, immutable evidence, hash, extracts, lineage
- **Sprint 3 — Entities + Relationships**: Entity registry, identifiers, matching, merge/unmerge, relationships, ownership/control, assets
- **Sprint 4 — Timeline + Follow-the-Value**: Events/timeline, ValueFlow, multi-leg chains, uncertainty classes, flow visualization
- **Sprint 5 — Typology + Hypothesis + Assessment**: Indicators, typology worksheet, competing hypotheses, gaps, confidence assessment
- **Sprint 6 — Search + Investigation Graph**: Permission-aware search, facets, graph projection, provenance side panel
- **Sprint 7 — Intelligence Product + Review + Dissemination**: Products, evidence index, peer review, corrections, approvals, export/referral, sharing log
- **Sprint 8 — Operational Release**: Retention, backup/restore, hardening, E2E pilot, release evidence and remediation

## Critical path
`Foundation → Authorization → Case → Evidence → Entity/Relationship → Timeline/ValueFlow → Typology/Hypothesis/Assessment → Product/Review/Dissemination → Operational Release`

## Release rule
MVP 0.1 is releasable only when the two-analyst end-to-end scenario passes, mandatory P0 SRS requirements are verified, backup/restore is tested, and no unresolved Critical or release-blocking High defect remains.

## Required release evidence
- SRS traceability matrix
- End-to-end pilot record
- Authorization negative tests
- Evidence integrity and lineage tests
- Entity merge/unmerge test
- Value-flow class persistence test
- Peer-review/dissemination tests
- Backup/restore record
- Known limitations and accepted exceptions

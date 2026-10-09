# Architecture Decision Records

ADRs for CS-AML v0.1.1. Numbering follows the list in
`Documents/CS-AML_Technical_Stack_and_Repository_Specification_v0.1.2.md` §32. ADR-0001 to ADR-0003 are named
there but have not been written yet.
ADR-0003 (S3 capability and evidence storage layout, product-neutral) and ADR-0005 (object-store product selection) are separate decisions. [v0.1.1 · C19]

| ADR | Title | Status |
|---|---|---|
| [0004](0004-keycloak-oidc.md) | Browser authentication: Keycloak OIDC with server-side (BFF) session | Accepted (2026-10-08) |
| [0005](0005-object-storage.md) | Object storage product for evidence | Proposed — evaluation open |
| [0006](0006-broker-cache-valkey.md) | Broker/cache: Valkey 8.x | Accepted (2026-10-08) |

Status values: `Proposed` (under evaluation), `Accepted` (decision recorded by the product owner),
`Superseded by ADR-xxxx`, `Rejected`. "Accepted" records a decision. It does not mean the decision has
been implemented or tested.

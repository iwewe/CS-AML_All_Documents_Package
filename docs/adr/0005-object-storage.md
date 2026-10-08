# ADR-0005 — Object storage product for evidence

- **Status:** Proposed — evaluation open (product not yet selected)
- **Date opened:** 2026-10-08
- **Decision authority:** Product owner (the S3-compatible capability was decided on 2026-10-08; the product is still open)
- **Audit finding:** A02 (MinIO Community recommended without a maintenance caveat)
- **Affected specifications:** Technical Stack §3, §16, §18, §32; Technology Architecture §6.2, §28.1

## Context

Original and derivative evidence objects need an S3-compatible store. It must support versioning, an immutability control
suitable for preserving originals (e.g. object lock / retention), server-side encryption, and verifiable backup and restore.
v0.1 named MinIO as the reference. The upstream MinIO Community repository (`minio/minio`) was archived on 25 April 2026 and
states it is no longer maintained (audit source S04). MinIO Community is a different product from commercial offerings such as
AIStor.

## Decision so far

- The application depends only on the **S3 API**. No product-specific APIs are used in application code.
- MinIO Community is **not** a default for any environment that holds real evidence.
- The product is selected through this ADR once the evaluation below is complete.

## Evaluation criteria (all must be recorded before acceptance)

| Criterion | Evidence required |
|---|---|
| Release line and maintenance status | Link to upstream release/support policy; date checked |
| Licence | Licence of the exact release; compatibility with the organisation's licence policy |
| Patch path | How security fixes are delivered and how fast |
| S3 compatibility | Results of the CS-AML compatibility test (multipart upload, versioning, object lock/retention if used, SSE, presigned URLs) |
| Integrity | Checksum behaviour; no silent change to stored originals |
| Backup and restore | Executed restore test with hash verification of a sample evidence set |
| Hosting/jurisdiction | Where data resides; fit with the privacy specification |
| Operations | Monitoring, capacity, upgrade procedure |

## Candidates to evaluate

These are candidates, not recommendations. Licence, feature and maintenance status SHALL be checked against upstream
sources at evaluation time.

| Candidate | Type |
|---|---|
| Managed S3-compatible service (cloud provider with object lock) | Managed |
| Ceph Object Gateway (RGW) | Self-hosted |
| SeaweedFS | Self-hosted |
| Garage | Self-hosted |
| Commercial MinIO offering (e.g. AIStor) | Self-hosted, commercial licence |

## Interim rule

Local development and CI may use any S3-compatible emulator with synthetic data only. No real evidence may be stored until this
ADR is Accepted.

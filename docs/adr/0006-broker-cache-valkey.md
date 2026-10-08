# ADR-0006 — Broker/cache: Valkey 8.x

- **Status:** Accepted
- **Date:** 2026-10-08
- **Decision authority:** Product owner
- **Audit finding:** A03 (Redis 7.x was too broad for a licence-stable baseline)
- **Affected specifications:** Technical Stack §3, §4, §16, §18, §19; Technology Architecture §6.2, §28.1; Product & Feature Annex C

## Context

v0.1 required "Redis 7.x" as the task broker, bounded cache and transient coordination store. That range spans different licences.
Redis ≤7.2 is BSD-3-Clause, Redis 7.4 is RSALv2/SSPLv1, and Redis 8.x adds an AGPLv3 option (audit source S05). An engineer
could pick a release that meets the text but not the organisation's licence policy.

## Decision

- Use **Valkey 8.x** (BSD-3-Clause, Linux Foundation project, Redis-protocol compatible) as the Celery broker and cache.
- Pin the exact minor/patch release and image digest in the dependency manifest, and record the licence in the SBOM. All three must
  refer to the same version.
- Application code uses the Redis protocol through standard clients (Celery `redis://` transport scheme). It uses no
  Valkey- or Redis-specific modules.
- Data in the broker/cache is transient. Canonical data stays in PostgreSQL, and no evidence or source-protected content is
  cached unless policy allows it.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Redis 7.2.x (BSD-3-Clause) | Older line; long-term maintenance outlook weaker than an actively developed fork |
| Redis 8.x under AGPLv3 | AGPL obligations need separate legal review; no functional need |
| RabbitMQ as broker + separate cache | Two services to operate for MVP |

## Consequences

- Upgrades within 8.x need a regression run of worker/broker integration tests.
- Moving to a later major version (e.g. 9.x) needs a new ADR or an amendment with licence re-check.

## Verification (not yet run)

- Celery integration tests pass against the pinned Valkey image.
- The SBOM entry, manifest version and image digest match.

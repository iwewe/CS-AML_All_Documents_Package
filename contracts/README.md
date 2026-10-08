# contracts/

`openapi.yaml` is the OpenAPI 3.1 contract for the CS-AML API, version 0.1.1. Its status is **draft for review**: nothing has been implemented or tested against it yet.

## Scope: the P0 vertical slice

The contract is derived from `Documents/CS-AML_API_Specification_v0.1.1.md` (endpoints and conventions) and `Documents/CS-AML_Data_Model_Specification_v0.1.1.md` (fields and enums). It covers:

- Common parts: the cookie session `__Host-csaml_session` with the CSRF header `X-CSRFToken`, `If-Match`/`ETag`, `Idempotency-Key`/`Idempotent-Replayed`, `Retry-After`, the error envelope with every error code from §9, the cursor list envelope, and the common object envelope.
- Auth/session endpoints (`/auth/*`, served outside `/api/v1`).
- Cases, charter, gates, tasks and activity.
- Sources and evidence: upload initiate, content and complete, metadata, content, integrity, extracts, lineage and derivatives.
- Claims, facts and verification decisions (§16A).
- Entities and relationships, including match candidates, merge/unmerge and resolution decisions.
- Value flows and their legs.
- Hypotheses and assessments, including finalize and provenance.
- Intelligence products (the six MVP templates), reviews, dissemination, export packages, the sharing log and job polling.

Anything marked `x-csaml-status: proposed` is a contract decision that the specifications do not fix. Examples are the list envelope and 400 for a missing REQUIRED `Idempotency-Key`. Each one needs review.

Multi-entity commands (merge, unmerge, `POST /resolution-decisions` and match-candidate decisions) send the body map `expected_versions` instead of `If-Match`. This is adopted (D-A04), not proposed. The property is defined on each request body but is not in `required`: a missing or incomplete map returns 428 PRECONDITION_REQUIRED, and a stale entry returns 412 PRECONDITION_FAILED with `details.current_record_versions`. *[v0.1.1 · C04, C05]*

## Not covered yet

- Assets, events, timeline, value-flow view and legend (§14–§15).
- Typologies, indicators, typology matches and intelligence gaps (§16).
- Search (§17), graph (§18), administration and audit (§20) and protected sources (§21).
- Value sets the specifications leave open: job, upload-session, gate and task status; risk rating; amount precision; export format.
- Per-resource sort and filter allowlists.
- How the SPA obtains the CSRF token.

## Validation

- `python3 tools/check_consistency.py` checks that every enum schema tagged `x-csaml-enum` matches `schemas/enums.yaml` (`x-csaml-enum-subset: true` allows a deliberate subset). It also checks that every `$ref` resolves, every path parameter is declared, and operationIds are unique.
- `npx @redocly/cli lint contracts/openapi.yaml` (recommended ruleset) passed on 2026-10-08 with 0 errors and 4 known warnings: the three `/auth/*` redirect operations (302/303) have no 2xx response, and the reusable `StateConflict` response is unused.

This file is the design contract (contract-first), maintained by hand. Once an implementation exists, API §28 requires the schema generated from the code to be diffed against this file in CI. *[v0.1.1 · C19]*

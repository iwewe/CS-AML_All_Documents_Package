# contracts/

`openapi.yaml` is the OpenAPI 3.1 contract for the CS-AML API, version 0.1.4. Its status is **Approved Internal Specification Baseline** (tag `v0.1.4-spec`, 2026-10-10; supersedes `v0.1.3-spec`). *[v0.1.4]*

## Scope

The contract is derived from `Documents/CS-AML_API_Specification_v0.1.4.md` (endpoints and conventions) and `Documents/CS-AML_Data_Model_Specification_v0.1.4.md` (fields and enums). Version 0.1.4 has 146 paths and 190 operations (v0.1.3: 138 paths, 180 operations; v0.1.2: 111 paths, 149 operations; v0.1.1: 72 paths, 92 operations). It covers:

- Common parts: the cookie session `__Host-csaml_session` with the CSRF header `X-CSRFToken`, `If-Match`/`ETag`, `Idempotency-Key`/`Idempotent-Replayed`, `Retry-After`, the error envelope with every error code from §9, the cursor list envelope, and the common object envelope.
- Auth/session endpoints (`/auth/*`, served outside `/api/v1`), including `csrf_token`/`username` on the session and OIDC back-channel logout. *[v0.1.2 · CR-I1-03, CR-I1-05, CR-I1-07]* Since v0.1.4: the session assurance fields `auth_level`, `auth_time`, `step_up`, the login parameters `acr` and `next`, and the 303 `LoginErrorRedirect` of a failed callback. *[v0.1.4 · CR-N-13, CR-N-14]*
- Cases, charter, gates, tasks, activity, case memberships and the per-case graph projection. *[v0.1.2 · CR-I1-02, CR-I3-07]* Since v0.1.4 also charter version history, gate status / transitions / preconditions / decision history, task detail and update with registered task type and status, and activity item fields. *[v0.1.4 · CR-N-01…CR-N-08]*
- Sources and evidence: upload initiate, content and complete, metadata, content, integrity, extracts (create and list), lineage and derivatives; since v0.1.4 OCR / text-extraction and offline machine-translation requests and the DerivedText list, detail and review. *[v0.1.4 · CR-N-09, CR-N-10]*
- Claims, facts and verification decisions (§16A), with provenance traces.
- Entities and relationships, including match candidates, merge/unmerge and resolution decisions, and provenance traces. *[v0.1.2 · CR-I2-04]*
- Assets, ownership interests and control assertions; events and the timeline. *[v0.1.2 · CR-I3-01, CR-I3-02]*
- Value flows and their legs, the value-flow view and legend. *[v0.1.2 · CR-I3-03, CR-I3-04, CR-I3-12]*
- Typology catalogue, typologies, indicators and typology matches; hypotheses with the ACH matrix (hypothesis links); intelligence gaps; assessments, including finalize, disconfirming searches, revisions and provenance. *[v0.1.2 · CR-I4-01…CR-I4-05, CR-I4-14]*
- Intelligence products (the six MVP templates), reviews, dissemination, export packages, the sharing log and job polling; since v0.1.3 also product templates, live rendering, frozen versions, corrections and withdrawal, assessment review submission and review requests, the dissemination list and revocation, export package list, detail and download, and registered job / package / dissemination / review statuses. *[v0.1.3 · CR-I6-01…CR-I6-12]*
- Search (`GET /search`) and graph exploration (`POST /graph/query`, `POST /graph/paths`). *[v0.1.3 · CR-I5-01, CR-I5-02]*
- Retention rules, retention evaluations, legal holds and disposition records. *[v0.1.3 · CR-I7-01…CR-I7-04]*
- The canonical single-extract resource `GET /evidence-extracts/{extractId}` and the unauthenticated readiness probe `GET /health`; the Prometheus `/metrics` endpoint is internal and not part of this contract. *[v0.1.3 · CR-I5-07, CR-I7-08]*

The I3 and I4 implementation extensions (`contracts/extensions/i3.yaml`, `i4.yaml` in the implementation repository) are merged into this file; they are no longer separate documents. *[v0.1.2 · CR-I3-01, CR-I4-01]* The I5, I6 and I7 extensions (`i5.yaml`, `i6.yaml`, `i7.yaml`) are merged in v0.1.3 in the same way. *[v0.1.3 · CR-I5-01, CR-I6-01, CR-I7-01]* The post-MVP extensions `case-workflow.yaml` and `n1.yaml` are merged in v0.1.4; the behaviour `n1.yaml` listed under `x-csaml-n1-behaviour` is expressed directly in the contract (`x-csaml-step-up`, `Session`, `authLogin`, `authCallback`, search enums, `JobType`). *[v0.1.4 · CR-N-01, CR-N-09, CR-N-13]*

Contract choices that the prose specifications do not fix carry `x-csaml-release-class`:

| Class | `x-csaml-status` | Meaning |
|---|---|---|
| `MUST_DECIDE_V0_1_1` | `decided` | Affects safety, approval, integrity or domain semantics; decided by the product owner on 2026-10-08 (API Specification §28 lists the seven decisions) |
| `ACCEPT_DEFAULT_V0_1_1` | `accepted-default` | Engineering default needed to implement (e.g. pagination envelope, response shapes); frozen, may evolve only compatibly |
| `DEFER_V0_2` | `deferred` | Outside the core vertical slice (task contracts) |
| `DECIDED_V0_1_2` | `decided` | Approved change request of 2026-10-09; `x-csaml-cr` lists the change-request IDs (`CHANGELOG.md`, v0.1.2) *[v0.1.2]* |
| `DECIDED_V0_1_3` | `decided` | Approved change request of 2026-10-09 from increments I5–I7; `x-csaml-cr` lists the IDs (`CHANGELOG.md`, v0.1.3) *[v0.1.3]* |
| `DECIDED_V0_1_4` | `decided` | Approved change request of 2026-10-10 from the post-MVP follow-ups; `x-csaml-cr` lists the IDs (`CHANGELOG.md`, v0.1.4) *[v0.1.4]* |

Further annotations: `x-csaml-ref-types` lists the permitted target classes of a reference field (CR-I2-07, CR-I3-10, CR-I4-14); `x-csaml-review-required: AML_SPECIALIST` marks the provisionally adopted typology-match thresholds (CR-I4-03); `x-csaml-enum-wire: code` marks the registry exception for `credibility_grade` (CR-I2-08). `decideEntityMatchCandidate` is `deprecated: true` (removal in v0.2; use `POST /resolution-decisions`, CR-I2-14). *[v0.1.2]* `x-csaml-step-up: <action>` marks the 13 high-risk operations that answer 403 STEP_UP_REQUIRED without a recent second-factor step-up (CR-N-13). *[v0.1.4]*

Multi-entity commands (merge, unmerge, `POST /resolution-decisions` and match-candidate decisions) send the body map `expected_versions` instead of `If-Match`. This is adopted (D-A04), not proposed. The property is defined on each request body but is not in `required`: a missing or incomplete map returns 428 PRECONDITION_REQUIRED, and a stale entry returns 412 PRECONDITION_FAILED with `details.current_record_versions`. *[v0.1.1 · C04, C05]*

## Not covered yet

- Administration and audit (§20, other than retention and health), protected sources (§21), `GET /capabilities`. *[v0.1.3]*
- Value sets the specifications leave open: `Asset.valuation_basis`; Methodology §14.1 event statuses. (Job status and export format are registered since v0.1.3; gate and task status, job type and the open `derivation_type` vocabulary since v0.1.4.) *[v0.1.4 · CR-N-03, CR-N-04, CR-N-09, CR-N-12]*
- Deferred to v0.2: server-side activity filters (`actor`, `action`, `target_type`), task links to objects, MONITORING / reopening, per-deployment step-up configuration. *[v0.1.4 · CR-N-03, CR-N-04, CR-N-08, CR-N-13]*
- Per-resource sort and filter allowlists.

## Validation

- `python3 tools/check_consistency.py` checks that every enum schema tagged `x-csaml-enum` matches `schemas/enums.yaml` (`x-csaml-enum-subset: true` allows a deliberate subset; `x-csaml-enum-wire: code` compares against the registry codes). It also checks that every `$ref` resolves, every path parameter is declared, operationIds are unique and every cited change-request ID is listed in `CHANGELOG.md`.
- `npx @redocly/cli lint contracts/openapi.yaml` (recommended ruleset) passed on 2026-10-10 (v0.1.4) with 0 errors and 4 warnings: the three `/auth/*` redirect operations (302/303) have no 2xx response, and `GET /health` (an unauthenticated probe) has no 4xx response (as in v0.1.3). *[v0.1.4]*

This file is the design contract (contract-first), maintained by hand. The reference implementation validates its requests and responses against it in conformance tests; API §28 requires the schema generated from the code to be diffed against this file in CI. *[v0.1.1 · C19]*

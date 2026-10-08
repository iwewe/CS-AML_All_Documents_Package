**CS-AML**

**API Specification**

Version 0.1.1

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML API Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Purpose**  
> Proposed normative HTTP API baseline (draft for review) for CS-AML MVP 0.1. *[v0.1.1 · A01]* It defines resource conventions, request/response envelopes, versioning, authorization behavior, filtering, pagination, concurrency, idempotency, uploads, search, graph projections, review/dissemination operations, errors, audit correlation and verification expectations.

> **Core API axiom**  
> The API SHALL expose canonical data and authorized derived views without erasing provenance, uncertainty, version history or permission boundaries. It SHALL NOT convert candidate, reconstructed, hypothetical, inferred or derived data into stronger canonical truth through transport semantics.

Status: Proposed normative API contract baseline for MVP 0.1 (draft for review) *[v0.1.1 · A01]*

Dependencies: Framework v0.1.1 · Data Model v0.1.1 · SRS v0.1.1 · Technology Architecture v0.1.1 · Frontend Architecture v0.1.1 · Control Implementation Guide v0.1.1 (Markdown, `Documents/*_v0.1.1.md`) *[v0.1.1 · A01]*

# Document Control

| **Attribute** | **Value** |
|----|----|
| Document ID | CSAML-API-0.1 |
| Version | 0.1.1 |
| Status | Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]* |
| Primary audience | Backend Engineer, Frontend Engineer, QA, Security Reviewer, Integration Engineer |
| Protocol | HTTPS + JSON; multipart/streaming where file transfer requires it |
| Reference style | Resource-oriented REST API with explicit action endpoints for workflow decisions |
| Normative verbs | SHALL / MUST / SHOULD / MAY |

# 1. Scope and Boundary

This document defines the externally observable API contract for the CS-AML MVP. It does not require a particular backend framework or database schema. The canonical server implementation MAY use Django REST Framework or equivalent, but clients SHALL rely on the documented API rather than backend internals.

> **Authorization rule**  
> Every API read, count, search result, relationship traversal, export candidate and mutation SHALL be permission-aware. UI behavior cannot broaden access.

# 2. API Design Principles

| **ID** | **Principle** | **Requirement** |
|----|----|----|
| API-P01 | Canonical resource first | Stable IDs identify canonical resources independent of UI route context. |
| API-P02 | Context explicit | Case context, version and projection scope are explicit rather than inferred from browser state. |
| API-P03 | Provenance preserved | Material analytical records expose provenance/evidence references appropriate to authorization. |
| API-P04 | Uncertainty preserved | Unknown, disputed, candidate, reconstructed and hypothetical states are first-class values. |
| API-P05 | Non-disclosing authorization | Denied requests SHALL not leak protected resource existence/content beyond policy. |
| API-P06 | Version-aware mutation | Conflicting updates fail explicitly; no last-write-wins for material canonical records. |
| API-P07 | Derived is labeled | Search, graph, path, summary and analytical projections are identified as derived/rebuildable. |
| API-P08 | Audit correlation | Material requests have correlation/request IDs and auditable actor/action context. |
| API-P09 | Predictable errors | Machine-readable error code + safe human message + field errors where relevant. |
| API-P10 | Evolution controlled | Breaking changes require versioning/migration strategy. |

# 3. Base URL, Versioning and Media Type

``` text
https://csaml.example.org/api/v1/
Accept: application/json
Content-Type: application/json
X-Request-ID: <optional-client-correlation-id>
X-CSRFToken: <django-csrf-token>        # unsafe methods only (see §4)
```

- Initial major version SHALL be `/api/v1/`.

- Breaking field removals/semantic changes require a new major API version or documented compatibility period.

- Additive optional fields MAY be introduced within v1.

- Clients SHALL ignore unknown response fields unless schema validation explicitly disallows them for a security reason.

- The OpenAPI document (`contracts/openapi.yaml`, see §28) SHALL be versioned with application releases. *[v0.1.1 · A11]*

# 4. Authentication and Principal Context

| **Concern** | **Requirement** |
|----|----|
| Authentication | Browser authentication is locked to a server-side session (BFF pattern). Django is a confidential OIDC client of Keycloak using Authorization Code + PKCE. Access, refresh and ID tokens stay server-side and are never exposed to JavaScript. Browsers SHALL NOT send `Authorization: Bearer`; bearer tokens from browsers are rejected. *[v0.1.1 · A11]* |
| Auth endpoints | `GET /auth/login` (redirect to IdP) · `GET /auth/callback` (code exchange, session creation) · `POST /auth/logout` (session destroyed; IdP logout initiated) · `GET /auth/session` (current principal, session expiry, coarse capabilities; 401 when no session). These are served by the same origin outside `/api/v1`. *[v0.1.1 · A11]* |
| Session cookie | The browser holds only `__Host-csaml_session` with attributes `HttpOnly; Secure; SameSite=Lax; Path=/` and no `Domain` attribute. *[v0.1.1 · A11]* |
| CSRF | Every unsafe method (POST/PUT/PATCH/DELETE) SHALL carry the Django CSRF token in the `X-CSRFToken` header; missing/invalid token → 403. *[v0.1.1 · A11]* |
| Origin / CORS | The API is same-origin (`/api/v1` behind Nginx). CORS is disabled by default. *[v0.1.1 · A11]* |
| Session timeouts | Idle and absolute session timeouts are security-policy configuration. *[v0.1.1 · A11]* |
| Principal | Server resolves user/service identity; client-submitted actor identity is not trusted. |
| MFA | Required claims/policy enforced server-side for sensitive actions where configured. |
| Service account | Machine/service API clients are out of MVP scope. When introduced, each SHALL be a distinct non-human principal with least privilege and no shared analyst identity; its authentication mechanism requires a separate decision. *[v0.1.1 · A11]* |
| Logout/revocation | After logout, session expiry or revocation, subsequent requests return 401. Keycloak back-channel logout SHOULD revoke the corresponding server-side sessions. *[v0.1.1 · A11]* |
| Impersonation | Not supported in MVP unless separately controlled/audited. |

# 5. Common Headers and Correlation

| **Header** | **Direction** | **Use** |
|----|----|----|
| Cookie (`__Host-csaml_session`) | Request | Browser session authentication (§4). `Authorization: Bearer` is not accepted from browsers. *[v0.1.1 · A11]* |
| X-CSRFToken | Request | Django CSRF token; REQUIRED on every unsafe method (§4). *[v0.1.1 · A11]* |
| X-Request-ID | Both | Correlation ID; server generates when absent. |
| ETag | Response | `"<record_version>"` returned on GET of every versioned resource (§10). *[v0.1.1 · A04]* |
| If-Match | Request | `"<record_version>"`; REQUIRED on mutations of versioned resources (§10). Missing → 428; stale → 412. *[v0.1.1 · A04]* |
| Idempotency-Key | Request | UUID; REQUIRED or SHOULD per §11. *[v0.1.1 · A11]* |
| Idempotent-Replayed | Response | `true` when the response is a replay of an earlier request with the same Idempotency-Key (§11). *[v0.1.1 · A11]* |
| Retry-After | Response | Rate limit/async polling guidance; also sent with 409 IDEMPOTENCY_IN_PROGRESS. *[v0.1.1 · A11]* |
| Content-Disposition | Response | Safe filename for export/download. |

# 6. Common Resource Envelope

``` text
{
  "id": "uuid",
  "object_type": "entity",
  "schema_version": "1.0",
  "record_version": 7,
  "status": "ACTIVE",
  "classification": "RESTRICTED",
  "created_at": "2026-10-07T10:00:00Z",
  "created_by": {"id":"...","display_name":"..."},
  "updated_at": "2026-10-07T11:12:00Z",
  "links": {...},
  "capabilities": ["read","update","link"]
}
```

> **Enum values and classification**  
> Controlled enumeration values on the wire (including `status`) are UPPER_SNAKE_CASE machine values derived from the Data Model Annex A registry; display labels are separate and translatable. *[v0.1.1 · A09]* `classification` takes one of `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED` (least → most restrictive; display labels Public, Internal, Sensitive, Restricted, Source-protected). Access labels are additive restrictions; the most restrictive applicable level plus all labels apply. Derived objects and exports inherit the highest classification of their inputs unless a recorded reviewer downgrade decision exists. A resource with unknown or missing classification fails closed (access denied; flagged for classification). *[v0.1.1 · A08]*

> **Capabilities**  
> `capabilities` MAY help the UI render permitted actions, but SHALL NOT replace server authorization. Capabilities are contextual and may change between requests.

# 7. Naming and Resource Conventions

| **Rule** | **Convention** |
|----|----|
| Collection names | Plural kebab-case or consistent plural nouns: `/cases`, `/entities`, `/value-flows`. |
| IDs | Opaque stable UUID-like identifiers; clients do not parse meaning from IDs. |
| Timestamps | ISO 8601 UTC in transport; original timezone may be additional metadata. |
| Enums | Stable UPPER_SNAKE_CASE machine values derived from the Data Model Annex A registry; user-facing localized labels are separate. *[v0.1.1 · A09]* |
| Unknown | Use `null`/explicit status per schema; never substitute 0/false/empty string when semantically different. |
| Money | Amount + currency; ranges preserve min/max/approximate/original value semantics. |
| Dates | Precision field accompanies partial/approximate dates where domain requires it. |
| Relationships | First-class resource, not hidden nested-only edge. |

# 8. Pagination, Sorting and Filtering

``` text
GET /api/v1/entities?case_id=...&type=COMPANY&status=CONFIRMED&classification=RESTRICTED,SOURCE_PROTECTED&sort=-updated_at&page[size]=50&page[after]=...
```

| **Concern** | **Baseline** |
|----|----|
| Pagination | Cursor-based SHOULD be preferred for mutable large collections; page-number MAY be used for stable admin lists. |
| Page size | Default 50; max configurable. Server MAY lower for expensive resources. |
| Sorting | Explicit allowlist only; deterministic secondary sort. |
| Filtering | Typed documented filters; no arbitrary raw SQL/query expressions. |
| Facets | Server computes permission-aware facets/counts. |
| Total count | MAY be omitted/approximate for expensive permission-filtered queries; semantics documented. |
| Search query | Input length/rate limits apply; results never reveal unauthorized counts/snippets. |

# 9. Error Model

``` text
{
  "error": {
    "code": "PRECONDITION_FAILED",
    "message": "The record changed after you opened it.",
    "request_id": "req_...",
    "details": {"current_record_version": 8},
    "field_errors": {}
  }
}
```

| **HTTP** | **Example code** | **Semantics** |
|----|----|----|
| 400 | INVALID_REQUEST | Malformed/semantically invalid request not tied to one field. |
| 401 | AUTHENTICATION_REQUIRED | No valid authenticated principal. |
| 403/404 | ACCESS_DENIED / NOT_FOUND | Deployment/policy chooses non-disclosing behavior consistently. |
| 409 | STATE_CONFLICT | Workflow/business-state conflict only (e.g. gate not satisfied, object already finalized, approving a rejected item). Not used for stale versions. *[v0.1.1 · A04]* |
| 409 | IDEMPOTENCY_IN_PROGRESS | A request with the same Idempotency-Key is still in flight; `Retry-After` included (§11). *[v0.1.1 · A11]* |
| 412 | PRECONDITION_FAILED | `If-Match` does not match the current `record_version`; `details.current_record_version` included. No silent overwrite. *[v0.1.1 · A04]* |
| 422 | VALIDATION_FAILED | Field/domain validation. |
| 422 | IDEMPOTENCY_KEY_REUSED | Same Idempotency-Key reused with a different payload (§11). *[v0.1.1 · A11]* |
| 428 | PRECONDITION_REQUIRED | Mutation of a versioned resource sent without `If-Match`. *[v0.1.1 · A04]* |
| 429 | RATE_LIMITED | Request rate or expensive operation threshold exceeded. |
| 500 | INTERNAL_ERROR | Safe generic message; request ID for support. |
| 503 | DEPENDENCY_UNAVAILABLE | Temporary backend dependency failure. |

The error code `VERSION_CONFLICT` used in v0.1 is retired; stale versions are reported only as 412 PRECONDITION_FAILED, which clients map to the "record changed" recovery UI. *[v0.1.1 · A04]*

**Evaluation order.** The server SHALL evaluate a request in this order and return the first failure: authentication (401) → authorization (403/404, non-disclosing) → header validation (400/428) → precondition (412) → body validation (422) → workflow state (409). *[v0.1.1 · A04]*

The error envelope above (`error.code`, `message`, `request_id`, `details`, `field_errors`) is the normative error envelope for v1. *[v0.1.1 · A11]*

> **Error safety**  
> Error payloads SHALL not include raw SQL, stack traces, filesystem paths, evidence snippets, protected-source identity or authorization-policy internals.

# 10. Concurrency and Record Versioning

- Material mutable resources SHALL expose `record_version` or equivalent concurrency token.

- Versioned resources SHALL return `ETag: "<record_version>"` on GET. *[v0.1.1 · A04]*

- Mutations of versioned resources (PATCH/PUT/DELETE and state-changing commands on a versioned resource) SHALL send `If-Match: "<record_version>"`. Missing `If-Match` → **428 PRECONDITION_REQUIRED**. *[v0.1.1 · A04]*

- Stale `If-Match` → **412 PRECONDITION_FAILED** with `details.current_record_version` and other safe metadata needed for recovery; the API SHALL NOT silently overwrite. *[v0.1.1 · A04]*

- A `record_version` in the body is optional; if present it SHALL equal the `If-Match` value, otherwise **400 INVALID_REQUEST**. *[v0.1.1 · A04]*

- **409 STATE_CONFLICT** is reserved for workflow/business-state conflicts. Approvals, merges, dissemination and assessment finalization SHALL validate both the precondition (412) and current workflow state (409), in the evaluation order of §9. *[v0.1.1 · A04]*

- A retried request carrying the same `Idempotency-Key` replays the original result (§11) instead of failing with 412. *[v0.1.1 · A04, A11]*

- Immutable/audit resources reject ordinary update/delete methods.

``` text
PATCH /api/v1/assessments/{id}
If-Match: "7"
{ "record_version": 7, "judgement": "..." }

→ 412 PRECONDITION_FAILED if current version is 8
  { "error": { "code": "PRECONDITION_FAILED", "details": {"current_record_version": 8}, ... } }
→ 428 PRECONDITION_REQUIRED if If-Match is absent
```

*[v0.1.1 · A04]*

# 11. Idempotency

Locked semantics: *[v0.1.1 · A11]*

| **Aspect** | **Rule** |
|----|----|
| Header | `Idempotency-Key: <UUID>` |
| Scope | (principal, HTTP method, route template + path parameters). |
| Retention | 24 hours from the first request. |
| Same key + same payload hash | Replay the original status and body with response header `Idempotent-Replayed: true`. |
| Same key + different payload | **422 IDEMPOTENCY_KEY_REUSED**. |
| Same key while the first request is in flight | **409 IDEMPOTENCY_IN_PROGRESS** with `Retry-After`. |
| Interaction with If-Match | A replay returns the original result; it does not re-evaluate the precondition and does not fail with 412. |

| **Operation** | **Idempotency requirement** |
|----|----|
| Normal PATCH with version token | `If-Match` protection (§10) generally sufficient; Idempotency-Key MAY be sent. *[v0.1.1 · A11]* |
| Create case/entity (and other creates) | Idempotency-Key SHOULD be sent. *[v0.1.1 · A11]* |
| Evidence ingest finalization | Idempotency-Key REQUIRED. *[v0.1.1 · A11]* |
| Merge/unmerge | Idempotency-Key REQUIRED. *[v0.1.1 · A11]* |
| Approve review/dissemination | Idempotency-Key REQUIRED; a repeat SHALL return the same completed decision, never a duplicate decision. *[v0.1.1 · A11]* |
| Export package generation | Idempotency-Key REQUIRED; ties a retry to the same approved package request. *[v0.1.1 · A11]* |

The response code for a request that omits a REQUIRED Idempotency-Key is not yet locked (open item, §28). *[v0.1.1 · A11]*

# 12. Case and Workflow API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET | /cases | Authorized case register. |
| POST | /cases | Create case. |
| GET | /cases/{caseId} | Canonical case detail. |
| PATCH | /cases/{caseId} | Version-aware case update. |
| GET | /cases/{caseId}/charter | Current charter + version history links. |
| POST | /cases/{caseId}/charter/versions | Create new charter version. |
| GET | /cases/{caseId}/gates | Lifecycle gates. |
| POST | /cases/{caseId}/gates/{gateId}/submit | Submit gate for decision. |
| POST | /cases/{caseId}/gates/{gateId}/approve | Independent approval action. |
| POST | /cases/{caseId}/gates/{gateId}/reject | Reject/return with rationale. |
| GET | /cases/{caseId}/tasks | Tasks. |
| POST | /cases/{caseId}/tasks | Create task. |
| GET | /cases/{caseId}/activity | Material case activity projection. |

# 13. Source, Evidence and File API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /sources | Register/query sources. |
| GET/PATCH | /sources/{sourceId} | Source detail/update. |
| GET | /evidence | Authorized evidence library. |
| POST | /evidence/uploads | Initiate upload session. |
| PUT/POST | /evidence/uploads/{uploadId}/content | Stream/upload bytes or receive pre-signed target according to deployment. |
| POST | /evidence/uploads/{uploadId}/complete | Finalize immutable evidence record and hash. |
| GET | /evidence/{evidenceId} | Evidence metadata. |
| GET | /evidence/{evidenceId}/content | Authorized content stream/download; supports range where safe. |
| POST | /evidence/{evidenceId}/verify-integrity | Recompute/verify integrity. |
| POST | /evidence/{evidenceId}/extracts | Create citation/extract. |
| GET | /evidence/{evidenceId}/lineage | Original/derivative lineage. |
| POST | /evidence/{evidenceId}/derivatives | Register approved derivative metadata/output. |

> **Evidence invariant**  
> File upload success SHALL NOT by itself mean evidence is complete. The completion endpoint SHALL only succeed after required metadata, storage write and integrity record succeed atomically or with documented compensating behavior.

# 14. Entity, Relationship and Asset API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /entities | Authorized entity search/register/create. |
| GET/PATCH | /entities/{entityId} | Canonical entity detail/update. |
| GET | /entities/{entityId}/identifiers | Identifiers/aliases with provenance. |
| GET | /entity-match-candidates | Candidate duplicates. |
| POST | /entity-match-candidates/{id}/decisions | Mark same/distinct/unresolved/defer. |
| POST | /entities/merge | Version-aware merge action. |
| POST | /entity-merges/{mergeId}/unmerge | Controlled reversal. |
| GET/POST | /relationships | First-class relationships. |
| GET/PATCH | /relationships/{relationshipId} | Relationship detail/update. |
| GET/POST | /assets | Asset registry. |
| GET/PATCH | /assets/{assetId} | Asset detail/update. |

# 15. Timeline and Value Flow API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /events | Events with temporal precision. |
| GET | /timeline | Derived timeline projection scoped by case/entity/date. |
| GET/POST | /value-flows | ValueFlow resources. |
| GET/PATCH | /value-flows/{flowId} | Flow detail/update. |
| POST | /value-flows/{flowId}/legs | Add version-aware flow leg. |
| GET | /value-flow-view | Derived graph/list projection for workspace. |
| GET | /value-flow-legend | Optional semantic metadata/labels for clients. |

> **Flow semantics**  
> Every ValueFlow response SHALL carry its epistemic class in `flow_class` with one of the wire values `DIRECT`, `DOCUMENTED`, `RECONSTRUCTED`, `HYPOTHETICAL` (UPPER_SNAKE_CASE; from the Data Model Annex A registry). *[v0.1.1 · A09]* No endpoint may collapse these into a generic “transaction” representation.

# 16. Typology, Hypothesis and Assessment API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET | /typologies | Versioned typology catalogue. |
| GET | /typologies/{typologyId} | Typology version/detail. |
| GET/POST | /indicators | Evidence-linked indicators/counter-indicators. |
| GET/POST | /typology-matches | Case typology worksheets. |
| GET/POST | /hypotheses | Competing hypotheses. |
| PATCH | /hypotheses/{id} | Version-aware update. |
| GET/POST | /intelligence-gaps | Explicit unknowns. |
| GET/POST | /assessments | Draft/versioned assessments. |
| POST | /assessments/{id}/finalize | Controlled finalization action. |
| GET | /assessments/{id}/provenance | Backward trace to hypotheses/facts/evidence. |

> **Confidence semantics** *[v0.1.1 · A09]*  
> `confidence.level` takes one of `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`; `confidence.rationale` is mandatory for every level. `INSUFFICIENT_BASIS` means a judgement was attempted but the evidential basis is insufficient; it is not a level below `LOW`, and the API SHALL NOT convert it to `LOW`, `null`, zero, or omit it, in any request, response, filter, sort or export. `null` is allowed only on drafts where no confidence judgement has been made yet; `POST /assessments/{id}/finalize` SHALL reject a null level (422). No normalization may raise certainty.

# 16A. Claim and Fact API

*[v0.1.1 · A10]* — Proposed in the v0.1.1 remediation; **requires product-owner approval** before implementation. Resource semantics follow Data Model §7.4 (Claim) and §7.5 (Fact). The paths follow this document's existing style for workflow decisions (`/resource/{id}/action` sub-paths, as in `/assessments/{id}/finalize`).

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /cases/{caseId}/claims | List/record source claims for a case (attributed to a source and/or evidence extract). |
| GET/PATCH | /claims/{claimId} | Claim detail; version-aware update of descriptive metadata and `claim_status`. The asserted proposition is never overwritten by analyst conclusions. |
| POST | /claims/{claimId}/verification-decisions | Record an append-only VerificationDecision on a claim. |
| GET/POST | /cases/{caseId}/facts | List facts; propose ("promote") a new fact, created as `PROVISIONAL`. |
| GET | /facts/{factId} | Fact detail, including verification history and `superseded_by`. |
| POST | /facts/{factId}/establish | Move a fact to `ESTABLISHED` (reviewer decision). |
| POST | /facts/{factId}/dispute | Move a fact to `DISPUTED` with evidence. |
| POST | /facts/{factId}/supersede | Move a fact to `SUPERSEDED` with a replacement fact reference. |
| GET | /facts/{factId}/dependents | Assessments and intelligence products that depend on the fact, with their `review_required` state. |

| **Concern** | **Rule** |
|----|----|
| Claim status | `claim_status`: `RECORDED`, `UNDER_REVIEW`, `CORROBORATED`, `CONTRADICTED`, `UNRESOLVED`. The `disputed` boolean is kept for compatibility and is derived (status `CONTRADICTED` or an open dispute); it is read-only. |
| VerificationDecision | Fields: `target_ref` (claim or fact), `decision`, `rationale`, `evidence_refs`, `decided_by` (server-resolved principal), `decided_at`, `review_ref` (optional). Append-only: no PATCH/DELETE; corrections are new decisions. |
| Fact promotion | `POST /cases/{caseId}/facts` SHALL include source claim refs and/or evidence refs and a VerificationDecision ref; otherwise 422. The new fact starts as `PROVISIONAL`. |
| Fact status | `fact_status`: `PROVISIONAL`, `ESTABLISHED`, `DISPUTED`, `SUPERSEDED`; `superseded_by` references the replacement fact. |
| Permissions | Investigator/Analyst MAY record claims and propose `PROVISIONAL` facts. `establish` requires a Reviewer who is not the proposer (otherwise 403). Any authorized case member MAY `dispute` with evidence refs. `supersede` requires a replacement fact ref (otherwise 422). |
| Preconditions | `PATCH /claims/{claimId}` and every fact command SHALL send `If-Match` (§10): missing → 428, stale → 412. An invalid transition (e.g. establishing a `SUPERSEDED` fact) → 409 STATE_CONFLICT. Commands SHOULD send `Idempotency-Key` (§11). |
| Dependent impact | When a fact becomes `DISPUTED` or `SUPERSEDED`, every dependent Assessment and IntelligenceProduct is flagged `review_required` with a link to the triggering decision. Published products are never mutated; a correction review task is created. History is preserved. |
| Certainty | A claim SHALL NOT be returned or exported as a fact without a VerificationDecision. |
| Audit | Claim creation, every VerificationDecision and every fact status change emit audit events (§27). |

# 17. Search API

``` text
GET /api/v1/search?q=company+x&type=entity,evidence&case_id=...&status=...&page[size]=25
```

| **Response element** | **Rule** |
|----|----|
| results | Only authorized canonical/derived references. |
| snippet | Permission-safe; SHALL not reveal hidden protected content. |
| facets | Permission-filtered counts. |
| rank/score | Search relevance only; SHALL not be labeled risk/suspicion. |
| source | Canonical object type + stable ID. |
| projection marker | Derived/extracted text result identifies derivative source when applicable. |

# 18. Graph API

``` text
POST /api/v1/graph/query
{
  "case_id": "...",
  "seed_entities": ["..."],
  "relationship_types": ["OWNS","DIRECTOR_OF"],
  "depth": 2,
  "include_value_flows": true
}
```

| **Element** | **Requirement** |
|----|----|
| Nodes | Canonical object references with authorized display metadata. |
| Edges | Relationship/ValueFlow IDs, type, dates, confidence/status, provenance refs as authorized. |
| Derived metrics | Explicitly marked derived with algorithm/version/input scope. |
| Path query | Output means path in authorized graph, not proof of culpability/causality. |
| Limits | Server enforces depth/node/edge budgets and rate limits. |
| Rebuildability | Graph projection is never the sole canonical source. |

# 19. Product, Review and Dissemination API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /products | Intelligence product library/create. |
| GET/PATCH | /products/{productId} | Current draft/version-aware edit. |
| GET | /products/{productId}/versions | Version history. |
| POST | /products/{productId}/submit-review | Freeze/submit version. |
| GET | /reviews | Review queue. |
| GET | /reviews/{reviewId} | Review workspace data. |
| POST | /reviews/{reviewId}/request-changes | Decision action. |
| POST | /reviews/{reviewId}/approve | Independent approval. |
| POST | /reviews/{reviewId}/reject | Reject with rationale. |
| POST | /disseminations | Create dissemination request. |
| POST | /disseminations/{id}/approve | Authorize recipient/purpose/package scope. |
| GET | /disseminations/{id}/export-candidates | Authorized selectable export objects. |
| POST | /disseminations/{id}/exports | Generate export package. |
| GET | /sharing-log | Immutable authorized sharing records. |

# 20. Administration and Audit API

| **Method** | **Endpoint** | **Purpose** |
|----|----|----|
| GET/POST | /vocabularies | Controlled vocabulary management. |
| GET/POST | /retention-policies | Retention policy management. |
| GET/PATCH | /case-memberships/{id} | Case membership/access administration. |
| GET | /audit-events | Permission-aware immutable audit explorer. |
| GET | /system/info | Build/schema/API version and safe diagnostics. |
| GET | /system/health | Health check; public/private detail according to deployment. |
| GET | /capabilities | Optional principal/deployment capability summary. |

# 21. Protected Source API Boundary

- Protected-source identity SHALL use dedicated endpoints and authorization scopes separated from ordinary source/evidence APIs.

- Ordinary evidence/source payloads SHALL reference protected source through non-identifying handles where needed.

- Protected-source identity SHALL not be included in generic search, graph, audit payloads, export candidates or global capability summaries.

- API documentation/examples SHALL use synthetic values and SHALL not encourage clients to cache protected identity broadly.

``` text
/api/v1/protected-sources/...   # restricted namespace; not part of ordinary analyst client bundle by default
```

# 22. Asynchronous Jobs

| **Operation** | **Async?** | **Pattern** |
|----|----|----|
| Large evidence processing | YES | Return 202 + job resource. |
| OCR/derivative generation | YES in Phase 2 | Job status + derived artifact on completion. |
| Large export package | YES | 202 + job; final download only after approval remains valid. |
| Graph projection rebuild | YES | Admin/operator job. |
| Normal CRUD | NO | Synchronous transaction. |
| Search | NO | Synchronous with timeout/rate limits. |

``` text
202 Accepted
{ "job": {"id":"job_...","status":"QUEUED","poll_url":"/api/v1/jobs/job_..."} }
```

# 23. File Transfer and Content Safety

- Uploads SHALL enforce server-side size/type policy and SHALL not trust browser MIME/extension alone.

- Original filenames are metadata; object storage keys are opaque.

- Content downloads SHALL use safe Content-Type/Content-Disposition and authorization on every request.

- Range requests MAY be supported for large evidence viewing.

- Active documents SHOULD be served in a way that prevents execution in the CS-AML origin context.

- Malware scanning/quarantine hooks SHALL not silently rewrite the original evidence; quarantine state is metadata/workflow.

# 24. Bulk Operations

| **Bulk action** | **MVP** |
|----|----|
| Bulk tag/classify low-risk metadata | MAY support with per-object authorization/results. |
| Bulk evidence export | Only through approved dissemination/export workflow. |
| Bulk entity merge | NOT supported. |
| Bulk deletion | NOT supported for ordinary analyst. |
| Bulk relationship import | MAY be later; each record requires provenance/validation. |
| Bulk audit retrieval | Privileged, paginated/rate-limited. |

# 25. Rate Limiting and Abuse Controls

- Authentication, search, graph traversal, export generation and upload endpoints SHOULD have differentiated limits.

- Rate-limit responses use 429 and MAY include Retry-After.

- Limits SHALL not reveal hidden resource counts.

- Privileged/bulk APIs require stronger authorization and audit.

- Automated clients/service accounts SHOULD have separately identifiable quotas.

# 26. API Security Requirements

| **ID** | **Requirement** |
|----|----|
| API-SEC-01 | TLS required outside explicitly isolated local development. |
| API-SEC-02 | All object access is authorized server-side using role + case/context + classification + need-to-know as applicable. |
| API-SEC-03 | Object IDs are not authorization secrets. |
| API-SEC-04 | Mass assignment is prevented by explicit writable-field schemas. |
| API-SEC-05 | Input validation and output encoding are applied consistently. |
| API-SEC-06 | CSRF protection applies to every unsafe method: browser auth is a cookie-based BFF session and requests SHALL carry `X-CSRFToken` (§4). *[v0.1.1 · A11]* |
| API-SEC-07 | The API is same-origin; CORS is disabled by default and any exception is explicit and minimal. *[v0.1.1 · A11]* |
| API-SEC-08 | Sensitive payloads are excluded/redacted from routine access logs. |
| API-SEC-09 | Export/download endpoints re-check authorization at retrieval time where appropriate. |
| API-SEC-10 | Schema/docs do not expose privileged endpoints to unauthorized clients as an access control mechanism; actual authorization still applies. |

# 27. Audit Semantics

| **Action** | **Audit expectation** |
|----|----|
| Create/update canonical object | Actor, action, object, version, timestamp, request ID; material before/after reference. |
| Entity merge/unmerge | Decision/rationale/evidence references + topology-impact record. |
| Assessment finalize | Version, author, confidence, gate state. |
| Review decision | Reviewer, product/version, decision, rationale. |
| Dissemination approval/export | Recipient/purpose/package/version/included object manifest. |
| Failed high-impact action | Security/audit event where policy requires. |
| Read access | Routine reads MAY be logged selectively; protected-source/access-sensitive reads SHOULD have stronger audit policy. |

# 28. API Schema and OpenAPI Requirements

- An OpenAPI 3.1 document SHALL be generated from the implementation, committed as `contracts/openapi.yaml`, linted in CI, used to generate the TypeScript client, and exercised by contract tests. *[v0.1.1 · A11]*

- Schemas SHALL identify required/nullable fields explicitly.

- Enums SHALL include stable machine values and descriptions.

- Examples SHALL use synthetic data.

- High-impact action endpoints SHALL document preconditions and conflict/error codes.

- Client TypeScript types SHALL be generated from `contracts/openapi.yaml`; generated code SHALL not replace domain semantics documentation. *[v0.1.1 · A11]*

> **Open items — not yet produced** *[v0.1.1 · A11]*  
> This package does not yet contain the OpenAPI artefact or full per-operation contracts. This document is a convention and endpoint baseline, not an executable contract. Outstanding:
> - `contracts/openapi.yaml` itself (OpenAPI 3.1), with CI lint and generated TypeScript client.
> - Full per-operation request/response schemas for every endpoint in §12–§22 and §16A.
> - Explicit required/nullable declarations per field.
> - Upload, async job and approval preconditions per operation (upload session states, job lifecycle and status enum, approval/re-approval and export validity rules).
> - Detailed contracts for task update, review comments and job lifecycle actions.
> - Pagination envelope: cursor/page fields of list responses are not yet locked (§8 states the query parameters only).
> - Policy-denial response details beyond the §9 error envelope.
> - Response code for a missing REQUIRED Idempotency-Key (§11).

# 29. Compatibility and Deprecation

| **Change** | **Policy** |
|----|----|
| Add optional response field | Compatible. |
| Add enum value | Potentially compatible only if clients are required to handle unknown values safely; announce. |
| Rename/remove field | Breaking; new major or migration window. |
| Change meaning of existing field | Breaking even if JSON shape unchanged. |
| Endpoint deprecation | Mark in schema/docs, announce removal version/date, provide replacement. |
| Controlled vocabulary change | Vocabulary versioning; historical records retain original term semantics. |

# 30. Verification and Contract Testing

| **Test class** | **Required verification** |
|----|----|
| Schema | Responses validate against OpenAPI/schema. |
| Authorization | Positive and negative tests for case membership/classification/protected source. |
| Non-disclosure | Unauthorized IDs/search/facets do not reveal hidden resource metadata. |
| Concurrency | Stale `If-Match` → 412 PRECONDITION_FAILED; missing `If-Match` → 428; workflow conflict → 409 STATE_CONFLICT; no overwrite in any case. *[v0.1.1 · A04]* |
| Idempotency | Retries do not duplicate selected actions; replay, key-reuse (422) and in-flight (409) behaviour per §11. *[v0.1.1 · A11]* |
| Evidence | Upload/finalize/hash/content authorization and lineage. |
| Analytical semantics | Flow classes, unknown/range values, candidate/disputed states preserved; `INSUFFICIENT_BASIS` round-trips unchanged; claim/fact transitions per §16A. *[v0.1.1 · A09, A10]* |
| Review/dissemination | Independent approval/preconditions/export manifest enforced. |
| Audit | Material actions create expected correlated audit records. |
| Performance | P0 list/search/graph endpoints meet documented MVP targets. |

# 31. API Definition of Done

| **Area** | **Done when** |
|----|----|
| Contract | Endpoint/resource has documented schema, methods, authorization context and error cases. |
| Traceability | Mapped to feature/SRS requirement. |
| Authorization | Positive/negative/non-disclosing tests pass. |
| Versioning | Mutable material resource has conflict semantics. |
| Audit | Material action emits required audit event/correlation. |
| Frontend | Generated/manual client integration handles loading/error/conflict states. |
| Docs | OpenAPI/examples updated with synthetic data. |
| Security | Input/output/file/download controls pass review. |
| Regression | Contract tests included in CI. |

# Annex A — Canonical Resource Baseline

| **Domain** | **Resources** |
|----|----|
| Case | Case, InvestigationQuestion/CharterVersion, Gate, Task, CaseActivity projection |
| Evidence | Source, EvidenceItem, EvidenceExtract, Derivative/Lineage, Claim, Fact, VerificationDecision *[v0.1.1 · A10]* |
| Identity | Entity, Identifier/Alias, MatchCandidate, MergeDecision |
| Relations/assets | Relationship, OwnershipInterest, ControlAssertion, Asset |
| Time/value | Event, Timeline projection, ValueFlow, ValueFlowLeg |
| Analysis | Indicator, Typology, TypologyMatch, Hypothesis, IntelligenceGap, Assessment |
| Products | IntelligenceProduct, ProductVersion, Review, Dissemination, ExportPackage, SharingLog |
| Governance | Vocabulary, RetentionPolicy, CaseMembership, AuditEvent, Job |

# Annex B — Request Review Checklist

- Is the canonical resource and case/context scope explicit?

- Does the endpoint preserve unknown/inference/candidate/value-flow class semantics?

- What authorization and non-disclosure behavior applies?

- Is a version token/precondition required?

- Could a retry duplicate a high-impact action; is idempotency needed?

- What audit event/correlation must be emitted?

- Could error details leak protected content?

- Are pagination/filter/sort fields allowlisted?

- Does the response include only the minimum authorized data needed?

- Is this canonical data or a derived projection, and is that distinction explicit?

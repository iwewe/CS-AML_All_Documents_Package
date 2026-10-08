**CS-AML**

**Frontend Architecture & State Management Specification**

Version 0.1.1

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML Frontend Architecture & State Management Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Purpose**  
> Proposed normative frontend architecture baseline (draft for review) for the CS-AML MVP. *[v0.1.1 · A01]* It defines frontend module boundaries, routing, state ownership, server-state synchronization, form and visualization state, authorization-aware rendering, concurrency handling, error recovery, accessibility, testing and frontend delivery conventions.

> **Core architecture axiom**  
> Frontend state SHALL preserve canonical server truth, workflow versioning, permission boundaries and analytical uncertainty. The client SHALL NOT manufacture durable truth by promoting local, cached, inferred or visualization-only state into canonical state.

Status: Proposed normative frontend implementation baseline for MVP 0.1 (draft for review) *[v0.1.1 · A01]*

Dependencies: SRS v0.1.1 · Technical Stack v0.1.1 · API Specification v0.1.1 · UX v0.1.1 · IA v0.1.1 · Screen Inventory v0.1.1 · Wireframe v0.1.1 · UI Design System v0.1.1 · High-Fidelity UI v0.1.1 · Storybook (Component Inventory) v0.1.1 (Markdown, `Documents/*_v0.1.1.md`) *[v0.1.1 · A01]*

# Document Control

| **Attribute** | **Value** |
|----|----|
| Document ID | CSAML-FEARCH-0.1 |
| Version | 0.1.1 |
| Status | Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]* |
| Primary audience | Frontend Engineer, UX Engineer, Tech Lead, QA, Security Reviewer |
| Reference stack | React 19 + TypeScript + Vite + Tailwind CSS 4 + shared Storybook design system |
| API assumption | Versioned same-origin REST API (`/api/v1`) with server-side BFF session; canonical authorization and validation remain server-side (API Specification v0.1.1) *[v0.1.1 · A11]* |
| Normative verbs | SHALL / MUST / SHOULD / MAY |

# 1. Scope and Non-Goals

This specification defines the frontend application architecture for the CS-AML MVP. It translates the screen and component specifications (draft for review) into implementation boundaries and state-management rules. It does not define backend business logic, canonical data schemas, authorization policy decisions, or API endpoint payloads; those are owned by backend specifications and the separate API Specification. *[v0.1.1 · A01]*

| **In scope** | **Out of scope** |
|----|----|
| Feature-module organization, routing, data fetching, cache ownership, local state, forms, optimistic updates, concurrency, error handling, authorization-aware UI, visualization state, testing | Database model, server-side policy engine, evidence storage implementation, backend transaction rules |
| Frontend adaptation of canonical analytical semantics | New analytical semantics not present in framework/data model |
| Client security behavior and non-leakage rules | Treating UI hiding as an authorization control |

> **Security boundary**  
> Hiding a control or object in the UI is a usability measure, not an authorization decision. Every protected read or mutation SHALL remain authorized and validated by the API.

# 2. Architecture Principles

| **ID** | **Principle** | **Requirement** |
|----|----|----|
| FE-P01 | Server truth first | Canonical objects, permissions, versions, approvals and audit-relevant state originate from server responses. |
| FE-P02 | State by ownership | Server state, form state, navigation state, workflow state, visualization state and ephemeral UI state SHALL have distinct owners. |
| FE-P03 | URL is durable navigation state | Object IDs, case context, active tabs, filters and shareable search context SHOULD live in URL state where safe. |
| FE-P04 | No monolithic global store | A single application-wide mutable store SHALL NOT become the default home for all state. |
| FE-P05 | Permission-aware by construction | Components receive authorized data; restricted metadata SHALL not be cached or rendered merely because a route was guessed. |
| FE-P06 | Version-aware editing | Editable canonical resources SHALL detect stale versions and prevent silent overwrite. |
| FE-P07 | Derived views stay derived | Graph layouts, timeline positions and view filters SHALL NOT silently mutate canonical relationships, events or value flows. |
| FE-P08 | Uncertainty preserved | Claim, fact, candidate, disputed, unknown and flow-class semantics persist through cache, form, visualization and export preview. |
| FE-P09 | Recover locally | Component/feature failures SHOULD degrade locally before forcing a whole-app failure. |
| FE-P10 | Accessible state | State changes, validation, loading and errors are exposed to keyboard and assistive technology. |

# 3. Reference Frontend Stack

| **Concern** | **Reference** | **Rule** |
|----|----|----|
| Runtime | React 19 + TypeScript | Strict TypeScript SHALL be enabled; `any` is exceptional and justified. |
| Build | Vite | Environment variables exposed to browser are explicitly allowlisted. |
| Styling | Tailwind CSS 4 + semantic CSS variables | Feature code consumes semantic tokens; raw status colors are prohibited where tokens exist. |
| Routing | React Router or equivalent | Routes use stable canonical IDs; case context is explicit. |
| Server state | TanStack Query or equivalent | Remote cache, invalidation, deduplication and mutation lifecycle are centralized here. |
| Forms | React Hook Form + schema validation or equivalent | Form state stays local to form boundary; server validation is mapped back to fields. |
| Schema types | TypeScript client/types generated from `contracts/openapi.yaml` (OpenAPI 3.1; not yet produced — open item in API Specification §28) | Handwritten duplicate DTO types SHOULD be minimized; enum types use the UPPER_SNAKE_CASE wire values. *[v0.1.1 · A09, A11]* |
| Visualization | Cytoscape.js + approved timeline/value-flow primitives | Visualization state remains non-canonical. |
| Storybook | Storybook | Shared components and compound patterns require stories/test coverage. |
| Tests | Vitest/Jest + Testing Library + Playwright | Behavior first; implementation-detail tests discouraged. |

# 4. Application Module Architecture

``` text
frontend/
  src/
    app/
      router/
      providers/
      error-boundaries/
    features/
      cases/
      evidence/
      entities/
      relationships/
      assets/
      timeline/
      valueflows/
      typologies/
      hypotheses/
      assessments/
      search/
      graph/
      products/
      reviews/
      dissemination/
      administration/
      audit/
    shared/
      api/
      auth/
      components/
      design-system/
      hooks/
      types/
      utils/
    test/
```

| **Layer** | **May depend on** | **SHALL NOT depend on** |
|----|----|----|
| app | features, shared | Feature internals via deep imports |
| feature | shared, explicitly published contracts from another feature | Another feature’s private components/store internals |
| shared API/auth | generic infrastructure | Feature UI |
| design-system | tokens, generic utilities | Case/entity/business-specific behavior |
| screen composition | feature public components, design system | Backend implementation details |

> **Boundary rule**  
> Cross-feature imports SHOULD use explicit public barrels/contracts. If two features repeatedly depend on the same domain presentation primitive, promote that primitive deliberately rather than creating circular imports.

# 5. Routing and Navigation State

``` text
/cases
/cases/:caseId/overview
/cases/:caseId/evidence/:evidenceId
/entities/:entityId?case=:caseId
/analysis/value-flows?case=:caseId
/products/:productId/review
/search?q=...&type=entity&case=...
```

| **State** | **URL?** | **Reason** |
|----|----|----|
| Canonical object ID | YES | Deep-linkable identity. |
| Case context | YES where relevant | Same entity may be opened inside different authorized case contexts. |
| Primary tab/section | YES | Back/forward navigation and shareable context. |
| Search query/facets | YES unless sensitive query policy forbids | Reproducibility and navigation. |
| Inspector open/closed | Usually NO | Ephemeral view state. |
| Unsaved form values | NO | Sensitive local state; do not leak into history/URL. |
| Graph viewport coordinates | Usually NO | Derived visualization state; MAY persist as named saved view later. |
| Protected-source identifiers | NO in ordinary route/query strings | Avoid browser history/log leakage. |

# 6. State Taxonomy and Ownership

| **State class** | **Examples** | **Owner** | **Persistence** |
|----|----|----|----|
| Server state | Case, entity, evidence metadata, assessment version, review status | Query/cache layer backed by API | Remote canonical; client cache ephemeral |
| Form state | Unsaved charter fields, hypothesis edit, relationship editor | Form boundary | Memory; optional safe draft policy only |
| Navigation state | Route, case context, active tab, filters | Router/URL | Browser history |
| Workflow UI state | Wizard step, review panel state | Feature component | Memory; derive from server when material |
| Visualization state | Selected graph nodes, zoom, hidden layers, timeline scale | Visualization controller | Memory; optional saved view, never canonical relationship truth |
| Ephemeral UI state | Modal open, tooltip, toast, drawer | Local component | Memory |
| Session/auth state | Authenticated principal, session expiry, coarse capabilities (from `GET /auth/session`) | Auth provider | Memory only; the HttpOnly session cookie is not readable by JavaScript and no tokens exist in the browser *[v0.1.1 · A11]* |
| Preference state | Density, reduced motion, column visibility | Preference service/local storage if approved | Local or server preference; no sensitive case content |

> **Hard rule**  
> Canonical server state SHALL NOT be copied into a global mutable store merely to make it easy to access. Use normalized/query cache access and feature selectors instead. Duplicate copies create version drift and authorization leakage risk.

# 7. Server-State Management

- Every query key SHALL include all dimensions that materially change authorization or representation, including canonical object ID, case context where relevant, and relevant filters.

- Cache entries SHALL be invalidated or updated after successful canonical mutations according to explicit mutation contracts.

- Unauthorized/forbidden responses SHALL not be cached as if they were ordinary empty data.

- Query retries SHOULD be disabled or limited for 401/403/404 non-disclosing authorization outcomes. Mutations SHALL NOT be automatically retried on 409, 412, 422 or 428; automatic retry of a high-impact command after a network failure SHALL reuse the same `Idempotency-Key`. *[v0.1.1 · A04, A11]*

- Background refetch MAY refresh read screens; editable screens require version-aware reconciliation before replacing user-visible data.

- Prefetch MAY be used for ordinary objects but SHALL NOT prefetch protected-source identity or `RESTRICTED`/`SOURCE_PROTECTED` content without an explicit authorized task. *[v0.1.1 · A08]*

- Client caches SHALL be cleared on logout/session revocation (including a 401 after back-channel revocation) and SHOULD be scoped to the authenticated principal. *[v0.1.1 · A11]*

| **Query example**     | **Key shape**                                      |
|-----------------------|----------------------------------------------------|
| Case overview         | \["case", caseId, "overview"\]                     |
| Entity detail in case | \["entity", entityId, {caseId}\]                   |
| Evidence reader       | \["evidence", evidenceId, {caseId, version}\]      |
| Search                | \["search", {q,type,caseId,filters,page}\]         |
| Review product        | \["product", productId, {version, mode:"review"}\] |

# 8. Mutation and Concurrency Model

| **Mutation type** | **Optimistic?** | **Rule** |
|----|----|----|
| Low-impact preference | YES | May update locally and rollback on failure. |
| Task status | Conditional | Only if authorization and version conflicts are simple; failure visibly rolls back. |
| Entity merge/unmerge | NO | High-impact/reversible canonical action; wait for server result. |
| Evidence metadata affecting provenance | NO | Server validates integrity/version. |
| Assessment finalization | NO | Requires server gate/version validation. |
| Review approval/rejection | NO | High-impact decision and independence checks. |
| Dissemination approval/export | NO | Server authorization/audit must succeed first. |
| Graph selection/layout | Local only | Not a canonical mutation. |

> **Concurrency contract** *[v0.1.1 · A04]*  
> Editable canonical resources carry `record_version`, returned as `ETag: "<record_version>"` on GET. Every mutation of a versioned resource SHALL send `If-Match: "<record_version>"` from the version the user is editing. The frontend SHALL NOT silently overwrite the newer server version. Response mapping:
>
> | **Response** | **Frontend behavior** |
> |----|----|
> | 412 PRECONDITION_FAILED | "Record changed" recovery: keep the user's unsaved edits, show `details.current_record_version`, offer compare/reload/re-apply. |
> | 409 STATE_CONFLICT | Workflow message explaining the state that blocks the action (e.g. gate not satisfied, already finalized); refetch the object state; no compare/merge flow. |
> | 428 PRECONDITION_REQUIRED | Client bug (missing `If-Match`): generic error with correlation ID, reported to telemetry; never shown as a user conflict. |
> | 409 IDEMPOTENCY_IN_PROGRESS | Wait per `Retry-After` and poll/retry with the same key. |
> | 422 IDEMPOTENCY_KEY_REUSED | Client bug: a key was reused with a different payload. |
>
> The v0.1 error code `VERSION_CONFLICT` is retired and SHALL NOT be mapped.

# 9. Form Architecture

- Forms SHALL use client-side schema validation for immediate feedback and server-side validation as authority.

- Unknown, null, approximate and zero SHALL remain distinct values where the domain model distinguishes them.

- Unsaved changes SHALL trigger safe-navigation protection for material forms.

- Form submission SHALL preserve field-level server errors and non-field errors.

- High-impact forms SHALL include explicit review summary before final action where defined by UX.

- Dynamic controlled-vocabulary fields SHALL retain term IDs and display labels; labels alone are not canonical values.

- Controlled enumerations are submitted and stored in client state as UPPER_SNAKE_CASE wire values (Data Model Annex A registry), e.g. `flow_class` `DIRECT`/`DOCUMENTED`/`RECONSTRUCTED`/`HYPOTHETICAL`; display labels are separate and translatable. *[v0.1.1 · A09]*

- `confidence.level` `INSUFFICIENT_BASIS` SHALL be rendered as its own neutral state (not as a level below Low, not as adverse, not as empty). Forms, sorting, filters and export previews SHALL NOT convert it to `LOW`, null, zero, or drop it; a null level is shown as "not yet assessed" and is allowed only on drafts. Rationale is required for every level. *[v0.1.1 · A09]*

- Protected-source identity SHALL not be auto-filled into ordinary evidence or export forms.

| **Form family** | **Draft behavior** |
|----|----|
| Case/charter | Local unsaved state; server version after save. |
| Evidence upload | Upload session state; failed upload does not create completed evidence. |
| Entity/relationship | Local edit; canonical mutation on save. |
| Hypothesis/assessment | Local edit + optional explicit server draft version; no invisible autosave that changes audit-relevant content. |
| Product editor | Versioned draft; autosave MAY be used if server-side version/audit semantics are explicit. |
| Review/dissemination | No optimistic finalization; server response authoritative. |

# 10. Authorization-Aware Rendering

| **Pattern** | **Requirement** |
|----|----|
| Capability check | UI MAY use server-provided capabilities to show/disable actions. |
| Object access | No component SHALL infer access solely from role name; object/case policy matters. |
| Non-disclosing denial | A 404/403 policy response SHALL map to the approved non-leaking system state. |
| Protected source | Protected-source identity components SHALL exist in separately permissioned feature boundary and SHALL not be imported into ordinary evidence screens. |
| Export preview | Only server-authorized export candidates are rendered as selectable. |
| Counts/facets | Counts returned by API are treated as already permission-filtered; frontend SHALL not reconstruct hidden totals. |
| Classification | Render the five levels from wire values `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED` (labels Public … Source-protected) together with access labels. An unknown or missing classification value SHALL render as restricted (fail closed), never default to Public. *[v0.1.1 · A08]* |

# 11. Error and Recovery Architecture

| **Failure class** | **UI behavior** |
|----|----|
| Network/transient | Local retry with clear status; preserve safe unsaved state where feasible. |
| Authentication expired | On 401, suspend protected work and re-authenticate via `GET /auth/login`; do not discard local form without warning where secure recovery is possible. *[v0.1.1 · A11]* |
| Authorization changed | Remove restricted cached content and transition to non-disclosing access state. |
| Validation | Field/non-field errors near source; no generic toast-only failure. |
| Concurrency conflict (412 PRECONDITION_FAILED) | Open "record changed" compare/reload/resolve flow; never auto-force overwrite. *[v0.1.1 · A04]* |
| Workflow state conflict (409 STATE_CONFLICT) | Show workflow message and refreshed state; no compare flow. *[v0.1.1 · A04]* |
| Missing precondition (428) / CSRF failure (403) | Treat as client defect: generic error with correlation ID; for CSRF, refresh the token via session bootstrap once before reporting. *[v0.1.1 · A04, A11]* |
| Integrity warning | Blocking error treatment for evidence integrity issue. |
| Partial feature failure | Local error boundary keeps surrounding case workspace usable. |
| Fatal application failure | Global recovery boundary with correlation ID; no sensitive payload in error display/log. |

# 12. Visualization State Management

| **Domain** | **Canonical state** | **Frontend-only state** |
|----|----|----|
| Graph | Entity/Relationship/Asset/ValueFlow objects | node positions, selection, zoom, hidden edge classes, inspector state |
| Timeline | Event records and temporal precision | scale, viewport, filters, expanded cards |
| Value Flow | ValueFlow/legs/class/evidence | canvas layout, selected leg, comparison overlays |
| Hypothesis matrix | Hypothesis/evidence link disposition | sorting, collapsed rows, temporary filter |
| Evidence reader | Evidence/Extract objects | page viewport, zoom, transient selection before extract save |

> **Derived-state rule**  
> Layout algorithms, centrality calculations, path highlighting and client-side clustering MAY assist navigation, but SHALL remain visibly derived and SHALL NOT create canonical relationships, risk labels or adverse assessment state.

# 13. Search and Filter State

- Global search query and approved facets SHOULD be URL-addressable.

- Facet counts are server-provided permission-filtered values.

- Debounced queries SHALL be cancellable to avoid displaying stale results after a newer query completes.

- Sensitive query strings MAY require history/logging safeguards; protected-source identity SHALL not be exposed through ordinary global search.

- Search results SHALL display canonical object type/status and context without manufacturing analytical priority from ranking position.

# 14. Session, Authentication and Logout

- Browser authentication is a server-side session (BFF) as defined in API Specification v0.1.1 §4. The frontend is not an OIDC client: it holds no client ID/secret, never receives access, refresh or ID tokens, and SHALL NOT send `Authorization: Bearer`. *[v0.1.1 · A11]*

- Login: navigate the browser to `GET /auth/login` (full-page redirect); the backend completes `GET /auth/callback` and sets the `__Host-csaml_session` cookie (HttpOnly, Secure, SameSite=Lax, Path=/). *[v0.1.1 · A11]*

- Bootstrap: on app start and after login, call `GET /auth/session` to obtain principal, session expiry and coarse capabilities; 401 means unauthenticated. *[v0.1.1 · A11]*

- CSRF: every unsafe request (POST/PUT/PATCH/DELETE) SHALL send the Django CSRF token in the `X-CSRFToken` header. All API calls are same-origin (`/api/v1`) with credentials included; no cross-origin API calls. *[v0.1.1 · A11]*

- Logout: `POST /auth/logout`, then clear query caches, feature state and sensitive in-memory state. The same clearing SHALL happen on user switch, on any 401 indicating session expiry or revocation (including Keycloak back-channel logout), and on a `GET /auth/session` principal change. *[v0.1.1 · A11]*

- Idle/session expiry behavior SHALL provide clear re-authentication path.

- Browser storage SHALL not contain raw evidence content, protected-source identity or any authentication token. *[v0.1.1 · A11]*

- Multi-tab session expiry SHOULD converge safely without preserving stale privileged UI.

# 15. Component and Feature Composition

| **Layer** | **Examples** | **State rule** |
|----|----|----|
| Design system | Button, DataGrid, Badge, ClassificationBanner | No business fetching; presentational/interaction state only. |
| Domain shared | EvidenceCitation, ProvenanceTrail, FlowClassBadge, EntityBlock | Receives typed domain props; no screen-specific navigation assumptions. |
| Feature component | EntityMatchCompare, HypothesisMatrix | May own feature queries/mutations and local feature state. |
| Screen container | SCR-ENT-005, SCR-HYP-001 | Coordinates route context, feature components, error/loading states. |
| App shell | Header, primary nav, session | Owns global navigation/session only. |

# 16. Performance and Rendering Strategy

| **Concern** | **Requirement** |
|----|----|
| Route splitting | Feature routes SHOULD be code-split to reduce initial bundle. |
| Large tables | Use pagination/virtualization where measured data volume requires it; virtualization SHALL preserve keyboard/accessibility. |
| Graph | Progressive rendering and node limits SHOULD be explicit; large graph failure SHALL degrade to list/filter tools. |
| Evidence reader | Stream/page-render rather than loading huge files wholly into memory where possible. |
| Search | Cancel stale requests; cache recent authorized queries briefly. |
| Re-render control | Memoization SHOULD follow measured cost, not blanket use. |
| Bundle budget | Critical route bundles SHOULD be monitored in CI with agreed thresholds. |

# 17. Accessibility Architecture

- Route changes SHALL move focus/announce context appropriately.

- Loading, error, save success and validation states SHALL be programmatically perceivable.

- Graph/timeline/value-flow views SHALL have an accessible list/table alternative that references the same canonical objects.

- Keyboard focus SHALL remain recoverable after modal/drawer close and after dynamic mutations.

- Reduced-motion preference SHALL apply to graph transitions and other animations.

- Virtualized tables SHALL retain semantics and keyboard navigation.

# 18. Frontend Security Requirements

| **ID** | **Requirement** |
|----|----|
| FE-SEC-01 | No authorization decision relies solely on hidden/disabled UI. |
| FE-SEC-02 | Sensitive API errors SHALL be rendered using non-disclosing approved states. |
| FE-SEC-03 | No raw evidence/protected-source content in analytics, telemetry breadcrumbs or routine console logs. |
| FE-SEC-04 | External links from evidence SHOULD use safe rel/referrer behavior according to policy. |
| FE-SEC-05 | HTML/markdown/user content SHALL be safely rendered; no unsanitized injection. |
| FE-SEC-06 | File previews SHALL be sandboxed/isolated as appropriate and not execute active content. |
| FE-SEC-07 | Browser storage use for case-sensitive state requires explicit security review. |
| FE-SEC-08 | Logout/user switch clears sensitive caches and feature state. |
| FE-SEC-09 | No authentication tokens in JavaScript-accessible memory or storage; no `Authorization: Bearer` from the browser; `X-CSRFToken` on every unsafe method. *[v0.1.1 · A11]* |

# 19. Testing Strategy

| **Layer** | **Minimum tests** |
|----|----|
| Design-system component | Storybook stories + interaction + accessibility + visual regression. |
| Feature component | Behavior, permission variants, loading/error, domain-state semantics. |
| Data hooks | Query keys, invalidation, mutation error mapping, conflict handling (412 / 409 / 428 mapping per §8), `INSUFFICIENT_BASIS` round-trip. *[v0.1.1 · A04, A09]* |
| Route/screen | Critical happy path + permission denied + stale version + responsive smoke. |
| End-to-end | Case → evidence → entity → value flow → hypothesis → assessment → review → dissemination. |
| Security | Direct route guesses, cached-data logout, hidden-action API bypass expectation, non-leaking denied states. |
| Accessibility | Keyboard, focus, announcements, graph/list alternatives. |

# 20. Observability and Telemetry

- Frontend errors SHOULD carry correlation/request IDs when provided by API.

- Operational telemetry SHALL avoid case titles, evidence snippets, protected-source identities and free-text analytical content.

- Performance metrics MAY include route load, API latency categories, rendering time and error rate using non-sensitive identifiers.

- User analytics SHALL follow the privacy specification; no keystroke/session replay over sensitive investigation screens by default.

# 21. Frontend Configuration and Feature Flags

| **Config** | **Rule** |
|----|----|
| API base URL | Build/deployment configuration; no hardcoded production URL. |
| OIDC config | None in the browser bundle: OIDC client configuration lives server-side (BFF); the frontend only knows the same-origin `/auth/*` endpoints. *[v0.1.1 · A11]* |
| Feature flags | Server/environment policy is authoritative for high-risk features; client flag alone cannot enable API capability. |
| Build metadata | Version/commit SHOULD be visible in diagnostics. |
| Experimental graph/AI features | Disabled by default unless approved deployment policy enables them. |

# 22. Screen-to-Feature Ownership Examples

| **Screen** | **Feature owner** | **Primary state owners** |
|----|----|----|
| SCR-CASE-003 | cases | case server state; route caseId; local panel state |
| SCR-EVD-003 | evidence | evidence server state; reader viewport; extract draft form |
| SCR-ENT-005 | entities | candidate server state; compare UI state; merge mutation |
| SCR-VAL-001 | valueflows | flow server state; filters in URL; canvas selection/layout local |
| SCR-HYP-001 | hypotheses | hypothesis server state; matrix filters local; edits form state |
| SCR-REV-002 | reviews/products | product version server state; comment form; approval mutation |
| SCR-DIS-002 | dissemination | authorized export candidates server state; selection form; export mutation |

# 23. Frontend Definition of Done

| **Area** | **Done when** |
|----|----|
| Architecture | Feature is in correct module and does not create circular/private cross-feature dependencies. |
| State ownership | Remote, form, route, visualization and ephemeral state have explicit owners. |
| Authorization | Denied/changed permissions are handled without data leakage; server remains authoritative. |
| Concurrency | Editable canonical records handle stale versions safely. |
| UI semantics | Shared design-system/domain components preserve uncertainty/provenance semantics. |
| Accessibility | Keyboard, focus and state announcements verified. |
| Tests | Unit/integration/screen/E2E coverage appropriate to risk; Storybook coverage for shared components. |
| Security | Sensitive content absent from logs/storage/telemetry beyond approved mechanisms. |
| Performance | Critical route/render performance meets MVP thresholds. |
| Traceability | Screen IDs and SRS/feature references included in implementation issue/test metadata where practical. |

# 24. Architecture Decision Baseline

| **Decision** | **Baseline** |
|----|----|
| FE-ADR-001 | Feature-oriented modular React application; no page-folder monolith. |
| FE-ADR-002 | TanStack Query-equivalent owns server state; no duplicate global canonical store. |
| FE-ADR-003 | Form library owns unsaved form state; durable draft requires explicit server object. |
| FE-ADR-004 | React Router-equivalent owns shareable navigation/filter context. |
| FE-ADR-005 | Visualization controllers own layout/selection; graph layout is not canonical truth. |
| FE-ADR-006 | Shared component package/design system before feature-local duplicates. |
| FE-ADR-007 | Version-aware mutations for canonical editable objects. |
| FE-ADR-008 | No offline-first evidence cache in MVP. |

# Annex A — State Ownership Decision Tree

``` text
Is the value canonical or returned by API?
  YES → Server/query state.
  NO → Is it an unsaved user edit?
    YES → Form state.
    NO → Must it survive/share via URL/back button?
      YES → Router/URL state.
      NO → Is it visualization-only (selection/layout/zoom)?
        YES → Visualization controller state.
        NO → Is it transient UI chrome?
          YES → Local component state.
          NO → Define explicit feature ownership; do not default to global store.
```

# Annex B — Frontend Review Checklist

- No canonical object copied into unversioned global mutable state.

- Query key includes relevant case/context dimensions.

- Logout/user switch clears sensitive caches.

- 403/404 non-disclosing states handled correctly.

- Unknown/null/zero distinctions preserved.

- No optimistic high-impact approval/merge/dissemination.

- Stale-version conflict tested: 412 → "record changed" recovery; 409 → workflow message; 428 → client bug. *[v0.1.1 · A04]*

- Graph/timeline/value-flow derived state does not mutate canonical objects.

- Keyboard/focus/error/loading states tested.

- No protected-source content in ordinary browser storage or telemetry.

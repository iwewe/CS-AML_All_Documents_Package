# ADR-0004 — Browser authentication: Keycloak OIDC with server-side (BFF) session

- **Status:** Accepted
- **Date:** 2026-10-08
- **Decision authority:** Product owner
- **Audit finding:** A11 (API contract gaps: session/bearer alternative was unresolved)
- **Affected specifications:** API Specification §3–§5, §26; Frontend Architecture §6–§8, §14; Technical Stack §3, §10–§11, §28, §32, §39; SRS-IF-003; MVP Breakdown ST-E1-01

## Context

The v0.1 specifications allowed either an OIDC session or a bearer token for the browser. Leaving that open would let the
frontend and backend teams build incompatible login, CSRF and cache-revocation behaviour. CS-AML handles source-protected
and restricted material, so tokens available to JavaScript would increase the impact of an XSS defect.

## Decision

- The Django backend is a **confidential OIDC client** of Keycloak (Authorization Code + PKCE). It acts as a
  backend-for-frontend (BFF).
- The browser holds only the session cookie `__Host-csaml_session` (HttpOnly, Secure, SameSite=Lax, Path=/). Access,
  refresh and ID tokens stay on the server and never reach JavaScript. Browsers do not send `Authorization: Bearer`.
- Unsafe methods require the Django CSRF token in the `X-CSRFToken` header.
- The API is same-origin (`/api/v1` behind Nginx), and CORS is disabled by default.
- Endpoints: `GET /auth/login`, `GET /auth/callback`, `POST /auth/logout`, `GET /auth/session`.
- Idle and absolute session timeouts are security-policy configuration. Keycloak back-channel logout SHOULD revoke
  sessions, and the frontend clears query caches on logout, 401 or revocation.
- Machine/service API clients are out of MVP scope and need a separate ADR.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| SPA public client with PKCE and bearer tokens in the browser | Tokens are reachable by injected script; refresh-token handling in the browser adds risk for restricted/source-protected data |
| Both mechanisms supported | Two security models to test; ambiguity was the audit finding itself |

## Consequences

- CSRF protection is mandatory and must be covered by negative tests.
- Session store and revocation are server responsibilities; horizontal scaling needs a shared session store.
- OpenAPI (`contracts/openapi.yaml`) documents cookie authentication only.

## Verification (not yet run)

- Negative tests: unsafe request without or with an invalid CSRF token is rejected; a request with a bearer header and no
  session is rejected.
- A browser storage inspection after login shows no tokens.
- Logout and back-channel revocation invalidate the session, and the UI clears cached data.

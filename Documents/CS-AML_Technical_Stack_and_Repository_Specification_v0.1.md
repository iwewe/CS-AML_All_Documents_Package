# CS-AML Technical Stack & Repository Specification v0.1

**Status:** Normative implementation specification for MVP 0.1

## Core engineering decision
CS-AML MVP SHALL use a modular monolith with PostgreSQL as the canonical analytical store, S3-compatible evidence storage, Redis/Celery for asynchronous work, standards-based OIDC, and a React/TypeScript analyst interface. Search and graph capabilities remain rebuildable projections; they are not canonical truth.

## Reference stack
- Ubuntu Server 24.04 LTS
- Docker Engine + Compose v2
- Python 3.12
- Django 5.2 LTS + Django REST Framework
- PostgreSQL 17 (+ PostGIS 3.5 where needed)
- Redis 7.x + Celery 5.x
- S3-compatible evidence storage (MinIO reference)
- Keycloak 26.x / standards-compliant OIDC
- React 19 + TypeScript + Vite + Tailwind CSS 4
- Cytoscape.js for MVP investigation graph
- PostgreSQL FTS/trigram search for MVP
- Nginx + Gunicorn
- OpenTelemetry + Prometheus/Grafana-compatible observability
- GitHub Actions or equivalent CI/CD

## Repository strategy
Monorepo with `backend/`, `frontend/`, `infra/`, `docs/`, `scripts/`, `tests/`, and `fixtures/`. Backend domain modules map to CS-AML capabilities: cases, evidence, entities, relationships, assets, timeline, valueflows, typologies, hypotheses, assessments, search, graph, products, reviews, dissemination, governance and audit.

## Deferred from MVP
Dedicated OpenSearch, Neo4j/Memgraph, Kubernetes, event bus, microservices and AI gateway are deferred until measured requirements justify them.

## Release rule
The MVP is technically releasable only after the full SRS end-to-end case-to-intelligence-product scenario passes, including negative authorization tests and tested backup/restore.

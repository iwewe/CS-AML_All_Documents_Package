# CS-AML Frontend Architecture & State Management Specification v0.1

**Status:** Normative frontend implementation baseline for MVP 0.1

## Core architecture axiom
Frontend state SHALL preserve canonical server truth, workflow versioning, permission boundaries and analytical uncertainty. The client SHALL NOT manufacture durable truth by promoting local, cached, inferred or visualization-only state into canonical state.

## Reference stack
React 19 + TypeScript + Vite + Tailwind CSS 4; TanStack Query-equivalent for server state; React Hook Form-equivalent for forms; React Router-equivalent for navigation; Cytoscape.js for graph; Storybook for shared components.

## State ownership
- Server state: remote canonical objects and versions
- Form state: unsaved edits
- Navigation state: URL/router context
- Visualization state: zoom/layout/selection/filter overlays
- Ephemeral UI state: modal/drawer/toast
- Session/auth state: authenticated principal and session
- Preference state: non-sensitive UI preferences

## Hard rules
- No monolithic global mutable store for canonical objects.
- Authorization remains server-side; UI hiding is not security.
- High-impact mutations are not optimistic.
- Editable canonical objects are version-aware.
- Logout/user switch clears sensitive caches.
- Protected-source identity is not stored in ordinary browser state.
- Graph/timeline/value-flow view state is derived, not canonical truth.

# ADR-0002 — Docusaurus (Public) + BookStack (Internal) for Documentation

| Field | Value |
|---|---|
| **Status** | Superseded by ADR-0004 |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | — |
| **Superseded by** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md) |

## Context

Orbeex needs documentation that is:

- high-quality (professional UI, search, navigation),
- docs-as-code (versioned with releases, reviewed via PR),
- deployable both **cloud-hosted for free** and **self-hosted** (including air-gapped),
- usable by both end users and the core team.

## Decision

- **Public documentation:** **Docusaurus** (docs-as-code, MDX/React, versioning, i18n,
  built-in search). Deploys free to GitHub Pages / Netlify / Vercel, or self-hosted as a
  static site.
- **Internal knowledge base:** **BookStack** (free, self-hosted, excellent UI).
- **API reference:** `rustdoc` published to GitHub Pages.
- **Approved alternatives:** MkDocs Material (simpler authoring), Wiki.js (internal KB),
  VitePress (lightweight Vue option).

## Rationale

Docusaurus is the industry standard for OSS documentation: it supports release-versioned
docs, full-text search, i18n, and free/self-hosted deployment — with no vendor lock-in.
BookStack covers non-versioned internal knowledge with a UI far better than a wiki folder
tree. Together they cover both audiences without duplication.

## Consequences

- **Positive:** professional UI, release-synced docs, zero cost, self-host capable.
- **Negative:** two systems to operate (public + internal); mitigated by clear ownership.
- **Follow-up:** docs build + broken-link check added to CI (Blueprint §7.3).

## Alternatives Considered

- **GitBook** — shifted to commercial; free tier restricted. Rejected.
- **MkDocs Material** — excellent, but less feature-complete for versioning/multi-audience.
  Kept as an approved fallback.
- **Confluence** — not self-hostable for free. Rejected.

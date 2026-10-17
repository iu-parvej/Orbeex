# ADR-0004 — Adopt Mintlify as the Documentation Platform

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | [ADR-0002](ADR-0002-documentation-platform.md) |

## Context

Orbeex needs documentation that is (a) high quality, (b) docs-as-code and versioned,
(c) usable by both end users and the core team, and (d) cost-effective for an open-source
project. The team has selected **Mintlify** (https://www.mintlify.com/) as the preferred
platform for its UI quality, AI-native tooling, and Git-based workflow.

## Decision

Adopt **Mintlify** as the primary public documentation platform for Orbeex.

- **Content lives in Git** as Markdown/MDX files; site config is `docs.json`. Full history
  is preserved and edited via normal PRs.
- **Authoring:** web editor + CLI (`mint dev` / `mintlify`) for local preview.
- **Hosting:** Mintlify-hosted (live at a `*.mintlify.site` address on Starter; custom
  domain also available on Starter).
- **Git sync:** connect the Orbeex repository (GitHub) — included on every plan.
- **Docs editing/pushing** is done through the repo (git push) and, where available, the
  Mintlify Developer API.

### Plan Selection

| Plan | Cost | Relevant Capabilities | Use for Orbeex |
|---|---|---|---|
| **Starter** | **$0/mo, free forever** | Full platform, custom domain, web editor, auth, **MCP server**, API playground, **Git sync**, search, 5 editor seats | Primary plan at launch |
| **Pro (OSS Program)** | **$0/mo for qualifying non-commercial OSS** | Everything in Starter + **Developer API**, **Admin APIs**, webhooks, analytics, AI Assistant, Autosync, preview deployments | **Apply for this** — unlocks API-driven editing |
| Pro (paid) | $450/mo annual | As above | Fallback if OSS program is declined |
| Enterprise | Contact | SSO/SCIM/RBAC, self-hosting, SLA | Later, if needed |

> **Note on "API access":** The Mintlify **Developer API and Admin APIs are Pro-only**
> (not on the free Starter plan). The free Starter plan still provides **Git sync** and an
> **MCP server**, so content can be pushed by editing MDX in Git, and can be edited
> through the web editor. Orbeex will **apply to the OSS Program for free Pro** to obtain
> the Developer API for automated/API-driven editing.

## Rationale

- Mintlify offers the highest-quality documentation UI with minimal maintenance.
- Docs-as-code (MDX + `docs.json`) keeps documentation in version control, satisfying
  Blueprint §7.3 (docs ship with the feature, reviewed via PR).
- Free Starter + a free-forever Pro tier for OSS make it cost-effective for an open-source
  project — including the Developer API once the OSS Program is granted.
- SOC 2 Type 2 and GDPR compliance meet Orbeex's enterprise bar.

## Consequences

- **Positive:** best-in-class UI, near-zero ops, Git-native, free for OSS, MCP server for
  agent access, clear upgrade path.
- **Negative:** Developer API requires Pro (apply to OSS Program); vendor-hosted (no true
  air-gapped self-hosting on the free/hosted tiers — Enterprise offers self-hosting).
- **Mitigation:** because docs are plain MDX in Git, we retain full portability — we can
  rebuild anywhere (e.g. Docusaurus/MkDocs) without content loss.
- **Follow-up:**
  - Apply to the Mintlify OSS Program for free Pro (Developer API).
  - Add a `docs-site/` workspace to the repo for Mintlify content (`docs.json`, `*.mdx`).
  - Keep `rustdoc` API reference published separately (GitHub Pages).

## Alternatives Considered

- **Docusaurus** (prior decision, ADR-0002) — excellent and fully self-hostable, but more
  ops and lower out-of-box polish than Mintlify. Retained as a **portability fallback**.
- **MkDocs Material** — simple and free/self-hosted; less feature-complete. Fallback.
- **GitBook** — commercial; free tier restricted. Rejected.
- **BookStack / Wiki.js** — good for internal KB; not chosen for public docs. Internal
  knowledge may still use a KB (see `brain/`), but public docs use Mintlify.

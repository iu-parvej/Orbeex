# ADR-0006 — Scalar Evaluated, Not Adopted; Mintlify Confirmed

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | — |
| **Related** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md), [ADR-0005](ADR-0005-mintlify-oss-program-sequencing.md) |

## Context

Orbeex operates a VPS and evaluated **Scalar** (https://github.com/scalar/scalar) as a
possible self-hosted alternative to Mintlify for documentation — with the question "is it
better than Mintlify on API, UI/UX, functionality, and everything?"

## Evaluation Findings

Scalar is two distinct products, which is decisive:

| Component | Nature | License | Self-hostable |
|---|---|---|---|
| Scalar **API Reference** (+ Client, parser, CLI, mock server) | Embeddable OpenAPI UI + API client | **MIT** | Yes, fully |
| Scalar **Docs** (hosted) | Mintlify-style hosted docs site (Markdown/MDX) | Proprietary, hosted | No (hosted) |

**Comparison summary:**

| Layer | Winner |
|---|---|
| Documentation site (prose/guides/user docs) | **Mintlify** (more polished; free Starter more generous) |
| API reference / OpenAPI playground | **Scalar** (best-in-class, MIT, self-hostable) |
| API client / testing | **Scalar** (Mintlify has none) |
| Self-hosting / sovereignty | **Scalar** (MIT components on VPS) |

**Pricing reality check:**
- Mintlify Starter: **free forever**, includes custom domain, web editor, **Git sync**, MCP
  server, API playground, 5 seats.
- Scalar Docs free: API docs + landing pages only; **Git Sync, MDX, custom domain are
  Pro-only ($150/mo)**.

## Decision

**Adopt Mintlify as Orbeex's documentation platform.** Scalar is **evaluated and not
adopted** for now.

- Rationale: Mintlify's free Starter plan is the most generous free tier for a
  documentation **site** (prose + guides + user docs), which is Orbeex's primary need, and
  it already satisfies our docs-as-code and AI-access requirements.
- Scalar's strengths (API reference, client) are **not required** at this stage and add a
  second system to operate.

## Consequences

- **Positive:** one documentation platform, zero cost, simplest operation.
- **Negative:** no best-in-class interactive OpenAPI reference today (Scalar's strength);
  Mintlify's API playground is used instead.
- **Reversible:** Scalar API Reference is **MIT** and can be **self-hosted on the VPS and
  embedded into a Mintlify MDX page at any time** in the future with no content loss
  (docs remain portable MDX). This option is retained, not rejected outright.

## Follow-up

- Continue with **free Mintlify Starter**; apply to the **OSS Program** later
  (ADR-0005).
- Revisit Scalar **only if/when** a first-class self-hosted interactive API reference is
  needed — then adopt the MIT API Reference as a VPS add-on, not a Mintlify replacement.

## Alternatives Considered

- **Scalar only** — rejected: free tier lacks Git sync/MDX/custom domain; more ops.
- **Mintlify + self-hosted Scalar API Reference (hybrid)** — deferred: good future option,
  not needed now; retained as the upgrade path.
- **Docusaurus + Scalar (fully self-hosted)** — deferred: more ops than needed.

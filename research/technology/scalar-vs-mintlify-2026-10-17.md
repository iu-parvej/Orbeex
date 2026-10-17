# Research Note — Scalar vs Mintlify (Documentation Platform)

**Date:** 2026-10-17
**Author:** Orbeex Core Team
**Status:** Concluded → decision recorded in `brain/decisions/ADR-0006`

## Question

Orbeex runs a VPS. Is **Scalar** (https://github.com/scalar/scalar) better than **Mintlify**
on API, UI/UX, functionality, self-hosting, and everything — enough to switch?

## Key Finding: Scalar is two products

| Component | Nature | License | Self-hostable |
|---|---|---|---|
| Scalar **API Reference** (+ Client, parser, CLI, mock server, editor) | Embeddable OpenAPI UI + API client | **MIT** | **Yes, fully** |
| Scalar **Docs** (hosted) | Mintlify-style hosted docs site (Markdown/MDX) | Proprietary, hosted | No (hosted) |

Mintlify ≈ "Scalar Docs" + "Scalar API Reference" combined, as one hosted platform.

## Comparison

| Dimension | Mintlify | Scalar |
|---|---|---|
| Docs site UX (prose/guides) | **Best-in-class** | Good; API-first DNA |
| Interactive API reference | Good | **Best-in-class** |
| API client (Postman-like) | None | **Full, MIT** |
| Free tier | **Starter free forever**: custom domain, Git sync, MCP, playground, 5 seats | Free: API docs + landing pages, 3 APIs, 1 seat; Git sync/MDX/custom domain = **Pro $150/mo** |
| Self-hosting | No (Enterprise only) | **Yes (MIT components, VPS)** |
| Developer API / programmatic edit | Pro | Registry/APIs Pro; **CLI free/MIT** |
| SDK generation / mock / registry | No | **Yes (broader API platform)** |
| Compliance | SOC 2 T2, GDPR | Self-host = we own compliance |
| License fit (Orbeex policy) | Service, not code | **MIT — allowed** |

## Verdict

- **API layer → Scalar** (MIT, self-hostable, best-in-class).
- **Documentation site → Mintlify** (more polished; free Starter far more generous).
- They are **complementary**, not strictly competing.

## Decision

Use **Mintlify** (see ADR-0004/0005). Scalar **not adopted now**. The MIT Scalar API
Reference remains a **retained future option** (embed into a Mintlify page / self-host on
the VPS) if a first-class interactive API reference is needed later.

## Sources

- https://github.com/scalar/scalar
- https://scalar.com/ and https://scalar.com/pricing
- https://www.mintlify.com/pricing

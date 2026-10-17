# Orbeex Domain Knowledge

Reusable knowledge gathered during the foundation session. Each item is evidence-backed and
points to where the authoritative detail lives.

## 1. GIS Landscape & Competitive Positioning

| Competitor | AI today | Orbeex exploit |
|---|---|---|
| QGIS | None natively | No AI trust layer; Python perf ceiling |
| ArcGIS Pro | Shallow AI assistants | Lock-in, cost, closed pipeline |
| GRASS GIS | None | Unusable UX at scale |
| Felt/Atlas | Some NL | Cloud-only, no desktop sovereignty |
| Mapbox/Google | N/A (SDKs) | Not desktop workstations |

**Core gap Orbeex fills:** agentic orchestration with **deterministic, auditable,
reversible** execution over a native engine — plus data sovereignty and multi-LLM.

## 2. Enterprise Standards Orbeox Must Meet

SOC 2 Type II, ISO/IEC 27001, SLSA Level 3, GDPR/data residency, SBOM, WCAG 2.2 AA,
signed reproducible builds, CVE response SLAs, tamper-evident audit logs.
Detail: `docs/05-security-compliance/` (planned).

## 3. Licensing Knowledge

- **Permissive vs copyleft:** Apache-2.0/MIT/BSD = max adoption, no reciprocity; GPL/AGPL =
  strong/network copyleft, blocks enterprise & SaaS.
- **Apache-2.0 vs MIT:** both permissive, but Apache-2.0 adds an explicit **patent grant**.
- **Chosen:** Apache-2.0 (software), CC-BY-4.0 (docs), DCO (contributions). See ADR-0001/0007.
- **Allowed deps:** Apache-2.0, MIT, BSD, ISC, Zlib, Unlicense, CC0, MPL-2.0 (isolated).
- **Forbidden deps:** GPL, AGPL, SSPL, non-OSI/source-available. Enforced by `cargo-deny`.

## 4. Documentation Platform Landscape (verified 2026-10-17)

| Platform | Type | License | Free tier | Self-host | Verdict |
|---|---|---|---|---|---|
| **Mintlify** | Hosted service | Proprietary | **Free forever** (custom domain, Git sync, MCP, 5 seats) | Enterprise only | **CHOSEN** |
| Scalar | API platform | MIT (core) | API docs free; Docs Git-sync = Pro $150/mo | **Yes (MIT parts)** | Evaluated; optional future API-ref add-on |
| Fumadocs | React/Next.js framework | MIT | Fully free | **Yes** | Evaluated; high ops cost |
| Docusaurus | Static-site generator | MIT | Fully free | Yes | Fallback |
| MkDocs Material | Static-site generator | MIT | Fully free | Yes | Fallback |
| BookStack / Wiki.js | Internal KB | MIT | Free | Yes | Optional internal KB |

**Mintlify plan boundary:** Starter free (hosting, custom domain, web editor, Git sync, CLI,
MCP server, playground, 5 seats). **Pro-only:** Developer/Admin REST API, webhooks,
analytics, hosted MCP write, preview deployments. Obtain Pro free via the **OSS Program**.

## 5. How to Interact with Mintlify (summary)

1. **Git** (`.mdx` + `docs.json`) — primary, free. Push = deploy.
2. **CLI** (`mint dev|validate|broken-links|a11y|format|new|export|score`) — free; use in CI.
3. **Search MCP server** (`<site>/mcp`) — free; read/verify by AI (read-only).
4. **Web editor** — free; quick edits.
5. **REST API** (`mint_` keys) — Pro/OSS-Pro; automation.
Full guide: `docs-site/MINTLIFY-GUIDE.md`.

## 6. Changelog & Traceability (enterprise standards)

- **Keep a Changelog 1.1.0** — canonical change types (Added/Changed/Deprecated/Removed/
  Fixed/Security), ISO 8601 dates, newest-first, one entry per version. Human-readable.
- **towncrier fragment model** — one note per PR in `changes/unreleased/<ref>.<type>.md`;
  compiled into the changelog at release. Avoids merge conflicts & git-log noise.
- **Conventional Commits** — structured messages (`feat(scope): ...`).
- **Requirements traceability** — feature ID → `FR-*` requirement → spec → docs → release.
- **Docs-as-code** — docs ship in the same PR as the change.
- Orbeex implementation: `changes/`, `features/registry/features.yaml`,
  `scripts/changelog/orbeex.py`, `.github/workflows/changelog.yml` (ADR-0010).

## 7. Key External References

- Choose a License appendix — https://choosealicense.com/appendix/
- Mintlify docs — https://www.mintlify.com/docs
- Mintlify OSS Program — https://www.mintlify.com/oss-program#eligibility
- Scalar — https://github.com/scalar/scalar
- Fumadocs — https://www.fumadocs.dev/
- Research evidence: `research/technology/scalar-vs-mintlify-2026-10-17.md`

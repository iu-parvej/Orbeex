# Current State Snapshot

| Field | Value |
|---|---|
| **Phase** | P0 — Foundation (early) |
| **Date** | 2026-10-17 |
| **Source code** | None yet |
| **Next milestone** | Complete foundation scaffold; begin P0 spikes |

## Completed

- [x] Directory scaffold created (`plan/`, `brain/`, `licensing/`, `docs/`, `docs-site/`,
      `research/`, `features/`, `tests/`, `releases/`, `software/`, `ai/`, `_legacy/`).
- [x] `MASTER_BLUEPRINT.md` written (primary AI instruction set).
- [x] `README.md` files for root, `plan/`, `brain/`, `licensing/`, `docs-site/`.
- [x] ADRs 0001–0009 recorded (`brain/decisions/`).
- [x] Licensing policy + dependency inventory + templates (`licensing/`).
- [x] Test strategy (`tests/strategy/`), performance budgets (`plan/metrics/`),
      glossary (`docs/glossary.md`).
- [x] Mintlify docs-site scaffold + `MINTLIFY-GUIDE.md`.
- [x] Brain populated: context, knowledge, decision log, state.
- [x] **Automated changelog + traceability system**: `changes/`, feature registry,
      `scripts/changelog/orbeex.py`, `require_fragment.py`, `.github/workflows/changelog.yml`
      (ADR-0010). Example feature `F-0001` demonstrates the full lifecycle.

## Not Started

- [ ] P0 spikes (10M-feature render, LLM tool-calling reliability, WASM feasibility).
- [ ] Remaining Blueprint crates (engine, ai, vector, raster, crs, io, render, app, …).
- [ ] OpenAPI spec for the Orbeex API (to feed Scalar/Mintlify later).
- [ ] Tier 3 institutional hardening (SOC 2/ISO mapping, SLSA L3, pen test).
- [ ] Pin GitHub Actions to full commit SHAs.

## Completed — Enterprise Hardening (from audit)

See `knowledge/enterprise-readiness-audit-2026-10-17.md` §8. Highlights:

- [x] **Git repository** initialized (`main`), `.gitattributes`, `.editorconfig`, `.gitignore`.
- [x] **Governance**: LICENSE (Apache-2.0), NOTICE, CONTRIBUTING, SECURITY, Code of Conduct,
      GOVERNANCE, SUPPORT, CITATION, CODEOWNERS, issue/PR templates.
- [x] **Rust workspace**: `Cargo.toml`, `orbeex-core` crate (Operation domain, typed errors,
      validated ids), `rust-toolchain.toml`, `rustfmt.toml`, `clippy.toml`, `deny.toml`.
- [x] **CI/CD**: `ci.yml` (fmt/clippy/test matrix/rustdoc/changelog), `deny.yml`, `audit.yml`,
      `unsafe-check.yml`, `docs.yml`, `codeql.yml`, `release.yml` (SBOM + SLSA provenance),
      `publish-docs.yml`, `dependabot.yml`.
- [x] **Automation tests + typing**: 15 pytest tests pass; mypy strict clean; parser hardened.
- [x] **Reproducibility**: Dockerfile, devcontainer, `.gitkeep` markers, NOTICE generation.

## Open Questions / Pending

- Set the real GitHub username for the noreply commit email before pushing.
- Decide when to start the P0 spikes.
- Apply to Mintlify OSS Program — timing per ADR-0005 (after established).
- Set up GitHub remote + branch protection + secret scanning/push protection on GitHub.
- Pin GitHub Actions to commit SHAs (Tier 2/3 hardening).

## Security & Style (2026-10-17)

- **Repo is public-safe.** No secrets or personal email in tracked files or git history
  (verified). History rewritten to a noreply identity. See `knowledge/security-guide.md`.
- Secret prevention in place: `.gitignore`, gitleaks pre-commit, CI scan, push protection
  (to enable on GitHub). ADR-0012.
- **Writing style:** professional, compact, factual English for all human docs. See
  `knowledge/writing-style-guide.md`. ADR-0014 (supersedes ADR-0013).
- **Policy set:** PRIVACY.md, DATA-USAGE.md, ACCEPTABLE-USE.md, TRADEMARK.md, plus SECURITY
  and GOVERNANCE. ADR-0015.

## Data & Privacy Commitments (standing)

- Local processing by default; no data leaves the machine unless AI is enabled.
- No telemetry or usage collection in the current version.
- Only task intent + dataset schema are sent to LLM providers by default (never raw data).
- AI features are opt-in and can be disabled; local models supported for full isolation.
- **Before shipping any telemetry or network feature, update `DATA-USAGE.md` first.**

## Audit (2026-10-17)

Full enterprise-readiness gap analysis complete →
`brain/knowledge/enterprise-readiness-audit-2026-10-17.md`.
**Verdict was: strong scaffold, zero product code, ~15% enterprise-ready.**
14 gaps (G-01…G-14) identified; **all Tier 0–2 gaps remediated** (see §8 of the audit).
`_legacy/` contains 7 empty dirs, 0 files.

## How to Update

Keep this file current at the end of each working session. Reflect: what changed, what's
next, what's blocked. This is the fastest way for an AI to resume work.

## Public Docs Live (2026-10-17)

- Mintlify site live at https://orbeex.mintlify.app (project portfolioofparvej/orbeex).
- New workflow: pages sourced in documentation/, pushed directly to Mintlify via MCP; broad-audience tone.
- 11 pages live; rewrites: introduction, quickstart; new: how-it-works, working-with-ai, your-data-and-privacy.

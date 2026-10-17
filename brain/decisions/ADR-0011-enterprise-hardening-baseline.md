# ADR-0011 — Enterprise Hardening Baseline (Repo, CI/CD, Supply Chain)

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | `brain/knowledge/enterprise-readiness-audit-2026-10-17.md` |

## Context

A full-directory audit found 14 gaps (G-01…G-14) against enterprise standards (SLSA,
OpenSSF Scorecard, SOC 2, ISO 27001). Two were blockers: no Git repository and no buildable
workspace. The instruction was to remediate all gaps with revertible history.

## Decision

Adopt and implement the enterprise baseline:

1. **Version control**: Git on `main`; `.gitattributes` (LF policy), `.editorconfig`,
   expanded `.gitignore`. Conventional Commits; DCO sign-off; CODEOWNERS.
2. **Governance**: Apache-2.0 LICENSE + NOTICE; SECURITY.md (disclosure + SLA);
   CONTRIBUTING, CODE_OF_CONDUCT, GOVERNANCE, SUPPORT, CITATION; issue/PR templates.
3. **Rust workspace**: `orbeex-core` as the first crate; pinned toolchain; `forbid(unsafe_code)`;
   workspace lints; `deny.toml` (license allow-list), `clippy.toml`, `rustfmt.toml`.
4. **CI/CD**: `ci.yml` (fmt/clippy/test matrix/rustdoc/changelog), `deny.yml`, `audit.yml`,
   `unsafe-check.yml`, `docs.yml`, `codeql.yml`, `release.yml` (SBOM + SLSA provenance),
   `publish-docs.yml`, `dependabot.yml`.
5. **Automation quality**: pytest suite + mypy for `scripts/changelog`; PyYAML-preferred
   parser with stdlib fallback.
6. **Reproducibility**: Dockerfile, devcontainer, `.gitkeep` markers, NOTICE generation.

## Rationale

- Version control + CI make the existing governance (Blueprint §5, §6) **enforceable**.
- SBOM + SLSA L2 provenance satisfy supply-chain requirements; hardening to L3 is Phase 6.
- Pinned toolchain, committed lockfile, and containers give reproducible builds.
- Tests + typing for automation remove the fragility flagged in G-08.

## Consequences

- **Positive:** all Tier 0–2 gaps closed; gates enforce quality automatically.
- **Negative:** Actions are pinned by **version tag** initially (not SHA) — a documented
  hardening follow-up; Rust build requires a platform linker locally.
- **Follow-up:** pin Actions to SHAs; set required status checks; Tier-3 (SOC 2/ISO, SLSA L3,
  pen test) in Phase 6.

## Alternatives Considered

- **Address gaps ad hoc later** — rejected: blockers must precede feature work.
- **Vendor CI (no OSS gates)** — rejected: enterprise requirements demand auditable gates.

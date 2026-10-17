# Orbeex — Enterprise Readiness Audit & Gap Analysis

| Field | Value |
|---|---|
| **Report type** | Full-directory audit + gap analysis + strategic roadmap |
| **Scope** | `D:\Orbeex` (all files & nested directories), excluding `_legacy/` content |
| **Date** | 2026-10-17 |
| **Auditor** | Senior Enterprise Software Architect / DevOps |
| **Benchmark** | Enterprise-grade OSS: SLSA, OpenSSF Scorecard, SOC 2, ISO 27001, Keep a Changelog, SemVer, Conventional Commits, Rust API guidelines |
| **Verdict** | **Strong planning scaffold; zero product code. ~15% toward enterprise-ready.** |

> **Purpose:** This report is a blocking prerequisite. Per instruction, **no further software
> development should begin until this gap analysis is reviewed and accepted.** It is not a
> criticism of direction — the foundation is deliberate and high quality — but it measures
> that foundation against what a deployable, auditable enterprise product requires.

---

## 1. Executive Summary

### 1.1 What exists today (verified)

| Category | Count / State |
|---|---|
| Files (excl. `_legacy`) | **50** |
| Directories | 78 (many intentionally empty scaffolds) |
| Product source code | **0** (no Rust, no `Cargo.toml`, no workspace) |
| Python automation | 2 scripts (`scripts/changelog/`) — parse & run OK |
| CI workflows | 1 (`.github/workflows/changelog.yml`) |
| Git repository | **NOT initialized** (`.git` absent) |
| Legacy archive | `_legacy/` — 7 empty dirs, 0 files |
| Documentation | Extensive planning docs; no ADRs for gaps below |

### 1.2 Findings at a glance

| # | Area | Severity | Status |
|---|---|---|---|
| G-01 | No Git repository / VCS history | **Blocker** | Missing |
| G-02 | No product code, build system, or workspace | **Blocker** | Missing |
| G-03 | No CI beyond changelog (no build/test/lint/audit) | **Critical** | Partial |
| G-04 | No supply-chain security (SLSA, provenance, SBOM gen) | **Critical** | Missing |
| G-05 | No dependency/lint/toolchain configuration | **Critical** | Missing |
| G-06 | No release/publish pipeline or signing | **High** | Missing |
| G-07 | No security policy / governance files | **High** | Missing |
| G-08 | Automation scripts lack tests & static typing | **Medium** | Partial |
| G-09 | Empty scaffold dirs indistinguishable from intended | **Medium** | Partial |
| G-10 | No containerization / reproducibility | **Medium** | Missing |
| G-11 | No observability, telemetry, or error budgets | **Medium** | Missing |
| G-12 | Accessibility & i18n not enforced | **Low–Medium** | Missing |
| G-13 | No `.editorconfig`, line-ending, or attribution automation | **Low** | Missing |
| G-14 | Legacy archive referenced but empty/unactioned | **Low** | Partial |

---

## 8. Remediation Status (updated 2026-10-17)

All gaps addressed in commits `50ef585`…`22e87c6` (+ follow-up ADRs). Summary:

| Gap | Status | Where |
|---|---|---|
| G-01 Git repo | ✅ Done | `.git`, `.gitattributes`, `.editorconfig` |
| G-02 Workspace/build | ✅ Skeleton | `Cargo.toml`, `orbeex-core` crate |
| G-03 CI coverage | ✅ Done | `.github/workflows/ci.yml` + others |
| G-04 Supply chain | ✅ L2 | `release.yml` (SBOM + SLSA provenance) |
| G-05 Dep/lint config | ✅ Done | `deny.toml`, `clippy.toml`, `rustfmt.toml`, `dependabot.yml` |
| G-06 Release/publish | ✅ Done | `release.yml`, `publish-docs.yml` |
| G-07 Governance files | ✅ Done | LICENSE, SECURITY, CONTRIBUTING, CoC, CODEOWNERS, templates |
| G-08 Automation quality | ✅ Done | `scripts/changelog/test_orbeex.py` (15 tests), `mypy` clean |
| G-09 Empty-dir ambiguity | ✅ Done | `.gitkeep` markers |
| G-10 Containerization | ✅ Done | `Dockerfile`, `.devcontainer` |
| G-11 Observability | ⏳ Planned | Phase 1+ (no runtime yet) |
| G-12 a11y/i18n | ◑ Partial | `mint a11y` in CI; i18n deferred |
| G-13 Hygiene | ✅ Done | SPDX headers, NOTICE generation |
| G-14 Legacy archive | ◑ Noted | empty; left as-is |

**Remaining Tier-3 (institutional):** SOC 2 / ISO 27001 control mapping, SLSA L3 hardening,
penetration test, performance-regression gates — deferred to Phase 6 per roadmap.

**Hardening follow-up:** pin GitHub Actions to full commit SHAs (see
`.github/workflows/README.md`).

---

## 2. Detailed Gap Analysis

### G-01 — No Git Repository (BLOCKER)

**Evidence:** `git status` → `fatal: not a git repository`. No `.git/`.

**Why it matters:** Enterprise standards (SLSA Source track, auditability, traceability,
signed commits, branch protection, PR review) all require version control. The entire
governance model in `MASTER_BLUEPRINT.md` (§5) is currently unenforceable.

**Required improvements:**
- `git init` with a `main` branch; add remote (GitHub org).
- `.gitattributes` (LF normalization, binary handling, linguist rules).
- Branch protection: required reviews, signed commits, status checks, no force-push.
- `CODEOWNERS` mapping paths → owners.
- Commit signing (GPG/SSH) policy; DCO enforcement via CI.

### G-02 — No Product Code / Build System (BLOCKER)

**Evidence:** `software/apps/`, `software/modules/` are empty. No `Cargo.toml`, no
`rust-toolchain.toml`, no `rustfmt.toml`, no `clippy.toml`, no `deny.toml`.

**Why it matters:** A "software" project with no buildable artifact cannot be reviewed for
architecture, performance, or security. The Blueprint describes a workspace of ~15 crates
(§2.3) and mandates `#![forbid(unsafe_code)]`, typed errors, etc. — none is present.

**Required improvements:**
- Rust workspace: root `Cargo.toml` + member crates per Blueprint §2.3.
- `rust-toolchain.toml` (pinned), `rustfmt.toml`, `clippy.toml` (`-D warnings`).
- `deny.toml` for `cargo-deny` (license allow-list per `licensing/`).
- Enforcement of `forbid(unsafe_code)` and error-code taxonomy (`ORX-*`).
- Architecture Decision Records ratified for crate boundaries (ADR-0003 exists; crate
  boundary ADR does not).

### G-03 — CI/CD Coverage Incomplete (CRITICAL)

**Evidence:** Only `.github/workflows/changelog.yml`. No build, test, lint, audit, or
release workflows.

**Why it matters:** Enterprise CI must gate every PR on correctness, security, and
licensing. Blueprint §6.4 lists required gates that are **not implemented**.

**Required improvements (new workflows):**
- `ci.yml`: `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test`, `cargo build`
  (all targets), matrix across `{ubuntu, windows, macos}`.
- `deny.yml`: `cargo deny check` (licenses, advisories, bans, sources).
- `audit.yml`: scheduled `cargo audit` + Dependabot.
- `unsafe-check.yml`: `grep`/`cargo-geiger` gate for `unsafe`.
- `docs.yml`: `mint validate`, `mint broken-links`, `mint a11y` (per `docs-site/`).
- `codeql.yml`: static analysis (Rust/JS).
- Required status checks configured on `main`.

### G-04 — Supply-Chain Security Absent (CRITICAL)

**Evidence:** No SBOM generation, no SLSA provenance, no artifact signing. Blueprint targets
**SLSA Level 3** and SBOM (Phase 6) but nothing is scaffolded.

**Why it matters:** Enterprise procurement (and ISO 27001 / SOC 2) require provenance and
SBOM. SLSA Build L2 = signed provenance from a hosted builder; **L3 = hardened builds**
(isolated runs, no user access to signing secrets).

**Required improvements:**
- SBOM generation (CycloneDX/SPDX) on every release → `licensing/compliance/sbom/`.
- SLSA provenance via GitHub Actions attestations (`actions/attest-build-provenance`),
  target Build L2 now, L3 by Phase 6.
- Sign artifacts + tags (Sigstore/cosign); publish verification instructions.
- `SECURITY.md`, threat model, CVE response SLA.
- Pin Actions by SHA; least-privilege `permissions:` on every workflow.

### G-05 — Dependency/Lint/Toolchain Config Missing (CRITICAL)

**Evidence:** No `deny.toml`, `clippy.toml`, `rustfmt.toml`, `.editorconfig`, `renovate.json`
/ `dependabot.yml`.

**Required improvements:**
- `deny.toml` generated **from** `licensing/policies/dependency-license-policy.md`.
- `.editorconfig`; `rustfmt.toml`; `clippy.toml`.
- `dependabot.yml` (cargo + github-actions + npm for `docs-site/`).
- Pre-commit hooks (`.pre-commit-config.yaml` or `lefthook.yml`) mirroring CI gates.

### G-06 — Release & Publish Pipeline Missing (HIGH)

**Evidence:** `releases/` and `plan/releases/` empty. No version bumping, no publish
workflow, no artifact build.

**Required improvements:**
- `release.yml`: tag-triggered; compile changelog (`orbeex.py compile`), build signed
  artifacts (Win MSI, macOS DMG, Linux AppImage/deb/rpm), generate SBOM + provenance,
  create GitHub Release from `changes/releases/<ver>.md`.
- Version authority: single source of truth (e.g. workspace `Cargo.toml`) read by tooling.
- Publish docs (Mintlify) on release; publish `rustdoc` to GitHub Pages.
- Dry-run/release-candidate flow; instant-rollback notes.

### G-07 — Governance & Security Files Missing (HIGH)

**Required improvements (standard OSS/enterprise set):**
- `SECURITY.md` (disclosure policy + SLA), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `GOVERNANCE.md`, `SUPPORT.md`, `CITATION.cff`.
- Issue/PR templates, `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`.
- `LICENSE` (Apache-2.0) + `NOTICE` + `licensing/licenses/` populated with full texts.

### G-08 — Automation Quality (MEDIUM)

**Evidence:** `scripts/changelog/orbeex.py` (18.9 KB) and `require_fragment.py` are pure
stdlib, parse correctly, and work — but have **no tests**, **no type checking**, and a
**hand-rolled YAML subset parser** (fragile by design).

**Required improvements:**
- Unit tests for both scripts (pytest or `unittest`), run in CI.
- Type hints are present; add **mypy/pyright** in CI.
- Replace the custom YAML subset with a tested dependency (PyYAML/ruamel) **or** document
  and fuzz the parser; keep the zero-dependency option behind a flag.
- Handle Windows CRLF explicitly; add `--strict`/exit-code contract tests.

### G-09 — Empty Scaffold Ambiguity (MEDIUM)

**Evidence:** 78 dirs, most empty. Empty dirs aren't tracked by Git anyway.

**Required improvements:**
- Add `.gitkeep` where a dir must exist, or a `README.md` stating intent.
- Distinguish "intended but empty" from "abandoned".

### G-10 — Containerization / Reproducibility (MEDIUM)

**Required improvements:**
- `Dockerfile` (+ multi-stage) for reproducible builds/CI parity; `docker-compose.yml` for
  local services if any; devcontainer (`.devcontainer/`).
- Reproducible-build settings (`SOURCE_DATE_EPOCH`), pinned toolchain, lockfiles committed.

### G-11 — Observability & Error Budgets (MEDIUM)

**Required improvements:**
- Define metrics/logging/tracing standards for the eventual engine (Blueprints §2, §6.6).
- Error-budget policy tied to `plan/metrics/performance-budgets.md`.
- Crash-report policy (opt-in, redacted) — referenced but not implemented.

### G-12 — Accessibility & i18n (LOW–MEDIUM)

**Required improvements:**
- CI a11y check for docs (`mint a11y`); WCAG 2.2 AA target (Blueprint §1.3) has no gate.
- Decide i18n strategy early (docs `docs.json` supports it; product i18n undefined).

### G-13 — Repo Hygience (LOW)

**Required improvements:**
- `.editorconfig`, enforced LF, `.gitattributes`.
- SPDX headers on all code files (Blueprint §4.6) — not yet applied to the Python scripts.
- Attribution/NOTICE automation (aligns with SBOM work).

### G-14 — Legacy Archive (LOW)

**Evidence:** `_legacy/` has 7 empty subdirs, 0 files. The "read-only archive" rule exists
but there's nothing to archive.

**Required improvements:**
- Either remove the empty `_legacy/` or populate it and apply the documented read-only rule
  via `CODEOWNERS` + branch rules.

---

## 3. Industry Best Practices to Adopt (benchmark)

| Domain | Standard | Applied action |
|---|---|---|
| Supply chain | **SLSA** Build L1→L3 | Provenance now (L2), harden to L3 by P6 |
| Repo health | **OpenSSF Scorecard** | Branch protection, pinned deps, `SECURITY.md` |
| Vulnerabilities | **CVE/OSV**, `cargo audit` | Scheduled scanning + Dependabot |
| Licensing | SPDX, allow-list | `deny.toml` + `licensing/` records |
| Change mgmt | **Keep a Changelog**, **SemVer**, **Conventional Commits** | Already adopted (ADR-0010) |
| Decisions | **ADR** (Nygard) | Already adopted |
| Build repro | **Reproducible Builds** | Pinned toolchain, `SOURCE_DATE_EPOCH` |
| Secure SDLC | **NIST SSDF**, ISO 27001 | Threat model, signed builds, access control |
| Compliance | SOC 2, GDPR | Audit logs, data-flow docs, DPA notes |
| Rust quality | **Rust API Guidelines**, `clippy -D warnings`, `forbid(unsafe_code)` | Lint gates in CI |

---

## 4. Prioritized Improvement Roadmap

### Tier 0 — Blockers (do first; prerequisites for everything)
1. **Initialize Git** + `.gitattributes` + `.editorconfig` + `.gitignore` review.
2. **Add Rust workspace skeleton** (`Cargo.toml`, `rust-toolchain.toml`, `rustfmt.toml`,
   `clippy.toml`, `deny.toml`) with one buildable placeholder crate.
3. **Baseline CI** (`ci.yml`): fmt, clippy, test, build matrix.
4. **Governance files**: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`,
   `CODEOWNERS`, issue/PR templates.

### Tier 1 — Critical (enterprise baseline)
5. `deny.yml`, `audit.yml`, `unsafe-check.yml`, `docs.yml`, `codeql.yml`.
6. SBOM + SLSA provenance (Build L2) on releases; pin Actions by SHA.
7. Release pipeline (`release.yml`) with signed artifacts.
8. Tests + type-checks for `scripts/changelog/*`; harden YAML parsing.
9. `.gitkeep`/README for intended-empty dirs.

### Tier 2 — High (production readiness)
10. Containerization + devcontainer; reproducible builds.
11. Observability/metrics/error-budget standards; crash-report pipeline.
12. i18n + a11y gates; SPDX headers everywhere.
13. Publish workflows: Mintlify docs + `rustdoc` to Pages.
14. Populate `licensing/licenses/`, generate `NOTICE` automatically.

### Tier 3 — Institutional (Phase 6 alignment)
15. SOC 2 / ISO 27001 control mapping + evidence collection.
16. SLSA L3 hardening; penetration test; threat-model review.
17. Performance regression gates in CI (bench baseline vs. threshold).

---

## 5. Traceability to Blueprint

| Blueprint clause | Requirement | Gap | Present? |
|---|---|---|---|
| §2.3 crate workspace | ~15 crates | G-02 | No |
| §4 licensing | deny.toml, SBOM, NOTICE | G-04/05 | No |
| §5.5 release process | signed artifacts, provenance | G-04/06 | No |
| §6.4 quality gates | fmt/clippy/test/deny/bench | G-03 | Partial (1/7) |
| §6.6 performance budgets | CI regression gate | G-03 | No |
| §7.3 docs maintenance | mint validate/broken-links in CI | G-03/12 | No |
| §8.1 Definition of Done | all gates enforceable | G-01/03 | No (no VCS/CI) |

**Gate coverage today: 1 of ~7. Definition of Done is not enforceable without Git + CI.**

---

## 6. What Is Already Good (retain)

- Correct, opinionated architecture thinking (Operation Graph, layered design).
- Solid decision discipline (10 ADRs, immutable, indexed).
- Changelog/traceability system is genuinely enterprise-shaped (Keep a Changelog +
  fragments + machine-readable registry + CI gate).
- Licensing policy is explicit and enforceable-ready (`cargo-deny` design).
- Documentation platform decision is well-reasoned with free + OSS-Pro path.
- Brain/context/state discipline is unusually strong for a greenfield project.

---

## 7. Recommendation

**Proceed in Tier-0 order before any feature coding.** The plan is sound; the *mechanisms*
that make an enterprise project real — version control, a buildable workspace, and CI gates —
are the missing layer. Tier 0 is small (days) and unblocks everything else.

**Immediate next 5 actions:**
1. `git init` + governance files (Tier 0.1, 0.4).
2. Rust workspace skeleton + `deny.toml` (Tier 0.2).
3. `ci.yml` baseline gates (Tier 0.3).
4. Tests + typing for `scripts/changelog/` (Tier 1.8).
5. SBOM + SLSA L2 in `release.yml` (Tier 1.6).

---

*End of audit. This report is a decision input, not a task list — approve, reorder, or
reject tiers before implementation begins.*

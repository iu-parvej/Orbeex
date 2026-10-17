# CI/CD Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| `ci.yml` | push/PR | fmt, clippy, build+test matrix, rustdoc, changelog/registry gates |
| `deny.yml` | push/PR/weekly | `cargo-deny`: licenses, advisories, bans |
| `audit.yml` | daily/on dep change | `cargo-audit` (RustSec) + `pip-audit` |
| `unsafe-check.yml` | push/PR | fail on raw `unsafe` / missing `forbid(unsafe_code)` |
| `codeql.yml` | push/PR/weekly | CodeQL for `actions` + `python` |
| `release.yml` | tag `v*.*.*` | compile changelog, build artifacts, SBOM, SLSA provenance, publish |

## Actions pinning policy (IMPORTANT)

Actions currently reference **major-version tags** (e.g. `actions/checkout@v4`) for
maintainability. **Hardening step (Tier 2): pin every action to a full commit SHA** for
supply-chain safety (OpenSSF Scorecard "Pinned-Dependencies"), ideally automated with
[`pinact`](https://github.com/suzuki-shunsuke/pinact) or Renovate's
`helpers:pinGitHubActionDigests`.

Until pinned, treat workflow changes with extra review. The `anchore/sbom-action@v0` entry
must be pinned on first successful run.

## Required status checks (branch protection on `main`)

Configure these as required before merge:
- `rustfmt`, `clippy`, `test (ubuntu/windows/macos)`, `rustdoc`
- `changelog & registry`
- `cargo-deny`, `forbid unsafe_code`
- `Documentation link check`
- `CodeQL`

## Local parity

Run the same gates locally (see `CONTRIBUTING.md`). Rust build/test requires a platform C
linker (MSVC on Windows, gcc/clang on Unix). `rustfmt` and the Python gates need no linker.

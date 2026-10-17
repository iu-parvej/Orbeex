# CI/CD Workflows

The repository is in its **planning-and-documentation phase**: Rust gates activate with the
first development milestone (see `.gitignore` — the scaffolding returns with `software/`).

| Workflow | Trigger | Purpose |
|---|---|---|
| `ci.yml` | push/PR | changelog fragment validation + documentation link check |
| `secret-scan.yml` | push/PR/daily | gitleaks secret scanning (full history) |
| `codeql.yml` | push/PR/weekly | CodeQL for `actions` + `python` |
| `audit.yml` | daily/on dep change | `pip-audit` (Python automation deps) |

## Rust gates (activate together with `software/`)

`fmt`, `clippy`, `build/test matrix` (3 OS), `rustdoc`, `cargo-deny`
(licenses/advisories/bans), `unsafe-check`, `release.yml` (signed artifacts + SBOM +
SLSA provenance), `publish-docs.yml` (rustdoc). Scaffolding is preserved in local git
history (tag `private-history-2026-10-17`).

## Actions pinning policy (IMPORTANT)

Actions currently reference **major-version tags** (e.g. `actions/checkout@v4`) for
maintainability. **Hardening step: pin every action to a full commit SHA** for supply-chain
safety (OpenSSF Scorecard "Pinned-Dependencies"), ideally automated with
[`pinact`](https://github.com/suzuki-shunsuke/pinact) or Renovate.

## Required status checks (branch protection on `main`)

- `changelog & registry`
- `documentation link check`
- `gitleaks`, `CodeQL`

## Local parity

```bash
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
python scripts/docs/check_local_links.py
```

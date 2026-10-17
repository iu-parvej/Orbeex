# Contributing to Orbeex

Orbeex is an open-source GIS written in Rust. This document defines how to submit changes.

## Ways to contribute

- Report bugs and request features via Issues, using the provided templates.
- Improve documentation.
- Submit code: features, fixes, and tests.
- Review pull requests and triage issues.

## Ground rules

- Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- Sign off every commit (DCO). Use `git commit -s` to add the required `Signed-off-by` line.
- Use [Conventional Commits](https://www.conventionalcommits.org/) for messages:
  `feat(scope): summary`, `fix(scope): …`, `docs: …`, `refactor: …`, `test: …`, `chore: …`.
- Keep pull requests small and focused. One logical change per PR.
- Do not commit secrets. The repository is public. Install the pre-commit hook below.

## Development setup

Requirements:

- Rust (version pinned in `rust-toolchain.toml`)
- Python 3.11+ (project automation)
- Node.js 20.17+ (documentation site)

Run the full verification suite before opening a pull request:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all
cargo deny check
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
```

Install the pre-commit hooks once to run these checks automatically:

```bash
pip install pre-commit
pre-commit install
```

## Pull request requirements

Every pull request must satisfy the project's Definition of Done:

1. Documentation updated in the same PR as any behavior change.
2. A change fragment added under `changes/unreleased/`:
   `python scripts/changelog/orbeex.py new-fragment --ref PR-<n> --type added --area <area>`
3. Tests for new behavior; existing tests pass.
4. All checks pass: formatting, clippy, tests, license checks, registry validation.
5. No `unsafe` code unless an ADR approves a specific, audited exception.

## Feature workflow

Small features: open an issue, get a nod from a maintainer, then build.
Large features: proposed through an issue first; maintainers track and prioritize them
before implementation begins.

## Architectural changes

Any structural or architectural change requires an Architecture Decision Record (ADR)
approved by the maintainers before implementation.

## License of contributions

Contributions are licensed under the Apache License 2.0 (see `LICENSE`). Signing off a
commit certifies the [Developer Certificate of Origin](https://developercertificate.org/).

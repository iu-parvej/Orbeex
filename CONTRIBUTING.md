# Contributing to Orbeex

Thank you for considering a contribution. Orbeex is an open-source, AI-native GIS built in
Rust. This guide keeps contributions fast to review and safe to merge.

## Ways to contribute

- Report bugs and request features via Issues (use the templates).
- Improve documentation.
- Submit code (features, fixes, tests).
- Review pull requests and triage issues.

## Ground rules

- Be respectful — see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Sign off every commit** (DCO). `git commit -s` adds the required `Signed-off-by` line.
- Follow [Conventional Commits](https://www.conventionalcommits.org/):
  `feat(scope): summary`, `fix(scope): …`, `docs: …`, `refactor: …`, `test: …`, `chore: …`.
- Keep pull requests small and focused; one logical change per PR.

## Development setup

Prerequisites (see `README.md` for details):

- Rust (pinned via `rust-toolchain.toml`)
- Python 3.11+ (for project automation)
- Node.js 20.17+ (for the `docs-site/` Mintlify site)

Run the full local check before opening a PR:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all
cargo deny check
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
```

## Pull request requirements

Every PR must satisfy the project's Definition of Done (`MASTER_BLUEPRINT.md` §8.1):

1. **Docs updated in the same PR** as any behavior change.
2. **A change fragment** added under `changes/unreleased/`:
   `python scripts/changelog/orbeex.py new-fragment --ref PR-<n> --type added --area <area>`
3. **Tests** for new behavior; existing tests pass.
4. **Quality gates green** (fmt, clippy, test, deny, license/registry validation).
5. **No `unsafe`** unless an ADR approves an audited exception.

## Feature workflow

Features follow `features/backlog → in-progress → completed` and are registered in
`features/registry/features.yaml`. See `features/README.md`.

## Architectural changes

Any structural or architectural change requires an **ADR** *before* implementation.
See `brain/decisions/README.md`.

## License of contributions

By contributing, you agree your contributions are licensed under the Apache License 2.0
(see `LICENSE`). You certify the [Developer Certificate of Origin](https://developercertificate.org/)
by signing off your commits.

# Contributing to Orbeex

Thanks for wanting to help. Orbeex is a free, open-source GIS built in Rust. This guide is
here to make your contribution easy to send and easy to review.

## Ways to contribute

- Report bugs and ask for features through Issues (use the templates).
- Improve the documentation — even fixing a typo helps.
- Send code: new features, fixes, and tests.
- Review pull requests and help triage issues.

## Ground rules

- Be kind and respectful — see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Sign off every commit** (this is the DCO). Adding `-s` does it for you:
  `git commit -s -m "your message"`. It appends a `Signed-off-by` line.
- Write commit messages in the [Conventional Commits](https://www.conventionalcommits.org/)
  style: `feat(scope): summary`, `fix(scope): …`, `docs: …`, `refactor: …`, `test: …`,
  `chore: …`.
- Keep pull requests small and focused. One change per PR is easiest to review.
- **Never commit secrets.** This repo is public. Install the pre-commit hook below and it
  will catch accidents before they leave your machine.

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

### Turn on the safety hooks (once)

```bash
pip install pre-commit
pre-commit install
```

Now every commit is scanned for secrets and basic mistakes automatically. It takes a moment
and saves a lot of pain.

## Pull request requirements

Every PR needs to meet the project's Definition of Done (`MASTER_BLUEPRINT.md` §8.1):

1. **Docs updated in the same PR** as any behavior change.
2. **A change fragment** added under `changes/unreleased/` — the easy way:
   `python scripts/changelog/orbeex.py new-fragment --ref PR-<n> --type added --area <area>`
3. **Tests** for new behavior; existing tests still pass.
4. **All checks green** (formatting, clippy, tests, license checks, registry validation).
5. **No `unsafe` code** unless an ADR approves a specific, audited exception.

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

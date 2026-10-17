# Orbeex

> Open-source, AI-native GIS workstation built in Rust.

Orbeex turns natural language into **reviewable, reversible, auditable geospatial
operations** — executed by a high-performance native engine on desktop and in the browser
(WASM), with zero vendor lock-in on the LLM tier.

## Start Here

- **[MASTER_BLUEPRINT.md](MASTER_BLUEPRINT.md)** — the primary instruction set. **Read this first.**
- [`plan/`](plan/) — roadmap & strategic execution.
- [`brain/`](brain/) — core logic, context, decisions.
- [`licensing/`](licensing/) — legal documentation & policy.
- [`docs/`](docs/) — architecture, guides, user documentation.

## Status

Foundation phase with enterprise hardening complete. See the audit
(`brain/knowledge/enterprise-readiness-audit-2026-10-17.md`) and `plan/roadmap/`.

## Development

Prerequisites: Rust (pinned via `rust-toolchain.toml`), Python 3.11+, Node.js 20.17+.

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace
cargo deny check
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow and
[.github/workflows/README.md](.github/workflows/README.md) for CI/CD.

## License

Code: Apache-2.0 · Docs: CC-BY-4.0. See [LICENSE](LICENSE) and [`licensing/`](licensing/).

# Orbeex

An open-source, AI-native Geographic Information System, written in Rust.

Orbeex converts natural-language instructions into explicit, reviewable geospatial
operations, which a native engine executes. Every action is recorded, reversible, and
auditable. Processing runs locally; data is never sent to a model provider.

## Features

**Natural-language workflow**
Describe a task in plain language. Orbeex derives the operation sequence, presents the plan,
and executes it after confirmation.

**Deterministic execution**
Every action is an operation in an append-only graph. This provides undo, full audit
history, and reproducible results. The AI layer never modifies data directly; it proposes
operations that the engine validates before running.

**Data sovereignty**
Spatial processing runs on the local machine. Only the task intent, or a dataset schema, is
sent to a language model, and only when enabled. Raw coordinates and attribute data are not
transmitted.

**Multi-provider AI**
Supports OpenAI, Anthropic, Google, DeepSeek, and Qwen with user-supplied API keys, plus
local models for offline use. No dependence on a single provider.

**Native performance**
A Rust engine with GPU-accelerated rendering. Designed for datasets in the millions of
features. Memory-safe by construction.

**Cross-platform**
Native builds for Windows, macOS, and Linux. A WebAssembly build provides a reduced feature
set in the browser.

## Repository layout

| Path | Contents |
|---|---|
| `MASTER_BLUEPRINT.md` | Primary design and engineering document |
| `plan/` | Roadmap and execution plan |
| `brain/` | Decisions (ADRs), project context, current state |
| `docs/` | Architecture and guides |
| `licensing/` | License policy and records |
| `changes/` | Changelog fragments and releases |
| `features/` | Feature specifications and registry |

## Status

Foundation phase. Repository structure, contribution rules, build system, and CI are in
place. The GIS engine is in early development. For details, see
`brain/knowledge/enterprise-readiness-audit-2026-10-17.md` and `plan/roadmap/`.

## Development

Requirements: Rust (version pinned in `rust-toolchain.toml`), Python 3.11+, Node.js 20.17+.

Run the full verification suite:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace
cargo deny check
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow.

## Policies

- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute
- [SECURITY.md](SECURITY.md) — vulnerability reporting and secret handling
- [PRIVACY.md](PRIVACY.md) — data handling and privacy
- [DATA-USAGE.md](DATA-USAGE.md) — data processing and the AI data flow
- [ACCEPTABLE-USE.md](ACCEPTABLE-USE.md) — permitted use of the software
- [TRADEMARK.md](TRADEMARK.md) — use of the Orbeex name and logo
- [GOVERNANCE.md](GOVERNANCE.md) — project governance
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — community standards

## License

Code is licensed under Apache-2.0. Documentation is licensed under CC-BY-4.0.
See [LICENSE](LICENSE) and the [`licensing/`](licensing/) directory.

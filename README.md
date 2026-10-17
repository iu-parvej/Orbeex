# Orbeex

**A free, open-source tool for working with maps and location data — controlled through plain language.**

Orbeex is a Geographic Information System written in Rust. Describe what you need in everyday language ("show every school within one kilometer of the river") and Orbeex builds the steps, shows you the plan, and runs it once you approve it. Every action is recorded and reversible. Your data never leaves your computer.

**Live documentation: [orbeex.mintlify.app](https://orbeex.mintlify.app)**

## How it works

1. **You ask** — in plain language, or with regular tools and menus.
2. **Orbeex plans** — complex tasks are broken into clear steps, shown before anything runs.
3. **You approve** — risky operations always require explicit confirmation, with a preview.
4. **Orbeex executes** — locally, with every step recorded so you can review, undo, and repeat.

## Features

| | |
|---|---|
| **Plain-language workflows** | Describe analysis tasks; Orbeex proposes the steps and executes them after confirmation. |
| **Deterministic execution** | Every action is an operation in an append-only history. Review, undo, and reproduce any result. |
| **Local-first processing** | Full map analysis runs on your machine. Nothing is uploaded. |
| **Bring your own AI** | OpenAI, Anthropic, Google, DeepSeek, Qwen, or local models. Your keys, your control. |
| **Native performance** | A memory-safe Rust engine with GPU rendering, built for large datasets. |
| **Cross-platform** | Windows, macOS, and Linux. A WebAssembly build covers browser use. |

## Documentation

Full documentation is hosted at **[orbeex.mintlify.app](https://orbeex.mintlify.app)**:

- [What is Orbeex?](https://orbeex.mintlify.app/introduction) — purpose and audience, for anyone
- [How Orbeex works](https://orbeex.mintlify.app/how-it-works) — the ask, plan, approve, execute cycle
- [Getting started](https://orbeex.mintlify.app/quickstart) — requirements and first session
- [Using AI with Orbeex](https://orbeex.mintlify.app/working-with-ai) — providers, keys, and data boundaries
- [Your data and privacy](https://orbeex.mintlify.app/your-data-and-privacy) — what is collected (nothing) and what is sent (almost nothing)

## Status

Planning and documentation phase. The repository carries the design documents, governance, policies, and project automation; the analysis engine arrives with the first development milestone.

**Planned order of delivery:** core engine → desktop application → AI layer → web (WASM) → plugin system → enterprise hardening → 1.0 release.

There are no releases yet. Watch the repository for the first public build.

## Development

Requirements for project automation and documentation checks: Python 3.11+.

```bash
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
python scripts/docs/check_local_links.py
```

Rust gates (fmt, clippy, tests, cargo-deny) activate together with the first development milestone.

## Project layout

| Path | Contents |
|---|---|
| `scripts/` | Project automation (changelog, checks) |
| `tests/` | Quality strategy and test assets |
| `docs/` | Contributor documentation |
| `licensing/` | License policy and third-party records |
| `policies/` | Privacy, data usage, acceptable use, trademark, governance |
| `changes/` | Changelog fragments and release notes |
| `.github/` | CI workflows and contribution templates |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Commits are signed off under the Developer Certificate of Origin and follow [Conventional Commits](https://www.conventionalcommits.org/). Changes to product behavior must include a changelog fragment and updated documentation.

## Security

Report vulnerabilities privately — see [SECURITY.md](SECURITY.md). Please do not open public issues for security problems. This repository is public: never commit secrets, keys, or tokens.

## Policies

[Privacy](policies/PRIVACY.md) · [Data usage](policies/DATA-USAGE.md) · [Acceptable use](policies/ACCEPTABLE-USE.md) · [Trademark](policies/TRADEMARK.md) · [Governance](policies/GOVERNANCE.md)

## License

Code is licensed under [Apache-2.0](LICENSE). Documentation is licensed under CC-BY-4.0.

# Orbeex

**A free, open-source GIS that you can talk to.**

Orbeex is a Geographic Information System — software for working with maps and spatial
data — built in Rust. What makes it different is that you describe what you want in plain
language, and Orbeex works out the steps, shows you the plan, and runs it for you once you
say yes.

Every action it takes is recorded, reviewable, and reversible. You stay in control, and the
data stays on your machine.

## Why people would use it

- **You can just ask.** Instead of clicking through menus, you type what you need:
  "find every parcel within 500 m of the river and export it as GeoJSON." Orbeex figures
  out the workflow, shows it to you, and runs it after you confirm.
- **Nothing happens behind your back.** Every change is logged as an *operation*. You can
  see the full history, understand each step, and undo anything.
- **Your data stays yours.** The heavy processing runs locally. Only the *intent* or a
  short description of your data is ever sent to an AI model — and only if you allow it.
- **Bring your own AI.** Use OpenAI, Claude, Gemini, DeepSeek, Qwen, or a local model with
  your own API key. No lock-in to one provider.
- **Built to be fast.** The engine is native Rust, so it's built for large datasets and
  smooth maps.

## Where to look first

- **[MASTER_BLUEPRINT.md](MASTER_BLUEPRINT.md)** — the main design document. Start here.
- [`plan/`](plan/) — the roadmap and what we're building next.
- [`brain/`](brain/) — why we made the big decisions, and current project state.
- [`docs/`](docs/) — architecture notes and guides.
- [`licensing/`](licensing/) — the licenses we use and our legal policy.

## Status

Early days. The project skeleton, the rules for contributing, and the build/CI setup are in
place. The GIS engine itself is just starting. If you want the full picture, read the audit
in `brain/knowledge/enterprise-readiness-audit-2026-10-17.md` and the roadmap in `plan/`.

## Getting set up

You'll need Rust (the exact version is pinned in `rust-toolchain.toml`), Python 3.11 or
newer, and Node.js 20.17 or newer.

Once those are installed, these commands check that everything is healthy:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace
cargo deny check
python scripts/changelog/orbeex.py validate-all
python -m pytest scripts/changelog -q
```

Want to help? Read [CONTRIBUTING.md](CONTRIBUTING.md). For how the automated checks work,
see [.github/workflows/README.md](.github/workflows/README.md).

## License

The code is under the Apache 2.0 license. The documentation is under CC-BY-4.0.
See [LICENSE](LICENSE) and the [`licensing/`](licensing/) folder for details.

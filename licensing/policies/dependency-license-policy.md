# Orbeex Dependency License Policy

Enforced by `cargo-deny` in CI. A failing `cargo deny check` is a **blocking**
build failure. This file is the binding policy — it applies from the first
development milestone, when the Rust workspace lands.

## Allowed (permissive)

| License | Notes |
|---|---|
| Apache-2.0 | Preferred |
| MIT | Accepted |
| BSD-2-Clause / BSD-3-Clause | Accepted |
| ISC, Zlib, Unlicense, CC0 | Accepted |
| MPL-2.0 | Accepted if isolated to unmodified files |

## Restricted (requires ADR + legal note)

| License | Condition |
|---|---|
| LGPL-2.1 / LGPL-3.0 | Dynamic linking only; no static link into core |
| EPL-1.0 / EPL-2.0 | Isolated modules only |
| CC-BY-3.0/4.0 | Documentation/data only, not code |

## Forbidden

- GPL-2.0 / GPL-3.0
- AGPL-3.0
- SSPL
- Any non-OSI "source-available" license

## Procedure for adding a dependency

1. Identify the exact license (check the crate's `LICENSE`/`Cargo.toml`).
2. Add an entry to `../third-party/inventory.md`.
3. If Restricted, write an ADR and a legal note under `../policies/`.
4. Run `cargo deny check` locally before raising the PR.

# Orbeex Test Strategy

Full standards: `MASTER_BLUEPRINT.md` §6.

## Philosophy

"Zero-error" is achieved by construction, not hope: memory safety, no panics in UI paths,
typed errors, deterministic execution, and heavy testing of the highest-risk numerics
(geometry & CRS).

## Testing Pyramid

| Layer | Tooling | Scope | CI Gate |
|---|---|---|---|
| Unit | `cargo test` | per-module | every PR |
| Integration | `cargo test` | cross-module | every PR |
| Property | `proptest` | geometry, CRS | nightly + critical modules |
| Fuzz | `cargo-fuzz` | format drivers | nightly |
| AI golden-plan | recorded LLM responses | NL → Operation Graph | every PR touching AI |
| Performance | `criterion` | benchmarks | fail if > 5% regression |
| E2E | UI automation | desktop + web | before merge to main |
| Compatibility | matrix | platform × format | release branches |

## Quality Gates (all must pass)

1. `cargo fmt --check`
2. `cargo clippy -- -D warnings`
3. `cargo test`
4. `cargo deny check` (licenses + advisories)
5. forbidden-`unsafe` check
6. benchmark regression ≤ 5%
7. AI golden-plan suite (when AI touched)

## AI Behavior Testing

- **planning-cases:** NL input → expected Operation Graph (golden files).
- **safety-cases:** inputs that MUST be refused or MUST require confirmation.
- **regression-cases:** every past AI failure locked in as a permanent test.

## Error Handling

- Stable codes `ORX-<AREA>-<NNNN>`, typed via `thiserror`.
- Every error: code + message + cause chain + remediation hint.
- Panics caught at shell boundary; never shown raw.
- Taxonomy documented in `docs/architecture/error-taxonomy.md`.

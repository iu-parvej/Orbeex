# Orbeex Performance Budgets & KPIs

Tracked from Phase 0. Source: `MASTER_BLUEPRINT.md` §6.6.

## Performance Budgets

| Metric | Budget | Measured In |
|---|---|---|
| Viewport Time-to-Display | < 100 ms @ 10M features | `tests/reports/` |
| Operation-graph execution overhead | < 5% | `tests/reports/` |
| Viewport update (interaction) | < 16 ms (60 fps target) | `tests/reports/` |
| Cold start (desktop) | < 2 s | `tests/reports/` |

## Reliability KPIs

| Metric | Target |
|---|---|
| AI valid-plan rate | ≥ 98% at GA |
| Destructive-op incident rate | 0 |
| Crash-free session rate | ≥ 99.9% |
| LLM cost within user budget | 100% |

## Business KPIs

| Metric | Target |
|---|---|
| Valid-plan rate on eval set (P0) | ≥ 90% |
| Benchmark regression per PR | ≤ 5% |
| Third-party plugin usable by AI (P5) | yes/no |

## Method

- Benchmarks via `criterion` in `software/.../benches` and `tests/`.
- Baselines stored in `tests/reports/baselines/`.
- Regressions > 5% fail the PR (Blueprint §6.4).

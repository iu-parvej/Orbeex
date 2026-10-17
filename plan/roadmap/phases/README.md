# Orbeex Roadmap — Phases

Source: `MASTER_BLUEPRINT.md` Appendix B. Detailed per-phase plans live alongside this file.

| Phase | Weeks | Goal | Exit Criterion |
|---|---|---|---|
| **P0** | 0–6 | Foundation & validation | Perf targets validated; ≥90% valid-plan rate; WASM go/no-go |
| **P1** | 6–20 | Core engine MVP | Reproducible 10-step analysis; fuzz-clean |
| **P2** | 20–34 | Desktop application | Analyst completes standard workflow unaided |
| **P3** | 28–44 | AI-native layer | 20 NL scenarios: correct plans + safe refusals |
| **P4** | 40–52 | Web / WASM | Interactive workflows at target latency |
| **P5** | 48–60 | Plugin ecosystem | Third-party plugin tool usable by AI agent |
| **P6** | 56–72 | Enterprise hardening | Mock security review + 100M-feature benchmark |
| **P7** | 72–84 | GA & scale | 1.0 desktop + web; marketplace live |

## Design Principles Across All Phases

1. Retire risk early (spikes before build).
2. Ship value continuously.
3. Every feature reduces to an Operation in the graph.
4. Desktop is the reference; web is a subset.
5. Never compromise auditability for feature velocity.

## Per-Phase Detail

- `phases/P0-foundation.md` … `phases/P7-ga.md`
- Milestones & exit criteria: `../milestones/`

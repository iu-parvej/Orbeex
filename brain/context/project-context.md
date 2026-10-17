# Orbeex Context — Fast Onboarding for AI & Humans

**Read this first, then `MASTER_BLUEPRINT.md`, then `decisions/README.md`.**

## What Orbeex Is

An open-source, **AI-native GIS** written in Rust. Natural language → **reviewable,
reversible, auditable geospatial operations** executed by a high-performance native engine
(desktop + WASM web). Multi-LLM, bring-your-own-key, local-first.

## The One Rule

> **Everything is an Operation.** Every action reduces to an `Operation` node in an
> append-only graph. This gives undo, audit, reproducibility, scripting, and AI safety.
> The AI never mutates data directly — it emits a typed Operation Graph the engine executes.

## Core Stack (planned)

- **Language:** Rust (100% core); `unsafe` forbidden by default.
- **UI:** egui + wgpu (desktop).
- **Web:** WASM (WebGPU + WebGL2 fallback), a degraded subset.
- **Data:** Arrow interchange; GeoPackage/FlatGeobuf/GeoJSON/GeoTIFF/COG.
- **AI:** provider-agnostic (OpenAI, Claude, Gemini, DeepSeek, Qwen, local/Ollama).

## Locked Decisions (see `decisions/`)

- License: **Apache-2.0** (all applicable software) + **CC-BY-4.0** (docs) + **DCO**.
- Docs platform: **Mintlify** (free Starter now; OSS Program later).
- Docs location: **main repo** under `docs-site/`.
- Evaluated, not adopted: **Scalar**, **Fumadocs**, **Docusaurus** (retained as options).

## Directory Map

| Path | Purpose |
|---|---|
| `MASTER_BLUEPRINT.md` | Primary instruction set — read first |
| `plan/` | Roadmap & execution (WHAT/WHEN) |
| `brain/` | Core logic, context, decisions (WHY) |
| `licensing/` | Legal documentation & policy |
| `docs/` | Architecture/guides (source of truth) |
| `docs-site/` | Mintlify public site (MDX + `docs.json`) |
| `research/` | Market & technology evidence |
| `features/` | Feature specs & tracking |
| `tests/` | QA strategy & reports |
| `releases/` | Changelogs & artifacts |
| `_legacy/` | Read-only archive |

## Operating Standards (short)

- No `unsafe`; no panics in UI paths; typed errors with stable codes (`ORX-<AREA>-<NNNN>`).
- Every feature: spec → ADR (if structural) → code → tests → docs → changelog fragment.
- Quality gates: fmt, clippy `-D warnings`, tests, `cargo-deny`, no-unsafe check, benchmarks.
- Docs ship **in the same PR** as the feature.

## Current State

Foundation phase. Structure + Master Blueprint + ADRs established; no source code yet.
See `state/current-state.md` and `plan/roadmap/`.

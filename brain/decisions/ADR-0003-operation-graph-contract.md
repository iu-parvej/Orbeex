# ADR-0003 — The Operation Graph as the Universal Contract

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | — |

## Context

Orbeex must guarantee undo, auditability, reproducibility, and safe AI execution. Existing
GIS tools treat these as separate features bolted onto GUI actions — making them
inconsistent, incomplete, and hard to audit.

## Decision

**Every action in Orbeex — human or AI, desktop or web, core or plugin — reduces to an
`Operation` node in an append-only operation graph.**

The AI never mutates data directly. It emits a **typed Operation Graph**, which the engine
validates (type + policy + cost) and executes deterministically. The graph is journaled so
sessions restore to the last committed node after a crash.

## Rationale

A single abstraction gives, for free:

- **Undo/redo** — move a cursor in the graph.
- **Auditability** — every change is a logged node with a reasoning trace.
- **Reproducibility** — replays are deterministic (AI is isolated in planning).
- **Scripting** — the graph is serializable and machine-authorable.
- **Incremental recompute** — changing a node recomputes only its downstream dependents.

## Consequences

- **Positive:** one contract for undo, audit, repro, scripting, and AI safety.
- **Negative:** all code must express work as Operations; ad-hoc mutation is banned.
- **Follow-up:** the Operation schema is versioned with a backward-compat policy (Blueprint §5.1).

## Alternatives Considered

- **Command pattern only** — insufficient: no dependency graph, weak reproducibility.
- **Event sourcing without a graph** — replayable but no dependency-aware recompute.
- **Direct mutation with a separate undo stack** — the incumbent approach. Rejected: this is
  exactly the design that makes existing tools unauditable and unsafe for AI.

# ADR-0008 — Fumadocs Evaluated, Not Adopted

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md), [ADR-0006](ADR-0006-scalar-evaluation-mintlify-confirmed.md) |

## Context

Orbeex evaluated **Fumadocs** (https://www.fumadocs.dev/) — an MIT-licensed React/Next.js
documentation **framework** — as a self-hosted alternative to Mintlify.

Distinction: Fumadocs is a **framework** (you build and host the site); Mintlify is a
**hosted service** (they host it).

## Evaluation Findings

| Axis | Winner |
|---|---|
| Zero-ops / speed | **Mintlify** |
| UI polish out-of-box | Mintlify (near-tie) |
| OpenAPI / API reference | **Mintlify** (Fumadocs author concedes this) |
| Full control / customizability | **Fumadocs** |
| Open-source / self-host sovereignty | **Fumadocs (MIT)** |
| Programmatic editing | **Fumadocs** (it's just code) |
| Cost (money) | Tie ($0) |
| Cost (engineering time) | **Mintlify** |

**Key data point:** Fumadocs' own creator states on his comparison page: *"Fumadocs is not
as powerful as Mintlify, for example, the OpenAPI integration of Mintlify… I wouldn't
recommend switching to Fumadocs from Mintlify if you're satisfied with the current way you
build docs."*

## Decision

**Adopt Mintlify; Fumadocs evaluated and not adopted.** Fumadocs would require Orbeex (a
Rust GIS/AI team) to become a permanent Next.js/React web team and own docs infrastructure —
a large, permanent tax for gains (customizability, sovereignty) that are not our bottleneck.

## Consequences

- **Positive:** keep zero-ops, free, polished docs; stay focused on GIS + AI.
- **Negative:** no full self-host sovereignty today.
- **Reversible:** docs remain portable MDX; Fumadocs consumes MDX, so migration is possible
  later with no content loss if total self-hosting becomes a requirement.

## Alternatives Considered

- **Fumadocs (self-hosted)** — deferred; high ops cost.
- **Docusaurus (self-hosted)** — deferred; higher ops than needed.

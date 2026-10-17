# ADR-0001 — Adopt Apache-2.0 for Code, CC-BY-4.0 for Documentation

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | — |

## Context

Orbeex is a free, community-driven, enterprise-targeted GIS. The license must balance:

- **Ease of adoption** (enterprise procurement, embedding, commercial use).
- **Patent protection** (critical for an enterprise-trust product).
- **Contributor clarity** (contribution terms must be unambiguous).
- **No barrier to the web/SaaS model** (rules out network-copyleft like AGPL).

## Decision

- **Source code:** Apache License 2.0.
- **Documentation:** Creative Commons Attribution 4.0 International (CC-BY-4.0).
- **Contribution:** DCO (Developer Certificate of Origin) required; no CLA at this time.

## Rationale

Apache-2.0 is permissive (maximum adoption, commercial-friendly) and includes an explicit
**patent grant**, unlike MIT. Strong copyleft (GPL/AGPL) would block the enterprise and
hosted adoption Orbeex depends on. CC-BY-4.0 is the documentation-standard permissive
license.

## Consequences

- **Positive:** broad adoption, patent safety, enterprise-friendly, procedurally simple.
- **Negative:** no copyleft protection — downstream closed forks are permitted.
- **Follow-up:** enforce dependency compatibility via `cargo-deny` (`deny.toml`).

## Alternatives Considered

- **MIT** — simplest, but no patent grant. Rejected for enterprise trust reasons.
- **AGPL-3.0** — protects against SaaS free-riding, but blocks the target market. Rejected.
- **Dual-license / open-core** — possible later; deferred (see ADR on relicensing policy).

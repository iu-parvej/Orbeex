# ADR-0007 — Adopt Apache-2.0 for All Applicable Software, CC-BY-4.0 for Docs, DCO for Contributions

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | none (clarifies/extends [ADR-0001](ADR-0001-license-selection.md)) |

## Context

ADR-0001 chose Apache-2.0 for code and CC-BY-4.0 for docs. The user directed that Apache-2.0
apply to the **full software and everything applicable**, not just a subset, and confirmed
CC-BY-4.0 for documentation and DCO for contributions.

## Decision

- **Apache-2.0** covers **all applicable Orbeex software**: source crates, plugins, tools,
  scripts, config, examples, and build tooling.
- **CC-BY-4.0** covers **all documentation** (public docs and in-repo docs).
- **DCO** (Developer Certificate of Origin, `Signed-off-by`) is required on all contributions.

## Rationale

Apache-2.0 is permissive, enterprise-friendly, and includes an explicit **patent grant**
(unlike MIT). Applying it uniformly avoids per-file license ambiguity. CC-BY-4.0 is the
standard permissive documentation license. DCO gives contributor clarity without a CLA.

## Consequences

- **Positive:** uniform, unambiguous licensing; enterprise trust; simple contribution terms.
- **Negative:** no copyleft protection (closed forks permitted) — accepted intentionally.
- **Follow-up:** SPDX headers on all source files; `NOTICE` and SBOM generated per release;
  `cargo-deny` enforces dependency compatibility (see `licensing/`).

## Alternatives Considered

- **MIT** — no patent grant. Rejected.
- **GPL/AGPL** — blocks target enterprise/web model. Rejected.
- **CLA instead of DCO** — reserved for a future relicense-need ADR.

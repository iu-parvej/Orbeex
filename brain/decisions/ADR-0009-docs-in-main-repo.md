# ADR-0009 — Documentation Lives in the Main Orbeex Repository

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md), [ADR-0005](ADR-0005-mintlify-oss-program-sequencing.md) |

## Context

Question raised: should Mintlify documentation live in a **separate GitHub repository**
(e.g. `orbeex-docs`) instead of inside the main Orbeex repository?

## Decision

**Keep documentation in the main Orbeex repository**, under `docs-site/` (Mintlify MDX +
`docs.json`). Do **not** create a separate docs repo.

Also: **do not use Mintlify's private organization repository.** Connect Mintlify's Git sync
to **our** repo and point it at the `docs-site/` path. If Mintlify already created a private
org repo during onboarding, use **"Clone to your own repository"** to move content into the
Orbeex repo.

## Rationale

- Blueprint §7.3 rule 2 requires a behavior-changing PR to update docs **in the same PR**.
  A separate repo makes this impossible to enforce and causes immediate docs drift.
- One PR = code + docs reviewed together; atomic changes and history.
- Mintlify Git sync supports a docs **subdirectory**, so a second repo is unnecessary.
- Avoids submodules, cross-repo sync automation, and "which repo is source of truth?" confusion.
- Matches the planned structure (`docs-site/` sits alongside `plan/`, `brain/`, `crates/`, …).

## Consequences

- **Positive:** atomic code+docs changes; single review; no sync overhead.
- **Negative:** docs commits are mixed into the main repo history (acceptable; scoped by path).
- **Follow-up:** connect Mintlify Git sync to the Orbeex repo → `docs-site/`.

## Alternatives Considered

- **Separate `orbeex-docs` repo** — rejected: drift, double-review, sync overhead. Makes sense
  only for a separate docs team, independent versioning, or public/private split — none apply.
- **Mintlify-hosted private org repo** — rejected: fragments ownership; keep docs in our repo.

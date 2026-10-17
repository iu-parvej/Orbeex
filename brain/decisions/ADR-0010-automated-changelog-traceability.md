# ADR-0010 — Automated Changelog, Traceability & Docs/Roadmap Sync

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | ADR-0003 (Operation Graph), ADR-0004 (Mintlify), ADR-0009 (docs in main repo) |

## Context

Orbeex needs enterprise-grade **traceability, auditability, and documentation discipline**:
every feature's creation/modification/removal must be recorded, and docs + roadmap must stay
aligned with the real feature state. Manual maintenance drifts.

## Industry Best Practices Adopted

- **Keep a Changelog 1.1.0** — human-readable changelog; canonical change types
  (Added/Changed/Deprecated/Removed/Fixed/Security); ISO 8601 dates; reverse-chronological.
- **towncrier fragment model** — one change note per PR in a `changes/` directory, compiled
  into the changelog at release. Avoids merge conflicts and "git log as changelog".
- **Semantic Versioning 2.0.0** — version semantics (already in Blueprint §5.1).
- **Conventional Commits** — structured commit messages (Blueprint §5.3).
- **Requirements traceability** — each feature maps to `FR-*` IDs, spec, docs, and release.
- **Docs-as-code** — docs ship in the same PR (Blueprint §7.3).

## Decision

Implement an automated changelog + feature-tracking + docs/roadmap-sync system:

1. **`changes/`** — fragments under `unreleased/`, compiled releases under `releases/`,
   `migrations/` for breaking changes, `templates/` for scaffolding.
   Top-level **`CHANGELOG.md`** follows Keep a Changelog; `changes/releases/` archives versions.
2. **Feature registry** — `features/registry/features.yaml`, machine-readable source of truth
   for feature state and traceability (id, status, area, priority, milestone, requirements,
   spec, docs, introduced, changes).
3. **Automation** — `scripts/changelog/orbeex.py` (pure stdlib, no deps):
   `validate-fragment`, `validate-all`, `compile`, `sync-docs`, `new-fragment`; plus
   `require_fragment.py` (CI gate).
4. **CI enforcement** — `.github/workflows/changelog.yml` runs validation, docs-sync, and the
   fragment-required gate on every PR.

## Rationale

- Fragments eliminate changelog merge conflicts and guarantee completeness.
- A machine-readable registry makes traceability and auditability automated, not aspirational.
- Pure-stdlib tooling runs anywhere (CI, locally) with no dependency or supply-chain cost.
- Enforced in CI → the process cannot silently rot.

## Consequences

- **Positive:** auditable, traceable, self-consistent docs/roadmap/changelog; zero-drift.
- **Negative:** contributors must add one small fragment per behavior-changing PR (cheap).
- **Follow-up:** add `mint validate`/`broken-links` to CI when `docs-site/` grows;
  extend `sync-docs` to regenerate `plan/roadmap` status tables if needed.

## Alternatives Considered

- **Manual CHANGELOG only** — rejected: drifts, incomplete, merge conflicts.
- **Git log as changelog** — rejected (Keep a Changelog's explicit anti-pattern).
- **External tool (towncrier/changesets)** — not chosen: Python/Node toolchain assumptions;
  a small pure-stdlib tool fits the monorepo and CI with no extra dependencies.

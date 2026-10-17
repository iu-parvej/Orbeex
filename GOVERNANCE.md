# Governance

## Model

Orbeex is a community-driven open-source project. It follows a **lightweight meritocratic**
model: contributors earn trust and responsibility through sustained, high-quality
contributions.

## Roles

| Role | Responsibilities |
|---|---|
| **Contributor** | Submits issues, docs, or code via pull requests. |
| **Reviewer** | Reviews PRs in an area; may be listed in `CODEOWNERS`. |
| **Maintainer** | Merges PRs, manages releases, stewards the roadmap and ADRs. |

## Decision-making

- **Day-to-day changes** (bug fixes, docs, small features): consensus via PR review.
- **Architectural/structural changes**: an **ADR** must be accepted before implementation
  (see `brain/decisions/`). ADRs are immutable once accepted; supersede, don't edit.
- **Project-wide or breaking changes**: maintainer approval + an ADR + a migration note
  under `changes/migrations/`.

## Becoming a maintainer

Sustained, high-quality contributions and constructive reviews. Existing maintainers
nominate; consensus among maintainers decides.

## Releases

Maintainers cut releases per `MASTER_BLUEPRINT.md` §5.5. All release artifacts are signed
and published with an SBOM and provenance.

## Licensing

All contributions are under the Apache License 2.0 by virtue of the DCO sign-off. A CLA is
not currently required (see `brain/decisions/ADR-0001`).

## Amendments

Changes to this document require a PR and maintainer consensus.

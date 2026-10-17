# ADR-0005 — Mintlify Adoption Sequencing: Free Starter Now, OSS Program Later

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | — |
| **Related** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md) |

## Context

ADR-0004 selected Mintlify as the documentation platform. Its Developer API / Admin APIs /
webhooks are **Pro-only**, and Mintlify offers a **free-forever Pro tier for qualifying
non-commercial open-source projects** via the OSS Program
(https://www.mintlify.com/oss-program#eligibility).

At this stage Orbeex is in early foundation work: the project is not yet publicly
established, and the OSS Program expects a recognized open-source license and a
non-commercial, community-driven project (no venture backing or for-profit ownership).

## Decision

1. **Now:** Use the **free Mintlify Starter plan** ($0/mo, free forever) — hosting, custom
   domain, web editor, Git sync, MCP server, API playground, search, 5 editor seats.
   Authoring and publishing happen via **Git** (MDX + `docs.json` in `docs-site/`).
2. **Later:** After the project is publicly established (license in place, public repo,
   community presence), **apply to the Mintlify OSS Program** for free Pro to unlock the
   **Developer API** and automated/API-driven editing.

## Rationale

- The Starter plan fully covers our needs today (Git-native docs, hosting, custom domain).
- Applying early would weaken the OSS Program application; applying once established
  maximizes eligibility and approval odds.
- No content or workflow is lost by starting free — docs are plain MDX in Git and migrate
  to Pro seamlessly.

## Consequences

- **Positive:** zero documentation cost now; no lock-in; clean upgrade path.
- **Negative:** API-driven editing/webhooks deferred until Pro is granted.
- **Follow-up (at time of application):**
  - Ensure the repo is public with the Apache-2.0 `LICENSE` in place.
  - Confirm non-commercial / community-driven status (no VC funding, no for-profit owner).
  - Submit application: https://www.mintlify.com/oss-program#eligibility

## Alternatives Considered

- **Apply to OSS Program immediately** — rejected: premature; better odds once established.
- **Pro (paid)** — rejected: unnecessary cost while OSS Program is available.

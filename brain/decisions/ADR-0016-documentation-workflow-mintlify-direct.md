# ADR-0016 — Public Documentation Workflow: `documentation/` Source, Mintlify-Direct Publishing

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | Publishing mechanics from [ADR-0009](ADR-0009-docs-in-main-repo.md) (single-repo principle is retained) |
| **Related** | [ADR-0004](ADR-0004-documentation-platform-mintlify.md), [ADR-0014](ADR-0014-professional-compact-writing-style.md) |

## Context

Documentation publishing has moved to a **Mintlify-direct** model. The Mintlify MCP
connection is active and pinned to project `portfolioofparvej/orbeex` — live at
https://orbeex.mintlify.app. Content has been rewritten for a broad, global,
non-technical audience, and the source pages now live in `documentation/`.

## Decision

1. **`documentation/` is the single local source** for public documentation pages
   (`*.mdx`). Its `README.md` defines the workflow and is binding.
2. **Publishing is direct to Mintlify via MCP tools** on branch `main`:
   `write_page` (existing pages), `create_node` (new pages), `move_node`/`update_node`
   (structure), then `publish`, confirmed with `deployment_status` until `live: true`.
3. **No `git push` for documentation.** Publishing flows through Mintlify's own Git
   integration. Local commits are made only for history/revert safety.
4. **Audience rule:** public pages target a broad, global, non-technical audience — clear
   everyday words, short sentences, accurate status claims, no jargon without explanation,
   no filler or emoji. Developer-oriented pages remain published under "Advanced topics".
5. **Content derivation:** pages draw their facts from `brain/` (decisions, context,
   knowledge) and `plan/` (roadmap) — never invented product claims.

## Rationale

- Direct MCP publishing removes GitHub from the documentation loop — faster iteration and
  no second push path to manage (a persistent user requirement).
- `documentation/` separates public-doc source from internal developer docs (`docs/`) and
  internal reference material, matching what the project syncs to Mintlify.
- A broad audience was unreachable with developer-first text; the earlier register tests
  showed plain, warm-compact language works best, with a professional register.

## Consequences

- **Positive:** docs update in minutes through one tool path; source and live site stay in
  sync; safe for Claude/AI editing because Mintlify's approval and review flow applies.
- **Negative:** docs content does not run through the normal review CI (lint/test/deny).
  Mitigation: tone/claim review per `documentation/README.md` and this ADR.
- **Follow-up:** keep `documentation/` and the live site in sync at all times; revisit if
  the Mintlify MCP loses the pinned-project connection (re-authentication handles it).

## Alternatives Considered

- **Keep `docs-site/` + Git-only publishing** — rejected: slower loop and a second push
  path, superseded by user direction.
- **AI edits inside the Mintlify dashboard only** — rejected: not machine-reproducible and
  drops local source-of-truth files.

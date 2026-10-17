# brain/ — Core Logic, Context & Decisions

Repository for core project logic, essential context, and high-level decision-making data.

**Scope:** WHY we build it this way and HOW we THINK about it.
**Not here:** scheduling (→ `plan/`), legal (→ `licensing/`).

## Contents

| Path | Purpose |
|---|---|
| `vision/` | Canonical vision statements (source of truth for "why") |
| `decisions/` | Architecture Decision Records (ADRs) — immutable, numbered |
| `context/` | Essential project context for onboarding AI + humans |
| `knowledge/` | Domain knowledge: GIS, CRS, formats, LLM behavior, decision log |
| `prompts/` | Canonical prompt templates used by the AI layer |
| `agents/` | Agent role definitions and orchestration specs |
| `state/` | Current project state snapshots |

**Protocol:** `decisions/` is the highest-authority technical record. ADRs are **never
edited after acceptance** — supersede with a new ADR. Naming: `ADR-NNNN-<slug>.md`.

## MANDATORY: Capture Every Decision Here

Every decision made during any working session **must be persisted in `brain/`** so future
AI/human collaborators can read and reuse it. This is a standing rule.

At the end of each session, ensure:

1. **New decisions** → a new `decisions/ADR-NNNN-<slug>.md` + rows in
   `decisions/README.md` and `knowledge/decision-log.md`.
2. **Reusable findings/knowledge** → `knowledge/`.
3. **Current status** → update `state/current-state.md`.
4. **Project context changes** → update `context/project-context.md`.
5. **Research evidence** → `research/` (and referenced from `knowledge/`).

If a decision changes an earlier one, mark the old ADR **Superseded** (never edit it).

## Quick Start for an AI Resuming Work

1. Read `MASTER_BLUEPRINT.md`.
2. Read `context/project-context.md`.
3. Read `decisions/README.md` and `knowledge/decision-log.md`.
4. Read `state/current-state.md`.
5. Continue from "Not Started" / "Open Questions".

## Standing Rules

- **Writing style:** all human-facing docs use professional, compact, plain English (see
  `knowledge/writing-style-guide.md`, ADR-0014). No AI-sounding filler.
- **Public docs workflow (mandatory):** source pages live in `documentation/`; publish
  directly to Mintlify via MCP tools on branch `main`, verify with `deployment_status`,
  **never `git push` for docs**. Audience: broad, global, non-technical. See ADR-0016 and
  `plan/execution/documentation-workflow.md`.
- **The repo is public:** never commit secrets (see `knowledge/security-guide.md`,
  ADR-0012). Install the pre-commit hook.
- **Every decision gets recorded here** (see above).

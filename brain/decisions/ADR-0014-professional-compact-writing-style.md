# ADR-0014 — Professional, Compact Documentation Style

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Supersedes** | [ADR-0013](ADR-0013-plain-english-writing-style.md) |

## Context

ADR-0013 set a plain-English, warm tone. In practice this drifted toward informal, wordy
prose. The project needs the register used by well-run software companies: professional,
compact, factual — the kind of writing that presents each feature clearly and concisely.

## Decision

Adopt a **professional, compact** style for all human-facing documentation. Full guide:
`brain/knowledge/writing-style-guide.md`.

Principles:
- Concise and factual. Every sentence carries information.
- Neutral tone. No marketing language, no exclamation marks, no emoji or decorative icons.
- Plain words, short sentences, one idea each.
- Lead with function; add context only if it helps.
- Structured for scanning: short paragraphs, tight lists, tables.
- Accurate about status — no overstating.

## Rationale

- Compact, factual docs are faster to read and easier to maintain.
- A neutral, professional register builds credibility with enterprise and technical readers.
- Consistent structure makes features comparable and the documentation predictable.

## Consequences

- **Positive:** dense, readable, professional documentation; consistent across the project.
- **Negative:** tone is a human review responsibility, not automatically enforced.
- **Follow-up:** apply to README, `CONTRIBUTING.md`, and all future docs. This supersedes the
  warmer tone of ADR-0013.

## Alternatives Considered

- **Warm/informal tone (ADR-0013)** — superseded: drifted wordy and informal.
- **Academic/formal register** — rejected: less scannable, slower to read.

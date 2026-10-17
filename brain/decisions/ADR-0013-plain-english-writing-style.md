# ADR-0013 — Documentation Writing Style

| Field | Value |
|---|---|
| **Status** | **Superseded by ADR-0014** |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | ADR-0004 (Mintlify docs) |
| **Superseded by** | [ADR-0014](ADR-0014-professional-compact-writing-style.md) |

## Context

Documentation should read like a person wrote it — clear, warm, and easy to follow. It was
drifting toward a stiff, "AI-sounding" tone with jargon and filler, which makes it harder
for newcomers and contributors.

## Decision

Adopt a **plain-English, human tone** for all human-facing writing: README files, docs,
comments, error messages, release notes. The full guide lives in
`brain/knowledge/writing-style-guide.md`.

Key points:
- Simple everyday words; short sentences; talk to the reader as "you".
- Lead with why, then how.
- No AI filler ("leverage", "seamless", "robust", "delve", "in today's world", etc.).
- Explain technical terms once, in plain words.
- Be honest about project status; don't oversell.

This does **not** change precise technical wording inside code where exact meaning matters.

## Rationale

- Plain writing is easier to translate, easier to search, and friendlier to newcomers.
- A consistent voice builds trust and makes the project feel human.
- It reduces review friction: everyone shares one standard.

## Consequences

- **Positive:** friendlier docs; lower barrier for contributors and users.
- **Negative:** tone is reviewed by humans, not linted automatically.
- **Follow-up:** reviewers apply the guide; new docs follow the examples in `README.md` and
  `CONTRIBUTING.md`.

## Alternatives Considered

- **Formal/technical register** — rejected: cold and harder to read.
- **Automated tone linter** — rejected for now: no reliable tool; human review is fine at
  this size.

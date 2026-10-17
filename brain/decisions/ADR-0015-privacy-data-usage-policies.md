# ADR-0015 — Enterprise Privacy & Data-Usage Policy Set

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | ADR-0012 (secret prevention), ADR-0001 (licensing) |

## Context

Orbeex handles sensitive spatial data (infrastructure, survey, and sometimes personal
data), and its AI features transmit requests to third-party model providers. Enterprise and
public-sector users require clear, precise statements about how data is handled. Comparable
projects publish a standard policy set. Orbeex had none.

## Decision

Adopt a full policy set, written in the professional, compact register (ADR-0014):

| Document | Purpose |
|---|---|
| `PRIVACY.md` | What data is processed, what is collected, user controls, regulatory position |
| `DATA-USAGE.md` | Mechanical data flow, what leaves the machine, telemetry levels |
| `ACCEPTABLE-USE.md` | Permitted and prohibited use |
| `TRADEMARK.md` | Use of the Orbeex name and logo, fork rules |
| `SECURITY.md` | Reporting, SLAs, secret handling (already present) |
| `GOVERNANCE.md` | Decision-making and roles (already present) |

Core commitments:
- **Local by default.** No data leaves the machine unless AI features are enabled.
- **No collection.** No telemetry, no crash reports, no usage data in the current version.
- **Schema, not data.** Only intent and schema are sent to providers by default.
- **Optional and reversible.** Every network feature is opt-in and can be disabled.
- **Local models supported** for full isolation.

## Rationale

- Enterprise procurement requires explicit data-handling statements.
- Orbeex's differentiator is data sovereignty; the policy set makes that concrete.
- Clear policies reduce legal risk and set user expectations.

## Consequences

- **Positive:** procurement-ready; the sovereignty claim becomes verifiable.
- **Negative:** policies must be maintained as features are added (for example, telemetry or
  update checks would require a `DATA-USAGE.md` update before release).
- **Follow-up:** update `DATA-USAGE.md` before shipping any telemetry or network feature.

## Alternatives Considered

- **Single combined policy file** — rejected: less precise, harder to reference.
- **No policies until later** — rejected: blocks enterprise adoption and is harder to
  retrofit.

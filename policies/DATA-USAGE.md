# Data Usage

**Last updated: 2026-10-17**

This document describes how Orbeex processes data, what leaves your machine, and the
controls available to you. It complements [PRIVACY.md](PRIVACY.md), which states the policy;
this document describes the mechanics.

## Data flow overview

```
Local machine                                  Network (only if AI enabled)
──────────────────────────────────────────     ──────────────────────────────
Dataset ──► Engine ──► Operation graph         Task intent + dataset schema
              │              │                        │
              │              ▼                        ▼
              │        Project file            LLM provider (your account)
              │        Audit log
              ▼
   All processing stays local
```

## What is processed locally

- All reading, writing, and transformation of geospatial data.
- The operation graph: an append-only record of every action, used for undo, audit, and
  reproducibility.
- Project files and the local audit log.
- API keys, stored in the operating system keychain.

## What may be sent to a model provider

Only when AI features are enabled, and only for the task in progress:

| Data | Sent by default | Notes |
|---|---|---|
| Task description (your words) | Yes | The instruction you typed. |
| Dataset schema | Yes | Field names, types, CRS, extent. No values. |
| Raw geometry and attributes | No | Sent only if you enable it for that task. |
| File paths | No | Not transmitted. |
| API keys | N/A | Used locally to authenticate; handled by the keychain. |

## Controls

- **Disable AI entirely** — the software operates as a standard GIS with no network access.
- **Select a provider** — you choose which provider receives requests.
- **Local mode** — use a local model (for example via an Ollama-compatible endpoint). No
  data leaves the machine.
- **Per-task redaction** — restrict additional context on a case-by-case basis.

## Default telemetry level

| Level | Status |
|---|---|
| Telemetry | Off. None is collected in the current version. |
| Crash reporting | Off. Submission is manual and optional. |
| Update checks | Not implemented. |

Any future telemetry will be opt-in, documented here before release, and inspectable.

## Auditability

Every operation is recorded locally in the operation graph. You can review the complete
history of changes to a project, and optionally export it.

## Contact

Open an issue in the repository for questions about data handling.

# changes/ — Changelog & Change Management

Structured, auditable changelog system. Based on **Keep a Changelog 1.1.0** semantics and
the **towncrier** *fragment* model, adapted for Orbeex (Blueprint §5, §7).

## How it works

- Each PR adds **one change fragment** to `unreleased/`.
- At release time, fragments are compiled into `releases/<version>.md` and removed.
- CI **validates** every fragment (`scripts/changelog/validate.py`) and enforces that a
  change fragment exists for any feature/behavior change.

## Fragment naming

```
unreleased/<ref>.<type>.md
```

- `<ref>` = the change's unique reference: feature ID (`F-0042`), issue/PR number, or an
  orphan ref starting with `+`.
- `<type>` = one of the canonical types below (Keep a Changelog set):

| Type | Keep a Changelog section | Meaning |
|---|---|---|
| `added` | Added | New feature/capability |
| `changed` | Changed | Change in existing functionality |
| `deprecated` | Deprecated | Soon-to-be-removed functionality |
| `removed` | Removed | Removed functionality |
| `fixed` | Fixed | Bug fix |
| `security` | Security | Vulnerability fix |
| `docs` | Documentation | Documentation-only change |
| `internal` | (hidden) | Build/CI/chore; not shown to users |

Examples:
```
unreleased/F-0042.added.md
unreleased/PR-118.fixed.md
unreleased/+typo-fix.docs.md
```

## Fragment format

Markdown with front-matter. `type` and `ref` are derived from the filename; `area` and
`feature` link to the feature registry for traceability.

```markdown
---
area: engine            # engine | ai | platform | plugin | docs | infra
feature: F-0042         # optional feature ID assigned by maintainers
breaking: false         # true if this is a breaking change
---

A concise, user-facing description of the change written in the imperative mood.
```

## Governance Rules

1. **One fragment per PR** minimum; more only if the PR spans distinct change types.
2. A PR touching behavior **must** include a fragment (enforced in CI).
3. Fragments are immutable once merged into a release; corrections are new entries.
4. `breaking: true` requires a migration note in `migrations/`.
5. Dates are ISO 8601 (`YYYY-MM-DD`).
6. The compiled changelog is the **human** record; the feature registry is the **machine**
   record; both are reconciled by CI.

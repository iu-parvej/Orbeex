# features/ — Feature Tracking

Feature specifications and development tracking. Lifecycle folders:

| Folder | Meaning |
|---|---|
| `backlog/` | Proposed, not started |
| `in-progress/` | Actively being built |
| `completed/` | Shipped |
| `templates/` | Spec + test-plan templates |
| `registry/` | Machine-readable feature registry (`features.yaml`) |

## Feature lifecycle

1. **Propose** — create `backlog/F-NNNN-<slug>/` from the template; add an entry to
   `registry/features.yaml` (status `proposed`).
2. **Implement** — move folder to `in-progress/`; set registry status `in-progress`; add
   change fragment(s) to `changes/unreleased/`.
3. **Ship** — move to `completed/`; set registry status `shipped` + `introduced: <semver>`;
   compile changelog; update docs and the roadmap.

## Conventions

- Feature ID: `F-NNNN` (unique, never reused).
- Folder name: `F-NNNN-<short-slug>`.
- Every feature traces to requirement IDs (`FR-*`) from the Master Blueprint.
- Every shipped feature has a test plan with acceptance criteria linked to its requirements.

See `README.md` (feature docs) and `../MASTER_BLUEPRINT.md` §2, §6.

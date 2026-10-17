# ADR-0012 — Secret Prevention & Public-Repo Safety

| Field | Value |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-10-17 |
| **Deciders** | Orbeex Core Team |
| **Related** | ADR-0011 |

## Context

The `main` branch will be a **public** repository. A single committed secret would be
exposed permanently (git history is forever), and a personal email in commit history would
be published. This needs to be prevented, not just detected.

## Decision

Adopt layered secret prevention, and rewrite local history to remove a personal email
before any push.

1. **`.gitignore` hardening** — block `.env` files, keys, certificates, tokens, credential
   files, and cloud-tool config. Allow only the safe `.env.example` template.
2. **Pre-commit hook** — `gitleaks` plus hygiene hooks (large files, merge conflicts,
   private keys, whitespace). Config: `.pre-commit-config.yaml`.
3. **CI scanning** — `.github/workflows/secret-scan.yml` runs gitleaks over full history on
   push/PR/daily. Config: `.gitleaks.toml`.
4. **GitHub push protection** — to be enabled in repo settings once pushed.
5. **Commit identity** — no personal emails. History was rewritten to
   `Orbeex Contributors <orbeex@users.noreply.github.com>`; backup refs, stash, and reflogs
   purged.
6. **Runtime design** — LLM API keys live in the OS keychain, never in repo files.

## Rationale

- Prevention (gitignore + hook + push protection) is better than cleanup.
- Rotating a leaked secret is the only real fix after exposure; history rewriting is
  secondary.
- A noreply commit identity protects contributor privacy on a public repo.

## Consequences

- **Positive:** very low chance of a secret ever reaching the public repo; privacy preserved.
- **Negative:** contributors must install the pre-commit hook to get local scanning (CI still
  catches it either way).
- **Note:** the noreply email is a placeholder until the real GitHub username is known; it
  should be updated to `<id>+<username>@users.noreply.github.com` before/at first push.

## Alternatives Considered

- **Rely on `.gitignore` alone** — rejected: too easy to bypass.
- **Squash/single-commit history** — rejected: keeps commits meaningful and revertible.
- **Leave the personal email** — rejected: publishes private data on a public repo.

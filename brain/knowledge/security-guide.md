# Keeping the Public Repo Safe

The `main` branch is **public**. This doc explains how we keep secrets and sensitive data
out of it, and what to do if one slips through.

## The layers of defense

We don't rely on any single check. Five layers, cheapest first:

1. **`.gitignore`** — blocks the obvious things before git even looks at them:
   `.env` files, keys (`*.key`, `*.pem`, `*.p12`), certificates, tokens, credential files,
   and cloud tool config (`~/.aws`, `.npmrc`, `.cargo/credentials.toml`).
   The safe template `.env.example` is explicitly allowed with `!.env.example`.

2. **Pre-commit hook (gitleaks)** — scans what you're about to commit, locally. Set up once:
   ```bash
   pip install pre-commit
   pre-commit install
   ```
   Config: `.pre-commit-config.yaml`. It also checks for large files, merge conflicts,
   private keys, and trailing whitespace.

3. **CI secret scanning** — `.github/workflows/secret-scan.yml` runs gitleaks over the
   **full git history** on every push, PR, and once a day. Config: `.gitleaks.toml`.

4. **GitHub push protection** — turn this on in the repo (Settings → Code security). GitHub
   then refuses a push that contains a detected secret, before it ever lands.

5. **Never write secrets to the repo by design** — Orbeex stores LLM API keys in the OS
   keychain at runtime, never in project files.

## The one rule that matters most

**Assume anything pushed is already leaked.** Deleting the file or rewriting history does
not take it back. So:

- **If you ever commit a real secret: rotate it first.** Immediately. Then clean up.

## What to do if a secret is committed

1. **Rotate/revoke the credential.** This is the actual fix. Do it before anything else.
2. Remove it from history with `git filter-repo` (GitHub's recommended tool).
3. Force-push, and tell any collaborators to re-clone.
4. If it's sensitive, contact GitHub Support to purge cached views.

## What we already verified

- No secrets, tokens, or private keys in the tracked files (scanned 2026-10-17).
- No personal email in git history — all commits use
  `Orbeex Contributors <orbeex@users.noreply.github.com>`.

## Commit identity policy

Commits must **not** expose a personal email. Use a GitHub noreply address:

```bash
git config user.name "Your Name"
git config user.email "<your-github-id>+<username>@users.noreply.github.com"
```

Before this policy was applied, the local history was rewritten with `git filter-branch` to
replace a personal email, then backup refs, the stash, and reflogs were purged so the old
address no longer exists anywhere in the repository objects.

## Enabling protection on GitHub (do this once it's pushed)

- Settings → Code security → enable **Secret scanning** and **Push protection**.
- Settings → Branches → protect `main`: require PRs, require status checks
  (see `.github/workflows/README.md`), require signed commits, block force-pushes.

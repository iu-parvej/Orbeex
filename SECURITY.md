# Security Policy

## Supported versions

Orbeex is in early development (pre-1.0). Security fixes are applied to the latest release
and the `main` branch.

| Version | Supported |
|---|---|
| `main` (unreleased) | ✅ |
| Latest tagged release | ✅ |
| Older releases | ❌ |

## Reporting a vulnerability

**Do not open a public issue for security vulnerabilities.**

Report privately using GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
(Security → Advisories → "Report a vulnerability"), or email the maintainers if enabled for
the repository.

Please include:

- A description of the issue and its impact.
- Steps to reproduce (proof of concept if possible).
- Affected version/commit.
- Any suggested remediation.

## What to expect

- **Acknowledgement** within 3 business days.
- **Initial assessment** (severity, affected versions) within 7 business days.
- A coordinated disclosure timeline; we aim to release a fix within 90 days of a confirmed
  high/critical issue, sooner when practical.
- Credit in the advisory, unless you prefer to remain anonymous.

## Response targets (SLA)

| Severity | Initial response | Target fix |
|---|---|---|
| Critical | 3 business days | 14 days |
| High | 5 business days | 30 days |
| Medium | 10 business days | 90 days |
| Low | Best effort | Next release |

## Supply chain

Orbeex targets **SLSA Build L2** provenance now, hardening toward **L3**. Releases publish an
**SBOM** (CycloneDX/SPDX) and signed provenance. Verify artifacts using the published
attestations before use.

## Scope

In scope: the Orbeex codebase and official build/publish pipeline. Out of scope:
third-party LLM providers, user-supplied API keys, and user data. Never commit secrets —
`.env`, keys, and tokens are git-ignored by policy.

## Keeping secrets out of the public repo

This repository is **public**. Committing a secret would expose it to everyone, and it
stays in git history even after deletion. We defend in several layers:

1. **`.gitignore`** blocks `.env` files, keys, tokens, certificates, and cloud credential
   files. Only the safe `.env.example` template is tracked.
2. **Pre-commit hook (gitleaks)** scans staged changes locally. Install it once:
   ```bash
   pip install pre-commit
   pre-commit install
   ```
3. **CI secret scanning** (`.github/workflows/secret-scan.yml`) runs gitleaks over the full
   history on every push, PR, and daily.
4. **GitHub push protection** (enable in repo settings → Code security) blocks pushes that
   contain detected secrets.
5. **Runtime keys are never written to the repo.** Orbeex stores LLM API keys in the OS
   keychain, not in project files.

### If a secret is ever committed

1. **Rotate/revoke it immediately** — assume it is compromised the moment it is pushed.
2. Remove it from history with `git filter-repo` (see GitHub's guide), then force-push.
3. Tell collaborators to re-clone or clean their clones.

Never rely on deletion alone; rotation is the real fix.

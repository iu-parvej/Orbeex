# Decision Log (Chronological)

Chronological record of decisions and their rationale, for fast AI/human context loading.
Authoritative detail lives in each ADR under `../decisions/`.

## 2026-10-17 — Foundation Session

| # | Decision | Rationale (short) | Record |
|---|---|---|---|
| 1 | **Operation Graph is the universal contract** | Everything reduces to an `Operation`; gives undo/audit/repro/scripting/safety for free | ADR-0003 |
| 2 | **Apache-2.0 (all applicable software) + CC-BY-4.0 (docs) + DCO** | Permissive + patent grant = enterprise trust; uniform licensing | ADR-0001, ADR-0007 |
| 3 | **Documentation platform = Mintlify** | Best-in-class UI, docs-as-code, generous free tier, MCP for AI | ADR-0004 |
| 4 | **Mintlify: free Starter now; OSS Program later** | Free Starter covers current needs; better OSS-Program odds once established | ADR-0005 |
| 5 | **Scalar evaluated, not adopted** | Mintlify wins on docs-site; Scalar retained as optional API-reference add-on (MIT, self-host) | ADR-0006 |
| 6 | **Fumadocs evaluated, not adopted** | Would require becoming a permanent Next.js team; Mintlify is zero-ops | ADR-0008 |
| 7 | **Docs live in the main Orbeex repo (`docs-site/`)** | Docs must ship with features in the same PR; no separate repo | ADR-0009 |
| 8 | **Master Blueprint + `plan/`, `brain/`, `licensing/` structure created** | Enterprise-grade scaffold for the project | MASTER_BLUEPRINT.md |
| 9 | **Automated changelog + traceability + docs/roadmap sync** | Keep a Changelog + towncrier fragments + feature registry + CI gates = auditable, zero-drift | ADR-0010 |

## 2026-10-17 — Enterprise Readiness Audit

| # | Item | Outcome | Record |
|---|---|---|---|
| 10 | **Full-directory enterprise audit** | 14 gaps found (G-01…G-14); verdict: strong scaffold, no product code, ~15% ready; Gate coverage 1/7 | `enterprise-readiness-audit-2026-10-17.md` |
| — | **Blockers** | No Git repo (G-01); no buildable workspace (G-02) | audit §4 Tier 0 |

## 2026-10-17 — Enterprise Hardening Implementation

| # | Decision/Action | Outcome | Record |
|---|---|---|---|
| 11 | **Implement all audit gaps (Tier 0–2)** | Git repo, governance, Rust workspace, full CI/CD + security workflows, tests/typing, containers | ADR-0011 |
| — | **Verification** | pytest 15 passed; mypy clean; fmt clean; changelog OK (6 fragments, 2 features) | session-log Session 4 |
| — | **Deferred** | Tier-3 (SOC 2/ISO, SLSA L3, pen test); pin Actions to SHAs | audit §8 |

## 2026-10-17 — Security & Writing Style

| # | Decision/Action | Outcome | Record |
|---|---|---|---|
| 12 | **Secret prevention for the public repo** | 5 layers: gitignore, gitleaks pre-commit, CI scan, push protection, keychain-only keys | ADR-0012 |
| — | **History rewritten** | Personal email removed from all commits; now `Orbeex Contributors <orbeex@users.noreply.github.com>`; refs/stash/reflog purged | security-guide.md |
| 13 | **Plain-English writing style** | All human-facing docs in clear, warm, non-AI tone | ADR-0013 |
| — | **Folder re-analysis** | No new structural gaps; verified no secrets/emails in tracked files | session-log Session 5 |

## 2026-10-17 — Documentation Register & Policies

| # | Decision/Action | Outcome | Record |
|---|---|---|---|
| 14 | **Professional, compact writing style** | Supersedes ADR-0013's warm tone; concise, factual, no filler/emoji | ADR-0014 |
| 15 | **Full privacy & data policy set** | PRIVACY, DATA-USAGE, ACCEPTABLE-USE, TRADEMARK + existing SECURITY/GOVERNANCE | ADR-0015 |
| — | **Core commitments** | Local by default; no collection; schema-not-data to LLMs; opt-in and reversible | PRIVACY.md, DATA-USAGE.md |

## How to add a decision

1. Write `ADR-NNNN-<slug>.md` in `../decisions/` (use an existing ADR as the template).
2. Mark any superseded ADR's status.
3. Add the row to `../decisions/README.md` and here.
4. If structural, reference it from `MASTER_BLUEPRINT.md`.

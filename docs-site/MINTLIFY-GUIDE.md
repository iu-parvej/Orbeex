# Mintlify Interaction Guide (for Orbeex)

**Purpose:** Authoritative, verified reference for how the Orbeex team and AI
collaborators create, edit, validate, and publish Mintlify documentation.
**Source:** Mintlify docs (verified 2026-10-17). See `ADR-0004`, `ADR-0005`.

---

## 0. Model: Docs-as-Code

Mintlify is **docs-as-code**. Every page is an `.mdx` file in the Orbeex repository;
site configuration lives in `docs-site/docs.json`. Editing = editing files + pushing to Git.

**Doc root for the Mintlify site:** `docs-site/` (contains `docs.json` and `*.mdx`).

---

## 1. Methods to Create & Edit Docs (ranked)

### Method 1 — Git (PRIMARY; free; always available) ✅
```bash
git clone <orbeex-repo>
# create or edit any .mdx under docs-site/
mint dev                    # local preview -> http://localhost:3000
git add . ; git commit -m "docs: <change>" ; git push   # push triggers deploy
```
- This is the **only method needing no paid plan**.
- Fits Blueprint §7.3: docs ship with the feature, reviewed via PR.
- **Orbeex uses this as the standard workflow.**

### Method 2 — Mintlify CLI (free; authoring + quality gates)
Install: `npm i -g mint` (Node.js ≥ 20.17.0 LTS).

| Command | Use |
|---|---|
| `mint dev` | Local preview (`--port`, `--no-open`) |
| `mint validate` | Strict build validation (incl. OpenAPI). Use in CI. |
| `mint broken-links` | Link checker (`--files`, `--check-anchors`, `--check-external`, `--check-redirects`) |
| `mint a11y` | Accessibility: contrast + alt text |
| `mint format` | Rewrite MDX to canonical style (use a dedicated branch) |
| `mint new <dir> --name <n> --theme <t>` | Scaffold a project |
| `mint export` | Self-contained offline zip |
| `mint score [url]` | Agent-readiness score (llms.txt, MCP, etc.) |
| `mint login` / `mint status` | Auth / session info |

### Method 3 — MCP server (free) — AI collaborator read/verify
Each site auto-hosts a **search MCP server** at `<site>/mcp` (no setup):
- Tools: **Search**, **Query docs filesystem** (read pages as Markdown), **Submit feedback**.
- Claude Code: `claude mcp add --transport http mintlify https://<site>/mcp`
- Discovery: `/.well-known/mcp`.

> The **search MCP is read-only**. The separate **admin MCP server** is for trusted
> write/edit and is plan-gated.

### Method 4 — Web editor (free)
`https://app.mintlify.com/editor` → edit → **Publish**. Good for quick non-Git edits.

### Method 5 — REST API (Pro / OSS-Pro) — automation only
- Admin API keys (`mint_...`), server-side only; scope `read`/`write`; IP allowlists.
- Endpoints: **Trigger update**, update status, preview deployment, agent jobs,
  assistant search/page-content, analytics exports.
- **Requires Pro** — obtain via the OSS Program (`ADR-0005`). Not needed today.

---

## 2. Orbeex Standard Workflow

1. **Author** — create/edit `.mdx` in `docs-site/` (Git).
2. **Preview** — `mint dev`.
3. **Gate** — `mint validate` + `mint broken-links` (+ `mint a11y`).
4. **Reformat** (optional) — `mint format` on a dedicated branch.
5. **Review** — open a PR (Blueprint §5).
6. **Publish** — merge/push to the production branch; Mintlify deploys.
7. **Verify** — `mint score <site-url>` and confirm the `.mintlify.site` URL loads.

## 3. CI Integration (planned)

Add a CI job that runs, on any change under `docs-site/`:
```bash
npm i -g mint
mint validate
mint broken-links
mint a11y
```
A failure blocks the PR (Blueprint §6.4 pattern).

## 4. Content Conventions

- File names: `kebab-case.mdx` (Blueprint §7.3).
- Frontmatter: `title`, `description`; add `noindex: true` to hide from search.
- Diagrams: Mermaid (text-first).
- Navigation: declared in `docs.json`.
- `.mintignore` excludes files from processing/indexing.

## 5. Security Notes

- **Never commit secrets.** Admin/assistant API keys and MCP client secrets go in CI
  secrets / env vars only (Blueprint §6.1, ADR-0001).
- Admin API keys are server-side secrets; never in client code.
- The search MCP key/credential is gated by plan; treat as a password.

## 6. Cost & Plan Boundary

| Capability | Plan |
|---|---|
| Git sync, web editor, CLI, MCP server, custom domain | **Free Starter** |
| REST API (updates), admin MCP, previews, analytics | **Pro / OSS-Pro** |

Per `ADR-0005`: use **free Starter now**; apply to the **OSS Program** later for Pro API access.

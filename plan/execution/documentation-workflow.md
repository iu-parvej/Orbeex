# Documentation Publishing Workflow (execution)

> Binding workflow. Decision: `brain/decisions/ADR-0016`. Blueprint §7.5 mirrors it.
> Local source folder: `documentation/` · Live site: https://orbeex.mintlify.app
> Project: `portfolioofparvej/orbeex` · Deploy branch: `main`

## Routine cycle (every time public docs change)

1. **Gather content** from `brain/` (context, decisions, knowledge, state) and `plan/`
   (roadmap, metrics). Facts only from these sources — no invented claims.
2. **Edit the page** in `documentation/<page>.mdx`. Audience rule: broad, global,
   non-technical readers. Keep sentences short; explain any GIS/AI term in one line.
3. **Push to Mintlify** via MCP tools on `branch: main`:
   - existing page → `Mintlify_write_page` (full file, frontmatter included);
   - new page → `Mintlify_create_node` with data `{ type: "page", path, title,
     description, content }` and `parentId` = the Documentation nav group;
   - reorder/rename → `Mintlify_move_node` / `Mintlify_update_node`.
4. **Publish:** `Mintlify_publish` (branch `main`, conventional title).
5. **Verify:** `Mintlify_deployment_status` until `live: true`. Site URL:
   https://orbeex.mintlify.app
6. **Record:** changelog fragment under `changes/unreleased/`, update
   `brain/state/current-state.md` + `session-log.md` as needed, commit locally
   (`git commit -s`), never `git push` for docs.

## Page inventory (live)

| Live path | Source file | Audience note |
|---|---|---|
| `/introduction` | `documentation/introduction.mdx` | High-level intro, any reader |
| `/how-it-works` | `documentation/how-it-works.mdx` | Ask → plan → approve → execute |
| `/quickstart` | `documentation/quickstart.mdx` | First-session flow, status-honest |
| `/working-with-ai` | `documentation/working-with-ai.mdx` | AI features and data bounds |
| `/your-data-and-privacy` | `documentation/your-data-and-privacy.mdx` | Privacy in plain language |
| `/concepts/*`, `/ai/*`, `/reference/glossary` | legacy `docs-site/` pages | Developer-oriented ("Advanced topics") |

## Review checklist (per page)

- [ ] Claims match `brain/` + `plan/` (no overstatement; "planned" when not shipped)
- [ ] No secrets, personal data, or sensitive real-world coordinates
- [ ] Terminology explained on first use; favicon-level jargon removed
- [ ] Tone: professional, compact, accessible (writing-style-guide.md)
- [ ] Links resolve within the site or point to the public GitHub repo

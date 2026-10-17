# Orbeex Documentation (source for Mintlify)

This folder is the source of truth for the public Orbeex documentation.

## Workflow

1. Pages here are written for a **broad, global audience** — not developers. Clear words, short sentences, no jargon without explanation.
2. Content is drawn from `brain/` (decisions, context, state) and `plan/` (roadmap).
3. Pages are pushed **directly to Mintlify** using the Mintlify MCP tools (`write_page`, `create_node`, then `publish`). This bypasses local git/GitHub pushes entirely: edits land in the Mintlify project and publish from there.
4. Keep this folder in sync with what is pushed, so the local copy always reflects the live site.

## Pages

| File | Live path | Audience note |
|---|---|---|
| `introduction.mdx` | `/introduction` | High-level introduction for anyone |
| `how-it-works.mdx` | `/how-it-works` | The ask → plan → approve → execute cycle, in plain words |
| `quickstart.mdx` | `/quickstart` | Getting started, honest about early status |
| `working-with-ai.mdx` | `/working-with-ai` | AI features, providers, what is and isn't sent |
| `your-data-and-privacy.mdx` | `/your-data-and-privacy` | Data handling in plain language |

Developer-oriented pages (Operation Graph, Core Brain, glossary) remain published under
"Advanced topics" for technical readers.

## Rules

- Follow `brain/knowledge/writing-style-guide.md` — professional, compact, plain.
- Never include secrets, real coordinates of sensitive sites, or personal data.
- Status claims must be accurate (say "planned" when something is not released).
- Update this folder first, then push to Mintlify — do not edit only one side.

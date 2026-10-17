# Orbeex Docs Site (Mintlify)

Public documentation for Orbeex, built and hosted on **[Mintlify](https://www.mintlify.com/)**.

Decision records:
- `../brain/decisions/ADR-0004-documentation-platform-mintlify.md`
- `../brain/decisions/ADR-0005-mintlify-oss-program-sequencing.md`

## Plan: free Starter now, OSS Program later

- **Now:** run on the **free Mintlify Starter plan** ($0/mo, free forever) — hosting, custom
  domain, web editor, Git sync, MCP server, API playground, search, 5 editor seats.
  Publish by pushing MDX to Git.
- **Later:** once the project is publicly established (Apache-2.0 `LICENSE` in place, public
  repo, community presence), **apply to the Mintlify OSS Program** for free Pro, unlocking
  the **Developer API** and automated/API-driven editing.
  Apply here: https://www.mintlify.com/oss-program#eligibility

## How it works

- Content is plain **Markdown/MDX in this Git repository**. Site config is `docs.json`.
- Mintlify hosts the site and syncs with this repo via **Git sync** (included on all plans).
- The **web editor** and CLI are used for authoring; the **Developer API** (Pro / free OSS
  Pro) enables automated/API-driven editing.

## Local development

```bash
npm i -g mint        # install the Mintlify CLI (Node >= 20.17)
mint dev             # preview at http://localhost:3000
mint validate        # strict build validation
mint broken-links    # check links
```

See **[MINTLIFY-GUIDE.md](MINTLIFY-GUIDE.md)** for the full, verified guide to every way to
create/edit/publish Mintlify docs (Git, CLI, MCP server, web editor, REST API).

## Applying for free Pro (OSS Program)

Orbeex qualifies as a non-commercial open-source project. **When the project is publicly
established**, apply to Mintlify's OSS Program to unlock **free Pro** (Developer API, Admin
APIs, webhooks, analytics, AI features): https://www.mintlify.com/oss-program#eligibility

Until then, use the free Starter plan (Git-based authoring).

## Portability

Because docs are plain MDX in Git, the site can be rebuilt elsewhere (Docusaurus, MkDocs
Material) with **no content loss** if needed. See Blueprint §7.

## Relationship to other docs

- `../docs/` — source-of-truth technical/architecture/guide docs (mirrored into pages here).
- `../brain/decisions/` — ADRs (the "why").
- `rustdoc` API reference is published separately.

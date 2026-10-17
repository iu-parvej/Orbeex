# ORBEEX — MASTER BLUEPRINT

> **This document is the primary instruction set for all AI collaborators and human
> contributors working on Orbeex. Read it fully before writing a single line of code,
> opening a file, or creating a directory. When in doubt, this document wins.**

| Field | Value |
|---|---|
| **Project** | Orbeex |
| **Type** | Open-source, community-driven, AI-native GIS workstation |
| **Primary Language** | Rust (100% core) |
| **License** | Apache-2.0 (code) · CC-BY-4.0 (docs) · see `licensing/` |
| **Blueprint Version** | 1.0.0 |
| **Status** | Active — Foundation Phase |
| **Owner** | Orbeex Core Team |
| **Last Updated** | 2026-10-17 |

---

## TABLE OF CONTENTS

1. [Mission & Core Objectives](#1-mission--core-objectives)
2. [Functional Requirements](#2-functional-requirements)
3. [Directory Usage Protocols](#3-directory-usage-protocols)
4. [Licensing & Compliance Policies](#4-licensing--compliance-policies)
5. [Versioning & Release Management](#5-versioning--release-management)
6. [Error Handling, Testing & QA Standards](#6-error-handling-testing--qa-standards)
7. [Documentation Management & Maintenance](#7-documentation-management--maintenance)
8. [AI Collaborator Operating Rules](#8-ai-collaborator-operating-rules)

---

## 1. MISSION & CORE OBJECTIVES

### 1.1 Mission

Orbeex is an open-source, AI-native Geographic Information System built in Rust. It
turns natural language into **reviewable, reversible, auditable geospatial operations**
executed by a high-performance native engine — on desktop and in the browser (WASM) —
with zero vendor lock-in on the LLM tier.

### 1.2 The Single Most Important Architectural Rule

> **Everything is an Operation.**
>
> Every action — human or AI, desktop or web, core or plugin — reduces to an `Operation`
> node in an append-only operation graph. This graph is the universal contract that gives
> Orbeex undo, audit, reproducibility, and scripting **for free**. Never bypass it.

The AI never touches data directly. It produces a **typed Operation Graph**; the engine
validates and executes it. This is the firewall between probabilistic and deterministic
systems.

### 1.3 Core Objectives (ranked)

| # | Objective | Success Criterion |
|---|---|---|
| O1 | **Deterministic, auditable execution** | 100% of actions traceable to an Operation node; full undo |
| O2 | **Extreme performance** | Viewport update < 100 ms on 10M-feature layers |
| O3 | **Memory safety / zero-error UX** | No panics in UI paths; `unsafe` forbidden by default |
| O4 | **AI-native orchestration** | NL → validated Operation Graph; ≥98% valid-plan rate |
| O5 | **Data sovereignty** | Raw data never leaves machine unless explicitly opted in |
| O6 | **Cross-platform parity** | Windows, macOS, Linux native; web as subset |
| O7 | **Extensibility without risk** | Sandboxed WASM plugins with stable ABI |

### 1.4 Non-Goals (V1)

- Replacing every QGIS/ArcGIS feature at launch (narrow scope, deep quality).
- Cloud-hosted data storage (local-first; cloud is opt-in, later).
- Training or hosting our own LLM (BYO API key / local model only).

### 1.5 Target Users (priority order)

1. Geospatial engineering teams in regulated industries (utilities, rail, telecom, defense).
2. Consultancies needing fast, supervised analysis.
3. Government / public sector with data-sovereignty mandates.
4. Academic & research (adoption funnel).

---

## 2. FUNCTIONAL REQUIREMENTS

### 2.1 The Core Brain

The "Core Brain" is the combination of the GIS execution engine and the AI orchestration
layer. Both live under `software/` and are governed by the single Operations contract.

**GIS Engine Requirements**

- FR-E01: Load/query/render vector datasets (GeoPackage, FlatGeobuf, GeoJSON, Shapefile-read).
- FR-E02: Load/render raster datasets (GeoTIFF, Cloud-Optimized GeoTIFF).
- FR-E03: CRS handling and reprojection with property-tested numerics.
- FR-E04: Core vector ops: buffer, clip, intersect, spatial join, dissolve, extract.
- FR-E05: Spatial indexing (R-tree in-memory; persistent on-disk index).
- FR-E06: Dependency-aware recomputation (change one node → recompute only downstream).
- FR-E07: Append-only journaling of every committed Operation.

**AI Orchestration Requirements**

- FR-A01: Provider adapters for OpenAI, Anthropic (Claude), Google (Gemini), DeepSeek, Qwen.
- FR-A02: Local/sovereign provider (e.g. Ollama-compatible) as first-class fallback.
- FR-A03: A `Model Router` selecting provider by task complexity, cost, capability, latency, policy.
- FR-A04: Intent parsing: NL → structured intent (goal, entities, constraints).
- FR-A05: Planning: intent → draft Operation Graph via tool/function-calling.
- FR-A06: Tool registry **generated from engine types** (never hand-written schemas).
- FR-A07: Validation & safety gate: type-check + policy-check + cost estimate before execution.
- FR-A08: Risk-tiered confirmation (safe = auto; additive = one-click; destructive = mandatory review + dry-run + backup).
- FR-A09: LLM redaction/audit middleware: schema-only context by default; raw coordinates never sent unless opted in.
- FR-A10: Cost governor with per-session budget and hard stop.

### 2.2 Platform Requirements

- FR-P01: Native binaries for Windows, macOS, Linux — no runtime dependency (no JVM/Python).
- FR-P02: Web build via WebAssembly (WebGPU with WebGL2 fallback) as a degraded subset.
- FR-P03: GPU-accelerated map rendering (wgpu).
- FR-P04: Signed installers + signed auto-update feed.
- FR-P05: Accessibility to WCAG 2.2 AA.

### 2.3 Plugin Requirements

- FR-X01: WASM sandboxed plugin host (capability-based permissions).
- FR-X02: Stable, SemVer-governed plugin ABI.
- FR-X03: Plugins may expose new tools that the AI agent can plan and execute.

### 2.4 Requirement ID Convention

`FR-<AREA>-<NN>` where AREA ∈ {E=engine, A=AI, P=platform, X=plugin}. All requirements are
tracked as feature specs under `features/`.

---

## 3. DIRECTORY USAGE PROTOCOLS

### 3.1 Top-Level Map

```
D:\Orbeex\
├── MASTER_BLUEPRINT.md     # ← THIS FILE. Primary instruction set. Read first.
├── plan\                   # Roadmap & strategic execution (WHAT & WHEN)
├── brain\                  # Core logic, context, decisions (WHY & HOW-THINK)
├── licensing\              # Legal documentation & license policy (LEGAL)
├── docs\                   # Architecture, guides, user-facing documentation
├── research\               # Market & technology research (EVIDENCE)
├── features\               # Feature specs & development tracking (WORK)
├── software\               # All source code — the actual product (CODE)
├── tests\                  # Test strategy, QA, reports (QUALITY)
├── releases\               # Changelogs & release artifacts (SHIP)
├── ai\                     # Agents, prompts, knowledge, training context
├── assets\                 # Icons, fonts, sample data, shaders
├── resources\              # Static reference material, datasets, third-party refs
├── scripts\                # Automation: setup, build, benchmark, maintenance
├── build\                  # Build outputs, intermediates (GIT-IGNORED)
└── _legacy\                # Preserved prior work (READ-ONLY; never edit)
```

### 3.2 `plan\` — Roadmap & Strategic Execution

| Path | Purpose |
|---|---|
| `plan\vision\` | Long-term product vision, strategy narratives, positioning |
| `plan\roadmap\phases\` | Phase-by-phase implementation plan (P0…P7) |
| `plan\roadmap\milestones\` | Milestone definitions + exit criteria |
| `plan\execution\` | Sprints, work breakdown, delivery schedules |
| `plan\releases\` | Release planning (what ships in which version) |
| `plan\metrics\` | KPIs, performance budgets, tracked targets |

**Protocol:** All planning documents are forward-looking. Historical plans are never
deleted — they are marked `STATUS: SUPERSEDED` and linked to their successor.

### 3.3 `brain\` — Core Logic, Context & Decisions

| Path | Purpose |
|---|---|
| `brain\vision\` | Canonical vision statements (source of truth for "why") |
| `brain\decisions\` | Architecture Decision Records (ADRs) — immutable, numbered |
| `brain\context\` | Essential project context for onboarding AI + humans |
| `brain\knowledge\` | Domain knowledge: GIS, CRS, formats, LLM behavior |
| `brain\prompts\` | Canonical prompt templates used by the AI layer |
| `brain\agents\` | Agent role definitions and orchestration specs |
| `brain\state\` | Current project state snapshots (what's built, what's next) |

**Protocol:** `brain\decisions\` is the highest-authority technical record. An ADR is
**never edited after acceptance** — to change a decision, write a new ADR that supersedes
it. ADR naming: `ADR-NNNN-<slug>.md`.

### 3.4 `licensing\` — Legal Documentation & Policy

| Path | Purpose |
|---|---|
| `licensing\licenses\` | Full text of licenses applied to Orbeex itself |
| `licensing\policies\` | Contribution policy, CLA/DCO, IP policy, relicense policy |
| `licensing\third-party\` | Inventory + licenses of all third-party dependencies |
| `licensing\compliance\` | Compliance records, audit trails, SBOM storage |
| `licensing\templates\` | Header templates, NOTICE templates, attribution templates |

**Protocol:** No dependency may be added to the project until its license is recorded in
`licensing\third-party\` and cleared against the policy in §4. CI enforces this.

### 3.5 Supporting Directories

- `software\` — all source. `software\apps\` (top-level apps) and `software\modules\`
  (core crate workspace). Each module is independently versioned and testable.
- `docs\` — `architecture\`, `adr\` (mirror/pointer to `brain\decisions\`), `guides\`, `user\`.
- `research\` — `market\`, `technology\`, `notes\`. Research informs decisions; it is
  evidence, not authority.
- `features\` — lifecycle: `backlog\` → `in-progress\` → `completed\`. One folder per
  feature, ID `F-NNNN`. Machine-readable state: `features\registry\features.yaml`.
- `changes\` — `unreleased\` (fragments), `releases\` (compiled), `migrations\`, `templates\`.
- `tests\` — `strategy\`, `qa\`, `reports\`.
- `releases\` — `changelogs\`, `artifacts\`.
- `_legacy\` — **read-only archive.** Never modify, never import from it without an ADR.

### 3.6 Directory Protocol Rules (MANDATORY)

1. **Never write to a directory that is not described here** without first updating this
   Blueprint (and, if structural, an ADR).
2. **Never place code outside `software\`** (and `tests\`, `scripts\`, `resources\`).
3. **Never place planning content outside `plan\`.** Never place decisions outside `brain\decisions\`.
4. **Never edit `_legacy\`.** Copy out via an ADR if reuse is justified.
5. **`build\` is git-ignored** and disposable; never store source or docs there.
6. Every file added must belong to exactly one of the above categories. If it fits two,
   the directory structure needs an ADR.

---

## 4. LICENSING & COMPLIANCE POLICIES

### 4.1 Recommendation Summary

**Orbeex code: Apache License 2.0.**
**Orbeex documentation: CC-BY-4.0.**
Rationale: Apache-2.0 is permissive (maximum adoption, enterprise-friendly, compatible
with commercial use) **and** includes an explicit patent grant — critical for a project
whose value proposition is enterprise trust. Pure MIT lacks the patent grant; strong
copyleft (GPL/AGPL) would block the enterprise/commercial adoption Orbeex needs.

### 4.2 License Decision Matrix

| License | Adoption Ease | Copyleft Protection | Patent Grant | Verdict for Orbeex |
|---|---|---|---|---|
| **Apache-2.0** | High | None | **Yes** | **CHOSEN** — enterprise default |
| MIT | Highest | None | No | Good fallback for small helpers |
| BSD-3-Clause | High | None | No | Acceptable dependency license |
| MPL-2.0 | High | File-level | Yes | Acceptable (isolated files) |
| LGPL-3.0 | Medium | Library-level | Yes | Caution — dynamic linking only |
| GPL-3.0 | Low | Strong | Yes | **Forbidden** in core |
| AGPL-3.0 | Lowest | Network | Yes | **Forbidden** (breaks SaaS/web model) |

### 4.3 Dependency License Policy

- **Allowed (permissive):** Apache-2.0, MIT, BSD-2/3-Clause, ISC, Zlib, Unlicense, CC0,
  MPL-2.0 (isolated).
- **Restricted (requires ADR + legal note):** LGPL (dynamic link only), EPL.
- **Forbidden:** GPL, AGPL, SSPL, any non-OSI or "source-available" license.
- Every dependency must be recorded in `licensing\third-party\inventory.md` with: name,
  version, license, linking type, and justification.
- `cargo-deny` config (`deny.toml`) enforces this list in CI. A failing `cargo-deny` is a
  **blocking** CI failure.

### 4.4 Contribution Policy

- **DCO (Developer Certificate of Origin)** required on every commit (`Signed-off-by`).
- A **CLA may be introduced** only if dual-licensing or relicensing flexibility is needed
  — requires an ADR and community consultation.
- Contributors retain copyright; contributions are licensed under Apache-2.0.
- All contributions must pass CI: lint, test, license check, and (for `software/ai`)
  AI golden-plan tests.

### 4.5 Compliance Artifacts

- **SBOM** (SPDX or CycloneDX) generated on every release, stored in
  `licensing\compliance\sbom\`.
- **NOTICE file** generated from third-party inventory, shipped with every binary.
- **SLSA Level 3** build provenance targeted from Phase 6.
- **Vulnerability policy:** documented in `SECURITY.md`; CVE response SLA defined there.

### 4.6 File Headers

Every source file in `software\` must carry the SPDX header:

```
// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 The Orbeex Contributors
```

Header templates live in `licensing\templates\`.

---

## 5. VERSIONING & RELEASE MANAGEMENT

### 5.1 Versioning Scheme

- **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`) for all published artifacts.
- Every crate/module in `software\modules\` is independently versioned; the product
  release version is the version of `software\apps\`.
- **Plugin ABI** carries its own explicit version (`orbeex-plugin-api-vX`), decoupled from
  the product version, with a documented compatibility window (≥ 2 minor releases).
- **Operation schema** is versioned; must be **backward-compatible within a major version**,
  with migration paths for any breaking change.

### 5.2 Branching Model

- **Trunk-based development.** `main` is always releasable.
- Short-lived branches: `feat/F-NNNN-slug`, `fix/slug`, `docs/slug`, `chore/slug`.
- Release branches cut from `main` only for stabilization: `release/x.y`.
- No long-lived development branches.

### 5.3 Commit Convention

**Conventional Commits** are mandatory:

```
<type>(<scope>): <subject>

[body]

Signed-off-by: Name <email>
```

Types: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`,
`revert`. Scope = affected module/area. Commits must be signed.

### 5.4 Changelog Workflow

- One **change fragment** per PR in `changes\unreleased\` (towncrier-style):
  `changes\unreleased\<ref>.<type>.md`, where `<ref>` is `F-NNNN` | `PR-<n>` | `+<orphan>`
  and `<type>` ∈ {added, changed, deprecated, removed, fixed, security, docs, internal}.
- Fragments are compiled into `releases\changelogs\<version>.md` at release time and the
  fragment files are archived alongside the release.
- `releases\` holds only generated/final changelogs; `plan\releases\` holds the *plan*.

**Automation (MANDATORY):** the changelog, feature registry, docs, and roadmap are kept in
sync by tooling and enforced in CI:

| Command | Purpose |
|---|---|
| `python scripts/changelog/orbeex.py validate-all` | Validate fragments + feature registry |
| `python scripts/changelog/orbeex.py compile --version X.Y.Z` | Build a release changelog |
| `python scripts/changelog/orbeex.py sync-docs --strict` | Verify docs/roadmap alignment |
| `python scripts/changelog/orbeex.py new-fragment --ref … --type …` | Scaffold a fragment |
| `python scripts/changelog/require_fragment.py` | CI gate: require a fragment for behavior changes |

The **feature registry** (`features/registry/features.yaml`) is the machine-readable source
of truth for feature state and traceability. Every shipped feature records its requirement
IDs, spec path, docs paths, and `introduced` version. CI reconciles the registry, fragments,
changelog, and docs. Full workflow: `changes/README.md`, `features/README.md`.

### 5.5 Release Process (checklist)

1. Freeze: cut `release/x.y` from `main`.
2. Verify all gates green: tests, lint, `cargo-deny`, AI golden-plan tests, benchmarks.
3. Bump versions; compile changelog; generate SBOM + NOTICE.
4. Build signed artifacts for all platforms; generate SLSA provenance.
5. Tag `vX.Y.Z` and sign the tag.
6. Publish release notes (from changelog) + artifacts + SBOM.
7. Record the release in `releases\` and update `plan\metrics\`.

### 5.6 Deprecation Policy

- Deprecations announced at least **one minor version** before removal.
- Deprecations carry machine-readable markers and a documented migration path in
  `changes\migrations\`.

---

## 6. ERROR HANDLING, TESTING & QA STANDARDS

### 6.1 Error Handling Standards (`software\`)

- **No panics in UI paths.** All fallible operations return `Result`.
- **`unsafe` is forbidden** workspace-wide via `#![forbid(unsafe_code)]`, except in a
  small, explicitly audited set of FFI crates (documented in an ADR). Enforced in CI.
- **Typed errors** via `thiserror`. Every error has:
  - a stable **code** (`ORX-<AREA>-<NNNN>`, AREA ∈ {VEC, RAS, CRS, IO, ENG, AI, UI, PLG}),
  - a human-readable message,
  - a cause chain,
  - a remediation hint.
- **Boundary catching:** panics are caught at the shell boundary and converted to
  user-visible, actionable errors. Raw panics are never shown.
- **Crash recovery:** the operation graph is continuously journaled; on crash, the session
  restores to the last committed node.
- **Error taxonomy** is documented in `docs\architecture\error-taxonomy.md`.

### 6.2 Testing Pyramid (enforced in CI)

| Layer | Scope | Gate |
|---|---|---|
| Unit | Per module, fast | Required on every PR |
| Integration | Cross-module workflows | Required on every PR |
| Property (`proptest`) | Geometry & CRS numerics | Nightly + on critical modules |
| Fuzz (`cargo-fuzz`) | All format drivers | Nightly |
| AI golden-plan | NL → expected Operation Graph (recorded LLM responses) | Required on every PR touching `software\ai` |
| Performance | Benchmarks vs baselines | Fail PR if > 5% regression |
| E2E | Desktop + web UI automation | Required before merge to `main` |
| Compatibility | Platform × format matrix | Required on release branches |

### 6.3 AI Behavior Testing

- `tests\qa\ai\planning-cases\` — NL inputs → expected Operation Graph (golden files).
- `tests\qa\ai\safety-cases\` — inputs that **must** be refused or must require confirmation.
- `tests\qa\ai\regression-cases\` — every past AI failure locked in as a test.
- LLM calls in tests are **mocked/recorded** for determinism; live-provider tests run
  separately in a non-blocking nightly job.

### 6.4 Quality Gates (all must pass to merge)

1. `cargo fmt --check`
2. `cargo clippy -- -D warnings`
3. `cargo test` (unit + integration)
4. `cargo deny check` (licenses + advisories + bans)
5. Forbidden-`unsafe` check
6. Benchmark regression ≤ 5%
7. AI golden-plan suite (when AI layer touched)

### 6.5 QA Artifacts

- Test strategy: `tests\strategy\`.
- QA plans & manuals: `tests\qa\`.
- Test reports (incl. coverage, performance baselines): `tests\reports\`.
- Every shipped feature must have a **test plan** (`features\...\test-plan.md`) with
  acceptance criteria traced to its `FR-*` IDs.

### 6.6 Performance Budgets

Tracked in `plan\metrics\performance-budgets.md`:

- Viewport Time-to-Display < 100 ms @ 10M features.
- Operation-graph execution overhead < 5%.
- AI valid-plan rate ≥ 98% at GA.
- Destructive-op incident rate = 0 (target).
- Crash-free session rate ≥ 99.9%.
- LLM cost within user budget 100% of the time.

---

## 7. DOCUMENTATION MANAGEMENT & MAINTENANCE

### 7.1 Documentation Stack

**Primary: Mintlify** (https://www.mintlify.com/) — AI-native docs platform. Content is
plain Markdown/MDX in Git with `docs.json` config; hosted by Mintlify with a custom domain
on the **free Starter plan**; Git sync and an MCP server included. Docs are edited/pushed
via Git PRs and the web editor, and via the **Developer API** once the free **OSS Program
(Pro)** is granted. Decision: `brain/decisions/ADR-0004`.

> **Plan note:** Developer API / Admin APIs / webhooks are **Pro-only**. Starter is free
> forever (hosting, custom domain, web editor, Git sync, MCP server, API playground, 5
> seats). **Plan of record:** run on the **free Starter plan now**; **after the project is
> publicly established**, apply to the Mintlify **OSS Program**
> (https://www.mintlify.com/oss-program#eligibility) for **free Pro** to enable
> API-driven editing. Decision: `brain/decisions/ADR-0005`.

**API reference from Rust:** `rustdoc` published to GitHub Pages.

**Portability fallback:** **Docusaurus** (prior ADR-0002) or **MkDocs Material** — because
docs are plain MDX in Git, the site can be rebuilt elsewhere with no content loss.

**Internal knowledge base (optional):** BookStack or Wiki.js (free, self-hosted) — for
internal, non-versioned knowledge. Public docs use Mintlify.

### 7.2 Documentation Types & Locations

| Type | Location | Audience |
|---|---|---|
| Public user docs | `docs-site/` (Mintlify MDX + `docs.json`), authored from `docs/` | End users |
| Developer guides | `docs/guides/` | Contributors |
| Architecture docs | `docs/architecture/` | Engineers |
| Decisions (ADR) | `brain/decisions/` | All contributors |
| API reference | generated from `rustdoc` | Developers |
| Internal knowledge base | BookStack / Wiki.js (self-hosted, optional) | Core team |
| Research | `research/` | Strategists |

### 7.3 Documentation Maintenance Rules

1. **Docs-as-code:** docs live in the repo, reviewed via PRs, versioned with the code.
2. **Docs ship with the feature.** A feature PR that changes behavior **must** update the
   relevant docs in the same PR, or it is not mergeable.
3. **ADRs are immutable** once accepted (supersede, never edit).
4. **Each doc has a clear owner** (front-matter `owner:` field) and a `last_reviewed:` date.
5. **Review cadence:** every doc reviewed at least once per minor release; stale docs
   (> 2 minor releases without review) are flagged in CI.
6. **Naming:** `kebab-case.md` for all docs; ADRs `ADR-NNNN-slug.md`.
7. **No orphan docs:** every doc must be linked from an index (`README` or docs sidebar).
8. **Broken-link check** runs in CI on every docs change.
9. **Diagrams** are text-first (Mermaid) so they live in version control and render in
   Docusaurus/MkDocs.
10. **Terminology** is governed by `docs\glossary.md` (GIS + AI + Orbeex terms).

### 7.4 Documentation as AI Context

Docs intended to feed AI collaborators (context, prompts, conventions) live under `brain\`
and `ai\`. These must be:
- concise and unambiguous (AI-optimized),
- kept in sync with the Blueprint,
- free of task-specific noise.

---

## 8. AI COLLABORATOR OPERATING RULES

> These rules govern any AI agent (including LLM-based coding assistants) operating in
> this repository.

1. **Read this Blueprint first.** Restate the applicable rule before acting if uncertain.
2. **Respect directory protocols (§3).** Do not create directories/files outside the
   defined structure without updating this Blueprint.
3. **Never bypass the Operations contract (§1.2).** All functionality reduces to an Operation.
4. **No `unsafe`, no panics in UI paths, typed errors with stable codes (§6.1).**
5. **Every feature follows the lifecycle:** spec → ADR (if structural) → implementation →
   tests → docs → changelog fragment.
6. **Any dependency addition requires a license record (§4.3).**
7. **Any structural or architectural change requires an ADR before implementation.**
8. **Never modify `_legacy\`.** Never commit secrets. Never edit accepted ADRs.
9. **When a request conflicts with this Blueprint, stop and flag the conflict** rather than
   silently violating a rule.
10. **Prefer correctness and auditability over speed.** In GIS, one wrong transform is a
    costly incident.
11. **Persist every decision and learning in `brain\` (MANDATORY).** At the end of every
    working session, record: new ADRs, reusable knowledge, updated current state, and a
    session-log entry. See `brain\README.md`. Future AI must be able to read and reuse it.

### 8.1 Definition of Done (per change)

A change is Done only when **all** are true:

- [ ] Requirement (FR-*) satisfied and traceable.
- [ ] Code complies with §6.1 (no unsafe, typed errors, no UI panics).
- [ ] Unit + integration tests pass; AI tests if AI layer touched.
- [ ] Quality gates (§6.4) all green.
- [ ] Docs updated in the same PR (§7.3 rule 2).
- [ ] License/compliance impact recorded if dependencies changed.
- [ ] Changelog fragment added to `changes\unreleased\`.
- [ ] Feature spec moved appropriately under `features\`.

---

## APPENDIX A — Canonical IDs & Conventions

| Artifact | Convention | Example |
|---|---|---|
| Requirement | `FR-<AREA>-<NN>` | `FR-A05` |
| Feature | `F-NNNN` | `F-0042` |
| ADR | `ADR-NNNN-slug` | `ADR-0003-arrow-as-interchange` |
| Error code | `ORX-<AREA>-<NNNN>` | `ORX-CRS-0012` |
| Plugin | `PLG-<slug>` | `PLG-ogr-import` |
| Phase | `P0…P7` | `P3` |
| Milestone | `M-<slug>` | `M-engine-mvp` |

## APPENDIX B — Phase Roadmap (summary)

| Phase | Weeks | Goal | Exit Criterion |
|---|---|---|---|
| P0 | 0–6 | Foundation & validation | Perf targets validated; ≥90% valid-plan rate |
| P1 | 6–20 | Core engine MVP | Reproducible 10-step analysis; fuzz-clean |
| P2 | 20–34 | Desktop application | Analyst completes standard workflow unaided |
| P3 | 28–44 | AI-native layer | 20 NL scenarios with correct plans + safe refusals |
| P4 | 40–52 | Web / WASM | Interactive workflows at target latency |
| P5 | 48–60 | Plugin ecosystem | Third-party plugin tool usable by AI agent |
| P6 | 56–72 | Enterprise hardening | Mock security review + 100M-feature benchmark |
| P7 | 72–84 | GA & scale | 1.0 across desktop + web; marketplace live |

## APPENDIX C — Glossary

See `docs\glossary.md` for the full GIS + AI + Orbeex glossary. Key terms:

- **Operation** — atomic, serializable unit of work in the operation graph.
- **Operation Graph** — append-only DAG of Operations; source of undo/audit/reproducibility.
- **Tool** — a typed, schema-described engine capability exposed to the LLM.
- **Core Brain** — the GIS engine + AI orchestration layer combined.
- **Safety Gate** — validation layer between AI proposal and execution.

---

*End of Master Blueprint. This document is versioned and itself governed by the change
process in §5. Amendments require a PR and, for structural changes, an ADR.*

# F-0001 — Vector Dataset Loading (GeoPackage)

| Field | Value |
|---|---|
| **Feature ID** | F-0001 |
| **Name** | Vector dataset loading (GeoPackage) |
| **Owner** | @orbeex-core |
| **Priority** | P0 |
| **Milestone** | P1 (Core engine MVP) |
| **Status** | in-progress |
| **Requirements** | FR-E01 |
| **Dependencies** | ADR-0003 (Operation Graph) |

## Problem

Users must be able to open GeoPackage (`.gpkg`) vector datasets as the first step of any
GIS workflow. This is the entry point for the engine's vector pipeline.

## User Story

> As a geospatial analyst, I want to load a GeoPackage file so that I can view and analyze
> its layers.

## Acceptance Criteria

- [ ] Load a GeoPackage from disk and enumerate its layers.
- [ ] Read layer schema: field names, types, geometry type, CRS, extent.
- [ ] Emit a `LoadDataset` Operation into the operation graph (undo-able).
- [ ] No panics on malformed files; typed error with a stable code (`ORX-IO-xxxx`).

## Design

Implemented in `orbeex-io` + `orbeex-vector`. The load is expressed as an `Operation`; the
engine validates and executes it. Details pending the P1 design pass.

## AI Interaction

Exposes a `load_dataset(path, format)` Tool to the AI agent. **Risk tier: additive**
(one-click confirm).

## Test Plan

See `test-plan.md` (to be written). Unit + integration + a fuzz target on the driver.

## Docs Impact

- `docs-site/reference/glossary.mdx`
- `docs/architecture/` (I/O layer)

# Orbeex Glossary

Terminology for GIS + AI + Orbeex. Governed by Blueprint §7.3 rule 10.

## Orbeex Core

| Term | Definition |
|---|---|
| **Operation** | Atomic, serializable unit of work in the operation graph. |
| **Operation Graph** | Append-only DAG of Operations; source of undo, audit, reproducibility. |
| **Core Brain** | The GIS execution engine + AI orchestration layer combined. |
| **Tool** | A typed, schema-described engine capability exposed to the LLM. |
| **Safety Gate** | Validation layer between an AI proposal and execution (type + policy + cost). |
| **Model Router** | Component selecting an LLM provider per task by complexity/cost/capability/latency/policy. |
| **Risk Tier** | Classification of an Operation: safe / additive / destructive. |
| **Dry-run** | Simulated execution of a proposed Operation Graph with no data mutation. |

## GIS

| Term | Definition |
|---|---|
| **GIS** | Geographic Information System. |
| **CRS** | Coordinate Reference System. |
| **Reprojection** | Transforming coordinates from one CRS to another. |
| **Vector** | Geometry-based spatial data (points, lines, polygons). |
| **Raster** | Grid/cell-based spatial data (imagery, DEMs). |
| **COG** | Cloud-Optimized GeoTIFF. |
| **Spatial Index** | Data structure (e.g. R-tree) accelerating spatial queries. |
| **Spatial Join** | Joining attributes by spatial relationship, not key equality. |
| **Buffer** | Geometry representing all points within a distance of an input. |
| **Extent** | Bounding box of a dataset or view. |

## AI

| Term | Definition |
|---|---|
| **LLM** | Large Language Model. |
| **Agentic** | An AI that plans, decides, and executes multi-step tasks. |
| **Intent Parsing** | Converting natural language into structured intent. |
| **Planning** | Converting intent into a draft Operation Graph. |
| **Function/Tool Calling** | LLM capability to emit structured tool invocations. |
| **ReAct Loop** | Reason → Act → Observe iterative agent loop. |
| **Sovereignty** | Keeping data local; sending only intent/schema to LLMs. |
| **Redaction** | Removing sensitive data before any external LLM call. |

## Standards

| Term | Definition |
|---|---|
| **OGC** | Open Geospatial Consortium. |
| **EPSG** | Registry of CRS codes. |
| **SLSA** | Supply-chain Levels for Software Artifacts. |
| **SBOM** | Software Bill of Materials. |
| **DCO** | Developer Certificate of Origin. |
| **ADR** | Architecture Decision Record. |

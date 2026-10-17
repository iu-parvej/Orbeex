# Third-Party Dependency Inventory

> Every dependency must be recorded here **before** it is added (Blueprint §4.3).
> CI (`cargo-deny`) verifies this list is consistent with the lockfile.

**Legend:** Link = `static` / `dynamic` / `build` · Status = `allowed` / `restricted` / `pending`

| Dependency | Version | License | Link | Status | Justification |
|---|---|---|---|---|---|
| _(serde)_ | _TBD_ | _MIT/Apache-2.0_ | _static_ | _allowed_ | _Serialization for Operation schema_ |
| _(thiserror)_ | _TBD_ | _MIT/Apache-2.0_ | _static_ | _allowed_ | _Typed errors_ |
| _(geo)_ | _TBD_ | _MIT/Apache-2.0_ | _static_ | _allowed_ | _Geometry primitives_ |
| _(wgpu)_ | _TBD_ | _MIT/Apache-2.0_ | _static_ | _allowed_ | _GPU rendering_ |
| _(tokio)_ | _TBD_ | _MIT_ | _static_ | _allowed_ | _Async runtime for AI layer_ |
| _(reqwest)_ | _TBD_ | _MIT/Apache-2.0_ | _static_ | _allowed_ | _HTTP client for LLM providers_ |

> Placeholder rows are illustrative. Replace with real entries as dependencies are locked in
> during Phase 0/1, with exact versions and verified licenses.

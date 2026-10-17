// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 The Orbeex Contributors

//! # orbeex-core
//!
//! Core domain types shared across the Orbeex workspace.
//!
//! The central abstraction is the [`Operation`]: **every action in Orbeex — human or AI,
//! desktop or web, core or plugin — reduces to an `Operation` node in an append-only
//! operation graph.** This single contract gives the project undo, audit, reproducibility,
//! scripting, and AI safety (see `MASTER_BLUEPRINT.md` and `ADR-0003`).
//!
//! This crate is intentionally dependency-light and platform-agnostic so it can compile to
//! `wasm32-unknown-unknown`.

#![forbid(unsafe_code)]

pub mod error;
pub mod ids;
pub mod operation;

pub use error::{ErrorCode, OrbeexError, Result};
pub use ids::{FeatureId, OperationId, SessionId};
pub use operation::{Operation, OperationKind, RiskTier};

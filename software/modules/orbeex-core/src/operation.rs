// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 The Orbeex Contributors

//! The [`Operation`] — the universal unit of work in Orbeex.
//!
//! See `ADR-0003`. Every action reduces to an `Operation`; the AI never mutates data
//! directly, it emits operations that the engine validates and executes.

use crate::ids::OperationId;
use serde::{Deserialize, Serialize};
use time::OffsetDateTime;

/// Risk classification used to decide how much confirmation an operation needs.
///
/// Mirrors the three-tier model in `MASTER_BLUEPRINT.md` §3.4.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum RiskTier {
    /// Read-only; auto-execute (e.g. zoom, query, summarize).
    Safe,
    /// Additive; one-click confirm (e.g. add a derived layer).
    Additive,
    /// Destructive; mandatory review, dry-run, and backup.
    Destructive,
}

/// The kind of work an [`Operation`] represents.
///
/// This is intentionally small for now; variants are added as capabilities land.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case", tag = "op")]
#[non_exhaustive]
pub enum OperationKind {
    /// Load a dataset from a path in the given format.
    LoadDataset {
        /// Source path (as provided; resolved by the engine).
        path: String,
        /// Format hint, e.g. `gpkg`, `geojson`.
        format: String,
    },
    /// Reproject a layer to a target CRS.
    Reproject {
        /// Target coordinate reference system, e.g. an EPSG code.
        target_crs: String,
    },
}

/// A single, immutable unit of work recorded in the append-only operation graph.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Operation {
    /// Stable identity of this operation.
    pub id: OperationId,
    /// The work to perform.
    pub kind: OperationKind,
    /// How risky this operation is (drives confirmation requirements).
    pub risk: RiskTier,
    /// When the operation was created.
    #[serde(with = "time::serde::rfc3339")]
    pub created_at: OffsetDateTime,
}

impl Operation {
    /// Create a new operation with a fresh id and the current timestamp.
    #[must_use]
    pub fn new(kind: OperationKind, risk: RiskTier) -> Self {
        Self {
            id: OperationId::new(),
            kind,
            risk,
            created_at: OffsetDateTime::now_utc(),
        }
    }

    /// Whether this operation may be auto-executed without human confirmation.
    #[must_use]
    pub fn is_auto_executable(&self) -> bool {
        matches!(self.risk, RiskTier::Safe)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn safe_operations_auto_execute() {
        let op = Operation::new(
            OperationKind::LoadDataset {
                path: "roads.gpkg".to_owned(),
                format: "gpkg".to_owned(),
            },
            RiskTier::Safe,
        );
        assert!(op.is_auto_executable());
    }

    #[test]
    fn destructive_operations_are_not_auto() {
        let op = Operation::new(
            OperationKind::Reproject {
                target_crs: "EPSG:3857".to_owned(),
            },
            RiskTier::Destructive,
        );
        assert!(!op.is_auto_executable());
    }

    #[test]
    fn operation_round_trips_through_json() {
        let op = Operation::new(
            OperationKind::Reproject {
                target_crs: "EPSG:4326".to_owned(),
            },
            RiskTier::Additive,
        );
        let json = serde_json::to_string(&op).expect("serialize");
        let back: Operation = serde_json::from_str(&json).expect("deserialize");
        assert_eq!(op, back);
    }
}

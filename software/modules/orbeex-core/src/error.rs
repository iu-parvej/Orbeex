// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 The Orbeex Contributors

//! Typed error taxonomy with stable `ORX-<AREA>-<NNNN>` codes.
//!
//! Every error carries a stable [`ErrorCode`], a human-readable message, an optional
//! cause chain, and a remediation hint, per `MASTER_BLUEPRINT.md` §6.1.

use std::fmt;
use thiserror::Error;

/// Result alias used throughout Orbeex.
pub type Result<T> = std::result::Result<T, OrbeexError>;

/// Error areas, mapping to the code prefix (e.g. `VEC` -> `ORX-VEC-…`).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum ErrorArea {
    /// Vector engine.
    Vec,
    /// Raster engine.
    Ras,
    /// Coordinate reference systems.
    Crs,
    /// Input/output and format drivers.
    Io,
    /// Execution engine.
    Eng,
    /// AI orchestration.
    Ai,
    /// User interface.
    Ui,
    /// Plugin host.
    Plg,
}

impl ErrorArea {
    /// The three-letter code prefix for this area.
    #[must_use]
    pub const fn prefix(self) -> &'static str {
        match self {
            Self::Vec => "VEC",
            Self::Ras => "RAS",
            Self::Crs => "CRS",
            Self::Io => "IO",
            Self::Eng => "ENG",
            Self::Ai => "AI",
            Self::Ui => "UI",
            Self::Plg => "PLG",
        }
    }
}

/// A stable, documented error code of the form `ORX-<AREA>-<NNNN>`.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct ErrorCode {
    area: ErrorArea,
    number: u16,
}

impl ErrorCode {
    /// Construct a new error code.
    #[must_use]
    pub const fn new(area: ErrorArea, number: u16) -> Self {
        Self { area, number }
    }

    /// The area of this code.
    #[must_use]
    pub const fn area(self) -> ErrorArea {
        self.area
    }

    /// The numeric part of this code.
    #[must_use]
    pub const fn number(self) -> u16 {
        self.number
    }
}

impl fmt::Display for ErrorCode {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "ORX-{}-{:04}", self.area.prefix(), self.number)
    }
}

/// The canonical Orbeex error type.
///
/// New variants should be added deliberately and each must map to a stable [`ErrorCode`].
#[derive(Debug, Error)]
#[non_exhaustive]
pub enum OrbeexError {
    /// An I/O error occurred while reading or writing a dataset.
    #[error("[{code}] I/O error: {message}")]
    Io {
        /// Stable error code.
        code: ErrorCode,
        /// Human-readable message.
        message: String,
        /// The underlying cause, if any.
        #[source]
        source: Option<Box<dyn std::error::Error + Send + Sync>>,
    },

    /// An operation failed validation (type or policy).
    #[error("[{code}] invalid operation: {message}")]
    InvalidOperation {
        /// Stable error code.
        code: ErrorCode,
        /// Human-readable message.
        message: String,
    },

    /// A feature or capability is not yet implemented.
    #[error("[{code}] not implemented: {message}")]
    NotImplemented {
        /// Stable error code.
        code: ErrorCode,
        /// Human-readable message.
        message: String,
    },
}

impl OrbeexError {
    /// The stable code associated with this error.
    #[must_use]
    pub const fn code(&self) -> ErrorCode {
        match self {
            Self::Io { code, .. }
            | Self::InvalidOperation { code, .. }
            | Self::NotImplemented { code, .. } => *code,
        }
    }

    /// A suggested remediation for the user, if known.
    #[must_use]
    pub fn remediation(&self) -> &'static str {
        match self {
            Self::Io { .. } => "Check the file path, permissions, and format, then retry.",
            Self::InvalidOperation { .. } => {
                "Review the proposed operation and correct its inputs."
            }
            Self::NotImplemented { .. } => "This capability is planned; see the project roadmap.",
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn code_display_is_orx_prefixed() {
        let code = ErrorCode::new(ErrorArea::Crs, 12);
        assert_eq!(code.to_string(), "ORX-CRS-0012");
    }

    #[test]
    fn error_exposes_code_and_remediation() {
        let err = OrbeexError::NotImplemented {
            code: ErrorCode::new(ErrorArea::Ai, 1),
            message: "planner not wired".to_owned(),
        };
        assert_eq!(err.code().to_string(), "ORX-AI-0001");
        assert!(!err.remediation().is_empty());
    }
}

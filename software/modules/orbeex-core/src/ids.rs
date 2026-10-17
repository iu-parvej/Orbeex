// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 The Orbeex Contributors

//! Stable identifiers for Orbeex domain objects.

use serde::{Deserialize, Serialize};
use std::fmt;
use uuid::Uuid;

/// A unique operation identifier (UUID v4).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(transparent)]
pub struct OperationId(Uuid);

impl OperationId {
    /// Create a new, random operation identifier.
    #[must_use]
    pub fn new() -> Self {
        Self(Uuid::new_v4())
    }
}

impl Default for OperationId {
    fn default() -> Self {
        Self::new()
    }
}

impl fmt::Display for OperationId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

/// A unique session identifier (UUID v4).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(transparent)]
pub struct SessionId(Uuid);

impl SessionId {
    /// Create a new, random session identifier.
    #[must_use]
    pub fn new() -> Self {
        Self(Uuid::new_v4())
    }
}

impl Default for SessionId {
    fn default() -> Self {
        Self::new()
    }
}

impl fmt::Display for SessionId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

/// A feature identifier following the `F-NNNN` convention.
///
/// Validated on construction so it can be relied upon for traceability.
#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(try_from = "String", into = "String")]
pub struct FeatureId(String);

impl FeatureId {
    /// Parse and validate a feature identifier of the form `F-` followed by 4 digits.
    ///
    /// # Errors
    /// Returns the offending input if it does not match `F-NNNN`.
    pub fn parse(input: &str) -> std::result::Result<Self, String> {
        let valid = input.len() == 6
            && input.starts_with("F-")
            && input[2..].bytes().all(|b| b.is_ascii_digit());
        if valid {
            Ok(Self(input.to_owned()))
        } else {
            Err(format!("invalid feature id '{input}': expected F-NNNN"))
        }
    }

    /// Borrow the identifier as a string slice.
    #[must_use]
    pub fn as_str(&self) -> &str {
        &self.0
    }
}

impl TryFrom<String> for FeatureId {
    type Error = String;
    fn try_from(value: String) -> std::result::Result<Self, Self::Error> {
        Self::parse(&value)
    }
}

impl From<FeatureId> for String {
    fn from(value: FeatureId) -> Self {
        value.0
    }
}

impl fmt::Display for FeatureId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.0)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn feature_id_accepts_valid() {
        let id = FeatureId::parse("F-0042").expect("valid id");
        assert_eq!(id.as_str(), "F-0042");
    }

    #[test]
    fn feature_id_rejects_invalid() {
        for bad in ["F-42", "f-0042", "F-0042x", "0042", ""] {
            assert!(FeatureId::parse(bad).is_err(), "should reject {bad:?}");
        }
    }

    #[test]
    fn operation_id_is_unique() {
        assert_ne!(OperationId::new(), OperationId::new());
    }
}

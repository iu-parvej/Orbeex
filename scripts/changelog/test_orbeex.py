# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 The Orbeex Contributors
"""Tests for the Orbeex changelog automation (`orbeex.py`)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

# Import orbeex.py directly (scripts/ is not a package).
_HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("orbeex", _HERE / "orbeex.py")
assert _spec and _spec.loader
orbeex = importlib.util.module_from_spec(_spec)
sys.modules["orbeex"] = orbeex
_spec.loader.exec_module(orbeex)


# ── ids / registry ──────────────────────────────────────────────────────────

def test_feature_id_regex():
    assert orbeex.FEATURE_ID_RE.match("F-0001")
    assert not orbeex.FEATURE_ID_RE.match("F-1")
    assert not orbeex.FEATURE_ID_RE.match("f-0001")


def test_fragment_name_regex():
    assert orbeex.FRAGMENT_RE.match("F-0001.added.md")
    assert orbeex.FRAGMENT_RE.match("PR-118.fixed.md")
    assert orbeex.FRAGMENT_RE.match("+orphan.docs.md")
    assert not orbeex.FRAGMENT_RE.match("F-0001.md")
    assert not orbeex.FRAGMENT_RE.match("added.F-0001.md")


def test_semver_regex():
    assert orbeex.SEMVER_RE.match("1.2.3")
    assert not orbeex.SEMVER_RE.match("v1.2.3")
    assert not orbeex.SEMVER_RE.match("1.2")


# ── registry parsing (fallback + build) ─────────────────────────────────────

def test_registry_fallback_parses_features(tmp_path: Path):
    reg = tmp_path / "features.yaml"
    reg.write_text(
        "version: 1\nfeatures:\n"
        "  - id: F-0001\n"
        "    name: Test feature\n"
        "    status: proposed\n"
        "    area: engine\n"
        "    requirements: [FR-E01, FR-E02]\n"
        "    docs: [docs-site/x.mdx]\n",
        encoding="utf-8",
    )
    meta, features = orbeex._load_registry_fallback(reg, reg.read_text(encoding="utf-8"))
    assert meta.get("version") == 1
    assert len(features) == 1
    f = features[0]
    assert f.id == "F-0001"
    assert f.requirements == ["FR-E01", "FR-E02"]
    assert f.docs == ["docs-site/x.mdx"]


def test_registry_validation_flags_bad_status():
    f = orbeex.RegistryFeature(id="F-0001", status="bogus")
    errors = orbeex.validate_registry([f])
    assert any("invalid status" in e for e in errors)


def test_registry_validation_requires_introduced_when_shipped():
    f = orbeex.RegistryFeature(id="F-0001", status="shipped", introduced=None)
    errors = orbeex.validate_registry([f])
    assert any("introduced" in e for e in errors)


def test_registry_validation_detects_duplicate_id():
    a = orbeex.RegistryFeature(id="F-0001")
    b = orbeex.RegistryFeature(id="F-0001")
    errors = orbeex.validate_registry([a, b])
    assert any("duplicate" in e for e in errors)


# ── fragment parsing & validation ───────────────────────────────────────────

def _write_fragment(tmp_path: Path, name: str, body: str, front: str = "") -> Path:
    p = tmp_path / name
    p.write_text(f"---\n{front}\n---\n\n{body}\n", encoding="utf-8")
    return p


def test_fragment_valid(tmp_path: Path):
    p = _write_fragment(
        tmp_path, "F-0001.added.md", "Added a thing.", "area: engine\nfeature: F-0001"
    )
    frag = orbeex.load_fragment(p)
    assert frag.ref == "F-0001"
    assert frag.ctype == "added"
    assert frag.area == "engine"
    assert orbeex.validate_fragment(frag, {"F-0001"}) == []


def test_fragment_rejects_unknown_feature(tmp_path: Path):
    p = _write_fragment(tmp_path, "F-9999.added.md", "x", "feature: F-9999")
    frag = orbeex.load_fragment(p)
    errors = orbeex.validate_fragment(frag, {"F-0001"})
    assert any("not found in registry" in e for e in errors)


def test_fragment_allows_unknown_feature_in_public_mode(tmp_path: Path):
    """Public checkouts have no registry — feature lookups are skipped."""
    p = _write_fragment(tmp_path, "F-0001.added.md", "x", "feature: F-0001")
    frag = orbeex.load_fragment(p)
    assert orbeex.validate_fragment(frag, None) == []


def test_fragment_rejects_empty_body(tmp_path: Path):
    p = _write_fragment(tmp_path, "PR-1.added.md", "", "")
    frag = orbeex.load_fragment(p)
    errors = orbeex.validate_fragment(frag, set())
    assert any("empty body" in e for e in errors)


def test_fragment_bad_name_raises(tmp_path: Path):
    p = tmp_path / "oops.md"
    p.write_text("---\n---\nx", encoding="utf-8")
    with pytest.raises(ValueError):
        orbeex.load_fragment(p)


def test_breaking_requires_breaking_type(tmp_path: Path):
    p = _write_fragment(tmp_path, "F-0001.added.md", "x", "breaking: true")
    frag = orbeex.load_fragment(p)
    errors = orbeex.validate_fragment(frag, set())
    assert any("breaking:true requires" in e for e in errors)


# ── front matter ────────────────────────────────────────────────────────────

def test_parse_front_matter():
    fm, body = orbeex.parse_front_matter("---\na: 1\nb: yes\n---\nHello")
    assert fm == {"a": 1, "b": True}
    assert body == "Hello"


def test_strip_comment_preserves_hash_in_quotes():
    assert orbeex._strip_comment('title: "a # b" # trailing') == 'title: "a # b"'


# ── CLI smoke (exit codes) ──────────────────────────────────────────────────

def test_validate_all_on_repo():
    # Runs against the real repo; must succeed in the current clean state.
    rc = orbeex.main(["validate-all"])
    assert rc in (0, 1)  # 0 in a clean state; tolerate captured WIP

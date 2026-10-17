#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 The Orbeex Contributors
"""
Generate NOTICE / third-party attribution from the dependency inventory.

Reads `licensing/third-party/inventory.md` (Markdown table) and writes a NOTICE
block listing dependencies and their licenses. Run in the release pipeline.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY = REPO_ROOT / "licensing" / "third-party" / "inventory.md"
NOTICE = REPO_ROOT / "NOTICE"
ROW_RE = re.compile(r"^\|\s*(?P<name>[^|]+?)\s*\|\s*(?P<version>[^|]+?)\s*\|\s*(?P<license>[^|]+?)\s*\|")


def parse_inventory(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if set(line.replace("|", "").strip()) <= {"-", ":", " "}:
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group("name").strip()
        if name.lower() in ("dependency", "name") or name.startswith("_("):
            continue
        rows.append((name, m.group("version").strip(), m.group("license").strip()))
    return rows


def main() -> int:
    if not INVENTORY.exists():
        print(f"error: inventory not found: {INVENTORY}", file=sys.stderr)
        return 1
    deps = parse_inventory(INVENTORY.read_text(encoding="utf-8"))
    lines = [
        "",
        "-------------------------------------------------------------------------------",
        "THIRD-PARTY DEPENDENCIES",
        "-------------------------------------------------------------------------------",
        "",
    ]
    if not deps:
        lines.append("(none recorded yet)")
    else:
        for name, version, license_ in sorted(deps):
            lines.append(f"- {name} {version} — {license_}")
    block = "\n".join(lines) + "\n"

    base = NOTICE.read_text(encoding="utf-8") if NOTICE.exists() else ""
    marker = "-------------------------------------------------------------------------------\nTHIRD-PARTY DEPENDENCIES"
    if marker in base:
        base = base.split(marker)[0].rstrip() + "\n"
    NOTICE.write_text(base.rstrip() + "\n" + block, encoding="utf-8")
    print(f"NOTICE updated with {len(deps)} dependencies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
CI gate: require a change fragment when a PR changes behavior.

Rule (Blueprint §5.4 / §7.3): a PR that touches product code or docs must include at
least one new file under `changes/unreleased/` matching `<ref>.<type>.md`.

Reads BASE_SHA and HEAD_SHA env vars (set by the workflow). Pure stdlib.
Exit 0 = satisfied (or not required); 1 = required but missing.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

FRAGMENT_RE = re.compile(r"^changes/unreleased/(F-\d{4}|PR-\d+|\+\S+)\.[a-z]+\.md$")

# Paths whose changes REQUIRE a fragment.
REQUIRE_PREFIXES = ("software/", "crates/", "src/", "docs/", "docs-site/")
# Paths that are exempt (meta/infra-only changes).
EXEMPT_PREFIXES = (
    "changes/", ".github/", "scripts/", "brain/", "plan/", "research/",
    "tests/", "licensing/",
)


def changed_files(base: str, head: str) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        capture_output=True, text=True, check=True,
    )
    return [l.strip() for l in out.stdout.splitlines() if l.strip()]


def main() -> int:
    base = os.environ.get("BASE_SHA")
    head = os.environ.get("HEAD_SHA")
    if not base or not head:
        print("require_fragment: BASE_SHA/HEAD_SHA not set; skipping.")
        return 0

    files = changed_files(base, head)
    if not files:
        print("require_fragment: no changed files; skipping.")
        return 0

    touches_required = any(f.startswith(REQUIRE_PREFIXES) for f in files)
    only_exempt = all(f.startswith(EXEMPT_PREFIXES) for f in files)
    has_fragment = any(FRAGMENT_RE.match(f) for f in files)

    if only_exempt or not touches_required:
        print("require_fragment: no fragment required for this change set.")
        return 0

    if has_fragment:
        print("require_fragment: change fragment present. OK.")
        return 0

    print("FAIL: this PR changes product/docs code but adds no change fragment.")
    print("Add one, e.g.:  python scripts/changelog/orbeex.py "
          "new-fragment --ref PR-<num> --type added --area engine")
    return 1


if __name__ == "__main__":
    sys.exit(main())

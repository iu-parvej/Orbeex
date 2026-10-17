#!/usr/bin/env python3
"""
Orbeex project automation — changelog, feature registry, docs & roadmap sync.

Single entry point with subcommands (see `--help`). Pure stdlib (no third-party deps)
so it runs anywhere without setup. Used by CI (.github/workflows) and locally.

Subcommands:
  validate-fragment <path>   Validate a single change fragment.
  validate-all               Validate all fragments + the feature registry (CI gate).
  compile --version X.Y.Z    Compile unreleased fragments into a release + CHANGELOG.
  sync-docs                  Report/verify docs + roadmap alignment with the registry.
  new-fragment               Scaffold a fragment for a change.

Exit codes: 0 = ok, 1 = validation failure, 2 = usage error.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
CHANGES_DIR = REPO_ROOT / "changes"
UNRELEASED_DIR = CHANGES_DIR / "unreleased"
RELEASES_DIR = CHANGES_DIR / "releases"
MIGRATIONS_DIR = CHANGES_DIR / "migrations"
REGISTRY_FILE = REPO_ROOT / "features" / "registry" / "features.yaml"
CHANGELOG_FILE = REPO_ROOT / "CHANGELOG.md"

# Keep a Changelog canonical types (+ docs/internal which are hidden from users).
VALID_TYPES = {
    "added", "changed", "deprecated", "removed",
    "fixed", "security", "docs", "internal",
}
# Types shown in the compiled changelog, in section order.
PUBLIC_SECTIONS = ["added", "changed", "deprecated", "removed", "fixed", "security"]
SECTION_TITLES = {
    "added": "Added", "changed": "Changed", "deprecated": "Deprecated",
    "removed": "Removed", "fixed": "Fixed", "security": "Security",
}
VALID_AREAS = {"engine", "ai", "platform", "plugin", "docs", "infra"}
VALID_STATUSES = {"proposed", "in-progress", "shipped", "deprecated", "removed"}
VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}

FRAGMENT_RE = re.compile(
    r"^(?P<ref>F-\d{4}|PR-\d+|\+\S+)\.(?P<type>[a-z]+)\.md$"
)
FEATURE_ID_RE = re.compile(r"^F-\d{4}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")

ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_RESET = "\033[0m"


# ---------------------------------------------------------------------------
# Minimal YAML reader (subset sufficient for the registry file)
# ---------------------------------------------------------------------------
# We intentionally avoid a PyYAML dependency. This parses the constrained registry
# schema: a top-level mapping with a `features:` list of flat mappings and inline
# lists like [FR-E01, FR-E02]. It is NOT a general YAML parser.

def _strip_comment(line: str) -> str:
    out, in_str = [], False
    for ch in line:
        if ch == '"':
            in_str = not in_str
        if ch == "#" and not in_str:
            break
        out.append(ch)
    return "".join(out).rstrip()


def _parse_scalar(text: str) -> object:
    text = text.strip()
    if text in ("null", "~", ""):
        return None
    low = text.lower()
    if low in ("true", "yes", "on"):
        return True
    if low in ("false", "no", "off"):
        return False
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(p) for p in inner.split(",")]
    if (text.startswith('"') and text.endswith('"')) or \
       (text.startswith("'") and text.endswith("'")):
        return text[1:-1]
    # Integers (avoid treating "1.2.3" or "F-0001" as numbers).
    if re.fullmatch(r"-?\d+", text):
        try:
            return int(text)
        except ValueError:
            return text
    return text


@dataclass
class RegistryFeature:
    id: str
    name: str = ""
    status: str = ""
    area: str = ""
    priority: str = ""
    milestone: str = ""
    owner: str = ""
    requirements: list = field(default_factory=list)
    spec: str = ""
    docs: list = field(default_factory=list)
    introduced: str | None = None
    changes: list = field(default_factory=list)


def load_registry(path: Path) -> tuple[dict, list[RegistryFeature]]:
    """Parse the registry file into (meta, features).

    Uses PyYAML when available (robust); otherwise falls back to a constrained
    stdlib parser sufficient for the registry schema. Raises ValueError on error.
    """
    if not path.exists():
        raise ValueError(f"registry not found: {path}")
    text = path.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore[import-untyped]

        data = yaml.safe_load(text) or {}
        if not isinstance(data, dict):
            raise ValueError(f"{path}: top level must be a mapping")
        meta = {k: v for k, v in data.items() if k != "features"}
        features = [_build_feature(dict(f), 0) for f in (data.get("features") or [])]
        return meta, features
    except ImportError:
        return _load_registry_fallback(path, text)


def _load_registry_fallback(path: Path, text: str) -> tuple[dict, list[RegistryFeature]]:
    """Constrained stdlib parser for the registry schema (no PyYAML available)."""
    lines = text.splitlines()

    meta: dict = {}
    features: list[RegistryFeature] = []
    in_features = False
    cur: dict | None = None

    for lineno, raw in enumerate(lines, 1):
        line = _strip_comment(raw)
        if not line.strip():
            continue
        stripped = line.strip()

        if not line.startswith((" ", "\t")):
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            if key == "features":
                in_features = True
                cur = None
                continue
            meta[key] = _parse_scalar(val)
            continue

        if in_features:
            if stripped.startswith("- "):
                if cur is not None:
                    features.append(_build_feature(cur, lineno))
                cur = {}
                body = stripped[2:].strip()
                if body:
                    k, _, v = body.partition(":")
                    cur[k.strip()] = _parse_scalar(v)
            else:
                if cur is None:
                    raise ValueError(f"{path}:{lineno}: item before any '- id:'")
                k, _, v = stripped.partition(":")
                cur[k.strip()] = _parse_scalar(v)

    if cur is not None:
        features.append(_build_feature(cur, len(lines)))
    return meta, features


def _build_feature(d: dict, lineno: int) -> RegistryFeature:
    if "id" not in d:
        raise ValueError(f"registry entry near line {lineno} is missing 'id'")
    return RegistryFeature(
        id=str(d.get("id", "")),
        name=str(d.get("name", "") or ""),
        status=str(d.get("status", "") or ""),
        area=str(d.get("area", "") or ""),
        priority=str(d.get("priority", "") or ""),
        milestone=str(d.get("milestone", "") or ""),
        owner=str(d.get("owner", "") or ""),
        requirements=list(d.get("requirements") or []),
        spec=str(d.get("spec", "") or ""),
        docs=list(d.get("docs") or []),
        introduced=d.get("introduced"),
        changes=list(d.get("changes") or []),
    )


# ---------------------------------------------------------------------------
# Fragment parsing
# ---------------------------------------------------------------------------

@dataclass
class Fragment:
    path: Path
    ref: str
    ctype: str
    area: str = ""
    feature: str = ""
    breaking: bool = False
    body: str = ""
    issues: list[str] = field(default_factory=list)


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Parse a leading '---' YAML front-matter block. Returns (dict, body)."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    fm: dict = {}
    for line in fm_raw.splitlines():
        line = _strip_comment(line)
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = _parse_scalar(v)
    return fm, body.lstrip("\n")


def load_fragment(path: Path) -> Fragment:
    name = path.name
    m = FRAGMENT_RE.match(name)
    if not m:
        raise ValueError(
            f"{path}: bad fragment name; expected '<ref>.<type>.md' "
            f"where ref is F-NNNN | PR-<n> | +<orphan> and type is one of "
            f"{sorted(VALID_TYPES)}"
        )
    ref, ctype = m.group("ref"), m.group("type")
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    issues = []
    if "issues" in fm and isinstance(fm["issues"], list):
        issues = [str(x) for x in fm["issues"]]
    return Fragment(
        path=path,
        ref=ref,
        ctype=ctype,
        area=str(fm.get("area", "") or ""),
        feature=str(fm.get("feature", "") or ""),
        breaking=bool(fm.get("breaking", False)),
        body=body.strip(),
        issues=issues,
    )


def validate_fragment(frag: Fragment, registry_ids: set[str]) -> list[str]:
    errors: list[str] = []
    if frag.ctype not in VALID_TYPES:
        errors.append(f"{frag.path}: invalid type '{frag.ctype}' (allowed: {sorted(VALID_TYPES)})")
    if not frag.body.strip():
        errors.append(f"{frag.path}: empty body — a fragment must describe the change")
    if frag.area and frag.area not in VALID_AREAS:
        errors.append(f"{frag.path}: invalid area '{frag.area}' (allowed: {sorted(VALID_AREAS)})")
    if frag.feature:
        if not FEATURE_ID_RE.match(frag.feature):
            errors.append(f"{frag.path}: feature '{frag.feature}' must match F-NNNN")
        elif frag.feature not in registry_ids:
            errors.append(f"{frag.path}: feature '{frag.feature}' not found in registry")
    if frag.breaking and frag.ctype not in ("changed", "removed", "deprecated"):
        errors.append(f"{frag.path}: breaking:true requires type changed|removed|deprecated")
    return errors


def validate_registry(features: list[RegistryFeature]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for f in features:
        if not FEATURE_ID_RE.match(f.id):
            errors.append(f"registry: id '{f.id}' must match F-NNNN")
        if f.id in seen:
            errors.append(f"registry: duplicate id '{f.id}'")
        seen.add(f.id)
        if f.status and f.status not in VALID_STATUSES:
            errors.append(f"registry: {f.id} invalid status '{f.status}'")
        if f.area and f.area not in VALID_AREAS:
            errors.append(f"registry: {f.id} invalid area '{f.area}'")
        if f.priority and f.priority not in VALID_PRIORITIES:
            errors.append(f"registry: {f.id} invalid priority '{f.priority}'")
        if f.status == "shipped" and not f.introduced:
            errors.append(f"registry: {f.id} shipped but 'introduced' version is missing")
        if f.introduced and not SEMVER_RE.match(str(f.introduced)):
            errors.append(f"registry: {f.id} 'introduced' must be semver")
    return errors


# ---------------------------------------------------------------------------
# Compile
# ---------------------------------------------------------------------------

def compile_release(version: str, date: str | None, keep: bool) -> int:
    if not SEMVER_RE.match(version):
        print(f"{ANSI_RED}error:{ANSI_RESET} version must be semver (X.Y.Z)")
        return 2
    date = date or _dt.date.today().isoformat()
    fragments = [load_fragment(p) for p in sorted(UNRELEASED_DIR.glob("*.md"))]
    if not fragments:
        print(f"{ANSI_YELLOW}no fragments to compile.{ANSI_RESET}")
        return 0

    by_type: dict[str, list[Fragment]] = {t: [] for t in PUBLIC_SECTIONS}
    hidden: list[Fragment] = []
    for fr in fragments:
        (by_type.setdefault(fr.ctype, []) if fr.ctype in PUBLIC_SECTIONS else hidden).append(fr)

    rel_lines = [f"## [{version}] - {date}", ""]
    for section in PUBLIC_SECTIONS:
        items = by_type.get(section) or []
        if not items:
            continue
        rel_lines.append(f"### {SECTION_TITLES[section]}")
        rel_lines.append("")
        for fr in items:
            scope = f" ({fr.area})" if fr.area else ""
            ref = f" [{fr.ref}]" if fr.ref != "+" else ""
            marker = " **BREAKING**" if fr.breaking else ""
            rel_lines.append(f"- {fr.body}{scope}{ref}{marker}")
        rel_lines.append("")
    release_md = "\n".join(rel_lines).rstrip() + "\n"

    # Archive the release.
    rel_path = RELEASES_DIR / f"{version}.md"
    rel_path.write_text(release_md, encoding="utf-8")

    # Update CHANGELOG.md: insert under the unreleased marker.
    changelog = CHANGELOG_FILE.read_text(encoding="utf-8") if CHANGELOG_FILE.exists() else "# Changelog\n"
    marker = "<!-- towncrier release notes start -->"
    if marker in changelog:
        head, _, tail = changelog.partition(marker)
        # Replace the "# [Unreleased]" block up to the next version header.
        new_tail = f"{marker}\n\n{release_md}\n## [Unreleased]\n\n_Nothing yet._\n"
        # Drop an existing unreleased placeholder if present.
        tail_after = tail
        m = re.search(r"\n## \[Unreleased\][\s\S]*?(?=\n## \[|\Z)", tail_after)
        if m:
            tail_after = tail_after[:m.start()] + "\n"
        changelog = head + new_tail + tail_after.lstrip("\n")
    else:
        changelog += f"\n{marker}\n\n{release_md}\n"
    CHANGELOG_FILE.write_text(changelog, encoding="utf-8")

    if keep:
        print(f"{ANSI_GREEN}next steps{ANSI_RESET} (keep mode): move fragments to {releases_dir_rel()}/{version}.fragments/")
    else:
        archive = RELEASES_DIR / f"{version}.fragments"
        archive.mkdir(parents=True, exist_ok=True)
        for fr in fragments:
            fr.path.rename(archive / fr.path.name)
        print(f"{ANSI_GREEN}compiled{ANSI_RESET} {len(fragments)} fragments -> {rel_path.relative_to(REPO_ROOT)}")
    return 0


def releases_dir_rel() -> str:
    return str(RELEASES_DIR.relative_to(REPO_ROOT)).replace("\\", "/")


# ---------------------------------------------------------------------------
# Docs / roadmap sync
# ---------------------------------------------------------------------------

def sync_docs(strict: bool) -> int:
    _, features = load_registry(REGISTRY_FILE)
    problems: list[str] = []
    for f in features:
        if f.spec and not (REPO_ROOT / f.spec).exists():
            problems.append(f"{f.id}: spec path missing: {f.spec}")
        for d in f.docs:
            if not (REPO_ROOT / d).exists():
                problems.append(f"{f.id}: docs path missing: {d}")
        if f.status == "shipped":
            if not f.docs:
                problems.append(f"{f.id}: shipped but no docs recorded")
            if not any(RELEASES_DIR.glob(f"{f.introduced}*.md")) if f.introduced else True:
                pass  # release file presence is advisory here
    if problems:
        for p in problems:
            print(f"{ANSI_YELLOW}warn{ANSI_RESET} {p}")
        if strict:
            print(f"{ANSI_RED}sync-docs: {len(problems)} problem(s){ANSI_RESET}")
            return 1
    else:
        print(f"{ANSI_GREEN}sync-docs: registry/docs aligned{ANSI_RESET}")
    return 0


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_validate_fragment(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.exists():
        print(f"{ANSI_RED}error:{ANSI_RESET} not found: {path}")
        return 2
    try:
        _, features = load_registry(REGISTRY_FILE)
        ids = {f.id for f in features}
        frag = load_fragment(path)
        errors = validate_fragment(frag, ids)
    except ValueError as exc:
        print(f"{ANSI_RED}error:{ANSI_RESET} {exc}")
        return 1
    if errors:
        for msg in errors:
            print(f"{ANSI_RED}FAIL{ANSI_RESET} {msg}")
        return 1
    print(f"{ANSI_GREEN}OK{ANSI_RESET} {path.name}")
    return 0


def cmd_validate_all(args: argparse.Namespace) -> int:
    errors: list[str] = []
    try:
        _, features = load_registry(REGISTRY_FILE)
    except ValueError as exc:
        print(f"{ANSI_RED}error:{ANSI_RESET} {exc}")
        return 1
    errors += validate_registry(features)
    ids = {f.id for f in features}

    frags = sorted(UNRELEASED_DIR.glob("*.md"))
    for p in frags:
        try:
            errors += validate_fragment(load_fragment(p), ids)
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        for msg in errors:
            print(f"{ANSI_RED}FAIL{ANSI_RESET} {msg}")
        print(f"{ANSI_RED}{len(errors)} error(s).{ANSI_RESET}")
        return 1
    print(f"{ANSI_GREEN}OK{ANSI_RESET} {len(frags)} fragment(s), "
          f"{len(features)} feature(s) valid.")
    return 0


def cmd_compile(args: argparse.Namespace) -> int:
    try:
        return compile_release(args.version, args.date, args.keep)
    except ValueError as exc:
        print(f"{ANSI_RED}error:{ANSI_RESET} {exc}")
        return 1


def cmd_sync_docs(args: argparse.Namespace) -> int:
    try:
        return sync_docs(args.strict)
    except ValueError as exc:
        print(f"{ANSI_RED}error:{ANSI_RESET} {exc}")
        return 1


def cmd_new_fragment(args: argparse.Namespace) -> int:
    ctype = args.type
    if ctype not in VALID_TYPES:
        print(f"{ANSI_RED}error:{ANSI_RESET} invalid type '{ctype}'")
        return 2
    ref = args.ref
    fname = f"{ref}.{ctype}.md"
    dest = UNRELEASED_DIR / fname
    if dest.exists():
        print(f"{ANSI_RED}error:{ANSI_RESET} already exists: {dest}")
        return 1
    fm = [f"area: {args.area or ''}", f"feature: {args.feature or ''}", "breaking: false"]
    dest.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + (args.message or "Describe the change.") + "\n",
                    encoding="utf-8")
    # (front matter begins with a single '---' delimiter, written above)
    print(f"{ANSI_GREEN}created{ANSI_RESET} {dest.relative_to(REPO_ROOT)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="orbeex", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    v1 = sub.add_parser("validate-fragment", help="validate one fragment")
    v1.add_argument("path")
    v1.set_defaults(func=cmd_validate_fragment)

    v2 = sub.add_parser("validate-all", help="validate all fragments + registry (CI gate)")
    v2.set_defaults(func=cmd_validate_all)

    c = sub.add_parser("compile", help="compile unreleased fragments into a release")
    c.add_argument("--version", required=True)
    c.add_argument("--date", default=None)
    c.add_argument("--keep", action="store_true", help="do not move fragment files")
    c.set_defaults(func=cmd_compile)

    s = sub.add_parser("sync-docs", help="check docs/roadmap alignment with registry")
    s.add_argument("--strict", action="store_true", help="exit 1 on any problem")
    s.set_defaults(func=cmd_sync_docs)

    n = sub.add_parser("new-fragment", help="scaffold a fragment")
    n.add_argument("--ref", required=True, help="F-NNNN | PR-<n> | +orphan")
    n.add_argument("--type", required=True, help="added|changed|deprecated|removed|fixed|security|docs|internal")
    n.add_argument("--area", default="")
    n.add_argument("--feature", default="")
    n.add_argument("--message", default="")
    n.set_defaults(func=cmd_new_fragment)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

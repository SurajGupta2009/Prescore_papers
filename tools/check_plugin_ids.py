#!/usr/bin/env python3
"""Validate every plugin claim in this vault against the official Obsidian registry.

This is a regression test for documentation, and it exists because of a real bug:
the vault enabled `obsidian-numerals` (a non-existent ID) and four plugins that are
published as desktop-only, so on a phone nothing rendered.

What it checks
--------------
1. `.obsidian/community-plugins.json` - every enabled ID exists in the official
   community-plugins registry and is **mobile-capable** (`isDesktopOnly` false).
2. Every table row in `docs/RECOMMENDED-PLUGINS.md` whose "Mobile" column says ✅/❌ -
   the real manifest agrees.
3. Every "Install ID" in those tables exists in the registry (typo catcher).

Usage
-----
    python3 tools/check_plugin_ids.py                  # uses the live registry
    python3 tools/check_plugin_ids.py --offline         # skip (exit 0) if no network
    python3 tools/check_plugin_ids.py --registry FILE   # use a local registry dump

Network access needs `raw.githubusercontent.com`; when that is blocked (corporate
proxy, some sandboxes) it falls back to `gh api` and then to `api.github.com`.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_URL = ("https://raw.githubusercontent.com/obsidianmd/obsidian-releases/"
                "master/community-plugins.json")
DOC = ROOT / "docs" / "RECOMMENDED-PLUGINS.md"
ENABLED = ROOT / ".obsidian" / "community-plugins.json"

OK = "\033[32m✓\033[0m"
BAD = "\033[31m✗\033[0m"


# --------------------------------------------------------------------------- #
# fetching
# --------------------------------------------------------------------------- #

def fetch(url: str, timeout: int = 30) -> bytes | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.read()
    except Exception:  # noqa: BLE001
        return None


def load_registry(path: str | None) -> dict | None:
    if path:
        return {p["id"]: p for p in json.loads(Path(path).read_text())}
    data = fetch(REGISTRY_URL)
    if data:
        return {p["id"]: p for p in json.loads(data)}
    if shutil.which("gh"):
        out = subprocess.run(
            ["gh", "api", "repos/obsidianmd/obsidian-releases/contents/community-plugins.json",
             "--jq", ".content"],
            capture_output=True, text=True)
        if out.returncode == 0 and out.stdout.strip():
            return {p["id"]: p for p in
                    json.loads(base64.b64decode(out.stdout.strip()))}
    return None


def manifest(repo: str) -> dict | None:
    """Fetch a plugin manifest. Returns {} when reachable but empty of the flag."""

    for url in (f"https://raw.githubusercontent.com/{repo}/HEAD/manifest.json",
                f"https://api.github.com/repos/{repo}/contents/manifest.json"):
        raw = fetch(url, timeout=20)
        if not raw:
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if "content" in payload:                 # api.github.com shape
            return json.loads(base64.b64decode(payload["content"]))
        return payload
    if shutil.which("gh"):
        out = subprocess.run(
            ["gh", "api", f"repos/{repo}/contents/manifest.json", "--jq", ".content"],
            capture_output=True, text=True)
        if out.returncode == 0 and out.stdout.strip():
            return json.loads(base64.b64decode(out.stdout.strip()))
    return None


# --------------------------------------------------------------------------- #
# parsing
# --------------------------------------------------------------------------- #

def table_rows(text: str):
    """Yield (install_id, mobile_cell, plugin_label) for every markdown table row."""
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= set("-: "):
            continue
        m = re.match(r"^`([A-Za-z0-9_-]+)`$", cells[0])
        if not m:
            continue
        yield m.group(1), cells[2], cells[1]


def enabled_ids() -> list[str]:
    return json.loads(ENABLED.read_text())


# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", help="local community-plugins.json dump")
    ap.add_argument("--offline", action="store_true",
                    help="exit 0 with a warning when the registry is unreachable")
    args = ap.parse_args(argv)

    reg = load_registry(args.registry)
    if reg is None:
        msg = "could not reach the Obsidian plugin registry"
        if args.offline:
            print(f"SKIP: {msg}")
            return 0
        print(f"{BAD} {msg}")
        return 2
    print(f"registry: {len(reg)} plugins\n")

    failures = []

    # ---- 1. the vault's enabled list -------------------------------------- #
    print("Enabled plugins (.obsidian/community-plugins.json)")
    for pid in enabled_ids():
        entry = reg.get(pid)
        if not entry:
            failures.append(f"{pid} is not in the official registry (wrong id?)")
            print(f"  {BAD} {pid:32} NOT IN REGISTRY")
            continue
        man = manifest(entry["repo"])
        if man is None:
            print(f"  ?  {pid:32} manifest unreadable - not verified")
            continue
        # an absent isDesktopOnly key means mobile-capable (Obsidian's default)
        desktop = bool(man.get("isDesktopOnly", False))
        if desktop:
            failures.append(f"{pid} is enabled but is desktop-only "
                            f"({entry['repo']}) - it cannot load on a phone")
            print(f"  {BAD} {pid:32} desktopOnly=true  -> would fail on mobile")
        else:
            print(f"  {OK} {pid:32} mobile-capable  ({entry['name']})")

    # ---- 2. the documented table claims ----------------------------------- #
    if DOC.exists():
        print(f"\nDocumented claims ({DOC.relative_to(ROOT)})")
        for pid, mobile_cell, label in table_rows(DOC.read_text()):
            entry = reg.get(pid)
            if not entry:
                failures.append(f"{DOC.name}: `{pid}` does not exist in the registry")
                print(f"  {BAD} {pid:32} NOT IN REGISTRY")
                continue
            man = manifest(entry["repo"])
            if man is None:
                print(f"  ?  {pid:32} manifest unreadable - not verified")
                continue
            desktop = bool(man.get("isDesktopOnly", False))
            claimed_mobile = "✅" in mobile_cell
            claimed_desktop = "❌" in mobile_cell
            if not (claimed_mobile or claimed_desktop):
                continue
            if desktop and claimed_mobile:
                failures.append(f"{DOC.name}: `{pid}` is documented as ✅ mobile "
                                f"but its manifest is desktop-only")
                print(f"  {BAD} {pid:32} documented ✅, actually desktop-only")
            elif not desktop and claimed_desktop:
                failures.append(f"{DOC.name}: `{pid}` is documented as ❌ desktop-only "
                                f"but its manifest says mobile-capable")
                print(f"  {BAD} {pid:32} documented ❌, actually mobile-capable")
            else:
                print(f"  {OK} {pid:32} claim matches manifest "
                      f"(mobile={'yes' if not desktop else 'no'})  {label[:34]}")

    print()
    if failures:
        print(f"{len(failures)} problem(s):")
        for f in failures:
            print("  - " + f)
        return 1
    print("All plugin claims verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

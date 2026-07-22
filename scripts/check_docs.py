#!/usr/bin/env python3
"""Fast, dependency-free checks for this documentation repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
BLUEPRINT_NOTICE = "Status: Blueprint"
FORBIDDEN = ("chat" + "gpt", "open" + "ai")


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def local_target(source: Path, raw: str) -> Path | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    path_part = unquote(target.split("#", 1)[0])
    return (source.parent / path_part).resolve()


def check() -> list[str]:
    failures: list[str] = []
    files = markdown_files()

    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        lowered = text.lower()
        for term in FORBIDDEN:
            if term in lowered:
                failures.append(f"{relative}: prohibited attribution term")

        if path.parent == ROOT / "use-cases" and BLUEPRINT_NOTICE not in text[:600]:
            failures.append(f"{relative}: missing standard blueprint notice")

        for match in MARKDOWN_LINK.finditer(text):
            target = local_target(path, match.group(1))
            if target is not None and not target.exists():
                failures.append(f"{relative}: broken local link -> {match.group(1)}")

    required = [
        ROOT / "README.md",
        ROOT / "docs" / "QUICKSTART.md",
        ROOT / "docs" / "SECURITY.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
    ]
    for path in required:
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")

    return failures


if __name__ == "__main__":
    problems = check()
    if problems:
        print("Documentation checks failed:")
        for problem in problems:
            print(f"- {problem}")
        sys.exit(1)
    print("Documentation checks passed.")

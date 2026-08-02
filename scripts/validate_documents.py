#!/usr/bin/env python3
"""Validate ClassQuest Markdown document references and core numeric rules."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

EXPECTED_FILES = {
    "PROJECT.md",
    "CLAUDE.md",
    "README.md",
    "tasks/NEXT_TASK.md",
    "tasks/BACKLOG.md",
    "tasks/DONE.md",
    "changelog/README.md",
    "changelog/Sprint-00.md",
    "changelog/Sprint-01.md",
    "docs/00_PROJECT_WORKFLOW.md",
    "docs/01_REQUIREMENTS_DECISIONS.md",
    "docs/02_ARCHITECTURE.md",
    "docs/03_DATABASE.md",
    "docs/04_UI_GUIDE.md",
    "docs/05_ART_GUIDE.md",
    "docs/06_AUDIO_GUIDE.md",
    "docs/07_GAME_RULE.md",
    "docs/08_DEPLOYMENT.md",
    "docs/sprints/Sprint-01-Setup-Plan.md",
    "docs/archive/02_SPRINT_00_PLAN_REPLACED.md",
    "decisions/README.md",
    "decisions/ADR-001-SUPABASE.md",
    "decisions/ADR-002-TEAM-MODE.md",
    "decisions/ADR-003-VERSION-POLICY.md",
    "decisions/ADR-004-STUDENT-IDENTITY.md",
}

FORBIDDEN_STALE_REFERENCES = {
    "tasks/tasks/NEXT_TASK.md",
    "docs/02_SPRINT_00_PLAN.md",
    "docs/03_SPRINT_01_SETUP_PLAN.md",
    "docs/00_REQUIREMENTS_DECISIONS.md",
}

CORE_RULES = {
    "PROJECT.md": [
        "방 3개",
        "3~5",
        "최대 30명",
        "2~6팀",
        "2회 오답",
        "3개월 MVP",
    ],
    "README.md": [
        "방 3개",
        "3~5개",
        "최대 30명",
        "2~6팀",
        "2회",
        "3개월 MVP",
    ],
    "docs/07_GAME_RULE.md": [
        "방 3개",
        "3~5개",
        "2~6팀",
    ],
}

def main() -> int:
    errors: list[str] = []

    for rel in sorted(EXPECTED_FILES):
        if not (ROOT / rel).exists():
            errors.append(f"missing expected file: {rel}")

    markdown_files = sorted(ROOT.rglob("*.md"))

    for file in markdown_files:
        text = file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (file.parent / clean).resolve()
            if not resolved.exists():
                errors.append(
                    f"broken link: {file.relative_to(ROOT)} -> {target}"
                )

        for stale in FORBIDDEN_STALE_REFERENCES:
            if stale in text:
                errors.append(
                    f"stale path reference: {file.relative_to(ROOT)} contains {stale}"
                )

    for rel, required_terms in CORE_RULES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"core rule missing: {rel} does not contain {term!r}")

    if errors:
        print("Document validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Document validation passed: "
        f"{len(markdown_files)} Markdown files, "
        f"{len(EXPECTED_FILES)} expected files, "
        f"0 broken links, 0 stale path references."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())

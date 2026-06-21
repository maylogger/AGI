#!/usr/bin/env python3
"""依 .cursor/rules/taiwan-traditional-chinese.mdc 對照表批次替換中文用語。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = frozenset({"sources", "clients", ".git", "__pycache__", "node_modules"})

# 先保護不應拆開的詞（合規出現在其中為子字串）
PROTECT_PHRASES: list[tuple[str, str]] = [
    ("不符合規定", "<<<PHRASE_NOT_COMPLIANT>>>"),
    ("組合規則", "<<<PHRASE_COMBO_RULES>>>"),
    ("疊合規則", "<<<PHRASE_STACK_RULES>>>"),
]

# 順序重要：先處理較長、較具體的片語
REPLACEMENTS: list[tuple[str, str]] = [
    ("不合規", "不符合規定"),
    ("非合規", "不符合規定"),
    ("合規性", "符規性"),
    ("合規型", "規定型"),
    ("合規", "規定"),
    ("智能", "智慧"),
]


def apply_to_text(text: str) -> str:
    for old, placeholder in PROTECT_PHRASES:
        text = text.replace(old, placeholder)
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    for old, placeholder in PROTECT_PHRASES:
        text = text.replace(placeholder, old)
    return text


def should_process(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.suffix not in {".md", ".yaml", ".yml", ".mdc"}:
        return False
    # 對照表本身保留「避免」欄示範用語
    if path.name == "taiwan-traditional-chinese.mdc":
        return False
    # Skill 內含對照表說明，避免誤替換
    if ".cursor" in path.parts and "skills" in path.parts:
        return False
    return True


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_process(path):
            continue
        original = path.read_text(encoding="utf-8")
        updated = apply_to_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(path.relative_to(ROOT))
    print(f"Updated {changed} files")


if __name__ == "__main__":
    main()

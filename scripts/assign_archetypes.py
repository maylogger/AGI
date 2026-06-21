#!/usr/bin/env python3
"""依 research/archetypes.yaml 規則回填 docs/*.profile.yaml 的 archetype 欄位"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print("需要 PyYAML：pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ARCHETYPES_PATH = ROOT / "research" / "archetypes.yaml"


def load_profile(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    body = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
    return yaml.safe_load(body)


def write_profile(profile: dict, path: Path) -> None:
    header = (
        "# AGI Profile — 聚合層（跨語料可查詢欄位）\n"
        "# 結構層：index_ref | 研究層：note_ref\n"
        "# 產生：python scripts/generate_profiles.py\n"
        "# archetype：python scripts/assign_archetypes.py\n\n"
    )

    def represent_none(self, _):
        return self.represent_scalar("tag:yaml.org,2002:null", "null")

    yaml.add_representer(type(None), represent_none)
    body = yaml.dump(
        profile,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )
    path.write_text(header + body, encoding="utf-8")


def profile_modules(profile: dict) -> set[str]:
    return set(profile.get("modules") or [])


def chapter_titles(profile: dict) -> list[str]:
    return [
        c.get("title", "").lower()
        for c in profile.get("chapter_sequence") or []
    ]


def depth_val(profile: dict, key: str) -> str:
    return (profile.get("depth") or {}).get(key, "")


def depth_num(profile: dict, key: str) -> int:
    return int((profile.get("depth") or {}).get(key, 0) or 0)


def modules_all(profile: dict, names: list[str]) -> bool:
    mods = profile_modules(profile)
    return all(n in mods for n in names)


def modules_any(profile: dict, names: list[str]) -> bool:
    mods = profile_modules(profile)
    return any(n in mods for n in names)


def modules_none(profile: dict, names: list[str]) -> bool:
    mods = profile_modules(profile)
    return not any(n in mods for n in names)


def chapter_keywords_any(profile: dict, keywords: list[str]) -> bool:
    titles = chapter_titles(profile)
    for kw in keywords:
        kw_l = kw.lower()
        for t in titles:
            if kw_l in t:
                return True
    return False


def brand_id_keywords_any(profile: dict, keywords: list[str]) -> bool:
    bid = profile.get("brand_id", "").lower()
    return any(kw.lower() in bid for kw in keywords)


def match_rule_block(profile: dict, block: dict) -> bool:
    if block.get("default"):
        return True

    if "top_level_max" in block:
        if depth_num(profile, "top_level_chapter_count") > block["top_level_max"]:
            return False
    if "top_level_min" in block:
        if depth_num(profile, "top_level_chapter_count") < block["top_level_min"]:
            return False
    if "sections_min" in block:
        if depth_num(profile, "section_count") < block["sections_min"]:
            return False
    if "sections_max" in block:
        if depth_num(profile, "section_count") > block["sections_max"]:
            return False
    if "strategy_depth" in block:
        if depth_val(profile, "strategy") != block["strategy_depth"]:
            return False
    if "strategy_depth_not" in block:
        if depth_val(profile, "strategy") == block["strategy_depth_not"]:
            return False

    if "modules_all" in block:
        if not modules_all(profile, block["modules_all"]):
            return False
    if "modules_any" in block:
        if not modules_any(profile, block["modules_any"]):
            return False
    if "modules_none" in block:
        if not modules_none(profile, block["modules_none"]):
            return False
    if "chapter_title_keywords_any" in block:
        if not chapter_keywords_any(profile, block["chapter_title_keywords_any"]):
            return False
    if "brand_id_keywords_any" in block:
        if not brand_id_keywords_any(profile, block["brand_id_keywords_any"]):
            return False

    if "any_of" in block:
        if not any(match_rule_block(profile, sub) for sub in block["any_of"]):
            return False

    return True


def classify(profile: dict, archetypes: list[dict]) -> str:
    sorted_arch = sorted(
        archetypes,
        key=lambda a: a.get("classification", {}).get("priority", 50),
    )
    for arch in sorted_arch:
        rules = arch.get("classification") or {}
        if match_rule_block(profile, rules):
            return arch["id"]
    return "brand_experience_guide"


def main() -> None:
    with open(ARCHETYPES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    archetypes = data.get("archetypes") or []

    profiles_paths = sorted(DOCS.glob("*.profile.yaml"))
    counts: Counter = Counter()
    updated = 0

    for path in profiles_paths:
        profile = load_profile(path)
        archetype_id = classify(profile, archetypes)
        if profile.get("archetype") != archetype_id:
            profile["archetype"] = archetype_id
            write_profile(profile, path)
            updated += 1
        counts[archetype_id] += 1

    print(f"Assigned archetypes for {len(profiles_paths)} profiles ({updated} updated)")
    print("Distribution:")
    for aid, c in counts.most_common():
        arch = next((a for a in archetypes if a["id"] == aid), {})
        name = arch.get("name", aid)
        pct = c / len(profiles_paths) * 100
        print(f"  {aid}: {c} ({pct:.1f}%)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""從 docs/*.index.yaml 與 docs/*.note.md 產生 docs/*.profile.yaml"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("需要 PyYAML：pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Module taxonomy（對齊 design-guideline-researcher SKILL）
KNOWN_MODULES = {
    "Brand Strategy",
    "Messaging",
    "Content Design",
    "Voice and Tone",
    "Visual Identity",
    "Visual Language",
    "Color System",
    "Typography System",
    "Layout System",
    "Interaction Design",
    "UI Components",
    "Design Tokens",
    "Photography System",
    "Illustration System",
    "Iconography System",
    "Motion Identity",
    "Product Language",
    "Information Design",
    "Data Visualization",
    "Accessibility",
    "Localization",
    "Internationalization",
    "Governance",
    "Operations",
    "Design Process",
    "Compliance",
    "Legal and Trademark",
    "Content Safety",
    "Measurement",
    "AI-Checkable Rules",
    "Examples",
    "Knowledge Architecture",
    "Brand Architecture",
    "Brand Touchpoint Governance",
    "Partnership Branding",
    "Publication Design",
    "Evaluation Framework",
    "Communication Framework",
    "Other",
}

STRATEGY_MODULES = {
    "Brand Strategy",
    "Messaging",
    "Brand Architecture",
    "Evaluation Framework",
    "Communication Framework",
    "Voice and Tone",
    "Content Design",
}

VISUAL_MODULES = {
    "Visual Identity",
    "Visual Language",
    "Color System",
    "Typography System",
    "Layout System",
    "Photography System",
    "Illustration System",
    "Iconography System",
    "Motion Identity",
    "Product Language",
    "Design Tokens",
    "UI Components",
    "Interaction Design",
    "Publication Design",
}

GOVERNANCE_MODULES = {
    "Governance",
    "Operations",
    "Compliance",
    "Legal and Trademark",
    "Content Safety",
    "Brand Touchpoint Governance",
    "Partnership Branding",
    "AI-Checkable Rules",
}

QUANTIFIABLE_RULE_RE = re.compile(
    r"\d|％|%|inch|px|mm|pt|>=|<=|≥|≤|minimum|maximum|不得|必須|至少|不可",
    re.IGNORECASE,
)

ABSTRACTION_RE = re.compile(
    r"10\.\s*\*\*Abstraction\*\*[：:]\s*(?:Guideline 模組類型[：:]?\s*)?(.*)",
)
FRAMEWORKS_RE = re.compile(r"6\.\s*\*\*Frameworks\*\*[：:]\s*(.*)")
PATTERNS_RE = re.compile(r"7\.\s*\*\*Patterns\*\*[：:]\s*(.*)")
RULES_RE = re.compile(r"8\.\s*\*\*Rules\*\*[：:]\s*(.*)")


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.strip().lower())


def flatten_chapters(chapters: list, parent_order: int = 0) -> list[dict]:
    """展平章節樹，保留 id、title、level、order。"""
    result: list[dict] = []
    for ch in chapters:
        entry = {
            "id": ch["id"],
            "title": ch["title"],
            "level": ch.get("level", 1),
            "order": ch.get("order", 0),
        }
        result.append(entry)
        children = ch.get("children") or []
        result.extend(flatten_chapters(children))
    return result


def build_title_map(flat: list[dict]) -> dict[str, str]:
    """normalized title -> chapter id"""
    mapping: dict[str, str] = {}
    for ch in flat:
        mapping[normalize_title(ch["title"])] = ch["id"]
    return mapping


def extract_modules_from_abstraction(text: str) -> list[str]:
    modules: list[str] = []
    for known in KNOWN_MODULES:
        if known in text:
            modules.append(known)
    # 處理 backtick 包裹
    for match in re.findall(r"`([^`]+)`", text):
        cleaned = match.strip()
        if cleaned in KNOWN_MODULES:
            modules.append(cleaned)
    return list(dict.fromkeys(modules))


def depth_level(score: int) -> str:
    if score >= 5:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def compute_depth(doc_modules: list[str], top_level: int, sections: int) -> dict:
    strategy_score = sum(1 for m in doc_modules if m in STRATEGY_MODULES)
    visual_score = sum(1 for m in doc_modules if m in VISUAL_MODULES)
    governance_score = sum(1 for m in doc_modules if m in GOVERNANCE_MODULES)

    # 章節結構啟發式：大章少、小節多 → 執行導向
    if top_level <= 2 and sections >= 6:
        visual_score += 1
    if top_level >= 5:
        visual_score += 1
    if any(m in doc_modules for m in ("Governance", "Compliance", "Operations")):
        governance_score += 1

    return {
        "strategy": depth_level(strategy_score),
        "visual": depth_level(visual_score),
        "governance": depth_level(governance_score),
        "top_level_chapter_count": top_level,
        "section_count": sections,
    }


def extract_framework_name(text: str) -> str:
    text = text.strip()
    # 去掉常見前綴
    for prefix in (
        "主要框架是",
        "框架是",
        "核心框架是",
        "存在",
        "Framework:",
    ):
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    # 取第一句或冒號前
    text = re.split(r"[。.]", text)[0].strip()
    if len(text) > 120:
        text = text[:117] + "..."
    return text


def extract_pattern_names(text: str) -> list[str]:
    patterns: list[str] = []
    # 「xxx」引號內
    for m in re.findall(r"「([^」]+)」", text):
        patterns.append(m.strip())
    if patterns:
        return [p.rstrip("。").strip() for p in patterns[:8]]
    # 可複用模式包含 xxx、yyy
    if "包含" in text:
        part = text.split("包含", 1)[1]
        for seg in re.split(r"[、,，]", part):
            seg = re.sub(r"^[「『\s]+|[」』\s]+$", "", seg.strip())
            if seg and len(seg) < 80:
                patterns.append(seg.rstrip("。").strip())
    if not patterns and len(text) < 100:
        patterns.append(text.strip())
    return patterns[:8]


def infer_module_from_title(title: str) -> str | None:
    t = title.lower()
    mapping = [
        ("logo", "Visual Identity"),
        ("color", "Color System"),
        ("typography", "Typography System"),
        ("type", "Typography System"),
        ("voice", "Voice and Tone"),
        ("tone", "Messaging"),
        ("governance", "Governance"),
        ("compliance", "Compliance"),
        ("motion", "Motion Identity"),
        ("imagery", "Photography System"),
        ("icon", "Iconography System"),
        ("layout", "Layout System"),
        ("brand", "Brand Strategy"),
        ("platform", "Brand Strategy"),
        ("pillar", "Brand Strategy"),
    ]
    for key, mod in mapping:
        if key in t:
            return mod
    return None


def parse_note(note_path: Path, title_map: dict[str, str], flat: list[dict]) -> dict:
    id_to_title = {ch["id"]: ch["title"] for ch in flat}
    content = note_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    current_id: str | None = None
    frameworks: list[dict] = []
    patterns: list[dict] = []
    rules: list[dict] = []
    chapter_modules: list[dict] = []
    chapter_mod_map: dict[str, list[str]] = {}
    all_modules: list[str] = []

    for line in lines:
        header_match = re.match(r"^(#{2,3})\s+(.+)$", line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            if title in ("Summary", "Research Intent"):
                current_id = None
                continue
            norm = normalize_title(title)
            current_id = title_map.get(norm)
            continue

        if not current_id:
            continue

        chapter_title = id_to_title.get(current_id, "")

        abs_match = ABSTRACTION_RE.match(line)
        if abs_match:
            mods = extract_modules_from_abstraction(abs_match.group(1))
            if mods:
                chapter_modules.append(
                    {"id": current_id, "title": chapter_title, "modules": mods}
                )
                chapter_mod_map[current_id] = mods
                all_modules.extend(mods)

        fw_match = FRAMEWORKS_RE.match(line)
        if fw_match:
            name = extract_framework_name(fw_match.group(1))
            if name:
                frameworks.append(
                    {
                        "name": name,
                        "chapter": current_id,
                        "chapter_title": chapter_title,
                    }
                )

        pat_match = PATTERNS_RE.match(line)
        if pat_match:
            for pname in extract_pattern_names(pat_match.group(1)):
                patterns.append(
                    {
                        "name": pname,
                        "chapter": current_id,
                        "chapter_title": chapter_title,
                    }
                )

        rules_match = RULES_RE.match(line)
        if rules_match:
            criterion = rules_match.group(1).strip()
            if QUANTIFIABLE_RULE_RE.search(criterion):
                module = infer_module_from_title(chapter_title) or ""
                if not module and chapter_mod_map.get(current_id):
                    module = chapter_mod_map[current_id][0]
                rules.append(
                    {
                        "module": module,
                        "criterion": criterion,
                        "chapter": current_id,
                        "chapter_title": chapter_title,
                    }
                )

    return {
        "modules": list(dict.fromkeys(all_modules)),
        "frameworks": frameworks,
        "patterns": patterns,
        "rules_ai_checkable": rules,
        "chapters": chapter_modules,
    }


def build_chapter_sequence(chapters: list) -> list[dict]:
    sequence: list[dict] = []
    for ch in sorted(chapters, key=lambda c: c.get("order", 0)):
        sequence.append(
            {
                "id": ch["id"],
                "title": ch["title"],
                "order": ch.get("order", 0),
                "level": ch.get("level", 1),
            }
        )
        children = ch.get("children") or []
        for child in sorted(children, key=lambda c: c.get("order", 0)):
            sequence.append(
                {
                    "id": child["id"],
                    "title": child["title"],
                    "order": child.get("order", 0),
                    "level": child.get("level", 2),
                }
            )
    return sequence


def generate_profile(stem: str) -> dict | None:
    index_path = DOCS / f"{stem}.index.yaml"
    note_path = DOCS / f"{stem}.note.md"

    if not index_path.exists() or not note_path.exists():
        return None

    with open(index_path, encoding="utf-8") as f:
        index_data = yaml.safe_load(f)

    chapters = index_data.get("chapters") or []
    flat = flatten_chapters(chapters)
    title_map = build_title_map(flat)

    top_level = len(chapters)
    sections = sum(len(ch.get("children") or []) for ch in chapters)

    parsed = parse_note(note_path, title_map, flat)
    depth = compute_depth(parsed["modules"], top_level, sections)

    profile = {
        "brand_id": stem,
        "index_ref": f"docs/{stem}.index.yaml",
        "note_ref": f"docs/{stem}.note.md",
        "archetype": None,
        "industry": None,
        "modules": parsed["modules"],
        "depth": depth,
        "chapter_sequence": build_chapter_sequence(chapters),
        "frameworks": parsed["frameworks"],
        "patterns": parsed["patterns"],
        "rules_ai_checkable": parsed["rules_ai_checkable"],
        "chapters": parsed["chapters"],
    }
    return profile


def write_profile_yaml(profile: dict, path: Path) -> None:
    """寫入 YAML，None 顯示為 null。"""

    def represent_none(self, _):
        return self.represent_scalar("tag:yaml.org,2002:null", "null")

    yaml.add_representer(type(None), represent_none)

    header = (
        "# AGI Profile — 聚合層（跨語料可查詢欄位）\n"
        "# 結構層：index_ref | 研究層：note_ref\n"
        "# 產生：python scripts/generate_profiles.py\n\n"
    )
    body = yaml.dump(
        profile,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )
    path.write_text(header + body, encoding="utf-8")


def main() -> None:
    stems = sorted(p.stem.replace(".index", "") for p in DOCS.glob("*.index.yaml"))
    created = 0
    skipped = 0
    errors: list[str] = []

    for stem in stems:
        try:
            profile = generate_profile(stem)
            if profile is None:
                skipped += 1
                continue
            out = DOCS / f"{stem}.profile.yaml"
            write_profile_yaml(profile, out)
            created += 1
        except Exception as e:
            errors.append(f"{stem}: {e}")

    print(f"Created {created} profile.yaml files")
    if skipped:
        print(f"Skipped {skipped} (missing index or note)")
    if errors:
        print(f"Errors {len(errors)}:")
        for err in errors[:10]:
            print(f"  - {err}")


if __name__ == "__main__":
    main()

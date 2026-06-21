#!/usr/bin/env python3
"""從 docs/*.profile.yaml 產生 research/corpus_report.md"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("需要 PyYAML：pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "research" / "corpus_report.md"

STRATEGY_KEYWORDS = (
    "brand",
    "platform",
    "pillar",
    "story",
    "voice",
    "tone",
    "messaging",
    "strategy",
    "position",
    "mission",
    "vision",
)


def load_profiles() -> list[dict]:
    profiles: list[dict] = []
    for path in sorted(DOCS.glob("*.profile.yaml")):
        text = path.read_text(encoding="utf-8")
        # 跳過註解行
        body = "\n".join(
            line for line in text.splitlines() if not line.startswith("#")
        )
        data = yaml.safe_load(body)
        if data:
            profiles.append(data)
    return profiles


def pct(n: int, total: int) -> str:
    if total == 0:
        return "0%"
    return f"{n / total * 100:.1f}%"


def bar(count: int, max_count: int, width: int = 20) -> str:
    if max_count == 0:
        return ""
    filled = round(count / max_count * width)
    return "█" * filled + "░" * (width - filled)


def infer_sequence_style(profile: dict) -> str:
    """策略前置 vs 資產前置（啟發式）。"""
    seq = profile.get("chapter_sequence") or []
    top_level = [c for c in seq if c.get("level") == 1]
    if not top_level:
        return "unknown"

    first_title = top_level[0].get("title", "").lower()
    strategy_score = sum(
        1 for kw in STRATEGY_KEYWORDS if kw in first_title
    )
    depth = profile.get("depth") or {}
    if depth.get("strategy") == "high" or strategy_score > 0:
        return "strategy_first"
    if profile.get("depth", {}).get("top_level_chapter_count", 0) <= 2:
        return "toolkit_flat"
    return "assets_first"


def suggest_cluster(profile: dict) -> str:
    """啟發式原型建議（供 archetype 第二階段參考，非最終分類）。"""
    depth = profile.get("depth") or {}
    modules = set(profile.get("modules") or [])
    top = depth.get("top_level_chapter_count", 0)
    sections = depth.get("section_count", 0)
    style = infer_sequence_style(profile)

    if "Brand Architecture" in modules or "Partnership Branding" in modules:
        return "multi_brand"
    if any(m in modules for m in ("UI Components", "Interaction Design", "Design Tokens")) and top >= 4:
        return "design_system"
    if style == "toolkit_flat" and top <= 2 and sections >= 5:
        return "corporate_toolkit"
    if depth.get("strategy") == "high" and top >= 5:
        return "full_brand_system"
    if style == "strategy_first" and top >= 3:
        return "full_brand_system"
    if sections <= 8 and top <= 3:
        return "logo_or_channel_focus"
    return "general_brand"


def normalize_framework_name(name: str) -> str:
    """粗略正規化 framework 名稱以便共現統計。"""
    n = name.strip()
    # 取冒號前、Framework 關鍵片段
    if "：" in n:
        n = n.split("：", 1)[0].strip()
    if ":" in n and len(n.split(":")[0]) < 40:
        n = n.split(":", 1)[0].strip()
    n = re.sub(r"\s+", " ", n)
    if len(n) > 50:
        n = n[:47] + "..."
    return n


def chapter_order_signature(profile: dict, max_items: int = 5) -> str:
    top = [
        c.get("title", "")
        for c in profile.get("chapter_sequence") or []
        if c.get("level") == 1
    ]
    return " → ".join(top[:max_items])


def generate_report(profiles: list[dict]) -> str:
    total = len(profiles)
    today = date.today().isoformat()

    module_doc_count: Counter = Counter()
    module_chapter_count: Counter = Counter()
    framework_norm: Counter = Counter()
    framework_pairs: Counter = Counter()
    pattern_count: Counter = Counter()
    depth_strategy: Counter = Counter()
    depth_visual: Counter = Counter()
    depth_governance: Counter = Counter()
    top_level_counts: Counter = Counter()
    section_counts: list[int] = []
    sequence_styles: Counter = Counter()
    cluster_hints: Counter = Counter()
    rules_per_doc: list[int] = []
    frameworks_per_doc: list[int] = []
    patterns_per_doc: list[int] = []
    modules_per_doc: list[int] = []
    order_signatures: Counter = Counter()
    archetype_filled = sum(1 for p in profiles if p.get("archetype"))
    industry_filled = sum(1 for p in profiles if p.get("industry"))
    archetype_counts: Counter = Counter(
        p.get("archetype") or "unassigned" for p in profiles
    )

    # Module co-occurrence
    module_cooccur: defaultdict[str, Counter] = defaultdict(Counter)

    for p in profiles:
        mods = list(dict.fromkeys(p.get("modules") or []))
        modules_per_doc.append(len(mods))
        for m in mods:
            module_doc_count[m] += 1
        for i, a in enumerate(mods):
            for b in mods[i + 1:]:
                pair = tuple(sorted([a, b]))
                module_cooccur[a][b] += 1
                module_cooccur[b][a] += 1

        for ch in p.get("chapters") or []:
            for m in ch.get("modules") or []:
                module_chapter_count[m] += 1

        fw_names = []
        for fw in p.get("frameworks") or []:
            norm = normalize_framework_name(fw.get("name", ""))
            if norm:
                framework_norm[norm] += 1
                fw_names.append(norm)
        frameworks_per_doc.append(len(p.get("frameworks") or []))

        if len(fw_names) >= 2:
            for i, a in enumerate(fw_names):
                for b in fw_names[i + 1:]:
                    pair = tuple(sorted([a, b]))
                    framework_pairs[pair] += 1

        for pat in p.get("patterns") or []:
            name = pat.get("name", "").strip()
            if name:
                pattern_count[name] += 1
        patterns_per_doc.append(len(p.get("patterns") or []))

        rules = p.get("rules_ai_checkable") or []
        rules_per_doc.append(len(rules))

        depth = p.get("depth") or {}
        depth_strategy[depth.get("strategy", "unknown")] += 1
        depth_visual[depth.get("visual", "unknown")] += 1
        depth_governance[depth.get("governance", "unknown")] += 1
        top = depth.get("top_level_chapter_count", 0)
        sec = depth.get("section_count", 0)
        top_level_counts[top] += 1
        section_counts.append(sec)

        style = infer_sequence_style(p)
        sequence_styles[style] += 1
        cluster_hints[suggest_cluster(p)] += 1
        order_signatures[chapter_order_signature(p)] += 1

    avg_sections = sum(section_counts) / total if total else 0
    avg_rules = sum(rules_per_doc) / total if total else 0
    avg_frameworks = sum(frameworks_per_doc) / total if total else 0
    avg_patterns = sum(patterns_per_doc) / total if total else 0
    avg_modules = sum(modules_per_doc) / total if total else 0
    docs_with_rules = sum(1 for r in rules_per_doc if r > 0)

    max_mod = module_doc_count.most_common(1)[0][1] if module_doc_count else 1

    lines: list[str] = [
        "# AGI Corpus Report",
        "",
        f"產生日期：{today}",
        f"語料規模：{total} 份 guideline profile",
        f"資料來源：`docs/*.profile.yaml`",
        f"產生命令：`python scripts/generate_corpus_report.py`",
        "",
        "## 摘要",
        "",
        f"- 平均每份 guideline 涵蓋 **{avg_modules:.1f}** 個模組類型、**{avg_frameworks:.1f}** 個 framework 條目、**{avg_patterns:.1f}** 個 pattern 條目。",
        f"- 平均每份有 **{avg_rules:.1f}** 條可量化／AI-checkable rules；**{docs_with_rules}** 份（{pct(docs_with_rules, total)}）至少有一條。",
        f"- 平均 **{avg_sections:.1f}** 個小節（level-2）；大章數最常見為 **{top_level_counts.most_common(1)[0][0]}** 個。",
        f"- `archetype` 已填：**{archetype_filled}** 份；`industry` 已填：**{industry_filled}** 份。",
        "",
        "### Archetype 分布",
        "",
        "| archetype | 份數 | 佔比 |",
        "|-----------|------|------|",
    ]

    for aid, c in archetype_counts.most_common():
        lines.append(f"| {aid} | {c} | {pct(c, total)} |")

    lines.extend([
        "",
        "定義見 `research/archetypes.yaml`；分類：`python scripts/assign_archetypes.py`。",
        "",
        "---",
        "",
        "## 1. 模組出現頻率（文件級）",
        "",
        "每份 profile 的 `modules` 欄位（來自 note Abstraction 正規化）。",
        "",
        "| 模組 | 出現份數 | 佔比 | 分佈 |",
        "|------|----------|------|------|",
    ])

    for mod, count in module_doc_count.most_common():
        lines.append(
            f"| {mod} | {count} | {pct(count, total)} | `{bar(count, max_mod)}` |"
        )

    lines.extend([
        "",
        "### 模組共現（前 15 對）",
        "",
        "同一文件內同時出現的模組對，供 module_graph 初稿參考。",
        "",
        "| 模組 A | 模組 B | 共現份數 |",
        "|--------|--------|----------|",
    ])

    pair_list: list[tuple[str, str, int]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for a, counter in module_cooccur.items():
        for b, c in counter.items():
            pair = tuple(sorted([a, b]))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            pair_list.append((pair[0], pair[1], c))
    pair_list.sort(key=lambda x: -x[2])

    for a, b, c in pair_list[:15]:
        lines.append(f"| {a} | {b} | {c} |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. 深度指標分布（depth）",
        "",
        "### strategy / visual / governance",
        "",
        "| 維度 | low | medium | high |",
        "|------|-----|--------|------|",
        f"| strategy | {depth_strategy.get('low', 0)} ({pct(depth_strategy.get('low', 0), total)}) | "
        f"{depth_strategy.get('medium', 0)} ({pct(depth_strategy.get('medium', 0), total)}) | "
        f"{depth_strategy.get('high', 0)} ({pct(depth_strategy.get('high', 0), total)}) |",
        f"| visual | {depth_visual.get('low', 0)} ({pct(depth_visual.get('low', 0), total)}) | "
        f"{depth_visual.get('medium', 0)} ({pct(depth_visual.get('medium', 0), total)}) | "
        f"{depth_visual.get('high', 0)} ({pct(depth_visual.get('high', 0), total)}) |",
        f"| governance | {depth_governance.get('low', 0)} ({pct(depth_governance.get('low', 0), total)}) | "
        f"{depth_governance.get('medium', 0)} ({pct(depth_governance.get('medium', 0), total)}) | "
        f"{depth_governance.get('high', 0)} ({pct(depth_governance.get('high', 0), total)}) |",
        "",
        "### 大章數（top_level_chapter_count）",
        "",
        "| 大章數 | 份數 | 佔比 |",
        "|--------|------|------|",
    ])

    for n in sorted(top_level_counts.keys()):
        c = top_level_counts[n]
        lines.append(f"| {n} | {c} | {pct(c, total)} |")

    lines.extend([
        "",
        "### 小節數分布（section_count）",
        "",
        f"- 最小：{min(section_counts)}",
        f"- 最大：{max(section_counts)}",
        f"- 平均：{avg_sections:.1f}",
        f"- 中位數：{sorted(section_counts)[len(section_counts) // 2]}",
        "",
        "---",
        "",
        "## 3. 章節順序模式",
        "",
        "### 啟發式分類",
        "",
        "| 模式 | 份數 | 佔比 | 說明 |",
        "|------|------|------|------|",
        f"| strategy_first | {sequence_styles.get('strategy_first', 0)} | "
        f"{pct(sequence_styles.get('strategy_first', 0), total)} | 首章含策略關鍵字或 strategy depth=high |",
        f"| toolkit_flat | {sequence_styles.get('toolkit_flat', 0)} | "
        f"{pct(sequence_styles.get('toolkit_flat', 0), total)} | ≤2 大章且小節多（類 AMD 扁平工具包） |",
        f"| assets_first | {sequence_styles.get('assets_first', 0)} | "
        f"{pct(sequence_styles.get('assets_first', 0), total)} | 視覺／資產章節前置 |",
        f"| unknown | {sequence_styles.get('unknown', 0)} | "
        f"{pct(sequence_styles.get('unknown', 0), total)} | 無法判斷 |",
        "",
        "### 常見大章順序（前 10）",
        "",
        "| 次數 | 大章順序（前 5 章） |",
        "|------|---------------------|",
    ])

    for sig, c in order_signatures.most_common(10):
        sig_esc = sig.replace("|", "\\|")
        lines.append(f"| {c} | {sig_esc} |")

    lines.extend([
        "",
        "---",
        "",
        "## 4. Framework 統計",
        "",
        "### 高頻 framework 名稱（正規化後，前 20）",
        "",
        "| Framework | 出現次數 |",
        "|-----------|----------|",
    ])

    for name, c in framework_norm.most_common(20):
        name_esc = name.replace("|", "\\|")
        lines.append(f"| {name_esc} | {c} |")

    lines.extend([
        "",
        "### Framework 共現（同文件內，前 10 對）",
        "",
        "| Framework A | Framework B | 共現次數 |",
        "|-------------|-------------|----------|",
    ])

    for pair, c in framework_pairs.most_common(10):
        a, b = pair
        lines.append(f"| {a} | {b} | {c} |")

    lines.extend([
        "",
        "---",
        "",
        "## 5. Pattern 統計",
        "",
        "高頻可複用 pattern 名稱（前 25）：",
        "",
        "| Pattern | 出現次數 |",
        "|---------|----------|",
    ])

    for name, c in pattern_count.most_common(25):
        name_esc = name.replace("|", "\\|")
        lines.append(f"| {name_esc} | {c} |")

    lines.extend([
        "",
        "---",
        "",
        "## 6. AI-Checkable Rules",
        "",
        f"- 有 quantifiable rules 的文件：**{docs_with_rules}** / {total}（{pct(docs_with_rules, total)}）",
        f"- 平均每份 rules 條數：**{avg_rules:.1f}**",
        f"- 最多 rules 的份數：**{max(rules_per_doc)}**",
        "",
        "---",
        "",
        "## 7. 啟發式原型建議（第二階段 archetype 參考）",
        "",
        "以下為演算法建議，**非最終 archetype 分類**；第二階段需專家標註與 `archetypes.yaml` 定稿。",
        "",
        "| 建議原型 | 份數 | 佔比 | 典型特徵 |",
        "|----------|------|------|----------|",
        f"| corporate_toolkit | {cluster_hints.get('corporate_toolkit', 0)} | "
        f"{pct(cluster_hints.get('corporate_toolkit', 0), total)} | 扁平、≤2 大章、小節多 |",
        f"| full_brand_system | {cluster_hints.get('full_brand_system', 0)} | "
        f"{pct(cluster_hints.get('full_brand_system', 0), total)} | strategy 高、大章多 |",
        f"| multi_brand | {cluster_hints.get('multi_brand', 0)} | "
        f"{pct(cluster_hints.get('multi_brand', 0), total)} | 含 Brand Architecture 等 |",
        f"| design_system | {cluster_hints.get('design_system', 0)} | "
        f"{pct(cluster_hints.get('design_system', 0), total)} | UI/元件/token 模組 |",
        f"| logo_or_channel_focus | {cluster_hints.get('logo_or_channel_focus', 0)} | "
        f"{pct(cluster_hints.get('logo_or_channel_focus', 0), total)} | 章節少、聚焦 |",
        f"| general_brand | {cluster_hints.get('general_brand', 0)} | "
        f"{pct(cluster_hints.get('general_brand', 0), total)} | 其餘 |",
        "",
        "### 參考先例",
        "",
        "| 原型參考 | brand_id | top_level | sections | strategy | visual | governance |",
        "|----------|----------|-----------|----------|----------|--------|------------|",
    ])

    refs = {
        "corporate_toolkit": "AMD_branding_guidelines_2020",
        "full_brand_system": "LucidMotors",
        "multi_brand": "WouldBankGroup_Branding_Visual_Identity_Guidelines_2016",
        "design_system": "Slack-Brand-Guidelines",
    }
    by_id = {p["brand_id"]: p for p in profiles}

    for label, bid in refs.items():
        p = by_id.get(bid)
        if not p:
            continue
        d = p.get("depth") or {}
        lines.append(
            f"| {label} | {bid} | {d.get('top_level_chapter_count')} | "
            f"{d.get('section_count')} | {d.get('strategy')} | {d.get('visual')} | {d.get('governance')} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 8. 對第二階段的建議",
        "",
        "1. **Archetype 定義**：已完成 `research/archetypes.yaml`；profile 已回填 archetype。",
        "2. **Module graph**：§1 模組共現 + note 的 Relationship 可合併為 `research/module_graph.yaml`。",
        "3. **章節順序**：§3 常見大章順序可作各原型的 `typical_chapter_sequence` 初稿。",
        "4. **Industry**：本報告未含產業維度；建議 archetype 定稿後抽樣手標 30 份 `industry`。",
        "5. **品質**：rules 抽取為啟發式；corpus 中部分 rules 為描述性句子，Coach 產出時需再篩選真正可量化規則。",
        "",
    ])

    return "\n".join(lines)


def main() -> None:
    profiles = load_profiles()
    if not profiles:
        print("No profile.yaml files found in docs/")
        sys.exit(1)

    report = generate_report(profiles)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(report, encoding="utf-8")
    print(f"Written {OUT} ({len(profiles)} profiles)")


if __name__ == "__main__":
    main()

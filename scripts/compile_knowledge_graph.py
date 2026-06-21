#!/usr/bin/env python3
"""編譯 AGI 知識圖譜（L3 決策層）。

讀取 docs/*.decisions.yaml（各文件 sidecar），執行：
  1. strict evidence 驗證——每筆 evidence 的 brand_id 必須有 index.yaml，
     且 chapter 必須存在於該 index 的章節樹（含子章節）。
  2. 依 dp- id 合併同名決策卡（union 各清單欄位、串接 evidence）。
  3. 依「不同支持品牌數」計算 confidence。
  4. 輸出全域圖譜 research/decision_patterns.yaml（含 by_industry /
     by_brand_type / by_module / by_signal 反向索引）。
  5. 交叉檢查 research/contexts/*.yaml 與 research/modules/*.yaml 中引用的
     dp- id 是否已萃取，列出待補（backlog）。
  6. 輸出報告 research/knowledge_graph_report.md。

用法：python scripts/compile_knowledge_graph.py
依賴：PyYAML
"""

from __future__ import annotations

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
RESEARCH = ROOT / "research"
OUT_GRAPH = RESEARCH / "decision_patterns.yaml"
OUT_REPORT = RESEARCH / "knowledge_graph_report.md"

# union 型清單欄位（合併時去重保序）
LIST_FIELDS_REASON = ["reason", "examples", "anti_patterns"]
APPLICABLE_KEYS = ["industries", "brand_types", "conditions", "archetypes"]
DEP_KEYS = ["requires", "enables", "conflicts_with"]


def strip_comments(text: str) -> str:
    return "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))


def load_yaml(path: Path):
    return yaml.safe_load(strip_comments(path.read_text(encoding="utf-8")))


def collect_chapter_ids(chapters) -> set[str]:
    """遞迴收集章節樹中所有 id。"""
    ids: set[str] = set()
    for ch in chapters or []:
        cid = ch.get("id")
        if cid:
            ids.add(str(cid))
        ids |= collect_chapter_ids(ch.get("children"))
    return ids


def load_index_chapter_ids() -> dict[str, set[str]]:
    """brand_id -> 該 index.yaml 的所有章節 id。"""
    mapping: dict[str, set[str]] = {}
    for idx in DOCS.glob("*.index.yaml"):
        stem = idx.name[: -len(".index.yaml")]
        try:
            data = load_yaml(idx) or {}
        except Exception:
            continue
        mapping[stem] = collect_chapter_ids(data.get("chapters"))
    return mapping


def uniq(seq):
    out = []
    for x in seq or []:
        if x not in out:
            out.append(x)
    return out


def confidence_from_brands(n: int) -> float:
    if n >= 4:
        return 0.95
    return {0: 0.0, 1: 0.5, 2: 0.7, 3: 0.85}.get(n, 0.5)


def merge_card(acc: dict, card: dict) -> None:
    """把單張 card 併入累積卡 acc（同一 dp- id）。"""
    if not acc.get("title"):
        acc["title"] = card.get("title")
    # problem：保留首個 statement，union signals
    prob = card.get("problem") or {}
    if not acc["problem"].get("statement"):
        acc["problem"]["statement"] = prob.get("statement")
    acc["problem"]["signals"] = uniq(
        acc["problem"].get("signals", []) + (prob.get("signals") or [])
    )
    # solution：保留首個
    if not acc.get("solution"):
        acc["solution"] = card.get("solution") or {}
    for f in LIST_FIELDS_REASON:
        acc[f] = uniq(acc.get(f, []) + (card.get(f) or []))
    aw_src = card.get("applicable_when") or {}
    for k in APPLICABLE_KEYS:
        acc["applicable_when"][k] = uniq(
            acc["applicable_when"].get(k, []) + (aw_src.get(k) or [])
        )
    dep_src = card.get("dependencies") or {}
    for k in DEP_KEYS:
        acc["dependencies"][k] = uniq(
            acc["dependencies"].get(k, []) + (dep_src.get(k) or [])
        )
    acc["evidence"].extend(card.get("evidence") or [])


def new_acc(dp_id: str) -> dict:
    return {
        "id": dp_id,
        "title": None,
        "problem": {"statement": None, "signals": []},
        "solution": {},
        "reason": [],
        "applicable_when": {k: [] for k in APPLICABLE_KEYS},
        "dependencies": {k: [] for k in DEP_KEYS},
        "examples": [],
        "anti_patterns": [],
        "evidence": [],
    }


def main() -> None:
    index_ids = load_index_chapter_ids()
    sidecars = sorted(DOCS.glob("*.decisions.yaml"))

    cards: dict[str, dict] = {}
    invalid_evidence: list[tuple[str, str, str, str]] = []  # (sidecar, dp, brand, chapter)
    raw_card_count = 0

    for sc in sidecars:
        data = load_yaml(sc) or {}
        for card in data.get("decisions") or []:
            dp_id = card.get("id")
            if not dp_id:
                continue
            raw_card_count += 1
            # 驗證 evidence
            valid_ev = []
            for ev in card.get("evidence") or []:
                b = ev.get("brand_id")
                c = str(ev.get("chapter")) if ev.get("chapter") is not None else None
                if b in index_ids and c and c in index_ids[b]:
                    valid_ev.append(ev)
                else:
                    invalid_evidence.append((sc.name, dp_id, str(b), str(c)))
            card = dict(card)
            card["evidence"] = valid_ev
            if dp_id not in cards:
                cards[dp_id] = new_acc(dp_id)
            merge_card(cards[dp_id], card)

    # 完稿：計算 confidence、status、去重 evidence
    verified: dict[str, dict] = {}
    unverified: list[str] = []
    for dp_id, acc in cards.items():
        # evidence 去重（brand_id+chapter）
        seen = set()
        dedup_ev = []
        for ev in acc["evidence"]:
            key = (ev.get("brand_id"), str(ev.get("chapter")))
            if key in seen:
                continue
            seen.add(key)
            dedup_ev.append(ev)
        acc["evidence"] = dedup_ev
        brand_count = len({ev.get("brand_id") for ev in dedup_ev})
        acc["evidence_brand_count"] = brand_count
        acc["confidence"] = confidence_from_brands(brand_count)
        acc["status"] = "verified" if brand_count >= 1 else "unverified"
        if brand_count >= 1:
            verified[dp_id] = acc
        else:
            unverified.append(dp_id)

    # 反向索引
    by_industry: defaultdict[str, list] = defaultdict(list)
    by_brand_type: defaultdict[str, list] = defaultdict(list)
    by_module: defaultdict[str, list] = defaultdict(list)
    by_signal: defaultdict[str, list] = defaultdict(list)
    for dp_id, acc in verified.items():
        aw = acc["applicable_when"]
        for ind in aw.get("industries", []):
            by_industry[ind].append(dp_id)
        for bt in aw.get("brand_types", []):
            by_brand_type[bt].append(dp_id)
        mod = (acc.get("solution") or {}).get("module")
        if mod:
            by_module[mod].append(dp_id)
        for sig in acc["problem"].get("signals", []):
            by_signal[sig].append(dp_id)

    # 引用覆蓋檢查：contexts / modules 中提到的 dp- id
    referenced: set[str] = set()
    ref_sources: defaultdict[str, list] = defaultdict(list)

    def scan_for_refs(obj, src):
        if isinstance(obj, dict):
            for v in obj.values():
                scan_for_refs(v, src)
        elif isinstance(obj, list):
            for v in obj:
                scan_for_refs(v, src)
        elif isinstance(obj, str) and obj.startswith("dp-"):
            referenced.add(obj)
            if src not in ref_sources[obj]:
                ref_sources[obj].append(src)

    unknown_evidence_brands: list[tuple[str, str, str]] = []  # (file, entry_id, brand)
    for ctx in (RESEARCH / "contexts").glob("*.yaml"):
        data = load_yaml(ctx) or {}
        scan_for_refs(data, ctx.name)
        for entry in data.get("entries") or []:
            for b in entry.get("evidence_brands") or []:
                if b not in index_ids:
                    unknown_evidence_brands.append((ctx.name, entry.get("id", "?"), b))
    for mod in (RESEARCH / "modules").glob("*.yaml"):
        scan_for_refs(load_yaml(mod), mod.name)

    backlog = sorted(referenced - set(verified.keys()) - set(unverified))

    # 寫出全域圖譜
    graph = {
        "version": 1,
        "generated": date.today().isoformat(),
        "source": "docs/*.decisions.yaml",
        "stats": {
            "verified_patterns": len(verified),
            "unverified_patterns": len(unverified),
            "sidecar_files": len(sidecars),
            "raw_cards": raw_card_count,
        },
        "patterns": [verified[k] for k in sorted(verified.keys())],
        "indices": {
            "by_industry": {k: sorted(v) for k, v in sorted(by_industry.items())},
            "by_brand_type": {k: sorted(v) for k, v in sorted(by_brand_type.items())},
            "by_module": {k: sorted(v) for k, v in sorted(by_module.items())},
            "by_signal": {k: sorted(v) for k, v in sorted(by_signal.items())},
        },
    }

    def represent_none(self, _):
        return self.represent_scalar("tag:yaml.org,2002:null", "null")

    yaml.add_representer(type(None), represent_none)
    header = (
        "# AGI 決策圖譜（L3）— 由 scripts/compile_knowledge_graph.py 自動產生\n"
        "# 請勿手動編輯；新增決策卡請改 docs/<brand_id>.decisions.yaml 後重跑。\n"
        "# schema：research/schemas/decision_pattern.schema.yaml\n\n"
    )
    OUT_GRAPH.write_text(
        header
        + yaml.dump(graph, allow_unicode=True, default_flow_style=False, sort_keys=False, width=100),
        encoding="utf-8",
    )

    # 報告
    lines = [
        "# AGI Knowledge Graph Report",
        "",
        f"產生日期：{date.today().isoformat()}",
        f"產生命令：`python scripts/compile_knowledge_graph.py`",
        "",
        "## 摘要",
        "",
        f"- 已驗證決策卡：**{len(verified)}**（至少一筆有效 evidence）",
        f"- 未驗證決策卡：**{len(unverified)}**",
        f"- sidecar 檔數：**{len(sidecars)}**；原始卡片數（合併前）：**{raw_card_count}**",
        f"- contexts/modules 引用但尚未萃取（backlog）：**{len(backlog)}**",
        "",
        "## 決策卡（依信心排序）",
        "",
        "| dp-id | 支持品牌數 | confidence | 模組 | 適用產業 |",
        "|-------|-----------|-----------|------|----------|",
    ]
    for dp_id in sorted(verified, key=lambda k: -verified[k]["confidence"]):
        a = verified[dp_id]
        mod = (a.get("solution") or {}).get("module", "")
        inds = ", ".join(a["applicable_when"].get("industries", [])) or "—"
        lines.append(
            f"| `{dp_id}` | {a['evidence_brand_count']} | {a['confidence']:.2f} | {mod} | {inds} |"
        )

    lines += ["", "## 反向索引：產業 → 決策卡", ""]
    for ind in sorted(by_industry):
        lines.append(f"- **{ind}**：{', '.join(sorted(by_industry[ind]))}")

    lines += ["", "## 反向索引：品牌類型 → 決策卡", ""]
    for bt in sorted(by_brand_type):
        lines.append(f"- **{bt}**：{', '.join(sorted(by_brand_type[bt]))}")

    if invalid_evidence:
        lines += [
            "",
            "## ⚠ 無效 evidence（strict 模式已排除）",
            "",
            "下列 evidence 的 brand_id 或 chapter 在 docs/*.index.yaml 找不到，需修正：",
            "",
            "| sidecar | dp-id | brand_id | chapter |",
            "|---------|-------|----------|---------|",
        ]
        for sc, dp, b, c in invalid_evidence:
            lines.append(f"| {sc} | `{dp}` | {b} | {c} |")

    if unknown_evidence_brands:
        lines += [
            "",
            "## ⚠ contexts 中找不到對應 docs 的 evidence_brands",
            "",
            "下列 evidence_brands 在 docs/ 沒有對應 index.yaml（可能拼字或大小寫不符）：",
            "",
            "| 檔案 | entry | brand_id |",
            "|------|-------|----------|",
        ]
        for f, eid, b in unknown_evidence_brands:
            lines.append(f"| {f} | {eid} | {b} |")

    if backlog:
        lines += [
            "",
            "## 待萃取 backlog（已被引用但尚無決策卡）",
            "",
            "contexts/modules 已引用下列 dp- id，但尚未在任何 sidecar 萃取。"
            "這是 extractor skill 的優先工作清單：",
            "",
        ]
        for dp in backlog:
            srcs = ", ".join(ref_sources.get(dp, []))
            lines.append(f"- `{dp}`（被 {srcs} 引用）")

    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 終端摘要
    print(f"Compiled {len(verified)} verified patterns from {len(sidecars)} sidecars.")
    print(f"  unverified: {len(unverified)} | invalid evidence: {len(invalid_evidence)} | backlog: {len(backlog)} | unknown ctx brands: {len(unknown_evidence_brands)}")
    print(f"Written: {OUT_GRAPH.relative_to(ROOT)}")
    print(f"Written: {OUT_REPORT.relative_to(ROOT)}")
    if invalid_evidence:
        print("⚠ 有無效 evidence，詳見報告。")


if __name__ == "__main__":
    main()

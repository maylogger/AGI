---
name: design-strategy-extractor
description: 當使用者想把既有 docs/*.note.md 的反向工程分析「升級」成可推理的決策知識（problem → solution → reason → applicable_when → evidence）時使用。此 skill 從 note.md + index.yaml 萃取 Decision Pattern 決策卡，寫入 docs/<brand_id>.decisions.yaml（strict evidence，連回真實章節），並可回填 profile.industry。支援增量處理：已完成或無新內容的文件會跳過以節省 token。適用於建立 AGI 知識圖譜 L3 決策層、把 128 份語料的「為什麼」結構化、或清理 knowledge_graph_report.md 的 backlog。
---

# Design Strategy Extractor

把 AGI 既有研究成果（`docs/*.note.md` 的十一維分析）**升級**成知識圖譜的 L3 決策層：可被 Design Strategy Agent 推理、可回溯證據的 **Decision Pattern 決策卡**。

核心轉換：

```text
note.md（散文式 why）  →  decisions.yaml（結構化 problem/solution/reason + evidence）
```

這不是重做 researcher 的分析，而是把已分析好的 `Chapter Purpose / Principles / Frameworks / Reusable Knowledge` 重新編碼成「高階設計師的決策」，並嚴格連回證據。

## 與其他 skill 的分工

| Skill | 輸入 | 輸出 |
|-------|------|------|
| design-guideline-researcher | PDF | `docs/*.index.yaml` + `note.md` |
| **design-strategy-extractor（本 skill）** | `note.md` + `index.yaml` | `docs/*.decisions.yaml` + 回填 `profile.industry` |
| design-guideline-coach | 客戶 brief + 知識圖譜 | `clients/<slug>/` guideline 初稿 |

## 台灣繁體正體用語

所有中文欄位（problem.statement、reason、excerpt 等）須遵循 [`.cursor/rules/taiwan-traditional-chinese.mdc`](../../rules/taiwan-traditional-chinese.mdc)。

## 必讀資源

開始前先讀：

1. [`research/schemas/decision_pattern.schema.yaml`](../../../research/schemas/decision_pattern.schema.yaml) — 決策卡欄位定義
2. [`research/contexts/industries.yaml`](../../../research/contexts/industries.yaml)、[`brand_types.yaml`](../../../research/contexts/brand_types.yaml) — `applicable_when` 可用的 id
3. [`research/knowledge_graph_report.md`](../../../research/knowledge_graph_report.md) 的 **backlog** — 已被引用但尚未萃取的 `dp-` id（優先補齊）
4. 既有 `docs/*.decisions.yaml`（如 3M、LucidMotors）作為格式範本

## strict evidence 原則（最重要）

- **每張卡至少一筆 `evidence`**，且 `evidence.chapter` 必須是該 `brand_id` 的 `index.yaml` 中真實存在的章節 id。
- `excerpt` 須節錄自 `note.md` 中支持此決策的語句，**不得杜撰**。
- 找不到證據就 **不要寫這張卡**。寧缺勿造。
- 編譯時 `scripts/compile_knowledge_graph.py` 會驗證所有 evidence；無效的會被列入報告的「無效 evidence」並排除。

## 增量處理

處理某份 `docs/<brand_id>.note.md` 前：

- 若 `docs/<brand_id>.decisions.yaml` 已存在且涵蓋該文件主要決策，**跳過**（除非使用者要求重萃或 note 已更新）。
- 優先處理 backlog 中被引用的 `dp-` id 對應的品牌（看 `applicable_when` 與 evidence_brands 線索）。
- 每批處理數份即可，不必一次跑完 128 份。

## 工作流程

1. **選取目標**：依使用者指定，或從 backlog 與尚無 sidecar 的 `docs/*.note.md` 中挑選。
2. **讀 note + index**：對每個大章／主要小節，從十一維分析中辨識「決策」——尤其是 `Chapter Purpose`（解決什麼問題）、`Principles`／`Reusable Knowledge`（為什麼）、`Frameworks`／`Patterns`（用什麼手法）。
3. **編碼成決策卡**：
   - `problem.statement`：此決策要解決的情境問題（描述情境，不描述品牌）。
   - `problem.signals`：可被客戶 intake 觸發的標籤（snake_case）。
   - `solution.move`：採用的設計手法／框架。
   - `reason`：為什麼這個手法能解決這個問題（多取自 Principles / Reusable Knowledge）。
   - `applicable_when`：對照 contexts 的 `industries` / `brand_types` id 與 archetype。
   - `dependencies`：requires / enables（對齊 `module_graph.yaml`）。
   - `anti_patterns`、`examples`：若 note 有提供。
   - `evidence`：`brand_id` + 真實 `chapter` + `excerpt`。
4. **沿用既有 dp- id**：若該決策與既有卡語意相同，**使用相同 `id`**（讓 compile 合併、累計 confidence）。只有新概念才建立新 `dp-` id（kebab-case、前綴 `dp-`）。
5. **回填 industry（可選）**：依 `industries.yaml` 的 `evidence_brands` 與 aliases 判斷該品牌產業，寫入 `docs/<brand_id>.profile.yaml` 的 `industry` 欄位（原為 null）。
6. **重編譯**：執行 `python scripts/compile_knowledge_graph.py`，確認新卡通過 strict 驗證、無「無效 evidence」。
7. **回報**：列出新增／合併的決策卡、回填的 industry、剩餘 backlog。

## `decisions.yaml` 格式

```yaml
brand_id: <與檔名 stem 相同>
decisions:
  - id: dp-<concept>
    title: 一句話標題
    problem:
      statement: ...
      signals: [snake_case, ...]
    solution:
      module: <module taxonomy>
      move: ...
      layer: strategy|language|visual_core|visual_extended|product|governance
    reason: [...]
    applicable_when:
      industries: [...]      # 見 industries.yaml
      brand_types: [...]     # 見 brand_types.yaml
      conditions: [...]
      archetypes: [...]      # 見 archetypes.yaml
    dependencies:
      requires: [...]
      enables: [...]
    examples: [...]
    anti_patterns: [...]
    evidence:
      - {brand_id: <stem>, chapter: ch-xx, excerpt: "節錄自 note.md"}
    status: extracted
```

## 品質檢查清單

- [ ] 每張卡至少一筆有效 evidence（chapter 存在於 index.yaml）
- [ ] `excerpt` 確實出自 note.md，未杜撰
- [ ] `applicable_when` 的 id 出自 contexts/archetypes，未自創未定義 id
- [ ] 語意重複的決策沿用既有 `dp-` id，而非另建
- [ ] 已執行 compile 腳本且報告無「無效 evidence」
- [ ] 中文遵循台灣繁體正體用語

## 觸發範例

- 「用 design-strategy-extractor 處理 docs 裡還沒有 decisions.yaml 的 5 份，優先補 backlog」
- 「把 Harrods、Coldwell_Banker 萃取成決策卡，補 dp-restraint-as-luxury-signal」
- 「重新萃取 LucidMotors 的 decisions 並重編譯知識圖譜」

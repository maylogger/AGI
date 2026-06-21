# AGI — 安裝、知識庫維護與原理

本文件涵蓋 [README.md](README.md) 之外的內容：環境安裝、擴充與維護知識庫的其他 Skill（Researcher、Strategy Extractor）、知識圖譜的原理與架構、維護腳本與延伸方向。為新客戶規劃 guideline 的日常使用方式（Coach）請見 [README.md](README.md)。

---

## 環境準備

1. Clone 本 repo，在本機中開啟專案
2. （Researcher 用）將 guideline PDF 放入 `sources/`（已 gitignore，不入庫）
3. （維護腳本用）Python 3 + PyYAML：`pip install pyyaml`

### 中文用語（台灣繁體正體）

Agent 產出中文須遵循 [`.cursor/rules/taiwan-traditional-chinese.mdc`](.cursor/rules/taiwan-traditional-chinese.mdc)（例如：合規→規定、智能→智慧）。批次修正既有檔案：

```bash
python scripts/apply_taiwan_zh_terms.py
```

---

## 擴充知識庫：分析既有 Guideline（Researcher）

**Skill：** `design-guideline-researcher`  
路徑：`.cursor/skills/design-guideline-researcher/SKILL.md`

### 做什麼

從 `sources/` 讀取 PDF，產出 `docs/` 下的 `index.yaml` 與 `note.md`。不是一般摘要，而是以 **Design Infrastructure Researcher** 視角 **反向工程**：

- 章節為什麼存在（Chapter Purpose）
- 使用了哪些 framework、pattern、可量化 rule
- 哪些知識可抽象為跨品牌模組（Module taxonomy）

### 怎麼觸發

```text
我把幾份 brand guideline PDF 放進 sources/ 了，請幫我建立 docs 的 index.yaml 和 note.md。
note 不要摘要，請從 Design Infrastructure Researcher 角度分析。
```

若 `index.yaml` 與 `note.md` 已完整，會 **跳過** 該 PDF（增量處理）。

### 分析後更新聚合層

```bash
python scripts/generate_profiles.py    # 產生 profile.yaml
python scripts/assign_archetypes.py    # 回填 archetype
python scripts/generate_corpus_report.py # 更新語料報告
```

### 十一維分析要點（`note.md`）

每個大章／主要小節回答：Chapter Purpose、Definition、Relationship、Design Execution、Principles、Frameworks、Patterns、Rules（盡量 AI-checkable）、Reusable Knowledge、Abstraction、Visual Evidence。

---

## 擴充知識庫：把 note 升級成決策卡（Strategy Extractor）

**Skill：** `design-strategy-extractor`

從既有 `docs/*.note.md` 萃取 **Decision Pattern 決策卡**（problem → solution → reason → applicable_when → **evidence**），寫入 `docs/<brand_id>.decisions.yaml`，再以 `compile_knowledge_graph.py` 編譯成全域圖譜。

### 怎麼觸發

```text
用 design-strategy-extractor 處理 docs 裡還沒有 decisions.yaml 的幾份，優先補 knowledge_graph_report.md 的 backlog。
```

### strict evidence

每張決策卡至少一筆 evidence，且 `chapter` 必須是該 `brand_id` 的 `index.yaml` 中真實章節；找不到證據就不寫卡。編譯時會驗證並把無效 evidence 列入報告。

### Coach vs Researcher vs Extractor

|      | Coach                     | Researcher           | Strategy Extractor                      |
| ---- | ------------------------- | -------------------- | --------------------------------------- |
| 輸入 | 客戶 brief + 知識圖譜     | 既有 PDF             | `note.md` + `index.yaml`                |
| 輸出 | `clients/` guideline 初稿 | `docs/` index + note | `docs/*.decisions.yaml` + 回填 industry |
| 角色 | 推理與產出                | 反向工程分析         | 把「為什麼」結構化成決策卡              |

---

## 原理與架構

### 核心假設

高階設計師規劃 guideline 時，並非從空白列章節，而是依序決策：

**組織情境 → Guideline 原型 → 必要模組 → 章節順序 → 規則粒度**

128 份已分析 guideline 是這套隱性邏輯的實證樣本。AGI 將其 **形式化** 為 archetype、module graph 與 profile 語料，供 Coach 推理與引用先例。

### 文件層資料模型（`docs/`）

| 層         | 檔案                         | 職責                                                              |
| ---------- | ---------------------------- | ----------------------------------------------------------------- |
| **結構層** | `docs/<name>.index.yaml`     | 章節 ID、標題、層級、順序、pages、事實摘要                        |
| **研究層** | `docs/<name>.note.md`        | 十一維反向工程分析（Researcher 產出）                             |
| **聚合層** | `docs/<name>.profile.yaml`   | modules、depth、archetype、frameworks 等跨語料欄位                |
| **決策層** | `docs/<name>.decisions.yaml` | problem→solution→reason 決策卡（Extractor 產出，strict evidence） |

### 知識圖譜七層堆疊（下層是事實、上層是推理）

| 層     | 名稱                     | 檔案                                                        | 說明                                    |
| ------ | ------------------------ | ----------------------------------------------------------- | --------------------------------------- |
| **L0** | Evidence 證據層          | `sources/*.pdf` + `docs/*.index.yaml`                       | 絕不發明的地基                          |
| **L1** | Structure 結構層         | `docs/*.profile.yaml`                                       | 章節序列、模組覆蓋                      |
| **L2** | Module 固定知識層        | `research/modules/*.yaml`                                   | 模組為何存在 + `driven_by` 決策驅動映射 |
| **L3** | Decision Patterns 決策層 | `docs/*.decisions.yaml` → `research/decision_patterns.yaml` | 決策卡（含證據、信心）                  |
| **L4** | Context 情境知識層       | `research/contexts/{industries,brand_types}.yaml`           | 產業／品牌類型 → 模組／決策卡           |
| **L5** | Blueprint 原型層         | `research/archetypes.yaml`                                  | 哪些組合構成一致的 guideline            |
| **L6** | Reasoning 推理層         | `agi`                                                       | 客戶資料 → 推薦的決策鏈                 |

**固定知識 vs 情境知識**：固定模組（Typography、Color、Logo、Governance、Accessibility）幾乎都要有，但其「方向與規格傾向」由 L2 的 `driven_by` 從策略決策推導；情境模組（新能源 → Story Framework；金融 → Trust／Governance；奢侈 → Craftsmanship／Heritage）由 L4 與 L3 命中的決策卡帶入。

```text
sources/*.pdf ─ Researcher ─► index.yaml + note.md
                                   │
                  ┌────────────────┼─────────────────┐
        generate_profiles.py            Strategy Extractor
                  ▼                             ▼
            profile.yaml                 decisions.yaml（strict evidence）
                  │                             │
       assign_archetypes / corpus      compile_knowledge_graph.py
                  ▼                             ▼
        research/archetypes.yaml      research/decision_patterns.yaml
        research/contexts/*.yaml      （by_industry/brand_type/module/signal 索引）
        research/modules/*.yaml                │
                  └──────────────┬─────────────┘
                                 ▼
                  Coach（客戶 brief → 知識圖譜推理 → Plan）
                                 ▼
                        clients/<slug>/（guideline 初稿）
```

### Guideline 原型（7 種 Archetype）

定義見 [`research/archetypes.yaml`](research/archetypes.yaml)。Coach 依 brief 推薦原型並引用同類先例：

| ID                         | 名稱               | 典型情境                              |
| -------------------------- | ------------------ | ------------------------------------- |
| `brand_experience_guide`   | 標準品牌體驗指南   | 多數單一品牌企業手冊（預設）          |
| `full_brand_system`        | 完整消費者品牌系統 | 策略前置、章節完整（如 LucidMotors）  |
| `corporate_toolkit`        | 企業品牌工具包     | 扁平、執行導向（如 AMD）              |
| `multi_brand_architecture` | 多品牌架構         | 母子公司、聯名（如 World Bank Group） |
| `product_design_system`    | 產品設計系統       | UI、token、元件                       |
| `logo_asset_guidelines`    | Logo 資產聚焦      | 合作夥伴、媒體用精簡規範              |
| `campaign_touchpoint`      | 活動／通路觸點     | 單一 campaign、動態識別               |

### 專案結構

```text
AGI/
├── README.md
├── MAINTENANCE.md             # 安裝、原理與架構、維護腳本
├── sources/                   # 原始 PDF（本機，不入 git）
├── docs/                      # 128+ 份已分析 guideline（index/note/profile/decisions）
├── clients/                   # Coach 產出的新客戶專案
├── research/
│   ├── schemas/               # decision_pattern / module_knowledge / context schema
│   ├── modules/               # L2 固定知識（含 driven_by）
│   ├── contexts/              # L4 industries.yaml、brand_types.yaml
│   ├── decision_patterns.yaml # L3 編譯後全域決策圖譜（自動產生）
│   ├── archetypes.yaml / module_graph.yaml / intake_schema.yaml
│   └── corpus_report.md / knowledge_graph_report.md
├── scripts/                   # profile、語料統計、知識圖譜編譯
└── .cursor/skills/
    ├── agi/        # 新客戶規劃（AGI）
    ├── design-guideline-researcher/   # 既有 PDF 分析
    └── design-strategy-extractor/     # note → 決策卡
```

### 研究層文件

| 檔案                                                                                                                                | 用途                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`research/decision_patterns.yaml`](research/decision_patterns.yaml)                                                                | **L3 決策圖譜**（自動產生）+ 反向索引            |
| [`research/contexts/industries.yaml`](research/contexts/industries.yaml) / [`brand_types.yaml`](research/contexts/brand_types.yaml) | **L4 情境知識**：產業／品牌類型 → 模組／決策卡   |
| [`research/modules/`](research/modules/)                                                                                            | **L2 固定知識**：模組目的 + `driven_by` 決策驅動 |
| [`research/schemas/`](research/schemas/)                                                                                            | 決策卡、模組知識、情境的 schema                  |
| [`research/archetypes.yaml`](research/archetypes.yaml)                                                                              | 原型定義、must-have 模組、分類規則               |
| [`research/module_graph.yaml`](research/module_graph.yaml)                                                                          | 模組依賴、Coach 跳步挑戰規則                     |
| [`research/intake_schema.yaml`](research/intake_schema.yaml)                                                                        | 客戶 brief 欄位 → archetype 映射                 |
| [`research/corpus_report.md`](research/corpus_report.md)                                                                            | 128 份語料統計                                   |
| [`research/knowledge_graph_report.md`](research/knowledge_graph_report.md)                                                          | 決策圖譜統計、無效 evidence、待萃取 backlog      |

語料摘要：高頻模組為 Governance、Visual Identity、Color System、Typography System；約 77% 為 `brand_experience_guide` 原型。

### 參考先例

| 原型         | 範例 `brand_id`                                           | 結構特徵                     |
| ------------ | --------------------------------------------------------- | ---------------------------- |
| 企業工具包   | `AMD_branding_guidelines_2020`                            | 1 大章 + 9 小節              |
| 完整品牌系統 | `Dubai_BRAND_GUIDELINES_2021`                             | 10 大章，策略→視覺→語氣→治理 |
| 多品牌架構   | `WouldBankGroup_Branding_Visual_Identity_Guidelines_2016` | 架構 + 聯名治理              |
| 標準品牌指南 | `Slack-Brand-Guidelines`                                  | 中等章節、視覺與治理完整     |
| Logo 聚焦    | `Tripadvisor_Logo_Guidelines_2020`                        | 章節精簡、資產導向           |

### 設計原則與限制

- **不發明規則**：PDF 不可讀時停止並告知需 OCR；Coach 未知色值／尺寸標 `TBD`
- **不抄襲先例**：只複用結構與 framework，不複製 HEX、標語、尺寸
- **增量處理**：Researcher 對完整輸出預設不覆蓋，除非明確要求重產
- **Git**：`sources/` 不入庫；`docs/`、`clients/`、`research/` 可入庫

---

## 維護腳本

```bash
python scripts/generate_profiles.py
python scripts/assign_archetypes.py
python scripts/generate_corpus_report.py
python scripts/compile_knowledge_graph.py   # 編譯 L3 決策圖譜 + 驗證 evidence
python scripts/apply_taiwan_zh_terms.py      # 依台灣繁體用語對照表修正中文
```

建議順序：更新 `note.md` 後依序執行 profile/archetype/corpus；新增或修改 `docs/*.decisions.yaml` 後執行 `compile_knowledge_graph.py`（會 strict 驗證每筆 evidence、合併同名決策卡並重建反向索引）。調整原型規則時改 `research/archetypes.yaml` 後重跑 `assign_archetypes.py`。

---

## 延伸方向

- 用 Extractor 增量清空 `knowledge_graph_report.md` 的 backlog，把 128 份全數萃成決策卡
- 回填全部 `profile.industry` 標籤（Extractor 可順帶處理），強化 L4 情境推理
- 專家驗證 archetype 與 industry/brand_type 邊界
- 決策卡之間的 `conflicts_with` 與一致性檢查
- 與 Figma、design token 工具整合；語意檢索（RAG）覆蓋決策卡 evidence

---

## Skill 路徑速查

| 用途                                 | Skill                                                 |
| ------------------------------------ | ----------------------------------------------------- |
| 新客戶規劃 guideline（知識圖譜推理） | `.cursor/skills/agi/SKILL.md`                         |
| 分析既有 PDF                         | `.cursor/skills/design-guideline-researcher/SKILL.md` |
| 把 note 升級成決策卡                 | `.cursor/skills/design-strategy-extractor/SKILL.md`   |

在 Agent 中以自然語言觸發即可；Agent 會依 description 自動選用對應 skill。

# AGI Corpus Report

產生日期：2026-06-18
語料規模：128 份 guideline profile
資料來源：`docs/*.profile.yaml`
產生命令：`python scripts/generate_corpus_report.py`

## 摘要

- 平均每份 guideline 涵蓋 **13.9** 個模組類型、**11.2** 個 framework 條目、**14.0** 個 pattern 條目。
- 平均每份有 **8.3** 條可量化／AI-checkable rules；**121** 份（94.5%）至少有一條。
- 平均 **7.7** 個小節（level-2）；大章數最常見為 **6** 個。
- `archetype` 已填：**128** 份；`industry` 已填：**0** 份。

### Archetype 分布

| archetype | 份數 | 佔比 |
|-----------|------|------|
| brand_experience_guide | 98 | 76.6% |
| full_brand_system | 13 | 10.2% |
| product_design_system | 7 | 5.5% |
| multi_brand_architecture | 4 | 3.1% |
| corporate_toolkit | 3 | 2.3% |
| logo_asset_guidelines | 2 | 1.6% |
| campaign_touchpoint | 1 | 0.8% |

定義見 `research/archetypes.yaml`；分類：`python scripts/assign_archetypes.py`。

---

## 1. 模組出現頻率（文件級）

每份 profile 的 `modules` 欄位（來自 note Abstraction 正規化）。

| 模組 | 出現份數 | 佔比 | 分佈 |
|------|----------|------|------|
| Governance | 116 | 90.6% | `████████████████████` |
| AI-Checkable Rules | 114 | 89.1% | `████████████████████` |
| Visual Identity | 112 | 87.5% | `███████████████████░` |
| Operations | 111 | 86.7% | `███████████████████░` |
| Color System | 102 | 79.7% | `██████████████████░░` |
| Typography System | 101 | 78.9% | `█████████████████░░░` |
| Brand Strategy | 88 | 68.8% | `███████████████░░░░░` |
| Layout System | 88 | 68.8% | `███████████████░░░░░` |
| Design Tokens | 78 | 60.9% | `█████████████░░░░░░░` |
| Content Design | 77 | 60.2% | `█████████████░░░░░░░` |
| Legal and Trademark | 69 | 53.9% | `████████████░░░░░░░░` |
| Photography System | 66 | 51.6% | `███████████░░░░░░░░░` |
| Messaging | 61 | 47.7% | `███████████░░░░░░░░░` |
| Knowledge Architecture | 58 | 45.3% | `██████████░░░░░░░░░░` |
| Visual Language | 55 | 43.0% | `█████████░░░░░░░░░░░` |
| Voice and Tone | 53 | 41.4% | `█████████░░░░░░░░░░░` |
| Brand Architecture | 48 | 37.5% | `████████░░░░░░░░░░░░` |
| Compliance | 48 | 37.5% | `████████░░░░░░░░░░░░` |
| Examples | 41 | 32.0% | `███████░░░░░░░░░░░░░` |
| Accessibility | 39 | 30.5% | `███████░░░░░░░░░░░░░` |
| Iconography System | 29 | 22.7% | `█████░░░░░░░░░░░░░░░` |
| Information Design | 28 | 21.9% | `█████░░░░░░░░░░░░░░░` |
| Product Language | 26 | 20.3% | `████░░░░░░░░░░░░░░░░` |
| Content Safety | 26 | 20.3% | `████░░░░░░░░░░░░░░░░` |
| Motion Identity | 25 | 19.5% | `████░░░░░░░░░░░░░░░░` |
| UI Components | 24 | 18.8% | `████░░░░░░░░░░░░░░░░` |
| Localization | 23 | 18.0% | `████░░░░░░░░░░░░░░░░` |
| Illustration System | 17 | 13.3% | `███░░░░░░░░░░░░░░░░░` |
| Measurement | 14 | 10.9% | `██░░░░░░░░░░░░░░░░░░` |
| Data Visualization | 11 | 8.6% | `██░░░░░░░░░░░░░░░░░░` |
| Interaction Design | 10 | 7.8% | `██░░░░░░░░░░░░░░░░░░` |
| Design Process | 9 | 7.0% | `██░░░░░░░░░░░░░░░░░░` |
| Evaluation Framework | 2 | 1.6% | `░░░░░░░░░░░░░░░░░░░░` |
| Internationalization | 1 | 0.8% | `░░░░░░░░░░░░░░░░░░░░` |
| Brand Touchpoint Governance | 1 | 0.8% | `░░░░░░░░░░░░░░░░░░░░` |
| Communication Framework | 1 | 0.8% | `░░░░░░░░░░░░░░░░░░░░` |
| Publication Design | 1 | 0.8% | `░░░░░░░░░░░░░░░░░░░░` |
| Partnership Branding | 1 | 0.8% | `░░░░░░░░░░░░░░░░░░░░` |

### 模組共現（前 15 對）

同一文件內同時出現的模組對，供 module_graph 初稿參考。

| 模組 A | 模組 B | 共現份數 |
|--------|--------|----------|
| Governance | Operations | 108 |
| AI-Checkable Rules | Governance | 107 |
| Governance | Visual Identity | 104 |
| AI-Checkable Rules | Visual Identity | 102 |
| AI-Checkable Rules | Operations | 101 |
| Operations | Visual Identity | 100 |
| Color System | Typography System | 94 |
| Color System | Governance | 93 |
| Color System | Visual Identity | 93 |
| AI-Checkable Rules | Color System | 93 |
| Governance | Typography System | 92 |
| Operations | Typography System | 92 |
| Typography System | Visual Identity | 91 |
| AI-Checkable Rules | Typography System | 91 |
| Color System | Operations | 91 |

---

## 2. 深度指標分布（depth）

### strategy / visual / governance

| 維度 | low | medium | high |
|------|-----|--------|------|
| strategy | 32 (25.0%) | 81 (63.3%) | 15 (11.7%) |
| visual | 2 (1.6%) | 21 (16.4%) | 105 (82.0%) |
| governance | 7 (5.5%) | 43 (33.6%) | 78 (60.9%) |

### 大章數（top_level_chapter_count）

| 大章數 | 份數 | 佔比 |
|--------|------|------|
| 1 | 1 | 0.8% |
| 2 | 2 | 1.6% |
| 3 | 10 | 7.8% |
| 4 | 18 | 14.1% |
| 5 | 18 | 14.1% |
| 6 | 24 | 18.8% |
| 7 | 12 | 9.4% |
| 8 | 21 | 16.4% |
| 9 | 8 | 6.2% |
| 10 | 7 | 5.5% |
| 11 | 3 | 2.3% |
| 12 | 2 | 1.6% |
| 13 | 1 | 0.8% |
| 14 | 1 | 0.8% |

### 小節數分布（section_count）

- 最小：0
- 最大：45
- 平均：7.7
- 中位數：6

---

## 3. 章節順序模式

### 啟發式分類

| 模式 | 份數 | 佔比 | 說明 |
|------|------|------|------|
| strategy_first | 54 | 42.2% | 首章含策略關鍵字或 strategy depth=high |
| toolkit_flat | 1 | 0.8% | ≤2 大章且小節多（類 AMD 扁平工具包） |
| assets_first | 73 | 57.0% | 視覺／資產章節前置 |
| unknown | 0 | 0.0% | 無法判斷 |

### 常見大章順序（前 10）

| 次數 | 大章順序（前 5 章） |
|------|---------------------|
| 1 | History & Mission → Our Story → Logo Usage → Color Palette → Typography & Language |
| 1 | Our Brand → Our New Visual Identity → Putting It All Together → Contact → Color Appendix |
| 1 | User Guide → Fundamentals → Stationery & Office Applications |
| 1 | Background → Introduction → The Accoya Identity → The Accoya Icons → Type and Straplines |
| 1 | Brand Foundation → Brand Elements → Best Practices |
| 1 | Visual Elements Overview → Logo System → Logo and Tagline → Colour System |
| 1 | Overview → Call To Action and Messaging → Logos and Imagery → Colors → Technical Specs and More |
| 1 | Guide Purpose and Review Process → Amazon Echo Guidelines → Alexa Guidelines |
| 1 | AMD Branding Guidelines |
| 1 | Essential Visual Identity Elements → Photography and Relationship Device → Card Art in Marketing → Brand Review Governance |

---

## 4. Framework 統計

### 高頻 framework 名稱（正規化後，前 20）

| Framework | 出現次數 |
|-----------|----------|
| 以元素、條件、限制與範例組成小型決策框架 | 41 |
| 可抽象為「核心資產 -> 使用條件 -> 例外處理 -> 錯誤排除 -> 應用驗證」框架，讓設... | 33 |
| 使用情境式決策框架 | 13 |
| Trademark compliance framework | 2 |
| asset governance framework | 2 |
| identity toolkit framework | 2 |
| logo governance framework | 2 |
| application proof framework | 2 |
| logo-derived spacing system | 2 |
| mission-to-identity framework | 2 |
| Palette hierarchy | 2 |
| Violation taxonomy | 2 |
| Template framework | 2 |
| typography framework | 2 |
| 此章形成 History -> International Mission -> Event ... | 1 |
| Problem -> Action -> Movement 的歷史框架 | 1 |
| Mission Alignment 框架 | 1 |
| Athlete Creation -> Professional Synthesis -> U... | 1 |
| Collaborative Identity Process | 1 |
| Asset Hierarchy 框架 | 1 |

### Framework 共現（同文件內，前 10 對）

| Framework A | Framework B | 共現次數 |
|-------------|-------------|----------|
| 以元素、條件、限制與範例組成小型決策框架 | 以元素、條件、限制與範例組成小型決策框架 | 230 |
| 以元素、條件、限制與範例組成小型決策框架 | 使用情境式決策框架 | 182 |
| 可抽象為「核心資產 -> 使用條件 -> 例外處理 -> 錯誤排除 -> 應用驗證」框架，讓設... | 可抽象為「核心資產 -> 使用條件 -> 例外處理 -> 錯誤排除 -> 應用驗證」框架，讓設... | 98 |
| 使用情境式決策框架 | 使用情境式決策框架 | 78 |
| 以使命/目標/行為/工具的四層框架運作 | 以元素、條件、限制與範例組成小型決策框架 | 14 |
| 以元素、條件、限制與範例組成小型決策框架 | 形成 science translation framework | 14 |
| 以元素、條件、限制與範例組成小型決策框架 | 採用 ingredient framework | 14 |
| 三元素平衡框架 | 以元素、條件、限制與範例組成小型決策框架 | 14 |
| 以元素、條件、限制與範例組成小型決策框架 | 採用 broadcast component framework | 14 |
| 以元素、條件、限制與範例組成小型決策框架 | 採用 touchpoint template framework | 14 |

---

## 5. Pattern 統計

高頻可複用 pattern 名稱（前 25）：

| Pattern | 出現次數 |
|---------|----------|
| 子系統規範頁 | 41 |
| 可重複使用的模式包括最小尺寸、留白單位、色彩角色、字體層級、背景相容性、範本化應用與 do/don’t 對照。 | 33 |
| 可複用為政府與大型公共服務品牌的 modular brand manual：核心識別、共同品牌、應用模板、特殊關係分層管理。 | 13 |
| minimum size | 4 |
| do-not examples | 2 |
| system fallback | 2 |
| 語氣人格化 | 2 |
| 字體角色分層 | 2 |
| color don'ts | 2 |
| benefit ladder | 2 |
| 可複用模式是 mission-led event branding：先說明運動起源，再定義本次活動如何承接該使命。 | 1 |
| 可複用模式是 founder-action story，用一個可理解的起點承載大型公益組織的使命。 | 1 |
| 可複用模式是母品牌使命與事件使命並列，適合大型活動、非營利組織與 chapter-based brand。 | 1 |
| co-created identity | 1 |
| origin story before usage rules | 1 |
| logo as participation evidence | 1 |
| 可複用模式是把設計 workshop 記錄變成 guideline 的品牌故事材料。 | 1 |
| hero mark | 1 |
| source marks | 1 |
| special-use clearance | 1 |
| approval gate | 1 |
| logo variant matrix | 1 |
| clear-space unit | 1 |
| partner lockup rule | 1 |
| hashtag governance | 1 |

---

## 6. AI-Checkable Rules

- 有 quantifiable rules 的文件：**121** / 128（94.5%）
- 平均每份 rules 條數：**8.3**
- 最多 rules 的份數：**27**

---

## 7. 啟發式原型建議（第二階段 archetype 參考）

以下為演算法建議，**非最終 archetype 分類**；第二階段需專家標註與 `archetypes.yaml` 定稿。

| 建議原型 | 份數 | 佔比 | 典型特徵 |
|----------|------|------|----------|
| corporate_toolkit | 1 | 0.8% | 扁平、≤2 大章、小節多 |
| full_brand_system | 9 | 7.0% | strategy 高、大章多 |
| multi_brand | 48 | 37.5% | 含 Brand Architecture 等 |
| design_system | 46 | 35.9% | UI/元件/token 模組 |
| logo_or_channel_focus | 3 | 2.3% | 章節少、聚焦 |
| general_brand | 21 | 16.4% | 其餘 |

### 參考先例

| 原型參考 | brand_id | top_level | sections | strategy | visual | governance |
|----------|----------|-----------|----------|----------|--------|------------|
| corporate_toolkit | AMD_branding_guidelines_2020 | 1 | 9 | medium | high | high |
| full_brand_system | LucidMotors | 7 | 45 | high | high | medium |
| multi_brand | WouldBankGroup_Branding_Visual_Identity_Guidelines_2016 | 6 | 19 | medium | medium | medium |
| design_system | Slack-Brand-Guidelines | 3 | 7 | medium | high | high |

---

## 8. 對第二階段的建議

1. **Archetype 定義**：已完成 `research/archetypes.yaml`；profile 已回填 archetype。
2. **Module graph**：§1 模組共現 + note 的 Relationship 可合併為 `research/module_graph.yaml`。
3. **章節順序**：§3 常見大章順序可作各原型的 `typical_chapter_sequence` 初稿。
4. **Industry**：本報告未含產業維度；建議 archetype 定稿後抽樣手標 30 份 `industry`。
5. **品質**：rules 抽取為啟發式；corpus 中部分 rules 為描述性句子，Coach 產出時需再篩選真正可量化規則。

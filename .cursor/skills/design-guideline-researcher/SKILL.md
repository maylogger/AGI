---
name: design-guideline-researcher
description: 當使用者想把 brand、design、identity、product、UI、content、voice、marketing 或 design-system guideline PDF 轉成可重複使用的 Agentic Guideline Intelligence 時使用此 skill。此 skill 會從 sources/ 讀取 PDF，輸出 docs/<PDF-name>.index.yaml 與 docs/<PDF-name>.note.md；會跳過已完成的輸出以節省 token，並將 note.md 寫成 Design Infrastructure Researcher 的反向工程分析，而不是一般摘要。適用於整理 guideline 章節、從 PDF 建立 docs、分析 guideline 為什麼被設計成這樣、或建立設計知識庫。
---

# Design Guideline Researcher

使用此 skill 將設計相關 guideline PDF 轉換成結構化知識檔。

目標不只是抽出目錄，而是理解這份 guideline 為什麼被設計成這樣、作者如何把抽象的品牌或設計意圖轉成可執行規範，以及哪些知識可以被抽象為可重複使用的 design infrastructure knowledge。

## 台灣繁體正體用語

撰寫 `note.md`、`index.yaml` summary 與所有中文說明時，須遵循 [`.cursor/rules/taiwan-traditional-chinese.mdc`](../../rules/taiwan-traditional-chinese.mdc)：

- 使用台灣繁體正體常見說法，避免大陸慣用詞
- 對照表目前重點：**合規** → **規定**（不合規 → 不符合規定）、**智能** → **智慧**
- 對照表未列詞彙仍須以台灣語感判斷

## 預期專案結構

預設輸入與輸出路徑：

```text
sources/
  Example_Guideline.pdf
docs/
  Example_Guideline.index.yaml   # 結構層：章節樹
  Example_Guideline.note.md      # 研究層：十一維分析
  Example_Guideline.profile.yaml # 聚合層：跨語料可查詢欄位（可選，見 scripts/generate_profiles.py）
```

如果使用者提供不同路徑，使用使用者指定的路徑；否則預設：

- 來源 PDF 放在 `sources/`。
- 輸出檔案放在 `docs/`。
- 每份 PDF 對應到 `docs/<PDF 檔名不含副檔名>.index.yaml` 與 `docs/<PDF 檔名不含副檔名>.note.md`。
- 聚合層 `docs/<PDF-name>.profile.yaml` 由 `python scripts/generate_profiles.py` 從 index + note 產生，供跨品牌統計與 Agent 檢索；schema 見 `research/profile.schema.yaml`。

## 增量處理

在讀取或重新處理 PDF 前，先檢查目標輸出是否已存在：

- `docs/<PDF-name>.index.yaml`
- `docs/<PDF-name>.note.md`

如果兩個檔案看起來都完整，跳過該 PDF。這能節省 token，也避免覆蓋既有研究成果。

當 `index.yaml` 包含以下內容時，視為完整：

- `title`
- `source`
- `chapters`
- 章節要點包含 `id`、`title`、`level`、`order`，並具備 `summary` 或可用的子節點

當 `note.md` 包含以下內容時，視為完整：

- `Research Intent`
- `Design Infrastructure Researcher` 研究視角
- 下列十一個分析要點：
  - `Chapter Purpose`
  - `Definition`
  - `Relationship`
  - `Design Execution`
  - `Principles`
  - `Frameworks`
  - `Patterns`
  - `Rules`
  - `Reusable Knowledge`
  - `Abstraction`
  - `Visual Evidence`

只有在以下情況才重新處理：

- 使用者明確要求重新產生
- 未發現必要檔案
- `index.yaml` 沒有可用章節結構
- `note.md` 仍是摘要型筆記，而不是研究分析型筆記
- 來源 PDF 比既有輸出檔更新

如果 `index.yaml` 完整，但沒有 `note.md` 或內容仍是摘要型，重用既有 `index.yaml`，只重寫 `note.md`。除非章節結構不足，否則避免重新讀取整份 PDF。

## 工作流程

1. **尋找來源 PDF**
   - 除非使用者指定其他資料夾，否則從 `sources/` 尋找 PDF。
   - 將每個 `file.pdf` 對應到 `docs/file.index.yaml` 與 `docs/file.note.md`。

2. **檢查既有輸出**
   - 讀取 PDF 前先套用增量處理規則。
   - 簡短回報哪些 PDF 被跳過。

3. **抽取文字並判斷是否需要 OCR**
   - 盡可能直接讀取 PDF 文字。
   - 如果 PDF 是掃描檔或文字抽取結果不可用，停止處理該 PDF 並告知使用者需要 OCR。不要從不可讀頁面憑空編造章節分析。

4. **建立章節結構**
   - 若 PDF 有目錄，優先使用目錄。
   - 若沒有目錄，從標題模式、頁面標籤、重複出現的 section header 與版面文字推斷章節。
   - 預設以大章與主要小節作為分析單元。
   - 避免把小標籤、圖說或裝飾性標題切得過細。

5. **寫入 `index.yaml`**
   - 保存機器可讀的章節結構。
   - `summary` 保持短、事實性、可掃描。

6. **寫入 `note.md`**
   - 除非使用者要求其他語言，否則使用繁體中文。
   - 不要把主要任務做成 guideline 摘要。
   - 從 Design Infrastructure Researcher 視角分析。
   - 對每個大章與主要小節回答下方十一個分析要點。

7. **驗證**
   - 確認 `index.yaml` 具備必要 key。
   - 確認 `note.md` 對每個目標分析單元都包含十一個要點。
   - 檢查 Markdown 標題階層。
   - 除非使用者明確要求，不要修改無關檔案或 plan 檔。

## `index.yaml` 格式

使用以下結構：

```yaml
title: '文件標題'
source: 'sources/Example_Guideline.pdf'
version: '可選版本'
date: '可選日期'
language: '可選語言代碼'
summary: '用繁體中文簡短描述這份文件的角色。'
chapters:
  - id: 'ch-01'
    title: '章節標題'
    level: 1
    order: 1
    pages: '1-5'
    summary: '短而事實性的章節摘要。'
    children:
      - id: 'ch-01-01'
        title: '小節標題'
        level: 2
        order: 1
        pages: '2'
        summary: '短而事實性的小節摘要。'
```

撰寫指引：

- 使用穩定 ID，例如 `ch-01`、`ch-01-01`。
- 有頁碼時使用 `pages`；只有在必要時才省略或使用 `unknown`。
- `summary` 保持事實性；深度研究分析放在 `note.md`。
- 含有標點、apostrophe、類似冒號的文字或特殊符號時，字串請加引號。

## `note.md` 格式

開頭使用：

```markdown
# [Document Title]

來源：`sources/Example_Guideline.pdf`
版本：[version if known]
日期：[date if known]
研究視角：Design Infrastructure Researcher

## Research Intent

這份筆記不摘要原始 Guideline，也不只重列章節。它從 Guideline 作者的角度反向推導：這份文件為什麼被設計成這樣、它如何把品牌理念轉化成可執行規範，以及哪些知識可以抽象成通用 Agentic Guideline Intelligence。
```

接著分析每個大章與主要小節：

```markdown
## [Top-Level Chapter]

1. **Chapter Purpose**：為什麼需要這個章節？它解決什麼問題？如果沒有它會發生什麼事？
2. **Definition**：這個章節在 Guideline 中定義什麼？邊界在哪裡？它不負責什麼？
3. **Relationship**：它如何延續上層章節？依賴哪些前置資訊？影響哪些後續章節？在整體架構中扮演什麼角色？
4. **Design Execution**：作者如何透過設計達成目的？使用哪些方法、機制或策略？如何把抽象理念轉成規範？
5. **Principles**：隱含哪些設計原則？作者相信什麼？背後的設計哲學是什麼？
6. **Frameworks**：是否存在決策框架、溝通框架或系統架構？該框架如何運作？
7. **Patterns**：是否存在可重複使用的設計模式？哪些模式可被其他品牌或產品複用？
8. **Rules**：有哪些明確規範？哪些可量化、驗證或交由 AI 執行？
9. **Reusable Knowledge**：哪些知識與品牌本身無關？哪些值得納入通用 Agentic Guideline Intelligence？
10. **Abstraction**：抽象化後，它屬於哪種類型的 Guideline 模組？
11. **Visual Evidence**：這個章節是否大量使用圖片、圖示、範例版面或視覺對照來說明？這些圖片大概呈現哪些內容？它們在章節中承擔示範、比較、警示、流程、比例、情境或治理證據中的哪種功能？

### [Major Section]

1. **Chapter Purpose**：...
   ...
10. **Abstraction**：...
11. **Visual Evidence**：...
```

## 分析立場

以 Design Infrastructure Researcher 身分工作：

- 反向推導 guideline 作者的設計意圖。
- 解釋章節為什麼存在，而不只是說明它寫了什麼。
- 區分 strategy、system、rule、example、governance、operations。
- 找出決策框架與可重複使用的設計模式。
- 盡可能把具體規範轉成 AI-checkable criteria。
- 抽出與單一品牌無關、可納入 Agentic Guideline Intelligence 的知識。

避免：

- 把一般摘要當成主要輸出
- 大段複製 PDF 原文
- 把裝飾性頁面標籤當成有意義章節
- 在來源模糊時自行發明規則
- 沒有理由就覆蓋已完成的既有輸出

## Module taxonomy

在 `Abstraction` 中可使用下列分類，但不要硬套。若某個章節屬於清單之外的模組類型，建立更準確的分類，並簡短說明原因。

常見分類：

- `Brand Strategy`
- `Messaging`
- `Content Design`
- `Voice and Tone`
- `Visual Identity`
- `Visual Language`
- `Color System`
- `Typography System`
- `Layout System`
- `Interaction Design`
- `UI Components`
- `Design Tokens`
- `Photography System`
- `Illustration System`
- `Iconography System`
- `Motion Identity`
- `Product Language`
- `Information Design`
- `Data Visualization`
- `Accessibility`
- `Localization`
- `Governance`
- `Operations`
- `Design Process`
- `Compliance`
- `Legal and Trademark`
- `Content Safety`
- `Measurement`
- `AI-Checkable Rules`
- `Examples`
- `Knowledge Architecture`
- `Other`

當章節橫跨多種角色時，可以使用多個分類。

## 品質檢查清單

完成前檢查：

- 每份已處理 PDF 都有 `docs/<PDF-name>.index.yaml`。
- 每份已處理 PDF 都有 `docs/<PDF-name>.note.md`。
- 除非使用者要求重新產生，完整既有檔案已被跳過。
- `index.yaml` 結構清楚、簡潔、機器可讀。
- `note.md` 包含 `Research Intent`。
- `note.md` 對每個選定分析單元使用十一個分析要點。
- `Rules` 在可行時包含可量化或 AI-checkable 的判準。
- `Reusable Knowledge` 抽出與單一品牌無關的知識。
- `Abstraction` 指派 guideline module type。
- 最終回覆摘要列出已處理、已跳過與受阻的 PDF。

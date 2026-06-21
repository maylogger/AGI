# AGI — Agentic Guideline Intelligence

本專案從上百份國際品牌 Design Guideline 蒸餾成可檢索、可統計、**可推理** 的 Design Guideline 知識圖譜，主要使用 **agi** Skill：直接協助 **新客戶** 規劃並產生接近完整版的 Design Guideline 具體建議初稿。

本專案不是傳統 Web 應用，而是 **內容庫 + Skills + 研究層 YAML**；能力來自 Agent 讀取使用者 brief 並依 Skill 規範產出檔案。

本專案製作的核心目標不是「學其他品牌長什麼樣」，而是「學品牌 **為什麼** 長這樣」：從 128 份語料抽取設計決策知識 → 建立知識圖譜 → AI 推理 → 為新客戶產生合適的 Design Guideline 架構與初稿。所有推薦都連回真實先例證據，不幻覺不自幹。

知識庫是如何被建立與維護的、安裝、原理與架構，請見 [MAINTENANCE.md](MAINTENANCE.md)。一般使用者可以直接看使用方法即可：

---

## 為新客戶規劃 Design Guideline

**Skill：** `agi`  
路徑：`.cursor/skills/agi/SKILL.md`

> 建議：CLAUDE CODE 使用者可以請 CLAUDE 轉為 CLAUDE SKILL 格式。

使用 Agent 模擬世界頂尖高階設計師的決策順序：先理解客戶情境，再推薦 Guideline 原型與章節結構，引用 AGI 中 128 份國際品牌指南的 **結構與邏輯**，最後產出接近可交付的 Design Guideline 初稿。

### 開始設計，起手 Prompt

在 Agent 對話中說：

```text
幫新客戶規劃 Design Guideline
```

或帶更多背景：

```text
請用 Agentic Guideline Intelligence，幫一家 B2B 科技公司規劃全新 Brand Guideline。
單一品牌、主要數位與簡報、有品牌負責人、要做完整手冊。
```

### 設計過程三階段

| 階段          | 你做什麼                     | Agent 做什麼                                                      |
| ------------- | ---------------------------- | ----------------------------------------------------------------- |
| **1. Intake** | 逐題回答                     | **一次只問一題**；問完 intake 與延伸問題；**不寫** guideline 檔案 |
| **2. Plan**   | 閱讀並回覆「確認」或指出修改 | **一次** 呈現完整規劃 Plan（原型、模組、章節、先例、TBD）         |
| **3. Build**  | 確認後產出                   | 寫入 `clients/<客戶名稱>/` 全套檔案                               |

### 輸出位置

```text
clients/<客戶名稱資料夾>/
  plan.md               # Plan
  intake.yaml           # 結構化 brief
  blueprint.yaml        # 原型、模組、章節計畫、先例 ID
  coach_session.md      # 問答與決策紀錄
  <客戶名稱資料夾>.index.yaml
  <客戶名稱資料夾>.note.md # Design Guideline 初稿在此
```

### 繼續未完成專案

假設你上次做一半，那麼可以用這個指令繼續：

```text
繼續 clients/acme-corp 的 Guideline，補 Color 和 Typography 章
```

### 其他 Prompt 示範：

| 情境          | 提示語範例                                   |
| ------------- | -------------------------------------------- |
| 多品牌 / 聯名 | 「多品牌金融集團，要 co-branding」           |
| 僅 logo 規範  | 「合作夥伴用的 logo 資產指南，章節精簡」     |
| 跨國企業      | 「國際資安老牌大廠，有三個子品牌需要打造」   |
| 產品          | 「SaaS 產品，要含 design system 與 token」   |
| 懶人模式      | 「直接協助我生出品牌策略，設計按照策略安排」 |

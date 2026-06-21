# Starling Bank Brand Guidelines

來源：`sources/starling_bank_brand_guidelines.pdf`
版本：2.1
研究視角：Design Infrastructure Researcher

## Summary

這份文件是 Starling Bank 針對線上使用情境的精簡品牌規範，聚焦於標誌套件、清除空間、色彩版本與核心色盤。先縮小文件邊界，讓使用者知道這不是完整品牌書，而是針對線上 logo suite 與 brand colours 的快速操作規範。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。文件相信線上環境需要快速、明確、低摩擦的規則；一致性來自少數高頻資產被正確使用。採用「scope first」框架：先界定用途，再提供可執行規格。

執行上，這份 guideline 透過 Introduction and Scope、Horizontal Logo System、Construction and Minimum Size、Clearspace 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。品牌 guideline 可先用 scope statement 限定責任，避免單一文件承擔所有品牌決策。

## Introduction and Scope

1. **Chapter Purpose**：先縮小文件邊界，讓使用者知道這不是完整品牌書，而是針對線上 logo suite 與 brand colours 的快速操作規範。
2. **Definition**：定義本文件只處理線上標誌與色彩使用，不處理語氣、攝影、排版、印刷物或產品 UI。
3. **Relationship**：它是所有後續標誌與色彩章節的使用前提，避免使用者把有限規範誤讀成全品牌治理系統。
4. **Design Execution**：以極短導言加下載入口降低導入成本，讓規範更像品牌資產使用說明，而非長篇策略文件。
5. **Principles**：文件相信線上環境需要快速、明確、低摩擦的規則；一致性來自少數高頻資產被正確使用。
6. **Frameworks**：採用「scope first」框架：先界定用途，再提供可執行規格。
7. **Patterns**：適合小型數位品牌規範使用的 minimal governance pattern：導言、logo variants、clearspace、colour tokens、contact。
8. **Rules**：AI 可檢查：若輸出內容涉及 Starling 線上標誌或色彩，必須引用此文件；若涉及離線印刷、攝影或語氣，應標記為超出此文件範圍。
9. **Reusable Knowledge**：品牌 guideline 可先用 scope statement 限定責任，避免單一文件承擔所有品牌決策。
10. **Abstraction**：`Knowledge Architecture`、`Governance`。
11. **Visual Evidence**：頁面主要以封面與簡短文字建立文件身份，視覺證據功能偏向入口與範圍標記，而非規則示範。

## Horizontal Logo System

1. **Chapter Purpose**：建立最常用水平標誌的可用性標準，確保不同線上版位仍保有可讀性與品牌辨識。
2. **Definition**：定義水平 logo 的最小尺寸、清除空間與背景色彩版本；不負責重新繪製 logo 或建立新組合。
3. **Relationship**：承接導言中的 logo suite 範圍，並成為日常線上應用的預設選項。
4. **Design Execution**：用構造敘述、尺寸數字與背景情境把抽象的「legibility」轉成可操作條件。
5. **Principles**：保持簡單形狀、足夠留白、依背景調整對比，而不是讓每個設計者自由判斷。
6. **Frameworks**：以「尺寸可讀性 + clearspace + 背景對比」作為 logo placement framework。
7. **Patterns**：標誌系統常見的三段式規範：minimum size、exclusion zone、colourway by background。
8. **Rules**：AI 可檢查：水平 logo 高度不得低於 20px；四周清除空間需至少為 S mark 的 0.5 倍；白底與淺色背景優先使用 primary colourway；深色背景使用 light colourway；亮色背景使用 white colourway。
9. **Reusable Knowledge**：最常用 logo variant 應被賦予最完整規則，因為它承擔多數品牌曝光風險。
10. **Abstraction**：`Visual Identity`、`AI-Checkable Rules`。
11. **Visual Evidence**：頁面使用 logo 實例、尺寸標記、clearspace 圖與 colourway 對照，功能是示範比例、對比與錯誤預防。

### Construction and Minimum Size

1. **Chapter Purpose**：保護小尺寸線上場景中的識別清晰度。
2. **Definition**：定義水平 logo 由簡單形狀構成，且高度不可小於 20px。
3. **Relationship**：支撐後續 clearspace 與 colourway，因為尺寸不足時其他規則無法補救可讀性。
4. **Design Execution**：以單一 px 數值避免含糊的「不要太小」。
5. **Principles**：數位品牌資產需要最低像素門檻。
6. **Frameworks**：minimum viable recognition threshold。
7. **Patterns**：用最小高度而非寬度定義 logo 可讀性。
8. **Rules**：AI 可檢查：任何水平 logo rendition 的 rendered height 必須大於或等於 20px。
9. **Reusable Knowledge**：小尺寸規則應綁定實際輸出單位。
10. **Abstraction**：`Visual Identity`、`Design Tokens`。
11. **Visual Evidence**：以 20px 標註搭配 logo 圖，承擔比例證據功能。

### Clearspace

1. **Chapter Purpose**：避免標誌被鄰近文字或圖形削弱辨識。
2. **Definition**：水平 logo 周圍保留 S mark 一半的空間。
3. **Relationship**：與最小尺寸共同形成可讀性下限。
4. **Design Execution**：使用 logo 自身元素作為量尺，讓規則可隨尺寸縮放。
5. **Principles**：清除空間應與品牌資產內在比例相連，而非固定任意距離。
6. **Frameworks**：logo-derived spacing system。
7. **Patterns**：以標誌字母或符號的一部分作為 exclusion zone。
8. **Rules**：AI 可檢查：logo bounding box 外 0.5 個 S mark 尺寸內不得有文字、圖示、邊框或影像干擾物。
9. **Reusable Knowledge**：可縮放的 clearspace 規則比固定像素更適用於多尺寸場景。
10. **Abstraction**：`Layout System`、`AI-Checkable Rules`。
11. **Visual Evidence**：clearspace 圖以量測框示範不可入侵區，功能是比例與治理證據。

### Colourways

1. **Chapter Purpose**：在多種背景上維持 logo 對比與品牌色彩一致。
2. **Definition**：依白底、淺色、深色、亮色背景選擇 primary、light 或 white colourway。
3. **Relationship**：把 logo placement 從尺寸空間延伸到色彩環境。
4. **Design Execution**：用背景分類而非自由審美判斷來決定版本。
5. **Principles**：可讀性優先於單一色彩執著；背景越複雜越需要更高對比。
6. **Frameworks**：background-to-logo mapping。
7. **Patterns**：按背景明度與彩度選擇標誌反白或淺色版本。
8. **Rules**：AI 可檢查：白色或淺色背景應用 primary colourway；深色背景應用 light colourway；高彩度亮色背景應用 white colourway；不得在低對比背景使用 primary logo。
9. **Reusable Knowledge**：logo 色彩規則可表達成背景分類決策樹。
10. **Abstraction**：`Color System`、`Visual Identity`。
11. **Visual Evidence**：頁面呈現不同 colourways 與 monochrome 參照，功能是對照與選擇示範。

## Vertical Logo System

1. **Chapter Purpose**：為空間比例不適合水平標誌的場景提供受控替代方案。
2. **Definition**：定義垂直 logo 的使用情境、最小高度、清除空間與色彩版本。
3. **Relationship**：它不是任意替換，而是對水平系統的補充，用於置中或獨立展示。
4. **Design Execution**：保留與水平版本相同的 clearspace 與 colourway 邏輯，但提高最小尺寸要求。
5. **Principles**：替代 logo variant 應有更嚴格的使用條件，以避免品牌版面失控。
6. **Frameworks**：variant governance framework：default variant、conditional variant、shared rules。
7. **Patterns**：垂直 logo 適合 badge-like 或 centerpiece 情境，需要更多留白。
8. **Rules**：AI 可檢查：垂直 logo 高度不得低於 60px；應置中或獨立使用；周圍需有大量清除空間；colourway 選擇需遵守與水平 logo 相同的背景規則。
9. **Reusable Knowledge**：品牌系統可讓不同 logo variants 共享規則，但用更高門檻區分主次。
10. **Abstraction**：`Visual Identity`、`Governance`。
11. **Visual Evidence**：使用垂直標誌、60px 標記、clearspace 與背景版本對照，功能是條件示範與比例控制。

## Colour Palette

1. **Chapter Purpose**：把 Starling 的線上品牌色彩轉成可複製、可實作的色彩 token。
2. **Definition**：列出 core、neutral、accent 色彩，包含 RGB、HEX、CMYK 數值。
3. **Relationship**：色彩章節支援 logo colourway 與線上品牌延展，提供具體輸出值。
4. **Design Execution**：以名稱與多色彩空間數值並列，讓設計、前端與印刷溝通都能引用。
5. **Principles**：色彩一致性需要語意名稱與精確數值並存。
6. **Frameworks**：semantic palette with implementation values。
7. **Patterns**：核心色、輔助中性色、強調色的三層色盤。
8. **Rules**：AI 可檢查：Starling Purple 必須使用 HEX `#6935D3`；Starling Sand 使用 `#F6EFEA`；Starling Orange 使用 `#F08357`；Starling Teal 使用 `#68D9CF`；Starling Navy 使用 `#192851`。
9. **Reusable Knowledge**：品牌色盤應同時提供 semantic role 與跨媒介數值。
10. **Abstraction**：`Color System`、`Design Tokens`。
11. **Visual Evidence**：色票與數值表承擔 token 證據功能，讓讀者可直接校驗顏色。

## Contact

1. **Chapter Purpose**：提供規範未涵蓋情境的治理出口。
2. **Definition**：定義品牌使用問題的聯絡方式。
3. **Relationship**：補足簡短文件無法涵蓋所有案例的治理缺口。
4. **Design Execution**：以單一 email 降低詢問成本。
5. **Principles**：精簡 guideline 需要明確 escalation path。
6. **Frameworks**：human review fallback。
7. **Patterns**：在規範結尾放置品牌聯絡窗口。
8. **Rules**：AI 可檢查：當使用情境超出本文件或背景分類不明確時，應標記為需品牌審核。
9. **Reusable Knowledge**：每份 guideline 都應設計例外處理機制。
10. **Abstraction**：`Governance`、`Operations`。
11. **Visual Evidence**：此章以文字聯絡資訊為主，證據功能是治理入口而非視覺示範。

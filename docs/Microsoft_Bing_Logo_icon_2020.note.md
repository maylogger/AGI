# Microsoft Bing Logo and Icon Guidance

來源：`sources/Microsoft_Bing_Logo_icon_2020.pdf`
日期：2020-10
研究視角：Design Infrastructure Researcher

## Summary

Microsoft Bing logo and icon guidance 以商標授權為起點，說明何時需要 license、如何使用 Microsoft Bing logo、product icon、最小尺寸、標籤與縮放比例。先建立商標使用門檻，避免外部使用者把 Microsoft Bing logo 用成未授權背書、贊助或相容性聲明。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。品牌資產使用不是設計問題的第一步，而是關係與授權問題。authorization flow：existing agreement → general Microsoft guidelines → business owner license → brand team contact。

執行上，這份 guideline 透過 Usage Requirements、Our Elements、Logo and Logo Usage、Product Icon 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。任何第三方 logo guideline 都應先問「是否有合法關係」而不是「該放哪個版本」。

## Usage Requirements

1. **Chapter Purpose**：先建立商標使用門檻，避免外部使用者把 Microsoft Bing logo 用成未授權背書、贊助或相容性聲明。
2. **Definition**：定義需要 trademark use license 的情境：使用 Microsoft Bing trademark、表示 sponsorship/endorsement、表示 compatibility endorsement，例如 “results from Microsoft Bing”。
3. **Relationship**：此章是後續 logo 與 icon 使用的法律前提；沒有授權或既有協議範圍，就不應進入視覺應用。
4. **Design Execution**：作者用決策流程引導使用者先查既有 Bing APIs / Bing Maps agreements，再查 Microsoft Trademark Guidelines，最後尋求 stand-alone authorization。
5. **Principles**：品牌資產使用不是設計問題的第一步，而是關係與授權問題。
6. **Frameworks**：authorization flow：existing agreement → general Microsoft guidelines → business owner license → brand team contact。
7. **Patterns**：短型商標 guideline 常先以 legal decision tree 控制入口，再提供少量視覺規格。
8. **Rules**：若使用 logo、名稱或暗示 Microsoft Bing 贊助、背書、相容性，即需確認 license；使用方式必須準確反映公司/產品與 Bing 的關係；不確定時需取得 Microsoft business owner 或 brand team 授權。
9. **Reusable Knowledge**：任何第三方 logo guideline 都應先問「是否有合法關係」而不是「該放哪個版本」。
10. **Abstraction**：`Legal and Trademark`、`Governance`、`Compliance`。
11. **Visual Evidence**：此章主要是授權文字與流程，功能是法律邊界證據。

## Our Elements

1. **Chapter Purpose**：界定外部可談論或呈現的 Microsoft Bing 基本識別元素。
2. **Definition**：包含 Microsoft Bing logo/icon 與 Results from Microsoft Bing 的語境。
3. **Relationship**：它把 Usage Requirements 的授權情境轉成實際可用元素。
4. **Design Execution**：以極簡元素頁面限制外部使用者可操作的品牌資產範圍。
5. **Principles**：商標 guideline 越短，越應避免提供過多可被誤用的品牌語言。
6. **Frameworks**：element set：logo → icon → attribution phrase。
7. **Patterns**：用 attribution phrase 支援產品資料來源標示，而非開放完整品牌系統。
8. **Rules**：若使用 “Results from Microsoft Bing” 或類似語句，需與實際資料來源/相容關係一致；不可用元素暗示超出事實的合作關係。
9. **Reusable Knowledge**：品牌元素可分為 identity asset 與 attribution text，兩者應有不同審核規則。
10. **Abstraction**：`Visual Identity`、`Product Language`、`Legal and Trademark`。
11. **Visual Evidence**：元素展示圖提供資產邊界證據。

## Logo and Logo Usage

1. **Chapter Purpose**：確保 logo 在亮、暗背景中具備可讀性，並避免使用者自行改造。
2. **Definition**：定義 positive logo 用於 light / white backgrounds，knock-out logo 用於 dark backgrounds 或照片暗部。
3. **Relationship**：此章承接元素章，將 logo 放入背景選擇邏輯。
4. **Design Execution**：用背景明暗決定 logo 版本，保持規格非常簡短。
5. **Principles**：小型商標 guideline 的核心是減少選項與例外，而不是建立完整設計系統。
6. **Frameworks**：background-based logo selection：light → positive gray logotype；dark/photo dark area → white knock-out。
7. **Patterns**：logo 使用規範可用二元背景判斷支援快速審核。
8. **Rules**：light/white background 使用 positive version；dark background 或照片暗部使用 knock-out version；不得選用導致低對比或不可讀的版本。
9. **Reusable Knowledge**：AI 可用背景亮度與 logo 版本比對，自動標記錯誤配對。
10. **Abstraction**：`Visual Identity`、`Accessibility`、`AI-Checkable Rules`。
11. **Visual Evidence**：logo version 頁與 usage 頁是背景對比與可讀性證據。

## Product Icon

1. **Chapter Purpose**：規範 Bing product icon 在小尺寸、標籤與縮放時仍保持識別與 Microsoft Bing 關聯。
2. **Definition**：涵蓋 product icon、sizing、labeling、scaling，以及 width 0.16 in / 4.23 mm / 16 px 的最小尺寸。
3. **Relationship**：它補足 logo 在產品介面或較小場景中的替代識別。
4. **Design Execution**：以 X、1/2X、1/8X 的比例標註 icon 與 Microsoft Bing 標籤之間的空間與尺度。
5. **Principles**：icon 規格需要可縮放的比例系統，而不只是固定像素。
6. **Frameworks**：icon lockup metrics：base width → clear space fractions → label relation → minimum size。
7. **Patterns**：用 X-based spacing 讓 icon 在不同尺寸下仍能被一致再製。
8. **Rules**：icon width 不得小於 0.16 in / 4.23 mm / 16 px；標籤與 icon 的間距應遵循 X、1/2X、1/8X 比例；不得縮放到標籤不可讀或 icon 形狀失真。
9. **Reusable Knowledge**：可將 icon guideline 轉為 bounding-box 與比例檢查。
10. **Abstraction**：`Iconography System`、`Design Tokens`、`AI-Checkable Rules`。
11. **Visual Evidence**：尺寸與 X 比例圖是主要可量測證據。

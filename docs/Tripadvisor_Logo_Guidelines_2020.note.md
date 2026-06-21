# Tripadvisor Design System Logos

來源：`sources/Tripadvisor_Logo_Guidelines_2020.pdf`
日期：2020-01-17
研究視角：Design Infrastructure Researcher

## Summary

Tripadvisor 標誌系統規範，定義主要與次要 logo lockup、最小尺寸、背景情境與基本使用原則。先把資產來源治理清楚，避免使用者從網路或舊檔案取得錯誤 logo；沒有這章，後續規範即使完整也可能套用在錯誤資產上。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。品牌一致性先從 asset provenance 開始，而不是只靠設計審美。採用「核准資產 + 使用規範」雙層治理：檔案來源控制形狀，指南控制情境。

執行上，這份 guideline 透過 Download、Primary Logo、Primary Horizontal Lockup、Primary Vertical Lockup 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。設計規範應把 asset retrieval 視為系統的一部分，而不是附錄。

## Download

1. **Chapter Purpose**：先把資產來源治理清楚，避免使用者從網路或舊檔案取得錯誤 logo；沒有這章，後續規範即使完整也可能套用在錯誤資產上。
2. **Definition**：此章定義「核准資產」的取得入口，不負責說明 logo 造型細節。
3. **Relationship**：它是整份文件的操作起點，後續主要與次要 logo 規則都假設使用者已取得正確檔案。
4. **Design Execution**：以下載提示加上「follow all guidelines」形成輕量授權流程，把品牌使用從自由取用改成受控資產分發。
5. **Principles**：品牌一致性先從 asset provenance 開始，而不是只靠設計審美。
6. **Frameworks**：採用「核准資產 + 使用規範」雙層治理：檔案來源控制形狀，指南控制情境。
7. **Patterns**：可重用為任何品牌 guideline 的 Asset Access Gate 模組。
8. **Rules**：AI 可檢查條件包括：使用素材必須來自核准下載包；輸出品不得引用未授權或未知來源 logo；若素材來源缺失，標記為需品牌審核。
9. **Reusable Knowledge**：設計規範應把 asset retrieval 視為系統的一部分，而不是附錄。
10. **Abstraction**：`Operations`、`Governance`、`Brand Asset Management`。
11. **Visual Evidence**：頁面以下載入口與簡短文字為主，視覺證據功能是操作引導，而不是比例教學。

## Primary Logo

1. **Chapter Purpose**：建立 Tripadvisor 最標準的辨識形式，讓大多數情境都有預設解答；沒有這章，使用者會在水平、垂直與圖示間任意選擇。
2. **Definition**：此章定義 primary logo suite，包括 Ollie、水平 lockup、垂直 lockup 與小空間垂直版本；不負責解決困難背景或特殊對比問題。
3. **Relationship**：它承接 Download 的資產治理，並為 Secondary Logos 提供「只有 primary 不適用時才替換」的基準。
4. **Design Execution**：作者用多頁大圖示意每種 lockup 的形狀、留白與比例，再用最小尺寸把視覺示例轉成可執行門檻。
5. **Principles**：主要識別應優先、清楚、可讀；變體存在是為了適配版面，而不是任意風格化。
6. **Frameworks**：以「logo form selection」框架運作：預設 horizontal，需要垂直版面時用 vertical，空間極小時使用 small-space vertical。
7. **Patterns**：常見模式是 Logo Suite Matrix，將標誌拆成圖示、水平 lockup、垂直 lockup與受限空間版本。
8. **Rules**：Ollie 最小高度 20px；horizontal lockup 最小高度 20px；vertical lockup 最小高度 37px；另一垂直 lockup 最小高度 50px；低於門檻時應拒絕或改用適當小空間版本。
9. **Reusable Knowledge**：每個 logo system 都應提供 form factors 與 minimum rendered size，讓跨媒介實作可被自動檢查。
10. **Abstraction**：`Visual Identity`、`Logo System`、`AI-Checkable Rules`。
11. **Visual Evidence**：大量使用 lockup 圖版、比例標記與 suite 排列；它們承擔示範、比例與可選版本辨識功能。

### Primary Horizontal Lockup

1. **Chapter Purpose**：提供最常用、最穩定的品牌簽名形式，適合寬版面與一般品牌露出。
2. **Definition**：定義 Ollie 與 wordmark 橫向組合的主要形式，不處理垂直空間或極窄容器。
3. **Relationship**：它是 primary suite 的核心版本，與 vertical lockup 形成版面方向上的互補。
4. **Design Execution**：以分頁圖像讓使用者看見 lockup 的標準比例與留白關係。
5. **Principles**：在足夠水平空間中保持完整名稱辨識優先於只使用圖示。
6. **Frameworks**：決策邏輯是「若水平寬度足夠，優先使用 horizontal lockup」。
7. **Patterns**：圖示加 wordmark 的水平簽名模式，可跨品牌複用。
8. **Rules**：AI 可檢查：horizontal lockup 高度不得低於 20px；不得拉伸、拆解或替換 lockup 內部比例；容器不足時不可壓縮，應改選其他核准版本。
9. **Reusable Knowledge**：品牌應把「預設 lockup」明確化，避免每個版面重新判斷。
10. **Abstraction**：`Logo System`。
11. **Visual Evidence**：示例以大幅 logo 圖形為主，功能是標準樣貌與比例校準。

### Primary Vertical Lockup

1. **Chapter Purpose**：讓較窄或置中版面仍能保留完整品牌識別。
2. **Definition**：定義 Ollie 與 wordmark 垂直排列的主要版本，不等同於次要 logo。
3. **Relationship**：它補足 horizontal lockup 無法適配的空間條件，仍屬 primary family。
4. **Design Execution**：用獨立頁面呈現垂直結構與多個比例標記。
5. **Principles**：同一品牌核心可透過 orientation 變體延展，但不可改變識別組件本身。
6. **Frameworks**：使用「容器方向」作為 lockup 選擇依據。
7. **Patterns**：Vertical Signature Pattern，適用於 avatar、窄幅廣告、置中落款。
8. **Rules**：AI 可檢查：vertical lockup 高度不得低於 37px；若採用另一垂直版本，最小高度不得低於 50px；不得任意調整圖示與字標距離。
9. **Reusable Knowledge**：指南應把 orientation adaptation 寫成受控變體，而非讓設計師自由重排。
10. **Abstraction**：`Visual Identity`、`Layout Adaptation`。
11. **Visual Evidence**：圖版主要承擔排列示範與尺寸比較功能。

### Small Space Vertical Lockup

1. **Chapter Purpose**：處理空間受限時仍需完整識別的情境，避免使用者縮小標準版本到不可讀。
2. **Definition**：定義小空間專用垂直 lockup，不是任意裁切或簡化。
3. **Relationship**：它位於 primary suite 的適配層，介於完整 primary lockup 與只用圖示之間。
4. **Design Execution**：透過獨立示意頁建立「小空間也有核准版本」的觀念。
5. **Principles**：可讀性比硬塞完整 lockup 更重要；小尺寸必須用被設計過的變體解決。
6. **Frameworks**：以 available space 作為變體選擇門檻。
7. **Patterns**：Responsive Logo Variant，可跨品牌用於 favicon、badge、窄欄與小卡片。
8. **Rules**：AI 可檢查：若容器無法滿足標準 vertical lockup 最小尺寸，必須使用核准小空間版本；不得自行裁切 Ollie 或 wordmark。
9. **Reusable Knowledge**：Logo system 應提供 responsive variants，而不是只定義單一 master logo。
10. **Abstraction**：`Responsive Identity`、`Logo System`。
11. **Visual Evidence**：視覺證據是小尺寸 lockup 示意與比例標記，功能是適配示範。

### Primary Logo Suite and Minimum Scale

1. **Chapter Purpose**：把多個主要版本集中成可查表的系統，並用最小尺寸限制品質底線。
2. **Definition**：定義 primary suite 的清單與各版本最小像素高度。
3. **Relationship**：它總結前面 primary lockup 示範，並與 secondary minimum scale 形成平行結構。
4. **Design Execution**：以 suite overview 加尺寸表將視覺變體轉成機器可讀規範。
5. **Principles**：可讀性與一致性需要數值化，不應只靠目測。
6. **Frameworks**：版本選擇 + 尺寸驗證雙階段框架。
7. **Patterns**：Minimum Size Table 是 logo guideline 的核心 pattern。
8. **Rules**：AI 可檢查：Ollie >= 20px high；horizontal lockup >= 20px high；vertical lockup >= 37px high；alternate vertical lockup >= 50px high；低於最小尺寸即不符合規定。
9. **Reusable Knowledge**：把 brand assets 轉成可測量 token，可讓自動審核工具偵測違規。
10. **Abstraction**：`Design Tokens`、`AI-Checkable Rules`。
11. **Visual Evidence**：表格式 logo suite 圖示承擔比較與規格確認功能。

## Secondary Logos

1. **Chapter Purpose**：為困難背景、留白不足或無法創造淺色底的情境提供受控替代方案；沒有此章，使用者會自行加框、反白或改色。
2. **Definition**：定義 Ollie 置於圓形中的次要 logo family，以及次要水平、垂直、小空間與背景版本；不替代 primary 作為預設選擇。
3. **Relationship**：此章依賴 Primary Logo 的基準，只有在 primary 不易成立時啟用。
4. **Design Execution**：用圓形承載 Ollie，讓圖示在複雜背景或低留白情境下保持清楚，並分別提供 light/dark background 版本。
5. **Principles**：品牌適配應透過設計過的容器解決，而非臨時效果。
6. **Frameworks**：情境式 fallback framework：背景困難、clear space 不足或需要深色背景時，改用 secondary suite。
7. **Patterns**：Contained Mark Pattern、Background-Specific Logo Variant。
8. **Rules**：AI 可檢查：描邊圓形版本不得與 Tripadvisor wordmark lockup；次要 logo 高度 >= 35px；secondary horizontal lockup >= 35px；secondary vertical lockup >= 52px；small-space secondary vertical lockup >= 69px。
9. **Reusable Knowledge**：次要標誌不是裝飾變體，而是為具體環境限制設計的 governance fallback。
10. **Abstraction**：`Logo System`、`Visual Identity`、`Brand Governance`。
11. **Visual Evidence**：大量以圓形 Ollie、light/dark 背景與 lockup suite 對照展示，功能是情境比較與可選版本辨識。

### Secondary Logo Rationale

1. **Chapter Purpose**：說明為何需要次要 logo，避免使用者把它視為風格選項。
2. **Definition**：界定次要 logo 用於 clear space 或 light background 無法建立的挑戰情境。
3. **Relationship**：它把使用條件放在 secondary suite 前方，先定義問題再給解法。
4. **Design Execution**：透過 Ollie in circle 建立可承受背景干擾的識別容器。
5. **Principles**：替代方案必須由問題驅動，而不是由視覺偏好驅動。
6. **Frameworks**：條件式啟用模型：若標準背景與留白不可行，才進入 secondary。
7. **Patterns**：Rationale Before Variants，是防止濫用變體的文件模式。
8. **Rules**：AI 可檢查：只有在無法建立清楚背景或留白時使用 secondary；stroked circle version 不得與 wordmark lockup；glyph 用途限於 body copy 附近的符號化使用。
9. **Reusable Knowledge**：每個 fallback asset 都應寫明觸發條件與禁用情境。
10. **Abstraction**：`Governance`、`Logo Fallback System`。
11. **Visual Evidence**：此段有 secondary circle 版本展示，功能是定義替代形狀。

### Secondary Horizontal and Vertical Lockups

1. **Chapter Purpose**：讓次要 logo 在不同版面方向中仍能保持系統一致。
2. **Definition**：定義 secondary horizontal、secondary vertical 與 limited-space secondary vertical lockups。
3. **Relationship**：延續 secondary rationale，提供具體可選版型。
4. **Design Execution**：分頁展示 preferred 與 small-space 狀態，避免使用者自行重組。
5. **Principles**：fallback 也需要完整的 responsive system。
6. **Frameworks**：與 primary 相同的 orientation selection，但套用於 contained mark。
7. **Patterns**：Secondary Suite Matrix，可用於任何需要容器標誌的品牌。
8. **Rules**：AI 可檢查：secondary horizontal lockup 高度不得低於 35px；secondary vertical lockup 高度不得低於 52px；small-space secondary vertical lockup 高度不得低於 69px；不得混用 primary wordmark 與非核准 secondary mark。
9. **Reusable Knowledge**：fallback variant 應與 primary variant 共享命名與決策邏輯，降低使用者學習成本。
10. **Abstraction**：`Logo System`、`Responsive Identity`。
11. **Visual Evidence**：多頁 lockup 圖示與比例標記承擔版型示範功能。

### Secondary Logo Suite and Minimum Scale

1. **Chapter Purpose**：把次要 logo 的背景版本與尺寸門檻集中，讓審核可操作。
2. **Definition**：涵蓋 light backgrounds、dark backgrounds、secondary horizontal/vertical lockups 與 minimum scale。
3. **Relationship**：對應 primary logo suite 的結構，是第二套可檢查規格。
4. **Design Execution**：按背景色分組，讓使用者先判斷背景，再選擇版本。
5. **Principles**：對比與可讀性是 logo 變體選用的主要依據。
6. **Frameworks**：Background Compatibility Matrix：light background 與 dark background 對應不同資產。
7. **Patterns**：背景分組資產表與 minimum scale table。
8. **Rules**：AI 可檢查：在 dark background 上必須使用核准深色背景版本；在 light background 上使用核准淺色背景版本；secondary logo >= 35px high；secondary horizontal >= 35px high；secondary vertical >= 52px high；small-space secondary vertical >= 69px high。
9. **Reusable Knowledge**：將背景條件加入 asset metadata，可支援自動推薦與規定檢查。
10. **Abstraction**：`Design Tokens`、`Accessibility-adjacent Contrast Governance`。
11. **Visual Evidence**：視覺證據是多版本套件與尺寸標示，功能是比較、選擇與驗證。

## Logo Usage

1. **Chapter Purpose**：提供最終使用原則，避免即使選對資產仍放在錯誤背景上。
2. **Definition**：定義 logo 理想使用：黑色 logo 搭配淺色品牌色或清楚背景。
3. **Relationship**：它收束 primary/secondary 選擇，將背景條件轉成實際輸出規範。
4. **Design Execution**：用簡短規則直接指出 preferred usage，而不是列大量例外。
5. **Principles**：品牌可讀性與背景清晰度優先；logo 不應被背景干擾。
6. **Frameworks**：Preferred Usage Rule：先嘗試 black logo on light/clear background，若不可行才回到 secondary suite。
7. **Patterns**：Usage Summary Module，適合作為設計交付前的最後檢查。
8. **Rules**：AI 可檢查：logo 背景應為淺色品牌色或清楚背景；若背景複雜或深色，不得直接使用主要黑色版本；應改用相容的 secondary/dark-background 版本。
9. **Reusable Knowledge**：每套 logo guideline 都需要「理想情境」而不只是「可用版本」。
10. **Abstraction**：`Brand Governance`、`AI-Checkable Rules`。
11. **Visual Evidence**：此章文字很少，視覺證據推定為 logo 放置示例，功能是使用情境示範。

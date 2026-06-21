# Amazon Brand Usage Guidelines

來源：`sources/Amazon_Brand_Usage_Guidelines.pdf`
日期：2012-10-08
研究視角：Design Infrastructure Researcher

## Summary

這份 display advertising style guide 規範連到 Amazon.com 的廣告如何使用 Amazon 品牌、CTA、logo、色彩、素材與 co-branding。先把 Amazon brand usage 定位為需要事前審核的高價值品牌資產治理，而不是自由下載的廣告素材。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。品牌可提高廣告效果，但必須以顧客清楚辨識與品牌資產保護為代價條件。使用 Amazon brand → 依 guideline 製作 → 事前提交 → 依 advertising policies 審核。

執行上，這份 guideline 透過 Overview、Call To Action and Messaging、CTA Overview and Recommended CTAs、Amazon Text Link CTAs 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。平台品牌的 partner guideline 應先定義審核權限，再給予執行細節。

## Overview

1. **Chapter Purpose**：先把 Amazon brand usage 定位為需要事前審核的高價值品牌資產治理，而不是自由下載的廣告素材。
2. **Definition**：定義文件適用於連到 Amazon.com 的 display advertisements，重點是 Amazon name、branding elements 與 high-level best practices。
3. **Relationship**：這章建立權限與審核前提，後續 CTA、logo、色彩、co-branding 規則都依賴「advance review」。
4. **Design Execution**：以 description、related documents 與目錄快速告知使用者哪些議題在本文件、哪些轉到 advertising specs。
5. **Principles**：品牌可提高廣告效果，但必須以顧客清楚辨識與品牌資產保護為代價條件。
6. **Frameworks**：使用 Amazon brand → 依 guideline 製作 → 事前提交 → 依 advertising policies 審核。
7. **Patterns**：短版 guideline 可用「核心品牌規則 + 外部 technical spec link」避免文件過度膨脹。
8. **Rules**：所有創意材料須事前提交 Amazon 核准；未獲 written approval 不應使用 Amazon branding elements。
9. **Reusable Knowledge**：平台品牌的 partner guideline 應先定義審核權限，再給予執行細節。
10. **Abstraction**：Governance、Legal and Trademark、Knowledge Architecture。
11. **Visual Evidence**：此章主要是文字與目錄，視覺功能是建立文件導航與治理前提。

## Call To Action and Messaging

1. **Chapter Purpose**：防止 CTA 誤導顧客、誤用 Amazon functionality 或把廣告看起來像 Amazon 站內功能。
2. **Definition**：涵蓋 CTA overview、recommended CTAs、text links、branded buttons、capitalization、brand phrases、offers、restricted content。
3. **Relationship**：這是廣告最接近使用者行動的語言層，直接影響顧客是否理解點擊後會發生什麼。
4. **Design Execution**：用允許 CTA 表格、字體規格、長度限制、錯誤示例與 why 說明建立可審核文案系統。
5. **Principles**：CTA 應短、動作清楚、landing page 一致、避免促銷欺騙與 Amazon 功能混淆。
6. **Frameworks**：Action intent → Allowed CTA → Visual treatment → Legal/brand review。
7. **Patterns**：將 CTA 分為 text link 與 button，並依 placement/interaction 定義允許與禁止，是廣告平台可複用模式。
8. **Rules**：CTA 不應超過 30 characters；不得換行；建議 action verb 開頭、sentence case、無結尾標點；Amazon 必須 title case。
9. **Reusable Knowledge**：CTA guideline 應同時規範文字、視覺樣式、互動目的與不可用促銷資訊。
10. **Abstraction**：Content Design、Interaction Design、Compliance、AI-Checkable Rules。
11. **Visual Evidence**：表格、allowed/not allowed 範例與 why callouts 是此章的主要證據。

### CTA Overview and Recommended CTAs

1. **Chapter Purpose**：把點擊行動與 landing page 結果對齊，降低 customer confusion。
2. **Definition**：定義 shopping 與 interaction 類 CTA，例如 Shop now at Amazon.com、Pre-order now、Clip coupon、Learn more、Watch now、See more。
3. **Relationship**：後續 text link 與 button 規格都建立在這些允許文案上。
4. **Design Execution**：用表格對應 destination/action 與 allowed visuals。
5. **Principles**：CTA 是承諾，必須準確描述點擊後的體驗。
6. **Frameworks**：CTA selection = customer action + destination + allowed visual treatment。
7. **Patterns**：把 CTA 文案綁定 landing page 類型，可被任何平台型廣告規範複用。
8. **Rules**：CTA 應盡量短；button 或 pointer text 應盡可能 action verb 開頭、sentence capped、無 ending punctuation。
9. **Reusable Knowledge**：允許 CTA 表格比開放式文案指南更易讓 AI 與審核團隊檢查。
10. **Abstraction**：Content Design、Interaction Design、AI-Checkable Rules。
11. **Visual Evidence**：CTA 表格本身是決策證據。

### Amazon Text Link CTAs

1. **Chapter Purpose**：確保 Amazon-style text links 在不同廣告尺寸中可讀且不被用來夾帶促銷訊息。
2. **Definition**：規範 Frutiger 57/67 Condensed、11.5pt/14pt、底線、長度、顏色、透明度與 .com 用法。
3. **Relationship**：將 recommended CTA 轉成可實作的 typography 與 graphic styling。
4. **Design Execution**：依 small/large ad units 分配字體尺寸，並指定 descender break 與 arrow/underline opacity。
5. **Principles**：可讀性與一致性優先；CTA 不應承擔促銷細節。
6. **Frameworks**：ad unit size → CTA type size；base color → arrow/underline 70% opacity。
7. **Patterns**：文字連結可作為品牌化互動元件，需要 design-token 級規範。
8. **Rules**：CTA 長度不得超過 30 characters；必須單行；text、arrow、underline 使用同一 base color；underline/arrow opacity 為文字色 70%。
9. **Reusable Knowledge**：互動文字也應有 component spec，不只是 UI kit 的 button 才需要規格。
10. **Abstraction**：Typography System、UI Components、AI-Checkable Rules。
11. **Visual Evidence**：範例圖展示 allowed text link 與 wrong promotion messaging。

### Amazon Branded Button CTAs

1. **Chapter Purpose**：避免廣告按鈕看起來像 Amazon.com 站內原生功能，造成廣告與網站功能混淆。
2. **Definition**：一般廣告不得使用 Amazon branded buttons；eCommerce ads 的 Add to Cart、Add to Wish List、Shop now、Clip coupon 是例外。
3. **Relationship**：補充 CTA overview 的 visual treatment 判斷。
4. **Design Execution**：用 not allowed/allowed 範例說明 advertiser branded buttons 或 Amazon text links 才是一般情境的安全選擇。
5. **Principles**：平台功能樣式是信任資產，不應被廣告隨意借用。
6. **Frameworks**：若按鈕會被誤認為 Amazon site functionality，則禁止；若是核准 eCommerce action，才可例外。
7. **Patterns**：平台應保護 native UI affordance，避免廣告借用後降低使用者信任。
8. **Rules**：非 eCommerce ads 不得使用 Amazon branded button；non-specific 或 inaccurate CTAs 不允許。
9. **Reusable Knowledge**：UI look-and-feel 也可受品牌 guideline 管理，尤其在平台廣告生態。
10. **Abstraction**：UI Components、Governance、Content Safety。
11. **Visual Evidence**：not allowed/allowed button examples 與 why 註記是關鍵證據。

### Capitalization, Brand Phrases and Offers

1. **Chapter Purpose**：控制專有名詞、Amazon 功能名稱與促銷訊息，避免法律、商標與顧客誤解風險。
2. **Definition**：涵蓋 Amazon capitalization、Gold Box、Deal of the Day、1-Click、Wish List、Subscribe & Save 等品牌片語，以及 free offers、sweepstakes、shipping discounts、prices。
3. **Relationship**：這節把 CTA 文案擴展到所有 Amazon-related claim。
4. **Design Execution**：列出需核准或不可使用的專有片語，並以 examples 說明類似 phrase 也可能造成混淆。
5. **Principles**：專有功能語彙只在真實、核准且上下文正確時可使用。
6. **Frameworks**：Term appears → Is proprietary/function-related? → Is context approved? → Legal review if offer/discount/price。
7. **Patterns**：平台品牌 guideline 應管理「近似語」而不只管理精確商標。
8. **Rules**：Amazon 不得全大寫或全小寫；價格顯示 strongly discouraged 且需 approval；free goods/services 必須標示 terms and conditions apply。
9. **Reusable Knowledge**：品牌詞庫應包含 prohibited、requires approval、allowed-with-context 三種狀態。
10. **Abstraction**：Legal and Trademark、Messaging、Compliance、AI-Checkable Rules。
11. **Visual Evidence**：相似片語與促銷示例展示哪些文案會被誤認為 Amazon 功能。

### Restricted and Unacceptable Ad Content

1. **Chapter Purpose**：建立最低內容安全底線，防止品牌出現在欺騙或未授權語境中。
2. **Definition**：禁止 deceptive、false、misleading content；未經批准不得使用 Amazon proprietary words、phrases、products。
3. **Relationship**：這是 CTA/messaging 章的風險收束，並把詳細規則導向 advertising specs。
4. **Design Execution**：用短 bullet 列出底線，避免讓使用者把前述允許例子解讀為全面開放。
5. **Principles**：顧客信任與真實性高於轉換率。
6. **Frameworks**：Content safety gate 先於 creative evaluation。
7. **Patterns**：短文件可保留 restricted content baseline，並連到完整政策文件。
8. **Rules**：任何聲明若無法由 landing page 或產品事實支持，應判定為 misleading；專有詞需明確 approval。
9. **Reusable Knowledge**：guideline 中應把「不能做」的底線與「需要另查 policy」的入口分開。
10. **Abstraction**：Content Safety、Compliance、Governance。
11. **Visual Evidence**：此節主要是政策文字，視覺證據較少。

## Logos and Imagery

1. **Chapter Purpose**：保護 Amazon logo、icon、site element 與 product imagery 不被未授權或錯誤情境使用。
2. **Definition**：涵蓋 Amazon.com logo、additional logos、icons、site elements、product imagery。
3. **Relationship**：視覺資產規範與 CTA 規範共同防止廣告被誤認為 Amazon 站內內容或官方背書。
4. **Design Execution**：以尺寸、clear space、顏色、禁止變形、權利清理與 approval 建立完整視覺治理。
5. **Principles**：商標完整性、素材權利、顧客辨識與平台信任同等重要。
6. **Frameworks**：Asset type → ownership/approval → visual spec → placement review。
7. **Patterns**：平台式品牌應同時管理 logo integrity 與 third-party imagery rights。
8. **Rules**：Amazon logo 最小 1 inch 或 72px；clear space 以 bold letter `o` 計算；商品圖不得從 Google 或搜尋引擎下載。
9. **Reusable Knowledge**：imagery guideline 應同時問「看起來對不對」與「權利是否可用」。
10. **Abstraction**：Visual Identity、Photography System、Legal and Trademark、AI-Checkable Rules。
11. **Visual Evidence**：logo 色版、尺寸標記、not allowed examples 與圖像授權示例構成證據。

### Amazon.com Logo Guidelines

1. **Chapter Purpose**：確保 Amazon logo 在 co-branded campaign 中具備固定尺寸、留白、色彩與完整 artwork。
2. **Definition**：定義 logo approval、minimum size、clear space、corporate colors、one-color smile、contrast 與 not allowed 用法。
3. **Relationship**：為 co-branding 章提供 logo 使用基礎。
4. **Design Execution**：用 `o` 作為相對留白單位，並指定 smile 不得灰色。
5. **Principles**：logo artwork 不可被語句、效果或背景破壞。
6. **Frameworks**：背景明暗 → 選擇 color/reversed/one-color；尺寸 → ≥ 1 inch/72px；周邊元素 → `o` clear space。
7. **Patterns**：logo 的 internal letterform 可成為 spacing token，適合跨媒介應用。
8. **Rules**：不得改比例或顏色、不得把 logo 放入句子、不得 outline、不得無 smile、不得放在 patterned background、不得加 drop shadow。
9. **Reusable Knowledge**：logo guideline 應把可接受色版列出，而不是只寫「使用官方 logo」。
10. **Abstraction**：Visual Identity、Layout System、AI-Checkable Rules。
11. **Visual Evidence**：preferred/reversed 色版與 not allowed 網格是強視覺證據。

### Additional Logos, Icons and Product Imagery

1. **Chapter Purpose**：防止廣告主任意借用 Amazon family logos、site elements 或未授權商品圖。
2. **Definition**：涵蓋 Shopping Cart、Amazon Student、Gold Box、Click to Look Inside、Customer Star Ratings、Subscribe & Save 等 icons/site elements，以及 product imagery。
3. **Relationship**：與 brand phrases 節形成語言與視覺雙重專有資產管理。
4. **Design Execution**：用非窮盡清單與 rights clearance 條款建立審核入口。
5. **Principles**：任何看似 Amazon 功能或商品的視覺都可能造成背書或功能混淆。
6. **Frameworks**：Asset source → Is Amazon family/site element? → Express approval required；Product image → Rights owner clearance。
7. **Patterns**：專有 UI/icon 清單應與 trademark/feature term 清單互相對照。
8. **Rules**：未經明確要求與批准不得使用 Amazon family logos、icons、site elements；商品圖需 owned 或 cleared for use。
9. **Reusable Knowledge**：品牌 guideline 應將 visual asset permission 與 copyright clearance 放在同一流程中。
10. **Abstraction**：Iconography System、Legal and Trademark、Governance。
11. **Visual Evidence**：icon/logo/product image examples 用來說明受控資產範圍。

## Colors

1. **Chapter Purpose**：避免廣告使用 Amazon 色彩來模仿 Amazon.com 介面或製造官方功能感。
2. **Definition**：定義 Amazon Orange、Amazon Blue 與相似色應與 Amazon page 有清楚視覺分離。
3. **Relationship**：延續 button 與 site element 的混淆防治邏輯。
4. **Design Execution**：提供色值，並要求使用相似 campaign branding 時以 border、faded edges 等方式分離。
5. **Principles**：品牌色不只是美學資產，也是平台功能辨識資產。
6. **Frameworks**：使用 Amazon-like colors → evaluate if emulating Amazon brand/page → require separation treatment。
7. **Patterns**：色彩 guideline 可以管理「contextual confusion」，不只管理 token correctness。
8. **Rules**：任何以 brand colors 明顯模仿 Amazon brand 或 site functionality 的圖形處理不允許；需有 defined border 或 faded edges 等分離手段。
9. **Reusable Knowledge**：平台廣告應建立 color-context collision rule，避免第三方 creative 看似原生 UI。
10. **Abstraction**：Color System、Governance、AI-Checkable Rules。
11. **Visual Evidence**：not allowed marquee 與 allowed example 展示色彩如何造成或避免混淆。

## Technical Specs and More

1. **Chapter Purpose**：承認本文件只處理品牌高階規則，將技術尺寸與 ad unit 細節導向專門文件。
2. **Definition**：提供 technical specs、eligible ad units、advertiser types 的外部入口。
3. **Relationship**：作為 implementation dependency，避免品牌 guideline 承擔所有廣告技術細節。
4. **Design Execution**：以單一 reference URL 管理更多規範。
5. **Principles**：知識架構應讓品牌、技術、政策各自維護。
6. **Frameworks**：Brand rules in current document；technical specs in linked spec repository。
7. **Patterns**：大型平台 guideline 可使用 modular documentation，不把所有規格塞進單一 PDF。
8. **Rules**：若素材涉及 ad unit 或 technical requirement，需同時符合 linked advertising specs。
9. **Reusable Knowledge**：guideline index 應明確標示哪些決策需查外部權威來源。
10. **Abstraction**：Knowledge Architecture、Operations。
11. **Visual Evidence**：此節為文字 reference，視覺證據低。

## Co-Branding

1. **Chapter Purpose**：區分 on Amazon 與 off Amazon placement 的品牌露出策略，避免站內廣告與 Amazon 內容混淆。
2. **Definition**：規範 Amazon logo 與 CTA 在站內、站外、AAP placement 中的使用。
3. **Relationship**：整合 CTA、logo、色彩與平台混淆風險，形成最終 placement guidance。
4. **Design Execution**：用 allowed/not allowed examples 指出站內應移除 Amazon logo，站外則需清楚使用 Amazon logo 或適當 text link CTA。
5. **Principles**：同一品牌資產在不同 placement 的風險不同，規則必須依 context 改變。
6. **Frameworks**：Placement context → On Amazon or off Amazon → Logo discouraged or required/appropriate → CTA placement rule。
7. **Patterns**：co-branding guideline 應先判斷媒介位置，再判斷視覺資產。
8. **Rules**：站內 ad placements 強烈不建議使用 Amazon logo；offsite ads 應清楚顯示 Amazon logo 或適當 text link CTA；應使用 `at Amazon.com` 而非 `on Amazon.com`。
9. **Reusable Knowledge**：co-branding 的核心不是雙方 logo 並列，而是使用者是否能理解內容來源與點擊結果。
10. **Abstraction**：Brand Collaboration、Governance、Content Design、AI-Checkable Rules。
11. **Visual Evidence**：on/off Amazon 的正反例圖提供 context-specific evidence。

### Branding On and Off Amazon

1. **Chapter Purpose**：把 placement-specific 的品牌規則落到實際創意範例。
2. **Definition**：站內、站外各有不同 Amazon logo 與 CTA 使用方式。
3. **Relationship**：此小節是全文件對「customer confusion」問題的總結。
4. **Design Execution**：透過 not allowed/allowed 創意 mockup 展示 logo 移除、CTA 位置與正確措辭。
5. **Principles**：品牌顯著性應服務清楚，而不是在所有地方最大化曝光。
6. **Frameworks**：If on Amazon → minimize Amazon branding；if off Amazon → make destination to Amazon explicit。
7. **Patterns**：依環境反轉 logo 使用原則，是平台品牌常見但容易被忽略的治理模式。
8. **Rules**：`Shop now at Amazon.com` 不應被拆到 button 外形成錯誤格式；站外 advertisement 需清楚包含 Amazon logo 或規定 CTA。
9. **Reusable Knowledge**：品牌指南應提供 placement-aware rules，避免單一規則跨情境誤用。
10. **Abstraction**：Brand Collaboration、Interaction Design、Governance。
11. **Visual Evidence**：正反例 mockups 與 why 註記提供具體判斷依據。

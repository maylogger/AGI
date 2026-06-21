# MICHELIN Brand Usage for Distributors and Retailers

來源：`sources/Michelin_DISTRIBUTOR_GUIDE_2019.pdf`
日期：2019-09
研究視角：Design Infrastructure Researcher

## Summary

Michelin Lifestyle 針對經銷商與零售商使用 MICHELIN 品牌的簡明規範，限制 logo、背景、保護區、廣告、活動、數位通路與品牌原則，避免第三方把自身溝通誤認為 MICHELIN 官方品牌環境。先界定第三方經銷商能做什麼、不能做什麼，防止 MICHELIN 品牌被誤用成經銷商品牌背書或官方通路。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。第三方品牌使用應支援產品銷售，但不得讓第三方看起來像品牌擁有者。limited brand permission：relationship → product focus → allowed asset → forbidden brand environment → validation。

執行上，這份 guideline 透過 Purpose and Permission Scope、Use of the Michelin Logo、Logo Versions and Size、Background and Protection Zone 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。第三方 guideline 應先定義 permission scope，再進入設計規格。

## Purpose and Permission Scope

1. **Chapter Purpose**：先界定第三方經銷商能做什麼、不能做什麼，防止 MICHELIN 品牌被誤用成經銷商品牌背書或官方通路。
2. **Definition**：定義 distributors / retailers 可在銷售 MICHELIN branded products 時使用 MICHELIN logo；不可使用 MICHELIN brand style、Michelin Man 圖像、手勢、舊廣告活動或自製 POS materials。
3. **Relationship**：這是後續 logo、背景、廣告、活動與數位規則的授權邊界。
4. **Design Execution**：作者用「只可使用 logo、且必須聚焦產品」來建立最小授權模型。
5. **Principles**：第三方品牌使用應支援產品銷售，但不得讓第三方看起來像品牌擁有者。
6. **Frameworks**：limited brand permission：relationship → product focus → allowed asset → forbidden brand environment → validation。
7. **Patterns**：授權方只開放 logo，而封鎖 brand style 與 mascot，是高價值品牌控制第三方風險的常見模式。
8. **Rules**：POS materials 只能使用 Michelin licensee 提供版本；溝通必須聚焦 MICHELIN 產品；沒有直接商業關係者不得使用品牌風格；logo 使用需由 licensee 與 Michelin Lifestyle Marketing and Communication team 驗證。
9. **Reusable Knowledge**：第三方 guideline 應先定義 permission scope，再進入設計規格。
10. **Abstraction**：`Legal and Trademark`、`Governance`、`Co-Branding`。
11. **Visual Evidence**：此章以 logo 與產品脈絡文字為主，功能是授權邊界證據。

## Use of the Michelin Logo

1. **Chapter Purpose**：讓第三方在必要時能正確顯示 MICHELIN logo，同時避免重繪、縮小、錯色或錯誤背景破壞品牌。
2. **Definition**：涵蓋 logo 版本、最小尺寸、不可修改、背景規則、保護區，以及廣告、海報、brochure 中的位置。
3. **Relationship**：它把第一章的有限授權轉為可量測的視覺規格。
4. **Design Execution**：以 horizontal preferred、stacked exception、monochrome exception、background variants 與 M-height protection zone 建立簡化判斷。
5. **Principles**：第三方使用規則越簡短，越需要明確限制可變項。
6. **Frameworks**：logo decision tree：media colour → background colour → logo version → minimum size → protection zone → product proximity。
7. **Patterns**：以 preferred / exception 架構控制 logo 版本，避免經銷商把例外當常態。
8. **Rules**：print 中 MICHELIN name 寬度不得小於 30 mm；screen 不得小於 85 px；不得 tamper、alter、remove parts 或 change proportions；Michelin Man 不得使用；logo 必須放在 MICHELIN 產品附近。
9. **Reusable Knowledge**：這些規則可直接轉成 AI-checkable logo QA：尺寸、比例、版本、背景、clear space、產品鄰近性。
10. **Abstraction**：`Visual Identity`、`AI-Checkable Rules`、`Legal and Trademark`。
11. **Visual Evidence**：logo 版本、背景色塊與保護區示意是主要比例與可讀性證據。

### Logo Versions and Size

1. **Chapter Purpose**：降低第三方選錯 logo 的機率。
2. **Definition**：定義 full colour horizontal logo 為偏好版本，stacked 與 monochrome 為例外。
3. **Relationship**：版本選擇影響後續背景與應用情境。
4. **Design Execution**：用 preference + exception 而不是多版本平權，建立清楚優先順序。
5. **Principles**：品牌在第三方環境中應盡量維持最強辨識版本。
6. **Frameworks**：preferred asset hierarchy。
7. **Patterns**：將例外版本限定在 production constraints。
8. **Rules**：horizontal logo 優先；stacked only as exception；黑白廣告可用 monochrome；最小尺寸為 print 30 mm、screen 85 px。
9. **Reusable Knowledge**：asset picker 應依媒介與背景自動推薦版本。
10. **Abstraction**：`Visual Identity`、`Design Tokens`。
11. **Visual Evidence**：各版本 logo 圖示提供選擇證據。

### Background and Protection Zone

1. **Chapter Purpose**：確保 logo 在複雜背景與不同色彩中仍可辨識。
2. **Definition**：定義 light、yellow、dark、mono 背景版本與 M-height protection zone。
3. **Relationship**：它把 logo 使用從資產層延伸到版面環境。
4. **Design Execution**：以背景類型決定 wordmark、support line 與 Michelin Man 顏色。
5. **Principles**：可讀性優先於裝飾整合。
6. **Frameworks**：background compatibility：homogeneous area → colour contrast → protected zone。
7. **Patterns**：用 logo 字母高度作為 clear-space unit，便於跨尺寸縮放。
8. **Rules**：背景需為均質色區或單純區域；Michelin Man 顏色維持黑線白填；wordmark 在深色背景為白；support line 在黃色背景改藍；保護區內不可有干擾元素。
9. **Reusable Knowledge**：可建立 contrast + clear-space detector。
10. **Abstraction**：`Layout System`、`Accessibility`、`AI-Checkable Rules`。
11. **Visual Evidence**：背景版本與保護區圖示提供驗收證據。

### Advertising, Posters and Brochures

1. **Chapter Purpose**：防止經銷商廣告看起來由 MICHELIN 官方署名或共同背書。
2. **Definition**：規範 adverts、posters、brochures 中 logo 的品牌環境與位置。
3. **Relationship**：它把 logo 規格套用到具體行銷材料。
4. **Design Execution**：要求廣告環境屬於經銷商 / 零售商品牌，MICHELIN logo 只作為產品標識。
5. **Principles**：logo 可以標識產品來源，但不應改變整體品牌主體。
6. **Frameworks**：advertising hierarchy：retailer brand signs ad → Michelin logo near product → no co-signing。
7. **Patterns**：第三方品牌使用應限制在 product adjacency。
8. **Rules**：廣告只能由 distributor/retailer 署名；不可由 MICHELIN 署名或共同署名；MICHELIN logo 必須緊鄰 MICHELIN branded products。
9. **Reusable Knowledge**：AI 可檢查 logo 與 product bounding boxes 是否鄰近、retailer logo 是否為主署名。
10. **Abstraction**：`Co-Branding`、`Legal and Trademark`、`Layout System`。
11. **Visual Evidence**：廣告版面示意負責情境與層級證據。

## Events and Digital

1. **Chapter Purpose**：處理展會與數位通路這些容易放大誤認的第三方 touchpoint。
2. **Definition**：涵蓋 events、trade fairs、websites、mobile apps、digital communications、approved content sharing 與 URL restriction。
3. **Relationship**：延伸前一章的 product adjacency 原則到空間與互動媒介。
4. **Design Execution**：在活動中允許 logo 支援產品展示，在數位中要求網站/APP 明確屬於經銷商品牌。
5. **Principles**：越接近完整體驗的媒介，越需要避免品牌主體被誤認。
6. **Frameworks**：channel rule：event presence / website / app / social → retailer identity first → Michelin content secondary → approved content only。
7. **Patterns**：將品牌風格與內容資產分開治理，允許分享核准內容但禁止套用整體風格。
8. **Rules**：展會概念與品牌風格必須屬於 distributor/retailer；digital 中 MICHELIN content 必須 secondary；只允許 dedicated MICHELIN product pages；MICHELIN logo 必須小於 distributor/retailer logo；不得在主要 domain 或 URL 使用 Michelin。
9. **Reusable Knowledge**：第三方 digital QA 可檢查 domain、logo hierarchy、page scope、content approval 與 brand style mimicry。
10. **Abstraction**：`Digital Brand Governance`、`Legal and Trademark`、`AI-Checkable Rules`。
11. **Visual Evidence**：活動與數位版面範例提供情境與層級證據。

## Key Principles and Validation

1. **Chapter Purpose**：把零散規則收束成品牌使用原則，讓第三方理解規範背後的判斷邏輯。
2. **Definition**：包含 fully support MICHELIN product/service sales、enhance exceptional brand image、comply with visual identity rules 與 validation。
3. **Relationship**：它是整份文件的審核框架，可用於未明列情境。
4. **Design Execution**：以三個 key principles 解釋為何不能推廣競品、不能低品質低價導向、不能濫用 logo 或 Michelin Man。
5. **Principles**：品牌資產使用權必須服務品牌產品與品牌形象，而非第三方流量或折扣。
6. **Frameworks**：principle-based review：sales support → image quality → visual compliance → licensee validation。
7. **Patterns**：短文件可在最後放 principle section，補足規則未覆蓋的新情境。
8. **Rules**：MICHELIN brand use 的唯一目標應是推廣可在銷售點取得的 MICHELIN products/services；不得用於競品；不得使用純價格導向、低品質、冗餘或不適當 logo / trademark / Michelin Man；不當使用需識別與修正。
9. **Reusable Knowledge**：可把 principles 轉成審稿問卷，用於新媒介或 AI 生成內容的風險判斷。
10. **Abstraction**：`Governance`、`Compliance`、`Brand Strategy`。
11. **Visual Evidence**：此章以原則文字與可能的示意版面為主，功能是治理與判準證據。

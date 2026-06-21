# Twitter Brand Guidelines

來源：`sources/twitter_brand_guidelines_2020.pdf`
日期：2020-10
研究視角：Design Infrastructure Researcher

## Summary

Twitter 2020 品牌規範，定義 logo、social icons、logo pairing lockups、Tweet treatments、Twitter marks 與商標法律要求。快速界定指南涵蓋 logo、hashtag、@reply、Tweets 等核心品牌元素，並承認文件非 exhaustive。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。簡短指南也需要 escalation path；品牌開放使用必須同時保留審核通道。Core Element Guide + Exception Escalation。

執行上，這份 guideline 透過 Using the Twitter Brand、Our Logo、The Basics、Spacing 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。Brand guideline 應在開頭明確說明 scope 與 unsupported cases 的處理方式。

## Using the Twitter Brand

1. **Chapter Purpose**：快速界定指南涵蓋 logo、hashtag、@reply、Tweets 等核心品牌元素，並承認文件非 exhaustive。
2. **Definition**：定義讀者在開始使用 Twitter brand 前應先讀本指南；未涵蓋情境需聯絡 trademarks@twitter.com。
3. **Relationship**：是後續 logo、lockup、Tweet、marks、legal 章節的入口與例外處理機制。
4. **Design Execution**：用短篇幅降低使用門檻，同時以 contact point 防止讀者自行推論未涵蓋使用。
5. **Principles**：簡短指南也需要 escalation path；品牌開放使用必須同時保留審核通道。
6. **Frameworks**：Core Element Guide + Exception Escalation。
7. **Patterns**：Scope Statement with Trademark Contact。
8. **Rules**：AI 可檢查：若使用情境不屬於 logo、hashtag/@reply、Tweets 或本文件明列範圍，需標記為「需聯絡 trademarks@twitter.com」；不得自行推定許可。
9. **Reusable Knowledge**：Brand guideline 應在開頭明確說明 scope 與 unsupported cases 的處理方式。
10. **Abstraction**：`Governance`、`Legal and Trademark`。
11. **Visual Evidence**：封面與 intro layout 簡短直接，功能是範圍設定而非視覺規格。

## Our Logo

1. **Chapter Purpose**：保護 Twitter bird 作為最可識別資產的完整性、顏色、空間與尺寸。
2. **Definition**：涵蓋 basics、spacing、color、social icons；不負責 Tweet rendering 或商標命名。
3. **Relationship**：logo 是 pairing lockups、marks 與 legal 條款的視覺核心。
4. **Design Execution**：以少量可測規則搭配圖例限制 logo 顏色、大小、clearspace、icon container。
5. **Principles**：高度識別資產應越少變體越好，讓一致性來自限制而非彈性。
6. **Frameworks**：Logo Protection Framework：approved colors、no modification、space, minimum size、social use.
7. **Patterns**：Minimal Logo Ruleset。
8. **Rules**：AI 可檢查：logo 只可為 Twitter blue 或 white；黑色例外需 approval；不得 alter/rotate/modify/animate；不得使用 outdated versions；clearspace >= 150% logo width；logo minimum width >= 16px。
9. **Reusable Knowledge**：強勢 consumer brand 的 logo guideline 可採「極少選項 + 明確禁用」模式。
10. **Abstraction**：`Logo System`、`AI-Checkable Rules`。
11. **Visual Evidence**：以 logo、clearspace、色彩背景、social icon 容器圖示示範可用與不可用邊界。

### The Basics

1. **Chapter Purpose**：以最短規則建立 bird logo 的不可變性。
2. **Definition**：只允許 blue/white，黑色需核准；禁止修改、旋轉、動畫、使用舊版。
3. **Relationship**：是 Our Logo 其他 spacing/color 規則的基底。
4. **Design Execution**：用 bullet list 把保護性規則放在前面，先禁止最常見誤用。
5. **Principles**：iconic mark 的價值在於穩定，不在於可表演性。
6. **Frameworks**：Immutable Mark Policy。
7. **Patterns**：Logo Basics Checklist。
8. **Rules**：AI 可檢查：logo fill 只能為 Twitter blue 或 white；black exception 必須有 approval flag；不得改形、旋轉、動畫、擬聲或使用舊版。
9. **Reusable Knowledge**：核心 logo 的第一層規則應可被視覺 diff 與 metadata 檢查。
10. **Abstraction**：`Visual Identity`、`Brand Governance`。
11. **Visual Evidence**：文字規則旁的 bird logo 承擔標準形狀基準。

### Spacing

1. **Chapter Purpose**：避免 logo 被其他元素壓迫，維持辨識與品牌尊重。
2. **Definition**：logo 四周空白至少為 logo width 的 150%，最小寬度 16px。
3. **Relationship**：補足 Basics 的形狀保護，將環境空間也納入治理。
4. **Design Execution**：以 100%/150% 圖解讓 clearspace 可量測。
5. **Principles**：空間是 logo 系統的一部分。
6. **Frameworks**：Proportional Clearspace Model。
7. **Patterns**：Clearspace as Percentage of Mark Width。
8. **Rules**：AI 可檢查：logo bounding box 周圍 clearspace >= 1.5 x logo width；rendered width >= 16px。
9. **Reusable Knowledge**：比例型 clearspace 易於跨尺寸自動計算。
10. **Abstraction**：`Layout System`、`AI-Checkable Rules`。
11. **Visual Evidence**：clearspace diagram 與 16px minimum 圖示承擔測量證據。

### Color

1. **Chapter Purpose**：維持 logo 在不同背景上的可讀性與品牌色一致性。
2. **Definition**：Twitter logo 永遠 blue 或 white；圖片上使用 white；淺圖可加 10-20% black tint。
3. **Relationship**：將 Basics 的色彩規則放進背景選擇與影像情境。
4. **Design Execution**：用三種核准背景範例說明 blue-on-light、white-on-blue/dark、white-on-imagery。
5. **Principles**：可讀性與品牌色限制同等重要。
6. **Frameworks**：Background-Dependent Logo Color。
7. **Patterns**：Image Overlay Contrast Rule。
8. **Rules**：AI 可檢查：image background 上 logo 必須為 white；light image 應加 10-20% black tint 以維持 white logo legibility；非 blue/white logo 需 permission。
9. **Reusable Knowledge**：影像背景使用規範應包含 overlay/tint 建議，而不只是說「需有對比」。
10. **Abstraction**：`Color System`、`Accessibility-adjacent Contrast Governance`。
11. **Visual Evidence**：三組背景示例承擔情境比較功能。

### Social Icons

1. **Chapter Purpose**：讓 Twitter 在 social icon rows 中既一致又能配合第三方 creative。
2. **Definition**：icon logo 保持 blue/white；容器背景可配合 creative；與其他 social icons 等高等尺寸；minimum width 32px。
3. **Relationship**：是 logo rules 在社群連結 UI 元件中的特例。
4. **Design Execution**：提供 square、circular、logo-only、rounded square 等容器選項。
5. **Principles**：平台 icon 可容器化，但核心 bird 不可改。
6. **Frameworks**：Social Icon Component Rule。
7. **Patterns**：Container-flexible, Mark-fixed。
8. **Rules**：AI 可檢查：social icon minimum width >= 32px；Twitter icon 與其他 social icons 等尺寸等高度；logo 本身仍只能 blue/white；有可能時移除容器；容器限 circle/square/rounded square。
9. **Reusable Knowledge**：社群圖示需要處理 icon set harmonization，而非只處理單一 logo。
10. **Abstraction**：`UI Components`、`Logo System`。
11. **Visual Evidence**：四種 social icon 圖例與 32px 標記是主要證據。

## Logo Pairing Lockups

1. **Chapter Purpose**：讓 @handle 或 #hashtag 與 Twitter logo 並置時保持 platform attribution 而不暗示過度聯名。
2. **Definition**：定義 @handle/#hashtag lockup、text height 與 clearspace，同時列出大量 misuse。
3. **Relationship**：承接 Our Logo 的 spacing/color，並連接 Twitter marks 的商標限制。
4. **Design Execution**：以 lockup template 加 misuse board 強化正反邊界。
5. **Principles**：Twitter logo 可以指示「在 Twitter 上」，但不可被改造成任意活動標章。
6. **Frameworks**：Attribution Lockup Framework：logo + handle/hashtag + clearspace + type ownership。
7. **Patterns**：Platform Handle Lockup。
8. **Rules**：AI 可檢查：logo pairing 中 logo 必須 blue/white；text scale = 100% logo height；需遵守 clearspace；不得加 gradients、unapproved patterns、special effects、drop shadows、extra elements、anatomy、random textures；不得 personify、multiply、skew/rotate/stretch、stack multiple logos、與 headlines/other logos lock up。
9. **Reusable Knowledge**：平台品牌可提供 hashtag/handle lockup 以降低錯誤自製標章。
10. **Abstraction**：`Co-branding`、`Social Platform Attribution`、`AI-Checkable Rules`。
11. **Visual Evidence**：lockup diagram 與大量 don't examples；功能是模板與警示。

## Tweet Treatments

1. **Chapter Purpose**：保護 Tweet 作為平台內容的真實性、脈絡與權利邊界。
2. **Definition**：規範 marketing 中使用 Tweets：必須真實存在、不改訊息、使用指定 typography、保留 credit，第三方內容權利由使用者自行評估。
3. **Relationship**：從 logo/marks 的品牌治理進入 content rendering 與 legal risk。
4. **Design Execution**：以 Tweet treatment 範例、字體規格與 credit 條件建立可複製模板。
5. **Principles**：社群內容的價值依賴真實存在、不可篡改與清楚歸屬。
6. **Frameworks**：Tweet Rendering Integrity：existence、message fidelity、visual template、credit, rights.
7. **Patterns**：Platform Content Card Treatment。
8. **Rules**：AI 可檢查：Tweet 必須為平台上真實存在；不得 alter message；@handle/Tweet/timestamp 用 Helvetica Neue Regular；username 用 Helvetica Neue Bold；Tweet + Media template 不得 alter image；必須顯示 account full name、handle 與 Twitter logo；第三方 Tweet/logo/image 需 legal review。
9. **Reusable Knowledge**：引用平台內容時，內容真實性與視覺樣式同時是品牌規範。
10. **Abstraction**：`Content Design`、`Legal and Trademark`、`UI Components`。
11. **Visual Evidence**：白底與 dark mode Tweet treatments 圖例承擔模板示範。

## Twitter Marks

1. **Chapter Purpose**：擴大治理範圍，讓讀者知道 Twitter brand 不只 bird logo，還包含名稱與產品詞。
2. **Definition**：Twitter marks 包含 Twitter name、logo、Tweet、任何識別 Twitter product source/origin 的詞語圖像等。
3. **Relationship**：是 Legal 條款前的語義定義，告訴讀者哪些元素受保護。
4. **Design Execution**：分 naming/visual design、books/publications、merchandise、publishing content 等情境列規則。
5. **Principles**：品牌 mark 不能被第三方用成自己的產品、出版物或商品來源。
6. **Frameworks**：Trademark Scope + Use Context Matrix。
7. **Patterns**：Protected Marks Inventory。
8. **Rules**：AI 可檢查：Twitter/Tweet/Retweet 必須大寫首字；不得把 Twitter marks 納入公司、產品、服務、網站、domain、application 名稱；書籍/出版物需清楚表示 about Twitter, not by Twitter；除 hashtag/handle lockup 或 social icons 外，不允許製作販售贈送帶 Twitter name/logo 的商品。
9. **Reusable Knowledge**：Brand guideline 應把「可提及」與「可命名/可商品化」分開。
10. **Abstraction**：`Legal and Trademark`、`Naming`。
11. **Visual Evidence**：此章以分欄文字為主，功能是情境分類與法律邊界。

## Legal: Twitter Trademark Guidelines

1. **Chapter Purpose**：將前面設計規範提升為法律條款，明確違規會終止使用許可。
2. **Definition**：定義使用 Twitter trademarks 必須遵守 guidelines、Terms of Service、Twitter rules and policies；Twitter 保留修改、取消、核准/拒絕權利。
3. **Relationship**：是整份 guideline 的 enforcement layer。
4. **Design Execution**：以 numbered clauses 列出禁止變更、合理間距、不得暗示背書、不得貶損、不得引用其他產品、unique naming、trademark statement 等。
5. **Principles**：商標使用不是設計建議，而是有限、可撤銷、必須嚴格遵守的授權。
6. **Frameworks**：Trademark License Compliance。
7. **Patterns**：Legal Enforcement Appendix。
8. **Rules**：AI 可檢查：不得改比例/顏色/形狀或增減元素；marks 需獨立出現並與其他視覺/文字元素保持合理間距；不得妨礙完整 readability/display；不得暗示 sponsorship/endorsement；不得用於貶損；Tweet/Retweet marks 僅可指 Twitter products；需使用 unique product/app/site name；含 marks 的 materials 必須顯示 trademark statement：“TWITTER, TWEET, RETWEET and the Twitter Bird logo are trademarks of Twitter Inc. or its affiliates.”
9. **Reusable Knowledge**：設計 guideline 的 legal appendix 可直接轉為 policy lint rules。
10. **Abstraction**：`Legal and Trademark`、`Compliance`、`AI-Checkable Rules`。
11. **Visual Evidence**：文字條款是主要證據；功能是法律約束而非視覺示範。

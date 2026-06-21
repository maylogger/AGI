# Identité Visuelle Musée Zadkine

來源：`sources/Musee_zadkine.pdf`
研究視角：Design Infrastructure Researcher

## Summary

Musée Zadkine 的視覺識別規範，定義基礎元素、紙品、導視、出版、電子出版與衍生商品，並需遵守巴黎市政府的總體規則。建立 Musée Zadkine 的基礎識別語言，同時明確指出所有延展需服從巴黎市政府的總體規則。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。博物館品牌需要在作品材質與公共機構規範之間取得平衡。`institutional constraint -> base identity tokens -> application templates`。

執行上，這份 guideline 透過 Les éléments de base、Le logotype、Taille, marge et cartouche、Cohabitation and Interdits 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。文化機構 guideline 應把「總管理機構規則」寫在開頭，避免地方品牌與母體規範衝突。

## Les éléments de base

1. **Chapter Purpose**：建立 Musée Zadkine 的基礎識別語言，同時明確指出所有延展需服從巴黎市政府的總體規則。
2. **Definition**：涵蓋 logotype、尺寸、邊距、cartouche、cohabitation、禁用項、iconography、color、typography；不處理個別應用模板。
3. **Relationship**：此章是後續紙品、導視、出版、電子與衍生品的母系統。
4. **Design Execution**：以雕塑材質色彩、觸感影像與 Helvetica Neue 建立 museum identity 的物質性與現代秩序。
5. **Principles**：博物館品牌需要在作品材質與公共機構規範之間取得平衡。
6. **Frameworks**：`institutional constraint -> base identity tokens -> application templates`。
7. **Patterns**：以基礎元素章節集中管理所有 design tokens，再輸出到多種媒介。
8. **Rules**：AI 可檢查：logo 寬度不得小於 30 mm；logo 四周 margin 為 logo 寬度的 1/20；擾動背景使用白版或 cartouche；cartouche 顏色需來自 Musée Zadkine palette；禁用十項不可發生。
9. **Reusable Knowledge**：文化機構 guideline 應把「總管理機構規則」寫在開頭，避免地方品牌與母體規範衝突。
10. **Abstraction**：`Visual Identity`、`Color System`、`Typography System`、`Governance`。
11. **Visual Evidence**：色票、logo 版本、尺寸圖、cohabitation 圖與禁用圖是高密度視覺證據，支援自動與人工審核。

### Le logotype

1. **Chapter Purpose**：讓 museum identity 能在不同背景與印刷條件下穩定呈現。
2. **Definition**：定義 Granit、Ébène、Noyer、black、white logo 版本及 CMYK/RVB/Pantone 值。
3. **Relationship**：logo 版本與後續 cartouche、cohabitation、出版物應用直接連動。
4. **Design Execution**：用材質命名的色彩版本強化 Zadkine 雕塑語境。
5. **Principles**：logo 色彩不只是品牌色，也可承載機構收藏或媒介的材質隱喻。
6. **Frameworks**：`material color name -> reproduction values -> usage condition`。
7. **Patterns**：museum/material-based logo color system。
8. **Rules**：AI 可檢查：黑版僅用於黑白或極端 reproduction 條件；白版用於彩色、深色、深色攝影或複雜背景；不得任意改 logo 色。
9. **Reusable Knowledge**：色彩命名若來自品牌物質世界，可增加 guideline 的文化脈絡與記憶性。
10. **Abstraction**：`Logo System`、`Color System`。
11. **Visual Evidence**：每個 logo 色版搭配 CMYK/RVB/Pantone 表，是跨媒介複製證據。

### Taille, marge et cartouche

1. **Chapter Purpose**：保護 logo 在各種背景上的可讀性與呼吸空間。
2. **Definition**：最小尺寸 30 mm、四周 margin 為 logo 寬度 1/20、cartouche 用於白版不可行的擾動背景。
3. **Relationship**：接續 logo 版本，進一步定義放置條件。
4. **Design Execution**：以 5 cm logo 對應 0.25 cm margin 的例子讓規則可算。
5. **Principles**：可讀性可透過比例公式治理，而不是靠設計者目測。
6. **Frameworks**：`minimum size + proportional margin + background container fallback`。
7. **Patterns**：cartouche 作為 disturbed background fallback。
8. **Rules**：AI 可檢查：logo 寬度 < 30 mm 為違規；margin 必須 ≥ logo width/20；cartouche padding 同 margin；cartouche color 必須屬於官方 palette。
9. **Reusable Knowledge**：cartouche 應被定義為條件式 fallback，而不是任意裝飾容器。
10. **Abstraction**：`Logo System`、`Layout System`、`AI-Checkable Rules`。
11. **Visual Evidence**：尺寸與 cartouche 圖示支援比例計算與背景適配判斷。

### Cohabitation and Interdits

1. **Chapter Purpose**：治理多 logo 並置與常見錯誤，特別是公共機構與合作單位同時出現的情境。
2. **Definition**：logo 水平排列、以字母基線對齊，左右距離至少為 logotype 初始 M 高度的 2 倍；列出 10 項禁用。
3. **Relationship**：將單一 logo 規則延展到 co-branding/public institution 場景。
4. **Design Execution**：用 x spacing 與基線對齊降低主觀排版判斷。
5. **Principles**：多標誌關係需要幾何秩序，否則公共機構版面容易失控。
6. **Frameworks**：`horizontal alignment + baseline + 2M spacing + misuse blacklist`。
7. **Patterns**：cohabitation grid for public/cultural brands。
8. **Rules**：AI 可檢查：多 logo 必須水平排列；基線對齊；左右間距 ≥ 2 倍 M 高；不得改比例、改色、拆分 logo、變形、使用 outline、使用漸層、放置在降低可讀性的背景、加陰影、分開兩個字。
9. **Reusable Knowledge**：禁用項若用編號圖示，可直接轉成審核 checklist。
10. **Abstraction**：`Logo System`、`Governance`、`AI-Checkable Rules`。
11. **Visual Evidence**：cohabitation 圖與十大禁用圖是強審核證據。

### Iconography, Color and Typography

1. **Chapter Purpose**：將博物館的雕塑、材質與公共資訊轉成可重複的影像、色彩與字體語言。
2. **Definition**：影像偏好材質和觸感；色彩來自木、石等雕塑材料；主字體 Helvetica Neue，替代字體 Arial。
3. **Relationship**：補足 logo 以外的 visual language，並支援所有應用模板。
4. **Design Execution**：透過 close-up、foreground material、sculpture detail、材質色票與字體族建立整體感。
5. **Principles**：文化機構視覺應讓作品特質成為系統來源。
6. **Frameworks**：`collection material -> image direction -> color palette -> typography hierarchy`。
7. **Patterns**：collection-derived design tokens。
8. **Rules**：AI 可檢查：攝影應優先呈現材質/觸感或作品局部；色彩需取自 Granit、Ébène、Noyer、Orme、Marbre、Pierre；印刷使用 Helvetica Neue；bureau/internet 僅在 Helvetica Neue 不可用時使用 Arial。
9. **Reusable Knowledge**：博物館品牌可從館藏材質抽象出色彩與影像方向，形成可複用的 cultural identity pattern。
10. **Abstraction**：`Photography System`、`Color System`、`Typography System`。
11. **Visual Evidence**：影像方向頁、色票表、字體 specimen 是基礎 token 的證據。

## La papeterie

1. **Chapter Purpose**：把 museum identity 放進最日常、最正式的文具系統。
2. **Definition**：名片、信紙、correspondence card、信封、便條紙、電子簽名與 museum stamp。
3. **Relationship**：直接使用基礎 logo、色彩、字體與地址資訊。
4. **Design Execution**：以樣張和固定資訊欄位建立低變動的行政模板。
5. **Principles**：公共文化機構的文具需同時有質感、正式性與資訊清楚度。
6. **Frameworks**：`identity token -> fixed institutional fields -> template by object type`。
7. **Patterns**：stationery template system。
8. **Rules**：AI 可檢查：名片建議使用 Conquéror Vergé 350g 或同級創作紙；名片正面色彩需從官方 palette 選擇；電子簽名需包含姓名、職稱、email、電話、地址與網站；印章尺寸為 59 x 23 mm。
9. **Reusable Knowledge**：文具規範應標示材質/紙張建議，因紙張是文化品牌觸感的重要媒介。
10. **Abstraction**：`Business Collateral`、`Operations`、`Print System`。
11. **Visual Evidence**：各文具樣張承擔欄位、比例與版面證據。

## La signalétique

1. **Chapter Purpose**：讓館內外導視與活動指示維持同一機構身份。
2. **Definition**：包含 institutional/exhibition calicot、入口門面與 badges。
3. **Relationship**：將基礎識別應用到空間與訪客接觸點。
4. **Design Execution**：以 banners、door 與 badge 樣張示範 logo、文字、網址與展覽名稱如何排布。
5. **Principles**：導視是公共服務，不應因視覺表現犧牲辨識。
6. **Frameworks**：`visitor touchpoint -> object template -> identity placement`。
7. **Patterns**：museum signage application set。
8. **Rules**：AI 可檢查：badge 可有姓名或無姓名兩種版本；展覽 calicot 需包含展期/展名/網址等必要資訊；空間應用不得違反基礎 logo 尺寸與 margin。
9. **Reusable Knowledge**：導視章節可用 object-based templates，比抽象規則更能避免施工錯誤。
10. **Abstraction**：`Wayfinding`、`Environmental Graphics`、`Operations`。
11. **Visual Evidence**：calicot、door、badge 圖示是實際空間物件證據。

## L’édition

1. **Chapter Purpose**：治理博物館最複雜的傳播場景：機構出版與展覽/活動出版。
2. **Definition**：涵蓋海報、明信片、參觀摺頁、宣傳摺頁、邀請卡、flyer、新聞稿、press kit、資料夾、廣告、展覽目錄與 co-editions。
3. **Relationship**：這章把基礎識別轉成大量版式模板，並處理與巴黎市政府 charte 的關係。
4. **Design Execution**：以實際尺寸與樣張定義不同媒體：40x60 cm、118x175 cm、210x176、4x3 m、320x240 cm、200x150 cm、A5 等。
5. **Principles**：展覽溝通需要允許內容更換，但品牌結構與公共資訊必須保持一致。
6. **Frameworks**：`communication type -> format size -> template composition -> institutional constraints`。
7. **Patterns**：publication template matrix。
8. **Rules**：AI 可檢查：指定格式應使用對應模板尺寸；參觀摺頁與 dépliant d’appel 需依巴黎市政府 charte 並使用 VistaSans；co-editions logo 水平排列、基線對齊、左右距離至少 2M。
9. **Reusable Knowledge**：出版章節應將「內容變動區」與「固定 institutional footer/identity 區」拆開治理。
10. **Abstraction**：`Editorial Design`、`Print System`、`Governance`。
11. **Visual Evidence**：大量 poster/flyer/press/catalouge/mockup 樣張是此章主要證據，功能是版式、尺寸與資訊層級示範。

### Communication institutionnelle

1. **Chapter Purpose**：建立博物館常態機構溝通的固定語氣與格式。
2. **Definition**：包含 institution poster、postcard、參觀摺頁與宣傳摺頁。
3. **Relationship**：承接基礎元素，且在部分文件中服從巴黎市政府 charte。
4. **Design Execution**：用固定尺寸和網站/地址/開館時間等資訊欄位維持公共服務一致。
5. **Principles**：機構型出版應比活動型更穩定，承載博物館本身而非單次展覽。
6. **Frameworks**：`institutional identity + public information + format scale`。
7. **Patterns**：evergreen museum communication templates。
8. **Rules**：AI 可檢查：dépliant d’aide à la visite 與 dépliant d’appel 使用 VistaSans；色帶從 Musée Zadkine palette 選擇；海報格式需符合列示尺寸。
9. **Reusable Knowledge**：母機構 charte 與子品牌 palette 可以透過「字體遵母、色彩取子」方式共存。
10. **Abstraction**：`Editorial Design`、`Governance`。
11. **Visual Evidence**：機構海報與摺頁樣張展示固定資訊與品牌區域。

### Communication évènementielle

1. **Chapter Purpose**：讓展覽與活動有足夠表現力，但仍維持 Zadkine identity。
2. **Definition**：包含 event poster、invitation、flyer、press release、press kit、folder、advertising inserts、exhibition catalogues、co-editions。
3. **Relationship**：相較 institutional communication，此節容納展名、展期、圖片與策展資訊的高度變化。
4. **Design Execution**：以多尺寸海報與活動物件樣張定義內容可替換區與固定身份欄位。
5. **Principles**：事件識別應在變化中保留 institution signature。
6. **Frameworks**：`event content -> campaign asset family -> institutional signature`。
7. **Patterns**：exhibition campaign kit。
8. **Rules**：AI 可檢查：活動素材需包含展名、展期、地點/網址等必要資訊；catalogue cartouche size 固定，標題長度透過 typography size 調整；co-editions 遵循 cohabitation spacing。
9. **Reusable Knowledge**：展覽品牌模板應允許標題長短變化，但固定容器尺寸能維持系列一致。
10. **Abstraction**：`Campaign System`、`Editorial Design`、`Print System`。
11. **Visual Evidence**：活動海報、邀請卡、flyer、press templates 與 catalogue cover 是版式族譜證據。

## L’édition électronique

1. **Chapter Purpose**：將印刷識別轉換到 email、web invitation、animated banners 與 newsletter。
2. **Definition**：包含 web invitation、animated institutional/event banners、e-newsletter，提供 jpg/pdf 與常見廣告尺寸。
3. **Relationship**：承接出版模板，但需要適應數位尺寸、動畫與 email 使用。
4. **Design Execution**：以 728x90、160x600、300x250 等標準 banner 尺寸示範資訊壓縮與視覺滑動/固定圖策略。
5. **Principles**：數位出版不是縮小印刷品，而是依格式重新排列必要資訊。
6. **Frameworks**：`digital object type -> fixed pixel dimensions -> information hierarchy -> motion/static choice`。
7. **Patterns**：digital banner adaptation pattern。
8. **Rules**：AI 可檢查：web invitation 用 jpg 插入 email、pdf 作附件；banner 應使用指定尺寸；若視覺素材適合，可上下滾動，否則用固定圖；newsletter 需保留日期、主題、CTA、取消訂閱等資訊。
9. **Reusable Knowledge**：電子出版 guideline 應定義像素尺寸與檔案使用方式，否則印刷模板很難正確轉譯。
10. **Abstraction**：`Digital Publishing`、`Responsive/Format Adaptation`、`Motion Identity`。
11. **Visual Evidence**：banner 與 newsletter 樣張提供尺寸、資訊取捨與動畫方向證據。

## Produits dérivés

1. **Chapter Purpose**：讓博物館商店與紀念商品維持機構識別，不變成隨意貼 logo。
2. **Definition**：包含 stylo、mug、sac、signet 等商品應用。
3. **Relationship**：將基礎 logo、色彩與網站資訊延展到物件與商品化場景。
4. **Design Execution**：以物件 mockup 控制 logo/網址在曲面、布面與小尺寸物件上的放置。
5. **Principles**：衍生品是品牌接觸點，也應遵守同一身份系統。
6. **Frameworks**：`object type -> imprint area -> identity placement -> readability`。
7. **Patterns**：museum merchandise application set。
8. **Rules**：AI 可檢查：商品上的 logo/網址需符合最小尺寸與 margin；小物件不得使用導致可讀性不足的複雜版面；不得任意改色或拆分 logo。
9. **Reusable Knowledge**：衍生品規範應將物件表面限制納入版面判斷。
10. **Abstraction**：`Merchandise System`、`Operations`。
11. **Visual Evidence**：筆、馬克杯、袋、書籤樣張是物件尺度與品牌放置證據。

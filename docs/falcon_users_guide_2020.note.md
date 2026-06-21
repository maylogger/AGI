# Falcon User’s Guide

來源：`sources/falcon_users_guide_2020.pdf`
版本：April 2020
研究視角：Design Infrastructure Researcher

## Summary

SpaceX Falcon launch service planning guide, defining vehicle capabilities, payload environments, interfaces, facilities, mission integration, operations, safety, and quick reference material for pre-contract customers.。建立文件的使用邊界，避免客戶把預合約規劃資料誤用為詳細設計依據；沒有此章會讓後續數據的法律、工程與協作責任不清。

最上層的原則是先建立判斷標準，再進入視覺、語氣或應用規格。simplicity、reliability、cost effectiveness、commonality、testability、human-rating safety margins。以「目的與限制 -> 能力與安全 -> 可靠性證據 -> 商務入口」建立客戶 onboarding framework。

執行上，這份 guideline 透過 Introduction、Vehicles、Performance、Environments 等章節，把抽象原則落到可操作的資產、版面、語氣、流程或治理規則。任何工程服務 guideline 都應先分離「通用規劃資訊」與「專案設計資料」，避免錯誤承諾。

## Introduction

1. **Chapter Purpose**：建立文件的使用邊界，避免客戶把預合約規劃資料誤用為詳細設計依據；沒有此章會讓後續數據的法律、工程與協作責任不清。
2. **Definition**：定義 Falcon guide 是 mission planning document，適用 5.2 m fairing Falcon configurations 與標準發射服務；不負責 mission-specific detailed design。
3. **Relationship**：作為全文件前置契約，後續 Vehicles、Performance、Interfaces、Operations 都依賴這裡建立的服務範圍與可靠性敘事。
4. **Design Execution**：作者用公司描述、系統共通性、安全特徵與可靠性原因，先建立客戶信任，再引導讀者接受後續技術門檻。
5. **Principles**：simplicity、reliability、cost effectiveness、commonality、testability、human-rating safety margins。
6. **Frameworks**：以「目的與限制 -> 能力與安全 -> 可靠性證據 -> 商務入口」建立客戶 onboarding framework。
7. **Patterns**：高風險服務 guideline 先聲明適用範圍，再列出可被驗證的可靠性設計原因。
8. **Rules**：AI 可檢查：文件用途必須標示為 pre-contract planning；詳細設計資料必須透過 mission manager 交換；價格需引用官方 capabilities 頁；可靠性論述需連回 engine、avionics、stage separation 三類失效風險。
9. **Reusable Knowledge**：任何工程服務 guideline 都應先分離「通用規劃資訊」與「專案設計資料」，避免錯誤承諾。
10. **Abstraction**：`Knowledge Architecture`、`Governance`、`Compliance`、`AI-Checkable Rules`。
11. **Visual Evidence**：使用車輛比較圖、安全特徵表與可靠性表格作為信任證據，功能是把工程承諾轉成可審查的架構證明。

## Vehicles

1. **Chapter Purpose**：讓客戶理解 Falcon 9 與 Falcon Heavy 的共通平台、差異與基本硬體邊界；沒有此章，payload planning 無法判斷可用載具。
2. **Definition**：定義 launch vehicle architecture、structures、propulsion、separation systems、avionics、coordinate frame；不處理 Dragon 專用能力。
3. **Relationship**：承接 Introduction 的可靠性敘事，並為 Performance、Environments、Interfaces 提供硬體基礎。
4. **Design Execution**：用 vehicle overview、dimension table、engine layout、coordinate frame 把複雜系統拆成可引用模組。
5. **Principles**：platform commonality、pneumatic separation、fault tolerance、coordinate precision、minimum unique infrastructure。
6. **Frameworks**：載具描述框架為「configuration -> structure/propulsion -> release/separation -> avionics/GNC -> coordinate reference」。
7. **Patterns**：將硬體系統轉成表格化 characteristics，並用標準座標系消除跨團隊語義差異。
8. **Rules**：AI 可檢查：Falcon 9 fairing configuration 應標示 LOX/RP-1 two-stage；Falcon Heavy 應標示 three first-stage cores；payload coordinate reference 必須含 X/Y/Z 軸定義；separation system 應描述 pneumatic, low-shock, testable。
9. **Reusable Knowledge**：技術 guideline 應用固定模組描述產品平台，避免每個客戶用不同語言理解介面。
10. **Abstraction**：`Product Language`、`Information Design`、`Technical Interface System`。
11. **Visual Evidence**：車輛外觀圖、engine layout、dimension table 與 coordinate frame 圖承擔比例、命名與空間參照功能。

## Performance

1. **Chapter Purpose**：把 launch capability 轉成客戶可初步規劃的軌道、質量、姿態與 deployment 條件。
2. **Definition**：定義 injection orbits、mass-to-orbit、mass properties、launch windows、attitude control、separation modes、multiple payload options。
3. **Relationship**：依賴 Vehicles 的硬體能力，並直接影響 Interfaces、Mission Integration 與 Operations 的需求收斂。
4. **Design Execution**：作者用可用軌道表、能力限制與「contact SpaceX」邊界，把公開資料與需專案分析的部分分開。
5. **Principles**：capability disclosure with constraint management、mission-specific validation、performance tradeoff transparency。
6. **Frameworks**：決策框架是「目標軌道 -> launch site -> vehicle -> mass property -> separation service -> nonstandard request」。
7. **Patterns**：以表格列通用選項，以文字標示性能懲罰或需洽詢項目。
8. **Rules**：AI 可檢查：每個 orbit row 必須包含 inclination range、vehicle、launch site；GTO/GSO/Earth escape 需標示可用基地；payload mass properties 超出圖示限制時必須標示 mission-unique coordination。
9. **Reusable Knowledge**：能力 guideline 應讓讀者先做 coarse planning，再明確指出何時進入客製分析。
10. **Abstraction**：`Decision Framework`、`Operations`、`Measurement`。
11. **Visual Evidence**：orbit service table 與 payload CG capability plot 是主要證據，功能是把性能限制視覺化為 planning envelope。

## Environments

1. **Chapter Purpose**：定義 payload 從運輸到飛行會遇到的最大預期環境，作為 customer verification 的基準。
2. **Definition**：涵蓋 transportation、temperature/humidity/cleanliness、loads、vibration、acoustic、shock、random vibration、EMI、pressure、thermal、free molecular heating。
3. **Relationship**：把 Vehicles 的工程特性轉成客戶 payload design 與 test campaign 的環境需求，並連到 Section 7 deliverables。
4. **Design Execution**：作者以曲線、頻譜、表格與 verification example，把抽象環境風險變成可量測規格。
5. **Principles**：envelope-based design、mission-specific analysis、margin disclosure、test evidence over verbal assurance。
6. **Frameworks**：環境規範框架是「source environment -> maximum expected level -> safety margin status -> customer verification activity」。
7. **Patterns**：每類環境用圖表建立 envelope，再用文字說明是否含 margin 與何時需專案調整。
8. **Rules**：AI 可檢查：EMI safety margin 須為 6 dB；fairing pressure decay rate 須不大於 0.40 psi/sec，短時段例外不大於 0.65 psi/sec 且不超過 5 秒；verification table 必須對每類環境列出 customer responsibility。
9. **Reusable Knowledge**：高可靠 guideline 應把「我們預期的環境」與「你必須提供的驗證」放在同一章，降低責任落差。
10. **Abstraction**：`Compliance`、`Measurement`、`AI-Checkable Rules`、`Risk Governance`。
11. **Visual Evidence**：大量曲線、頻譜與表格作為工程 envelope 證據，功能是驗證、比較與風險治理。

## Interfaces

1. **Chapter Purpose**：定義 SpaceX 與客戶 payload 之間的機械、電氣、命令與 timing 接點，避免介面假設不一致。
2. **Definition**：包含 1575-mm bolted interface、fairing envelope、access doors、RF antenna、payload electrical connectivity、separation commands、breakwire indication、IRIG timing。
3. **Relationship**：把 Vehicles 與 Performance 的能力落到實際 payload integration 接面，也支撐 Operations 的流程安排。
4. **Design Execution**：作者用標準值、替代尺寸、可標準服務與 nonstandard service 的分界來治理複雜介面。
5. **Principles**：standard interface first、mission-unique exceptions controlled、physical access before encapsulation、electrical availability by phase。
6. **Frameworks**：介面治理框架是「standard interface -> optional standard accommodation -> nonstandard service -> verification requirement」。
7. **Patterns**：用 phase table 表示 electrical availability，讓不同時間點的責任與連線狀態可被檢查。
8. **Rules**：AI 可檢查：standard mechanical interface 必須為 1575 mm / 62.01 in；fairing maximum dynamic envelope 必須標示 4.6 m diameter 與 11 m height；flight phase 不提供 payload command/telemetry access as standard service；至少一個 loopback circuit 需用於 separation indication。
9. **Reusable Knowledge**：介面 guideline 應用「標準、例外、驗證」三層，讓工程、商務與操作流程一致。
10. **Abstraction**：`Interface Design`、`Operations`、`Governance`。
11. **Visual Evidence**：fairing envelope 圖、connectivity table 與 cable length table 承擔空間、流程與限制證據功能。

## Facilities

1. **Chapter Purpose**：讓客戶理解每個 launch site 與 support facility 的地理、設備與 accommodation 條件。
2. **Definition**：定義 East Coast facilities、Vandenberg、Hawthorne、McGregor、Washington DC 等場域角色。
3. **Relationship**：承接 Performance 的 launch site choice，並影響 Operations 的 processing、integration、transport 與 personnel planning。
4. **Design Execution**：用 facility-by-facility 描述把服務能力與地點限制分開，讓客戶可做 logistics planning。
5. **Principles**：site specificity、operational readiness、customer accommodation、range dependency。
6. **Frameworks**：場域框架是「launch capability -> payload processing -> personnel access -> support facility」。
7. **Patterns**：每個設施以功能、地點與可用服務描述，形成可重複的 facility profile。
8. **Rules**：AI 可檢查：每個 launch site 應標示 location、range、payload processing relation；personnel accommodation 需分別列於 CCAFS/KSC 與 VAFB。
9. **Reusable Knowledge**：大型服務 guideline 應將 physical infrastructure 視為 customer journey 的一部分，而不是附錄。
10. **Abstraction**：`Operations`、`Service Blueprint`、`Infrastructure Profile`。
11. **Visual Evidence**：場域照片與平面資訊主要作為情境與信任證據，協助客戶想像實際作業環境。

## Mission Integration and Services

1. **Chapter Purpose**：定義從 contracting 到 deliverables 的協作模型，讓客戶知道哪些服務標準包含、哪些需要額外協調。
2. **Definition**：涵蓋 contracting、mission management、standard services、schedule、customer deliverables。
3. **Relationship**：把前面能力與介面章節轉成專案管理節奏，並預告 Operations 的實作流程。
4. **Design Execution**：作者將 mission manager 作為中心節點，讓所有 technical exchange 都有明確窗口。
5. **Principles**：single accountable interface、standard service clarity、deliverable-driven integration。
6. **Frameworks**：任務整合框架是「contract -> mission manager -> standard/nonstandard service -> schedule -> deliverables」。
7. **Patterns**：以 deliverable table 治理雙方文件交換，避免只用會議溝通。
8. **Rules**：AI 可檢查：所有 nonstandard service 必須標示需協調；customer deliverables 必須對應 schedule milestone；mission manager 是技術資料交換角色。
9. **Reusable Knowledge**：任何 B2B technical guideline 都需要把服務邊界轉成 deliverable governance。
10. **Abstraction**：`Operations`、`Governance`、`Service Contracting`。
11. **Visual Evidence**：schedule 與 deliverables table 承擔流程與責任證據功能。

## Operations

1. **Chapter Purpose**：將 spacecraft 從交付、處理、整合、發射到 post-launch report 的流程標準化。
2. **Definition**：定義 delivery、transportation、processing、joint operations、launch organization、control centers、rollout、countdown、scrub、ascent、separation、disposal。
3. **Relationship**：操作章是前面所有能力、環境、介面與整合要求的實際執行路徑。
4. **Design Execution**：以 chronological flow 描述任務，降低客戶對現場活動、停點與責任切換的未知。
5. **Principles**：sequence control、access control、contingency planning、mission-specific coordination。
6. **Frameworks**：操作框架是「arrival -> processing -> encapsulation -> integration -> rollout -> countdown -> flight -> report」。
7. **Patterns**：用 sample mission profile 將抽象作業轉為可預期時間序列。
8. **Rules**：AI 可檢查：encapsulation 後 payload access 受限；rollout 與 launch pad operations 必須連到 electrical interface availability；scrub/recycle 需有流程說明；post-launch reports 必須列入 flight operations。
9. **Reusable Knowledge**：作業 guideline 應以時間序列連接介面狀態、現場權限與資料交付。
10. **Abstraction**：`Operations`、`Service Blueprint`、`Process Governance`。
11. **Visual Evidence**：mission profile 圖與流程表作為時間、責任與作業順序證據。

## Safety

1. **Chapter Purpose**：明確規範客戶 payload safety 責任與 waiver 機制，降低發射場高風險作業的不確定性。
2. **Definition**：涵蓋 safety requirements、hazardous systems and operations、waivers。
3. **Relationship**：承接 Introduction 的安全設計承諾，並落實到 Operations 的現場行為與 customer compliance。
4. **Design Execution**：用簡短章節把安全責任從技術描述中抽出，使它具有 governance 優先權。
5. **Principles**：compliance before operations、hazard disclosure、controlled exception。
6. **Frameworks**：安全框架是「requirement -> hazard identification -> operational control -> waiver」。
7. **Patterns**：將 waiver 作為例外治理模組，而不是隱性協商。
8. **Rules**：AI 可檢查：所有 hazardous operations 必須在 mission integration 中揭露；不符合安全要求的項目需以 waiver 形式處理；waiver 不應省略風險與批准路徑。
9. **Reusable Knowledge**：高風險 guideline 必須把 exception handling 寫成正式流程。
10. **Abstraction**：`Compliance`、`Governance`、`Risk Management`。
11. **Visual Evidence**：此章偏文字治理，視覺證據較少；其證據功能由流程要求與 waiver language 承擔。

## Contact Information

1. **Chapter Purpose**：提供從文件轉入正式溝通的出口，避免讀者在 nonstandard 或 mission-specific 問題上自行推斷。
2. **Definition**：定義 Falcon services contact path。
3. **Relationship**：補足全文件多處「contact SpaceX」的行動落點。
4. **Design Execution**：將聯絡資訊獨立成章，讓它成為所有例外與客製需求的共同出口。
5. **Principles**：clear escalation、single source of inquiry、controlled interpretation。
6. **Frameworks**：聯絡框架是「公開 guide -> 客戶疑問 -> official contact -> mission-specific exchange」。
7. **Patterns**：在 guideline 中所有未公開數據都應導向官方聯絡節點。
8. **Rules**：AI 可檢查：文件若出現 mission-unique、upon request、contact 等描述，必須能在 contact section 找到後續路徑。
9. **Reusable Knowledge**：guideline 不應讓讀者用公開資料填補未公開規格；應提供可追溯聯絡節點。
10. **Abstraction**：`Operations`、`Governance`。
11. **Visual Evidence**：通常不需要視覺；資訊設計重點是可尋址性。

## Quick Reference

1. **Chapter Purpose**：集中圖表、表格、縮寫與變更紀錄，提高工程文件可檢索性與版本治理能力。
2. **Definition**：包含 list of figures、list of tables、list of acronyms、change log。
3. **Relationship**：作為全文件的導航與維護層，支援跨章節查找與版本比較。
4. **Design Execution**：把 reference material 從內容章節抽出，降低主文負擔。
5. **Principles**：traceability、maintainability、fast lookup、version awareness。
6. **Frameworks**：參照框架是「figures -> tables -> acronyms -> change log」。
7. **Patterns**：技術 guideline 應提供獨立 quick reference，讓使用者不用全文搜尋。
8. **Rules**：AI 可檢查：所有圖表引用應出現在 reference list；acronym 應有定義；change log 應可指出文件更新歷史。
9. **Reusable Knowledge**：長篇規範文件需要 metadata chapter 作為資訊治理基礎。
10. **Abstraction**：`Knowledge Architecture`、`Documentation System`。
11. **Visual Evidence**：以列表而非圖像承擔 evidence map 功能，讓使用者快速定位原始證據。

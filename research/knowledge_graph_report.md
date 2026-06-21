# AGI Knowledge Graph Report

產生日期：2026-06-21
產生命令：`python scripts/compile_knowledge_graph.py`

## 摘要

- 已驗證決策卡：**34**（至少一筆有效 evidence）
- 未驗證決策卡：**0**
- sidecar 檔數：**125**；原始卡片數（合併前）：**455**
- contexts/modules 引用但尚未萃取（backlog）：**0**

## 決策卡（依信心排序）

| dp-id | 支持品牌數 | confidence | 模組 | 適用產業 |
|-------|-----------|-----------|------|----------|
| `dp-origin-story-before-rules` | 6 | 0.95 | Brand Strategy | nonprofit_social, consumer_retail_hospitality |
| `dp-clearspace-from-logo-geometry` | 71 | 0.95 | Visual Identity | public_sector |
| `dp-cobranding-grid-governance` | 37 | 0.95 | Brand Architecture | finance, tech_software, public_sector, education, nonprofit_social, media_entertainment, consumer_retail_hospitality |
| `dp-monochrome-logo-by-contrast` | 37 | 0.95 | Visual Identity | finance |
| `dp-platform-before-visual-rules` | 45 | 0.95 | Brand Strategy | industrial_materials_science, tech_software, media_entertainment, finance, education, public_sector, nonprofit_social, consumer_retail_hospitality, new_energy_mobility |
| `dp-from-to-voice-translation` | 9 | 0.95 | Voice and Tone | industrial_materials_science, tech_software, finance, public_sector, nonprofit_social, education |
| `dp-personality-words-as-evaluation-criteria` | 26 | 0.95 | Brand Strategy | industrial_materials_science, nonprofit_social, tech_software, education, finance, consumer_retail_hospitality, media_entertainment, public_sector |
| `dp-system-toolkit-over-template` | 16 | 0.95 | Visual Language | industrial_materials_science, tech_software, consumer_retail_hospitality, finance, media_entertainment, education, public_sector |
| `dp-logo-vs-lockup-distinction` | 8 | 0.95 | Visual Identity | industrial_materials_science, finance, tech_software, media_entertainment, education |
| `dp-color-set-over-single-pickers` | 4 | 0.95 | Color System | industrial_materials_science, media_entertainment, nonprofit_social, tech_software |
| `dp-contact-before-appendix` | 21 | 0.95 | Governance | finance, tech_software, industrial_materials_science, public_sector, nonprofit_social, media_entertainment, education |
| `dp-custom-typeface-as-identity-asset` | 13 | 0.95 | Typography System | industrial_materials_science, tech_software, public_sector, media_entertainment, new_energy_mobility |
| `dp-trademark-permission-flow` | 21 | 0.95 | Legal and Trademark | tech_software, finance, education, public_sector, media_entertainment, consumer_retail_hospitality, new_energy_mobility |
| `dp-media-split-typography` | 12 | 0.95 | Typography System | finance, public_sector, education, nonprofit_social |
| `dp-bold-contrast-for-challenger` | 8 | 0.95 | Color System | tech_software, media_entertainment |
| `dp-approval-gate-for-exceptions` | 18 | 0.95 | Governance | public_sector, finance, luxury_premium, consumer_retail_hospitality, education, tech_software, industrial_materials_science, media_entertainment |
| `dp-modular-manual-for-public-units` | 33 | 0.95 | Brand Architecture | public_sector, education, media_entertainment, luxury_premium, finance, consumer_retail_hospitality, nonprofit_social, tech_software |
| `dp-restrained-palette-for-trust` | 11 | 0.95 | Color System | public_sector, finance, tech_software, media_entertainment |
| `dp-accessible-contrast-pairs` | 9 | 0.95 | Accessibility | education, public_sector, nonprofit_social, finance, tech_software |
| `dp-one-brand-one-voice-governance` | 6 | 0.95 | Governance | tech_software, finance, public_sector, nonprofit_social, media_entertainment, new_energy_mobility |
| `dp-asset-protection-for-legacy` | 9 | 0.95 | Visual Identity | luxury_premium, finance, media_entertainment, public_sector |
| `dp-palette-roles-and-usage-limits` | 5 | 0.95 | Color System | finance, consumer_retail_hospitality, luxury_premium, nonprofit_social |
| `dp-persona-driven-voice` | 5 | 0.95 | Voice and Tone | tech_software, media_entertainment, finance |
| `dp-content-forward-flexible-identity` | 4 | 0.95 | Visual Language | media_entertainment, public_sector |
| `dp-responsible-framing-for-regulated-category` | 3 | 0.85 | Content Design | finance, tech_software |
| `dp-bilingual-identity-system` | 3 | 0.85 | Typography System | public_sector, finance, education |
| `dp-restraint-as-luxury-signal` | 3 | 0.85 | Voice and Tone | luxury_premium |
| `dp-editorial-typography-for-premium` | 3 | 0.85 | Typography System | luxury_premium, media_entertainment |
| `dp-message-hierarchy-by-persona` | 2 | 0.70 | Messaging | tech_software, media_entertainment |
| `dp-name-usage-governance` | 2 | 0.70 | Legal and Trademark | finance, public_sector, luxury_premium |
| `dp-story-framework-category-education` | 2 | 0.70 | Messaging | new_energy_mobility, tech_software |
| `dp-inclusive-language-governance` | 1 | 0.50 | Content Design | nonprofit_social, public_sector |
| `dp-cheatsheet-for-mass-touchpoints` | 1 | 0.50 | Operations | consumer_retail_hospitality |
| `dp-compliance-copy-as-layout-system` | 1 | 0.50 | Compliance | finance |

## 反向索引：產業 → 決策卡

- **consumer_retail_hospitality**：dp-approval-gate-for-exceptions, dp-cheatsheet-for-mass-touchpoints, dp-cobranding-grid-governance, dp-modular-manual-for-public-units, dp-origin-story-before-rules, dp-palette-roles-and-usage-limits, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **education**：dp-accessible-contrast-pairs, dp-approval-gate-for-exceptions, dp-bilingual-identity-system, dp-cobranding-grid-governance, dp-contact-before-appendix, dp-from-to-voice-translation, dp-logo-vs-lockup-distinction, dp-media-split-typography, dp-modular-manual-for-public-units, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **finance**：dp-accessible-contrast-pairs, dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-bilingual-identity-system, dp-cobranding-grid-governance, dp-compliance-copy-as-layout-system, dp-contact-before-appendix, dp-from-to-voice-translation, dp-logo-vs-lockup-distinction, dp-media-split-typography, dp-modular-manual-for-public-units, dp-monochrome-logo-by-contrast, dp-name-usage-governance, dp-one-brand-one-voice-governance, dp-palette-roles-and-usage-limits, dp-persona-driven-voice, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-responsible-framing-for-regulated-category, dp-restrained-palette-for-trust, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **industrial_materials_science**：dp-approval-gate-for-exceptions, dp-color-set-over-single-pickers, dp-contact-before-appendix, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-logo-vs-lockup-distinction, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-system-toolkit-over-template
- **luxury_premium**：dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-editorial-typography-for-premium, dp-modular-manual-for-public-units, dp-name-usage-governance, dp-palette-roles-and-usage-limits, dp-restraint-as-luxury-signal
- **media_entertainment**：dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-bold-contrast-for-challenger, dp-cobranding-grid-governance, dp-color-set-over-single-pickers, dp-contact-before-appendix, dp-content-forward-flexible-identity, dp-custom-typeface-as-identity-asset, dp-editorial-typography-for-premium, dp-logo-vs-lockup-distinction, dp-message-hierarchy-by-persona, dp-modular-manual-for-public-units, dp-one-brand-one-voice-governance, dp-persona-driven-voice, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-restrained-palette-for-trust, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **new_energy_mobility**：dp-custom-typeface-as-identity-asset, dp-one-brand-one-voice-governance, dp-platform-before-visual-rules, dp-story-framework-category-education, dp-trademark-permission-flow
- **nonprofit_social**：dp-accessible-contrast-pairs, dp-cobranding-grid-governance, dp-color-set-over-single-pickers, dp-contact-before-appendix, dp-from-to-voice-translation, dp-inclusive-language-governance, dp-media-split-typography, dp-modular-manual-for-public-units, dp-one-brand-one-voice-governance, dp-origin-story-before-rules, dp-palette-roles-and-usage-limits, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules
- **public_sector**：dp-accessible-contrast-pairs, dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-bilingual-identity-system, dp-clearspace-from-logo-geometry, dp-cobranding-grid-governance, dp-contact-before-appendix, dp-content-forward-flexible-identity, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-inclusive-language-governance, dp-media-split-typography, dp-modular-manual-for-public-units, dp-name-usage-governance, dp-one-brand-one-voice-governance, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-restrained-palette-for-trust, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **tech_software**：dp-accessible-contrast-pairs, dp-approval-gate-for-exceptions, dp-bold-contrast-for-challenger, dp-cobranding-grid-governance, dp-color-set-over-single-pickers, dp-contact-before-appendix, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-logo-vs-lockup-distinction, dp-message-hierarchy-by-persona, dp-modular-manual-for-public-units, dp-one-brand-one-voice-governance, dp-persona-driven-voice, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-responsible-framing-for-regulated-category, dp-restrained-palette-for-trust, dp-story-framework-category-education, dp-system-toolkit-over-template, dp-trademark-permission-flow

## 反向索引：品牌類型 → 決策卡

- **category_creator**：dp-bold-contrast-for-challenger, dp-content-forward-flexible-identity, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-story-framework-category-education, dp-system-toolkit-over-template
- **challenger**：dp-bold-contrast-for-challenger, dp-contact-before-appendix, dp-content-forward-flexible-identity, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-message-hierarchy-by-persona, dp-persona-driven-voice, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-responsible-framing-for-regulated-category, dp-restrained-palette-for-trust, dp-story-framework-category-education
- **heritage_legacy**：dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-compliance-copy-as-layout-system, dp-custom-typeface-as-identity-asset, dp-editorial-typography-for-premium, dp-from-to-voice-translation, dp-logo-vs-lockup-distinction, dp-modular-manual-for-public-units, dp-name-usage-governance, dp-one-brand-one-voice-governance, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-restrained-palette-for-trust, dp-restraint-as-luxury-signal, dp-system-toolkit-over-template
- **institutional_public_trust**：dp-accessible-contrast-pairs, dp-approval-gate-for-exceptions, dp-asset-protection-for-legacy, dp-bilingual-identity-system, dp-clearspace-from-logo-geometry, dp-cobranding-grid-governance, dp-compliance-copy-as-layout-system, dp-contact-before-appendix, dp-content-forward-flexible-identity, dp-custom-typeface-as-identity-asset, dp-from-to-voice-translation, dp-inclusive-language-governance, dp-logo-vs-lockup-distinction, dp-media-split-typography, dp-modular-manual-for-public-units, dp-name-usage-governance, dp-one-brand-one-voice-governance, dp-origin-story-before-rules, dp-palette-roles-and-usage-limits, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-restrained-palette-for-trust, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **mass_consumer**：dp-cheatsheet-for-mass-touchpoints, dp-palette-roles-and-usage-limits, dp-system-toolkit-over-template
- **mission_driven**：dp-accessible-contrast-pairs, dp-cobranding-grid-governance, dp-from-to-voice-translation, dp-inclusive-language-governance, dp-media-split-typography, dp-modular-manual-for-public-units, dp-origin-story-before-rules, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules
- **platform_ecosystem**：dp-approval-gate-for-exceptions, dp-cobranding-grid-governance, dp-logo-vs-lockup-distinction, dp-message-hierarchy-by-persona, dp-modular-manual-for-public-units, dp-monochrome-logo-by-contrast, dp-one-brand-one-voice-governance, dp-persona-driven-voice, dp-personality-words-as-evaluation-criteria, dp-platform-before-visual-rules, dp-responsible-framing-for-regulated-category, dp-system-toolkit-over-template, dp-trademark-permission-flow
- **premium_luxury**：dp-asset-protection-for-legacy, dp-editorial-typography-for-premium, dp-name-usage-governance, dp-palette-roles-and-usage-limits, dp-restraint-as-luxury-signal

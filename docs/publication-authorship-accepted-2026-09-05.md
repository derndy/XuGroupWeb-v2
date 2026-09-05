# Publication authorship and accepted work — 5 September 2026

## Source priority and limits

The PI requests `*` for corresponding authors and `#` for co-first authors, including accepted conference papers before online publication. Their current [SCUT profile](https://www2.scut.edu.cn/bmse/2019/0222/c26925a633837/page.htm) is the preferred authority when metadata is unavailable elsewhere. That exact page could not be retrieved in this session. The accessible search index of the [older SCUT profile](https://www2.scut.edu.cn/bmse_en/2019/1216/c21293a478201/page.htm) contains six 2025 entries, but no current 2026 list. This batch does not claim to have reconciled the current profile.

Published publisher/repository records and the author-supplied publication list supplement the available SCUT entries. No contribution is inferred from author order, institution, supervision or funding. An absent marker means no verified marker was imported; it does not certify that the author lacks that role. Existing 75 records with correspondence symbols and 14 records with co-first symbols keep those assignments and taxonomy URLs.

## Role additions

Names are kept out of BibTeX role syntax. The table records the display metadata added to the ten recent records; original author order and DOI identities remain unchanged.

| Bundle | Corresponding (`*`) | Co-first (`#`) | Evidence |
| --- | --- | --- | --- |
| `2026-sonochemical-molecular-glue` | Xu Zhen | Not established | [Wiley author details](https://onlinelibrary.wiley.com/doi/10.1002/anie.7024563); only Xu Zhen is identified as corresponding |
| `2026-e-cloudbind` | Shidang Xu | Yujian Liu; Yutong Wang; Qingquan Wang | [Nature paper](https://www.nature.com/articles/s41467-026-74196-5) and author-supplied publication list |
| `2025-trem2-nanovesicles` | Yanjuan Gu; Wing-Tak Wong; Shiying Li; Haiyu Zhou | Bin Xu; Hongrui Qiu; Huili Wang | [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12445342/), indexed corresponding-author addresses and explicit equal-contribution note |
| `2025-tautomerism-mrna-hydrogel` | Shidang Xu; Kunyu Zhang; Liming Bian | Not established | SCUT profile entry 3; [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S3050562325001151) |
| `2025-ml-nanoparticle-delivery` | Shidang Xu; Bin Liu | Not established | SCUT entry 6 and [full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12376635/) |
| `2025-nir-ii-fluorescence-activation` | Shidang Xu; Xiqun Jiang; Xu Zhen | Not established | SCUT entry 4; retain the school's three markers pending the current profile. Publisher/coauthor records additionally mark Yuyan Jiang; this discrepancy is not silently reconciled. |
| `2025-syncanimation` | Xiaoli Liu | Yujian Liu; Shidang Xu | [IJCAI paper](https://www.ijcai.org/proceedings/2025/0185.pdf) and author-supplied publication list. The older SCUT index displays `#` after Xiaoli Liu too, whereas the paper/list identify correspondence. Current SCUT wording remains to be checked. |
| `2025-cdsr-whole-slide-images` | Shidang Xu | Yujian Liu; Yuechuan Lin; Dongxu Shen | SCUT entry 1 and explicit marks in the author-supplied list. Applies to the existing preprint record, not an asserted final conference author list. |
| `2025-mogaface` | Shidang Xu; Xiaoli Liu | Not established | SCUT entry 2 and [preprint](https://arxiv.org/html/2508.01218v1) |
| `2025-dynamic-reaction-path-descriptors` | Shipu Xu; Haiyang Huang; Shidang Xu | Not established | [ChemRxiv manuscript](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/68fee1333e6156d3be3a1513/original/dynamic-reaction-path-descriptors-integrating-mechanistic-insights-for-enhanced-ai-driven-reaction-prediction.pdf), page 1 correspondence block |

## Accepted conference work

| Work | Status | Bibliographic treatment |
| --- | --- | --- |
| AnyAvatar | ACM MM 2026, accepted poster | New bundle. [Authors' project page source](https://github.com/AISHIWEILAI/AnyAvatar.github.io/blob/main/index.html), blob `9da11d5f5e331127906e2eb699c6c8d5c3e0363e`, explicitly marks Yujian Liu, Dongxu Shen and Haoran Li as equal contributors, and Peng Cao, Shidang Xu and Xiaoli Liu as corresponding. This newer public list supplements the earlier supplied CV. All ten authors retain their order. |
| MPFusion-MIL | ACM MM 2026, accepted | New bundle. Author-supplied publication list confirms ten authors and Shidang Xu as corresponding; conference acceptance and invitation records corroborate status/year. No public paper URL, DOI or page range has been invented. |
| PyraE2E | ECCV 2026, accepted | New bundle. [Official accepted-paper list](https://eccv.ecva.net/Conferences/2026/AcceptedPapers) confirms selection. Supplied author list identifies Yuechuan Lin and Yujian Liu as co-first and Shidang Xu as corresponding, with nine authors. |
| CDSR | PRCV 2026, accepted | Linked from the accepted-work section to the existing 2025 preprint. Acceptance correspondence uses the title “Learning Whole Slide Image Representations from Few High-Resolution Patches via Cascaded Dual-Scale Reconstruction”. Final author metadata differs from the seven-author preprint metadata on the older SCUT profile; no conference citation is manufactured from that older list. |
| MoGaFace | PRCV 2026, accepted | Linked to the existing 2025 preprint. Acceptance correspondence confirms status, but subsequent conference author-list revisions need the current profile or final manuscript. Preserve the eight-author preprint citation and label its version clearly. |

Only the requested bibliography facts are included here. Private source documents, correspondence, contact addresses, administrative identifiers and research-project details are not included in Git.

The index contains **91 canonical records**. Its separate accepted-work section links all **five** accepted conference works; these links are not five additional bibliography records. Three new records belong to 2026. The two PRCV preprint records retain their 2025 dates, DOI identities and author lists; their citation notes now disclose the accepted conference version. Existing year/type filters continue to describe the canonical records, while the accepted-work section remains a distinct overview.

## Display and date rules

- `author_roles.corresponding` and `author_roles.equal_first` contain exact display names without symbols. The renderer also supports existing trailing `*`/`#` names without migrating or duplicating author archives. Unknown roles or missing named authors fail the build.
- Superscripts have descriptive accessible labels; the index and publication details explain both symbols. Theme author notes and links are retained. Other content types retain the pinned theme author renderer.
- `acceptance` holds a verified year, venue and optional accepted-version title. `publication_status: accepted` identifies a new accepted paper whose citation is a conference record. Preprints with acceptance metadata remain preprint records.
- New accepted papers use a year-start `date` only to enter Hugo's 2026 index. `date_precision: year` renders only 2026; `show_date: false` suppresses the theme's inferred January header. They have no DOI, pages, online date or inferred acceptance day.
- Accepted papers omit inferred Open Graph publication/modification times and JSON-LD dates; JSON-LD explicitly says `creativeWorkStatus: Accepted`. The pinned SEO templates retain existing behavior for all other pages.

## Remaining content check

Reconcile the current SCUT profile when a readable copy is available, especially final CDSR/MoGaFace authors, the noted JACS/SyncAnimation discrepancies, and equal-first roles absent from the available records. Do not interpret this batch as complete certification of all historical author contributions. Add conference DOI/pages only when assigned and update the accepted overview at the same time.

## Validation

Both Hugo build contexts pass (885 pages); both publication audits report 91 records / 15 years / seven types. Both scientific-image audits pass. The nine Node filter tests and three DOI tests pass. Isolated invalid-content builds reject unknown roles, nonexistent role members and missing acceptance metadata.

The generated-index/detail check verifies all 13 new/updated role mappings, all five accepted-work links, year-only dates and absence of invented accepted-publication timestamps/DOIs/pages. All 88 previous author identities, order, routes and attachment actions remain; 86 earlier citations are byte-identical, while two preprint notes disclose PRCV acceptance. All original 78 source bundles/assets are unchanged. Nine other main-content trees are unchanged; homepage text/links are preserved. All 1,245 internal links/anchors resolve, production/preview content matches, and preview-only noindex remains. These checks do not constitute browser layout/interaction testing or complete source reconciliation.

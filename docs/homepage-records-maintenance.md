# Homepage publications, people and news

The original H08–H10 batch started from merged PR #3. The current five-paper selection starts from `main` at `c9afdcf43cb59d679c1cc199f95a81814f07e615`, after PRs #12 and #13 merged. Review branch: `content/research-invitations-selected-work`. Publication/member/news/gallery records, existing URLs and original images are preserved.

## Single sources

| Homepage surface | Canonical source | Presentation |
| --- | --- | --- |
| Selected papers | Ordered `page` and `focus` references in `data/homepage.yml`; bibliographic facts in the referenced `content/publication/` bundles; focus labels in `website_text.home.publications.focus` | `layouts/partials/home/publications.html` |
| Citation downloads | The selected bundles' existing `cite.bib` resources | Inline actions beneath each paper; links appear only for files that exist |
| Research programme and group photo | `data/website_text.yml` → `home.people` and `shared.people_introduction`; `data/people_page.yml` → featured-photo record | `layouts/partials/home/people.html` |
| Latest news | `content/post/` titles, dates, categories and publication state | `layouts/partials/home/news.html`; newest three eligible records at build time |
| Order and styling | `layouts/landing/home.html`, `assets/scss/template.scss` | After testbeds, before the closing invitation; single columns below 62rem |

Do not copy paper titles, author lists, DOIs, news dates or photo captions into another data register. Public pages remain English. An existing internal review document is not a research asset for visitors.

## Current five-paper selection — 5 September 2026

This is an editorial selection, not a five-newest list or a quality ranking. Four recent papers show representation, cross-scale and multimodal methods; the older JACS paper retains the lab's active-discovery foundation. Their short focus labels describe the specific work, not a claim that a method has demonstrated transfer across every lab testbed.

| Bundle | Venue and status | Editorial focus and evidence |
| --- | --- | --- |
| `2026-e-cloudbind` | Nature Communications, 2026, published | Representation and interaction learning; [publisher paper](https://www.nature.com/articles/s41467-026-74196-5) describes electron-density point clouds and molecular graphs, including robustness to imperfect structures. |
| `2026-pyrae2e` | ECCV 2026, Accepted | Cross-scale learning for whole-slide images; [official accepted list](https://eccv.ecva.net/Conferences/2026/AcceptedPapers) confirms the paper. No unverified performance claims are added. |
| `2026-anyavatar` | ACM MM 2026, Accepted | 3D avatars with uncalibrated cameras; reuses the existing record and the primary project-source check in [the accepted-work audit](publication-authorship-accepted-2026-09-05.md). The project page could not be reread in this session; the new focus stays at title-level description. |
| `2025-syncanimation` | IJCAI 2025, published | Audio-driven multimodal generation; [official proceedings abstract](https://www.ijcai.org/proceedings/2025/185) connects audio, pose and talking-head generation. |
| `9-2021-xu-et-al-self-improving-photosensitizer-discovery-system-via-bayesian-search-with-first-principle-simulations` | JACS 2021, published | Active learning and a self-improving discovery loop; [ACS publisher record](https://pubs.acs.org/doi/10.1021/jacs.1c08211). Deliberately retained for the connection between Bayesian search, simulation and discovery, not recency. |

AnyAvatar and PyraE2E keep explicit Accepted labels and year-only dates. Do not infer an online/acceptance day from their internal sorting date, and do not invent a DOI or pages. Three published selections retain their actual DOI links. All five keep their canonical authors, role markers and BibTeX bytes. The older Chemistry of Materials paper is removed only from this homepage selection, not from the publication archive. MPFusion-MIL remains in the archive; this selection uses one WSI paper to leave space for other methods.

The citation sidebar is replaced by inline paper-detail, publisher and BibTeX actions. This avoids repeating five full titles in a second column. Five records still make this section longer than its former two-record version; browser layout review remains necessary.

## Historical initial paper selection and evidence

The selection illustrates computational discovery and molecular design. It is not a ranking, claim of the newest papers, or mapping of older papers to every current pillar.

| Existing bundle | Identity check | Homepage actions |
| --- | --- | --- |
| `9-2021-xu-et-al-self-improving-photosensitizer-discovery-system-via-bayesian-search-with-first-principle-simulations` | [ACS publisher record](https://pubs.acs.org/doi/10.1021/jacs.1c08211) indexed title, DOI and 17 November 2021 date checked on 5 September 2026; consistent with the existing source. Authors/venue and local citation remain the canonical repository values. | Existing detail route, publisher DOI record, local BibTeX download |
| `73-Chem Mater-2020-All-in-one molecular AIE theranostics fluorescence image guided and mitochondria targeted chemo-and photodynamic cancer cell ablation` | Reuses the publisher-deposited Crossref and ACS/NUS identity check in [the publication audit](publication-link-audit-2026-09-05.md); DOI `10.1021/acs.chemmater.0c01187`. | Existing detail route, publisher DOI record, local BibTeX download |

No paper metadata or citation bytes are changed. This is not a new archive-wide bibliographic audit, confirmation of publisher full-text access, or verification of every external PDF. No code, dataset, protocol or benchmark release is invented. Such resources can be added in a later batch when real approved records and usable destinations exist; citation downloads are explicitly labelled as citations.

To change the selection, edit `page` references only after checking the canonical paper and its source identity, and connect each `focus` key to a short label in `data/website_text.yml`. Missing pages/focus labels, duplicates, non-publication pages, artwork, types other than journal articles or conference papers, and draft/future-dated selections fail the build. Accepted conference records require the existing acceptance metadata. A preprint with a conference acceptance notice remains a preprint and is not silently treated as the final paper. Keep the list small and the citations readable; do not use publication counters or full abstract cards.

## Documentary photograph

The homepage reuses the People page's featured image, `static/images/people/东盛楼_20250910.png`, with its existing caption, “Welcome dinner for the incoming class · 2025,” and alt text. The source was visually inspected and is a 1200 × 900 group photograph with a 2025 welcome-dinner label. No identities are inferred from the image.

The complete source image is displayed at its natural aspect ratio, with dimensions read from the file, lazy loading and asynchronous decoding. Colour, embedded caption, framing and original bytes are untouched. This reuses an already public source; it is not a new rights/consent determination. Existing photo-review requirements still apply before release. The original PNG is about 1.9 MB; responsive derivative optimisation can be considered during actual browser/performance review without recropping the photograph.

Only image 05 is a principal conceptual illustration on Home. This documentary photograph does not move or duplicate any of the six approved conceptual artworks.

## News selection

At the original H08–H10 checkpoint the three latest eligible records were:

| Date | Existing title |
| --- | --- |
| 22 November 2025 | College Table Tennis Team Tournament |
| 4 June 2025 | Xinxuan Li joins the group as a PhD student |
| 16 April 2025 | Qiyun Zhou joins the group as a master’s student |

The homepage preserves the original event dates. It does not imply newly reported 2026 activity. When a source has no category, the broad label “Lab update” is used; no new taxonomy or inferred award category is added. Headlines link to their original routes. No carousel, duplicated summary, extra news photograph or client-side dependency is added.

The selection excludes drafts, empty titles, future event dates and future publication dates even when preview builds enable `--buildFuture` or `--buildDrafts`. Fewer than three eligible entries produce fewer cards; no eligible entries omit the section. New records enter the homepage after an eligible build, not through a browser clock or live service.

See [News maintenance](news-maintenance.md) for editing the actual records and [People maintenance](people-directory-maintenance.md) for image and profile changes.

## Review boundary

Verify both Hugo build contexts, the six-image audit, exact publication/citation preservation, all main-page internal links, unique IDs and heading landmarks. For the original H08–H10 batch, the baseline was the evidence-loop build. For this five-paper batch, compare against merged PR #12/#13 and allow only the changes described in [the copy review](research-copy-and-selected-work-2026-09-05.md).

Before release, inspect desktop/tablet/320px layouts, focus, text zoom and photo loading in a supported real browser. The current internal preview cannot start this Hugo checkout, so source checks do not establish browser QA success. Keep the delivery as a draft PR; merging and hosting changes require a separate release instruction.

## Current text-editing location

Homepage section headings, descriptions and labels live in `data/website_text.yml` under `home.publications`, `home.people` and `home.news`. The five-paper batch adds `home.publications.focus`, conference/Accepted labels and inline action labels, with eligibility rules as described above. See [the editing guide](website-text-maintenance.md).

# Homepage publications, people and news

This batch implements H08–H10 of the design brief. Start from v2 `main` at `13d699772ec8e76d59fe219511fa370ea8496945`, the merge of PR #3. Review branch: `design/homepage-publications-people-news`. Publication/member/news/gallery records, existing URLs and original images are preserved.

## Single sources

| Homepage surface | Canonical source | Presentation |
| --- | --- | --- |
| Selected papers | Ordered page references in `data/homepage.yml`; bibliographic facts in the referenced `content/publication/` bundles | `layouts/partials/home/publications.html` |
| Citation downloads | The selected bundles' existing `cite.bib` resources | The same partial; links appear only for files that exist, and the citation column is omitted when none exist |
| Research programme and group photo | Existing research framing; `data/people_page.yml` introduction and featured-photo record | `layouts/partials/home/people.html` |
| Latest news | `content/post/` titles, dates, categories and publication state | `layouts/partials/home/news.html`; newest three eligible records at build time |
| Order and styling | `layouts/landing/home.html`, `assets/scss/template.scss` | After testbeds, before the closing invitation; single columns below 62rem |

Do not copy paper titles, author lists, DOIs, news dates or photo captions into another data register. Public pages remain English. An existing internal review document is not a research asset for visitors.

## Initial paper selection and evidence

The selection illustrates computational discovery and molecular design. It is not a ranking, claim of the newest papers, or mapping of older papers to every current pillar.

| Existing bundle | Identity check | Homepage actions |
| --- | --- | --- |
| `9-2021-xu-et-al-self-improving-photosensitizer-discovery-system-via-bayesian-search-with-first-principle-simulations` | [ACS publisher record](https://pubs.acs.org/doi/10.1021/jacs.1c08211) indexed title, DOI and 17 November 2021 date checked on 5 September 2026; consistent with the existing source. Authors/venue and local citation remain the canonical repository values. | Existing detail route, publisher DOI record, local BibTeX download |
| `73-Chem Mater-2020-All-in-one molecular AIE theranostics fluorescence image guided and mitochondria targeted chemo-and photodynamic cancer cell ablation` | Reuses the publisher-deposited Crossref and ACS/NUS identity check in [the publication audit](publication-link-audit-2026-09-05.md); DOI `10.1021/acs.chemmater.0c01187`. | Existing detail route, publisher DOI record, local BibTeX download |

No paper metadata or citation bytes are changed. This is not a new archive-wide bibliographic audit, confirmation of publisher full-text access, or verification of every external PDF. No code, dataset, protocol or benchmark release is invented. Such resources can be added in a later batch when real approved records and usable destinations exist; citation downloads are explicitly labelled as citations.

To change the selection, edit page references only after checking the canonical paper and its publisher identity. Missing pages, duplicate selections, non-publication pages, non-article types, artwork records and unpublished selections fail the build. Keep the list small and the citations readable; do not use publication counters or full abstract cards.

## Documentary photograph

The homepage reuses the People page's featured image, `static/images/people/东盛楼_20250910.png`, with its existing caption, “Welcome dinner for the incoming class · 2025,” and alt text. The source was visually inspected and is a 1200 × 900 group photograph with a 2025 welcome-dinner label. No identities are inferred from the image.

The complete source image is displayed at its natural aspect ratio, with dimensions read from the file, lazy loading and asynchronous decoding. Colour, embedded caption, framing and original bytes are untouched. This reuses an already public source; it is not a new rights/consent determination. Existing photo-review requirements still apply before release. The original PNG is about 1.9 MB; responsive derivative optimisation can be considered during actual browser/performance review without recropping the photograph.

Only image 05 is a principal conceptual illustration on Home. This documentary photograph does not move or duplicate any of the six approved conceptual artworks.

## News selection

At this checkpoint the three latest eligible records are:

| Date | Existing title |
| --- | --- |
| 22 November 2025 | College Table Tennis Team Tournament |
| 4 June 2025 | Xinxuan Li joins the group as a PhD student |
| 16 April 2025 | Qiyun Zhou joins the group as a master’s student |

The homepage preserves the original event dates. It does not imply newly reported 2026 activity. When a source has no category, the broad label “Lab update” is used; no new taxonomy or inferred award category is added. Headlines link to their original routes. No carousel, duplicated summary, extra news photograph or client-side dependency is added.

The selection excludes drafts, empty titles, future event dates and future publication dates even when preview builds enable `--buildFuture` or `--buildDrafts`. Fewer than three eligible entries produce fewer cards; no eligible entries omit the section. New records enter the homepage after an eligible build, not through a browser clock or live service.

See [News maintenance](news-maintenance.md) for editing the actual records and [People maintenance](people-directory-maintenance.md) for image and profile changes.

## Review boundary

Verify both Hugo build contexts, the six-image audit, exact publication/citation preservation, all main-page internal links, unique IDs and heading landmarks. Compare the other ten main-content trees against the evidence-loop build. Home's earlier sections should match exactly except for the closing invitation's section number, now 09.

Before release, inspect desktop/tablet/320px layouts, focus, text zoom and photo loading in a supported real browser. The current internal preview cannot start this Hugo checkout, so source checks do not establish browser QA success. Keep the delivery as a draft PR; merging and hosting changes require a separate release instruction.

# Xu Lab website — current project state

Updated: 5 September 2026. Read this file first when continuing development. `PROJECT_STATE.md` is a compatibility pointer to this canonical lowercase file.

## Current source and delivery boundary

| Item | Current value |
| --- | --- |
| Repository | Public `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-publications-2025-2026` (isolated worktree) |
| Current review branch | `content/publications-2025-2026` |
| Branch point | `main` at `83a9fcdf11ee5a3295ba495b140177330086dd93`, after PR #9 merged |
| Previous merged work | PRs #1–9, including Gallery repair and the shared homepage text file |
| Gallery repair | [PR #8](https://github.com/derndy/XuGroupWeb-v2/pull/8), merged while this batch was being prepared; its changes are included in the base |
| Current PR | Prepared locally; draft PR publication follows validation |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Current release instruction | Review branch and draft PR only; no merge or production switch |

The user now prioritizes missing 2025–2026 Publications, referencing their SCUT and Google Scholar profiles. This batch adds ten individually verified public records in a review branch and draft PR. It does not merge, modify the original repository, or change hosting or production settings.

The bibliography was first verified against PR #8 at `bd762ef…`. During delivery, GitHub showed PR #9 merged at `83a9fcd…`. The publication commit was rebased onto this newer main; README/state conflicts were resolved by retaining the homepage text migration and its full maintenance/delivery history. Product files did not conflict. Both builds and the preservation audit are repeated on the combined source. The usual approved-images checkout and its separate workflow were left untouched.

## Latest batch — Publications for 2025 and 2026

- Added ten canonical bundles and matching BibTeX files: eight records for 2025 and two for 2026. Six are journal articles, one is the official IJCAI conference paper, and three are explicitly labeled preprints using the existing Working paper type. The index now contains 88 records across 15 years and seven display types.
- Full author order, titles, venues, years and DOI identifiers are checked against primary publisher/organizer/repository records and publisher-deposited Crossref metadata. The [source audit](docs/publications-update-2026-09-05.md) records every source, date conflict and duplicate/version decision.
- Includes all six 2025 entries from the indexed official SCUT supervisor profile. The supplied SCUT URL could not be read directly, and Scholar returned HTTP 403. This is an individually verified addition, not a claim of complete Scholar reconciliation. A current export remains useful for the completeness check.
- Journal dates use verified first publication; citations retain final issue metadata where assigned. SyncAnimation has only a verified month in its organizer citation: `date_precision: month` displays August 2025, with day 01 only a Hugo sorting anchor. The preprint version of SyncAnimation is not duplicated.
- No abstracts, PDFs, scientific figures or new author biography claims were imported. Existing homepage paper selections and all previous content remain intact.

### Validation of the Publications update

- Production and preview-equivalent Hugo builds passed: 864 pages each (including expanded author/taxonomy archives).
- Both builds pass the 88-record / 15-year / seven-type publication audit and the six-approved-image / 24-variant audit.
- Nine existing Node filter/state tests and three DOI tests passed; whitespace checks pass.
- All ten new records have the expected date/year/type, full source-matched authors, exact DOI links and downloadable BibTeX bytes. Three preprint notices and the month-only conference display are verified in generated HTML.
- All 78 original source bundles and citations are byte-identical to main; their rendered record and detail content remains identical to the Gallery baseline. The ten other main-page content trees are unchanged.
- All 1,202 internal links/anchors across eleven main pages resolve. Production/preview main content matches; preview-only noindex is retained.
- Browser layout, Scholar completeness and interactive citation-modal testing remain separate checks. No browser QA was performed for this bibliography batch.

Temporary build outputs: `/workspace/scratch/7457cd2d5ea9/build-publications-2026` and `build-publications-2026-preview`; preservation baseline: `build-gallery-overlap`. The reproducible one-off audit is `/workspace/scratch/7457cd2d5ea9/verify-publications-2026.py`. Source metadata snapshots and the preparation script are temporary retrieval/verification aids outside Git; the public source audit is the durable provenance record.

## Previous completed batch — homepage text in one editable file

- Created `data/website_text.yml`: `home` holds homepage headings, explanations, labels, four testbed cards and calls to action; `shared` holds its scientific definitions, evidence-loop steps, five pillar display fields and the shared team introduction.
- Moved the existing shared copy out of `data/research_system.yml` / `data/people_page.yml` and connected every existing consumer. The new `research/pillars.html` helper combines editable display fields with stable IDs/routes and detailed research records. Missing required pillar copy fails the build.
- About, Research, all three pillar pages and People continue to read the same shared wording. A real edit check confirms one change reaches the expected pages. There is no second maintained copy of these entries.
- Preserved publication/news/member records and their selection logic, the approved photograph/illustration captions, all images, routes, metadata, CSS, JavaScript and hosting configuration.
- Added `docs/website-text-maintenance.md` with exact field locations, the GitHub editing process, plain-text/YAML guidance and shared-page effects. Updated the relevant existing maintenance guides.
- This completes homepage wording only. Other page copy, global navigation/footer and homepage browser-tab/search metadata retain their existing sources. Continue migrating other pages in later bounded batches.

### Validation

- Final production and preview-equivalent Hugo builds pass: 736 pages each.
- **All eleven main-page HTML files, including the full homepage, are byte-identical to the pre-change production build.** No CSS or JavaScript changes.
- All 1,069 internal links/anchors resolve. One H1/main, unique IDs, preview-only noindex and matching production/preview main text verified.
- The existing audits pass for all 78 publication records, citation bytes, six approved scientific image placements and 24 uncropped WebP variants.
- Shared YAML values match their original values exactly; all unmoved research data matches the original source structure.
- Eight temporary changes in only `website_text.yml` update homepage text, a testbed card, a news link, About's shared definition, the evidence loop, pillar titles/roles and the People introduction. Quotes, ampersands, Chinese text and literal HTML are rendered correctly as plain text. The approved wording was restored and rebuilt afterward.
- Whitespace checks pass. No browser layout or interaction test was performed for this text-source move; byte-identical HTML does not resolve earlier whole-site browser-review items.

Temporary reproducible outputs: `/workspace/scratch/4a70b09acb33/build-home-text-before`, `build-home-text`, `build-home-text-preview`, and `build-home-text-edit-check`. After PR #8 merged, both final builds were repeated and all eleven production HTML files matched `/workspace/scratch/7457cd2d5ea9/build-gallery-overlap` byte-for-byte. Gallery source, styles and maintenance notes also match the new main exactly. The one-off migration/edit-check scripts are in scratch and are not published.

## Design decisions to retain

1. Read [website-design-and-asset-placement.md](docs/website-design-and-asset-placement.md) in full for the supplied design plan. The repository edition preserves the design and six-image register while omitting private Library retrieval identifiers. The original attachment's SHA-256 is recorded there.
2. Read [design-implementation-review-2026-09-05.md](docs/design-implementation-review-2026-09-05.md) for the full existing/missing/changed comparison and next batches.
3. Preserve the exact homepage title, subtitle and tagline. English public pages remain English; do not insert sentence-by-sentence Chinese translations.
4. The three pillars are scientific learning-system design, evidence engineering, and mathematical/frontier exploration. Space, Interaction and Learning are co-designed dimensions of a learner, not replacements for the pillars.
5. Materials and biomedical applications are cross-pillar testbeds. Scientific Learning Grammar remains a long-term programme, not an established theory.
6. The Hero uses live semantic HTML. Each major page has at most one principal conceptual artwork. Original images, approved captions and conceptual attribution remain unchanged.
7. Reuse actual public records. Do not expose internal project packages, governance diagrams, blank templates or unsupported claims from the Drive archive.
8. Keep existing `/publication/`, `/post/`, `/contact/` and `/research/learning-system-design/` routes. The design's alternative route labels do not authorize breaking existing URLs.
9. `noindex` is not access control. Public branches and previews must contain only material suitable for public access. Image approval is not authorization to merge or switch production.

## Previous completed batch — Gallery overlap repair

- Browser inspection reproduced overlapping photographs, captions and the following year's heading on the live Gallery at a 1363 × 936 CSS-pixel viewport.
- The theme's gallery shortcode and our documentary page shared `.gallery-grid`. The theme supplied `grid-auto-rows: 150px`, dense packing and a 30px gap. A measured card was only 150px high while its photograph and caption extended more than 600px; later rows and years began before that content ended.
- Renamed the documentary grid to `.lab-gallery-grid`, explicitly using content-sized rows, normal row order and zero gap to match its existing border treatment. The theme's shortcode is unchanged.
- Changed card figures from percentage height to a natural flex column, with a non-shrinking photograph and expanding caption. Caption margins and alignment are now explicit; long text wraps in both cards and the original-photo viewer.
- All 19 records, English/Chinese titles, descriptions, alt text, categories, years, original/thumbnail image bytes, URLs and the viewer script are preserved. No image editing, new dependency or content change.

### Source validation of the Gallery repair

- Production and preview-equivalent Hugo builds passed: 736 pages each.
- Six approved scientific image placements and 24 uncropped WebP variants pass the existing audit. All 78 publication records, routes, actions and citation bytes match the preceding About-principles build.
- All 1,069 internal links/anchors resolve across eleven main pages, with unique IDs, one H1/main and preview-only noindex.
- Gallery HTML differs only in the isolated grid class names. All 19 records and original-image links are present without JavaScript. Production/preview Gallery content matches; all ten other main-content trees are identical to baseline.
- Viewer JavaScript syntax and whitespace checks pass. Canonical data, image files, viewer script and hosting configuration are unchanged.

### Browser verification of the Gallery repair

The matching [Gallery preview](https://deploy-preview-8--xushidang-lab.netlify.app/gallery/) was inspected at **1363 × 936 CSS pixels**. All 19 thumbnails loaded successfully. Geometry checks found no card/card intersection, caption overflow, overlapping caption blocks, content extending past its year section, or page horizontal overflow. All three grids use `auto` rows and normal row flow. The representative first 2024 card is now about 611px high, accommodating its 285px photograph and 326px caption instead of the former 150px row.

Screenshots confirmed separation between the 2024 heading and photographs, between the first and second photo rows, and at the 2023 section. The native viewer was checked with 2024 and 2023 records: original photos load, the photograph and caption occupy separate regions, and no horizontal overflow occurs. Mouse opening, Enter opening, Next, ArrowLeft, last-to-first wrapping, Escape/close and focus restoration to the opening card were verified. Viewer JavaScript was not modified.

**Remaining browser coverage:** mobile/tablet widths, touch and 200% text/zoom have not been tested. The available browser controls did not provide effective resizing/zoom; a narrow-viewport fixture was blocked by browser URL policy. The existing responsive breakpoints now target the isolated grid and the content-sized row repair applies at every breakpoint, but source inspection is not a claim of mobile browser success. Earlier whole-site browser-review items remain separate.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-gallery-overlap` and `build-gallery-overlap-preview`; baseline: `build-about-principles`. The one-off preservation audit is `/workspace/scratch/7457cd2d5ea9/verify-gallery-overlap.py`. These temporary reproducible outputs remain outside Git.

## Previous completed batch — About research principles and directions

- Added two chapters after the existing scientific-learning explanation and before the onward routes: six shared research principles, then NOW / NEXT 3–5 YEARS / HORIZON.
- All six principles and all three stage labels/titles/descriptions are read verbatim from the existing top-level `research_system.principles` and `research_system.horizons` records already displayed on Research. Shared data is unchanged; no duplicate scientific copy is introduced.
- About-specific headings and framing live in `content/about/index.md`. The stage introduction explicitly separates direction/ambition from evidence strength and completed results. Scientific Learning Grammar remains a long-term research horizon, with no invented completion date or current-capability claim.
- Added a real Research-principles link and three links to the existing pillar horizon sections, using canonical public titles and detail URLs.
- Principles use a two-column semantic list; the three stages form a vertical ordered list with labels beside explanations. Both reflow to one column below 48rem. Native links and visible focus require no new script, dependency or disclosure interaction.
- Preserved the entire existing About hero, vision chapter, approved image 04, onward routes and original introduction/metadata. No hosting, asset, publication or other page-source change.

See [About maintenance](docs/about-maintenance.md) for editing locations, shared-source effects, stage semantics and reading order.

### Validation of the About-principles batch

- Production and preview-equivalent Hugo builds passed, 736 pages each.
- All six approved original images/placements/captions and 24 uncropped WebP variants passed both audits.
- All 78 publication records, routes, attachment actions and citation bytes match the preceding About-learning build in both contexts.
- All 1,069 internal links/anchors resolve across eleven main pages, with unique IDs and one H1/main per page. The four new destinations include all three real pillar horizon anchors.
- Six canonical principles and three canonical stages match exactly; stage order, ambition/evidence qualification, chapter reading order and descriptive pillar links verified.
- Existing About hero, complete vision chapter and onward routes are identical to baseline. Original Markdown introduction/metadata, shared research data and hosting configuration are unchanged; all ten other main-content trees match exactly.
- Production/preview About main-content trees match; preview-only noindex verified on eleven pages. New text colour pairs meet at least 4.56:1 contrast. Whitespace checks passed.

Real browser layout, keyboard/touch, text zoom and image-loading review remain pending. Build and source checks do not constitute browser QA.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-about-principles` and `build-about-principles-preview`; baselines: `build-about-learning` and `build-about-learning-preview`. One-off generated-HTML audit: `/workspace/scratch/7457cd2d5ea9/verify-about-principles.py`. These are temporary reproducible outputs outside Git.

## Previous completed batch — About's scientific learning chapter

- Added the Space–Interaction–Learning middle chapter on `/about/`, with the three existing canonical questions/definitions read from `research_system.grammar` and a short explanation of mutual shaping.
- Kept the three design choices within the learner distinct from the broader research pillars. Existing shared grammar data and the homepage are unchanged.
- Preserved image 04 at its approved `about-vision` placement, displayed full width after the explanation. Its original bytes, alt, approved caption, conceptual/AI attribution, download action and four WebP variants are unchanged. The loop is described as a visual metaphor.
- Added canonical evidence/feedback text and a clearly labelled Research horizon block for Scientific Learning Grammar. The latter is a long-term aim/open question, with a real link to Pillar I's horizon section.
- Moved existing About hero and onward-route wording out of the template and into `content/about/index.md`, without changing rendered text. New About-specific copy is in that same file's `about` front matter; the existing introduction stays in its Markdown body. Shared definitions/captions keep their canonical data sources.
- Added scoped About styles with three desktop definition columns, two following text columns and single-column reflow below 62rem. The explanation, image and caption keep the same document reading order.
- No new image, script, dependency, result, timeline, private project or operating-policy content; no hosting change. Fuller principles/culture/roadmap chapters remain separate work.

See [About maintenance](docs/about-maintenance.md) for editing locations, scientific boundaries, image handling and shared-source effects. This is an About-page text organisation improvement, not a completed site-wide single-file text migration.

### Validation of the About-learning batch

- Production and preview-equivalent Hugo builds passed, 736 pages each.
- All six approved original images/placements/captions and 24 uncropped WebP variants passed both audits.
- All 78 publication records, routes, actions and citation bytes match the preceding Contact-pathways build in both contexts.
- All 1,065 internal links/anchors resolve across eleven main pages, with unique IDs and one H1/main per page. The three new destinations include the real Pillar I horizon anchor.
- Three shared definitions/questions, canonical evidence/feedback, explicit long-term qualification and explanation → image → caption document order verified.
- Existing About hero, onward routes and illustration HTML are identical to baseline. The original Markdown introduction, page title/search metadata and shared grammar data are preserved. All ten other main-content trees match exactly.
- Production/preview About main-content trees match; preview-only noindex verified on eleven pages. New text colour pairs meet at least 4.51:1 contrast. Whitespace checks passed.

Real browser layout, keyboard/touch, text zoom and image-loading review remain pending. No browser QA or unsupported local preview workaround is claimed.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-about-learning` and `build-about-learning-preview`; baselines: `build-contact-pathways` and `build-contact-pathways-preview`. One-off generated-HTML audit: `/workspace/scratch/7457cd2d5ea9/verify-about-learning.py`. These are temporary reproducible outputs outside Git.

## Previous completed batch — four Contact pathways

- Added four stable sections on `/contact/`: scientific collaboration, experimental partnership, joining the lab and research-asset use. A top navigation links to these sections and the existing contact details.
- Each route explains suitable questions, a useful contribution, three items for a first email, a conditional next step, a suggested email subject and a related public page.
- All new text/labels are in `data/contact_page.yml` under `pathways`. `layouts/partials/contact/pathways.html` renders the cards; the existing contact template adds the navigation and section.
- Email links derive their recipient from the existing displayed contact email and prefill only a correctly encoded suggested subject. The page sends no email and adds no form, visitor-input field, JavaScript or dependency.
- The applicant route asks about openings, funding and application timing; it makes no funded-vacancy, admission or response-time promise. The resource route refers to specific published work and its access/reuse terms without inventing releases.
- Scoped Contact styles use two desktop columns, one column below 62rem, native fragment links, focusable route targets, visible focus and wrapping text/buttons.
- The existing contact facts, appointment URL, library photograph, closing illustration/caption/download and all other main-page content remain intact. No hosting file or source image changes.

See [Contact maintenance](docs/contact-maintenance.md) for the four stable anchors, content locations, suggested subjects and factual boundaries.

### Validation of the Contact-pathways batch

- Production and preview-equivalent Hugo builds passed, 736 pages each.
- All six approved original images/placements/captions and 24 uncropped WebP variants passed both audits.
- All 78 publication records, routes, attachment actions and citation bytes match the preceding homepage-records build in both contexts.
- All 1,062 internal links/anchors resolve across eleven main pages; IDs are unique and each page has one H1/main.
- Four complete route cards, five jump destinations and four related-page links verified. Each mailto recipient equals the displayed email, and each distinct decoded subject equals the suggested subject. No body parameter or form fields were added.
- Contact's previous hero content, contact-information section and closing section match the baseline HTML. Existing contact data and image bytes are preserved; all ten other main-content trees match exactly.
- Production/preview Contact main-content trees match. All eleven preview pages have noindex; their production equivalents do not. New text colour pairs meet at least 4.56:1 contrast. Whitespace checks passed.

Real browser layout, keyboard/touch, zoom, mail-client launch and live appointment availability remain untested. A hosted preview build is not browser QA. No unsupported browser-preview workaround was introduced.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-contact-pathways` and `build-contact-pathways-preview`; preservation baselines: `build-home-records` and `build-home-records-preview`. The one-off generated-HTML audit is `/workspace/scratch/7457cd2d5ea9/verify-contact-pathways.py`; build outputs and the audit runner are temporary, reproducible files outside Git.

## Previous completed batch — homepage scientific explanation

- Replaced the static, absolutely positioned Hero diagram with six native `details`/`summary` concepts: Evidence, Space, Interaction, Learning, Mechanism and Design. Definitions and real research links are usable without JavaScript. Learner dimensions use neutral styling; outcomes are explicitly proposals/aims to test.
- Added H03: scientific questions, definitions, connected choices and an evidence-feedback explanation. Compact and expanded forms share `data/research_system.yml` and `layouts/partials/research/learning-grammar.html`.
- Preserved the already-present Beyond Prediction section and all three exact homepage statements.
- Changed the secondary Hero action to the existing Scientific testbeds section.
- Replaced duplicate homepage pillar content with canonical formal titles, core questions and routes. Each card has a direct Explore link. Existing public invitations and three concise capability terms remain.
- Reduced the Hero headline scale and removed fixed-height pillar cards; added responsive grammar layouts and visible focus styles. Browser confirmation remains pending.
- Saved the design plan, implementation comparison, asset-location record and updated README/state instructions.

The new grammar follows the meaning of the original Drive `space-interaction-learning-map.svg`, which was retrieved and read. It does not publish the original source sheet. The archive manifest lists 91 materials; the six existing repository images already match their approval hashes and were not regenerated or reimported.

## Previous completed batch — homepage publications, people and news

- Added H08 with two selected existing research papers, canonical title/author/venue/year data, publisher DOI links and the two actual BibTeX downloads. Selected does not mean newest. No public dataset/code/protocol release is implied.
- Added H09 with the existing People introduction, a short research-programme statement, the complete 2025 welcome-dinner photograph and its exact alt/caption, plus People/Gallery links. Natural 1200 × 900 aspect ratio, lazy loading and original image bytes are retained.
- Added H10 with the three newest eligible canonical News records: 22 November, 4 June and 16 April 2025. Original titles/dates/routes remain; missing categories use the broad label Lab update.
- Three homepage partials read existing sources. Only ordered publication references are new data. Invalid, duplicate, artwork or unpublished paper selections fail the build. News excludes draft and future event/publication dates even in permissive previews.
- CSS uses desktop columns and single columns below 62rem, readable citations and visible focus. There is no new script, dependency, image payload or hosting change.
- Inserted the sections after testbeds and before Join; the closing invitation is now numbered 09. All other earlier homepage content and the other ten main-page content trees are preserved.

See [homepage-records-maintenance.md](docs/homepage-records-maintenance.md) for exact source paths, paper-selection evidence, photo treatment and editing rules.

### Validation of the homepage-records batch

- Production and preview-equivalent builds passed, 736 pages each.
- Six approved conceptual images, captions/placements, exact original downloads and 24 uncropped WebP derivatives passed both build audits.
- All 78 publication records, actions and citation bytes match the evidence-loop baseline in both builds.
- All 1,053 internal links/anchors resolve across eleven main pages; unique IDs and exactly one H1/main per page.
- Selected paper titles/authors/DOIs match the canonical publication index; both downloaded citation files match baseline bytes. Photo dimensions, bytes, alt and caption match the existing source. Three news dates/order match in both builds.
- A separate permissive preview with temporary draft, future-event and future-publication fixtures rendered those fixture pages but excluded them all from the homepage. The three real homepage news entries were unchanged. Fixtures were removed after the check.
- All ten other main-content trees match the baseline; all previous homepage sections match except the intended closing section number. New text colours pass at least 4.56:1 contrast on their specified backgrounds.
- All eleven preview pages have noindex; their production equivalents do not. Whitespace checks passed.

Real browser layout, keyboard/touch, text zoom and photo-loading performance remain pending. Netlify now reports a successful matching preview, linked in the delivery record below; its build success is not browser QA. The reused below-fold PNG is about 1.9 MB; responsive derivatives can be considered during that performance review.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-home-records` and `build-home-records-preview`; preservation baseline: `build-evidence-loop` / `build-evidence-loop-preview`. Temporary fixture output: `build-home-records-gates`. Outputs and the one-off audit runner are reproducible scratch files outside Git.

## Previous completed batch — homepage evidence loop

- Implemented the six design-brief steps separately: Observe, Question, Design evidence, Learn, Test, Explain or design.
- Replaced the navy chapter with a pale-teal section, solid reading-sequence arrows and a dashed feedback return. Narrow-screen CSS presents the six steps vertically. A visible return link targets Observe.
- Each native disclosure provides an explanation, example question, typical research output and contributing-pillar links. Content remains available without JavaScript; no new animation or dependency was added.
- `evidence_loop` in `data/research_system.yml` is the shared semantic source. The new partial `layouts/partials/research/evidence-loop.html` resolves real pillar IDs and fails the build for an invalid reference.
- Labels identify the loop as a conceptual framework. The copy describes a flexible research approach and explicitly treats explanations/designs as subject to testing.
- No other homepage section, source image, record collection or hosting configuration is edited.

### Validation of the evidence-loop batch

- Production and preview-equivalent Hugo builds passed: 736 pages each.
- All six exact approved original images, captions/placements and 24 WebP variants passed the visual audit on both builds.
- All 78 publications and citation bytes match the preceding build.
- The six distinct native evidence-step controls each have an example question, research output and real pillar links. All 13 pillar links and the Return to Observe anchor resolve.
- All 1,029 internal links/anchors resolve across eleven main pages, with unique IDs and one H1/main each.
- All other homepage sections and all ten other main-content trees exactly match the preceding grammar build.
- Text colour/background pairs in the new section pass at least 4.5:1 contrast; arrow/path colours exceed the non-text contrast threshold.
- All eleven main preview pages have noindex; corresponding production pages do not inherit it.
- Whitespace checks passed; no new scripts, images, dependencies or hosting changes.

Real browser layout, keyboard, touch, zoom and reduced-motion checks remain pending because the existing Hugo checkout has no compatible internal preview entrypoint; no new preview attempt was made in this continuation. Static checks do not demonstrate browser interaction success.

Build outputs: `/workspace/scratch/7457cd2d5ea9/build-evidence-loop` and `build-evidence-loop-preview`. The preceding `build-home-grammar` output supplies the preservation baseline. All are reproducible, temporary outputs outside Git.

## Existing work retained

| Surface | Existing implementation |
| --- | --- |
| Home | Exact identity copy, scientific grammar, three pillars, evidence loop, testbeds with image 05, selected papers/citations, documentary team photo, three dated news entries and closing invitation |
| Research and three pillars | Overview, interconnected research map, detailed scope/methods/testbeds/principles/horizons and images 01–03 |
| About | Research identity, shared Space–Interaction–Learning explanation, full-width image 04, evidence feedback, qualified long-term programme and onward links; fuller principles/culture/roadmap still pending |
| Contact / Join / Collaborate | Four audience pathways, preparation guidance, suggested email subjects, shared contact facts/links, appointment link, authentic library photograph and image 06 |
| People | 16 current-member profiles, 7 undergraduate records, 9 alumni records and authentic photographs |
| Gallery | 19 documentary records, year grouping, server-rendered content and progressively enhanced dialog |
| News | 18 published records; incomplete record excluded as draft |
| Publications | 88 records, 15 years, seven types, filters/search, citations, ten 2025–2026 additions and previous verified identity corrections |

Approved image source paths, captions, hashes and destinations are in `data/research_assets.yml` and `docs/scientific-visual-approval-2026-09-05.md`. All six original PNGs and all 24 uncropped WebP derivatives are retained. Image 05 remains the only principal conceptual illustration on Home, alongside the authentic group photograph; image 06 stays on Contact.

## Validation of the previous grammar batch

Completed locally on 5 September 2026:

- Production-equivalent Hugo build: 736 pages, passed.
- Preview-equivalent Hugo build: 736 pages, passed. All eleven main preview surfaces have noindex; their production counterparts do not. Scientific image audit also passed on the preview build.
- Scientific visual audit: six approved placements, six exact PNG downloads, 24 uncropped WebP variants, approved labels/captions and legacy exclusion passed.
- Publication audit and comparison with the pre-batch build: all 78 records, author/title content, order, routes, attachment actions and citation bytes preserved.
- Eleven main surfaces: exactly one H1 and one main landmark each; unique IDs; 1,015 internal links and page fragments resolve.
- Exact homepage H1/subtitle/tagline; six native concept controls with definitions and links; three correct pillar destinations; one homepage conceptual figure.
- All ten other main-content HTML trees match the preceding build, including attributes and text.
- Design documentation is outside rendered content/static; no source-sheet or new bitmap payload added.
- `git diff --check` passed.

Not completed: real browser layout, keyboard, touch, 200% zoom and reduced-motion verification; complete external link/download checks; live email/phone clients or appointment availability. The supervised browser preview could not start for this Hugo checkout because it requires a compatible package/dev-server entrypoint. Do not claim screenshot or browser-test success. No migration or unrelated dependency was introduced to work around it.

Build folders under `/workspace/scratch/7457cd2d5ea9/`: `build-home-grammar` and `build-home-grammar-preview`. The preceding `build-contact` output was used only for preservation comparison. These outputs are temporary, reproducible and excluded from Git.

## Reproduce core checks

Run from the checkout, with Hugo Extended 0.139.4 and Go available. Use output directories outside source.

```bash
HUGO_ENV=production hugo --gc --minify -b https://xushidang-lab.netlify.app/ -d /absolute/production-build
python -B scripts/audit-research-visuals.py /absolute/production-build
python -B scripts/audit-publications.py /absolute/production-build
HUGO_ENV=production HUGO_DEPLOY_CONTEXT=preview hugo --gc --minify --buildFuture -b https://example.invalid/ -d /absolute/preview-build
python -B scripts/audit-research-visuals.py /absolute/preview-build
git diff --check
```

For presentation-only changes, add `--before /absolute/preceding-build` to the publication audit. Its strict count/order check intentionally does not pass against a pre-addition 78-record baseline; this batch separately verified preservation of all original records.

`https://example.invalid/` is an offline validation origin, not a hosted preview. On this workspace the binaries are `/workspace/tools/hugo-0.139.4/hugo` and `/workspace/tools/go-1.23.4/go/bin/go`.

## Continue in small batches

1. Recheck main and `content/publications-2025-2026`. PRs #8 and #9 are merged and included in this branch’s base; preserve any newer user changes.
2. Review and merge only after an explicit release instruction. This batch makes no merge or hosting change.
3. Finish the bibliography completeness check against a readable current SCUT/Scholar list or export, and check for verified final venues for the three preprints. Next text-management batch: move About's remaining page-level copy into `website_text.yml`, preserving output and the already connected shared definitions. Then extend the same approach to Contact, Research and the other pages.
4. Keep individual publication, news and member records separate. Use `docs/website-text-maintenance.md` as the current editing map.
5. Resume the About testbed explanation, public research-culture content, navigation and publication-resource improvements in later batches. Do not publish unfinished operating-handbook or private management material.
6. Earlier mobile/tablet, 200% text/zoom and whole-site browser-review items remain separate; the Gallery repair's own coverage is recorded on PR #8.

## Historical checkouts

The original `/workspace/sites/xugroup-web` and its PR #3 are historical work in `derndy/XuGroupWeb`; preserve them and their untracked candidate PNGs. `/workspace/sites/xugroup-web-v2` shares the Git database with this checkout. Old local `main` is not proof of remote `main`. The original prepared local source history remains under `checkpoint/local-source-20260905`.

## Historical GitHub delivery — grammar batch

Published to `design/homepage-research-grammar` in commit `699c9ce6f6fe4641ffa7f2e02a0d5dc929a9a9fa`; its tree `743a2a3dd3d4d1b7af68148cac57ee12c72503cf` exactly matches the tested local source. This later state-record commit changes documentation only. The connected GitHub account originally created [Draft PR #2](https://github.com/derndy/XuGroupWeb-v2/pull/2) targeting `main`. That delivery did not merge it; GitHub now reports that PR merged before this continuation.

GitHub reported zero commit statuses at the prepared head. No matching hosted Netlify preview has been confirmed. A draft PR is a source review link, not a running website preview. The former production URL still requires a separate deployment-state review before any release decision.

## Historical GitHub delivery — evidence-loop batch

Published to `design/homepage-evidence-loop` in commit `a4b6167f6434c4bd5a392573eb55ccaefcef2e75`. The published tree `7ffba7e892ada4944ce7e5f9f505808594a7fdc4` exactly matches the locally tested source. The local source commit is retained under `checkpoint/evidence-loop-local-source`, and the working branch is aligned with GitHub. This later state update is documentation only.

[PR #3](https://github.com/derndy/XuGroupWeb-v2/pull/3) was delivered as a draft targeting `main` and has since merged before this continuation. No merge or production switch was performed by that delivery. GitHub reported zero commit statuses at the prepared head; no corresponding hosted preview is confirmed. Inspect actual PR/branch/deployment state before the next continuation.

## Historical GitHub delivery — homepage records batch

Published to `design/homepage-publications-people-news` in commit `f9044c8d40353e44b573c48fe760e1fcbfe145f3`. The published tree `c09c8b969071ab8851eeed38d74fa056759c49f5` exactly matches the locally tested source. The original local commit is retained under `checkpoint/home-records-local-source`; the checkout is aligned with the GitHub branch. This subsequent state-record update changes documentation only.

[PR #4](https://github.com/derndy/XuGroupWeb-v2/pull/4) was delivered as a draft targeting `main` and has since merged before this continuation. At delivery GitHub reported `netlify/xushidang-lab/deploy-preview` **success** for the product commit, with [the matching preview](https://deploy-preview-4--xushidang-lab.netlify.app). This is the first confirmed hosted preview for this batch. It has not received real browser/interaction review. Future documentation commits may trigger another preview build; inspect the actual PR head and check status before release.

The source delivery did not merge the PR, modify either main branch, or change hosting settings/production. Do not infer production state from preview success. The following continuation implements Contact's four audience pathways.

## Historical GitHub delivery — Contact pathways batch

Published to `design/contact-pathways` in commit `3a70b70f8d6d2ed492030bd9fb3749352a8e11f7`. Its tree `4bd9933a8571678dd0c0fd9d9a5e9fcc1b037b5b` exactly matches the tested local source. The original local source commit is retained under `checkpoint/contact-pathways-local-source`; the checkout is aligned with GitHub. This subsequent project-state update changes documentation only.

[PR #5](https://github.com/derndy/XuGroupWeb-v2/pull/5) was delivered as a draft targeting `main` and has since merged before this continuation. At delivery GitHub reported `netlify/xushidang-lab/deploy-preview` **success** for the product commit, with [the matching Contact preview](https://deploy-preview-5--xushidang-lab.netlify.app/contact/). Real browser, keyboard/touch, zoom and installed mail-client behaviour remain unreviewed. Documentation commits can trigger a further preview build; check the actual final PR head before release.

This delivery did not merge the PR, modify either main branch, send email, or change hosting settings/production. The following continuation implements About's Space–Interaction–Learning explanation with approved image 04 in the middle chapter.

## Historical GitHub delivery — About learning chapter

Published to `design/about-learning-system` in commit `8fe262b3f8d250b0bfb6300f2eab824a124a8013`. Its tree `c91434f2bbc77bfbf805a34d345a66b65f6ab801` exactly matches the tested local source. The original local commit is retained under `checkpoint/about-learning-local-source`; the checkout is aligned with GitHub. This subsequent project-state update changes documentation only.

[PR #6](https://github.com/derndy/XuGroupWeb-v2/pull/6) was delivered as a draft targeting `main` and has since merged before this continuation. At delivery GitHub reported `netlify/xushidang-lab/deploy-preview` **success** for the product commit, with [the matching About preview](https://deploy-preview-6--xushidang-lab.netlify.app/about/). Real browser layout, keyboard/touch, zoom and image loading remain unreviewed. Documentation commits can trigger a further preview build; check the actual final PR head before release.

This delivery did not merge the PR, modify either main branch or change production/hosting settings. The following continuation implements About's shared research principles and NOW/NEXT/HORIZON sequence.

## Historical GitHub delivery — About principles and directions

Published to `design/about-principles-horizons` in commit `e41f614cf84f7a3b76e375f78edb075c09b91a7e`. Its tree `93c29084a2431a176e4d3e818d41d800561e78ea` exactly matches the tested local source. The original local commit is retained under `checkpoint/about-principles-local-source`; the checkout is aligned with GitHub. This subsequent project-state update changes documentation only.

[PR #7](https://github.com/derndy/XuGroupWeb-v2/pull/7) was delivered as a draft and has since merged. GitHub reports `netlify/xushidang-lab/deploy-preview` **success** for the product commit, with [the matching About preview](https://deploy-preview-7--xushidang-lab.netlify.app/about/). Real browser layout, keyboard/touch, zoom and image loading remain unreviewed. Documentation commits can trigger a further preview build; check the actual final PR head before release.

This delivery did not merge the PR, modify either main branch or change production/hosting settings. Next bounded source batch: why molecular/material testbeds matter, using existing public research questions and actual destinations.

## Historical GitHub delivery — Gallery overlap repair

Published to `fix/gallery-overlap` in commit `a5a7d360a9091c876035d25fbca3e0f54195710e`; tree `f60a55f8c8beba01c5d21d40f9edec3569124688` exactly matches the locally tested source. The original local commit is retained under `checkpoint/gallery-overlap-local-source`; the checkout is aligned with the remote review branch. This following update records verification and delivery only.

[PR #8](https://github.com/derndy/XuGroupWeb-v2/pull/8) was delivered as a draft and has since merged. Netlify reports a successful Deploy Preview for the product commit, and the [actual Gallery preview](https://deploy-preview-8--xushidang-lab.netlify.app/gallery/) received the desktop checks listed above. Documentation updates may trigger another build; inspect the final PR head before release.

No PR merge, original-repository edit, production switch or hosting/workflow change was performed by this repair. The separate workflow deletion on main is preserved. Next content batch remains About's explanation of why molecular/material testbeds matter, after reconciling the current PR/main state.

## Historical GitHub delivery — homepage text file

Published to `refactor/homepage-text-file` in product commit `2ec0194313b49d0bcd854c5687fb6fb11d90591a`. GitHub tree `fd5f97342f2a49622a17d915f8d69039efc4efcd` exactly matches the checked local source. The original local commit is retained at `checkpoint/home-text-local-source`; the working checkout was aligned with the published branch. This following update records delivery only.

[PR #9](https://github.com/derndy/XuGroupWeb-v2/pull/9) was delivered as a draft and merged during this Publications update. Netlify reports **success** for the product commit: [homepage preview](https://deploy-preview-9--xushidang-lab.netlify.app/). This confirms the hosted build, not browser interaction coverage. Documentation updates may trigger another build; inspect the final PR head before release.

No PR merge, original-repository edit, production switch or hosting/workflow change was performed by this batch. Next text-management batch: About's remaining page copy, with the same output-preservation check.

## GitHub delivery — Publications update

The verified source is prepared on `content/publications-2025-2026`. Public branch, draft PR, tested tree and actual Netlify status will be recorded after the authorized GitHub write. No production release is requested.

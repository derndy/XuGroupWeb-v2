# Xu Lab website — current project state

Updated: 6 September 2026. Read this file first when continuing development. `PROJECT_STATE.md` is a compatibility pointer to this canonical lowercase file.

## Current source and delivery boundary

| Item | Current value |
| --- | --- |
| Repository | Public `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-pillar-i-visual` |
| Current review branch | `content/people-responsive-photos` |
| Branch point | `main` at `80f49e4295639d90216583a234d11b89912e4708`, after PR #21 merged |
| Incorporated main | Includes merged PRs #14–21 |
| Previous merged work | PRs #1–10, #12–21; preserved in this review branch |
| Gallery repair | [PR #8](https://github.com/derndy/XuGroupWeb-v2/pull/8), merged while this batch was being prepared; its changes are included in the base |
| Current PR | [Draft PR #22](https://github.com/derndy/XuGroupWeb-v2/pull/22), open for review; PR #21 is merged |
| Hosted preview | [People](https://deploy-preview-22--xushidang-lab.netlify.app/people/); check matching Netlify status before release |
| Withdrawn rewrite | [PR #11](https://github.com/derndy/XuGroupWeb-v2/pull/11), closed without merging at the PI's instruction |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Current release instruction | Review branch and draft PR only; no merge or production switch |

The PI rejected PR #11's broad public-marketing rewrite because it made the lab sound generic and displaced the original research identity. It was closed without merging. Merged PR #12 retains the original identity with six wording refinements and places the complete Vision at the end of Join / Collaborate. Do not restore the withdrawn rewrite or the superseded homepage placement. The latest instruction accepts bounded method/testbed and postdoctoral-invitation improvements, requests five selected papers including NC/ECCV, and asks to remove the public research pages' internal management/audit tone.

## Latest batch — People photographs

Added 36 proportional WebP versions across 22 placements: three existing group photographs (one reused on Home) and 18 member portraits. Actual intrinsic image dimensions replace hard-coded portrait dimensions. All originals, captions, member identities and profile routes remain unchanged. The welcome photograph's 800-pixel version is 89,752 bytes versus the 1,914,729-byte PNG original.

Production build and baseline audits pass. All 250 local image references resolve, all new variants have valid dimensions, and visible main-element text throughout the generated site is preserved. Browser viewport testing remains pending. See [batch record](docs/people-responsive-photos-2026-09-06.md). Paper sourcing priorities remain PyraE2E and the selected JACS paper.

## Previous batch — Gallery image sizes and framework viewing

Added 68 proportional WebP variants for the 23 existing Gallery photographs, selected according to the established grid widths. JPEG fallback thumbnails, original-photo viewing, captions and viewer metadata are preserved. All three framework diagrams now have direct wide/vertical SVG links. No new photographic facts or research results are introduced.

Both builds pass; all 250 populated local image references resolve in 536 index pages. Gallery text/viewer attributes and framework explanations match the baseline. The seven conceptual-image audit and 91-publication audit pass. Browser viewport testing remains pending. See [batch record](docs/gallery-responsive-images-2026-09-06.md).

## Previous batch — SyncAnimation and paper-image loading

Added Figure 2 directly from the CC BY 4.0 arXiv v1 paper to the SyncAnimation homepage selection and detail page. Its credit explicitly names that source version; the IJCAI record and author symbols are unchanged. Three of five homepage selections now have authentic method figures. The complete original is retained, with full-size viewing and a wide homepage placement.

Added a 1600-pixel intermediate WebP size for all three paper figures, closing the jump between 1200 pixels and full resolution. There are now 15 paper-image derivatives across six placements. All 250 populated local image references resolve in 536 index pages. Both builds and all existing image/publication audits pass; ten other main pages remain unchanged. Browser viewport testing remains pending.

Source and checks: [SyncAnimation visual record](docs/syncanimation-visual-2026-09-06.md). PR #19 has merged; this batch has a new draft PR. Next remaining selected-paper figures: PyraE2E and the selected JACS paper.

## Previous batch — AnyAvatar figure and News image descriptions

Added the authors' original AnyAvatar pipeline to its homepage selection and accepted-paper detail. The full-width homepage composition suits the wide figure; the original remains uncropped and available for full-size viewing. Source/license checks are recorded in [the batch note](docs/anyavatar-news-visuals-2026-09-06.md). Reuse is under CC BY-NC 4.0 for this noncommercial academic website, distinct from E-CloudBind's CC BY 4.0.

Four 2026 News records already contained `featured_alt`, but the detail header only read `image.alt_text`. A pinned header override now uses the existing description as fallback and displays it below the image when no caption exists. It does not duplicate or invent event facts. Both builds, all 91 publications and seven conceptual-image audits pass. Ten other main pages are unchanged; 248 populated image references resolve in 536 index pages. Browser viewport review remains pending.

PR #18 is merged; this batch has its own draft review branch. Next paper visuals: PyraE2E, SyncAnimation and the selected JACS paper.

## Previous batch — first source-backed selected-paper figure

Added the official E-CloudBind Figure 2 to its homepage selection and publication detail page. The original 2005 × 1791 PNG is retained byte-for-byte, with proportional WebP variants, full-size viewing, author attribution and the article's CC BY 4.0 license. The figure is published research artwork, distinct from the site's seven generated conceptual illustrations. No experimental figure is recreated or cropped.

Source and validation: [selected-paper visual record](docs/selected-paper-visuals-2026-09-06.md). Both builds and existing image/publication audits pass; ten other main-page content trees are unchanged, and 246 populated local image references resolve across 536 generated index pages. The Gallery viewer's one initially empty image is intentional. Browser layout review is still pending. Next: source-backed visuals for the remaining four homepage selections; review legacy image alt text in bounded batches.

PR #17 has merged. This batch uses a new draft PR and does not merge or change production configuration.

## Previous batch — whole-site image review and three framework diagrams

Continued at the PI's instruction to inspect the whole site and increase or improve imagery. Added three precise, editable SVG frameworks, each with a desktop and a mobile composition. Pillar I shows joint design, Pillar II shows the evidence feedback loop, and Pillar III shows stress-test feedback to assumptions. Existing node labels and explanations remain canonical in `data/research_system.yml`; the full HTML explanation is available below each diagram. The seven raster illustrations and all publication content are unchanged.

See [the whole-site image review](docs/website-image-review-2026-09-06.md) for coverage, validation and remaining priorities. PR #16 merged while this batch was being prepared. Deliver these changes on a new draft PR; do not merge or change production. The prior image batch follows below.

## Previous batch — regenerate and upload Pillar I visual

The PI instructed “原文件找不到，重新制作并上传”. Regenerated the unavailable original as a new conceptual illustration, CONCEPT-RES-007, and placed it on Pillar I using the existing responsive component. Source, hash, caption and instruction-based authorization are recorded in [the asset note](docs/pillar-i-visual-2026-09-06.md). This is not an exact recovery or a claim of separate PI pixel review. The seven illustrations produce 28 uncropped responsive WebP variants. Original page text, the architecture map, all 91 publications, News, Gallery and member records are preserved. Browser layout review and the known legacy author-archive slug collision remain separate follow-ups. Next visual priority: source-backed figures for the five selected papers.

PR #15 has now merged; the sections below record earlier work and its historical delivery status.

## Historical repair — resolve PR #15 conflicts with main

Main merged PR #14 after PR #15 branched. The merge conflicts were confined to `README.md` and this state file; both development histories are retained. The stylesheet merged automatically, keeping both the member-profile styles and the five-paper layout changes.

- Incorporated main at `d980fbb9a03d99dcf9fd0397d8905cec5fcd6d5f` into the PR branch with both histories retained.
- Preserved PR #14 News, Gallery, member records, portraits, profile fixes and the visual-expansion plan.
- Preserved PR #15's five selected papers, research invitations, public-facing wording and central Contact text source. No new editorial or image decisions are made.
- Production and preview-equivalent builds pass (895 pages each), along with both publication/image audits, nine JavaScript tests, three DOI tests and 1,440 internal links across the eleven main pages. Exact source comparisons preserve all 46 main-side changed files and all 14 PR-side changed files outside the two documentation resolutions and shared stylesheet. The stylesheet retains both branches' changes. Five selected papers are present.
- The repair updates the existing PR #15 with a two-parent merge commit, without rewriting its history. Check its matching Netlify status before release. No merge into main or production-setting change is performed; browser review and the previously noted author-archive collision remain separate follow-ups.

## Incorporated PR #14 — member-detail repair and visual priority

- On the existing draft PR #14, repaired the 18 member detail pages without editing member facts or images. Added a visible category-aware Back to People link, a semantic main/H1 and portrait dimensions. Replaced inline global CSS and history-only navigation with scoped styles and ordinary links; long contact strings wrap and education/experience rows stack on narrow screens.
- Production/preview builds pass (895 pages). Profile content/links, the eleven main-page content trees, all 91 publications and six approved scientific illustrations are preserved. Browser layout testing remains pending.
- The PI then requested more images and diagrams. The next priority is explained in [the visual expansion plan](docs/visual-expansion-plan-2026-09-05.md): first a Pillar I candidate, then source-backed selected-paper visuals, then targeted research scenarios. One conceptual candidate is shown in conversation for approval; no new research image has been published or marked approved.
- Historical delivery was on PR #14, subsequently merged into main. Its content is now incorporated into PR #15 to resolve conflicts; the original v1 PR remains untouched. PR #15 remains a draft, with no production-setting changes.

## Previous batch — migrate v1 News, Gallery and People

- Migrated six News entries and four Gallery photographs from v1 PR #2 into the current v2 design. Added the two new profiles/portraits and graduate alumni section, updated member roles, and reconciled the two undergraduate graduates named in the source news.
- **PI correction: Yuting Qin and Shidao Wang joined in 2026.** Their News record displays only that year; no month/day is invented. Their profiles also say 2026.
- Preserved all existing News/publication sources and 19 Gallery records. Current totals: 24 published News, 23 Gallery images, 16 current profile cards, two graduate-alumni cards, five undergraduate rows and eleven undergraduate alumni rows.
- [Migration audit](docs/v1-content-migration-2026-09-05.md) accounts for all 32 source PR paths and records the profile/date corrections. New image bytes are exact copies of the source PR; Gallery layout and viewer are unchanged.
- Both Hugo builds pass: 895 pages each. All 91 publication records/citations, six approved illustrations/24 variants and 1,400 internal links/anchors pass checks. Seven other main-content trees match main; Home only refreshes its canonical latest news. Browser review remains pending.
- Working outputs: `/workspace/scratch/7457cd2d5ea9/build-v1-migration` and `build-v1-migration-preview`. The one-off verifier is `verify-v1-migration.py` in the same scratch directory.
- Remaining factual details: exact incoming-member joining day, Meitang Peng's MSc completion/transfer history, and the two new undergraduate alumni's next positions. No unresolved fact is invented.
- Publish this branch and a draft PR only. Do not merge or change production. Do not modify, merge or close the source v1 PR.

### Migration delivery

Published product commit `3f21125ebad68c6218a66ff0eeb44ae2aee1d846` has tree `c356549b3fd7e4ecbcd27e830055ddb8fe524217`, exactly matching the verified local source. All 13 unique new image blobs were copied to v2 with matching source Git hashes. Netlify reports success for the product commit at the preview links above. The local source checkpoint is retained at `checkpoint/v1-migration-local-source`.

This following documentation-only commit records the delivery. Inspect the final PR-head Netlify check before release. No v1 modification, PR merge, production switch or hosting/workflow change was performed. The new joining-year correction is 2026; exact day, the noted MSc history and undergraduate alumni destinations remain the only factual follow-ups from this migration.

## Previous follow-up — Join / Collaborate text in one editing file

PR #15 remains open and draft; this source-only follow-up continues its existing branch from `4754daf11392323de49f24067c13a812ff1ba162`. No new copy, visual design or research claims are introduced.

- Moved exact Contact hero, four pathways and closing text to `data/website_text.yml` → `contact.hero`, `contact.pathways` and `contact.closing`. Existing contact-detail labels and appointment-button text live at `contact.information`. The full `contact.vision` remains unchanged at page end.
- `data/contact_page.yml` retains contact facts and the original documentary photo record. Page title/search summary retain `content/contact/index.md`. Templates combine the central copy with canonical email facts; all subjects, URLs, IDs and factual values are preserved.
- Production and preview-equivalent builds pass, 885 pages each. All eleven main-page HTML files are byte-identical to the preceding PR #15 outputs in both contexts. Exact YAML comparisons verify every moved value and unchanged facts/photo/Vision/other website copy. A temporary one-file label edit reaches Contact only and was restored. Publication and approved-image audits pass.
- Build outputs are `build-contact-text` and `build-contact-text-preview` under `/workspace/scratch/4a70b09acb33/`; preceding `build-research-invitations` outputs are the baseline. These are reproducible temporary outputs, not source files.
- Separate follow-up discovered during broader comparison: legacy starred and unstarred author taxonomy names can generate the same archive URL. Some author archive titles and paper lists vary between builds, e.g. `Ben Zhong Tang` / `Ben Zhong Tang*` at `/author/ben-zhong-tang/`. No author data or taxonomy template changes belong to this text migration. Do not claim archive-wide byte identity; investigate and fix the collision in a separate bounded batch while preserving role markers and canonical publication records.
- No browser testing, PR merge or production-setting change is performed. The editing guides and README now show the new Contact text paths. The existing PR #15 preview URL is retained; verify the new head's status after saving.

Next bounded development candidate: diagnose the legacy author-archive collision, then repair its routing/list assembly without altering corresponding/co-first roles. Do not change research wording or replace the selected papers as incidental cleanup.

## Previous batch in the same draft — five selected papers and public-facing research invitations

- Selected E-CloudBind (Nature Communications 2026), PyraE2E (ECCV 2026, Accepted), AnyAvatar (ACM MM 2026, Accepted), SyncAnimation (IJCAI 2025) and the self-improving photosensitizer discovery system (JACS 2021). The fifth is deliberately older to show the active-discovery foundation; this is not a five-newest ranking. All 91 archive records remain.
- `data/homepage.yml` contains ordered `page`/`focus` references. `website_text.home.publications.focus` supplies one short research-focus label per paper; titles, authors, roles, venues, DOI and BibTeX still come from canonical bundles. Accepted papers retain year-only dates and have no invented online date/DOI. Citation downloads move inside the individual entries instead of repeating five titles in a sidebar.
- Home and Research clarify that model architectures, learning methods and evidence acquisition are contributions in their own right. Molecular, biological and materials systems remain important testbeds. Formal pillars and their questions are unchanged; no extra fields are added to Pillar III.
- Join explicitly invites method/architecture-led postdoctoral proposals and discussion of how they connect with group research and needed project support. It does not promise a funded opening, particular facility or resource. Contact facts and all email subjects remain unchanged.
- Research/pillar language such as evaluation contracts, owners, adjudication and release review is replaced by scientific explanations of comparison, evidence quality, reproducibility and experimental confirmation. Technical approval/metadata checks remain intact. The shared NOW horizon also changes on About; its other content does not.
- The original hero, Space–Interaction–Learning definitions, pillar cards and complete final Contact Vision are preserved. [The bounded review](docs/research-copy-and-selected-work-2026-09-05.md) flags the material changes, selected-paper rationale, source limitations and representative wording comparisons.

### Validation and delivery

- Production and preview-equivalent builds pass, 885 pages each. All 91 publication records, author identities/roles, citation bytes and six approved originals/24 variants pass existing audits.
- All 1,417 internal links/anchors across eleven main-page documents resolve in both builds. H1/main landmarks, unique IDs, matching production/preview content and preview-only noindex pass.
- Five-paper HTML checks pass for order, canonical titles/authors/citations, focus labels, correct journal/conference types, Accepted states and year-only dates. Isolated invalid selections are rejected for duplicates and accepted preprints masquerading as conference papers.
- All nine existing publication JavaScript tests and three DOI regression tests pass.
- Original hero, homepage grammar/pillars/evidence loop/people/news are unchanged. People/Gallery/News/Publication main-content trees match baseline; Contact details/mailto subjects/final Vision match baseline. About differs only in the shared NOW horizon.
- Reproducible scratch builds: `build-research-invitations`, `build-research-invitations-preview`, with baseline `build-vision-contact` under `/workspace/scratch/4a70b09acb33/`. Source baseline is the branch point above; generated files are not committed.
- Browser layout/interaction review remains pending. The five-paper section is longer than the old two-paper section even after eliminating the repeated citation column. No PR merge, hosting change or production switch is performed.
- Published as draft PR #15 in product commit `dd576a74a89d7b36f9439a378e5da321dee25125`. Its tree `e931e8a448a7f04d223aa31f3217771fe02896d2` exactly matches the checked local source. Netlify reports success for that product commit. This delivery-note update does not change page content; any new commit triggers its own preview check.

Next review: inspect the new homepage selection and Join invitation, confirm the intentional older JACS choice, and check narrow-screen layout before release. Keep the remaining SCUT/accepted-author source reconciliation items from the prior bibliography audit separate; no new author metadata is introduced here.

## Previous completed batch — move Vision to the end of Join / Collaborate

- Removed the full Vision chapter from Home and appended it after the approved closing illustration on `/contact/`, the page labeled Join / Collaborate in navigation. It is the final section before the site footer.
- Moved the single text source from `home.vision` to `contact.vision` in `data/website_text.yml`. Every text value is preserved exactly. The earlier six wording refinements are untouched; this relocation makes no further editorial choices.
- Moved the same scoped styles into `_contact.scss`, renamed the chapter's classes/anchor for Contact, and retained the existing small-screen layout. The new direct destination is `/contact/#contact-vision-title`.
- Preserved all existing Contact pathways, contact details, photograph, illustration and their order. The rest of the homepage, including its closing Join / Collaborate button, is unchanged.
- Incorporated main's newly merged PR #13 in the review branch. README/state conflicts were resolved by retaining both histories; all new publication content and author-role implementation match main exactly.
- The PI requests prominent reporting of major changes and uncertain choices. This batch's only substantive page change is the requested relocation; future batches must flag semantic/positioning uncertainty rather than grouping it under minor edits.

### Validation and delivery of the relocation

- Production and preview-equivalent Hugo builds pass: 885 pages each. Both pass the 91-record publication/citation audit and the six-approved-image/24-variant audit.
- YAML comparison confirms that only the vision's data path changed. Rendered vision text matches the preceding homepage chapter exactly, appears once on Contact, is its final main-content section, and is absent from Home.
- All eleven main-content trees match the combined PR #12 + latest-main baseline after accounting for the relocated chapter. All 1,377 internal links/anchors resolve; H1/main landmarks, unique IDs and preview-only noindex pass.
- Build outputs: `/workspace/scratch/4a70b09acb33/build-vision-contact` and `build-vision-contact-preview`; combined-source baseline: `build-vision-move-before`. All are reproducible scratch outputs outside Git.
- Delivery updates the existing draft PR #12, preserving the earlier review history and merged PR #13. No PR merge, production switch or hosting change is performed. Real browser layout/interaction review remains pending.

## Previous iteration — original identity with the PI's homepage vision

The following records describe the earlier placement. The latest instruction above supersedes that placement; the wording remains intact.

- Preserved the original hero title, subtitle, tagline and buttons; formal pillar titles, roles, questions and cards; and Space–Interaction–Learning framing. All publication, news and member records retain their separate sources.
- Added `home.vision` in `data/website_text.yml`, rendered as an unnumbered chapter after Beyond Prediction. Existing chapter numbering stays unchanged. The English adaptation and original Chinese vision are documented in `docs/website-text-maintenance.md`.
- Retained the broad goal of understanding the world, identifying emerging questions and cultivating future leaders. Scientific foresight, conditional decades/centuries horizons, evidence, revision and explicit assumptions remain visible.
- Presented domain intelligence system architects as one training path. Includes model architecture, infrastructure, scientific and intelligent systems, objective functions, search spaces and evaluation criteria, with short explanations of the last three. Intelligence per unit of energy is an illustrative open question; the vision leaves room for future problems and methods.
- Changed only six existing YAML values: one additive sentence connecting the original thesis to AI for Science/scientific foundation models/generative design, two testbed wording simplifications, the Learning definition, the Mechanism link label, and one evidence-loop explanation. The two learning edits reduce operational specificity; no detailed research-roadmap rewrite or whole-site confidentiality claim is made.
- Added scoped `.home-vision` styles using the existing typography/colours and a single-column small-screen layout. No JavaScript, images, dependency or hosting changes.

### Validation of the vision refinement

- Production and preview-equivalent Hugo builds pass: 864 pages each.
- Both builds pass the existing audits for all 88 publication records/citation bytes and six approved illustrations/24 variants.
- All 1,334 internal links and anchors across the eleven full main-page documents resolve, including navigation/footer links. Each has one H1/main and unique IDs; preview-only noindex and matching production/preview main text are verified.
- Original hero copy/actions, all three pillar cards, selected-publication/people/news sections and the closing invitation are unchanged. Nine other main-content trees match baseline; About differs only in the intended shared Learning definition.
- All requested vision concepts, the conditional long horizon, the open energy question and the qualification of architects as one path appear in generated HTML. A structured YAML comparison confirms exactly six changed existing values; every new field is under `home.vision`.
- Whitespace checks pass. Real browser layout/interaction review of the added chapter remains pending; build and HTML checks are not browser QA.

Build outputs: `/workspace/scratch/4a70b09acb33/build-home-vision` and `build-home-vision-preview`. Baseline: `build-public-copy-current-baseline`, built from main at `99698f1`. These are reproducible scratch outputs outside Git. The rejected `build-public-copy` output is not a valid baseline for future work.

### GitHub delivery

Published to `content/homepage-vision-refinement` in initial product commit `4737805d0d67471e86625081c5222442f2b01dac`. Its tree `aa95abf41a52d30405d3a95c56b1f42987bb1b92` exactly matches the checked local source. The original local commit remains at `checkpoint/home-vision-local-source`. [Draft PR #12](https://github.com/derndy/XuGroupWeb-v2/pull/12) targets main; Netlify reports **success** for that product commit and the preview linked above.

The following delivery update records the PR and makes two small fidelity adjustments within the new vision: questions of growing importance, and questioning assumptions that limit our thinking. It does not add further edits to the six original-text values. Production and preview builds pass again. Subsequent commits trigger another preview build; inspect the final PR head and its status before release. No merge, production switch or hosting/workflow change was performed.

## Previous completed batch — author roles and accepted conference work

PR #13 has merged into main at `ddd34615da16f6e2fe3b085c66972bc10c8fe13a` and is included in this review branch.

- Unified publication author display: `*` means corresponding; `#` means co-first/equal contribution. Existing author taxonomy identities and links are retained, including legacy marked names. A visible legend appears on the index and details; superscripts have accessible labels.
- Added verified author-role metadata to ten recent records. The 75 legacy correspondence assignments and 14 legacy co-first assignments are preserved. This is not a complete new audit of all historical contributions.
- Added three 2026 accepted conference bundles with citations: AnyAvatar (ACM MM), MPFusion-MIL (ACM MM), and PyraE2E (ECCV). No unassigned DOI, page range, online date or acceptance day is invented. The Hugo sorting anchor is displayed only as a year and is omitted from accepted-work publication metadata.
- Added a distinct accepted-work overview linking all five 2026 conference works. CDSR and MoGaFace now disclose PRCV 2026 acceptance while retaining clearly identified 2025 preprint citations. Their final conference author metadata needs the current profile or final manuscript; the older preprint author lists are not presented as final conference citations.
- Canonical inventory: 91 records across 15 years and seven types. The accepted overview is five links to these records, not five additional records. Year/type filters retain canonical publication/preprint dates.
- Source evidence, role assignments, discrepancies and version limits are in [the authorship/Accepted audit](docs/publication-authorship-accepted-2026-09-05.md); schema/update instructions are in [Publications maintenance](docs/publications-maintenance.md).

### Validation

- Production and preview-equivalent builds pass, 885 pages each. Both pass the 91-record publication audit and six-approved-image / 24-variant audit.
- Nine existing Node tests and three DOI tests pass. Three isolated invalid-content builds correctly reject an unknown role, a role naming a missing author, and an accepted record without acceptance metadata.
- All 13 new/updated role mappings match the generated index and detail authors. All 88 previous author identities, order, record URLs and attachment actions are preserved. Original 78 source bundles and assets remain byte-identical; 86 previous citations are unchanged, and the other two change only their PRCV acceptance/version notes.
- Three new accepted records show year-only dates, correct conference types, explicit Accepted citations, and no invented DOI/pages/dates in their HTML, BibTeX or JSON-LD. Both PRCV preprints retain their original date, authors and DOI.
- All 1,245 internal links/anchors across eleven main pages resolve. Nine other main-content trees are identical; homepage text and author links are preserved with only shared symbol markup changing. Production/preview main content matches and preview noindex is retained.
- No browser visual or interaction QA was performed for this bibliography batch. Current SCUT reconciliation and the noted final-author discrepancies remain content follow-ups.

Temporary outputs: `/workspace/scratch/7457cd2d5ea9/build-authorship-accepted` and `build-authorship-accepted-preview`. The one-off preservation verifier is `/workspace/scratch/7457cd2d5ea9/verify-authorship-accepted.py`. The public source audit is the durable evidence record; private source documents are not committed.

## Previous completed batch — Publications for 2025 and 2026

PR #10 has merged. The bibliography was first verified against PR #8 at `bd762ef…` and rebased onto merged PR #9 at `83a9fcd…` during its delivery, preserving the homepage text migration and Gallery repair. Both builds and the preservation audit passed on the combined source. The following records describe that completed addition.

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
10. Preserve the lab's distinctive research identity. The PI allows restrained simplification, additive familiar terminology and a faithful vision at the end of Join / Collaborate; wholesale marketing repositioning and the earlier homepage vision placement were rejected. Explicitly report substantial changes and uncertain editorial choices. See the current editing guide and do not restore PR #11.

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

1. Recheck main and `content/homepage-vision-refinement`. PRs #1–10 and #13 are merged and included; PR #11 was rejected and closed without merging. PR #12 is the current review draft. Preserve any newer user changes.
2. Review and merge only after an explicit release instruction. This batch makes no merge or hosting change.
3. Review the restrained wording and Vision at the end of Join / Collaborate before another editorial batch. Next text-management batch: move About's remaining page-level copy into `website_text.yml`, preserving output and the already connected shared definitions. Current SCUT reconciliation, bibliography completeness and final PRCV author metadata remain separate follow-ups; retain PR #13's acceptance/version distinctions.
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

## Historical GitHub delivery — Publications update

Published to `content/publications-2025-2026` in product commit `fbe2a439f4519c4aff33f821eac997e24b7b5893`. Its GitHub tree `7c03fb51cd97bb1dc03ddffa702967d11b5947a8` exactly matches the locally verified source after rebasing onto merged PR #9. The local source commit is retained at `checkpoint/publications-2026-local-source`; the isolated worktree is aligned with the public branch. This following update changes documentation only.

[PR #10](https://github.com/derndy/XuGroupWeb-v2/pull/10) was delivered as a draft and has since merged. At delivery, Netlify reported **success** for the product commit, with [the matching Publications preview](https://deploy-preview-10--xushidang-lab.netlify.app/publication/). An HTTP 200 read of that preview confirmed 88 server-rendered records, eight in 2025, two in 2026, and preview noindex. This was an HTML check, not browser visual/interaction QA.

No PR merge, production switch, original-repository edit or hosting/workflow change was performed by this batch. Next bibliography step is completeness against a readable SCUT/Scholar list or export and verified final-version reconciliation for the three preprints.

## GitHub delivery — authorship and Accepted update

Published to `fix/publication-authorship-accepted` in product commit `316ee331e26a79ae2186aeb93c5e3ed928cb63c1`. Its GitHub tree `8131aab17f4bb192d276a9c4aa6a2c2c6c7651db` exactly matches the tested local source. The isolated worktree is aligned with the public branch; its local source commit remains at `checkpoint/authorship-accepted-local-source`.

[PR #13](https://github.com/derndy/XuGroupWeb-v2/pull/13) was delivered as a draft and has since merged. Netlify reports **success** for the product commit at [the Publications preview](https://deploy-preview-13--xushidang-lab.netlify.app/publication/). This following state-record commit changes documentation only and may trigger another preview; check the current PR head before release. No browser visual/interaction QA is claimed.

The current main used by this batch is merged PR #10 at `99698f19834baf7b7aa3da2a358650c78e2535ed`. No merge, production switch, original-repository edit or hosting change was performed. Continue by reconciling the current SCUT profile and final PRCV author metadata; do not silently combine preprint authors with a final conference citation.

# Xu Lab website — current project state

Updated: **6 September 2026**. Read this file first. It is the current handoff record; `PROJECT_STATE.md` remains a pointer to it.

The previous 80,855-byte state record is preserved in full in [project-history-through-pr24-2026-09-06.md](project-history-through-pr24-2026-09-06.md). That file contains historical delivery details and superseded instructions. Use the current snapshot below for decisions; consult the history for context.

## 1. Repository, branch and delivery state

| Item | Current value |
| --- | --- |
| Repository | Public [derndy/XuGroupWeb-v2](https://github.com/derndy/XuGroupWeb-v2) |
| Production address | https://xushidang-lab.netlify.app/ |
| Stack | Hugo Extended 0.139.4; Hugo Blox / Bootstrap; GitHub + Netlify |
| Source checkout in this session | `/workspace/scratch/04b018b9a160/XuGroupWeb-v2` — this local path is temporary; GitHub is durable |
| Verified main / batch base | `3f0209e3a4cc8231a017c0a4d1b05e30801edc57` |
| Base tree | `a0a577453e7a4cf6f4fb827f403a84774569ee29` |
| Previous PR | [PR #24](https://github.com/derndy/XuGroupWeb-v2/pull/24) **merged**, confirmed through GitHub after the user's correction |
| Current branch | `content/jacs-visual-site-status`, based on that merge |
| Current PR | New draft PR pending creation; this batch does not update merged PR #24 |
| Current preview | Pending the new draft PR and its matching Netlify check |
| Delivery boundary | Publish the review branch and draft PR; the user decides whether to merge. No production-setting changes in this batch. |
| Withdrawn direction | [PR #11](https://github.com/derndy/XuGroupWeb-v2/pull/11) was rejected and closed without merging; preserve the original research identity |

The last confirmed successful preview before this batch belongs to PR #24 at commit `6028651a0e65d3b58ed7881a5835d9a454f69896`. It is evidence about that version only. A successful preview is not proof that production or browser interactions have been checked. Always reread GitHub main, the active PR and its exact-head status when continuing.

## 2. User intent and established choices

- Continue checking the entire site and add or improve useful images and scientific diagrams in small, carefully verified batches. The current request explicitly requires a thorough GitHub status record.
- Keep the site's distinctive research identity, original homepage headline/subtitle/tagline, and the formal three-pillar definitions in the repository. Do not substitute a generic marketing rewrite or infer current pillar names from older conversation summaries.
- Public research language should explain the science and invite interest. Internal audit, ownership and release-management language belongs in development records.
- Five selected papers remain E-CloudBind, PyraE2E, AnyAvatar, SyncAnimation and the 2021 self-improving photosensitizer JACS paper. The older JACS choice is deliberate: it shows the active-discovery foundation.
- Keep the complete Vision chapter at the **end of Join / Collaborate**, as already approved. The withdrawn homepage placement is superseded.
- Maintain the single editable copy source where already established: `data/website_text.yml`. Research scope/details still use `data/research_system.yml`; publication facts and author roles remain in their canonical bundles.
- Treat concept illustrations, exact teaching diagrams and published/author-provided figures as different asset categories. Do not present synthetic imagery or worked examples as measured results.

## 3. Current batch — JACS figure and maintainable status record

### What changed and why

1. The homepage's selected JACS paper previously had no figure although its publication bundle already contained a discovery-system diagram. The existing `featured.jpeg` now serves both Home and the paper detail through the credited paper-figure component.
2. The old uncaptioned detail-page banner is replaced by one credited figure below the article information. The detail page still shows exactly one image, with meaningful alternative text, a source link and original-size viewing.
3. The image component can read a page-bundle resource as well as a global asset. Hash checks and mandatory caption/source/reuse metadata apply to both. No duplicate master image is created.
4. The 693 × 469 original is unchanged. The figure component generates 480- and 693-pixel WebP versions and caps display at native width to avoid enlarging small images. The 480-pixel version is 30,716 bytes, versus 116,517 bytes for the original JPEG.
5. Added `scripts/audit-site-images.py`, a reusable standard-library checker for local image and responsive-picture references. It reports empty alt text as a review queue, not as confirmed defects.
6. Replaced the long, conflicting status chronology with this current snapshot and preserved its entire prior text in the linked history file. `PROJECT_STATE.md` still points here. Prior decisions, checkouts, commits and detailed batch reports remain available.

### Source and reuse basis

The image is the existing author-website resource in the JACS publication bundle. SHA-256: `33091716685e42651e71a28027a7b646064a00cdfc98b6367a2248cb2f1f3073`.

[Published article](https://doi.org/10.1021/jacs.1c08211): Shidang Xu et al., *Journal of the American Chemical Society* 143 (2021), 19769–19777. [ACS author-sharing policy](https://pubs.acs.org/pages/authors_sharing), retrieved from its indexed official text on 6 September 2026, permits authors' noncommercial website reuse of their figures with proper citation and disclosure of changes. The site links that policy and does not label the image Creative Commons. No new publisher image was downloaded; direct ACS page requests returned 403. The original website image was inspected, and the description follows what it visibly shows. No figure number or higher-resolution source was inferred.

Full change/source record: [docs/jacs-visual-and-site-status-2026-09-06.md](docs/jacs-visual-and-site-status-2026-09-06.md).

## 4. Current visual coverage across the site

Counts below describe `<img>` elements inside each main route's main content. HTML diagrams/maps can add visual information without adding image elements. Counts are not unique asset counts.

| Route | Images | Current coverage and next need |
| --- | ---: | --- |
| Home `/` | 6 | Concept image, team photograph and **four of five** selected-paper figures. PyraE2E remains the selected-paper gap. |
| About `/about/` | 1 | Conceptual vision illustration and existing structured explanatory content. |
| Research `/research/` | 1 | Overview illustration and HTML system maps. |
| Pillar I `/research/learning-system-design/` | 3 | Concept illustration, joint-design framework and the worked interaction-structure example from merged PR #24. |
| Pillar II `/research/evidence-engineering/` | 3 | Concept illustration, closed-loop framework and evidence-choice example. |
| Pillar III `/research/mathematical-frontiers/` | 2 | Concept illustration and assumptions/stress-test feedback framework. |
| Publications `/publication/` | 0 | Searchable bibliography; four selected-paper detail pages have credited figures. Preserve the text-focused archive. |
| People `/people/` | 21 | Existing group photographs and profile cards, with responsive variants. |
| News `/post/`, first listing | 10 | Existing article photographs with current listing descriptions. Older detail images need review. |
| Gallery `/gallery/` | 24 | 23 photographs plus the intentionally empty image slot used by the viewer. |
| Join / Collaborate `/contact/` | 2 | Documentary photograph, conceptual illustration and the final Vision chapter. |

### Figure inventory and maintenance locations

| Asset family | Current state | Source of truth |
| --- | --- | --- |
| Conceptual illustrations | Seven originals; 28 uncropped WebP variants; existing captions and scope labels | `data/research_assets.yml`; `layouts/partials/research/conceptual-figure.html` |
| Pillar frameworks | Three frameworks, each with wide/mobile SVGs and full-size links | `scripts/render-framework-diagrams.py`; `data/research_system.yml`; `assets/media/frameworks/` |
| Evidence-choice example | Two SVGs; uncertainty and ambiguous-result path preserved | `scripts/render-evidence-choice.py`; `layouts/partials/research/evidence-choice.html` |
| Interaction example | Two SVGs; same raw-feature mean 2.5, connected-pair products 14 vs 11 | `scripts/render-interaction-structure.py`; `website_text.research_figures.interaction_structure` |
| Selected-paper figures | E-CloudBind, AnyAvatar, SyncAnimation, JACS; original-size links and credits | `data/paper_visuals.yml`; `layouts/partials/publications/paper-figure.html` |
| Gallery photos | 23 masters, 68 responsive WebP variants from the earlier batch | Existing Gallery data, templates and image assets; captions/viewer metadata retained |
| People photos | 18 profile portraits plus group-photo placements; 36 derivatives from the earlier batch | Existing member records, photograph data and People templates |

The seven conceptual images retain the recorded approval/regeneration history. The seventh was regenerated on the user's explicit instruction; this does not imply a separate pixel-by-pixel approval event. Consult the original asset records before changing scientific meaning.

## 5. Validation completed for this batch

| Check | Result and coverage |
| --- | --- |
| Production-equivalent build | Pass; 895 Hugo pages |
| Preview-equivalent build | Pass; 895 Hugo pages |
| Whole-site image references | Pass in both builds: **538 HTML files**, **254 image elements**, **433 local image/picture/srcset references**, **zero missing files** |
| Counter change from PR #24 | The previous report scanned 536 `index.html` files. The new reusable checker also includes `404.html` and `search.html`; 538 is scan coverage, not two newly created content pages. |
| Publication baseline | Pass: 91 records; titles, authors/role links, order, routes, attachment controls and citation bytes preserved |
| Conceptual images / frameworks | Pass: all seven originals, 28 variants and baseline architecture/introductory content preserved |
| Page-content preservation | All eleven main routes plus the JACS detail retain their prior main-element text after excluding the new figure captions; IDs are unique on those routes |
| JACS placement | Four figures on Home; exactly one JACS detail image; meaningful alt text, correct 693 × 469 dimensions and both original-size links |
| Asset integrity | Both placements serve the exact existing JPEG hash; no image edits, cropping or enlargement; 480-pixel WebP visually inspected |
| Historical record | Previous 80,855-byte state text preserved without edits after the history banner |
| GitHub delivery | Pending current product commit and new draft PR; update this row after saving |

Temporary build outputs in this session are `/workspace/scratch/7457cd2d5ea9/build-jacs` and `build-jacs-preview`. The preceding `build-interaction` and `build-interaction-preview` outputs are comparison baselines. These outputs are reproducible and not committed; source, scripts and review notes are saved to GitHub.

### Checks not completed

- Full browser layout, keyboard/touch interaction, 200% text enlargement and reduced-motion testing for the current version. The last browser-preview attempt failed because the available supervised runtime requires a compatible Node development project and this repository is Hugo without `package.json`. This batch does not retry an unchanged setup or add an unrelated framework. Standalone image inspection and successful builds do not establish browser success.
- Live production layout and complete external-link availability. Local image checks do not verify publisher, Scholar, email-client or appointment-service availability.
- Full factual reconciliation of every author role and newly accepted paper against the latest readable SCUT/Scholar sources; see the separate backlog below.

## 6. Remaining issues, in order

| Priority | Item | Concrete next action / completion condition |
| --- | --- | --- |
| 1 | PyraE2E is the only selected paper without a figure | Obtain the authors' actual framework/overview asset and a source/reuse record. Add attribution and full-size viewing; retain Accepted status and avoid invented proceedings facts. |
| 1 | Current-version browser verification | Use a compatible, authorized preview when available. Check Home figures, all five SVG examples/frameworks, Gallery viewer and People on desktop/narrow screens; check keyboard closing/focus and 200% text enlargement. |
| 2 | Legacy image descriptions | Current scan has **80 empty alt entries**: 73 publication-detail images, six News-detail images and one intentional Gallery viewer slot. Review each image with its article/caption before deciding whether it needs a description; never infer identities or event facts. The JACS item is now fixed. |
| 2 | Legacy author archive collision | Starred/unstarred author taxonomy terms can share an archive URL and yield inconsistent author listings. Repair routing/list assembly separately while preserving all author roles and canonical publication records. |
| 2 | Latest SCUT / Google Scholar reconciliation | Latest official SCUT page and Scholar have been intermittently unreadable. Use the user's official homepage as authority when records differ, per their instruction. Resolve missing author markers and final PRCV lists without copying uncertain preprint authors into final citations. |
| 2 | Accepted-paper metadata | Preserve AnyAvatar, MPFusion-MIL and PyraE2E accepted records, and the separate PRCV acceptance notes for CDSR/MoGaFace. Add formal dates/DOIs/proceedings details only with verified sources. |
| 3 | Remaining member facts from v1 migration | Joining year for Yuting Qin and Shidao Wang is confirmed as **2026**; exact joining day remains unknown. Meitang's MSc completion/transfer history and the two undergraduate alumni's next destinations remain unconfirmed. |
| 3 | More explanatory visuals | Add only where a concrete research idea remains hard to understand. Avoid repeating broad conceptual artwork or lengthening pages without a clear benefit. |
| 3 | Text maintenance / later development | About's remaining page-level copy migration and further content refinements are separate bounded tasks; preserve approved research definitions and the final Contact Vision. |

## 7. Recent history and evidence index

All rows below except the current batch are merged work. Historical reports contain the status at their own delivery time.

| Work | Record |
| --- | --- |
| PR #24: concrete interaction-structure example | [Interaction diagram review](docs/interaction-structure-diagram-2026-09-06.md) |
| PR #23: evidence-choice example | [Evidence-choice review](docs/evidence-choice-diagram-2026-09-06.md) |
| PR #22: People photo sizes | [People image review](docs/people-responsive-photos-2026-09-06.md) |
| PR #21: Gallery responsive photos and framework viewing | [Gallery image review](docs/gallery-responsive-images-2026-09-06.md) |
| PR #20: SyncAnimation figure | [SyncAnimation record](docs/syncanimation-visual-2026-09-06.md) |
| PR #19: AnyAvatar figure and News captions | [AnyAvatar / News record](docs/anyavatar-news-visuals-2026-09-06.md) |
| PR #18: E-CloudBind figure | [Selected-paper source record](docs/selected-paper-visuals-2026-09-06.md) |
| PR #17: three SVG frameworks | [Initial whole-site image review](docs/website-image-review-2026-09-06.md) |
| PR #16: regenerated Pillar I concept | [Pillar I asset record](docs/pillar-i-visual-2026-09-06.md) |
| PR #15: selected papers and research wording | [Research copy / selected work](docs/research-copy-and-selected-work-2026-09-05.md) |
| PR #14: v1 News/Gallery/People migration | [Migration record](docs/v1-content-migration-2026-09-05.md) |
| PR #13: author symbols and accepted papers | [Authorship / acceptance record](docs/publication-authorship-accepted-2026-09-05.md) |
| Full prior chronology | [Unedited history through PR #24](project-history-through-pr24-2026-09-06.md) |

## 8. Reproduce checks and continue safely

Run from the repository with Hugo Extended 0.139.4 and Go on PATH. Use output directories outside the checkout.

```bash
HUGO_ENV=production hugo --gc --minify -b https://xushidang-lab.netlify.app/ -d /absolute/production-build
python -B scripts/audit-site-images.py /absolute/production-build
python -B scripts/audit-publications.py /absolute/production-build --before /absolute/preceding-build
python -B scripts/audit-research-visuals.py /absolute/production-build --before /absolute/preceding-build
HUGO_ENV=production HUGO_DEPLOY_CONTEXT=preview hugo --gc --minify --buildFuture -b https://review.invalid/ -d /absolute/preview-build
python -B scripts/audit-site-images.py /absolute/preview-build
python -B scripts/audit-site-images.py /absolute/production-build --json

git diff --check
```

The JSON option lists the pages and sources needing description review. `review.invalid` is an offline test origin, not a hosted site. If no preceding build exists, build the verified base first or omit `--before` and explicitly state that cross-version preservation was not checked. Do not compare against an old 78- or 88-publication baseline and misinterpret the intentional additions as regressions.

Session tools: `/workspace/tools/hugo-0.139.4/hugo`, `/workspace/tools/go-1.23.4/go/bin/go`; Go module cache `/workspace/tools/go-mod-cache`. These paths are conveniences, not project dependencies.

At the next continuation: (1) fetch current main and PR state; (2) preserve any newer edits; (3) choose one backlog item; (4) implement and verify; (5) record scope, files, source limits, checks, exact product commit and preview status here; (6) publish a draft PR or update the still-open one. If the previous PR has merged, start a new branch from current main. Do not treat historical instructions or successful older previews as current authorization or validation.

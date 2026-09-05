# Xu Lab website — current project state

Updated: 5 September 2026. Read this file first when continuing development. `PROJECT_STATE.md` is a compatibility pointer to this canonical lowercase file.

## Current source and delivery boundary

| Item | Current value |
| --- | --- |
| Repository | Public `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-approved-images` |
| Current review branch | `design/homepage-publications-people-news` |
| Base | `main` at `13d699772ec8e76d59fe219511fa370ea8496945` |
| Previous PR | [PR #3](https://github.com/derndy/XuGroupWeb-v2/pull/3), now merged; PRs #1 and #2 are also merged |
| Current PR | Prepared locally; draft PR publication pending |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Current release instruction | Review branch and draft PR only; no merge or production switch |

The earlier status file described PR #1 as open and draft. GitHub now confirms it was merged; its former `design/approved-scientific-images` remote branch was deleted. The grammar and evidence-loop batches have also merged as PRs #2 and #3. This continuation starts from `13d6997…` main, whose website tree matches the tested evidence-loop checkpoint. Do not recreate the deleted branch or repeat the completed six-image integration.

The recorded production URL, `https://xushidang-lab.netlify.app/`, was read on 5 September: HTTP 200, older carousel HTML, three empty Hero headings, and no approved homepage H1. It is not serving the latest v2 homepage observed in source. This checks returned HTML only; Netlify linkage, branch settings and deployment history have not been inspected. Do not infer production state merely from a GitHub merge or the configured `baseURL`.

At the start of this continuation, v2 `main` was `13d699772ec8e76d59fe219511fa370ea8496945`. The original repository and production were not modified. This continuation publishes a review branch only; it does not change either main branch or hosting configuration.

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

## Previous completed batch — homepage scientific explanation

- Replaced the static, absolutely positioned Hero diagram with six native `details`/`summary` concepts: Evidence, Space, Interaction, Learning, Mechanism and Design. Definitions and real research links are usable without JavaScript. Learner dimensions use neutral styling; outcomes are explicitly proposals/aims to test.
- Added H03: scientific questions, definitions, connected choices and an evidence-feedback explanation. Compact and expanded forms share `data/research_system.yml` and `layouts/partials/research/learning-grammar.html`.
- Preserved the already-present Beyond Prediction section and all three exact homepage statements.
- Changed the secondary Hero action to the existing Scientific testbeds section.
- Replaced duplicate homepage pillar content with canonical formal titles, core questions and routes. Each card has a direct Explore link. Existing public invitations and three concise capability terms remain.
- Reduced the Hero headline scale and removed fixed-height pillar cards; added responsive grammar layouts and visible focus styles. Browser confirmation remains pending.
- Saved the design plan, implementation comparison, asset-location record and updated README/state instructions.

The new grammar follows the meaning of the original Drive `space-interaction-learning-map.svg`, which was retrieved and read. It does not publish the original source sheet. The archive manifest lists 91 materials; the six existing repository images already match their approval hashes and were not regenerated or reimported.

## Latest batch — homepage publications, people and news

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

Real browser layout, keyboard/touch, text zoom and photo-loading performance remain pending: the existing Hugo checkout has no compatible internal preview entrypoint. Static checks are not browser QA. The reused below-fold PNG is about 1.9 MB; responsive derivatives can be considered during that performance review.

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
| About | Introductory research identity, image 04 and onward links; fuller vision/culture chapters still pending |
| Contact / Join / Collaborate | Shared layout, central facts, mailto/tel links, appointment link, authentic library photograph and image 06; four audience pathways still pending |
| People | 16 current-member profiles, 7 undergraduate records, 9 alumni records and authentic photographs |
| Gallery | 19 documentary records, year grouping, server-rendered content and progressively enhanced dialog |
| News | 18 published records; incomplete record excluded as draft |
| Publications | 78 records, 13 years, seven types, filters/search, citations and previous verified identity corrections |

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
python -B scripts/audit-publications.py /absolute/production-build --before /absolute/preceding-build
HUGO_ENV=production HUGO_DEPLOY_CONTEXT=preview hugo --gc --minify --buildFuture -b https://example.invalid/ -d /absolute/preview-build
python -B scripts/audit-research-visuals.py /absolute/preview-build
git diff --check
```

`https://example.invalid/` is an offline validation origin, not a hosted preview. On this workspace the binaries are `/workspace/tools/hugo-0.139.4/hugo` and `/workspace/tools/go-1.23.4/go/bin/go`.

## Continue in small batches

1. Check local changes, remote `main`, review branch and actual PR/check status before editing. Preserve newer user work; compare any moved branch with this record.
2. Review the changed homepage at 320 px, tablet, desktop and 200% text/zoom when a supported browser preview is available. Open every concept by mouse/touch and keyboard; verify focus, links and reading order.
3. H05 is merged, and H08–H10 are implemented in this review branch. Verify browser presentation before release; do not repeat the source implementation.
4. Next bounded batch: Contact's four audience pathways, using existing verified contact facts and approved public positioning.
5. Then complete About's middle Space–Interaction–Learning chapter/culture/horizons and expand shell navigation with real destinations.
6. Continue the publication identity/external-download review and approved project/resource connections in separate, evidence-backed batches.
7. Merge or change Netlify only after an explicit release instruction.

## Historical checkouts

The original `/workspace/sites/xugroup-web` and its PR #3 are historical work in `derndy/XuGroupWeb`; preserve them and their untracked candidate PNGs. `/workspace/sites/xugroup-web-v2` shares the Git database with this checkout. Old local `main` is not proof of remote `main`. The original prepared local source history remains under `checkpoint/local-source-20260905`.

## Historical GitHub delivery — grammar batch

Published to `design/homepage-research-grammar` in commit `699c9ce6f6fe4641ffa7f2e02a0d5dc929a9a9fa`; its tree `743a2a3dd3d4d1b7af68148cac57ee12c72503cf` exactly matches the tested local source. This later state-record commit changes documentation only. The connected GitHub account originally created [Draft PR #2](https://github.com/derndy/XuGroupWeb-v2/pull/2) targeting `main`. That delivery did not merge it; GitHub now reports that PR merged before this continuation.

GitHub reported zero commit statuses at the prepared head. No matching hosted Netlify preview has been confirmed. A draft PR is a source review link, not a running website preview. The former production URL still requires a separate deployment-state review before any release decision.

## Historical GitHub delivery — evidence-loop batch

Published to `design/homepage-evidence-loop` in commit `a4b6167f6434c4bd5a392573eb55ccaefcef2e75`. The published tree `7ffba7e892ada4944ce7e5f9f505808594a7fdc4` exactly matches the locally tested source. The local source commit is retained under `checkpoint/evidence-loop-local-source`, and the working branch is aligned with GitHub. This later state update is documentation only.

[PR #3](https://github.com/derndy/XuGroupWeb-v2/pull/3) was delivered as a draft targeting `main` and has since merged before this continuation. No merge or production switch was performed by that delivery. GitHub reported zero commit statuses at the prepared head; no corresponding hosted preview is confirmed. Inspect actual PR/branch/deployment state before the next continuation.

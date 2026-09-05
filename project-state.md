# Xu Lab website — current project state

Updated: 5 September 2026. Read this file first when continuing development. `PROJECT_STATE.md` is a compatibility pointer to this canonical lowercase file.

## Current source and delivery boundary

| Item | Current value |
| --- | --- |
| Repository | Public `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-approved-images` |
| Current review branch | `design/about-principles-horizons` |
| Branch point | `main` at `424fcdb79a3d3006aa255538fe075e83b00fffb2` |
| Latest observed `main` | `9755a438edcfe100153cf253601ece3a8de4eaf8` — newer workflow deletion outside this batch |
| Previous PR | [PR #6](https://github.com/derndy/XuGroupWeb-v2/pull/6), now merged; PRs #1–5 are also merged |
| Current PR | [Draft PR #7](https://github.com/derndy/XuGroupWeb-v2/pull/7), open and draft |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Current release instruction | Review branch and draft PR only; no merge or production switch |

GitHub confirms PRs #1–6 merged before this continuation. This batch starts from `424fcdb…` main, whose source tree matches the preceding About-learning checkpoint. No open PR was returned at the initial check. Preserve newer work if the branch moves again; do not recreate deleted historical branches or repeat completed image/homepage integration.

Earlier on 5 September, `https://xushidang-lab.netlify.app/` returned older carousel HTML without the approved homepage H1. That was a historical HTML observation, not a statement about current production after subsequent user merges. Production has not been rechecked in this batch. The PR #6 Netlify preview succeeded, but production branch settings and deployment history have not been inspected. Do not infer current production state from a GitHub merge or configured baseURL alone.

At the start of this continuation, v2 `main` was `424fcdb79a3d3006aa255538fe075e83b00fffb2`. This batch publishes a review branch only; it does not merge either main branch or change hosting configuration. The original repository is untouched.

During final delivery verification, remote `main` advanced to `9755a438edcfe100153cf253601ece3a8de4eaf8` (`Delete .github/workflows/publish.yaml`). A fetch confirmed that its only change from this branch's starting point is that workflow deletion. This separate commit was not made by the About batch. PR #7 remained open and draft at the subsequent GitHub check; the review branch still starts at `424fcdb…`. Preserve the newer main-branch work and recheck the current base before the next continuation. Production effects of that separate workflow change have not been inspected.

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

## Latest batch — About research principles and directions

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
2. Review About and the preceding Contact/homepage work at 320 px, tablet, desktop and 200% text/zoom in the hosted preview. Verify image clarity, keyboard focus, reading order and interactions; this source batch does not complete browser QA.
3. Homepage H05/H08–H10, Contact's four pathways and About's learning chapter are merged. About's principles and stage sequence are implemented in this review branch. Do not repeat completed source work.
4. Next bounded batch: About's explanation of why molecular/material testbeds matter, using existing public research questions and actual page destinations.
5. Then complete appropriate public research-culture content and improve shell navigation with real destinations. Do not publish an unfinished lab operating handbook or private management rules from another conversation.
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

## GitHub delivery — About principles and directions

Published to `design/about-principles-horizons` in commit `e41f614cf84f7a3b76e375f78edb075c09b91a7e`. Its tree `93c29084a2431a176e4d3e818d41d800561e78ea` exactly matches the tested local source. The original local commit is retained under `checkpoint/about-principles-local-source`; the checkout is aligned with GitHub. This subsequent project-state update changes documentation only.

[Draft PR #7](https://github.com/derndy/XuGroupWeb-v2/pull/7) targets `main`. GitHub reports `netlify/xushidang-lab/deploy-preview` **success** for the product commit, with [the matching About preview](https://deploy-preview-7--xushidang-lab.netlify.app/about/). Real browser layout, keyboard/touch, zoom and image loading remain unreviewed. Documentation commits can trigger a further preview build; check the actual final PR head before release.

This delivery did not merge the PR, modify either main branch or change production/hosting settings. Next bounded source batch: why molecular/material testbeds matter, using existing public research questions and actual destinations.

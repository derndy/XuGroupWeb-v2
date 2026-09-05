# Xu Lab website — current project state

Updated: 5 September 2026. Read this file first when continuing development. `PROJECT_STATE.md` is a compatibility pointer to this canonical lowercase file.

## Current source and delivery boundary

| Item | Current value |
| --- | --- |
| Repository | Public `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-approved-images` |
| Current review branch | `design/homepage-research-grammar` |
| Base | `main` at `6f19566096c95560cd58b1a11fbcea4f259d04e7` |
| Previous PR | [PR #1](https://github.com/derndy/XuGroupWeb-v2/pull/1), merged on 5 September 2026 at 09:36:40 UTC |
| Current PR | [PR #2](https://github.com/derndy/XuGroupWeb-v2/pull/2), open and draft |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Current release instruction | Review branch and draft PR only; no merge or production switch |

The earlier status file described PR #1 as open and draft. GitHub now confirms it was merged; its former `design/approved-scientific-images` remote branch was deleted. This batch begins from that merge. Do not recreate the deleted branch or repeat the completed six-image integration.

The recorded production URL, `https://xushidang-lab.netlify.app/`, was read on 5 September: HTTP 200, older carousel HTML, three empty Hero headings, and no approved homepage H1. It is not serving the latest v2 homepage observed in source. This checks returned HTML only; Netlify linkage, branch settings and deployment history have not been inspected. Do not infer production state merely from a GitHub merge or the configured `baseURL`.

Before publishing this review branch, v2 `main` remained at `6f195660…`; original `derndy/XuGroupWeb/main` remained at `b39bb3113f9601433155075204c209672f1758fb`. Neither main branch nor hosting configuration is to be changed by this batch.

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

## Latest completed batch — homepage scientific explanation

- Replaced the static, absolutely positioned Hero diagram with six native `details`/`summary` concepts: Evidence, Space, Interaction, Learning, Mechanism and Design. Definitions and real research links are usable without JavaScript. Learner dimensions use neutral styling; outcomes are explicitly proposals/aims to test.
- Added H03: scientific questions, definitions, connected choices and an evidence-feedback explanation. Compact and expanded forms share `data/research_system.yml` and `layouts/partials/research/learning-grammar.html`.
- Preserved the already-present Beyond Prediction section and all three exact homepage statements.
- Changed the secondary Hero action to the existing Scientific testbeds section.
- Replaced duplicate homepage pillar content with canonical formal titles, core questions and routes. Each card has a direct Explore link. Existing public invitations and three concise capability terms remain.
- Reduced the Hero headline scale and removed fixed-height pillar cards; added responsive grammar layouts and visible focus styles. Browser confirmation remains pending.
- Saved the design plan, implementation comparison, asset-location record and updated README/state instructions.

The new grammar follows the meaning of the original Drive `space-interaction-learning-map.svg`, which was retrieved and read. It does not publish the original source sheet. The archive manifest lists 91 materials; the six existing repository images already match their approval hashes and were not regenerated or reimported.

## Existing work retained

| Surface | Existing implementation |
| --- | --- |
| Home | Exact identity copy, Beyond Prediction, three pillars, evidence loop, testbeds with image 05, closing invitation |
| Research and three pillars | Overview, interconnected research map, detailed scope/methods/testbeds/principles/horizons and images 01–03 |
| About | Introductory research identity, image 04 and onward links; fuller vision/culture chapters still pending |
| Contact / Join / Collaborate | Shared layout, central facts, mailto/tel links, appointment link, authentic library photograph and image 06; four audience pathways still pending |
| People | 16 current-member profiles, 7 undergraduate records, 9 alumni records and authentic photographs |
| Gallery | 19 documentary records, year grouping, server-rendered content and progressively enhanced dialog |
| News | 18 published records; incomplete record excluded as draft |
| Publications | 78 records, 13 years, seven types, filters/search, citations and previous verified identity corrections |

Approved image source paths, captions, hashes and destinations are in `data/research_assets.yml` and `docs/scientific-visual-approval-2026-09-05.md`. All six original PNGs and all 24 uncropped WebP derivatives are retained. The latest homepage still contains only image 05; image 06 stays on Contact.

## Validation of this batch

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
3. Improve H05's six-step evidence loop with an explicit return path; retain scientific feedback rather than inserting internal release procedures.
4. Add H08–H10 with actual public publications, a suitable authentic lab photo, and the latest real news. Do not invent eligible projects or resource releases to fill empty sections.
5. Complete About's middle Space–Interaction–Learning chapter/culture/horizons and Contact's four audience pathways. Expand shell navigation and supporting pages with real destinations.
6. Continue the publication identity/external-download review and approved project/resource connections in separate, evidence-backed batches.
7. Merge or change Netlify only after an explicit release instruction.

## Historical checkouts

The original `/workspace/sites/xugroup-web` and its PR #3 are historical work in `derndy/XuGroupWeb`; preserve them and their untracked candidate PNGs. `/workspace/sites/xugroup-web-v2` shares the Git database with this checkout. Old local `main` is not proof of remote `main`. The original prepared local source history remains under `checkpoint/local-source-20260905`.

## GitHub delivery of this batch

Published to `design/homepage-research-grammar` in commit `699c9ce6f6fe4641ffa7f2e02a0d5dc929a9a9fa`; its tree `743a2a3dd3d4d1b7af68148cac57ee12c72503cf` exactly matches the tested local source. This later state-record commit changes documentation only. The connected GitHub account created [Draft PR #2](https://github.com/derndy/XuGroupWeb-v2/pull/2) targeting `main`. No merge was performed.

GitHub reported zero commit statuses at the prepared head. No matching hosted Netlify preview has been confirmed. A draft PR is a source review link, not a running website preview. The former production URL still requires a separate deployment-state review before any release decision.

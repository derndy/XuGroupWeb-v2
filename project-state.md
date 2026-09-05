# Xu Lab website — current project state

Updated: 5 September 2026. Read this file first when continuing development. The canonical filename is `project-state.md`; `PROJECT_STATE.md` is a compatibility pointer for earlier prompts.

## Active project

| Item | Current value |
| --- | --- |
| Development repository | `derndy/XuGroupWeb-v2` |
| Working checkout | `/workspace/sites/xugroup-approved-images` |
| Working branch | `design/approved-scientific-images` |
| Base branch | Remote `main` |
| Remote base checkpoint at this review | `b39bb3113f9601433155075204c209672f1758fb` |
| Last product-change commit | `b9f9c75c4e11e25751f747068c8b5d3220541239` |
| Last product-change tree | `445a55a8b7b5e811a3f35741ed0290578c96be53` |
| Stack | Hugo Extended 0.139.4, Hugo Blox/Bootstrap, GitHub + Netlify |
| Release state | Draft review only; no merge or production switch |

The commit containing this state file is a later documentation checkpoint. Use `git rev-parse HEAD HEAD^{tree}` and the remote branch to identify its exact current commit and tree; do not expect this document to contain its own commit hash.

## Why the attached handoff differs

The attached `XuGroupWeb_Project_Handoff_2026-09-05.md` describes an earlier checkpoint in the original `derndy/XuGroupWeb` repository. Its original checkout, local image-01 commit and old Draft PR #3 are still present, but newer work exists in the separate v2 repository worktree.

The newer scientific approval record explicitly supersedes the one-image decision: the PI approved images 01–03 with “1-3 approve” and 04–06 with “4-6 approve”. The six-image integration and About page were already implemented before this continuation. See `docs/scientific-visual-approval-2026-09-05.md` for the exact original hashes, captions and approved placements.

The separate review destination is recorded in `docs/approved-images-integration-review.md`. Continue on the v2 review branch. Do not copy these changes back to the old repository or assume the old Netlify preview shows this branch.

| Other checkout or remote | State when inspected | Handling |
| --- | --- | --- |
| `/workspace/sites/xugroup-web` | Local `318ea506…`, tree `506ca0fd…`; image 01 only; two untracked candidate PNGs | Preserve; do not overwrite, add or delete its candidates |
| Original `XuGroupWeb` Draft PR #3 | Head `688544fc…`, tree `bed4e6e9…`; 11 earlier slices | Historical review; unchanged by this continuation |
| `/workspace/sites/xugroup-web-v2` | Local `main` at `318ea506…` | Shared Git database for this worktree; local `main` is not remote production state |
| Remote `XuGroupWeb-v2/main` | `b39bb311…` | Imported original base; not the redesigned website |

## Completed website surfaces

- Homepage: approved title, subtitle and tagline, research-system structure, testbeds and recruitment links.
- Research: integrated overview and three complete Pillar detail routes, preserving the research taxonomy and conceptual architecture maps.
- About / Vision: existing research identity and links to Research, People and Contact.
- People: 16 current-member profiles, 7 undergraduate records, 9 alumni records and existing photographs.
- Gallery: 19 server-rendered documentary photo records, year grouping and progressively enhanced photo dialog.
- News: 18 published records and six featured images; incomplete record explicitly excluded as a draft.
- Publications: 78 records, 13 years and seven display types, accessible search/filter controls, citation downloads, and the four previously verified identity corrections.
- Contact / Join / Collaborate: shared layout, central contact data, direct email and phone links, appointment link, uncropped original library photograph and approved closing image.

## Approved scientific images

| Image | Asset | Public placement |
| --- | --- | --- |
| 01 | `CONCEPT-RES-001` | `/research/` after the introduction |
| 02 | `CONCEPT-RES-002` | `/research/evidence-engineering/` opening section |
| 03 | `CONCEPT-RES-003` | `/research/mathematical-frontiers/` opening section |
| 04 | `CONCEPT-RES-004` | `/about/` vision section |
| 05 | `CONCEPT-RES-005` | `/` scientific-testbeds section |
| 06 | `CONCEPT-RES-006` | `/contact/` closing section |

All six original PNGs retain their approved bytes and dimensions. Each has four uncropped WebP variants, a visible conceptual/AI-generated label, its approved caption, descriptive alternative text and a direct original download. Pillar I keeps its precise semantic architecture map. Legacy scientific images remain blocked. Conceptual approval is not approval of experimental evidence or a production release.

## Work completed in this continuation

1. Reconciled the earlier handoff with all three local checkouts, both GitHub repositories, the old PR and the six-image approval record.
2. Rebuilt the six-image checkpoint before editing.
3. Refined Contact in commit `b9f9c75…`: removed its legacy inline stylesheet, used the shared layout and design tokens, made email/phone clickable, retained the appointment destination, supplied actual photo dimensions, and added a page-specific search description.
4. Moved existing Contact facts and copy into `data/contact_page.yml`; documented safe editing in `docs/contact-maintenance.md`.
5. Added this repository-controlled continuation record.

No person, publication, News, Gallery or research fact was changed in the Contact slice. No image bytes, approved captions, or placement approvals were changed. The other ten redesigned main-content HTML trees match the pre-Contact baseline, including attributes and text.

## Validation

Completed locally on 5 September 2026:

- Production build: 736 pages; passed.
- Netlify-equivalent preview build with `--buildFuture` and preview environment: 736 pages; passed. The preview base URL was `https://example.invalid/` solely for offline validation; it is not a hosted website.
- Scientific visual audit: six approved placements, six exact originals, 24 uncropped WebP variants; passed on both builds.
- Publication audit and baseline comparison: 78 records, 13 years, seven types; titles, authors, ordering, routes, attachments and citation bytes preserved.
- Publication JavaScript tests: 9/9 passed; DOI regression tests: 3/3 passed.
- Eleven main surfaces: one H1 and one main landmark each; unique authored IDs; 1,002 internal links and page fragments resolve.
- Contact facts, matching `mailto:`/`tel:` destinations, appointment URL, metadata and original photograph verified against the previous page.
- All eleven preview surfaces emit `noindex`; corresponding production-build pages do not inherit it.
- `git diff --check`: passed.

Not completed: real browser layout/keyboard review, live email/phone client interaction, full external archive/download checks, appointment availability, or production release. File-level validation does not imply browser or live-service success.

Temporary build outputs for this continuation are under `/workspace/scratch/7457cd2d5ea9/`: `build-production` is the pre-Contact baseline, `build-contact` is the final production-equivalent output, and `build-preview` is the final preview-equivalent output. These can be regenerated and are not source files.

## Reproduce checks

Run from the active checkout. Use an absolute output directory outside the source tree.

```bash
export PATH=/workspace/tools/go-1.23.4/go/bin:$PATH
HUGO_ENV=production /workspace/tools/hugo-0.139.4/hugo --gc --minify -b https://xushidang-lab.netlify.app/ -d /absolute/production-build
python -B scripts/audit-research-visuals.py /absolute/production-build
python -B scripts/audit-publications.py /absolute/production-build
node --test tests/publications.test.mjs
python -B -m unittest tests/test_publication_links.py
git diff --check
HUGO_ENV=production HUGO_DEPLOY_CONTEXT=preview /workspace/tools/hugo-0.139.4/hugo --gc --minify --buildFuture -b https://example.invalid/ -d /absolute/preview-build
python -B scripts/audit-research-visuals.py /absolute/preview-build
```

## Next development step

1. Read `git status`, branch/upstream, local commit/tree, remote review head, PR state and hosted checks before editing. Preserve any new user work. Stop to compare if either branch moved unexpectedly.
2. Complete desktop/mobile and keyboard review of the eleven redesigned surfaces when browser QA is requested. Focus on all six uncropped illustrations, narrow-screen Contact layout, navigation, Gallery dialog, and publication filters.
3. Resolve concrete presentation issues in small reviewable commits. Keep factual publication-identity review in its own evidence-backed change.
4. Continue the archive-wide publication identity, bibliography and external-download review.
5. Release only after an explicit PI decision. A draft PR or image approval does not authorize merging `main` or switching Netlify.

## Delivery status

The earlier push was rejected by automatic approval review because the request at that time did not explicitly authorize the public destination. No alternate write route was attempted after that rejection.

The PI has now explicitly instructed: first ensure the state file is saved in GitHub as `project-state.md`, then “publish the prepared branch to public and open a draft PR, keeping the production website unchanged.” This replies directly to the destination-specific request for public `derndy/XuGroupWeb-v2`, branch `design/approved-scientific-images`, and a draft PR targeting `main`. That publication is authorized. A merge or Netlify production switch remains excluded.

Before this authorized push, GitHub was rechecked: the v2 repository is public, `main` still points to `b39bb311…`, the prepared branch is absent, the default branch contains no project-state file, and the repository has no pull requests. The original `XuGroupWeb/main` also remains at `b39bb311…`.

Publication is in progress. Confirm the remote branch and exact state-file bytes, open one draft PR and inspect its actual checks. Record the confirmed PR URL and hosted-check outcome here before the next handoff. The old PR #3 preview is not evidence for this newer work.

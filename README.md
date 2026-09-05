# Xu Lab website

The public website for **Xu Lab — Scientific Learning & Discovery Systems** at South China University of Technology.

## Technology

- Hugo Extended `0.139.4`
- Hugo Blox / Bootstrap module stack
- GitHub source control
- Netlify production and Deploy Preview builds

The Netlify build is defined in `netlify.toml`:

```bash
hugo --gc --minify -b $URL
```

The generated site is written to `public/`.

## Repository map

```text
assets/scss/template.scss     Shared design tokens and site styling
audit/                        Non-published legacy assets and review material
config/_default/              Site, menu, module, and metadata settings
content/_index.md             Homepage metadata
content/about/index.md        About-specific text and chapter settings
content/research/             Research content
content/person/               Member profiles
content/publication/          Publication records
content/post/                 Canonical News records and bundled images
data/research_system.yml      Three-Pillar research content model
data/research_assets.yml      Scientific-visual inventory and release state
data/people_page.yml          People-page copy, group-photo records, and routes
data/homepage.yml             Reviewed homepage publication references
data/contact_page.yml         Contact facts and four audience pathways
layouts/                      Custom page templates and reusable partials
static/images/                Public photographs and fixed web assets
static/data/gallery-data.json Canonical Gallery records and page copy
```

## Local validation

Install Hugo Extended `0.139.4` and Go, then run:

```bash
hugo server --buildFuture
```

Before opening a pull request, run the production-equivalent build:

```bash
HUGO_ENV=production hugo --gc --minify -b https://xushidang-lab.netlify.app/
```

## Change workflow

1. Create a branch from `main`.
2. Edit content or templates in the appropriate source directory.
3. Run the production build and inspect the generated pages.
4. Publish the review branch, open a draft PR, and inspect a matching Deploy Preview when available.
5. Confirm scientific wording, image rights, responsive behaviour, links, and metadata.
6. Merge or change hosting only with an explicit release instruction. Confirm the actual Netlify repository/branch linkage before making a production decision.

Project-specific scientific claims must remain off the public site until their scientific status, evidence status, publication state, and approval are recorded.

## Current redesign

Start with [`project-state.md`](project-state.md) for the active branch, reconciled handoff, latest validation and delivery status.

The [website design and asset-placement brief](docs/website-design-and-asset-placement.md) records the intended design. The [implementation comparison](docs/design-implementation-review-2026-09-05.md) identifies what exists, what this batch changes, and what remains.

This separate redesign repository is `derndy/XuGroupWeb-v2`. The original `derndy/XuGroupWeb` remains the fallback. PR #1 merged the approved-image redesign into v2 `main`. PR #2 merged the homepage grammar, PR #3 the evidence loop, PR #4 the homepage publications/people/news, PR #5 the four Contact pathways, and PR #6 About’s scientific-learning chapter. The current review batch is `design/about-principles-horizons`; its status is recorded in `project-state.md`. The redesign establishes the visual system, accessible global shell, semantic homepage, integrated Research landing page, governed three-Pillar data model, the complete reusable Pillar detail-page set, scientific-visual release gates, evidence loop, research horizons, testbed framing, recruitment pathway, a genuine 404 recovery page, a semantic People directory, a server-rendered documentary Gallery with accessible progressive enhancement, and a source-backed News ledger. Existing member records, portraits, Gallery photographs, News titles, dates, summaries, featured images, and public URLs are preserved. Publication improvements from the source redesign are retained. Six PI-approved conceptual illustrations now have exact source records, captions, and permitted placements.

See [`docs/redesign-foundation.md`](docs/redesign-foundation.md) for the baseline audit and implementation boundaries.
See [`docs/people-directory-maintenance.md`](docs/people-directory-maintenance.md) before changing member records, portraits, group photographs, or People-page copy.
See [`docs/gallery-maintenance.md`](docs/gallery-maintenance.md) before changing Gallery records, captions, thumbnails, categories, or public image files.
See [`docs/news-maintenance.md`](docs/news-maintenance.md) before adding or changing News records, dates, summaries, images, drafts, or public routes.

See [`docs/scientific-visual-approval-2026-09-05.md`](docs/scientific-visual-approval-2026-09-05.md) for all six approved originals and their placements.

See [`docs/homepage-records-maintenance.md`](docs/homepage-records-maintenance.md) before changing homepage paper selections, citation actions, the documentary photograph or news eligibility.

See [`docs/contact-maintenance.md`](docs/contact-maintenance.md) before changing contact facts, the four audience pathways or suggested email subjects.

See [`docs/about-maintenance.md`](docs/about-maintenance.md) before changing About copy, shared scientific definitions or the image 04 chapter.

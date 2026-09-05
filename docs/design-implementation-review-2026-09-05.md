# Design implementation review — 5 September 2026

Read with [the design brief](website-design-and-asset-placement.md) and [current project state](../project-state.md). The brief defines the intended experience; this review records what the source actually implements.

## Baseline and scope

- Repository: public `derndy/XuGroupWeb-v2`.
- Baseline: `main` at `6f19566096c95560cd58b1a11fbcea4f259d04e7`, the merge of PR #1. Its website tree matches the previous prepared checkpoint.
- Current batch: `design/homepage-research-grammar`, based on that merge, for draft review only.
- On this date the recorded production URL, `https://xushidang-lab.netlify.app/`, returned HTTP 200 with the older carousel markup, three empty Hero headings, and no approved homepage title. This is an HTML observation, not a browser screenshot or proof of its Netlify repository settings.
- The new homepage work is evaluated against the latest v2 source, not that older hosted page. Neither `main` nor hosting configuration is changed by this batch.

## Comparison with the design brief

| Area | Before this batch | This batch / remaining work |
| --- | --- | --- |
| H01 identity and Hero | Exact H1, subtitle and tagline present; static diagram hidden from assistive technology behind a single image description; dimensions reused pillar colours | Preserved exact copy; six native disclosure controls provide definitions and research links; neutral learner grouping distinguishes dimensions from pillars; explicit evidence feedback and proposed outcomes; shorter headline scale and a truthful Scientific testbeds CTA |
| H02 Beyond Prediction | Already present with the main explanatory proposition | Preserved. Do not rebuild it as a missing section |
| H03 Space–Interaction–Learning | No separate explanation | Added scientific questions, definitions, connected choices and evidence feedback; both Hero and expanded explanation use `research_system.grammar` |
| H04 three contributions | Hard-coded duplicates of pillar records; no individual links or displayed core questions; Pillar II formal title shortened | Uses canonical formal titles, questions, colours and routes; retains concise public invitations and three capability labels; each card links directly to its pillar |
| H05 evidence loop | Five static steps on navy; no explicit diagram return path; test and design combined | Still needs the six-step structure, visible return path, pale-teal treatment and deeper explanations from the brief |
| H06 selected projects | Omitted; existing pillar project arrays are empty | Keep omitted until approved public project records exist; private archive project material is not automatically eligible |
| H07 scientific testbeds | Image 05 appears once, uncropped with caption, in the light testbeds section; four cards | Preserved. Cards still need useful evidence-backed deeper links |
| H08 publications/resources | No homepage featured-output section; complete publication index exists | Add a small verified selection. Add resource actions only where a real, approved resource exists |
| H09 people/culture | No homepage photograph/culture section; People and Gallery retain authentic records | Select a suitable existing public photo with date/event context, then add the homepage section |
| H10 latest news | No homepage news section; 18 published records are available on News | Add up to three actual records in reverse date order; no invented recent activity |
| H11 closing invitation | Navy invitation with Contact and People links; no second conceptual image | Preserve the single-artwork rule; four audience routes can follow the dedicated Contact improvement |
| Research / pillars | Three distinct pillars, overview map, conceptual figures, scope/methods/testbeds/horizons and review principles exist | Expand responsive named relationships and reuse the grammar on Pillar I when improving that page; do not change the current route to match an aspirational URL |
| Six approved artwork placements | All six exact source files integrated with approved captions, originals and 24 WebP derivatives | No artwork or approval change in this batch; all six pass the existing source/placement audit |
| About / Vision | Brief introduction, image 04 and navigation onward | Still needs the fuller Space–Interaction–Learning chapter, principles, culture and NOW/NEXT/HORIZON sequence |
| Join / Collaborate | `/contact/` has verified contact fields, library photograph, invitation and image 06 | Still needs four audience-specific pathways and current, verified opportunity information. Keep `/contact/` working |
| People, Gallery, News, Publications | Redesigned independent pages, authentic records and existing functionality | Preserved. Whole-site browser/keyboard checks and external publication/download verification remain pending |
| Header / footer / languages | Navigation uses current pages; About is linked from content but absent from main menu; grouped menus and supporting policies incomplete | Improve site shell after usable destination pages exist; remove glass styling; never expose missing-language links or invent privacy statements |
| Projects / Resources | Full public record collections not implemented | Requires public records, useful actions and explicit source support before adding cards, filters or menu destinations |

## Drive materials and their roles

The supplied folder was read and its archive manifest inspected. It contains 91 listed items: 12 core design/copy files, 24 PNG assets, 29 SVG/HTML/toolkit files, 16 content/model/deployment files, and 10 internal scientific/release files. These archive categories describe references, not permission to publish their contents.

- Core design packs 01–06 are present by exact filename in the archive manifest. The current brief controls copy/taxonomy conflicts with those earlier packs.
- The original `space-interaction-learning-map.svg` was retrieved from Drive and its full SVG text, title and description read. It defines co-design, state/scale, interaction/path/operator, guiding signals/update laws, divide/recompose, reusable dictionaries, and evidence feedback.
- This batch adapts its co-design and feedback meanings to live HTML. It does not embed the fixed-size source sheet or its developer annotations. Dictionary/grammar synthesis remains a long-term programme on the pillar pages, not an achieved result.
- Wireframes and design-system files remain implementation references. Templates, private project packages, governance diagrams and blank scientific figures are not copied into the public source or rendered pages.
- The six archive PNGs have the same titles/source identities as the brief's approved originals. Their archive copies were located by metadata; those duplicate bytes were not downloaded. Existing repository originals were checked against the approval hashes instead.

### Approved originals retained in this checkout

| No. | Repository original | Page / placement |
| --- | --- | --- |
| 01 | `assets/media/research/three-pillars-discovery-core.png` | `/research/` — below introduction |
| 02 | `assets/media/research/evidence-spiral.png` | `/research/evidence-engineering/` — opening explanation |
| 03 | `assets/media/research/mathematics-frontiers.png` | `/research/mathematical-frontiers/` — below opening statement |
| 04 | `assets/media/research/mobius-cycle.png` | `/about/` — vision illustration; fuller surrounding chapter pending |
| 05 | `assets/media/research/testbeds-horizons.png` | `/` — scientific testbeds |
| 06 | `assets/media/research/signals-discovery.png` | `/contact/` — closing invitation |

Use `data/research_assets.yml` for exact hashes, original Drive links, dimensions, captions and permissions. Archive candidates outside this register remain unused.

## Maintenance of this homepage batch

- `data/research_system.yml`: shared grammar definitions, questions, relationships and destinations; existing canonical pillar records plus short homepage invitations/terms.
- `layouts/partials/research/learning-grammar.html`: compact Hero and expanded explanation.
- `layouts/partials/research/learning-concept.html`: native `details`/`summary` controls. There is no JavaScript dependency or hover-only definition.
- `layouts/landing/home.html`: section order and canonical pillar iteration; approved title/subtitle/tagline remain exact.
- `assets/scss/template.scss`: scoped grammar layouts and responsive reflow; obsolete absolute-positioned Hero map rules removed.

Keep map labels neutral within the learner; pillar category colours belong to pillar cards. Mechanism and Design are proposals/aims to be tested, not automatic outputs of prediction. Do not replace the six approved source images or alter their captions while maintaining the explanatory map.

## Validation and next batch

Validation results for the final source are recorded in `project-state.md`. The internal browser preview could not start because this Hugo project has no compatible preview server/package entrypoint. No framework migration or preview-only dependency was added. Real browser layout, keyboard and touch verification are still pending; static HTML checks do not substitute for those checks.

Next bounded design batch: H05's explicit evidence return loop, then H08–H10 using existing public publication, photo and news records. After that, finish About and the four Contact pathways. Keep project/resource records dependent on approved public source material.

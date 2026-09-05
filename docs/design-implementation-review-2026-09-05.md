# Design implementation review — 5 September 2026

Read with [the design brief](website-design-and-asset-placement.md) and [current project state](../project-state.md). The brief defines the intended experience; this review records what the source actually implements.

## Baseline and scope

- Repository: public `derndy/XuGroupWeb-v2`.
- Baseline: `main` at `6f19566096c95560cd58b1a11fbcea4f259d04e7`, the merge of PR #1. Its website tree matches the previous prepared checkpoint.
- First batch: `design/homepage-research-grammar`, reviewed in PR #2 and since merged.
- Second batch: `design/homepage-evidence-loop`, merged as PR #3.
- Third batch: `design/homepage-publications-people-news`, merged as PR #4.
- Fourth batch: `design/contact-pathways`, merged as PR #5.
- Current batch: `design/about-learning-system`, based on v2 `main` at `98aeaba4b9bbf89a8e1e016f80886404cbcddad2`, for draft review only.
- On this date the recorded production URL, `https://xushidang-lab.netlify.app/`, returned HTTP 200 with the older carousel markup, three empty Hero headings, and no approved homepage title. This is an HTML observation, not a browser screenshot or proof of its Netlify repository settings.
- The new homepage work is evaluated against the latest v2 source, not that older hosted page. Neither `main` nor hosting configuration is changed by this batch.

## Comparison with the design brief

| Area | Before this batch | This batch / remaining work |
| --- | --- | --- |
| H01 identity and Hero | Exact H1, subtitle and tagline present; static diagram hidden from assistive technology behind a single image description; dimensions reused pillar colours | Preserved exact copy; six native disclosure controls provide definitions and research links; neutral learner grouping distinguishes dimensions from pillars; explicit evidence feedback and proposed outcomes; shorter headline scale and a truthful Scientific testbeds CTA |
| H02 Beyond Prediction | Already present with the main explanatory proposition | Preserved. Do not rebuild it as a missing section |
| H03 Space–Interaction–Learning | No separate explanation | Added scientific questions, definitions, connected choices and evidence feedback; both Hero and expanded explanation use `research_system.grammar` |
| H04 three contributions | Hard-coded duplicates of pillar records; no individual links or displayed core questions; Pillar II formal title shortened | Uses canonical formal titles, questions, colours and routes; retains concise public invitations and three capability labels; each card links directly to its pillar |
| H05 evidence loop | Five static steps on navy; no explicit diagram return path; test and design combined | Completed in the evidence-loop batch: six steps, pale-teal chapter, solid forward arrows and dashed feedback path, vertical mobile layout, native disclosures with questions/outputs/canonical pillar links. Browser review remains pending |
| H06 selected projects | Omitted; existing pillar project arrays are empty | Keep omitted until approved public project records exist; private archive project material is not automatically eligible |
| H07 scientific testbeds | Image 05 appears once, uncropped with caption, in the light testbeds section; four cards | Preserved. Cards still need useful evidence-backed deeper links |
| H08 publications/resources | No homepage featured-output section; complete publication index exists | Implemented: two selected existing papers, DOI records and real BibTeX downloads. Dataset/code/protocol/benchmark releases remain dependent on approved public records |
| H09 people/culture | No homepage photograph/culture section; People and Gallery retain authentic records | Implemented: existing 2025 welcome-dinner photo/alt/caption, short programme introduction, People/Gallery links; natural aspect ratio and lazy loading |
| H10 latest news | No homepage news section; 18 published records are available on News | Implemented: latest three eligible records, original dates/titles/routes, broad category fallback; draft/future gates apply even to permissive previews |
| H11 closing invitation | Navy invitation with Contact and People links; no second conceptual image | Preserve the single-artwork rule; four audience routes can follow the dedicated Contact improvement |
| Research / pillars | Three distinct pillars, overview map, conceptual figures, scope/methods/testbeds/horizons and review principles exist | Expand responsive named relationships and reuse the grammar on Pillar I when improving that page; do not change the current route to match an aspirational URL |
| Six approved artwork placements | All six exact source files integrated with approved captions, originals and 24 WebP derivatives | No artwork or approval change in this batch; all six pass the existing source/placement audit |
| About / Vision | Brief introduction, image 04 and navigation onward | Space–Interaction–Learning chapter implemented with canonical definitions, mutual-shaping metaphor, full-width image 04, evidence feedback and a qualified long-term programme. Fuller principles/culture/NOW–NEXT–HORIZON sequence remain |
| Join / Collaborate | `/contact/` has verified contact fields, library photograph, invitation and image 06 | Four audience pathways implemented with preparation guidance, conditional next steps, suggested subject email links and real related routes. Confirmed vacancies remain source-dependent; the page asks visitors to enquire about current availability |
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
| 04 | `assets/media/research/mobius-cycle.png` | `/about/` — Space–Interaction–Learning middle chapter, after the live-text explanation |
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

H08–H10 and the four Contact pathways are merged; About's Space–Interaction–Learning chapter is implemented in the current batch. Next bounded batch: its research principles and NOW/NEXT/HORIZON sequence, reusing existing public pillar material. Keep project/resource records dependent on approved public source material.


## Second batch — explicit evidence feedback

The evidence-loop batch implements H05 only. The steps are Observe, Question, Design evidence, Learn, Test, and Explain or design. Each native disclosure includes a short explanation, example question, typical research output and relevant pillar links. No result, downloadable resource or completed autonomous discovery system is implied.

`data/research_system.yml` contains the step content. `layouts/partials/research/evidence-loop.html` renders it and resolves contributing pillars from existing canonical IDs; a missing pillar ID fails the build. The component has a caller-supplied ID prefix so future reuse on another page can retain unique anchors. This batch uses it only on Home.

The pale-teal section uses solid forward arrows and a dashed return path. On narrow screens, the steps become one vertical sequence and the feedback path runs beside it. The visible return link targets Observe. Native details work without added JavaScript; new styles add no animation. Real browser confirmation of layout, keyboard and touch behaviour is still pending.

Source scope: the homepage evidence section, its reusable partial, shared research data, scoped styles and these maintenance notes. Every other homepage section and the other ten main-page content trees are checked against the previous build. Approved artwork, publication/member/news/gallery records and hosting files are preserved.


## Third batch — published work and lab records

H08 presents two selected canonical research papers with full title/author/venue/year information, publisher DOI links and their real citation files. The citations column is conditional on existing files. This does not create a resource catalogue or imply available code, datasets or protocols. Selection evidence and source contracts are in [homepage-records-maintenance.md](homepage-records-maintenance.md).

H09 reuses the existing People photo record at full aspect ratio, including its 2025 event caption and alt. The original 1200 × 900 PNG is unchanged and loads lazily below the research sections. A short programme introduction and real People/Gallery routes connect the research to the team.

H10 uses the latest three published News bundles. Dates are visible and unchanged; the latest is 22 November 2025. Drafts and future event/publication dates are excluded even when previews enable them. No extra news facts, summary copies, photo payloads, scripts or dependencies are introduced.

The new sections follow testbeds and precede the closing invitation, now numbered 09. Validation passes both builds, the six-image audit, preservation of all 78 publications/citation files, 1,053 internal links/anchors, unchanged ten other main-content trees and previous homepage sections except numbering. Temporary permissive-preview fixtures confirm that draft and future news stay off the homepage. Browser layout, keyboard/touch, zoom and image-loading checks remain pending.


## Fourth batch — four ways to contact the lab

The existing `/contact/` page now has stable sections for scientific collaboration, experimental partnership, joining the lab and research-asset use. Each includes the suitable question, a visitor contribution, preparation guidance, a possible next step and an email action. Five introductory links reach the four sections and existing contact details. Related links lead to Research, Evidence Engineering, People and Publications.

All new text and suggested subjects live in `data/contact_page.yml`. Email actions use the existing contact address and correctly encoded subject text; there is no form, message-sending action or new script. Suggested subjects are draft conventions, not a pre-existing mandatory application policy. Openings/funding are matters to enquire about, and resource access depends on specific public work and its terms.

Cards use two desktop columns and one column below 62rem, natural text height, wrapping buttons and visible focus. The old hero text, contact details, appointment link, photo and approved closing artwork are preserved, as are all ten other main-content trees. Both builds passed, with six approved image placements, all 78 publications/citation bytes and 1,062 internal links/anchors verified. Real browser, keyboard/touch, zoom and email-client checks remain pending. See [Contact maintenance](contact-maintenance.md) for source contracts.


## Fifth batch — About's connected learning system

The About middle chapter now explains Space, Interaction and Learning using the same canonical questions and definitions as Home. New surrounding copy describes their mutual influence within the learner and keeps these design choices distinct from the three research pillars. The existing introduction, hero and onward routes are preserved.

Image 04 stays at its approved placement and full content width, following the explanation. This uses the brief's full-width option to keep the detailed loop readable. The original image/caption/alt/attribution/download and derivatives are unchanged; a separate text paragraph identifies the loop as a metaphor. Evidence feedback and a Research horizon block follow, with Scientific Learning Grammar framed as a long-term aim/open question.

About-specific copy, including the former hard-coded hero and onward-link labels, now lives in `content/about/index.md`. Shared scientific definitions and approved captions retain their canonical data sources. Scoped styles reflow the text columns without reordering the explanation, image or caption.

Both builds passed; the six-image audit, all 78 publication/citation records and 1,065 internal links/anchors are verified. Existing About hero/routes/figure HTML and the other ten main-content trees match baseline. Real browser layout, keyboard/touch, zoom and image loading remain unreviewed. See [About maintenance](about-maintenance.md).

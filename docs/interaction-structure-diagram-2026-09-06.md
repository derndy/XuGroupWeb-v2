# Interaction-structure diagram — 6 September 2026

Base: main `2fccbc673fa984810caf6d7f8bbec99fbfda731d`, after PR #23 merged.

## Purpose and scientific meaning

Pillar I explains interaction structure but previously had no concrete worked example. The new figure compares two graphs with the same four scalar feature values and a different assignment of connections. Averaging the raw features gives 2.5 for both. Summing connected-pair products gives 14 for A and 11 for B.

This is an original illustrative calculation, not a paper figure, a proposed model, a measured result or a claim of a physical mechanism. Nodes are generic information units. Geometric positions and line lengths carry no scientific meaning. The example does not claim that this calculation distinguishes every graph or that pooling after interaction-aware processing necessarily loses information.

The purpose follows the existing Pillar I Representation space / Interaction structure scope and Interaction map output in `data/research_system.yml`. It preserves the research direction and existing text.

## Placement and maintenance

- Added after the existing Pillar I scope cards, at `/research/learning-system-design/#interaction-structure-title`.
- Wide SVG: 960 × 700. Mobile SVG: 440 × 1120, selected below the existing 47.99rem breakpoint. Both are below 6 KB and require no raster derivatives.
- Accessible description, caption, expandable HTML calculation, and full-size links accompany the figure. Graph labels and numbers provide meaning independently of color. All diagram text is also described in HTML for reading and text enlargement.
- New prose is in `data/website_text.yml` → `research_figures.interaction_structure`, preserving the site's central editing approach. Existing text keys are unchanged.
- `scripts/render-interaction-structure.py` regenerates both SVGs using the Python standard library. Pair products are calculated from the defined pairs, not manually entered as scores. If values or pairings change, update the accompanying HTML calculation and description as well.

## Whole-site review

The output review covers 536 index pages and eleven main routes. All 428 local image / picture source / srcset references resolve. There are 253 image elements, including the intentionally unpopulated Gallery viewer image. No external image URL is used in this scan.

| Main route | Image elements in main content | Review finding |
| --- | ---: | --- |
| Home | 5 | Three selected papers have authentic figures. PyraE2E and the selected JACS paper still need source-backed visuals. |
| About | 1 | Existing conceptual figure and caption preserved. |
| Research | 1 | Overview image and HTML system maps preserved. |
| Pillar I | 3 | Added the worked interaction example; retained the illustration and framework. |
| Pillar II | 3 | Existing evidence-choice example and wide/mobile framework preserved. |
| Pillar III | 2 | Existing illustration and framework preserved. |
| Publications | 0 | Index remains a bibliography; three selected-paper detail figures are retained. |
| People | 21 | Existing photos, descriptions and responsive variants retained. |
| News, first listing | 10 | Existing article images and descriptions retained. |
| Gallery | 24 | Twenty-three photos plus the intentionally empty viewer slot. |
| Join / Collaborate | 2 | Existing documentary and conceptual imagery retained. |

Every populated main-page image has alternative text. Across all 536 pages there are 81 empty alternative-text attributes, including the Gallery viewer slot and existing legacy detail-page imagery. These are a contextual review queue, not 81 confirmed defects; do not invent people, events, or scientific interpretations to fill them.

## Validation and limits

- Production and preview-equivalent builds each pass with 895 pages.
- Existing main-element text on all eleven main pages matches the preceding build after excluding the added figure. IDs are unique on these pages; diagram source and full-size links resolve.
- The 91-publication baseline audit preserves titles, author roles/links, ordering, routes, attachments and citation bytes. The seven-conceptual-image / 28-WebP audit and existing framework content checks pass.
- Both new SVGs were rendered and visually inspected, including a 360-pixel-wide mobile rendering. Graph pairings, arithmetic, labels and whitespace are correct. Regeneration reproduces the checked SVG bytes.
- Browser page testing could not start: the available supervised preview requires a compatible Node development project, while this repository uses Hugo without package.json. No package, server or hosting changes were added for this check. Browser layout, keyboard behavior, and 200% text enlargement remain untested.

Delivery is a separate draft PR. No merge into main or production-setting change is performed. Next priorities: authentic figures for the remaining two selected papers; contextual alternative-text review of older detail pages; full browser layout testing when a compatible preview is available.

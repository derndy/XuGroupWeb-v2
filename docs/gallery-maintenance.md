# Gallery maintenance

The Gallery is a documentary record of lab life. It contains group activities, shared meals, sport, welcomes, and milestones. It is not the release surface for scientific figures, unpublished results, project evidence, or generic decorative photography.

## Source map

| Source | Purpose |
| --- | --- |
| `static/data/gallery-data.json` | Canonical page copy, year groups, categories, captions, alt text, dimensions, and image records |
| `layouts/landing/gallery.html` | Server-rendered page structure and accessible photograph viewer |
| `static/js/gallery.js` | Progressive enhancement for the native dialog viewer |
| `assets/scss/template.scss` | Gallery layout and visual treatment |
| `static/images/gallery/` | Full-size public photographs |
| `static/images/gallery/thumbnails/` | Web thumbnails shown in the grid |

The page is rendered from `gallery-data.json` during the Hugo build. Every photograph must remain available as a normal link to its original file. The page must still expose all records when JavaScript is unavailable.

## Record contract

Each `images` record requires:

- a stable `id` in the form `GAL-YYYY-NNN`;
- the existing `fileName` and a matching `thumbnailName`;
- `year`, controlled `category`, and human-readable `categoryLabel`;
- concise English `title` and meaning-equivalent Chinese `titleZh`;
- a factual `caption` that states the event and year without unsupported claims;
- purpose-specific `alt` text that describes the visible scene and does not merely repeat the caption;
- verified original and thumbnail dimensions; and
- a `ratio` of `3-2` or `4-3` matching the source image.

The controlled categories are declared in the same JSON file. Add a new category there before using it in a record. Keep year groups in descending order and keep photographs in a stable editorial order within each year.

## Add a photograph

1. Confirm that the photograph belongs in the lab-life collection. Route scientific media through the scientific-visual approval process instead.
2. Record the media owner and obtain the required consent or licence for public use.
3. Remove unnecessary camera, location, and personal metadata before committing a new public asset.
4. Give the original a stable filename. Do not rename an existing public file because its URL may already be referenced.
5. Create a thumbnail that preserves the source aspect ratio. Use a width of 600 pixels and avoid upscaling.
6. Add the original under `static/images/gallery/` and its thumbnail under `static/images/gallery/thumbnails/`.
7. Measure both files and add one complete record to `static/data/gallery-data.json`.
8. Write English and Chinese titles that refer to the same event. Keep the English caption public-facing and factual.
9. Write alt text from the visible content. Do not identify people unless identification is necessary, approved, and reliably maintained.
10. Run the release checks below and review the Netlify Deploy Preview before merging.

## Release controls

Before a Gallery change is approved, verify:

- every record has a unique asset ID;
- every original and thumbnail exists at the declared path;
- recorded dimensions match the actual files;
- each record uses a declared year and category;
- captions, dates, English/Chinese titles, consent, rights, and owner review are current;
- the Gallery has one main landmark and one H1;
- all photograph cards are present in the generated HTML before JavaScript runs;
- there are no inline event handlers, inline styles, blank image links, or runtime-generated content dependencies;
- `node --check static/js/gallery.js` passes;
- the production-equivalent Hugo build passes; and
- keyboard navigation, focus restoration, the original-image fallback, and responsive layout pass in the Deploy Preview.

## Existing collection status

The 19 photographs present when this page was refactored are retained as a legacy-public collection with their public filenames and URLs unchanged. A future binary-maintenance pass may review embedded metadata and media compression. That pass must preserve URL stability or include an explicit redirect and reference audit; it is intentionally separate from page-layout changes.

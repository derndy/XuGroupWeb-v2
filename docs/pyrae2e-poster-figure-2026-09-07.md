# PyraE2E poster overview

7 September 2026. Base main: `234659a1d82d0684bf1194cd441a8de0429d7785`, after merged PR #34. Review branch: `content/selected-paper-visual-followup`.

## Purpose and placement

PyraE2E was the only homepage selected paper without a figure. The new image shows the authors' method overview on the homepage and the existing PyraE2E detail page. It is a method diagram, not a generated concept or a new claim of experimental performance. The five selected records keep their order. The canonical paper Markdown and citation remain unchanged, including the accepted status and year-only sorting date.

The excerpt retains the complete dashed outer frame of panel (a), including its embedded exploration panel (b). Lower detail panels (c–d), surrounding poster text and results are outside this crop. The caption identifies the excerpt; the full conference poster is linked. A wide homepage placement and uncropped responsive variants preserve its geometry.

## Primary source and verification

- Conference page: <https://eccv.ecva.net/virtual/2026/poster/3340>
- Original PNG: <https://eccv.ecva.net/media/PosterPDFs/ECCV%202026/3340.png?t=1788280593.0451055>
- Accepted-paper listing: <https://eccv.ecva.net/Conferences/2026/AcceptedPapers>
- Original: 4031 × 2880 pixels, 5,474,065 bytes.
- Original SHA-256: `69fb5965db9052436c2339a74e094284656071f15ef2b31594d500ab9839749f`.

The conference page's structured title and nine ordered authors were compared with the site's canonical record; they agree after case normalization. The poster's title and authors were also inspected visually. Page/poster timestamps are not treated as paper publication or acceptance dates. No DOI or proceedings details are inferred.

## Reuse basis and review

Responsible owner: Shidang Xu, coauthor and owner of this lab website. His current instruction authorizes continuing to add and improve website imagery. This draft prepares an excerpt from the authors' own conference poster for that author-lab website. It does not claim separate approval of these exact pixels or broader rights for third parties. The user retains the merge decision.

No explicit Creative Commons or other public reuse license was found for this poster. The record therefore uses `author_reuse`, not an invented public license or an unrelated publisher policy. The figure retains author credit, excerpt disclosure and a link to the full conference poster. Its scope is only this author-lab website; do not carry this reuse basis to an unrelated site or asset. The build requires a documented basis, a matching publication author, this scope and an existing review record. Licensed figures continue to require their existing license and license URL. The concept/result-figure governance paths are unchanged.

## Mechanical derivative

Repository asset: `assets/media/papers/pyrae2e-method-overview.png`.

- Crop on original pixels: left 2205, top 549, width 1776, height 625.
- Proportional resize to 1280 × 450; remove the verified fully opaque alpha channel; PNG compression level 9 without palette reduction.
- Web asset: 302,807 bytes; SHA-256 `1fac456701f837246623c241e82b851bbd907a95443a605f506c557538bbdbb8`.
- Sharp recipe: `.extract({left:2205,top:549,width:1776,height:625}).removeAlpha().resize({width:1280}).png({compressionLevel:9})`.
- Hugo derives 480-, 800-, 1200- and 1280-pixel WebP variants at quality 90. The clickable PNG retains the full web-excerpt dimensions.

No generative editing, redrawing, relabeling, recoloring or changes to arrows/data were used. Resampling changes pixels but retains the selected diagram's content and proportions. The original and final excerpt were visually inspected. A small preview cannot make all scientific labels legible; the image opens at its full excerpt size and the source link provides the complete poster.

## Validation

Production and deploy-preview-equivalent Hugo builds pass with 895 pages each. Both builds pass the publication and concept audits: 91 preserved publication records/citations, seven concepts and 24 uncropped concept WebP variants. All 466 local image/picture/srcset references resolve across 538 production HTML files. The baseline had 456 references; the ten additions are the new PNG plus four WebP references at each of two placements. The 74 empty-alt and one empty-source review entries are inherited from the baseline, not introduced here.

All 121 built main-content trees match the baseline after removing only the new PyraE2E figures and the homepage figure-layout wrapper. The four previous figure records, all concept records, homepage selections and canonical PyraE2E Markdown/BibTeX are preserved. The new figure appears exactly once at each intended placement, with a linked caption, nonempty alt text, full-size link, source credit and four uncropped WebP widths. All five homepage selected papers now have figures. No removed AI-generation/original-download labels appear in built visible text. Checked production pages remain indexable and preview equivalents carry `noindex`.

The original and final standalone images were visually inspected. Real browser layout and live-production state have not been verified. Delivery is a draft PR; check its final CI/deploy-preview status before merge.

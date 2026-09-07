# Two legacy paper figure displays

7 September 2026. Base main: `080a8d74143f01489067f083a1f0e416248aaa7b`, after merged PR #35. Review branch: `content/legacy-paper-image-descriptions`.

## Changes

Two 2024 publication figures had empty alternative text and no explanation beside the image. The Bi₂O₂Se characterization figure also compressed many panels into a 720-pixel column. Both original figures are informative and remain unchanged; they do not need generative replacement.

- **SQD-I / halogen bonds:** add a short description linking the shown molecular geometry, crystal transformation and charge redistribution, plus author credit and the source caption link. Keep the existing uncropped 720 × 831 WebP and link the full 997 × 1151 JPEG through the image itself.
- **Bi₂O₂Se / gas sensing:** explain that the image characterizes the film and adsorption sites. In particular, panels (e–f) concern oxygen adsorption, not a direct visualization of nitrogen-dioxide sensing. Increase the uncropped WebP display from 720 to 1200 pixels wide (1200 × 664; 106,114 bytes), and link the original 2001 × 1108 JPEG.

`featured_alt` provides a concise visual description; optional `featured_caption` provides the visible explanation and source link below the image. `image.link_to_original` opts these two images into a normal keyboard-accessible link with an explicit accessible name and focus outline. The existing `image.placement: 2` setting supplies the wider sensor-figure placement. There is no new download badge, overlay or JavaScript interaction. Existing news descriptions and other header images retain their previous behavior.

## Sources and retained assets

The two original repository images were visually inspected. Descriptions use their actual panels and the canonical paper abstracts; the gas-sensor panel assignments were also checked against the publisher's Figure 1 caption.

| Paper | Figure/source | Original SHA-256 |
| --- | --- | --- |
| Xiaoyu Ye et al., Advanced Science (2024), DOI 10.1002/advs.202400661 | Figure 1; [archived article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11220701/) | `49dce2f88bb3f9ff9b4da3819ec382afb0a5fd4330c31ba51eaf960635ff63e9` |
| Shipu Xu et al., Nature Communications (2024), DOI 10.1038/s41467-024-50443-5 | [Figure 1 and full caption](https://www.nature.com/articles/s41467-024-50443-5#Fig1) | `63b4698962c77b1e7c72103b8d56a20650ae29bed7054e0429592ca882148fab` |

Each JPEG remains in its existing publication bundle. No source pixels, panels, annotations, scale bars or rights statements are modified. No new public reuse license is asserted. Display resampling uses the established Hugo `Fit` and WebP pipeline, without cropping or generative editing.

## Validation and remaining review

Production and deploy-preview-equivalent Hugo builds pass with 895 pages each. Publication and concept audits preserve 91 records/citations, seven concepts and 24 concept WebP variants. All 466 local image/picture/srcset references resolve across 538 production HTML files. The empty-alt queue decreases from 74 to 72 entries.

All 121 main-content trees match the baseline after removing only the two intended captions and image-link wrappers and normalizing their intended image attributes. The original image/attachment bytes and all bibliographic fields are unchanged; the only new frontmatter fields are the two image descriptions and display settings. Homepage selections, selected-paper figures and concept records are unchanged. Each full-size link resolves to the unchanged local JPEG; both display aspect ratios are preserved. Scoped caption/focus styles compile, and production/preview indexing behavior is correct on the five checked pages. No removed AI-generation/original-download labels appear in visible built text. Both originals and the larger sensor WebP were visually inspected; browser layout, keyboard/touch interaction and live-production state were not tested.

The Gallery empty-source/empty-alt entry is the initially closed dialog's image placeholder. `static/js/gallery.js` assigns its source and alternative text when opening a photograph and removes its source when closing. It is not evidence of a missing gallery file and is left unchanged. The other 71 empty-alt entries belong to older publication figures and remain a contextual review queue, not an instruction to generate generic replacement images. A next small batch can inspect two or three of those figures. Delivery is a draft PR; check its final preview before merge.

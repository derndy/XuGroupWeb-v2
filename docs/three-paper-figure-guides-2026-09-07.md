# Three paper figure guides

7 September 2026. Base main: `ea774c3095c08419ac93066b19785b6db2cc3fe1`, after merged PR #36. Review branch: `content/three-paper-figure-guides`.

This round adds reading guidance to three existing scientific diagrams. All use the `featured_alt`, `featured_caption` and `image.link_to_original` options introduced in PR #36. The two complex landscape diagrams also use its existing wider image placement. Shared templates and styles are unchanged.

| Paper | Reading guidance and display | Primary source |
| --- | --- | --- |
| Jucai Gao et al., anthracene-bridged photosensitizers | Connect the donor–acceptor bridge, singlet oxygen and molecular breakdown. Preserve the compact 583 × 527 display. | [Chemistry of Materials](https://doi.org/10.1021/acs.chemmater.2c03274) |
| Lianfeng Fan et al., QTANHOH photo-immunotherapy | Explain nanoparticle assembly and the strategy combining reactive oxygen generation, HDAC inhibition and immune signaling. Increase display from 720 × 471 to 1000 × 654. | [Advanced Functional Materials](https://doi.org/10.1002/adfm.202313755) |
| Jingjing Liu et al., MPO-sensitive MR imaging | Locate the nanoprobe strategy in the liver inflammatory environment and identify MPO as the intended aggregation trigger. Increase display from 720 × 282 to 1000 × 391. | [ACS Nano](https://doi.org/10.1021/acsnano.2c06233) |

The visible explanations include author credit and DOI links. Alternative text describes what the pictures actually show. No unverified figure number, clinical efficacy or safety claim is added. The diagrams, canonical abstracts and indexed primary publisher records support the descriptions; direct publisher page retrieval returned HTTP 403, so full-text access is not claimed. The Fan paper's first-online date is 15 December 2023 and its issue citation is 2024; its existing publication date is preserved and the new image credit does not introduce a competing year.

## Retained images

Each original `featured.jpg` remains byte-for-byte in its publication bundle. There is no cropping, upscaling, generative editing or alteration of labels, pathways or chemical structures. Each image opens the original JPEG; the existing Hugo WebP pipeline supplies the page display. No new public reuse license or rights statement is asserted.

| Original figure | SHA-256 | Display WebP bytes |
| --- | --- | --- |
| Anthracene, 583 × 527 | `81edbdd6de0c4fdaf1267e42594066586cd4d2fced7f1d9285b5146d723e7049` | 11,230 |
| QTANHOH, 1000 × 654 | `95f0ef846968b18c92d3a91f13bacc400bfa083dc5ee17375bfbd7987a98f3c8` | 69,098 |
| MPO/liver, 1000 × 391 | `09f8b66e605b8e3b4e3fd3444e29126c45ab4f0cbf3b197e9d15564e8a39829b` | 35,812 |

## Checks

Production and deploy-preview-equivalent Hugo builds pass with 895 pages each. Publication and concept audits preserve 91 records/citations, seven concepts and 24 concept WebP variants. All 466 local image/picture/srcset references resolve across 538 production HTML files. Empty-alt review entries decrease from 72 to 69, including the known, intentionally empty closed Gallery viewer; 68 older publication figures remain for contextual review.

All 121 main-content trees match the baseline after normalizing only the three intended figure presentations. Only the new image frontmatter fields differ in the three paper records; bibliographic fields, original image/attachment bytes, shared templates/styles, homepage selections and the selected-paper/concept records are preserved. All three full-size links resolve to the unchanged original JPEGs, and display dimensions preserve each full image without enlargement. Production and preview indexing behavior is correct on the five checked pages. Removed AI-generation/original-download labels remain absent from built visible text.

The three originals and the two newly widened WebP copies were visually inspected. Real browser layout/interaction and live production were not verified. Delivery is one draft PR; the user retains the merge decision. Continue with a bounded visual review rather than automatically regenerating already suitable diagrams or processing the entire alt-text queue in one turn.

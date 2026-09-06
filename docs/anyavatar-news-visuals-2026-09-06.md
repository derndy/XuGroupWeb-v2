# AnyAvatar and News image improvements — 6 September 2026

## Authentic AnyAvatar pipeline

Source repository: https://github.com/AISHIWEILAI/AnyAvatar

Source snapshot: `072626efc11f0e35a77c058eeb242ccfeca1e093`. README embeds `static/images/pipeline.png`. The original was fetched from https://raw.githubusercontent.com/AISHIWEILAI/AnyAvatar/main/static/images/pipeline.png and inspected.

- Repository original: `assets/media/papers/anyavatar-pipeline.png`.
- Dimensions: 3020 × 1094 pixels; 1,174,893 bytes.
- SHA256: `16006bb94de96e7dd2cb55cae7024121051be0eca2f07336a19d918095e4e6fb`.
- Git blob: `d2239204c27cc8965023e960bf6cf063f1c783ea`, matching the authors' source.
- License checked: https://github.com/AISHIWEILAI/AnyAvatar/blob/main/LICENSE . It explicitly specifies CC BY-NC 4.0 and covers software and associated documentation, including the README's figure. This academic group website is a noncommercial research presentation; commercial reuse is not granted.
- Public credit links authors' repository and https://creativecommons.org/licenses/by-nc/4.0/ and identifies display-size / image-format adjustments. The full original is retained; there is no crop or content edit.

The figure depicts ray proximity localization, multi-view FLAME fitting, Gaussian binding, camera-pose optimization, structured triplane appearance and novel-view rendering. The displayed faces are part of the authors' existing figure; no identity or new performance claim is inferred. This is labelled as an authors' project figure, not a newly published proceedings figure. The existing ACM MM 2026 accepted metadata and author-role symbols remain unchanged.

Two placements use the same source: homepage selection and publication detail. A wide homepage layout avoids squeezing the 2.76:1 figure into the portrait-oriented E-CloudBind column. Both offer full-size viewing. The four WebP derivatives (480, 800, 1200, 3020 pixels) preserve the full aspect ratio. `data/paper_visuals.yml` remains the canonical mapping, caption and license record.

## Four News descriptions

The May 24 thesis defense, May 29 interdisciplinary cinema gathering, April 12 badminton tournament and June 10 graduation records already include `featured_alt` descriptions used by list views. The pinned Hugo Blox header only read `image.alt_text`, leaving these detail-image alt attributes empty.

A repository override of the pinned `page_header.html` now uses existing `image.alt_text` first, then `featured_alt`. When `featured_alt` exists and no explicit image caption exists, the description is rendered below the image in a normal article container. This avoids overlaying new text on a photograph. No photo bytes or event descriptions are edited. Preserve this small customization when upgrading the pinned template.

## Validation and boundaries

Production and preview builds pass (895 pages each). Both existing image audits preserve seven conceptual originals / 28 WebP derivatives and the three framework diagrams. Publication audits preserve all 91 records, citations, title/author text, symbols and accepted status. Ten other main-page content trees are unchanged. The four News details render the exact existing descriptions as alt and captions. Both new figure placements preserve the original hash, dimensions and proportional derivatives.

The full local-image scan covers 536 index pages: all 248 populated references resolve; one initially empty Gallery viewer slot is intentional. Browser viewport testing is not performed. Remaining legacy image descriptions need contextual review, not automated invented labels.

Delivery: new draft PR on `content/paper-visuals-next`, based on merged PR #18. Do not merge or change production configuration. Next source-backed figures are PyraE2E, SyncAnimation and the selected JACS paper.

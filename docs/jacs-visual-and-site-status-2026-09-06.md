# JACS visual and whole-site status review — 6 September 2026

Base: merged PR #24, main `3f0209e3a4cc8231a017c0a4d1b05e30801edc57`. The user corrected PR #24's status during this task; GitHub confirmed the merge. This batch therefore uses the new `content/jacs-visual-site-status` branch, not the closed PR.

## Visual change

The homepage's selected JACS publication now uses its existing discovery-system diagram. The same original appears once on the detail page with meaningful alt text, source attribution, an ACS author-reuse-policy link and full-size viewing. Previously the detail banner had empty alt text and no source caption; adding a second figure would have duplicated it. `image.preview_only: true` retains the bundle image for preview metadata while allowing the credited component to display it once below the article information.

The publication, author list, DOI, abstract, citation download and selected-paper ordering are unchanged. All 91 records remain. Four of the five homepage selections now have figures; PyraE2E is still missing an author-sourced figure.

`publications/paper-figure.html` now resolves either an existing global resource or a page-bundle resource. All existing integrity and metadata checks apply. Display width is capped at the image's native width; larger existing figures remain constrained by their normal page containers.

## Image source, description and reuse

- Original: `content/publication/9-2021-xu-et-al-self-improving-photosensitizer-discovery-system-via-bayesian-search-with-first-principle-simulations/featured.jpeg`.
- Dimensions: 693 × 469; 116,517 bytes. SHA-256: `33091716685e42651e71a28027a7b646064a00cdfc98b6367a2248cb2f1f3073`.
- The bytes are inherited from the user's website. They were inspected, retained exactly and reused directly; no second master image is added and no scientific content is altered.
- The visible diagram links labelled/uncertain search regions, uncertainty and singlet–triplet energy gaps, Bayesian search and active-learning cycles. The new description follows those visible elements and adds no measured result.
- Generated WebP sizes used by this component: 480 × 325, 30,716 bytes; 693 × 469, 48,844 bytes. Both preserve the full frame. The 480-pixel output was visually inspected.
- Article: Shidang Xu et al., *J. Am. Chem. Soc.* **143** (2021), 19769–19777, [DOI 10.1021/jacs.1c08211](https://doi.org/10.1021/jacs.1c08211).
- Reuse basis: [ACS Policies on Public Posting, Sharing, and Preprints](https://pubs.acs.org/pages/authors_sharing), section “Reuse of Figures, Tables, Artwork, and Text Extracts,” checked 6 September 2026 through indexed official content. Authors may reuse their own figures on noncommercial personal/institutional websites with a proper article citation and clear notice of modifications. This is author-specific reuse, not a Creative Commons grant to all visitors.
- Direct ACS article/policy requests returned 403; indexed official policy text was readable. No publisher image was fetched or matched, and no figure number, graphical-abstract designation or higher-resolution source was claimed.

## Full-site checks

Production and preview builds each pass with 895 Hugo pages. The new standard-library script `scripts/audit-site-images.py` scans all 538 generated HTML files, including 536 index pages plus 404/search pages. All 433 local image/picture/srcset references resolve; 254 image elements exist and no external image URLs are present. Source references are counted per occurrence, not as distinct files.

Eighty empty alt entries remain: 73 publication-detail images, six News-detail images and the intentional Gallery viewer slot. This is a contextual review queue; empty alt text can be appropriate for decorative images. Do not fabricate captions to drive the counter to zero. JACS now has a meaningful description, reducing the previous queue by one.

The existing 91-publication audit preserves titles, author roles/links, ordering, routes, attachments and citation bytes. The seven-conceptual-image / 28-WebP and baseline framework audits pass. All eleven main routes plus the JACS detail retain their prior main-element text after excluding the added figure captions. Their IDs are unique. Original JPEG hashes, both full-size links and image dimensions are verified. The detail page has exactly one image and Home has four selected-paper figures.

No new browser test was run: the previous preview attempt established that the supervised browser runtime does not support this Hugo setup. Current page layout, keyboard/touch behavior, 200% text enlargement and reduced-motion behavior remain unverified. Standalone image inspection is not page-layout verification.

## State-record changes

`project-state.md` now provides a current repository/branch/PR snapshot, user decisions, batch scope, source/reuse limits, route-by-route visual coverage, maintenance paths, completed and missing checks, a prioritized backlog, an evidence index and reproducible build/check commands.

The prior 80,855-byte text is preserved verbatim after a historical banner in `project-history-through-pr24-2026-09-06.md`. The archive stays at repository root so its relative links continue to resolve. `PROJECT_STATE.md` retains its pointer to the canonical current file. The README now points to the current state instead of calling a previously merged branch current.

The current backlog explicitly preserves the PyraE2E figure gap, legacy image-description queue, browser-testing limitation, author-archive collision, SCUT/Scholar and final PRCV reconciliation, incomplete member dates/destinations, and separate text-maintenance work.

Delivery is a new draft PR only. The user merged PR #24; this batch does not merge itself or change production settings. Record the product commit and matching preview result in the current state before handoff.

## Confirmed delivery

Saved to [draft PR #25](https://github.com/derndy/XuGroupWeb-v2/pull/25) in product commit `b2f7e35094ac2455de35d3e769fbe7bbcdfb12a3`. GitHub tree `a0ddcb3f30278cf60d84af80966b988c0060f6b9` exactly matches the locally verified source. The matching Netlify Deploy Preview check returned success. [Homepage preview](https://deploy-preview-25--xushidang-lab.netlify.app/#home-publications-title). This following documentation-only update records delivery and triggers a later head check; it does not change the website output. No PR merge or production-setting change was performed.

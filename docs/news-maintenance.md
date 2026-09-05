# News maintenance

The News section is an editorial lab record. Its landing page reads the existing Hugo news bundles directly; it does not maintain a second copy of titles, dates, summaries, images, or URLs.

## Source map

| Source | Purpose |
| --- | --- |
| `content/post/_index.md` | News landing-page title, description, and introduction |
| `content/post/<record>/index.md` | Canonical title, date, summary, body, and publication state for one record |
| `content/post/<record>/featured.jpg` | Optional record-specific image |
| `layouts/post/list.html` | Latest-entry and year-archive structure |
| `layouts/partials/news-record.html` | Reusable archive record |
| `assets/scss/template.scss` | News layout and visual treatment |

Do not copy news facts into a separate data file. The source bundle is the canonical record, and the landing page derives its short presentation from that record at build time.

## Create a record

1. Create a new folder under `content/post/` without renaming any existing folder.
2. Add `index.md` with a verified title and ISO date.
3. Set `draft: true` while wording, date, people, affiliations, claims, and assets are under review.
4. Put the exact short summary before `<!--more-->`. Do not maintain a different summary elsewhere.
5. Add the full body after `<!--more-->` only when there is approved information beyond the summary.
6. Add `featured.jpg` only when it belongs to that record and public use has been approved.
7. Add a factual `featured_alt` field when an image-specific description is available. Legacy records fall back to the existing title; new images should not rely on that fallback.
8. Remove unnecessary camera, location, and personal metadata from new public images before committing them.
9. Review the generated record page and News landing page in the Netlify Deploy Preview.
10. Change `draft` to `false` or remove it only after the publication gate is approved.

Minimal draft structure:

```yaml
---
title: "Approved factual title"
date: YYYY-MM-DD
draft: true
featured_alt: "Factual description of the visible scene"
---
```

Omit unresolved information. Do not publish placeholders, inferred facts, stronger wording, invented metrics, unverified affiliations, or an unapproved translation.

## Scientific and bilingual controls

- A news record that mentions scientific work may use only an approved public claim with its original scope, limitations, evidence boundary, and citation.
- Readiness for publication is not scientific peer review. Do not imply that internal, preliminary, accepted, released, and peer-reviewed states are interchangeable.
- Keep publication state, scientific status, evidence status, access, horizon, and indexation as separate decisions when they apply.
- English and Chinese are separate canonical page-language records. Add a Chinese companion only after its meaning, metadata, route, and reciprocal language link are approved; neither language may make a stronger claim.
- Do not machine-translate a published record directly into the repository.

## Image and URL controls

- Keep images inside the record bundle and use `featured.jpg` for the listing image.
- Record the media owner, rights or consent, and review date outside the public page in the appropriate governance register.
- Do not use paper figures, experimental results, or private screenshots as lifestyle imagery.
- Do not rename a published record folder or move its image without a redirect and reference audit. Hugo derives the public URL from the folder name.
- Preserve original aspect ratios. The News ledger displays the complete source image rather than forcing a decorative crop.

## Release checks

Before a News change is approved, verify:

- every public record has a non-empty title and valid date;
- every unresolved record is explicitly `draft: true` and is absent from the public build and sitemap;
- the chronological order and year counts match the source records;
- every listed destination exists and preserves its expected URL;
- summaries shown on the landing page are derived from the canonical Markdown source;
- all displayed images exist and include intrinsic width, height, and non-empty alt text;
- no image binary changed unintentionally;
- the landing page has one main landmark and one H1;
- all published records are present in the generated HTML without JavaScript;
- there are no inline styles, inline event handlers, empty links, or pagination that hides records;
- title, description, canonical URL, RSS link, and sitemap entry are present; and
- the production-equivalent Hugo build and Netlify Deploy Preview pass.

## Current archive status

The refactored landing page contains 18 published source-backed records across 2022–2025 and six existing featured images. The Mengting Guan record is retained as an explicit draft because its earlier file was entirely commented out; it is not listed, built, indexed, or treated as approved content.

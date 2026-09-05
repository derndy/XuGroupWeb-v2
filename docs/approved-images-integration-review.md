# Approved image integration — ready for GitHub review

Prepared on 5 September 2026 for `derndy/XuGroupWeb-v2`.

Local branch: `design/approved-scientific-images`.

## Completed change

| Image | Page | Placement |
|---|---|---|
| 01 — Three pillars, one discovery core | `/research/` | Research overview after the introduction |
| 02 — Evidence Spiral of Discovery | `/research/evidence-engineering/` | After the opening, before the semantic architecture map |
| 03 — Mathematics to Frontiers, and Back | `/research/mathematical-frontiers/` | After the opening, before the semantic architecture map |
| 04 — Möbius cycle of space–interaction–learning | `/about/` | About / Vision illustration |
| 05 — From Testbeds to Discovery Horizons | `/` | Scientific-testbeds section |
| 06 — Signals into scientific discovery | `/contact/` | Join / Collaborate closing section |

All six PNG originals and approved captions are preserved. Each figure has factual alternative text, a conceptual/AI-generated label, intrinsic dimensions, lazy loading and an original download. The browser selects an uncropped WebP variant at 640, 960, 1440 or 1672 pixels. No image was recoloured, cropped or upscaled.

The new About page uses the existing research identity and is linked from Home and Research. Contact facts and its documentary image remain unchanged. Pillar I keeps its precise semantic map. The inherited People, Gallery, News and Publications redesign is retained.

Netlify deploy-preview and branch-deploy contexts now emit `noindex,nofollow`; production does not inherit this preview-only setting.

## Completed validation

- Hugo Extended 0.139.4 production and preview-equivalent builds: passed, 736 pages each.
- Image audit: all six placements, original hashes/downloads, captions, dimensions and 24 WebP variants passed.
- Scientific headings, existing section content, Pillar introductions and semantic maps preserved against the baseline.
- Main-content local links on seven surfaces resolve; About is present in the sitemap.
- People, Gallery and News main content preserved against the baseline.
- All 78 publication records: titles, authors, order, routes, attachments and citation bytes preserved.
- Preview indexing controls checked on six routes; production checked separately.
- Git whitespace check passed.
- Browser layout review and a hosted Netlify preview were not performed.

## Publication status

The implementation is complete locally. On 5 September 2026, the PI explicitly authorized publishing the prepared branch to the public `derndy/XuGroupWeb-v2` repository and opening a draft pull request, in response to a destination-specific approval request.

The approved delivery is the branch `design/approved-scientific-images` and a draft pull request targeting `main`. Merging, switching Netlify and changes to `derndy/XuGroupWeb` remain outside this delivery. The pull request provides the remote commit and any hosted check results.

### Continuation outcome

The later continuation also completed the Contact presentation update in `b9f9c75` and revalidated the full six-image site. Its push attempt was rejected by automatic approval review because the current request did not explicitly authorize the public `derndy/XuGroupWeb-v2` destination. Despite the earlier recorded authorization above, this tool action remains blocked. No alternate write route was attempted, and no new draft PR or hosted preview was created. See `PROJECT_STATE.md` for the current local checkpoint and the exact remaining approval.

The PI subsequently replied to the destination-specific request and explicitly authorized publishing the prepared branch to public GitHub and opening a draft PR, while keeping the production website unchanged. The prior approval blocker is resolved. Follow `project-state.md` for the confirmed delivery result.

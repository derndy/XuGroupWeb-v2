# Website image review — 6 September 2026

## Coverage and findings

Reviewed the built source for all eleven main pages and scanned 536 generated index pages for local image references. This is source/output inspection, not browser viewport testing or a live remote-image availability check.

| Page | Existing visual coverage | Finding / action |
| --- | --- | --- |
| Home | Learning grammar, evidence loop, conceptual testbed image and PI portrait | Five selected papers have no card figures; source-backed paper visuals are next. |
| About | Approved conceptual vision image | Keep current placement; no additional decorative image needed now. |
| Research | System map and approved overview image | Keep overview while making detailed framework relationships more explicit. |
| Pillar I | Regenerated illustration and five-step framework | Add joint-design diagram with bidirectional middle relationships. |
| Pillar II | Approved conceptual image and five-step framework | Add a visible return from measurement to decision context. |
| Pillar III | Approved conceptual image and five-step framework | Add stress-test feedback to assumptions. |
| Publications | Text index; many legacy detail bundles have figures | Preserve 91 records; newer selected-paper visuals need source and attribution review. |
| People | 21 image elements on the main page | Existing portraits are retained. |
| News | 10 image elements on the first listing page | Existing event photographs retained; detailed article image descriptions merit a separate pass. |
| Gallery | 23 photographs plus an initially empty viewer image | Keep the existing viewer; its image receives its source when opened. |
| Contact / Join | Two image elements | Existing practical and conceptual imagery retained. |

The image scan found 242 local image elements, including one intentionally empty Gallery viewer slot. All 241 populated local image sources resolve. There are 85 empty alternative-text attributes, including the viewer slot and legacy figure/banner uses. These are a follow-up review queue, not a claim that all 85 are errors: decorative images and captioned images need contextual assessment. No photo identities or research results were inferred to fill these descriptions.

## This bounded implementation

Three original, code-native SVG diagrams use the existing five node labels per Pillar. Six assets provide 900 × 460 desktop and 400 × 900 mobile compositions. The method is an editable diagram generator, not AI-generated experimental imagery. Source: `scripts/render-framework-diagrams.py`; canonical labels: `data/research_system.yml`; rendered files: `assets/media/frameworks/`.

The framework template uses a responsive picture element with intrinsic dimensions, meaningful alternative text and lazy loading. Long labels wrap inside nodes. Full existing HTML descriptions remain available through a keyboard-accessible details control; original captions retain their conceptual limitation. This replaces the default wall of five narrow cards with a diagram and optional detailed reading. No new results, paper art, people or experimental facts are introduced.

## Validation

Production and preview builds pass, 895 pages each. The existing seven-image / 28-WebP audit and 91-publication audit pass in both builds. Eight other main-page content trees are unchanged. Three Pillar introductions, briefs, framework node lists and other section contents match the baseline; new diagram assets exist, dimensions are reserved, and H1/IDs remain valid. Desktop and mobile SVG assets were rendered and inspected, with long-label wrapping corrected before delivery. Browser layout testing remains pending.

## Next bounded work

1. Obtain and review authentic method/overview figures for E-CloudBind, PyraE2E, AnyAvatar, SyncAnimation and the selected JACS paper, then add attributable figures to selected work. Existing presence of a legacy file alone does not establish new-placement reuse rights.
2. Review empty alternative text on News and publication detail images against their actual visual content and captions.
3. Browser-check Gallery, the three frameworks and selected work at narrow widths and enlarged text when browser testing is requested.

PR #16 merged while this batch was prepared. Delivery uses a new draft PR from `content/research-framework-diagrams`, based on that merge; production and the original v1 repository remain unchanged by this batch.

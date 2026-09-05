# About page maintenance

Route: `/about/`. This bounded batch implements the Space–Interaction–Learning middle chapter from the design brief. It starts from v2 `main` at `98aeaba4b9bbf89a8e1e016f80886404cbcddad2`, after PR #5 merged. Review branch: `design/about-learning-system`.

## Editing locations

| Change | Source |
| --- | --- |
| Page title, search summary and introductory paragraphs | `content/about/index.md` metadata and Markdown body |
| Displayed hero title/eyebrow, chapter framing, metaphor, long-term programme and onward links | `content/about/index.md` → `about` front matter |
| Shared Space / Interaction / Learning names, questions and definitions | `data/research_system.yml` → `grammar.dimensions` |
| Shared evidence definition, feedback text and evidence route | `data/research_system.yml` → `grammar.evidence` and `grammar.feedback` |
| Page layout and shared-source integration | `layouts/landing/about.html` |
| Scoped About styling | `assets/scss/_about.scss`, imported by `assets/scss/template.scss` |
| Approved image selection | `data/site_visuals.yml` → `about_vision` |
| Image 04 original, caption, alt, hash and approval | `data/research_assets.yml` → `CONCEPT-RES-004` |

All About-specific editorial text now lives in the existing About Markdown file: the old hero and onward-link text was moved from the template without changing what it says. Shared scientific definitions and approved captions remain in their canonical data records. This is a page-level editing improvement, not a completed site-wide single-file text migration.

Editing shared grammar data also affects Home; review both pages when changing it. This batch only reads those records and does not modify the shared scientific wording. Keep the three definitions consistent rather than maintaining another copy in the About page.

## Scientific framing

Space, Interaction and Learning are connected design choices within the learner. They are not three independent research pillars. The broader research programme still connects learning-system design, evidence engineering and mathematical/frontier exploration; molecular/material applications remain testbeds.

The chapter explains the representation–interaction–learning relationship before the artwork. The feedback block uses existing canonical evidence text to connect proposed explanations/designs to further tests. It links to the existing Evidence Engineering page.

Scientific Learning Grammar is labelled **Research horizon** and described with an explicit long-term aim and an open question about transfer across scientific settings. It is not presented as an established theory, completed operator library or achieved general system. The programme link resolves to the existing Pillar I research-horizon heading.

No new result, project record, dataset/code release, timeline, institutional fact or lab operating policy is introduced. The fuller culture, principles and NOW/NEXT/HORIZON chapters remain later bounded work, using appropriate approved public material.

## Image 04 and reading order

Image 04 remains `assets/media/research/mobius-cycle.png`, at the approved `about-vision` placement. The source was visually inspected: a detailed luminous loop and surrounding abstract scientific forms. The design brief allows full-width presentation when a side-by-side arrangement would reduce clarity. This chapter keeps the complete image at full content width, so it is not squeezed beside several paragraphs or cropped into a small card.

Reading order is: chapter introduction → three live-text definitions → a short explanation of the visual metaphor → full image → exact approved caption → evidence feedback and long-term programme → existing onward routes. CSS does not reorder this sequence on smaller screens. Definitions and the two following text blocks become single columns below 62rem.

The loop is identified as a metaphor for mutual shaping; the text makes no claim of exact Möbius topology. The original PNG bytes, alt text, approved caption, visible conceptual/AI-generated label, download action and four uncropped WebP variants are unchanged. No labels are painted onto the artwork and no additional image is introduced.

## Validation and release

Completed build and preservation results are recorded in `project-state.md`. Check both Hugo contexts, all six image placements and all 78 publication/citation records. Verify About's three shared definitions, evidence text, programme qualification, unique heading IDs and three new destinations, including the Pillar I horizon anchor. Compare the old hero, illustration and onward routes and the ten other main-content trees with the preceding Contact-pathways build.

Real browser layout, keyboard/touch, text zoom and image loading remain separate review work. A successful Netlify build is not browser QA. Keep this delivery as a draft PR; no merge or production/hosting change is part of the batch.

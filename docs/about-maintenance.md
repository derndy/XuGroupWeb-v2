# About page maintenance

Route: `/about/`. The Space–Interaction–Learning middle chapter was delivered in PR #6 and is now merged. This bounded batch adds research principles and the NOW / NEXT 3–5 YEARS / HORIZON sequence. It starts from v2 `main` at `424fcdb79a3d3006aa255538fe075e83b00fffb2`. Review branch: `design/about-principles-horizons`.

## Editing locations

| Change | Source |
| --- | --- |
| Page title, search summary and introductory paragraphs | `content/about/index.md` metadata and Markdown body |
| Displayed hero title/eyebrow, chapter framing, metaphor, long-term programme and onward links | `content/about/index.md` → `about` front matter |
| Shared Space / Interaction / Learning names, questions and definitions | `data/website_text.yml` → `shared.grammar.dimensions` |
| Shared evidence definition, feedback text and evidence route | `data/website_text.yml` → `shared.grammar.evidence` and `shared.grammar.feedback` |
| Principles and horizon chapter headings, framing and related-link introduction | `content/about/index.md` → `about.principles` and `about.horizons` |
| Six scientific principles and three stage records, shared with Research | `data/research_system.yml` → top-level `principles` and `horizons` |
| Detailed horizon destinations and their descriptive link labels | `data/research_system.yml` → `pillars[].detail_url` and `pillars[].public_title`; existing `#pillar-horizon-title` on each pillar page |
| Page layout and shared-source integration | `layouts/landing/about.html` |
| Scoped About styling | `assets/scss/_about.scss`, imported by `assets/scss/template.scss` |
| Approved image selection | `data/site_visuals.yml` → `about_vision` |
| Image 04 current source, prior original, caption, alt, hash and instruction basis | `data/research_assets.yml` → `CONCEPT-RES-004` |

All About-specific editorial text now lives in the existing About Markdown file: the old hero and onward-link text was moved from the template without changing what it says. Shared scientific definitions and approved captions remain in their canonical data records. This is a page-level editing improvement, not a completed site-wide single-file text migration.

Editing shared grammar data also affects Home; editing the top-level principles or horizons affects Research and About. Review the affected pages together. This batch only reads shared records and does not modify the shared scientific wording. Keep definitions, principles and stage content consistent rather than maintaining another copy in the About page.

## Scientific framing

Space, Interaction and Learning are connected design choices within the learner. They are not three independent research pillars. The broader research programme still connects learning-system design, evidence engineering and mathematical/frontier exploration; molecular/material applications remain testbeds.

The chapter explains the representation–interaction–learning relationship before the artwork. The feedback block uses existing canonical evidence text to connect proposed explanations/designs to further tests. It links to the existing Evidence Engineering page.

Scientific Learning Grammar is labelled **Research horizon** and described with an explicit long-term aim and an open question about transfer across scientific settings. It is not presented as an established theory, completed operator library or achieved general system. The programme link resolves to the existing Pillar I research-horizon heading.

No new result, project record, dataset/code release, deadline, institutional fact or lab operating policy is introduced. Research culture, the rationale for testbeds and a PI programme overview remain later bounded work using appropriate approved public material.

## Principles and research directions

The six principles are rendered verbatim from Research's existing public records: Mechanism-aligned, Evidence-efficient, Uncertainty-aware, Compositional, Testable and Design-oriented. They are a shared scientific approach, not a new operating handbook. The related link reaches the real `/research/#principles` section.

The three stages use the same labels, titles, text and order as Research's top-level horizon records. The About introduction explicitly distinguishes timing/ambition from evidence strength and completed results. NOW describes ongoing work, NEXT 3–5 YEARS expresses intended connections, and HORIZON remains an open long-term programme. Do not add a fixed completion date, completed-status marker or evidence-strength badge to these stages.

The stage list is followed by three descriptive links to the existing pillar horizon sections. Each link uses the canonical pillar's public title and detail URL, so visitors can follow learner design, evidence engineering and mathematical exploration in more depth. No private archive text or new scientific claim is imported.

Principles form a two-column semantic list; horizons remain three vertically ordered rows with a label beside each explanation. Both become single columns below 48rem. Native links, visible focus outlines, wrapping content and natural heights require no additional JavaScript or interaction to read the material. List roles retain list semantics when CSS removes markers.

## Image 04 and reading order

Updated 7 September 2026, after merged PR #31. Image 04 now uses `assets/media/research/representation-interaction-revision.png` at the existing `about-vision` placement. Three interlinked bands distinguish spatial arrangements, relationships and revision while suggesting mutual shaping. These are design choices within the learner, not the research programme's three pillars. The artwork is a metaphor, not exact topology, a measured result or an algorithm.

This chapter keeps the complete image at full content width. Reading order remains: chapter introduction → three shared live-text definitions → explanation of the visual metaphor → image → descriptive caption → evidence feedback and long-term programme → principles → NOW/NEXT/HORIZON → detailed pillar links → onward routes. CSS does not reorder this sequence on smaller screens.

The current web source is 1280 × 720 and produces uncropped 640-, 960- and 1280-pixel WebP variants. The caption, alt text, source hash and generation record match this version. The old `mobius-cycle.png` remains unchanged in the repository with its complete original record under `previous_version`. The user authorized regeneration for draft review; no separate approval of the exact new pixels is claimed. The shared component's AI label and original-download control were removed in PR #29 and remain absent. No text is painted onto the artwork.

Prompt, rationale and source transformation: [About concept record](about-concept-2026-09-07.md). Current checks are recorded at the top of `project-state.md`; older batch numbers elsewhere in this document describe their original delivery.

## Validation and release

Completed build and preservation results are recorded in `project-state.md`. Check both Hugo contexts, all seven image placements and all 91 publication/citation records. Verify the six canonical principles, three canonical stages in order, explicit ambition/evidence distinction, unique heading IDs and all four new destinations. Compare the previous About page with the baseline build, allowing only the intended image, caption, alternative text and metaphor wording changes. Preserve the other page content and destinations. Preserve page metadata, the original Markdown introduction, shared research data and hosting configuration.

Real browser layout, keyboard/touch, text zoom and image loading remain separate review work. A successful Netlify build is not browser QA. Keep this delivery as a draft PR; no merge or production/hosting change is part of the batch.

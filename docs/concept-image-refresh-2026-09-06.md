# Concept image review and caption cleanup — 6 September 2026

Base: `3fda4dcc2a0c06546a59b3905ffb07a7b0e737c9` (main after merged PR #28).
Branch: `design/concept-images-cleanup`.

The PI asked to remove the visible “AI generated” and “download origin.png” labels and to inspect and regenerate concept images where a better fit is possible. This instruction supersedes the earlier presentation rule requiring an AI badge. It authorizes the image work and draft PR; it is not a claim that the PI separately reviewed the new pixels.

## Presentation change

The shared `conceptual-figure.html` component now renders the image and one explanatory caption. The AI badge and original-download control are removed from HTML, not hidden with CSS. Obsolete badge/button styles are removed. All seven placements keep alternative text, caption association, intrinsic image dimensions, an original PNG fallback and uncropped WebP variants. Provenance and previous-version records remain in `data/research_assets.yml`. Published paper credits, source links, exact framework diagrams and their full-size links retain their existing behaviour.

## Review of all seven concept images

| Placement / asset | Decision | Reason |
| --- | --- | --- |
| Research overview / 001 | Replace with `research-system-design.png` | The old glowing core, dense paths and repeated spirals made three contributions hard to distinguish. The new composition gives learning structure, evidence and mathematical constraints distinct groups. |
| Pillar II / 002 | Replace with `evidence-discovery-cycle.png` | The old ascending spiral suggested a molecular screening machine and inevitable progress. The replacement makes candidate choice, observation, model revision and the return to inquiry visible. |
| Pillar III / 003 | Retain `mathematics-frontiers.png` | Mathematical forms, varied scientific settings and a return path support the page's exchange between methods and scientific questions. It remains atmospheric; the separate exact framework carries the detailed logic. |
| About / 004 | Retain `mobius-cycle.png` | A single recurring form is effective for the conceptual relationship between representation, interaction and learning. It is not used to explain an algorithm. |
| Home testbeds / 005 | Replace with `scientific-testbeds.png` | The old image was crowded and low in contrast, with small molecular objects dominating. The replacement balances material/delivery, sequence/protein and scientific data motifs at a useful scale. |
| Join / Collaborate / 006 | Retain `signals-discovery.png` | Converging inputs and branching possibilities suit the closing invitation. Repeating this motif in the technical research sections is avoided. |
| Pillar I / 007 | Retain `representation-interaction-learning.png` | Recurring entities and three legible headings already make this the clearest existing concept illustration. |

The three generated replacements are explanatory artwork. The site's exact SVG frameworks and worked examples continue to provide precise definitions, arrows, quantities and scientific caveats. They were not passed through image generation. The actual third Pillar remains mathematical/data-science exploration, not an applications category.

## New sources and version history

All three new sources are RGB PNGs, 1672 × 941. They were generated once each with the built-in image tool, inspected at full size, and integrated without cropping, retouching or recompression. The source prompts are in [the prompt record](concept-image-prompts-2026-09-06.md).

| Asset | Source under `assets/media/research/` | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| 001 | `research-system-design.png` | 1,681,858 | `abc150c581fdd3776c1d8dc70c46353e297667f8ee788ed3a9aee60ce46dab59` |
| 002 | `evidence-discovery-cycle.png` | 1,462,408 | `23b1d6338dbdb44408cd19cb29b05f8eb29f71502e681b586d587737d1961b41` |
| 005 | `scientific-testbeds.png` | 1,766,252 | `73138d719fec4e47d21e815d4c941a03a9894ac048da4924f03a91afcae6a275` |

Each changed record contains its complete prior record under `previous_version`, including the old source hash, captions, Drive archive and original approval. The old PNGs remain under their original paths for recovery and are no longer referenced for rendering. No new Drive archive is claimed. Other asset records are unchanged.

## Visual inspection and limits

- The new images contain no text, badges, download controls, watermarks or logos. Light grounds, larger forms and the existing blue/teal/navy palette pair with the site's white research sections and Pillar I illustration.
- Overview: the observation tiles include natural-image motifs. They stand for varied inputs; neither those tiles nor the mathematical surface represent collected evidence or a fitted model. A reader can use the existing three-part HTML guide to identify the three contributions.
- Evidence: the generator introduced a stylized physical probe that enters from the upper edge and explicit arrows. The probe is a metaphor for an observation, not a specification for lab equipment or a restriction to physical experiments. The caption and exact evidence framework set the scientific scope. A faint alternative graph remains visible.
- Testbeds: ribbon, porous structure, vesicle and signal/image patterns are illustrative. They are not a known protein structure, microscopy results or measured traces.
- The original artwork is preserved in the image frame at every width. Readable explanatory language remains outside the raster images.

## Validation

Validation results are recorded in the current section at the top of `project-state.md`. The existing conceptual-visual check now enforces clean captions with conceptual context and the absence of the removed badge/download controls, while retaining all hash, dimension, placement, responsive-image and legacy-exclusion checks. No publication facts, member profiles, research definitions or production configuration are changed.

Delivery follows the existing review-branch → draft PR → user review workflow. A successful build or preview does not itself mean the production site has changed.

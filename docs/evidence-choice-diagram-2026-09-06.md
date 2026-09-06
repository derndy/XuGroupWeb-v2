# Evidence-choice diagram — 6 September 2026

Base: main `36cfe4636bfc09a79efa8dc9c6b4feaef2e6fbe4`, after PR #22 merged.

## Purpose and scientific scope

Pillar II already has an overall discovery loop. This local diagram expands one part of that loop: choosing evidence that could distinguish explanations fitting current observations. It connects a feasible perturbation, differing predictions, measurement with controls, and the assessment of differences against uncertainty. The two outcome branches retain both informative and ambiguous results. Neither branch claims that one experiment establishes a unique mechanism.

Grounding: the existing Pillar II introduction, Competing hypotheses / Acquire or create / Measure and update framework nodes, and Active acquisition scope in `data/research_system.yml`. This is an original conceptual teaching diagram, not a paper figure, an experimental result, a quantitative model or a claim of completed work. No external image was used.

## Placement and maintenance

One figure is added after Pillar II's existing scope cards at `/research/evidence-engineering/`. The original scope text and overarching framework remain unchanged. The figure has a meaningful alt description, HTML caption, uncertainty qualification and direct links to both SVGs.

Editable generator: `scripts/render-evidence-choice.py`. Run it from the repository root to regenerate `assets/media/frameworks/evidence-choice.svg` (960 × 850) and `evidence-choice-mobile.svg` (440 × 1130). It uses only the Python standard library. Keep the template description and generator labels consistent when changing the scientific explanation.

The narrow composition retains the two competing explanations side by side with larger labels. The responsive picture reserves the appropriate dimensions at the 47.99rem breakpoint. Existing site colors distinguish the ambiguous branch, with explicit text so color is not the sole cue.

## Validation

Both Hugo builds pass (895 pages each). The whole-site source/output scan covers 536 index pages in each build; all 251 populated local image references resolve. Exactly one new diagram placement and its two full-size links exist. Existing main-element visible text matches the prior build after removing the new figure. Publication and research-visual baseline audits pass: all 91 publication records and seven approved conceptual raster images / 28 WebP derivatives are preserved.

Both SVG compositions were rasterized and inspected as standalone assets. Adjustments removed junction arrowheads, wrapped long labels, and enlarged narrow-layout labels. This is asset inspection, not browser layout testing; browser viewport review remains pending.

Delivery: draft PR only; no production merge or configuration change. Remaining priorities include authentic PyraE2E and selected-JACS figures, legacy image descriptions, and browser layout review when requested.

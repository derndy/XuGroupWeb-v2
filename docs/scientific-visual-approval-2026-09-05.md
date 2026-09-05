# Scientific visual approval — 5 September 2026

## Decisions

The PI approved images 01–03 with **“1-3 approve”**, followed by images 04–06 with **“4-6 approve”**. Each decision refers to the actual original image, its planned page placement, and the caption shown immediately before the decision. All six originals are approved as shown; image 01 was not recoloured or edited.

This supersedes the earlier one-image decision recorded in this file. It approves conceptual website use, not experimental results. Saving the implementation to the separate redesign repository does not change the original website or authorize a Netlify production switch.

| Review | Asset | Approved placement | Approved source SHA-256 |
|---|---|---|---|
| 01 | CONCEPT-RES-001 — Three pillars, one discovery core | Research Overview, below the introduction. | `735a2c053ef15d2d265a301d5de684dc783cb7474e36e0cbf33d428e6da4ae6a` |
| 02 | CONCEPT-RES-002 — Evidence Spiral of Discovery | Pillar II, alongside the explanation of evidence engineering. | `c55e7fd1dac7e954746f5556a9286fdb5be4d7ff6e36bccd462a80c851ff8ff9` |
| 03 | CONCEPT-RES-003 — Mathematics to Frontiers, and Back | Pillar III, below its opening statement. | `4870b89430de42b07079645d3189f1e37f5d059034f6a03e6b4ec8e4b6875092` |
| 04 | CONCEPT-RES-004 — Möbius cycle of space–interaction–learning | About / Vision, beside the explanation of Space–Interaction–Learning. | `1d72f9a2acede990f979fedce445d18ef62212503a25f217ebea24658c777b9c` |
| 05 | CONCEPT-RES-005 — From Testbeds to Discovery Horizons | Homepage, scientific-testbeds section. | `3b48ea0f1403fd38c3981574534e40b6c4bc75c9fd14772edb6640af9fe95a8e` |
| 06 | CONCEPT-RES-006 — Signals into scientific discovery | Join / Collaborate, closing section. | `82e5f04b9d83b4812487bb9308a84bf9e47811133d260fe34f8edc692d798e7a` |

## Captions

### 01 — Three pillars, one discovery core

A conceptual view of three connected research pillars: learning-system design, evidence engineering, and mathematical exploration.

### 02 — Evidence Spiral of Discovery

A conceptual illustration of repeated cycles linking candidate design, evidence generation, evaluation, and model revision.

### 03 — Mathematics to Frontiers, and Back

A conceptual view of the exchange between mathematical structures and scientific questions, with each informing the other.

### 04 — Möbius cycle of space–interaction–learning

A conceptual illustration of how scientific representations, interactions, and learning continually shape one another.

### 05 — From Testbeds to Discovery Horizons

A conceptual illustration of scientific testbeds connecting materials and biomedical questions with future discovery directions.

### 06 — Signals into scientific discovery

A conceptual illustration of diverse scientific inputs coming together to open new directions for discovery and design.

## Delivery

- Original PNGs preserve their exact SHA-256 values and 1672 × 941 dimensions.
- The shared component creates uncropped WebP copies at 640, 960, 1440 and 1672 pixels; no upscaling.
- Every image retains its approved caption, factual alternative text, a visible conceptual/AI-generated label, and an original download link.
- Text remains outside the images and precedes them on narrow screens. The 06 invitation uses a stacked layout to preserve the full image.
- Each consuming page includes one conceptual illustration at most. Pillar I keeps its existing precise semantic architecture map.
- The existing source-hash, dimensions, role and placement checks apply to all six records. Conceptual review cannot satisfy the result-figure evidence gate.
- The two legacy Research PNGs remain blocked and outside the public output.

## Implementation scope

- Six approved image records, exact captions and bounded page placements.
- About / Vision route with copy drawn from the existing research identity and links from Home and Research.
- Existing Contact facts and documentary image retained; one semantic main landmark and an approved closing illustration added.
- Original scientific text, People, Gallery, News, Publications and their media remain in place.

## Validation commands

```bash
hugo --gc --minify -b https://xushidang-lab.netlify.app/ -d /absolute/build
python3 -B scripts/audit-research-visuals.py /absolute/build --before /absolute/baseline
python3 -B scripts/audit-publications.py /absolute/build --before /absolute/baseline
git diff --check
```

Run the same clean build with Netlify preview settings and `--buildFuture`. These are source/build checks; browser layout review is a separate activity.

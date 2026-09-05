# Scientific visual governance

Scientific visuals have an explicit role: conceptual illustration, conceptual framework, method diagram, or evidence-bearing figure. A file being present in the repository does not make it approved for public use.

## Publication gate

A visual may render on a public Pillar or Project page only when all of the following are recorded:

- stable `asset_id`;
- repository `source_path`;
- public `public_url` for an approved web derivative;
- scientific role: conceptual framework, method diagram, data figure, result figure, or photograph;
- accurate caption and alternative text;
- provenance and versioned evidence source;
- rights or participant-consent status;
- scientific evidence status;
- publication state;
- responsible owner and last review date.

For result-bearing visuals, `rights_status`, `evidence_status`, and `publication_state` must all equal `APPROVED`. The `governed-figure.html` partial makes missing or non-approved metadata a Hugo build error rather than silently publishing the asset. This gate remains unchanged.

For approved AI-generated conceptual illustrations, use `scientific_role: conceptual-illustration`, `evidence_status: CONCEPT_REVIEWED`, and `APPROVED` rights/publication states. The separate `conceptual-asset.html` partial requires the PI approval record, the source file's approved SHA-256 and dimensions, and the exact intended placement. It cannot accept a result figure through this conceptual path. Resizing for web delivery does not change the approved source; a content change or a new placement requires review of that change, not re-approval of uses already authorized.

Conceptual diagrams must state that they are conceptual and must not use styling or captions that imply measured results. Generic AI imagery is not a substitute for a scientific figure.

All six conceptual illustrations were approved as shown on 5 September 2026. See [the approval record](scientific-visual-approval-2026-09-05.md) for their exact sources, captions and permitted placements. Images 01–03 cover Research and Pillars II/III; 04–06 cover About/Vision, homepage testbeds and Join/Collaborate. Their public label identifies the conceptual/AI-generated role; internal approval history stays in the repository.

## Legacy Research images

The files now stored as `audit/legacy-research-assets/2.png` and `audit/legacy-research-assets/4.png` arrived in the initial repository import. Their original component sources, reuse rights, captions, alternative text, and approval history are not recorded. They therefore remain in the repository for traceability but are classified as `BLOCKED / REVIEW_REQUIRED` in `data/research_assets.yml`. Keeping them outside Hugo's `content/` and `static/` trees also prevents them from being copied into the public website output.

## Intake sequence

1. Add or update the asset record in `data/research_assets.yml`.
2. Verify the source file, component provenance, and image dimensions.
3. Write a factual caption and concise alternative text.
4. Record rights or consent and the relevant evidence object or approved conceptual source.
5. Obtain scientific and publication approval.
6. Add the approved `asset_id` to the relevant Pillar or Project visual list; do not duplicate the metadata.
7. Run the production Hugo build and inspect the resulting figure, caption, link, crop, and mobile behaviour.
8. Review the Netlify Deploy Preview before merge.

For conceptual illustrations, place the original under `assets/media/research/` and connect its ID through `overview_visual` or `detail.intro_visual` in `data/research_system.yml`, or the named placements in `data/site_visuals.yml`. Use `conceptual-figure.html` for the caption, original download, and responsive variants. Keep these images out of the result-evidence `detail.visuals` list. Hugo publishes only referenced image resources; do not move unapproved files into `static/`.

# Research invitations and five selected papers — 5 September 2026

Base: merged PR #12/#13, `main` at `c9afdcf43cb59d679c1cc199f95a81814f07e615`. Branch: `content/research-invitations-selected-work`. Delivery is a draft PR only; no merge or deployment-setting change.

## Requested boundary

Preserve the original hero title, subtitle, tagline, formal three pillars, shared Space–Interaction–Learning definitions and the complete Vision at the end of Join / Collaborate. Do not revive the rejected generic marketing rewrite. Make a bounded connection between research methods, demonstrated work and joining opportunities. Keep molecular, biological and materials work as important testbeds, not the exclusive scope of the methods. Do not add more fields to Pillar III.

## Changes requiring attention

1. Home and Research now state more clearly that model architectures, learning methods and evidence acquisition can themselves be research contributions. This changes the emphasis, not the declared pillar structure. The fourth homepage testbed mentions multimodal data, consistent with existing computer-vision papers; the other three testbed cards are retained.
2. Five homepage papers replace two. Citation actions now sit within each paper entry to avoid a second list repeating five titles. The five-paper section is still longer; no claim is made that the entire homepage retains its previous height.
3. Join explicitly welcomes postdoctoral proposals centred on a method or architecture. The wording asks what applicants want to shape and how it connects with the group's scientific work. Funding, openings, application timing and necessary project support remain questions for discussion, not guarantees.
4. Management-style passages become scientific explanations. Research standards, uncertainty, comparisons, negative evidence and reproducibility remain. Backend approval/metadata validation stays intact. About shares the revised NOW horizon and therefore changes at that same entry; its other text and the complete Vision are untouched.

## Representative before / after

| Earlier public wording | New wording | What remains |
| --- | --- | --- |
| Evaluation contract; frozen splits, stop conditions | Evaluation framework; comparisons, controls and uncertainty tests | Evaluation quality and limits, without internal sign-off language |
| Public statements must resolve to a reviewed record, evidence object, figure, and responsible owner | Connect conclusions to the data, methods and analyses that support them | Reproducibility and support for claims |
| Evidence audit | Evidence quality | Measurement context, coverage, bias, uncertainty and unresolved gaps |
| Generated candidates remain proposals until measurement, adjudication and release review are complete | Test predictions with measurements that can confirm, refine or challenge their expected effects | Prediction is not experimental confirmation |
| Contribution contract / Intended artifacts / Evidence discipline | Research contributions / What we aim to develop / Scientific principles | Clear distinction between work sought and established results |

Some stable YAML keys and class names still contain `review` or `responsibility`; these are implementation identifiers, not public copy. Unused asset-provenance templates and scientific-image release checks are not disabled or relabelled. This is not an archive-wide privacy review, and it introduces no unpublished targets, protocols or detailed architectures.

## Selection judgment and limits

The homepage order is E-CloudBind (Nature Communications 2026), PyraE2E (ECCV 2026, Accepted), AnyAvatar (ACM MM 2026, Accepted), SyncAnimation (IJCAI 2025) and the self-improving photosensitizer discovery system (JACS 2021). [The maintenance guide](homepage-records-maintenance.md) records the primary sources and each focus.

The fifth choice is deliberately older: it connects active learning and Bayesian search to an actual discovery system. This is an editorial choice about breadth and continuity, not a claim to list the five newest or highest-impact papers. MPFusion-MIL and the formerly selected Chemistry of Materials paper remain available in the archive. Short labels describe each paper's scope; they do not assert field-wide impact or demonstrated generalisation beyond its evidence. No future project details or unpublished results are added.

AnyAvatar's existing authorship/acceptance source was checked in the prior bibliography batch. Its public project page could not be reread this time, so this batch does not make new technical or performance claims. The existing SCUT-profile/author-role reconciliation limits remain as documented in [the accepted-work audit](publication-authorship-accepted-2026-09-05.md).

## Validation

Both Hugo build contexts pass (885 pages). Both publication audits preserve all 91 records, canonical author text/links, ordering, attachment controls and citation bytes; both visual audits preserve six approved originals and 24 uncropped variants. All 1,417 internal links/anchors across eleven main pages resolve in each build; single H1/main, unique IDs, matching production/preview content and preview-only noindex pass.

All nine existing publication JavaScript tests and three DOI regression tests pass. Two temporary invalid selections correctly fail the build: a duplicate paper and an accepted preprint whose canonical type is still Working paper. The final five-paper order and each paper/focus pairing are checked after restoring the selection.

Generated-HTML checks confirm exactly five selections with canonical titles/authors/citations, correct conference/journal labels, two explicit Accepted states and year-only dates, and no fabricated DOI. The original homepage hero, pillar cards, grammar, evidence loop, people and news sections are unchanged. People, Gallery, News and Publication main-content trees match the baseline exactly. Contact facts, mailto subjects and final Vision match the baseline; About differs only in the shared NOW entry.

Browser layout, keyboard/touch interaction and external client behaviour have not been tested in this batch. Build success is not a substitute for that review. Refer to `project-state.md` and the actual PR-head checks for delivery status.

# Publication link audit — 5 September 2026

This is the review record for Slice 10, based on the four malformed DOI fields identified in Slice 09. Baseline remote commit: `a2da7b03397bac9b3ce1ca6be3972a6dcf115e4d`; baseline source tree: `3e2bc920ba0d9d58c6959858c4e5ac17aab619c2`.

## Decision and evidence

Correct the publication identity before repairing its URL. Two existing records describe artwork-related journal entries, while their old DOI fields refer to the underlying research papers. Their titles, dates, abstracts, and citation page/article numbers identify the frontispiece or cover. Preserve those records and their public routes; do not turn them into duplicates of the full papers.

The three journal identifiers and bibliographic fields below were checked against publisher-deposited Crossref metadata using the public works API. Wiley's journal pages/issue listing and the AIChE organizer page provide additional source evidence. Sources were checked on 5 September 2026.

| Bundle prefix | Authoritative evidence | Applied changes |
| --- | --- | --- |
| `67- Wiley Online Library-2018-Photoacoustic Imaging` | [Wiley frontispiece](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.201870214), [Crossref record](https://api.crossref.org/works/10.1002/adma.201870214), [underlying paper](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.201800766) | Set `doi` to `10.1002/adma.201870214` and add it to `cite.bib`. The existing title, online date 2018-07-16, and citation article number 1870214 refer to the frontispiece. Move the old HTML paper destination out of `url_pdf` into a custom link named “Research article”. |
| `73-Chem Mater-2020-All-in-one molecular AIE theranostics` | [ACS record](https://pubs.acs.org/doi/10.1021/acs.chemmater.0c01187), [Crossref record](https://api.crossref.org/works/10.1021/acs.chemmater.0c01187), [author-institution repository record](https://scholarbank.nus.edu.sg/entities/publication/18e0278b-8435-464d-a501-53233c1c80b7) | Store the bare DOI. Use the publisher-deposited full title, Chemistry of Materials / Chem. Mater., and first-online date 2020-05-11. Align BibTeX title and journal, add issue 11 and DOI, and expand pages to 4681–4691. Retain volume 32, all authors, the repository PDF, abstract, summary, and Hugo scheduling date. |
| `76-Small-2016-Cell Tracking Organic Nanoparticles` | [Crossref cover record](https://api.crossref.org/works/10.1002/smll.201670244), [Wiley issue: Cover Picture](https://onlinelibrary.wiley.com/toc/16136829/2016/12/47), [underlying paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/smll.201601630) | Set `doi` to `10.1002/smll.201670244` and add it to `cite.bib`. Retain the cover's 2016-12-15 online date and page 6419. Correct BibTeX volume/issue from 47/12 to 12/47. Move the existing full-paper PDF to a custom link named “Research article PDF”. |
| `79-Virtual AIChE Annual Meeting-2020-Physically Informed` | [Organizer abstract 605068](https://aiche.confex.com/aiche/2020/webprogram/Paper605068.html), reached through the [organizer author index](https://aiche.confex.com/aiche/2020/webprogram/authorx.html) | Clear `doi` and `url_pdf`; add a “Conference abstract” custom link to the organizer's static record and the same URL in BibTeX. The organizer confirms the title, author order, and 2020-11-17 date and says an extended-abstract file was not uploaded. |

The AIChE change means **no DOI is recorded here**; it is not a claim that no DOI exists anywhere. The HTML abstract is a useful source in its own right and must not be presented as a PDF download.

Crossref confirms Small volume 12, issue 47, pages 6419–6419 for the cover; the underlying paper instead occupies pages 6576–6585. The Advanced Materials frontispiece and full paper likewise have different DOI suffixes (`201870214` and `201800766`). This distinction is substantive, not URL formatting.

The ACS landing-page fetch returned 403 in the retrieval environment. The correction uses the successfully retrieved publisher-deposited Crossref record, corroborated by the indexed ACS and NUS bibliographic records. This audit does not claim that ACS full text or the existing NUS PDF was downloaded successfully. The Wiley frontispiece bibliographic search result and Crossref record were available; not every publisher HTML endpoint was retrievable.

## Exact preservation boundary

- Four existing page bundles and their four citation files are updated; no bundle is added, removed, renamed, or given a new route.
- All author arrays/order/notes, abstracts, summaries, tags, scientific claims, image files, and Hugo `publishDate` values are preserved.
- Only the ACS record's title, venue, abbreviated venue, and `date` change in addition to the documented DOI/link fields. Its chronological position follows the corrected first-online date.
- Full-paper destinations for the two artwork records remain available under explicit labels. Neither link is presented as the DOI/PDF of the artwork record itself.
- Citation entry keys remain stable. Existing author spellings and truncation conventions are not silently revised; a later full citation audit can address them separately.
- The other 74 publication bundles are unchanged. No shared layout, stylesheet, filter behavior, hosting configuration, or production branch is changed.

## Verification and remaining scope

Run the production and Netlify-equivalent preview builds, then `scripts/audit-publications.py` on each output. The audit now checks DOI-button syntax in the index and every linked detail page. Regression tests cover valid identifiers, duplicated resolver prefixes, a meeting URL in the DOI slot, escaped URL prefixes, malformed links, and records with no DOI.

For this metadata patch, compare the other 74 record signatures and citation bytes exactly against the baseline. Inspect the four intended exceptions individually, including the source diff, generated DOI/custom links in both index and detail pages, and downloaded citation bytes. Do not loosen the existing strict `--before` check: it should reject an intentional metadata change when used as a presentation-only check.

Build success does not certify scientific content, browser behavior, publisher availability, or PDF access. The remaining archive-wide title/venue/date/citation audit, explicit cover/frontispiece presentation, and browser preview review are subsequent bounded work. Keep PR #3 in draft; this patch does not authorize a merge to production.

Completed local checks: production and preview-equivalent builds each generated 735 pages; the publication audit passed for 78 records, 13 years, and five types. Three DOI regression tests passed, and the new gate rejected the actual pre-fix build. The four intended metadata diffs were checked field by field, the other 74 record signatures and citation files matched the baseline, and all 78 publication routes, author arrays, abstracts, summaries, and image files were preserved. Corrected attachment controls agree between the index and the four detail pages. No browser/visual QA was performed in this slice.

Follow-up: Slice 11 adds explicit Frontispiece and Cover picture display classifications for the two verified artwork records, with shared index/filter/detail labels and separate research-paper explanations. It preserves this audit's corrected metadata and citation files. See [Publications maintenance](publications-maintenance.md#artwork-classification-and-research-paper-links) for the field contract and completed checks.

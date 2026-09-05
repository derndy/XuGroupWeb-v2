# Publications update — 5 September 2026

## Scope and source coverage

This update adds ten previously absent, publicly documented records: eight from 2025 and two from 2026. They comprise six journal articles, one conference paper, and three preprints. The existing 78 bundles, citation files, figures and routes are unchanged. The new total is 88 records, with 2025 and 2026 derived automatically in the index and year filter.

The user requested an update against their [SCUT profile](https://www2.scut.edu.cn/bmse/2019/0222/c26925a633837/page.htm) and [Google Scholar profile](https://scholar.google.com/citations?user=HiGQESUAAAAJ&hl=en&sortby=pubdate). The supplied SCUT URL could not be retrieved (search-reader failure and direct-request timeout); Scholar returned HTTP 403. Neither profile was successfully read directly, so this is **not a certified complete reconciliation with Scholar**.

Search retrieved the indexed text of a second [official SCUT supervisor profile](https://www2.scut.edu.cn/bmse/2021/1213/c40036a498850/page.htm). Its six 2025 entries are CDSR, MoGaFace, the Cell Biomaterials hydrogel paper, the JACS fluorescence paper, SyncAnimation, and the Advanced Science review. All six are included here after checking their primary records. Opening that alternate profile currently redirects to an invalid-article notice; its indexed text is discovery evidence, not a claim that the live page was readable. Other candidates were discovered through author/title searches and then verified independently.

Author order, titles, venues and identifiers were checked against publishers, the IJCAI organizer, arXiv, ChemRxiv, and publisher-deposited Crossref metadata. Journal author lists retain full names; no contribution or corresponding-author markers are inferred. Publisher line breaks and typographic hyphens are normalized for readable titles. ACS/PubMed capitalization `Wing-Tak Wong` is retained where Crossref uses `Wing-tak`.

## Added records

Each bundle contains `index.md` and `cite.bib`. DOI links use bare identifiers in front matter, with a single resolver added by the existing template. The source links below support the record identity and publication status, not an independent scientific validation of the work.

| Bundle under `content/publication/` | Title | Source and DOI | Website date / citation |
| --- | --- | --- | --- |
| `2026-sonochemical-molecular-glue` | A Sonochemically Activatable Pro-Molecular Glue for Spatiotemporally Controlled Targeted Protein Degradation | [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/anie.7024563); [Crossref](https://api.crossref.org/works/10.1002/anie.7024563) | 30 Aug 2026, first online; *Angew. Chem. Int. Ed.*, e7024563. No volume/issue assigned in retrieved metadata. |
| `2026-e-cloudbind` | An electron-density point-cloud framework for robust protein-ligand interaction prediction | [Nature](https://www.nature.com/articles/s41467-026-74196-5); DOI `10.1038/s41467-026-74196-5` | 11 Jun 2026, first published; *Nat. Commun.* 17(1), 7424. |
| `2025-dynamic-reaction-path-descriptors` | Dynamic Reaction Path Descriptors: Integrating Mechanistic Insights for Enhanced AI-Driven Reaction Prediction | [ChemRxiv, version 1](https://chemrxiv.org/engage/chemrxiv/article-details/68fee1333e6156d3be3a1513); DOI `10.26434/chemrxiv-2025-w2h8c` | 6 Nov 2025, posted preprint. |
| `2025-trem2-nanovesicles` | Anti-Triggering Receptor Expressed on Myeloid Cells 2-Conjugated Nanovesicles Loaded Vadimezan Reprogram Tumor-Associated Macrophages to Combat Recurrent Lung Cancer | [ACS](https://pubs.acs.org/doi/10.1021/acsnano.5c10375); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40879116/) | 29 Aug 2025, first online; *ACS Nano* 19(36), 32674–32692. |
| `2025-cdsr-whole-slide-images` | Minimal High-Resolution Patches Are Sufficient for Whole Slide Image Representation via Cascaded Dual-Scale Reconstruction | [arXiv](https://arxiv.org/abs/2508.01641); DOI `10.48550/arXiv.2508.01641` | 3 Aug 2025, submitted preprint. |
| `2025-mogaface` | MoGaFace: Momentum-Guided and Texture-Aware Gaussian Avatars for Consistent Facial Geometry | [arXiv](https://arxiv.org/abs/2508.01218); DOI `10.48550/arXiv.2508.01218` | 2 Aug 2025, submitted preprint. |
| `2025-syncanimation` | SyncAnimation: A Real-Time End-to-End Framework for Audio-Driven Human Pose and Talking Head Animation | [IJCAI record](https://www.ijcai.org/proceedings/2025/185); [organizer BibTeX](https://www.ijcai.org/proceedings/2025/bibtex/185); DOI `10.24963/ijcai.2025/185` | Aug 2025, month precision; *IJCAI-25*, 1657–1665. |
| `2025-tautomerism-mrna-hydrogel` | Molecular tautomerism-induced formation of supramolecular hydrogel for mRNA enrichment and delivery | [Cell](https://www.cell.com/cell-biomaterials/fulltext/S3050-5623(25)00115-1); [Crossref](https://api.crossref.org/works/10.1016/j.celbio.2025.100124) | 20 Jun 2025, first online; *Cell Biomater.* 1(8), 100124. |
| `2025-ml-nanoparticle-delivery` | Machine Learning-Enhanced Nanoparticle Design for Precision Cancer Drug Delivery | [Wiley](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202503138); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40536233/) | 19 Jun 2025, first online; *Adv. Sci.* 12(30), e03138. Review article. |
| `2025-nir-ii-fluorescence-activation` | Tuning Second Near-Infrared Fluorescence Activation by Regulating the Excited-State Charge Transfer Dynamics Change Ratio | [ACS](https://pubs.acs.org/doi/10.1021/jacs.5c03763); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40331824/) | 7 May 2025, first online; *J. Am. Chem. Soc.* 147(20), 17330–17341. |

## Date and version decisions

- Use first online publication for journals where verified, not the later issue date. The Cell page's indexed publisher text says 20 June 2025; ScienceDirect assigns the final article to the issue dated 23 September 2025. Crossref confirms full authors, volume, issue and article number but supplies only September for its publication date. The record keeps the publisher's first-online date and the final issue metadata.
- Nature says first published 11 June 2026 and version of record 28 July 2026. The former is the chronological date; both belong to the same DOI and are not separate publications.
- IJCAI's downloadable BibTeX explicitly gives August 2025; its Crossref deposit gives September 2025, and neither supplies a day. Prefer the organizer's citation, retaining its August month in BibTeX. Hugo's `2025-08-01` is only a sorting anchor: `date_precision: month` makes the index show `Aug 2025` with machine-readable `2025-08`. The existing publication detail header already displays month/year. No exact publication day is claimed in the visible bibliography.
- Cite SyncAnimation once as the official conference paper, not again as arXiv `2501.14646`.
- CDSR, MoGaFace and Dynamic Reaction Path Descriptors are included as preprint versions using the existing `Working paper` taxonomy, explicit preprint venue text, a detail notice, and a BibTeX preprint note. No journal/conference version was verified for these records. Secondary reports of a later MoGaFace conference acceptance are insufficient to assign an unverified proceedings citation; reconcile with an organizer/publisher record or PI-provided citation later.
- Exclude *A Closed-Loop Hybrid Discovery System of Type I Photosensitizers for Hypoxic Tumor Therapy* (`10.1002/advs.202515103`): its [full author list](https://pubmed.ncbi.nlm.nih.gov/41386764/) does not include Shidang Xu. A related topic or citation is not authorship evidence.

No abstracts, paper PDFs or figures were copied. Detail pages link to the authoritative record for abstracts and access options. This update does not alter the homepage's two explicitly selected papers, older metadata, author profiles, Gallery, hosting configuration, or production branch. Public bibliographic records are added under the user's existing authorization in a review branch and draft PR; no merge is authorized.

## Validation and remaining work

Build, generated-HTML, baseline-preservation and existing test results are recorded in `project-state.md` after validation. Check that the new year choices contain eight and two records, all ten DOI/citation pairs match source metadata, the three preprints are distinguishable, and the month-only conference record never displays an invented day in the index.

The remaining completeness check requires a readable current SCUT/Scholar list or a Scholar BibTeX/CSV export. That limitation does not block publication of these individually verified additions. Browser layout and citation-modal interaction were not tested in this bibliography update; the existing publication maintenance checklist remains available for a later visual review.

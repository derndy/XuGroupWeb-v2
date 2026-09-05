# Contact page maintenance

Route: `/contact/`. The navigation label is **Join / Collaborate**; the existing page title remains **Contact**.

## Editing locations

| Change | Source |
| --- | --- |
| Name, email, phone, address, appointment destination | `data/contact_page.yml` → `contact` |
| Vision at the end of the page | `data/website_text.yml` → `contact.vision` |
| Opening and closing copy | `data/website_text.yml` → `contact.hero` and `contact.closing` |
| Four audience routes, preparation guidance, suggested email subjects and labels | `data/website_text.yml` → `contact.pathways` |
| Contact-detail labels and appointment-button wording | `data/website_text.yml` → `contact.information` |
| Library photograph and its factual description | `data/contact_page.yml` → `photo` |
| Page title, search summary, optional Markdown body | `content/contact/index.md` |
| Semantic structure and contact links | `layouts/landing/contact.html` |
| Four route cards and subject-prefilled email links | `layouts/partials/contact/pathways.html` |
| Contact layout and narrow-screen rules | `assets/scss/_contact.scss` |
| Approved closing artwork selection | `data/site_visuals.yml` → `join_collaborate` |
| Scientific-image approval, caption, alt text and source hash | `data/research_assets.yml` → `CONCEPT-RES-006` |

The primary contact facts were retained from the original page. They are not newly verified by this layout change. Get PI confirmation before changing a factual value. Keep the phone as a quoted string so its displayed form is not altered by YAML parsing. Email and phone links are generated from those same displayed values.

The appointment link retains `https://calendly.com/xushidang` and uses the current tab. It has not been checked for live appointment availability.

The existing 420 × 280 library photograph remains at its original public path and preserves its bytes. The template reads its actual dimensions. The stylesheet preserves its full aspect ratio and caps its displayed width at 420 CSS pixels under the default font size. Do not crop it or replace it with conceptual artwork.

The closing illustration retains its approved placement, caption, alternative text, visible conceptual/AI-generated label and original PNG download. Route any scientific-asset changes through the existing approval rules.

## Four contact pathways

The original pathway batch began at v2 `main` commit `b9ad9189828d76da1fb0cc634169528026bdc78c`, after PR #4 merged. These are sections on the existing `/contact/` route, with stable anchors; they are not new page bundles.

| Audience | Stable destination | Suggested email subject |
| --- | --- | --- |
| Scientific collaborator | `/contact/#scientific-collaboration` | `Xu Lab \| Scientific collaboration` |
| Experimental / testbed partner | `/contact/#experimental-partnership` | `Xu Lab \| Experimental partnership` |
| Prospective student / researcher | `/contact/#join-the-lab` | `Xu Lab \| Prospective researcher` |
| Paper / research-resource user | `/contact/#research-asset-use` | `Xu Lab \| Research asset enquiry` |

Each card explains the suitable question, what the visitor can contribute, three useful items for a first email, a possible next step, and a related existing page. The introduction offers direct links to all four cards and the primary contact details. Cards appear in two columns on desktop and one column below 62rem. Content remains visible without JavaScript; native anchors, focusable fragment targets and email links require no form or service.

The four pathways' visible wording and labels live in `data/website_text.yml` → `contact.pathways`, alongside the vision at `contact.vision`. Keep IDs stable when changing wording, because other pages can link directly to them. Keep the related URLs pointed at actual public pages. Changing a card's label or subject does not require editing its template. The template combines this copy with the separate contact facts; email recipients still come only from `data/contact_page.yml` → `contact.email`.

The email recipient is derived from the same `contact.email` field as the displayed primary address. Only the subject is prefilled; it is URL-encoded with percent-encoded spaces. No message is sent by the page, and no body, attachment or visitor data is transmitted to the lab until the visitor chooses to send an email through their own client. Email subjects are newly suggested conventions for this draft, not a claim of an existing mandatory application policy or verified inbox automation.

The applicant route requests a short introduction/CV, research interest and a shareable work sample. It asks visitors to enquire about current openings, funding and application timing; this draft does not advertise a confirmed funded vacancy or admission guarantee. Next steps are conditional, with no promised response time. The research-resource route points to actual publication records and makes access/reuse dependent on the particular resource and its terms. It does not imply that unlisted code, datasets or protocols are available.

No lab handbook, internal management rules, private project material or new institutional contact fact is introduced. Homepage text and the ten other main pages are outside this batch's product scope.

## Validation of the pathway batch

The completed results and hosted draft preview, when available, are recorded in `project-state.md`. Check both Hugo build contexts, publication/citation preservation, the six-image audit and internal links across the eleven main pages. On Contact, verify the five jump destinations, four distinct mailto subjects/recipient, four related-page URLs and complete preparation/next-step copy. The pre-existing contact details, appointment link, photo and closing artwork should remain byte-for-byte equivalent in generated HTML.

Real browser layout, keyboard/touch, zoom and email-client behaviour need separate review. Build success and valid mailto encoding do not demonstrate a working installed mail client or appointment availability.

## Previous Contact-layout validation — 5 September 2026

- Hugo Extended 0.139.4 production and preview-equivalent builds: 736 pages each.
- Six scientific-image placements, six approved originals and 24 uncropped WebP variants pass the existing audit on both builds.
- All 78 publication records and citation bytes match the pre-Contact baseline.
- Nine publication JavaScript tests and three DOI regression tests pass.
- Eleven main surfaces have one H1, one main landmark and unique authored IDs. All 1,002 authored internal links/fragments tested within those main surfaces resolve.
- The other ten main-content HTML trees match the pre-Contact baseline, including attributes and text.
- Contact name, email, phone, address, appointment destination and library photograph match the previous page. Email and phone now have matching `mailto:`/`tel:` links.
- Contact has a page-specific search description, no inline stylesheet, real photograph dimensions and visible keyboard-focus styles.
- Preview-only `noindex` is present on all eleven checked preview surfaces and absent on the corresponding production-build pages.

These checks inspect generated files and link markup. Browser layout, keyboard interaction, phone/email client launch and live external appointment availability still require review.

## Vision at the end of Join / Collaborate

The PI requested removing the full Vision chapter from the homepage to reduce its length and moving it to the end of this page. Render `site.Data.website_text.contact.vision` after the approved illustration section, immediately before the end of the main content. Its anchor is `/contact/#contact-vision-title`. All wording and the existing responsive arrangement are preserved; only placement, the data path and scoped class names change. The homepage has no duplicate version. Vision styles are in `_contact.scss` alongside this page's existing styles. The four pathways, contact information, photograph and approved illustration retain their content and order.

## Method-led postdoctoral invitation — 5 September 2026

The hero now explicitly welcomes postdoctoral researchers, PhD candidates, academic collaborators and industry partners. The joining route invites proposals whose main contribution is a new method or model architecture, connected to a scientific question. Its optional `research_space_label` and `research_space` fields render one extra definition-list entry only on that route. Other cards keep their existing structure.

The next conversation may explore a proposed direction, potential group collaborators, and the data/experimental/computational support it would need. This is an invitation to discuss fit, not a promise that a particular facility, dataset, funded position or independent group already exists. The existing instruction to ask about openings, funding and timing remains. Contact facts, email subjects, links, documentary photograph, approved image and complete closing Vision are unchanged. See [the bounded copy review](research-copy-and-selected-work-2026-09-05.md).

## Text-source migration — follow-up in PR #15

Moved the exact hero, four pathways and closing copy from `data/contact_page.yml` into `data/website_text.yml` under `contact`. Added `contact.information` for the existing contact-detail labels and appointment-button label. No public wording, IDs, links, subjects or layout changed. The complete Vision remains at the end, under its existing `contact.vision` key. Contact facts and the documentary photograph retain their original file; page title/search summary retain their content bundle.

Both Hugo contexts pass (885 pages). All eleven main-page HTML files are byte-identical to the preceding PR #15 build in each context. Exact YAML comparisons preserve every moved value, contact fact, photo record, Vision and other website-text entry. A temporary one-file change to the joining route's research-space label appeared on Contact only and was then restored. The existing publication and approved-image audits pass. Browser testing is not part of this source-only migration.

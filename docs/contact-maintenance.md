# Contact page maintenance

Route: `/contact/`. The navigation label is **Join / Collaborate**; the existing page title remains **Contact**.

## Editing locations

| Change | Source |
| --- | --- |
| Name, email, phone, address, appointment destination | `data/contact_page.yml` → `contact` |
| Opening and closing copy | `data/contact_page.yml` → `hero` and `closing` |
| Library photograph and its factual description | `data/contact_page.yml` → `photo` |
| Page title, search summary, optional Markdown body | `content/contact/index.md` |
| Semantic structure and contact links | `layouts/landing/contact.html` |
| Contact layout and narrow-screen rules | `assets/scss/_contact.scss` |
| Approved closing artwork selection | `data/site_visuals.yml` → `join_collaborate` |
| Scientific-image approval, caption, alt text and source hash | `data/research_assets.yml` → `CONCEPT-RES-006` |

The primary contact facts were retained from the original page. They are not newly verified by this layout change. Get PI confirmation before changing a factual value. Keep the phone as a quoted string so its displayed form is not altered by YAML parsing. Email and phone links are generated from those same displayed values.

The appointment link retains `https://calendly.com/xushidang` and uses the current tab. It has not been checked for live appointment availability.

The existing 420 × 280 library photograph remains at its original public path and preserves its bytes. The template reads its actual dimensions. The stylesheet preserves its full aspect ratio and caps its displayed width at 420 CSS pixels under the default font size. Do not crop it or replace it with conceptual artwork.

The closing illustration retains its approved placement, caption, alternative text, visible conceptual/AI-generated label and original PNG download. Route any scientific-asset changes through the existing approval rules.

## Validation recorded on 5 September 2026

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

# Edit website text / 网站文字修改指南

Start with **[`data/website_text.yml`](../data/website_text.yml)**. The homepage and its shared explanations read from this file. The latest copy is written for postdoctoral/PhD researchers, industry partners and research peers. The remaining pages will move in later batches.

## Make a text change in GitHub

1. Open `data/website_text.yml` on your review branch（审核分支）. After this change is merged, the file will also be on `main`（主分支）.
2. Click the pencil to edit. Find the field using the table below.
3. Replace its wording, preserving the field name, indentation（缩进）and quotation marks. Long paragraphs use `>-`; edit the indented lines beneath it. Use spaces, not tabs.
4. Save the change to the review branch or a new branch and open a PR（合并请求）.
5. Wait for the Netlify preview（预览）to pass. Open the homepage and any shared pages affected by the edit. Check both narrow and wide screens if text length changes substantially.
6. Merge（合并）when the wording and layout are ready. Netlify publishes after the production-branch build succeeds, provided automatic deployment（自动部署）is enabled for that branch.

A branch save updates its preview after a successful build. It does not itself merge the change into `main`.

## Find the right field

| Text to change | Location in `website_text.yml` | Where it appears |
| --- | --- | --- |
| Main title, subtitle and tagline | `home.hero.title`, `home.hero.subtitle`, `home.hero.tagline` | Homepage hero |
| Hero recruitment/industry buttons | `home.hero.primary_link` / `primary_url` and `secondary_link` / `secondary_url` | Postdocs/PhD enquiry and scientific collaboration sections on Contact |
| Hero diagram headings and instructions | `home.map` | Homepage diagram |
| Research ambition | `home.thesis` | Homepage section 01 |
| Space–Interaction–Learning framing | `home.grammar` | Homepage section 02 |
| Space, Interaction, Learning, Evidence, Mechanism and Design definitions | `shared.grammar` | Homepage; the shared dimensions/evidence/feedback also feed About |
| Three-pillar section heading and button labels | `home.pillars` | Homepage section 03 |
| Each pillar's formal title, role, question, homepage invitation and terms | `shared.pillars.pillar-i`, `pillar-ii`, `pillar-iii` | Homepage; formal titles/roles/questions are also read by Research and pillar pages wherever used |
| Evidence-loop headings and labels | `home.evidence_loop` | Homepage section 04 |
| Six evidence-loop steps and explanations | `shared.evidence_loop` | Homepage evidence loop |
| Four application/opportunity cards | `home.testbeds` | Homepage section 05 |
| Publication and citation section wording | `home.publications` | Homepage section 06 |
| People and culture section wording | `home.people` | Homepage section 07 |
| Shared team introduction | `shared.people_introduction` | Homepage and People page |
| News heading, fallback category and link label | `home.news` | Homepage section 08 |
| Closing invitation and buttons | `home.join` | Homepage section 09 |

Changing a `shared` entry changes every connected use of that entry. This avoids maintaining a second copy. It does not rename separate page titles or rewrite independent paragraphs elsewhere.

### Example: title and subtitle

```yaml
home:
  hero:
    title: "AI for Science. Discovery Beyond Prediction."
    subtitle: >-
      We bring together artificial intelligence, molecular science and experimental insight to advance drug
      discovery, biotechnology and advanced materials.
```

`>-` joins the indented lines into one paragraph. To use a double quotation mark inside a quoted value, write `\"`; alternatively use a `>-` paragraph. Text is rendered as plain text: HTML tags such as `<em>` will appear literally. Keep `id`, `url` and `pillars` reference fields unchanged during wording edits because they connect definitions to sections and research pages.

## Records that retain their own files

| Item | Editing location |
| --- | --- |
| Individual publications, authors, venues, DOI links and citations | `content/publication/` |
| Homepage paper selection | `data/homepage.yml` (ordered page references) |
| Individual news posts and event dates | `content/post/` |
| Individual member profiles | `content/person/` |
| Undergraduate and alumni register | `data/US_Alumni.yml` |
| Documentary photograph, alt text and approved caption | `data/people_page.yml` → `photos.featured` |
| Scientific illustrations and approved captions | Existing `data/research_assets.yml` and `data/site_visuals.yml` records; follow the visual approval guide |

Page-level text for About, Contact, other Research sections, People, News and Gallery has not been fully moved yet. Global navigation/footer wording and homepage browser-tab/search metadata (`content/_index.md`) retain their existing sources. This first batch does not add an in-browser editor.

## How the connection works

Hugo templates（页面模板）read `site.Data.website_text.home` or `site.Data.website_text.shared`. The shared pillar helper, `layouts/partials/research/pillars.html`, combines the five editable display fields with the original IDs, routes and detailed research records. All pillar consumers use that helper; it fails the build if required shared pillar copy is missing. Grammar, evidence-loop and team-introduction consumers read their new shared entries directly.

Publications and news still resolve actual content records at build time. Draft/future news gates, publication selection checks, image approval records, CSS（样式表）and JavaScript（交互脚本）are unchanged. Hero and closing buttons now read their labels and destinations from this file. Both recruitment buttons reach `/contact/#join-the-lab`; both industry buttons reach `/contact/#scientific-collaboration`. Other research links remain available in the following sections.

For future text moves, build a baseline first, connect each moved entry, compare generated pages, and try a temporary edit from the new source before restoring the approved wording. The original text-source migration verified byte-identical HTML for all eleven main pages and a real one-file edit across homepage/shared consumers. Editorial changes intentionally change rendered wording and need a check of text, links and any affected shared pages. Longer wording still needs its own layout review.

## Public writing direction — 5 September 2026

The PI now positions the website as an external window for recruitment, industry collaboration and research visibility. This instruction supersedes the earlier requirement to freeze the original homepage headline, subtitle and tagline.

- Lead with recognisable fields: AI for Science, AI for Biomedicine, scientific foundation models, multimodal learning, generative design and trustworthy AI. Present these as research interests and questions; do not imply a released platform or a proven commercial service.
- Make relevance visible to biotechnology, pharmaceutical and materials R&D teams: complex data, candidate design, experiment planning and scientific decisions.
- Speak directly to postdoctoral and PhD researchers about original ideas, crossing disciplines and shaping a research direction. Enquiries do not imply a confirmed funded vacancy.
- Retain scientific substance through broad questions about learning, molecular relationships, generalisation, evidence and reliable decisions. Avoid detailed unpublished project designs, implementation choices or research timetables in promotional copy.
- Keep public pages in English. Shared entries affect About, Research, pillar pages and People, but independent paragraphs, detailed roadmaps, metadata and repository history are outside this file's coverage.

The three public pillar titles are now **Scientific AI & Multimodal Learning**, **Generative Design & AI-Guided Discovery**, and **Trustworthy AI & Mathematical Discovery**. Their stable IDs, routes and existing scientific responsibilities remain. This is a public-language update, not a change to the underlying research programme.

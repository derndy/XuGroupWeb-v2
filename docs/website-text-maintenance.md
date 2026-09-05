# Edit website text / 网站文字修改指南

Start with **[`data/website_text.yml`](../data/website_text.yml)**. Phase 1 connects the homepage's own wording and the shared explanations it uses. Existing wording and page layout are preserved. The remaining pages will move in later batches.

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
| Hero diagram headings and instructions | `home.map` | Homepage diagram |
| Beyond Prediction | `home.thesis` | Homepage section 01 |
| Space–Interaction–Learning framing | `home.grammar` | Homepage section 02 |
| Space, Interaction, Learning, Evidence, Mechanism and Design definitions | `shared.grammar` | Homepage; the shared dimensions/evidence/feedback also feed About |
| Three-pillar section heading and button labels | `home.pillars` | Homepage section 03 |
| Each pillar's formal title, role, question, homepage invitation and terms | `shared.pillars.pillar-i`, `pillar-ii`, `pillar-iii` | Homepage; formal titles/roles/questions are also read by Research and pillar pages wherever used |
| Evidence-loop headings and labels | `home.evidence_loop` | Homepage section 04 |
| Six evidence-loop steps and explanations | `shared.evidence_loop` | Homepage evidence loop |
| Four scientific testbed cards | `home.testbeds` | Homepage section 05 |
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
    title: "Designing Scientific Learning and Discovery Systems"
    subtitle: >-
      We design how scientific systems represent information, organize interactions, learn from evidence,
      and generate new knowledge and designs.
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

Publications and news still resolve actual content records at build time. Draft/future news gates, publication selection checks, URLs, image approval records, CSS（样式表）and JavaScript（交互脚本）are unchanged.

For future text moves, build a baseline first, connect each moved entry, compare generated pages, and try a temporary edit from the new source before restoring the approved wording. This batch verifies byte-identical HTML for all eleven main pages and a real one-file edit across homepage/shared consumers. Longer future wording still needs its own layout review.

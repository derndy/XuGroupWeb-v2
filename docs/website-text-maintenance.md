# Edit website text / 网站文字修改指南

Start with **[`data/website_text.yml`](../data/website_text.yml)**. Phase 1 connects the homepage's own wording and the shared explanations it uses. The original migration preserved all wording and layout; subsequent restrained edits preserve that identity. The vision lives at `contact.vision` and appears only at the end of Join / Collaborate. The current batch clarifies methods versus testbeds, selects five papers and improves research invitations; [its review](research-copy-and-selected-work-2026-09-05.md) records the scope and meaningful choices. The remaining pages will move in later batches.

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
| Lab vision, scientific foresight and domain intelligence system architects | `contact.vision` | Last chapter on Join / Collaborate (`/contact/#contact-vision-title`) |
| Space–Interaction–Learning framing | `home.grammar` | Homepage section 02 |
| Space, Interaction, Learning, Evidence, Mechanism and Design definitions | `shared.grammar` | Homepage; the shared dimensions/evidence/feedback also feed About |
| Three-pillar section heading and button labels | `home.pillars` | Homepage section 03 |
| Each pillar's formal title, role, question, homepage invitation and terms | `shared.pillars.pillar-i`, `pillar-ii`, `pillar-iii` | Homepage; formal titles/roles/questions are also read by Research and pillar pages wherever used |
| Evidence-loop headings and labels | `home.evidence_loop` | Homepage section 04 |
| Six evidence-loop steps and explanations | `shared.evidence_loop` | Homepage evidence loop |
| Four scientific testbed cards | `home.testbeds` | Homepage section 05 |
| Publication and citation section wording | `home.publications` | Homepage section 06 |
| Five paper-specific research focus labels | `home.publications.focus` | Under each selected paper title; keys are connected in `data/homepage.yml` |
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
| Homepage paper selection | `data/homepage.yml` (ordered `page` references and `focus` label keys) |
| Individual news posts and event dates | `content/post/` |
| Individual member profiles | `content/person/` |
| Undergraduate and alumni register | `data/US_Alumni.yml` |
| Documentary photograph, alt text and approved caption | `data/people_page.yml` → `photos.featured` |
| Scientific illustrations and approved captions | Existing `data/research_assets.yml` and `data/site_visuals.yml` records; follow the visual approval guide |

Page-level text for About, Contact, other Research sections, People, News and Gallery has not been fully moved yet. Detailed pillar copy and the shared NOW/NEXT/HORIZON statements remain in `data/research_system.yml`; the NOW wording also appears on About. The postdoctoral invitation and pathway copy remain in `data/contact_page.yml`. Some Research section labels remain in its templates. Global navigation/footer wording and homepage browser-tab/search metadata (`content/_index.md`) retain their existing sources. No in-browser editor is added.

## How the connection works

Hugo templates（页面模板）read `site.Data.website_text.home` or `site.Data.website_text.shared`. The shared pillar helper, `layouts/partials/research/pillars.html`, combines the five editable display fields with the original IDs, routes and detailed research records. All pillar consumers use that helper; it fails the build if required shared pillar copy is missing. Grammar, evidence-loop and team-introduction consumers read their new shared entries directly.

Publications and news still resolve actual content records at build time. The five-paper update extends publication eligibility to accepted conference papers, reuses acceptance validation and moves citations to inline actions. Draft/future news gates, canonical URLs, image approval records and JavaScript（交互脚本）are unchanged.

For future text moves, build a baseline first, connect each moved entry, compare generated pages, and try a temporary edit from the new source before restoring the approved wording. The original migration verified byte-identical HTML for all eleven main pages and a real one-file edit across homepage/shared consumers. Subsequent wording changes and additions need their own checks.

## Current editorial direction — restrained refinement

The PI rejected the broad public-marketing rewrite in PR #11 as too generic. That draft was closed without merging. Start from the original text in merged PR #9, preserving the exact hero title/subtitle/tagline, formal three-pillar names, research questions and Space–Interaction–Learning framework. Add accessible context rather than replacing the lab's identity. Do not treat the withdrawn PR as approved wording.

For every batch, explicitly report substantial layout/meaning changes and any uncertain editorial choices to the PI. The previous relocation changed placement only. The current copy batch removes public-facing management language without changing the backend image/record validation. It welcomes method-led postdoctoral proposals without promising funded vacancies, independence arrangements or resources that have not been confirmed.

The preceding wording revision changed only six existing YAML values:

| Field | Scope of the edit |
| --- | --- |
| `home.thesis.paragraph_two` | Retain the original sentence; append one connection to AI for Science, scientific foundation models and generative design |
| `home.testbeds.title` | Replace “Consequential” with “Real-world” |
| `home.testbeds.introduction` | Simplify the opening sentence about applications connecting the research |
| `shared.grammar.dimensions` → `learning.definition` | Use learning goals, feedback and constraints; omit the detailed list of guiding signals/update rules |
| `shared.grammar.aims` → `mechanism.link_text` | Explain the link in terms of what evidence can establish |
| `shared.evidence_loop.steps` → `learn.explanation` | Use “Revise the learning system” instead of enumerating internal choices |

The established research terminology remains elsewhere, including Identifiability and the formal pillar titles. The two learning edits reduce operational specificity; this is not a whole-site confidentiality audit. Do not add unpublished targets, architectures, protocols or project timelines during future copy edits.

All added vision text is under `contact.vision`. It was moved from the homepage to the end of `/contact/` without changing any wording. Keep this as the single editable source; do not add a second homepage copy. The English adaptation retains scientific foresight, conditional decades/centuries horizons, evidence and revision, explicit assumptions, and intellectual leadership. Domain intelligence system architects are **one training path**, spanning model architecture, infrastructure, scientific and intelligent systems, objective functions, search spaces and evaluation criteria. Energy-efficient intelligence is an illustrative open question, not a declared project or achieved result. The horizon remains open to problems and methods that have not yet emerged.

The limited contemporary vocabulary is context, not a claim that the lab has released a foundation model or generative-design platform. Recent terminology was checked against primary research, including [AlloyGPT](https://www.nature.com/articles/s41524-025-01768-2) and [MetaFO](https://www.nature.com/articles/s41524-025-01925-7); these are external examples, not lab publications or endorsements.

### PI-supplied vision — source for the English adaptation

**理解世界，开拓未来**

我们的目标是加深对世界的理解，发现那些重要性正在显现的问题，并培养能够引领所在领域未来发展的研究者。

我们重视科学远见：识别变化的早期信号，联系不同领域的发展，看清现象背后的结构，并审视那些限制我们思考的假设。我们的视野涵盖未来数十年的变化，也在有意义的情况下延伸至数百年的尺度。我们追问：未来哪些问题与约束将变得重要？什么样的知识能够开辟新的方向？

我们以证据为基础，不断接近真实与真理，并始终愿意修正自己的认识。关于未来的判断应当讲清其假设，并落到当下可以研究的问题上。思想引领力来自有价值的问题和扎实的理解。

其中一条培养路径，是培养领域智能系统架构师，涵盖模型架构、基础设施，以及科学系统与智能系统的设计。他们围绕值得研究的问题，定义目标函数、搜索空间与评价标准。例如，追问单位能耗能够产生多少有效智能，即如何提升智能能耗比，就可能打开一个新的研究方向。我们的愿景也为尚未出现的重要问题和研究方法保留空间。

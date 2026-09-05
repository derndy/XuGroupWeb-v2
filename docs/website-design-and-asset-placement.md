> Repository edition: preserves the supplied design brief and approved image register. Private Library retrieval identifiers in Appendix B and individual image records are omitted. The unchanged attachment remains the source reference. Historical branch/PR notes below describe earlier work; read [project-state.md](../project-state.md) for live implementation status. This file is development guidance, not a public website page.

# Xu Lab — Website Design & Asset Placement Brief

**课题组网站设计方案与已有素材安置说明**
**Version:** 1.0 · 5 September 2026
**Source attachment SHA-256:** `186652c994c09458ed8dade1e250d4d8e195086130d7387648ca4fd16b02474e`

**Purpose:** A self-contained design contract（设计约定）for a new GPT conversation to implement the planned website, especially the correct reuse and placement of existing materials and images.

This file preserves the two detailed website-design responses supplied in the current conversation, together with the saved six-image approval record. It covers the entire lab website, with the homepage as the principal composition. It is a design specification（设计规范）, not a claim that every page has been built or released.

**The image originals are linked in Appendix A; their pixels are not embedded in this Markdown file.** A new GPT conversation with access to those files can retrieve them directly. If access is unavailable, attach the six original PNGs listed there. Do not regenerate substitute artwork simply because it is absent from the new conversation.

## 1. Start here: authority and decisions

### How the next GPT should use this file

1. Read this entire brief, particularly Sections 5–6 and Appendix A, before building pages.
2. Read the latest project-state file and inspect the actual repository（代码仓库）to learn what already exists. This brief controls intended design; live files establish implementation state.
3. Match existing assets by exact title, source identity and, for the six approved PNGs, SHA-256（文件校验值）. Record the mapping before integrating images.
4. Reuse completed work and implement in small, reviewable batches. Quality takes priority over completing every page at once.
5. Produce a working preview（预览）and list the pages/assets completed and still missing. Respect the current session's publication instructions; this file alone is not an instruction to merge or change production（正式网站）.

### Resolved differences across earlier drafts

| Topic | Instruction for implementation |
|---|---|
| Homepage title, subtitle and tagline | Preserve the user's exact three statements in Section 2. Earlier assistant-proposed alternatives remain supporting-copy options; they do not silently replace these statements. |
| Three research pillars（研究板块） | Use learner design, evidence engineering, and mathematical/frontier exploration. Applications remain cross-pillar testbeds（跨板块科学试验场景）. |
| Space–Interaction–Learning | These are connected design dimensions, especially within Pillar I and the wider system. Do not equate Space=Pillar I, Interaction=Pillar II, Learning=Pillar III. |
| Brand and “Beyond Prediction” | XU LAB is the working website identity. “Beyond Prediction” is the planned intellectual hook（思想切入点）, not a new lab name or a proven-results claim. |
| Image approvals | The saved approval record explicitly approves all six images as shown, their placements and captions. An older project-state snapshot records only image 01 in code. Reconcile the code record with the existing six-image approval; do not ask the PI to repeat an already documented approval for unchanged files and placements. |
| Mobile image treatment | Preserve the approved composition by default. Use an uncropped responsive image before considering an alternate crop. Never remove meaningful structure to fill a mobile frame. |
| Framework | The saved implementation handoff identifies Hugo Blox. Continue that system if the current repository confirms it. The earlier Astro proposal was conditional, not an instruction to rebuild completed work. |
| Preview and privacy | `noindex` reduces search indexing; it does not restrict access. Confidential material must stay out of publicly accessible branches, builds and previews. |

If a genuine conflict remains, identify the exact statement or asset affected and continue unaffected work. Do not treat every historical difference as a reason to stop the whole task.

### Stable design decisions

- A light, editorial（编辑型）, geometric（几何型）, evidence-forward（证据导向）website.
- A browsable research argument（可浏览的研究论证）with attractive entry points and inspectable scientific support.
- One connected scientific system, with three distinct contributions.
- Text introduces the scientific proposition before the principal explanatory image.
- The homepage Hero（首屏主视觉区）uses a meaningful SVG/HTML system diagram, not a generated PNG.
- At most one large cinematic conceptual image（电影感概念图）per major page; precise diagrams and real photographs have separate roles.
- Projects connect research questions, evidence, publications, resources and people.
- English is primary. Chinese pages follow the same structure separately, rather than sentence-by-sentence bilingual text on the public English pages.
- No full dark-mode toggle in Version 1; selected navy sections provide contrast.
- Existing facts, routes and authentic photographs are preserved unless an authorized content correction is supported.

## 2. Identity, language and research structure

### Exact homepage statements

**H1 — preserve verbatim:**

> Designing Scientific Learning and Discovery Systems

**Subtitle — preserve verbatim:**

> We design how scientific systems represent information, organize interactions, learn from evidence, and generate new knowledge and designs.

**Tagline — preserve verbatim:**

> Learn better. Create better evidence. Discover deeper. Design forward.

| Role | Website text |
|---|---|
| Header identity | XU LAB |
| Programme line | Scientific Learning & Discovery Systems |
| Browser/search title | Xu Lab \| Scientific Learning & Discovery Systems |
| Eyebrow（标题上方短引导语） | Scientific Learning · Evidence Engineering · Mathematical Data Science |
| Primary CTA（行动按钮） | Explore our research |
| Secondary CTA | Projects & Evidence; use a truthful live destination, such as Scientific testbeds, if Projects is not ready |

The planned supporting hook is **Beyond prediction: discovering testable molecular mechanisms and hidden principles.** Position it after the Hero or within the next statement section. Present it as a research aim. Do not narrow the whole website to molecular mechanisms alone, and do not imply that hidden principles have already been established.

Longer supporting copy available from the design discussion:

> We design the spaces, interactions, learning dynamics, and evidence loops of scientific intelligence—and develop the mathematics that turns complex data into identifiable mechanisms, decisive experiments, and useful designs.

Use this on Research/About where depth is useful; avoid stacking multiple near-identical introductory paragraphs in the Hero.

### Three pillars: short labels, formal names and contributions

| Pillar | Navigation label | Formal research title | Core question | Main scope |
|---|---|---|---|---|
| I | Scientific Learning | Foundational Scientific Learning-System Design | How should a scientific system learn? | Representation spaces（表示空间）, interaction structures（交互结构）, guiding signals（引导信号）, learning dynamics（学习动力学）, primitives（基本单元）, operators（算子）and dictionaries |
| II | Evidence Engineering | Evidence Engineering and Closed-Loop Discovery & Design | What evidence should the system create and acquire? | Evidence quality, data factories, perturbations（扰动）, experimental design, active acquisition（主动获取）, candidate design, feedback |
| III | Mathematical Frontiers | Mathematical Data Science and Frontier Exploration | What becomes identifiable, testable and designable at the frontier? | Identifiability（可辨识性）, uncertainty（不确定性）, causal reasoning（因果推理）, statistical inference（统计推断）, computation, inverse and generative design（逆向与生成设计） |

The Research page should make the different roles visible: Pillar I designs the learner; Pillar II creates and selects evidence around it; Pillar III supplies mathematical questions, limits and new possibilities. Their relationship is reciprocal（相互作用的）, not a maturity ranking or a rigid one-way sequence.

Materials, drug delivery, molecular interactions, proteins, peptides and sequences are **scientific testbeds**, not a fourth pillar and not a replacement for Pillar III.

The website should support three reading depths:

| Time available | Visitor takeaway |
|---|---|
| 10–20 seconds | What the lab is trying to change |
| 1–2 minutes | How learning, evidence and mathematics form one system |
| 5–10 minutes | Which projects, evidence and outputs support the programme |

## 3. Navigation and page map

| Main navigation | Destinations |
|---|---|
| Research | Overview; Scientific Learning; Evidence Engineering; Mathematical Frontiers |
| Projects | Project index; project details |
| Outputs | Publications; Resources |
| People | PI; current members; collaborators; alumni |
| Updates | News; Gallery |
| About | Vision; principles; research culture; roadmap |
| Join / Collaborate | Collaborators; testbed partners; applicants; research-asset users |

Target routes are listed below. They express design intent, not a command to rename established URLs. Preserve existing routes or provide a verified redirect（重定向）when mapping to the current Hugo site.

| Page | Intended route |
|---|---|
| Home | `/` |
| Research overview | `/research` |
| Pillar I | `/research/scientific-learning` |
| Pillar II | `/research/evidence-engineering` |
| Pillar III | `/research/mathematical-frontiers` |
| Projects and details | `/projects`; `/projects/[project-slug]` |
| Publications | `/publications` and existing publication detail URLs |
| Resources and details | `/resources`; `/resources/[resource-slug]` |
| People and profiles | `/people`; existing individual profile URLs |
| News and articles | `/news`; existing article URLs |
| Gallery | `/gallery` |
| About / Vision | `/about` |
| Join / Collaborate | `/join` |
| Supporting pages | `/accessibility`; `/privacy`; real 404 handling |

Initial bilingual scope: Home, Research, About and Join. News, Publications and Gallery may remain English first. Do not show a language switch leading to missing pages.

Header: white surface, thin lower border, clear active page indication, sticky on scroll, and one filled Join / Collaborate button. Recruitment can receive a quiet static “Open positions” marker only when that status is current. Use no flashing marker, heavy shadow or glass effect.

## 4. Homepage: section-by-section composition

The intended sequence contains 11 sections. Empty evidence-dependent sections may be omitted; do not fill them with invented claims. Related short sections can share a visual band without losing their reading order.

### H01 — Hero: identity before imagery

- **Job:** Establish the lab's scientific mission immediately.
- **Desktop:** A 12-column layout, approximately seven columns of text and five of precise system diagram. Let the heading determine height; avoid a forced full-screen panel.
- **Text order:** Eyebrow → exact H1 → exact subtitle → two CTAs → tagline.
- **Visual:** Responsive SVG/HTML（响应式矢量图／网页结构）with Space, Interaction, Learning, Evidence, Mechanism and Design. Mechanism/design are research aims or outputs, not automatic claims of causal discovery.
- **Interaction:** Hover or keyboard focus highlights named relationships. Activation opens a brief definition and relevant research link. Touch users receive the same information. Keep visible labels and a text equivalent.
- **Motion:** A short, one-time entrance may introduce paths; no continuous rotation. Respect reduced-motion preferences.
- **Mobile:** All essential text and CTAs precede the diagram. Keep the tagline readable instead of forcing it into one line.
- **Do not place here:** Any of the six approved cinematic PNGs, a carousel, a group-photo banner, or a CV block.

### H02 — Beyond Prediction: the memorable proposition

Use a quiet, spacious statement section.

> Prediction asks what may happen. Scientific discovery asks what structure, interaction or mechanism makes it happen—and what evidence would distinguish that explanation from alternatives.

Follow with three short ideas: **Learn the right scientific structure**; **Generate decisive evidence**; **Turn patterns into principles and possibilities**. The tone is inviting and intellectually clear. Detailed qualifications belong on the deeper research/project pages.

### H03 — Space · Interaction · Learning: explain the scientific grammar

Introduce the map with **Scientific intelligence is a designed system.** Explain the thesis before displaying the larger map.

| Dimension | Question to display |
|---|---|
| Space | What distinctions should the representation preserve? |
| Interaction | Which relationships should the system expose? |
| Learning | What update process turns evidence into reusable knowledge? |

The Hero is the compact orientation; this section adds explanations and feedback relationships. Do not show the same large diagram twice. Reuse one component/data source with a compact Hero variant and an expanded explanatory variant. A simple reading sequence can help orientation, but the complete view must retain feedback and joint design.

### H04 — Three Contributions, One System

Three connected cards use blue, teal and amber. A shared baseline or subtle connecting line shows membership in one system. Each card contains pillar number, short public title, formal title, core question, three capability keywords and a specific Explore link.

| Pillar | Public-facing invitation |
|---|---|
| I | Learn the right scientific structure |
| II | Create evidence that changes what can be learned |
| III | Turn patterns into principles and possibilities |

Keep cards short. Move long capability lists and output explanations to the pillar pages. The Research page expands their asymmetric（角色不对称的）relationship beyond these accessible entry cards.

### H05 — Closed Evidence Loop

Use a pale teal section with a precise diagram: **Observe → Question → Design evidence → Learn → Test → Explain or design**, with a clear return path. The sequence is a reading aid, not a claim that every project follows one fixed workflow.

Solid arrows describe primary information/evidence movement; dashed return paths describe feedback, revised questions or changed constraints. Selecting a step can reveal the contributing pillar, a typical artifact（研究产物）and an example question. Render steps vertically on mobile. Do not substitute the Evidence Spiral PNG for this functional explanation.

### H06 — Selected Research

Display at most three eligible projects. Each answers: What is the problem? What does the work change? What evidence exists? What can the visitor inspect?

Cards include name, scientific question, contribution, pillar/testbed tags, readable status, available output, members and review date. Keep internal approval operations out of the visitor flow. If no projects are approved for publication, omit this section and route visitors to verified research descriptions and publications.

### H07 — Scientific Testbeds: the homepage's only cinematic image

**Assigned asset: 05 — From Testbeds to Discovery Horizons.**

Order: section heading → short explanation → large approved image → approved caption → four compact testbed cards. A side-by-side heading/text introduction is acceptable on desktop; text stays outside the detailed artwork.

Suggested heading: **Scientific testbeds where learning and evidence meet.**

Testbed cards: molecular interactions and drug discovery; biomaterials and delivery systems; proteins, peptides and sequences; complex scientific data and mechanisms. Explain the scientific difficulty of each and connect it to relevant research/projects. Use present-tense capability claims only when supported; otherwise describe the research question.

Use a light full-width chapter, bounded by the content grid. Keep the artwork large and uncropped by default; it is not a tiny card thumbnail or a background texture. No text overlay. Do not reuse asset 05 as the Hero.

### H08 — Publications and Reusable Research Assets

Two columns on desktop; stacked sections on mobile. Feature a small number of verified papers and available datasets, code, protocols or benchmarks（基准）. Connect to a related project when that public project exists. Publications remain useful and accessible even when no public project record is ready.

Avoid citation counters, invented download counts or empty resource cards. Bibliographic（文献）records should look like readable references; resources should make the action—view, download, open repository or request access—clear.

### H09 — People and Culture

Use one authentic lab photograph, a short PI research-programme statement, and optionally 3–6 member cards. Link to People and Gallery. Choose an approved, current photograph; preserve natural colour and provide event/date context. The full PI biography does not belong in the homepage's upper half.

### H10 — Latest News

Three recent, verified items, in date order, without a carousel. Show date, category and a short headline. Useful categories include publications, talks/awards, releases and lab/member updates. Do not fabricate recent activity to fill the section.

### H11 — Join / Collaborate

Navy closing section with a concise invitation:

> Bring a difficult scientific question, an experimental testbed, or an idea worth stress-testing.

Provide routes for scientific collaboration, testbed partnership, joining the lab and research-asset use. **Do not add asset 06 here:** it belongs on the dedicated Join page, so the homepage retains one principal cinematic image. This closing section can use typography and simple geometry.

## 5. Existing images: fixed placement and handling

### A. Six approved conceptual images

These placements and captions are already approved for the unchanged source images. Appendix A carries the exact original filenames, direct Drive links and hashes. Titles below are human-readable asset names, not guessed filesystem paths.

| No. / asset | Page and exact section | Desktop treatment | Mobile treatment | Pairing and restrictions |
|---|---|---|---|---|
| 01 — Three pillars, one discovery core | Research Overview, below its written introduction and before the precise research map | One large chapter image, native proportions, within the page grid | Text first; complete image; caption immediately below | Introduce the three contributions in text, show the conceptual image, then explain relationships with SVG/HTML. Do not duplicate it on Home or use it as evidence. |
| 02 — Evidence Spiral of Discovery | Pillar II, alongside the first explanation of evidence engineering | A principal illustration beside or immediately below the opening explanation, followed by the functional evidence-loop diagram | Explanation → full image → caption → precise vertical loop | Pair with candidate design, evidence generation, evaluation and model revision. Keep loop labels in HTML/SVG. No equations, performance numbers or labels added to the approved PNG. |
| 03 — Mathematics to Frontiers, and Back | Pillar III, below its opening statement | Large principal image; explanatory text before it and questions/capabilities after it | Opening statement → uncropped image → caption → mathematical questions | Explain two-way exchange between mathematical structures and scientific questions. Do not frame Pillar III as a collection of application domains. |
| 04 — Möbius cycle of space–interaction–learning | About / Vision, middle chapter beside the Space–Interaction–Learning explanation | Image and a short explanatory block; full-width image if the side-by-side version loses clarity | Explanation first, full image second, caption third | A metaphor（隐喻）for mutual shaping. Keep Scientific Learning Grammar labelled as a long-term research programme. Do not claim exact Möbius topology（莫比乌斯拓扑）. Not the opening Hero. |
| 05 — From Testbeds to Discovery Horizons | Home, H07 Scientific Testbeds | Large illustration in a light chapter; heading/text above, four testbed cards below | Text → complete image → caption → single-column cards | The homepage's only cinematic image. No long overlay text. Testbeds connect the pillars rather than becoming a fourth pillar. |
| 06 — Signals into scientific discovery | Dedicated Join / Collaborate page, closing section | Short invitation at left and illustration at right. Genuine dark negative space（留白）may hold brief text if readable; separate columns are the robust default | Invitation/CTA first, complete image below, visible caption | Frame scientific inputs coming together. Do not repeat on the Home closing CTA, flatten it into every card, or imply a real instrument/photo. |

All six use the visible category **Conceptual visualization**. Record and disclose AI generation in the figure attribution（图片来源说明）; retain the approved caption verbatim. A compact second line such as “AI-generated conceptual illustration; not experimental evidence” can provide the distinction without turning the page into an internal approval dashboard.

### B. Two additional image candidates

| Asset | Design decision | Handling |
|---|---|---|
| Luminous amber verification aperture | Internal/archive only | Retain the source if found; do not publish merely to use all available artwork. Not included in the six-image approval record. |
| Three-territory map with amber ring | Reserve alternative for a future social/campaign composition | Do not use beside asset 01 or treat it as one of the six approved images. Any new public use requires an applicable approval. |

Their original locations were not verified for this brief. Keep those entries as named candidates rather than inventing file links.

### C. Processing rules for all image integrations

1. **Locate and inspect.** Retrieve the exact source, view it, confirm its filename and hash where supplied, and inspect embedded labels before deciding its layout.
2. **Preserve masters（原始母版）.** Keep the original PNG unchanged. Generate web derivatives（网页派生版本）from a copy. Record transformations and source identity.
3. **Preserve meaning.** Default to the entire approved composition using native aspect ratio and `object-fit: contain` where appropriate. Never stretch an image. Never crop essential objects, labels, feedback paths or foreground elements.
4. **Mobile first in reading order.** Text stays before the image. If a separate crop adds value, define the protected area only after visual inspection. If meaning would be lost, keep the full image and adjust layout instead. Changes to scientific content or the approved composition need a new applicable decision.
5. **Use responsive files.** The design targets 640, 960, 1440 and up to 1920 px widths, but never upscale a smaller master. The saved handoff records 1672 × 941 px for images 01–03; confirm other dimensions when retrieving them. WebP is a practical default; AVIF is optional when supported by the current build. Retain PNG access/fallback.
6. **Reserve space.** Provide intrinsic width/height and an appropriate source set. Load below-the-fold art lazily; avoid six full-size PNGs on initial page load.
7. **Keep text live.** Do not bake new headings or captions into bitmap artwork. Existing labels in approved art remain part of the source; provide a readable adjacent explanation rather than pretending those labels are responsive text.
8. **Caption and text equivalent.** Use the approved captions in Appendix A. Write alt text（替代文本）after viewing the actual image; it should describe the visible meaningful content, not guessed detail from a title. This brief deliberately does not supply unverified pixel-level alt text.
9. **Check context.** The same image can look like a result when placed beside a performance claim. The conceptual label and surrounding wording must make its role clear.
10. **Review each placement.** Inspect desktop and mobile views, reading order, caption, contrast and missing-image behaviour. Reuse the original without unnecessary regeneration or visual edits.

### D. Three public visual classes

| Class | Examples | Presentation | Evidence boundary |
|---|---|---|---|
| Conceptual visual（概念视觉） | The six approved illustrations; explanatory system maps | Large artwork or precise labelled diagram; visible conceptual category | A conceptual illustration communicates an idea; visual approval does not validate a scientific claim. |
| Scientific evidence figure（科学证据图） | Real benchmark plots, controlled comparisons, measured/inferred mechanism figures | White figure frame, figure number, complete caption, evidence status, full-size access | State measured vs inferred content, conditions and limits. Use “validated” only with support. |
| Documentary photograph（纪实照片） | Group photograph, conference, graduation, lab event | Natural photography, event/date caption and a relevant album/profile link | Use authentic images with appropriate public-use permission; no generated substitutes. |

Precise diagrams can be conceptual or evidence-based. Decide their class from what they assert and support—not from SVG versus PNG format.

## 6. Prepared diagrams, templates and written materials

### Diagram and template placement

| Prepared material | Public destination | Required adaptation（改编处理） | What stays internal |
|---|---|---|---|
| Space–Interaction–Learning Map; known design label `space-interaction-learning-map.svg` | Home H01 compact version, Home H03 explanatory version, Pillar I full version | Rebuild/adapt as responsive SVG/HTML with live labels, explanations and feedback. Reuse the same semantic source rather than duplicate disconnected diagrams. | Original design annotations and developer notes |
| Three-Pillar Research Map SVG | Research Overview, after conceptual image 01 | Show learner, evidence environment, mathematical lens, testbeds and named feedback relationships. Use different layouts on desktop/mobile. | Draft exports with obsolete taxonomy or misleading colour assignments |
| Closed-loop discovery/evidence-loop material | Home H05 and Pillar II | Compact steps on Home; deeper selectable explanations on Pillar II. Main flows and return loops have different line styles. | Review/release procedures unrelated to scientific discovery |
| High-quality-evidence material | Pillar II and appropriate project/resource explanations | Translate reliability, coverage, informativeness, provenance（来源记录）and negative evidence into readable criteria | Internal audit status, private student commentary and unpublished results |
| Near–Mid–Far roadmap / Horizon material | Research and About | A labelled `NOW / NEXT 3–5 YEARS / HORIZON` sequence; no invented deadline or achieved-status claim | Internal career/grant strategy |
| Method-to-Testbed Matrix（方法—试验场映射表） | Research testbeds and selected project cross-links | Build as accessible HTML table/cards; map real questions, methods and testbeds | Unapproved project IDs, metrics and proposals |
| Research icon system | Research cards, resource labels and selected controls | Extract individual consistent SVG components; keep visible labels. Icons support reading, not replace it. | Full icon contact sheet/toolkit page |
| Project thumbnail templates | Project index and eligible resource previews | Fill with real, approved project-specific structure; focus each thumbnail on one contribution | Unfilled templates and invented scientific details |
| Scientific figure templates | Students' figure-authoring workflow; completed approved figures may enter projects/publications | Reuse panel logic, caption structure and visual rules with actual data | Blank templates, figure QA instructions and review notes |
| Page wireframes（页面线框图） | Implementation reference only | Translate spatial relationships into real components and content | Whole wireframe screenshots, numbered developer callouts |
| Authoring / release / migration SVGs | Internal maintenance documentation | Retain as development guidance if useful | All public Home, Research, People and Gallery pages |
| PI / Join / collaboration copy kits | About, People and Join, using the relevant short/long version | Tailor to the reader's purpose, check current openings/contact facts | Applicant review rules, private trackers and unverified achievements |

The SVG names above are design labels from the supplied discussions. Their exact current repository paths must be discovered; do not assume a filename in this brief already exists in the checkout.

### Six existing material packs to reuse

These files were located and their introductory contents read while preparing this brief. Their detailed pages remain reference material for the implementation conversation. The current design decisions and explicit user wording take priority over older alternatives within the packs.

| Pack / exact filename | Use in the new build | Read boundary |
|---|---|---|
| `Research_Website_Materials_01_Core_Narrative.docx` | Research descriptions at different lengths, stable three-pillar scope, supporting About language | Keep the current exact Hero subtitle; do not restore an older variant automatically. |
| `Research_Website_Materials_02_Research_Maps.docx` | Three-Pillar Map and Space–Interaction–Learning Map semantics（语义）, labels and feedback | Earlier colour shorthand must not imply the three dimensions equal the three pillars. |
| `Research_Website_Materials_03_Page_Architecture.docx` | Home, Research, Evidence Engineering, About section architecture and responsive reading order | The current compact navigation supersedes earlier simplified menus. |
| `Research_Website_Materials_04_Visual_Direction_and_Components.docx` | Editorial layout, component patterns, geometry, type and visual hierarchy（视觉层级） | Use it as a design reference, not a screenshot to embed. |
| `Research_Website_Materials_05_Scientific_Imagery_and_Iconography_Toolkit.docx` | Diagram language, research icons, thumbnails, evidence-figure templates and text equivalents | Templates are not scientific results. |
| `Research_Website_Materials_06_Collaboration_Join_Us_Research_Assets_and_PI_Profile.docx` | Four contact paths, opportunity status, resource details, PI biography lengths | Verify current status and contact details before public use. |

The supplied attachment retains the private retrieval identifiers in its Appendix B. Source documents do not need to be published on the website to reuse their ideas.

## 7. Page specifications beyond the homepage

### Research Overview

Order: **One scientific system. Three distinct contributions.** → written introduction → image 01 + approved caption → precise Three-Pillar Map → three contribution sections → shared methods/principles → NOW/NEXT/HORIZON → cross-pillar testbeds → relevant projects and resources.

Image 01 gives an overall conceptual impression; the precise map explains the actual relationships. Avoid a second large cinematic image and avoid replacing the map with three isolated boxes.

### Shared pillar-page template（可复用页面模板）

Page label → engaging headline → precise scientific thesis → principal visual → limitation addressed → core questions → system/method diagram → capabilities → eligible current projects → evidence/outputs → open questions → focused collaboration CTA.

| Page | Principal visual | Required content |
|---|---|---|
| Pillar I — Scientific Learning | Full Space–Interaction–Learning diagram; no additional cinematic PNG required | Representation spaces; interaction structures; guiding signals; learning dynamics; primitive anchors; divide/recompose; mechanism-aligned representations（机制对齐表示）; methods/software; open questions |
| Pillar II — Evidence Engineering | Image 02 after/beside the opening explanation; precise loop later | Limits of passive datasets; evidence quality/source; data factories; perturbations and experimental design; active learning/information gain; candidate/dataset acquisition; closed-loop discovery; protocols/datasets; testbed partnership |
| Pillar III — Mathematical Frontiers | Image 03 below the opening statement | Mathematical questions; computation/statistical inference; identifiability; uncertainty and out-of-distribution behaviour（分布外表现）; causal/mechanistic reasoning; inverse design; frontier stress tests; benchmarks and code |

Do not manufacture active-project cards or completed capabilities for a page whose source material describes only future research.

### Projects and project detail

Index filters: pillar, scientific question, testbed, scientific status, output type and evidence status. Use only filters supported by actual records; avoid a crowded empty control panel.

Detail order: project identity/status → scientific question → why existing approaches are insufficient → contribution → method/system → evidence design → supported current results → alternative explanations/controls → limitations → datasets/code/protocols/publications → team → related work → citation/contact.

Keep scientific status, evidence status, publication state and time horizon distinct in the data model. Show visitors only useful, plain-language status. Internal acceptance fields stay in maintenance records. Conceptual illustrations must be identified as such; authentic result figures take priority when available.

### Publications

Readable bibliography with featured work, year/pillar/member/type filters where supported, DOI/journal/preprint links, abstract, BibTeX download（文献引用文件）, related project and dataset/code. Preserve existing records and URLs. A peer-reviewed paper（同行评审论文）, preprint（预印本）, cover picture and frontispiece（卷首插图）must not be presented as interchangeable research-output types. Do not generate citation counts.

### Resources

Types: dataset, code, benchmark, protocol, model, figure or teaching asset. Make the main action obvious. Include version, maintainer, licence（许可）, provenance, access level, evidence status, citation, review date and related project/publication when applicable. Never invent a download, software release or access entitlement.

### People

Order: authentic group image → PI → research staff/postdocs → PhD students → master's students → undergraduate researchers → collaborators → alumni. Preserve actual membership and role facts.

Member cards: consistent portrait treatment, name, role, interests, current project if public, and supported email/ORCID/Scholar/GitHub/profile links. Detail pages lead with the person's scientific questions and contribution, then projects/outputs, short biography and contact. PI content opens with the research programme rather than a long list of titles or awards.

### News

Reverse chronological list with publications, awards, talks, releases, new members and lab activities. Significant items have stable individual URLs. A news story and a gallery album about the same event should link to each other instead of repeating all content.

### Gallery

Real lab photographs only. Group by year in descending order; use large thumbnails, event/date captions and a lightbox（大图浏览层）. Support keyboard navigation, Escape to close, focus restoration, touch swiping, zoom and landscape viewing. Retain direct-image access if JavaScript fails. Do not autoplay or use conceptual scientific artwork to fill the gallery.

### About / Vision

Mission → research thesis → Space–Interaction–Learning explanation with image 04 in the middle chapter → Scientific Learning Grammar as a long-term programme → principles → NOW/NEXT/HORIZON → research culture → why these testbeds → PI programme overview.

Keep current capabilities, the next 3–5 years and the long horizon visibly distinct. Internal monograph plans, career ambitions and private management records are not public website copy.

### Join / Collaborate

Provide four routes: scientific collaborator; experimental/testbed partner; prospective student/researcher; research-asset user. Each explains suitable questions, what context to send, the expected contribution, the verified contact route and what happens next. Do not promise response times without an established practice.

Recruitment content includes current opening status, suitable backgrounds, application materials, a work sample and a verified email subject format. Do not imply a funded position merely because a recruitment template exists. Use image 06 in the closing invitation, following Section 5.

### Footer and supporting pages

Quiet columns for Research; Projects & Outputs; People & Updates; Join / Collaborate. Institution area: Xu Lab, verified school/university, Guangzhou, confirmed email and scholarly links. Final row: accessibility, privacy, sitemap, real update information and copyright. Keep claims about privacy/analytics consistent with actual site behaviour.

## 8. Visual system and reusable components

### Colour tokens（颜色变量）

| Role | Value | Usage |
|---|---|---|
| Primary navy | `#0B2545` | Lab identity, headings, selected dark chapters |
| Pillar I blue | `#2E74B5` | Learning-system category |
| Pillar II teal | `#2A8C82` | Evidence-engineering category |
| Pillar III amber | `#A86F18` | Mathematical/frontier category |
| Border grey | `#D7DEE7` | Dividers, frames, inactive structure |
| Light background | `#F6F8FB` | Quiet background sections |
| Body text | `#102642` | Main reading text |

Aim for a predominantly light website: roughly 70% white/light, 20% navy sections, 10% accent colour, as a visual guide rather than a rigid quota. Purple may occur in artwork but is not a fourth category. Status labels must include text and cannot rely on pillar colour alone.

### Typography and spacing

- English/UI: Inter; Chinese: Noto Sans SC; compact technical metadata: IBM Plex Mono. Prefer self-hosted, licensed font files when adding these families; preserve a coherent existing implementation unless a change is needed.
- Use a clear sans-serif（无衬线）hierarchy. Large confident headings, moderate body type and quiet metadata; never shrink essential labels to fit a diagram.
- Maximum content width: 1280 px. Long-form reading width: 720–780 px; aim to keep normal paragraph lines below about 75 characters.
- Desktop grid: 12 columns. Section spacing: approximately 96 px desktop, 64 px tablet and 48 px mobile.
- Cards: 12–16 px corners where appropriate, 1 px cool-grey borders, very light shadows. Vary component shape by content type instead of putting everything in identical boxes.
- Background rhythm: light introductory section, white analytical section, occasional navy chapter, white evidence section. Do not force a dark Hero on every page.

### Component catalogue（组件目录）

Names describe responsibilities; implement as Hugo partials/layouts or the equivalent in the actual stack.

| Component group | Components | Key behaviour |
|---|---|---|
| Site shell | SiteHeader, MobileNavigation, SiteFooter | Clear active state, usable keyboard navigation, real destinations |
| Scientific explanation | PageHero, ScientificThesis, SystemMap, PillarCard, EvidenceLoop, HorizonRail | Live readable labels; feedback semantics; progressive depth（逐层深入） |
| Research records | ProjectCard, ProjectStatusStrip, PublicationCard, ResourceCard | Different information hierarchy for each content type |
| People and updates | PersonCard, NewsCard, GalleryGrid, GalleryLightbox | Human photography; chronology; accessible image browsing |
| Figures | ConceptualImage, EvidenceFigure, FigureCaption | Distinct visual classes, correct caption, source/rights data |
| Navigation between content | JoinPathCard, RelatedContent | One useful deeper route and one related route; no dead-end generic CTA |

Interaction budget: node highlighting, short path introduction, slight card movement, normal anchor scrolling and gallery swipe. Exclude autoplay Hero carousels, particle backgrounds, continuously spinning molecules, heavy parallax（视差效果）, glass panels and automatic audio/video.

## 9. Responsive layout and accessibility（响应式布局与无障碍）

| Width/context | Required treatment |
|---|---|
| 320–480 px | Text before principal image; one-column pillar/project sequence; vertical maps and loops; captions visible; no page-level horizontal scrolling |
| Around 768 px | Hero may stay stacked; two-column content when comfortable; navigation stays mobile if labels become crowded |
| At least 1200 px | 12-column grid; side panels for diagram explanations if useful; maintain readable paragraph width |
| Touch | No hover-only information; reachable controls; gallery swipe/zoom with visible controls |
| Keyboard | Visible focus, equivalent map functions, labelled controls; focus returns to the triggering image after a lightbox closes |
| Reduced motion | Static diagrams or instant state changes; no required animation to access meaning |
| JavaScript unavailable | Main text, publications, images and useful links remain visible; interactive enhancements fail gracefully |

Use semantic headings（语义标题）with one page H1, a skip link, real links/buttons, meaningful alt text and explicit image dimensions. Test text/background contrast, particularly captions on dark sections and amber/teal text on pale surfaces. Do not assume the palette passes in every combination.

Responsive diagrams should reorganize, not just shrink. When a complete relationship cannot remain readable as one mobile figure, use named sequential blocks plus an explicit feedback explanation. Tables may use cards or a labelled scroll region; do not allow the whole page to overflow.

## 10. Content model and public/private boundaries

Students should update structured content（结构化内容）rather than page layout code. Keep one source for research taxonomy（研究分类体系）and share it across navigation, maps, tags and cross-links.

### Record fields

| Record family | Fields to support |
|---|---|
| Shared | title, slug, summary, owner, last_reviewed, related records |
| Research/project | pillar, testbeds, scientific_question, contribution, scientific_status, evidence_status, publication_state, horizon, team, related_publications, related_resources |
| Visual | asset_id, source file/URL, visual_type, source identity/hash, alt_text, caption, rights, AI/source attribution, approved placement, transform history |
| Resource | version, maintainer, licence, access, evidence status, citation, related project/publication |
| Gallery | original, thumbnail, event, date/year, caption, permitted public use |

Use the existing repository's field names where practical. This table specifies meaning; it does not require creating a second competing metadata schema（元数据结构）.

**Keep three states separate:** scientific status describes progress of the work; evidence status describes what supports the claim; publication state describes whether the content may be exposed. NOW/NEXT/HORIZON describes timing and ambition, not evidence strength.

Only render eligible public records. A PI-approved conceptual image can be reused in its approved placement, but it cannot authorize unrelated project results. No `TBD`, internal filenames, private review comments, candidate metrics or broken download buttons on public pages.

A non-indexed preview can still be public. Keep confidential project materials and unpublished private files outside its deployed directory and outside public Git history. For content already eligible for a public preview, use preview `noindex` metadata and the existing review flow.

Student editing scope: member/news/gallery records, verified publications, approved project text, approved images and alt text. Changes to the core research taxonomy, homepage thesis, visual tokens, status logic and navigation need the responsible design/scientific owner. Do not translate this internal division of work into confusing visitor-facing controls.

## 11. Implementation context: continue existing work

### Historical context recovered from the saved handoff

The following comes from `XuGroupWeb_Project_Handoff_2026-09-05.md`. It was read for this design brief; GitHub and Netlify were not re-inspected in this task. Verify live state before using any branch/PR instruction.

| Item | Recorded context |
|---|---|
| Repository | [derndy/XuGroupWeb](https://github.com/derndy/XuGroupWeb) |
| Existing stack | Hugo Blox; saved handoff specified Hugo Extended `0.139.4` |
| Working branch | `design/site-foundation-v1` |
| Review PR | [Draft PR #3](https://github.com/derndy/XuGroupWeb/pull/3) |
| Preview | [Recorded Netlify preview](https://deploy-preview-3--xushidang-lab.netlify.app) |
| Production site | [Recorded production URL](https://xushidang-lab.netlify.app/) |
| Previous local checkout | `/workspace/sites/xugroup-web` — a prior workspace path, not guaranteed to exist in a new conversation |

That snapshot describes completed foundation, Research/Pillar pages, People, Gallery, News and Publications work, with image 01 prepared in a later local batch. It also describes a local/remote history difference. **Do not infer that this difference still exists, redo old synchronization blindly, or recreate all pages from scratch.** The implementation conversation must read the current state first.

The snapshot's claim that only image 01 is approved in the repository conflicts with the separate saved PI approval record for all six images. The latter provides exact filenames, bytes, placements and captions. Treat this as an approval-record synchronization task for unchanged approved material, not as absence of PI approval.

### Known repository entry points from that snapshot

These are repository-relative historical paths, to be verified in the actual checkout.

| Responsibility | Recorded files |
|---|---|
| Build/hosting | `netlify.toml`; `.github/workflows/publish.yaml`; `config/_default/hugo.yaml` |
| Design foundation | `assets/scss/template.scss`; `docs/redesign-foundation.md` |
| Research | `data/research_system.yml`; `content/research/`; `layouts/landing/research.html`; `layouts/landing/pillar.html` |
| Scientific assets | `data/research_assets.yml`; `docs/scientific-visual-governance.md`; `docs/scientific-visual-approval-2026-09-05.md`; `scripts/audit-research-visuals.py` |
| People | `data/people_page.yml`; `layouts/landing/people.html`; `layouts/partials/people/` |
| Gallery | `static/data/gallery-data.json`; `layouts/landing/gallery.html`; `static/js/gallery.js` |
| News | `content/post/`; `layouts/post/list.html`; `layouts/partials/news-record.html` |
| Publications | `content/publication/`; `data/publication_kinds.yaml`; `layouts/publication/`; `assets/js/publications.mjs` |

The handoff recorded image 01 at `assets/media/research/three-pillars-discovery-core.png`, and candidates 02/03 at `assets/media/research/evidence-spiral.png` and `assets/media/research/mathematics-frontiers.png`. Match them against Appendix A before reuse. Paths for images 04–06 were not verified here; choose consistent repository paths after inspecting conventions, and retain their original source identities.

### Recommended build sequence

1. **State and source map:** Read current project-state files, inspect branch/worktree/PR state, and resolve the six originals. Produce a brief “existing / missing / needs adjustment” list.
2. **Global design and maps:** Reuse or refine the shared palette, type, header/footer, semantic Hero and maps. Keep the approved exact homepage copy.
3. **Homepage:** Apply H01–H11 where eligible content exists. Integrate image 05 only in Testbeds; pair it with explanatory cards and a real lab photograph elsewhere.
4. **Research and pillars:** Preserve working pages, incorporate image 01, image 02 and image 03 in their exact approved places; retain precise diagrams.
5. **About and Join:** Use image 04 in the About middle chapter and image 06 in the Join closing section. Finish clear audience routes and truthful recruitment information.
6. **Content connections:** Connect approved projects, publications, resources and people. Preserve already-working News, Gallery and bibliography features.
7. **Review:** Check the actual preview at desktop/mobile widths, fix meaningful layout or content-routing problems, and record the final asset-to-page mapping.

If the current code already satisfies a step, verify and keep it. Do not rewrite merely to match the suggested component names. If the next user requests a separate repo or a fresh platform, follow that explicit instruction while preserving the approved design and assets.

## 12. Acceptance criteria（验收标准）

The first usable build should demonstrate:

- [ ] Exact homepage H1, subtitle and tagline preserved.
- [ ] Text-led Hero with a legible semantic map; no conceptual PNG replacing it.
- [ ] Space, Interaction and Learning are not mislabelled as the three pillars.
- [ ] Learning-system design, evidence engineering and mathematical/frontier exploration remain distinct and connected.
- [ ] Testbeds cross the pillars; no applications-only Pillar III or added fourth pillar.
- [ ] Each of the six approved images is in its assigned page/section, or a specific missing-source/build blocker is reported.
- [ ] Image 05 is the only large cinematic artwork on Home; image 06 appears on Join, not as a second Home artwork.
- [ ] Full compositions, correct source identity, unchanged approved captions and visible conceptual attribution are preserved.
- [ ] Research maps use readable live labels and feedback; their mobile versions remain understandable.
- [ ] No wireframe, governance diagram, blank template or archive candidate appears as public scientific content.
- [ ] Evidence figures and real photographs remain visibly distinct from conceptual illustrations.
- [ ] Existing names, membership, news, publications, image URLs and working routes remain intact unless an evidenced correction was requested.
- [ ] All shown projects, resource actions, openings and scientific claims have appropriate support; empty blocks are omitted cleanly.
- [ ] Home, Research, pillars, About and Join work at 320 px, a representative tablet width and desktop width without clipped text or page overflow.
- [ ] Keyboard interaction, visible focus, reduced-motion behaviour, caption visibility and gallery closing/focus return work.
- [ ] Images have suitable file sizes, responsive sources, intrinsic dimensions, captions and checked alt text.
- [ ] Navigation, relevant cross-links, downloads and real 404 handling work; preview metadata reflects preview status.
- [ ] The current project build and relevant existing checks pass; focused browser review confirms the changed pages.
- [ ] A final change record names implemented sections, actual asset paths, deferred items and the preview URL. Deployment status is reported truthfully.

## 13. Prompt to paste into the new conversation

Attach this file, then paste:

> Read the attached Xu Lab website design and asset-placement brief in full and apply it to the website. First inspect the current repository and latest PROJECT_STATE.md/project-state.md so you preserve work already completed. Use the approved design, exact homepage title/subtitle/tagline, and three research pillars. Give special attention to Sections 5–6 and Appendix A: retrieve and reuse the six approved original images, match their source identities, and place each in its specified page and section with its approved caption. Reuse the prepared research maps, diagrams, copy and templates according to their assigned roles. Keep conceptual art, evidence figures and real photographs distinct. The six unchanged source images and placements are already approved; reconcile any stale approval records rather than asking me to approve them again. If originals cannot be accessed, identify exactly which files I should attach and continue the work that does not depend on them. Implement in small, high-quality batches, show a working preview, and report what is complete and what remains. Keep production unchanged unless I separately instruct you to publish it.

**Chinese quick instruction（可直接使用的中文提示）：**

> 请完整读取附件，按其中的设计方案继续创建课题组网站，尤其严格执行已有图片与材料的安置方案。先检查当前 GitHub 和项目状态文件，复用已经完成的代码。六张原图及对应摆放和图注已经获批，请按附录定位原图，不要重新生成替代图，也不要因旧记录未同步而让我重复批准。先做高质量、可检查的预览，分批完善；未经本轮额外发布指令，不改正式网站。

## Appendix A. Exact six-image approval and source register

The following is preserved from the saved `XuLab_Scientific_Image_Approvals.md` record, read on 5 September 2026. Its direct image links and hashes make this handoff usable without the old chat. Retrieval of that record does not mean the six binary files were downloaded or visually re-audited during this file-writing task. Verify the exact bytes and current access when implementing; the documented approval itself need not be repeated.

### Xu Lab — Scientific Image Approvals

Updated: 2026-09-05

#### Decisions recorded

PI: derndy. All six images are **APPROVED AS SHOWN**, including their planned placements and captions（图注）.

- 01–03: user instruction “1-3 approve”.
- 04–06: user instruction “4-6 approve”; the user supplied the group website Google Drive folder.
- Image 01 remains unchanged. Earlier suggested colour/check-mark edits were not applied.

These AI-generated conceptual illustrations（概念示意图）are approved for conceptual website use. Approval does not turn the imagery into validated scientific results or documentary photographs. No website deployment or GitHub change was performed by this review-and-save task.

Repository context from the review conversation: `derndy/XuGroupWeb`, branch `design/site-foundation-v1`, Draft PR #3. This context was not re-inspected in this task.

#### Approved image register

| No. | Image | Decision | Planned placement |
|---|---|---|---|
| 01 | Three pillars, one discovery core | APPROVED AS SHOWN | Research Overview, below the introduction. |
| 02 | Evidence Spiral of Discovery | APPROVED AS SHOWN | Pillar II, alongside the explanation of evidence engineering. |
| 03 | Mathematics to Frontiers, and Back | APPROVED AS SHOWN | Pillar III, below its opening statement. |
| 04 | Möbius cycle of space–interaction–learning | APPROVED AS SHOWN | About / Vision, beside the explanation of Space–Interaction–Learning. |
| 05 | From Testbeds to Discovery Horizons | APPROVED AS SHOWN | Homepage, scientific-testbeds section. |
| 06 | Signals into scientific discovery | APPROVED AS SHOWN | Join / Collaborate, closing section. |

#### Google Drive locations

- [Group website folder](https://drive.google.com/drive/folders/1YzLvkhzMMNfcRh2QG8RWhYAVPRs0-Gjm)
- [03_BRAND_MEDIA_MASTERS — six original PNGs](https://drive.google.com/drive/folders/1bdUauWg9D0PRELgHoXKjvOPRle0q7rsB)
- [04_RELEASE_EVIDENCE — approval record](https://drive.google.com/drive/folders/1rX_GMyovQ9Es1OrikCkeFZTraHkXuxb9)

#### Captions and exact source identity

Review numbers refer to the source bytes identified by the SHA-256 values below. Original images were uploaded without visual changes.

##### 01 — Three pillars, one discovery core

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “1-3 approve”.
- Placement: Research Overview, below the introduction.
- Approved caption（图注）: A conceptual view of three connected research pillars: learning-system design, evidence engineering, and mathematical exploration.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/1Vfy8ZFdOS-JrTwrRROOj7nKX0EEWxj6X/view?usp=drivesdk)
- Drive filename: `01_Three_Pillars_One_Discovery_Core.png`
- SHA-256: `735a2c053ef15d2d265a301d5de684dc783cb7474e36e0cbf33d428e6da4ae6a`

##### 02 — Evidence Spiral of Discovery

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “1-3 approve”.
- Placement: Pillar II, alongside the explanation of evidence engineering.
- Approved caption（图注）: A conceptual illustration of repeated cycles linking candidate design, evidence generation, evaluation, and model revision.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/18QqgwpHMlntsqxgWz_Eet05mrDxD9IWi/view?usp=drivesdk)
- Drive filename: `02_Evidence_Spiral_of_Discovery.png`
- SHA-256: `c55e7fd1dac7e954746f5556a9286fdb5be4d7ff6e36bccd462a80c851ff8ff9`

##### 03 — Mathematics to Frontiers, and Back

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “1-3 approve”.
- Placement: Pillar III, below its opening statement.
- Approved caption（图注）: A conceptual view of the exchange between mathematical structures and scientific questions, with each informing the other.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/1f-CrVk6oL8w1AlQlEne91-7nnJmX_1mU/view?usp=drivesdk)
- Drive filename: `03_Mathematics_to_Frontiers_and_Back.png`
- SHA-256: `4870b89430de42b07079645d3189f1e37f5d059034f6a03e6b4ec8e4b6875092`

##### 04 — Möbius cycle of space–interaction–learning

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “4-6 approve”.
- Placement: About / Vision, beside the explanation of Space–Interaction–Learning.
- Approved caption（图注）: A conceptual illustration of how scientific representations, interactions, and learning continually shape one another.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/1zyaKpWkmmKO-XRbpfVV6jKLickEciXIL/view?usp=drivesdk)
- Drive filename: `04_Mobius_Cycle_Space_Interaction_Learning.png`
- SHA-256: `1d72f9a2acede990f979fedce445d18ef62212503a25f217ebea24658c777b9c`

Display note: use the loop as a visual metaphor; the public caption makes no claim about exact Möbius topology.

##### 05 — From Testbeds to Discovery Horizons

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “4-6 approve”.
- Placement: Homepage, scientific-testbeds section.
- Approved caption（图注）: A conceptual illustration of scientific testbeds connecting materials and biomedical questions with future discovery directions.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/1msYeId_zaA8SD0Yp8Hw4PCe8HLyrxmeX/view?usp=drivesdk)
- Drive filename: `05_From_Testbeds_to_Discovery_Horizons.png`
- SHA-256: `3b48ea0f1403fd38c3981574534e40b6c4bc75c9fd14772edb6640af9fe95a8e`

Display note: keep it large within the light homepage testbeds section, with text outside the detailed image.

##### 06 — Signals into scientific discovery

- Decision: **APPROVED AS SHOWN** — 2026-09-05, derndy (PI).
- Approval message: “4-6 approve”.
- Placement: Join / Collaborate, closing section.
- Approved caption（图注）: A conceptual illustration of diverse scientific inputs coming together to open new directions for discovery and design.
- Visible category label: Conceptual visualization
- [Original PNG in Google Drive](https://drive.google.com/file/d/1uYILO-1orxIcupSqH-h8xpq6zOBUJyTJ/view?usp=drivesdk)
- Drive filename: `06_Signals_into_Scientific_Discovery.png`
- SHA-256: `82e5f04b9d83b4812487bb9308a84bf9e47811133d260fe34f8edc692d798e7a`

Display note: brief invitation text can occupy the dark left-hand space; use a stacked text/image layout on mobile.

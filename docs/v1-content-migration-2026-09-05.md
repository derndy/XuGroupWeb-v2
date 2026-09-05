# v1 content migration — 5 September 2026

## Source and boundary

The PI requested migration of the outstanding News, Gallery and member material in [derndy/XuGroupWeb PR #2](https://github.com/derndy/XuGroupWeb/pull/2), “Update news, team members, and gallery,” submitted by `meitangpeng-hub`. The inspected source head is `36135be707ce1d68218d4bdf01d790780fa5d851`, branch `update20260904`, compared with base `b39bb3113f9601433155075204c209672f1758fb` (32 changed paths). The v2 migration starts from main at `c9afdcf43cb59d679c1cc199f95a81814f07e615`, including merged PRs #12 and #13.

The PI explicitly confirmed that the incoming members joined in **2026**. This supersedes the source welcome news's 2025 date. Public migration is authorized as a v2 review branch/draft PR; the v1 PR remains open and neither repository's production branch is changed by this migration.

## News (six additions)

| Date shown | Record | Assets |
| --- | --- | --- |
| 2026, year only | Yuting Qin and Shidao Wang join as master's students | Profiles link from People; no event photograph supplied |
| 17 October 2025 | Yujian Liu receives the 2025 National Scholarship | No photograph supplied |
| 12 April 2026 | BME Faculty-Student Badminton Tournament; group team wins championship | Featured photo |
| 24 May 2026 | Yujian Liu and Yinghao Liu's master's thesis defenses | Featured photo |
| 29 May 2026 | Interdisciplinary gathering and movie outing with the Wang and Lin groups | Featured photo |
| 10 June 2026 | Graduation ceremony | Featured photo and two inline photos |

Source titles, summaries, event bodies, affiliations and images are retained. Added factual `featured_alt` values for the four new featured images after inspecting them. All 18 existing published News sources and the Mengting Guan draft are unchanged; the source PR's Qiyun punctuation fix was already present in v2.

The welcome record uses `/post/2026-yuting-qin-and-shidao-wang-join-the-group/`, with the former v1 PR route retained as a Hugo alias (rendered into Netlify `_redirects`). `date: 2026-01-01` is only a Hugo year-sorting anchor; `date_precision: year`, `show_date: false` and `subtitle: Joined in 2026` prevent a fabricated day in visible dates. News list, latest card and homepage date rendering share `news-date.html`. Year-only records omit inferred publication timestamps from article Open Graph and JSON-LD. Do not interpret a Hugo/feed sorting timestamp as an event day. Exact joining month/day remains unconfirmed.

## Gallery (four additions)

Added badminton, movie outing and two graduation photographs as `GAL-2026-001` through `GAL-2026-004`, with a new 2026 section. All 19 prior records, corrected 2023 dates, dimensions, categories and captions are preserved. Total: 23 photographs across 2023–2026.

The v1 schema-1 array is adapted into v2's existing schema 2.0. Added bilingual titles, factual English captions and image-specific alt text. Original images and thumbnails retain their source bytes and dimensions. All 16 imported image paths across profiles, News and Gallery contain 13 unique Git blobs; the three shared News/Gallery originals are intentionally present at both existing content paths. No image was generated, cropped, recompressed or retouched. The supplied image files have no EXIF fields. Rights context is the PI's explicit public migration instruction for their existing group-content PR; no separate participant-consent claim is made.

The existing Gallery template, viewer JavaScript and Gallery CSS are unchanged, retaining PR #8's overlap repair. Only the member-card heading selectors change in shared CSS.

## People and consistency corrections

- Added Yuting Qin (`qyt`) and Shidao Wang (`wsd`), their supplied portraits, education, contact links and 2026 joining biographies. Omitted Yuting's literal `Pending.` biography placeholder.
- Moved Yinghao Liu (`yh`) and Yujian Liu (`yj`) to `graduate_alumni`, preserving profiles and portraits and using the supplied completed 2023–2026 degrees.
- Added a dedicated Graduate alumni section using v2's existing card design. Current team has 16 cards; Graduate alumni has two. No v1 inline-style/click-handler layout is copied.
- Imported Meitang Peng's 2025 PhD role. The source retained a contradictory master's-student biography and a present-tense MSc enrollment date; aligned the biography with the supplied PhD role, added the supplied PhD entry year, and represented the MSc history as “Entered in 2023.” No MSc completion or transfer date is inferred.
- Imported Qiyun Zhou's apostrophe normalization.
- Renamed the undergraduate alumni data key to `undergraduate_alumni`, as in the source PR. The graduation article explicitly confirms Yutong Wang and Qingquan Wang's bachelor's graduation in 2026; moved these two existing rows from current students to undergraduate alumni, extending their existing 2022 start years to 2022–2026. No next positions or unverified Chinese spellings are added. Missing next positions display an em dash. Five current undergraduate rows and eleven undergraduate alumni rows remain; all other rows and order are preserved.

## Verification

Production and preview-equivalent Hugo 0.139.4 builds pass (895 pages each). The publication audit preserves all 91 records, author symbols, accepted-work status, routes and citation bytes. All six approved scientific images and 24 variants pass the existing image audit.

The migration check verifies 24 published News records, 23 Gallery images, 16 current-member cards, two graduate-alumni cards, exact bytes at all 16 imported image paths, original Gallery record preservation, the year-only cohort display and redirect, and production/preview parity. Seven other main-page content trees match merged main; Home changes only through its canonical latest-three News section. All 1,400 internal links/anchors across the eleven main documents resolve. New member and news image URLs exist. Preview noindex is retained. Browser layout/interaction review remains pending; these are build/source/HTML checks.

## All 32 source paths accounted for

| Source PR path | Migration disposition |
| --- | --- |
| `content/person/pmt/_index.md` | Imported role; aligned biography and education wording with the supplied PhD entry |
| `content/person/qy/_index.md` | Copied source record |
| `content/person/qyt/_index.md` | Copied new profile; omitted Pending. placeholder |
| `content/person/qyt/avatar.jpg` | Copied byte-for-byte at the same path |
| `content/person/wsd/_index.md` | Copied source record |
| `content/person/wsd/avatar.jpg` | Copied byte-for-byte at the same path |
| `content/person/yh/_index.md` | Copied source record |
| `content/person/yj/_index.md` | Copied source record |
| `"content/post/25-04-16-Qiyun_joins_the_group_as_a_master\342\200\231s_student/index.md"` | Already present with the corrected apostrophe; no duplicate or edit |
| `content/post/25-09-21-Yuting Qin and Shidao Wang join the group/index.md` | Migrated to 2026-yuting-qin-and-shidao-wang-join-the-group; PI year correction and old-route redirect |
| `content/post/25-10-17-Yujian Liu receives the 2025 National Scholarship/index.md` | Copied source record |
| `content/post/26-04-12-2026 BME Faculty-Student Badminton Tournament/featured.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-04-12-2026 BME Faculty-Student Badminton Tournament/index.md` | Copied text; added factual featured_alt |
| `content/post/26-05-24-Master's Thesis Defenses/featured.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-05-24-Master's Thesis Defenses/index.md` | Copied text; added factual featured_alt |
| `content/post/26-05-29-Interdisciplinary Group Gathering and Movie Outing/featured.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-05-29-Interdisciplinary Group Gathering and Movie Outing/index.md` | Copied text; added factual featured_alt |
| `content/post/26-06-10-Graduation Ceremony 2026/degree_conferral.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-06-10-Graduation Ceremony 2026/featured.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-06-10-Graduation Ceremony 2026/group_photo2.jpg` | Copied byte-for-byte at the same path |
| `content/post/26-06-10-Graduation Ceremony 2026/index.md` | Copied text; added factual featured_alt |
| `data/US_Alumni.yml` | Imported key rename; reconciled two undergraduate graduates using the source graduation news |
| `layouts/partials/people-custom.html` | Adapted graduate-alumni rendering into v2 landing/people.html and shared member cards; v1 layout not copied |
| `static/data/gallery-data.json` | Merged four new image records into v2 schema 2.0 |
| `static/images/gallery/20_badminton_2026.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/21_movie_outing_2026.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/22_graduation_group_2026.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/23_graduation_group_2026_2.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/thumbnails/20_badminton_2026_t.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/thumbnails/21_movie_outing_2026_t.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/thumbnails/22_graduation_group_2026_t.jpg` | Copied byte-for-byte at the same path |
| `static/images/gallery/thumbnails/23_graduation_group_2026_2_t.jpg` | Copied byte-for-byte at the same path |

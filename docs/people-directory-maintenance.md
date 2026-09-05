# People directory maintenance

The People page separates verified member facts from page presentation. Keep that boundary intact whenever the directory is updated.

## Source map

| Content | Canonical source | Notes |
| --- | --- | --- |
| Current member name, role, biography, education, links, and avatar path | `content/person/<slug>/_index.md` | One record per public profile. Do not duplicate these facts in a layout or data file. |
| Current member portrait | `content/person/<slug>/avatar.jpg` | The path is declared in the member record and used by both the directory and profile page. |
| Undergraduate and alumni rows | `data/US_Alumni.yml` | Preserve the existing order unless the lab approves a different ordering rule. |
| Page introduction, section copy, group-photo captions, and onward routes | `data/people_page.yml` | Presentation copy only; it must not become a second member register. |
| Group photographs | `static/images/people/` | Every published photograph needs confirmed rights/consent, factual alt text, and a dated caption. |
| Page structure | `layouts/landing/people.html` | Semantic sections, registers, group moments, and onward routes. |
| Current-member grouping | `layouts/partials/people-custom.html` | Reads the `category` field and sorts published profiles by title. |
| Reusable member card | `layouts/partials/people/member-card.html` | Shared portrait, role, profile, email, and research-profile markup. |
| Visual system | `assets/scss/template.scss` | All People styles use the `people-` prefix and shared `lab-` tokens. |

Do not edit generated files in `public/`.

## Add or update a current member

1. Open the member’s canonical record at `content/person/<slug>/_index.md`.
2. Verify the spelling of the English and Chinese names with the member.
3. Verify the current role, programme year, education, biography, and every contact or research-profile URL.
4. Set `category` to an already supported public group:
   - `principle_investigator` for the Principal Investigator;
   - `graduate_student` for a current graduate researcher.
5. Place the approved square portrait beside the record and keep the record’s `avatar` path accurate.
6. Confirm that the face remains meaningful in a square crop at 320 px. Do not use appearance judgments in alt text.
7. Build the site and open both `/people/` and `/person/<slug>/` in the Deploy Preview.

The current legacy category value `principle_investigator` is intentionally retained for compatibility even though the public heading uses the correct phrase “Principal Investigator.” Do not silently rename it without migrating and testing every dependent template.

## Update an undergraduate or alumni record

1. Edit only `data/US_Alumni.yml`.
2. For an undergraduate, verify `name` and `role`.
3. For an alumnus, verify `name`, the former `role`, and the recorded next position in `current`.
4. Omit an unresolved fact rather than inserting a placeholder or guessed destination.
5. Build the site and confirm the row appears in the correct table with no content changes to adjacent rows.

## Replace or add a group photograph

1. Put the approved source image in `static/images/people/`.
2. Confirm publication rights and consent before adding it to the page data.
3. Add or update the corresponding entry in `data/people_page.yml`.
4. Write alt text that identifies the event and context without guessing identities, emotions, or appearance.
5. Write a short caption containing the event and year.
6. Use the real static path with no image-service query string.
7. Check the complete image at desktop width and its meaningful crop at 320 px.

The People page uses one current group photograph beside the introduction and keeps older group photographs in the Group record section. Member portraits belong with member cards; scientific figures belong on governed Research or Project pages, not in the People directory.

## Release checks

Before requesting review, confirm all of the following:

- The production-equivalent Hugo build succeeds with Extended `0.139.4`.
- `/people/` contains exactly one `h1` and one `main` landmark.
- Every current member has one card, a working canonical profile route, a non-empty portrait alt, and valid contact destinations.
- Member names, roles, biographies, education, and links still come from `content/person/`.
- Undergraduate and alumni rows still come from `data/US_Alumni.yml`.
- Every photograph exists at its generated URL and declares width, height, and meaningful alt text.
- Tables retain captions plus scoped column and row headers.
- All in-page jump links and onward routes resolve.
- The page has a unique title, description, canonical URL, and sitemap entry.
- No inline `<style>`, `style=`, `onclick`, empty `href="#"`, or missing `people.min.js` dependency has been reintroduced.
- The Netlify Deploy Preview succeeds before merge.

Keep the pull request in draft until member facts, portrait use, photograph rights, and the rendered page have been reviewed by the lab owner.

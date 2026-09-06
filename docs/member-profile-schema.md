# Member-owned profile schema

The Xu Lab website treats each detail page as a member-owned profile inside a PI-governed lab platform. The shared template preserves the lab identity, accessibility and release process; the member supplies or confirms the personal content. A profile is not a separate website, subdomain or free-form HTML surface.

## Architecture

| Layer | Public route | Responsibility |
| --- | --- | --- |
| Lab identity | `/` | Shared research programme and invitation |
| Team directory | `/people/` | One concise, comparable card per member |
| Member profile | `/person/<slug>/` | Full individual introduction and collaboration surface |
| Canonical outputs | `/publication/<slug>/` | Publication facts linked from profiles rather than copied into them |

Existing `/person/<slug>/` routes remain canonical for this first release. Human-readable `/people/<english-name>/` routes may be considered later only with aliases and complete link testing.

## Ownership boundary

### Stable fields

These fields support both the directory and the profile page. Changes require factual verification.

- `title`, `role`, `category`, `organizations`
- `avatar`
- `bio`: one concise sentence for the People directory and profile fallback
- `education`, `experience`
- `social`

The legacy category value `principle_investigator` is retained for compatibility.

### Extended profile fields

All extended fields are optional. Empty sections are omitted rather than displaying placeholders.

| Field | Shape | Public purpose |
| --- | --- | --- |
| `headline` | string | One clear research identity statement in the hero |
| `focus_areas` | string list | Three to five concise research tags |
| `research_questions` | list of `question` + optional `context` | Two to four scientific questions the member genuinely cares about |
| `current_work` | list of `title`, `summary`, optional `status` and `role` | One to three public-safe descriptions of ongoing work |
| `contribution_profile` | `methods`, `domains`, `can_contribute` lists | Concrete capabilities a collaborator can understand |
| `working_principles` | list of `title` + optional `detail` | Member-authored working philosophy; never infer it from project records |
| `publication_name` | string | Exact canonical author name used to validate selected publications |
| `selected_work` | list of canonical publication `page` references | Selected outputs without duplicating titles, venues or dates |
| `beyond_research` | Markdown string | Optional member-authored interests or current learning |
| `collaboration` | `statement`, `can_contribute`, `looking_for`, `formats` | Specific and actionable collaboration directions |

### Example

```yaml
headline: "A specific one-sentence research identity."
focus_areas:
  - "Method or domain"
research_questions:
  - question: "A question the member genuinely wants to answer?"
    context: "Why it matters and how the member approaches it."
current_work:
  - title: "Public-safe project or direction"
    status: "Active direction"
    summary: "One sentence with no unpublished result claim."
    role: "The member's specific contribution."
contribution_profile:
  methods:
    - "Method"
  domains:
    - "Scientific domain"
  can_contribute:
    - "Concrete contribution"
publication_name: "Exact Author Name"
selected_work:
  - page: "/publication/canonical-bundle-slug/"
working_principles:
  - title: "Member-authored principle"
    detail: "What it means in practice."
beyond_research: |
  A short member-authored paragraph.
collaboration:
  statement: "A specific invitation."
  can_contribute:
    - "Capability offered"
  looking_for:
    - "Complementary expertise or evidence"
  formats:
    - "Joint study, benchmarking, internship conversation, or another bounded format"
```

## Editorial and privacy rules

- The member may shape the personal voice, research questions, working principles, interests and collaboration invitation.
- The PI retains final editorial and publication approval through a draft pull request.
- Do not publish private phone numbers, home addresses, identity documents, personal records, credentials, unpublished data or confidential partner information.
- Describe ongoing work at the question/direction level. Do not claim an unpublished result, acceptance, validation or collaboration commitment.
- `working_principles` and `beyond_research` require direct member authorship or confirmation. Omit them when this evidence is absent.
- Collaboration text is an invitation to discuss, not a promise of supervision, funding, access, authorship, internship placement or employment.
- Selected publications must resolve to canonical website records and list `publication_name` as an author. The build fails on an invalid reference or author mismatch.
- Members must not add HTML, CSS, scripts, third-party embeds or a separate visual theme.

## Prototype scope

The first prototype uses Meitang Peng's existing verified role, education, contact and publication records. New question, current-work, contribution and collaboration copy is provisional and requires Meitang's and the PI's review before merge. Personal beliefs, hobbies and unverified project results are deliberately not inferred.

## Drive and watcher rollout

The current Google Drive portal remains unchanged while the prototype is under review. After the schema and rendered page are approved:

1. update the shared Drive `MEMBER_PROFILE_TEMPLATE.md`;
2. replace the approved member's Drive `profile.md` with the accepted canonical version;
3. extend Watcher validation to the optional fields and canonical publication references;
4. make the Watcher detect any open PR already changing the same member paths before creating a new one;
5. roll the schema out member by member, preserving one draft PR review boundary.


# Mativio — Project status (handover, 26 Nov 2026)

## Branches and deployments

| Branch | PR | State | Contents |
|---|---|---|---|
| `main` | — | **Live** at https://mativio-website.netlify.app | PRs #1–#5 and #7 merged |
| `review/botanical` | #6 | Open, awaiting owner approval | Botanical theme, mobile menu switch, listings scaling, gallery/lightbox, time-slot picker, legal updates, neighbourhood content, exact locations, real statuses and rents, mobile pillars 2 × 2 |
| **`review/responsive-ux`** | **#8** | **Open, current development branch** (built on `review/botanical`, so it contains #6) | Responsive/accessibility audit fixes, plus these handover docs and `tools/audit/` |

- Previews: https://deploy-preview-6--mativio-website.netlify.app and https://deploy-preview-8--mativio-website.netlify.app.
- **Merge plan (owner decides):** merging #8 ships #6 as well; close #6 afterwards or merge it first. Before merging, bring `main` into the branch (`git merge origin/main`). The branch doesn't yet have the PR #7 skill files (`.claude/skills/ui-ux-pro-max/`); no conflicts are expected.
- Other branches (`claude/*`, `review/spec-alignment`, `review/batch-2`, `review/batch-3`) are already merged.
- Ship to production in **one batch** when the owner approves (about 15 Netlify credits per production deploy).

## Merged history

| PR | Title |
|---|---|
| #1 | First draft homes-for-rent site |
| #2 | Redesign: new UI with light and dark themes; logo merged into the wordmark and collapsing on scroll |
| #3 | Spec alignment: localities, bottom-sheet filters, budget and type filters, swipe gallery, sticky mobile CTA, in-person/video viewing with review step, neighbourhood guide, Privacy/Terms drafts, 404/offline/loading, `/homes/<id>/` share links; viewing bookings, enquiry delivery, notify me, 360°/video tabs, general booking and requirement alerts |
| #4 | All homes semi-furnished with parking; Privacy and Terms approved; pricing placeholders |
| #5 | Mobile first fold: full-bleed photo hero with theme button; Netlify badge hidden |
| #7 | Adds the `ui-ux-pro-max` Claude skill |

## Completed features (on the development branch)

- **Brand and design:** collapsing M + ATIVIO wordmark, light/dark themes, botanical leaf cut-outs, Cormorant Garamond + Manrope, approved animations.
- **Discovery:** home page, properties listing (search, availability chips with counts, 5 filters, 5 sorts, grid/list, paging of 9, filter persistence, empty state).
- **Details:** gallery and lightbox, tabs (Overview, Photos, 360°, Video, Location, Neighbourhood), status-based actions, sticky mobile CTA.
- **Conversion:** book a viewing (in person or video, day and slot in IST, review step, reference `MTV-xxxx`), ask a question, notify me / register interest, requirement alerts, contact form. All four are Netlify Forms with a honeypot.
- **Content:** three locality pages with the verified neighbourhood guide; real listings and statuses (`docs/property-data.md`); SEO titles and descriptions per home and locality; share pages with Open Graph previews.
- **Legal:** Privacy Policy and Terms (DPDP Act 2023 and Rules 2025), dated 26 Nov 2026, with no host named.
- **Responsive and accessibility audit (PR #8):**
  - Country-code phone fields (fixes non-Indian numbers being saved as +91).
  - AA contrast: 0 failures; navy text on gold buttons; accent `#80613C`.
  - One H1 per view; linked form errors; skip link; modal menu and filter sheet.
  - Fluid type tokens; header 84/72/64; hero 42/58; tablet portrait stack; compact tablet nav.
  - 44 px targets; swipeable chips; keyboard-operable gallery; "Sending…" state.
  - Theme tokens per the brief.
  - Full audit: 288 measurements before and after.

## Pending — waiting on the owner

1. Contact phone, WhatsApp and email, for `CONTACT`, the Contact page, the footer and the privacy contact.
2. Deposits; bathrooms and area for all homes; #674 ready date, rents and furnishing; a #568 map pin.
3. Real photos, floor plans, 360° panoramas and short videos per home; genuine neighbourhood photos.
4. Viewing hours and days (`VIEWING`).
5. The name of the Coffee Board Layout park; measured distances for the neighbourhood guide.
6. **Netlify:** enable form detection, redeploy, set the form-notification email recipient. Not confirmed as done.
7. **Own domain** (e.g. mativio.in), then update `SITE`, the OG URLs and rebuild `homes/`.
8. Approval to merge #6/#8 and **go live** (the site is in test mode until the owner says so).
9. CCTV system brand/model (for Phase 5).

## Known issues and limitations

- Lighthouse and axe-core haven't been run (they couldn't be installed in the cloud sandbox). Run them on the PR #8 preview.
- No real screen-reader or 200% zoom pass yet; no physical-device testing.
- Images are low-resolution placeholders with no `srcset`/WebP (the hero is 850 px wide but displayed at about 940 px). Fix when the real photos arrive (responsive sizes, WebP/AVIF, width/height attributes).
- Google Fonts: no `preconnect` to `fonts.gstatic.com`; consider self-hosting.
- Footer links are 41 px wide (they pass AA's 24 px but are under the brief's 44 px).
- Status-badge colours are set directly rather than via tokens.
- The local `main` ref in old clones may be stale; always `git fetch` first.
- A leftover git stash (`WIP on review/batch-2`) may exist in the old cloud clone. Ignore it; it isn't in the remote.
- Forms only work on Netlify; local posts fail by design and show the fallback.

## Technical dependencies

| Dependency | Use | Notes |
|---|---|---|
| Netlify | Hosting, deploy previews, Forms | Production from `main`; previews per PR; about 15 credits per production deploy |
| GitHub `matkevin/mativio-website` | Source, PRs | Use the REST API for PRs in Claude Code cloud (GraphQL blocked) |
| Google Fonts | Cormorant Garamond, Manrope | `display=swap`; fallbacks set |
| Pannellum 2.5.6 (cdnjs) | 360° viewer | Loaded only when a tour exists |
| Google Maps short links | Location buttons | No API key |
| Node (any recent) | `tools/build-home-pages.mjs` | No npm packages |
| Python 3 + Playwright (Chromium) | `tools/audit/*` | Dev only |

## Integrations and project tooling

- **ClickUp:** Startup space, folder "Mativio Website". The "1 · Get tenants (now)" list holds the Phase 1 to-dos.
- **Claude project "Property Website":** source docs (brand draft, UI/UX spec, roadmap, neighbourhood content audit, responsive quality audit). Their content is carried into `docs/`.
- **21st.dev MCP** (free tier: 2 component retrievals a day, AI generation off). The gallery and time picker were adapted from it. Its API key is **not** stored anywhere in the repo. The owner was advised to rotate the key that was shared in chat.
- **Scheduled task:** one is set for **27 Nov 2026, 08:00 Qatar time**, in the old Claude Chat environment. It fetches the 21st.dev Drawer and Reveal components, rebuilds, pushes to `review/botanical` only, comments on PR #6 and updates a ClickUp task. Development now continues on `review/responsive-ux`, so the owner may want to cancel it or retarget it to this branch.

## Next suggested steps

1. The owner reviews the PR #8 preview on phone, tablet and desktop.
2. Run Lighthouse and axe on the preview and fix anything real.
3. Fill in `CONTACT`, set up Netlify Forms notifications, then do one end-to-end test enquiry agreed with the owner.
4. Replace placeholder media as it arrives (with responsive images).
5. Batch-merge with approval and go live; then the own domain.

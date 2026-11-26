# Mativio — Project status (updated 27 Nov 2026)

## Branches and deployments

| Branch | PR | State | Contents |
|---|---|---|---|
| `main` | — | **Live** at https://mativio-website.netlify.app | PRs #1–#5, #7 and #8 merged |
| `review/botanical` | #6 | Closed (superseded by #8) | Botanical theme, mobile menu switch, listings scaling, gallery/lightbox, time-slot picker, legal updates, neighbourhood content, exact locations, real statuses and rents, mobile pillars 2 × 2 |
| `review/responsive-ux` | #8 | **Merged** 26 Nov 2026 (contains #6) | Responsive/accessibility audit, handover docs, `tools/audit/`, spiral-wave background, home order, tagline in footer only, drag-to-close filter sheet, scroll reveals |
| **`review/radial-backgrounds`** | **#9** | **Open, current development branch** | L4 Radial Mist / D4 Radial Depth page backgrounds (replace the spiral waves); full-bleed leaves; header tagline restored; docs refreshed after #8 |

- Preview: https://deploy-preview-9--mativio-website.netlify.app.
- **Merge plan (owner decides):** merge #9 when the owner approves the new backgrounds.
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
| #8 | Responsive UX audit, handover docs, spiral-wave backgrounds, home order (properties before pillars), white button text in light mode, tagline in footer only, drag-to-close filter sheet, scroll reveals |

## Completed features (on the development branch)

- **Brand and design:** collapsing M + ATIVIO wordmark, light/dark themes, botanical leaf cut-outs, Cormorant Garamond + Manrope, approved animations.
- **Discovery:** home page, properties listing (search, availability chips with counts, 5 filters, 5 sorts, grid/list, paging of 9, filter persistence, empty state).
- **Details:** gallery and lightbox, tabs (Overview, Photos, 360°, Video, Location, Neighbourhood), status-based actions, sticky mobile CTA.
- **Conversion:** book a viewing (in person or video, day and slot in IST, review step, reference `MTV-xxxx`), ask a question, notify me / register interest, requirement alerts, contact form. All four are Netlify Forms with a honeypot.
- **Content:** three locality pages with the verified neighbourhood guide; real listings and statuses (`docs/property-data.md`); SEO titles and descriptions per home and locality; share pages with Open Graph previews.
- **Legal:** Privacy Policy and Terms (DPDP Act 2023 and Rules 2025), dated 26 Nov 2026, with no host named.
- **Motion (PR #8):** drag-to-close filter sheet with half/full snap points; gentle scroll reveals (off under reduced motion).
- **Responsive and accessibility audit (PR #8):**
  - Country-code phone fields (fixes non-Indian numbers being saved as +91).
  - AA contrast: accent `#80613C`; 0 failures apart from the gold primary buttons in light mode, which keep white text at the owner's request (2.3–3.2:1, accepted exception).
  - Home page order: hero, Our Properties, pillars, Our Localities, Our Story (owner's request, 26 Nov 2026).
  - Page background: L4 Radial Mist (light) and D4 Radial Depth (dark), PR #9; it replaces the L2/D2 spiral waves from #8. Hero photos fade with masks.
  - Tagline "Land · Living · Legacy" in the header (folds on scroll) and the footer, not in the hero; left hero leaf nudged clear of the text at tablet and phone widths.
  - Full-bleed leaves (PR #9): every cut-out's cropped edge sits on the screen edge at all widths.
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
8. Approval to merge #9, and to say when the site leaves test mode for real tenants.
9. CCTV system brand/model (for Phase 5).

## Known issues and limitations

- Lighthouse and axe-core haven't been run (they couldn't be installed in the cloud sandbox). Run them on the live site or the current PR preview.
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
- **Scheduled task:** the "next 21st.dev components" task (drag-to-close filter sheet and scroll reveal) was done early, on 27 Nov 2026, on `review/responsive-ux` instead of `review/botanical`, and its 08:00 run was cancelled. No scheduled tasks remain.

## Next suggested steps

1. The owner reviews the PR #9 preview (new backgrounds) on phone, tablet and desktop.
2. Run Lighthouse and axe on the preview and fix anything real.
3. Fill in `CONTACT`, set up Netlify Forms notifications, then do one end-to-end test enquiry agreed with the owner.
4. Replace placeholder media as it arrives (with responsive images).
5. Batch-merge with approval and go live; then the own domain.

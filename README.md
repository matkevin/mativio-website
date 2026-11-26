# Mativio website

Mativio, family-owned homes for rent in North Bengaluru. *Land · Living · Legacy.*

- **Live (production):** https://mativio-website.netlify.app (deploys from `main`)
- **Repository:** https://github.com/matkevin/mativio-website
- **Current development branch:** `review/responsive-ux`, PR #8, preview https://deploy-preview-8--mativio-website.netlify.app
- **Status:** test mode; changes are reviewed on deploy previews and shipped to `main` in batches with owner approval. See `docs/project-status.md`.

Working rules for contributors and Claude Code are in **`CLAUDE.md`**.

## What the site does (Phase 1)

- Showcases the family's homes, with status: Available now, Available soon, Under construction, Under renovation, Currently occupied.
- One shareable link per home (`/homes/<id>/`) with a rich WhatsApp/social preview.
- Search, filters, sort, grid/list view and paging for many listings.
- Property details: gallery with lightbox, 360° tour and video tabs (content pending), amenities, location with Google Maps link, neighbourhood guide.
- Book a viewing (in person or video call, day + time slot in IST), ask a question, notify me / register interest, "not finding the right home?" requirement alerts, contact form.
- Locality pages, Our Story, Privacy Policy, Terms of Use, 404, offline and loading states.
- Light (default) and dark themes, remembered per visitor.

Full journeys are in `docs/user-journeys.md`.

## Architecture

| Layer | Choice |
|---|---|
| Pages | One static `index.html` with inline CSS, markup and vanilla JS; hash routing (`location.hash` → `route()`), views are `<section data-view="…">` toggled with `.on` |
| Data | JS constants in `index.html`: `CONTACT`, `P` (listings), `ST` (statuses), `CTA` (status → action), `LOC` (localities), `NB` (neighbourhood guide), `VIEWING` (bookable days and times) |
| Share pages | `tools/build-home-pages.mjs` (Node, no dependencies) reads `P` and writes `homes/<id>/index.html` with Open Graph tags, which redirect to `/#p-<id>` |
| Forms | Netlify Forms: `enquiry`, `notify`, `requirement`, `contact` (hidden skeleton forms in the HTML for detection; honeypot `bot-field`; JS posts `application/x-www-form-urlencoded` to `/`) |
| Fonts | Google Fonts: Cormorant Garamond 500/600, Manrope 400–700 (`display=swap`) |
| 360° viewer | Pannellum 2.5.6 from cdnjs, loaded on demand only when a tour exists |
| Maps | Google Maps short links per home (`p.map`); no embedded map API |
| Hosting | Netlify, production branch `main`, deploy previews for PRs |
| Build | None. No package.json, no bundler |

There's no backend or database yet. Phase 2 (admin) proposes Supabase; see `docs/product-roadmap.md`.

## Repository structure

```
/
├── index.html                 # the whole site (styles, markup, data, scripts)
├── 404.html                   # Netlify's page for unknown paths
├── homes/<id>/index.html      # generated share pages (do not hand-edit)
├── assets/
│   ├── logo.png               # Mativio "M" monogram (used as the first letter of the wordmark)
│   ├── photos/                # hero, card and gallery photos (*_l light theme, *_d dark theme)
│   └── leaves/                # botanical leaf cut-outs (transparent PNG)
├── tools/
│   ├── build-home-pages.mjs   # builds homes/<id>/ share pages from P
│   └── audit/                 # Playwright responsive/a11y/regression scripts (see below)
├── docs/                      # handover documentation
├── CLAUDE.md                  # permanent instructions for Claude Code
└── .claude/skills/ui-ux-pro-max/  # Claude skill (on main via PR #7; not yet on review branches)
```

## Run locally

No install is needed. Either open `index.html` directly, or serve the folder so `/homes/<id>/` links resolve:

```bash
python3 -m http.server 8080   # then open http://localhost:8080/#home
```

Forms only deliver on Netlify; locally the post fails and the site shows its "couldn't send" fallback, which is expected.

### Rebuild share pages (after any change to `P`)

```bash
node tools/build-home-pages.mjs
```

### Audit and regression scripts (Python + Playwright)

```bash
python3 tools/audit/measure.py index.html /tmp/audit-out     # 12 widths × light/dark × 12 views: type sizes, header, overflow, touch targets, contrast; screenshots
python3 tools/audit/functional.py index.html                 # filters, sheet, drawer, gallery, viewing form, sticky CTA (POSTs intercepted)
python3 tools/audit/phone_test.py index.html                 # what phone number the enquiry form would send
python3 tools/audit/drawer_reveal_test.py index.html /tmp/dr  # drag sheet (half/full/close, keyboard) and scroll reveals, both themes
```

The scripts block Google Fonts, so screenshots use fallback fonts; computed sizes are unaffected. Lighthouse and axe haven't been run yet; run them on a deploy preview.

## Netlify configuration

There's no `netlify.toml`; the site is configured in the Netlify UI (confirm there before changing anything):

- Site: `mativio-website`. Production branch: `main`. No build command; publish directory is the repo root.
- **Deploy previews** are built for pull requests: `deploy-preview-<PR>--mativio-website.netlify.app`. They're free; production deploys cost about 15 credits each, so ship in batches.
- **Forms:** enable *Forms → form detection*, then redeploy once. Add email alerts under *Site configuration → Notifications → Form submission notifications* (owner to set the recipient). Not yet confirmed as done.
- The injected Netlify badge is hidden with CSS (`#nl-badge, .nl-badge, #nl-card, .nl-card`).
- **Own domain:** planned (e.g. mativio.in). When it's added, update `SITE` in `tools/build-home-pages.mjs`, the `og:url`/`og:image` meta tags in `index.html`, and rebuild `homes/`.

## Editing content (in `index.html` `<script>`)

- **`CONTACT`**: `phone`, `whatsapp` (digits with country code, e.g. `919876543210`), `email`, `address`. While empty, the site says details are "to be added", and a failed send offers "Try again". When `whatsapp` or `email` is set, failures also offer "Send on WhatsApp" / "Send by email".
- **`P`**: listings. Fields: `id`, `title`, `name` (locality key), `area`, `addr`, `near`, `map`, `hint`, `units`, `type`, `bhk`, `sqft`, `baths`, `parking`, `furn`, `rent` (number or `null`), `fromPrice`, `deposit`, `status` (`now`, `soon`, `let`, `reno`, `build`), `from` (YYYY-MM-DD), `added`/`listed`, `featured`, `about`, `seo`, `amen[]`, `card[light,dark]`, `photos[]` (names or `{f,title,cat}`), `floorplan`, `tour[]` (`{title,src}` equirectangular 2:1 JPGs), `video` (MP4) or `youtube` (id). Empty or `null` values show as "TBC".
- **`LOC`**: locality pages (`tagline`, `about`, `hl` highlights, `seo`). Homes match a locality by `name`.
- **`NB`**: neighbourhood guide by locality (owner's verified master list; **no distances** until measured).
- **`VIEWING`**: `days` ahead (14), `closed` weekdays (0 = Sunday), `times` (24 h), `taken` slots (`"YYYY-MM-DD HH:MM"`), `zone` (IST).
- Photos: put JPGs in `assets/photos/` and refer to them without `.jpg`.

## Routes (hash links)

`#home`, `#properties`, `#p-<id>`, `#visit-<id>` (book a viewing), `#video-<id>` (video-call viewing), `#enquire-<id>` (ask a question), `#interest-<id>` (notify me / register interest), `#book` (viewing for any home), `#localities`, `#loc-<id>`, `#story`, `#contact`, `#privacy`, `#terms`, `#thanks`; anything else shows the in-page 404.

## Documentation

- `CLAUDE.md`: permanent instructions and working rules
- `docs/brand-guidelines.md`: logo, palette, typography, voice
- `docs/design-system.md`: tokens, breakpoints, components, themes, animations
- `docs/user-journeys.md`: every customer journey and behaviour
- `docs/property-data.md`: verified property information and business rules
- `docs/project-status.md`: branches, done, pending, known issues, dependencies
- `docs/product-roadmap.md`: phases 1–5

# CLAUDE.md — Mativio website: permanent instructions

Read this first, every session. Then read `docs/project-status.md` for where things stand.

## What this project is

**Mativio** is the website of a family that owns and rents out its own homes in North Bengaluru (Devasandra, Coffee Board Layout and Kempapura, Hebbal). Phase 1 is a public showcase: homes, availability, one shareable link per home, enquiries, viewing requests and "notify me" alerts. Later phases add an owner dashboard and tenant portal: rent dues, renewals, maintenance with SLAs, tenant requests and CCTV health. See `docs/product-roadmap.md`.

The owner (repo owner `matkevin`) approves every change that goes live. The site is in **test mode**. The owner will say when it is ready for real tenants.

## Working rules (non-negotiable)

1. **Never push to `main` or merge a PR without the owner's explicit approval.** `main` auto-deploys to production on Netlify.
2. **Work on a `review/*` branch and open a PR.** PR deploy previews are free; use them for review. The current development branch is `review/radial-backgrounds` (PR #9); see `docs/project-status.md`.
3. **Batch changes.** Each production deploy costs about 15 Netlify credits. Collect reviewed work and ship it together when the owner says go.
4. **Don't redesign.** The visual direction, brand, animations, responsive behaviour and journeys are approved. Refine; don't replace. When a task is content-only, don't touch layout, styles, animations or journeys.
5. **Never invent property facts.** Rents, deposits, sizes, bathrooms, dates, distances and photos come only from the owner. Unknown values show as "TBC" or "To be confirmed" (rent `null` shows "Price on request"). See `docs/property-data.md`.
6. **No secrets in the repo**: no API keys, tokens, passwords or form-endpoint credentials. The owner's private financial notes (valuations, forecasts) are **not** project material; never add them to the repo or the site.
7. **Privacy policy:** don't name Netlify (or any host) as the holder of user data. An own domain is coming.
8. **Testing must not send real enquiries.** Intercept POSTs in Playwright (see `tools/audit/`). Don't submit forms on the live site or previews unless the owner asks.
9. **Preserve accessibility** (WCAG 2.2 AA): text contrast ≥ 4.5:1, one H1 per view, labelled fields with linked errors, 44 px touch targets, dialogs that trap and restore focus, reduced motion respected.

## Architecture in one paragraph

A static single-page site. `index.html` holds all the CSS, markup, data and vanilla JavaScript inline; there's no framework and no build step. Views are hash-routed (`#home`, `#properties`, `#p-<id>`, …) and shown or hidden with `[data-view].on`. Listing data lives in JS constants (`P`, `LOC`, `NB`, `VIEWING`, `CONTACT`). `tools/build-home-pages.mjs` generates `/homes/<id>/` share pages with Open Graph previews from `P`. Forms post to Netlify Forms. Hosting is Netlify with deploy previews per PR. Details are in `README.md`.

## Do / don't when editing

- Keep everything in `index.html` unless there's a strong reason; match the existing compact code style.
- Use the CSS tokens (`--bg`, `--card`, `--ink`, `--mute`, `--accent`, `--btn`, `--btnInk`, `--fs-hero`, `--fs-h1`, `--fs-h2`, `--fs-badge`, `--hdr`, `--side`). Don't hard-code colours or font sizes.
- Fonts: Cormorant Garamond for headings, Manrope for body and UI. Always include a fallback (`Manrope,system-ui,sans-serif`).
- After changing `P` (add, rename, reprice, change status), run `node tools/build-home-pages.mjs` and commit `homes/`.
- New statuses must be added to `ST`, the badge CSS, the `CTA` mapping and `tools/build-home-pages.mjs`.
- Check both themes and widths 1440, 1024, 834, 390 and 320 before asking for review (`tools/audit/measure.py`).
- Write in plain British/Indian English (neighbourhood, colour) with ₹ amounts in Indian format (₹1,85,000).

## Git and GitHub notes

- GitHub GraphQL is blocked in Claude Code cloud sessions, so `gh pr create` fails. Open PRs with REST: `gh api repos/matkevin/mativio-website/pulls -f title=... -f head=<branch> -f base=main -F body=@body.md`.
- End commit messages and PR bodies with the attribution lines the harness provides.
- PR descriptions: say what changed, how it was verified, and "review only, do not merge".

## Where to find things

| Need | File |
|---|---|
| Setup, structure, Netlify, editing data | `README.md` |
| Logo, palette, type, voice | `docs/brand-guidelines.md` |
| Tokens, breakpoints, components, animations | `docs/design-system.md` |
| Every customer journey and route | `docs/user-journeys.md` |
| Verified property facts and business rules | `docs/property-data.md` |
| Done / pending / known issues / dependencies | `docs/project-status.md` |
| Future phases | `docs/product-roadmap.md` |

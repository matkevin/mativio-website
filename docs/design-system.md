# Mativio — Design system

These are the values live on `main` (PR #8 merged 26 Nov 2026), plus open review PRs where noted. Everything lives in the `<style>` block of `index.html`. The final block, "Responsive refinement (audit 26 Nov 2026)", holds the shared tokens and wins over earlier rules.

## Theme tokens

Themes switch with `html[data-theme=dark]`, saved in `localStorage["mativio-theme"]` and applied before first paint by an inline script in `<head>`. Light is the default. Both themes use the same components; only the tokens differ.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#F8F5EF` | `#142235` | Page background |
| `--bgArt` | Radial Mist (two CSS radial gradients) | Radial Depth (two CSS radial gradients) | Page background art (see "Page background") |
| `--bg2` | `#f3e9da` | `#0f1b2b` | Tint mixed into the Bengaluru banner surface |
| `--card` | `#FFFFFF` | `#1D2D40` | Surfaces: cards, forms, filter panel |
| `--ink` | `#142235` | `#F2EEE5` | Primary text |
| `--mute` | `#525A58` | `#B6BFCA` | Secondary text |
| `--line` | `#e7dac6` | `#2c3f58` | Borders, dividers |
| `--accent` | `#80613C` | `#C5AD83` | Accent text, links, rules, focus ring |
| `--btn` | gold gradient `#c9a66c→#ad8a52` | `#d8bb88→#c5a46c` | Primary button fill |
| `--btnInk` | `#fff` (white) | `#142235` (navy) | Primary button text (owner's choice; light-mode contrast is an accepted exception, see below) |
| `--field` | `#fffdf9` | `#13243a` | Inputs |
| `--footer` | navy | `#0b1420` | Footer background |
| `--shadow` | warm brown, soft | black, soft | Elevation |
| Fixed | `--navy #142235`, `--gold #C5AD83`, `--ivory #F2EEE5`, `--olive #454C47` | | Brand constants |

On production `main`, the light values were `--bg #f8f1e6`, `--card #fffaf3`, `--mute #5d6570`, `--accent #a9874f`, and the dark values were `--card #182a40` and `--mute #aab3be`. These were changed in PR #8 for contrast and to match the brief. PR #8 also briefly set the light `--btnInk` to navy; at the owner's request (26 Nov 2026) it is back to white, as in PR #6. White on the gold gradient is 2.3–3.2:1, so primary buttons in light mode are a known, owner-accepted exception to AA text contrast.

Status badges (`.badge` + class):

| Status | Class | Light bg / text | Dark bg / text |
|---|---|---|---|
| Available now | `b-now` | `#4a5a3f` / `#f2eee5` | `#3f5143` / `#e9f0e4` |
| Available soon | `b-soon` | `#f1dcb4` / `#5b4318` | `#d9bd8a` / `#2b2112` |
| Currently occupied | `b-occ` | `#e3e0da` / `#4d4f52` | `#3a4658` / `#dfe4ea` |
| Under construction | `b-build` | `#f3e3c4` / `#6a4a12` | `#7a5a24` / `#fbefd8` |
| Under renovation | `b-reno` | `#e6dcf0` / `#4b2d6b` | `#5a4670` / `#f1e9fa` |

All badges pass AA (5.5–6.9:1).

## Typography tokens (fluid)

| Token | Desktop ≥ 1200 | Tablet 600–1199 | Mobile < 600 |
|---|---|---|---|
| `--fs-hero` (home H1) | `clamp(76px,5.9vw,88px)` | `clamp(56px,6.2vw,64px)` | `clamp(40px,11.5vw,48px)` |
| `--fs-h1` (page titles) | `clamp(56px,4.3vw,64px)` | `clamp(44px,5.4vw,48px)` | `clamp(36px,9.6vw,40px)` |
| `--fs-h2` (section titles, `.ctitle`) | `clamp(44px,3.2vw,48px)` | `clamp(36px,4.4vw,40px)` | `clamp(30px,8.4vw,34px)` |
| H3 / card title | `clamp(24px,2.4vw,30px)` | | 24 px |
| Body | 16 px / 1.6 | | |
| Buttons | 16 px, 600 | | 17 px hero CTA |
| Inputs | 16 px minimum (prevents iOS zoom) | | |
| Metadata | 13–14 px | | |
| `--fs-badge` | 12 px | | |
| Eyebrow `.tag` | 12–13 px, 600, letter-spacing .3em, uppercase | | |

Headings use Cormorant Garamond 500, line-height 1.05, `text-wrap: balance`. Body and UI use Manrope with a system fallback. Each view has **exactly one H1**.

## Breakpoints and layout

Side padding `--side`: 80 px (≥ 1440), 48 (≤ 1439), 32 (≤ 1279), 24 (≤ 1023), 20 (≤ 833), 16 (≤ 374). Content max-width is 1440 px (`.wrap`). Header height `--hdr` is 84 px on desktop, 72 on tablet (≤ 1199) and 64 on mobile (≤ 833).

| Range | Behaviour |
|---|---|
| ≥ 1366 | Header shows the wordmark plus the "LAND · LIVING · LEGACY" tagline (folds away on scroll) |
| ≥ 1024 | Full navigation: Home, Properties, Localities, Our Story, Contact · theme switch · "Book a viewing" |
| 1024–1199 landscape and desktop | Hero split ≈ 42% copy / 58% photo; the photo bleeds to the right edge and fades into the page |
| 834–1199 portrait | Hero stacks: copy first, then a full-width photo |
| 834–1023 | Compact navigation: menu button, theme switch, "Book" |
| ≤ 1100 | Brand pillars in a 2 × 2 grid with descriptions (4 across above that) |
| ≤ 833 (mobile layout) | Hamburger menu; round theme button in the header; full-bleed photo hero under a transparent header; property cards one per row (home page cards scroll horizontally); availability chips in one swipeable row; filters in a bottom sheet |
| ≤ 599 | Full-width hero CTA; sticky bottom action bar on property details, shown **only while the page's own action buttons are off screen** (see Components) |

Property listing grid: 3 columns on desktop, 2 on tablet, 1 on mobile. Card image ratio is 1.6:1. The Properties page shows 9 homes per page with "Show more", in grid or list view (`localStorage["mativio-view"]`). The home page shows up to 6 homes.

## Components

- **Buttons:** `.btn` is a pill (radius 999 px), min-height 52 px, gold gradient, white text in light mode and navy in dark; on hover it brightens and lifts 1 px. `.btn.line` is outlined with an accent border. `.link` is a text link with an accent underline, min-height 44 px.
- **Pills/chips:** `.pill`, 44 px high, used for availability filters (with counts), gallery tabs and segmented choices. The selected pill is navy (gold in dark).
- **Property card (standard, use everywhere):** photo → status pill (left) + furnishing (right) → title → locality → rent ("₹32,000 / month" or "Price on request") → three stats (Bathrooms* · Parking · Owner rental "Direct") → "View property details" → status action (see `docs/property-data.md`).
- **Home-page mini card (`.mini`):** photo → title + status pill → availability or rent → details. **≤ 1199 px:** the pill sits on the photo's top-left corner so the title gets the full width (owner feedback, 27 Nov 2026). Pills never shrink (`flex:none`).
- **Button labels never wrap on phones:** the Our Story "Get to know us" button uses tighter padding (≤ 599 px: `0 20px`; ≤ 374 px: `0 16px`, 15 px text). The notify-form button takes its own full-width row (≤ 599 px). Action-row buttons (`.dacts`) tighten at ≤ 374 px. Check with a wrap scan at 430/390/360/320 when adding buttons.
- **Property details header (phones ≤ 599 px):** the status badge sits on its own line above the address instead of beside it. **≤ 374 px:** the four key facts become a 2 × 2 grid.
- **Sticky phone action bar (`#mcta`, ≤ 599 px, property details):** rent and the status action ("Book a viewing" / "Register interest" / "Notify me"). An IntersectionObserver (`watchCTA()`) watches the in-page buttons marked `data-pcta`: the main action button and, for homes that aren't available, the notify form's submit button. The bar slides out (`.off`: `translateY(110%)`, then `visibility:hidden`, `inert`, `aria-hidden`) while any of them is on screen, and slides back in once they're all off screen. It works from the real viewport height, so short and tall phones behave correctly. Mark any new in-page equivalent of the bar's action with `data-pcta`.
- **Header:** sticky; becomes translucent with blur and a hairline on scroll; the wordmark folds (see Animations).
- **Mobile menu (`#drawer`):** full-screen navy dialog (`role=dialog`, `aria-modal`) with links, "Book a viewing" and a dark-mode switch. Focus moves in and is trapped; Esc and the close button restore focus.
- **Filters:** a search field; availability chips; selects for Locality, Type, Size, Furnishing, Budget and Sort; a result count; a grid/list toggle. On mobile the selects live in a **drag-to-close bottom sheet** (`#sheet`, which becomes a dialog when open) with Reset and Show, and the "Filters" button shows the active count. The sheet opens at **half** height (55% of the screen, at least 320 px, with Reset and Show always visible). Dragging the handle or header up snaps it to **full** (86%); a fast or long drag down closes it. The handle (`#fGrab`) is a button, so Enter or a tap toggles half/full. Esc, the close button, the scrim and Show also close it. It was inspired by 21st.dev "Drawer" (wensity) and written in vanilla JS.
- **Gallery:** swipeable slider with dots; tap, click or Enter opens the **lightbox** (`.lb`, modal: arrows, swipe, Esc, focus returned). The Photos tab has category chips. It was adapted from 21st.dev "Image Gallery" and rewritten without React.
- **Time-slot picker (`#tsp`):** a strip of the next 14 days plus that day's times, keyboard navigable (arrow keys), showing the IST note. It was adapted from 21st.dev "Time Slot Picker" without React.
- **Forms:** labelled fields (`.fld`), errors in `.err` shown with `.fld.bad` and linked by `aria-invalid` + `aria-describedby`, and a country-code picker with each phone field (`.tel select.cc`). Flow: review step, then "Sending…" (aria-busy), then the confirmation page.
- **Tabs on property details:** Overview, Photos, 360° Tour, Video, Location, Neighbourhood.
- **Pillars:** an icon plus title plus line, with thin dividers.
- **Bengaluru banner, Our Story band, footer.**
- **System states:** loading shimmer, empty results, offline banner (`#offline`), in-page 404.
- **Skip link:** "Skip to content", visible on focus; it moves focus to the view's heading.

## Page background (owner-approved, 27 Nov 2026)

The page sits on a subtle radial gradient from the owner's "Subtle Background Variations" board: **L4 Radial Mist** in light mode and **D4 Radial Depth** in dark mode. It replaced the L2/D2 spiral waves that shipped in PR #8.

- `--bgArt` holds two CSS radial gradients per theme, with no image files:
  - **Light:** an ivory mist (`#FCFAF5`) centred left of middle (36% 44%), fading over cream `#F7EFE3` to champagne `#F2E6D3` at the edges.
  - **Dark:** a steel-blue glow (`#223A53` at 80%) at 34% 42%, over deep slate `#13223A`, fading to midnight navy `#0E1B2E` at the edges.
- `body::before` is a fixed, full-viewport layer (`z-index:-1`, `pointer-events:none`) showing `var(--bgArt)` over `var(--bg)`. It stays put while content scrolls, so every view gets the same backdrop. `--bg` is still the fallback and the colour used by the translucent header.
- Hero photos fade into the background with **CSS masks**, not colour overlays, so they blend in without a visible box (desktop split hero, tablet-portrait stacked hero, mobile full-bleed hero).
- **Contrast:** all text that sits directly on the background keeps ≥ 4.5:1 (≥ 3:1 for large text), measured against the rendered pixels in both themes at 1440/834/390 across 10 views. If you change `--bgArt`, re-check: `tools/audit/measure.py` only reads CSS colours and can't see gradients.

**Full-bleed leaves (27 Nov 2026).** Each cut-out has flat cropped edges where the photo was cut. Those edges must sit on the **screen edge**, not the content column, so the leaves look as if they grow in from outside the screen at every width (including > 1440 px):

| Leaf | Cropped edges | Rule |
|---|---|---|
| `.lf-a` (`d_tl`, hero top-left, > 1100 px) | left, top | `left: calc(50% - 50vw - 30px)`; the top crop fades with a mask |
| `.lf-c` (`d_l`, hero left) | left | ≥ 1280: `left: calc(50% - 50vw - 10px)`; 834–1279: `-118px`; phones: beside the "Our Properties" heading |
| `.lf-b` (`t_br`, pillars right, > 833 px) | bottom | turned −90° about its bottom-right corner so the crop faces the right screen edge: `right: calc(50% - 50vw - 4px)`, `bottom:-10px`, `aspect-ratio:224/320` (needed so the lazy image loads); 118 px wide ≤ 1100 |
| `.lf-s` (`t_l`, Our Story) | left | `left: calc((min(100vw,1440px) - 100vw)/2 - var(--side) - 16px)` (its section isn't centred) |
| `.lf-m` (`m_tr`, phone hero top-right) | right, top | `right: calc(50% - 50vw - 10px)`; the top crop fades with a mask |
| `.lf-f1` / `.lf-f2` (footer) | left / both | the footer is full width; the left crop of `.lf-f2` fades with a mask |

`calc(50% - 50vw)` is the distance from a centred containing block to the screen edge. `body{overflow-x:clip}` stops the bleed causing sideways scroll.

## Botanical theme (approved, PR #6)

Real photographic leaf cut-outs (`assets/leaves/*.png`, classes `.lf .lf-a/-b/-c/-s/-m`) are absolutely positioned around the hero, the pillars and the banner. They're non-interactive (`pointer-events:none`, `aria-hidden`) and dimmed in dark mode (`opacity .6; brightness .55`). The spiral-wave page background (above) sits behind them. Keep this restrained; don't add drawn leaves or heavier gradients.

## Animations (approved; keep exactly)

| Element | Behaviour |
|---|---|
| Wordmark fold | "ATIVIO" and the header tagline collapse with `grid-template-columns: 1fr → 0fr` (0.8 s `cubic-bezier(.4,0,.2,1)`), with opacity fading over 0.55 s after a 0.15 s delay. This animates to the exact letter width whatever the font (it fixed the missing "O" bug). The M image shrinks from 42 to 38 px |
| Fold trigger | Collapses when `scrollY > 80` and re-expands when `< 16` (hysteresis, rAF-throttled) |
| Header | Background and shadow transition 0.5 s; blur 12 px when scrolled |
| View change | `fade`: 0.4 s, opacity 0→1, translateY 8 px→0 |
| Buttons | Hover: `brightness(1.05)` and `translateY(-1px)` |
| Loading | Shimmer keyframes on placeholders |
| Lightbox | Opens from the tapped photo; slides between photos |
| Scroll reveal | Home pillars, home cards, the Bengaluru banner, the story band, Our Story blocks, locality tiles and neighbourhood groups fade in and rise 16 px (opacity 0.6 s, transform 0.7 s, staggered 70 ms within a row) as they enter the viewport. It uses IntersectionObserver plus a MutationObserver, so newly rendered items are picked up. The hero is never hidden. JS adds `.rvon` to `<html>` only when motion is allowed. Inspired by 21st.dev "Reveal" (klyv-ui) |
| Filter sheet | Height animates 0.32 s between snap points; follows the finger while dragging |
| Reduced motion | `prefers-reduced-motion: reduce` turns off all animations and transitions, and scroll reveals are not applied at all |

## Accessibility baseline (verified 26 Nov 2026, PR #8)

- Contrast: 0 failures across 288 checks (12 widths × 2 themes × 12 views).
- One H1 per view, skip link, visible focus ring (2 px accent, 3 px offset).
- Touch targets ≥ 44 px, except footer links at 41 px wide (AA requires 24 px).
- Dialogs trap and restore focus; Esc closes them.
- Errors are announced through `aria-describedby`; the viewing-type group and time picker are labelled.
- No horizontal overflow from 320 to 1920 px.
- Still to run: Lighthouse and axe on a deploy preview, a real screen-reader pass and 200% zoom.

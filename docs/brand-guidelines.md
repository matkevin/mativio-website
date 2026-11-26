# Mativio — Brand guidelines

Source: the owner's brand board (Nov 2026), the first brand draft and approved website decisions. **The brand is approved; don't change it.**

## Name and lockups

- Public brand: **MATIVIO**, always in capitals in the wordmark. Write "Mativio" in running text.
- Tagline: **LAND · LIVING · LEGACY** (capitals, middle dots, wide letter-spacing). It appears in the **header** (wide screens, folding away on scroll) and the **footer**, but not in the home hero (owner's decision, 27 Nov 2026).
- Headline: *Rooted in Bengaluru. Built for Generations.*
- Hero line: **Find a place to call home.** Supporting line: *Family-owned homes, thoughtfully cared for in Bengaluru.*
- Brand promise: a family legacy of thoughtfully owned properties, enduring value and a vision for the future.

## Logo

- The mark is a serif **"M" with a sweeping stroke** (`assets/logo.png`). The owner particularly likes it being **the first letter of the wordmark**: the site renders the image M followed by the text "ATIVIO" in Cormorant Garamond. Never redraw, recolour or distort the M.
- **Header behaviour (approved):** the wordmark (M + ATIVIO) and, on wide screens, the "LAND · LIVING · LEGACY" tagline beside it fold away on scroll so only the M remains, then unfold near the top. See `docs/design-system.md` → Animations.
- Variants on the brand board: gold on navy (dark), navy on ivory (light), and app icons (M on a navy square, M on an ivory square). The site uses the same `logo.png` in both themes.
- Favicon: `assets/logo.png`.

## Colour palette

| Name | Hex | Use |
|---|---|---|
| Midnight Navy | `#142235` | Primary text (light), dark-theme background, primary navy buttons |
| Champagne Gold | `#C5AD83` | Accent, buttons (gold gradient), dark-theme accent text, dividers |
| Warm Ivory | `#F2EEE5` | Dark-theme text; ivory surfaces (UI board also shows `#F7F5EF`) |
| Heritage Olive | `#454C47` | "Available now" status family |

Accessible web values (from the responsive audit, PR #8):
- Light theme accent **text** is a deeper bronze, `#80613C` (5.2:1 on ivory). Pure Champagne Gold is too light for small text on ivory.
- Gold buttons use **white text in light mode** and **navy text in dark mode** (owner's choice, 26 Nov 2026, restoring the PR #6 styling). White on the light-mode gold is about 2.3–3.2:1, below WCAG AA's 4.5:1; this is an accepted owner exception.

Status colours: Available now = olive; Available soon = gold; Currently occupied = grey; Under renovation = purple; Under construction = amber/bronze. Exact values are in `docs/design-system.md`.

## Typography

| Role | Typeface | Notes |
|---|---|---|
| Editorial headings (H1–H3, wordmark) | **Cormorant Garamond** 500/600 | Close to the logo lettering. No italics, no thin weights |
| Body and UI (text, buttons, forms, labels) | **Manrope** 400–700 | Always with a fallback: `Manrope,system-ui,sans-serif` |

The first brand draft suggested Jost for body text; it was replaced by Manrope per the UI/UX board. Don't reintroduce Jost.

## Imagery

- Real photography of leafy, golden-hour Bengaluru residences; warm and natural.
- **Botanical theme (approved):** real photographic leaf cut-outs (`assets/leaves/*.png`) frame sections. Never use drawn or SVG leaves (rejected as unnatural). In dark mode leaves are dimmed.
- Light/dark photo pairs: `*_l.jpg` for light, `*_d.jpg` for dark.
- Current photos are **placeholders** until the owner supplies real photos, floor plans, 360° images and videos. Artist's impressions (e.g. the #674 elevation) must be labelled as such.

## Voice

- Warm, plain and personal: a family that owns and looks after its homes. "Our family will get back to you."
- Direct owner rental: no brokers ("Owner rental · Direct").
- Honest about availability and unknowns: "Price on request", "To be confirmed", "Viewing times are a preference until we confirm."
- British/Indian English spelling; rupees in Indian grouping (₹1,85,000 / month).

## Brand elements

Four trust pillars (home page): **Family-Owned**, **Thoughtfully Managed**, **Bengaluru Rooted**, **Built for Generations**, each with an icon and a one-line description. Board icon set: Properties, Land, Partnerships, Legacy.

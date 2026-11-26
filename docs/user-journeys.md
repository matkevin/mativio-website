# Mativio — User journeys and functionality

These are the journeys live on `main` (PR #8 merged 26 Nov 2026). All are approved; preserve them. Routes are hash links handled by `route()` in `index.html`.

## Global

- **Header:** logo (to Home) · Home · Properties · Localities · Our Story · Contact · light/dark switch · "Book a viewing". Tablet 834–1023 uses a compact menu; mobile ≤ 833 uses a hamburger plus a round theme button.
- **Theme:** light by default; the choice is remembered on the device and never sent to the server (stated in the Privacy Policy).
- **Footer:** brand, navigation, Privacy and Terms links.
- **Page title and meta description** follow the home or locality being viewed (SEO).
- **System states:** loading shimmer, empty results, offline banner, in-page 404 ("This page isn't here"; for a removed home, "This home isn't listed anymore" with a link to available homes). Netlify serves `404.html` for unknown paths.

## A. Find an available home (primary conversion)

1. **Home** (`#home`): hero "Find a place to call home." with "Explore available homes" and "Get to know us". Then "Our Properties" (up to 6 homes, best first, then "View all N properties"), the four pillars, the Bengaluru/localities banner, the Our Story band and the footer.
2. **Properties** (`#properties`): search, filters and sort (journey D). Cards follow the standard card order.
3. **Property details** (`#p-<id>`): back link; tabs Overview · Photos · 360° Tour · Video · Location · Neighbourhood; gallery with lightbox; title (H1), rent, address and status badge; key facts (size, bathrooms*, parking, owner rental "Direct"); about text; amenities; Google Maps link; neighbourhood guide. The action follows status (see `docs/property-data.md`). On phones an available home shows a **sticky bottom bar** with the rent and "Book a viewing".
4. **Enquire or book** (journeys B and C), leading to the **confirmation** (`#thanks`) with a reference `MTV-xxxx`.
5. The owner follows up by phone, WhatsApp or email to arrange the viewing.

## B. Availability and alerts

- **Available now:** "Book a viewing".
- **Available soon / Under renovation / Under construction:** "Register interest" (`#interest-<id>`), which scrolls to the inline form on the details page.
- **Currently occupied:** "Notify me" (`#interest-<id>`). The form says "Currently occupied. Want to know first?"
- **Notify form** (Netlify form `notify`): name*, mobile* (with country code), optional email. It sends `home, name, phone, email`, then shows a thank-you and disables the form. On failure it says "We couldn't save this just now…".
- **Not finding the right home?** (Netlify form `requirement`) on Properties: locality, size, budget, move-in, name*, mobile*. It sends a matching-home alert request.

## C. Book a viewing

Routes: `#visit-<id>` (pre-selects the home and in-person viewing), `#video-<id>` (pre-selects a video call), `#book` (any home, with a home picker), `#enquire-<id>` (pre-selects "Ask a question").

1. Choose the home (pre-selected from a listing). The sub-line shows "Name · BHK · rent".
2. "I'd like to": **Book a viewing** or **Ask a question**.
3. Viewing type: **In person** or **Video call (remote)**.
4. Pick a **day** (next 14 days) and a **time** from `VIEWING.times`, labelled **India Standard Time (IST)**. Past or taken slots are unavailable.
5. Name*, phone* (country-code picker, +91 by default), optional email, and a message (required, 10+ characters, for "Ask a question").
6. **Inline validation:** errors show under each field, focus moves to the first error, and errors are announced. Phone rules: India 10 digits starting 6–9; other countries 6–14 digits; a number typed with "+" picks its own country code.
7. **Review step:** "Check your details" with Edit or "Confirm viewing request" / "Send enquiry", plus the consent line linking to the Privacy Policy.
8. **Sending…** (button busy), then Netlify form `enquiry` with `home, ref, kind, viewing_type, date, slot, name, phone (international format), email, message`.
9. **Success:** "Viewing requested!" or "Enquiry received!", with the reference and a summary. It says "We'll call you to confirm the viewing time" (or "…send a video-call link") within 1 business day. **The chosen time is a preference until the owner confirms.** The form resets.
10. **Failure:** "Almost there, <name>". The values are kept. If `CONTACT.whatsapp` or `CONTACT.email` is set, it offers "Send on WhatsApp" / "Send by email" with the request pre-written; otherwise "Try again" re-submits.

## D. Search and filtering

1. Search by property name or locality.
2. Availability chips with counts: All · Available now · Available soon · Under construction · Occupied. On mobile they're one swipeable row.
3. Filters: Locality, Property type, Home size, Furnishing, Budget. On mobile they're in a bottom sheet that opens at half height; drag up for full height, drag down to close (the handle is also a button). It has Reset and Show, and an active-filter count on the "Filters" button.
4. Sort: **Relevance** (default: available now, then soon, renovation and construction, then occupied; search matches and `featured` homes rise; then newest), Latest, Available soonest, Rent low→high, Rent high→low.
5. Grid or list view (remembered); 9 per page with "Show more".
6. Empty results show a message and the requirement form.
7. **Filters persist** when you open a home and come back.

## E. Share a home

- Each home has a clean link `/homes/<id>/` with its own preview (title, BHK, rent or "Price on request", status, furnishing, photo) for WhatsApp and social apps. It redirects to `/#p-<id>`.
- Hash links `#p-<id>` are also shareable.
- These are generated by `node tools/build-home-pages.mjs`.

## F. Localities

- `#localities` lists Devasandra, Coffee Board and Kempapura.
- `#loc-<id>` has a tagline, description and highlights ("Ideal for…"), then the **neighbourhood guide** (education, healthcare, lifestyle, business, parks, connectivity; no distances shown until measured), then "Homes in <locality>".

## G. Brand and company

- **Our Story** (`#story`): "Rooted in Bengaluru. Built for Generations." with the family narrative and pillars.
- **Contact** (`#contact`): "Get in Touch", contact lines (phone and email show "to be added" until `CONTACT` is filled in), and the contact form (Netlify form `contact`: name*, email*, message*). If sending fails and an email is configured, it opens the visitor's email app with the message ready.
- **Privacy Policy** (`#privacy`) and **Terms of Use** (`#terms`): approved and dated 26 November 2026; written for India's DPDP Act 2023 and Rules 2025 (consent, withdrawal, grievance response within 90 days, breach notice, nominee). Viewing times are a preference until confirmed. There are no bookings or payments on the site. **No host is named as the holder of user data.**

## Keyboard and assistive technology

- Skip link; visible focus everywhere.
- Gallery: Tab to it, Enter opens the lightbox, arrows move between photos, Esc closes.
- Menu and filter sheet are modal dialogs; the time picker supports arrow keys.
- Errors are linked to their fields; `role=status` notes for the notify and requirement forms.
- Reduced motion is respected.

## Testing note

Use `tools/audit/functional.py` and `phone_test.py`. They intercept POSTs, so **no real enquiries are sent**.

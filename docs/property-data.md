# Mativio — Property data and business rules

**Source of truth:** the `P`, `LOC` and `NB` constants in `index.html`, as confirmed by the owner up to 26 Nov 2026. Never add or change a fact (rent, deposit, size, bathrooms, dates, distances, photos) without the owner confirming it. Private financial analysis (valuations, forecasts, plot sizes) is deliberately **not** recorded here or anywhere in the repo.

## Listings

| `id` | Title | Locality / address | Units | Rent | Status | Notes |
|---|---|---|---|---|---|---|
| `devasandra` | Devasandra Residence | Devasandra, off New BEL Road, near Mathikere, North Bengaluru (**not** the K R Puram Devasandra). Map: https://maps.app.goo.gl/Pbh5tyYMyPwbS9TV8 | 2 × 2 BHK apartments, **1 available now** | ₹32,000 / month per apartment | `now` (Available now) | Semi-furnished; 2 car parking spaces; near Ramaiah Institute of Technology, Ramaiah Medical College and Ramaiah Memorial Hospital |
| `coffee-board` | Coffee Board Residence, #568 | #568, Coffee Board Layout, Hebbal Kempapura, Bengaluru 560024 | 3 × 3 BHK apartments | ₹40,000 / month each | `let` (Currently occupied) | Semi-furnished; each has 1 bathroom + 1 separate toilet; building has 3 car spaces plus bike parking. Map pin still to be supplied |
| `coffee-board-1hk` | Coffee Board Residence, #568 (1 HK) | Same building as #568 | 1 × 1 HK (hall + kitchen) | ₹20,000 / month | `let` | Semi-furnished; 1 toilet; shares the building's car and bike parking |
| `coffee-board-674` | Coffee Board Residence, #674 | #674, Coffee Board Layout, Hebbal Kempapura, Bengaluru 560024. Map: https://maps.app.goo.gl/1DsC1DBcLu2BLS2V6 | New building: 2 × 2 BHK + 5 × 1 BHK (7 apartments) | `null` → "Price on request" | `build` (Under construction) | `featured`. Photos `cof674`, `cof674_wide` are the **artist's impression / elevation**. Furnishing, parking and ready date TBC. Rents will be announced closer to completion |
| `kempapura` | Kempapura Hostel | 1st Cross Road, Vinayaka Layout 2nd Stage, Hebbal Kempapura, Bengaluru 560024; near Treat restaurant. Map: https://maps.app.goo.gl/YaLAnFr4UK3qQGUf6 | Whole hostel building: 30 rooms with hostel dining | ₹1,85,000 / month for the whole building | `let` | **Leased as one unit**; bike parking only (no cars); semi-furnished; Presidency College and St Mary's College close by |

All homes are semi-furnished with parking (owner, 24 Nov 2026), except #674, which is TBC while under construction.

### Not yet supplied (show as "TBC" / "To be confirmed")

- Deposits for every home.
- Bathrooms for Devasandra and #674, and the built-up area (sq ft) for all.
- Floor plans, real photos, 360° tours and videos for all homes. The current photos are representative placeholders.
- #674 completion and ready date, configuration details, and rents.
- A map pin for #568.
- `CONTACT` phone, WhatsApp and email (also used in the Privacy and Terms contact lines). Address shows "Bengaluru, Karnataka".
- Viewing hours: the current defaults are 14 days ahead, every day, at 10:00, 11:00, 12:00, 15:00, 16:00, 17:00 and 18:00 IST.
- The name of the park in Coffee Board Layout (shown generically).
- Measured walking and driving distances. **No distances are shown** until they're measured from the exact locations.

## Localities (`LOC`)

| `id` | Name | Area line | Tagline | Ideal for |
|---|---|---|---|---|
| `devasandra` | Devasandra | Devasandra, off New BEL Road, near Mathikere, North Bengaluru | Live close to everything | Students, researchers, medical professionals, working professionals, families |
| `coffee-board` | Coffee Board | Coffee Board Layout, Hebbal Kempapura, North Bengaluru | A neighbourhood to call home | Families, working professionals, long-term tenants |
| `kempapura` | Kempapura | Hebbal Kempapura, North Bengaluru | Stay connected to opportunity | IT professionals, corporate employees, college students, hostel residents |

The neighbourhood guide (`NB`) is the owner's verified master list (content audit, 26 Nov 2026):

- **Devasandra:**
  - Education: Ramaiah Institute of Technology, Ramaiah Medical College, Ramaiah University of Applied Sciences, IISc.
  - Healthcare: Ramaiah Memorial Hospital, Ramaiah Medical College Hospital, local clinics and pharmacies.
  - Lifestyle: New BEL Road shopping district, cafés, supermarkets, bakeries, gyms, banks and ATMs.
  - Connectivity: New BEL Road, M.S. Ramaiah Road, Yeshwanthpur Metro, Yesvantpur Junction, BMTC; Mathikere, Sanjaynagar, Dollars Colony and Hebbal.
- **Coffee Board:**
  - Parks: neighbourhood parks, walking areas.
  - Education: Jain Heritage School, Vidya Niketan School, Presidency College, Sindhi College, preschools.
  - Business: Embassy Manyata Business Park, Kirloskar Business Park, Brigade Magnum, Hebbal and Nagawara corridors.
  - Healthcare: Manipal Hospital Hebbal, Aster CMI, Bangalore Baptist.
  - Lifestyle: supermarkets, grocers, restaurants, bakeries, pharmacies, banks, shopping centres.
  - Connectivity: Kempapura Main Road, ORR, Hebbal Junction, Bellary Road, airport corridor; Sahakar Nagar, Amruthahalli and Nagawara.
- **Kempapura:**
  - Business: Manyata, Kirloskar, Brigade Magnum, Hebbal corporate corridor.
  - Education: Presidency College, St Mary's College, Sindhi College, Vidya Niketan, Jain Heritage.
  - Healthcare: Manipal Hebbal, Aster CMI, Bangalore Baptist.
  - Lifestyle: Esteem Mall, Elements Mall, Hebbal Lake, restaurants, supermarkets, fitness centres.
  - Connectivity: Hebbal Flyover, ORR, Bellary Road (NH 44), airport corridor, BMTC and airport buses; Nagawara, Sahakar Nagar and Amruthahalli.

Removed as unverified, so don't re-add them: CV Raman Road, ORR (for Devasandra), Jakkur Lake, Golden Square, Karle Town Centre, St Johns, Eurokids, Rainbow Children's Hospital, and every distance ("0.3 km", "next door"…).

SEO page title: "Mativio — Homes for Rent in North Bengaluru". Each home and locality has an `seo` line used for the meta description and share preview.

## Business rules

| Rule | Detail |
|---|---|
| Statuses (`ST`) | `now` Available now · `soon` Available soon (optional `from` date) · `let` Currently occupied · `reno` Under renovation · `build` Under construction |
| Primary action (`CTA`) | `now` → **Book a viewing** (`#visit-<id>`); `soon`, `reno`, `build` → **Register interest**; `let` → **Notify me** (both `#interest-<id>`) |
| Rent display | Number → "₹32,000 / month" (Indian grouping); `fromPrice:true` → "from ₹…"; `null` → **"Price on request"** |
| Unknown values | Empty or `null` → "TBC"; deposit "To be confirmed"; the bathrooms stat carries an asterisk until confirmed |
| Multi-unit buildings | One listing per unit type (#568 3 BHK and #568 1 HK are separate). `units` and `hint` describe counts and availability |
| Whole-building lease | The Kempapura hostel is let as a single unit; don't list rooms individually |
| Owner rental | Every home is rented directly by the family ("Owner rental · Direct"); no brokers |
| Viewing times | Preferences until the owner confirms; always shown in IST |
| No transactions | No bookings, deposits or payments are taken on the site (Terms §3) |
| Phone numbers | Stored in international format (`+91 9845012345`, `+44 7700900123`) |
| Enquiry reference | `MTV-` + 4 random digits, shown to the visitor and sent with the form |
| Relevance sort | Available now → soon → renovation/construction → occupied; then search match, `featured`, newest (`added`/`listed`) |
| Photos | Light/dark pairs `*_l`/`*_d`; label artist's impressions; one or more `tour` panoramas (2:1 equirectangular) or `video`/`youtube` enable those tabs, otherwise they show "coming soon" |
| Share pages | Regenerate `homes/` after any change to `P` |

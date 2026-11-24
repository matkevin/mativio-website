# mativio-website
Mativio for Property Rental Solutions

A static site: open `index.html` in a browser. No build step. Light theme by default, with a dark theme toggle (the visitor's choice is remembered).

- `index.html`: the page (styles, listings data and scripts are inline)
- `assets/logo.png`: the Mativio "M" monogram (the wordmark reads M + ATIVIO and collapses to the M on scroll)
- `assets/photos/`: property and hero photos (`*_l.jpg` shown in light theme, `*_d.jpg` in dark)

## Editing
At the top of the `<script>` in `index.html`:

- `CONTACT`: phone, WhatsApp and email. When `whatsapp` or `email` is filled in, enquiries get a "Send on WhatsApp" / "Send by email" button. Until then the site says enquiries are not delivered yet.
- `P`: the listings. `status` is `"now"` (Available), `"soon"` (Opening Soon) or `"let"` (Occupied). `from` is an optional `"YYYY-MM-DD"` availability date. `card` and `photos` name files in `assets/photos/` (without `.jpg`).

## 360° tours and videos
Each home in `P` has:
- `tour`: a list of 360° photos, e.g. `[{title:"Living room",src:"assets/360/devasandra-living.jpg"}]`. Use equirectangular JPGs (2:1, e.g. 6000×3000) from a 360° camera (Insta360, Ricoh Theta) or a phone panorama app. Several entries give room-to-room buttons.
- `video`: an MP4 path like `assets/video/devasandra.mp4` (keep it under ~20 MB), or `youtube`: a YouTube video id.
Until these are added, the property page shows "coming soon" in the 360° Tour and Video tabs.

## Enquiries (Netlify Forms)
Four forms are sent to Netlify: `enquiry` (viewing requests and questions), `notify` (alerts for one Opening Soon / Occupied home), `requirement` (what a visitor is looking for: locality, size, budget, move-in) and `contact`.
In Netlify: **Forms → Enable form detection**, then redeploy once. Submissions appear under **Forms**; add email alerts under **Site configuration → Notifications → Emails and webhooks → Form submission notifications**.

## Shareable home links
Each home has a clean link, `/homes/<id>/` (e.g. `/homes/devasandra/`), with its own preview (title, rent, photo) when shared on WhatsApp. These pages live in `homes/` and are made by:

    node tools/build-home-pages.mjs

Run it again whenever you add, rename or reprice a home in `P`.

## Listing fields (in `P`)
`title` (card name), `name` (locality), `status` (`now`, `soon`, `let`, `reno`), `rent`, `deposit`, `bhk`, `sqft`, `baths`, `parking`, `furn`, `floorplan`, `photos`, `tour`, `video`/`youtube`. Empty or `null` values show as "TBC".
The main button on cards and pages follows the status: Available now → Book a viewing; Available soon or Under renovation → Register interest; Currently occupied → Notify me.

## Neighbourhood guide
`NB` (in the script) lists nearby colleges, hospitals, shops, transport and business hubs for each locality. It shows on the locality page and in the Neighbourhood tab of each home.

## Localities and legal pages
- `LOC` (in the script, above the listings filters): locality pages with description and highlights. Homes are matched to a locality by name.
- Privacy Policy (`#privacy`) and Terms of Use (`#terms`) are drafts marked "Draft for review"; remove the label once approved.
- `404.html` is shown by Netlify for unknown paths; unknown in-page links show the in-page 404.

## Pages (hash links)
`#home`, `#properties`, `#book` (book a viewing for any home), `#localities`, `#loc-<id>`, `#privacy`, `#terms`, `#p-<id>` (one home, shareable), `#visit-<id>` (book a viewing), `#video-<id>` (book a video-call viewing), `#interest-<id>` (register interest / notify me), `#enquire-<id>` (ask a question), `#story`, `#contact`.

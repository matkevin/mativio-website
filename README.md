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
Three forms are sent to Netlify: `enquiry` (viewing requests and questions), `notify` (alerts for Opening Soon / Occupied homes) and `contact`.
In Netlify: **Forms → Enable form detection**, then redeploy once. Submissions appear under **Forms**; add email alerts under **Site configuration → Notifications → Emails and webhooks → Form submission notifications**.

## Pages (hash links)
`#home`, `#properties`, `#p-<id>` (one home, shareable), `#visit-<id>` (book a viewing), `#enquire-<id>` (ask a question), `#story`, `#contact`.

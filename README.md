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

## Pages (hash links)
`#home`, `#properties`, `#p-<id>` (one home, shareable), `#enquire-<id>`, `#story`, `#contact`.

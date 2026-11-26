// Builds a shareable page for each home at /homes/<id>/ with its own link preview
// (title, rent, photo) for WhatsApp and social apps. Visitors are taken straight to
// the home's page on the site. Run after changing the listings in index.html:
//   node tools/build-home-pages.mjs
import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "node:fs";

const SITE = "https://mativio-website.netlify.app";
const html = readFileSync(new URL("../index.html", import.meta.url), "utf8");
const m = html.match(/const P=(\[[\s\S]*?\n\]);/);
if (!m) throw new Error("Could not find the listings (const P=[...]) in index.html");
const P = Function(`"use strict";return (${m[1]})`)();

const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const inr = n => "₹" + n.toLocaleString("en-IN");
const status = { now: "Available now", soon: "Available soon", let: "Currently occupied", reno: "Under renovation", build: "Under construction" };

const out = new URL("../homes/", import.meta.url);
if (existsSync(out)) rmSync(out, { recursive: true });
for (const p of P) {
  const dir = new URL(`${p.id}/`, out);
  mkdirSync(dir, { recursive: true });
  const title = `${p.title} · ${p.bhk} · ${p.rent == null ? "Price on request" : (p.fromPrice ? "from " : "") + inr(p.rent) + "/month"}`;
  const desc = `${p.seo ? p.seo + " " : ""}${status[p.status]} · ${p.furn}. Family-owned home, rented directly by Mativio.`;
  const img = `${SITE}/assets/photos/${p.card[0]}.jpg`;
  const target = `/#p-${p.id}`;
  writeFileSync(new URL("index.html", dir), `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)} · Mativio</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${SITE}/homes/${p.id}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mativio">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="${img}">
<meta property="og:url" content="${SITE}/homes/${p.id}/">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0; url=${target}">
<script>location.replace(${JSON.stringify(target)})</script>
</head>
<body><p><a href="${target}">View ${esc(p.title)} on Mativio</a></p></body>
</html>
`);
}
console.log(`Built ${P.length} home pages in homes/`);

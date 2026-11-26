"""Responsive + a11y measurement for the Mativio single-page site.
Usage: python3 measure.py <index.html> <out_dir>
"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(sys.argv[1]).resolve().as_uri()
OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
WIDTHS = [1920, 1440, 1280, 1194, 1024, 834, 768, 430, 390, 375, 360, 320]
PAGES = ["home", "properties", "p-devasandra", "p-coffee-board-674", "visit-devasandra",
         "localities", "loc-devasandra", "story", "contact", "privacy", "terms", "nope"]
SHOT_PAGES = {"home", "properties", "p-devasandra", "visit-devasandra"}

JS = r"""
() => {
 const vis = e => { const r = e.getBoundingClientRect(), s = getComputedStyle(e);
   return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && e.closest('[data-view]:not(.on)') === null; };
 const px = v => Math.round(parseFloat(v) * 10) / 10;
 const W = innerWidth, out = {W};
 // overflow
 out.scrollW = document.documentElement.scrollWidth;
 out.overflow = [];
 if (out.scrollW > W + 1) {
   for (const e of document.querySelectorAll('body *')) { if (!vis(e)) continue; const r = e.getBoundingClientRect();
     if (r.right > W + 1 && getComputedStyle(e).position !== 'fixed') { let a = e.parentElement, clipped = false;
       while (a) { const o = getComputedStyle(a).overflowX; if (o === 'hidden' || o === 'auto' || o === 'scroll' || o === 'clip') { clipped = true; break } a = a.parentElement }
       if (!clipped) out.overflow.push((e.tagName + '.' + [...e.classList].join('.')).slice(0, 60) + ' r=' + Math.round(r.right)); } }
   out.overflow = out.overflow.slice(0, 8);
 }
 const hdr = document.querySelector('header'); out.header = hdr ? Math.round(hdr.getBoundingClientRect().height) : null;
 const typ = sel => [...document.querySelectorAll(sel)].filter(vis).slice(0, 3).map(e => { const s = getComputedStyle(e);
   return {t: e.textContent.trim().slice(0, 28), fs: px(s.fontSize), ff: s.fontFamily.split(',')[0].replace(/"/g, ''), fw: s.fontWeight, it: s.fontStyle === 'italic'}; });
 out.h1 = typ('h1'); out.h2 = typ('h2'); out.h3 = typ('h3');
 out.body = typ('main p, [data-view].on p').slice(0, 2);
 const fsSet = sel => [...new Set([...document.querySelectorAll(sel)].filter(vis).map(e => px(getComputedStyle(e).fontSize)))].sort((a, b) => a - b);
 out.btnFs = fsSet('.btn, button.btn, a.btn');
 out.inputFs = fsSet('input:not([type=radio]):not([type=checkbox]):not([type=hidden]), select, textarea');
 out.badgeFs = fsSet('.badge, [class*="b-"]');
 // touch targets
 const small = [];
 for (const e of document.querySelectorAll('a[href], button, input, select, textarea, [role=button], [tabindex="0"]')) {
   if (!vis(e) || e.type === 'hidden') continue; const r = e.getBoundingClientRect();
   if (e.tagName === 'A' && getComputedStyle(e).display === 'inline' && e.closest('p,li')) continue; // inline text links exempt
   if (r.width < 44 || r.height < 44) small.push(((e.getAttribute('aria-label') || e.textContent || e.name || e.tagName).trim().slice(0, 22)) + ` ${Math.round(r.width)}x${Math.round(r.height)}`);
 }
 out.smallTargets = small.length; out.smallEx = [...new Set(small)].slice(0, 8);
 // side padding: left edge of first visible section content
 const sec = [...document.querySelectorAll('[data-view].on .sec, [data-view].on > *')].find(vis);
 if (sec) { const s = getComputedStyle(sec); out.secPad = [px(s.paddingLeft), px(s.paddingRight)]; out.secLeft = Math.round(sec.getBoundingClientRect().left); out.secW = Math.round(sec.getBoundingClientRect().width) }
 // property grid columns
 const cards = [...document.querySelectorAll('[data-view].on .card, [data-view].on article')].filter(vis);
 if (cards.length) { const top = Math.round(cards[0].getBoundingClientRect().top); out.cardCols = cards.filter(c => Math.abs(c.getBoundingClientRect().top - top) < 4).length; out.cards = cards.length;
   out.cardImgRatios = [...new Set(cards.slice(0, 6).map(c => { const i = c.querySelector('img'); if (!i) return null; const r = i.getBoundingClientRect(); return r.height ? Math.round(r.width / r.height * 100) / 100 : null }))]; }
 // hero split
 const hero = document.querySelector('[data-view=home].on .hero, [data-view=home].on .shot');
 const shot = document.querySelector('[data-view=home].on .shot');
 if (shot) { const r = shot.getBoundingClientRect(); out.heroShotPct = Math.round(r.width / W * 100); out.heroShotTop = Math.round(r.top + scrollY); }
 const ctaBtn = document.querySelector('[data-view=home].on .ctas .btn'); if (ctaBtn) out.heroCtaW = Math.round(ctaBtn.getBoundingClientRect().width);
 // contrast (solid backgrounds only)
 const lum = c => { const m = c.match(/[\d.]+/g); if (!m) return null; const f = c.startsWith('color(') ? 1 : 255; const [r, g, b] = m.slice(0, 3).map(v => { v = v / f; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4 }); return .2126 * r + .7152 * g + .0722 * b; };
 const alpha = c => { const a = c.match(/\/\s*([\d.]+)/); if (a) return +a[1]; if (c.startsWith('color(')) return 1; const m = c.match(/[\d.]+/g); return m && m.length > 3 ? +m[3] : 1 };
 const bgOf = e => { while (e) { const s = getComputedStyle(e); if (s.backgroundImage !== 'none') return null; if (alpha(s.backgroundColor) > .9) return s.backgroundColor; e = e.parentElement } return getComputedStyle(document.body).backgroundColor };
 const fails = [];
 for (const e of document.querySelectorAll('[data-view].on *, header *, footer *')) {
   if (!vis(e) || ![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
   const s = getComputedStyle(e); if (alpha(s.color) < .9) continue; const bg = bgOf(e); if (!bg) continue;
   const L1 = lum(s.color), L2 = lum(bg); const cr = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
   const large = parseFloat(s.fontSize) >= 24 || (parseFloat(s.fontSize) >= 18.66 && +s.fontWeight >= 700);
   if (cr < (large ? 3 : 4.5)) fails.push(`${e.textContent.trim().slice(0, 24)} ${cr.toFixed(2)}`);
 }
 out.contrastFails = fails.length; out.contrastEx = [...new Set(fails)].slice(0, 6);
 // a11y basics
 out.imgNoAlt = [...document.querySelectorAll('img')].filter(i => !i.hasAttribute('alt')).length;
 out.unlabeled = [...document.querySelectorAll('input:not([type=hidden]), select, textarea')].filter(vis).filter(i => !(i.labels && i.labels.length) && !i.getAttribute('aria-label') && !i.getAttribute('aria-labelledby')).map(i => i.name || i.id).slice(0, 6);
 out.btnNoName = [...document.querySelectorAll('button, a[href]')].filter(vis).filter(b => !(b.textContent.trim() || b.getAttribute('aria-label') || b.getAttribute('title') || b.querySelector('img[alt]:not([alt=""])'))).length;
 return out;
}
"""

res = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    for theme in ["light", "dark"]:
        for w in WIDTHS:
            ctx = b.new_context(viewport={"width": w, "height": 900 if w > 600 else 844}, device_scale_factor=1)
            ctx.add_init_script(f"try{{localStorage.setItem('mativio-theme','{theme}')}}catch(e){{}}")
            ctx.route("**/fonts.g*/**", lambda r: r.abort())
            pg = ctx.new_page()
            pg.goto(SRC + "#home"); pg.wait_for_timeout(400)
            for page in PAGES:
                pg.evaluate(f"location.hash='{page}'"); pg.wait_for_timeout(250)
                pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(100)
                res[f"{theme}|{w}|{page}"] = pg.evaluate(JS)
                if page in SHOT_PAGES and (theme == "light" or w in (1440, 834, 390)):
                    pg.screenshot(path=str(OUT / f"{theme}_{w}_{page}.png"))
            ctx.close()
    b.close()
(OUT / "metrics.json").write_text(json.dumps(res, indent=1))
print(len(res), "measurements")

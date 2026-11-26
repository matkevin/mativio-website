"""Functional + keyboard checks. No real form submissions (network to Netlify is blocked/intercepted)."""
import pathlib, sys, json
from playwright.sync_api import sync_playwright
SRC = pathlib.Path(sys.argv[1]).resolve().as_uri()
R = {}
def t(name, fn):
    try: R[name] = fn()
    except Exception as e: R[name] = f"ERROR {e}"[:160]
with sync_playwright() as p:
    b = p.chromium.launch()
    # mobile
    c = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    posted = []
    c.route("**/fonts.g*/**", lambda r: r.abort())
    pg = c.new_page()
    pg.on("request", lambda rq: posted.append(rq.url) if rq.method == "POST" else None)
    pg.route("**/*", lambda r: r.fulfill(status=200, body="ok") if r.request.method == "POST" else r.continue_())
    pg.goto(SRC + "#properties"); pg.wait_for_timeout(400)
    # filter chip -> detail -> back
    def persist():
        pg.locator("[data-view=properties] .pill", has_text="Occupied").first.click(); pg.wait_for_timeout(200)
        before = pg.locator("[data-view=properties].on .card:visible, [data-view=properties].on article:visible").count()
        pg.locator("[data-view=properties].on .card a, [data-view=properties].on article a").first.click(); pg.wait_for_timeout(300)
        h = pg.evaluate("location.hash"); pg.go_back(); pg.wait_for_timeout(300)
        pressed = pg.locator("[data-view=properties] .pill[aria-pressed=true]").first.inner_text()
        after = pg.locator("[data-view=properties].on .card:visible, [data-view=properties].on article:visible").count()
        return {"went_to": h, "cards_before": before, "cards_after": after, "chip_after_back": pressed.replace("\n", " ")}
    t("filter_persist_after_back", persist)
    def sheet():
        btn = pg.locator("button", has_text="Filters").first; btn.click(); pg.wait_for_timeout(300)
        s = pg.locator("#sheet")
        info = {"role": s.get_attribute("role"), "aria_modal": s.get_attribute("aria-modal"),
                "focus_in_sheet": pg.evaluate("document.getElementById('sheet').contains(document.activeElement)"), "role_when_open": s.get_attribute("role"), "modal_when_open": s.get_attribute("aria-modal"),
                "has_reset": pg.locator("#sheet button", has_text="Reset").count() + pg.locator("#sheet button", has_text="Clear").count(),
                "has_apply": pg.locator("#sheet button", has_text="Show").count() + pg.locator("#sheet button", has_text="Apply").count(),
                "count_badge_text": btn.inner_text().replace("\n", " ")}
        pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
        info["closed_on_esc"] = not pg.evaluate("document.getElementById('sheet').classList.contains('on')||document.body.classList.contains('sheet-on')")
        info["focus_back_to_button"] = pg.evaluate("document.activeElement&&document.activeElement.textContent.includes('Filters')")
        return info
    t("filter_sheet", sheet)
    def empty():
        pg.fill("[data-view=properties] input[type=search], [data-view=properties] input", "zzzz"); pg.wait_for_timeout(300)
        txt = pg.locator("[data-view=properties].on").inner_text()
        pg.fill("[data-view=properties] input[type=search], [data-view=properties] input", ""); pg.wait_for_timeout(200)
        return "empty state shown" if ("No homes" in txt or "no homes" in txt.lower() or "Not finding" in txt) else "no empty message found"
    t("empty_state", empty)
    def drawer():
        pg.locator("[aria-label='Open menu']").first.click(); pg.wait_for_timeout(300)
        d = pg.locator("#drawer")
        r = {"aria_modal": d.get_attribute("aria-modal"), "focus_in": pg.evaluate("document.getElementById('drawer').contains(document.activeElement)")}
        for _ in range(15): pg.keyboard.press("Tab")
        r["focus_trapped_after_15_tabs"] = pg.evaluate("document.getElementById('drawer').contains(document.activeElement)")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
        r["closes_on_esc"] = pg.evaluate("getComputedStyle(document.getElementById('drawer')).visibility==='hidden'||!document.getElementById('drawer').classList.contains('on')")
        return r
    t("mobile_drawer", drawer)
    def detail():
        pg.goto(SRC + "#p-devasandra"); pg.wait_for_timeout(500)
        sticky = pg.evaluate("""(()=>{const e=[...document.querySelectorAll('[data-view=property].on *')].find(x=>0)||[...document.querySelectorAll('body *')].find(x=>getComputedStyle(x).position==='fixed'&&x.getBoundingClientRect().bottom>=innerHeight-2&&x.offsetHeight>40&&x.offsetHeight<140&&x.textContent.includes('viewing')||getComputedStyle(x).position==='sticky');return e?e.className+' '+Math.round(e.getBoundingClientRect().height):null})()""")
        return {"sticky_cta": sticky}
    t("detail_sticky_cta_available", detail)
    def detail_let():
        pg.goto(SRC + "#p-coffee-board"); pg.wait_for_timeout(400)
        txt = pg.locator("[data-view=property].on").inner_text()
        return {"book_viewing_shown_for_occupied": "Book a viewing" in txt, "notify_shown": ("Notify" in txt or "notify" in txt)}
    t("detail_occupied_cta", detail_let)
    def prefill():
        pg.goto(SRC + "#visit-devasandra"); pg.wait_for_timeout(400)
        return {"home_selected": pg.eval_on_selector("#eHomeSel", "e=>e.value"),
                "ist_shown": "IST" in pg.locator("[data-view=enquire].on").inner_text() or "India Standard" in pg.locator("[data-view=enquire].on").inner_text(),
                "preference_note": "preference" in pg.locator("[data-view=enquire].on").inner_text().lower() or "confirm" in pg.locator("[data-view=enquire].on").inner_text().lower()}
    t("viewing_prefill", prefill)
    def validation():
        pg.fill("#eName", "Test User"); pg.fill("#ePhone", "7700 900123"); pg.select_option("#eCC", "+44")
        pg.evaluate("document.getElementById('eForm').requestSubmit()"); pg.wait_for_timeout(300)
        bad = pg.evaluate("[...document.querySelectorAll('#eForm .fld.bad')].map(f=>f.querySelector('label')?.textContent)")
        inv = pg.evaluate("[...document.querySelectorAll('#eForm [aria-invalid=true]')].length")
        return {"invalid_fields": bad, "aria_invalid_count": inv, "uk_number_accepted": "Phone number *" not in bad,
                "name_kept": pg.eval_on_selector("#eName", "e=>e.value"),
                "date_error_linked": pg.evaluate("document.getElementById('tsp').getAttribute('aria-describedby')")}
    t("enquiry_validation_intl_phone", validation)
    c.close()
    # desktop keyboard
    c = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    c.route("**/fonts.g*/**", lambda r: r.abort())
    pg = c.new_page(); pg.goto(SRC + "#p-devasandra"); pg.wait_for_timeout(500)
    def gallery():
        r = {}
        pg.keyboard.press("Tab")
        r["skip_link_first"] = pg.evaluate("document.activeElement.textContent.trim().slice(0,30)")
        r["focus_ring_visible"] = pg.evaluate("(()=>{const s=getComputedStyle(document.activeElement);return s.outlineStyle!=='none'&&parseFloat(s.outlineWidth)>0||s.boxShadow!=='none'})()")
        img = pg.locator("[data-view=property].on img").first
        r["gallery_img_focusable"] = img.evaluate("e=>!!e.closest('button,a,[tabindex]')")
        pg.focus("#gal"); pg.keyboard.press("Enter"); pg.wait_for_timeout(300)
        r["gallery_enter_opens_lightbox"] = pg.evaluate("!!document.querySelector('.lb')&&!document.querySelector('.lb').hidden")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
        r["h1_on_detail"] = pg.evaluate("[...document.querySelectorAll('[data-view].on h1')].map(h=>h.textContent)")
        img.click(force=True); pg.wait_for_timeout(300)
        lb = pg.locator(".lb")
        r["lightbox_open"] = lb.count() > 0 and not lb.first.evaluate("e=>e.hidden")
        if r["lightbox_open"]:
            r["focus_in_lightbox"] = pg.evaluate("document.querySelector('.lb').contains(document.activeElement)")
            s0 = pg.evaluate("document.querySelector('.lb img')?.src"); pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(200)
            r["arrow_key_changes_image"] = s0 != pg.evaluate("document.querySelector('.lb img')?.src")
            pg.keyboard.press("Escape"); pg.wait_for_timeout(200); r["esc_closes"] = pg.evaluate("document.querySelector('.lb').hidden")
        r["reduced_motion_transition_on_wordmark"] = pg.evaluate("(()=>{const e=document.querySelector('.brand *[class*=word],.brand span');return e?getComputedStyle(e).transitionDuration:null})()")
        return r
    t("desktop_keyboard_gallery", gallery)
    c.close(); b.close()
R["form_posts_made"] = "none to production (POSTs intercepted locally)"
print(json.dumps(R, indent=1))

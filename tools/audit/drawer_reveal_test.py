"""Tests the drag-to-close filter sheet and scroll reveals. Usage: python3 drawer_reveal_test.py index.html out_dir"""
import pathlib, sys, json
from playwright.sync_api import sync_playwright
SRC = pathlib.Path(sys.argv[1]).resolve().as_uri(); OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
R = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    for theme in ("light", "dark"):
        for w in (390, 834, 1440):
            c = b.new_context(viewport={"width": w, "height": 844 if w < 600 else 900})
            c.add_init_script(f"try{{localStorage.setItem('mativio-theme','{theme}')}}catch(e){{}}")
            c.route("**/fonts.g*/**", lambda r: r.abort())
            pg = c.new_page(); errs = []
            pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "fonts" not in m.text and "ERR_FAILED" not in m.text else None)
            pg.goto(SRC + "#home"); pg.wait_for_timeout(500)
            r = {"rvon": pg.evaluate("document.documentElement.classList.contains('rvon')"),
                 "reveal_items": pg.evaluate("document.querySelectorAll('.rv').length"),
                 "visible_before_scroll": pg.evaluate("document.querySelectorAll('.rv.in').length")}
            pg.evaluate("window.scrollTo(0,document.body.scrollHeight)"); pg.wait_for_timeout(900)
            pg.evaluate("window.scrollTo(0,document.body.scrollHeight/2)"); pg.wait_for_timeout(900)
            r["revealed_after_scroll"] = pg.evaluate("document.querySelectorAll('.rv.in').length")
            r["hidden_left_on_home"] = pg.evaluate("[...document.querySelectorAll('[data-view=home] .rv:not(.in)')].length")
            if w == 390:
                pg.goto(SRC + "#properties"); pg.wait_for_timeout(400); pg.evaluate("scrollTo(0,0)")
                pg.click("#fOpen"); pg.wait_for_timeout(500)
                h_half = pg.evaluate("Math.round(document.getElementById('sheet').getBoundingClientRect().height)")
                r["sheet_open_height"] = h_half; r["footer_visible_at_open"] = pg.evaluate("(()=>{const f=document.querySelector('#sheet .sft').getBoundingClientRect();return f.bottom<=innerHeight+1&&f.height>0})()")
                pg.screenshot(path=str(OUT / f"{theme}_390_sheet_half.png"))
                g = pg.locator("#fGrab").bounding_box(); x, y = g["x"] + g["width"] / 2, g["y"] + g["height"] / 2
                # drag up -> full
                pg.mouse.move(x, y); pg.mouse.down(); pg.mouse.move(x, y - 200, steps=12); pg.wait_for_timeout(250); pg.mouse.up(); pg.wait_for_timeout(500)
                r["after_drag_up_height"] = pg.evaluate("Math.round(document.getElementById('sheet').getBoundingClientRect().height)")
                r["grab_label_full"] = pg.get_attribute("#fGrab", "aria-label")
                pg.screenshot(path=str(OUT / f"{theme}_390_sheet_full.png"))
                # keyboard toggle on the handle
                pg.focus("#fGrab"); pg.keyboard.press("Enter"); pg.wait_for_timeout(450)
                r["enter_on_handle_height"] = pg.evaluate("Math.round(document.getElementById('sheet').getBoundingClientRect().height)")
                # drag down -> close
                g = pg.locator("#fGrab").bounding_box(); x, y = g["x"] + g["width"] / 2, g["y"] + g["height"] / 2
                pg.mouse.move(x, y); pg.mouse.down(); pg.mouse.move(x, y + 300, steps=10); pg.wait_for_timeout(250); pg.mouse.up(); pg.wait_for_timeout(500)
                r["closed_after_drag_down"] = not pg.evaluate("document.getElementById('sheet').classList.contains('open')")
                r["focus_back_on_filters_btn"] = pg.evaluate("document.activeElement.id")
                # filters still work: open, choose locality, Show
                pg.click("#fOpen"); pg.wait_for_timeout(400)
                pg.select_option("#fLoc", index=1); pg.click("#fApply"); pg.wait_for_timeout(400)
                r["filter_count_after_apply"] = pg.locator("#fN").inner_text()
                pg.keyboard.press("Escape")
            r["console_errors"] = errs[:3]
            R[f"{theme}|{w}"] = r; c.close()
    # reduced motion: nothing hidden
    c = b.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce"); c.route("**/fonts.g*/**", lambda r: r.abort())
    pg = c.new_page(); pg.goto(SRC + "#home"); pg.wait_for_timeout(400)
    R["reduced_motion"] = {"rvon": pg.evaluate("document.documentElement.classList.contains('rvon')"), "rv_items": pg.evaluate("document.querySelectorAll('.rv').length")}
    b.close()
print(json.dumps(R, indent=1))

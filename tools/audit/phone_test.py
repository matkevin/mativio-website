"""Checks what phone number the enquiry form would send, via the review step (no real submission)."""
import pathlib, sys, json
from playwright.sync_api import sync_playwright
SRC = pathlib.Path(sys.argv[1]).resolve().as_uri()
cases = [("+91", "98450 12345"), ("+91", "098450 12345"), ("+44", "7700 900123"), ("+91", "+44 7700 900123"), ("+974", "5512 3456"), ("+91", "12345")]
out = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for cc, num in cases:
        pg = b.new_page(viewport={"width": 390, "height": 844}); pg.route("**/fonts.g*/**", lambda r: r.abort())
        pg.goto(SRC + "#visit-devasandra"); pg.wait_for_timeout(300)
        pg.check('input[name=kind][value="Ask a question"]', force=True)
        pg.fill("#eName", "Test User"); pg.fill("#eMsg", "Is parking covered?")
        if pg.locator("#eCC").count(): pg.select_option("#eCC", cc)
        pg.fill("#ePhone", num)
        pg.evaluate("document.getElementById('eForm').requestSubmit()"); pg.wait_for_timeout(250)
        bad = pg.evaluate("document.getElementById('ePhone').closest('.fld').classList.contains('bad')")
        inv = pg.get_attribute("#ePhone", "aria-invalid"); desc = pg.get_attribute("#ePhone", "aria-describedby")
        review = pg.evaluate("(()=>{const d=[...document.querySelectorAll('#eReview dt')].find(x=>x.textContent==='Mobile');return d?d.nextElementSibling.textContent:null})()")
        pg.close()
        out.append({"picked": cc, "typed": num, "rejected": bad, "aria-invalid": inv, "error_linked": bool(desc), "would_send": review})
    b.close()
print(json.dumps(out, indent=1))

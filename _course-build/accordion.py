"""Turn a module page's main sections into accordions (objectives open, the rest closed)."""
import re
import sys

SECTION = re.compile(
    r'<section( class="alt")?(?: id="(\w+)")?><div class="wrap">\n'
    r'  <p class="eyebrow">(.*?)</p>\n  <h2>(.*?)</h2>\n(.*?)\n</div></section>', re.S)


def accordionize(page):
    if 'class="acc"' in page:
        return page

    def rep(m):
        alt, sid, eyebrow, title, body = m.groups()
        if title.startswith("How the"):
            return m.group(0)
        if not sid:
            sid = "objectives" if "objectives" in title.lower() else "practice"
        opened = " open" if sid == "objectives" else ""
        return (f'<section{alt or ""}><div class="wrap">\n'
                f'<details class="acc" id="{sid}"{opened}><summary><span class="acc-head">'
                f'<span class="eyebrow">{eyebrow}</span><span class="acc-title">{title}</span></span></summary>\n'
                f'<div class="acc-body">\n{body}\n</div></details>\n</div></section>')

    page = SECTION.sub(rep, page)
    return page.replace("</body>", '<script src="../js/accordion.js"></script>\n</body>', 1)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        with open(path, "w", encoding="utf-8") as f:
            f.write(accordionize(text))
        print("accordions:", path, text.count("<section"), "sections")

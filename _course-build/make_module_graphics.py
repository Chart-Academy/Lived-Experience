"""Draw the module card pictures for both courses into images/ (mod-cp-01.svg … mod-swf-08.svg).

Usage, from the repo's root folder:
  python _course-build/make_module_graphics.py
"""
NAVY, W = "#1F2A44", "#fff"
PALETTE = ["#3A56A6", "#3F6B50", "#B5522B", "#D71F2D"]


def person(x=0, y=0, s=1, fill=W):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-34" r="26" fill="{fill}"/>'
            f'<path d="M-46 50c0-42 20-62 46-62s46 20 46 62z" fill="{fill}"/></g>')


ICONS = {
    # people and roles
    "role": lambda c: person(-40, 0, 1) + f'<g transform="translate(55 -10)"><rect x="-38" y="-48" width="76" height="96" rx="8" fill="{NAVY}"/>'
                      f'<rect x="-14" y="-56" width="28" height="16" rx="5" fill="{W}"/><g fill="{W}" opacity=".85">'
                      f'<rect x="-24" y="-20" width="48" height="7" rx="3"/><rect x="-24" y="-2" width="40" height="7" rx="3"/><rect x="-24" y="16" width="48" height="7" rx="3"/></g></g>',
    "ethics": lambda c: f'<path d="M0 -80l70 26v40c0 46-30 78-70 94-40-16-70-48-70-94v-40z" fill="{W}"/>'
                        f'<path d="M-28 4l20 20 38-42" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>',
    "heart": lambda c: f'<path d="M0 70C-70 24-86 -8-86 -34c0-26 20-44 44-44 18 0 32 10 42 26 10-16 24-26 42-26 24 0 44 18 44 44 0 26-16 58-86 104z" fill="{W}"/>'
                       f'<path d="M-50 -6h22l12-24 18 50 14-26h34" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
    "talk": lambda c: f'<path d="M-85 -60h100a14 14 0 0 1 14 14v50a14 14 0 0 1-14 14h-60l-26 22v-22h-14a14 14 0 0 1-14-14v-50a14 14 0 0 1 14-14z" fill="{W}"/>'
                      f'<path d="M85 -10h-80a14 14 0 0 0-14 14v44a14 14 0 0 0 14 14h44l24 20v-20h12a14 14 0 0 0 14-14v-44a14 14 0 0 0-14-14z" fill="{NAVY}"/>'
                      f'<g fill="{c}"><circle cx="-50" cy="-21" r="7"/><circle cx="-28" cy="-21" r="7"/><circle cx="-6" cy="-21" r="7"/></g>',
    "plan": lambda c: f'<rect x="-62" y="-78" width="124" height="156" rx="12" fill="{W}"/><rect x="-24" y="-88" width="48" height="22" rx="7" fill="{NAVY}"/>'
                      + "".join(f'<path d="M-40 {y}l8 8 14-16" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
                                f'<rect x="-6" y="{y - 2}" width="48" height="9" rx="4" fill="{NAVY}" opacity=".35"/>' for y in (-38, -4, 30)),
    "pin": lambda c: f'<path d="M0 -84a58 58 0 0 1 58 58c0 44-58 104-58 104S-58 18-58 -26A58 58 0 0 1 0 -84z" fill="{W}"/>'
                     f'<circle cx="0" cy="-26" r="22" fill="{c}"/><path d="M-110 70h220" stroke="{NAVY}" stroke-width="8" stroke-linecap="round" stroke-dasharray="2 18"/>',
    "doc": lambda c: f'<path d="M-55 -80h76l34 34v126h-110z" fill="{W}"/><path d="M21 -80v34h34" fill="{NAVY}" opacity=".3"/>'
                     f'<g fill="{c}" opacity=".55"><rect x="-38" y="-40" width="60" height="8" rx="4"/><rect x="-38" y="-18" width="76" height="8" rx="4"/>'
                     f'<rect x="-38" y="4" width="70" height="8" rx="4"/><rect x="-38" y="26" width="50" height="8" rx="4"/></g>'
                     f'<path d="M30 70l44-44 16 16-44 44-22 6z" fill="{NAVY}"/>',
    "exam": lambda c: f'<path d="M0 -70l110 42-110 42-110-42z" fill="{W}"/><path d="M-62 -6v40c0 18 28 30 62 30s62-12 62-30v-40l-62 24z" fill="{W}"/>'
                      f'<path d="M96 -22v52" stroke="{NAVY}" stroke-width="6"/><circle cx="96" cy="36" r="9" fill="{NAVY}"/>',
    "group": lambda c: person(-62, 6, .62) + person(62, 6, .62) + person(0, -6, .8, NAVY) + f'<path d="M-110 76h220" stroke="{W}" stroke-width="8" stroke-linecap="round"/>',
    "growth": lambda c: f'<path d="M-90 60h40v-40h40v-40h40v-40h40" fill="none" stroke="{W}" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>'
                        f'<path d="M64 -84l30 8-8 30" fill="none" stroke="{W}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
                        + person(-70, 18, .5, NAVY),
    "calm": lambda c: f'<circle cx="0" cy="0" r="78" fill="{W}"/><path d="M-50 -10c16-14 34-14 50 0s34 14 50 0M-50 22c16-14 34-14 50 0s34 14 50 0" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"/>',
    "safety": lambda c: f'<path d="M0 -84l72 28v42c0 48-32 80-72 98-40-18-72-50-72-98v-42z" fill="{W}"/>'
                        f'<rect x="-24" y="-8" width="48" height="40" rx="6" fill="{c}"/><path d="M-14 -8v-12a14 14 0 0 1 28 0v12" fill="none" stroke="{c}" stroke-width="8"/>',
    "health": lambda c: f'<circle cx="0" cy="0" r="78" fill="{W}"/><path d="M-14 -46h28v32h32v28h-32v32h-28v-32h-32v-28h32z" fill="{c}"/>',
}

COURSES = {
    "cp": ["role", "ethics", "heart", "talk", "plan", "pin", "doc", "exam"],
    "swf": ["ethics", "heart", "growth", "group", "calm", "safety", "health", "doc"],
}

if __name__ == "__main__":
    for code, icons in COURSES.items():
        for i, name in enumerate(icons, start=1):
            c = PALETTE[(i - 1) % 4] if code == "cp" else PALETTE[(i + 1) % 4]
            label = f"{'CP' if code == 'cp' else 'SWF'} {i:02d}"
            body = (f'<rect width="640" height="360" fill="{c}"/>'
                    f'<circle cx="560" cy="60" r="140" fill="#fff" opacity=".08"/><circle cx="70" cy="330" r="110" fill="#fff" opacity=".08"/>'
                    f'<g transform="translate(320 190)">{ICONS[name](c)}</g>'
                    f'<text x="32" y="58" font-family="Oswald, Arial, sans-serif" font-size="40" font-weight="600" fill="#fff">{i:02d}</text>')
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" role="img" aria-label="{label} module picture">\n'
                   f'{body}\n</svg>\n')
            with open(f"images/mod-{code}-{i:02d}.svg", "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"wrote images/mod-{code}-{i:02d}.svg")

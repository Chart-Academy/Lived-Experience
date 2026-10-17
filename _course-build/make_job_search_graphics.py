"""Draw the Job Search Support graphics (flat style, site colors) into images/.

Usage, from the repo's root folder:
  python _course-build/make_job_search_graphics.py
"""
RED, BLUE, NAVY, PALE, PALE2, GROUND = "#D71F2D", "#3A56A6", "#1F2A44", "#EEF2FA", "#DDE5F4", "#D5DDEE"
TIERS = ["#3A56A6", "#3F6B50", "#B5522B", "#D71F2D", "#3A56A6", "#3F6B50"]


def svg(w, h, title, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n'
            f'<title id="t">{title}</title>\n<desc id="d">{desc}</desc>\n{body}\n</svg>\n')


def sparkle(x, y, r, color=RED):
    return (f'<path d="M{x} {y - r}C{x + r * .15} {y - r * .15} {x + r * .15} {y - r * .15} {x + r} {y}'
            f'C{x + r * .15} {y + r * .15} {x + r * .15} {y + r * .15} {x} {y + r}C{x - r * .15} {y + r * .15} {x - r * .15} {y + r * .15} {x - r} {y}'
            f'C{x - r * .15} {y - r * .15} {x - r * .15} {y - r * .15} {x} {y - r}z" fill="{color}"/>')


# ---------------------------------------------------------------- hero
hero = svg(640, 360, "A job seeker using AI to plan her job search",
           "Illustration of a woman at a laptop with an AI sparkle, a résumé, a magnifying glass over job listings, and a calendar.", f'''
<rect width="640" height="360" fill="{PALE}"/>
<circle cx="560" cy="70" r="120" fill="{PALE2}"/>
<rect x="0" y="300" width="640" height="60" fill="{GROUND}"/>
<!-- résumé -->
<g transform="translate(60 50)">
  <rect width="120" height="150" rx="8" fill="#fff" stroke="{BLUE}" stroke-width="4"/>
  <circle cx="30" cy="32" r="14" fill="{BLUE}"/>
  <rect x="52" y="22" width="52" height="8" rx="4" fill="{NAVY}"/><rect x="52" y="36" width="36" height="6" rx="3" fill="#9AA6C2"/>
  <g fill="#9AA6C2"><rect x="16" y="64" width="88" height="6" rx="3"/><rect x="16" y="80" width="76" height="6" rx="3"/>
  <rect x="16" y="100" width="88" height="6" rx="3"/><rect x="16" y="116" width="64" height="6" rx="3"/></g>
  <circle cx="104" cy="136" r="18" fill="#3F6B50"/><path d="M95 136l6 6 12-12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<!-- listings + magnifier -->
<g transform="translate(470 120)">
  <g fill="#fff" stroke="{BLUE}" stroke-width="3">
    <rect width="110" height="30" rx="6"/><rect y="40" width="110" height="30" rx="6"/><rect y="80" width="110" height="30" rx="6"/>
  </g>
  <rect x="10" y="12" width="60" height="6" rx="3" fill="{NAVY}"/><rect x="10" y="52" width="70" height="6" rx="3" fill="{NAVY}"/><rect x="10" y="92" width="50" height="6" rx="3" fill="{NAVY}"/>
  <circle cx="90" cy="15" r="7" fill="#3F6B50"/><circle cx="90" cy="55" r="7" fill="#3F6B50"/>
  <path d="M84 89l12 12M96 89l-12 12" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>
  <circle cx="-30" cy="70" r="26" fill="none" stroke="{NAVY}" stroke-width="7"/><path d="M-11 89l20 20" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>
</g>
<!-- calendar -->
<g transform="translate(470 30)">
  <rect width="78" height="64" rx="8" fill="#fff" stroke="{BLUE}" stroke-width="3"/><rect width="78" height="18" rx="8" fill="{RED}"/>
  <g fill="{PALE2}"><rect x="10" y="26" width="14" height="10"/><rect x="32" y="26" width="14" height="10"/><rect x="54" y="26" width="14" height="10"/>
  <rect x="10" y="44" width="14" height="10"/><rect x="54" y="44" width="14" height="10"/></g><rect x="32" y="44" width="14" height="10" fill="#3F6B50"/>
</g>
<!-- desk + laptop -->
<rect x="190" y="236" width="270" height="14" rx="4" fill="{NAVY}"/>
<rect x="208" y="250" width="12" height="56" fill="{NAVY}"/><rect x="430" y="250" width="12" height="56" fill="{NAVY}"/>
<path d="M300 236l14-74h110l-14 74z" fill="{BLUE}"/><rect x="290" y="232" width="140" height="6" rx="3" fill="{NAVY}"/>
{sparkle(360, 198, 16, "#fff")}
<!-- person -->
<circle cx="250" cy="118" r="30" fill="#8A5A3C"/>
<path d="M218 116c0-30 18-44 34-44s34 14 34 40c-6-10-20-18-34-18s-26 10-34 22z" fill="{NAVY}"/>
<path d="M206 236c0-50 20-82 46-82s46 32 46 82z" fill="{RED}"/>
<path d="M286 196l40 18" stroke="#8A5A3C" stroke-width="12" stroke-linecap="round"/>
{sparkle(330, 70, 22)}{sparkle(372, 104, 12, BLUE)}{sparkle(300, 40, 9, BLUE)}
''')

# ---------------------------------------------------------------- per-agent icons
ICONS = {
    "J1": "Career Profile Agent", "J2": "Résumé Optimizer", "J3": "Skills-to-Openings Agent",
    "J4": "Interview Practice Coach", "J5": "Application Assistant", "J6": "Job Search Manager",
}


def icon(j, c):
    """A white icon centered at (0, 0), about 160 px wide."""
    w = "#fff"
    if j == "J1":
        return (f'<circle cx="0" cy="-30" r="34" fill="{w}"/><path d="M-60 70c0-50 26-74 60-74s60 24 60 74z" fill="{w}"/>'
                f'<g transform="translate(62 -50)">{sparkle(0, 0, 26, "#F7C9CD")}</g>')
    if j == "J2":
        return (f'<rect x="-55" y="-75" width="110" height="145" rx="10" fill="{w}"/>'
                f'<g fill="{c}" opacity=".45"><rect x="-38" y="-52" width="76" height="9" rx="4"/><rect x="-38" y="-30" width="60" height="9" rx="4"/>'
                f'<rect x="-38" y="-8" width="76" height="9" rx="4"/><rect x="-38" y="14" width="50" height="9" rx="4"/></g>'
                f'<circle cx="48" cy="58" r="30" fill="{NAVY}"/><path d="M34 58l10 10 18-20" fill="none" stroke="{w}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    if j == "J3":
        return (f'<g fill="{w}"><rect x="-80" y="-70" width="120" height="34" rx="8"/><rect x="-80" y="-24" width="120" height="34" rx="8"/>'
                f'<rect x="-80" y="22" width="120" height="34" rx="8"/></g>'
                f'<circle cx="40" cy="10" r="38" fill="none" stroke="{NAVY}" stroke-width="10"/><path d="M68 38l26 26" stroke="{NAVY}" stroke-width="13" stroke-linecap="round"/>')
    if j == "J4":
        return (f'<path d="M-85 -60h100a14 14 0 0 1 14 14v50a14 14 0 0 1-14 14h-60l-26 22v-22h-14a14 14 0 0 1-14-14v-50a14 14 0 0 1 14-14z" fill="{w}"/>'
                f'<path d="M85 -10h-80a14 14 0 0 0-14 14v44a14 14 0 0 0 14 14h44l24 20v-20h12a14 14 0 0 0 14-14v-44a14 14 0 0 0-14-14z" fill="{NAVY}"/>'
                f'<g fill="{c}"><circle cx="-50" cy="-21" r="7"/><circle cx="-28" cy="-21" r="7"/><circle cx="-6" cy="-21" r="7"/></g>')
    if j == "J5":
        return (f'<path d="M-90 -10l170-70-50 160-40-60z" fill="{w}"/><path d="M-10 20l90-100-50 100z" fill="{NAVY}" opacity=".35"/>'
                f'<path d="M-10 20v50l26-30" fill="{w}"/>')
    return (f'<rect x="-80" y="-70" width="160" height="140" rx="12" fill="{w}"/><rect x="-80" y="-70" width="160" height="34" rx="12" fill="{NAVY}"/>'
            f'<g fill="{c}" opacity=".35"><rect x="-62" y="-22" width="30" height="22"/><rect x="-15" y="-22" width="30" height="22"/><rect x="32" y="-22" width="30" height="22"/>'
            f'<rect x="-62" y="14" width="30" height="22"/><rect x="32" y="14" width="30" height="22"/></g>'
            f'<rect x="-15" y="14" width="30" height="22" fill="{c}"/>')


cards = {}
for i, (j, name) in enumerate(ICONS.items()):
    c = TIERS[i]
    cards[j] = svg(640, 360, f"{j} {name}", f"Icon illustration for the {name}.", f'''
<rect width="640" height="360" fill="{c}"/>
<circle cx="560" cy="60" r="140" fill="#fff" opacity=".08"/><circle cx="70" cy="330" r="110" fill="#fff" opacity=".08"/>
<g transform="translate(320 185)">{icon(j, c)}</g>
<text x="32" y="58" font-family="Oswald, Arial, sans-serif" font-size="40" font-weight="600" fill="#fff">{j}</text>''')

# ---------------------------------------------------------------- process diagram
steps = [("J1", "Know your", "target"), ("J2", "Optimize", "your résumé"), ("J3", "Find the right", "openings"),
         ("J4", "Practice the", "interview"), ("J5", "Apply with", "confidence"), ("J6", "Stay", "organized")]
body = [f'<rect width="960" height="300" rx="16" fill="{PALE}"/>',
        f'<path d="M110 120H850" stroke="{PALE2}" stroke-width="14" stroke-linecap="round"/>']
for i, (j, a, b) in enumerate(steps):
    x = 110 + i * 148
    c = TIERS[i]
    body.append(f'<circle cx="{x}" cy="120" r="54" fill="{c}"/>'
                f'<g transform="translate({x} 118) scale(.36)">{icon(j, c)}</g>'
                f'<text x="{x}" y="206" text-anchor="middle" font-family="Oswald, Arial, sans-serif" font-size="22" font-weight="600" fill="{NAVY}">{j}</text>'
                f'<text x="{x}" y="232" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="{NAVY}">{a}</text>'
                f'<text x="{x}" y="252" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="{NAVY}">{b}</text>')
body.append(f'<text x="480" y="44" text-anchor="middle" font-family="Oswald, Arial, sans-serif" font-size="22" font-weight="600" fill="{RED}">'
            f'SET IT UP  →  RUN IT  →  CHECK IT  →  REVISE IT</text>')
process = svg(960, 300, "The AI job search process",
              "Six steps, one agent each: J1 know your target, J2 optimize your résumé, J3 find the right openings, J4 practice the interview, "
              "J5 apply with confidence, J6 stay organized. For every agent: set it up, run it, check it, revise it.", "\n".join(body))

for name, text in [("job-search.svg", hero), ("ai-job-search-process.svg", process)] + \
        [(f"js-{j.lower()}.svg", t) for j, t in cards.items()]:
    with open(f"images/{name}", "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote images/" + name)

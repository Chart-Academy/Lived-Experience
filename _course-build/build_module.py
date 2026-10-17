"""Build a course module from its data in cp_modules.py (Community Practitioner) or swf_modules.py (Survivor Workforce Facilitator).

Writes the five files that make up a module, following Module 1 (the finished model):
  modules/{cp|swf}-NN.html                     module page
  slides/cp-NN.html                      slide deck with presenter notes
  practice/cp-NN.html                    in-class packet (role cards and team worksheet)
  assignments/CP-Module-NN-Assignment.docx
  assignments/CP-Module-NN-Team-Notes.docx

Usage, from the repo's root folder (needs python-docx):
  python _course-build/build_module.py cp 2       # one module
  python _course-build/build_module.py cp all     # CP Modules 2-8 (Module 1 is hand-built)
  python _course-build/build_module.py swf all    # SWF Modules 1-8
"""
import html
import re
import sys

from accordion import accordionize
import cp_modules
import swf_modules

COURSES = {
    "cp": dict(code="cp", prefix="CP", page="community-practitioner.html", name="Certified Community Practitioner",
               pathway="HS-BCP pathway", modules=cp_modules.MODULES, first=2),
    "swf": dict(code="swf", prefix="SWF", page="survivor-workforce-facilitator.html",
                name="Certified Survivor Workforce Facilitator", pathway="NADSP DSP-I pathway",
                modules=swf_modules.MODULES, first=1),
}
C = COURSES["cp"]
MODULES = C["modules"]

ROLE_CLASSES = ["r-housing", "r-benefits", "r-reentry", "r-health", "r-work", "r-lead"]
CARD_TAGS = ["t2", "t3", "t4", "t1", "t2", "t3"]
BOX_COLORS = ["c2", "c3", "c4", "c1", "c2", "c3"]


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def fiction(c):
    return c.get("fiction", f"{c['name']} is fictional.")


def nn(m):
    return f"{m['num']:02d}"


# ---------------------------------------------------------------- shared page parts
def header(active="cp"):
    cur = ' aria-current="page"'
    return f'''<header class="site-header"><div class="wrap">
<a class="brand" href="../index.html"><img src="../images/chart-logo-icon.png" alt="Chart Academy logo"><span class="brand-text">Chart Academy<small>Workforce Credentialing · with IRSJA</small></span></a>
<nav aria-label="Main"><input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Show or hide the menu"><label for="nav-toggle" class="nav-btn" aria-hidden="true"><span class="bars"></span>Menu</label>
<ul class="nav">
<li><a href="../index.html">Home</a></li>
<li><a href="../getting-started.html">Getting Started</a></li>
<li><a href="../community-practitioner.html"{cur if C["code"] == "cp" else ""}>Community Practitioner</a></li>
<li><a href="../survivor-workforce-facilitator.html"{cur if C["code"] == "swf" else ""}>Survivor Workforce Facilitator</a></li>
<li><a href="../credentials.html">Credentials</a></li>
<li><a href="../job-search.html">Job Search</a></li>
</ul></nav>
</div></header>'''


FOOTER = '''<footer class="site-footer"><div class="wrap cols">
<div><h4>Courses</h4><ul>
<li><a href="../community-practitioner.html">Certified Community Practitioner</a></li>
<li><a href="../survivor-workforce-facilitator.html">Certified Survivor Workforce Facilitator</a></li></ul></div>
<div><h4>Support</h4><ul><li><a href="../getting-started.html">Getting Started</a></li><li><a href="../credentials.html">Credentials</a></li><li><a href="../job-search.html">Job Search Support</a></li><li><a href="../capstone.html">Capstone</a></li></ul></div>
<div><p>© 2026 Chart Academy<br>In partnership with IRSJA · <a href="https://www.thechartacademy.com" target="_blank" rel="noopener">thechartacademy.com</a></p><p><a href="#top">Back to top ↑</a></p></div>
</div></footer>'''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
{css}
</head>'''


def flow_minutes(m):
    """Clock times for each block, including breaks."""
    t, out = 0, []
    for block in m["flow"]:
        out.append((t, t + block["min"], block))
        t += block["min"]
    assert t == m["hours"] * 60, f"Module {m['num']} flow adds to {t} min, expected {m['hours'] * 60}"
    return out


def clock(mins):
    return f"{mins // 60}:{mins % 60:02d}"


# ---------------------------------------------------------------- module page
def module_page(m):
    prev_link = (f'<a class="btn ghost" href="{C["code"]}-{m["num"] - 1:02d}.html">← Module {m["num"] - 1:02d}</a>'
                 if m["num"] > 1 else f'<a class="btn ghost" href="../{C["page"]}">← Course overview</a>')
    nxt = MODULES.get(m["num"] + 1)
    next_link = (f'<a class="btn ghost" href="{C["code"]}-{m["num"] + 1:02d}.html">Module {m["num"] + 1:02d} · {nxt["title"]} →</a>'
                 if nxt else '<a class="btn ghost" href="../job-search.html">Next: Job Search Support →</a>')
    flow = "\n".join(
        f'    <div class="f-{b["kind"]}"><b>{b["label"]} · {b["min"]} min</b><span>{b["desc"]}</span></div>'
        for b in m["flow"] if b["kind"] != "break")
    breaks = sum(b["min"] for b in m["flow"] if b["kind"] == "break")
    objectives = "\n".join(f"    <li>{o}</li>" for o in m["objectives"])
    roles = "\n".join(
        f'    <div class="card"><span class="tag {CARD_TAGS[i]}">Role</span><h3>{r["name"]}</h3><p class="small">{r["where"]}</p></div>'
        for i, r in enumerate(m["roles"]))
    steps = "\n".join(f'    <li><strong>{s["label"]} ({s["min"]} min):</strong> {s["desc"]}</li>' for s in m["steps"])
    parts = "\n".join(
        f'    <div class="card"><span class="tag {CARD_TAGS[i]}">Part {i + 1}</span><h3>{p["title"]}</h3><p>{p["summary"]}</p></div>'
        for i, p in enumerate(m["assignment"]["parts"]))
    rubric = "\n".join(f'    <tr><th>{r[0]} · 5</th><td>{r[1]}</td></tr>' for r in m["assignment"]["rubric"])
    extra_dl = ""
    for f in m.get("extra_downloads", []):
        extra_dl += f'''
  <div class="download">
    <div><div class="file">{f["title"]}</div><div class="meta">{f["meta"]}</div></div>
    <a class="btn" href="../assignments/{f["file"]}" download>{f["button"]}</a>
  </div>'''
    return HEAD.format(title=f'Module {m["num"]} · {strip_tags(m["title"])} · Chart Academy',
                       css='<link rel="stylesheet" href="../css/style.css?v=20261016d">') + f'''
<body id="top">
{header()}

<main>
<div class="hero"><div class="wrap">
  <p class="crumbs"><a href="../{C["page"]}">{C["name"]}</a> › <a href="../{C["page"]}#modules">Modules</a> › Module {nn(m)}</p>
  <p class="eyebrow">Module {nn(m)} · {m["hours"]} hours · Learn → Practice → Apply</p>
  <h1>{m["title"]}</h1>
  <p class="lead">{m["lead"]}</p>
  <div class="btns">
    <a class="btn" href="#slides">Class slides</a>
    <a class="btn ghost" href="#assignment">Assignment</a>
    <a class="btn ghost" href="../practice/{C["code"]}-{nn(m)}.html">In-class packet</a>
  </div>
</div></div>

<section class="alt"><div class="wrap">
  <p class="eyebrow">Today's class</p>
  <h2>How the {m["hours_word"]} hours flow</h2>
  <div class="flow">
{flow}
  </div>
  <p class="small">Includes {breaks} minutes of breaks. There is no homework: everything is submitted by the end of class. Practice cases are fictional. Never bring real client information to class.</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">By the end of this module</p>
  <h2>Learning objectives</h2>
  <p>The learner will be able to:</p>
  <ol>
{objectives}
  </ol>
</div></section>

<section class="alt" id="slides"><div class="wrap">
  <p class="eyebrow">Learn</p>
  <h2>Class slides</h2>
  <div class="deck-frame"><iframe src="../slides/{C["code"]}-{nn(m)}.html" title="Module {m["num"]} class slides" loading="lazy" allowfullscreen></iframe></div>
  <div class="btns">
    <a class="btn" href="../slides/{C["code"]}-{nn(m)}.html" target="_blank" rel="noopener">Open slides full screen</a>
  </div>
  <p class="small" style="margin-top:12px"><strong>Instructors:</strong> open the slides full screen. Use the arrow keys to move, press <strong>N</strong> for presenter notes, and press <strong>F</strong> for full screen.</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Practice · in class · groups of 4–6</p>
  <h2>{m["activity_title"]}</h2>
  <p>{m["case"]["page_intro"]}</p>
  <p>{m["case"]["page_how"]}</p>
  <div class="grid g3">
{roles}
  </div>
  <ol style="margin-top:18px">
{steps}
  </ol>
  <div class="download">
    <div><div class="file">Team Notes: {m["team_notes_title"]}</div><div class="meta">Word document (.docx) · one note-taker per team, or upload it to Google Docs and share it so the team can type together</div></div>
    <a class="btn" href="../assignments/{C["prefix"]}-Module-{nn(m)}-Team-Notes.docx" download>Download team notes</a>
  </div>{extra_dl}
  <p class="small">Instructors: print the role cards and team worksheet from the <a href="../practice/{C["code"]}-{nn(m)}.html">in-class packet</a>.</p>
</div></section>

<section class="alt" id="assignment"><div class="wrap">
  <p class="eyebrow">Apply · 20 points · completed and submitted in class</p>
  <h2>Module {m["num"]} assignment</h2>
  <p>{m["assignment"]["intro"]} You'll complete it in the last part of class and upload it before you leave. There is no homework.</p>
  <div class="grid g3">
{parts}
  </div>

  <div class="download">
    <div><div class="file">{C["prefix"]} Module {nn(m)} Assignment</div><div class="meta">Word document (.docx) · opens in Word, Google Docs, or Pages</div></div>
    <a class="btn" href="../assignments/{C["prefix"]}-Module-{nn(m)}-Assignment.docx" download>Download the assignment</a>
  </div>

  <h3>How to submit</h3>
  <ol>
    <li>Download the assignment and type your answers into the shaded boxes. Use your team notes for Part 2.</li>
    <li>Save the file with your name, for example <em>{C["prefix"]}-Module-{nn(m)}-Your-Name.docx</em>.</li>
    <li>Upload it to the Module {m["num"]} assignment in Canvas before you leave class. Working on paper? Upload a clear photo of each page.</li>
  </ol>
  <p><a class="btn" href="#">Submit in Canvas</a> <span class="small">(link to be added)</span></p>

  <div class="own-words"><b>In your own words</b>Write Part 3 yourself. You choose what to share, and you never have to share more than you're comfortable with.</div>

  <h3 style="margin-top:22px">How it's graded</h3>
  <table class="facts">
{rubric}
  </table>
</div></section>

<section><div class="wrap">
  <div class="mod-nav">
    {prev_link}
    <a class="btn ghost" href="../{C["page"]}#modules">All modules</a>
    {next_link}
  </div>
</div></section>
</main>

{FOOTER}
</body>
</html>
'''


# ---------------------------------------------------------------- slides
def slides(m):
    short = m["short_title"]
    out = []

    def add(body, cls="slide", notes=None, foot=True):
        n = len(out) + 1
        f = (f'  <div class="foot"><span><img src="../images/chart-logo-icon.png" alt="">Module {nn(m)} · {short}</span><span>{n}</span></div>\n'
             if foot else "")
        note = f'  <aside class="notes">{notes}</aside>\n' if notes else ""
        out.append(f'<!-- {n} -->\n<section class="{cls}">\n{body}\n{f}{note}</section>')

    def brk(kind, part, title, line, notes=None):
        n = len(out) + 1
        note = f'  <aside class="notes">{notes}</aside>\n' if notes else ""
        out.append(f'<!-- {n} -->\n<section class="slide break {kind}">\n  <p class="eyebrow" style="color:#fff">{part}</p>\n'
                   f'  <h2>{title}</h2>\n  <p>{line}</p>\n  <div class="foot"><span>Module {nn(m)} · {short}</span><span>{n}</span></div>\n{note}</section>')

    # 1 Title
    out.append(f'''<!-- 1 -->
<section class="slide title">
  <img class="logo" src="../images/chart-logo-icon.png" alt="Chart Academy logo">
  <p class="eyebrow">{C["name"]} · Module {nn(m)} · {m["hours"]} hours</p>
  <h1>{m["slide_title_html"]}</h1>
  <p style="font-size:34px;max-width:900px">{m["subtitle"]}</p>
  <div class="foot"><span>Chart Academy · in partnership with IRSJA</span><span>{C["pathway"]}</span></div>
  <aside class="notes">{m["title_notes"]}</aside>
</section>''')
    # 2 Agenda
    rows = []
    for start, end, b in flow_minutes(m):
        k = {"open": "open", "learn": "learn", "practice": "practice", "apply": "apply", "break": "open"}[b["kind"]]
        rows.append(f'    <li><span class="t">{clock(start)}–{clock(end)}</span><span class="k {k}">{b["label"]}</span>{b["agenda"]}</li>')
    add('  <p class="eyebrow">Today</p>\n  <h2>Our {} hours</h2>\n  <ul class="agenda">\n{}\n  </ul>'.format(m["hours_word"], "\n".join(rows)),
        notes="Times are a guide. Protect the Practice and Apply blocks. If something runs long, shorten Learn.")
    # 3 Objectives
    add('  <p class="eyebrow">By the end of today you will be able to</p>\n  <h2>Learning objectives</h2>\n  <ol>\n' +
        "\n".join(f"    <li>{o}</li>" for o in m["slide_objectives"]) + "\n  </ol>",
        notes="Read these aloud. Tell learners we will come back to this slide at the end and check each one off together.")
    # 4 Opening
    op = m["opening"]
    add(f'  <p class="eyebrow">Opening circle <span class="timer">{op["min"]} min</span></p>\n  <h2>{op["title"]}</h2>\n'
        f'  <p class="quote">{op["quote"]}</p>\n  <p class="small">Share as much or as little as you want. You can always pass.</p>',
        notes=op["notes"])
    # Learn
    brk("learn", "Part 1", "Learn", m["learn_line"])
    for s in m["learn"]:
        add(f'  <p class="eyebrow">{s["eyebrow"]}</p>\n  <h2>{s["title"]}</h2>\n{s["body"]}', notes=s["notes"])
    qc = m["quick_check"]
    add(f'  <p class="eyebrow">Quick check <span class="timer">{qc["min"]} min</span></p>\n  <h2>{qc["title"]}</h2>\n  <ol>\n' +
        "\n".join(f"    <li>{q}</li>" for q in qc["items"]) + "\n  </ol>", notes=qc["notes"])
    # Practice
    brk("practice", "Part 2", "Practice", m["practice_line"], notes=m["practice_notes"])
    c = m["case"]
    add(f'''  <p class="eyebrow">The case · fictional</p>
  <h2>{c["slide_title"]}</h2>
  <div class="cols">
    <div>
      <p>{c["slide_intro"]}</p>
      <ul>
{chr(10).join(f"        <li>{b}</li>" for b in c["bullets"])}
      </ul>
    </div>
    <div class="box c2">
      <h3>{c.get("quote_label", "What they say")}</h3>
      {c["quote"]}
    </div>
  </div>''', notes=c["slide_notes"])
    roles = "\n".join(f'    <div class="box {BOX_COLORS[i]}"><h3>{r["name"]}</h3>{r["where"]}</div>' for i, r in enumerate(m["roles"]))
    add(f'  <p class="eyebrow">Your team · one role each</p>\n  <h2>{m["roles_title"]}</h2>\n  <div class="cols3">\n{roles}\n  </div>\n'
        f'  <p class="small" style="margin-top:16px">{m["roles_small"]}</p>', notes=m["roles_notes"])
    for st in m["step_slides"]:
        body = f'  <p class="eyebrow">{st["eyebrow"]} <span class="timer">{st["min"]} min</span></p>\n  <h2>{st["title"]}</h2>\n{st["body"]}'
        add(body, notes=st["notes"])
    db = m["debrief"]
    add(f'  <p class="eyebrow">Debrief · whole class <span class="timer">{db["min"]} min</span></p>\n  <h2>Step out of role</h2>\n  <ol>\n' +
        "\n".join(f"    <li>{q}</li>" for q in db["questions"]) + "\n  </ol>", notes=db["notes"])
    # Apply
    brk("apply", "Part 3", "Apply", m["apply_line"])
    a = m["assignment"]
    add(f'''  <p class="eyebrow">Your assignment · complete it in class <span class="timer">{a["minutes"]} min</span></p>
  <h2>Module {m["num"]} assignment</h2>
  <div class="cols">
    <div>
      <ol>
        <li><strong>Download</strong> the assignment from the Module {m["num"]} page.</li>
        <li><strong>Parts 1 and 2</strong> ({a["parts12_min"]} min): {a["parts12_desc"]} Use your team notes.</li>
        <li><strong>Part 3</strong> ({a["part3_min"]} min): your lived experience reflection.</li>
        <li><strong>Upload</strong> it to Canvas before you leave.</li>
      </ol>
    </div>
    <div class="box c3"><h3>Due</h3>By the end of class today. There is no homework.</div>
  </div>''', notes="Show the module page on screen so learners can see where to download the assignment. Learners without a computer can complete a printed copy and upload a photo of each page. Give a 5-minute warning before moving on to the exit ticket.")
    add(f'''  <p class="eyebrow">Part 3 · on your own <span class="timer">{a["part3_min"]} min</span></p>
  <h2>{a["reflection_title"]}</h2>
  <p>{a["reflection_slide"]}</p>
  <div class="own-words" style="margin-top:20px"><b>In your own words</b>{m["own_words"]}</div>''',
        notes="Keep this slide up while learners write. Near the end, invite two or three volunteers to read one sentence aloud. Learners write this part themselves.")
    nxt = MODULES.get(m["num"] + 1)
    nxt_note = f"Module {m['num'] + 1}: {nxt['title']}" if nxt else "Job Search Support"
    add('  <p class="eyebrow">Before you go <span class="timer">5 min</span></p>\n  <h2>Exit ticket</h2>\n  <ol>\n' +
        "\n".join(f"    <li>{q}</li>" for q in m["exit_ticket"]) + "\n  </ol>\n" +
        f'  <div class="warn" style="margin-top:22px">Before you leave, make sure your Module {m["num"]} assignment is uploaded to Canvas.</div>',
        notes=f"Go back to slide 3 and check off each objective with the group. Collect exit tickets and use the questions to open {nxt_note}.")

    body = "\n\n".join(out)
    return HEAD.format(title=f'Module {m["num"]} Slides · {strip_tags(m["title"])}',
                       css='<link rel="stylesheet" href="../css/slides.css">') + f'''
<body>
<div class="progress"></div>
<div class="deck"><div class="stage">

{body}

</div></div>

<div class="controls">
  <a href="../modules/{C["code"]}-{nn(m)}.html" title="Back to the module page">Module</a>
  <a href="../practice/{C["code"]}-{nn(m)}.html" title="Open the in-class packet">Packet</a>
  <button class="toggle-notes" title="Presenter notes (N)">Notes</button>
  <button class="prev" aria-label="Previous slide">←</button>
  <span class="count"></span>
  <button class="next" aria-label="Next slide">→</button>
</div>
<script src="../js/slides.js"></script>
</body>
</html>
'''


# ---------------------------------------------------------------- in-class packet
def packet(m):
    c = m["case"]
    cards = []
    for i, r in enumerate(m["roles"]):
        facts = "\n".join(f"          <li>{f}</li>" for f in r["facts"])
        label = r.get("facts_label", "Only you know:")
        need = f'\n        <p class="need"><strong>{r.get("need_label", "You need from another role:")}</strong> {r["need"]}</p>' if r.get("need") else ""
        extra = f'\n        <p class="small">{r["extra"]}</p>' if r.get("extra") else ""
        cards.append(f'''      <div class="role-card {ROLE_CLASSES[i]}">
        <h3>{r["name"]}</h3><p class="where">{r["where"]}</p>
        <p><strong>{label}</strong></p>
        <ul>
{facts}
        </ul>{need}{extra}
      </div>''')
    ws = m["worksheet"]
    head = "".join(f'<th style="width:{w}%">{h}</th>' if w else f"<th>{h}</th>" for h, w in ws["columns"])
    first = ws.get("first_col") or [""] * ws["rows"]
    rows = "\n".join("      <tr>" + f"<td>{first[i]}</td>" + "<td></td>" * (len(ws["columns"]) - 1) + "</tr>" for i in range(ws["rows"]))
    plan = "\n".join(
        f'    <p style="margin-top:12px"><strong>{p}</strong></p>\n    <div class="lines">' + "<div></div>" * n + "</div>"
        for p, n in ws["plan"])
    return HEAD.format(title=f'Module {m["num"]} In-Class Packet · {strip_tags(m["title"])}',
                       css='<link rel="stylesheet" href="../css/style.css?v=20261016d">\n<link rel="stylesheet" href="../css/practice.css?v=20261016b">') + f'''
<body id="top">
{header()}

<main class="sheet">
  <div class="sheet-tools">
    <a class="btn" href="javascript:window.print()">Print this packet</a>
    <a class="btn ghost" href="../modules/{C["code"]}-{nn(m)}.html">Back to Module {m["num"]}</a>
  </div>

  <div class="sheet-head">
    <div>
      <p class="eyebrow">{C["name"]} · Module {nn(m)} · In-class packet</p>
      <h1>{m["activity_title"]}</h1>
    </div>
    <img src="../images/chart-logo-icon.png" alt="Chart Academy logo">
  </div>

  <div class="note info"><strong>For instructors:</strong> {m["packet_instructions"]}</div>
  <div class="note todo"><strong>Remember:</strong> {fiction(c)} Never use real client names or details in class.</div>

  <section class="part">
    <h2><span class="tag t2">The case</span> {c["slide_title"]}</h2>
    <p>{c["packet_text"]}</p>
    <p><em>{c["quote"]}</em></p>
  </section>

  <section class="part">
    <h2><span class="tag t3">Step 1</span> Role cards <span class="small">· cut apart · {m["steps"][0]["min"]} min on your own</span></h2>
    <div class="role-cards">
{chr(10).join(cards)}
    </div>
  </section>

  <section class="part page-break">
    <h2><span class="tag t4">Step 2</span> {ws["title"]} <span class="small">· team huddle · {m["steps"][1]["min"]} min</span></h2>
    <p>{ws["instructions"]}</p>
    <table class="ws-table">
      <tr>{head}</tr>
{rows}
    </table>
  </section>

  <section class="part">
    <h2><span class="tag t1">Step 3</span> Our plan <span class="small">· {m["steps"][2]["min"]} min · present in 2 min</span></h2>
{plan}
  </section>
</main>

{FOOTER}
</body>
</html>
'''


# ---------------------------------------------------------------- Word files
def word_files(m, logo, out_dir):
    from docx_kit import Kit
    a = m["assignment"]
    c = m["case"]
    # Assignment
    k = Kit(logo)
    k.header(f"{C['name'].upper()} · MODULE {nn(m)} · ASSIGNMENT", strip_tags(m["title"]))
    k.name_date()
    k.h2("About this assignment")
    k.para(strip_tags(a["intro"]) + " You complete it in class. There is no homework.")
    k.bullets([
        ("How to complete it: ", "Download this file, type your answers into the shaded boxes, and save it. Use your team notes for Part 2."),
        ("How to submit: ", f"Upload your saved file to the Module {m['num']} assignment in Canvas. "
                            "Working on paper? Print it, fill it in, and upload a clear photo of each page."),
        ("Due: ", "By the end of class today. Upload it before you leave."),
        ("Points: ", "20 (see the rubric on the last page)."),
    ])
    k.callout("Remember:", f"{fiction(c)} Never include real client names or details.", "FFF8E1", "8A6900")
    qn_ = 1
    for i, part in enumerate(a["parts"]):
        k.h2(f"Part {i + 1} · {part['title']}")
        if i == 2:
            k.callout("In your own words.", "Write this part yourself. You choose what to share, and you never have to share "
                      "more than you're comfortable with.", "EDF3EE", "3F6B50")
        if part.get("note"):
            k.para(part["note"], italic=True, muted=True)
        for item in part["items"]:
            if item["type"] == "roles":
                k.para(f"{qn_}. Which role did you play? Mark one with an X.", bold=True, after=2)
                k.role_picker([r["name"] for r in m["roles"]])
                qn_ += 1
            elif item["type"] == "q":
                k.answer_box(f"{qn_}. {item['text']}", item.get("h", 0.9), item.get("hint"))
                qn_ += 1
            elif item["type"] == "grid":
                if item.get("text"):
                    k.para(f"{qn_}. {item['text']}", bold=True, after=2)
                    qn_ += 1
                k.grid(item["columns"], item["widths"], item["rows"], item.get("h", 0.55), item.get("first_col"))
    k.rubric(a["rubric_full"])
    k.footer(f"Chart Academy Workforce Credentialing · {C['name']} · Module {nn(m)} Assignment")
    k.save(f"{out_dir}/{C['prefix']}-Module-{nn(m)}-Assignment.docx")

    # Team Notes
    t = Kit(logo)
    t.header(f"{C['name'].upper()} · MODULE {nn(m)} · TEAM NOTES", f"Team Notes: {m['team_notes_title']}")
    t.h2("How to use these notes")
    t.bullets([
        ("One note-taker: ", "The team lead (or a volunteer) types the team's notes here during the huddle."),
        ("Or work together: ", "Upload this file to Google Drive, open it with Google Docs, and share it with your team so everyone can type at once."),
        ("Before you leave: ", f"Everyone on the team uses these notes to finish Part 2 of their own Module {m['num']} assignment. "
                               "The note-taker uploads these notes to Canvas with the team's names."),
    ])
    t.callout("Remember:", f"{fiction(c)} Never include real client names or details.", "FFF8E1", "8A6900")
    t.h2("Our team")
    tbl = t.grid(["Name", "Role"], [3.35, 3.35], len(m["roles"]), 0.35)
    for i, r in enumerate(m["roles"], start=1):
        t.cell_text(tbl, i, 1, r["name"])
    t.h2("The case")
    t.para(strip_tags(c["packet_text"]))
    t.para(strip_tags(c["quote"]), italic=True)
    tn = m["team_notes"]
    t.h2("Step 1 · What each role knows")
    t.para("Each role shares what is on their card. The note-taker fills in that row.", italic=True, muted=True)
    t.grid(tn["step1_columns"], tn["step1_widths"], len(m["roles"]), 0.75, first_col=[r["name"] for r in m["roles"]])
    ws = m["worksheet"]
    t.h2(f"Step 2 · {ws['title']}")
    t.para(strip_tags(ws["instructions"]), italic=True, muted=True)
    cols = [h for h, _ in ws["columns"]]
    t.grid(cols, tn["step2_widths"], ws["rows"], 0.55, first_col=ws.get("first_col"))
    t.h2("Step 3 · Our plan")
    for p, n in ws["plan"]:
        t.answer_box(p, 0.4 + 0.3 * n)
    t.h2("Presentation · 2 minutes")
    t.para("Each person says one sentence in role.", italic=True, muted=True)
    t.grid(["Role", "My sentence"], [1.8, 4.9], len(m["roles"]), 0.45, first_col=[r["name"] for r in m["roles"]])
    t.footer(f"Chart Academy Workforce Credentialing · {C['name']} · Module {nn(m)} Team Notes")
    t.save(f"{out_dir}/{C['prefix']}-Module-{nn(m)}-Team-Notes.docx")


def build(num):
    m = MODULES[num]
    for path, text in ((f"modules/{C['code']}-{nn(m)}.html", accordionize(module_page(m))),
                       (f"slides/{C['code']}-{nn(m)}.html", slides(m)),
                       (f"practice/{C['code']}-{nn(m)}.html", packet(m))):
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    word_files(m, "images/chart-logo-icon.png", "assignments")
    for extra in m.get("extra_builders", []):
        extra()
    print(f"built Module {num}: {strip_tags(m['title'])}")


if __name__ == "__main__":
    course = sys.argv[1] if len(sys.argv) > 1 else "cp"
    arg = sys.argv[2] if len(sys.argv) > 2 else "all"
    C = COURSES[course]
    MODULES = C["modules"]
    for n in (sorted(k for k in MODULES if k >= C["first"]) if arg == "all" else [int(arg)]):
        build(n)

# Project notes: where we left off (October 17, 2026)

Notes for picking the work back up. Live site: https://chart-academy.github.io/Lived-Experience/

Nothing secret is in this file or anywhere in this repo. Tokens and keys live only in Apps Script **Script Properties**.
Answer keys and the grading script live only in the private `_instructor/` folder on the course computer (see the last section).

## What's built

| Area | Status |
|---|---|
| **Community Practitioner** (HS-BCP) | 8 modules: page, slides with presenter notes, in-class packet, Assignment and Team Notes (Word) |
| **Survivor Workforce Facilitator** (women-centered, NADSP DSP-I) | 8 modules, same pieces as above |
| **Job Search Support** (both courses) | Overview page + 6 session pages (J1–J6), each with an AI agent, a Canvas worksheet with an agent log, the AI Job Search Toolkit, a résumé template, and a tracker |
| **Capstone** (both courses) | Page with each capstone's requirements and its 50-point rubric |
| **Credentials** tab | HS-BCP and DSP-I details, the path to the credential, the career ladder |
| **Getting Started** | Accounts, ground rules, Day One Readiness Check for each course |
| **Canvas** | Every "Submit in Canvas" button is connected. No placeholders remain on the site. |
| **Readiness Checks** | Day One and Final for each course (Google Forms). Final forms stay closed until the last class. |
| **Grading** | Separate grading system for these courses (not shared with the AI course). See below. |

## Canvas

- Community Practitioner = course **409**. Survivor Workforce Facilitator = course **410**. (The AI course is 408; keep them separate.)
- Assignment IDs: CP Modules 2537–2544, CP J1–J6 2545–2550, CP Capstone 2569;
  SWF Modules 2551–2558, SWF J1–J6 2559–2564, SWF Capstone 2570. Readiness Check assignments are in a "Readiness Check" group in each course.
- All links live in `_course-build/canvas_links.py`, so module rebuilds keep them.
- Grade posting is Manual: grades stay hidden until a teacher clicks **Post grades**.
- Rubrics: modules and Job Search = 20 points (4 rows × 5: Full 5, Partial 3, Not yet 1). Capstones = 50 points
  (rows of 5 and 10). Readiness: Day One = complete/incomplete, Final = out of 12.

## Readiness Check links

| Course | Day One | Final |
|---|---|---|
| Community Practitioner | https://forms.gle/mdGGdeu43kNwqZxH6 | https://forms.gle/WpZyQhz3vt21vqsFA |
| Survivor Workforce Facilitator | https://forms.gle/NFfAHocgoHp5QT9z9 | https://forms.gle/VJKT8izhshXVdhY4A |

Open and close them from the grading sheet's **Lived Experience Grading** menu. Day One and Final use the same questions,
so the **Readiness Growth** tab shows each student's change.

## Grading system (Google Sheet "Lived Experience · Grading")

- Apps Script file: **LE-Grading**, currently **v3**. Every version is saved as `LE-Grading-vN.gs` with a changelog.
  The first line of **Test connections** shows which version is pasted.
- Script Properties: `CANVAS_TOKEN` (a token from Cedric's own Canvas account) and `ANTHROPIC_API_KEY`.
- Claude gives each submission a first score, row by row, from the private grading key; teachers review and post.
- Tabs: **Canvas Grading** (every grade, with SpeedGrader links and a Regrade column), **Readiness Results**,
  **Readiness Growth**, **Readiness Summary**.

## How to change things

| To change… | Do this |
|---|---|
| A module (CP 2–8, all SWF) | Edit `_course-build/cp_modules.py` or `swf_modules.py`, then `python _course-build/build_module.py cp N` (or `swf N`, or `all`). CP Module 1 is hand-built. |
| Job Search worksheets, toolkit, or tracker | Edit `_course-build/build_job_search.py` or `job_search_agents.py`, then run `build_job_search.py`. Session pages `modules/js-j1.html`–`js-j6.html` are edited directly. |
| Module card pictures or Job Search graphics | `_course-build/make_module_graphics.py`, `make_job_search_graphics.py` |
| Canvas links | `_course-build/canvas_links.py`, then rebuild the modules |
| A rubric or answer key | Edit the course data or `_instructor/answer_keys.py`, run `python3 _instructor/le-grading/build.py` (saves a new version), paste it into Apps Script, then run **Canvas: update rubrics** and **Canvas: update assignment descriptions** |

The full build guide is `_course-build/README.md`. Python needs `python-docx` for the Word files.

## Still to do (final touches)

- [ ] Publish the Canvas assignments in 409 and 410 when students should see them, then turn on automatic grading.
- [ ] Before each cohort, confirm hotline numbers and DC agency details flagged "confirm before class" in the presenter notes
      (CFSA hotline, DC Victim Hotline, DC safe leave and fair chance hiring rules, DC health programs).
- [ ] Confirm the current HS-BCP exam details with CCE and update Module 8 if anything changed.
- [ ] NADSP: confirm the organization contract for the E-Badge Academy, and whether the Survivor course will count as
      NADSP Accredited Education toward the 50-hour badge.
- [ ] Course grade weights in Canvas (modules, Job Search, capstone, readiness) are not set yet.
- [ ] Optional: a Grading page and a Final Assessment page for these courses, like the AI course has.
- [ ] Optional: a teacher's edition (in-class packets, presenter notes, and answer keys in one place).
- [ ] The Credentials page still shows the career-ladder infographic (removed from the home page). Decide whether to keep it.

## Private files (not on GitHub)

These are kept only in `_instructor/` on the course computer, because they contain answer keys or grading details:
the answer keys (`CP-`, `SWF-`, `JS-Answer-Keys.docx` and `answer_keys.py`), the grading script and its versions
(`le-grading/`), and the retired standalone Readiness script. **Back this folder up somewhere private** (for example,
a restricted Google Drive folder). Never upload it to this public repo.

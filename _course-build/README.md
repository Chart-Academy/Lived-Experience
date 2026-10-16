# How this course is built

A guide for continuing work on the Chart Academy Lived Experience courses from any device or any new Claude session. Folders that start with `_` are not published to the website.

**Starting a new Claude session?** Paste this:

> I'm building the Chart Academy Lived Experience courses. Read `_course-build/README.md` in github.com/Chart-Academy/Lived-Experience and follow it. Then continue with the next module.

## The two courses

| Course | Code | National credential |
|---|---|---|
| Certified Community Practitioner | `cp` | HS-BCP (CCE) |
| Certified Survivor Workforce Facilitator | `swf` | DSP-I (NADSP) |

Each course is 80 hours: 45 hours of content (8 modules), 15 hours of Job Search Support (shared by both courses), and a 20-hour capstone. Each course page (`community-practitioner.html`, `survivor-workforce-facilitator.html`) lists its 8 modules with objectives.

## Design rules

1. **Every class follows Learn → Practice → Apply.**
2. **Modules teach the work, not the job hunt.** Job Search Support covers finding jobs.
3. **Practice is a work connection.** Learners role-play practitioners from different agencies working one fictional case as a team. Each role card holds facts only that role knows, so the team has to share to see the whole picture.
4. **Every module ends with a personal lived-experience connection and reflection,** written in the learner's own words.
5. **There is no homework.** Assignments are completed in class and uploaded to Canvas before learners leave.
6. **Learners download a Word (.docx) assignment,** fill it in, and upload it. Paper copies can be uploaded as photos.
7. **Group work includes a downloadable Team Notes file** (.docx). One note-taker fills it in, or the team shares it in Google Docs.
8. **No AI references in either course** unless it's an AI assignment. Only Job Search Support (and its setup in Getting Started) mentions AI.
9. **Cases are fictional.** Never use real client information.
10. **Later:** the in-class packets move into a teacher's edition once the course is built.

## The module pattern

Module 1 of Community Practitioner is the finished model. Copy it for every new module, replacing `cp-01` with the course code and module number (for example `cp-02` or `swf-01`).

| File | What it is |
|---|---|
| `modules/cp-01.html` | Module page: four-hour flow, objectives, embedded slides, team activity, Team Notes download, assignment download, how to submit, rubric |
| `slides/cp-01.html` | Slide deck. Arrow keys move between slides, N shows presenter notes, F goes full screen. Each `<section class="slide">` is one slide, and presenter notes go in `<aside class="notes">`. |
| `practice/cp-01.html` | In-class packet for instructors: printable role cards and a paper team map |
| `assignments/CP-Module-01-Assignment.docx` | Individual assignment. Part 1: your role. Part 2: the team's systems map and plan. Part 3: lived-experience reflection. Rubric: 4 criteria × 5 points = 20. |
| `assignments/CP-Module-01-Team-Notes.docx` | Shared team notes for the group activity |

Shared files: `css/style.css` (site), `css/slides.css` + `js/slides.js` (slide decks), `css/practice.css` (packets).

Then, in the course page's module section, add buttons under that module: **Open Module N**, **Slides**, and **Assignment (.docx)**.

### Four-hour class flow (Module 1 example)

| Time | Block | What happens |
|---|---|---|
| 0:00–0:20 | Open | Welcome and opening circle |
| 0:20–1:30 | Learn | Content slides and a quick check |
| 1:30–1:45 | Break | |
| 1:45–3:15 | Practice | Team roles: 15 min in role, 30 min team huddle, 20 min plan and present, 15 min debrief |
| 3:15–4:00 | Apply | Complete the assignment (Parts 1–2: 10 min, Part 3 reflection: 25 min), upload, exit ticket |

Module hours differ (4–8). Scale the Learn and Practice blocks to fit.

## Making the Word files

The scripts in this folder build the Word files with Python. Install the dependency once with `pip install python-docx`, then run from the repo's root folder:

```
python _course-build/make_cp01_docx.py assignments/CP-Module-01-Assignment.docx images/chart-logo-icon.png
python _course-build/make_cp01_team_notes.py assignments/CP-Module-01-Team-Notes.docx images/chart-logo-icon.png
```

Module 1 of Community Practitioner was built by hand with the two scripts above. Every other module is generated from data:

- `cp_modules.py` holds the content for Community Practitioner Modules 2–8.
- `swf_modules.py` holds the content for Survivor Workforce Facilitator Modules 1–8.
- `build_module.py` writes all five files for a module (page, slides, packet, assignment, team notes). `docx_kit.py` and `accordion.py` are its helpers.

To change a module, edit its entry in the data file and rebuild:

```
python _course-build/build_module.py cp 4      # one module
python _course-build/build_module.py swf all   # a whole course
```

Rebuilding rewrites the module's five files, so make changes in the data file, not in the generated HTML. The Word files use fixed table widths and put Word's table settings in the order Word expects, so they open cleanly in Word, Google Docs, and Pages.

## Publishing

The site is published with GitHub Pages from the `main` branch. Changes go live 1–5 minutes after a commit. Several commits in a row can take longer, because each one restarts the build.

- **On github.com:** use Add file → Upload files. The upload page can't create new folders. To make one, first create a file such as `newfolder/.gitkeep` with Add file → Create new file, then upload into that folder.
- **From a Claude session:** Claude can upload through the Claude in Chrome extension while you're signed in to GitHub, or commit directly if the session has GitHub access.

## Still to do

- [x] Modules 2–8 for Community Practitioner and 1–8 for Survivor Workforce Facilitator
- [ ] Replace placeholder Canvas links (`href="#"`): "Submit in Canvas" and "Start the Readiness Check"
- [ ] Grading page and Final Assessment page
- [ ] Teacher's edition (gather the in-class packets and presenter notes)
- [ ] Confirm credential pathway details with CCE and NADSP

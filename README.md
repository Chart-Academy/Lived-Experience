# Chart Academy Workforce Credentialing: Course Site

Offered by Chart Academy in partnership with IRSJA.

A static course website for two 80-hour courses:

- **Certified Community Practitioner**, leading to HS-BCP (CCE)
- **Certified Survivor Workforce Facilitator** (women-centered), leading to NADSP DSP-I

Each course has 45 hours of content, 15 hours of job search support, and a 20-hour capstone.

**Picking the work back up?** Start with [`_course-build/PROJECT-NOTES.md`](_course-build/PROJECT-NOTES.md): what's built,
Canvas and Readiness Check links, the grading system, how to change things, and what's still to do.

## Files

| File | Page |
|---|---|
| `index.html` | Home: both courses, the 80-hour breakdown, and the career ladder |
| `getting-started.html` | Day one: accounts, ground rules, and the Day One Readiness Check for each course |
| `community-practitioner.html` | Course 1 overview, its 8 module cards, and the Final Readiness Check |
| `survivor-workforce-facilitator.html` | Course 2 overview, its 8 module cards, and the Final Readiness Check |
| `credentials.html` | HS-BCP and DSP-I details and the path to the credential |
| `job-search.html`, `modules/js-j1.html` to `js-j6.html` | Job Search Support overview, and one page per session with its AI agent and Canvas activity |
| `capstone.html` | 20-hour capstone for both courses, with each capstone's rubric |
| `modules/`, `slides/`, `practice/`, `assignments/` | Module pages, class slides, in-class packets, and Word assignments |
| `css/`, `js/`, `images/` | Shared styles (red #D71F2D, blue #3A56A6), scripts, logo, and graphics |
| `_course-build/` | Build scripts and course data (see its README and PROJECT-NOTES) |

## Publish on GitHub Pages (about 10 minutes, no coding)

1. Sign in at github.com. Switch to the `chart-academy` organization so the site lives next to your other courses.
2. Click **+ → New repository**. Name it, for example, `workforce-credentialing`. Set it to **Public**, then click **Create repository**.
3. Click **uploading an existing file**. Drag in all of this folder's contents, including the `css` and `images` folders. Click **Commit changes**.
4. Go to **Settings → Pages**. Under "Build and deployment," set Source to **Deploy from a branch**, Branch to **main**, and folder to **/(root)**. Click **Save**.
5. Wait 1–2 minutes. Your site will be live at `https://<account-name>.github.io/workforce-credentialing/`.

To edit a page later, open the file on GitHub, click the pencil icon, make your change, and click **Commit changes**. The site updates within a minute or two.

## To-do

See the checklist in [`_course-build/PROJECT-NOTES.md`](_course-build/PROJECT-NOTES.md#still-to-do-final-touches).

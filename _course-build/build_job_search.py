"""Build the Job Search Support Canvas activities (Word worksheets, résumé template, tracker template).

Usage, from the repo's root folder (needs python-docx):
  python _course-build/build_job_search.py
"""
import csv

from docx_kit import Kit
from job_search_agents import AGENTS, AI_NOTE

LOGO = "images/chart-logo-icon.png"
OUT = "assignments"
KICKER = "JOB SEARCH SUPPORT · SESSION {n} · CANVAS ACTIVITY"
OWN = ("In your own words · no AI.", "Write this part yourself, without AI. You choose what to share about your own life.",
       "EDF3EE", "3F6B50")
PRIVACY = ("Privacy:", "Never share your address, phone, email, Social Security number, or bank details with an AI tool. "
           "This worksheet goes only to your instructor in Canvas.", "FFF8E1", "8A6900")


def start(n, title, intro, submit):
    k = Kit(LOGO)
    k.header(KICKER.format(n=n), title)
    k.name_date()
    k.h2("About this activity")
    k.para(intro)
    k.bullets([
        ("How to complete it: ", "Download this file, type your answers into the shaded boxes, and save it."),
        ("What to upload to Canvas: ", submit),
        ("Due: ", "By the end of the session. There is no homework."),
        ("Points: ", "20 (see the rubric on the last page)."),
    ])
    k.callout(*PRIVACY)
    return k


def agent_log(k, n):
    a = AGENTS[n]
    k.h2(f"Agent log · {a['name']}")
    k.para("Record how you set up and checked the agent. Starter instructions are on the Job Search page and in the "
           "AI Job Search Toolkit.", italic=True, muted=True)
    k.grid(["", "My answer"], [2.4, 4.3], 4, 0.6,
           first_col=["What I put in the [brackets] (no private details)", "Something the agent got wrong, or I had to check",
                      "How I revised the instructions", "Where I checked it (link, posting, or person)"])


def finish(k, n, rubric, name):
    k.rubric(rubric)
    k.footer(f"Chart Academy Workforce Credentialing · Job Search Support · Session {n} Canvas Activity")
    k.save(f"{OUT}/{name}")
    print("saved", name)


# ---------------------------------------------------------------- J1
k = start("J1", "Your Target Role & Must-Haves",
          "Choose the job you're going after. Look at five real postings, decide what you need from a job, and place your target "
          "role on the career ladder.",
          "this worksheet (.docx), saved as JS-J1-Your-Name.docx.")
k.h2("Part 1 · Five real postings")
k.para("Find five real postings for jobs that fit SOC 21-1093 and your course credential. Use Indeed, DC Government Careers, "
       "or a nonprofit job board.", italic=True, muted=True)
k.grid(["#", "Job title", "Employer", "Pay", "Schedule", "Where I found it"], [0.35, 1.5, 1.45, 0.9, 1.1, 1.4], 5, 0.5,
       first_col=["1", "2", "3", "4", "5"])
k.h2("Part 2 · Must-haves and nice-to-haves")
k.grid(["", "Must-have (I can't take the job without it)", "Nice-to-have"], [1.4, 2.8, 2.5], 4, 0.5,
       first_col=["Pay", "Schedule", "Commute", "Other"])
k.answer_box("1. Which posting is your target role? Why does it fit your must-haves?", 0.9)
k.h2("Part 3 · The career ladder")
k.answer_box("2. Which tier is your target job on (Tier 1 Entry, 2 Practitioner, 3 Leadership, 4 Enterprise)? "
             "What is the next rung, and what would it take to get there?", 1.0)
agent_log(k, "J1")
k.callout(*OWN)
k.answer_box("3. Finish this sentence: “The job I'm going after is … because …”", 0.8)
finish(k, "J1", [
    ["Five postings (Part 1)", "Five real, relevant postings with pay, schedule, and source.", "Three or four, or details missing.", "Fewer than three."],
    ["Must-haves, target, and ladder (Part 2, Part 3)", "Realistic must-haves and a target role placed on the ladder with a next step.", "Partly complete.", "Missing."],
    ["Agent log", "Career Profile Agent set up with no private details, checked, and revised.", "Log is incomplete.", "Missing."],
    ["In your own words (question 3)", "Specific and in the learner's own words.", "General.", "Missing."],
], "JS-J1-Target-Role.docx")

# ---------------------------------------------------------------- J2
k = start("J2", "Résumé from Lived Experience",
          "Turn what you've actually done, at work, as a volunteer, as a peer, as a caregiver, and in your own life, into a résumé "
          "employers hire for. Then tailor it to your target posting.",
          "two files: (1) your tailored résumé (.docx or .pdf) and (2) this worksheet (.docx).")
k.callout("Start here:", "Use the Résumé Template from the Job Search page if you don't have a résumé yet.", "F6F8FC", "3A56A6")
k.h2("Part 1 · From experience to bullet points")
k.para("Write three things you have actually done. Turn each one into an action-and-result bullet point.", italic=True, muted=True)
k.grid(["What I did, in everyday words", "Résumé bullet (action + result)"], [3.0, 3.7], 3, 0.8)
k.answer_box("1. Write your credential and two course competencies the way they will appear on your résumé.", 0.8,
             hint="(Example: “Certified Community Practitioner training, Chart Academy, 2026. HS-BCP candidate.”)")
k.answer_box("2. If you have a gap or justice involvement, write one honest, forward-looking sentence about it. If not, write “Not needed.”",
             0.8)
k.h2("Part 2 · Résumé Optimizer: your changes")
k.para("Remove your address, phone, and email before you paste your résumé into AI. Every change must still be true.",
       italic=True, muted=True)
k.grid(["What AI suggested", "Did I use it? (Yes / Changed it / No)", "Why"], [2.6, 1.6, 2.5], 3, 0.7)
k.answer_box("3. How did you tailor your résumé to your target posting? Name two changes.", 0.9)
agent_log(k, "J2")
k.callout(*OWN)
k.answer_box("4. Finish this sentence: “The biggest change I made to my résumé was … because …”", 0.8)
finish(k, "J2", [
    ["Bullets and credential (Part 1)", "Three true action-and-result bullets and an accurate credential line.", "Bullets are duties, not results.", "Missing, or not true."],
    ["Gap sentence (question 2)", "Honest, brief, and forward-looking, or correctly marked not needed.", "Too long or too much detail.", "Missing."],
    ["AI review and tailoring (Part 2)", "Clear record of AI suggestions and the learner's own decisions; résumé is tailored.", "Partly complete.", "Missing, or résumé not uploaded."],
    ["In your own words (question 4)", "Specific and in the learner's own words.", "General.", "Missing."],
], "JS-J2-Resume-Worksheet.docx")

# Résumé template
k = Kit(LOGO)
k.header("JOB SEARCH SUPPORT · RÉSUMÉ TEMPLATE", "Your Name")
k.para("City, State · Phone · Professional email · LinkedIn (optional)", muted=True)
k.callout("How to use this template:", "Replace every gray line with your own information, then delete these instructions. "
          "Every line must describe something you actually did.", "F6F8FC", "3A56A6")
for heading, lines in (
    ("Summary", ["Two or three sentences: who you are, the role you want, and the strengths you bring, including lived experience."]),
    ("Credentials and Training", ["Certified Community Practitioner (or Certified Survivor Workforce Facilitator) training, Chart Academy, 2026",
                                  "HS-BCP candidate (or NADSP DSP-I in progress)"]),
    ("Skills", ["Case management · Resource navigation · Trauma-informed communication · Documentation · De-escalation · Bilingual (if true)"]),
    ("Experience", ["Job title, Employer, City · Month Year – Month Year",
                    "• Action verb + what you did + result (number if you can)",
                    "• Action verb + what you did + result",
                    "Peer, volunteer, or caregiving role, Organization · Dates",
                    "• Action verb + what you did + result"]),
    ("Education", ["School or program, City · Year (diploma, GED, certificate, or degree)"]),
):
    k.h2(heading)
    for line in lines:
        p = k.para(line, muted=True)
k.footer("Chart Academy Workforce Credentialing · Job Search Support · Résumé Template")
k.save(f"{OUT}/JS-Resume-Template.docx")
print("saved JS-Resume-Template.docx")

# ---------------------------------------------------------------- J3
k = start("J3", "Openings Scorecard",
          "Find 10 real openings, compare each one to your must-haves, and spot any scams.",
          "this worksheet (.docx), saved as JS-J3-Your-Name.docx.")
k.h2("Part 1 · Ten real openings")
k.para("Search Indeed, DC Government Careers, and nonprofit job boards yourself. Rate each opening: Good fit, Not a fit, or Scam.",
       italic=True, muted=True)
k.grid(["#", "Job title and employer", "Source", "Pay", "Meets must-haves?", "Rating", "Why"],
       [0.35, 1.7, 0.9, 0.7, 0.9, 0.85, 1.3], 10, 0.42, first_col=[str(i) for i in range(1, 11)])
k.h2("Part 2 · Scams and next steps")
k.answer_box("1. List three red flags of a scam listing. Did you find any? Describe it without sharing the link.", 1.0)
k.answer_box("2. Which two openings will you apply to first? Write their apply-by dates.", 0.8)
k.answer_box("3. Set up one job alert. What search words and filters did you use?", 0.7)
agent_log(k, "J3")
k.callout(*OWN)
k.answer_box("4. Finish this sentence: “I knew one listing was a scam because …” (or “A listing that looked too good to be true was …”)", 0.8)
finish(k, "J3", [
    ["Ten openings (Part 1)", "Ten real openings, fully filled in, with ratings that match the must-haves.", "Six to nine, or ratings unclear.", "Fewer than six."],
    ["Scams and next steps (questions 1–3)", "Three red flags, two openings with dates, and a job alert.", "Partly complete.", "Missing."],
    ["Agent log", "Skills-to-Openings Agent set up, every ranking checked, instructions revised.", "Log is incomplete.", "Missing."],
    ["In your own words (question 4)", "Specific and in the learner's own words.", "General.", "Missing."],
], "JS-J3-Openings-Scorecard.docx")

# ---------------------------------------------------------------- J4
k = start("J4", "STAR Stories & Interview Practice",
          "Write two STAR stories, practice them with the Interview Practice Coach and with a real person, and decide what you will "
          "share about your lived experience.",
          "this worksheet (.docx), saved as JS-J4-Your-Name.docx.")
k.h2("Part 1 · Two STAR stories")
for i in (1, 2):
    k.para(f"Story {i}. Interview question it answers:", bold=True, after=2)
    k.grid(["", "My story"], [1.3, 5.4], 4, 0.55, first_col=["Situation", "Task", "Action", "Result"])
k.h2("Part 2 · Practice and feedback")
k.grid(["Practice", "Feedback I got", "What I'll change"], [1.6, 2.6, 2.5], 3, 0.6,
       first_col=["AI coach round 1", "AI coach round 2", "Mock interview (person)"])
k.answer_box("1. Who did your mock interview, and what was one thing they said you did well?", 0.7)
agent_log(k, "J4")
k.callout(*OWN)
k.answer_box("2. What will you share about your lived experience in an interview, and what will you keep private? Why?", 1.2)
k.answer_box("3. Finish this sentence: “My strongest STAR story is about … because it shows …”", 0.8)
finish(k, "J4", [
    ["STAR stories (Part 1)", "Two complete stories with a clear action and a real result.", "One complete, or results are vague.", "Missing."],
    ["Practice, feedback, and agent log (Part 2)", "Three practice rounds recorded, with changes made, and a complete agent log.", "Two rounds, or log incomplete.", "Missing."],
    ["Lived experience choices (question 2)", "Thoughtful, safe choice about what to share and why.", "General.", "Missing."],
    ["In your own words (question 3)", "Specific and in the learner's own words.", "General.", "Missing."],
], "JS-J4-STAR-Interview.docx")

# ---------------------------------------------------------------- J5
k = start("J5", "Application Packet",
          "Put together your cover letter, a follow-up email, and your 30-second introduction, and submit or save one real application.",
          "two files: (1) this worksheet (.docx) and (2) a screenshot of your application confirmation or saved job. "
          "Cover your personal information in the screenshot.")
k.h2("Part 1 · Cover letter")
k.answer_box("Write a short cover letter for one real posting (3 short paragraphs: why this job, what you bring, a polite close).", 3.0,
             hint="(You may use AI to check spelling and tone. Every sentence must be true.)")
k.h2("Part 2 · Follow-up email and introduction")
k.answer_box("1. Write a polite follow-up email to send one week after you apply. Include a subject line.", 1.3)
k.grid(["Application", "Details"], [1.8, 4.9], 4, 0.4,
       first_col=["Job title and employer", "Submitted or saved?", "Date submitted, or apply-by date", "Follow-up date"])
agent_log(k, "J5")
k.callout(*OWN)
k.answer_box("2. Write your 30-second introduction for an employer partner.", 1.0,
             hint="(Who you are, your credential, what you're looking for, one strength.)")
finish(k, "J5", [
    ["Cover letter (Part 1)", "Specific to the posting, true, clear, and professional.", "Generic, or has errors.", "Missing."],
    ["Follow-up and application (question 1, table, screenshot)", "Professional follow-up email, and one application submitted or saved with a date and a screenshot.", "Partly complete.", "Missing."],
    ["Agent log", "Every research source opened and checked; the letter is true and in the learner's voice.", "Log is incomplete.", "Missing."],
    ["30-second introduction (question 2)", "Clear, confident, and in the learner's own words.", "General.", "Missing."],
], "JS-J5-Application-Packet.docx")

# ---------------------------------------------------------------- J6
k = start("J6", "Tracker & 90-Day Plan",
          "Set up your application tracker, block time on your calendar, and write a 90-day plan for getting hired and finishing "
          "your credential.",
          "three things: (1) this worksheet (.docx), (2) your tracker (download it from Google Sheets as .xlsx or .csv), and "
          "(3) a screenshot of your calendar for the next two weeks.")
k.callout("Start here:", "Download the Job Search Tracker template from the Job Search page. In Google Sheets, choose File, Import, "
          "Upload, then add every job you've applied to or saved.", "F6F8FC", "3A56A6")
k.h2("Part 1 · My tracker")
k.grid(["", "Answer"], [3.2, 3.5], 3, 0.4,
       first_col=["How many jobs are in my tracker?", "How many have I applied to?", "My next follow-up date"])
k.h2("Part 2 · My 90-day plan")
k.grid(["", "Job search", "Credential", "Taking care of me"], [1.1, 1.9, 1.9, 1.8], 3, 0.8,
       first_col=["Days 1–30", "Days 31–60", "Days 61–90"])
k.answer_box("1. Which weekly times did you block on your calendar for applications and credential steps?", 0.7)
k.answer_box("2. Who will you check in with during the next 90 days (instructor, mentor, classmate), and how often?", 0.7)
agent_log(k, "J6")
k.callout(*OWN)
k.answer_box("3. Finish this sentence: “My next three steps to get hired are …”", 0.9)
finish(k, "J6", [
    ["Tracker and calendar (Part 1 and uploads)", "Tracker with status and follow-up dates, and a calendar with weekly blocks.", "One is incomplete.", "Missing."],
    ["90-day plan and support (Part 2)", "Realistic steps for job search, credential, and self-care, with a check-in plan.", "Some periods missing.", "Missing."],
    ["Agent log", "Job Search Manager set up, its plan checked for conflicts, instructions revised.", "Log is incomplete.", "Missing."],
    ["In your own words (question 3)", "Specific and in the learner's own words.", "General.", "Missing."],
], "JS-J6-Tracker-90-Day-Plan.docx")

with open(f"{OUT}/JS-Job-Search-Tracker.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([
        ["Date found", "Job title", "Employer", "Link", "Pay", "Schedule", "Fits must-haves? (Y/N)",
         "Status (Saved / Applied / Interview / Offer / Not selected)", "Date applied", "Follow-up date", "Interview date", "Offer date", "Contact name", "Notes"],
        ["", "Community Outreach Specialist", "Example Nonprofit", "", "", "Mon–Fri days", "Y", "Saved", "", "", "", "", "", ""],
    ])
print("saved JS-Job-Search-Tracker.csv")

# ---------------------------------------------------------------- AI Job Search Toolkit
k = Kit(LOGO)
k.header("JOB SEARCH SUPPORT · AI JOB SEARCH TOOLKIT", "Your Six Job Search Agents")
k.para("Save a copy of this file in your Google Drive. Fill in the [brackets] yourself, then paste the instructions into your "
       "AI assistant (Gemini, Claude, ChatGPT, or Copilot) to start each agent. Keep your revised versions here so your agents "
       "keep working after the course ends.")
k.callout("Ground rules:", "Remove your address, phone, and email before sharing your résumé. Every line must describe something "
          "you actually did. Check every fact, link, and ranking yourself. Search and apply for jobs yourself; never let AI log in "
          "to a job site or apply for you. Never pay a fee or share bank details or your Social Security number to get a job.",
          "FFF8E1", "8A6900")
for n, a in AGENTS.items():
    k.h2(f"{n} · {a['name']}")
    k.para(a["does"], italic=True, muted=True)
    k.para(f"Tools: {a['tools']} · {a['adapted']}", muted=True, size=9.5)
    for line in (a["prompt"] + "\n\n" + AI_NOTE).split("\n"):
        k.para(line, size=10, after=1)
    k.answer_box("My version (what I put in the brackets, and what I changed after testing):", 1.0)
k.footer("Chart Academy Workforce Credentialing · Job Search Support · AI Job Search Toolkit")
k.save(f"{OUT}/JS-AI-Job-Search-Toolkit.docx")
print("saved JS-AI-Job-Search-Toolkit.docx")

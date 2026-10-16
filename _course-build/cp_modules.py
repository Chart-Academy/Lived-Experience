"""Content for Certified Community Practitioner Modules 2-8.

build_cp_module.py turns each entry into the module page, slides, in-class packet and Word files.
Every case is fictional. Agency names and phone numbers marked "confirm before class" must be checked
by the instructor before each cohort.
"""
import csv

# Minutes for each block, by module length. Breaks are included so the agenda adds up to the full day.
TIMING = {
    4: dict(open=20, learn=70, b1=("Break", 15), practice=90, b2=None, apply=45, steps=(15, 35, 25, 15), p12=10, p3=25),
    5: dict(open=20, learn=90, b1=("Break", 15), practice=115, b2=("Break", 10), apply=50, steps=(20, 40, 30, 25), p12=15, p3=25),
    6: dict(open=20, learn=100, b1=("Lunch", 30), practice=140, b2=("Break", 10), apply=60, steps=(20, 50, 40, 30), p12=20, p3=30),
    7: dict(open=20, learn=120, b1=("Lunch", 45), practice=160, b2=("Break", 15), apply=60, steps=(20, 60, 45, 35), p12=20, p3=30),
    8: dict(open=20, learn=130, b1=("Lunch", 45), practice=190, b2=("Break", 15), apply=80, steps=(25, 75, 55, 35), p12=35, p3=35),
}
WORDS = {4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}


def finish(m):
    """Fill in the timing, flow and short rubric from the module's length."""
    t = TIMING[m["hours"]]
    m["hours_word"] = WORDS[m["hours"]]
    d = m["flow_text"]
    m["flow"] = [
        dict(kind="open", label="Open", min=t["open"], desc=d["open"], agenda=d["open"]),
        dict(kind="learn", label="Learn", min=t["learn"], desc=d["learn"], agenda=d["learn"]),
        dict(kind="break", label=t["b1"][0], min=t["b1"][1], desc="", agenda="Step away, stretch, and eat"),
        dict(kind="practice", label="Practice", min=t["practice"], desc=d["practice"], agenda=d["practice"]),
        dict(kind="break", label=(t["b2"] or ("", 0))[0], min=(t["b2"] or ("", 0))[1], desc="", agenda="Short break"),
        dict(kind="apply", label="Apply", min=t["apply"], desc="Complete and submit your assignment, then an exit ticket",
             agenda="Assignment, upload, and exit ticket"),
    ]
    m["flow"] = [b for b in m["flow"] if b["min"]]
    for s, mins in zip(m["steps"], t["steps"]):
        s["min"] = mins
    for s, mins in zip(m["step_slides"], t["steps"]):
        s["min"] = mins
    m["debrief"]["min"] = t["steps"][3]
    a = m["assignment"]
    a["parts12_min"], a["part3_min"] = t["p12"], t["p3"]
    a["minutes"] = t["p12"] + t["p3"]
    a["rubric"] = [(r[0].split(" (")[0], r[1]) for r in a["rubric_full"]]
    m["opening"].setdefault("min", 15)
    m["quick_check"].setdefault("min", 10)
    return m


def debrief_steps(d1, d2, d3):
    return [
        dict(label="In role, on your own", desc=d1),
        dict(label="Team huddle", desc=d2),
        dict(label="Plan and present", desc=d3),
        dict(label="Debrief", desc="step out of role and talk about what it was like on the other side of the desk."),
    ]


REFLECT_HINT = "(150–250 words.)"

MODULES = {}

# =====================================================================================================
# MODULE 2 · Ethics, Boundaries & Confidentiality
# =====================================================================================================
MODULES[2] = finish(dict(
    num=2, hours=5,
    title="Ethics, Boundaries &amp; Confidentiality",
    short_title="Ethics &amp; Boundaries",
    slide_title_html="Ethics, Boundaries<br>&amp; Confidentiality",
    subtitle="Doing the right thing when you know the neighborhood, the family, and the story.",
    title_notes="Welcome everyone back. Today is about trust: how practitioners earn it, protect it, and sometimes have to explain its limits. Many learners will work in the same community they come from. That is a strength, and it also means ethical questions show up at the grocery store, at church, and online. Say that today has no trick questions. Most real dilemmas have more than one reasonable answer, and the skill is how you think it through.",
    lead="The ethical standards of human services, what you can and can't keep private, and how to hold boundaries when you work in your own community. You'll learn the standards, work through real dilemmas as a team, and plan for the boundaries you'll need to watch.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Ethical standards, confidentiality and its limits, mandated reporting, and boundaries",
                   practice="Team roles: the ethics case conference for Tanya's case"),
    objectives=[
        "Apply the National Organization for Human Services (NOHS) Ethical Standards for Human Services Professionals to practice situations.",
        "Explain confidentiality, informed consent, and the limits of confidentiality, including mandated reporting.",
        "Recognize boundary risks and dual relationships when working in one's own community, and plan how to handle them.",
        "Identify information that may never be shared without consent, and how to say no respectfully.",
    ],
    slide_objectives=[
        "Use the NOHS Ethical Standards to think through a real situation",
        "Explain confidentiality and its limits in plain words",
        "Know when you must make a report, and how",
        "Spot and handle boundary risks in your own community",
    ],
    opening=dict(title="Who did you trust, and why?",
                 quote="Think of a time you trusted a helper, a teacher, a counselor, a caseworker, with something private. What did they do that made it safe? Or think of a time that trust was broken. What happened?",
                 notes="Give one minute of quiet thinking first. Write the trust-builders people name on the board: kept my business private, told me the truth, did what they said, didn't judge me. Keep the list up. By the end of Learn, every item on it will connect to an ethical standard. If someone shares a time trust was broken, thank them and don't ask for details."),
    learn_line="The standards, the limits of confidentiality, and the boundaries that protect clients and you.",
    learn=[
        dict(eyebrow="The standards", title="NOHS Ethical Standards",
             body="""  <p>The National Organization for Human Services publishes the ethical standards for our field. They are organized by who you are responsible to:</p>
  <div class="cols3">
    <div class="box c2"><h3>Clients</h3>Respect, dignity, informed consent, privacy, and acting in their best interest</div>
    <div class="box c3"><h3>The public and society</h3>Advocacy, fairness, and respect for diverse communities</div>
    <div class="box c4"><h3>Colleagues</h3>Cooperation, respect, and addressing ethical concerns properly</div>
    <div class="box c1"><h3>Employers</h3>Following agency policy and raising concerns through the right channels</div>
    <div class="box c2"><h3>The profession</h3>Honesty about your skills and credentials, and continued learning</div>
    <div class="box c3"><h3>Self</h3>Self-awareness, self-care, and knowing your own biases</div>
  </div>""",
             notes="Hand out or project the current NOHS Ethical Standards (available on the NOHS website). Do not ask learners to memorize standard numbers. The skill is knowing which area applies and what it asks of you. The HS-BCP exam expects learners to apply ethics to scenarios, so connect every example today back to one of these areas."),
        dict(eyebrow="Confidentiality", title="What stays private, and why",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Confidentiality</strong> means what a client tells you stays inside the agency and is shared only with the people who need it to help them.</li>
        <li><strong>Informed consent</strong> means the client knows what you'll do, what you'll share, with whom, and why, and agrees to it.</li>
        <li><strong>A release of information</strong> is the signed form that lets you share specific information with a specific agency.</li>
      </ul>
    </div>
    <div class="box c2"><h3>Never without consent</h3>Whether someone is your client at all. Their health, mental health, or substance use history. Their immigration status, criminal record, or address. What they told you in private.</div>
  </div>""",
             notes="Stress that even confirming someone is a client breaks confidentiality. Practice the phrase: “I'm not able to say whether someone receives services here.” Ask learners to repeat it out loud. Mention that some records have extra federal protection, such as substance use treatment records (42 CFR Part 2) and health information (HIPAA). We go deeper on records in Module 7."),
        dict(eyebrow="The limits", title="When you can't keep it private",
             body="""  <p>Tell clients the limits at the start, before they share, not after.</p>
  <table class="tbl">
    <tr><th>Situation</th><th>What it means for you</th></tr>
    <tr><td><strong>Risk of serious harm to self</strong></td><td>Follow agency safety procedures and get your supervisor right away</td></tr>
    <tr><td><strong>Threat of serious harm to someone else</strong></td><td>Follow agency procedures. You may need to warn or report.</td></tr>
    <tr><td><strong>Suspected child abuse or neglect</strong></td><td>Mandated report (next slide)</td></tr>
    <tr><td><strong>Suspected abuse of a vulnerable adult</strong></td><td>Report under agency policy and DC law</td></tr>
    <tr><td><strong>Court order</strong></td><td>Your supervisor and agency legal staff handle the response</td></tr>
  </table>""",
             notes="Model how to explain the limits in plain words: “What you tell me stays private, with a few exceptions. If I'm worried you might be hurt or might hurt someone, or if a child is being hurt, I have to get help. I'll always tell you if that happens.” Have learners practice saying it to a partner in their own words."),
        dict(eyebrow="Mandated reporting · DC", title="If you suspect a child is being hurt",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>You don't need proof. Reasonable suspicion is enough.</li>
        <li>Don't investigate or question the child in detail.</li>
        <li>Call the DC Child and Family Services Agency (CFSA) hotline: <strong>(202) 671-SAFE (7233)</strong>, 24 hours.</li>
        <li>Tell your supervisor and follow agency policy.</li>
        <li>Write down what you saw and heard, in facts, the same day.</li>
      </ol>
    </div>
    <div class="box c1"><h3>Remember</h3>The report is yours to make. Telling your supervisor doesn't replace it unless your agency's policy says the supervisor files it with you.</div>
  </div>""",
             notes="Confirm before class: the CFSA hotline number, and the current list of mandated reporters in the DC Code (social service workers are on it). Some learners may have had CFSA involvement in their own families. Acknowledge that this can bring up strong feelings. The purpose of a report is safety and support for the family, and the practitioner's job is to report, not to decide."),
        dict(eyebrow="Boundaries", title="Working in your own community",
             body="""  <div class="cols">
    <div>
      <p><strong>A dual relationship</strong> is when you have another connection to a client besides being their practitioner: neighbor, church member, relative, old friend, landlord, coworker.</p>
      <p>In a close community, some overlap can't be avoided. The goal is to manage it, not pretend it isn't there.</p>
    </div>
    <div class="box c3"><h3>Manage it</h3>
      Tell your supervisor. Ask if the case should go to a coworker. Talk with the client about how you'll act if you see each other outside. Never use what you learned at work in your personal life.</div>
  </div>""",
             notes="This is where lived experience is both a strength and a risk. Ask: “Who here would almost certainly run into a client at the store, at church, or on the bus?” Most hands go up. Normalize it. Then ask: “What would you say if a client waved and said, ‘Hey, you're my caseworker!’ in front of your friends?” Practice: let the client lead. If they greet you, greet them back. Never mention the agency."),
        dict(eyebrow="Gray areas", title="Gifts, social media, and sharing your story",
             body="""  <table class="tbl">
    <tr><th>Situation</th><th>Usually okay</th><th>Usually not okay</th></tr>
    <tr><td><strong>Gifts</strong></td><td>A thank-you card, a small token, under agency policy</td><td>Money, services, expensive gifts, anything that creates a debt</td></tr>
    <tr><td><strong>Social media</strong></td><td>An agency page with agency rules</td><td>Friending or following clients, posting about your day at work</td></tr>
    <tr><td><strong>Self-disclosure</strong></td><td>A brief share, only when it helps the client</td><td>Long stories, sharing to feel better yourself, sharing details you haven't healed from</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Always check your agency's written policy. When in doubt, ask your supervisor first.</p>""",
             notes="Self-disclosure is a big topic for a lived experience course. Teach the test: “Who is this for?” If it is for the client, keep it short and bring it back to them. If it is for you, save it for supervision or your own support. Peer roles may share more by design. Practitioner roles share less."),
        dict(eyebrow="A method", title="Six steps for an ethical decision",
             body="""  <ol>
    <li><strong>Name the problem.</strong> What is the conflict, and whose interests are involved?</li>
    <li><strong>Check the standards and the rules.</strong> NOHS standards, agency policy, and the law.</li>
    <li><strong>Think about who is affected.</strong> The client, family, community, agency, and you.</li>
    <li><strong>List the options</strong> and what could happen with each.</li>
    <li><strong>Consult.</strong> Talk with your supervisor before you act, unless someone is in danger right now.</li>
    <li><strong>Act and document.</strong> Do it, then write down what you did and why.</li>
  </ol>""",
             notes="Teams will use these six steps in Practice. Point out that step 5 is not optional for a new practitioner. Asking is a strength, not a weakness. Supervisors would always rather hear about a dilemma before than after."),
    ],
    quick_check=dict(title="Okay, not okay, or it depends?",
                     items=["A client's mother calls and asks if her son came to his appointment.",
                            "A client gives you a homemade card that says thank you.",
                            "You see a client at the grocery store. They don't say hello, so you don't either.",
                            "A 10-year-old tells you her dad hit her with a belt last night.",
                            "You share a client's story with your best friend, without a name."],
                     notes="Answers: 1) Not okay to confirm without a release. 2) Usually okay, check policy. 3) Okay, let the client lead. 4) Mandated report. 5) Not okay. Details can identify someone, especially in a small community. Move quickly; Practice goes deeper."),
    practice_line="Step into a role and run an ethics case conference as a team.",
    practice_notes="Hand out the in-class packet. One packet per team. Teams of 4 or 5 can combine the Team lead with another role.",
    activity_title="Team roles: Tanya's ethics case conference",
    team_notes_title="Tanya's Ethics Case Conference",
    case=dict(
        name="Tanya",
        page_intro="<strong>Tanya, 29</strong> (fictional), is a single mother of a 6-year-old who has come to a neighborhood resource center for help with back rent. The center is in the same neighborhood where one of its outreach workers grew up, and several ethical questions come up in the same week.",
        page_how="Each person on your team plays a staff member who faced one of those questions. Your role card has the facts only you know. In the case conference, your team uses the six steps to decide what to do about each one.",
        slide_title="Meet Tanya",
        slide_intro="<strong>Tanya, 29</strong>, came to a neighborhood resource center for help with two months of back rent. She has a 6-year-old son.",
        bullets=["She lives three blocks from the center",
                 "One outreach worker knows her family from church",
                 "Several staff each hit an ethical question this week",
                 "Today's team meeting is an ethics case conference"],
        quote="“I almost didn't come in. Everybody around here knows everybody. I need to know my business stays my business.”",
        quote_label="What Tanya says",
        slide_notes="Read the case aloud. Point out what Tanya said: her biggest worry is privacy. Every decision the team makes today should be checked against that worry, and against the limits of confidentiality.",
        packet_text="<strong>Tanya, 29</strong>, came to a neighborhood resource center for help with two months of back rent. She lives three blocks away with her 6-year-old son. She signed a release of information that lets the center share her information with the rental assistance program only. One of the center's outreach workers grew up in the neighborhood and knows Tanya's family from church. This week, several staff members each ran into an ethical question about Tanya's case. Today is the team's ethics case conference.",
    ),
    roles_title="Six staff, six questions",
    roles_small="Each card has facts only you know. Bring them to the case conference.",
    roles_notes="Assign roles on purpose. The family support worker card is the mandated reporting situation and works best with a confident learner. Remind teams that the Team lead runs the six steps for each question.",
    roles=[
        dict(name="Intake coordinator", where="Front desk and intake",
             facts=["Tanya's cousin called yesterday and asked, “Is Tanya getting help there? Her mom wants to know.”",
                    "You said, “I think so, let me check,” then stopped yourself and said you'd call back.",
                    "Tanya's release covers the rental assistance program only."],
             need="Advice on what to say when you call the cousin back, and whether to tell Tanya."),
        dict(name="Outreach worker", where="Grew up in the neighborhood",
             facts=["You've known Tanya's family from church for 15 years. Tanya's aunt is your mother's friend.",
                    "Tanya sent you a friend request on social media last night.",
                    "She offered to braid your daughter's hair for free “to say thank you.”",
                    "You haven't told your supervisor you know the family."],
             need="A plan for the dual relationship that keeps Tanya's trust."),
        dict(name="Housing specialist", where="Rental assistance",
             facts=["Tanya's landlord called and asked you to send “her full history” before he agrees to a payment plan.",
                    "Tanya asked you to leave a past eviction off her rental assistance application because “it was years ago.”",
                    "The application asks about past evictions and says answers must be true."],
             need="What you can share with the landlord, and how to talk with Tanya about the eviction question."),
        dict(name="Family support worker", where="Home visits",
             facts=["On a home visit, Tanya's son had a bruise on his upper arm.",
                    "When Tanya went to answer the door, he said, “Mom's boyfriend gets real mad sometimes.”",
                    "Tanya seemed nervous and asked you not to mention the boyfriend to anyone."],
             need="The team to confirm your next steps today, and how to stay honest with Tanya.",
             extra="This is a mandated reporting situation. The team decides how, not whether."),
        dict(name="Program assistant", where="Events and records",
             facts=["A coworker posted photos from the center's back-to-school event. Tanya and her son are in one, with the center's name in the caption.",
                    "Tanya didn't sign a photo release.",
                    "In the break room, two staff talked about Tanya's rent situation by name while a volunteer was there."],
             need="What to do about the photo, and how to raise the break-room talk."),
        dict(name="Team lead", where="Runs the case conference",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Walk the team through the six steps for each question.",
                    "Write each decision on the team's decision table."],
             extra="<strong>Only you know:</strong> agency policy says staff may accept thank-you cards but not services or gifts worth more than $10, and dual relationships must be reported to a supervisor."),
    ],
    steps=debrief_steps("read your card and decide what you think is right before you hear the others.",
                        "each role presents its question. Use the six steps and fill in the decision table.",
                        "pick the hardest question, explain your decision, and write what you'll say to Tanya."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>Read the facts only you know</li>
    <li>Write down: what is the ethical question?</li>
    <li>Which area of the standards applies: clients, colleagues, employer, public, profession, or self?</li>
    <li>What do <em>you</em> think should happen?</li>
  </ul>""",
             notes="Walk the room. Some learners will want to jump to an answer. Ask them to name the question first. For the family support worker, quietly confirm they understand this is a mandated report."),
        dict(eyebrow="Step 2 · team huddle", title="Run the case conference",
             body="""  <div class="cols">
    <div>
      <p>For each role's question, the Team lead walks through the six steps:</p>
      <ol class="small">
        <li>Name the problem</li><li>Check the standards and rules</li><li>Who is affected?</li>
        <li>List the options</li><li>Consult</li><li>Act and document</li>
      </ol>
    </div>
    <div class="box c3"><h3>Decision table</h3>Write each situation, your call (okay, not okay, or it depends), the standard, and what you'll do.</div>
  </div>""",
             notes="Teams often spend too long on the first question. Call time every 8 minutes. Make sure every team handles the child's bruise as a required report and decides who calls and when."),
        dict(eyebrow="Step 3 · plan and present", title="What will you say to Tanya?",
             body="""  <ul>
    <li>Your team's <strong>hardest question</strong>, and how you decided</li>
    <li>The <strong>exact words</strong> you'll use to explain one decision to Tanya</li>
    <li>What goes to your <strong>supervisor</strong></li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Each person says one sentence in role.</div>""",
             notes="Listen for whether teams protect Tanya's dignity while still meeting the limits of confidentiality. Praise teams that plan to tell Tanya about the report rather than hide it, when it is safe for the child."),
    ],
    debrief=dict(questions=["Which question was hardest, and why?",
                            "Did anyone change their mind after hearing the team?",
                            "Where did your own community show up in this case?",
                            "What will you do the first time a client sends you a friend request?"],
                 notes="Step out of role. Ask learners to notice how much of ethics is about relationships, not rules. Connect back to the opening list of trust-builders."),
    apply_line="Show what you learned, then connect it to your own community.",
    own_words="“A boundary I will need to watch in my own community is … and I will handle it by …”",
    exit_ticket=["Say in one sentence how you'd explain the limits of confidentiality to a client.",
                 "What number do you call to report suspected child abuse in DC?",
                 "One question you still have about ethics or boundaries."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. The Team lead holds the decision table. Confirm the CFSA hotline number before class.",
    worksheet=dict(
        title="Decision table",
        instructions="For each role's question, write your team's call (okay, not okay, or it depends), the area of the standards that applies, and what you will do.",
        columns=[("Situation", 24), ("Our call", 14), ("Standard area", 18), ("What we will do", 0)],
        rows=6,
        first_col=["Cousin's call", "Friend request and gift", "Landlord and the eviction question", "Child's bruise",
                   "Photo and break-room talk", "Not telling the supervisor"],
        plan=[("Our hardest question, and how we decided:", 2),
              ("The exact words we'll use with Tanya:", 2),
              ("What we'll bring to our supervisor:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "The ethical question", "What I thought before the huddle"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.6, 0.9, 1.3, 2.9]),
    assignment=dict(
        intro="Capture the ethical thinking from your team's case conference, then plan for the boundaries in your own community.",
        parts=[
            dict(title="Your role's question", summary="The dilemma your role faced, the standard that applies, and what you'd say.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What was your role's ethical question? Explain it in your own words.", h=0.8),
                        dict(type="q", text="Which area of the NOHS Ethical Standards applies, and why?", h=0.8,
                             hint="(Clients, the public and society, colleagues, employers, the profession, or self.)"),
                        dict(type="q", text="What would you do? Write what you would say, as if you are talking to the person.", h=1.0)]),
            dict(title="Your team's decisions", summary="Your team's calls on all six questions, mandated reporting steps, and the limits of confidentiality in plain words.",
                 note="Use your team's decision table from class.",
                 items=[dict(type="grid", text="Fill in your team's decision for each situation.",
                             columns=["Situation", "Our call", "Why"], widths=[2.0, 1.2, 3.5], rows=6, h=0.5,
                             first_col=["Cousin's call", "Friend request and gift", "Landlord and eviction",
                                        "Child's bruise", "Photo and break-room talk", "Not telling the supervisor"]),
                        dict(type="q", text="List the steps for the child's bruise, in order, including who calls and what number.", h=1.0),
                        dict(type="q", text="Explain the limits of confidentiality the way you would say it to Tanya on her first day.", h=1.0,
                             hint="(Plain words, 3–5 sentences.)")]),
            dict(title="Boundaries in my community", summary="The boundary risks in your own community and your plan to handle them, in your own words.",
                 items=[dict(type="grid", text="Name two places in your own life where you might run into a client.",
                             columns=["Where", "What could happen", "How I'll handle it"], widths=[1.8, 2.45, 2.45], rows=2, h=0.7,
                             first_col=["1.", "2."]),
                        dict(type="q", text="Has someone ever kept, or broken, your trust when you were getting help? How will that experience shape the way you protect your clients' privacy?",
                             h=2.4, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “A boundary I will need to watch in my own community is … and I will handle it by …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's question (Part 1)", "Names the dilemma, the right standard area, and a realistic, respectful response.",
             "Dilemma is named. The standard or response is unclear.", "Missing, or the response breaks confidentiality."],
            ["Team decisions (Part 2 table)", "A sound call and reason for all six situations.",
             "Most situations complete, or reasons are thin.", "Few situations complete."],
            ["Mandated reporting and limits (Part 2, questions 6–7)", "Correct reporting steps and number. Limits explained in plain, respectful words.",
             "Steps are partly correct, or the explanation uses jargon.", "Reporting steps are wrong or missing."],
            ["Community boundaries (Part 3)", "Specific places and plans. Reflection is thoughtful and in the learner's own words.",
             "Places or plans are general, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's question and your team's decisions.",
        reflection_title="Boundaries in my community",
        reflection_slide="Name two places in your own life where you might run into a client, and how you'll handle each. Then write about a time someone kept or broke your trust, and what it teaches you about protecting your clients.",
    ),
))

# =====================================================================================================
# MODULE 3 · Trauma-Informed Practice
# =====================================================================================================
MODULES[3] = finish(dict(
    num=3, hours=6,
    title="Trauma-Informed Practice",
    short_title="Trauma-Informed Practice",
    slide_title_html="Trauma-Informed<br>Practice",
    subtitle="Asking “what happened to you?” instead of “what's wrong with you?”",
    title_notes="Set the tone before you start: today's topic can bring up personal memories. Tell learners they can step out at any time, no explanation needed, and that they never have to share their own trauma. Point out where water and tissues are and who to talk to if something comes up. Name one or two crisis lines on the board (988 Suicide and Crisis Lifeline, call or text 988). Many learners will bring deep lived knowledge to this module. Honor that.",
    lead="How trauma shapes the way people show up for help, and how to make every step of the process safer. You'll learn SAMHSA's six principles, rewrite a harmful intake as a team, and make a plan to care for yourself in this work.",
    flow_text=dict(open="Welcome, ground rules, and opening circle",
                   learn="What trauma is, trauma responses, SAMHSA's six principles, and vicarious trauma",
                   practice="Team roles: redesign Rosa's intake"),
    objectives=[
        "Explain the four Rs and the six principles of a trauma-informed approach from SAMHSA.",
        "Recognize common trauma responses and avoid practices that re-traumatize clients.",
        "Rewrite intake questions and everyday language to be trauma-informed.",
        "Create a personal plan to prevent burnout and manage vicarious trauma.",
    ],
    slide_objectives=[
        "Explain the four Rs and SAMHSA's six principles",
        "Recognize trauma responses, and what makes them worse",
        "Rewrite intake questions to be trauma-informed",
        "Make your own plan for burnout and vicarious trauma",
    ],
    opening=dict(title="A place that felt safe",
                 quote="Think of a place, an office, a clinic, a school, a church, where you felt safe and respected the moment you walked in. What did you notice? What did people do or say?",
                 notes="Do not ask about trauma in the opening. Ask about safety. Write what people name: someone greeted me, they explained what would happen, I wasn't rushed, it was quiet, I could choose where to sit. That list will match SAMHSA's principles almost exactly. Point that out later."),
    learn_line="What trauma does, what helps, and how to protect yourself in this work.",
    learn=[
        dict(eyebrow="The basics", title="What trauma is",
             body="""  <div class="cols">
    <div>
      <p>SAMHSA describes trauma with <strong>three Es</strong>:</p>
      <ul>
        <li><strong>Event:</strong> what happened, once, many times, or over years</li>
        <li><strong>Experience:</strong> how the person lived it. The same event affects people differently.</li>
        <li><strong>Effects:</strong> lasting effects on health, trust, relationships, and daily life</li>
      </ul>
    </div>
    <div class="box c2"><h3>It's common</h3>Many people who come for services have lived through violence, loss, incarceration, homelessness, racism, or community violence. Assume anyone could have a trauma history, without asking them to prove it.</div>
  </div>""",
             notes="This framework comes from SAMHSA's Concept of Trauma and Guidance for a Trauma-Informed Approach (2014). Name historical and community trauma, not just individual events. Keep the focus on the practitioner's role: we don't diagnose or treat trauma. We make our services safer."),
        dict(eyebrow="The four Rs", title="A trauma-informed program…",
             body="""  <div class="cols">
    <div class="box c2"><h3>Realizes</h3>how common trauma is and how it affects people</div>
    <div class="box c3"><h3>Recognizes</h3>the signs of trauma in clients, families, and staff</div>
    <div class="box c4"><h3>Responds</h3>by building this knowledge into policies, practices, and language</div>
    <div class="box c1"><h3>Resists re-traumatization</h3>by changing what hurts people, even by accident</div>
  </div>""",
             notes="Ask: “Have you ever been in a service setting that re-traumatized you or someone you know?” Examples learners often name: being searched, waiting for hours, telling their story over and over, being talked about in front of them, rules enforced with no explanation."),
        dict(eyebrow="Trauma responses", title="When the body feels danger",
             body="""  <table class="tbl">
    <tr><th>Response</th><th>What it can look like in an office</th><th>What can help</th></tr>
    <tr><td><strong>Fight</strong></td><td>Raised voice, arguing, “attitude”</td><td>Stay calm, lower your voice, give space and choices</td></tr>
    <tr><td><strong>Flight</strong></td><td>Leaving, missing appointments, rushing</td><td>Shorter visits, clear next steps, follow up</td></tr>
    <tr><td><strong>Freeze</strong></td><td>Going quiet, blank stare, “I don't know”</td><td>Slow down, check in, offer a break</td></tr>
    <tr><td><strong>Fawn</strong></td><td>Agreeing to everything, over-apologizing</td><td>Check real understanding, make it safe to say no</td></tr>
  </table>""",
             notes="These are survival responses, not character flaws. A client who “has an attitude” may be in fight mode. A client who “isn't motivated” may be in freeze. Ask: “How would you have described this client before today? How would you describe them now?”"),
        dict(eyebrow="SAMHSA's six principles", title="A trauma-informed approach",
             body="""  <div class="cols3">
    <div class="box c2"><h3>1. Safety</h3>Physical and emotional safety for clients and staff</div>
    <div class="box c3"><h3>2. Trustworthiness and transparency</h3>Clear explanations, decisions made openly</div>
    <div class="box c4"><h3>3. Peer support</h3>People with lived experience help build safety and hope</div>
    <div class="box c1"><h3>4. Collaboration and mutuality</h3>Sharing power. Healing happens in relationships.</div>
    <div class="box c2"><h3>5. Empowerment, voice, and choice</h3>Building on strengths and real choices</div>
    <div class="box c3"><h3>6. Cultural, historical, and gender issues</h3>Recognizing bias, history, and identity</div>
  </div>""",
             notes="Go back to the opening list on the board. Match each item to a principle. Point out principle 3: peer support is a core part of a trauma-informed approach. That is where many people in this room fit."),
        dict(eyebrow="In practice", title="Small changes, big difference",
             body="""  <table class="tbl">
    <tr><th>Instead of…</th><th>Try…</th><th>Principle</th></tr>
    <tr><td>“You have to answer all of these.”</td><td>“You can skip any question you don't want to answer.”</td><td>Voice and choice</td></tr>
    <tr><td>“Why didn't you…?”</td><td>“What happened next?”</td><td>Safety</td></tr>
    <tr><td>Starting the form right away</td><td>“Here's what we'll do today and how long it takes.”</td><td>Transparency</td></tr>
    <tr><td>“Non-compliant”</td><td>“Couldn't make it to the last two appointments”</td><td>Collaboration</td></tr>
  </table>""",
             notes="These are the kinds of rewrites teams will do in Practice. Ask learners to add one more example from their own experience."),
        dict(eyebrow="Taking care of you", title="Burnout and vicarious trauma",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Vicarious trauma:</strong> taking on the effects of trauma by hearing others' stories again and again</li>
        <li><strong>Compassion fatigue:</strong> feeling numb, drained, or unable to care as much</li>
        <li><strong>Burnout:</strong> exhaustion from workload and stress over time</li>
      </ul>
    </div>
    <div class="box c1"><h3>Warning signs</h3>Trouble sleeping, irritability, dreading work, feeling hopeless, thinking about clients' stories at home, using more alcohol or other substances. Lived experience can make this hit closer to home.</div>
  </div>""",
             notes="Say clearly: having your own history does not make you a worse practitioner. It means you need a plan. Your plan should include supervision, someone outside work you can talk to, and a way to leave work at work. Remind learners of 988 and the employee assistance programs many agencies offer."),
    ],
    quick_check=dict(title="Which principle?",
                     items=["Telling a client exactly how long the intake will take and what happens next.",
                            "Letting a client choose whether to meet in the office or by phone.",
                            "A peer specialist who has been homeless co-leads the housing group.",
                            "Making sure the waiting room has no TV playing violent news.",
                            "Offering forms in the client's first language."],
                     notes="Answers: 1) Trustworthiness and transparency. 2) Empowerment, voice, and choice. 3) Peer support. 4) Safety. 5) Cultural, historical, and gender issues. More than one principle can fit. Accept good reasoning."),
    practice_line="Step into a role and redesign an intake that hurt the person it was meant to help.",
    practice_notes="Hand out the in-class packet. Remind learners that Rosa is fictional. If the case brings up something personal for anyone, they can step out or switch to the Team lead role.",
    activity_title="Team roles: redesign Rosa's intake",
    team_notes_title="Redesigning Rosa's Intake",
    case=dict(
        name="Rosa",
        page_intro="<strong>Rosa, 37</strong> (fictional), left an abusive partner three weeks ago with her 12-year-old son. She came to a family services center for help, sat through the center's standard intake, and left halfway through.",
        page_how="Each person on your team plays a staff member who saw part of what happened. Your role card has facts only you know. Together, your team rewrites the intake form so the next person in Rosa's situation feels safe enough to stay.",
        slide_title="Meet Rosa",
        slide_intro="<strong>Rosa, 37</strong>, left an abusive partner three weeks ago and is staying with a friend with her 12-year-old son.",
        bullets=["She came to a family services center for help",
                 "The intake took place in a busy room",
                 "Halfway through the form, she got up and left",
                 "Your team's job: fix the intake so the next Rosa stays"],
        quote="“They asked me why I stayed so long. I didn't have an answer that wouldn't make me cry in front of a stranger. So I left.”",
        quote_label="What Rosa told a friend",
        slide_notes="Read the case slowly. Pause after the quote. Ask: “Which principle did that question break?” (Safety; voice and choice.) Then hand out the cards.",
        packet_text="<strong>Rosa, 37</strong>, left an abusive partner three weeks ago with her 12-year-old son, Mateo. They are staying on a friend's couch. Rosa came to a family services center for help with housing and school for Mateo. The center used its standard intake form, in a busy room, with no explanation of what would happen. Halfway through, Rosa got up and left. Later she told the peer support specialist why. The center has asked your team to fix the intake.",
    ),
    roles_title="Six staff, one intake",
    roles_small="Each card has facts only you know. You'll need all six to fix the intake.",
    roles_notes="The Peer support specialist card holds the most important facts. Give it to a learner who is comfortable speaking up. Any learner can swap to Team lead if the content is hard for them.",
    roles=[
        dict(name="Intake worker", where="Did Rosa's intake",
             facts=["The intake was in the shared front room. Other clients could hear.",
                    "You read the questions straight from the form, as you were trained.",
                    "Rosa jumped when a door slammed, and moved to the chair closest to the exit.",
                    "She left right after the question “Why didn't you leave sooner?”"],
             need="A new script for the first five minutes of intake."),
        dict(name="Domestic violence advocate", where="Partner agency",
             facts=["Rosa's partner controlled the money and her phone. She is afraid he can find her.",
                    "The form asks for her current address. She doesn't want it written anywhere.",
                    "She has told her story to police, a hospital, and a shelter hotline in three weeks."],
             need="An intake that doesn't make her tell the whole story again, and protects her location."),
        dict(name="Housing navigator", where="Housing programs",
             facts=["Rosa may qualify for housing help for survivors of domestic violence.",
                    "The application needs some information, but not the details of the abuse.",
                    "The current form asks for every address she has had in five years."],
             need="To know which questions are really needed for housing, and which can wait."),
        dict(name="Youth and family worker", where="School and family support",
             facts=["Mateo's teacher says he is “defiant” and “refuses to follow directions.”",
                    "Mateo has trouble sleeping and gets angry when adults raise their voices.",
                    "The intake form asks the parent to rate the child's “behavior problems.”"],
             need="A trauma-informed way to ask about Mateo that doesn't label him."),
        dict(name="Peer support specialist", where="Has lived experience of leaving abuse",
             facts=["Rosa told you she almost didn't come in. The waiting room TV was showing a crime show.",
                    "She said: “I want to decide what I share and when. Nobody has let me decide anything in years.”",
                    "She said she would come back if she could meet somewhere quieter, with someone she has met before."],
             need="The team to build choice into every step."),
        dict(name="Team lead", where="Runs the redesign meeting",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Go through the old intake questions one by one.",
                    "Write the team's rewrites on the worksheet."],
             extra="<strong>Only you know:</strong> the center's director has agreed to change the form, the room, and the script, but needs a one-page plan by the end of the day."),
    ],
    steps=debrief_steps("read your card and mark the old intake questions you think caused harm.",
                        "share what you know, then go through each old question: which principle does it break, and how would you rewrite it?",
                        "write the new first five minutes of intake and three changes to the room or process."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card and the old form",
             body="""  <ul>
    <li>Read the facts only you know</li>
    <li>Read the eight old intake questions on the team worksheet</li>
    <li>Mark the ones your role thinks caused harm</li>
    <li>Which of SAMHSA's six principles do they break?</li>
  </ul>""",
             notes="Most learners will mark almost every question. That's fine. Ask them to pick the two worst from their role's point of view."),
        dict(eyebrow="Step 2 · team huddle", title="Rewrite the intake",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role shares what they know</li>
        <li>For each old question: keep it, change it, move it later, or drop it?</li>
        <li>Write the rewrite and the principle</li>
      </ol>
    </div>
    <div class="box c3"><h3>Test every question</h3>Do we need this today? Does Rosa know why we're asking? Can she skip it? Is it in plain words?</div>
  </div>""",
             notes="Push teams to drop or delay questions, not just reword them. A trauma-informed intake asks only what is needed now. Check that teams handle the address question safely."),
        dict(eyebrow="Step 3 · plan and present", title="The new first five minutes",
             body="""  <ul>
    <li>What staff <strong>say first</strong> when Rosa sits down</li>
    <li>Three changes to the <strong>room or process</strong></li>
    <li>Your team's <strong>best rewrite</strong> and its principle</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Each person says one sentence in role.</div>""",
             notes="Ask one team to act out their first five minutes, with the Intake worker greeting the instructor as Rosa."),
    ],
    debrief=dict(questions=["Which old question surprised you most once you saw it through Rosa's eyes?",
                            "What changes cost nothing at all?",
                            "Where have you seen services do this well?",
                            "How are you feeling after this case? What do you need right now?"],
                 notes="End the debrief with a grounding moment: one slow breath together, or name one thing you can see, hear, and feel. Check in with anyone who seemed affected before the break."),
    apply_line="Show what you learned, then make a plan to care for yourself.",
    own_words="“When I notice I'm carrying a client's stress, I will …”",
    exit_ticket=["Name the six principles. How many can you remember without looking?",
                 "One change you'd make at an agency you have been to.",
                 "One thing on your wellness plan you'll do this week."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. Any learner can switch to the Team lead role if the case is hard for them. Have 988 and your agency's support contacts posted in the room.",
    worksheet=dict(
        title="Old intake, new intake",
        instructions="Here are eight questions from the center's old intake form. For each one, decide whether to keep, change, move later, or drop it. Write the principle it breaks and your rewrite.",
        columns=[("Old question", 30), ("Principle it breaks", 20), ("Our rewrite, or keep / move / drop", 0)],
        rows=8,
        first_col=["“Why didn't you leave sooner?”", "“Describe the abuse in detail.”",
                   "“Abuser's full name, address, and phone.” (required)", "“List every address for the last 5 years.”",
                   "“Have you ever been arrested? Explain.”", "“Rate your child's behavior problems, 1–10.”",
                   "“Do you use drugs or alcohol?”", "“Sign here.” (no explanation)"],
        plan=[("What staff say in the first five minutes:", 3),
              ("Three changes to the room or process:", 3),
              ("Our best rewrite, and the principle behind it:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "What my role knows", "The old questions my role would change"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[2.2, 1.5, 3.0]),
    assignment=dict(
        intro="Capture the trauma-informed changes your team made to Rosa's intake, then make your own plan for burnout and vicarious trauma.",
        parts=[
            dict(title="Your role's view", summary="What your role saw, the trauma response you noticed, and the change you'd make.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What did your role know about Rosa or Mateo that the rest of the team didn't?", h=0.8),
                        dict(type="q", text="What trauma response (fight, flight, freeze, or fawn) did Rosa or Mateo show? What was the clue?", h=0.8),
                        dict(type="q", text="Name one practice your role should change, and which of SAMHSA's six principles it supports.", h=0.8)]),
            dict(title="Your team's new intake", summary="Three rewritten questions, the new first five minutes, and the changes to the room.",
                 note="Use your team's worksheet from class.",
                 items=[dict(type="grid", text="Choose three old questions and show your team's rewrite.",
                             columns=["Old question", "Principle", "Rewrite"], widths=[2.1, 1.5, 3.1], rows=3, h=0.7,
                             first_col=["1.", "2.", "3."]),
                        dict(type="q", text="Write what staff will say in the first five minutes when Rosa sits down.", h=1.1,
                             hint="(Write it as a short script.)"),
                        dict(type="q", text="List three changes to the room or process, and why each one matters.", h=1.0)]),
            dict(title="My wellness plan", summary="Your warning signs and your plan for burnout and vicarious trauma, in your own words.",
                 items=[dict(type="grid", text="Fill in your wellness plan.",
                             columns=["", "My plan"], widths=[2.2, 4.5], rows=4, h=0.6,
                             first_col=["My early warning signs", "What helps me reset during the day",
                                        "Who I can talk to (at work and outside work)", "How I'll leave work at work"]),
                        dict(type="q", text="Your own experience may help you understand clients like Rosa. How will you use that understanding, and how will you protect yourself from carrying too much?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “When I notice I'm carrying a client's stress, I will …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's view (Part 1)", "Names what the role knew, a trauma response with a clear clue, and a change tied to a principle.",
             "Answers are present but the response or principle is unclear.", "Missing answers, or labels the client."],
            ["Rewritten questions (Part 2 table)", "Three rewrites that are safer, plain, and tied to the right principle.",
             "Rewrites are only slightly changed, or principles are missing.", "Few or no rewrites."],
            ["First five minutes and changes (Part 2, questions 6–7)", "A warm, transparent script that offers choice, and three realistic changes.",
             "Script or changes are general.", "Missing."],
            ["Wellness plan and reflection (Part 3)", "A specific, realistic plan. Reflection is thoughtful and in the learner's own words.",
             "Plan is general, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's view and your team's new intake.",
        reflection_title="My wellness plan",
        reflection_slide="Fill in your early warning signs, what helps you reset, who you can talk to, and how you'll leave work at work. Then write about how your own experience can help you, and how you'll protect yourself.",
    ),
))

# =====================================================================================================
# MODULE 4 · Communication & Interviewing Skills
# =====================================================================================================
MODULES[4] = finish(dict(
    num=4, hours=6,
    title="Communication &amp; Interviewing Skills",
    short_title="Communication Skills",
    slide_title_html="Communication &amp;<br>Interviewing Skills",
    subtitle="Listening so people feel heard, and asking so people want to answer.",
    title_notes="Today is the most hands-on module so far. Learners will spend most of the afternoon practicing in triads. Explain that it will feel awkward at first, and that awkward is how skills get built. Many learners have spent years on the other side of the desk being interviewed. Invite them to use that: they know what a bad interview feels like.",
    lead="The listening and interviewing skills practitioners use every day. You'll learn active listening, the basics of motivational interviewing, and de-escalation, then practice them in rotating triads with three clients who will only open up if you ask the right way.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Active listening, OARS, motivational interviewing, adapting for each person, and de-escalation",
                   practice="Triads: three clients, three rounds, every person practices"),
    objectives=[
        "Use active listening skills: open questions, reflecting, and summarizing.",
        "Apply basic motivational interviewing (MI) skills, including OARS and change talk.",
        "Adapt communication for culture, language, literacy, age, and disability.",
        "Use de-escalation techniques with a client who is upset or angry.",
    ],
    slide_objectives=[
        "Ask open questions, reflect, and summarize",
        "Use OARS and listen for change talk",
        "Adapt for language, literacy, culture, and disability",
        "Calm a conversation that is heating up",
    ],
    opening=dict(title="The best listener you know",
                 quote="Think of someone who really listens to you. When you talk with them, what do they do, with their face, their body, their words, that tells you they're listening?",
                 notes="Write the answers on the board in two columns: what they do with their body, and what they say. Body: eye contact, nodding, putting the phone down, leaning in. Words: asking more, saying back what you said, not jumping in with advice. You've just built the active listening checklist together."),
    learn_line="The skills that make people want to keep talking.",
    learn=[
        dict(eyebrow="Active listening", title="Listening is something you do",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Attend:</strong> face the person, put your phone away, use a calm and open posture</li>
        <li><strong>Follow:</strong> short encouragers like “mm-hm,” “go on,” and silence</li>
        <li><strong>Reflect:</strong> say back the meaning or the feeling</li>
        <li><strong>Summarize:</strong> pull it together and check that you got it right</li>
      </ul>
    </div>
    <div class="box c2"><h3>Silence is a skill</h3>Wait three to five seconds after a person stops talking. Many people say the most important thing after a pause.</div>
  </div>""",
             notes="Try it: ask a volunteer a simple question and count five seconds of silence out loud after they answer. Ask the class how it felt. Most people rush to fill silence. Clients notice."),
        dict(eyebrow="Questions", title="Open and closed questions",
             body="""  <table class="tbl">
    <tr><th>Closed (yes, no, or a fact)</th><th>Open (tell me more)</th></tr>
    <tr><td>“Do you have a job?”</td><td>“Tell me about your work over the last year.”</td></tr>
    <tr><td>“Are you okay with that plan?”</td><td>“What do you think about that plan?”</td></tr>
    <tr><td>“Did you go to the appointment?”</td><td>“How did the appointment go?”</td></tr>
    <tr><td>“Why didn't you call?”</td><td>“What got in the way of calling?”</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Closed questions are useful for facts, like a date of birth. Open questions are how you learn what matters.</p>""",
             notes="Point out the last row: “why” questions can sound like blame, even when you don't mean it. “What got in the way” invites the story without judgment."),
        dict(eyebrow="Motivational interviewing", title="OARS",
             body="""  <div class="cols">
    <div class="box c2"><h3>O · Open questions</h3>“What would make the biggest difference for you right now?”</div>
    <div class="box c3"><h3>A · Affirmations</h3>“You kept going to that job even when the bus was two hours each way. That takes commitment.”</div>
    <div class="box c4"><h3>R · Reflections</h3>“You're tired of starting over, and you want something that lasts.”</div>
    <div class="box c1"><h3>S · Summaries</h3>“So far you've said housing is first, then the job. Did I get that right?”</div>
  </div>""",
             notes="Motivational interviewing (MI), developed by William Miller and Stephen Rollnick, is a way of talking with people about change that respects their own reasons. Practitioners use the basic skills. Full MI takes more training. Affirmations must be specific and true, not empty praise."),
        dict(eyebrow="Motivational interviewing", title="Listen for change talk",
             body="""  <div class="cols">
    <div>
      <p>When people talk about change, they often feel two ways. MI helps them hear their own reasons.</p>
      <ul>
        <li><strong>Desire:</strong> “I want…”</li>
        <li><strong>Ability:</strong> “I could…”</li>
        <li><strong>Reasons:</strong> “It would help my kids if…”</li>
        <li><strong>Need:</strong> “I have to…”</li>
      </ul>
    </div>
    <div class="box c3"><h3>The spirit of MI</h3>Partnership, acceptance, compassion, and drawing out the person's own ideas. Not pushing, lecturing, or arguing.</div>
  </div>""",
             notes="When you hear change talk, reflect it back: “You want your kids to see you working.” Avoid the “righting reflex,” the urge to fix the problem for the client. Telling people what to do usually makes them argue for not changing."),
        dict(eyebrow="Meet people where they are", title="Adapting how you communicate",
             body="""  <table class="tbl">
    <tr><th>If the person…</th><th>Try…</th></tr>
    <tr><td><strong>Speaks another language</strong></td><td>A trained interpreter or language line, never their child. Speak to the client, not the interpreter.</td></tr>
    <tr><td><strong>Has limited reading</strong></td><td>Plain words, read forms aloud, “teach-back”: “Tell me in your words what we'll do next.”</td></tr>
    <tr><td><strong>Is hard of hearing</strong></td><td>Face them, quiet room, don't shout, write key points, ask what works best</td></tr>
    <tr><td><strong>Comes from a different culture</strong></td><td>Ask, don't assume. “What's important for me to understand about you and your family?”</td></tr>
  </table>""",
             notes="Teach-back is one of the most useful tools in the course. It checks your explanation, not the client's intelligence. Say: “I want to make sure I explained it well.” Under federal civil rights law, agencies that receive federal funds must provide language access. Using a child to interpret puts the child in an adult role."),
        dict(eyebrow="De-escalation", title="When someone is upset",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Safety first.</strong> Stay between the person and nothing; keep your own exit clear.</li>
        <li><strong>Lower your voice</strong> and slow down.</li>
        <li><strong>Name the feeling:</strong> “You're really frustrated. That makes sense.”</li>
        <li><strong>Don't argue</strong> the facts yet.</li>
        <li><strong>Offer a choice:</strong> “Do you want to sit down, or take a minute?”</li>
        <li><strong>Get help</strong> if anyone is in danger. Follow your agency's safety plan.</li>
      </ol>
    </div>
    <div class="box c1"><h3>Remember</h3>Anger is often fear or helplessness. The person is angry at the situation, even if it's aimed at you.</div>
  </div>""",
             notes="Connect to Module 3: anger can be a fight response. Practice the line “You're really frustrated, and you have every reason to be” with the whole room. Make sure learners know never to stay in an unsafe situation to finish a conversation."),
    ],
    quick_check=dict(title="Make it open",
                     items=["“Do you have kids?”",
                            "“Are you looking for work?”",
                            "“Did the shelter help you?”",
                            "“Why did you miss your appointment?”",
                            "“Is everything okay at home?”"],
                     notes="Have learners rewrite each one out loud. Sample answers: “Tell me about your family.” “What kind of work are you thinking about?” “What was the shelter like for you?” “What got in the way of the appointment?” “How are things at home?”"),
    practice_line="Practice in triads. Every person plays practitioner, client, and observer.",
    practice_notes="Split each team of six into two triads. Each triad runs three rounds, and the roles rotate every round. Teams of 4 or 5: one triad, and the extra people observe.",
    activity_title="Triads: three clients, three rounds",
    team_notes_title="Three Clients, Three Rounds",
    case=dict(
        name="the three clients",
        fiction="All three clients are fictional.",
        page_intro="Three clients (all fictional) are waiting at a neighborhood service center: <strong>Mr. Curtis Bell, 71</strong>, a veteran who is hard of hearing; <strong>Ms. Ana Morales, 44</strong>, who is more comfortable in Spanish; and <strong>Mr. Darnell Price, 35</strong>, who is angry because his benefits were cut.",
        page_how="Your team splits into triads: practitioner, client, and observer. Each client card has facts the client shares only if the practitioner listens well. You'll rotate three times, so everyone plays every part.",
        slide_title="Three clients",
        slide_intro="Three clients are waiting at a neighborhood service center today.",
        bullets=["<strong>Mr. Curtis Bell, 71:</strong> veteran, hard of hearing",
                 "<strong>Ms. Ana Morales, 44:</strong> more comfortable in Spanish",
                 "<strong>Mr. Darnell Price, 35:</strong> angry about a benefits cut",
                 "Each one has something important they won't say unless you listen well"],
        quote="“Nobody ever asks me what I think. They just hand me a paper and tell me where to sign.”",
        quote_label="What one client says",
        slide_notes="Explain that the client cards have hidden facts. If the practitioner asks a closed question, the client gives a short answer. If they ask open questions and reflect, the client shares more. Clients: play it honestly. Don't make it impossible.",
    ),
    roles_title="Cards for each triad",
    roles_small="Three client cards, a practitioner guide, an observer checklist, and a team lead card. Rotate cards each round.",
    roles_notes="Hand each triad all three client cards, the practitioner guide, and the observer checklist. Learners pass the cards each round. The Team lead keeps time for both triads.",
    roles=[
        dict(name="Client 1 · Mr. Curtis Bell, 71", where="Veteran, hard of hearing",
             facts_label="Share only if the practitioner asks an open question or reflects what you said:",
             facts=["You don't hear well if someone talks fast or looks down at a paper. Say “What?” a lot.",
                    "You came about a utility shutoff notice, but you're embarrassed to say you can't read the small print.",
                    "Your wife died last year. She handled all the bills.",
                    "You served in the Army and don't know you might qualify for VA help."],
             need="If the practitioner faces you, slows down, and checks understanding, open up.", need_label="How to play it:"),
        dict(name="Client 2 · Ms. Ana Morales, 44", where="More comfortable in Spanish",
             facts_label="Share only if the practitioner asks an open question or reflects what you said:",
             facts=["You understand some English but miss details. You nod even when you don't understand.",
                    "Your 15-year-old usually interprets for you, but you don't want her to hear about this.",
                    "You came about food, but the real worry is that your landlord said he'll raise the rent next month.",
                    "You clean offices at night and can only come in the morning."],
             need="If the practitioner offers an interpreter and uses teach-back, open up. If they ask, “Do you understand?”, just say “Yes.”",
             need_label="How to play it:"),
        dict(name="Client 3 · Mr. Darnell Price, 35", where="Angry about a benefits cut",
             facts_label="Share only if the practitioner names your feeling and stays calm:",
             facts=["Your SNAP was cut off this month. You start the conversation upset and loud.",
                    "You mailed the renewal form. You have a photo of it on your phone.",
                    "You're really scared: your two kids are coming to stay with you this weekend.",
                    "You were treated badly at another office last week."],
             need="Calm down only if the practitioner stays calm, names your feeling, and doesn't argue. If they argue or rush, get louder.",
             need_label="How to play it:"),
        dict(name="Practitioner guide", where="Whoever plays the practitioner",
             facts_label="Your goals each round (8 minutes):",
             facts=["Find out what brought the client in, and what they're really worried about.",
                    "Use OARS: open questions, affirmations, reflections, and a summary.",
                    "Adapt to the person: language, hearing, reading, or feelings.",
                    "End with teach-back: “Tell me in your words what we'll do next.”"]),
        dict(name="Observer checklist", where="Whoever is observing",
             facts_label="Make a tally mark each time you hear:",
             facts=["An open question, an affirmation, a reflection, a summary",
                    "Plain language or a check for understanding (teach-back)",
                    "A calm, de-escalating response",
                    "A closed question that shut the conversation down"],
             need="Write down the exact question that opened up the conversation the most.", need_label="Also:"),
        dict(name="Team lead", where="Timekeeper for both triads",
             facts_label="Your job:",
             facts=["Each round: 8 minutes of interview, then 5 minutes of feedback, observer first.",
                    "Call “rotate” and make sure the cards move so everyone plays every part.",
                    "Collect each observer's tallies on the team worksheet."],
             extra="<strong>Only you know:</strong> after round 3, you'll lead the team in naming the one question that worked best with each client."),
    ],
    steps=[
        dict(label="Read your cards", desc="read the client cards, the practitioner guide, and the observer checklist."),
        dict(label="Three rounds", desc="interview for 8 minutes, give feedback for 5, then rotate. Everyone plays practitioner, client, and observer."),
        dict(label="Plan and present", desc="share the questions that opened up each client and the de-escalation words that worked."),
        dict(label="Debrief", desc="step out of role and talk about what it was like to be listened to, or not."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · read your cards", title="Get ready",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Split into triads</li>
        <li>Choose who starts as practitioner, client, and observer</li>
        <li>Clients: read your card, and play it honestly</li>
        <li>Practitioner: read your guide</li>
        <li>Observer: read the checklist</li>
      </ul>
    </div>
    <div class="box c3"><h3>Round order</h3>Round 1: Mr. Bell<br>Round 2: Ms. Morales<br>Round 3: Mr. Price</div>
  </div>""",
             notes="Make sure each triad has all three client cards. Round 3 (de-escalation) works best last, after people have warmed up."),
        dict(eyebrow="Step 2 · three rounds", title="Interview, feedback, rotate",
             body="""  <table class="tbl">
    <tr><th>Each round</th><th>Time</th></tr>
    <tr><td><strong>Interview:</strong> the practitioner uses OARS and adapts to the client</td><td>8 min</td></tr>
    <tr><td><strong>Feedback:</strong> observer first, then the client, then the practitioner</td><td>5 min</td></tr>
    <tr><td><strong>Rotate:</strong> pass the cards to the right</td><td>1 min</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Feedback: one thing that worked, and one thing to try next time.</p>""",
             notes="Walk the room and listen for closed questions. Run the rounds at least twice through if time allows, so learners can try again with what they learned. Step in quickly if any role-play becomes too heated."),
        dict(eyebrow="Step 3 · plan and present", title="What opened people up?",
             body="""  <ul>
    <li>The <strong>question</strong> that opened up each client the most</li>
    <li>The <strong>words</strong> that calmed Mr. Price down</li>
    <li>One <strong>closed question</strong> to retire forever</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Each person says one sentence.</div>""",
             notes="Write the best questions from every team on the board. That list becomes the class's question bank."),
    ],
    debrief=dict(questions=["What was it like to play the client?",
                            "When did you feel listened to? When didn't you?",
                            "What was hardest to do as the practitioner?",
                            "Which skill will you practice this week, outside of class?"],
                 notes="Many learners will say playing the client was eye-opening. Connect it to lived experience: “You've been interviewed many times. Now you know what to do differently.”"),
    apply_line="Show what you learned, then reflect on how you listen.",
    own_words="“The question that opened up the conversation the most was … because …”",
    exit_ticket=["What do the letters in OARS stand for?",
                 "Rewrite this as an open question: “Do you need help with food?”",
                 "One thing you'll do differently the next time someone is upset with you."],
    packet_instructions="Print one packet per team of six (two triads), or one per triad. Cut the cards apart. Each triad needs all three client cards, the practitioner guide, and the observer checklist. Run round 3 (Mr. Price) last.",
    worksheet=dict(
        title="Listening tally",
        instructions="Observers: make a tally mark each time you hear the skill. Write the round's best question in the last row.",
        columns=[("Skill", 34), ("Round 1 · Mr. Bell", 22), ("Round 2 · Ms. Morales", 22), ("Round 3 · Mr. Price", 0)],
        rows=8,
        first_col=["Open question", "Affirmation", "Reflection", "Summary", "Teach-back or plain language",
                   "Calm, de-escalating response", "Closed question that shut it down", "Best question this round"],
        plan=[("The question that opened up each client the most:", 3),
              ("The words that calmed Mr. Price down:", 1),
              ("One closed question to retire forever, and how we'd rewrite it:", 1)],
    ),
    team_notes=dict(step1_columns=["Card", "What this card asks you to do", "What to watch for"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[2.3, 1.45, 1.5, 1.45]),
    assignment=dict(
        intro="Capture what you learned as practitioner, client, and observer, then reflect on how you listen.",
        parts=[
            dict(title="Your rounds", summary="What happened when you were the practitioner, and the feedback you received.",
                 note="Answer about the round when you played the practitioner.",
                 items=[dict(type="grid", text="Which client did you interview as the practitioner? Mark one with an X.",
                             columns=["Client", "Mark X"], widths=[5.5, 1.2], rows=3, h=0.3,
                             first_col=["Mr. Curtis Bell", "Ms. Ana Morales", "Mr. Darnell Price"]),
                        dict(type="q", text="Write two open questions you asked, and what the client shared because of them.", h=0.9),
                        dict(type="q", text="Write one reflection you made. Was it a reflection of meaning or of feeling?", h=0.7),
                        dict(type="q", text="What feedback did your observer give you? What will you try next time?", h=0.8)]),
            dict(title="Your team's question bank", summary="The questions that opened each client up, de-escalation words, and adapting for each person.",
                 note="Use your team's listening tally from class.",
                 items=[dict(type="grid", text="For each client, write what your team learned.",
                             columns=["Client", "The question that worked best", "How we adapted"], widths=[1.6, 2.6, 2.5], rows=3, h=0.7,
                             first_col=["Mr. Bell", "Ms. Morales", "Mr. Price"]),
                        dict(type="q", text="Write the words, in order, that you would use to calm Mr. Price down.", h=0.9,
                             hint="(Write it as a short script.)"),
                        dict(type="q", text="Why should Ms. Morales's daughter not interpret for her? What should the practitioner do instead?", h=0.8)]),
            dict(title="How I listen", summary="What you learned about yourself as a listener, in your own words.",
                 items=[dict(type="grid", text="Rate yourself today on each skill, then name one to grow.",
                             columns=["Skill", "Strong / Okay / Still learning", "My example from today"], widths=[1.8, 1.9, 3.0], rows=4, h=0.5,
                             first_col=["Open questions", "Reflections", "Adapting to the person", "Staying calm"]),
                        dict(type="q", text="Think about a time you were interviewed for services, and felt listened to, or didn't. How will that experience shape the way you listen to clients?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “The question that opened up the conversation the most was … because …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your rounds (Part 1)", "Specific open questions and a real reflection, with clear feedback and a next step.",
             "Examples are general, or feedback is missing.", "Missing, or examples are closed questions."],
            ["Question bank (Part 2 table)", "A strong question and a fitting adaptation for each client.",
             "Two clients complete, or adaptations are vague.", "Few answers."],
            ["De-escalation and language access (Part 2, questions)", "A calm script that names the feeling, and a correct answer on interpreters.",
             "Script or interpreter answer is partly correct.", "Missing, or the script argues with the client."],
            ["How I listen (Part 3)", "Honest self-ratings with examples. Reflection is thoughtful and in the learner's own words.",
             "Ratings without examples, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your rounds and your team's question bank.",
        reflection_title="How I listen",
        reflection_slide="Rate yourself on four skills and name one to grow. Then write about a time you were interviewed for services, and what it teaches you about how you'll listen.",
    ),
))
MODULES[4]["case"]["packet_text"] = MODULES[4]["case"]["page_intro"].replace(" (all fictional)", "") + " " + MODULES[4]["case"]["page_how"]

# =====================================================================================================
# MODULE 5 · Case Management & Service Coordination
# =====================================================================================================
TRACKER_FILE = "CP-Module-05-Follow-Up-Tracker.csv"


def build_tracker():
    rows = [
        ["Date opened", "Goal", "Action step", "Who is responsible", "Agency and contact", "Due date",
         "Status (Not started / In progress / Done / Stuck)", "Follow-up date", "Notes (facts only, no private details)"],
        ["", "Keep the family housed", "Apply for emergency rental assistance", "Monique with case manager", "", "", "Not started", "", ""],
        ["", "", "", "", "", "", "", "", ""],
    ]
    with open(f"assignments/{TRACKER_FILE}", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


MODULES[5] = finish(dict(
    num=5, hours=8,
    title="Case Management &amp; Service Coordination",
    short_title="Case Management",
    slide_title_html="Case Management &amp;<br>Service Coordination",
    subtitle="From the first meeting to the day the case closes, one plan, many partners.",
    title_notes="This is the longest module, and the heart of the practitioner role. Tell learners that today they'll put Modules 1 through 4 together: the systems map, ethics, trauma-informed practice, and interviewing. Plan a stretch break in the middle of Learn. The Practice block is long on purpose. Teams will build a full 30-day plan and a working tracker.",
    lead="The full case management cycle, from intake to closing. You'll learn strengths-based assessment and SMART goals, then work as a team to build a 30-day service plan and a follow-up tracker for a family juggling several agencies at once.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="The case management cycle, strengths-based assessment, SMART goals, and coordination",
                   practice="Team roles: the Carter family's 30-day plan and follow-up tracker"),
    objectives=[
        "Describe the stages of the case management cycle: intake, assessment, planning, linkage, monitoring, and closing.",
        "Complete a strengths-based assessment.",
        "Write a service plan with SMART goals.",
        "Coordinate services across two or more agencies and track follow-ups.",
    ],
    slide_objectives=[
        "Walk through the six stages of case management",
        "Assess strengths, not just needs",
        "Write SMART goals with the client",
        "Coordinate agencies and track every follow-up",
    ],
    opening=dict(title="Who kept track for you?",
                 quote="Think of a time you, or someone you love, had to deal with several offices at once. Who kept track of everything? What fell through the cracks?",
                 notes="Many learners will say “I did,” or “nobody.” That's the point. Case management is the job of making sure the client doesn't have to carry the whole system alone. Write down what fell through the cracks. Those are the reasons for follow-up."),
    learn_line="The cycle, the assessment, the plan, and the follow-up.",
    learn=[
        dict(eyebrow="The cycle", title="Six stages of case management",
             body="""  <div class="cols3">
    <div class="box c2"><h3>1. Intake</h3>First contact, eligibility, consent, and building trust</div>
    <div class="box c3"><h3>2. Assessment</h3>Strengths, needs, goals, and risks, from the client's view</div>
    <div class="box c4"><h3>3. Planning</h3>SMART goals and steps, written with the client</div>
    <div class="box c1"><h3>4. Linkage</h3>Referrals and warm handoffs to the right agencies</div>
    <div class="box c2"><h3>5. Monitoring</h3>Follow-up, checking progress, and adjusting the plan</div>
    <div class="box c3"><h3>6. Closing</h3>Goals met, or a planned transition, with a way back</div>
  </div>""",
             notes="Stress that the cycle repeats. Monitoring often sends you back to assessment when something changes. Closing is planned, not a case going quiet. Ask: “Have you ever had a case closed on you without warning? How did that feel?”"),
        dict(eyebrow="Assessment", title="Start with strengths",
             body="""  <div class="cols">
    <div>
      <p>A <strong>strengths-based assessment</strong> asks what is working, and builds the plan on it.</p>
      <ul>
        <li><strong>Personal:</strong> skills, experience, faith, humor, determination</li>
        <li><strong>Relationships:</strong> family, friends, neighbors, church</li>
        <li><strong>Community:</strong> programs, places, and people the client already trusts</li>
        <li><strong>Survival:</strong> what they've already handled. “How have you managed so far?”</li>
      </ul>
    </div>
    <div class="box c2"><h3>Ask</h3>“What's going well right now, even a little?”<br><br>“Who do you count on?”<br><br>“What have you gotten through before?”</div>
  </div>""",
             notes="People with lived experience are often experts at spotting survival strengths that others miss. Make the point: a needs-only assessment makes the client a list of problems. A strengths-based assessment makes them a partner."),
        dict(eyebrow="Planning", title="SMART goals",
             body="""  <table class="tbl">
    <tr><th></th><th>Means</th><th>Example</th></tr>
    <tr><td><strong>S</strong>pecific</td><td>Says exactly what will happen</td><td>Apply for emergency rental assistance</td></tr>
    <tr><td><strong>M</strong>easurable</td><td>You can tell when it's done</td><td>Application submitted, with a confirmation number</td></tr>
    <tr><td><strong>A</strong>chievable</td><td>Realistic with the client's time and resources</td><td>With help from the case manager on a weekday morning</td></tr>
    <tr><td><strong>R</strong>elevant</td><td>Matters to the client</td><td>Monique's top worry is losing the apartment</td></tr>
    <tr><td><strong>T</strong>ime-bound</td><td>Has a date</td><td>By October 30</td></tr>
  </table>""",
             notes="Write a weak goal on the board: “Monique will get stable housing.” Have the class make it SMART together. Remind them: the goals belong to the client. Use the client's words when you can."),
        dict(eyebrow="Linkage", title="Coordinating across agencies",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Get a <strong>release of information</strong> for each agency before sharing</li>
        <li>Agree on <strong>one lead</strong> so the client isn't juggling five case managers</li>
        <li>Share only what each agency <strong>needs</strong> for its part</li>
        <li>Make <strong>warm handoffs</strong>, then confirm the client got there</li>
      </ul>
    </div>
    <div class="box c3"><h3>Case conference</h3>When several agencies are involved, a short meeting, with the client present when possible, can fix conflicts like overlapping appointments.</div>
  </div>""",
             notes="Connect to Module 1 (systems map) and Module 2 (releases of information). Ask: “Which conflict from Denise's case could a case conference have solved?” (The SNAP interview at the same time as her supervision check-in.)"),
        dict(eyebrow="Monitoring", title="Follow-up is the job",
             body="""  <div class="cols">
    <div>
      <p>A referral that isn't followed up is just a phone number.</p>
      <ul>
        <li>Put every action step in a <strong>tracker</strong>: who, what, by when</li>
        <li>Check in on the date you promised</li>
        <li>Mark steps that are <strong>stuck</strong> and find out why</li>
        <li>Update the plan when life changes</li>
      </ul>
    </div>
    <div class="box c1"><h3>The tracker</h3>Today your team builds a follow-up tracker in Google Sheets from the course template. Keep notes factual and leave private details out.</div>
  </div>""",
             notes="Show the tracker template on screen (download it from the module page and open it in Google Sheets: File, Import, Upload). Point out the Status column. Explain that agencies use their own case management systems. The skill, tracking every step to done, is the same."),
        dict(eyebrow="Closing", title="Ending well",
             body="""  <table class="tbl">
    <tr><th>Close when…</th><th>How</th></tr>
    <tr><td><strong>Goals are met</strong></td><td>Review progress together. Celebrate it. Give a way to come back.</td></tr>
    <tr><td><strong>The client moves to another program</strong></td><td>Warm transfer with a release, and a final check-in</td></tr>
    <tr><td><strong>The client stops coming</strong></td><td>Follow agency outreach steps first. Send a closing letter that leaves the door open.</td></tr>
  </table>""",
             notes="Ask: “What would a good ending have looked like in your own experience?” Closing well is part of trauma-informed practice: no surprise endings."),
    ],
    quick_check=dict(title="Which stage?",
                     items=["You call the clinic to see if your client made it to her appointment.",
                            "You ask a client, “What's going well for you right now?”",
                            "You and the client write, “Submit the job training application by Friday.”",
                            "You walk the client to the benefits office and introduce her to the worker.",
                            "You review the plan together and say goodbye, leaving the door open."],
                     notes="Answers: 1) Monitoring. 2) Assessment. 3) Planning. 4) Linkage. 5) Closing. Then take a stretch break before Practice."),
    practice_line="Step into a role and build a family's 30-day plan and tracker as a team.",
    practice_notes="Hand out the in-class packet. Teams need one laptop for the tracker. Plan a short stretch break halfway through the huddle.",
    activity_title="Team roles: the Carter family's 30-day plan",
    team_notes_title="The Carter Family's 30-Day Plan",
    extra_downloads=[dict(title="Follow-Up Tracker template", file=TRACKER_FILE, button="Download the tracker",
                          meta="Spreadsheet template (.csv) · open it in Google Sheets with File, Import, Upload, then share it with your team")],
    extra_builders=[build_tracker],
    case=dict(
        name="The Carter family",
        fiction="The Carter family is fictional.",
        page_intro="<strong>Monique Carter, 58</strong> (fictional), is raising her two grandchildren, ages 7 and 11, while their mother is in treatment. Monique works part time as a home health aide, is two months behind on rent, and has diabetes. Her 11-year-old has an IEP at school.",
        page_how="Each person on your team plays a practitioner from a different agency. Your role card has facts only you know. Together, your team builds Monique's 30-day service plan with SMART goals and a follow-up tracker.",
        slide_title="Meet the Carter family",
        slide_intro="<strong>Monique Carter, 58</strong>, is raising her grandchildren, Jaylen (11) and Amari (7), while their mother is in treatment.",
        bullets=["Works part time as a home health aide",
                 "Two months behind on rent",
                 "Has diabetes and has been missing doctor visits",
                 "Jaylen has an IEP and is struggling at a new school"],
        quote="“I raised my kids. I can raise these two. I just can't do it with five offices calling me at work.”",
        quote_label="What Monique says",
        slide_notes="Point out Monique's strengths in her own words: experience raising children, determination, a job. Her request is about coordination. A plan with one lead and one tracker answers it.",
        packet_text="<strong>Monique Carter, 58</strong>, is raising her grandchildren, Jaylen (11) and Amari (7), while their mother is in a residential treatment program. Monique works part time as a home health aide, mostly weekday mornings. She is two months behind on rent, has diabetes, and has missed her last two doctor visits. Jaylen has an Individualized Education Program (IEP) and started a new school this fall. Several agencies are involved, and none of them are talking to each other. Your team meets to build one 30-day plan.",
    ),
    roles_title="Five agencies and a lead",
    roles_small="Each card has facts only you know. The plan only works if every agency is in it.",
    roles_notes="The Lead case manager is the Team lead role in this module. Give it to a learner who is organized; they will run the tracker.",
    roles=[
        dict(name="Housing stability specialist", where="Emergency rental assistance program",
             facts=["Monique owes about $2,400 in back rent. The landlord sent a notice but has not filed in court yet.",
                    "Rental assistance needs: photo ID, the lease, the landlord's notice, proof of income, and proof of the grandchildren in the home.",
                    "Funding is first come, first served this month."],
             need="Proof that the grandchildren live with Monique."),
        dict(name="Kinship care navigator", where="Kinship caregiver support program",
             facts=["Monique has no legal paperwork showing she is the children's caregiver.",
                    "She may qualify for kinship caregiver support, which can include a monthly payment. Eligibility must be checked.",
                    "The children's mother agrees with the arrangement and will sign papers at her treatment program."],
             need="A time when Monique can visit the treatment program, outside her work hours."),
        dict(name="Benefits outreach worker", where="Public benefits service center",
             facts=["Monique gets SNAP for herself only. The grandchildren were never added.",
                    "Adding them could increase her benefits and give the children Medicaid if they don't already have coverage.",
                    "The renewal interview can be done by phone."],
             need="The kinship paperwork, and the children's birth certificates or Social Security numbers."),
        dict(name="Community health worker", where="Neighborhood health center",
             facts=["Monique's blood sugar was high at her last visit, six months ago.",
                    "She missed two appointments because they were during her work hours.",
                    "The clinic has early evening hours on Wednesdays.",
                    "She told you, “If I get sick, who takes care of the kids?”"],
             need="A plan that protects Monique's own health too."),
        dict(name="School family liaison", where="Jaylen's school",
             facts=["Jaylen's IEP came from his old school. A new IEP meeting must be scheduled.",
                    "He has been late 6 times because Monique works early. The school has a before-care program.",
                    "Jaylen told the counselor he worries about his mom."],
             need="Monique's availability for the IEP meeting, and her consent to share with other agencies."),
        dict(name="Lead case manager (Team lead)", where="Runs the meeting and the tracker",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Write the SMART goals on the team worksheet.",
                    "Enter every action step in the team's Google Sheets tracker."],
             extra="<strong>Only you know:</strong> Monique asked for one person to call her, only on her lunch break (12:00 to 12:30), and only by text first."),
    ],
    steps=[
        dict(label="In role, on your own", desc="read your card and write one SMART goal your agency could work on with Monique."),
        dict(label="Team huddle", desc="assess strengths, find the conflicts between agencies, and agree on three to five SMART goals."),
        dict(label="Plan, track, and present", desc="build the 30-day plan and enter every step in the follow-up tracker, then present."),
        dict(label="Debrief", desc="step out of role and talk about what it's like to be the family in the middle."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>Read the facts only you know</li>
    <li>What strength of Monique's does your agency see?</li>
    <li>What does your agency need, and from whom?</li>
    <li>Write one SMART goal your agency could work on</li>
  </ul>""",
             notes="Check that each draft goal has a date and a way to measure it. Many first drafts will be vague."),
        dict(eyebrow="Step 2 · team huddle", title="Assess, then agree on goals",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>List Monique's strengths together</li>
        <li>Find the conflicts: who needs what from whom?</li>
        <li>Put things in order. What has to happen first?</li>
        <li>Agree on three to five SMART goals</li>
      </ol>
    </div>
    <div class="box c3"><h3>Watch for</h3>Steps that depend on each other. The kinship paperwork unlocks SNAP, Medicaid, and rental assistance.</div>
  </div>""",
             notes="This is a long huddle. Call a 5-minute stretch halfway. Make sure teams discover the chain: kinship paperwork, then proof of the children in the home, then rental assistance and benefits."),
        dict(eyebrow="Step 3 · plan, track, and present", title="Build the plan and the tracker",
             body="""  <ul>
    <li>Write the <strong>30-day plan</strong> on the worksheet: goal, steps, who, by when</li>
    <li>Open the <strong>tracker template</strong> in Google Sheets and share it with your team</li>
    <li>Enter <strong>every action step</strong>, with a due date and a follow-up date</li>
    <li>Respect Monique's request: one lead, texts at lunch</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 3 minutes: your first goal, your lead, and your tracker.</div>""",
             notes="Teams without a laptop can fill in a printed tracker. Ask each team to show their tracker on screen. Look for a follow-up date on every row."),
    ],
    debrief=dict(questions=["What would Monique's month look like without a lead case manager?",
                            "Which step unlocked the most other steps?",
                            "How did you build the plan around her strengths?",
                            "What will you check on day 7, day 14, and day 30?"],
                 notes="Return to the opening: what fell through the cracks? Ask how today's plan would have caught it."),
    apply_line="Show what you learned, then connect it to your own strengths.",
    own_words="“The client's biggest strength in this case was … and I built the plan around it by …”",
    exit_ticket=["Name the six stages of case management, in order.",
                 "Make this SMART: “Monique will take care of her health.”",
                 "One thing you'll put in every follow-up tracker you ever make."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. Each team needs one laptop to build the tracker in Google Sheets from the template on the module page.",
    worksheet=dict(
        title="30-day service plan",
        instructions="Write three to five SMART goals with Monique. For each goal, list the action steps, who is responsible, the due date, and how you'll know it's done.",
        columns=[("SMART goal", 26), ("Action steps", 26), ("Who", 14), ("By when", 12), ("How we'll know", 0)],
        rows=5,
        plan=[("Monique's strengths, and how the plan uses them:", 2),
              ("Lead case manager, and the follow-up schedule (day 7, 14, 30):", 2),
              ("What would tell us it's time to close or transition the case:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "What my agency knows and needs", "My draft SMART goal"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.6, 1.6, 1.0, 0.9, 1.6]),
    assignment=dict(
        intro="Capture the plan your team built for the Carter family, then connect case management to your own strengths.",
        parts=[
            dict(title="Your agency's part", summary="What your agency knew, your SMART goal, and how it depended on the others.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="Write your agency's SMART goal. Label each part: S, M, A, R, and T.", h=1.0),
                        dict(type="q", text="Which step in your agency depended on another agency? Explain the chain.", h=0.8),
                        dict(type="q", text="Which stage of the case management cycle was your role mostly working in? How do you know?", h=0.7)]),
            dict(title="Your team's 30-day plan", summary="Strengths, three SMART goals, and the follow-up schedule your team built.",
                 note="Use your team's worksheet and tracker from class.",
                 items=[dict(type="grid", text="List three of Monique's strengths.",
                             columns=["Strength", "How the plan uses it"], widths=[2.4, 4.3], rows=3, h=0.45,
                             first_col=["1.", "2.", "3."]),
                        dict(type="grid", text="Copy three SMART goals from your team's plan.",
                             columns=["SMART goal", "First action step", "Who", "By when"], widths=[2.4, 2.3, 1.0, 1.0], rows=3, h=0.6),
                        dict(type="q", text="Describe your follow-up plan for day 7, day 14, and day 30, and how you'll respect Monique's request about contact.", h=1.0)]),
            dict(title="Strengths in my own life", summary="How strengths-based planning connects to your own life, in your own words.",
                 items=[dict(type="q", text="Think of a hard stretch in your own life, or the life of someone close to you. What strengths got you or them through it? How would a strengths-based plan have helped?",
                             h=2.4, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “The client's biggest strength in this case was … and I built the plan around it by …”", h=0.8)]),
        ],
        rubric_full=[
            ["Agency's part (Part 1)", "A correct SMART goal with every part labeled, and a clear chain between agencies.",
             "Goal is missing a part, or the chain is unclear.", "Missing, or the goal is vague."],
            ["Strengths and SMART goals (Part 2 tables)", "Specific strengths used in the plan, and three complete SMART goals.",
             "Strengths are general, or goals are missing parts.", "Few strengths or goals."],
            ["Follow-up plan (Part 2, last question)", "A clear day 7, 14, and 30 plan that respects Monique's contact request.",
             "Plan is partly complete.", "Missing."],
            ["Reflection (Part 3)", "Specific strengths tied to life and the job. Thoughtful and in the learner's own words.",
             "Strengths are general, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your agency's part and your team's 30-day plan.",
        reflection_title="Strengths in my own life",
        reflection_slide="Think of a hard stretch in your own life, or the life of someone close to you. What strengths got you through? How would a strengths-based plan have helped?",
    ),
))

# =====================================================================================================
# MODULE 6 · Resource Navigation in DC
# =====================================================================================================
MODULES[6] = finish(dict(
    num=6, hours=6,
    title="Resource Navigation in DC",
    short_title="Resource Navigation",
    slide_title_html="Resource Navigation<br>in DC",
    subtitle="Finding the right door, checking it's still open, and walking the client through it.",
    title_notes="Before class, check that the room has working internet and that learners can make phone calls (their own phones, or a classroom phone). Today learners will verify real DC resources by website and phone. Re-check every agency name, address, and phone number on these slides before each cohort; resources change often, and that is the lesson of the day.",
    lead="How to find DC resources, check that the information is still right, and connect clients with a warm handoff instead of a phone number on a sticky note. You'll verify real resources as a team and plan a returning citizen's first two weeks.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Key DC resources, checking eligibility and accuracy, warm handoffs, and common barriers",
                   practice="Team roles: verify Kevin's resources and plan his first two weeks"),
    objectives=[
        "Locate key DC resources for housing, food, benefits, health, reentry, and employment.",
        "Check eligibility and verify that resource information is current.",
        "Make a warm handoff instead of a cold referral.",
        "Plan around common barriers: ID, transportation, documents, and wait lists.",
    ],
    slide_objectives=[
        "Find key DC resources in six areas",
        "Check eligibility and verify what's current",
        "Make a warm handoff",
        "Plan around ID, transportation, documents, and wait lists",
    ],
    opening=dict(title="The wrong door",
                 quote="Have you ever been sent somewhere for help, and when you got there, it had moved, closed, changed its hours, or wasn't the right place? What did that cost you?",
                 notes="Almost everyone has a story. Write down the costs people name: bus fare, a missed shift, a day lost, giving up. That is why we verify. A wrong referral costs the client, not the practitioner."),
    learn_line="Where to look, how to check, and how to hand off.",
    learn=[
        dict(eyebrow="Start here", title="Ways to find resources in DC",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>211 (DC):</strong> a phone and online directory of community resources</li>
        <li><strong>Official agency websites:</strong> dc.gov agency pages for current hours, locations, and eligibility</li>
        <li><strong>Your agency's resource guide:</strong> useful, but check the date it was last updated</li>
        <li><strong>Other practitioners:</strong> the people who know which programs actually answer the phone</li>
      </ul>
    </div>
    <div class="box c2"><h3>Rule of thumb</h3>If you haven't checked it in the last 90 days, treat it as unverified.</div>
  </div>""",
             notes="Confirm before class how DC 211 currently operates and how to reach it. Show the class one official dc.gov agency page on screen. Point out where it lists hours and what to bring."),
        dict(eyebrow="Key DC agencies · confirm before class", title="Six areas, where to start",
             body="""  <table class="tbl">
    <tr><th>Area</th><th>Start with</th></tr>
    <tr><td><strong>Shelter and housing</strong></td><td>DC Department of Human Services (DHS): shelter hotline and homeless services</td></tr>
    <tr><td><strong>Food and benefits</strong></td><td>DHS Economic Security Administration (ESA) service centers: SNAP, TANF, Medicaid</td></tr>
    <tr><td><strong>Health</strong></td><td>Community health centers; DC Department of Behavioral Health access line</td></tr>
    <tr><td><strong>Reentry</strong></td><td>Mayor's Office on Returning Citizen Affairs (MORCA)</td></tr>
    <tr><td><strong>ID and documents</strong></td><td>DC DMV (ID cards); DC Health Vital Records (birth certificates)</td></tr>
    <tr><td><strong>Employment</strong></td><td>Department of Employment Services (DOES) and American Job Centers</td></tr>
  </table>""",
             notes="Before each cohort, look up and write the current phone number and main location for each agency on the board. Don't trust last cohort's notes. That's today's lesson."),
        dict(eyebrow="Verify", title="Five things to check before you refer",
             body="""  <ol>
    <li><strong>Is it open?</strong> Current address, hours, and whether it's walk-in or by appointment</li>
    <li><strong>Who qualifies?</strong> Age, income, residency, family size, and other rules</li>
    <li><strong>What to bring?</strong> ID, proof of address, income, Social Security card, and so on</li>
    <li><strong>Is there a wait?</strong> Wait lists, first-come funding, or intake days</li>
    <li><strong>Who to ask for?</strong> A name or a direct line, so you can make a warm handoff</li>
  </ol>
  <p class="small">Write down the date you checked and where you found it.</p>""",
             notes="These five checks are the columns of the team's verification log. Practice with one resource as a class: look it up live and fill in all five."),
        dict(eyebrow="Handoffs", title="Cold referral or warm handoff?",
             body="""  <div class="cols">
    <div class="box c1"><h3>Cold referral</h3>“Here's a number. Give them a call.”<br><br>The client has to explain everything again, may not get through, and may give up.</div>
    <div class="box c3"><h3>Warm handoff</h3>“I'm calling my contact at the job center right now, with you here, so you don't have to start over.”<br><br>With consent, you introduce the client, share what's needed, and confirm the next step.</div>
  </div>""",
             notes="Model a warm handoff call out loud, with the instructor as the practitioner and a volunteer as the receiving agency. Script: who you are, who the client is (with consent), what they need, what you've already done, what you're asking for, and the next step. Always confirm the client has a release on file."),
        dict(eyebrow="Barriers", title="What stops people from getting there",
             body="""  <table class="tbl">
    <tr><th>Barrier</th><th>Ways around it</th></tr>
    <tr><td><strong>No ID</strong></td><td>Start ID and birth certificate requests first. Ask which programs can begin without ID. Look for fee help.</td></tr>
    <tr><td><strong>Transportation</strong></td><td>Plan the route with the client. Ask about transit help. Group appointments in one area.</td></tr>
    <tr><td><strong>Missing documents</strong></td><td>A checklist for each program. Copies kept safely, with consent.</td></tr>
    <tr><td><strong>Wait lists</strong></td><td>Get on the list now. Find a bridge resource while waiting.</td></tr>
    <tr><td><strong>No phone</strong></td><td>Ask about free phone programs. Agree on another way to reach them.</td></tr>
  </table>""",
             notes="ID is the master key for most programs. In the Practice case, the team will see how many doors depend on Kevin's ID. Ask learners which barrier they have personally run into most."),
        dict(eyebrow="Keep it current", title="Building a shared resource guide",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>One row per resource, with the <strong>date verified</strong></li>
        <li>Note <strong>who</strong> checked it and <strong>how</strong> (website or phone)</li>
        <li>Mark anything older than 90 days for re-checking</li>
        <li>Add tips: “Ask for intake, not the front desk.” “Arrive before 9.”</li>
      </ul>
    </div>
    <div class="box c2"><h3>Today</h3>Your team will verify six resources and add them to the class guide. Every cohort after you will use it, and re-check it.</div>
  </div>""",
             notes="Set up a shared class guide (for example, a Google Sheet) before class and share it with the cohort. Teams add their verified rows during Practice."),
    ],
    quick_check=dict(title="What would you check?",
                     items=["A flyer from two years ago says a food pantry is open Saturdays.",
                            "A client says, “My friend said the job center does walk-ins.”",
                            "Your agency's guide lists a phone number with no name.",
                            "A program's website says “funding available” with no date."],
                     notes="For each one, have learners name which of the five checks they'd do first. There's no single right answer. The habit of checking is the point."),
    practice_line="Step into a role, verify real DC resources, and plan a client's first two weeks.",
    practice_notes="Hand out the in-class packet. Each role verifies the resource on its card by website and, if possible, by phone. Give teams 20 minutes for checking before the huddle.",
    activity_title="Team roles: Kevin's first two weeks",
    team_notes_title="Kevin's First Two Weeks",
    case=dict(
        name="Kevin",
        page_intro="<strong>Kevin Brooks, 26</strong> (fictional), came home from prison two weeks ago. He is sleeping on a friend's couch, has no ID, no income, and an old phone that only works on Wi-Fi. He wants to work and wants to see his daughter.",
        page_how="Each person on your team plays a navigator holding a listing from an old resource guide. Your job is to check whether it is still right, using the official website and a phone call if you can. Then your team plans Kevin's first two weeks, in the right order, with a warm handoff.",
        slide_title="Meet Kevin",
        slide_intro="<strong>Kevin Brooks, 26</strong>, came home from prison two weeks ago.",
        bullets=["Sleeping on a friend's couch, which can't last",
                 "No ID, no income, phone works only on Wi-Fi",
                 "Wants to work and to see his 4-year-old daughter",
                 "Your team has an old resource guide. Is it still right?"],
        quote="“I've got a list of 20 places people told me to go. I don't have bus fare for 20 places. Tell me which three.”",
        quote_label="What Kevin says",
        slide_notes="Kevin's request is the task: put the resources in order, and only send him where it will work. Remind teams that the listings on their cards come from an old, made-up guide. The point is to find the current, official information.",
        packet_text="<strong>Kevin Brooks, 26</strong>, came home from prison two weeks ago. He is sleeping on a friend's couch, but his friend's lease doesn't allow it, so he has about two weeks. His state ID expired while he was inside, and he doesn't have his birth certificate. He has no income, and his phone only works on Wi-Fi. He wants to work, and he wants to see his 4-year-old daughter. Your agency's resource guide is old. Your team's job is to check each listing, fix what's wrong, and plan Kevin's first two weeks.",
    ),
    roles_title="Six navigators, six listings",
    roles_small="Each card has an old listing. Check it against the official website, and by phone if you can.",
    roles_notes="The listings on the cards are made up and purposely out of date. Learners must find the real, current information. Have the Team lead start the class guide while others verify.",
    roles=[
        dict(name="Housing navigator", where="Shelter and housing",
             facts_label="The old guide says:",
             facts=["“Shelter: call the main DHS number and ask for the shelter list.”",
                    "“Walk in to any shelter after 7 p.m.”"],
             need="Find the current way to request shelter in DC, the hours, and whether there's a hotline. Note what Kevin should do if his couch falls through.",
             need_label="Verify:"),
        dict(name="Benefits navigator", where="Food and benefits",
             facts_label="The old guide says:",
             facts=["“SNAP: apply in person only, at the service center on your side of town.”",
                    "“Bring photo ID or you can't apply.”"],
             need="Find the current ways to apply for SNAP and Medicaid in DC (online, phone, in person), and what to do if Kevin doesn't have ID yet.",
             need_label="Verify:"),
        dict(name="Reentry navigator", where="Returning citizen services",
             facts_label="The old guide says:",
             facts=["“Returning citizens office: open Tuesdays and Thursdays only.”",
                    "“Ask for the ID voucher at the front desk.”"],
             need="Find MORCA's current location, hours, and services, and whether it helps with ID or birth certificate fees.",
             need_label="Verify:"),
        dict(name="ID and documents navigator", where="ID and vital records",
             facts_label="The old guide says:",
             facts=["“DC ID: bring any one document.”",
                    "“Birth certificates: same-day at the vital records office, cash only.”"],
             need="Find the documents DC DMV requires for an ID card, and how to request a birth certificate, the cost, and how long it takes. Note: Kevin was born in DC.",
             need_label="Verify:"),
        dict(name="Employment navigator", where="Jobs and training",
             facts_label="The old guide says:",
             facts=["“Job center: walk in any time, ask for a counselor.”",
                    "“Ask about the transitional jobs program for people with records.”"],
             need="Find the nearest American Job Center, its hours, and DOES programs for returning citizens, including what Kevin needs to enroll.",
             need_label="Verify:"),
        dict(name="Team lead", where="Plans the order and the handoff",
             facts_label="Your job:",
             facts=["Keep time and make sure every role reports back.",
                    "Start the team's verification log while others check.",
                    "Lead the team in choosing Kevin's first three stops, in order."],
             extra="<strong>Only you know:</strong> Kevin's supervision officer requires him to look for work, and Kevin can get to most places only by walking or by bus fare from his friend."),
    ],
    steps=[
        dict(label="Verify, in role", desc="check your card's old listing against the official website, and by phone if you can. Note what changed."),
        dict(label="Team huddle", desc="report back, fill in the verification log, and add your rows to the class resource guide."),
        dict(label="Plan and present", desc="choose Kevin's first three stops in order, plan around his barriers, and role-play one warm handoff call."),
        dict(label="Debrief", desc="step out of role and talk about what you found and what it would have cost Kevin."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · verify, in role", title="Check your listing",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Read the old listing on your card</li>
        <li>Find the official website. Is the listing still right?</li>
        <li>If you can, call. Ask the five questions.</li>
        <li>Write down what changed, the date, and your source</li>
      </ol>
    </div>
    <div class="box c3"><h3>On the phone</h3>“Hi, I'm a student in a human services training program. I'm updating our resource guide. Can I ask a few questions about your services?”</div>
  </div>""",
             notes="Walk the room. If calls go to voicemail, that's real-world data too: note it. Remind learners not to give any real client information on calls. They're verifying general information only."),
        dict(eyebrow="Step 2 · team huddle", title="Report back and log it",
             body="""  <ul>
    <li>Each role reports: what was wrong, and what's right now</li>
    <li>Fill in the verification log together</li>
    <li>Add your rows to the class resource guide</li>
    <li>Notice: how many doors depend on Kevin's ID?</li>
  </ul>""",
             notes="Ask each team which listing was most out of date. Most will find at least one. Make sure the ID chain comes up."),
        dict(eyebrow="Step 3 · plan and present", title="Kevin's first three stops",
             body="""  <ul>
    <li>Kevin's <strong>first three stops</strong>, in order, and why</li>
    <li>One <strong>barrier</strong> and how you'll get around it</li>
    <li>Act out <strong>one warm handoff call</strong>: two people, 1 minute</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 3 minutes, including the call.</div>""",
             notes="Ask teams whether they can group stops in one part of town or handle some online or by phone. Kevin asked for three, not twenty."),
    ],
    debrief=dict(questions=["What was out of date? What would it have cost Kevin?",
                            "Which resource was easiest to verify? Hardest?",
                            "What did it feel like to make the call?",
                            "Have you ever been given a list like Kevin's? What would have helped?"],
                 notes="Celebrate the class resource guide. Tell learners it's now theirs to keep up to date."),
    apply_line="Show what you learned, then connect it to your own experience.",
    own_words="“A resource that was out of date was … I found the right information by …”",
    exit_ticket=["Name the five things you check before you refer.",
                 "What's the difference between a cold referral and a warm handoff?",
                 "One DC resource you didn't know about before today."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. The listings on the cards are made up and out of date on purpose. Learners verify them against official websites, and by phone if possible. Make sure the room has internet, and set up a shared class resource guide before class.",
    worksheet=dict(
        title="Verification log",
        instructions="For each listing, write what the old guide said, what you found, the date and source, and what Kevin needs to bring.",
        columns=[("Resource", 18), ("Old guide said", 20), ("What we found (date, source)", 26), ("Who qualifies, what to bring", 0)],
        rows=6,
        first_col=["Shelter", "SNAP and Medicaid", "MORCA", "DC ID and birth certificate", "American Job Center", "Other"],
        plan=[("Kevin's first three stops, in order, and why:", 3),
              ("One barrier, and how we'll get around it:", 1),
              ("Our warm handoff call (who calls whom, and what they say):", 2)],
    ),
    team_notes=dict(step1_columns=["Role", "What the old guide said", "What we found, with date and source"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.3, 1.4, 2.0, 2.0]),
    assignment=dict(
        intro="Capture what your team verified for Kevin and the plan you built, then connect it to your own experience finding help.",
        parts=[
            dict(title="Your listing", summary="What your listing said, what you found, and how you checked.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What did your old listing say, and what did you find? Include the date and your source.", h=1.0),
                        dict(type="q", text="Who qualifies for this resource, and what does Kevin need to bring?", h=0.8),
                        dict(type="q", text="What would have happened if Kevin had followed the old listing?", h=0.7)]),
            dict(title="Kevin's plan", summary="His first three stops, the barriers, and your warm handoff script.",
                 note="Use your team's verification log from class.",
                 items=[dict(type="grid", text="Write Kevin's first three stops, in order.",
                             columns=["Stop", "Why it comes here", "What Kevin brings"], widths=[1.9, 2.6, 2.2], rows=3, h=0.6,
                             first_col=["1.", "2.", "3."]),
                        dict(type="q", text="Name two barriers Kevin faces and how your team planned around them.", h=0.9),
                        dict(type="q", text="Write your warm handoff call as a script. Who is calling whom, and what do they say?", h=1.1,
                             hint="(Include consent, what Kevin needs, and the next step.)")]),
            dict(title="Finding help, in my own life", summary="Your own experience looking for help, in your own words.",
                 items=[dict(type="q", text="Think of a time you, or someone close to you, had to find help, and the information was wrong, missing, or confusing. What happened? What will you do as a practitioner so your clients don't go through that?",
                             h=2.4, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “A resource that was out of date was … I found the right information by …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your listing (Part 1)", "Clear old vs. current information with a date and official source, plus eligibility and documents.",
             "Information is partly verified, or the source is missing.", "Missing, or not verified."],
            ["First three stops (Part 2 table)", "A logical order that puts ID and urgent needs first, with what to bring.",
             "Order is partly explained.", "Missing, or the order doesn't work."],
            ["Barriers and handoff (Part 2, questions)", "Realistic barrier plans and a specific, consent-based warm handoff.",
             "Barrier plans or the handoff are general.", "Missing, or a cold referral."],
            ["Reflection (Part 3)", "Specific experience tied to how they'll practice. In the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your listing and Kevin's plan.",
        reflection_title="Finding help, in my own life",
        reflection_slide="Write about a time you, or someone close to you, had to find help and the information was wrong, missing, or confusing. What will you do so your clients don't go through that?",
    ),
))

# =====================================================================================================
# MODULE 7 · Documentation & Professional Writing
# =====================================================================================================
MODULES[7] = finish(dict(
    num=7, hours=5,
    title="Documentation &amp; Professional Writing",
    short_title="Documentation",
    slide_title_html="Documentation &amp;<br>Professional Writing",
    subtitle="If it isn't written down, it didn't happen. If it's written badly, it can hurt.",
    title_notes="Many learners have read their own case files, or wished they could. Open by acknowledging that what practitioners write follows clients for years: into court, housing applications, and the next agency. Today is about writing notes that are accurate, respectful, private, and useful.",
    lead="How to write case notes and professional messages that are accurate, respectful, and private. You'll learn the DAP format, objective and strengths-based language, and the basic privacy rules, then fix a set of weak notes as a team.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Why documentation matters, DAP notes, objective language, privacy, and professional email",
                   practice="Team roles: fix the notes from Ms. Hayes's home visit"),
    objectives=[
        "Write case notes in the DAP (Data, Assessment, Plan) format.",
        "Use objective, strengths-based language instead of judgments or labels.",
        "Store and share records according to privacy rules, including HIPAA and 42 CFR Part 2.",
        "Proofread for a professional tone in notes and emails.",
    ],
    slide_objectives=[
        "Write a DAP note",
        "Use facts and strengths, not labels",
        "Keep records private and share only what's needed",
        "Write a professional referral email",
    ],
    opening=dict(title="What would your file say?",
                 quote="Imagine a caseworker wrote a note about you on your hardest day. What would you want it to say? What would you never want it to say?",
                 notes="Let learners think quietly, then share only if they want to. Write the “want it to say” list on the board: what I was dealing with, that I showed up, what I'm good at, the plan. The “never” list will be full of labels: difficult, non-compliant, manipulative. That's today's lesson."),
    learn_line="Notes that are accurate, respectful, private, and useful.",
    learn=[
        dict(eyebrow="Why it matters", title="Who reads your notes?",
             body="""  <div class="cols3">
    <div class="box c2"><h3>Your team</h3>The next worker needs to know what happened and what's next</div>
    <div class="box c3"><h3>Funders and auditors</h3>Proof that services happened</div>
    <div class="box c4"><h3>Courts and lawyers</h3>Records can be requested by a court order</div>
    <div class="box c1"><h3>Other agencies</h3>With a signed release</div>
    <div class="box c2"><h3>The client</h3>Clients often have the right to see their records</div>
    <div class="box c3"><h3>You, later</h3>Memory fades. Notes don't.</div>
  </div>""",
             notes="The test: write every note as if the client will read it, because they might. Write it the same day, while it's fresh."),
        dict(eyebrow="The format", title="DAP notes",
             body="""  <table class="tbl">
    <tr><th></th><th>What goes here</th><th>Example</th></tr>
    <tr><td><strong>D</strong>ata</td><td>Facts: what you saw, heard, and did. Quotes in quotation marks.</td><td>Met with client at her home, 45 min. Client said, “I'm worried about the rent.” Showed a landlord notice dated 10/1.</td></tr>
    <tr><td><strong>A</strong>ssessment</td><td>Your professional view, based on the data</td><td>Client is at risk of eviction. She is organized and kept all her paperwork.</td></tr>
    <tr><td><strong>P</strong>lan</td><td>Next steps: who, what, by when</td><td>Worker will submit rental assistance referral by 10/8. Client will bring lease to the office 10/9 at 10 a.m.</td></tr>
  </table>""",
             notes="Other formats exist (SOAP, BIRP, narrative). Agencies choose their own. DAP is common and easy to learn. Point out that the Assessment is still based on the facts, never on feelings about the client."),
        dict(eyebrow="Language", title="Facts, not labels",
             body="""  <table class="tbl">
    <tr><th>Instead of…</th><th>Write…</th></tr>
    <tr><td>“Client was hostile.”</td><td>“Client raised his voice and said, ‘You people never help.’”</td></tr>
    <tr><td>“Non-compliant with plan.”</td><td>“Client did not attend the 10/2 or 10/9 appointments. Said bus fare was the barrier.”</td></tr>
    <tr><td>“House was a mess.”</td><td>“Dishes and clothing on the floor of the kitchen and living room.”</td></tr>
    <tr><td>“Ex-con” / “addict”</td><td>“Returning citizen” / “person in recovery” (only if relevant and allowed)</td></tr>
    <tr><td>“Seems depressed.”</td><td>“Client said she has ‘no energy’ and is sleeping 12 hours a day.” (Refer; don't diagnose.)</td></tr>
  </table>""",
             notes="This connects to Module 1 (know your lane: don't diagnose) and Module 3 (trauma-informed language). Ask: “Which of these labels has been used about you or someone you know?”"),
        dict(eyebrow="Privacy", title="Minimum necessary",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Write only what's needed</strong> for the service. Leave out gossip and private details that don't matter.</li>
        <li><strong>HIPAA</strong> protects health information held by health plans, health care providers, and their partners.</li>
        <li><strong>42 CFR Part 2</strong> gives extra protection to substance use disorder treatment records.</li>
        <li><strong>Share only with a release</strong>, only what the release covers.</li>
      </ul>
    </div>
    <div class="box c1"><h3>Store it safely</h3>Lock paper files. Never leave screens open. Don't text or email client details from personal accounts. Follow agency policy.</div>
  </div>""",
             notes="Keep this practical. Learners don't need to be lawyers. They need habits: minimum necessary, a release before sharing, and secure storage. Your agency's privacy officer is the expert. Tell learners to ask which rules apply at their job."),
        dict(eyebrow="Professional writing", title="A referral email",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Subject:</strong> clear, with no client name. “Referral: job training, consent on file”</li>
        <li><strong>Who you are</strong> and your agency</li>
        <li><strong>What the client needs</strong>, minimum necessary</li>
        <li><strong>What you've done</strong> already</li>
        <li><strong>What you're asking</strong>, and by when</li>
        <li><strong>How to reach you</strong></li>
      </ol>
    </div>
    <div class="box c3"><h3>Before you send</h3>Is it the right person? Is there a release? Did you use a secure method? Did you read it out loud once?</div>
  </div>""",
             notes="Many agencies send client details only through secure systems, not regular email. Teach the structure, and tell learners to follow their agency's rules for how to send."),
        dict(eyebrow="Proofread", title="Four checks before you sign",
             body="""  <ol>
    <li><strong>Accurate:</strong> dates, times, names, and quotes are right</li>
    <li><strong>Objective:</strong> no labels or opinions written as facts</li>
    <li><strong>Complete:</strong> D, A, and P are all there, and the note is signed and dated</li>
    <li><strong>Professional:</strong> no slang, texting shortcuts, or unclear abbreviations</li>
  </ol>
  <div class="warn" style="margin-top:18px">Never change or delete a signed note. Add a dated correction, following agency policy.</div>""",
             notes="Read one weak note out loud and run the four checks with the class. Then move to Practice."),
    ],
    quick_check=dict(title="Fact or label?",
                     items=["“Client was very rude.”",
                            "“Client arrived 25 minutes late and said the bus didn't come.”",
                            "“Client is lazy about job searching.”",
                            "“Client said, ‘I applied to three jobs this week.’”",
                            "“Client is probably using again.”"],
                     notes="Labels: 1, 3, 5. Facts: 2, 4. Have learners rewrite 1, 3, and 5 out loud. For 5, there are no facts in the note at all. What would you need to observe or hear, and is it your role to write it?"),
    practice_line="Step into a role and fix the notes from one home visit as a team.",
    practice_notes="Hand out the in-class packet. Each role card has that worker's weak note and what really happened.",
    activity_title="Team roles: fix the notes from Ms. Hayes's visit",
    team_notes_title="Fixing the Notes from Ms. Hayes's Visit",
    case=dict(
        name="Ms. Hayes",
        page_intro="<strong>Ms. Lorraine Hayes, 59</strong> (fictional), had a home visit from a team of workers after she fell behind on her utility bill and stopped picking up her medications. Every worker wrote a note about the same visit, and none of the notes are good enough.",
        page_how="Each person on your team plays one of the workers. Your card has your weak note and what really happened. Together, your team finds the problems, rewrites one strong DAP note for the visit, and writes a referral email.",
        slide_title="Meet Ms. Hayes",
        slide_intro="<strong>Ms. Lorraine Hayes, 59</strong>, had a home visit after she fell behind on her utility bill and stopped picking up her medications.",
        bullets=["Five workers were at the visit or followed up",
                 "Each one wrote a note",
                 "Every note has problems",
                 "Your team writes the one note that gets it right"],
        quote="“I read what they wrote about me last time. ‘Uncooperative.’ I was scared. Nobody wrote that down.”",
        quote_label="What Ms. Hayes says",
        slide_notes="Ms. Hayes's quote is the heart of today. Notes follow people. Ask: what would a fair note about that visit have said?",
        packet_text="<strong>Ms. Lorraine Hayes, 59</strong>, lives alone and works part time at a school cafeteria. She fell behind on her electric bill and received a shutoff notice. Her pharmacy reported that she hasn't picked up her blood pressure medication in six weeks. A team of workers visited her home on October 6 and followed up the next day. Every worker wrote a note, and every note has problems. Your team's job is to fix them.",
    ),
    roles_title="Five weak notes and a lead",
    roles_small="Each card has your weak note and what really happened.",
    roles_notes="Learners may enjoy finding the problems. Keep the focus on fixing: every problem should end with a rewrite.",
    roles=[
        dict(name="Outreach worker", where="Led the home visit",
             facts_label="Your note says:",
             facts=["“Client was uncooperative and wouldn't let us in at first. Home was filthy. She seems out of it.”"],
             need="She opened the door after about 2 minutes and said, “I wasn't expecting anyone.” There were dishes in the sink and mail piled on the table. She answered every question and said she'd been “feeling dizzy.”",
             need_label="What really happened:"),
        dict(name="Utility assistance specialist", where="Energy bill help",
             facts_label="Your note says:",
             facts=["“Talked to client re: $$. Needs LIHEAP ASAP. Will f/u.”"],
             need="She owes $612. The shutoff date is October 20. You gave her the energy assistance application. She needs her ID and her last two pay stubs. You'll call her on October 9 at 3 p.m., after her shift.",
             need_label="What really happened:"),
        dict(name="Community health worker", where="Medication follow-up",
             facts_label="Your note says:",
             facts=["“Client is noncompliant with meds and probably has dementia. Her daughter is useless and lives in MD and never visits. Client also told me she was in rehab in 2009.”"],
             need="She said the medicine cost went up to $47 and she “had to choose between the light bill and the pills.” Her daughter lives in Maryland and calls weekly. The 2009 treatment has nothing to do with this visit.",
             need_label="What really happened:"),
        dict(name="Benefits outreach worker", where="Benefits check",
             facts_label="Your note says:",
             facts=["“Client might qualify for some stuff. Didn't have papers. Told her to come in.”"],
             need="She may qualify for help paying Medicare costs through DC Medicaid programs. She has her Medicare card but needs her bank statements. She agreed to an appointment on October 14 at 10 a.m.",
             need_label="What really happened:"),
        dict(name="Peer support specialist", where="Followed up the next day",
             facts_label="Your note says:",
             facts=["“Went back 10/7. Me and Ms. H just talked for a while about life. She's sweet. Same thing happened to me with my light bill lol.”"],
             need="You visited 30 minutes on October 7. She said she felt “less alone.” She asked about a senior wellness center near her. You agreed to bring information on October 10.",
             need_label="What really happened:"),
        dict(name="Team lead", where="Signs off on the final note",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Lead the team through the four proofreading checks for each note.",
                    "Write the team's final DAP note on the worksheet."],
             extra="<strong>Only you know:</strong> Ms. Hayes signed a release for the utility program and the health center only. She asked that her daughter not be contacted."),
    ],
    steps=[
        dict(label="In role, on your own", desc="read your weak note and what really happened. List every problem you can find."),
        dict(label="Team huddle", desc="run the four proofreading checks on each note, then sort the facts into Data, Assessment, and Plan."),
        dict(label="Plan and present", desc="write one strong DAP note for the visit and a referral email, then present."),
        dict(label="Debrief", desc="step out of role and talk about what it's like to read a note about yourself."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Find the problems",
             body="""  <ul>
    <li>Read your weak note</li>
    <li>Read what really happened</li>
    <li>List every problem: labels, opinions, missing facts, private details, slang, missing plan</li>
    <li>Rewrite your note on your own first</li>
  </ul>""",
             notes="Most learners find the obvious labels quickly. Push them to find the missing information too: dates, amounts, next steps."),
        dict(eyebrow="Step 2 · team huddle", title="Check and sort",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role reads its weak note out loud</li>
        <li>Run the four checks: accurate, objective, complete, professional</li>
        <li>Sort every fact into D, A, or P</li>
        <li>Decide what to leave out</li>
      </ol>
    </div>
    <div class="box c3"><h3>Ask</h3>Is this needed for the service? Does the release cover it? Would I be okay with Ms. Hayes reading it?</div>
  </div>""",
             notes="Check that teams leave out the 2009 treatment history (not relevant, and protected) and don't contact the daughter."),
        dict(eyebrow="Step 3 · plan and present", title="One strong note and an email",
             body="""  <ul>
    <li>Write <strong>one DAP note</strong> for the October 6 visit</li>
    <li>Write a <strong>referral email</strong> to the utility program: subject line and body</li>
    <li>Name <strong>what you left out</strong>, and why</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Read your Assessment out loud.</div>""",
             notes="Have teams read their Assessment line. Ask the class: would Ms. Hayes feel this is fair?"),
    ],
    debrief=dict(questions=["Which weak note would hurt Ms. Hayes most if she read it?",
                            "What did you leave out, and why?",
                            "How did the facts change the story?",
                            "How will you write about clients from your own community?"],
                 notes="Return to the opening lists. Ask: did your team's note say what you'd want your own file to say?"),
    apply_line="Show what you learned, then reflect on how records follow people.",
    own_words="“The note I fixed had a problem with … and I changed it to …”",
    exit_ticket=["What do D, A, and P stand for?",
                 "Rewrite as a fact: “Client was agitated.”",
                 "One privacy habit you'll start now."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. The Team lead writes the final DAP note.",
    worksheet=dict(
        title="Note fixes",
        instructions="For each weak note, list the problems and the fix. Then write your team's DAP note below.",
        columns=[("Note from", 22), ("The problems", 34), ("Our fix", 0)],
        rows=5,
        first_col=["Outreach worker", "Utility assistance specialist", "Community health worker", "Benefits outreach worker",
                   "Peer support specialist"],
        plan=[("D (Data):", 3), ("A (Assessment):", 2), ("P (Plan):", 2),
              ("Referral email subject line and first two sentences:", 2)],
    ),
    team_notes=dict(step1_columns=["Role", "Problems in my note", "My first rewrite"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.6, 2.4, 2.7]),
    assignment=dict(
        intro="Capture what your team fixed in Ms. Hayes's notes, write your own DAP note, then reflect on how records follow people.",
        parts=[
            dict(title="Your note", summary="The problems in your role's note and your rewrite.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="List three problems in your role's weak note. Name the proofreading check each one fails.", h=0.9,
                             hint="(Accurate, objective, complete, or professional.)"),
                        dict(type="q", text="Rewrite your role's note so it passes all four checks.", h=1.2),
                        dict(type="q", text="What did you leave out, and why?", h=0.7)]),
            dict(title="The team's DAP note and email", summary="One complete DAP note for the visit and a professional referral email.",
                 note="Use your team's worksheet from class. You may improve on it.",
                 items=[dict(type="grid", text="Write the DAP note for the October 6 visit.",
                             columns=["", "Note"], widths=[1.3, 5.4], rows=3, h=0.9,
                             first_col=["Data", "Assessment", "Plan"]),
                        dict(type="q", text="Write a referral email to the utility assistance program. Include a subject line.", h=1.4,
                             hint="(Minimum necessary. No client name in the subject line.)"),
                        dict(type="q", text="Ms. Hayes asked that her daughter not be contacted, and her release covers only two agencies. How does that change what you write and share?", h=0.8)]),
            dict(title="Records follow people", summary="How notes have affected you or people you know, in your own words.",
                 items=[dict(type="q", text="Records follow people into court, housing, jobs, and the next agency. Has a record, a label, or a report ever affected you or someone close to you? How will that shape the way you write about clients?",
                             h=2.4, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “The note I fixed had a problem with … and I changed it to …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your note (Part 1)", "Three real problems matched to the right check, and a rewrite that passes all four.",
             "Some problems found, or the rewrite still has a label.", "Missing, or the rewrite repeats the problems."],
            ["DAP note (Part 2 table)", "Facts in Data, a fair Assessment based on them, and a Plan with who, what, and when.",
             "Sections are mixed up or missing details.", "Missing, or uses labels."],
            ["Email and privacy (Part 2, questions)", "A clear, professional email with minimum necessary detail, and correct privacy reasoning.",
             "Email is unclear, or privacy reasoning is partly right.", "Missing, or shares information without consent."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your note, the team's DAP note, and the email.",
        reflection_title="Records follow people",
        reflection_slide="Has a record, a label, or a report ever affected you or someone close to you? How will that shape the way you write about clients?",
    ),
))

# =====================================================================================================
# MODULE 8 · HS-BCP Exam Readiness
# =====================================================================================================
MODULES[8] = finish(dict(
    num=8, hours=5,
    title="HS-BCP Exam Readiness",
    short_title="Exam Readiness",
    slide_title_html="HS-BCP<br>Exam Readiness",
    subtitle="You've done the work. Now let's get you ready to prove it.",
    title_notes="Before class, download the current HS-BCP candidate information from the Center for Credentialing &amp; Education (CCE), the organization that issues the credential. Check the exam format, content areas, eligibility routes, and fees, and update the Learn slides if anything has changed. Don't guess at exam details. Point learners to CCE's official information. Many learners carry test anxiety. Name it, normalize it, and remind them this course has already prepared them.",
    lead="What the HS-BCP exam asks of you, where you're strong, and where to study. You'll learn test strategies for scenario questions, coach each other through practice questions as a study squad, and leave with a credential plan with real dates.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="The HS-BCP credential, the exam, and strategies for scenario questions",
                   practice="Study squad: coach each other through practice questions from every module"),
    objectives=[
        "Describe the HS-BCP credential, how to qualify, and the format of the exam, using CCE's current information.",
        "Complete practice questions and identify their two weakest areas.",
        "Use test strategies for scenario-based questions.",
        "Create a personal credential plan with dates.",
    ],
    slide_objectives=[
        "Know what the HS-BCP is and how to qualify",
        "Find your two weakest areas",
        "Use strategies for scenario questions",
        "Leave with a credential plan and real dates",
    ],
    opening=dict(title="A test you passed",
                 quote="Think of a test or challenge you were nervous about and got through anyway: a driving test, a GED, an interview, a hard conversation. What helped you get through it?",
                 notes="Write what helped on the board: practice, someone believed in me, I studied a little every day, I slept the night before. Point out that these are test strategies. Learners already have them."),
    learn_line="The credential, the exam, and how to answer scenario questions.",
    learn=[
        dict(eyebrow="The credential", title="Human Services Board Certified Practitioner",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Issued by the <strong>Center for Credentialing &amp; Education (CCE)</strong></li>
        <li>Shows you meet a national standard for human services practice</li>
        <li>Eligibility is based on <strong>education and supervised work experience</strong>. The exact routes are on CCE's website.</li>
        <li>Requires passing the exam, and continuing education to keep it</li>
      </ul>
    </div>
    <div class="box c2"><h3>Check the source</h3>Exam details, fees, and eligibility can change. Always use CCE's current candidate information, not a friend's advice or an old website.</div>
  </div>""",
             notes="Show CCE's HS-BCP page on screen. Walk through the eligibility routes and help learners figure out which route fits them. Some may need more education or supervised experience before they can sit for the exam. That's okay: their credential plan will include those steps."),
        dict(eyebrow="The exam · confirm with CCE", title="What to expect",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Multiple-choice questions, many of them <strong>scenarios</strong>: “A client tells you… What should you do first?”</li>
        <li>Content areas cover the knowledge and skills of human services practice</li>
        <li>Check CCE's candidate handbook for the current number of questions, time limit, content areas, and how to schedule</li>
      </ul>
    </div>
    <div class="box c3"><h3>This course covered</h3>Roles and systems · Ethics · Trauma-informed practice · Communication · Case management · Resources · Documentation</div>
  </div>""",
             notes="Fill in the current exam format from CCE's handbook on the board before class. Map each CCE content area to the course module that covers it. Learners should see that Modules 1 through 7 were exam prep all along."),
        dict(eyebrow="Strategy", title="Reading a scenario question",
             body="""  <ol>
    <li><strong>Read the last line first.</strong> What is it asking: first, best, most important, or NOT?</li>
    <li><strong>Find the key facts.</strong> Safety? A child? Consent? Your role's limits?</li>
    <li><strong>Cross out</strong> answers that break ethics, skip consent, or step outside your role.</li>
    <li><strong>Choose the best answer</strong>, not just a true one. Several may be true.</li>
    <li><strong>Don't add facts</strong> that aren't in the question.</li>
  </ol>""",
             notes="Model this with one question out loud. Learners' lived experience is a strength, but on the exam they need to answer by the professional standard, not by “what we did at my program.”"),
        dict(eyebrow="Strategy", title="Patterns that point to the best answer",
             body="""  <table class="tbl">
    <tr><th>If the question involves…</th><th>The best answer usually…</th></tr>
    <tr><td><strong>Safety or risk of harm</strong></td><td>Puts safety first, before paperwork or rapport</td></tr>
    <tr><td><strong>A first meeting</strong></td><td>Builds rapport and explains confidentiality and its limits</td></tr>
    <tr><td><strong>Sharing information</strong></td><td>Gets consent or a release first</td></tr>
    <tr><td><strong>Something outside your role</strong></td><td>Refers, consults a supervisor, or both</td></tr>
    <tr><td><strong>Client choice</strong></td><td>Respects self-determination, even if you disagree</td></tr>
  </table>""",
             notes="These are patterns, not rules. Every one connects to a module: safety (Modules 2–3), consent (Modules 2 and 7), role limits (Module 1), self-determination (Modules 4–5)."),
        dict(eyebrow="Test day", title="Taking care of yourself",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Before:</strong> study in short sessions. Sleep. Know the route and what ID to bring.</li>
        <li><strong>During:</strong> breathe. Skip and come back. Watch the clock, but don't stare at it.</li>
        <li><strong>After:</strong> whatever happens, you have a plan. Many people pass on a second try.</li>
      </ul>
    </div>
    <div class="box c1"><h3>Test anxiety is normal</h3>Try box breathing: in for 4, hold for 4, out for 4, hold for 4. Practice it now so it works on test day.</div>
  </div>""",
             notes="Do one minute of box breathing together. Ask learners about accommodations: if they have a documented disability, CCE has a process for requesting testing accommodations. Point them to the candidate handbook."),
        dict(eyebrow="Your plan", title="A credential plan with dates",
             body="""  <table class="tbl">
    <tr><th>Step</th><th>Example</th></tr>
    <tr><td>Check my eligibility route on CCE's website</td><td>This week</td></tr>
    <tr><td>Gather transcripts and proof of experience</td><td>Within 30 days</td></tr>
    <tr><td>Apply and pay, or apply for a fee waiver or sponsor if available</td><td>Date</td></tr>
    <tr><td>Study my two weakest areas, 3 times a week</td><td>Starting date</td></tr>
    <tr><td>Schedule and take the exam</td><td>Date</td></tr>
  </table>""",
             notes="Every learner leaves with this plan filled in during Apply. Ask whether Chart Academy or the learner's employer can sponsor exam fees, and share what's available."),
    ],
    quick_check=dict(title="Try one",
                     items=["A client tells you during intake that she has thought about ending her life. What should you do FIRST?",
                            "A) Finish the intake so you have complete information",
                            "B) Stay with her, ask directly about her safety, and follow agency procedure to get help now",
                            "C) Refer her to a therapist and give her the number",
                            "D) Tell her you'll check in at your next meeting"],
                     notes="Best answer: B. Safety comes first, and you don't leave her alone with a number. Walk through the strategy: last line first (FIRST), key fact (risk of harm), cross out A and D, and C is a cold referral. Remind learners of 988."),
    practice_line="Become a study squad. Coach each other through practice questions from every module.",
    practice_notes="Hand out the in-class packet. Each coach card has two practice questions written for this course, with the best answer and the reason. These are not real exam questions. The coach reads the question, the team answers, then the coach explains.",
    activity_title="Study squad: coach the team",
    team_notes_title="Study Squad",
    case=dict(
        name="practice questions",
        fiction="All practice questions and people in them are written for this course. They are not real exam questions.",
        page_intro="Your team becomes a <strong>study squad</strong>. Each person is the coach for one part of the course, with practice questions written for this course (not real exam questions).",
        page_how="Each coach reads their questions to the team, everyone answers on their own, then the coach walks the team through the best answer using the scenario strategy. Every learner tracks their own results to find their two weakest areas.",
        slide_title="Your study squad",
        slide_intro="Today your team is a study squad. Each person coaches one part of the course.",
        bullets=["Coach cards have two practice questions each, with answers",
                 "Everyone answers on their own first",
                 "The coach explains the best answer, using the strategy",
                 "Track your own results to find your two weakest areas"],
        quote="“I know this stuff from living it. I just need to learn how the test wants me to say it.”",
        quote_label="What a past learner said",
        slide_notes="This quote captures today. Learners know the work. The exam asks them to choose by the professional standard. Coaching each other is one of the best ways to learn it.",
        packet_text="Your team is a study squad. Each person is the coach for one part of the course. The coach reads each practice question aloud. Everyone writes their answer on their own, without talking. Then the coach reveals the best answer and explains why, using the scenario strategy. Each learner tracks their own results on the team worksheet. These questions were written for this course. They are not real exam questions.",
    ),
    roles_title="Six coaches",
    roles_small="Each coach has two practice questions, the best answer, and why.",
    roles_notes="Give the Ethics coach card to a confident reader, since it goes first. The Team lead keeps time and the strategy poster.",
    roles=[
        dict(name="Ethics and boundaries coach", where="Modules 1 and 2",
             facts_label="Your questions (read aloud, then reveal):",
             facts=["Q1. A client's sister calls and asks whether her brother kept his appointment. What should you do? A) Tell her yes, since she's family. B) Say you can't confirm whether someone receives services. C) Ask the client later if it was okay. D) Transfer her to your supervisor. <strong>Best: B.</strong> Even confirming someone is a client breaks confidentiality without a release.",
                    "Q2. A client offers you $50 to thank you for your help. What is the best response? A) Accept it so you don't offend her. B) Accept and give it to the agency. C) Thank her warmly and explain you can't accept money, following agency policy. D) Ignore the offer. <strong>Best: C.</strong> Decline respectfully and follow policy."]),
        dict(name="Trauma-informed practice coach", where="Module 3",
             facts_label="Your questions (read aloud, then reveal):",
             facts=["Q1. A client goes silent and stares at the floor when you ask about her housing history. What should you do first? A) Repeat the question more slowly. B) Move to the next section. C) Pause, check in, and offer her a choice to take a break or skip it. D) Note that she is uncooperative. <strong>Best: C.</strong> This may be a freeze response. Offer safety and choice.",
                    "Q2. Which practice best supports “trustworthiness and transparency”? A) Explaining what will happen in the meeting and how long it will take. B) Keeping the intake form private from the client. C) Asking all questions in one visit. D) Using clinical terms. <strong>Best: A.</strong>"]),
        dict(name="Communication coach", where="Module 4",
             facts_label="Your questions (read aloud, then reveal):",
             facts=["Q1. Which is an open question? A) “Do you have a job?” B) “Are you okay?” C) “What has your work been like this year?” D) “Did you go to the clinic?” <strong>Best: C.</strong>",
                    "Q2. A client who speaks limited English brings her 12-year-old to interpret. What should you do? A) Use the child, since she's there. B) Arrange a trained interpreter or language line. C) Speak slowly and loudly in English. D) Reschedule without explaining. <strong>Best: B.</strong> Don't use children as interpreters."]),
        dict(name="Case management coach", where="Module 5",
             facts_label="Your questions (read aloud, then reveal):",
             facts=["Q1. Which goal is SMART? A) “Client will find housing.” B) “Client will feel better.” C) “Client will submit the rental assistance application, with the case manager, by May 15.” D) “Client will try to work.” <strong>Best: C.</strong>",
                    "Q2. You referred a client to a job program two weeks ago. What is the next step in the case management cycle? A) Close the case. B) Follow up to see if she connected and how it's going. C) Make a new referral. D) Wait for the program to call you. <strong>Best: B.</strong> Monitoring."]),
        dict(name="Resources and documentation coach", where="Modules 6 and 7",
             facts_label="Your questions (read aloud, then reveal):",
             facts=["Q1. Which is the best example of a warm handoff? A) Giving the client a phone number. B) Emailing the client a list. C) With consent, calling the agency together and introducing the client. D) Telling the client to walk in. <strong>Best: C.</strong>",
                    "Q2. Which case note sentence is written best? A) “Client was hostile.” B) “Client raised his voice and said, ‘Nobody helps me.’” C) “Client had an attitude.” D) “Client seemed upset, probably drinking.” <strong>Best: B.</strong> Facts, not labels."]),
        dict(name="Team lead and test coach", where="Strategy and time",
             facts_label="Your job:",
             facts=["Keep time: about 6 minutes per coach.",
                    "Before each reveal, ask: “What's the last line asking? What are the key facts? What can we cross out?”",
                    "Make sure everyone writes their own answer before the reveal."],
             extra="<strong>Only you know:</strong> after all the coaches finish, the team writes one practice question of its own for another team to answer."),
    ],
    steps=[
        dict(label="Prepare to coach", desc="read your coach card, practice reading the questions aloud, and plan how you'll explain the best answer."),
        dict(label="Study squad rounds", desc="each coach leads their questions. Everyone answers on their own, then the coach explains. Track your results."),
        dict(label="Write and trade", desc="your team writes one new practice question and trades it with another team, then shares top strategies."),
        dict(label="Debrief", desc="talk about how it felt to coach, and what your results told you."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · prepare to coach", title="Get ready to coach",
             body="""  <ul>
    <li>Read your two questions and the best answers</li>
    <li>Practice reading each question out loud</li>
    <li>Plan how you'll explain <em>why</em>, using the strategy</li>
    <li>Team lead: set up the timer and the worksheet</li>
  </ul>""",
             notes="Coaches will be nervous about reading aloud. Remind them: teaching is the best way to learn."),
        dict(eyebrow="Step 2 · study squad rounds", title="Answer, reveal, explain",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>The coach reads the question</li>
        <li>Everyone writes an answer, no talking</li>
        <li>Team lead asks the strategy questions</li>
        <li>The coach reveals the best answer and explains</li>
        <li>Everyone marks their results on the worksheet</li>
      </ol>
    </div>
    <div class="box c3"><h3>Ask every time</h3>What's the last line asking? What are the key facts? What can we cross out?</div>
  </div>""",
             notes="If time allows, add more practice questions you've written or from approved study materials. Don't use questions from unauthorized sources claiming to be real exam questions."),
        dict(eyebrow="Step 3 · write and trade", title="Write your own question",
             body="""  <ul>
    <li>As a team, write <strong>one scenario question</strong> with four answers</li>
    <li>Trade with another team and answer theirs</li>
    <li>Share your team's <strong>top three test strategies</strong></li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes: your question and your top strategy.</div>""",
             notes="Writing a question forces learners to think like the exam. Good questions have one best answer and three that are tempting but wrong."),
    ],
    debrief=dict(questions=["What did coaching teach you that answering didn't?",
                            "Which areas came up as weak for you?",
                            "Which strategy will you use most?",
                            "What would help you most between now and the exam?"],
                 notes="Collect information on the class's weakest areas so you can plan review sessions or office hours."),
    apply_line="Show what you learned, then build your credential plan.",
    own_words="“My next three steps toward the HS-BCP are …”",
    exit_ticket=["Name one strategy for scenario questions.",
                 "What are your two weakest areas?",
                 "What is the date of the first step on your credential plan?"],
    packet_instructions="Print one packet per team. Cut the coach cards apart and give one to each person. The practice questions were written for this course and are not real exam questions. Before class, check CCE's current HS-BCP information and update the slides if anything has changed.",
    worksheet=dict(
        title="My results by area",
        instructions="Each learner fills in a row for each area: how many of the two questions you got right, and what you noticed. Use a separate worksheet for each person, or use the Team Notes file.",
        columns=[("Area", 26), ("Right (of 2)", 12), ("Why I missed it (pattern)", 30), ("Study action", 0)],
        rows=5,
        first_col=["Ethics and boundaries", "Trauma-informed practice", "Communication", "Case management",
                   "Resources and documentation"],
        plan=[("Our team's practice question (with four answers and the best one):", 4),
              ("Our top three test strategies:", 3)],
    ),
    team_notes=dict(step1_columns=["Coach", "Questions I'll lead", "How I'll explain the best answers"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.8, 0.9, 2.0, 2.0]),
    assignment=dict(
        intro="Capture what you learned as a coach and a test-taker, then build your personal credential plan with dates.",
        parts=[
            dict(title="Your coaching", summary="The question you coached and how you explained the best answer.",
                 note="Answer about the coach card you held in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="Pick one question you coached. Explain why the best answer is best, and why one wrong answer is tempting.", h=1.1),
                        dict(type="q", text="Which module does this question connect to, and what did you learn in that module that helps?", h=0.8)]),
            dict(title="Your results and study plan", summary="Your results by area, your two weakest areas, and your study plan.",
                 note="Use your results from the study squad.",
                 items=[dict(type="grid", text="Fill in your results.",
                             columns=["Area", "Right (of 2)", "Study action"], widths=[2.3, 1.2, 3.2], rows=5, h=0.45,
                             first_col=["Ethics and boundaries", "Trauma-informed practice", "Communication", "Case management",
                                        "Resources and documentation"]),
                        dict(type="q", text="Name your two weakest areas and exactly how you'll study each one.", h=0.9,
                             hint="(What, how often, and with whom.)"),
                        dict(type="q", text="Walk through the scenario strategy for the quick-check question on safety. Why is B the best answer?", h=0.9)]),
            dict(title="My credential plan", summary="Your next steps toward the HS-BCP, with dates, in your own words.",
                 items=[dict(type="grid", text="Build your credential plan.",
                             columns=["Step", "Date", "Who can help"], widths=[3.4, 1.4, 1.9], rows=5, h=0.45,
                             first_col=["Check my eligibility route on CCE's website", "Gather transcripts and proof of experience",
                                        "Apply (and ask about fee help)", "Study my two weakest areas", "Schedule and take the exam"]),
                        dict(type="q", text="Why does this credential matter to you? Think about where you started and where you're going. What will it mean for you, your family, or your community?",
                             h=2.0, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “My next three steps toward the HS-BCP are …”", h=0.8)]),
        ],
        rubric_full=[
            ["Coaching (Part 1)", "Clear explanation of the best answer and the tempting wrong answer, tied to a module.",
             "Explanation is partly clear.", "Missing."],
            ["Results and study plan (Part 2)", "Honest results, two named weak areas, and a specific study plan.",
             "Results are present but the study plan is general.", "Missing."],
            ["Scenario strategy (Part 2, last question)", "Uses the strategy steps correctly to explain why B is best.",
             "Partly uses the strategy.", "Missing, or incorrect."],
            ["Credential plan and reflection (Part 3)", "Realistic dates for every step. Reflection is thoughtful and in the learner's own words.",
             "Some dates missing, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your coaching and your results.",
        reflection_title="My credential plan",
        reflection_slide="Put a real date on every step of your credential plan and name who can help. Then write about why this credential matters to you.",
    ),
))

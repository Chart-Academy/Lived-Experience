"""Content for Certified Survivor Workforce Facilitator Modules 1-8 (women-centered, NADSP DSP-I pathway).

build_module.py turns each entry into the module page, slides, in-class packet and Word files.
Every case is fictional. Hotlines and agency details marked "confirm before class" must be checked by the
instructor before each cohort.
"""
from cp_modules import finish, debrief_steps, REFLECT_HINT

PORTFOLIO = ("Save this part. It is written so you can use it as one of the four work samples in your "
             "NADSP DSP-I portfolio.")

MODULES = {}

# =====================================================================================================
# MODULE 1 · The Facilitator Role & NADSP Code of Ethics
# =====================================================================================================
MODULES[1] = finish(dict(
    num=1, hours=5,
    title="The Facilitator Role &amp; NADSP Code of Ethics",
    short_title="Role &amp; Code of Ethics",
    slide_title_html="The Facilitator Role<br>&amp; NADSP Code of Ethics",
    subtitle="Walking beside women as they rebuild, with ethics that protect them and you.",
    title_notes="Welcome the cohort. Many of the women in this room have lived through what the women they will support are living through now. Say plainly: that is the reason this course exists, and nobody ever has to share her own story to take part. Today they will learn what a survivor workforce facilitator does, the NADSP Code of Ethics, and how to hold boundaries. They will finish a draft reflection for the Code of Ethics Commitment E-Badge, the first badge toward DSP-I.",
    lead="What a survivor workforce facilitator does, the NADSP Code of Ethics that guides direct support, and how to hold boundaries when a woman's story mirrors your own. You'll work through real ethical situations as a team and draft the reflection for your first E-Badge.",
    flow_text=dict(open="Welcome, community agreements, and opening circle",
                   learn="The facilitator role, the NADSP Code of Ethics, boundaries, and the DSP-I path",
                   practice="Team roles: ethics decisions at a women's workforce program"),
    objectives=[
        "Describe the duties of a survivor workforce facilitator and a direct support professional in programs that serve women.",
        "Explain each tenet of the NADSP Code of Ethics with a workplace example.",
        "Set healthy boundaries when supporting women whose experiences may mirror their own.",
        "Prepare a written reflection for the Code of Ethics Commitment E-Badge.",
    ],
    slide_objectives=[
        "Describe the facilitator and direct support roles",
        "Explain the NADSP Code of Ethics with real examples",
        "Hold boundaries when her story sounds like yours",
        "Draft your Code of Ethics Commitment reflection",
    ],
    opening=dict(title="A woman who walked beside you",
                 quote="Think of a woman who helped you, or someone you love, through a hard time. She didn't fix everything. She walked beside you. What did she do that mattered?",
                 notes="Set community agreements first: what's shared here stays here, speak from your own experience, you can pass, and you can step out any time. Then the opening question. Write what women name: she believed me, she didn't judge, she let me decide, she showed up, she kept my business private. Keep the list. Every item matches a tenet of the NADSP Code of Ethics."),
    learn_line="The role, the Code of Ethics, and the boundaries that keep everyone safe.",
    learn=[
        dict(eyebrow="The role", title="What a survivor workforce facilitator does",
             body="""  <div class="cols">
    <ul>
      <li>Welcomes women into workforce programs and builds trust</li>
      <li>Helps each woman set her own goals for safety, stability, and work</li>
      <li>Leads workforce readiness groups and workshops</li>
    </ul>
    <ul>
      <li>Connects women to housing, safety, health, child care, and benefits</li>
      <li>Supports women through job search, training, and the first months on the job</li>
      <li>Keeps accurate, private records and works with a team</li>
    </ul>
  </div>
  <p class="small" style="margin-top:20px">Settings: domestic violence and anti-trafficking programs, women's reentry programs, shelters, workforce centers, and community nonprofits.</p>""",
             notes="Connect to the opening list. Point out that direct support professionals (DSPs) work in many settings. The DSP-I credential recognizes the skills and ethics of direct support work. In this course, those skills are applied to supporting women survivors on the path to work."),
        dict(eyebrow="Know your lane", title="What the role is, and isn't",
             body="""  <table class="tbl">
    <tr><th></th><th>Facilitator (you)</th><th>Counselor or therapist</th><th>Lawyer or legal advocate</th></tr>
    <tr><td><strong>Does</strong></td><td>Supports goals, safety, stability, and work. Refers and follows up.</td><td>Treats trauma and mental health conditions</td><td>Gives legal advice, protection orders, custody, immigration</td></tr>
    <tr><td><strong>Does not</strong></td><td>Diagnose, give therapy, or give legal advice</td><td>Usually doesn't do job placement</td><td>Usually doesn't do day-to-day support</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Knowing when to refer is part of the job, not a failure.</p>""",
             notes="Ask: “A woman asks you whether she should file for a protection order. What do you do?” (Listen, share information about where she can get legal help, offer a warm handoff to a legal advocate, and respect her choice.)"),
        dict(eyebrow="NADSP Code of Ethics", title="The tenets",
             body="""  <div class="cols3">
    <div class="box c2"><h3>Person-centered supports</h3>Her goals, her choices, her life</div>
    <div class="box c3"><h3>Physical and emotional well-being</h3>Safety, health, and dignity</div>
    <div class="box c4"><h3>Integrity and responsibility</h3>Honesty, reliability, and owning mistakes</div>
    <div class="box c1"><h3>Confidentiality</h3>Her story is hers to share</div>
    <div class="box c2"><h3>Justice, fairness, and equity</h3>Equal treatment and fair access</div>
    <div class="box c3"><h3>Respect</h3>Dignity in words and actions</div>
    <div class="box c4"><h3>Relationships</h3>Supporting healthy connections</div>
    <div class="box c1"><h3>Self-determination</h3>She decides, with support</div>
    <div class="box c2"><h3>Advocacy</h3>Speaking up for her rights</div>
  </div>""",
             notes="Before class, download the current NADSP Code of Ethics from nadsp.org and check that the tenets on this slide match the current version. Hand out the full text. Learners will need it for the Commitment E-Badge reflection."),
        dict(eyebrow="Ethics in practice", title="What the tenets look like at work",
             body="""  <table class="tbl">
    <tr><th>Tenet</th><th>In a women's workforce program</th></tr>
    <tr><td><strong>Self-determination</strong></td><td>She chooses whether to take a job offer, even if you think she should</td></tr>
    <tr><td><strong>Confidentiality</strong></td><td>You never tell an employer she is a survivor without her written consent</td></tr>
    <tr><td><strong>Justice and fairness</strong></td><td>Every woman gets the same chance at the job leads, not just the ones staff like</td></tr>
    <tr><td><strong>Relationships</strong></td><td>You support her friendships and family ties, without becoming her friend yourself</td></tr>
    <tr><td><strong>Advocacy</strong></td><td>You speak up when an employer's policy unfairly shuts women out</td></tr>
  </table>""",
             notes="Ask learners to add one more example for any tenet from their own experience, as a participant or a worker."),
        dict(eyebrow="Boundaries", title="When her story sounds like yours",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Notice it:</strong> a racing heart, wanting to rescue her, or thinking about her case at night</li>
        <li><strong>Share wisely:</strong> brief, only if it helps her, and then bring it back to her</li>
        <li><strong>No dual relationships:</strong> not her friend, landlord, employer, or social media follower</li>
        <li><strong>Use supervision:</strong> talk it through with your supervisor, not with her</li>
      </ul>
    </div>
    <div class="box c1"><h3>Ask yourself</h3>“Who is this for: her, or me?”<br><br>“Would I do this for every woman in the program?”</div>
  </div>""",
             notes="This is the heart of a lived experience course. Normalize it: being moved by a woman's story means you care. Boundaries are what let you keep caring for years without burning out."),
        dict(eyebrow="Your credential", title="The path to DSP-I",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>15 E-Badges</strong> through the NADSP E-Badge Academy</li>
        <li><strong>First:</strong> the Code of Ethics Commitment E-Badge (today)</li>
        <li><strong>50 hours</strong> of accredited education</li>
        <li><strong>Core competencies:</strong> Crisis Prevention and Intervention, Safety, Person-Centered Practices, Health and Wellness</li>
        <li><strong>A portfolio</strong> of four work samples</li>
      </ul>
    </div>
    <div class="box c3"><h3>In this course</h3>Modules 3, 5, 6, and 7 line up with the core competency badges. Several assignments are built to be work samples.</div>
  </div>""",
             notes="Show the Credentials page on the course site. Explain how enrollment in the E-Badge Academy works for this cohort (an organization enrolls learners; individuals can't buy enrollment on their own). Confirm current requirements on nadsp.org."),
    ],
    quick_check=dict(title="Which tenet?",
                     items=["A woman decides to turn down a job offer because the shift ends after dark. You respect it.",
                            "An employer calls asking why a participant is in your program. You don't say.",
                            "You make sure every woman hears about the new job fair, not just the ones you know best.",
                            "You help a woman reconnect with her sister, who has been a good support.",
                            "You tell your manager a hiring partner won't consider any woman with a record."],
                     notes="Answers: 1) Self-determination. 2) Confidentiality. 3) Justice, fairness, and equity. 4) Relationships. 5) Advocacy. More than one tenet can fit. Accept good reasoning."),
    practice_line="Step into a role and work through the ethical questions in one woman's case as a team.",
    practice_notes="Hand out the in-class packet. One packet per team. Teams of 4 or 5 can combine the Team lead with another role.",
    activity_title="Team roles: ethics at Women Rising",
    team_notes_title="Ethics at Women Rising",
    case=dict(
        name="Angela",
        page_intro="<strong>Angela, 31</strong> (fictional), joined Women Rising, a workforce program for women survivors, after leaving an abusive relationship and spending 18 months in a shelter. She wants a full-time job with benefits. This month, several staff members each hit an ethical question about her case.",
        page_how="Each person on your team plays a staff member at Women Rising. Your role card has facts only you know. Together, your team decides what to do about each question, using the NADSP Code of Ethics.",
        slide_title="Meet Angela",
        slide_intro="<strong>Angela, 31</strong>, joined Women Rising, a workforce program for women survivors.",
        bullets=["Left an abusive relationship two years ago",
                 "Lived in a shelter for 18 months, now in transitional housing",
                 "Worked in restaurants for 10 years",
                 "Wants a full-time job with health insurance"],
        quote="“For years someone else made every decision for me. I need people who will let me make my own, even the wrong ones.”",
        quote_label="What Angela says",
        slide_notes="Angela's words point straight to self-determination. Keep coming back to them during the case: whose decision is it?",
        packet_text="<strong>Angela, 31</strong>, joined Women Rising, a workforce program for women survivors, after leaving an abusive relationship two years ago and spending 18 months in a shelter. She now lives in transitional housing. She worked in restaurants for 10 years and wants a full-time job with health insurance. This month, several staff members each ran into an ethical question about her case. Today is the team meeting.",
    ),
    roles_title="Six staff, six questions",
    roles_small="Each card has facts only you know. Bring them to the team meeting.",
    roles_notes="Assign the Peer mentor card to a learner who is comfortable talking about boundaries. Remind teams to name a tenet for every decision.",
    roles=[
        dict(name="Workforce facilitator", where="Angela's main contact",
             facts=["Angela invited you to her church's women's day and to her birthday dinner.",
                    "She texts you on your personal phone at night. You gave her the number during a hard week.",
                    "You like her a lot and don't want to hurt her feelings."],
             need="A respectful way to reset the relationship."),
        dict(name="Job developer", where="Works with employers",
             facts=["A hotel wants to interview Angela for a full-time job with benefits.",
                    "The hiring manager asked you, “Is she one of the domestic violence women? I need to know if there'll be drama.”",
                    "Angela has not signed a release to share anything about her history."],
             need="What to say to the hiring manager, and what to tell Angela."),
        dict(name="Housing advocate", where="Transitional housing",
             facts=["A staff member wants to make counseling a requirement for Angela to keep her housing.",
                    "Angela said she isn't ready for counseling and gets support from her church group.",
                    "Program rules don't require counseling."],
             need="The team to decide whose choice this is."),
        dict(name="Peer mentor", where="Has lived experience of leaving abuse",
             facts=["Angela's story is very close to yours. You've been thinking about her case at night.",
                    "You've been telling her what you did when you left, in a lot of detail.",
                    "Last week she said, “I'm not you. Stop telling me what to do.”"],
             need="Help sorting out what is for Angela and what is for you."),
        dict(name="Program assistant", where="Front desk and events",
             facts=["You heard two staff joking about “the drama ladies” in the break room.",
                    "Staff tell their favorite participants about job leads first.",
                    "Angela asked you why other women always seem to hear about jobs before she does."],
             need="How to raise these concerns, and with whom."),
        dict(name="Team lead", where="Runs the meeting",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "For each question, ask: “Which tenet applies? What would Angela want?”",
                    "Write each decision on the team's ethics table."],
             extra="<strong>Only you know:</strong> the hotel's application asks whether applicants have ever had a protection order. Women Rising has advocated with other employers to remove questions like this."),
    ],
    steps=debrief_steps("read your card and decide which tenet applies before you hear the others.",
                        "each role presents its question. Name the tenet, list the options, and decide together.",
                        "choose the hardest question, explain your decision, and write what you'll say to Angela."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>Read the facts only you know</li>
    <li>What is the ethical question?</li>
    <li>Which tenet of the NADSP Code of Ethics applies?</li>
    <li>What would Angela want?</li>
  </ul>""",
             notes="Walk the room. If a learner seems affected by the Peer mentor card, quietly offer to swap roles."),
        dict(eyebrow="Step 2 · team huddle", title="Decide together",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role shares its question</li>
        <li>Name the tenet</li>
        <li>List the options and what could happen</li>
        <li>Decide, and write it on the ethics table</li>
      </ol>
    </div>
    <div class="box c3"><h3>Keep asking</h3>“Whose decision is this?” and “Would we do this for every woman in the program?”</div>
  </div>""",
             notes="Call time every 6 to 7 minutes. Make sure the job developer's question is handled without disclosing anything about Angela."),
        dict(eyebrow="Step 3 · plan and present", title="What will you say to Angela?",
             body="""  <ul>
    <li>Your team's <strong>hardest question</strong>, and the tenet behind your decision</li>
    <li>The <strong>exact words</strong> you'll use with Angela</li>
    <li>One thing to raise with your <strong>supervisor</strong> or the program</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Each person says one sentence in role.</div>""",
             notes="Praise teams that protect Angela's dignity and her right to decide."),
    ],
    debrief=dict(questions=["Which question was hardest, and why?",
                            "Where did your own experience help you see the situation? Where did it get in the way?",
                            "What's one boundary you'll set from day one on the job?",
                            "Which tenet matters most to you right now?"],
                 notes="The last question leads straight into the Code of Ethics Commitment reflection in Apply."),
    apply_line="Show what you learned, then draft your Code of Ethics Commitment reflection.",
    own_words="“The part of the Code of Ethics that matters most to me is … because …”",
    exit_ticket=["Name three tenets of the NADSP Code of Ethics.",
                 "One thing a facilitator should refer, not handle herself.",
                 "One question you still have about DSP-I."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. Any learner can swap to the Team lead role if a card feels too close to home. Bring printed copies of the current NADSP Code of Ethics.",
    worksheet=dict(
        title="Ethics table",
        instructions="For each role's question, write the tenet that applies and what your team will do.",
        columns=[("Situation", 26), ("Tenet", 22), ("What we will do", 0)],
        rows=6,
        first_col=["Invitations and late-night texts", "The hiring manager's question", "Required counseling",
                   "The peer mentor's advice", "Jokes and job leads", "The protection order question"],
        plan=[("Our hardest question, and the tenet behind our decision:", 2),
              ("The exact words we'll use with Angela:", 2),
              ("What we'll raise with our supervisor or the program:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "The ethical question", "The tenet I think applies"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[2.0, 1.6, 3.1]),
    assignment=dict(
        intro="Capture the ethical decisions from Angela's case, then draft your reflection for the Code of Ethics Commitment E-Badge.",
        parts=[
            dict(title="Your role's question", summary="The question your role faced, the tenet, and what you'd say.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What was your role's ethical question? Explain it in your own words.", h=0.8),
                        dict(type="q", text="Which tenet of the NADSP Code of Ethics applies, and why?", h=0.8),
                        dict(type="q", text="What would you do? Write what you would say, as if you are talking to the person.", h=1.0)]),
            dict(title="Your team's decisions", summary="Your team's decisions, with a tenet for each, and how to handle the employer.",
                 note="Use your team's ethics table from class.",
                 items=[dict(type="grid", text="Fill in your team's decision for each situation.",
                             columns=["Situation", "Tenet", "Our decision"], widths=[2.0, 1.5, 3.2], rows=6, h=0.5,
                             first_col=["Invitations and texts", "Hiring manager's question", "Required counseling",
                                        "Peer mentor's advice", "Jokes and job leads", "Protection order question"]),
                        dict(type="q", text="Write exactly what the job developer should say to the hiring manager.", h=0.9),
                        dict(type="q", text="Name one boundary you will set from day one, and how you'll explain it to a participant.", h=0.8)]),
            dict(title="My Code of Ethics Commitment", summary="A draft reflection for your Code of Ethics Commitment E-Badge, in your own words.",
                 note="This is a draft. Your instructor will explain how to submit your final reflection to the NADSP E-Badge Academy.",
                 items=[dict(type="grid", text="Choose three tenets and connect each one to your life and your future work.",
                             columns=["Tenet", "Where I've seen it in my own life", "How I'll practice it on the job"],
                             widths=[1.8, 2.45, 2.45], rows=3, h=0.75, first_col=["1.", "2.", "3."]),
                        dict(type="q", text="Why do you commit to the NADSP Code of Ethics? How will your own experience shape the way you support women?",
                             h=2.4, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “The part of the Code of Ethics that matters most to me is … because …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's question (Part 1)", "Names the question, the right tenet, and a respectful, realistic response.",
             "Question is named. The tenet or response is unclear.", "Missing, or the response breaks confidentiality."],
            ["Team decisions (Part 2 table)", "A sound decision and tenet for all six situations.",
             "Most situations complete, or tenets are missing.", "Few situations complete."],
            ["Employer script and boundary (Part 2, questions)", "Protects Angela's privacy and sets a clear, kind boundary.",
             "Partly protects privacy, or the boundary is vague.", "Shares private information, or missing."],
            ["Code of Ethics reflection (Part 3)", "Three tenets tied to life and work. Thoughtful and in the learner's own words.",
             "Tenets are general, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's question and your team's decisions.",
        reflection_title="My Code of Ethics Commitment",
        reflection_slide="Choose three tenets and connect each to your life and your future work. Then write why you commit to the NADSP Code of Ethics. This is the draft for your first E-Badge.",
    ),
))

# =====================================================================================================
# MODULE 2 · Trauma Recovery & Stabilization
# =====================================================================================================
MODULES[2] = finish(dict(
    num=2, hours=6,
    title="Trauma Recovery &amp; Stabilization",
    short_title="Trauma &amp; Stabilization",
    slide_title_html="Trauma Recovery<br>&amp; Stabilization",
    subtitle="Safety and stability first. Then the path to work.",
    title_notes="Today's topic can bring up personal memories. Tell learners they can step out at any time, no explanation needed, and never have to share their own trauma. Post support lines on the board before class: 988 Suicide and Crisis Lifeline (call or text 988), the National Domestic Violence Hotline (1-800-799-7233, or text START to 88788), and the DC Victim Hotline (confirm the number before class). Point out where water and tissues are.",
    lead="How violence, exploitation, and incarceration affect women at work, and why stability has to come before a job search. You'll learn a trauma-informed, gender-responsive approach and rank one mother's stabilization needs with your team.",
    flow_text=dict(open="Welcome, grounding, and opening circle",
                   learn="Trauma and women's lives, trauma at work, SAMHSA's principles, and stabilization",
                   practice="Team roles: Marisol's stabilization plan"),
    objectives=[
        "Explain how domestic violence, sexual violence, trafficking, and incarceration can affect attention, trust, attendance, and job performance.",
        "Apply SAMHSA's six principles of a trauma-informed approach, including cultural, historical, and gender issues, to women's workforce programs.",
        "Identify the stabilization needs (housing, safety, child care, health, income) that come before job placement.",
        "Use self-care and support strategies to prevent burnout.",
    ],
    slide_objectives=[
        "Explain how trauma shows up at work",
        "Use SAMHSA's six principles in a women's program",
        "Put stabilization needs in the right order",
        "Make a plan to take care of yourself",
    ],
    opening=dict(title="What helped you feel steady?",
                 quote="Think of a time your life felt shaken up. What was the first thing that helped you feel steady again? A place, a person, a routine, a paycheck?",
                 notes="Do not ask about trauma. Ask about steadiness. Write what learners name: a safe place to sleep, my kids were okay, someone I could call, money coming in, a routine. That list is the stabilization list you'll use all day."),
    learn_line="What trauma does, why stability comes first, and how to care for yourself.",
    learn=[
        dict(eyebrow="Women's lives", title="Trauma many women carry",
             body="""  <div class="cols">
    <ul>
      <li><strong>Domestic violence:</strong> physical, emotional, sexual, and financial abuse by a partner</li>
      <li><strong>Sexual violence</strong> at any age</li>
      <li><strong>Trafficking:</strong> forced labor or commercial sex through force, fraud, or coercion</li>
    </ul>
    <ul>
      <li><strong>Incarceration:</strong> separation from children, and trauma before and during</li>
      <li><strong>Homelessness</strong> and unsafe housing</li>
      <li><strong>Community and historical trauma</strong>, including racism</li>
    </ul>
  </div>
  <div class="warn" style="margin-top:18px">Many women have lived through more than one. Assume any woman could have a trauma history, without asking her to prove it.</div>""",
             notes="Keep this factual and brief. Women in the room may have lived through these. Name that the course takes a strengths-based view: survivors are experts in survival."),
        dict(eyebrow="Trauma at work", title="How it can show up on the job",
             body="""  <table class="tbl">
    <tr><th>What staff might see</th><th>What may be going on</th></tr>
    <tr><td>Missing work or arriving late</td><td>Court dates, unsafe commute, child care fell through, an abuser sabotaging her</td></tr>
    <tr><td>Trouble focusing</td><td>Poor sleep, hypervigilance, constant worry about safety</td></tr>
    <tr><td>Clashing with a supervisor</td><td>A raised voice or controlling style can feel like danger</td></tr>
    <tr><td>Not speaking up</td><td>Years of being punished for having needs</td></tr>
    <tr><td>Gaps in work history</td><td>Incarceration, being kept from working, or fleeing</td></tr>
  </table>""",
             notes="These are survival responses, not character flaws. Ask learners how they'd want an employer to respond in each case."),
        dict(eyebrow="SAMHSA's six principles", title="A trauma-informed approach",
             body="""  <div class="cols3">
    <div class="box c2"><h3>Safety</h3>Physical and emotional safety, including her location</div>
    <div class="box c3"><h3>Trustworthiness and transparency</h3>No surprises. Explain every step.</div>
    <div class="box c4"><h3>Peer support</h3>Women with lived experience as guides</div>
    <div class="box c1"><h3>Collaboration and mutuality</h3>Power shared, not held over her</div>
    <div class="box c2"><h3>Empowerment, voice, and choice</h3>She decides. Build on her strengths.</div>
    <div class="box c3"><h3>Cultural, historical, and gender issues</h3>Gender-responsive and culturally grounded</div>
  </div>""",
             notes="From SAMHSA's Guidance for a Trauma-Informed Approach (2014). For women who survived control, choice is healing in itself. Ask: “Which principle did the woman who walked beside you live out?”"),
        dict(eyebrow="Gender-responsive", title="What it means for women",
             body="""  <ul>
    <li><strong>Relationships matter:</strong> women often heal and grow through connection</li>
    <li><strong>Children are central:</strong> custody, child care, and school shape every decision</li>
    <li><strong>Safety is ongoing:</strong> leaving can be the most dangerous time</li>
    <li><strong>Economic abuse is common:</strong> ruined credit, no savings, and no work history</li>
    <li><strong>Women-only spaces</strong> can feel safer for women who were harmed by men</li>
  </ul>""",
             notes="Gender-responsive programs design services around women's lives and pathways. Stress that the skills apply to anyone you support, and that every woman is different. Ask, don't assume."),
        dict(eyebrow="Stabilization", title="Stability before a job search",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Safety:</strong> is she safe today, tonight, and on the way to work?</li>
        <li><strong>Shelter:</strong> a stable place to sleep</li>
        <li><strong>Children:</strong> safe care and school</li>
        <li><strong>Health:</strong> urgent physical and mental health needs</li>
        <li><strong>Income:</strong> benefits or emergency funds to bridge the gap</li>
        <li><strong>Documents:</strong> ID, Social Security card, birth certificates</li>
      </ol>
    </div>
    <div class="box c3"><h3>Her order, not ours</h3>The order is a guide. Ask her what feels most urgent. A job can be part of stabilization when she's ready.</div>
  </div>""",
             notes="Many women want a job immediately, and income can mean safety. The skill is helping her see what has to be in place for a job to last, without taking over the decision."),
        dict(eyebrow="Taking care of you", title="Burnout and vicarious trauma",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Vicarious trauma:</strong> taking on effects from hearing women's stories again and again</li>
        <li><strong>Triggers:</strong> a story close to your own can bring old feelings back</li>
        <li><strong>Burnout:</strong> exhaustion from workload and stress over time</li>
      </ul>
    </div>
    <div class="box c1"><h3>Your plan</h3>Supervision. Someone outside work. A way to leave work at work. Your own support when you need it. That's strength, not weakness.</div>
  </div>""",
             notes="Learners will build a wellness plan in Apply. Remind them of 988 and any employee assistance program at their future job."),
    ],
    quick_check=dict(title="What might be going on?",
                     items=["A participant misses every Tuesday session.",
                            "A woman freezes when a male staff member raises his voice in the hallway.",
                            "A participant refuses to give her home address on a form.",
                            "A woman wants to start work tomorrow, but she's sleeping in her car with her kids."],
                     notes="Possible answers: court dates or supervision check-ins; a trauma response; safety, she may be hiding from an abuser; stabilization needs come first, but respect her urgency and look for a bridge like emergency shelter and income."),
    practice_line="Step into a role and help one mother decide what comes first.",
    practice_notes="Hand out the in-class packet. Remind learners Marisol is fictional, and anyone can switch to the Team lead role.",
    activity_title="Team roles: Marisol's stabilization plan",
    team_notes_title="Marisol's Stabilization Plan",
    case=dict(
        name="Marisol",
        page_intro="<strong>Marisol, 28</strong> (fictional), left an abusive partner six weeks ago with her two children, ages 3 and 8. She is staying in a domestic violence shelter and came to a women's workforce program because she wants a job right away.",
        page_how="Each person on your team plays someone supporting Marisol. Your role card has facts only you know. Together, your team ranks her stabilization needs, with Marisol's own priorities in mind, and decides what comes before, and alongside, her job search.",
        slide_title="Meet Marisol",
        slide_intro="<strong>Marisol, 28</strong>, left an abusive partner six weeks ago with her two children, ages 3 and 8.",
        bullets=["Staying in a domestic violence shelter, which has a 90-day limit",
                 "Her partner controlled all the money",
                 "Worked as a home health aide before he made her quit",
                 "Wants a job right now"],
        quote="“I need my own money. I'm never depending on a man again. Just help me find a job.”",
        quote_label="What Marisol says",
        slide_notes="Marisol's urgency is valid: income is safety for her. The team's job is to honor that and make sure the job can last.",
        packet_text="<strong>Marisol, 28</strong>, left an abusive partner six weeks ago with her children, Sofia (8) and Leo (3). They are staying in a domestic violence shelter with a 90-day limit. Her partner controlled all the money, and she has no bank account of her own. She worked as a home health aide for four years before he made her quit. She came to a women's workforce program and wants a job right away.",
    ),
    roles_title="Six supports, one plan",
    roles_small="Each card has facts only you know. Marisol's priorities come first.",
    roles_notes="The Workforce facilitator card holds Marisol's goals. The Team lead makes sure the team asks what Marisol wants before ranking.",
    roles=[
        dict(name="Shelter advocate", where="Domestic violence shelter",
             facts=["Marisol has 44 days left at the shelter.",
                    "Her ex has been driving past her old job and her sister's house.",
                    "The shelter's location is confidential. Marisol can't give it on job applications."],
             need="A plan for the address question and her commute."),
        dict(name="Child and family worker", where="Family support program",
             facts=["Leo, 3, has no child care. There's a wait list for subsidized care, but survivors may get priority. Eligibility must be checked.",
                    "Sofia, 8, changed schools and is having nightmares.",
                    "Marisol asked about custody. Her ex has not filed anything yet."],
             need="Child care before any job can start, and a legal referral for custody questions."),
        dict(name="Benefits outreach worker", where="Public benefits",
             facts=["Marisol has no income. She may qualify for SNAP, TANF, and Medicaid for herself and the children.",
                    "Her ID and the children's birth certificates are still at her ex's apartment.",
                    "She doesn't have a bank account. Her ex has wrecked her credit."],
             need="Replacement documents, and a safe way to get her things."),
        dict(name="Community health worker", where="Women's health center",
             facts=["Marisol has headaches since her ex hit her head against a wall two months ago. She hasn't seen a doctor.",
                    "She says she sleeps 3 to 4 hours a night.",
                    "She told you, “I'm fine. I don't have time to be sick.”"],
             need="A medical visit and support for sleep and stress, without pushing her.",
             extra="Know your lane: a head injury needs a medical evaluation. Refer; don't diagnose."),
        dict(name="Workforce facilitator", where="Women's workforce program",
             facts=["Marisol has four years of experience as a home health aide and liked the work.",
                    "Her certification lapsed. A refresher course takes two weeks.",
                    "A home care agency is hiring for day shifts, with flexible hours."],
             need="To know when she's ready, and what has to be in place first."),
        dict(name="Team lead", where="Runs the planning meeting",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Before ranking anything, ask: “What does Marisol say matters most?”",
                    "Write the team's ranking on the worksheet."],
             extra="<strong>Only you know:</strong> Marisol told the shelter staff, “If I can't show my kids I can take care of us, what was the point of leaving?”"),
    ],
    steps=debrief_steps("read your card and decide which of Marisol's needs your role sees as most urgent.",
                        "share what you know, then rank Marisol's needs together: now, in 30 days, or later.",
                        "write Marisol's first week, and how the job search fits into it."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>Read the facts only you know</li>
    <li>Which need does your role see as most urgent?</li>
    <li>What does your role need from someone else?</li>
    <li>What might Marisol say about it?</li>
  </ul>""",
             notes="Walk the room. Check in with anyone who seems affected."),
        dict(eyebrow="Step 2 · team huddle", title="Rank the needs together",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role shares what it knows</li>
        <li>List every need on the worksheet</li>
        <li>Mark each one: now, 30 days, or later</li>
        <li>Find what unlocks other steps</li>
      </ol>
    </div>
    <div class="box c3"><h3>Remember</h3>Marisol wants a job now. How can the plan honor that and still keep her and her children safe?</div>
  </div>""",
             notes="Teams should find the chains: documents unlock benefits; child care unlocks work; safety planning is needed for the commute and the address question."),
        dict(eyebrow="Step 3 · plan and present", title="Marisol's first week",
             body="""  <ul>
    <li>Marisol's <strong>top three needs</strong>, in order, and why</li>
    <li>Her <strong>first week</strong>, day by day</li>
    <li>Where the <strong>job search</strong> fits, and what has to be in place first</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Each person says one sentence in role.</div>""",
             notes="Praise teams that build the job search into the plan rather than telling her to wait."),
    ],
    debrief=dict(questions=["What surprised you about how many needs were connected?",
                            "How did your team honor Marisol's urgency?",
                            "What would have happened if she started a job next week?",
                            "How are you feeling right now? What do you need?"],
                 notes="End with a grounding moment: one slow breath together, or name three things you can see. Check in with anyone who seemed affected before the break."),
    apply_line="Show what you learned, then make your own wellness plan.",
    own_words="“A sign that someone needs stabilization before a job search is …”",
    exit_ticket=["Name three stabilization needs that often come before a job search.",
                 "Name two of SAMHSA's six principles.",
                 "One thing on your wellness plan you'll do this week."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. Any learner can switch to the Team lead role. Post 988, the National Domestic Violence Hotline, and the DC Victim Hotline in the room (confirm numbers before class).",
    worksheet=dict(
        title="Stabilization ranking",
        instructions="List each of Marisol's needs. Mark when it must happen, who helps, and whether it must come before the job search.",
        columns=[("Need", 24), ("Now / 30 days / later", 18), ("Who helps", 20), ("Before the job search?", 0)],
        rows=7,
        first_col=["Safety (commute, address)", "Housing after the shelter", "Child care for Leo", "Sofia's school and sleep",
                   "Health and sleep", "Documents and bank account", "Income and benefits"],
        plan=[("Marisol's top three needs, in order, and why:", 3),
              ("Marisol's first week, day by day:", 3),
              ("Where the job search fits:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "What my role knows", "The need my role sees as most urgent"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.9, 1.3, 1.6, 1.9]),
    assignment=dict(
        intro="Capture your team's stabilization plan for Marisol, then make your own wellness plan.",
        parts=[
            dict(title="Your role's view", summary="What your role knew, the trauma at work, and the need your role saw first.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What did your role know about Marisol that the rest of the team didn't?", h=0.8),
                        dict(type="q", text="How might Marisol's trauma show up at a new job? Name one thing an employer could do to help.", h=0.9),
                        dict(type="q", text="Which of SAMHSA's six principles did your role need most, and why?", h=0.7)]),
            dict(title="Marisol's stabilization plan", summary="Her top needs in order, her first week, and where the job search fits.",
                 note="Use your team's worksheet from class.",
                 items=[dict(type="grid", text="Write Marisol's top three needs, in order.",
                             columns=["Need", "Why it comes here", "Who helps"], widths=[1.9, 3.0, 1.8], rows=3, h=0.6,
                             first_col=["1.", "2.", "3."]),
                        dict(type="q", text="Describe Marisol's first week, and where the job search fits in it.", h=1.1),
                        dict(type="q", text="Marisol said, “Just help me find a job.” Write what you would say to her.", h=0.9,
                             hint="(Honor her goal. Explain your thinking in plain words.)")]),
            dict(title="My wellness plan", summary="Your warning signs and plan for burnout and vicarious trauma, in your own words.",
                 items=[dict(type="grid", text="Fill in your wellness plan.",
                             columns=["", "My plan"], widths=[2.2, 4.5], rows=4, h=0.6,
                             first_col=["My early warning signs", "What helps me reset during the day",
                                        "Who I can talk to (at work and outside work)", "How I'll leave work at work"]),
                        dict(type="q", text="What helped you, or a woman close to you, feel steady during a hard time? How will that shape the way you support women like Marisol, and how will you protect yourself?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “A sign that someone needs stabilization before a job search is …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's view (Part 1)", "Clear facts, a realistic example of trauma at work, and a principle tied to the role.",
             "Answers are present but general.", "Missing, or labels Marisol."],
            ["Top three needs (Part 2 table)", "A logical, safety-first order with clear reasons.",
             "Order is partly explained.", "Missing, or ignores safety."],
            ["First week and response (Part 2, questions)", "A realistic week that honors her urgency, and a respectful response.",
             "Week or response is general.", "Missing, or dismisses her goal."],
            ["Wellness plan and reflection (Part 3)", "A specific plan. Reflection is thoughtful and in the learner's own words.",
             "Plan is general, or the reflection is short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's view and Marisol's plan.",
        reflection_title="My wellness plan",
        reflection_slide="Fill in your warning signs, what helps you reset, who you can talk to, and how you'll leave work at work. Then write about what helped you feel steady during a hard time.",
    ),
))

# =====================================================================================================
# MODULE 3 · Person-Centered Practices & Mobility Planning
# =====================================================================================================
MODULES[3] = finish(dict(
    num=3, hours=6,
    title="Person-Centered Practices &amp; Mobility Planning",
    short_title="Person-Centered Planning",
    slide_title_html="Person-Centered Practices<br>&amp; Mobility Planning",
    subtitle="Her goals, her strengths, her plan. Not the program's.",
    title_notes="Today lines up with the Person-Centered Practices core competency badge for DSP-I. Learners will practice a person-centered conversation and write an economic mobility plan. Tell them the plan they write today is designed to be used as a portfolio work sample.",
    lead="How to lead a conversation that surfaces a woman's own goals, strengths, and preferences, and turn it into a workforce readiness and economic mobility plan. You'll practice the conversation and write the plan as a team.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Person-centered thinking, goal conversations, economic mobility, and self-determination",
                   practice="Team roles: Tasha's mobility plan"),
    objectives=[
        "Lead a person-centered conversation that surfaces a participant's goals, strengths, and preferences.",
        "Write a workforce readiness and economic mobility plan with short- and long-term steps, including child care and rebuilding credit.",
        "Support choice and self-determination, even when you disagree.",
        "Document evidence of person-centered practice for a Core Competency E-Badge.",
    ],
    slide_objectives=[
        "Lead a person-centered goal conversation",
        "Write a mobility plan with short- and long-term steps",
        "Support her choices, even when you disagree",
        "Create evidence for the Person-Centered Practices badge",
    ],
    opening=dict(title="A plan someone made for you",
                 quote="Have you ever had a plan made for you, by a program, a court, a family member, that didn't fit your life? What was missing?",
                 notes="Most learners will have a story. Write what was missing: they didn't ask me, it didn't fit my schedule, it ignored my kids, it was their goal, not mine. Today is about doing the opposite."),
    learn_line="Planning with her, not for her.",
    learn=[
        dict(eyebrow="Person-centered thinking", title="What's important to her, and for her",
             body="""  <div class="cols">
    <div class="box c2"><h3>Important TO her</h3>What makes her life meaningful: her children, faith, independence, her own money, being respected</div>
    <div class="box c3"><h3>Important FOR her</h3>What keeps her safe and healthy: safety, health care, stable housing</div>
  </div>
  <p style="margin-top:18px">A good plan balances both. A plan that only covers what's important <em>for</em> her won't last.</p>""",
             notes="This distinction is central to person-centered practice in direct support. Ask: “What's important to you that a program never asked about?”"),
        dict(eyebrow="The conversation", title="Questions that open up her goals",
             body="""  <table class="tbl">
    <tr><th>Instead of…</th><th>Ask…</th></tr>
    <tr><td>“What job do you want?”</td><td>“What would a good life look like for you in two years?”</td></tr>
    <tr><td>“What are your barriers?”</td><td>“What's gotten in the way before? What helped?”</td></tr>
    <tr><td>“Do you have skills?”</td><td>“What are you proud of? What do people come to you for?”</td></tr>
    <tr><td>“You should apply here.”</td><td>“What do you think of this option? What would make it work for you?”</td></tr>
  </table>""",
             notes="Model a short conversation with a volunteer. Learners will practice with Tasha's card in Practice."),
        dict(eyebrow="Strengths", title="Survival skills are job skills",
             body="""  <table class="tbl">
    <tr><th>What she did to survive</th><th>The job skill</th></tr>
    <tr><td>Kept her kids fed on almost nothing</td><td>Budgeting, problem-solving</td></tr>
    <tr><td>Got through years of incarceration</td><td>Resilience, following procedures, adapting</td></tr>
    <tr><td>Planned a safe way out</td><td>Planning, risk assessment, discretion</td></tr>
    <tr><td>Helped other women inside or in the shelter</td><td>Peer support, leadership</td></tr>
  </table>""",
             notes="This connects to Job Search, where learners turn lived experience into a résumé. Ask each learner to name one survival skill of her own, privately or aloud."),
        dict(eyebrow="Economic mobility", title="More than a job",
             body="""  <div class="cols3">
    <div class="box c2"><h3>Income</h3>A job, then a better job</div>
    <div class="box c3"><h3>Credit and banking</h3>Her own account, repairing credit damaged by abuse</div>
    <div class="box c4"><h3>Housing</h3>A home she controls</div>
    <div class="box c1"><h3>Family</h3>Child care and time with her children</div>
    <div class="box c2"><h3>Training</h3>Credentials that lead to higher pay</div>
    <div class="box c3"><h3>Support</h3>People and community she can count on</div>
  </div>""",
             notes="Financial abuse often leaves women with ruined credit, debts in their name, and no savings. Point out free financial coaching and credit-building resources available in DC (confirm before class)."),
        dict(eyebrow="Self-determination", title="When you disagree",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Share information and options, clearly and honestly</li>
        <li>Ask what she thinks, and why</li>
        <li>Help her think through what could happen</li>
        <li>Respect her decision, and stay available</li>
      </ul>
    </div>
    <div class="box c1"><h3>The exception</h3>If someone is in immediate danger, follow your agency's safety procedures. Otherwise, it's her life and her choice.</div>
  </div>""",
             notes="For women who survived control, having someone respect her choice can be healing. Ask: “What's the difference between advice and control?”"),
        dict(eyebrow="Your E-Badge", title="Evidence of person-centered practice",
             body="""  <ul>
    <li>Today's mobility plan can be a <strong>work sample</strong> for your DSP-I portfolio</li>
    <li>Show her <strong>voice</strong>: her goals in her words</li>
    <li>Show her <strong>strengths</strong>, not just barriers</li>
    <li>Show <strong>her choices</strong> and how the plan respects them</li>
    <li>Never include real names or details. Use the fictional case.</li>
  </ul>""",
             notes="Explain how NADSP reviews badge evidence, and point learners to the E-Badge Academy applicant handbook. Confirm current requirements."),
    ],
    quick_check=dict(title="To her, or for her?",
                     items=["Going to her daughter's Sunday games",
                            "Getting her blood pressure checked",
                            "Working somewhere she isn't treated like her record",
                            "A safety plan for the commute",
                            "Having her own bank account"],
                     notes="Answers: 1) To. 2) For. 3) To. 4) For. 5) Both. Many items are both. The point is to ask about both."),
    practice_line="Step into a role, hold a goal conversation, and write a woman's mobility plan as a team.",
    practice_notes="Hand out the in-class packet. One learner plays Tasha and reveals her goals only through good, open questions. The facilitator leads the conversation in front of the team.",
    activity_title="Team roles: Tasha's mobility plan",
    team_notes_title="Tasha's Mobility Plan",
    case=dict(
        name="Tasha",
        page_intro="<strong>Tasha Greene, 39</strong> (fictional), came home three months ago after six years in federal prison. Her 15-year-old daughter lives with Tasha's mother. Tasha is staying in a women's reentry house and has a part-time job at a warehouse.",
        page_how="One person plays Tasha, and her card has goals she shares only if asked the right way. The facilitator leads a goal conversation while the team listens. Then the team writes Tasha's mobility plan together, with each role adding what it knows.",
        slide_title="Meet Tasha",
        slide_intro="<strong>Tasha Greene, 39</strong>, came home three months ago after six years in federal prison.",
        bullets=["Lives in a women's reentry house",
                 "Part-time job at a warehouse, nights",
                 "Her daughter, 15, lives with Tasha's mother",
                 "Everyone has an opinion about what she should do next"],
        quote="“My parole officer has a plan. My mother has a plan. The program has a plan. Nobody asked me.”",
        quote_label="What Tasha says",
        slide_notes="Tasha's quote is today's lesson. The team's job is to find her plan, not give her another one.",
        packet_text="<strong>Tasha Greene, 39</strong>, came home three months ago after six years in federal prison. She lives in a women's reentry house and works part-time nights at a warehouse. Her daughter, Jada (15), lives with Tasha's mother. Tasha's supervision officer, her mother, and the reentry program each have ideas about what she should do next. Your team's job is to find out what Tasha wants, and plan with her.",
    ),
    roles_title="Five supports and Tasha",
    roles_small="Tasha shares her goals only through open questions and listening. Everyone else adds what they know.",
    roles_notes="Give the Tasha card to a learner who is comfortable role-playing. Tell her to answer closed questions briefly and open up only when the facilitator really listens.",
    roles=[
        dict(name="Tasha", where="The participant",
             facts_label="Share only if asked an open question or listened to well:",
             facts=["Inside, you trained as a peer mentor and earned a certificate in medical billing.",
                    "You want to work in medical billing, on days, so you can be home when Jada gets out of school.",
                    "Your big goal: an apartment where Jada can live with you, within a year.",
                    "You're scared to tell anyone about your credit. Your ex opened cards in your name."],
             need="If the facilitator tells you what to do, say “Okay,” and shut down.", need_label="How to play it:"),
        dict(name="Workforce facilitator", where="Leads the goal conversation",
             facts_label="Your goals for the conversation (10 minutes):",
             facts=["Find out what a good life looks like for Tasha in one and two years.",
                    "Find her strengths and what's important to her.",
                    "Use open questions. Don't suggest jobs until she has told you her goals.",
                    "End by summarizing her goals in her words."]),
        dict(name="Reentry navigator", where="Women's reentry program",
             facts=["Tasha's supervision requires her to keep a job and stay in the reentry house for three more months.",
                    "She needs approval from her supervision officer to move or change jobs.",
                    "Some employers in DC must wait until after a conditional offer to ask about criminal records under DC's fair chance hiring law (confirm details before class)."],
             need="A plan that keeps her in good standing with supervision."),
        dict(name="Training coordinator", where="Community college workforce program",
             facts=["A 12-week medical billing and coding course starts next month, on weekday evenings.",
                    "Tuition can be covered by a workforce grant if she enrolls through the American Job Center.",
                    "Graduates often start at entry-level medical office jobs with day schedules."],
             need="To know if evening classes fit her life."),
        dict(name="Family support worker", where="Works with Tasha's family",
             facts=["Jada wants to live with her mom, but she's nervous.",
                    "Tasha's mother is tired and has health problems. She wants Tasha to take over soon.",
                    "A family counselor is available for reunification support, if Tasha and Jada want it."],
             need="A timeline for Jada that's realistic for everyone."),
        dict(name="Team lead", where="Keeps time and writes the plan",
             facts_label="Your job:",
             facts=["Keep time: 10 minutes for the goal conversation, then the team plans.",
                    "Write the mobility plan on the worksheet, in Tasha's words when you can.",
                    "After the conversation, ask Tasha: “Does this plan sound like yours?”"],
             extra="<strong>Only you know:</strong> a free financial coaching program for women offers credit repair help, including disputing accounts opened by an abuser."),
    ],
    steps=[
        dict(label="Read your card", desc="get ready for the conversation. Tasha and the facilitator prepare. Everyone else reads what they know."),
        dict(label="Goal conversation and huddle", desc="the facilitator and Tasha talk for 10 minutes while the team listens. Then the team plans together."),
        dict(label="Plan and present", desc="write Tasha's mobility plan, check it with Tasha, and present."),
        dict(label="Debrief", desc="step out of role and talk about what it's like to be planned for, or planned with."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · read your card", title="Get ready",
             body="""  <ul>
    <li><strong>Tasha:</strong> read your card. Open up only to open questions.</li>
    <li><strong>Facilitator:</strong> plan your first three open questions</li>
    <li><strong>Everyone else:</strong> read what you know. Listen for what fits her goals.</li>
  </ul>""",
             notes="Check that each facilitator has open questions ready."),
        dict(eyebrow="Step 2 · goal conversation and huddle", title="Listen first, then plan",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Goal conversation: 10 minutes. The team listens and takes notes.</li>
        <li>Huddle: each role adds what it knows</li>
        <li>Find what fits her goals, and what's in the way</li>
        <li>Start the plan, one area at a time</li>
      </ol>
    </div>
    <div class="box c3"><h3>Listen for</h3>Medical billing. Days. Jada. An apartment. Credit. Did your facilitator find all five?</div>
  </div>""",
             notes="After the conversation, ask each team how many of Tasha's hidden goals came out. Let the facilitator try again for 3 minutes if key goals are missing."),
        dict(eyebrow="Step 3 · plan and present", title="Tasha's mobility plan",
             body="""  <ul>
    <li>Her goals <strong>in her words</strong></li>
    <li>Steps for <strong>30 days, 6 months, and 1 year</strong></li>
    <li>How the plan fits <strong>supervision, Jada, and her credit</strong></li>
    <li>Ask Tasha: <strong>does this sound like yours?</strong></li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Tasha says whether it's her plan.</div>""",
             notes="Tasha's verdict is the best test of person-centered practice."),
    ],
    debrief=dict(questions=["Tasha: when did you start opening up?",
                            "Facilitators: what was hardest about not giving advice?",
                            "What was important TO Tasha? What was important FOR her?",
                            "Have you ever had a plan made for you? How was today different?"],
                 notes="Connect back to the opening. The difference between today's plan and the plans learners described is who wrote it."),
    apply_line="Show what you learned, then connect it to your own goals.",
    own_words="“I kept the plan person-centered by …”",
    exit_ticket=["What's the difference between important TO her and important FOR her?",
                 "Write one open question that helps a woman talk about her goals.",
                 "One survival skill of yours that is also a job skill."],
    packet_instructions="Print one packet per team. Cut the cards apart. Give the Tasha card to a learner who is comfortable role-playing, and the Workforce facilitator card to someone who wants to practice leading the conversation.",
    worksheet=dict(
        title="Mobility plan",
        instructions="Write Tasha's goals in her words, then the steps for each area.",
        columns=[("Area", 18), ("Her goal, in her words", 24), ("30 days", 19), ("6 months", 19), ("1 year", 0)],
        rows=6,
        first_col=["Work and career", "Training", "Income, banking, and credit", "Housing", "Jada and family", "Support and well-being"],
        plan=[("Tasha's strengths, and how the plan uses them:", 2),
              ("How the plan fits supervision:", 1),
              ("Tasha's verdict: is this her plan?", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "What my role knows", "How it fits Tasha's goals"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.3, 1.6, 1.25, 1.25, 1.3]),
    assignment=dict(
        intro="Capture Tasha's mobility plan as a work sample of person-centered practice, then connect it to your own goals.",
        parts=[
            dict(title="The goal conversation", summary="What opened Tasha up, and how your role supported her plan.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="Write two open questions from the goal conversation and what Tasha shared because of them.", h=0.9),
                        dict(type="q", text="Name something important TO Tasha and something important FOR her.", h=0.7),
                        dict(type="q", text="Was there a moment where someone wanted to decide for Tasha? How should it have been handled?", h=0.8)]),
            dict(title="Tasha's mobility plan", summary="Her goals and steps across six areas. Can be used as a DSP-I work sample.",
                 note=PORTFOLIO,
                 items=[dict(type="grid", text="Write Tasha's mobility plan.",
                             columns=["Area", "Her goal", "30 days", "6 months", "1 year"],
                             widths=[1.3, 1.6, 1.25, 1.25, 1.3], rows=6, h=0.6,
                             first_col=["Work", "Training", "Money and credit", "Housing", "Jada and family", "Support"]),
                        dict(type="q", text="Explain how this plan shows person-centered practice: her voice, her strengths, and her choices.", h=1.1)]),
            dict(title="My own mobility", summary="Your own goals and strengths, in your own words.",
                 items=[dict(type="grid", text="Name three survival skills from your own life that are also job skills.",
                             columns=["What I did", "The job skill"], widths=[3.35, 3.35], rows=3, h=0.5, first_col=["1.", "2.", "3."]),
                        dict(type="q", text="What would a good life look like for you in two years? What's important to you, and how will this work help you get there?",
                             h=2.0, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “I kept the plan person-centered by …”", h=0.8)]),
        ],
        rubric_full=[
            ["Goal conversation (Part 1)", "Real open questions with results, and a clear to/for distinction.",
             "Examples are general.", "Missing, or closed questions only."],
            ["Mobility plan (Part 2 table)", "Goals in her words, with realistic steps in every area.",
             "Some areas or steps missing.", "Few areas complete."],
            ["Person-centered evidence (Part 2, question)", "Clearly shows her voice, strengths, and choices.",
             "Partly explained.", "Missing."],
            ["My own mobility (Part 3)", "Specific skills and goals. Thoughtful and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="the goal conversation and Tasha's mobility plan.",
        reflection_title="My own mobility",
        reflection_slide="Name three survival skills from your own life that are also job skills. Then write about what a good life looks like for you in two years.",
    ),
))

# =====================================================================================================
# MODULE 4 · Communication & Group Facilitation
# =====================================================================================================
MODULES[4] = finish(dict(
    num=4, hours=6,
    title="Communication &amp; Group Facilitation",
    short_title="Group Facilitation",
    slide_title_html="Communication &amp;<br>Group Facilitation",
    subtitle="Leading groups where women feel safe enough to speak, and strong enough to grow.",
    title_notes="Today learners will co-facilitate a real segment of a women's workforce readiness group. This builds toward the capstone, where they design and lead a full session. Expect nerves. Many learners have sat in groups. Few have led one.",
    lead="The listening skills that build trust one-on-one, and the facilitation skills that make a women's group feel safe. You'll co-facilitate a segment of a workforce readiness group, handle common challenges, and give each other feedback.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Active listening, plain language, group agreements, facilitation skills, and disclosure",
                   practice="Team roles: co-facilitate the Pathways Circle"),
    objectives=[
        "Use active listening, open questions, and plain language.",
        "Set group agreements and manage participation in a women's workforce readiness group.",
        "Respond to disclosure in a group respectfully and safely.",
        "Adapt communication for culture, literacy, and disability.",
    ],
    slide_objectives=[
        "Listen actively and speak in plain language",
        "Set group agreements and manage participation",
        "Respond safely when a woman discloses in group",
        "Adapt for culture, literacy, and disability",
    ],
    opening=dict(title="A group that worked",
                 quote="Think of a group you were part of, a class, a support group, a church circle, a team, where you felt safe to speak. What did the leader do?",
                 notes="Write what learners name: she knew our names, she set rules together with us, she didn't let one person take over, she didn't force anyone to share, she started and ended on time. That's the facilitation checklist."),
    learn_line="Listening, leading, and keeping the group safe.",
    learn=[
        dict(eyebrow="One-on-one", title="Listening that builds trust",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Open questions:</strong> “What was that like for you?”</li>
        <li><strong>Reflections:</strong> “You're proud of how far you've come.”</li>
        <li><strong>Affirmations:</strong> specific and true. “You showed up every week.”</li>
        <li><strong>Summaries:</strong> “So far I've heard… Did I get that right?”</li>
      </ul>
    </div>
    <div class="box c2"><h3>Plain language</h3>Short sentences. Everyday words. No program jargon. Check with teach-back: “Tell me in your words what we'll do next.”</div>
  </div>""",
             notes="These are the OARS skills from motivational interviewing. Practice one reflection as a whole class."),
        dict(eyebrow="Group agreements", title="Build them together",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>What's shared here stays here</li>
        <li>Speak from your own experience</li>
        <li>You can pass. Nobody has to share her story.</li>
        <li>One person speaks at a time</li>
        <li>Phones on silent; step out if you need to</li>
      </ul>
    </div>
    <div class="box c3"><h3>Why build them together?</h3>Women follow agreements they made. Ask: “What do you need from this group to feel safe?” Write their words.</div>
  </div>""",
             notes="Be honest about limits: facilitators can't guarantee confidentiality among participants. Say: “I'll keep what you share private, except for safety. I'm asking everyone to do the same.”"),
        dict(eyebrow="Facilitation skills", title="Managing participation",
             body="""  <table class="tbl">
    <tr><th>If…</th><th>Try…</th></tr>
    <tr><td><strong>One woman dominates</strong></td><td>“Thank you. Let's hear from someone who hasn't spoken yet.” Use rounds or pairs.</td></tr>
    <tr><td><strong>Someone is silent</strong></td><td>Pairs first, then share. Never force it. Check in privately after.</td></tr>
    <tr><td><strong>The group goes off topic</strong></td><td>“That's important. Let's put it in the parking lot and come back to it.”</td></tr>
    <tr><td><strong>Conflict</strong></td><td>Calm voice, point back to the agreements, and talk privately at the break.</td></tr>
  </table>""",
             notes="Each of these challenges is on a role card in Practice."),
        dict(eyebrow="Disclosure", title="When a woman shares something painful",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Thank her</strong> for trusting the group</li>
        <li><strong>Don't dig</strong> for details in front of everyone</li>
        <li><strong>Protect her and the group:</strong> gently move on</li>
        <li><strong>Check in privately</strong> at the break</li>
        <li><strong>Safety first:</strong> if she's in danger now, follow agency procedures</li>
      </ol>
    </div>
    <div class="box c1"><h3>Try</h3>“Thank you for sharing that. It took courage. I'd like to check in with you at the break. For now, let's take a breath together.”</div>
  </div>""",
             notes="Practice the script out loud. Disclosure in a group can affect other survivors in the room. The facilitator's job is to keep the whole group safe."),
        dict(eyebrow="Adapting", title="Every woman in the room",
             body="""  <table class="tbl">
    <tr><th>If a participant…</th><th>Try…</th></tr>
    <tr><td><strong>Speaks another language</strong></td><td>A trained interpreter, translated handouts, pairs with a bilingual peer if she agrees</td></tr>
    <tr><td><strong>Has limited reading</strong></td><td>Read handouts aloud, use pictures, never call on someone to read</td></tr>
    <tr><td><strong>Has a disability</strong></td><td>Ask what works best. Accessible room, breaks, and materials.</td></tr>
    <tr><td><strong>Has a different culture or faith</strong></td><td>Ask, don't assume. Respect holidays, dress, and family roles.</td></tr>
  </table>""",
             notes="Ask: “What would have made a group easier for you or someone you know?”"),
        dict(eyebrow="Running a session", title="A simple session plan",
             body="""  <ol>
    <li><strong>Welcome</strong> and check-in round (one word or “pass”)</li>
    <li><strong>Agreements</strong> reminder</li>
    <li><strong>Activity:</strong> one topic, one skill</li>
    <li><strong>Pairs or small groups</strong> to practice</li>
    <li><strong>Share back</strong> and summarize</li>
    <li><strong>Close:</strong> one takeaway, and what's next</li>
  </ol>""",
             notes="This is the structure teams will use in Practice and in the capstone."),
    ],
    quick_check=dict(title="What would you say?",
                     items=["A participant keeps interrupting others.",
                            "A woman starts crying while talking about her ex.",
                            "Two participants start arguing about whose turn it is.",
                            "Nobody answers your question."],
                     notes="Have learners say their response out loud. Sample answers: redirect warmly to others; thank her, offer tissues, check in at the break; point to the agreements; turn it into a pairs activity."),
    practice_line="Co-facilitate a segment of a women's workforce readiness group, and handle what comes up.",
    practice_notes="Each team runs the Pathways Circle three times, rotating co-facilitators so at least four people lead. Participants play their cards. The observer gives feedback after each round.",
    activity_title="Team roles: co-facilitate the Pathways Circle",
    team_notes_title="Co-Facilitating the Pathways Circle",
    case=dict(
        name="the Pathways Circle",
        fiction="The Pathways Circle and every participant in it are fictional.",
        page_intro="The <strong>Pathways Circle</strong> (fictional) is a weekly workforce readiness group for women survivors. Today's 15-minute segment: <em>“Talking about gaps in your work history.”</em>",
        page_how="Two people co-facilitate while the others play participants with challenges on their cards. After each round, the observer gives feedback and the roles rotate, so at least four people get to lead.",
        slide_title="The Pathways Circle",
        slide_intro="A weekly workforce readiness group for women survivors. Today's 15-minute segment:",
        bullets=["<strong>“Talking about gaps in your work history”</strong>",
                 "Two co-facilitators lead",
                 "Participants play the cards they're dealt",
                 "Three rounds, rotating leaders"],
        quote="“Every interview, they ask about the gap. What am I supposed to say? That I was locked up? That he wouldn't let me work?”",
        quote_label="What one participant says",
        slide_notes="This quote opens the segment. The topic is real and charged: every participant has a reason for a gap. The co-facilitators' job is to keep it safe and practical.",
        packet_text="The <strong>Pathways Circle</strong> is a weekly workforce readiness group for women survivors. Today's 15-minute segment is “Talking about gaps in your work history.” Two co-facilitators lead. The rest of the team plays participants. Each participant card has a challenge to bring to the group. After each round, the observer gives feedback, and new co-facilitators take over.",
    ),
    roles_title="Two leads, four participants",
    roles_small="Rotate after each round so at least four people co-facilitate.",
    roles_notes="Participants: play your card honestly, not to make it impossible. Co-facilitators use the session plan.",
    roles=[
        dict(name="Co-facilitator A", where="Opens and leads the activity",
             facts_label="Your part:",
             facts=["Welcome, check-in round, and agreements reminder (4 minutes).",
                    "Introduce the topic and ask one open question to start.",
                    "Lead the pairs activity: practice a one-sentence answer about a work gap."]),
        dict(name="Co-facilitator B", where="Supports and closes",
             facts_label="Your part:",
             facts=["Watch the group. Step in when someone needs support or the group goes off track.",
                    "Lead the share-back and summary.",
                    "Close: one takeaway from each woman, and what's next week."]),
        dict(name="Participant · Denise", where="Talks a lot",
             facts_label="Your challenge:",
             facts=["You answer every question first and tell long stories.",
                    "You mean well. You want to help the younger women.",
                    "Stop if a co-facilitator redirects you kindly. If they're harsh, get quiet and hurt."]),
        dict(name="Participant · Ama", where="Quiet, English is her second language",
             facts_label="Your challenge:",
             facts=["You understand most English but are afraid to speak in a group.",
                    "You have a gap because your employer took your passport and made you work without pay for two years.",
                    "You'll speak in a pair, but not to the whole group, unless invited gently."]),
        dict(name="Participant · Rochelle", where="Discloses",
             facts_label="Your challenge:",
             facts=["Halfway through, you say, “My gap is because he put me in the hospital. Twice.” Your voice shakes.",
                    "If the facilitators handle it with care, you're okay and stay.",
                    "If they ask for details or ignore it, you leave the room."]),
        dict(name="Observer and timekeeper", where="Gives feedback each round",
             facts_label="Your job:",
             facts=["Keep time: 15 minutes per round, then 5 minutes of feedback.",
                    "Tally: open questions, reflections, inviting quiet voices, redirecting, handling disclosure.",
                    "Give one thing that worked and one thing to try."],
             extra="Rotate: after each round, two new people become co-facilitators."),
    ],
    steps=[
        dict(label="Prepare", desc="co-facilitators plan their opening and question. Participants read their cards."),
        dict(label="Three rounds", desc="run the 15-minute segment, get feedback, and rotate co-facilitators."),
        dict(label="Plan and present", desc="share what worked for each challenge and your best one-sentence answer about a work gap."),
        dict(label="Debrief", desc="step out of role and talk about what it was like to lead, and to be led."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · prepare", title="Get ready to lead",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Co-facilitators:</strong> plan your welcome, agreements, and first open question</li>
        <li><strong>Participants:</strong> read your card</li>
        <li><strong>Observer:</strong> set up the tally</li>
      </ul>
    </div>
    <div class="box c3"><h3>The session plan</h3>Welcome · agreements · activity · pairs · share back · close</div>
  </div>""",
             notes="Make sure co-facilitators divide the parts before round 1."),
        dict(eyebrow="Step 2 · three rounds", title="Lead, get feedback, rotate",
             body="""  <table class="tbl">
    <tr><th>Each round</th><th>Time</th></tr>
    <tr><td><strong>Run the segment:</strong> co-facilitators lead, participants play their cards</td><td>15 min</td></tr>
    <tr><td><strong>Feedback:</strong> observer first, then participants, then co-facilitators</td><td>5 min</td></tr>
    <tr><td><strong>Rotate:</strong> two new co-facilitators</td><td>1 min</td></tr>
  </table>""",
             notes="Walk between teams. Watch especially how co-facilitators handle Rochelle's disclosure. Step in if a role-play becomes too real for anyone."),
        dict(eyebrow="Step 3 · plan and present", title="What worked?",
             body="""  <ul>
    <li>What worked with <strong>Denise, Ama, and Rochelle</strong></li>
    <li>Your team's best <strong>one-sentence answer</strong> about a work gap</li>
    <li>One thing every facilitator should <strong>always do</strong></li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes.</div>""",
             notes="Collect the best one-sentence answers on the board. They're useful for Job Search too."),
    ],
    debrief=dict(questions=["What was it like to lead?",
                            "Participants: when did you feel safe? When didn't you?",
                            "How did your team handle Rochelle's disclosure?",
                            "What will you take into your capstone workshop?"],
                 notes="Many learners will say leading was harder than it looked. Connect it to the capstone, where they'll design and lead a full session."),
    apply_line="Show what you learned, then reflect on how you lead.",
    own_words="“When the group got off track, I …”",
    exit_ticket=["Name two group agreements you'd always use.",
                 "What would you say if a woman discloses abuse in group?",
                 "One thing you'll practice before your capstone."],
    packet_instructions="Print one packet per team. Cut the cards apart. Rotate co-facilitators after each round so at least four learners lead. Watch the disclosure role-play closely and step in if needed.",
    worksheet=dict(
        title="Facilitation feedback",
        instructions="The observer makes a tally mark for each skill in each round, then writes one thing that worked.",
        columns=[("Skill", 34), ("Round 1", 22), ("Round 2", 22), ("Round 3", 0)],
        rows=7,
        first_col=["Open question", "Reflection or affirmation", "Invited a quiet voice", "Redirected kindly",
                   "Handled disclosure with care", "Used plain language", "One thing that worked"],
        plan=[("What worked with Denise, Ama, and Rochelle:", 3),
              ("Our best one-sentence answer about a work gap:", 1),
              ("One thing every facilitator should always do:", 1)],
    ),
    team_notes=dict(step1_columns=["Card", "My part or challenge", "What I'll watch for"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[2.3, 1.45, 1.5, 1.45]),
    assignment=dict(
        intro="Capture what you learned as a co-facilitator and participant, then reflect on how you lead.",
        parts=[
            dict(title="Your round", summary="What you did as co-facilitator, and the feedback you got.",
                 note="Answer about the round when you co-facilitated. If you didn't lead, answer about the round you observed.",
                 items=[dict(type="roles"),
                        dict(type="q", text="Describe one moment when you used a facilitation skill. What did you say, and what happened?", h=0.9),
                        dict(type="q", text="What feedback did you get? What will you try next time?", h=0.8)]),
            dict(title="Handling the challenges", summary="How to handle each participant challenge, and disclosure.",
                 note="Use your team's feedback sheet from class.",
                 items=[dict(type="grid", text="For each participant, write what worked.",
                             columns=["Participant", "The challenge", "What worked"], widths=[1.5, 2.2, 3.0], rows=3, h=0.7,
                             first_col=["Denise", "Ama", "Rochelle"]),
                        dict(type="q", text="Write the exact words you'd use when a woman discloses abuse in group.", h=0.9),
                        dict(type="q", text="Write three group agreements you'd use, and why each one matters for women survivors.", h=0.9)]),
            dict(title="How I lead", summary="Your strengths and growth as a facilitator, in your own words.",
                 items=[dict(type="q", text="Think of a group where you felt safe, or unsafe. How will that experience shape the way you lead groups of women?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “When the group got off track, I …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your round (Part 1)", "A specific moment with a clear skill and result, and a next step.",
             "General description.", "Missing."],
            ["Participant challenges (Part 2 table)", "A fitting, respectful response for each participant.",
             "Two complete, or responses are vague.", "Few responses."],
            ["Disclosure and agreements (Part 2, questions)", "Safe, caring disclosure response and three well-reasoned agreements.",
             "Partly safe, or reasons are thin.", "Unsafe response (asks for details), or missing."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your round and the challenges.",
        reflection_title="How I lead",
        reflection_slide="Think of a group where you felt safe, or unsafe. How will that experience shape the way you lead groups of women?",
    ),
))

# =====================================================================================================
# MODULE 5 · Crisis Prevention & Behavior Support
# =====================================================================================================
MODULES[5] = finish(dict(
    num=5, hours=7,
    title="Crisis Prevention &amp; Behavior Support",
    short_title="Crisis Prevention",
    slide_title_html="Crisis Prevention<br>&amp; Behavior Support",
    subtitle="Seeing it coming, calming it down, and supporting her after.",
    title_notes="Today lines up with the Crisis Prevention and Intervention core competency badge for DSP-I. Practice involves role-playing escalation. Set ground rules: no physical contact, anyone can call “pause” at any time, and the instructor will stop any role-play that becomes too real. The debrief forms learners complete are designed to be portfolio work samples. Plan a stretch break inside the Learn block.",
    lead="How to notice early warning signs, calm a situation before it becomes a crisis, and support a woman afterward. You'll learn positive behavior support and practice de-escalation in three scenarios at a job training site.",
    flow_text=dict(open="Welcome, ground rules, and opening circle",
                   learn="Why crises happen, warning signs, de-escalation, positive behavior support, and when to get help",
                   practice="Team roles: three scenarios at a job training site"),
    objectives=[
        "Recognize early warning signs of escalation.",
        "Use verbal de-escalation techniques in role-play.",
        "Explain positive behavior support and why it replaces punishment.",
        "Know when and how to escalate to a supervisor, crisis line, or emergency services.",
    ],
    slide_objectives=[
        "Spot the early warning signs",
        "Calm things down with words",
        "Use positive behavior support",
        "Know when to get more help",
    ],
    opening=dict(title="What calmed you down?",
                 quote="Think of a time you were really upset, scared, or angry. What did someone do that made it worse? What made it better?",
                 notes="Write two columns: made it worse (yelling, threats, “calm down,” crowding, being ignored) and made it better (calm voice, space, being heard, a choice, time). This is de-escalation in learners' own words."),
    learn_line="Prevent, calm, support, and know when to call for help.",
    learn=[
        dict(eyebrow="Why it happens", title="Behavior is communication",
             body="""  <div class="cols">
    <div>
      <p>Behavior that looks like “acting out” is often a woman trying to meet a need or protect herself:</p>
      <ul>
        <li>Feeling unsafe or threatened</li>
        <li>Feeling controlled, disrespected, or ignored</li>
        <li>Exhaustion, hunger, pain, or fear about her children</li>
        <li>A trigger that brings back past trauma</li>
      </ul>
    </div>
    <div class="box c2"><h3>Ask</h3>Not “What's wrong with her?” but “What does she need right now?”</div>
  </div>""",
             notes="Connect to Module 2. For survivors, a supervisor's raised voice or a locked door can feel like danger."),
        dict(eyebrow="Early warning signs", title="See it coming",
             body="""  <table class="tbl">
    <tr><th>Stage</th><th>What you might see</th><th>What helps</th></tr>
    <tr><td><strong>Calm</strong></td><td>Engaged, relaxed</td><td>Build trust and routines</td></tr>
    <tr><td><strong>Triggered</strong></td><td>Tense face, quiet, pacing, checking her phone</td><td>Check in privately: “You seem stressed. What's going on?”</td></tr>
    <tr><td><strong>Escalating</strong></td><td>Louder voice, arguing, swearing</td><td>De-escalate: calm voice, space, choices</td></tr>
    <tr><td><strong>Crisis</strong></td><td>Threats, throwing things, running out</td><td>Safety first. Get help.</td></tr>
    <tr><td><strong>Recovery</strong></td><td>Tired, embarrassed, quiet</td><td>Support, no shaming. Talk later.</td></tr>
  </table>""",
             notes="The earlier you notice, the easier it is. Most crises can be prevented at the triggered stage."),
        dict(eyebrow="De-escalation", title="Calm it down",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Check safety:</strong> your exit, her exit, and others nearby</li>
        <li><strong>Give space:</strong> at least two arm lengths. Stand at an angle.</li>
        <li><strong>Lower your voice</strong> and slow down</li>
        <li><strong>Name the feeling:</strong> “You're really upset. I get it.”</li>
        <li><strong>Offer choices:</strong> “Do you want to sit here or step outside with me?”</li>
        <li><strong>Don't argue, threaten, or touch</strong></li>
      </ol>
    </div>
    <div class="box c1"><h3>Never say</h3>“Calm down.”<br>“You need to…”<br>“If you don't stop, I'll…”</div>
  </div>""",
             notes="Practice the phrases out loud as a class. Ask learners to add phrases that worked for them."),
        dict(eyebrow="Positive behavior support", title="Support, not punishment",
             body="""  <table class="tbl">
    <tr><th>Punishment approach</th><th>Positive behavior support</th></tr>
    <tr><td>“She's kicked out of the program for yelling.”</td><td>“What triggered it? How can we prevent it?”</td></tr>
    <tr><td>Focuses on stopping the behavior</td><td>Focuses on the need behind it</td></tr>
    <tr><td>Rules enforced the same way, no matter what</td><td>Changes the environment and teaches new skills</td></tr>
    <tr><td>Often re-traumatizes</td><td>Builds safety and trust</td></tr>
  </table>""",
             notes="Positive behavior support doesn't mean no limits. It means limits with understanding, and plans to prevent the next crisis."),
        dict(eyebrow="When to get help", title="Know when it's beyond you",
             body="""  <table class="tbl">
    <tr><th>Situation</th><th>Call</th></tr>
    <tr><td><strong>Anyone is in immediate danger</strong></td><td>911, and follow your agency's emergency plan</td></tr>
    <tr><td><strong>She talks about ending her life</strong></td><td>Stay with her. Call or text 988. Get your supervisor.</td></tr>
    <tr><td><strong>An abuser shows up</strong></td><td>Agency safety plan, security, and 911 if needed</td></tr>
    <tr><td><strong>You're unsure</strong></td><td>Your supervisor, right away</td></tr>
  </table>""",
             notes="Make sure learners know never to stay in an unsafe situation to finish a conversation. Confirm any DC crisis lines before class."),
        dict(eyebrow="After a crisis", title="Recovery and debrief",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Check on her:</strong> safety, needs, and how she's feeling</li>
        <li><strong>No shaming.</strong> Talk about it when she's calm.</li>
        <li><strong>Plan together:</strong> what helps next time?</li>
        <li><strong>Check on yourself</strong> and your coworkers</li>
        <li><strong>Document</strong> facts, not labels, the same day</li>
      </ul>
    </div>
    <div class="box c3"><h3>Debrief form</h3>Today you'll complete a debrief form for each scenario. They're designed to be portfolio work samples.</div>
  </div>""",
             notes="Show the debrief form on the worksheet. Take a stretch break before Practice."),
    ],
    quick_check=dict(title="Better or worse?",
                     items=["“Calm down!”",
                            "“You're really frustrated. That makes sense.”",
                            "Standing close and blocking the door",
                            "“Do you want to talk here or step outside with me?”",
                            "“If you keep yelling, you're out of the program.”"],
                     notes="Worse: 1, 3, 5. Better: 2, 4."),
    practice_line="Step into a role and practice de-escalation in three scenarios at a job training site.",
    practice_notes="Ground rules: no physical contact; anyone can call “pause” at any time. Rotate roles so three different learners practice de-escalating. Complete a debrief form after each scenario.",
    activity_title="Team roles: three scenarios at Bright Start Training",
    team_notes_title="Three Scenarios at Bright Start Training",
    case=dict(
        name="Brianna",
        fiction="Brianna, the training site, and every person in the scenarios are fictional.",
        page_intro="<strong>Brianna, 24</strong> (fictional), is in week three of a culinary job training program for women. She's talented, and she has had a hard week. Today, three things happen.",
        page_how="Your team acts out three scenarios. Each time, a different person plays the facilitator who de-escalates. Brianna's card tells her what she's feeling and what calms her. After each scenario, the team completes a debrief form.",
        slide_title="Meet Brianna",
        slide_intro="<strong>Brianna, 24</strong>, is in week three of a culinary job training program for women.",
        bullets=["Scenario 1: the chef criticizes her in front of everyone",
                 "Scenario 2: she gets a text from her ex during class",
                 "Scenario 3: she's told she'll lose her stipend for being late",
                 "A different person de-escalates each time"],
        quote="“Everybody is always telling me to calm down. Nobody asks why I'm upset.”",
        quote_label="What Brianna says",
        slide_notes="Brianna's quote is the lesson. In each scenario, the facilitator should find out why before trying to fix anything.",
        packet_text="<strong>Brianna, 24</strong>, is in week three of a culinary job training program for women. She is one of the most talented students. She left a violent relationship four months ago and lives with her aunt. She has a 2-year-old son. This week, her son was sick, she's slept very little, and her ex has been texting her. Today, three things happen at the training site.",
    ),
    roles_title="Brianna, the facilitator, and the people around her",
    roles_small="Rotate the facilitator role each scenario. Brianna can be the same person or rotate.",
    roles_notes="Give the Brianna card to a learner who is comfortable playing strong emotion. Remind everyone of the pause rule.",
    roles=[
        dict(name="Brianna", where="Training participant",
             facts_label="What you're feeling:",
             facts=["Scenario 1: the chef says loudly, “Are you even trying?” You feel humiliated. You slam a pan down.",
                    "Scenario 2: your ex texts, “I know where your aunt lives.” You stop working and start pacing and crying.",
                    "Scenario 3: you're told you'll lose this week's $150 stipend for being late twice. You yell, “I was at the clinic with my son!”"],
             need="Calm down when the facilitator gives you space, names your feeling, and offers a choice. Get louder if they argue or crowd you.",
             need_label="How to play it:"),
        dict(name="Facilitator (rotates)", where="Program staff, de-escalates",
             facts_label="Your goals each scenario (5 minutes):",
             facts=["Notice the warning signs and check safety.",
                    "Lower your voice, give space, name the feeling.",
                    "Offer a choice. Find out what she needs.",
                    "Know when to get help: Scenario 2 needs a safety response."]),
        dict(name="Chef instructor", where="Training kitchen",
             facts=["Scenario 1: you're under pressure. A catering order is due in two hours.",
                    "You think Brianna is one of your best students, but you never tell her.",
                    "After she calms down, you can apologize for calling her out in front of the class, if the facilitator helps."]),
        dict(name="Classmate", where="Another participant",
             facts=["You're friends with Brianna.",
                    "In Scenario 2, you know her ex has hurt her before. You want to help but don't know how.",
                    "In Scenario 3, you start to join in, yelling that the stipend rule is unfair."],
             need="Calm down if the facilitator speaks to you calmly and gives you a job, like getting water."),
        dict(name="Program manager", where="Sets the stipend rules",
             facts=["Scenario 3: the rule says two late arrivals means losing the week's stipend.",
                    "You do have the power to excuse lateness for medical appointments with a note.",
                    "You'll make an exception if the facilitator explains Brianna's situation calmly."]),
        dict(name="Team lead and observer", where="Keeps time and runs the debrief",
             facts_label="Your job:",
             facts=["Keep time: 5 minutes per scenario, then 10 minutes for the debrief form.",
                    "Call “pause” if anyone needs a break or a role-play gets too real.",
                    "Lead the team through the debrief form after each scenario."],
             extra="<strong>Only you know:</strong> the program has a safety plan for situations like Scenario 2, including a private room, the security desk, and a phone to call the shelter's advocate."),
    ],
    steps=[
        dict(label="Read your cards", desc="read your card and plan how you'll play it. Agree on the ground rules."),
        dict(label="Three scenarios", desc="act out each scenario for 5 minutes, then complete a debrief form. Rotate the facilitator each time."),
        dict(label="Plan and present", desc="share your team's best de-escalation phrases and a prevention plan for Brianna."),
        dict(label="Debrief", desc="step out of role and talk about how it felt to be in the middle of a crisis."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · read your cards", title="Get ready",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Read your card</li>
        <li>Choose who facilitates each scenario</li>
        <li>Agree on the ground rules</li>
      </ul>
    </div>
    <div class="box c1"><h3>Ground rules</h3>No physical contact. Anyone can call “pause.” Stay in your seat or space.</div>
  </div>""",
             notes="Check that every team knows the pause rule."),
        dict(eyebrow="Step 2 · three scenarios", title="Act, debrief, rotate",
             body="""  <table class="tbl">
    <tr><th>Each scenario</th><th>Time</th></tr>
    <tr><td><strong>Act it out:</strong> the facilitator de-escalates</td><td>5 min</td></tr>
    <tr><td><strong>Debrief form:</strong> warning signs, what you did, what worked, safety, next time</td><td>10 min</td></tr>
    <tr><td><strong>Rotate:</strong> a new facilitator</td><td>1 min</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Scenario 2 is a safety situation. The facilitator should use the program's safety plan.</p>""",
             notes="Watch Scenario 2 closely. The right response includes getting Brianna to a safe, private space and connecting her to an advocate, not just calming her down."),
        dict(eyebrow="Step 3 · plan and present", title="Prevent the next one",
             body="""  <ul>
    <li>Your team's three best <strong>de-escalation phrases</strong></li>
    <li>A <strong>prevention plan</strong> for Brianna: what would stop these from happening?</li>
    <li>What the <strong>program</strong> should change</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 3 minutes.</div>""",
             notes="Strong teams suggest program changes: private feedback from the chef, a lateness policy for medical visits, and a safety plan with the shelter."),
    ],
    debrief=dict(questions=["What did it feel like to play Brianna?",
                            "Which scenario was hardest to de-escalate? Why?",
                            "What warning signs did you notice early?",
                            "What would positive behavior support look like for Brianna next week?"],
                 notes="End with a reset: a stretch or a slow breath. Role-playing crisis can leave people activated."),
    apply_line="Show what you learned, then reflect on what calms you.",
    own_words="“The first sign of escalation I noticed was … and I responded by …”",
    exit_ticket=["Name three early warning signs of escalation.",
                 "One phrase you'll never use, and one you'll always use.",
                 "When should you call 911 or 988?"],
    packet_instructions="Print one packet per team. Cut the cards apart. Go over the ground rules before starting: no physical contact, and anyone can call “pause.” Rotate the facilitator role each scenario. Each learner needs a debrief form for each scenario they facilitate.",
    worksheet=dict(
        title="De-escalation debrief form",
        instructions="Complete one column for each scenario. Write facts, not labels.",
        columns=[("", 26), ("Scenario 1 · the chef", 24), ("Scenario 2 · the text", 24), ("Scenario 3 · the stipend", 0)],
        rows=6,
        first_col=["Warning signs we saw", "What the facilitator did", "What worked", "What made it worse",
                   "Safety steps or who we called", "What we'd do next time"],
        plan=[("Our three best de-escalation phrases:", 3),
              ("A prevention plan for Brianna:", 2),
              ("What the program should change:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "What my card says", "What I'll do or watch for"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.7, 1.65, 1.65, 1.7]),
    assignment=dict(
        intro="Capture your de-escalation practice as a work sample, then reflect on what calms you.",
        parts=[
            dict(title="Your scenario", summary="The scenario you facilitated or played, and what you learned.",
                 note="Answer about the scenario where you played the facilitator. If you didn't, answer about one you observed.",
                 items=[dict(type="roles"),
                        dict(type="q", text="Which scenario did you facilitate or observe? What were the early warning signs?", h=0.8),
                        dict(type="q", text="Write the exact words that helped calm the situation.", h=0.8)]),
            dict(title="De-escalation debrief", summary="A complete debrief form. Can be used as a DSP-I work sample.",
                 note=PORTFOLIO,
                 items=[dict(type="grid", text="Complete the debrief form for one scenario.",
                             columns=["", "What happened"], widths=[2.2, 4.5], rows=6, h=0.55,
                             first_col=["Scenario", "Warning signs", "What the facilitator did", "What worked",
                                        "Safety steps or who was called", "Prevention plan for next time"]),
                        dict(type="q", text="Explain how positive behavior support would change the way the program responds to Brianna.", h=1.0),
                        dict(type="q", text="Name a situation that would require calling 911 or 988, and what you would do first.", h=0.8)]),
            dict(title="What calms me", summary="Your own triggers and calming strategies, in your own words.",
                 items=[dict(type="q", text="Think about a time you were very upset. What helped, and what made it worse? How will that shape how you respond to women in crisis, and how you take care of yourself after?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “The first sign of escalation I noticed was … and I responded by …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your scenario (Part 1)", "Accurate warning signs and specific, calming words.",
             "Signs or words are general.", "Missing."],
            ["Debrief form (Part 2 table)", "Every row complete, factual, with a real prevention plan.",
             "Some rows missing or vague.", "Few rows complete, or uses labels."],
            ["Positive behavior support and safety (Part 2, questions)", "Clear PBS explanation and a correct safety response.",
             "Partly correct.", "Missing, or unsafe response."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your scenario and a debrief form.",
        reflection_title="What calms me",
        reflection_slide="Think about a time you were very upset. What helped, and what made it worse? How will that shape how you respond to women in crisis?",
    ),
))

# =====================================================================================================
# MODULE 6 · Safety & Safety Planning
# =====================================================================================================
MODULES[6] = finish(dict(
    num=6, hours=5,
    title="Safety &amp; Safety Planning",
    short_title="Safety Planning",
    slide_title_html="Safety &amp;<br>Safety Planning",
    subtitle="Safety at home, at work, on the commute, and online.",
    title_notes="Today lines up with the Safety core competency badge for DSP-I. The safety plan learners write is designed to be a portfolio work sample. Safety planning is personal for many survivors. Remind learners that they can step out at any time, and post the National Domestic Violence Hotline (1-800-799-7233), the National Human Trafficking Hotline (1-888-373-7888), and the DC Victim Hotline (confirm before class) in the room.",
    lead="How to help a woman build a safety plan that covers home, work, her commute, her children, and technology, and how to keep her location private in every record. You'll build a full safety plan as a team for a woman starting a new job.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Safety planning, workplace safety, technology safety, privacy, and DC safety resources",
                   practice="Team roles: Lena's safety plan for her new job"),
    objectives=[
        "Help a woman build a safety plan that covers work, the commute, child care pickup, and technology, including stalking and location tracking.",
        "Identify workplace safety risks and emergency procedures.",
        "Protect participant location and contact information in all records.",
        "Connect participants to DC domestic violence and safety resources.",
    ],
    slide_objectives=[
        "Build a safety plan with her, not for her",
        "Spot workplace safety risks",
        "Protect her location in every record",
        "Connect her to DC safety resources",
    ],
    opening=dict(title="Feeling safe",
                 quote="What makes a place feel safe to you? Think about a workplace, a building, or a route you take every day.",
                 notes="Keep it general. Write what learners name: good lighting, people I trust, knowing the exits, a locked door, not being alone. Safety planning builds on what women already do to stay safe."),
    learn_line="Planning for safety everywhere she goes.",
    learn=[
        dict(eyebrow="Safety planning", title="Her plan, built on what she knows",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>She is the expert on her own safety. Ask what she already does.</li>
        <li>A plan covers <strong>home, work, the commute, children, and technology</strong></li>
        <li>It changes as her life changes: a new job, a new address, a court date</li>
        <li>Leaving, and the months after, can be the most dangerous time</li>
      </ul>
    </div>
    <div class="box c2"><h3>Partner with advocates</h3>Domestic violence advocates are trained in safety planning. Facilitators support the plan and refer for the rest.</div>
  </div>""",
             notes="Know your lane: facilitators support safety planning around work and the program. Detailed safety planning and legal options go to trained advocates. The National Domestic Violence Hotline can help anyone make a plan."),
        dict(eyebrow="At work", title="Workplace safety",
             body="""  <table class="tbl">
    <tr><th>Risk</th><th>Planning ideas</th></tr>
    <tr><td><strong>He knows where she works</strong></td><td>With her consent, share a photo with security or the front desk</td></tr>
    <tr><td><strong>Calls or visits at work</strong></td><td>Screen calls, a code word with a trusted coworker</td></tr>
    <tr><td><strong>Parking lot or bus stop</strong></td><td>Walk out with someone, change routes and times</td></tr>
    <tr><td><strong>Court dates and appointments</strong></td><td>Know her rights to safe leave (DC law allows paid leave for domestic violence-related needs; confirm details)</td></tr>
  </table>""",
             notes="Confirm before class the current DC rules on paid safe leave under the Accrued Sick and Safe Leave Act, and on workplace protections for survivors. Telling an employer is always her choice."),
        dict(eyebrow="Technology", title="Technology safety",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Location sharing:</strong> check phone settings, shared family plans, and apps</li>
        <li><strong>Tracking devices</strong> in a car, bag, or her child's things</li>
        <li><strong>Accounts:</strong> new passwords, two-step sign-in, and check who has access</li>
        <li><strong>Social media:</strong> no check-ins, workplace names, or photos that show where she is</li>
      </ul>
    </div>
    <div class="box c1"><h3>Careful</h3>Suddenly changing everything can alert an abuser. Plan changes with her and an advocate.</div>
  </div>""",
             notes="Technology safety resources for survivors are available through national domestic violence organizations. Encourage learners to use a safer device when a survivor's phone may be monitored."),
        dict(eyebrow="Privacy", title="Protecting her location",
             body="""  <div class="cols">
    <div>
      <ul>
        <li>Never write a shelter address or her new address in places others can see</li>
        <li>Use the program's address on forms when allowed</li>
        <li>Never confirm she's in your program to anyone who calls</li>
        <li>Check releases before sharing anything, even with other agencies</li>
        <li>Be careful with photos, sign-in sheets, and group emails</li>
      </ul>
    </div>
    <div class="box c3"><h3>Ask her</h3>“Who knows where you live and work? Who should never find out?”</div>
  </div>""",
             notes="Ask learners about confidential address options in DC and how programs handle addresses for survivors (research and confirm before class)."),
        dict(eyebrow="DC resources · confirm before class", title="Where to connect her",
             body="""  <table class="tbl">
    <tr><th>Need</th><th>Resource</th></tr>
    <tr><td><strong>24-hour help and safety planning</strong></td><td>National Domestic Violence Hotline: 1-800-799-7233 · DC Victim Hotline</td></tr>
    <tr><td><strong>Trafficking</strong></td><td>National Human Trafficking Hotline: 1-888-373-7888</td></tr>
    <tr><td><strong>Protection orders</strong></td><td>DC Superior Court Domestic Violence Division, with an advocate</td></tr>
    <tr><td><strong>Shelter and advocacy</strong></td><td>DC domestic violence programs (list current ones on the board)</td></tr>
    <tr><td><strong>Immediate danger</strong></td><td>911</td></tr>
  </table>""",
             notes="Before class, confirm the DC Victim Hotline number and the current DC domestic violence programs. Write them on the board. Never send a woman to a resource you haven't checked."),
    ],
    quick_check=dict(title="Safe or risky?",
                     items=["Posting a group photo from the program's job fair on social media",
                            "Using the program's address on a job application",
                            "Telling a caller, “She's not here right now”",
                            "Helping her turn off location sharing, after planning with an advocate",
                            "Emailing her new address to the whole team"],
                     notes="Risky: 1, 3 (it confirms she's a participant), 5. Safer: 2, 4. Say: “I'm not able to confirm who is in our program.”"),
    practice_line="Step into a role and build a full safety plan for a woman starting a new job.",
    practice_notes="Hand out the in-class packet. Anyone can switch to the Team lead role.",
    activity_title="Team roles: Lena's safety plan",
    team_notes_title="Lena's Safety Plan",
    case=dict(
        name="Lena",
        page_intro="<strong>Lena, 35</strong> (fictional), starts a new job at a hospital laundry next Monday. She left her abusive husband five months ago. He still lives in the same neighborhood, and they share custody of their 6-year-old son.",
        page_how="Each person on your team plays someone helping Lena get ready for her first day. Your role card has facts only you know. Together, your team builds a safety plan with Lena that covers home, the commute, work, child care pickup, and technology.",
        slide_title="Meet Lena",
        slide_intro="<strong>Lena, 35</strong>, starts a new job at a hospital laundry next Monday.",
        bullets=["Left her abusive husband five months ago",
                 "He lives in the same neighborhood",
                 "They share custody of their son, 6",
                 "She takes the bus to work and picks her son up from after-school care"],
        quote="“I finally got a job. I'm not letting him take this from me too.”",
        quote_label="What Lena says",
        slide_notes="Lena's determination is a strength. The plan should protect her job, not make it harder to keep.",
        packet_text="<strong>Lena, 35</strong>, left her abusive husband, Victor, five months ago. He still lives in their neighborhood, and they share custody of their son, Mateo (6), under a temporary court order. Lena starts a new job at a hospital laundry next Monday, on the 7 a.m. to 3:30 p.m. shift. She takes two buses to work and picks Mateo up from after-school care at 5 p.m. Your team is helping her get ready for her first day.",
    ),
    roles_title="Six supports, one safety plan",
    roles_small="Each card has facts only you know. Lena decides what goes in her plan.",
    roles_notes="The Tech safety card has important facts. Make sure teams handle the location sharing carefully, not by suddenly turning everything off.",
    roles=[
        dict(name="Domestic violence advocate", where="Community DV program",
             facts=["Victor has violated the stay-away part of the court order once. Lena reported it.",
                    "Lena has a protection order that covers her home, but not her new workplace yet. It may be possible to add it.",
                    "Lena has a code word with her sister."],
             need="An updated order and a plan for custody exchanges."),
        dict(name="Workforce facilitator", where="Women's workforce program",
             facts=["Lena hasn't told her new employer anything about Victor.",
                    "The hospital has security at the main entrance, but the laundry uses a back loading dock.",
                    "Lena is worried telling HR will make her look like “trouble.”"],
             need="A plan for what, if anything, Lena tells her employer."),
        dict(name="Hospital HR contact", where="Lena's new employer",
             facts=["The hospital has a workplace violence prevention policy and works with security on safety plans for employees.",
                    "Employees can request schedule changes for court dates.",
                    "HR keeps safety information confidential and shares it only with security, with the employee's consent."],
             need="Lena's consent before anything is shared."),
        dict(name="After-school care director", where="Mateo's program",
             facts=["Victor is on Mateo's pickup list for his custody days.",
                    "Last week, Victor showed up on Lena's day and argued with staff.",
                    "The program needs a copy of the custody order to enforce pickup days."],
             need="A copy of the order and a plan for Lena's pickup days."),
        dict(name="Tech safety specialist", where="Helps with phones and accounts",
             facts=["Lena's phone is still on Victor's family plan.",
                    "Her location sharing is on. Victor may be able to see where she is.",
                    "Mateo's tablet, which goes back and forth between homes, is logged into Victor's account."],
             need="A careful plan, made with the advocate, so Victor isn't alerted."),
        dict(name="Team lead", where="Writes the safety plan",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Go setting by setting: home, commute, work, child care, technology, and records.",
                    "Write the plan on the worksheet, and check every item with “Is this Lena's choice?”"],
             extra="<strong>Only you know:</strong> Lena's bus stop is two blocks from Victor's apartment."),
    ],
    steps=debrief_steps("read your card. What risk does your role see? What does Lena already do to stay safe?",
                        "share what you know and build the safety plan setting by setting.",
                        "check the plan against Lena's choices and present her first-day plan."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>What safety risk does your role see?</li>
    <li>What does your role need from someone else?</li>
    <li>What would Lena want?</li>
  </ul>""",
             notes="Walk the room and check in with anyone who seems affected."),
        dict(eyebrow="Step 2 · team huddle", title="Build the plan, setting by setting",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Home</li><li>The commute</li><li>Work</li><li>Child care pickup</li><li>Phone and online</li><li>Records and documents</li>
      </ol>
    </div>
    <div class="box c3"><h3>For each setting</h3>What's the risk? What's the plan? Who knows? Is it Lena's choice?</div>
  </div>""",
             notes="Teams should spot the bus stop near Victor's apartment, the loading dock entrance, the pickup list, and the phone plan."),
        dict(eyebrow="Step 3 · plan and present", title="Lena's first day",
             body="""  <ul>
    <li>Lena's plan for <strong>Monday</strong>, from leaving home to picking up Mateo</li>
    <li>What she'll tell her <strong>employer</strong>, if anything, and why</li>
    <li>The <strong>technology</strong> steps, and who helps</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes.</div>""",
             notes="Praise teams that keep the decision about telling HR with Lena, and that plan technology changes carefully with the advocate."),
    ],
    debrief=dict(questions=["Which risk would you have missed on your own?",
                            "How did your team keep Lena in charge of her plan?",
                            "What's one way you'll protect a woman's location in your records?",
                            "How are you feeling? What do you need right now?"],
                 notes="End with a grounding moment. Remind learners where to find support."),
    apply_line="Show what you learned, then reflect on safety in your own life.",
    own_words="“A safety risk people often overlook at a new job is …”",
    exit_ticket=["Name four settings a safety plan should cover.",
                 "What should you say if someone calls asking if a woman is in your program?",
                 "Name one national hotline and its number."],
    packet_instructions="Print one packet per team. Cut the role cards apart. Any learner can switch to the Team lead role. Confirm DC hotline numbers and programs before class and post them in the room.",
    worksheet=dict(
        title="Safety plan",
        instructions="For each setting, write the risk, the plan, who knows, and whether Lena agreed.",
        columns=[("Setting", 18), ("The risk", 24), ("The plan", 30), ("Who knows · Lena agreed?", 0)],
        rows=6,
        first_col=["Home", "The commute", "Work", "Child care pickup", "Phone and online", "Records and documents"],
        plan=[("Lena's Monday, from home to pickup:", 3),
              ("What Lena will tell her employer, and why:", 1),
              ("Technology steps, and who helps:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "The risk my role sees", "What my role can do"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.2, 1.6, 2.2, 1.7]),
    assignment=dict(
        intro="Capture Lena's safety plan as a work sample, then reflect on safety in your own life.",
        parts=[
            dict(title="Your role's view", summary="The risk your role saw and how it fits Lena's plan.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What safety risk did your role see that others might have missed?", h=0.8),
                        dict(type="q", text="How did your team make sure the plan was Lena's choice?", h=0.8)]),
            dict(title="Lena's safety plan", summary="A full safety plan across six settings. Can be used as a DSP-I work sample.",
                 note=PORTFOLIO,
                 items=[dict(type="grid", text="Write Lena's safety plan.",
                             columns=["Setting", "Risk", "Plan", "Who knows"], widths=[1.2, 1.6, 2.4, 1.5], rows=6, h=0.6,
                             first_col=["Home", "Commute", "Work", "Child care", "Phone and online", "Records"]),
                        dict(type="q", text="Name two ways you will protect a woman's location and contact information in your records.", h=0.8),
                        dict(type="q", text="Which resources would you connect Lena to, and how? Include at least one hotline.", h=0.8)]),
            dict(title="Safety in my life", summary="What safety means to you, in your own words.",
                 items=[dict(type="q", text="What has helped you, or a woman close to you, feel safe? How will that shape the way you help women plan for safety, while letting them lead?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “A safety risk people often overlook at a new job is …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's view (Part 1)", "A specific risk, and clear respect for Lena's choices.",
             "General.", "Missing, or decides for Lena."],
            ["Safety plan (Part 2 table)", "Realistic risks and plans for all six settings.",
             "Some settings missing or vague.", "Few settings complete."],
            ["Privacy and resources (Part 2, questions)", "Correct privacy practices and appropriate resources with a hotline.",
             "Partly correct.", "Missing, or shares her location."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's view and Lena's safety plan.",
        reflection_title="Safety in my life",
        reflection_slide="What has helped you, or a woman close to you, feel safe? How will that shape the way you help women plan for safety, while letting them lead?",
    ),
))

# =====================================================================================================
# MODULE 7 · Health & Wellness Support
# =====================================================================================================
MODULES[7] = finish(dict(
    num=7, hours=4,
    title="Health &amp; Wellness Support",
    short_title="Health &amp; Wellness",
    slide_title_html="Health &amp;<br>Wellness Support",
    subtitle="Supporting women's whole-person health on the path to work.",
    title_notes="Today lines up with the Health and Wellness core competency badge for DSP-I. The wellness resource sheet learners make is designed to be a portfolio work sample. Remind learners of the role's limits: facilitators support access to care and healthy routines. They don't diagnose or give medical advice.",
    lead="The physical and mental health barriers that can keep women from working, and how to help them get care and build routines that support a job. You'll build a wellness resource sheet as a team for a new mother starting work.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Women's health and work, health effects of violence, getting care, and wellness routines",
                   practice="Team roles: Patrice's wellness plan"),
    objectives=[
        "Identify physical and mental health barriers to employment, including women's health, pregnancy and postpartum needs, and the health effects of violence.",
        "Support participants in accessing health care and benefits.",
        "Encourage wellness routines that support job retention.",
    ],
    slide_objectives=[
        "Identify health barriers to work",
        "Help women get health care and benefits",
        "Build wellness routines that help keep a job",
    ],
    opening=dict(title="One healthy habit",
                 quote="What is one habit that helps you stay well when life gets busy? Sleep, prayer, a walk, a call with a friend, music?",
                 notes="Go around the room quickly. Write the habits on the board. These are the wellness routines learners will help others build."),
    learn_line="Health, care, and the routines that help women keep a job.",
    learn=[
        dict(eyebrow="Health and work", title="Health barriers women face",
             body="""  <div class="cols">
    <ul>
      <li>Chronic conditions without regular care: diabetes, high blood pressure, asthma</li>
      <li>Pregnancy, postpartum recovery, and breastfeeding</li>
      <li>Depression, anxiety, and PTSD</li>
    </ul>
    <ul>
      <li>Injuries from violence, including head injuries</li>
      <li>Substance use, and recovery</li>
      <li>No insurance, no doctor, or no time to go</li>
    </ul>
  </div>""",
             notes="Ask: “Which of these have you seen keep someone from working, or keeping a job?”"),
        dict(eyebrow="Violence and health", title="The health effects of violence",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Head injuries</strong> from being hit or strangled can cause headaches, memory problems, and trouble focusing</li>
        <li><strong>Strangulation</strong> can cause serious injury even without visible marks</li>
        <li><strong>Chronic pain, sleep problems,</strong> and stress-related illness</li>
        <li><strong>Reproductive coercion:</strong> an abuser controlling birth control or pregnancy</li>
      </ul>
    </div>
    <div class="box c1"><h3>Know your lane</h3>Don't diagnose. If she describes these, encourage a medical visit and offer a warm handoff.</div>
  </div>""",
             notes="Many survivors don't connect symptoms like memory problems to past injuries. Helping her get evaluated can change everything, including how she does at work."),
        dict(eyebrow="Getting care · confirm before class", title="Health care and benefits in DC",
             body="""  <table class="tbl">
    <tr><th>Need</th><th>Where to start</th></tr>
    <tr><td><strong>Health coverage</strong></td><td>DC Medicaid and the DC Healthcare Alliance (through DHS); DC Health Link</td></tr>
    <tr><td><strong>Primary care</strong></td><td>Community health centers, with sliding-scale fees</td></tr>
    <tr><td><strong>Mental health</strong></td><td>DC Department of Behavioral Health access line</td></tr>
    <tr><td><strong>Mothers and babies</strong></td><td>WIC, postpartum care, and home visiting programs</td></tr>
    <tr><td><strong>Crisis</strong></td><td>988 Suicide and Crisis Lifeline (call or text)</td></tr>
  </table>""",
             notes="Confirm current program names, eligibility, and contact information before class."),
        dict(eyebrow="At work", title="Health supports on the job",
             body="""  <table class="tbl">
    <tr><th>Need</th><th>What may be available (confirm current law and policy)</th></tr>
    <tr><td><strong>Breastfeeding</strong></td><td>Break time and a private space to pump (federal PUMP Act; DC law)</td></tr>
    <tr><td><strong>Pregnancy</strong></td><td>Reasonable accommodations (federal Pregnant Workers Fairness Act)</td></tr>
    <tr><td><strong>Doctor visits</strong></td><td>Paid sick leave under DC law</td></tr>
    <tr><td><strong>Disability or mental health</strong></td><td>Reasonable accommodations under the ADA</td></tr>
  </table>""",
             notes="Learners don't need to be legal experts. They need to know these protections exist so they can point women to HR, an advocate, or legal help. Confirm details before class."),
        dict(eyebrow="Routines", title="Wellness routines that help keep a job",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Sleep:</strong> a regular bedtime, as much as life allows</li>
        <li><strong>Food:</strong> plan meals and snacks for long shifts</li>
        <li><strong>Movement:</strong> a short walk counts</li>
        <li><strong>Connection:</strong> one person she can call</li>
        <li><strong>Calm:</strong> breathing, prayer, music, or quiet time</li>
        <li><strong>Appointments:</strong> scheduled before she starts work</li>
      </ul>
    </div>
    <div class="box c3"><h3>Her routine</h3>Ask what already works for her. Build on it. Small and realistic beats perfect.</div>
  </div>""",
             notes="Connect back to the opening list of healthy habits."),
    ],
    quick_check=dict(title="What would you do?",
                     items=["A participant says she's had headaches and trouble remembering things since her ex choked her.",
                            "A new mother is worried she can't pump at her new job.",
                            "A participant says she's been feeling hopeless and doesn't see the point anymore.",
                            "A woman has no health insurance and needs her blood pressure medicine."],
                     notes="1) Encourage an urgent medical visit; strangulation and head injuries need evaluation. 2) Share that she likely has a right to break time and a private space; connect her to HR or an advocate. 3) Ask directly about safety, stay with her, call or text 988, and get your supervisor. 4) Help her apply for coverage and connect to a community health center."),
    practice_line="Step into a role and build a wellness plan for a new mother starting work.",
    practice_notes="Hand out the in-class packet. Remind learners: support and refer, don't diagnose.",
    activity_title="Team roles: Patrice's wellness plan",
    team_notes_title="Patrice's Wellness Plan",
    case=dict(
        name="Patrice",
        page_intro="<strong>Patrice, 26</strong> (fictional), had a baby four months ago and starts a job as a pharmacy technician trainee in two weeks. She left an abusive relationship while pregnant.",
        page_how="Each person on your team plays someone supporting Patrice's health. Your role card has facts only you know. Together, your team builds a wellness resource sheet and plan that helps Patrice start, and keep, her new job.",
        slide_title="Meet Patrice",
        slide_intro="<strong>Patrice, 26</strong>, had a baby four months ago. She starts a pharmacy technician trainee job in two weeks.",
        bullets=["Left an abusive relationship while pregnant",
                 "Breastfeeding her son, Malik",
                 "Hasn't had a postpartum checkup",
                 "Excited, and exhausted"],
        quote="“I want this job so bad. But some days I can barely get out of bed, and I don't know if that's normal.”",
        quote_label="What Patrice says",
        slide_notes="Patrice's words may point to postpartum depression, which is common and treatable. The team's job is to encourage care and connect her, not diagnose.",
        packet_text="<strong>Patrice, 26</strong>, had her son, Malik, four months ago. She left an abusive relationship while pregnant and lives with her grandmother. She starts a job as a pharmacy technician trainee in two weeks, on day shifts. She is breastfeeding and hasn't had a postpartum checkup. She told her facilitator she's excited about the job but some days can barely get out of bed.",
    ),
    roles_title="Five supports and a lead",
    roles_small="Each card has facts only you know. Support and refer. Don't diagnose.",
    roles_notes="The Peer mentor card holds the facts that point to postpartum depression. Make sure teams respond with care and a referral, not a diagnosis.",
    roles=[
        dict(name="Community health worker", where="Women's health center",
             facts=["Patrice missed her postpartum checkup because she had no ride.",
                    "Her Medicaid coverage for pregnancy may continue after birth. Check her current coverage.",
                    "The health center offers postpartum visits with a depression screening."],
             need="A ride, and an appointment before she starts work."),
        dict(name="WIC and benefits worker", where="WIC program",
             facts=["Patrice and Malik are enrolled in WIC.",
                    "WIC offers breastfeeding support and can help with a breast pump.",
                    "Her WIC appointment is on a weekday morning, which will conflict with her new shift."],
             need="A new appointment time that fits her work schedule."),
        dict(name="Peer mentor", where="Has lived experience as a young mother",
             facts=["Patrice told you she cries most days and feels like she's “failing Malik.”",
                    "She said she sometimes feels numb, and that she hasn't told anyone because she's afraid they'll take the baby.",
                    "You had postpartum depression and got help. You're comfortable sharing that briefly."],
             need="A gentle way to encourage her to talk to a doctor, without scaring her.",
             extra="She has not said anything about hurting herself or the baby. If she does, follow the safety steps: stay with her, call 988, get your supervisor."),
        dict(name="Workforce facilitator", where="Women's workforce program",
             facts=["The pharmacy is a large chain with an HR department.",
                    "Patrice is afraid to ask for pumping breaks in her first week.",
                    "Her training includes standing for long shifts and some evening study."],
             need="A plan for what Patrice can ask for at work, and how."),
        dict(name="Child care navigator", where="Child care subsidy program",
             facts=["Malik has a spot at an infant care center starting next week, with a subsidy.",
                    "The center is a 20-minute bus ride from the pharmacy.",
                    "Patrice's grandmother can do pickup three days a week, not all five."],
             need="A backup plan for the other two days."),
        dict(name="Team lead", where="Writes the wellness plan",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Build the wellness resource sheet: need, resource, how to connect, workplace support.",
                    "Keep asking: “Is this realistic for a new mother starting a new job?”"],
             extra="<strong>Only you know:</strong> Patrice said the thing that helps her most is her Sunday walk with her grandmother and Malik."),
    ],
    steps=debrief_steps("read your card and decide what health need your role sees first.",
                        "share what you know and fill in the wellness resource sheet together.",
                        "write Patrice's plan for her first two weeks and how her routines fit."),
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Read your card",
             body="""  <ul>
    <li>What health need does your role see?</li>
    <li>What's in the way of care?</li>
    <li>What does your role need from someone else?</li>
  </ul>""",
             notes="Check in with the Peer mentor. Make sure she's comfortable with her card."),
        dict(eyebrow="Step 2 · team huddle", title="Build the wellness resource sheet",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role shares what it knows</li>
        <li>List every health need</li>
        <li>Match each one to a resource and how to connect</li>
        <li>Add what she can ask for at work</li>
      </ol>
    </div>
    <div class="box c3"><h3>Know your lane</h3>Encourage a postpartum visit with a doctor. Don't diagnose.</div>
  </div>""",
             notes="Make sure teams prioritize the postpartum checkup with depression screening, and handle it with care."),
        dict(eyebrow="Step 3 · plan and present", title="Patrice's first two weeks",
             body="""  <ul>
    <li>Appointments to schedule <strong>before</strong> she starts</li>
    <li>What she can <strong>ask for at work</strong>, and how</li>
    <li>One <strong>wellness routine</strong> built on what she already does</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes.</div>""",
             notes="Praise teams that build on her Sunday walk."),
    ],
    debrief=dict(questions=["How did your team talk about Patrice's mood without diagnosing her?",
                            "Which barrier to care was hardest to solve?",
                            "What protections at work did you not know about before today?",
                            "What's one wellness routine you'll keep for yourself?"],
                 notes="Connect back to the opening habits. Wellness applies to the facilitator, too."),
    apply_line="Show what you learned, then reflect on your own wellness.",
    own_words="“One wellness habit that helps people keep a job is …”",
    exit_ticket=["Name two health barriers to work.",
                 "Name one workplace right a breastfeeding mother may have.",
                 "What would you do if a participant said she felt hopeless?"],
    packet_instructions="Print one packet per team. Cut the role cards apart. Remind learners to support and refer, not diagnose. Confirm DC health resources before class.",
    worksheet=dict(
        title="Wellness resource sheet",
        instructions="For each need, list the resource, how Patrice connects to it, and what she can ask for at work.",
        columns=[("Need", 22), ("Resource", 24), ("How to connect", 26), ("Support at work", 0)],
        rows=6,
        first_col=["Postpartum checkup", "Mood and sleep", "Breastfeeding and pumping", "Health coverage",
                   "Child care backup", "Daily wellness routine"],
        plan=[("Appointments to schedule before she starts:", 2),
              ("What she'll ask for at work, and how:", 2),
              ("One wellness routine, built on what she already does:", 1)],
    ),
    team_notes=dict(step1_columns=["Role", "The health need my role sees", "What's in the way"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.5, 1.6, 1.8, 1.8]),
    assignment=dict(
        intro="Capture Patrice's wellness resource sheet as a work sample, then reflect on your own wellness.",
        parts=[
            dict(title="Your role's view", summary="The health need your role saw, and how to support it.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="What health need did your role see, and what was in the way of care?", h=0.8),
                        dict(type="q", text="Write what you would say to Patrice to encourage a postpartum checkup, without diagnosing.", h=0.9)]),
            dict(title="Patrice's wellness resource sheet", summary="Needs, resources, and work supports. Can be used as a DSP-I work sample.",
                 note=PORTFOLIO,
                 items=[dict(type="grid", text="Complete Patrice's wellness resource sheet.",
                             columns=["Need", "Resource", "How to connect", "Support at work"],
                             widths=[1.5, 1.6, 1.8, 1.8], rows=5, h=0.6,
                             first_col=["Postpartum care", "Mood and sleep", "Pumping at work", "Health coverage", "Child care backup"]),
                        dict(type="q", text="Describe one wellness routine for Patrice that will help her keep her job.", h=0.8)]),
            dict(title="My wellness", summary="Your own wellness routines, in your own words.",
                 items=[dict(type="q", text="What helps you stay well when life is hard? How will taking care of your own health help you support other women?",
                             h=2.0, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “One wellness habit that helps people keep a job is …”", h=0.8)]),
        ],
        rubric_full=[
            ["Role's view (Part 1)", "A clear need and barrier, and a caring encouragement that doesn't diagnose.",
             "General, or the encouragement is unclear.", "Missing, or diagnoses."],
            ["Wellness resource sheet (Part 2 table)", "Realistic resources and connections for every need.",
             "Some rows missing or vague.", "Few rows complete."],
            ["Wellness routine (Part 2, question)", "A realistic routine that builds on what Patrice already does.",
             "General.", "Missing."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your role's view and the wellness resource sheet.",
        reflection_title="My wellness",
        reflection_slide="What helps you stay well when life is hard? How will taking care of your own health help you support other women?",
    ),
))

# =====================================================================================================
# MODULE 8 · Documentation & Resource Referral
# =====================================================================================================
MODULES[8] = finish(dict(
    num=8, hours=6,
    title="Documentation &amp; Resource Referral",
    short_title="Documentation &amp; Referral",
    slide_title_html="Documentation &amp;<br>Resource Referral",
    subtitle="Notes that protect her, and referrals that actually connect.",
    title_notes="This is the last content module before Job Search and the capstone. Today brings together safety, privacy, and person-centered practice in writing. For survivors, records can follow them into court, custody cases, and job applications, and a careless note can put a woman in danger.",
    lead="How to write objective, strengths-based progress notes that protect a woman's privacy and safety, and how to make referrals that connect. You'll fix a set of weak notes as a team, write referrals, and track them.",
    flow_text=dict(open="Welcome and opening circle",
                   learn="Progress notes, strengths-based language, privacy and safety in records, and referrals that connect",
                   practice="Team roles: fix the notes and referrals for Yvonne"),
    objectives=[
        "Write objective, strengths-based progress notes.",
        "Make referrals to DC employment, reentry, housing, and women's and survivor services, with a warm handoff.",
        "Track referrals and follow-ups in a shared log.",
        "Proofread and revise their own writing for clarity and a professional tone.",
    ],
    slide_objectives=[
        "Write objective, strengths-based notes",
        "Keep her safe in every record",
        "Make referrals with a warm handoff",
        "Track every referral to the end",
    ],
    opening=dict(title="What would you want it to say?",
                 quote="Imagine a program wrote a note about you on your hardest day. What would you want it to say? What would you never want it to say?",
                 notes="Write two lists: want (what I was facing, that I showed up, what I'm good at, the plan) and never (labels like difficult, dramatic, non-compliant, and details that weren't anyone's business). That's today's lesson."),
    learn_line="Writing that's accurate, respectful, private, and safe.",
    learn=[
        dict(eyebrow="Progress notes", title="A simple structure",
             body="""  <table class="tbl">
    <tr><th></th><th>What goes here</th><th>Example</th></tr>
    <tr><td><strong>What happened</strong></td><td>Facts: date, length, what she said and did. Quotes in quotation marks.</td><td>10/14, 45 min. Participant said, “I applied to two jobs this week.”</td></tr>
    <tr><td><strong>Progress</strong></td><td>Movement toward her goals, and strengths</td><td>Completed her résumé. Practiced her interview answer with confidence.</td></tr>
    <tr><td><strong>Next steps</strong></td><td>Who, what, by when</td><td>Facilitator will send referral to training program by 10/16. Participant will call by 10/18.</td></tr>
  </table>""",
             notes="Agencies use different formats (DAP, SOAP, narrative). This structure maps easily onto any of them."),
        dict(eyebrow="Language", title="Facts and strengths, not labels",
             body="""  <table class="tbl">
    <tr><th>Instead of…</th><th>Write…</th></tr>
    <tr><td>“Dramatic, crying again.”</td><td>“Participant cried while talking about custody. Took a break and returned.”</td></tr>
    <tr><td>“Non-compliant, missed sessions.”</td><td>“Missed 10/2 and 10/9. Said child care fell through both days.”</td></tr>
    <tr><td>“Still with her abuser.”</td><td>Leave it out unless needed for safety planning, and then only the minimum.</td></tr>
    <tr><td>“Ex-offender” / “prostitute”</td><td>“Returning citizen” / “survivor of trafficking,” only if relevant and allowed</td></tr>
  </table>""",
             notes="Labels follow women into court and custody cases. Ask: “Would she feel respected reading this?”"),
        dict(eyebrow="Privacy and safety", title="Records can put her in danger",
             body="""  <div class="cols">
    <div>
      <ul>
        <li><strong>Never</strong> write a shelter address or her new address in shared notes</li>
        <li><strong>Minimum necessary:</strong> only what's needed for the service</li>
        <li><strong>Releases:</strong> share only what she has agreed to, with whom she has agreed</li>
        <li>Records can be <strong>subpoenaed</strong> in court and custody cases</li>
        <li>Lock paper files. Use secure systems, not personal email or texts.</li>
      </ul>
    </div>
    <div class="box c1"><h3>Before you write</h3>“If her abuser's lawyer read this, could it hurt her?”</div>
  </div>""",
             notes="Survivor programs often have special confidentiality rules, including under federal funding laws for domestic violence services. Learners should ask about their agency's rules. Confirm current requirements before class."),
        dict(eyebrow="Referrals", title="Referrals that connect",
             body="""  <div class="cols">
    <div>
      <ol>
        <li><strong>Check it:</strong> the resource is current and she's eligible</li>
        <li><strong>Ask her:</strong> does she want it? What worries her?</li>
        <li><strong>Get consent</strong> to share, in writing</li>
        <li><strong>Warm handoff:</strong> call together, introduce her</li>
        <li><strong>Log it</strong> and set a follow-up date</li>
        <li><strong>Follow up:</strong> did she connect? How did it go?</li>
      </ol>
    </div>
    <div class="box c3"><h3>For survivors</h3>Check that the program is safe for her: women-only if she prefers, and no chance of running into her abuser.</div>
  </div>""",
             notes="A referral that isn't followed up is just a phone number."),
        dict(eyebrow="Tracking", title="The referral log",
             body="""  <table class="tbl">
    <tr><th>Date</th><th>Referred to</th><th>For</th><th>Consent?</th><th>Follow-up date</th><th>Outcome</th></tr>
    <tr><td>10/14</td><td>Training program</td><td>Medical billing course</td><td>Yes, signed</td><td>10/21</td><td>Enrolled</td></tr>
    <tr><td>10/14</td><td>Legal advocate</td><td>Custody question</td><td>Yes, signed</td><td>10/18</td><td>Appointment 10/25</td></tr>
  </table>
  <p class="small" style="margin-top:14px">No addresses or private details in the log. Facts and dates only.</p>""",
             notes="Show learners how a shared log helps a team make sure nothing falls through the cracks."),
        dict(eyebrow="Proofread", title="Four checks before you save",
             body="""  <ol>
    <li><strong>Accurate:</strong> dates, names, quotes</li>
    <li><strong>Objective:</strong> facts and strengths, no labels</li>
    <li><strong>Safe and private:</strong> no location, minimum necessary</li>
    <li><strong>Professional:</strong> clear, no slang or texting shortcuts</li>
  </ol>
  <div class="warn" style="margin-top:18px">Never change a saved note. Add a dated correction, following agency policy.</div>""",
             notes="Run the four checks on one weak note as a class, then move to Practice."),
    ],
    quick_check=dict(title="Fix it or keep it?",
                     items=["“Participant was very emotional and dramatic.”",
                            "“Participant said, ‘I want to work in a hospital.’”",
                            "“Staying at [shelter name] on 14th Street.”",
                            "“Completed résumé. Next session 10/20 at 10 a.m.”"],
                     notes="Fix: 1 (label), 3 (location). Keep: 2, 4."),
    practice_line="Step into a role and fix the notes and referrals for one woman's case.",
    practice_notes="Hand out the in-class packet. Each role card has that worker's weak note or referral and what really happened.",
    activity_title="Team roles: fix the notes and referrals for Yvonne",
    team_notes_title="Fixing Yvonne's Notes and Referrals",
    case=dict(
        name="Yvonne",
        page_intro="<strong>Yvonne, 42</strong> (fictional), is a survivor of labor trafficking who has been in a women's workforce program for two months. Several staff wrote notes and referrals for her this week, and every one has problems.",
        page_how="Each person on your team plays one of those staff members. Your card has your weak note or referral and what really happened. Together, your team fixes them, writes one strong progress note, and builds a referral log.",
        slide_title="Meet Yvonne",
        slide_intro="<strong>Yvonne, 42</strong>, is a survivor of labor trafficking. She has been in a women's workforce program for two months.",
        bullets=["Lives in confidential housing for survivors",
                 "Wants to work as a home health aide",
                 "Five staff wrote notes or referrals this week",
                 "Every one has problems"],
        quote="“The people who held me wrote everything down about me. I need to know what you're writing, and who sees it.”",
        quote_label="What Yvonne says",
        slide_notes="For a trafficking survivor, records can feel like control. Yvonne's request is reasonable: she can see her records and know who they're shared with.",
        packet_text="<strong>Yvonne, 42</strong>, is a survivor of labor trafficking. For three years she was forced to work as a live-in housekeeper without pay. She now lives in confidential housing for survivors and has been in a women's workforce program for two months. She wants to work as a home health aide. This week, five staff members wrote notes or referrals about her. Every one of them has problems.",
    ),
    roles_title="Five weak notes and a lead",
    roles_small="Each card has your weak note or referral and what really happened.",
    roles_notes="Make sure teams catch the location in the housing note and the over-sharing in the referral email.",
    roles=[
        dict(name="Workforce facilitator", where="Progress note",
             facts_label="Your note says:",
             facts=["“Yvonne is very paranoid about her info. Seemed checked out. Probably needs therapy. Talked about jobs.”"],
             need="Yvonne asked who can see her file (a reasonable question). She said she was tired from a night class. You reviewed three home health aide job postings, and she chose two to apply to by Friday 10/18.",
             need_label="What really happened:"),
        dict(name="Housing advocate", where="Progress note",
             facts_label="Your note says:",
             facts=["“Visited Y at the safe house on Monroe St, apt 2B. Place is fine. She's doing ok.”"],
             need="You visited on 10/14 for 30 minutes. Her lease renewal is due 11/1. She asked for help understanding it. You'll review it together on 10/22.",
             need_label="What really happened:"),
        dict(name="Legal advocate", where="Referral email",
             facts_label="Your email to a training program says:",
             facts=["Subject: “Yvonne Barnes, trafficking victim.” Body: “Please enroll her. She was trafficked for 3 years and has a T visa application pending. Very sweet lady.”"],
             need="Yvonne signed a release to share only her name, contact through the program, and that she is interested in the home health aide course. She did not agree to share anything about trafficking or immigration.",
             need_label="What really happened:"),
        dict(name="Health navigator", where="Referral log entry",
             facts_label="Your log says:",
             facts=["“Ref'd to clinic. Will f/u.”"],
             need="On 10/15 you referred Yvonne to a community health center for a physical required by the training program. She signed consent. Her appointment is 10/24 at 9 a.m. You'll call her on 10/25 to check how it went.",
             need_label="What really happened:"),
        dict(name="Peer mentor", where="Progress note",
             facts_label="Your note says:",
             facts=["“Y and I had a good talk. She told me everything about what happened to her and her family back home. So sad. She's a fighter!!”"],
             need="You met for 40 minutes on 10/16. Yvonne said she felt “less alone.” She wants to join the women's support group on Thursdays. Her story is hers. It doesn't belong in a progress note.",
             need_label="What really happened:"),
        dict(name="Team lead", where="Signs off and builds the log",
             facts_label="Your job:",
             facts=["Keep time and make sure every role speaks.",
                    "Run the four checks on every note: accurate, objective, safe and private, professional.",
                    "Build the referral log and write the team's best progress note."],
             extra="<strong>Only you know:</strong> Yvonne has asked to read her file. Program policy allows participants to see their own records."),
    ],
    steps=[
        dict(label="In role, on your own", desc="read your weak note or referral and what really happened. List every problem."),
        dict(label="Team huddle", desc="run the four checks on every note and rewrite each one together."),
        dict(label="Plan and present", desc="write one strong progress note, a safe referral email, and a referral log, then present."),
        dict(label="Debrief", desc="step out of role and talk about what it's like to read what others write about you."),
    ],
    step_slides=[
        dict(eyebrow="Step 1 · on your own, in role", title="Find the problems",
             body="""  <ul>
    <li>Read your weak note or referral</li>
    <li>Read what really happened</li>
    <li>List every problem: labels, guesses, location, over-sharing, missing next steps</li>
    <li>Write your own rewrite first</li>
  </ul>""",
             notes="Learners will spot the labels quickly. Push them to find the safety problems."),
        dict(eyebrow="Step 2 · team huddle", title="Check and fix",
             body="""  <div class="cols">
    <div>
      <ol>
        <li>Each role reads its note out loud</li>
        <li>Run the four checks</li>
        <li>Rewrite it together</li>
        <li>Ask: “Would Yvonne be okay reading this?”</li>
      </ol>
    </div>
    <div class="box c1"><h3>Safety first</h3>Which note could put Yvonne in danger if the wrong person saw it?</div>
  </div>""",
             notes="The housing note includes her confidential address. The referral email shares her trafficking history and immigration status without consent. Both are serious."),
        dict(eyebrow="Step 3 · plan and present", title="One strong note, one safe referral, one log",
             body="""  <ul>
    <li>Write <strong>one progress note</strong> for the facilitator's 10/14 meeting</li>
    <li>Rewrite the <strong>referral email</strong> within what Yvonne agreed to share</li>
    <li>Build the <strong>referral log</strong> for this week</li>
  </ul>
  <div class="box c2" style="margin-top:18px">Present in 2 minutes. Read your referral email out loud.</div>""",
             notes="Ask the class: would Yvonne be comfortable if she read each team's email?"),
    ],
    debrief=dict(questions=["Which note would hurt Yvonne most if the wrong person read it?",
                            "What did you leave out, and why?",
                            "How would you explain to Yvonne who can see her file?",
                            "How will you write about women from your own community?"],
                 notes="Return to the opening lists. Did your team's notes say what you'd want your own file to say?"),
    apply_line="Show what you learned, then reflect on how records follow women.",
    own_words="“A referral works better when …”",
    exit_ticket=["Name the four checks before you save a note.",
                 "Rewrite as a fact: “She was dramatic.”",
                 "One thing you'll never put in a progress note."],
    packet_instructions="Print one packet per team. Cut the role cards apart and give one to each person. The Team lead builds the referral log and the final progress note.",
    worksheet=dict(
        title="Note and referral fixes",
        instructions="For each weak note or referral, list the problems and your team's fix.",
        columns=[("From", 22), ("The problems", 34), ("Our fix", 0)],
        rows=5,
        first_col=["Workforce facilitator", "Housing advocate", "Legal advocate (email)", "Health navigator (log)", "Peer mentor"],
        plan=[("Our progress note (what happened, progress, next steps):", 3),
              ("Our referral email (subject line and body):", 3),
              ("Referral log: date, referred to, for, consent, follow-up date:", 2)],
    ),
    team_notes=dict(step1_columns=["Role", "Problems in my note or referral", "My first rewrite"],
                    step1_widths=[1.8, 2.45, 2.45], step2_widths=[1.6, 2.4, 2.7]),
    assignment=dict(
        intro="Capture what your team fixed for Yvonne, write a progress note and referral, then reflect on how records follow women.",
        parts=[
            dict(title="Your note", summary="The problems in your role's note and your rewrite.",
                 note="Answer from the point of view of the role you played in class.",
                 items=[dict(type="roles"),
                        dict(type="q", text="List three problems in your role's note or referral. Name the check each one fails.", h=0.9,
                             hint="(Accurate, objective, safe and private, or professional.)"),
                        dict(type="q", text="Rewrite it so it passes all four checks.", h=1.2)]),
            dict(title="Progress note, referral, and log", summary="One strong note, a safe referral email, and a referral log.",
                 note="Use your team's worksheet from class. You may improve on it.",
                 items=[dict(type="grid", text="Write the progress note for the facilitator's 10/14 meeting.",
                             columns=["", "Note"], widths=[1.4, 5.3], rows=3, h=0.8,
                             first_col=["What happened", "Progress", "Next steps"]),
                        dict(type="q", text="Rewrite the referral email to the training program, within what Yvonne agreed to share. Include a subject line.", h=1.3),
                        dict(type="grid", text="Fill in the referral log for this week.",
                             columns=["Date", "Referred to", "For", "Consent?", "Follow-up"], widths=[0.9, 1.6, 1.8, 1.0, 1.4], rows=2, h=0.45)]),
            dict(title="Records follow women", summary="How records have affected you or women you know, in your own words.",
                 items=[dict(type="q", text="Records can follow women into court, custody cases, and jobs. Has a record or label ever affected you or a woman close to you? How will that shape the way you write about the women you support?",
                             h=2.2, hint=REFLECT_HINT),
                        dict(type="q", text="Finish this sentence: “A referral works better when …”", h=0.8)]),
        ],
        rubric_full=[
            ["Your note (Part 1)", "Three real problems matched to the right check, and a rewrite that passes all four.",
             "Some problems found, or the rewrite still has a problem.", "Missing."],
            ["Progress note (Part 2 table)", "Facts, progress with strengths, and next steps with who and when.",
             "Sections incomplete.", "Missing, or uses labels or location."],
            ["Referral and log (Part 2)", "A professional email that shares only what Yvonne agreed to, and a complete log.",
             "Email or log partly correct.", "Shares information without consent, or missing."],
            ["Reflection (Part 3)", "Thoughtful, specific, and in the learner's own words.",
             "General, or short.", "Missing, or not in the learner's own words."],
        ],
        parts12_desc="your note, then the team's progress note, referral, and log.",
        reflection_title="Records follow women",
        reflection_slide="Has a record or label ever affected you or a woman close to you? How will that shape the way you write about the women you support?",
    ),
))

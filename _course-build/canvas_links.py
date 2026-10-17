"""Canvas assignment links for the "Submit in Canvas" buttons (from the grading script's "Show assignment links").

Community Practitioner = course 409, Survivor Workforce Facilitator = course 410.
"""
BASE = "https://thechartacademy.instructure.com/courses/"
IDS = {
    "cp": {"M01": 2537, "M02": 2538, "M03": 2539, "M04": 2540, "M05": 2541, "M06": 2542, "M07": 2543, "M08": 2544,
           "J1": 2545, "J2": 2546, "J3": 2547, "J4": 2548, "J5": 2549, "J6": 2550},
    "swf": {"M01": 2551, "M02": 2552, "M03": 2553, "M04": 2554, "M05": 2555, "M06": 2556, "M07": 2557, "M08": 2558,
            "J1": 2559, "J2": 2560, "J3": 2561, "J4": 2562, "J5": 2563, "J6": 2564},
}
COURSE = {"cp": 409, "swf": 410}


def link(code, key):
    return f"{BASE}{COURSE[code]}/assignments/{IDS[code][key]}"

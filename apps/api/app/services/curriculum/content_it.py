"""IT001 — Information Technology Essentials.

A compact, data-driven course bundle in the same importer contract as the
PHY211 / CSE014 bundles: pure JSON-able Python dictionaries. Adding a new
lesson or a new material is editing this file — the importer (``seed.py``)
re-imports idempotently on next boot.

Each bundle is one module + one lesson. Materials (videos, links, notes) live
in ``resources``; the course-detail Materials tab reads them through the
catalog API and never hard-codes a single thing in the frontend.

Content blocks intentionally carry NO ``sort_order``: the importer assigns
sequential offsets (summary blocks follow teaching blocks), which keeps
re-imports collision-free.
"""

from __future__ import annotations

COURSE_CODE = "IT001"
COURSE_TITLE = "Information Technology Essentials"
COURSE_CREDITS = 2
COURSE_DESCRIPTION = (
    "Information Technology Essentials (IT001) — a compact first-year "
    "foundation: what a computer system is, how networks and the internet "
    "work, how to stay safe online, and the everyday data & productivity "
    "tools you will use through your degree. Materials are curated per lesson."
)

DEPARTMENT_CODE = "CS"
DEPARTMENT_NAME = "Computer Science"
FACULTY_CODE = "ENG"
FACULTY_NAME = "Faculty of Engineering"

MODULE = {
    "code": "M1",
    "title": "Module 1 — Foundations of Information Technology",
    "description": (
        "Computer systems, networking and security, and data & productivity "
        "tools — enough theory to operate confidently and enough practical "
        "practice to use the tools well."
    ),
    "sort_order": 1,
}

COMPETENCIES = [
    {
        "code": "it-computer-systems",
        "title": "Computer systems and hardware",
        "description": "Explain the role of CPU, memory and storage and how an operating system coordinates them.",
        "taxonomy_level": "UNDERSTAND",
        "sort_order": 1,
    },
    {
        "code": "it-networking-security",
        "title": "Networks, the internet and security",
        "description": "Describe LAN/WAN, IP and DNS, and apply safe online behaviour against common threats.",
        "taxonomy_level": "UNDERSTAND",
        "sort_order": 2,
    },
    {
        "code": "it-data-tools",
        "title": "Data and productivity tools",
        "description": "Use spreadsheets, word processors and plain structured files to organise small datasets.",
        "taxonomy_level": "APPLY",
        "sort_order": 3,
    },
]

# --- Lesson contents -----------------------------------------------------

IT1_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "A computer is a system",
        "body": (
            "A computer is not a single magical box — it is a system etched "
            "into hardware and coordinated by software. At its core sit four "
            "kinds of components: **input** devices (keyboard, mouse, camera, "
            "microphone), **processing** (the CPU), **storage** (SSDs and hard "
            "drives), and **output** (screen, speakers, printer). The operating "
            "system is the software whose only job is to coordinate all of it: "
            "it schedules the CPU, hands memory to running programs, and hides "
            "the messy details of each device behind standard interfaces."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "CPU, RAM and storage are not the same thing",
        "body": (
            "The **CPU** *executes* instructions. **RAM** (main memory) *holds* "
            "the program and its data while it runs — it is fast and volatile, "
            "so it forgets everything when power goes away. **Storage** (SSD, "
            "HDD) keeps files permanently. A common beginner mistake is calling "
            "a laptop '16 GB' of memory 'a big hard drive' — memory and storage "
            "answer different needs."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Hardware at a glance",
        "body": (
            "| Component | Job | Volatile? |\n"
            "|---|---|---|\n"
            "| CPU | Executes instructions | — |\n"
            "| RAM | Program + working data | Yes — forgotten on power-off |\n"
            "| SSD/HDD | Permanent files and installed software | No |\n"
            "| GPU | Parallel math for graphics (and ML) | — |\n"
            "| Motherboard | Connects every component | — |"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Deciding what to buy: 8 GB vs 512 GB",
        "body": (
            "A student sees '8 GB RAM, 512 GB SSD' and asks which number is "
            "'the memory'. Both are memory, but of kinds: **8 GB of RAM** sets "
            "how much work the machine can hold *at once* (too little and it "
            "thrashes), while **512 GB of SSD** sets what survives *between "
            "sessions* (browser, files, lectures). For an everyday machine you "
            "want enough of both — they are not interchangeable."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "How the operating system provides order",
        "body": (
            "An OS like Windows, macOS, Ubuntu or ChromeOS gives each running "
            "program its own slice of memory, fair slices of CPU time, and a "
            "common way to talk to files and devices. Because of that sharing, "
            "app permissions and file ownership exist: the OS enforces *who may "
            "do what*. That is also why you install one program at a time and "
            "why an update can require a restart — the OS is the referee, not "
            "just a launcher."
        ),
    },
]

IT1_SUMMARY = [
    {
        "section_type": "SUMMARY",
        "title": "Key ideas",
        "body": (
            "- A computer = input + processing + storage + output, coordinated "
            "by an operating system.\n"
            "- RAM is fast and volatile; storage is permanent and slower.\n"
            "- The OS shares CPU, memory and devices between programs and "
            "enforces permissions."
        ),
    },
]

IT1_PRACTICE = [
    {
        "level": "UNDERSTAND",
        "prompt": "Which of these stores data permanently, even when the machine is off?",
        "options": [
            "RAM",
            "SSD or hard disk",
            "CPU cache",
            "Registers inside the CPU",
        ],
        "correct_index": 1,
        "explanation": "RAM, cache and registers are volatile — they forget everything at power-off. SSD/hard disk keeps data.",
        "competency_code": "it-computer-systems",
        "difficulty": 1,
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What is the operating system's main job?",
        "options": [
            "To build the web pages you browse",
            "To coordinate hardware and software so programs share the machine safely",
            "To store your files in the cloud",
            "To make the CPU faster",
        ],
        "correct_index": 1,
        "explanation": "The OS is the referee: it schedules the CPU, hands out memory, and mediates access to devices and files.",
        "competency_code": "it-computer-systems",
        "difficulty": 1,
    },
]

IT2_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "Networks and the internet, in one picture",
        "body": (
            "A **LAN** (local area network) links devices in one building — your "
            "home or a campus lab. A **WAN** links LANs over long distances; the "
            "internet is the largest public WAN. Every device on a network gets "
            "an **IP address** (e.g. `192.168.1.10`) so messages can be routed "
            "to it, and **packets** carry chunks of every message between "
            "machines — that is why any two nodes can talk even while thousands "
            "of conversations cross the same wires."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "You type a name; the DNS looks up the number",
        "body": (
            "Humans remember `university.edu`; routers need numbers. The **DNS** "
            "(Domain Name System) is the internet's phone book: it translates a "
            "hostname like `www.university.edu` into an IP address, and your "
            "browser then opens a connection to that address. If DNS fails, 'the "
            "site loads slowly or not at all' is often really 'the name could "
            "not be resolved'."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Security threats, translated",
        "body": (
            "| Threat | What it looks like | Defence |\n"
            "|---|---|---|\n"
            "| Phishing | Fake email/website urging a login or payment | Check the sender + URL; never click through email |\n"
            "| Malware | Attachments or downloads that run code | Keep software updated; scan downloads |\n"
            "| Password reuse | One leaked password unlocks many sites | Unique passwords per site + a password manager |\n"
            "| Public Wi-Fi sniffing | Attacker on the same network | Use HTTPS; avoid sensitive logins on open Wi-Fi |"
        ),
    },
    {
        "section_type": "WARNING",
        "title": "The 'urgent' message is the giveaway",
        "body": (
            "Phishing works by urgency: *'Your account will be closed in 24 "
            "hours — click here.'* Legitimate institutions almost never ask for "
            "a password by email. Slow down: examine the sender address and the "
            "link target before you click. When in doubt, type the address "
            "yourself and log in through the real site."
        ),
    },
]

IT2_SUMMARY = [
    {
        "section_type": "SUMMARY",
        "title": "Key ideas",
        "body": (
            "- LANs are local, WANs connect them; the internet is the big WAN.\n"
            "- IP addresses address machines; DNS turns hostnames into IPs.\n"
            "- Phishing + reused passwords + open Wi-Fi are the real-world "
            "threats; update, verify and use unique passwords."
        ),
    },
]

IT2_PRACTICE = [
    {
        "level": "UNDERSTAND",
        "prompt": "What does the DNS do?",
        "options": [
            "It encrypts all network traffic",
            "It translates human-readable hostnames into IP addresses",
            "It assigns IP addresses to your hardware permanently",
            "It blocks every website you visit",
        ],
        "correct_index": 1,
        "explanation": "The DNS is the internet's phone book: it maps names like university.edu to IP addresses that routers use.",
        "competency_code": "it-networking-security",
        "difficulty": 1,
    },
    {
        "level": "UNDERSTAND",
        "prompt": "An email says your bank account will close unless you click the link and enter your password. What should you do?",
        "options": [
            "Click the link immediately — it is urgent",
            "Forward it to friends in case they missed it",
            "Verify: check the sender and the real bank site, never log in through the email link",
            "Reply with your password so the bank confirms it is you",
        ],
        "correct_index": 2,
        "explanation": "Urgency is the classic phishing trigger. Verify out-of-band (visit the official site, call the bank) and never enter credentials from an email link.",
        "competency_code": "it-networking-security",
        "difficulty": 1,
    },
]

IT3_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "Data tools: the same ideas, different boxes",
        "body": (
            "A spreadsheet, a word processor and a plain CSV file feel "
            "different but share a core idea: **data is arranged in a grid and "
            "formats describe meaning**. A spreadsheet cell is part of a "
            "table (columns = fields, rows = records); a CSV file is that table "
            "saved as plain comma-separated text; a word-processing document "
            "combines content with layout (headings, styles, page setup). Once "
            "you see tables everywhere, moving between tools is easy."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Cell references turn static numbers into living tables",
        "body": (
            "In a spreadsheet, write `=B2*C2` instead of `=200*0.15`. The "
            "formula reads *values from cells* rather than hard-coded numbers, "
            "so when you change B2 the result updates. That is the whole power "
            "of computation over paper: **the table reacts**. `SUM`, `AVERAGE`, "
            "`IF` and filters are the everyday toolkit for small datasets."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "File types you will meet",
        "body": (
            "| Type | Genre | Opening it | When to use |\n"
            "|---|---|---|---|\n"
            "| CSV | Plain text table | Any editor or spreadsheet | Data exchange, imports |\n"
            "| XLSX | Spreadsheet workbook | Excel, LibreOffice, Sheets | Tables + formulas |\n"
            "| DOCX | Word document | Word, LibreOffice, Docs | Essays and reports |\n"
            "| PDF | Fixed layout | Any reader | Final documents that must not reflow |"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "From rows to insight: a tiny grade sheet",
        "body": (
            "Take attendance `scores.csv` with columns `student, quiz1, quiz2`. "
            "In a spreadsheet add `=AVERAGE(B2:C2)` for each row to get a "
            "personal average, then a filter to show only rows below a "
            "threshold. Two minutes of real editing beats a page of theory — "
            "open the file, add the formula, watch the column fill in."
        ),
    },
]

IT3_SUMMARY = [
    {
        "section_type": "SUMMARY",
        "title": "Key ideas",
        "body": (
            "- Tables are everywhere: columns are fields, rows are records.\n"
            "- Formulas reference cells so tables recompute when inputs change.\n"
            "- CSV/XLSX/DOCX/PDF are different formats for different jobs; each "
            "is just data plus meaning."
        ),
    },
]

IT3_PRACTICE = [
    {
        "level": "APPLY",
        "prompt": "Cell B2 holds 200 and C2 holds 0.15. Which formula always reflects later edits to those cells?",
        "options": ["=200*0.15", "=B2*C2", "=200*C2", "=B2*15% permanently stored as 30"],
        "correct_index": 1,
        "explanation": "Only =B2*C2 reads live cell values, so the result updates when either cell changes.",
        "competency_code": "it-data-tools",
        "difficulty": 2,
    },
    {
        "level": "UNDERSTAND",
        "prompt": "You must email your university a report that must look identical on every screen. Which format?",
        "options": ["CSV", "XLSX", "PDF", "PY"],
        "correct_index": 2,
        "explanation": "PDF fixes the layout — everything else reflows or is editable, so the reader may see it differently.",
        "competency_code": "it-data-tools",
        "difficulty": 1,
    },
]

# --- Materials (resources) ------------------------------------------------

def _video(title, description, url, duration_seconds=None, sort_order=1):
    return {
        "resource_type": "VIDEO",
        "title": title,
        "description": description,
        "external_url": url,
        "duration_seconds": duration_seconds,
        "sort_order": sort_order,
    }


IT1_MATERIALS = [
    _video(
        "Computers and the Internet — how it all fits",
        "Khan Academy's Computers and the Internet course: bits, hardware, "
        "operating systems and networks.",
        "https://www.khanacademy.org/computing/computers-and-internet",
        6900,
        1,
    ),
    _video(
        "How Computers Work (Crash Course CS #4)",
        "The CPU, memory and the fetch–decode–execute loop in seven minutes.",
        "https://www.youtube.com/watch?v=O5nskjZ_GoI",
        420,
        2,
    ),
    _video(
        "Random-access memory — reference",
        "What RAM does, why it is volatile, and how it differs from storage.",
        "https://en.wikipedia.org/wiki/Random-access_memory",
        None,
        3,
    ),
]

IT2_MATERIALS = [
    _video(
        "The Internet: how it works (Khan Academy)",
        "Packets, IP addresses and the DNS — the internet as a postal service.",
        "https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet",
        2700,
        1,
    ),
    _video(
        "Stay Safe Online — security basics",
        "The National Cybersecurity Alliance's practical checklist for safer "
        "browsing and accounts.",
        "https://staysafeonline.org/resources/",
        2400,
        2,
    ),
    _video(
        "Domain Name System — reference",
        "How hostnames map to IP addresses and what an authoritative lookup is.",
        "https://en.wikipedia.org/wiki/Domain_Name_System",
        None,
        3,
    ),
]

IT3_MATERIALS = [
    _video(
        "LibreOffice Documentation — Calc & Writer guides",
        "Full, free documentation for spreadsheet and word-processing basics.",
        "https://documentation.libreoffice.org/en/english-documentation/",
        None,
        1,
    ),
    _video(
        "Comma-separated values — reference",
        "The CSV format: plain-text tables and why they are everywhere in data "
        "exchange.",
        "https://en.wikipedia.org/wiki/Comma-separated_values",
        None,
        2,
    ),
]

# --- Bundle assembly ------------------------------------------------------

IT1_LINKS = [{"code": "it-computer-systems", "role": "teaches"}]
IT2_LINKS = [{"code": "it-networking-security", "role": "teaches"}]
IT3_LINKS = [{"code": "it-data-tools", "role": "teaches"}]

IT1_LESSON = {
    "code": "IT1",
    "title": "Computers, Hardware and Operating Systems",
    "description": (
        "What a computer system is, how the CPU, RAM, storage and motherboard "
        "fit together, and how the operating system coordinates them."
    ),
    "estimated_minutes": 40,
    "difficulty": "beginner",
    "objectives": [
        "Identify the four roles (input, processing, storage, output) in any computer.",
        "Explain the difference between RAM and storage with a concrete example.",
        "Describe what an operating system does and why permissions exist.",
    ],
    "prerequisites": ["No prerequisites — a starting lesson."],
    "sort_order": 1,
}

IT2_LESSON = {
    "code": "IT2",
    "title": "Networks, the Internet and Security",
    "description": (
        "LANs and WANs, IP addressing and DNS, and the everyday security "
        "practices that keep you safe online."
    ),
    "estimated_minutes": 45,
    "difficulty": "beginner",
    "objectives": [
        "Distinguish LAN and WAN and sketch how the internet moves packets.",
        "Explain what DNS does and why hostnames need it.",
        "Recognise phishing and apply safe habits for passwords and public Wi-Fi.",
    ],
    "prerequisites": ["IT1 — Computers, Hardware and Operating Systems."],
    "sort_order": 2,
}

IT3_LESSON = {
    "code": "IT3",
    "title": "Data and Productivity Tools",
    "description": (
        "Spreadsheets that compute, documents that lay out, and plain-text "
        "tables — the everyday toolkit for handling small datasets."
    ),
    "estimated_minutes": 45,
    "difficulty": "beginner",
    "objectives": [
        "Read a table as fields and records in a spreadsheet or CSV.",
        "Write formulas that reference cells so tables recompute live.",
        "Choose between CSV, XLSX, DOCX and PDF for a task.",
    ],
    "prerequisites": ["IT1 — Computers, Hardware and Operating Systems."],
    "sort_order": 3,
}


def _bundle(module, lesson, contents, summary, practice, links, materials, competency_codes, competencies):
    return {
        "course": {
            "code": COURSE_CODE,
            "title": COURSE_TITLE,
            "credits": COURSE_CREDITS,
            "description": COURSE_DESCRIPTION,
            "department_code": DEPARTMENT_CODE,
            "department_name": DEPARTMENT_NAME,
            "faculty_code": FACULTY_CODE,
            "faculty_name": FACULTY_NAME,
            "module": module,
            "lesson": lesson,
            "competencies": competencies,
            "competency_prerequisites": [],
            "lesson_competencies": links,
            "lesson_contents": contents,
            "summary_contents": summary,
            "resources": materials,
            "practice_items": practice,
        }
    }


BUNDLES = [
    _bundle(
        MODULE,
        IT1_LESSON,
        IT1_CONTENTS,
        IT1_SUMMARY,
        IT1_PRACTICE,
        IT1_LINKS,
        IT1_MATERIALS,
        ["it-computer-systems"],
        COMPETENCIES,
    ),
    _bundle(
        MODULE,
        IT2_LESSON,
        IT2_CONTENTS,
        IT2_SUMMARY,
        IT2_PRACTICE,
        IT2_LINKS,
        IT2_MATERIALS,
        ["it-networking-security"],
        COMPETENCIES,
    ),
    _bundle(
        MODULE,
        IT3_LESSON,
        IT3_CONTENTS,
        IT3_SUMMARY,
        IT3_PRACTICE,
        IT3_LINKS,
        IT3_MATERIALS,
        ["it-data-tools"],
        COMPETENCIES,
    ),
]
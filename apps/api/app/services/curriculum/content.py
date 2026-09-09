"""PHY211 — Physics, Module 1, Lecture 1: Electric Charge.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 1, Fall 2024 — 'Electric
Charge: Properties, Quantization, and Charging Methods').

This is the single source of truth imported into the DB by
``curriculum.seed`` (bootstrap path) and the CLI importer. The API never
renders the whole bundle on one page: lecture, summary, videos, and practice
are served as purpose-built views.

Fields are deliberately plain JSON-able Python so importing a new lesson is
just adding another bundle to the importer's bundle list.
"""

from __future__ import annotations

from .content_final import BUNDLE as BUNDLE_FINAL
from .content_l2 import BUNDLE as BUNDLE_L2
from .content_l3 import BUNDLE as BUNDLE_L3
from .content_l4 import BUNDLE as BUNDLE_L4
from .content_l5 import BUNDLE as BUNDLE_L5
from .content_l6 import BUNDLE as BUNDLE_L6
from .content_l7 import BUNDLE as BUNDLE_L7
from .content_l8 import BUNDLE as BUNDLE_L8
from .content_l9 import BUNDLE as BUNDLE_L9
from .content_l10 import BUNDLE as BUNDLE_L10
from .content_l11 import BUNDLE as BUNDLE_L11
from .content_l12 import BUNDLE as BUNDLE_L12
from .content_review1 import BUNDLE as BUNDLE_REVIEW1
from .content_review2 import BUNDLE as BUNDLE_REVIEW2
from .content_math1 import BUNDLES as BUNDLES_MATH1
from .content_cse014 import BUNDLES as BUNDLES_CSE014
from .content_it import BUNDLES as BUNDLES_IT

COURSE_CODE = "PHY211"
COURSE_TITLE = "Physics"
COURSE_CREDITS = 3
COURSE_DESCRIPTION = (
    "General Physics (PHY211) — first-year core course. Chapter 1 of Module "
    "1 covers electrostatics: the properties of electric charge, its "
    "quantization, unit conversions, and the three charging methods, ending "
    "in charge transfer and the authority of evidence. Built on the "
    "competency-graph and evidence-based learning model of the Arete platform."
)

DEPARTMENT_CODE = "PHYS"
DEPARTMENT_NAME = "Physics"
FACULTY_CODE = "ENG"
FACULTY_NAME = "Faculty of Engineering"

MODULE = {
    "code": "M1",
    "title": "Module 1 — Foundations of Electrostatics",
    "description": (
        "Chapter 1: Electric Force & Electric Field. Fundamentals of charge, "
        "its quantization, and the three charging methods."
    ),
    "sort_order": 1,
}

LESSON = {
    "code": "L1",
    "title": "Electric Charge: Properties, Quantization, and Charging Methods",
    "description": (
        "Lecture 1 — the vocabulary and rules every later stage of Chapter 1 "
        "(force, field) assumes: the elementary charge, quantization, unit "
        "conversions, and rubbing / induction / conduction."
    ),
    "estimated_minutes": 75,
    "difficulty": "easy-medium",
    "objectives": [
        "State the fundamental unit of charge e = 1.6 × 10⁻¹⁹ C and what Millikan's 1909 discovery revealed.",
        "List the key properties of electric charge, the attraction/repulsion rule, and the SI unit (coulomb).",
        "Explain what 'charge is quantized' means and apply Q = ±Ne.",
        "Count the electrons (or protons) in a given total charge, handling signs correctly.",
        "Convert fluently between coulombs, milli-, micro-, nano-, and picocoulombs.",
        "Describe charging by rubbing and predict the sign of each object for glass–silk and plastic–wool.",
        "Describe the step-by-step induction procedure (including grounding) and predict the induced sign.",
        "Describe charging by conduction and predict the resulting sign.",
        "Apply Q ∝ r, q′ = q_t / r_t, and q_i′ = q′ × r_i to find final charges on touching conducting spheres.",
    ],
    "prerequisites": [
        "The basic structure of the atom (protons and electrons).",
        "SI prefixes and powers of ten.",
        "Elementary algebra.",
        "The qualitative difference between a conductor and an insulator.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
# section_type ∈ TEXT / FORMULA / EXAMPLE / KEY_POINT / WARNING / TABLE /
# IMAGE / VIDEO / SUMMARY / DIFFICULT_CONCEPT
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Charge is not continuous. It comes in identical, indivisible packets, and every "
            "charge ever measured is a whole-number multiple of one tiny unit — the elementary "
            "charge e. In 1909 Robert Millikan discovered that whenever an object becomes "
            "charged, the amount it carries is always a multiple of e."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Elementary charge",
        "body": "e = 1.6 × 10⁻¹⁹ C",
        "metadata": {
            "meaning": "The smallest possible magnitude of charge; the magnitude of the electron's and proton's charge.",
            "when_used": "Every quantization or electron-counting problem.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Quantization rule",
        "body": "Charge is built from identical units of magnitude e = 1.6 × 10⁻¹⁹ C. There is no such thing as a fraction of an elementary charge.",
    },
    {
        "section_type": "TEXT",
        "title": "2. Properties of Electric Charge",
        "body": (
            "There are exactly two kinds of charge. The electron is the smallest negative "
            "charge (q_e = −e), the proton the smallest positive charge (q_p = +e). Same-sign "
            "charges repel; opposite-sign charges attract. The SI unit of charge is the coulomb (C). "
            "Any total charge is an integer multiple of e:  Q = ±Ne, so the allowed values are "
            "±1e, ±2e, ±3e, … — nothing in between."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Quantization of charge",
        "body": "Q = ±Ne   (Q: total charge, N: a whole number of elementary charges, e = 1.6 × 10⁻¹⁹ C)",
        "metadata": {"when_used": "Checking whether a charge is physically possible; counting charge carriers."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Physical and impossible charges",
        "body": (
            "A charge of +3.2 × 10⁻¹⁹ C is physically meaningful: it equals exactly 2e. "
            "A charge of +2.4 × 10⁻¹⁹ C is not — that would be 1.5e, and half-packets don't exist."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Interaction rule",
        "body": "Like repels, unlike attracts, and every charge in nature is Q = ±Ne with N a whole number.",
    },
    {
        "section_type": "TEXT",
        "title": "3. Quantization in Action: Counting Electrons",
        "body": (
            "Rearranging Q = ±Ne turns any charge into a count of elementary particles: "
            "N = Q/(±e). For a negative total charge Q, N = Q/(−e) — both negatives cancel, so N "
            "— a count of objects — always comes out positive. Getting a negative number of "
            "electrons is a guaranteed sign of a sign-handling error."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Counting electrons",
        "body": "N = Q / (±e)",
        "metadata": {"when_used": "Whenever a charge is given and a particle count is requested."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Sphere carrying −64 μC",
        "body": (
            "Convert: Q = −64 × 10⁻⁶ C. Then N = (−64 × 10⁻⁶) / (−1.6 × 10⁻¹⁹). "
            "64/1.6 = 40 and 10⁻⁶/10⁻¹⁹ = 10¹³, so N = 40 × 10¹³ = 4 × 10¹⁴ electrons. "
            "Sanity check: N is positive, as any count must be."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "The Prefix Staircase",
        "body": "| Unit | Symbol | Value |\n|---|---|---|\n| 1 millicoulomb | 1 mC | 10⁻³ C |\n| 1 microcoulomb | 1 μC | 10⁻⁶ C |\n| 1 nanocoulomb | 1 nC | 10⁻⁹ C |\n| 1 picocoulomb | 1 pC | 10⁻¹² C |",
        "metadata": {
            "note": "Each step down the staircase divides the charge by 1000 — and therefore divides the electron count by 1000 too.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Unit conversions",
        "body": "1 mC = 10⁻³ C   1 μC = 10⁻⁶ C   1 nC = 10⁻⁹ C   1 pC = 10⁻¹² C",
        "metadata": {"when_used": "Before any calculation involving a prefixed charge."},
    },
    {
        "section_type": "TEXT",
        "title": "5. Charging Method I: Rubbing (Friction) — for Insulators",
        "body": (
            "Rubbing two different materials transfers electrons from one to the other, leaving "
            "one object positive and the other negative. Glass rubbed with silk: electrons move "
            "from the rod to the silk — rod positive, silk negative. Plastic rubbed with wool: "
            "electrons move from wool to plastic — plastic negative, wool positive. Total charge "
            "is unchanged; it has only been redistributed. Rubbing charges insulators."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Friction moves electrons only",
        "body": "The object that loses electrons becomes positive; the one that gains them becomes negative.",
    },
    {
        "section_type": "TEXT",
        "title": "6. Charging Method II: Induction — for Conductors",
        "body": (
            "A conductor can be given a net charge without any contact at all. Procedure for a "
            "neutral metal sphere: (1) charge a rod (e.g. plastic on wool → negative); (2) bring "
            "the rod near, never touching; (3) free electrons redistribute — repelled to the far "
            "end, leaving the near side positive (the sphere stays neutral overall); (4) connect "
            "the far end to the Earth — the repelled electrons drain into the ground; (5) "
            "disconnect the ground wire FIRST, then remove the rod — the sphere keeps a net "
            "positive charge. Induction always leaves the target with the OPPOSITE sign of the "
            "charging object: negative rod → positive sphere, positive rod → negative sphere."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Induction never touches",
        "body": (
            "A negatively charged rod near a grounded sphere: electrons flee into the Earth, the "
            "ground wire is cut, the rod is removed — the sphere ends positive even though the "
            "rod never touched it and never gave it a single charge."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Induction = no contact + opposite sign",
        "body": "The electrons that move travel between the sphere and the ground, never between the rod and the sphere. Order matters: ground → drain → disconnect → remove.",
    },
    {
        "section_type": "TEXT",
        "title": "7. Charging Method III: Conduction — for Conductors",
        "body": (
            "Conduction charges by direct contact: part of the charge flows onto the neutral "
            "object, which ends up with the SAME sign as the charging object. Identical spheres "
            "share charge equally. General case — spheres of different sizes: the shared charge "
            "is proportional to the radius, Q ∝ r. Bigger sphere → bigger share. "
            "Machinery: q′ = q_t / r_t = (q₁ + q₂ + ⋯)/(r₁ + r₂ + ⋯), then q_i′ = q′ × r_i, "
            "and q₁′/q₂′ = r₁/r₂."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Charge per unit radius after contact",
        "body": "q′ = q_t / r_t = (q₁ + q₂ + q₃ + ⋯) / (r₁ + r₂ + r₃ + ⋯)",
        "metadata": {
            "when_used": "Conducting spheres brought into contact with one another.",
            "assumptions": "Negative charges enter the sum with a minus sign; sharing is proportional to radius.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Final charge on each sphere",
        "body": "q_i′ = q′ × r_i   (and  q₁′/q₂′ = r₁/r₂)",
        "metadata": {"when_used": "Immediately after computing q′. Verify final charges sum back to q_t."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Three spheres touched together",
        "body": (
            "Radii 3 m, 2 m, 1 m with charges 10 C, 20 C, −10 C. q_t = 10 + 20 − 10 = 20 C; "
            "r_t = 3 + 2 + 1 = 6 m; q′ = 20/6 ≈ 3.333 C/m. Final charges: 3.333 × 3 = 10 C, "
            "3.333 × 2 ≈ 6.667 C, 3.333 × 1 ≈ 3.333 C. Check: 10 + 6.667 + 3.333 = 20 C ✓,"
            " and ratios 10 : 6.667 : 3.333 = 3 : 2 : 1 = radii ✓."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Conduction = contact + same sign",
        "body": "Contact ⇒ same sign as the charger ⇒ the split follows the radii, not a 50/50 coin flip. Only identical spheres end up equal.",
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — Counting electrons on a charged sphere",
        "body": (
            "Sphere carries −64 μC. (1) Convert: Q = −64 × 10⁻⁶ C. (2) Q = −Ne. "
            "(3) N = (−64 × 10⁻⁶)/(−1.6 × 10⁻¹⁹). (4) 64/1.6 = 40 and 10⁻⁶/10⁻¹⁹ = 10¹³, "
            "so N = 40 × 10¹³ = 4 × 10¹⁴ electrons. (5) N is positive — a count always is."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — Electron counts across the prefix staircase",
        "body": (
            "−1 mC → 6.25 × 10¹⁵ electrons; −1 μC → 6.25 × 10¹²; −1 nC → 6.25 × 10⁹; "
            "−1 pC → 6.25 × 10⁶. Every step down the staircase removes three powers of ten "
            "from both the charge and the electron count."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — Charge sharing among three spheres",
        "body": (
            "Sphere 1 (r=3 m, 10 C), sphere 2 (r=2 m, 20 C), sphere 3 (r=1 m, −10 C) all touch. "
            "q_t = 10 + 20 − 10 = 20 C; r_t = 6 m; q′ = 20/6 ≈ 3.333 C/m. "
            "q₁′ = 10 C, q₂′ ≈ 6.667 C, q₃′ ≈ 3.333 C. Verify: sum = 20 C ✓; ratios 3:2:1 ✓."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Charge is quantized",
        "body": "Do NOT accept any charge value as possible — Q/e must be a whole number. A charge like 2.4 × 10⁻¹⁹ C is impossible.",
    },
    {
        "section_type": "WARNING",
        "title": "Sign slips when counting electrons",
        "body": "A count of particles cannot be negative. Divide a negative charge by −e so the signs cancel and N > 0.",
    },
    {
        "section_type": "WARNING",
        "title": "Prefix mix-ups",
        "body": "μ = 10⁻⁶, n = 10⁻⁹, p = 10⁻¹², m = 10⁻³. Read the symbol carefully — misreading μ as milli is the classic blunder.",
    },
    {
        "section_type": "WARNING",
        "title": "Induction vs conduction",
        "body": "Induction is precisely the no-contact method and gives the OPPOSITE sign. Conduction requires direct contact and gives the SAME sign.",
    },
    {
        "section_type": "WARNING",
        "title": "Order of operations in induction",
        "body": "Disconnect the ground wire BEFORE removing the rod. Remove the rod first and the electrons flow back — the sphere returns to neutral.",
    },
    {
        "section_type": "WARNING",
        "title": "No 50/50 split for unequal spheres",
        "body": "Charge splits in proportion to radius (Q ∝ r). Only identical spheres split equally — compute q′ = q_t/r_t, then multiply by each radius.",
    },
    {
        "section_type": "WARNING",
        "title": "Negative charges in the total",
        "body": "q_t is an algebraic sum — negative charges subtract. And a neutral sphere contributes its radius (a share of charge) even with q = 0.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Quantization of Charge",
        "body": (
            "Macroscopic charges look smooth, but charge behaves like eggs, not milk: you can have "
            "1, 2, 12 eggs — never 1.5. To test any proposed charge, divide by e; the result must "
            "be an integer. Example: −4.8 × 10⁻¹⁹ C / (−1.6 × 10⁻¹⁹ C) = 3 → yes; −4.0 × 10⁻¹⁹ C "
            "→ 2.5 → no, half-electrons don't exist. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Charging by Induction",
        "body": (
            "The rod never touches the sphere; it just pushes the free electrons around. The ground "
            "wire gives displaced electrons a one-way exit or entrance. Close the exit before the "
            "rod walks away and the sphere keeps the imbalance — opposite sign. Analogy: people "
            "backing away from a 'bouncer' at the door; open the far exit and some leave the room; "
            "close it before the bouncer walks away. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Charge Sharing Proportional to Radius",
        "body": (
            "Spheres in contact don't equalize total charge — they equalize charge-per-radius "
            "(q′ = q_t/r_t), then each gets q′ × r_i. Analogy: connected water tanks — the level "
            "equalizes but the bigger tank holds more water. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Sign Bookkeeping When Counting Electrons",
        "body": (
            "A count is always a positive whole number: if your arithmetic yields "
            "−6.25 × 10¹² electrons, something went wrong. Convert the prefixed unit, write the "
            "charge with its sign, divide by −e for a negative charge (or +e for positive), then "
            "confirm the result is positive. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Metric Prefixes for Charge",
        "body": (
            "Four prefixes spanning twelve orders of magnitude. Learn the staircase: each step "
            "down m → μ → n → p divides by 1000. 0.75 μC = 0.75 × 10⁻⁶ C = 7.5 × 10⁻⁷ C. "
            "Difficulty: EASY."
        ),
    },
]

# --- summary view blocks (rendered only on the /summary route) ---------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Charge comes only in multiples of e = 1.6 × 10⁻¹⁹ C: Q = ±Ne.\n"
            "• Electron: −e. Proton: +e. Like repels; unlike attracts. Unit: coulomb.\n"
            "• Prefix conversions: mC = 10⁻³ C, μC = 10⁻⁶ C, nC = 10⁻⁹ C, pC = 10⁻¹² C.\n"
            "• Count electrons by dividing the charge by e (magnitudes — a count is positive).\n"
            "• Rubbing charges insulators; induction and conduction charge conductors.\n"
            "• Rubbing: glass→silk leaves glass positive; wool→plastic leaves plastic negative.\n"
            "• Induction: no contact, OPPOSITE sign; ground → drain → disconnect → remove.\n"
            "• Conduction: contact, SAME sign; spheres split proportionally to radius (Q ∝ r).\n"
            "• For touching spheres: q′ = q_t/r_t, then q_i′ = q′ × r_i — the pieces must sum back to q_t."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Elementary charge (e) — the fundamental unit of charge, 1.6 × 10⁻¹⁹ C, the indivisible unit discovered by Millikan (1909).\n"
            "• Quantization of charge — every charge is an integer multiple of e: Q = ±Ne.\n"
            "• Repulsive / attractive force — between same-sign / opposite-sign charges.\n"
            "• Coulomb (C) — the SI unit of electric charge.\n"
            "• Rubbing (friction) — charging by transferring electrons between two rubbed insulators.\n"
            "• Induction — charging a conductor without contact via a nearby charge + a ground connection.\n"
            "• Conduction — charging by direct contact; part of the charge flows onto the other object."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• e = 1.6 × 10⁻¹⁹ C — size of the fundamental unit.\n"
            "• Q = ±Ne — quantization.\n"
            "• N = Q/(±e) — counting charge carriers.\n"
            "• q′ = q_t/r_t — shared charge per unit radius after spheres touch.\n"
            "• q_i′ = q′ × r_i — final charge on each sphere.\n"
            "• q₁′/q₂′ = r₁/r₂ — final charges in the ratio of the radii.\n"
            "• Q ∝ r — bigger spheres take bigger shares."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Charge comes in packets of e, so any charge is Q = ±Ne and counting electrons is just "
            "division. Likes repel, unlikes attract. To charge something: RUB an insulator (electrons "
            "hop — glass +, plastic −), INDUCE a conductor (near + ground → opposite sign), or use "
            "CONDUCTION (touch → same sign). When conducting spheres touch, charge spreads in "
            "proportion to radius: q′ = q_t/r_t, each gets q′ × radius, and the pieces must sum back "
            "to the total. Induction: opposite sign, no contact. Conduction: same sign, contact. "
            "Ground before you remove the rod — always."
        ),
    },
]

# --- video lectures (resources; scripts/checks hidden until the /videos view) --
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "Charge Without Touching: How Induction Really Works",
        "description": (
            "The five-step induction procedure, the role of grounding, the sign rule, and why the "
            "ground wire must be disconnected before the rod is removed."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Charging a conductor by induction (procedure, grounding, sign rule, order of operations)",
            "target_student": "First-year university student",
            "objective": "Narrate the five-step induction procedure, predict the induced sign (opposite to the charging object), and explain why the ground wire is disconnected before the rod is removed.",
            "hook": "A negatively charged rod gives a neutral metal sphere a POSITIVE charge without ever touching it — 'sounds impossible, let's watch it step by step.'",
            "explanation_steps": [
                "Review like-repels/unlike-attracts and that conductors contain free electrons.",
                "A charged object NEAR a conductor can redistribute its electrons without transfer.",
                "Five steps with visuals: approach → polarization → ground the far end → disconnect → remove.",
                "Derive the sign rule: opposite sign, always.",
                "Reverse scenario: positive rod → electrons flow from ground onto the sphere → negative.",
            ],
            "common_mistake": "Believing the sphere ends up with the SAME sign as the rod, or that charge flows between rod and sphere.",
            "check": "You have a positively charged rod. Describe, in order, how to charge a neutral metal sphere NEGATIVELY by induction — and state when exactly you disconnect the ground wire.",
            "final_takeaway": "Induction = charge without contact; the ground supplies or removes electrons; disconnect first, remove the rod second; result is always the opposite sign.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "When Spheres Touch: Why the Big One Gets More Charge",
        "description": (
            "Charge sharing by conduction between conducting spheres: Q ∝ r, q′ = q_t/r_t, "
            "q_i′ = q′ × r_i, with built-in verification checks."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Charge sharing by conduction between conducting spheres; Q ∝ r",
            "target_student": "First-year university student",
            "objective": "Compute final charges on touching conducting spheres (including negative initial charges) and verify via conservation and radius ratios.",
            "hook": "'A big sphere with 12 C touches a small neutral sphere. Half and half, right? Wrong.'",
            "explanation_steps": [
                "Conduction basics: contact required; the touched object takes the charger's sign.",
                "Identical spheres → equal split (the familiar special case).",
                "General spheres → charge proportional to radius, Q ∝ r.",
                "Recipe: q_t (algebraic sum) → r_t → q′ = q_t/r_t → q_i′ = q′ × r_i.",
                "Two safety checks: final charges sum to q_t; charge ratios equal radius ratios.",
            ],
            "common_mistake": "Splitting the total 50/50 regardless of radius; forgetting that −10 C subtracts in the total.",
            "check": "Sphere A (radius 4 m, 12 C) touches neutral Sphere B (radius 2 m). What is each final charge — and what's the ratio?",
            "final_takeaway": "Spheres in contact equalize charge per radius, not total charge: q′ = q_t/r_t, multiply by each radius, and the final charges must add back to the original total.",
        },
        "sort_order": 2,
    },
]

# --- practice items (3 levels; answers stay server-side only) ---------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "What does it mean to say that electric charge is 'quantized'? State the value of the fundamental unit of charge.",
        "options": [
            "Charge exists only in integer multiples of e; e = 1.6 × 10⁻¹⁹ C; Q = ±Ne",
            "Charge is continuous; e = 1 C; Q = Ne²",
            "Charge only comes in two fixed amounts, +1 C and −1 C",
            "Quantized means charge cannot move at all",
        ],
        "correct_index": 0,
        "explanation": "Charge exists only in integer multiples of e = 1.6 × 10⁻¹⁹ C — any total charge is Q = ±Ne with N a whole number.",
        "skill": "quantization concept",
        "difficulty": 1,
        "competency_code": "charge-quantization",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Classify each pair as attractive or repulsive: (a) two electrons; (b) a proton and an electron; (c) two protons.",
        "options": [
            "(a) repulsive, (b) attractive, (c) repulsive",
            "(a) attractive, (b) repulsive, (c) attractive",
            "(a) repulsive, (b) repulsive, (c) attractive",
            "(a) attractive, (b) attractive, (c) repulsive",
        ],
        "correct_index": 0,
        "explanation": "Like charges repel, opposite charges attract. Electrons repel electrons; a proton and an electron attract; protons repel protons.",
        "skill": "charge interaction rules",
        "difficulty": 1,
        "competency_code": "charge-properties",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Name the three charging methods, and for each state whether direct contact is required and which type of material it applies to in this lecture.",
        "options": [
            "Rubbing — contact, insulators; induction — no contact, conductors; conduction — contact, conductors",
            "Rubbing — no contact, conductors; induction — contact, insulators; conduction — contact, conductors",
            "Induction — contact, insulators; conduction — no contact, conductors; rubbing — contact, conductors",
            "Rubbing — no contact, insulators; induction — contact, conductors; conduction — no contact, conductors",
        ],
        "correct_index": 0,
        "explanation": "Rubbing charges insulators (contact); induction charges conductors without contact; conduction charges conductors with direct contact.",
        "skill": "method classification",
        "difficulty": 1,
        "competency_code": "charging-methods",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "A glass rod is rubbed with silk. What are the final signs of the rod and the silk, and which particles moved and in which direction?",
        "options": [
            "Rod positive, silk negative; electrons moved from the rod to the silk",
            "Rod negative, silk positive; electrons moved from the silk to the rod",
            "Rod positive, silk negative; protons moved from the rod to the silk",
            "Rod negative, silk negative; no particles moved",
        ],
        "correct_index": 0,
        "explanation": "Friction transfers electrons only. The object that loses electrons becomes positive — so the glass rod ends positive and the silk ends negative.",
        "skill": "friction charging",
        "difficulty": 1,
        "competency_code": "charging-methods",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Which charging method does this lecture assign to insulators?",
        "options": ["Rubbing (friction)", "Induction", "Conduction", "All three equally"],
        "correct_index": 0,
        "explanation": "Rubbing (friction) is the method used for charging insulators; induction and conduction both apply to conductors.",
        "skill": "method classification",
        "difficulty": 1,
        "competency_code": "charging-methods",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Which of these charges is physically impossible?",
        "options": [
            "−3.2 × 10⁻¹⁹ C",
            "−4.0 × 10⁻¹⁹ C",
            "+6.4 × 10⁻¹⁹ C",
            "−9.6 × 10⁻¹⁹ C",
        ],
        "correct_index": 1,
        "explanation": "−3.2e-19 C = −2e (possible); +6.4e-19 C = +4e and −9.6e-19 C = −6e (possible). −4.0e-19 C = −2.5e — N must be an integer, so it's impossible.",
        "skill": "quantization as a validity test",
        "difficulty": 2,
        "competency_code": "charge-quantization",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A conducting sphere carries −96 μC. How many excess electrons does it have?",
        "options": [
            "6 × 10¹⁴ electrons",
            "6 × 10¹⁵ electrons",
            "1.6 × 10¹⁵ electrons",
            "6 × 10¹³ electrons",
        ],
        "correct_index": 0,
        "explanation": "N = (−96 × 10⁻⁶)/(−1.6 × 10⁻¹⁹) = 60 × 10¹³ = 6 × 10¹⁴ electrons.",
        "skill": "electron counting with prefix conversion",
        "difficulty": 2,
        "competency_code": "charge-units",
    },
    {
        "level": "APPLY",
        "prompt": "An object carries +4.8 μC. How many electrons were removed from it?",
        "options": [
            "3 × 10¹³ electrons",
            "3 × 10¹² electrons",
            "7.68 × 10¹³ electrons",
            "3 × 10¹⁴ electrons",
        ],
        "correct_index": 0,
        "explanation": "A positive charge means an electron deficit: N = |Q|/e = (4.8 × 10⁻⁶)/(1.6 × 10⁻¹⁹) = 3 × 10¹³ electrons removed.",
        "skill": "electron counting, positive case",
        "difficulty": 2,
        "competency_code": "charge-units",
    },
    {
        "level": "APPLY",
        "prompt": "Two identical conducting spheres carry 8 C and 4 C. They are touched together and separated. What is the final charge on each?",
        "options": [
            "6 C each",
            "8 C and 4 C (unchanged)",
            "5 C and 5 C",
            "6 C and 4 C",
        ],
        "correct_index": 0,
        "explanation": "Identical spheres share equally: (8 + 4)/2 = 6 C each. The same answer comes from q′ = q_t/r_t with equal radii.",
        "skill": "contact charge sharing; consistency of routes",
        "difficulty": 2,
        "competency_code": "charge-transfer",
    },
    {
        "level": "APPLY",
        "prompt": "A conducting sphere of radius 5 m carrying 15 C touches a NEUTRAL conducting sphere of radius 2.5 m. Find each final charge.",
        "options": [
            "10 C and 5 C",
            "7.5 C and 7.5 C",
            "12.5 C and 2.5 C",
            "15 C and 0 C",
        ],
        "correct_index": 0,
        "explanation": "q_t = 15 C, r_t = 7.5 m, q′ = 2 C/m → sphere 1: 2 × 5 = 10 C; sphere 2: 2 × 2.5 = 5 C. The neutral sphere contributes its radius but zero charge.",
        "skill": "applying q′ = q_t/r_t with a neutral participant",
        "difficulty": 2,
        "competency_code": "charge-transfer",
    },
    {
        "level": "APPLY",
        "prompt": "You want to charge a neutral metal sphere NEGATIVELY by induction. What must you do, in order?",
        "options": [
            "Bring a POSITIVE rod near; ground the sphere so electrons flow up from the Earth; disconnect the ground while the rod is still near; remove the rod",
            "Bring a NEGATIVE rod near; ground the sphere; remove the rod; then disconnect the ground",
            "Touch the sphere with a positive rod, then ground it",
            "Bring a positive rod near and simply wait; no ground wire is needed",
        ],
        "correct_index": 0,
        "explanation": "Induction with a positive charger yields a negative target: the rod pulls electrons up from the Earth through the wire; disconnect the ground while the rod is still in place, then remove the rod.",
        "skill": "induction procedure and sign rule",
        "difficulty": 2,
        "competency_code": "charging-methods",
    },
    {
        "level": "APPLY",
        "prompt": "Convert: (a) 0.5 mC into μC; (b) 250 nC into μC; (c) the number of electrons in −1 μC.",
        "options": [
            "(a) 500 μC, (b) 0.25 μC, (c) 6.25 × 10¹² electrons",
            "(a) 0.5 μC, (b) 0.0025 μC, (c) 6.25 × 10¹⁵ electrons",
            "(a) 5 μC, (b) 0.25 μC, (c) 6.25 × 10⁹ electrons",
            "(a) 500 μC, (b) 2500 μC, (c) 6.25 × 10¹² electrons",
        ],
        "correct_index": 0,
        "explanation": "0.5 mC = 0.5 × 10⁻³ C = 500 μC. 250 nC = 250 × 10⁻⁹ C = 0.25 μC. −1 μC → (10⁻⁶)/(1.6 × 10⁻¹⁹) = 6.25 × 10¹² electrons.",
        "skill": "prefix conversions; electron counting",
        "difficulty": 2,
        "competency_code": "charge-units",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Three conducting spheres are touched together simultaneously: r₁=1 m/2 C, r₂=2 m/−4 C, r₃=3 m/neutral. Find the final charge on each and verify two independent ways.",
        "options": [
            "q₁′ ≈ −0.333 C, q₂′ ≈ −0.667 C, q₃′ = −1 C",
            "q₁′ ≈ 0.667 C, q₂′ ≈ −1.333 C, q₃′ ≈ −2 C",
            "q₁′ = −1 C, q₂′ = −1 C, q₃′ = −1 C",
            "q₁′ ≈ 0.5 C, q₂′ ≈ −1 C, q₃′ ≈ −1.5 C",
        ],
        "correct_index": 0,
        "explanation": "q_t = 2 + (−4) + 0 = −2 C; r_t = 6 m; q′ = −1/3 C/m. Final: q₁′ = −1/3 C, q₂′ = −2/3 C, q₃′ = −1 C. Check conservation: sum = −2 C ✓; ratios 1:2:3 = radii ✓. The neutral sphere still takes a share via its radius.",
        "skill": "full charge-sharing with mixed signs and a neutral sphere",
        "difficulty": 3,
        "competency_code": "charge-transfer",
    },
    {
        "level": "TRANSFER",
        "prompt": "Give a neutral metal sphere a NEGATIVE charge by induction — no charged object may touch it, and you only have a positively charged rod and a ground wire. Describe the complete procedure, stating at every step which way electrons move.",
        "options": [
            "Bring the positive rod near (no contact) → free electrons shift to the near side; connect the ground → electrons are drawn UP from the Earth onto the sphere; disconnect the wire while the rod is still in place; remove the rod → sphere left negative",
            "Bring the positive rod near → electrons drain into the Earth → sphere positive; disconnect; remove",
            "Touch the rod to the sphere → electrons flow from the sphere to the rod → sphere positive",
            "Ground the sphere first, then bring the positive rod near and remove the rod — no wire disconnect needed",
        ],
        "correct_index": 0,
        "explanation": "Induction with a positive charger yields a negative target: the rod's influence draws electrons from the Earth up the wire and onto the sphere; disconnect the wire while the rod is still near, then remove the rod.",
        "skill": "induction procedure transferred to a planning task",
        "difficulty": 3,
        "competency_code": "charging-methods",
    },
    {
        "level": "TRANSFER",
        "prompt": "A classmate claims friction left a dust particle with a charge of −5.0 × 10⁻¹⁹ C. Evaluate the claim using quantization, and if impossible, state the two nearest ALLOWED negative charges.",
        "options": [
            "Impossible — 5.0/1.6 = 3.125, not an integer. Nearest allowed: −3e = −4.8 × 10⁻¹⁹ C and −4e = −6.4 × 10⁻¹⁹ C",
            "Possible — −5.0e-19 C is exactly −3e",
            "Impossible — nearest allowed are −4e and −5e",
            "Possible — any multiple of 10⁻²⁰ C is allowed",
        ],
        "correct_index": 0,
        "explanation": "Charge must be an integer multiple of e: 5.0 × 10⁻¹⁹ / 1.6 × 10⁻¹⁹ = 3.125 → not an integer → impossible. The allowed values bracket it as −3e and −4e.",
        "skill": "applying Q = ±Ne as a physical constraint in a novel context",
        "difficulty": 3,
        "competency_code": "charge-quantization",
    },
    {
        "level": "TRANSFER",
        "prompt": "A negatively charged rod is held near — but NOT touching — a small neutral conductor hanging from an insulating thread. Describe the charge distribution inside the conductor and predict whether the rod attracts or repels it.",
        "options": [
            "Free electrons are repelled to the far side (near face positive, far face negative); the opposite-sign near charge is closer to the rod, so the rod ATTRACTS the conductor",
            "The conductor becomes entirely negative and is repelled",
            "Nothing changes because the rod never touches the conductor; no force acts",
            "The conductor becomes entirely positive and is attracted",
        ],
        "correct_index": 0,
        "explanation": "The rod repels free electrons to the far side and leaves the near face positive. Because the opposite-sign charge is now closer to the rod than the same-sign charge, the net interaction is attraction — the redistribution is exactly the lecture's induction mechanism.",
        "skill": "transfer of the polarization mechanism to a prediction task",
        "difficulty": 3,
        "competency_code": "charge-properties",
    },
    {
        "level": "TRANSFER",
        "prompt": "Show mathematically that 'two identical spheres share charge equally' is a special case of q_i′ = (q_t/r_t) × r_i, and find the final charges when a sphere carrying Q touches a neutral identical sphere.",
        "options": [
            "With equal radii, each sphere ends with q_t/2; for Q touching a neutral identical sphere, each ends with Q/2",
            "With equal radii, each sphere keeps its own original charge; no sharing happens",
            "Two identical spheres always equalize to the large sphere's charge",
            "The formula only applies to unequal spheres; identical spheres always split 3:1",
        ],
        "correct_index": 0,
        "explanation": "With r₁ = r₂ = r: q_t = q₁ + q₂, r_t = 2r, q′ = (q₁ + q₂)/(2r), and q₁′ = q₂′ = (q₁ + q₂)/2 — equal halves. A charge Q touching a neutral identical sphere: each ends with Q/2.",
        "skill": "deriving a stated special case from the general formula",
        "difficulty": 3,
        "competency_code": "charge-transfer",
    },
]

# --- competencies (linked to the lesson via lesson_competencies) -------------
COMPETENCIES = [
    {
        "code": "charge-properties",
        "title": "Properties of Electric Charge",
        "taxonomy_level": "understand",
        "description": "Describe the two types of charge, the attraction/repulsion rule, and the coulomb as the SI unit.",
        "sort_order": 0,
    },
    {
        "code": "charge-quantization",
        "title": "Quantization of Charge",
        "taxonomy_level": "recall",
        "description": "State that charge is quantized (Q = ±Ne, e = 1.6 × 10⁻¹⁹ C) and use it to judge whether a charge is physically possible.",
        "sort_order": 1,
    },
    {
        "code": "charge-units",
        "title": "Charge Units and Electron Counting",
        "taxonomy_level": "recall",
        "description": "Convert between coulombs and mC/μC/nC/pC and count the elementary charges in a given charge.",
        "sort_order": 2,
    },
    {
        "code": "charge-transfer",
        "title": "Charge Transfer by Conduction",
        "taxonomy_level": "apply",
        "description": "Compute final charges when conducting spheres touch, using q′ = q_t/r_t and q_i′ = q′ × r_i.",
        "sort_order": 3,
    },
    {
        "code": "charging-methods",
        "title": "Charging Methods",
        "taxonomy_level": "apply",
        "description": "Distinguish rubbing, induction, and conduction; predict the sign each method produces and the role of grounding.",
        "sort_order": 4,
    },
]

COMPETENCY_PREREQUISITES = [
    ("charge-properties", "charge-quantization"),
    ("charge-quantization", "charge-units"),
    ("charge-units", "charge-transfer"),
    ("charge-properties", "charging-methods"),
]

LESSON_COMPETENCIES = [
    {"code": "charge-properties", "role": "teaches"},
    {"code": "charge-quantization", "role": "teaches"},
    {"code": "charge-units", "role": "teaches"},
    {"code": "charge-transfer", "role": "teaches"},
    {"code": "charging-methods", "role": "teaches"},
]

BUNDLES = [
    {
        "course": {
            "code": COURSE_CODE,
            "title": COURSE_TITLE,
            "credits": COURSE_CREDITS,
            "description": COURSE_DESCRIPTION,
            "department_code": DEPARTMENT_CODE,
            "department_name": DEPARTMENT_NAME,
            "faculty_code": FACULTY_CODE,
            "faculty_name": FACULTY_NAME,
            "module": MODULE,
            "lesson": LESSON,
            "lesson_contents": LESSON_CONTENTS + WORKED_EXAMPLES + WARNINGS + DIFFICULT_CONCEPTS,
            "summary_contents": SUMMARY_CONTENTS,
            "resources": VIDEO_RESOURCES,
            "competencies": COMPETENCIES,
            "competency_prerequisites": COMPETENCY_PREREQUISITES,
            "lesson_competencies": LESSON_COMPETENCIES,
            "practice_items": PRACTICE_ITEMS,
        }
    },
    BUNDLE_L2,
    BUNDLE_L3,
    BUNDLE_L4,
    BUNDLE_L5,
    BUNDLE_L6,
    BUNDLE_L7,
    BUNDLE_L8,
    BUNDLE_L9,
    BUNDLE_L10,
    BUNDLE_L11,
    BUNDLE_L12,
    BUNDLE_REVIEW1,
    BUNDLE_REVIEW2,
    BUNDLE_FINAL,
    *BUNDLES_MATH1,
    *BUNDLES_CSE014,
    *BUNDLES_IT,
]

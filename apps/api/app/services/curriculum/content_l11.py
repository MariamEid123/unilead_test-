"""PHY211 — Physics, Module 9, Lecture 11: Image Formation — Mirrors.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 11, Fall 2024 —
'Image Formation: Mirrors', Chapter 10).

Builds the image-formation vocabulary (real vs virtual), the plane mirror's
exact construction, the spherical mirror's three principal rays and five
zones, then the apparatus: the mirror equation 1/p + 1/q = 1/f = 2/R,
magnification M = −q/p, and power in diopters. Imported by
``curriculum.content`` and seeded by ``curriculum.seed``.
"""

from __future__ import annotations

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
    "code": "M9",
    "title": "Module 9 — Image Formation: Mirrors",
    "description": (
        "Chapter 10 (Part 1): turning reflection into images. The real/virtual "
        "distinction, the plane mirror's exact construction, the spherical "
        "mirror's principal rays and object zones, and the mirror equation with "
        "magnification and power that locks every case into arithmetic."
    ),
    "sort_order": 9,
}

LESSON = {
    "code": "L11",
    "title": "Image Formation: Mirrors — Real and Virtual Images, Plane and Spherical Mirrors, and the Mirror Equation",
    "description": (
        "Lecture 11 — how a mirror turns rays into pictures. Real images (rays "
        "meet, can be screened) versus virtual (extensions meet), the plane "
        "mirror's p = −q identity, the concave mirror's converging geometry and "
        "five object zones, the convex mirror's always virtual/upright/small "
        "verdict, and the equation 1/p + 1/q = 1/f = 2/R that rules them all."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Define principal axis, vertex, focal point/length (f), and center/radius of curvature (C, R) for spherical mirrors.",
        "Classify an image as real (rays meet, screenable, q+) or virtual (extensions meet, unscreenable, q−).",
        "Construct the plane-mirror image with two rays and prove p = −q with M = +1.",
        "Identify concave (converging, f+) vs. convex (diverging, f−) mirrors and their F/C positions.",
        "Trace the three principal rays (parallel→F, through F→parallel, through C→back).",
        "Characterize images for the concave mirror's five object zones and the convex mirror's single verdict.",
        "Solve 1/p + 1/q = 1/f = 2/R with the full sign convention (f+, q+, M+ rules).",
        "Compute magnification M = −q/p and mirror power F = 1/f in diopters (f in meters).",
    ],
    "prerequisites": [
        "Law of reflection θi = θr with angles from the normal (Lecture 10).",
        "The ray model of light and image formation by ray geometry (Lecture 10).",
        "Qualitative refraction competence — apparent depth and ray bending (Lecture 10).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A mirror is a machine for turning rays into pictures. Three ideas "
            "run the whole lesson: every image is where reflected rays (or their "
            "backward extensions) meet; a plane mirror just bounces geometry "
            "across a line; and a curved mirror trades flatness for convergence — "
            "one formula, 1/p + 1/q = 1/f, locates every image the surface can "
            "make. Sign conventions are the whole game: get q's sign and "
            "everything else follows."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Vocabulary of Image Formation",
        "body": (
            "The principal axis is the symmetry line of the mirror; the vertex "
            "(pole) sits at its center; the center of curvature C is the sphere's "
            "center, at radius R; the focal point F lies halfway, f = R/2. "
            "Distances: object distance p, image distance q; sizes h and h′ with "
            "signs; magnification M = h′/h. Distant sources send effectively "
            "parallel rays, which a concave mirror collects at F — the origin of "
            "the focal point."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Real vs virtual: the screen test",
        "body": (
            "REAL image: reflected rays actually MEET in front of the mirror — a "
            "screen catches it (projector!) and q is positive. VIRTUAL image: "
            "reflected rays only LOOK like they came from there; the extensions "
            "meet behind the mirror — no screen can catch it, and q is negative. "
            "Your eye accepts both; optics must know which."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The Plane Mirror",
        "body": "p = −q   (|q| = p),   M = +1",
        "metadata": {
            "meaning": "Image the same distance behind the mirror as the object is in front, same size, upright, virtual, and LEFT/RIGHT reversed.",
            "when_used": "Wherever a scene is mirrored. Two rays from the object's tip, reflected by θi = θr, meet at the same point behind the mirror — identical triangles prove p = |q|.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Concave vs Convex Geometry",
        "body": (
            "A CONCAVE mirror curves toward the object — a converging mirror: "
            "f positive, F and C in FRONT. A CONVEX mirror curves away — a "
            "diverging mirror: f negative, F and C behind. Every sign in the "
            "equation keys off these two facts: the concave mirror gathers rays "
            "(and burns paper at F); the convex mirror only spreads them, which "
            "is why it always makes a small, upright, virtual view."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Three Principal Rays",
        "body": (
            "For any off-axis object, three special rays locate the image: (1) a "
            "ray parallel to the axis reflects through F; (2) a ray through F "
            "reflects parallel to the axis; (3) a ray through C reflects back "
            "along itself. Their intersection is the image point — draw two, "
            "check with the third."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Five Zones of a Concave Mirror",
        "body": (
            "Slide the object along p and the concave image cycles through five "
            "characters: p > 2f → real, inverted, REDUCED; p = 2f → real, "
            "inverted, SAME SIZE (q = 2f, M = −1); 2f > p > f → real, inverted, "
            "ENLARGED; p = f → image AT INFINITY (rays exit parallel); p < f → "
            "VIRTUAL, upright, ENLARGED — the makeup mirror. Only the inside-of-F "
            "zone flips to virtual."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Convex Verdict: One Case, Forever",
        "body": (
            "A convex mirror has one answer in every zone: virtual, upright, "
            "reduced. No real image, no enlargement — which makes it the "
            "security mirror, a wide upright view of everything behind it. "
            "p = 24 cm, f = −12 cm: q = −8 cm, M = +1/3."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The Mirror Equation",
        "body": "1/p + 1/q = 1/f = 2/R",
        "metadata": {
            "meaning": "One reciprocal relation locates every image: p > 0 for real objects; q+ real in front, q− virtual behind; f+ concave / f− convex.",
            "when_used": "Every numerical mirror problem. Solve for the unknown reciprocal, then invert twice — and carry q's sign into the magnification.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Magnification and Mirror Power",
        "body": "M = −q/p     and     F = 1/f  (diopters, f in meters)",
        "metadata": {
            "meaning": "M's sign gives orientation (+ upright, − inverted) and |M| the size. Power measures how strongly the mirror bends rays — its sign restates the type (concave +, convex −).",
            "when_used": "Size/type questions and prescription-style problems. Strict meters-only rule: f in cm gives a 100× wrong power.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "One equation, five zones, all signs",
        "body": (
            "Don't memorize five zone tables AND an equation — the equation "
            "reproduces the tables. Plug p and f with their signs; the q that "
            "comes out carries the verdict: q > 0 real, q < 0 virtual; M next "
            "gives size and orientation. The zone table is the intuition; the "
            "equation is the machine."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — the concave mirror, object beyond C",
        "body": (
            "Concave mirror, f = +10 cm, object at p = 25 cm. Mirror equation: "
            "1/25 + 1/q = 1/10 → 1/q = 1/10 − 1/25 = 3/50 → q = +16.7 cm. "
            "M = −q/p = −16.7/25 ≈ −0.67. Verdict: real, inverted, reduced "
            "(|M| < 1), in front — the table's first zone, recovered by arithmetic."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — the concave mirror, object inside F",
        "body": (
            "Same mirror (f = +10 cm), object at p = 5 cm: 1/5 + 1/q = 1/10 → "
            "1/q = −1/10 → q = −10 cm. M = −(−10)/5 = +2.0. Verdict: VIRTUAL "
            "(extensions meet behind), upright (M > 0), twice the size — the "
            "makeup-mirror zone. Negative q is not 'no image': it is a virtual "
            "image."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — the convex mirror",
        "body": (
            "Convex mirror f = −12 cm, object at p = 24 cm: 1/24 + 1/q = −1/12 "
            "→ 1/q = −1/8 → q = −8 cm. M = −(−8)/24 = +1/3. Verdict: virtual, "
            "upright, one-third size, behind the mirror — as every convex mirror "
            "demands."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — power in diopters",
        "body": (
            "(a) Concave mirror, f = +20 cm → f = 0.20 m → F = 1/0.20 = +5.0 "
            "diopters. (b) Convex mirror, f = −25 cm → f = −0.25 m → F = 1/(−0.25)"
            " = −4.0 diopters. The sign restates the type; feeding cm instead of "
            "meters would be off by 100×."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — the plane mirror as the limit",
        "body": (
            "Send R → ∞ and the mirror equation becomes flat: 1/f = 2/R → 0, so "
            "1/p + 1/q = 0 → q = −p — exactly the plane mirror's fact. The plane "
            "mirror is the R → ∞ limit of the same formula: one machinery runs "
            "flat and curved mirrors alike."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Dropped minus in M",
        "body": "M = −q/p: the minus is the entire orientation answer. M > 0 upright, M < 0 inverted — dropping it flips upside-down scenes upright.",
    },
    {
        "section_type": "WARNING",
        "title": "Wrong f sign",
        "body": "Concave f is positive, convex negative — set it before substituting. One sign apart, two different images.",
    },
    {
        "section_type": "WARNING",
        "title": "'q < 0 = no image'",
        "body": "Negative q is a VIRTUAL image behind the mirror — it exists for your eye even though no screen catches it. q < 0 is an answer, not an error.",
    },
    {
        "section_type": "WARNING",
        "title": "Virtual means invisible",
        "body": "Virtual images are perfectly visible; the rays only seem to come from behind the mirror. 'Virtual' describes geometry (extensions), not visibility.",
    },
    {
        "section_type": "WARNING",
        "title": "cm in the power formula",
        "body": "F = 1/f demands METERS: f = 20 cm → 0.20 m → 5 diopters. A cm input silently returns a number 100× too large.",
    },
    {
        "section_type": "WARNING",
        "title": "f/R mix-up and Ray 3 drawn bent",
        "body": "f = R/2 (R = 40 cm ⇒ f = 20 cm), and the ray through C reflects straight back along itself — drawing it bent invents a second reflection.",
    },
    {
        "section_type": "WARNING",
        "title": "|M| misread",
        "body": "|M| gives sizing (1 same, < 1 reduced, > 1 enlarged); the sign gives orientation. Reading only one halves the answer.",
    },
    {
        "section_type": "WARNING",
        "title": "One-size-fits-all mirror",
        "body": "A convex mirror NEVER enlarges and NEVER makes a real image — not for near objects, not for distant ones. The verdict is unconditional.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Real vs Virtual: Rays or Extensions?",
        "body": (
            "A real image is made where reflected rays genuinely cross (screen "
            "catches it, q > 0); a virtual image by backward extensions (no "
            "screen, q < 0). Analogy: a projector casts a real image on a "
            "screen — walk behind it and nothing is there; a bathroom mirror "
            "shows you a reflection you cannot touch because it is built behind "
            "the glass. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Sign Convention Ledger",
        "body": (
            "The mirror equation only works with the full ledger: f+ concave / "
            "f− convex; q+ real front / q− virtual behind; M+ upright / M− "
            "inverted; p+ for real objects. Analogy: a bank ledger — miss one "
            "sign and the whole account balances wrong. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Five Zones of the Concave Mirror",
        "body": (
            "One converging geometry, five verdicts as the object moves in. "
            "Analogy: zooming a projector — far objects reduce, nearby ones "
            "enlarge, and crossing F flips the image into virtual. The equation "
            "reproduces all five; the table is memory, the formula is truth. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Magnification's Sign and Size",
        "body": (
            "M = −q/p packs two answers in one number: sign says upright/"
            "inverted, |M| says bigger/smaller/same. Students who read only the "
            "magnitude let a perfectly inverted image float by. Difficulty: "
            "EASY–MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Drawing the Three Principal Rays",
        "body": (
            "Ray selection, not ray tracing, is the skill: parallel→F, through "
            "F→parallel, through C→back; the image is where two cross. Analogy: "
            "finding a meeting point from three streets — take the two clearest "
            "routes, let the third confirm. Difficulty: MEDIUM–HARD."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Real image: rays MEET in front — screen ✓, q+; virtual: extensions meet behind — screen ✗, q−.\n"
            "• Plane mirror: p = −q, M = +1, virtual, upright, left/right reversed.\n"
            "• Concave = converging (f+, F/C front); convex = diverging (f−, F/C back).\n"
            "• Three principal rays: ∥→F; through F→∥; through C→back.\n"
            "• Concave five zones: >2f real-inverted-small; =2f real-inverted-same (q=2f); F–2f real-inverted-big; =f infinity; <f VIRTUAL-upright-big.\n"
            "• Convex: always virtual, upright, reduced.\n"
            "• Mirror equation 1/p + 1/q = 1/f = 2/R, f = R/2; power F = 1/f (f in meters, diopters).\n"
            "• M = −q/p: sign = orientation, |M| = size. Signs: f+ concave, q+ real, M+ upright."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Principal axis / vertex — the mirror's symmetry line and center.\n"
            "• Center of curvature C — center of the sphere, at radius R.\n"
            "• Focal point F / focal length f — where distant rays gather; f = R/2.\n"
            "• Object distance p / image distance q — signed positions along the axis.\n"
            "• Real image — formed by meeting rays (front, q+, screenable).\n"
            "• Virtual image — formed by backward extensions (behind, q−, unscreenable).\n"
            "• Magnification M = h′/h = −q/p; Diopter (Δ) — power unit: F = 1/f with f in meters."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• 1/p + 1/q = 1/f = 2/R — mirror equation; f = R/2.\n"
            "• M = −q/p — magnification (sign = orientation, |M| = size).\n"
            "• F = 1/f (f in m) — mirror power in diopters.\n"
            "• Plane mirror: q = −p, M = +1 (the R → ∞ limit).\n"
            "• Concave zones: p = 2f → q = 2f, M = −1; p = f → q → ∞."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Real images meet in front (screen ✓, q+); virtual ones hide behind "
            "the mirror (extensions, q−). A plane mirror flips space: p = −q, "
            "M = +1, left/right reversed. Curved mirrors: concave converges (f+), "
            "convex diverges (f−); f = R/2; three rays — parallel→F, "
            "through-F→parallel, through-C→back — pin any image. Concave zones: "
            "beyond 2f real-small, at 2f real-same, F to 2f real-big, at F "
            "infinity, inside F virtual-big. Convex: always virtual-upright-"
            "small. Numbers come from 1/p + 1/q = 1/f = 2/R with one sign ledger "
            "(f+, q+, M+) and M = −q/p; power F = 1/f in METERS is the mirror's "
            "diopter bend-o-meter."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "Signs That Speak: Conquering the Mirror Equation",
        "description": (
            "The full sign convention, the mirror equation 1/p + 1/q = 1/f = 2/R, "
            "magnification M = −q/p, and power in diopters — the machinery that "
            "turns every mirror case into arithmetic."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The mirror equation and its sign conventions",
            "target_student": "First-year university student",
            "objective": "Solve the mirror equation with correct signs and report magnification and power for any spherical-mirror case.",
            "hook": "One equation, one ledger of signs, and every mirror on Earth — flat, concave, convex — answers the same way. Signs are not homework trivia; they ARE the physics.",
            "explanation_steps": [
                "Real vs virtual: rays meet vs extensions; q+ front vs q− behind.",
                "The sign ledger: p > 0; f+ concave, f− convex; M+ upright.",
                "1/p + 1/q = 1/f = 2/R; f = R/2.",
                "Worked concave: f = +10, p = 25 → q = +16.7, M = −0.67.",
                "Worked convex: f = −12, p = 24 → q = −8, M = +1/3.",
                "M = −q/p (sign orientation, |M| size); power F = 1/f in meters → diopters.",
            ],
            "common_mistake": "Dropping the minus in M; wrong f sign; treating q < 0 as 'no image'; cm in the power formula.",
            "check": "A concave mirror with f = 10 cm holds an object at 5 cm. Locate the image and describe it fully.",
            "final_takeaway": "Feed the ledger into 1/p + 1/q = 1/f and the q that comes out speaks: sign = location and type, M = orientation and size.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Five Zones of a Concave Mirror",
        "description": (
            "The concave mirror's five object zones — reduced to same-size to "
            "enlarged to infinity to virtual — read off ray diagrams and the "
            "mirror equation, including the makeup-mirror case."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The concave mirror's five image zones",
            "target_student": "First-year university student",
            "objective": "Predict the image character (real/virtual, upright/inverted, size) as object distance p passes through 2f and f.",
            "hook": "Slide an object toward one bowl-shaped mirror and the picture runs a whole play: shrink, meet you at full size, blow up, vanish, then reappear giant and right-side-up — five acts, one mirror.",
            "explanation_steps": [
                "The three principal rays and their intersection point.",
                "Act 1: p > 2f → real, inverted, reduced.",
                "Act 2: p = 2f → real, inverted, same size (q = 2f, M = −1).",
                "Act 3: 2f > p > f → real, inverted, enlarged.",
                "Act 4: p = f → rays exit parallel — image at infinity.",
                "Act 5: p < f → virtual, upright, enlarged (makeup), q < 0.",
                "Worked numbers: f = +10, p = 25 → M = −0.67; p = 5 → q = −10, M = +2.",
            ],
            "common_mistake": "Memorizing the table without the equation; forgetting the F → virtual flip; expecting convex mirrors to enlarge.",
            "check": "Object sits between F and the mirror. Real or virtual? Larger or smaller? Where's q?",
            "final_takeaway": "Five zones, one mirror: real-small → real-same → real-big → infinity → virtual-big, and the equation reproduces all five.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "Distinguish a real image from a virtual image formed by a mirror.",
        "options": [
            "Real: reflected rays actually MEET in front (screenable, q+); virtual: only the backward extensions meet behind the mirror (unscreenable, q−)",
            "Real: behind the mirror; virtual: in front; the screen is irrelevant",
            "Real: always inverted; virtual: always upright; location is irrelevant",
            "Real: produced only by convex mirrors; virtual: only by plane mirrors",
        ],
        "correct_index": 0,
        "explanation": "The distinction is ray-meeting geometry: real images are where reflected rays intersect (q > 0, catchable on a screen); virtual images are where their extensions intersect (q < 0).",
        "skill": "real vs virtual classification",
        "difficulty": 1,
        "competency_code": "real-virtual-images",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State the complete set of plane-mirror image properties.",
        "options": [
            "Same distance behind as the object is in front (|q| = p), same size, virtual, upright, and left/right reversed",
            "Half the object distance, inverted, and real",
            "Twice the object size, virtual, inverted",
            "Same distance, but only the top half is rendered",
        ],
        "correct_index": 0,
        "explanation": "The plane mirror's construction (identical triangles) proves |q| = p; the image is virtual, upright, M = +1, and reverses left and right (not up and down).",
        "skill": "plane-mirror properties",
        "difficulty": 1,
        "competency_code": "plane-mirrors",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What distinguishes a concave from a convex mirror in the sign convention?",
        "options": [
            "Concave has f + (F and C in FRONT); convex has f − (F and C BEHIND)",
            "Concave has f −; convex has f +; both put F in front",
            "Concave never forms real images; convex never forms virtual ones",
            "The sign is set by object distance, not by mirror shape",
        ],
        "correct_index": 0,
        "explanation": "Concave mirrors curve toward the object, gather rays, and take f > 0 (F, C in front); convex mirrors curve away, spread rays, and take f < 0 (F, C behind).",
        "skill": "concave vs convex identity",
        "difficulty": 1,
        "competency_code": "spherical-mirrors",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Using the mirror equation, what image does a concave mirror form for an object placed inside F?",
        "options": [
            "Virtual, upright, enlarged (q < 0, |M| > 1) — the makeup-mirror case",
            "Real, inverted, reduced",
            "Real, inverted, same size",
            "No image forms at all inside F",
        ],
        "correct_index": 0,
        "explanation": "For p < f the equation returns q < 0 with |q| > p: a virtual image behind the mirror, upright and enlarged — exactly the makeup-mirror reading.",
        "skill": "inside-F zone prediction",
        "difficulty": 1,
        "competency_code": "mirror-equation",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A concave mirror has f = +10 cm and an object at p = 25 cm. Locate the image and its magnification.",
        "options": [
            "1/q = 1/10 − 1/25 → q = +16.7 cm; M = −0.67 (real, inverted, reduced)",
            "1/q = 1/10 + 1/25 → q = 7.1 cm; M = −0.29",
            "q = +8.0 cm; M = −0.32",
            "q = −16.7 cm; M = +0.67 (virtual, upright)",
        ],
        "correct_index": 0,
        "explanation": "1/25 + 1/q = 1/10 → 1/q = 3/50 → q = +16.7 cm; M = −16.7/25 ≈ −0.67. Positive q with |M| < 1: real, inverted, reduced — zone one.",
        "skill": "mirror equation with signs",
        "difficulty": 2,
        "competency_code": "mirror-equation",
    },
    {
        "level": "APPLY",
        "prompt": "Same concave mirror (f = +10 cm) but the object moves to p = 5 cm. Describe the image.",
        "options": [
            "1/q = 1/10 − 1/5 → q = −10 cm; M = +2: virtual, upright, enlarged",
            "q = +3.3 cm; M = −0.67: real, inverted, reduced",
            "q = +10 cm; M = −2: real, inverted, enlarged",
            "q = −3.3 cm; M = +0.67: virtual, upright, reduced",
        ],
        "correct_index": 0,
        "explanation": "1/5 + 1/q = 1/10 → 1/q = −1/10 → q = −10 cm; M = −(−10)/5 = +2.0. Negative q, positive M, |M| > 1 — the mirror flips to virtual and magnifies.",
        "skill": "inside-F computation",
        "difficulty": 2,
        "competency_code": "mirror-equation",
    },
    {
        "level": "APPLY",
        "prompt": "A convex mirror has f = −12 cm with an object at p = 24 cm. Find q and M.",
        "options": [
            "1/q = −1/12 − 1/24 → q = −8 cm; M = +1/3 (virtual, upright, reduced)",
            "1/q = −1/12 + 1/24 → q = −24 cm; M = +1",
            "q = +8 cm; M = −1/3 (real, inverted, reduced)",
            "q = −36 cm; M = +1.5 (virtual, enlarged)",
        ],
        "correct_index": 0,
        "explanation": "1/24 + 1/q = −1/12 → 1/q = −1/8 → q = −8 cm; M = −(−8)/24 = +1/3. Convex mirrors always deliver virtual, upright, reduced.",
        "skill": "convex mirror computation",
        "difficulty": 2,
        "competency_code": "mirror-magnification",
    },
    {
        "level": "APPLY",
        "prompt": "A concave mirror has radius R = 30 cm. What are f and the power in diopters?",
        "options": [
            "f = 15 cm = 0.15 m → F = 1/0.15 ≈ +6.7 diopters",
            "f = 30 cm = 0.30 m → F ≈ +3.3 diopters",
            "f = 15 cm = 0.15 m → F = 1/0.15 = +6.7 is wrong because power uses R: F = 2/0.30 ≈ 6.7 — same number",
            "f = 7.5 cm → F ≈ +13 diopters",
        ],
        "correct_index": 0,
        "explanation": "f = R/2 = 15 cm = 0.15 m; F = 1/f = 1/0.15 ≈ +6.7 diopters (equivalently 2/R). Concave → the sign is +; meters are mandatory.",
        "skill": "radius → focal length → power",
        "difficulty": 2,
        "competency_code": "mirror-equation",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "A mirror has power +2.5 D. Identify it and locate the image of an object 40 cm away.",
        "options": [
            "f = 1/2.5 = 0.40 m = 40 cm, concave (f+); p = 40 = 2f → q = +40 cm, M = −1: real, inverted, same size at C",
            "f = 0.40 m, convex; q = −40 cm, M = +1",
            "f = 2.5 cm; q is huge; virtual",
            "Power cannot identify the mirror type",
        ],
        "correct_index": 0,
        "explanation": "f = 1/F = 0.40 m = 40 cm, positive → concave. p = 40 cm = 2f ⇒ q = 2f = 40 cm, M = −1 — the mirror's signature case at the center of curvature.",
        "skill": "power-first reasoning",
        "difficulty": 3,
        "competency_code": "mirror-magnification",
    },
    {
        "level": "TRANSFER",
        "prompt": "You need a makeup mirror that shows an enlarged upright image of your face at a fixed reading distance. Which mirror and zone, and why must the image be virtual?",
        "options": [
            "A CONCAVE mirror with the face inside F: q < 0, M = |q|/p > +1 — virtual, upright, enlarged; any real image would be inverted",
            "A convex mirror near the face: always reduced, so no",
            "A concave mirror with the face beyond C: real and inverted — acceptable for makeup",
            "A plane mirror tilted: enlarges by geometry",
        ],
        "correct_index": 0,
        "explanation": "The makeup mirror is the concave p < f zone: the equation forces q < 0 and |M| > 1. A real image is always inverted for single mirrors — useless for a cosmetic face.",
        "skill": "mirror selection and zone planning",
        "difficulty": 3,
        "competency_code": "spherical-mirrors",
    },
    {
        "level": "TRANSFER",
        "prompt": "An object moves from far away toward a concave mirror (f = 10 cm). At which positions does the image change from (a) real to virtual and (b) reduced to enlarged?",
        "options": [
            "(a) Crossing p = f (10 cm): inside F is virtual, outside is real; (b) crossing p = 2f (20 cm): closer than 2f is enlarged",
            "(a) p = 2f; (b) p = f — both flips at the same point",
            "(a) p = ∞ only; (b) never — concave mirrors always enlarge",
            "(a) At p = R; (b) at p = R/2",
        ],
        "correct_index": 0,
        "explanation": "The five-zone grammar: real→virtual crossing happens at F (p = f), reduced→enlarged at 2f (p = 2f). Both landmarks are structural, not arithmetic accidents.",
        "skill": "five-zone crossing analysis",
        "difficulty": 3,
        "competency_code": "mirror-equation",
    },
    {
        "level": "TRANSFER",
        "prompt": "Design check: a concave mirror yields q = −10 cm, M = +2 for p = 5 cm. Now the object is moved to p = 15 cm. Predict f and the new image with the same mirror.",
        "options": [
            "f from the old case: 1/f = 1/5 + 1/(−10) = 0.1 → f = 10 cm; new: 1/15 + 1/q = 1/10 → q = +30 cm, M = −2 (real, inverted, enlarged, zone between F and 2f)",
            "f = 5 cm; new q = 7.5 cm",
            "The old case fixes nothing; f is unknowable",
            "f = 10 cm; new image is virtual like the old one",
        ],
        "correct_index": 0,
        "explanation": "The same mirror keeps f. Back-substituting old data gives f = 10 cm; at p = 15 cm the equation yields q = +30 cm, M = −2 — the image hopped into the F–2f zone, real, inverted, enlarged.",
        "skill": "reverse design through the equation",
        "difficulty": 3,
        "competency_code": "mirror-equation",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "reflection-law",
        "title": "Law of Reflection",
        "taxonomy_level": "apply",
        "description": "Apply θi = θr with angles measured from the normal to flat and angled surfaces.",
        "sort_order": 44,
    },
    {
        "code": "real-virtual-images",
        "title": "Real and Virtual Images",
        "taxonomy_level": "understand",
        "description": "Classify an image as real (rays meet in front, screenable, q+) or virtual (extensions meet behind, q−).",
        "sort_order": 49,
    },
    {
        "code": "plane-mirrors",
        "title": "Plane Mirrors",
        "taxonomy_level": "apply",
        "description": "Construct the plane-mirror image and apply p = −q with M = +1, virtual, upright, left/right reversal.",
        "sort_order": 50,
    },
    {
        "code": "spherical-mirrors",
        "title": "Spherical Mirrors and Principal Rays",
        "taxonomy_level": "apply",
        "description": "Identify concave (f+) vs convex (f−) mirrors, trace the three principal rays, and characterize the image zones.",
        "sort_order": 51,
    },
    {
        "code": "mirror-equation",
        "title": "The Mirror Equation",
        "taxonomy_level": "apply",
        "description": "Solve 1/p + 1/q = 1/f = 2/R with the full sign convention and compute mirror power F = 1/f in diopters.",
        "sort_order": 52,
    },
    {
        "code": "mirror-magnification",
        "title": "Magnification for Mirrors",
        "taxonomy_level": "apply",
        "description": "Apply M = −q/p: interpret sign as orientation and |M| as size, including power-first and design problems.",
        "sort_order": 53,
    },
]

COMPETENCY_PREREQUISITES = [
    ("reflection-law", "plane-mirrors"),
    ("reflection-law", "spherical-mirrors"),
    ("plane-mirrors", "real-virtual-images"),
    ("spherical-mirrors", "real-virtual-images"),
    ("real-virtual-images", "mirror-equation"),
    ("mirror-equation", "mirror-magnification"),
]

LESSON_COMPETENCIES = [
    {"code": "real-virtual-images", "role": "teaches"},
    {"code": "plane-mirrors", "role": "teaches"},
    {"code": "spherical-mirrors", "role": "teaches"},
    {"code": "mirror-equation", "role": "teaches"},
    {"code": "mirror-magnification", "role": "teaches"},
]

BUNDLE = {
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
}

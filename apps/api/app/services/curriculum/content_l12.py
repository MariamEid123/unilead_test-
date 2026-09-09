"""PHY211 — Physics, Module 10, Lecture 12: Lenses.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 12, Fall 2024 —
'Lenses', Chapter 10 continued).

Transfers the image-formation machinery from mirrors to lenses: converging
vs diverging shapes and sign rules, the image-side flip, the lens equation
and its six cases, three lens ray diagrams, camera/projector/magnifier
instruments, and the two optical aberrations with their fixes. Imported by
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
    "code": "M10",
    "title": "Module 10 — Lenses",
    "description": (
        "Chapter 10 (Part 2): the same equation, a new optical element. "
        "Converging and diverging lenses, the lens equation 1/p + 1/q = 1/f and "
        "its six converging-lens cases, three lens ray diagrams, the "
        "camera/projector/magnifier instruments, and the chromatic and "
        "spherical aberrations that real optics must fight."
    ),
    "sort_order": 10,
}

LESSON = {
    "code": "L12",
    "title": "Lenses: Converging and Diverging Lenses, the Lens Equation, Lens Ray Diagrams, and Optical Aberrations",
    "description": (
        "Lecture 12 — the partner of the mirror equation. Converging lenses "
        "(thick at the center, f+) and diverging lenses (thick at the edges, "
        "f−), the six object zones of a converging lens, ray diagrams with the "
        "undeviated center ray, the camera/projector/magnifier cases, and the "
        "two aberrations — chromatic (color fringes, fixed by a doublet) and "
        "spherical (edge blur, fixed by an aperture) — that decide real lens "
        "design."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Identify converging (thick center, f+) vs diverging (thick edges, f−) lenses from shape and sign.",
        "State the image-side flip: a lens places q+ on the FAR side (light has passed), where the mirror put it in front.",
        "Solve the lens equation 1/p + 1/q = 1/f with magnification M = −q/p under the same sign ledger.",
        "Enumerate the six object cases of a converging lens from p = ∞ to p < f.",
        "Apply the never-varying diverging-lens verdict: virtual, upright, reduced.",
        "Trace the three lens principal rays (parallel→F′, through-center undeviated, through F→parallel).",
        "Explain the camera (distant → at F), projector (f < p < 2f), and magnifier (p < f) geometries.",
        "Describe chromatic aberration (n varies with λ, violet bends more, f_red > f_violet) and its achromatic-doublet fix.",
        "Describe spherical aberration (marginal vs paraxial rays) and its aperture/shaping fixes.",
    ],
    "prerequisites": [
        "Refraction and Snell's law n₁sinθ₁ = n₂sinθ₂ with the index n = c/v (Lecture 10).",
        "The mirror equation and its full sign convention (Lecture 11).",
        "Real vs virtual images, ray diagrams, and the object-zone grammar (Lecture 11).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A lens bends light instead of bouncing it — but the bookkeeping is "
            "identical to the mirror's: same equation 1/p + 1/q = 1/f, same "
            "sign rules, same zones, with ONE crucial flip: the lens lets light "
            "THROUGH, so the far side hosts the real images. This lecture runs "
            "the six cases of a converging lens, the diverging lens's one "
            "verdict, then the aberrations that separate idealized formulas from "
            "glass you can actually buy."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Converging and Diverging Lenses",
        "body": (
            "A CONVERGING (convex) lens is thicker in the center — it gathers "
            "parallel rays to a focal point on the far side, f positive. A "
            "DIVERGING (concave) lens is thicker at the edges — it spreads rays "
            "as if from a virtual focus on the near side, f negative. The sign "
            "rule matches the mirrors: + gathers, − spreads — but the focus "
            "LIVES on the far side of the lens for the converging case."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The Great Flip: q+ is beyond the lens",
        "body": (
            "A MIRROR reflects light back — its real images sit IN FRONT (on the "
            "incident side). A LENS transmits light — its real images sit on the "
            "FAR side, beyond the lens. Everything you learned about mirrors "
            "transfers, except where the picture lands: for the lens, positive q "
            "is BEHIND the optical element."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The Lens Equation and Magnification",
        "body": "1/p + 1/q = 1/f     and     M = −q/p",
        "metadata": {
            "meaning": "Identical to the mirror machinery: p > 0 for real objects; q+ real beyond the lens, q− virtual on the near side; f+ converging, f− diverging; M sign = orientation, |M| = size.",
            "when_used": "Every lens problem. The only difference from mirrors is where q+ lives — nothing else in the algebra changes.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Lens maker's field of view: the six cases",
        "body": "p = ∞ → at F · p > 2f → real, inverted, reduced · p = 2f → real, inverted, same size · f < p < 2f → real, inverted, enlarged · p = f → no image (rays parallel) · p < f → virtual, upright, enlarged",
        "metadata": {
            "meaning": "A converging lens cycles through six acts as the object approaches, mirroring the concave mirror zones but with images landing beyond the lens.",
            "when_used": "Predicting image character; choosing the lens case for an instrument (camera = p > 2f, projector = f < p < 2f, magnifier = p < f).",
        },
    },
    {
        "section_type": "TEXT",
        "title": "The Diverging Lens Verdict",
        "body": (
            "A diverging lens has exactly one answer, like the convex mirror: "
            "virtual, upright, reduced — for every object position. It cannot "
            "project real images, only shrink the scene behind it, which is why "
            "it appears in combination instruments and eyeglasses for myopia "
            "correction rather than as a projector lens."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Ray Diagrams for Lenses",
        "body": (
            "Three principal rays replace the mirror trio: (1) a ray parallel to "
            "the axis refracts through the FAR focal point F′; (2) a ray through "
            "the CENTER passes UNDEVIATED (thin-lens approximation); (3) a ray "
            "through the NEAR focal point F emerges parallel. Where two meet is "
            "the image; check with the third."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Instrument Trilogy",
        "body": (
            "The six cases ARE the instruments. CAMERA: a distant scene (p > 2f "
            "or p ≈ ∞) casts a real, small, inverted image near F — the film or "
            "sensor sits at the focal plane. PROJECTOR: the slide sits between f "
            "and 2f, casting a real, enlarged, inverted image across the room. "
            "MAGNIFIER: the object sits inside F, and the lens delivers a "
            "virtual, upright, enlarged view."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Chromatic Aberration",
        "body": (
            "The index n varies with wavelength, so different colors follow "
            "different paths through one lens: violet (n largest) bends MOST and "
            "meets the axis before red — f_red > f_violet. White light fans into "
            "colored fringes. The fix is the achromatic DOUBLET: cement a "
            "converging and a diverging lens of different glasses so the "
            "dispersions cancel while the focusing power survives."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Spherical Aberration",
        "body": (
            "A spherical surface is only approximately a focusing surface: "
            "MARGINAL rays (near the edge) meet the axis closer than PARAXIAL "
            "rays (near the center), smearing the focus into a blur even for "
            "monochromatic light. The fixes are geometry, not glass: a variable "
            "aperture to cut the marginal rays, or a specially shaped surface "
            "(parabolic, or a sharp-edged lens) that sends every ray to one "
            "focus."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — converging lens, p = 30 cm, f = 10 cm",
        "body": (
            "1/30 + 1/q = 1/10 → 1/q = 1/10 − 1/30 = 1/15 → q = +15 cm. "
            "M = −15/30 = −0.5. Verdict: real (q+ BEYOND the lens), inverted "
            "(M < 0), half size — the p > 2f camera-style case."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — object AT the focal point",
        "body": (
            "f = 10 cm, p = 10 cm: 1/10 + 1/q = 1/10 → 1/q = 0 → q → ∞. The "
            "rays leave the lens parallel — no image forms, exactly the "
            "transformation a lighthouse or projector collimator needs. This is "
            "NOT 'image at F'; F is where the object sits."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — the magnifying glass",
        "body": (
            "Same lens, object at p = 5 cm (< f): 1/5 + 1/q = 1/10 → 1/q = −1/10 "
            "→ q = −10 cm. M = −(−10)/5 = +2.0. Verdict: VIRTUAL image on the "
            "object's side of the lens, upright, twice the size — the inside-F "
            "magnifier act."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — diverging lens, p = 24 cm, f = −12 cm",
        "body": (
            "1/24 + 1/q = −1/12 → 1/q = −1/8 → q = −8 cm. M = −(−8)/24 = +1/3. "
            "Verdict: virtual, upright, one-third size — the diverging lens's "
            "single unconditional answer, matching the convex mirror's."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — camera focusing",
        "body": (
            "A mountain (p ≈ ∞) photographed through a converging lens with "
            "f = 50 mm: image at q ≈ f = 50 mm — the sensor sits one focal "
            "length behind the lens. Bring a flower to p = 25 cm: 1/250 + 1/q = "
            "1/50 (all in mm) → 1/q = 1/50 − 1/250 = 4/250 → q ≈ 62.5 mm. The "
            "lens must rack OUT ~12 mm to refocus — the mechanics behind every "
            "autofocus."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "The q-location flip",
        "body": "After mirrors, put real images IN FRONT — wrong for lenses. A lens's q+ lies BEYOND it; only virtual images return to the near side.",
    },
    {
        "section_type": "WARNING",
        "title": "There is no outside-the-lens for f",
        "body": "Converging f+ and diverging f− signs mirror the concave/convex rule — but the converging F is on the far side of the lens, not the near side as with a concave mirror.",
    },
    {
        "section_type": "WARNING",
        "title": "'q = ∞' read as 'image at F'",
        "body": "When p = f, 1/q = 0 — the image is AT INFINITY (parallel rays). It is not at the focal point; that is where the object stands.",
    },
    {
        "section_type": "WARNING",
        "title": "Chromatic fix = a single lens",
        "body": "No single lens removes chromatic aberration — it needs the ACHROMATIC DOUBLET, two lenses of different glass whose dispersions cancel. One lens only shifts the fringes.",
    },
    {
        "section_type": "WARNING",
        "title": "Aberration blur = 'out of focus'",
        "body": "Spherical aberration blurs because marginal and paraxial rays differ — even perfectly focused paraxial light is smeared by the edges. An aperture fixes it; moving the screen does not.",
    },
    {
        "section_type": "WARNING",
        "title": "M sign but new geography",
        "body": "M = −q/p gives the same meaning as mirrors (sign = orientation, |M| = size) — but q's sign now locates images on the far (real) or near (virtual) side of the lens.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The q-Side Flip (Mirrors → Lenses)",
        "body": (
            "Everything transfers except geography: a mirror reflects light back, "
            "so q+ is in FRONT; a lens transmits, so q+ is BEYOND it. Analogy: "
            "a tennis ball against a wall bounces back to your side; through a "
            "screen door it keeps travelling and lands deeper on the far side. "
            "Same math, flipped stage. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Six Converging-Lens Cases",
        "body": (
            "Six acts from infinity to inside F: at F (tiny sharp), between F "
            "and 2F (small), at 2F (same), F–2F (large), at F (infinity), inside "
            "F (virtual giant). Analogy: projector zoom — the object position "
            "dictates which act you see, and only the inside-F act is virtual. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Center Ray: Light That Never Bends",
        "body": (
            "A ray through the lens's center passes undeviated — a thin-lens "
            "miracle students often forget because refraction is 'supposed' to "
            "bend. Through the center the two surfaces are parallel and the lens "
            "behaves like a slab: out comes the same direction, just offset. "
            "Difficulty: EASY–MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Two Aberrations, Two Cures",
        "body": (
            "Chromatic is a MATERIALS failure (n varies with color; violet bends "
            "most; f_red > f_violet) — fixed by the glass pair of a doublet. "
            "Spherical is a SHAPE failure (marginal vs paraxial rays) — fixed by "
            "aperture or special surfaces. Analogy: colored fringes = bad "
            "eyeglass recipe; edge blur = bad curvature. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "f_red > f_violet and the order of colors",
        "body": (
            "Larger n (violet) ⇒ more bending ⇒ shorter focal length. Keep a "
            "mental ruler: red has the LONGEST f, violet the SHORTEST — "
            "rainbows order themselves and so do focal points. Difficulty: "
            "MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Converging lens: thick center, f+; diverging lens: thick edges, f−.\n"
            "• THE FLIP: lens real images land BEYOND the lens (q+ far side); mirror q+ was in front.\n"
            "• Lens equation 1/p + 1/q = 1/f; M = −q/p — mirror signs, flipped stage.\n"
            "• Six converging cases: ∞ → at F; >2f real-inverted-reduced; =2f real-inverted-same; f< p <2f real-inverted-enlarged; =f infinity; <f virtual-upright-enlarged.\n"
            "• Diverging lens: always virtual, upright, reduced.\n"
            "• Lens rays: parallel→F′; through-center undeviated; through F→parallel.\n"
            "• Instruments: camera (p > 2f → image at sensor near F); projector (f < p < 2f); magnifier (p < f).\n"
            "• Chromatic aberration: n varies with λ, violet bends most, f_red > f_violet — fix: achromatic doublet.\n"
            "• Spherical aberration: marginal vs paraxial rays — fix: aperture or specially shaped surface."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Converging/convex lens — thicker at center, f > 0, gathers parallel rays on the far side.\n"
            "• Diverging/concave lens — thicker at edges, f < 0, spreads rays from a virtual focus.\n"
            "• Optical center — the point where a ray passes undeviated.\n"
            "• Real image (lens) — formed by meeting rays BEYOND the lens, q+, screenable.\n"
            "• Virtual image (lens) — formed by extensions on the OBJECT side, q−.\n"
            "• Chromatic aberration — wavelength-dependent n smears colors; fix = achromatic doublet.\n"
            "• Spherical aberration — marginal vs paraxial focal mismatch; fix = aperture / shaping.\n"
            "• Focal plane — where distant rays converge; the camera sensor's home."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• 1/p + 1/q = 1/f — lens equation (mirror-style signs, q+ beyond the lens).\n"
            "• M = −q/p — magnification; sign = orientation, |M| = size.\n"
            "• Six-case landmarks: p = 2f → q = 2f, M = −1; p = f → q → ∞; p < f → q < 0, |M| > 1.\n"
            "• Chromatic order: f_red > f_violet (n_violet largest)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Lenses bend instead of bounce, so the only new rule is geography: "
            "is the image on the far side (q+, real, screenable — camera, "
            "projector) or the near side (q−, virtual — magnifier)? Converging "
            "lenses are thick-centered with f+; diverging thick-edged with f− "
            "and one eternal answer: virtual, upright, reduced. The equation is "
            "the mirror's own: 1/p + 1/q = 1/f, M = −q/p. Six cases: far "
            "objects shrink to F, p = 2f matches size, f-to-2f enlarges, p = f "
            "sends rays parallel, and inside F everything goes virtual-giant. "
            "Ray diagrams lean on the center ray, which never bends. Real glass "
            "then adds two fights: chromatic (violet bends most, f_red > "
            "f_violet — fix with a doublet) and spherical (edge rays vs center "
            "rays — fix with an aperture)."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Great Flip: Reading Lens Signs After Mirrors",
        "description": (
            "How the mirror sign convention transfers to lenses — with the one "
            "change that matters: real images live BEYOND the lens, not in "
            "front. The lens equation, its six cases, and worked examples."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The lens equation and its mirror-difference sign geography",
            "target_student": "First-year university student",
            "objective": "Solve 1/p + 1/q = 1/f for converging and diverging lenses and place the image on the correct side, with M = −q/p.",
            "hook": "Everything you already know about the mirror equation survives — one plot twist swapped the stage. Same math; the real images now live beyond the lens.",
            "explanation_steps": [
                "Converging (thick center, f+) vs diverging (thick edges, f−).",
                "The flip: lens q+ is on the FAR side; mirror q+ was in front.",
                "1/p + 1/q = 1/f; M = −q/p; signs otherwise unchanged.",
                "Worked: f = +10, p = 30 → q = +15, M = −0.5 (real, inverted, reduced).",
                "Worked: p = 10 = f → q = ∞; p = 5 < f → q = −10, M = +2.",
                "Diverging: f = −12, p = 24 → q = −8, M = +1/3 — always virtual.",
            ],
            "common_mistake": "Putting real images in front like mirrors; reading the p = f case as 'image at F'; forgetting that only the near side hosts virtuals.",
            "check": "A converging lens (f = 12 cm) holds an object at 30 cm. Locate the image and describe it completely — on which side?",
            "final_takeaway": "One equation, one sign ledger, one flip: lenses keep the mirror's math but move real images to their far side.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "From Projector to Magnifying Glass: The Zones of a Converging Lens",
        "description": (
            "The six object zones of a converging lens read from ray diagrams "
            "and the equation — camera, projector, and magnifier as real-world "
            "versions of three zones — plus the two aberrations and their fixes."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The six converging-lens cases and instrument geometry",
            "target_student": "First-year university student",
            "objective": "Predict image character across the six zones, map each zone to an instrument, and distinguish the two aberrations.",
            "hook": "Slide a photograph under a single lens and it runs the whole camera-to-magnifier menagerie: shrink, match, blow up, vanish, then reappear giant and upright.",
            "explanation_steps": [
                "Lens ray trio: parallel→F′; center ray undeviated; through F→parallel.",
                "Zone 1: p ≈ ∞ → image at F (camera sensor).",
                "Zone 2: p > 2f → real, inverted, reduced; p = 2f → same size.",
                "Zone 3: f < p < 2f → real, inverted, enlarged (projector).",
                "Zone 4: p = f → no image, collimated light.",
                "Zone 5: p < f → virtual, upright, enlarged (magnifying glass).",
                "Aberrations: chromatic (doublet fix) and spherical (aperture fix).",
            ],
            "common_mistake": "Confusing the projector's slide position with the camera's; forgetting the center ray; treating both aberrations as the same defect.",
            "check": "A conference projector must magnify a slide. Between which landmarks must the slide sit, and what type of image reaches the screen?",
            "final_takeaway": "Six zones, three instruments: cameras sit far, projectors mid, magnifiers near — and the two aberrations are defeated by glass pairing and aperture geometry.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "How can you identify a converging lens from a diverging lens by shape and by focal-length sign?",
        "options": [
            "Converging: thicker at the CENTER, f > 0; diverging: thicker at the EDGES, f < 0",
            "Converging: thicker at the edges, f < 0; diverging: thicker at the center, f > 0",
            "Converging: any symmetric shape, f is always +; diverging: always −",
            "The sign of f is set by the object distance, not the shape",
        ],
        "correct_index": 0,
        "explanation": "Converging (convex) lenses bulge in the center and take f > 0; diverging (concave) lenses are thick at the edges and take f < 0 — the sign rides the shape.",
        "skill": "lens type identification",
        "difficulty": 1,
        "competency_code": "thin-lenses",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What is 'the great flip' between mirrors and lenses in the sign convention?",
        "options": [
            "For a lens, real images land on the FAR side (q+ beyond the lens) because light passes through; a mirror's real image sat IN FRONT",
            "Lenses put all images in front; mirrors put all images behind",
            "The signs of f swap between mirrors and lenses",
            "For lenses, virtual images are also beyond the lens",
        ],
        "correct_index": 0,
        "explanation": "Light transmits through a lens, so its real (q+) images are beyond it; a mirror reflects, so its real images were on the incident side. p/f/M rules are otherwise unchanged.",
        "skill": "mirror-to-lens geography",
        "difficulty": 1,
        "competency_code": "thin-lenses",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What causes chromatic aberration, and how is it cured?",
        "options": [
            "n varies with wavelength; violet bends the MOST so f_red > f_violet; the fix is an ACHROMATIC DOUBLET of two different glasses",
            "The lens surface is imperfectly ground; the fix is polishing",
            "Marginal rays meet nearer than paraxial ones; the fix is a variable aperture",
            "Lenses absorb red light preferentially; the fix is a tinted coating",
        ],
        "correct_index": 0,
        "explanation": "Chromatic aberration is a materials effect — wavelength-dependent n spreads colors (violet strongest). A single lens cannot cure it; the achromatic doublet cancels the dispersions of two glasses.",
        "skill": "chromatic aberration cause and cure",
        "difficulty": 1,
        "competency_code": "chromatic-aberration",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What causes spherical aberration, and why does an aperture help?",
        "options": [
            "MARGINAL rays focus nearer than PARAXIAL rays (a spherical surface is not exactly focusing); cutting the marginal rays with an aperture restores one sharp focus",
            "Short wavelengths focus long; the fix is polishing the edges",
            "The lens bends red and violet differently; the fix is an achromatic pair",
            "The image is upside down; the fix is a second lens",
        ],
        "correct_index": 0,
        "explanation": "Spherical aberration is a geometry defect: edge (marginal) rays meet the axis closer than center (paraxial) rays, blurring even monochromatic images. An aperture removes the marginal rays, and shaped surfaces collimate them.",
        "skill": "spherical aberration cause and cure",
        "difficulty": 1,
        "competency_code": "spherical-aberration",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A converging lens f = +10 cm holds an object at p = 30 cm. Locate the image and its magnification.",
        "options": [
            "1/q = 1/10 − 1/30 = 1/15 → q = +15 cm (BEYOND the lens); M = −0.5: real, inverted, reduced",
            "q = +7.5 cm; M = −0.25",
            "q = −15 cm; M = +0.5: virtual, upright",
            "q = +30 cm; M = −1: real, same size",
        ],
        "correct_index": 0,
        "explanation": "1/30 + 1/q = 1/10 → q = +15 cm beyond the lens; M = −15/30 = −0.5. Positive q is the far side — the p > 2f camera-style case.",
        "skill": "lens equation beyond-F case",
        "difficulty": 2,
        "competency_code": "lens-equation",
    },
    {
        "level": "APPLY",
        "prompt": "Same converging lens (f = +10 cm) with the object at p = 5 cm. Describe the image.",
        "options": [
            "1/q = 1/10 − 1/5 = −1/10 → q = −10 cm; M = +2: VIRTUAL, upright, enlarged — on the object's side",
            "q = +3.3 cm; M = −0.67: real, inverted, reduced",
            "q = +10 cm; M = −2: real, inverted, enlarged",
            "q = −3.3 cm; M = +0.67: virtual, upright, reduced",
        ],
        "correct_index": 0,
        "explanation": "p < f gives 1/q = −1/10 → q = −10 cm (object side), M = −(−10)/5 = +2: virtual, upright, twice the size — the magnifying-glass case.",
        "skill": "inside-F magnifier case",
        "difficulty": 2,
        "competency_code": "lens-equation",
    },
    {
        "level": "APPLY",
        "prompt": "A diverging lens has f = −12 cm with the object at p = 24 cm. Find q and M.",
        "options": [
            "1/q = −1/12 − 1/24 = −1/8 → q = −8 cm; M = +1/3: virtual, upright, reduced",
            "1/q = −1/24 → q = −24 cm; M = +1",
            "q = +8 cm; M = −1/3: real, inverted, reduced",
            "q = −36 cm; M = +1.5: virtual, enlarged",
        ],
        "correct_index": 0,
        "explanation": "The diverging lens's one verdict: q = −8 cm, M = +1/3 — virtual, upright, reduced, always, for every object position.",
        "skill": "diverging lens computation",
        "difficulty": 2,
        "competency_code": "lens-equation",
    },
    {
        "level": "APPLY",
        "prompt": "For a converging lens (f = 10 cm), an object sits at p = 2f = 20 cm. Using the lens rays, what is the image?",
        "options": [
            "q = 2f = 20 cm BEYOND the lens; M = −1: real, inverted, SAME SIZE (rays cross at 2F′)",
            "q = 10 cm at F′; M = −0.5: real, reduced",
            "q = −20 cm; M = +1: virtual, same size",
            "No image: all rays emerge parallel",
        ],
        "correct_index": 0,
        "explanation": "At p = 2f the lens ray trio crosses exactly at 2F′ beyond the lens: q = 2f, M = −1 — the symmetric same-size act. The center ray keeps this case trivially constructible.",
        "skill": "2f ray-diagram case",
        "difficulty": 2,
        "competency_code": "lens-ray-diagrams",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "A projector must throw a REAL, ENLARGED image of a slide across a room with a converging lens of f = 10 cm. Where must the slide sit, and where does the screen go?",
        "options": [
            "Slide between F and 2f (10 < p < 20 cm); screen beyond 2F′ — f < p < 2f gives q > 2f, real, inverted, enlarged",
            "Slide beyond 2f (p > 20 cm); screen between F and 2F′ — reduced, wrong for projecting",
            "Slide inside F (p < 10 cm): virtual, unreachable screen",
            "Slide exactly at F (p = 10 cm): collimated beam to the screen",
        ],
        "correct_index": 0,
        "explanation": "Projection needs an enlarged real image: object between f and 2f → q beyond 2f, inverted and enlarged — the slide must live in the F–2F zone and the screen beyond 2F′.",
        "skill": "instrument-zone design",
        "difficulty": 3,
        "competency_code": "lens-equation",
    },
    {
        "level": "TRANSFER",
        "prompt": "Design a camera: a lens of f = 50 mm must capture a distant scene (p ≈ ∞). Where is the sensor, and how far must it move to instead focus an object at 25 cm?",
        "options": [
            "Distant: sensor at the focal plane, q ≈ f = 50 mm; at p = 25 cm: 1/250 + 1/q = 1/50 → q ≈ 62.5 mm, so rack OUT ≈ 12 mm",
            "Distantly: sensor at 2f = 100 mm; near object changes nothing",
            "Distant: sensor at 10 mm; at 25 cm: q ≈ 48 mm",
            "The same focal-plane position works for every distance — cameras have no moving parts",
        ],
        "correct_index": 0,
        "explanation": "Distant rays focus at the focal plane (q ≈ f = 50 mm); 25 cm requires q ≈ 62.5 mm. The 12 mm rack is exactly what focusing mechanisms do.",
        "skill": "camera focus computation",
        "difficulty": 3,
        "competency_code": "lens-ray-diagrams",
    },
    {
        "level": "TRANSFER",
        "prompt": "You inspect a telescope photo: stars show red-and-blue fringes at their edges. Which aberration is this, and which color forms the near-side focus?",
        "options": [
            "CHROMATIC aberration — violet (largest n) bends most and focuses NEAREST; f_red > f_violet; the fix is an achromatic doublet",
            "SPHERICAL aberration — edge rays focus closer; the fix is an aperture",
            "Both aberrations are identical; the fix is polishing",
            "It is a diffraction artifact; no lens defect is involved",
        ],
        "correct_index": 0,
        "explanation": "Colored fringes betray wavelength-dependent n: violet focuses nearest (f_violet smallest), red farthest. That is chromatic aberration's fingerprint — cured with a two-glass doublet, not an aperture.",
        "skill": "aberration diagnosis",
        "difficulty": 3,
        "competency_code": "chromatic-aberration",
    },
    {
        "level": "TRANSFER",
        "prompt": "A B/W photograph shot wide-open is blurred even in white light with no color fringes; stopping the lens to a small aperture sharpens it. Diagnose the defect.",
        "options": [
            "SPHERICAL aberration — monochromatic blur from marginal rays focusing before paraxial ones; an aperture removes them",
            "Chromatic aberration — but it must be both colors; an aperture cannot help",
            "Turned a diverging lens's normal virtual blur into real blur",
            "An aperture defect; changing geometry is irrelevant",
        ],
        "correct_index": 0,
        "explanation": "Monochrome edge blur that an aperture cures is spherical aberration's signature: marginal vs paraxial mismatch. Chromatic needs a doublet (and shows color), not an aperture.",
        "skill": "aberration differential diagnosis",
        "difficulty": 3,
        "competency_code": "spherical-aberration",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "refraction-snell",
        "title": "Refraction and Snell's Law",
        "taxonomy_level": "apply",
        "description": "Apply n = c/v and n₁sinθ₁ = n₂sinθ₂, and explain that frequency is invariant while speed and wavelength scale by n.",
        "sort_order": 45,
    },
    {
        "code": "mirror-equation",
        "title": "The Mirror Equation",
        "taxonomy_level": "apply",
        "description": "Solve 1/p + 1/q = 1/f = 2/R with the full sign convention and compute mirror power F = 1/f in diopters.",
        "sort_order": 52,
    },
    {
        "code": "thin-lenses",
        "title": "Converging and Diverging Lenses",
        "taxonomy_level": "understand",
        "description": "Identify converging (thick center, f+) vs diverging (thick edges, f−) lenses and the image-side flip vs mirrors.",
        "sort_order": 54,
    },
    {
        "code": "lens-equation",
        "title": "The Lens Equation and Its Six Cases",
        "taxonomy_level": "apply",
        "description": "Solve 1/p + 1/q = 1/f with M = −q/p, place images on the correct side, and characterize all six converging-lens cases.",
        "sort_order": 55,
    },
    {
        "code": "lens-ray-diagrams",
        "title": "Lens Ray Diagrams and Instruments",
        "taxonomy_level": "apply",
        "description": "Trace the three lens principal rays (parallel→F′, center undeviated, through F→parallel) and map zones to camera, projector, and magnifier.",
        "sort_order": 56,
    },
    {
        "code": "chromatic-aberration",
        "title": "Chromatic Aberration",
        "taxonomy_level": "understand",
        "description": "Explain wavelength-dependent n (violet bends most, f_red > f_violet) and the achromatic-doublet fix.",
        "sort_order": 57,
    },
    {
        "code": "spherical-aberration",
        "title": "Spherical Aberration",
        "taxonomy_level": "understand",
        "description": "Explain the marginal-vs-paraxial focal mismatch and the aperture and surface-shaping fixes.",
        "sort_order": 58,
    },
]

COMPETENCY_PREREQUISITES = [
    ("refraction-snell", "thin-lenses"),
    ("mirror-equation", "lens-equation"),
    ("thin-lenses", "lens-ray-diagrams"),
    ("lens-ray-diagrams", "lens-equation"),
    ("lens-equation", "chromatic-aberration"),
    ("lens-equation", "spherical-aberration"),
]

LESSON_COMPETENCIES = [
    {"code": "thin-lenses", "role": "teaches"},
    {"code": "lens-equation", "role": "teaches"},
    {"code": "lens-ray-diagrams", "role": "teaches"},
    {"code": "chromatic-aberration", "role": "teaches"},
    {"code": "spherical-aberration", "role": "teaches"},
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

"""PHY211 — Physics, Module 6, Lecture 8: Magnetic Fields and Forces.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 8, Fall 2024 —
'Magnetic Fields', Chapter 7).

Opens the magnetism arc: dipoles and monopoles, the field B, the force on a
moving charge, circular motion in a uniform field, and the derivation of the
force on a current-carrying wire. Imported by ``curriculum.content`` and
seeded by ``curriculum.seed``.
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
    "code": "M6",
    "title": "Module 6 — Magnetic Fields & Forces",
    "description": (
        "Chapter 7: the field that surrounds moving charges — magnetic poles "
        "and the absent monopole, the field B, the sideways force F = qv × B "
        "with the right-hand rule, circular motion in a uniform field, and the "
        "macroscopic force on a current-carrying wire."
    ),
    "sort_order": 6,
}

LESSON = {
    "code": "L8",
    "title": "Magnetic Fields: Poles, the Force on a Moving Charge, and Force on a Wire",
    "description": (
        "Lecture 8 — the operating field of magnetism: why every magnet is a "
        "dipole, how B is defined, the sideways force F = |q|vB sin θ on a "
        "moving charge, circle motion r = mv/(|q|B), and the derivation of the "
        "current-wire force F = IL × B from counting charge carriers."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "State the pole-interaction rules, the 1/r² pole force, and why no magnetic monopole can be isolated.",
        "Define B operationally (compass-north direction) and describe the N → S field-line pattern outside a magnet.",
        "Compute the force F = |q|vB sin θ (zero when v ∥ B, |q|vB when v ⊥ B) on any moving charge.",
        "Find the force direction with the right-hand rule for v × B and flip it for negative charges.",
        "Convert fields between tesla (1 T = 1 N/(A·m)) and gauss (1 T = 10⁴ G).",
        "Apply uniform circular motion r = mv/(|q|B) and ω = v/r, and derive ω = |q|B/m.",
        "Reproduce the derivation F = (qv × B)nAL → F = IL × B and apply F = BIL sin θ.",
    ],
    "prerequisites": [
        "Electric current I = Q/t and the carrier picture of a wire (Lecture 6).",
        "Properties of electric charge, including the sign rule for positive/negative charge (Lecture 1).",
        "Uniform circular motion: centripetal force and angular speed.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Magnetism looks like electricity but lives one level deeper: every "
            "magnet is a dipole with north and south, never a single pole; the "
            "field B surrounds MOVING charge, not static charge; and the force that "
            "field exerts is always sideways — perpendicular to both the motion "
            "and the field. This lecture banks those three facts, then shows a "
            "current-carrying wire is just a river of charges, so its force "
            "collapses to F = BIL sin θ."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Magnetic Poles: The Dipole Rule",
        "body": (
            "Every magnet, whatever its shape, has exactly two poles — north and "
            "south — and poles interact like electric charges: like poles repel "
            "(N–N, S–S), unlike attract (N–S). The pole force falls off as the "
            "inverse square of distance. The names come from suspension in "
            "Earth's field: a freely turning bar magnet rotates until its north "
            "pole points toward Earth's geographic north."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "No magnetic monopoles",
        "body": (
            "Cut a bar magnet in half and you get two smaller COMPLETE magnets, "
            "each with a north AND a south pole. Cut again: the same, forever. A "
            "single isolated pole has never been observed — magnetism is "
            "fundamentally dipolar."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Magnetic Fields and Field Lines",
        "body": (
            "Any MOVING electric charge — and any magnet — fills the space around "
            "it with a magnetic field B. The operational definition of direction: "
            "the direction of B at any location is the direction the north pole of "
            "a compass needle points there. Outside a magnet, field lines run from "
            "the north pole to the south pole. (Instructor note: into-page fields "
            "are drawn ⊗, out-of-page fields ⊙.)"
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Force on a moving charge (magnitude)",
        "body": "F_B = |q| v B sin θ",
        "metadata": {
            "meaning": "The magnetic force on a charge q moving with speed v in a field B, where θ is the angle BETWEEN v and B.",
            "when_used": "Every moving-charge force problem. Minimum F = 0 when v ∥ B (θ = 0° or 180°); maximum |q|vB when v ⊥ B (θ = 90°).",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Alignment kills the force",
        "body": (
            "Moving parallel to the field gives sin θ = 0 — the force vanishes no "
            "matter how fast or how strong the field. Perpendicularity maximizes "
            "it. Identify the angle BETWEEN the velocity and the field before "
            "substituting anything."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Force direction: the vector law",
        "body": "F_B = q v × B",
        "metadata": {
            "meaning": "The force is a CROSS product: perpendicular to BOTH v and B. Direction from the right-hand rule (fingers along v, curl toward B, thumb = force for a POSITIVE charge).",
            "when_used": "Direction problems, including into/out-of-page notation. NEGATIVE charges reverse the answer — solve for a positive charge, then flip.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Sideways, never forward",
        "body": (
            "The magnetic force never points along v and never along B — it is "
            "perpendicular to both, every time. Contrast gravity (along g) and "
            "electric forces (along E): magnetism is the sideways force. Flip for "
            "electrons."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Units of B",
        "body": "1 T = 1 Wb/m² = 1 N/(C·m/s) = 1 N/(A·m)     and     1 T = 10⁴ gauss",
        "metadata": {
            "meaning": "The tesla is built from the force law; the gauss is the common non-SI unit.",
            "when_used": "Convert gauss to tesla (divide by 10⁴) before substituting into any formula.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Force on a TV electron",
        "body": (
            "An electron in an old TV tube moves at 8.0 × 10⁶ m/s; coils create a "
            "0.025 T field at 60° to its velocity. θ = 60° (the angle between the "
            "given vectors), so F = |q|vB sin θ = (1.6 × 10⁻¹⁹)(8.0 × 10⁶)(0.025)"
            "(sin 60°) = 2.8 × 10⁻¹⁴ N. Magnitude only — direction needs the "
            "right-hand rule, then a flip because the charge is negative."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Circular motion in a uniform field",
        "body": "|q| v B = mv²/r  →  r = mv/(|q|B)     and     ω = v/r",
        "metadata": {
            "meaning": "With v ⊥ B the magnetic force is always centripetal: constant magnitude, always toward the center — the particle circles at constant speed.",
            "when_used": "Find r, v, or B for a circling particle. r ∝ momentum; r ∝ 1/(|q|B). Combining the two formulas gives ω = |q|B/m (independent of v).",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "The field steers, it doesn't push",
        "body": (
            "A perpendicular force changes the DIRECTION of the velocity, never its "
            "magnitude — that is uniform circular motion. The particle never speeds "
            "up in the uniform field."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Proton orbit speed",
        "body": (
            "A proton circles with r = 0.14 m in a 0.35 T field. From "
            "r = mv/(|q|B): v = |q|rB/m = (1.6 × 10⁻¹⁹)(0.14)(0.35)/(1.67 × 10⁻²⁷) "
            "= 4.7 × 10⁶ m/s. ω = v/r = 3.4 × 10⁷ rad/s. Double the speed: the "
            "radius doubles, ω = |q|B/m unchanged."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Force on a current-carrying wire",
        "body": "F_B = I L × B    with    magnitude F_B = B I L sin θ",
        "metadata": {
            "meaning": "L is a VECTOR pointing along the current with magnitude equal to the segment length; θ is the angle between the wire (current) and B. Zero when the wire is parallel to B; maximum BIL when perpendicular.",
            "when_used": "Force on any straight current-carrying segment; direction from the same right-hand rule.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "From one charge to a whole wire",
        "body": (
            "Each carrier in the wire feels q v × B. A straight segment of length L "
            "and cross-section A has volume AL, holding nAL carriers, so the total "
            "force is F = (qv × B)nAL. The current relation I = nqAv regroups the "
            "swarm (v and L both lie along the wire), collapsing everything into "
            "F = IL × B — one macroscopic law hiding an army of charges."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Wire in a field",
        "body": (
            "A 0.50 m wire carries 2.0 A perpendicular to a 0.10 T field: "
            "F = BIL = (0.10)(2.0)(0.50) = 0.10 N. Tilted to 60° instead: "
            "F = BIL sin 60° ≈ 0.087 N. Laid parallel to B: F = 0."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — force on a TV electron",
        "body": (
            "An electron in an old-style picture tube moves toward the screen at "
            "8.0 × 10⁶ m/s; a 0.025 T field lies at 60° to its velocity. Step 1: "
            "θ = 60°. Step 2: F = |q|vB sin θ. Step 3: F = (1.6 × 10⁻¹⁹)(8.0 × 10⁶)"
            "(0.025)(0.866) = 2.8 × 10⁻¹⁴ N. The formula gives the magnitude; the "
            "direction requires the right-hand rule for v × B followed by a flip "
            "because the charge is negative."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — proton orbit speed",
        "body": (
            "A proton (m = 1.67 × 10⁻²⁷ kg) circles with radius 14 cm in a uniform "
            "0.35 T field perpendicular to its velocity. From r = mv/(|q|B): "
            "v = |q|rB/m = (1.6 × 10⁻¹⁹)(0.14)(0.35)/(1.67 × 10⁻²⁷) = 4.7 × 10⁶ m/s. "
            "Extension: ω = v/r = 3.4 × 10⁷ rad/s."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — force on a current-carrying wire",
        "body": (
            "A straight 0.50 m wire carries 2.0 A perpendicular to a 0.10 T uniform "
            "field. θ = 90° → sin θ = 1 → F = BIL = (0.10)(2.0)(0.50) = 0.10 N. At "
            "60° to the field: F = 0.10 × sin 60° ≈ 0.087 N. Parallel to the field: "
            "F = 0."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — direction workout",
        "body": (
            "A proton moves due east, B points due north: right-hand rule (fingers "
            "east, curl toward north) gives the force UP, out of the ground. Same "
            "motion, electron: flip → force DOWN, same magnitude. B into the page "
            "(⊗), proton moving right: v × B = up the page. Direction problems are "
            "always two steps: right-hand rule, then a sign check."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Force along B",
        "body": "The magnetic force is a CROSS product — perpendicular to BOTH v and B. It never points along the field, unlike gravity along g.",
    },
    {
        "section_type": "WARNING",
        "title": "The missing flip for electrons",
        "body": "F = qv × B: a negative charge reverses the force direction. Solve for a positive charge, then flip if q < 0.",
    },
    {
        "section_type": "WARNING",
        "title": "Angle from the surface or normal",
        "body": "θ is strictly the angle between v and B. If a problem gives an angle to another reference, convert before substituting — and never use the complement.",
    },
    {
        "section_type": "WARNING",
        "title": "Dropping sin θ",
        "body": "F = |q|vB is the MAXIMUM, valid only at θ = 90°. The general case needs F = |q|vB sin θ; sin 90° = 1 recovers the maximum.",
    },
    {
        "section_type": "WARNING",
        "title": "Gauss and tesla mixed",
        "body": "1 G = 10⁻⁴ T. A field given in gauss is off by 10⁴ if fed into a formula raw — convert to tesla first.",
    },
    {
        "section_type": "WARNING",
        "title": "Inverting r = mv/(|q|B)",
        "body": "The radius grows with momentum and shrinks with field and charge: fast/heavy = big circle; strong field/charge = small circle.",
    },
    {
        "section_type": "WARNING",
        "title": "Expecting the particle to speed up",
        "body": "The magnetic force is centripetal — it changes the DIRECTION of v, not its magnitude. No acceleration along the path.",
    },
    {
        "section_type": "WARNING",
        "title": "θ from the wrong line for wires",
        "body": "In F = BIL sin θ, θ is between the wire (current direction) and B itself — not between the wire and the normal or the page.",
    },
    {
        "section_type": "WARNING",
        "title": "L as a bare number",
        "body": "L is a VECTOR along the current. Assign it the current's direction before applying the right-hand rule to IL × B.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Right-Hand Rule and the Cross-Product Direction",
        "body": (
            "The answer lives in 3-D, perpendicular to two given vectors at once. "
            "Fingers along v, curl toward B, thumb = force for a positive charge; "
            "flip if q < 0. If v is parallel to B no curl is possible — force zero. "
            "Analogy: a car in a crosswind is shoved sideways, neither forward "
            "(along v) nor along the wind. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Zero-Force Alignment (v ∥ B)",
        "body": (
            "Intuition says maximum alignment with the field should mean maximum "
            "effect — but sin θ kills the force exactly when motion and field line "
            "up. A rudder works only when water flows ACROSS its blade; flow along "
            "it and nothing turns. θ = 0° or 180° → F = 0; θ = 90° → |q|vB. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Circular Motion from a Perpendicular Force",
        "body": (
            "Students expect forces to speed things up, but a force always "
            "perpendicular to the velocity changes only its direction — uniform "
            "circular motion. Setting |q|vB equal to the centripetal demand gives "
            "r = mv/(|q|B); solve for whichever quantity is asked (r, v, or B). "
            "Analogy: swinging a ball on a string — inward pull, constant speed. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "From Single Charges to a Whole Wire (the F = BIL derivation)",
        "body": (
            "A microscopic-to-macroscopic leap: each carrier feels qv × B; a "
            "segment of volume AL holds nAL carriers; the total is (qv × B)nAL; "
            "substituting I = nqAv collapses everything into F = IL × B. Analogy: "
            "rain on a windshield — (force per drop) × (number of drops). The "
            "wire's neutrality cancels NET charge, not the carriers' motion. "
            "Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "No Magnetic Monopoles",
        "body": (
            "Electricity is built from isolated charges, so students assume "
            "magnetism has isolated poles too — it does not. Every fragment of a "
            "divided magnet keeps both poles. Analogy: a coin — cut however finely, "
            "every piece still has a head and a tail. Difficulty: EASY."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Every magnet is a dipole — like poles repel, unlike attract, force ∝ 1/r²; no monopole exists.\n"
            "• Moving charge and magnets set up B; direction = where a compass north points; lines outside run N → S.\n"
            "• F = |q|vB sin θ — zero when v ∥ B, maximum |q|vB when v ⊥ B.\n"
            "• Direction: perpendicular to both v and B; right-hand rule, then FLIP for negative charges.\n"
            "• 1 T = 1 N/(A·m) = 10⁴ gauss.\n"
            "• v ⊥ B ⇒ uniform circular motion: |q|vB = mv²/r, r = mv/(|q|B), ω = v/r = |q|B/m.\n"
            "• A current is a stream of charges: F = (qv × B)nAL → F = IL × B, F = BIL sin θ."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Magnetic pole — the two (N and S) ends of every magnet; like repel, unlike attract.\n"
            "• Magnetic monopole — an isolated single pole — never observed; cutting always yields N–S pairs.\n"
            "• Magnetic field B — region around moving charges and magnets; direction = compass-north direction.\n"
            "• Tesla — SI unit of B: 1 T = 1 N/(A·m) = 10⁴ gauss.\n"
            "• Centripetal force — the inward force |q|vB that bends a perpendicular velocity into a circle.\n"
            "• L (in F = IL × B) — vector along the current, magnitude = segment length."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• F = qv × B — vector force on a moving charge.\n"
            "• F = |q|vB sin θ — magnitude; θ between v and B.\n"
            "• 1 T = 1 N/(A·m) = 10⁴ G — units.\n"
            "• |q|vB = mv²/r ⇒ r = mv/(|q|B); ω = v/r ⇒ ω = |q|B/m — circular motion.\n"
            "• I = nqAv; F = (qv × B)nAL ⇒ F = IL × B; F = BIL sin θ — wire force."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Every magnet has two poles; like repel, unlike attract, force ∝ 1/r² — "
            "no monopoles, ever. Moving charges and magnets make B; its direction "
            "is compass-north; lines outside run N → S. Force on a moving charge: "
            "F = |q|vB sin θ — zero parallel, max |q|vB perpendicular; direction "
            "perpendicular to both, right-hand rule, flip for negative charges. "
            "Units: 1 T = 1 N/(A·m) = 10⁴ G. v ⊥ B ⇒ circle: r = mv/(|q|B), "
            "ω = v/r — the field steers, never pushes. A wire is a river of "
            "charges: count nAL carriers, fold in I = nqAv, and get F = BIL sin θ, "
            "θ between current and field."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Sideways Force: Mastering the Right-Hand Rule",
        "description": (
            "Magnitude and direction of the magnetic force F = qv × B: the "
            "sin θ factor, the right-hand rule, the flip for negative charges, "
            "and the TV-electron example."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Direction and magnitude of the magnetic force F = qv × B",
            "target_student": "First-year university student",
            "objective": "Determine both magnitude and direction of the magnetic force on any moving charge, including negative charges.",
            "hook": "Old TVs steered electrons in flight with pure magnetism — never touching them. The push is never forward and never along the field — always sideways.",
            "explanation_steps": [
                "Magnitude F = |q|vB sin θ: zero when v ∥ B, max when perpendicular.",
                "Direction perpendicular to both v and B (cross product).",
                "Right-hand rule: fingers along v, curl toward B, thumb = F for positive charge.",
                "Negative charge → flip the answer.",
                "Page notation: ⊙ out of the page, ⊗ into the page.",
                "Worked example: electron at 8.0 × 10⁶ m/s, B = 0.025 T at 60° → 2.8 × 10⁻¹⁴ N.",
            ],
            "common_mistake": "Forgetting the flip for negative charges; measuring the angle from the surface instead of between v and B.",
            "check": "A proton moves north; B points east. Which way is the force?",
            "final_takeaway": "Magnetic force = cross product: perpendicular to both v and B, proportional to sin θ, reversed for negative charges.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "From One Charge to a Whole Wire: Where F = BIL Comes From",
        "description": (
            "The derivation of the force on a current-carrying conductor from the "
            "single-charge law: counting nAL carriers and collapsing via "
            "I = nqAv into F = IL × B."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Derivation of the force on a current-carrying conductor from the single-charge law",
            "target_student": "First-year university student",
            "objective": "Reproduce and explain the derivation F = (qv × B)nAL → F = IL × B, and apply F = BIL sin θ.",
            "hook": "Inside every electric motor a plain copper wire jumps in a magnetic field — but magnetic forces act on MOVING charges, and a wire is just metal sitting still. The resolution: a current is charges in motion, and we can count them.",
            "explanation_steps": [
                "One carrier feels qv × B.",
                "A segment of length L and area A has volume AL → nAL carriers.",
                "Total force = (qv × B) · nAL.",
                "The current relation I = nqAv.",
                "Since v and L lie along the wire, the scalars regroup → F = IL × B, magnitude BIL sin θ.",
                "Worked numbers: 0.50 m, 2.0 A, 0.10 T ⊥ → 0.10 N; 60° → 0.087 N; parallel → 0.",
            ],
            "common_mistake": "Measuring θ between the wire and the normal/page; treating L as a directionless length; feeding gauss without converting.",
            "check": "Double the current and halve the length — what happens to the force? And if the wire lies parallel to B?",
            "final_takeaway": "A wire is a river of charges: count the carriers (nAL), fold in I = nqAv, and the single-charge law becomes F = BIL sin θ.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "State the two pole-interaction rules for magnets, and how the pole force depends on distance.",
        "options": [
            "Like poles repel, unlike attract; the pole force varies as 1/r²",
            "Like poles and unlike poles both repel; force varies as 1/r",
            "North attracts north, south attracts south; force is constant with distance",
            "Like poles attract, unlike poles repel; force varies as 1/r²",
        ],
        "correct_index": 0,
        "explanation": "N–N or S–S repel; N–S attract — like electric charges but for poles; the force falls off as the inverse square of the separation.",
        "skill": "pole rules and 1/r² force",
        "difficulty": 1,
        "competency_code": "magnetic-poles",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What happens when a bar magnet is cut in half — and why does this make an isolated magnetic pole impossible?",
        "options": [
            "You get two smaller COMPLETE magnets, each with its own N and S; every fragment remains a dipole, so a single pole can never be isolated",
            "You get one 'north-only' and one 'south-only' magnet",
            "The two halves become non-magnetic",
            "You get two complete magnets only if the cut is clean; a jagged cut separates the poles",
        ],
        "correct_index": 0,
        "explanation": "Cutting never separates poles: each piece keeps a north and a south pole. Magnetism is fundamentally dipolar — no monopole has ever been observed.",
        "skill": "the absent monopole",
        "difficulty": 1,
        "competency_code": "magnetic-poles",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "How is the direction of B at a point defined experimentally — and what surrounds any MOVING electric charge, in addition to its electric field?",
        "options": [
            "B's direction is where a compass needle's north pole points there; a moving charge is surrounded by a magnetic field (a static one is not)",
            "B's direction is where the field lines end at the south pole; moving charges only feel electric forces",
            "B's direction is along the charge's velocity; only magnets produce fields",
            "B's direction is defined by the force direction on a static charge",
        ],
        "correct_index": 0,
        "explanation": "A compass at any location tracks B's direction (its north pole points along B). A moving charge sets up a magnetic field; motion is the essential ingredient.",
        "skill": "operational definition of B",
        "difficulty": 1,
        "competency_code": "magnetic-fields",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "When is the magnetic force on a moving charge exactly zero, and what is its maximum value?",
        "options": [
            "Zero when v ∥ B (θ = 0° or 180°); maximum |q|vB when v ⊥ B (θ = 90°)",
            "Zero when v ⊥ B; maximum |q|vB when v ∥ B",
            "Zero when the speed is low; maximum qvB² always",
            "The force is never zero for a moving charge in a field",
        ],
        "correct_index": 0,
        "explanation": "F = |q|vB sin θ: sin θ vanishes for parallel (or antiparallel) velocity, and maxes at 1 for perpendicular motion — alignment kills the force entirely.",
        "skill": "zero-force and maximum conditions",
        "difficulty": 1,
        "competency_code": "magnetic-force-charge",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A charge of +2.0 μC moves at 3.0 × 10⁴ m/s in a 0.040 T field, with its velocity at 30° to the field. Find the force.",
        "options": [
            "F = (2.0 × 10⁻⁶)(3.0 × 10⁴)(0.040)(sin 30°) = 1.2 × 10⁻³ N",
            "F = (2.0 × 10⁻⁶)(3.0 × 10⁴)(0.040) = 2.4 × 10⁻³ N",
            "F = (2.0 × 10⁻⁶)(3.0 × 10⁴)(0.040)(sin 60°) = 2.1 × 10⁻³ N",
            "F = (2.0 × 10⁻⁶)(3.0 × 10⁴)/(0.040) = 1.5 N",
        ],
        "correct_index": 0,
        "explanation": "θ = 30° between v and B, so include sin 30° = 0.5. F = (2.0 × 10⁻⁶)(3.0 × 10⁴)(0.040)(0.5) = 1.2 × 10⁻³ N. Dropping sin θ overstates by 2×.",
        "skill": "sin θ with the correct angle",
        "difficulty": 2,
        "competency_code": "magnetic-force-charge",
    },
    {
        "level": "APPLY",
        "prompt": "A proton (m = 1.67 × 10⁻²⁷ kg) moves at 3.0 × 10⁶ m/s perpendicular to a 0.20 T field. Find the radius of its circular path.",
        "options": [
            "r = (1.67 × 10⁻²⁷ × 3.0 × 10⁶)/(1.6 × 10⁻¹⁹ × 0.20) ≈ 0.157 m",
            "r = (1.6 × 10⁻¹⁹ × 0.20)/(1.67 × 10⁻²⁷ × 3.0 × 10⁶) ≈ 6.4 × 10⁹ m",
            "r = (1.67 × 10⁻²⁷ × 3.0 × 10⁶) × (1.6 × 10⁻¹⁹ × 0.20) ≈ 1.6 × 10⁻³⁹ m",
            "r = (3.0 × 10⁶)/(0.20) = 1.5 × 10⁷ m",
        ],
        "correct_index": 0,
        "explanation": "r = mv/(|q|B) = (1.67 × 10⁻²⁷ × 3.0 × 10⁶)/(1.6 × 10⁻¹⁹ × 0.20) = 0.157 m. Momentum on top, charge×field on the bottom.",
        "skill": "orbit radius formula",
        "difficulty": 2,
        "competency_code": "circular-motion-field",
    },
    {
        "level": "APPLY",
        "prompt": "A 1.5 m straight wire carries 5.0 A at 60° to a 0.30 T field. Find the force on it.",
        "options": [
            "F = (0.30)(5.0)(1.5)(sin 60°) ≈ 1.9 N",
            "F = (0.30)(5.0)(1.5) = 2.25 N",
            "F = (0.30)(5.0)(1.5)(sin 30°) ≈ 1.1 N",
            "F = (0.30)(5.0)/(1.5) = 1.0 N",
        ],
        "correct_index": 0,
        "explanation": "F = BIL sin θ with θ the angle between the wire and B: (0.30)(5.0)(1.5)(0.866) ≈ 1.95 N ≈ 1.9 N. Dropping sin 60° overstates by ~16%.",
        "skill": "wire force with angle",
        "difficulty": 2,
        "competency_code": "force-current-wire",
    },
    {
        "level": "APPLY",
        "prompt": "Convert: (a) 0.005 T to gauss; (b) 0.50 gauss to tesla.",
        "options": [
            "(a) 0.005 T = 50 G; (b) 0.50 G = 5.0 × 10⁻⁵ T",
            "(a) 0.005 T = 5 × 10⁻⁵ G; (b) 0.50 G = 5000 T",
            "(a) 0.005 T = 500 G; (b) 0.50 G = 5 × 10⁻⁴ T",
            "(a) 0.005 T = 50 G; (b) 0.50 G = 50 T",
        ],
        "correct_index": 0,
        "explanation": "1 T = 10⁴ G: 0.005 × 10⁴ = 50 G; and 0.50/10⁴ = 5.0 × 10⁻⁵ T. Test: a 0.025 T TV field is 250 G.",
        "skill": "gauss↔tesla conversion",
        "difficulty": 2,
        "competency_code": "magnetic-fields",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Starting from r = mv/(|q|B) and ω = v/r, derive an expression for ω that contains no v. If a proton doubles its speed in a fixed field, what happens to r and ω?",
        "options": [
            "ω = v/(mv/|q|B) = |q|B/m — independent of v; doubling v doubles r and leaves ω unchanged",
            "ω = mv/|q|B — doubling v doubles ω and r",
            "ω = |q|vB/m — doubling v doubles both r and ω",
            "No such expression exists; ω always depends on v",
        ],
        "correct_index": 0,
        "explanation": "ω = v/r = v/(mv/|q|B) = |q|B/m, which has no v. Doubling the speed doubles the radius (r ∝ v) but the angular speed ω = |q|B/m stays put.",
        "skill": "algebraic elimination for ω",
        "difficulty": 3,
        "competency_code": "circular-motion-field",
    },
    {
        "level": "TRANSFER",
        "prompt": "An electron moves along +x while the field points along +y. Determine the direction of the magnetic force — then repeat for a proton.",
        "options": [
            "v × B = x̂ × ŷ = +ẑ → force along +z for the proton; the electron's force is along −z",
            "v × B = x̂ × ŷ = +ẑ → force along +z for both charges",
            "The force points along −x for the proton and +x for the electron",
            "Force along +y for the proton, −y for the electron",
        ],
        "correct_index": 0,
        "explanation": "For a positive charge, F ∝ v × B = x̂ × ŷ = +ẑ (out of the ground). The electron is negative, so its force is the opposite: along −z.",
        "skill": "3-D direction with the sign flip",
        "difficulty": 2,
        "competency_code": "magnetic-force-charge",
    },
    {
        "level": "TRANSFER",
        "prompt": "A horizontal wire carries current due east in a region where the field points due north (both horizontal). Find the direction of the force on the wire.",
        "options": [
            "F = IL × B: east × north = up — the force is vertically UPWARD",
            "F = IL × B: east × north = down — the force is vertically downward",
            "The force points west — opposite to the current",
            "The wire feels no force because it is horizontal",
        ],
        "correct_index": 0,
        "explanation": "L points east, B points north; the cross product east × north (x̂ × ŷ) is +ẑ — straight up. Same right-hand rule as the single-charge force.",
        "skill": "force direction via IL × B",
        "difficulty": 2,
        "competency_code": "force-current-wire",
    },
    {
        "level": "TRANSFER",
        "prompt": "Design task: a proton moving at 4.7 × 10⁶ m/s must circle with radius 0.50 m. What magnetic field is required?",
        "options": [
            "B = mv/(|q|r) = (1.67 × 10⁻²⁷ × 4.7 × 10⁶)/(1.6 × 10⁻¹⁹ × 0.50) ≈ 0.098 T",
            "B = |q|r/(mv) = (1.6 × 10⁻¹⁹ × 0.50)/(1.67 × 10⁻²⁷ × 4.7 × 10⁶) ≈ 1.0 × 10⁴ T",
            "B = mv·|q|·r ≈ 6.3 × 10⁻⁴⁰ T",
            "B = r·m/(v·|q|) ≈ 0.10 m·kg/(m·C) — needs no units",
        ],
        "correct_index": 0,
        "explanation": "Invert r = mv/(|q|B) for B = mv/(|q|r) = (1.67 × 10⁻²⁷)(4.7 × 10⁶)/(1.6 × 10⁻¹⁹)(0.50) ≈ 0.098 T. Fast or heavy + big circle ⇒ weaker field.",
        "skill": "design inversion of the radius formula",
        "difficulty": 3,
        "competency_code": "circular-motion-field",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "charge-properties",
        "title": "Properties of Electric Charge",
        "taxonomy_level": "understand",
        "description": "Describe the two types of charge, the attraction/repulsion rule, and the coulomb as the SI unit.",
        "sort_order": 0,
    },
    {
        "code": "electric-current",
        "title": "Electric Current",
        "taxonomy_level": "understand",
        "description": "Define current I = Q/t (ampere), count charges via Q = Ne, and distinguish conventional current from electron flow.",
        "sort_order": 21,
    },
    {
        "code": "magnetic-poles",
        "title": "Magnetic Poles and the Absent Monopole",
        "taxonomy_level": "understand",
        "description": "State the pole-interaction rules and 1/r² pole force, and explain why an isolated magnetic pole cannot exist.",
        "sort_order": 33,
    },
    {
        "code": "magnetic-fields",
        "title": "The Magnetic Field B",
        "taxonomy_level": "understand",
        "description": "Define B by the compass-north direction, describe field-line patterns, and convert between tesla and gauss.",
        "sort_order": 34,
    },
    {
        "code": "magnetic-force-charge",
        "title": "Magnetic Force on a Moving Charge",
        "taxonomy_level": "apply",
        "description": "Compute F = |q|vB sin θ and apply the right-hand rule for qv × B, including the flip for negative charges.",
        "sort_order": 35,
    },
    {
        "code": "circular-motion-field",
        "title": "Circular Motion in a Uniform B Field",
        "taxonomy_level": "apply",
        "description": "Apply r = mv/(|q|B) and ω = v/r = |q|B/m to a charged particle circling perpendicular to a uniform field.",
        "sort_order": 36,
    },
    {
        "code": "force-current-wire",
        "title": "Magnetic Force on a Current-Carrying Wire",
        "taxonomy_level": "apply",
        "description": "Derive and apply F = IL × B (magnitude BIL sin θ) for a straight wire in a uniform field.",
        "sort_order": 37,
    },
]

COMPETENCY_PREREQUISITES = [
    ("charge-properties", "magnetic-poles"),
    ("magnetic-poles", "magnetic-fields"),
    ("electric-current", "magnetic-fields"),
    ("magnetic-fields", "magnetic-force-charge"),
    ("magnetic-force-charge", "circular-motion-field"),
    ("magnetic-force-charge", "force-current-wire"),
]

LESSON_COMPETENCIES = [
    {"code": "magnetic-poles", "role": "teaches"},
    {"code": "magnetic-fields", "role": "teaches"},
    {"code": "magnetic-force-charge", "role": "teaches"},
    {"code": "circular-motion-field", "role": "teaches"},
    {"code": "force-current-wire", "role": "teaches"},
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

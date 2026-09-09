"""PHY211 — Physics, Module 1, Lecture 3: The Electric Field and the Dipole.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 3, Fall 2024 — 'The
Electric Field, Field Lines, Particle Motion, and the Electric Dipole').

Imported by ``curriculum.content`` alongside the Lecture 1 and Lecture 2
bundles; seeded by ``curriculum.seed``.
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

# Re-declared identically to content.py so the module update stays idempotent.
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
    "code": "L3",
    "title": "The Electric Field, Field Lines, and the Electric Dipole",
    "description": (
        "Lecture 3 — the idea that a charge modifies the space around it: the "
        "defining equation E = F/q₀, the point-charge field with its direction "
        "rules, field lines, particle motion in a field, and the electric "
        "dipole with its torque and energy."
    ),
    "estimated_minutes": 80,
    "difficulty": "medium",
    "objectives": [
        "Define the electric field and state E = F/q₀ with the unit N/C, explaining why the test charge acts like a thermometer, not an ingredient.",
        "Compute the field of a point charge E = K|Q|/r² and state the direction rules (away from +, toward −).",
        "Compute the force on any charge in a known field via F = qE.",
        "Find the acceleration of a particle in a field via a = E|q|/m, including the electron vs proton contrast.",
        "State the four rules that electric field lines obey, including the no-crossing rule.",
        "Apply superposition to fields: each charge contributes its own field and the total is the vector sum.",
        "Define the dipole moment p = q·2a (from − to +) and compute torque τ = pE sinθ and energy U = pE cosθ.",
        "Describe polarization: the torque rotates the dipole toward alignment with the field.",
    ],
    "prerequisites": [
        "Coulomb's law and the force between point charges (Lecture 2).",
        "Vector addition on a line (Lecture 2).",
        "Charge signs and elementary charge qₑ = 1.6 × 10⁻¹⁹ C (Lecture 1).",
    ],
    "sort_order": 3,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Coulomb's law tells us the force between two charges, but it leaves a mystery: how "
            "does one charge 'know' another is there? The field answer: a charge changes the "
            "space around it, and that change — the electric field — is what pushes the second "
            "charge. The field exists everywhere around the source, whether or not anything is "
            "there to feel it. This lecture teaches you to read that invisible change."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Defining equation of the field",
        "body": "E = F / q₀    (unit: N/C)",
        "metadata": {
            "meaning": "Force per unit positive test charge at a point of the field.",
            "when_used": "Measuring or using the field at a point; converting between field and force (F = qE).",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "The test charge reads, it does not create",
        "body": "Drop a small positive q₀, measure F, divide by q₀. A bigger probe feels a bigger force, but F/q₀ comes out the same every time. The field is the source's property, like a thermometer reading a room's temperature without creating the warmth.",
    },
    {
        "section_type": "FORMULA",
        "title": "Point-charge field",
        "body": "E = K|Q| / r²",
        "metadata": {
            "meaning": "Field strength at distance r from a single point charge Q.",
            "when_used": "Any point-charge source; the probe cancels out of the derivation (E = KQq₀/r² ÷ q₀).",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Direction rules",
        "body": "Field points AWAY from a positive charge and TOWARD a negative charge. Magnitudes go in E = K|Q|/r²; direction is decided by the sign of Q.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "Field of a negative point charge",
        "body": (
            "A −3 μC charge; point P is 30 cm away. E = (9 × 10⁹)(3 × 10⁻⁶)/(0.3)² "
            "= 3 × 10⁵ N/C. The source is negative, so at P the field arrow points straight at "
            "the charge. A +2 μC test charge at P feels F = qE = (2 × 10⁻⁶)(3 × 10⁵) = 0.6 N — "
            "and a +4 μC probe would feel 1.2 N; dividing by each probe's charge returns the "
            "same 3 × 10⁵ N/C every time."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Particles Accelerate in the Field",
        "body": (
            "A charge in a field feels F = qE and accelerates at a = F/m = E|q|/m. Because masses "
            "differ wildly, so do accelerations: an electron and a proton feel equal-magnitude "
            "forces in the same field (both |q| = e), yet the electron's acceleration is roughly "
            "1830× larger. The electron accelerates OPPOSITE to E (negative charge). This is the "
            "engine behind charge accelerators."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Particle acceleration",
        "body": "a = E|q| / m   (and F = qE)",
        "metadata": {"when_used": "Motion of a charged particle in a known uniform field; electron vs proton comparisons."},
    },
    {
        "section_type": "TEXT",
        "title": "Field Lines",
        "body": (
            "Field lines are a drawing of the field, and they follow four hard rules: (1) they "
            "begin on positive charges and terminate on negative charges; (2) they NEVER cross; "
            "(3) the tangent to a line at any point gives the direction of E there; (4) the "
            "number of lines leaving a positive charge (or entering a negative one) is "
            "proportional to the charge's magnitude. The no-crossing rule is absolute: at a "
            "crossing, one point would have two field directions — impossible for a single vector."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Field-line rules",
        "body": "Start on +, end on −; never intersect; tangent = E's direction; line density ∝ charge magnitude.",
    },
    {
        "section_type": "TEXT",
        "title": "Superposition of Fields",
        "body": (
            "Each charge contributes its own field, and the total field at a point is the vector "
            "sum of the individual fields — the same signed recipe as forces, but you don't need "
            "a charge sitting at the point to ask the question. Example trap: at the exact "
            "midpoint between two equal positive charges the fields cancel to zero (each points "
            "away from its own charge, so they oppose), even though each one is large."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Electric Dipole",
        "body": (
            "A dipole is two charges of equal magnitude and opposite sign, ±q, held a fixed "
            "distance 2a apart. Its dipole moment p has magnitude p = q·2a and points from the "
            "NEGATIVE toward the POSITIVE charge. In a uniform field the two forces +qE and −qE "
            "cancel — net force zero — but they act on opposite ends of the object, producing a "
            "torque that rotates the dipole toward alignment with the field (polarization)."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Dipole moment",
        "body": "p = q·2a   (direction: from −q to +q)",
        "metadata": {"meaning": "Charge magnitude times the full separation 2a.",
                     "when_used": "Any dipole problem — direction matters as much as magnitude."},
    },
    {
        "section_type": "FORMULA",
        "title": "Torque on a dipole",
        "body": "τ = pE sinθ   (also τ⃗ = p⃗ × E⃗)",
        "metadata": {
            "meaning": "Rotational effect of the field on the dipole at angle θ to the field; maximum at θ = 90°.",
            "when_used": "Predicting whether a dipole rotates, and how strongly.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Dipole potential energy (course formula)",
        "body": "U = pE cosθ",
        "metadata": {
            "meaning": "Energy of a dipole at angle θ to the field, in this course's convention.",
            "when_used": "Energy landmarks: U maximum at θ = 0 (aligned), U = 0 at θ = 90°.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "No net force, but it still spins",
        "body": "A dipole in a UNIFORM field has zero net force yet feels a torque pE sinθ — equal, opposite, OFFSET forces form a couple (like a steering wheel). Answer 'torque', never 'nothing'.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "Dipole numbers",
        "body": (
            "q = 1 μC on each end, 2a = 2 cm, E = 5 × 10⁵ N/C, θ = 30°. p = (1 × 10⁻⁶)(0.02) "
            "= 2 × 10⁻⁸ C·m. τ = pE sin30° = (2 × 10⁻⁸)(5 × 10⁵)(0.5) = 5 × 10⁻³ N·m. "
            "U = pE cos30° ≈ 8.66 × 10⁻³ J. Two formulas, one shape: sine for the twist, cosine "
            "for the energy."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — field at a distance",
        "body": (
            "E at 0.5 m from a +2 μC charge: E = (9 × 10⁹)(2 × 10⁻⁶)/(0.5)² = 7.2 × 10⁴ N/C, "
            "directed away from the charge. Halve the distance and the field quadruples."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — electron accelerated by a field",
        "body": (
            "Electron placed at the point of the previous example (E = 7.2 × 10⁴ N/C): "
            "a = E|e|/mₑ = (7.2 × 10⁴)(1.6 × 10⁻¹⁹)/(9.1 × 10⁻³¹) ≈ 1.27 × 10¹⁶ m/s², directed "
            "OPPOSITE to E — toward the +2 μC charge. Negative charge, reversed force."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — a dipole at 90°",
        "body": (
            "Dipole with ±3 μC separated by 4 cm in a uniform 2 × 10⁵ N/C field, axis "
            "perpendicular to the field: p = (3 × 10⁻⁶)(0.04) = 1.2 × 10⁻⁷ C·m; net force = 0 "
            "(equal and opposite forces in a uniform field); τ = pE sin90° = (1.2 × 10⁻⁷)"
            "(2 × 10⁵) = 2.4 × 10⁻² N·m — the maximum twist. Energy at 90°: U = pE cos90° = 0."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — superposition of fields outside the pair",
        "body": (
            "q₁ = +5 μC at the origin, q₂ = −3 μC at x = 0.1 m, point P at x = 0.3 m. "
            "E₁ = (9 × 10⁹)(5 × 10⁻⁶)/0.3² = 5 × 10⁵ N/C, away from +q₁ → +x. "
            "E₂ = (9 × 10⁹)(3 × 10⁻⁶)/0.2² = 6.75 × 10⁵ N/C, toward −q₂ (left of P) → −x. "
            "Net = 5 × 10⁵ − 6.75 × 10⁵ = −1.75 × 10⁵ → 1.75 × 10⁵ N/C in −x."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — zero field between unlike strengths",
        "body": (
            "+4 μC and +16 μC fixed 30 cm apart, find the point between them where the net field "
            "is zero: balance 4/x² = 16/(0.3 − x)² → 2/x = 4/(0.3 − x) → 2(0.3 − x) = 4x → "
            "x = 0.1 m from the 4 μC charge (0.2 m from the 16 μC). The equilibrium point hugs "
            "the smaller charge — the same rule as the force problem in Lecture 2, now applied "
            "to fields."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "'The field depends on what I put in it'",
        "body": "No. A bigger test charge feels a bigger FORCE, but F/q always gives the same E. The field is the source's property — the probe only reads it.",
    },
    {
        "section_type": "WARNING",
        "title": "Shoving the sign into E = K|Q|/r²",
        "body": "A 'negative field' from the formula is meaningless. Magnitudes in; direction out — toward negative, away from positive.",
    },
    {
        "section_type": "WARNING",
        "title": "Electron direction flip",
        "body": "F = qE with q negative: the electron accelerates OPPOSITE to E. If your answer has the electron moving along E, swap it.",
    },
    {
        "section_type": "WARNING",
        "title": "Dipole moment from + to −",
        "body": "p⃗ points from the NEGATIVE charge toward the POSITIVE charge. Reversing it flips the sense of the torque.",
    },
    {
        "section_type": "WARNING",
        "title": "Sin/cos swap between τ and U",
        "body": "Torque is largest at 90° → τ = pE sinθ. Energy is largest at alignment (this course's convention) → U = pE cosθ. Maximize one, the other dies.",
    },
    {
        "section_type": "WARNING",
        "title": "'No net force means nothing happens'",
        "body": "For a dipole in a uniform field the forces cancel (no translation) but the OFFSET lines of action spin it (rotation). The correct answer is torque.",
    },
    {
        "section_type": "WARNING",
        "title": "Field lines crossing 'close up'",
        "body": "Never. At a crossing one point would have two directions of E — impossible for a single vector regardless of charge proximity.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Field Concept: Invisible but Real",
        "body": (
            "The jump is from 'force between two things' to 'something filling space'. The test "
            "charge is a thermometer: it reads the field but does not create it — take it away "
            "and the field remains. Keep the two-step picture: source → creates field → field "
            "pushes anything you drop in. The E = KQ/r² result follows because the probe "
            "cancels out of Coulomb's law. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Superposition of Fields and Cancellation",
        "body": (
            "Every charge contributes a field at a point; the total is the vector sum. At the "
            "midpoint of two equal positive charges the fields are equal in magnitude and "
            "opposite in direction — the NET field is zero even though each contribution is "
            "huge. Magnitude and direction are separate; cancellation is a direction story. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Dipole Torque: Equal Forces That Still Turn",
        "body": (
            "Equal, opposite, and OFFSET forces make a couple — zero translation, pure rotation. "
            "The lever arm is the perpendicular gap 2a sinθ, shrinking as the dipole aligns, so "
            "τ = qE·2a sinθ = pE sinθ. The torque rotates p⃗ toward E⃗ (polarization). A steering "
            "wheel demonstrates the idea: both hands push equally and oppositely, and the wheel "
            "still turns. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Electron vs Proton in the Same Field",
        "body": (
            "Equal forces (both |q| = e), wildly different accelerations: a = E|q|/m, and "
            "mₑ ≈ m_p/1830. The electron accelerates ~1830× harder and moves AGAINST the field "
            "direction. Charge accelerators exploit exactly this. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Field-Line Rules",
        "body": (
            "Four absolute rules: begin on + and end on −; never intersect; tangent = direction "
            "of E; density ∝ charge magnitude. The tangent rule alone forces no-crossing — two "
            "tangents at one point would mean two field directions there. Difficulty: MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• The field is the source's modification of space; E = F/q₀ (N/C) with a positive test charge.\n"
            "• Point charge: E = K|Q|/r² — away from +, toward −; quarter strength at double distance.\n"
            "• Force on any charge: F = qE; acceleration a = E|q|/m — electron ≈ 1830× the proton's, opposite direction.\n"
            "• Field lines: start on +, end on −, never cross, tangent = direction, density ∝ magnitude.\n"
            "• Superposition: fields add as vectors — equal opposite charges cancel at the midpoint.\n"
            "• Dipole: p = q·2a from − to +; uniform field gives zero net force but torque τ = pE sinθ.\n"
            "• Polarization: the torque swings the dipole into alignment; energy (course formula) U = pE cosθ."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Electric field (E) — force per unit positive test charge; a property of the source, present whether or not a probe is there.\n"
            "• Test charge (q₀) — a small positive charge used to measure the field; it reads rather than creates.\n"
            "• Field line — a curve tangent to E everywhere, drawn from + to −.\n"
            "• Electric dipole — two equal, opposite charges separated by 2a.\n"
            "• Dipole moment (p) — q·2a, pointing from − to +.\n"
            "• Polarization — alignment of the dipole with the field under the torque."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• E = F/q₀ — defining equation (N/C).\n"
            "• E = K|Q|/r² — point-charge field.\n"
            "• F = qE — force on a charge in a field.\n"
            "• a = E|q|/m — particle acceleration.\n"
            "• p = q·2a — dipole moment.\n"
            "• τ = pE sinθ — torque on a dipole.\n"
            "• U = pE cosθ — dipole energy (course convention)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "A charge fills space with a field that exists whether or not anything is there to "
            "feel it. To read it: drop in a positive probe, measure the force, divide — "
            "E = F/q₀. For a point source E = K|Q|/r² — away from plus, toward minus, quarter "
            "strength at double distance. Fields add as vectors. Particles accelerate at "
            "a = E|q|/m — electrons whip around 1830× faster than protons, opposite to E. A "
            "dipole in a uniform field: zero net force, but torque pE sinθ swings it into "
            "alignment with the field, storing energy pE cosθ. No net force doesn't mean "
            "nothing happens — it means nothing translates. The spin is the story."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Electric Field: Reading the Invisible",
        "description": (
            "What a field is, how the test charge measures it without creating it, the "
            "point-charge field, direction rules, and field superposition."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The electric field: E = F/q₀, E = KQ/r², direction rules, superposition",
            "target_student": "First-year university student",
            "objective": "Explain that the field belongs to the source (thermometer, not ingredient), compute E from F and Q, and state the direction rules.",
            "hook": "How does this charge know that charge is over there? Nothing touches, nothing connects — yet push happens. The answer: the space isn't empty, it's changed.",
            "explanation_steps": [
                "The field exists at every point around a source, with or without a probe.",
                "Measure it: place q₀, feel F, compute E = F/q₀ (N/C).",
                "Thermometer analogy: removing the probe never removes the field.",
                "Derive E = KQ/r²: the probe cancels out of Coulomb's law.",
                "Direction rules: away from +, toward −; 1/r² scaling.",
                "The lecture's example: −3 μC at 30 cm → E = 3 × 10⁵ N/C toward the charge.",
                "Superposition: fields add as vectors.",
            ],
            "common_mistake": "Believing the field depends on the test charge; shoving the sign into E = KQ/r².",
            "check": "A +4 μC test charge at P feels 0.2 N. What is E at P, and what force would a +8 μC charge feel there?",
            "final_takeaway": "E = F/q₀ reads the source's property; E = K|Q|/r² computes it; away from plus, toward minus, quarter at double the distance.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "Zero Net Force, But It Still Spins: The Dipole",
        "description": (
            "Dipole moment, why a uniform field exerts no net force yet a torque, the "
            "torque/energy formulas, and the alignment motion called polarization."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Dipole moment p = q·2a, torque τ = pE sinθ, polarization, U = pE cosθ",
            "target_student": "First-year university student",
            "objective": "Explain why a dipole in a uniform field feels zero net force but a torque, compute p, τ, and U, and describe the alignment motion.",
            "hook": "A rule you've trusted since school: no net force, no motion. Two equal opposite charges in a uniform field break it — the forces cancel, and yet it spins.",
            "explanation_steps": [
                "Build the dipole: ±q, separation 2a, moment p = q·2a from − to +.",
                "Forces in a uniform field: +qE and −qE → sum zero.",
                "Steering-wheel insight: equal, opposite, OFFSET forces = a couple = pure rotation.",
                "Geometry: lever arm 2a sinθ → τ = pE sinθ.",
                "Polarization: torque drives θ → 0; aligned dipole is calm (τ = 0).",
                "Energy (course convention): U = pE cosθ; landmarks at 0° and 90°.",
            ],
            "common_mistake": "Reporting a net force for the dipole; pointing p⃗ from + to −; sin/cos swap between τ and U.",
            "check": "The same dipole sits at θ = 90°. Net force? Torque in terms of p and E? Energy?",
            "final_takeaway": "Equal-and-opposite-but-offset forces give zero net force and torque pE sinθ — the dipole rotates until it aligns with the field.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "Define the electric field in words and write its defining equation with the correct unit.",
        "options": [
            "The field exists in the region around a charged object and exerts a force on any charge placed in it; E = F/q₀ with q₀ a positive test charge; unit N/C",
            "The field is the force between two charges; E = F/r²; unit N·m",
            "The field only exists where a test charge is placed; E = qF; unit C/N",
            "The field describes charge itself; E = Q²/r; unit C/m",
        ],
        "correct_index": 0,
        "explanation": "A charge modifies the space around it; the field exerts a force on any charge placed in it. E = F/q₀ with a positive test charge, measured in N/C.",
        "skill": "field definition",
        "difficulty": 1,
        "competency_code": "electric-field",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State the direction of the electric field (a) surrounding an isolated positive charge; (b) surrounding an isolated negative charge.",
        "options": [
            "(a) radially away from the charge; (b) radially toward the charge",
            "(a) radially toward the charge; (b) radially away from the charge",
            "Both point along a single line toward each other",
            "Both directions circulate around the charge",
        ],
        "correct_index": 0,
        "explanation": "Field lines begin on positive charges and terminate on negative ones: away from +, toward −.",
        "skill": "direction rules",
        "difficulty": 1,
        "competency_code": "electric-field",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why does an electron and a proton in the same electric field have aₑ ≫ a_p even though the forces on them have equal magnitude?",
        "options": [
            "a = E|q|/m; both have |q| = e but mₑ ≪ m_p (~factor 1830), so the electron's acceleration is ~1830× larger",
            "The electron feels a larger force because it is smaller",
            "The proton's charge is larger, so it accelerates faster",
            "The electron moves along the field while the proton moves against it",
        ],
        "correct_index": 0,
        "explanation": "Both feel equal force (same |q| = e), but acceleration divides by mass; the electron is ~1830× lighter, so it accelerates ~1830× harder. The source links this to charge accelerators.",
        "skill": "a ∝ 1/m",
        "difficulty": 2,
        "competency_code": "particle-motion",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "In which direction is the dipole moment p⃗ of an electric dipole drawn, and what is its magnitude?",
        "options": [
            "From −q toward +q along the axis; p = q·2a with 2a the charge separation",
            "From +q toward −q along the axis; p = q·2a",
            "Perpendicular to the axis; p = q·a",
            "From −q toward +q; p = 2q/a",
        ],
        "correct_index": 0,
        "explanation": "The moment points from the negative to the positive charge along the axis, with magnitude p = q·2a where 2a is the full separation.",
        "skill": "dipole definition",
        "difficulty": 1,
        "competency_code": "electric-dipole",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "Calculate the magnitude and direction of the electric field at a point 0.5 m from a +2 μC charge.",
        "options": [
            "7.2 × 10⁴ N/C, directed away from the charge",
            "3.6 × 10⁴ N/C, directed toward the charge",
            "7.2 × 10⁴ N/C, directed toward the charge",
            "1.44 × 10⁵ N/C, directed away from the charge",
        ],
        "correct_index": 0,
        "explanation": "E = (9 × 10⁹)(2 × 10⁻⁶)/(0.5)² = 7.2 × 10⁴ N/C. Positive source ⇒ field points away from it.",
        "skill": "point-charge field",
        "difficulty": 2,
        "competency_code": "electric-field",
    },
    {
        "level": "APPLY",
        "prompt": "An electron is placed in a uniform field E pointing in +x. Which way does it accelerate, and how does its acceleration compare to a proton's in the same field?",
        "options": [
            "Electron −x with |a| about 1830× the proton's (proton +x)",
            "Electron +x with |a| about 1830× the proton's",
            "Both accelerate +x with equal acceleration",
            "Electron −x with |a| about 1/1830 the proton's",
        ],
        "correct_index": 0,
        "explanation": "F = qE with q negative points opposite E; a = |q|E/m and mₑ ≈ m_p/1830, so the electron accelerates ~1830× harder, opposite to the field.",
        "skill": "sign flip + mass scaling",
        "difficulty": 2,
        "competency_code": "particle-motion",
    },
    {
        "level": "APPLY",
        "prompt": "A dipole has charges ±3 μC separated by 4 cm in a uniform field of 2 × 10⁵ N/C with its axis perpendicular to the field. Find p, the net force, and the torque.",
        "options": [
            "p = 1.2 × 10⁻⁷ C·m; net force = 0; τ = 2.4 × 10⁻² N·m",
            "p = 6 × 10⁻⁸ C·m; net force = 0.6 N; τ = 1.2 × 10⁻² N·m",
            "p = 1.2 × 10⁻⁷ C·m; net force = 0.6 N; τ = 0",
            "p = 3 × 10⁻⁷ C·m; net force = 0; τ = 6 × 10⁻² N·m",
        ],
        "correct_index": 0,
        "explanation": "p = (3 × 10⁻⁶)(0.04) = 1.2 × 10⁻⁷ C·m. In a uniform field the forces cancel (net force 0). θ = 90° ⇒ τ = pE sin90° = (1.2 × 10⁻⁷)(2 × 10⁵) = 2.4 × 10⁻² N·m, the maximum.",
        "skill": "dipole quantities",
        "difficulty": 2,
        "competency_code": "electric-dipole",
    },
    {
        "level": "APPLY",
        "prompt": "Two charges lie on the x-axis: q₁ = +5 μC at the origin and q₂ = −3 μC at x = 0.1 m. Find the net electric field at point P, x = 0.3 m.",
        "options": [
            "1.75 × 10⁵ N/C in −x (5 × 10⁵ away from +q₁ minus 6.75 × 10⁵ toward −q₂)",
            "1.75 × 10⁵ N/C in +x",
            "1.175 × 10⁶ N/C in +x (magnitudes summed)",
            "6.75 × 10⁵ N/C in −x (q₁ ignored)",
        ],
        "correct_index": 0,
        "explanation": "E₁ = (9 × 10⁹)(5 × 10⁻⁶)/0.3² = 5 × 10⁵ N/C away from +q₁ (+x). E₂ = (9 × 10⁹)(3 × 10⁻⁶)/0.2² = 6.75 × 10⁵ N/C toward −q₂ (−x). Net = −1.75 × 10⁵ → 1.75 × 10⁵ N/C in −x.",
        "skill": "field superposition",
        "difficulty": 3,
        "competency_code": "electric-field",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Two positive charges, +4 μC and +16 μC, are fixed 30 cm apart. Using the direction rules for fields, find the point between them where the net field is zero.",
        "options": [
            "0.1 m from the 4 μC charge (0.2 m from the 16 μC)",
            "0.2 m from the 4 μC charge",
            "0.15 m from the 4 μC charge",
            "0.24 m from the 4 μC charge",
        ],
        "correct_index": 0,
        "explanation": "Between like charges the fields oppose: 4/x² = 16/(0.3−x)² → 2/x = 4/(0.3−x) → 2(0.3−x) = 4x → x = 0.1 m from the 4 μC charge. The zero point hugs the smaller charge.",
        "skill": "transferring the equilibrium procedure from forces to fields",
        "difficulty": 3,
        "competency_code": "electric-field",
    },
    {
        "level": "TRANSFER",
        "prompt": "A dipole is released from rest at θ = 90° in a uniform field. Describe its motion, and give its torque and energy at release and when it stops rotating.",
        "options": [
            "At release τ = pE (max), U = pE cos90° = 0; torque rotates p⃗ toward E⃗, θ and τ shrink, stopping at θ = 0 with τ = 0 and U = pE",
            "At release τ = 0, U = pE; it accelerates translationally along the field",
            "It stays at 90° forever because the forces cancel",
            "It rotates but the torque stays constant at pE throughout",
        ],
        "correct_index": 0,
        "explanation": "Released broadside: maximum torque pE and zero energy. The torque rotates the dipole toward alignment (polarization); as θ drops, sinθ drops, so the torque shrinks. At θ = 0 it stops: τ = 0, U = pE.",
        "skill": "qualitative dipole dynamics",
        "difficulty": 3,
        "competency_code": "electric-dipole",
    },
    {
        "level": "TRANSFER",
        "prompt": "A student claims: 'At the exact midpoint between two equal positive charges, the field is huge because both charges contribute.' Evaluate the claim.",
        "options": [
            "False — each charge produces equal-magnitude fields in OPPOSITE directions (each away from its own charge), so E_net = 0; a positive test charge would be in unstable equilibrium",
            "True — the two fields add to twice the single-charge value",
            "False — the fields cancel only for equal NEGATIVE charges",
            "True — superposition always doubles the field between charges",
        ],
        "correct_index": 0,
        "explanation": "At the midpoint each charge's field points away from its own charge, so the two equal-magnitude vectors oppose and cancel: E_net = 0. Large contributions, zero vector sum — direction decides.",
        "skill": "direction-based cancellation reasoning",
        "difficulty": 2,
        "competency_code": "electric-field",
    },
    {
        "level": "TRANSFER",
        "prompt": "An electron is released from rest in a region where E = 4 × 10⁴ N/C in +x. Find the direction and magnitude of its acceleration, and name the application the source connects to this large aₑ.",
        "options": [
            "a ≈ 7 × 10¹⁵ m/s² in −x (opposite E); charge accelerators exploit the electron's huge charge-to-mass response",
            "a ≈ 7 × 10¹⁵ m/s² in +x; essentially zero useful application",
            "a ≈ 3.8 × 10¹² m/s² in −x; household lighting",
            "a ≈ 7 × 10¹⁷ m/s² in −x; capacitors only",
        ],
        "correct_index": 0,
        "explanation": "a = E|e|/mₑ = (4 × 10⁴)(1.6 × 10⁻¹⁹)/(9.1 × 10⁻³¹) ≈ 7 × 10¹⁵ m/s², opposite to E (negative charge). The electron's light mass makes it the workhorse of charge accelerators.",
        "skill": "sign flip + mass scaling + application",
        "difficulty": 3,
        "competency_code": "particle-motion",
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
        "code": "charge-units",
        "title": "Charge Units and Electron Counting",
        "taxonomy_level": "recall",
        "description": "Convert between coulombs and mC/μC/nC/pC and count the elementary charges in a given charge.",
        "sort_order": 2,
    },
    {
        "code": "coulomb-force",
        "title": "Coulomb's Law for Point Charges",
        "taxonomy_level": "apply",
        "description": "Compute the electric force magnitude between two point charges and assign its direction from the charge signs.",
        "sort_order": 5,
    },
    {
        "code": "electric-field",
        "title": "The Electric Field",
        "taxonomy_level": "understand",
        "description": "Define E = F/q₀, compute the point-charge field E = K|Q|/r², and apply the direction and superposition rules.",
        "sort_order": 8,
    },
    {
        "code": "field-lines",
        "title": "Electric Field Lines",
        "taxonomy_level": "understand",
        "description": "State and apply the four rules for drawing electric field lines, including the no-crossing rule.",
        "sort_order": 9,
    },
    {
        "code": "particle-motion",
        "title": "Charged Particle Motion in a Field",
        "taxonomy_level": "apply",
        "description": "Find the acceleration of a charged particle a = E|q|/m, including direction and the electron vs proton contrast.",
        "sort_order": 10,
    },
    {
        "code": "electric-dipole",
        "title": "The Electric Dipole",
        "taxonomy_level": "apply",
        "description": "Compute dipole moment p = q·2a, torque τ = pE sinθ, and energy U = pE cosθ; describe polarization.",
        "sort_order": 11,
    },
]

COMPETENCY_PREREQUISITES = [
    ("coulomb-force", "electric-field"),
    ("electric-field", "field-lines"),
    ("electric-field", "particle-motion"),
    ("electric-field", "electric-dipole"),
]

LESSON_COMPETENCIES = [
    {"code": "electric-field", "role": "teaches"},
    {"code": "field-lines", "role": "teaches"},
    {"code": "particle-motion", "role": "teaches"},
    {"code": "electric-dipole", "role": "teaches"},
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

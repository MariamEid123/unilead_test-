"""PHY211 — Physics, Module 12, Lesson 14: Final Review Problem Clinic (Ch. 6–10).

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: 'Part 2' additional practice set for the PHY211 final —
74 multiple-choice problems spanning DC resistor networks → RC transients →
magnetism (poles, forces, wire & solenoid fields, superposition) → reflection
& refraction → mirrors → thin lenses and aberrations).

A consolidation lesson rather than new instruction: students PRACTICE across
the final-review syllabus, REMEDIATE weak topics, RETRY, then transfer to the
final-exam clinic. Imported by ``curriculum.content`` and seeded by
``curriculum.seed``.
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
    "code": "M12",
    "title": "Module 12 — Final Review Problem Clinic (Ch. 6–10)",
    "description": (
        "Consolidation of Chapters 6–10: DC resistor networks and RC "
        "transients, magnetic poles and the Earth's field, forces on moving "
        "charges and current wires, wire and solenoid fields with "
        "superposition, reflection and refraction, mirror and lens equations "
        "with the unified sign convention, and chromatic/spherical aberration."
    ),
    "sort_order": 12,
}

LESSON = {
    "code": "L14",
    "title": "Final Review: Circuit Networks, Magnetism, Mirrors & Lenses",
    "description": (
        "A practice-first consolidation of the final syllabus: reduce resistor "
        "networks and follow RC transients with the time constant; master "
        "magnetic forces by the right-hand rule and field superposition; and "
        "drive every imaging question through the mirror/lens equation with "
        "one sign convention."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Reduce series-parallel resistor networks, distributing current and voltage correctly.",
        "Analyze RC charging and discharging with τ = RC and the 63%/37% markers.",
        "Identify magnetic poles (including the Earth's field) and describe field-line patterns.",
        "Compute magnetic forces on moving charges and current-carrying wires with the right-hand rule.",
        "Compute wire and solenoid fields (B = μ₀I/2πr, B = μ₀nI) and superpose parallel-wire fields.",
        "Apply reflection and Snell's law with n = c/v and the normal-angle rule.",
        "Solve the mirror equation 1/p + 1/q = 1/f with the unified sign convention.",
        "Solve the thin-lens equation, characterize the converging-lens cases, and identify aberrations.",
    ],
    "prerequisites": [
        "Electric current, Ohm's law, resistance, and resistivity (Lectures 6–7).",
        "Series and parallel resistor networks and RC circuits (Lectures 8–10).",
        "Magnetic poles, fields, forces, and wire/solenoid fields (Lectures 11–13).",
        "Reflection, refraction, mirrors, thin lenses, and aberrations (Lectures 14–15).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "The final exam rewards three skills: algebra of resistor "
            "networks (with the RC race on top), a reliable right-hand "
            "physics for magnetic forces AND fields, and one sign convention "
            "that makes every mirror and lens the same equation. This clinic "
            "drills each until it is fast."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "DC Resistor Networks",
        "body": (
            "Reduce OUTSIDE-IN: single-series chains add (Req = ΣRᵢ), "
            "single-parallel groups take reciprocals (1/Req = Σ1/Rᵢ, always "
            "BELOW the smallest). Then unwind with the two invariants: series "
            "components share the SAME current, parallel branches share the "
            "SAME voltage. Check with one battery equation: ISupplied = "
            "ℰ/Rtotal feeds the whole collapse."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Parallel current split",
        "body": (
            "Splitting current across parallel resistors: I divides INVERSE "
            "proportionally to resistance (the 12 Ω branch takes half the "
            "current of the 6 Ω branch). Always verify ΣI_branch = I_total."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "RC Transients",
        "body": (
            "One clock, two faces: τ = RC. Charging builds toward ℰ this way: "
            "q = q₀(1 − e^(−t/τ)) — at t = τ the capacitor is at 63% of full "
            "charge, at 3τ near 95%. Discharging decays by q = q₀e^(−t/τ) — "
            "37% of the charge remains at one time constant. A FULLY charged "
            "capacitor in steady state acts like an OPEN CIRCUIT (no current "
            "through its branch); an empty one acts like a short (or a wire) "
            "the instant the switch closes."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Capacitor personality",
        "body": (
            "Completely discharged → ideal short circuit (all current at "
            "switch-closing). Completely charged → open circuit (branch dead "
            "in steady state). Everything between is the exponential race to "
            "63% / 37%."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Magnetic Poles and the Earth's Field",
        "body": (
            "Every magnet has two poles; an isolated monopole does not exist. "
            "Like poles repel, unlike attract. Field lines exit the NORTH "
            "pole and enter the SOUTH. The Earth behaves like a bar magnet: "
            "the geographic NORTH pole region is a magnetic SOUTH pole — "
            "which is why a compass 'north' needle is attracted there."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Magnetic forces: moving charge and wire",
        "body": "F = |q|vB sin θ     and     F = ILB sin θ",
        "metadata": {
            "meaning": "One force law with the same angle story: only the velocity component PERPENDICULAR to B experiences a force, and the right-hand rule sets the direction from v and B (flip for a negative charge).",
            "when_used": "F = 0 whenever v ∥ B (θ = 0 or 180°); maximum when v ⊥ B (θ = 90°). The wire version has the same rule with the current direction.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Fields from wires and solenoids",
        "body": "B = μ₀I/(2πr)     and     B = μ₀nI    (n = N/L)",
        "metadata": {
            "meaning": "The long-straight-wire field falls as 1/r in a ring around the wire; the solenoid interior is uniform across its cross-section and set by n = N/L.",
            "when_used": "Superpose parallel-wire fields as vectors at the point of interest: equal same-direction currents cancel MIDWAY between the wires and ADD outside the pair; opposite-direction currents add between them.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Reflection and Refraction",
        "body": (
            "Angles are measured from the NORMAL, never the surface. "
            "Reflection: θᵢ = θᵣ. Refraction: n₁sinθ₁ = n₂sinθ₂ with n = c/v. "
            "Frequency is INVARIANT across the boundary; into a denser medium "
            "the speed and the wavelength both shrink (v = λf, so λ = λ₀/n). "
            "Moving from dense to rare, past the critical angle θc = "
            "sin⁻¹(n₂/n₁), light totally internally reflects."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Mirrors and Lenses: One Equation",
        "body": (
            "1/p + 1/q = 1/f works for BOTH mirrors and lenses (mirrors: "
            "f = R/2; power F = 1/f). The unified sign convention: REAL "
            "object p > 0 on the incoming side; REAL image q > 0 on the "
            "reflecting/refracting side; VIRTUAL images q < 0. Concave ("
            "converging) mirrors and convex (converging) lenses have f > 0; "
            "convex mirrors and concave lenses have f < 0. Diverging elements "
            "give upright, reduced, virtual images for real objects. "
            "Magnification M = −q/p — negative M means inverted."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Aberrations",
        "body": (
            "Chromatic aberration: n depends on wavelength, so a single lens "
            "bends violet more than red (f_violet ≠ f_red); a cemented "
            "achromatic doublet cancels it. Spherical aberration: rays far "
            "from the axis (marginal rays) focus before paraxial rays; "
            "stopping down the aperture or aspheric shaping fixes it."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — a mixed resistor network",
        "body": (
            "ℰ = 24 V battery driving a 1.0 Ω resistor in series with a "
            "6.0 Ω ∥ 3.0 Ω block. Parallel block: 1/R = 1/6 + 1/3 = 1/2 → "
            "R = 2.0 Ω. Total: R = 1 + 2 = 3.0 Ω, so I = 24/3 = 8.0 A. "
            "Across the block V = 8 × 2 = 16 V; the 6 Ω branch takes "
            "16/6 = 2.67 A and the 3 Ω takes 16/3 = 5.33 A, summing to 8.0 A."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — how long to reach 95%?",
        "body": (
            "A 100-V source charges 10 µF through 2.0 MΩ: τ = RC = "
            "(2 × 10⁶)(10 × 10⁻⁶) = 20 s. The capacitor crosses 63% at one "
            "time constant and 95% (1 − e⁻³) at t ≈ 3τ = 60 s."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — force on a proton",
        "body": (
            "A proton (q = +e) shoots at v = 2.0 × 10⁶ m/s into B = 0.50 T at "
            "30° to the field: F = qvB sinθ = (1.6 × 10⁻¹⁹)(2 × 10⁶)(0.50)(0.5) "
            "= 8.0 × 10⁻¹⁴ N. The right-hand rule puts v × B up; the positive "
            "charge follows it."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — canceling wire fields",
        "body": (
            "Two long wires carry the same 10 A in the SAME direction, 10 cm "
            "apart. Midway each wire contributes B = μ₀I/(2πr) = "
            "(4π × 10⁻⁷)(10)/(2π × 0.05) = 4.0 × 10⁻⁵ T in OPPOSITE "
            "directions, so the net field is ZERO at the midpoint; outside the "
            "pair the fields add to 8.0 × 10⁻⁵ T."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — Snell at the glass-air lid",
        "body": (
            "Light leaves glass (nₐ = 1.52) at 30° from the normal toward air: "
            "1.52 sin30° = 1.00 sinθ₂ → sinθ₂ = 0.76 → θ₂ ≈ 49°. The ray bends "
            "AWAY from the normal as it speeds up."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 6 — converging lens two ways",
        "body": (
            "Object 15 cm in front of a concave (converging) mirror with "
            "f = 10 cm: 1/q = 1/10 − 1/15 = 1/30 → q = +30 cm. Real image, "
            "M = −q/p = −2 (inverted, doubled). If the object moves inside the "
            "focus (p < f), 1/q turns negative — the image flips virtual and "
            "upright."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Angles are from the NORMAL",
        "body": "θᵢ and θᵣ are measured off the normal to the surface, not off the surface plane. 90° − surface angle почти every time.",
    },
    {
        "section_type": "WARNING",
        "title": "Parallel current split is inverse",
        "body": "The LOWEST resistor in a parallel group takes the HIGHEST current. I ∝ 1/R, and verify ΣI_branch = I_total.",
    },
    {
        "section_type": "WARNING",
        "title": "Fully charged capacitor = open circuit",
        "body": "In steady DC, a charged capacitor blocks its branch entirely; a discharged one is a short at switch-closing. Do not treat it like a resistor.",
    },
    {
        "section_type": "WARNING",
        "title": "The Earth's poles are label-flipped",
        "body": "The geographic NORTH pole is a magnetic SOUTH pole — it attracts compass 'north' needles. Field lines there point into the ground.",
    },
    {
        "section_type": "WARNING",
        "title": "F = qvB with θ between v and B",
        "body": "The angle goes between the VELOCITY and the FIELD vectors. Max force at 90°, zero for motion along the field.",
    },
    {
        "section_type": "WARNING",
        "title": "Sign conventions are mirror-symmetric",
        "body": "q > 0 on the incoming side; real images add on the reflecting/refracting side. Never mix the object/image side rules between mirrors and lenses.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Imaging sign conventions",
        "body": (
            "A single sign error flips real to virtual. Anchor on the "
            "INCOMING side: object distance p is always positive there; a "
            "negative q means the image is on the same side as the incoming "
            "light (virtual). Analogy: a bank teller counts cash coming IN "
            "and out of one window — direction determines the sign. Steps: "
            "set the object side → assign f by the element (converging/diverging) → "
            "solve → carry the q sign into M = −q/p. Difficulty: VERY HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The right-hand rule and the negative charge",
        "body": (
            "F = qv × B: fingers v → curl into B → thumb is the force for a "
            "POSITIVE charge; reverse it for electrons. Students forget the "
            "flip. Analogy: the thumb of a left-handed friend — the same curl "
            "gives the opposite answer. If the paper only gives magnitudes, "
            "ask the sign question separately. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Superposing fields of parallel wires",
        "body": (
            "Fields are VECTORS with circulation directions, so the same "
            "geometry adds or cancels depending on current directions. "
            "Equal same-direction currents cancel MIDWAY and add outside; "
            "opposite directions add midway and cancel outside. Draw the B "
            "rings first, then superpose at the single point of interest. "
            "Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The RC time constant as one clock",
        "body": (
            "τ = RC is a single period for both growth and decay — students "
            "memorize growth but not that decay REUSES the same τ. Anchor on "
            "the 63%/37% pair: fully discharge to 37% in one τ. Analogy: a "
            "bath filling and draining through the same plug — the same "
            "hourglass governs both directions. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Converging vs diverging elements",
        "body": (
            "Thick-center-is-forward for lenses and center-of-curvature for "
            "mirrors. A diverging LENS (concave, f < 0) can never throw a "
            "real image of a real object — always upright, reduced, virtual. "
            "Analogy: the exit sign in a hall of mirrors — diverging devices "
            "always shrink and pull the picture 'behind'. Difficulty: MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Series networks share current; parallel branches share voltage; parallel equivalent is below the smallest.\n"
            "• One clock, two faces: τ = RC — 63% on charge, 37% left on discharge; fully charged capacitor = open circuit.\n"
            "• Like poles repel, unlike attract; Earth's geographic north is a magnetic SOUTH pole.\n"
            "• Magnetic force F = qvB sinθ = ILB sinθ, maximum perpendicular, zero parallel; right-hand rule, flip for negative charge.\n"
            "• Wire B = μ₀I/2πr, solenoid B = μ₀nI; superpose parallel-wire fields vectorially.\n"
            "• Angles from the normal; Snell n₁sinθ₁ = n₂sinθ₂; frequency invariant, λ = λ₀/n in matter.\n"
            "• Every mirror and lens obeys 1/p + 1/q = 1/f with one sign convention; M = −q/p."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Time constant τ = RC.\n"
            "• Magnetic pole — the two ends of any magnet; no monopoles.\n"
            "• Right-hand rule — v (fingers) → B (curl) → force thumb, flipped for negative charge.\n"
            "• Critical angle — the dense-to-rare incidence that gives an emergent 90°.\n"
            "• Real vs virtual image — where the outgoing rays actually cross.\n"
            "• Chromatic aberration — wavelength-dependent refraction.\n"
            "• Spherical aberration — marginal rays focusing before paraxial rays."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• Req = ΣRᵢ (series); 1/Req = Σ1/Rᵢ (parallel).\n"
            "• q = q₀(1 − e^(−t/τ)); q = q₀e^(−t/τ); τ = RC.\n"
            "• F = qvB sinθ; F = ILB sinθ.\n"
            "• B = μ₀I/(2πr); B = μ₀nI.\n"
            "• n = c/v; n₁sinθ₁ = n₂sinθ₂; θc = sin⁻¹(n₂/n₁).\n"
            "• 1/p + 1/q = 1/f (mirrors: f = R/2); M = −q/p."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Resistors: series same I, parallel same V, reduce outside-in. "
            "RC: one τ does both directions; charged = open, empty = short. "
            "Magnetism: poles come in pairs, Earth's north is magnetic south; "
            "F = qvB = ILB with the hand rule; wire and solenoid fields from "
            "μ₀I/2πr and μ₀nI, superpose vectors. Optics: angles from the "
            "normal, Snell + n = c/v, and ONE equation 1/p + 1/q = 1/f for "
            "mirrors and lenses alike."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Capacitor's Two Personalities: Short Circuit, Open Circuit, and the Race In Between",
        "description": (
            "RC circuits without the memorization: why the same capacitor acts "
            "as a short at switch-closing, an open in steady state, and "
            "follows one exponential between them — 63% up, 37% down on the "
            "same τ = RC clock."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Capacitor limiting behavior and the RC time constant",
            "target_student": "First-year university student",
            "objective": "Predict the instant-after-closing and steady-state currents in RC branches and compute τ-driven voltages.",
            "hook": "The same device is a wire at t = 0⁺ and a switch-turned-off at t = ∞ — and only one clock governs the transition.",
            "explanation_steps": [
                "Discharged capacitor: empty gate, all current passes → effective short circuit.",
                "Fully charged capacitor: no current through the branch → effective open circuit.",
                "Between the limits: q = q₀(1 − e^(−t/τ)) up, q = q₀e^(−t/τ) down.",
                "τ = RC is shared — the 63%/37% pair is one picture.",
            ],
            "common_mistake": "Treating the charged capacitor as a resistor or battery while the circuit settles.",
            "check": "A charged 10 µF capacitor sits across a 2.0 MΩ resistor. After opening the source, when is the voltage down to 37%?",
            "final_takeaway": "Two steady-state personalities plus one exponential race; τ = RC times both directions.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "One Equation, Every Mirror and Lens: The Sign Convention That Ends the Confusion",
        "description": (
            "1/p + 1/q = 1/f for every imaging element, parallel and "
            "perpendicular cases, with the side rules and magnification "
            "M = −q/p — the one sign convention that finally ends mirror-vs-lens "
            "confusion."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Unified mirror/lens equation with single sign convention",
            "target_student": "First-year university student",
            "objective": "Solve any single-element imaging problem and characterize real/virtual, upright/inverted outcomes.",
            "hook": "Concave mirror or converging lens — write one equation, get the answer for both.",
            "explanation_steps": [
                "Object side: p > 0 always, image side for q flips per element.",
                "f carries the sign: converging (+), diverging (−); mirrors f = R/2.",
                "Solve 1/p + 1/q = 1/f, then M = −q/p decides size and orientation.",
                "q < 0 → virtual: behind a mirror, same side as the object for a lens.",
            ],
            "common_mistake": "Reversing which side counts as 'real' between mirrors and lenses.",
            "check": "Object 15 cm in front of a concave mirror with f = 10 cm: describe the image.",
            "final_takeaway": "One equation + one convention: real adds up on the inside, virtual gives q < 0.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "A capacitor that has been fully charged in a DC circuit acts like which circuit element in steady state?",
        "options": [
            "An OPEN CIRCUIT — no current flows through its branch",
            "A short circuit — all current races through it",
            "A low-value resistor — some current leaks slowly",
            "A small battery — it keeps driving current forever",
        ],
        "correct_index": 0,
        "explanation": "Once fully charged the plates stop the flow: steady-state current through a charged capacitor is zero, so its branch behaves like an open circuit.",
        "skill": "capacitor steady-state personality",
        "difficulty": 1,
        "competency_code": "review-dc-circuits",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Which magnetic pole corresponds to Earth's geographic NORTH pole region?",
        "options": [
            "A magnetic SOUTH pole — it attracts the compass 'north' needle",
            "A magnetic NORTH pole — compass needles point to like poles",
            "Neutral — the geographic pole has no magnetic character",
            "Both poles simultaneously",
        ],
        "correct_index": 0,
        "explanation": "Opposite poles attract, so a compass north needle is drawn to a region that acts as a magnetic SOUTH pole — Earth's geographic north is the magnetic south.",
        "skill": "Earth's magnetic polarity",
        "difficulty": 1,
        "competency_code": "review-magnetic-fields",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "When light passes from air into glass, which statement is correct?",
        "options": [
            "Frequency is unchanged; both speed and wavelength DECREASE",
            "Speed increases; frequency remains unchanged",
            "Wavelength increases; frequency decreases",
            "Speed and frequency both increase",
        ],
        "correct_index": 0,
        "explanation": "n = c/v: a higher index means slower light. Frequency is set at the source and never changes at a boundary (v = λf), so λ = λ₀/n must shrink as well.",
        "skill": "c/v/λ across a boundary",
        "difficulty": 1,
        "competency_code": "review-optics-basics",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "For a REAL object (any position), which image is always produced by a diverging LENS?",
        "options": [
            "Virtual, upright, and reduced",
            "Real, inverted, and magnified",
            "Real, upright, and reduced",
            "Virtual, inverted, and magnified",
        ],
        "correct_index": 0,
        "explanation": "A diverging (concave) lens can never converge outgoing rays, so the image is virtual (q < 0), upright (M > 0), and smaller — for every real-object position.",
        "skill": "diverging lens, fixed character",
        "difficulty": 1,
        "competency_code": "review-lenses",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A 4.0 Ω and a 6.0 Ω resistor sit in parallel across a 12-V battery. Find the equivalent resistance and the battery current.",
        "options": [
            "Req = 2.4 Ω and I = 5.0 A",
            "Req = 10 Ω and I = 1.2 A",
            "Req = 2.4 Ω and I = 2.9 A",
            "Req = 5.0 Ω and I = 2.4 A",
        ],
        "correct_index": 0,
        "explanation": "1/Req = 1/4 + 1/6 = 5/12 → Req = 12/5 = 2.4 Ω (below the smallest). The battery current follows: I = 12/2.4 = 5.0 A.",
        "skill": "parallel network reduction",
        "difficulty": 2,
        "competency_code": "review-dc-circuits",
    },
    {
        "level": "APPLY",
        "prompt": "A proton moves at 2.0 × 10⁶ m/s at 30° to a 0.50-T magnetic field. Find the magnetic force magnitude.",
        "options": [
            "F ≈ 8.0 × 10⁻¹⁴ N",
            "F ≈ 1.6 × 10⁻¹³ N",
            "F ≈ 8.0 × 10⁻⁷ N",
            "F ≈ 1.6 × 10⁻⁷ N",
        ],
        "correct_index": 0,
        "explanation": "F = qvB sinθ = (1.6 × 10⁻¹⁹)(2.0 × 10⁶)(0.50)(sin 30° = 0.5) = 8.0 × 10⁻¹⁴ N.",
        "skill": "force on a moving charge",
        "difficulty": 2,
        "competency_code": "review-magnetic-force",
    },
    {
        "level": "APPLY",
        "prompt": "A 2.0-m wire carries 3.0 A perpendicular to a 0.40-T field. Find the force on the wire.",
        "options": [
            "F = 2.4 N",
            "F = 4.8 N",
            "F = 1.2 N",
            "F = 0.60 N",
        ],
        "correct_index": 0,
        "explanation": "Perpendicular gives sin θ = 1: F = ILB = (3.0)(2.0)(0.40) = 2.4 N.",
        "skill": "force on a current wire",
        "difficulty": 2,
        "competency_code": "review-magnetic-force",
    },
    {
        "level": "APPLY",
        "prompt": "An object sits 20 cm in front of a concave mirror with focal length 12 cm. Locate the image.",
        "options": [
            "q = 30 cm, REAL image, inverted",
            "q = 7.5 cm, virtual image, upright",
            "q = 8.0 cm, real image, upright",
            "q = 30 cm, virtual image, upright",
        ],
        "correct_index": 0,
        "explanation": "1/q = 1/f − 1/p = 1/12 − 1/20 = 2/60 → q = +30 cm. A positive q is real, M = −q/p = −1.5 inverted.",
        "skill": "mirror equation",
        "difficulty": 2,
        "competency_code": "review-mirrors",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "A 10 µF capacitor is charged to 100 V, then discharged through a 2.0 MΩ resistor. Approximately what is the voltage one time constant after discharge begins?",
        "options": [
            "≈ 37 V — one τ leaves e⁻¹ ≈ 0.37 of the charge",
            "≈ 63 V — one τ gains 63% back",
            "≈ 13 V — two factors of e⁻¹",
            "≈ 50 V — half-life logic is the same as time constant",
        ],
        "correct_index": 0,
        "explanation": "τ = RC = 20 s, and V = V₀e^(−t/τ): at t = τ the voltage is 100e⁻¹ ≈ 37 V. 2τ would give ≈ 13 V; 63% is the CHARGING side.",
        "skill": "RC discharge and the 37% marker",
        "difficulty": 3,
        "competency_code": "review-dc-circuits",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two long, parallel wires carry equal currents in the SAME direction. Where is the net magnetic field zero?",
        "options": [
            "MIDWAY between the wires — the fields point opposite and cancel",
            "Nowhere — fields always add between the wires",
            "Outside the pair, far beyond either wire",
            "At the surface of each wire individually",
        ],
        "correct_index": 0,
        "explanation": "Each wire's field circulates per its own current; midway, the two rings are equal in magnitude and opposite in direction, so B_net = 0 there. Outside the pair the fields add.",
        "skill": "parallel-wire field superposition",
        "difficulty": 3,
        "competency_code": "review-magnetic-fields",
    },
    {
        "level": "TRANSFER",
        "prompt": "A concave mirror forms an upright, virtual image 2× larger. The object stands 15 cm in front. Find the focal length.",
        "options": [
            "f = +30 cm",
            "f = +10 cm",
            "f = −15 cm",
            "f = +7.5 cm",
        ],
        "correct_index": 0,
        "explanation": "M = +2 with q virtual → q = −2p = −30 cm. Then 1/f = 1/15 + 1/(−30) = 1/30 → f = +30 cm (concave, converging).",
        "skill": "magnification to focal length",
        "difficulty": 3,
        "competency_code": "review-mirrors",
    },
    {
        "level": "TRANSFER",
        "prompt": "Light traveling in glass (n = 1.52) hits a glass-air boundary at 30° from the normal. What is the refraction angle in air?",
        "options": [
            "θ₂ ≈ 49° — the ray bends AWAY from the normal as it speeds up",
            "θ₂ ≈ 19° — the ray bends toward the normal",
            "θ₂ ≈ 30° — the angle is unchanged",
            "Total internal reflection — no ray emerges",
        ],
        "correct_index": 0,
        "explanation": "n₁sinθ₁ = n₂sinθ₂: 1.52 sin30° = sinθ₂ → sinθ₂ = 0.76 → θ₂ ≈ 49°. Into the lower index the ray bends away from the normal.",
        "skill": "Snell's law with indices",
        "difficulty": 3,
        "competency_code": "review-optics-basics",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "electric-current",
        "title": "Electric Current",
        "taxonomy_level": "understand",
        "description": "Define current I = Q/t (ampere), count charges via Q = Ne, and distinguish conventional current from electron flow.",
        "sort_order": 21,
    },
    {
        "code": "ohms-law",
        "title": "Ohm's Law",
        "taxonomy_level": "apply",
        "description": "Apply V = IR to resistors, treating V as the drop across and I as the current through, for ohmic materials.",
        "sort_order": 23,
    },
    {
        "code": "resistance-resistivity",
        "title": "Resistance and Resistivity",
        "taxonomy_level": "apply",
        "description": "Use R = ρL/A, distinguish material resistivity from object resistance, and apply the temperature rule R_T = R₀(1 + αT).",
        "sort_order": 24,
    },
    {
        "code": "series-networks",
        "title": "Resistors in Series",
        "taxonomy_level": "apply",
        "description": "Reduce series chains (Req = ΣRᵢ), distribute current equally and voltage by Vᵢ = IRᵢ, and verify with the drop-check.",
        "sort_order": 27,
    },
    {
        "code": "parallel-networks",
        "title": "Resistors in Parallel",
        "taxonomy_level": "apply",
        "description": "Reduce parallel groups (1/Req = Σ1/Rᵢ), use shortcuts, distribute current inverse-proportionally, and respect the below-smallest bound.",
        "sort_order": 28,
    },
    {
        "code": "rc-charging",
        "title": "RC Charging",
        "taxonomy_level": "apply",
        "description": "Compute τ = RC, q₀ = Cℰ, I₀ = ℰ/R and use q = q₀(1 − e^(−t/τ)) with the 63%/37% time-constant markers.",
        "sort_order": 31,
    },
    {
        "code": "rc-discharging",
        "title": "RC Discharging",
        "taxonomy_level": "apply",
        "description": "Apply q = q₀e^(−t/τ) to discharging capacitors and reuse the SAME τ as the charging clock.",
        "sort_order": 32,
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
        "code": "force-current-wire",
        "title": "Magnetic Force on a Current-Carrying Wire",
        "taxonomy_level": "apply",
        "description": "Derive and apply F = IL × B (magnitude BIL sin θ) for a straight wire in a uniform field.",
        "sort_order": 37,
    },
    {
        "code": "wire-field",
        "title": "Field of a Straight Current-Carrying Wire",
        "taxonomy_level": "apply",
        "description": "Compute B = μ₀I/(2πr) for a long straight wire, apply its proportionalities, and superpose fields from parallel wires.",
        "sort_order": 39,
    },
    {
        "code": "solenoid-field",
        "title": "Field of a Solenoid and Solenoid Design",
        "taxonomy_level": "apply",
        "description": "Compute the uniform interior field B = μ₀nI with n = N/L, and design a solenoid via n = B/(μ₀I), N = nL, d = N·2πr.",
        "sort_order": 41,
    },
    {
        "code": "reflection-law",
        "title": "Law of Reflection",
        "taxonomy_level": "apply",
        "description": "Apply θi = θr with angles measured from the normal to flat and angled surfaces.",
        "sort_order": 44,
    },
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
    {
        "code": "review-dc-circuits",
        "title": "Final Review: DC Networks and RC Circuits",
        "taxonomy_level": "apply",
        "description": "Review series-parallel resistor reduction, branch current/voltage distribution, and RC transients on the shared τ clock.",
        "sort_order": 66,
    },
    {
        "code": "review-magnetic-force",
        "title": "Final Review: Magnetic Forces",
        "taxonomy_level": "apply",
        "description": "Review F = qvB sinθ and F = ILB sinθ with the right-hand rule, including the negative-charge flip.",
        "sort_order": 67,
    },
    {
        "code": "review-magnetic-fields",
        "title": "Final Review: Magnetic Poles and Fields",
        "taxonomy_level": "apply",
        "description": "Review pole interactions, the Earth's field, wire and solenoid fields, and parallel-wire superposition.",
        "sort_order": 68,
    },
    {
        "code": "review-optics-basics",
        "title": "Final Review: Reflection and Refraction",
        "taxonomy_level": "apply",
        "description": "Review the normal-angle rule, n = c/v, Snell's law, and the frequency-invariance result.",
        "sort_order": 69,
    },
    {
        "code": "review-mirrors",
        "title": "Final Review: Mirrors",
        "taxonomy_level": "apply",
        "description": "Review the mirror equation and sign convention, real vs virtual images, and spherical aberration.",
        "sort_order": 70,
    },
    {
        "code": "review-lenses",
        "title": "Final Review: Thin Lenses and Aberrations",
        "taxonomy_level": "apply",
        "description": "Review converging/diverging identification, the lens-equation cases, and chromatic aberration.",
        "sort_order": 71,
    },
]

COMPETENCY_PREREQUISITES = [
    ("electric-current", "review-dc-circuits"),
    ("ohms-law", "review-dc-circuits"),
    ("resistance-resistivity", "review-dc-circuits"),
    ("series-networks", "review-dc-circuits"),
    ("parallel-networks", "review-dc-circuits"),
    ("rc-charging", "review-dc-circuits"),
    ("rc-discharging", "review-dc-circuits"),
    ("magnetic-fields", "review-magnetic-fields"),
    ("magnetic-poles", "review-magnetic-fields"),
    ("wire-field", "review-magnetic-fields"),
    ("solenoid-field", "review-magnetic-fields"),
    ("review-magnetic-fields", "review-magnetic-force"),
    ("magnetic-force-charge", "review-magnetic-force"),
    ("force-current-wire", "review-magnetic-force"),
    ("reflection-law", "review-optics-basics"),
    ("refraction-snell", "review-optics-basics"),
    ("review-optics-basics", "review-mirrors"),
    ("mirror-equation", "review-mirrors"),
    ("spherical-aberration", "review-mirrors"),
    ("review-optics-basics", "review-lenses"),
    ("thin-lenses", "review-lenses"),
    ("lens-equation", "review-lenses"),
    ("chromatic-aberration", "review-lenses"),
]

LESSON_COMPETENCIES = [
    {"code": "review-dc-circuits", "role": "teaches"},
    {"code": "review-magnetic-force", "role": "teaches"},
    {"code": "review-magnetic-fields", "role": "teaches"},
    {"code": "review-optics-basics", "role": "teaches"},
    {"code": "review-mirrors", "role": "teaches"},
    {"code": "review-lenses", "role": "teaches"},
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

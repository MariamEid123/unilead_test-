"""PHY211 — Physics, Module 13, Lesson 15: Final Exam Problem Clinic (Ch. 6–10).

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: 'Final' — the final-exam problem clinic built on the same
Chapters 6–10 problem bank as the Part 2 clinic, packaged as a standalone
lesson with 9 objectives, 13 worked examples, 12 common mistakes, 5 difficult
concepts, and 4 video lesson plans).

Where Module 12 consolidates, this clinic operates at EXAM SPEED: the same
competencies drilled for problem solving under one equation per topic, one
right-hand flip for negative charges, and one sign convention for all imaging.
Imported by ``curriculum.content`` and seeded by ``curriculum.seed``.
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
    "code": "M13",
    "title": "Module 13 — Final Exam Problem Clinic (Ch. 6–10)",
    "description": (
        "Exam-speed review of the final syllabus: circuit surgery (networks + "
        "RC), magnetic forces and field superposition for wires and solenoids, "
        "Snell's law with apparent depth and the critical angle, and every "
        "imaging question driven by the single mirror/lens equation with one "
        "sign convention."
    ),
    "sort_order": 13,
}

LESSON = {
    "code": "L15",
    "title": "Final Exam Clinic: Circuits, Magnetism & Optics Under the Clock",
    "description": (
        "A timed-review clinic: work the network-surgery invariants, run the "
        "RC clock, flip the right-hand rule for electrons, superpose wire "
        "fields without guessing signs, jump Snell to apparent depth and the "
        "critical angle, and drive all imaging through one equation."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Reduce series-parallel networks and distribute current and voltage without a calculator-first instinct.",
        "Deploy the single RC time constant for both charging and discharging questions.",
        "Apply magnetic pole rules, the Earth's field, and the absent monopole.",
        "Compute qvB and ILB forces, flipping the right-hand rule for negative charges.",
        "Compute wire and solenoid fields and superpose parallel-wire fields by reference directions.",
        "Apply Snell's law, apparent depth, and the critical angle with n = c/v.",
        "Solve the mirror and lens equations with one unified sign convention.",
        "Identify chromatic and spherical aberrations and their fixes.",
    ],
    "prerequisites": [
        "Electric current, Ohm's law, resistance, and resistivity (Lectures 6–7).",
        "Series and parallel resistor networks and RC circuits (Lectures 8–10).",
        "Magnetic poles, fields, forces, and wire/solenoid fields (Lectures 11–13).",
        "Reflection, refraction, apparent depth, mirrors, thin lenses, and aberrations (Lectures 14–15).",
        "Competency in the Module 12 final-review clinic.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "This clinic is about SPEED and ONE-LINER structure. Every topic "
            "fits a stencil: circuits → collapse to one Req (or one τ); "
            "magnetism → one force law plus right hand; optics → one equation "
            "1/p + 1/q = 1/f with a single sign convention. When stuck, ask "
            "'what is locked?' — the battery voltage, the shared current, or "
            "the shared charge — and everything else follows."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Circuit Surgery: One Resistor at a Time",
        "body": (
            "Series chains: Req = ΣRᵢ with the SAME current and divided "
            "voltages Vᵢ = IRᵢ. Parallel groups: 1/Req = Σ1/Rᵢ with the SAME "
            "voltage and inverse-proportional currents. Work OUTSIDE-IN — "
            "collapse, then unwind from the battery: ISupplied = ℰ/Rtotal "
            "becomes the seed for every branch split."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The drop-check",
        "body": (
            "Voltages around any closed loop must sum to the battery emf. After "
            "unwinding a network, add the drops for a sanity check — a common "
            "exam-saver when the numbers feel off."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The RC Clock",
        "body": (
            "τ = RC is ONE period serving both directions. Charging: "
            "q = q₀(1 − e^(−t/τ)), 63% at one τ, ~95% at 3τ. Discharging: "
            "q = q₀e^(−t/τ), 37% left at one τ. Initial current I₀ = ℰ/R and "
            "final charge q₀ = Cℰ set the endpoints of the race. A charged "
            "capacitor is an open circuit in steady state; an empty one is a "
            "short the instant the switch closes."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Magnetic Geography",
        "body": (
            "Poles come in pairs; isolated monopoles do not exist. Like repel, "
            "unlike attract; lines exit north, enter south. The Earth is a bar "
            "magnet with the geographic NORTH pole acting as a magnetic SOUTH "
            "pole — which is why a compass north needle is attracted there. "
            "Field-line density is field-strength; rings around wires and "
            "uniform interior concentrations in solenoids."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Forces and the right hand",
        "body": "F = |q|vB sin θ     F = ILB sin θ     F_L to v × B",
        "metadata": {
            "meaning": "Only the component of motion PERPENDICULAR to B feels the force; sin θ kills parallel motion and maximizes at 90°.",
            "when_used": "Right hand: fingers along v or I, curl into B, thumb = F for a POSITIVE carrier; for an ELECTRON flip the thumb. Whenever the charge is negative, the answer reverses.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Field Superposition Without Guessing",
        "body": (
            "Long straight wire: B = μ₀I/(2πr) in rings around the wire. "
            "Solenoid interior: B = μ₀nI with n = N/L, uniform across the "
            "cross-section. To superpose, draw each B vector at the target "
            "point from its source wire, THEN add. Equal SAME-direction "
            "currents cancel midway and add outside the pair; OPPOSITE "
            "currents add midway and cancel outside."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Optics: Angles, Indices, and the Critical Edge",
        "body": (
            "Angles are from the NORMAL. Reflection: θᵢ = θᵣ. Refraction: "
            "n₁sinθ₁ = n₂sinθ₂ with n = c/v. Frequency is invariant at the "
            "boundary; speed and wavelength scale by n (λ = λ₀/n). Going from "
            "dense to rare past θc = sin⁻¹(n₂/n₁), light totally internally "
            "reflects — diamond's sparkle, fiber optics, and the 'shiny' "
            "underwater ceiling are all this effect."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Apparent depth illusion",
        "body": (
            "Seen normally through a single surface, an object at real depth d "
            "appears at d/n: the water always looks SHALLOWER than it is, and "
            "gaps shift the same ratio. n = c/v does the whole job — no rays "
            "need sketching on the exam."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Mirrors & Lenses: the Single Equation",
        "body": (
            "One equation, all elements: 1/p + 1/q = 1/f. Mirrors use "
            "f = R/2 and power F = 1/f (diopters). Object side is where light "
            "comes in (p always positive); real images add on the "
            "reflecting/refracting side (q > 0); virtual images carry q < 0. "
            "Converging elements (concave mirror, convex lens) take f > 0; "
            "diverging ones f < 0. M = −q/p: negative M is inverted. "
            "Aberrations — chromatic (n varies with color, fix: achromatic "
            "doublet) and spherical (marginal rays beat paraxial rays, fix: "
            "stop the aperture / aspheric surface)."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — network with a pendant branch",
        "body": (
            "12 Ω and 6 Ω in parallel with a 4 Ω series tail and a 9-V battery: "
            "block = (12 × 6)/(12 + 6) = 4.0 Ω; total = 4 + 4 = 8.0 Ω; "
            "I = 9/8 = 1.125 A. Block voltage = 1.125 × 4 = 4.5 V, so the "
            "12 Ω branch takes 4.5/12 = 0.375 A and the 6 Ω takes "
            "4.5/6 = 0.75 A; the two branches rejoin to 1.125 A."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — the RC endpoints",
        "body": (
            "ℰ = 10 V charges C = 20 µF through R = 5.0 kΩ: I₀ = 10/5000 = "
            "2.0 mA, q₀ = 20 × 10⁻⁶ × 10 = 2.0 × 10⁻⁴ C, and τ = RC = 0.10 s. "
            "At t = 0.30 s the charge is 2.0 × 10⁻⁴ × (1 − e⁻³) ≈ 1.9 × 10⁻⁴ C."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — electron in a field, the flip",
        "body": (
            "An electron (q = −e) at v = 3.0 × 10⁶ m/s enters B = 0.40 T at "
            "60°: F = |q|vB sinθ = (1.6 × 10⁻¹⁹)(3 × 10⁶)(0.40)(0.866) ≈ "
            "1.7 × 10⁻¹³ N. The right hand on v × B gives the force for a "
            "positive object; for the electron the force points exactly "
            "OPPOSITE."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — two wires, add or subtract",
        "body": (
            "Two long wires, 10 A each, 10 cm apart: at the midpoint each wire "
            "gives B = μ₀I/(2π × 0.05) = 4.0 × 10⁻⁵ T. SAME direction currents "
            "→ the rings oppose at midpoint → B_net = 0; OPPOSITE currents → "
            "the rings reinforce → B_net = 8.0 × 10⁻⁵ T. Outside the pair the "
            "situation swaps."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — apparent depth",
        "body": (
            "A coin sits 1.8 m below a lake surface (n_w = 1.33). Viewed from "
            "above, d_app = d/n_w = 1.8/1.33 ≈ 1.35 m. The water looks 0.45 m "
            "shallower, so a swimmer underestimates the drop."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 6 — a magnifying camera lens",
        "body": (
            "Object at p = 18 cm, converging lens f = 12 cm: "
            "1/q = 1/12 − 1/18 = 1/36 → q = 36 cm (real, on the far side); "
            "M = −q/p = −2, a real, inverted, doubled image — the projection "
            "geometry of a slide projector."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "The parallel-current trap",
        "body": "The SMALLEST resistor drains the LARGEST current; verify ΣI_branch = I_total before moving on.",
    },
    {
        "section_type": "WARNING",
        "title": "Fully charged capacitor",
        "body": "Steady state → open circuit (branch dead). Do not compute an RC transient where none exists.",
    },
    {
        "section_type": "WARNING",
        "title": "Electrons flip the right hand",
        "body": "v × B points the force for a positive charge; an electron feels the OPPOSITE direction. The flipped thumb is half of every 'which way?' problem.",
    },
    {
        "section_type": "WARNING",
        "title": "Parallel-wire sign",
        "body": "Same-direction currents cancel midway; opposite-direction currents add midway. Draw the two B vectors at the point FIRST.",
    },
    {
        "section_type": "WARNING",
        "title": "Angles from the normal",
        "body": "The incident, reflected, and refracted angles all sit on the NORMAL, not the surface plane.",
    },
    {
        "section_type": "WARNING",
        "title": "Apparent depth is a reduction, not an add",
        "body": "Critical / apparent-depth: the pool always looks SHALLOWER: d_app = d/n, and the shift is d(1 − 1/n).",
    },
    {
        "section_type": "WARNING",
        "title": "One sign convention",
        "body": "q > 0 on the incoming side and real images add on the reflecting/refracting side, for BOTH mirrors and lenses. Mixing side-rules is the top exam error.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The right-hand rule and the negative-charge flip",
        "body": (
            "The hand rule is a convention for POSITIVE motion; the exam "
            "always hides at least one electron. Anchor the positive answer "
            "first, then flip it. Analogy: a one-way street sign read in a "
            "mirror — same geometry, opposite travel. Steps: fingers v → curl "
            "B → thumb for q > 0 → reverse for q < 0. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Superposition of parallel-wire fields",
        "body": (
            "Wire fields are rings with handedness, so 'same direction' and "
            "'opposite direction' swap the add/cancel zones. Sketch the rings "
            "at the single point of interest before adding. Analogy: two taps "
            "stirring a bathtub with clockwise (add) or mirror-image swirls "
            "(cancel). Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Apparent depth and the emerging ray",
        "body": (
            "The brain straightens refracted rays, so the perceived source "
            "sits shallower than the real one (d_app = d/n). Students draw "
            "the reflected angle at the wrong interface. Steps: find where "
            "light LEAVES the denser medium, apply Snell there, then imagine "
            "the backward-straightened rays. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "One sign convention, two element types",
        "body": (
            "The single hardest thing to unlearn is mirror-vs-lens side rules. "
            "Anchor: light comes in one side; real images cross on the "
            "inside; virtual means q < 0 on the incoming side. Walk every "
            "case through the same 1/p + 1/q = 1/f pipeline rather than "
            "recalling the six-case table cold. Difficulty: VERY HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The exam-speed invariant hunt",
        "body": (
            "Fast problems are won by naming the locked quantity: the battery "
            "pinches V across a sub-network; series pins I; series capacitors "
            "pin Q; a disconnected capacitor pins Q. Everything else is "
            "algebra. Analogy: a detective asking 'what cannot change?' before "
            "looking at the scene. Difficulty: HARD."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Circuits: collapse outside-in; series shares I, parallel shares V; check the sum of drops.\n"
            "• RC: τ = RC is one clock — 63% up, 37% down; charged capacitor blocks its branch.\n"
            "• Magnetism: poles paired, Earth's geographic north = magnetic south; F = qvB = ILB with the right hand, flipped for negatives.\n"
            "• Fields: wire μ₀I/2πr, solenoid μ₀nI; same-direction wires cancel midway, opposite add midway.\n"
            "• Optics: angles from the normal; Snell n₁sinθ₁ = n₂sinθ₂; n = c/v; λ = λ₀/n.\n"
            "• Apparent depth d/n always shallower; θc = sin⁻¹(n₂/n₁) enables TIR.\n"
            "• One imaging equation 1/p + 1/q = 1/f with one sign convention; M = −q/p.\n"
            "• Aberrations: chromatic (split into achromatic doublet) and spherical (stop the aperture)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Series / parallel equivalent — the resistance that replaces a group (below smallest for parallel).\n"
            "• Time constant τ = RC.\n"
            "• Pole — always paired; no isolated monopole.\n"
            "• Right-hand rule — force direction for a positive velocity cross field.\n"
            "• Apparent depth — perceived shallowness d/n of an object seen through a surface.\n"
            "• Critical angle — the dense-to-rare incidence that yields a 90° emergent ray.\n"
            "• Virtual image — the point from which outgoing rays appear to diverge.\n"
            "• Chromatic / spherical aberration — color-dependent focus and marginal-ray focus."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• Req = ΣRᵢ; 1/Req = Σ1/Rᵢ.\n"
            "• τ = RC; q = q₀(1 − e^(−t/τ)); q = q₀e^(−t/τ).\n"
            "• F = qvB sinθ; F = ILB sinθ.\n"
            "• B = μ₀I/(2πr); B = μ₀nI.\n"
            "• n = c/v; n₁sinθ₁ = n₂sinθ₂; d_app = d/n; θc = sin⁻¹(n₂/n₁).\n"
            "• 1/p + 1/q = 1/f; M = −q/p; F = 1/f."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Ask what is locked. Circuits: collapse to Req, unwrap from the "
            "battery. RC: one τ both ways. Magnetism: every pole is paired; "
            "F = qvB = ILB with one hand and a flip for electrons; rings "
            "around wires superpose, so drawing the two B vectors settles add "
            "or subtract. Optics: angles from the normal, Snell + n = c/v, "
            "apparent depth d/n, TIR past θc, and one equation for every "
            "mirror and lens. Aberrations: color and edge rays — two fixes, "
            "doublet and aperture."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "Three Fingers, No Guessing: The Right-Hand Rule and the Angles That Kill the Force",
        "description": (
            "The one hand that answers every magnetic-force question: where "
            "v and I point, where B points, what sin θ does, and the single "
            "flip that turns a proton answer into an electron answer."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Right-hand rule for qv × B and IL × B, with the negative-charge flip",
            "target_student": "First-year university student",
            "objective": "Determine magnetic force directions and magnitudes for positive and negative carriers without guessing.",
            "hook": "One hand, three fingers, and one sneaky flip — and the exam loses its favorite trick question.",
            "explanation_steps": [
                "F = |q|vB sinθ: only the perpendicular component of motion feels force.",
                "Right-hand rule: fingers along v (or I), curl into B, thumb = F for a positive charge.",
                "The flip: electrons reverse the thumb.",
                "θ is measured BETWEEN v and B — parallel is zero force, perpendicular is maximum.",
            ],
            "common_mistake": "Forgetting to flip the hand for a negative charge or measuring θ from the wrong vector.",
            "check": "An electron moves east through an upward B. Which way does the force point?",
            "final_takeaway": "Right hand for the positive carrier, flip for the electron; sin θ gates the magnitude.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "Two Wires, One Question: Add or Subtract?",
        "description": (
            "Superposition for parallel current-carrying wires in one decision "
            "tree: reference rings, same-direction vs opposite-direction rules, "
            "and the B = μ₀I/2πr magnitudes that make the exam numeric work."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Superposition of long-wire magnetic fields",
            "target_student": "First-year university student",
            "objective": "Decide add-vs-cancel and compute the net field for any pair of parallel wires.",
            "hook": "Two identical wires, one question, and the answer flips on a single word: direction.",
            "explanation_steps": [
                "Each wire wraps B in rings: thumb along current, fingers curl.",
                "Draw B at the target point from EACH wire.",
                "Same-direction currents → opposite rings → cancel midway; opposite currents → same rings → add midway.",
                "Outside the pair the roles swap; magnitudes from B = μ₀I/2πr.",
            ],
            "common_mistake": "Applying the resistor 'same-direction adds' intuition to magnetic rings.",
            "check": "Two wires, 10 A each, opposite currents, 10 cm apart: what is B midway?",
            "final_takeaway": "Draw the rings first; the add-or-subtract answer is the rings themselves.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "For resistors in PARALLEL, which quantity is the SAME across every branch?",
        "options": [
            "The voltage drop — every branch sits across the same potential difference",
            "The current — all branches carry the same amps",
            "The power — each branch dissipates identically",
            "The charge — each branch stores the same coulombs",
        ],
        "correct_index": 0,
        "explanation": "Parallel branches share the same two nodes, hence the same voltage; current divides inversely with resistance so the amp readings differ.",
        "skill": "parallel invariant",
        "difficulty": 1,
        "competency_code": "exam-circuits",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "A negative charge moves PARALLEL to a uniform magnetic field. The magnetic force on it is:",
        "options": [
            "ZERO — sin θ = 0 for motion along B",
            "Maximum, but opposite to v × B for the electron",
            "Half-strength and perpendicular to B",
            "Zero only for positive charges",
        ],
        "correct_index": 0,
        "explanation": "F = |q|vB sinθ, and sin 0° = 0: motion parallel to the field experiences no magnetic force regardless of sign.",
        "skill": "parallel motion, zero force",
        "difficulty": 1,
        "competency_code": "exam-magnetism",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "For total internal reflection to occur, light must be:",
        "options": [
            "Traveling from a HIGHER-index medium toward a lower index, at incidence beyond the critical angle",
            "Entering a denser medium at any angle",
            "Reflecting off a mirror's surface",
            "Moving from a lower-index medium into a higher one past 90°",
        ],
        "correct_index": 0,
        "explanation": "TIR needs a dense-to-rare step (n₁ > n₂) and an incidence angle past θc = sin⁻¹(n₂/n₁); then the boundary emits no refracted ray.",
        "skill": "total internal reflection condition",
        "difficulty": 1,
        "competency_code": "exam-optics-basics",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "A CONVEX (diverging) mirror always produces which image for a real object?",
        "options": [
            "Virtual, upright, and REDUCED",
            "Real, inverted, and magnified",
            "Real, upright, and reduced",
            "Virtual, inverted, and magnified",
        ],
        "correct_index": 0,
        "explanation": "A convex mirror never gathers outgoing rays, so the image is virtual (q < 0), upright (M > 0), and smaller — for every real-object position.",
        "skill": "convex mirror, fixed character",
        "difficulty": 1,
        "competency_code": "exam-imaging",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A 100 µF capacitor charges through a 1.0 kΩ resistor from a 12-V source. Find the time constant and the initial charging current.",
        "options": [
            "τ = 0.10 s and I₀ = 12 mA",
            "τ = 10 s and I₀ = 12 mA",
            "τ = 0.10 s and I₀ = 1.2 mA",
            "τ = 1.0 s and I₀ = 120 mA",
        ],
        "correct_index": 0,
        "explanation": "τ = RC = (1.0 × 10³)(100 × 10⁻⁶) = 0.10 s; the empty capacitor is a short at t = 0, so I₀ = ℰ/R = 12/1000 = 12 mA.",
        "skill": "RC time constant and initial current",
        "difficulty": 2,
        "competency_code": "exam-circuits",
    },
    {
        "level": "APPLY",
        "prompt": "A 0.50-m wire carrying 8.0 A sits perpendicular to a 0.20-T field. Find the magnetic force on the wire.",
        "options": [
            "F = 0.80 N",
            "F = 8.0 N",
            "F = 3.2 N",
            "F = 0.16 N",
        ],
        "correct_index": 0,
        "explanation": "Perpendicular gives sin θ = 1: F = ILB = (8.0)(0.50)(0.20) = 0.80 N, directed by the right-hand rule on I × B.",
        "skill": "force on a current wire",
        "difficulty": 2,
        "competency_code": "exam-magnetism",
    },
    {
        "level": "APPLY",
        "prompt": "A coin lies 1.8 m below the surface of a lake (n = 1.33). How deep does it appear when viewed from directly above?",
        "options": [
            "d_app ≈ 1.35 m — the water looks shallower by the factor n",
            "d_app ≈ 2.4 m — the water magnifies the depth",
            "d_app = 1.8 m — apparent depth equals real depth",
            "d_app ≈ 0.90 m — the depth halves",
        ],
        "correct_index": 0,
        "explanation": "Seen normally, d_app = d/n = 1.8/1.33 ≈ 1.35 m. The boundary bends the emerging rays so the brain places the coin higher.",
        "skill": "apparent depth",
        "difficulty": 2,
        "competency_code": "exam-optics-basics",
    },
    {
        "level": "APPLY",
        "prompt": "An object sits 30 cm in front of a converging lens with f = 10 cm. Locate the image.",
        "options": [
            "q = 15 cm — real and inverted",
            "q = 7.5 cm — virtual and upright",
            "q = 20 cm — real and upright",
            "q = 15 cm — virtual and inverted",
        ],
        "correct_index": 0,
        "explanation": "1/q = 1/f − 1/p = 1/10 − 1/30 = 2/30 → q = +15 cm (real, far side); M = −q/p = −0.5, inverted.",
        "skill": "thin lens equation",
        "difficulty": 2,
        "competency_code": "exam-imaging",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Four 12-Ω resistors are arranged as: two in parallel, in series with two in parallel. Find the equivalent resistance.",
        "options": [
            "Req = 12 Ω",
            "Req = 3 Ω",
            "Req = 24 Ω",
            "Req = 48 Ω",
        ],
        "correct_index": 0,
        "explanation": "Each parallel pair: 1/R = 1/12 + 1/12 = 1/6 → 6 Ω; two 6 Ω in series give 12 Ω.",
        "skill": "mixed-network collapse",
        "difficulty": 3,
        "competency_code": "exam-circuits",
    },
    {
        "level": "TRANSFER",
        "prompt": "Design a solenoid with interior field B = 0.10 T carrying I = 2.0 A over length L = 0.50 m. How many turns are needed?",
        "options": [
            "N ≈ 2.0 × 10⁴ turns",
            "N ≈ 4.0 × 10⁴ turns",
            "N ≈ 2.0 × 10³ turns",
            "N ≈ 8.0 × 10³ turns",
        ],
        "correct_index": 0,
        "explanation": "n = B/(μ₀I) = 0.10/(4π × 10⁻⁷ × 2.0) ≈ 3.98 × 10⁴ m⁻¹; N = nL ≈ 2.0 × 10⁴ turns.",
        "skill": "solenoid design",
        "difficulty": 3,
        "competency_code": "exam-magnetism",
    },
    {
        "level": "TRANSFER",
        "prompt": "Light in glass (n = 1.52) strikes a glass-air boundary. Find the critical angle.",
        "options": [
            "θc ≈ 41°, beyond which the ray totally reflects",
            "θc ≈ 49°, beyond which the ray straightens",
            "θc ≈ 90°, TIR is impossible here",
            "θc ≈ 33°, below which nothing emerges",
        ],
        "correct_index": 0,
        "explanation": "sin θc = n₂/n₁ = 1.00/1.52 = 0.658 → θc ≈ 41°. Incidence past this completely reflects; below it, part refracts to air.",
        "skill": "critical angle",
        "difficulty": 3,
        "competency_code": "exam-optics-basics",
    },
    {
        "level": "TRANSFER",
        "prompt": "A converging lens (f = 12 cm) forms a real image 36 cm away. Where is the object, and what is the magnification?",
        "options": [
            "p = 18 cm with M = −2 (inverted, doubled)",
            "p = 9 cm with M = −4",
            "p = 36 cm with M = −1",
            "p = 18 cm with M = +2 (virtual)",
        ],
        "correct_index": 0,
        "explanation": "1/p = 1/f − 1/q = 1/12 − 1/36 = 2/36 → p = 18 cm; M = −q/p = −36/18 = −2, a real, inverted, doubled image.",
        "skill": "lens equation with magnification",
        "difficulty": 3,
        "competency_code": "exam-imaging",
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
        "code": "exam-circuits",
        "title": "Final Exam: Circuit Surgery",
        "taxonomy_level": "apply",
        "description": "Solve mixed resistor networks and RC transients at exam speed, using the shared-τ clock and network invariants.",
        "sort_order": 72,
    },
    {
        "code": "exam-magnetism",
        "title": "Final Exam: Magnetic Forces and Fields",
        "taxonomy_level": "apply",
        "description": "Compute qvB and ILB forces with the right-hand flip, wire/solenoid fields, and parallel-wire superposition.",
        "sort_order": 73,
    },
    {
        "code": "exam-optics-basics",
        "title": "Final Exam: Refraction, Apparent Depth, Critical Angle",
        "taxonomy_level": "apply",
        "description": "Apply Snell's law, apparent depth d/n, and the critical-angle condition for total internal reflection.",
        "sort_order": 74,
    },
    {
        "code": "exam-imaging",
        "title": "Final Exam: Mirrors, Lenses, and Aberrations",
        "taxonomy_level": "apply",
        "description": "Drive all imaging through 1/p + 1/q = 1/f with one sign convention, and identify chromatic/spherical aberration.",
        "sort_order": 75,
    },
]

COMPETENCY_PREREQUISITES = [
    ("electric-current", "exam-circuits"),
    ("ohms-law", "exam-circuits"),
    ("resistance-resistivity", "exam-circuits"),
    ("series-networks", "exam-circuits"),
    ("parallel-networks", "exam-circuits"),
    ("rc-charging", "exam-circuits"),
    ("rc-discharging", "exam-circuits"),
    ("magnetic-fields", "exam-magnetism"),
    ("magnetic-poles", "exam-magnetism"),
    ("wire-field", "exam-magnetism"),
    ("solenoid-field", "exam-magnetism"),
    ("magnetic-force-charge", "exam-magnetism"),
    ("force-current-wire", "exam-magnetism"),
    ("reflection-law", "exam-optics-basics"),
    ("refraction-snell", "exam-optics-basics"),
    ("exam-optics-basics", "exam-imaging"),
    ("mirror-equation", "exam-imaging"),
    ("thin-lenses", "exam-imaging"),
    ("lens-equation", "exam-imaging"),
    ("chromatic-aberration", "exam-imaging"),
    ("spherical-aberration", "exam-imaging"),
]

LESSON_COMPETENCIES = [
    {"code": "exam-circuits", "role": "teaches"},
    {"code": "exam-magnetism", "role": "teaches"},
    {"code": "exam-optics-basics", "role": "teaches"},
    {"code": "exam-imaging", "role": "teaches"},
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

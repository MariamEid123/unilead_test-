"""PHY211 — Physics, Module 7, Lecture 9: Sources of the Magnetic Field.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 9, Fall 2024 —
'Sources of the Magnetic Field', Chapter 8).

Builds every field from moving charge: the Biot–Savart law as the master
ingredient, then the straight wire, the loop/coil, the solenoid (including a
design procedure), and Lenz's law for induced currents. Imported by
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
    "code": "M7",
    "title": "Module 7 — Sources of the Magnetic Field",
    "description": (
        "Chapter 8: where B actually comes from. The Biot–Savart law slices any "
        "current into elements, then the canonical geometries — straight wire, "
        "loop/coil, solenoid — follow in one step each; solenoid design ties the "
        "formulas to a physical build, and Lenz's law closes the loop with the "
        "direction of induced currents."
    ),
    "sort_order": 7,
}

LESSON = {
    "code": "L9",
    "title": "Sources of the Magnetic Field: Biot–Savart, Wires, Loops, Solenoids, and Lenz's Law",
    "description": (
        "Lecture 9 — the master equation of magnetism: the four experimental "
        "observations of Biot and Savart, the field of a long straight wire "
        "B = μ₀I/(2πr), the loop center B = μ₀I/2R and its bar-magnet look, the "
        "uniform interior of a solenoid B = μ₀nI with the full design chain "
        "(target B → turns → wire length), and Lenz's law for the direction of "
        "induced current."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "State the four experimental observations behind the Biot–Savart law and the law's vector and magnitude forms.",
        "Identify μ₀ = 4π × 10⁻⁷ T·m/A as the magnetic permeability of free space.",
        "Compute the field of a long straight wire B = μ₀I/(2πr) and its proportionalities (∝ I, ∝ 1/r).",
        "Compute the field at the center of a current loop B = μ₀I/(2R) and of an N-turn coil B = μ₀NI/(2R).",
        "Describe the field-line patterns of a loop and a solenoid, and their resemblance to bar magnets.",
        "Compute the uniform interior field of a solenoid B = μ₀nI with n = N/L.",
        "Design a solenoid: target B → turns N → wire length d = N·2πr.",
        "State Lenz's law and determine the direction of an induced current for a changing flux.",
    ],
    "prerequisites": [
        "Electric current I = Q/t and the carrier picture (Lecture 6).",
        "The magnetic field B, its direction, and its units (Lecture 8).",
        "The right-hand rule for v × B as practiced in Lecture 8.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Lecture 8 told us what B does (sideways forces, circles, wire pulls). "
            "This lecture says where B comes from: moving charge, quantified by "
            "the Biot–Savart law. Every geometry — wire, loop, solenoid — is the "
            "same law applied with more order, and Lenz's law finally says what "
            "happens when a field through a loop begins to change."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Experiments of Biot and Savart",
        "body": (
            "Biot and Savart measured the field contribution dB from a tiny "
            "current element and found four facts: (1) dB ∝ I — more current, "
            "more field; (2) dB ∝ ds — longer element, more contribution; (3) dB ∝ "
            "sin θ — the element's tilt relative to the direction to the point "
            "matters; (4) dB ∝ 1/r² — the field dies off with the square of the "
            "distance from the element."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "The Biot–Savart Law",
        "body": "dB = (μ₀/4π) I ds sin θ / r²",
        "metadata": {
            "meaning": "ced one current element ds contributes dB, always PERPENDICULAR to both the element direction ds and the vector r̂ to the point; μ₀ = 4π × 10⁻⁷ T·m/A is the magnetic permeability of free space.",
            "when_used": "Fields of current distributions. Sum (integrate) the elements over the entire wire — nothing is ever a single element.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Slice, then sum",
        "body": (
            "The strength of Biot–Savart is that it chops any current shape into "
            "tiny straight pieces, finds each dB, and adds them with direction. "
            "The straight-wire, loop, and solenoid results below are what the sum "
            "produces — never apply the whole-wire formula at once."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Field of a long straight wire",
        "body": "B = μ₀I / (2πr)",
        "metadata": {
            "meaning": "At distance r from an infinitely long straight wire. Field lines CIRCLE the wire (right-hand rule: thumb along the current, fingers curl along B).",
            "when_used": "Straight-wire geometries. Watch the proportions: B ∝ I (double the current, double B) and B ∝ 1/r (double the distance, HALVE B).",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Wire field numbers",
        "body": (
            "A wire carries 10 A; a point sits 0.10 m away: B = (4π × 10⁻⁷)(10)/"
            "(2π)(0.10) = 2.0 × 10⁻⁵ T. Double the distance to 0.20 m: 1.0 × 10⁻⁵ T. "
            "Raise the current to 20 A: 4.0 × 10⁻⁵ T — the two proportionalities "
            "in action."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Center of a current loop (and an N-turn coil)",
        "body": "B = μ₀I / (2R)      N-turn coil:  B = μ₀NI / (2R)",
        "metadata": {
            "meaning": "At the center of a circular loop of radius R. Every turn adds its field, so N turns multiply by N.",
            "when_used": "Loop/coil center problems. Do NOT confuse with the straight-wire formula — loop puts R (not r) in the denominator; the 2π is gone.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "A loop is a short bar magnet",
        "body": (
            "The field-line pattern around a current loop resembles the field "
            "around a SHORT bar magnet: field lines pass through the loop, wrap "
            "outside, and return. The field at the center points along the loop's "
            "axis — the right-hand curl rule (fingers along the current, thumb = "
            "field direction at the center)."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Solenoid: a Helix That Makes a Uniform Field",
        "body": (
            "Wind a long wire into a helix — that is a solenoid. Inside, the "
            "contributions of all the turns align along the axis and produce a "
            "uniform field: B = μ₀ n I, with n = N/L the number of turns per unit "
            "length. The solenoid is a long bar magnet: the interior field is "
            "uniform and axial, and it strengthens with more turns per meter and "
            "more current."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Solenoid interior field",
        "body": (
            "A solenoid has 400 turns over 0.20 m carrying 2.0 A. n = N/L = 400/"
            "0.20 = 2000 turns/m. B = μ₀nI = (4π × 10⁻⁷)(2000)(2.0) ≈ 5.0 × 10⁻³ T. "
            "To wind such a solenoid with wire of radius r, the total wire length "
            "is d = N × 2πr (each turn is one circumference)."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Solenoid Design: The Full Chain",
        "body": (
            "The lecture's worked example designs a solenoid for a bacteria-"
            "magnetism experiment. Given the target field B, the current I, and "
            "the winding length L, climb the chain in reverse: (1) n = B/(μ₀I) — "
            "turns per meter the field demands; (2) N = nL — total turns; "
            "(3) d = N·2πr — total wire length to buy. Design problems turn "
            "formulas around: decide what unknown the target field fixes, solve "
            "for it, then keep climbing."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Forces Between Parallel Currents (Qualitative)",
        "body": (
            "Because each wire sits in the other's B field, parallel wires exert "
            "forces on each other: currents in the SAME direction attract, "
            "opposite currents repel. The lecture presents these as figures only; "
            "the quantitative formulas are beyond this course's scope."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Lenz's Law: Nature Fights Back",
        "body": (
            "A closed, conducting loop experiences an induced current only when "
            "the magnetic flux through it CHANGES. The direction of that induced "
            "current always opposes the CHANGE — the induced field supports the "
            "original field when the flux decreases, and opposes it when the flux "
            "increases. If the field is static, there is no induced current at "
            "all."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The four-step Lenz recipe",
        "body": (
            "(1) Is the flux CHANGING? No change → no current. (2) Which way — "
            "increasing or decreasing? (3) Oppose the change: increasing → induced "
            "field AGAINST the original; decreasing → induced field WITH the "
            "original. (4) Curl the right hand along the induced current: the "
            "thumb points along the induced field."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — solenoid design chain (source example)",
        "body": (
            "Design a solenoid producing B = 2.0 × 10⁻⁴ T for a bacteria-magnetism "
            "experiment, winding length L = 0.10 m, current I = 1.0 A, wire radius "
            "r = 2.0 cm. Step 1: n = B/(μ₀I) = 2.0 × 10⁻⁴/(4π × 10⁻⁷ × 1.0) "
            "≈ 159 turns/m. Step 2: N = nL = 159 × 0.10 ≈ 16 turns. Step 3: total "
            "wire d = N·2πr = 16 × 2π × 0.020 ≈ 2.01 m. The chain: target field → "
            "turns per meter → turns → wire to buy."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — field of a straight wire",
        "body": (
            "A wire carries 10 A. The field 0.10 m away: B = μ₀I/(2πr) = "
            "(4π × 10⁻⁷)(10)/(2π)(0.10) = 2.0 × 10⁻⁵ T. Check the proportions: at "
            "0.20 m, B = 1.0 × 10⁻⁵ T (half); with 20 A at 0.10 m, B = 4.0 × 10⁻⁵ T "
            "(double). Each factor moves by its own proportional rule."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — center of a loop and an N-turn coil",
        "body": (
            "A circular loop of radius 5.0 cm carries 5.0 A. Center field: "
            "B = μ₀I/(2R) = (4π × 10⁻⁷)(5.0)/(2 × 0.050) ≈ 6.3 × 10⁻⁵ T. Wrap the "
            "same wire into N = 50 turns at the same radius: B = μ₀NI/(2R) = "
            "(4π × 10⁻⁷)(50)(5.0)/(0.10) ≈ 3.1 × 10⁻³ T — fifty times the "
            "single-turn value."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — solenoid interior field",
        "body": (
            "A 400-turn solenoid is wound over 0.20 m and carries 2.0 A. "
            "n = N/L = 400/0.20 = 2000 turns/m. B = μ₀nI = (4π × 10⁻⁷)(2000)(2.0) "
            "≈ 5.0 × 10⁻³ T. The interior field is uniform: same B at every axial "
            "point, independent of where inside you measure."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — Lenz direction workout",
        "body": (
            "A bar-magnet's north pole approaches (north first) a closed loop from "
            "the left. Flux through the loop is increasing, northward into the "
            "loop. Lenz: oppose the increase → the loop's induced field points "
            "southward (away from the approaching north pole). Right-hand curl "
            "with the thumb southward gives the induced current viewed from the "
            "magnet's side as clockwise, magnetically repelling the approach. "
            "Pull the magnet away: flux decreasing → induced field northward → the "
            "loop attracts, resisting the retreat."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Whole-wire treatment",
        "body": "Biot–Savart needs the wire SLICED into elements and summed. Substituting as if the whole wire were one element gives garbage — the law is a pointwise building block.",
    },
    {
        "section_type": "WARNING",
        "title": "Opposing the field instead of the change",
        "body": "The induced field opposes the CHANGE in flux, not the field itself. A decreasing flux is SUPPORTED by the induced field — always ask 'increasing or decreasing?' first.",
    },
    {
        "section_type": "WARNING",
        "title": "r vs r², and the missing sin θ",
        "body": "dB falls off as 1/r² from its element; the integrated straight wire then gives 1/r. Feed the θ into sin θ and the distance into the right power for the chosen formula.",
    },
    {
        "section_type": "WARNING",
        "title": "N vs n",
        "body": "n is turns PER UNIT LENGTH (n = N/L); N is the total count. The solenoid field uses n — forget the division and you're off by the length's worth of turns.",
    },
    {
        "section_type": "WARNING",
        "title": "Wire length vs solenoid length",
        "body": "The winding takes d = N·2πr meters of wire — each turn is a circumference. That wire length is not the solenoid's length L; mixing the two ruins a design at step 3.",
    },
    {
        "section_type": "WARNING",
        "title": "Loop/wire formula mix-up",
        "body": "Wire B = μ₀I/(2πr) vs loop-center B = μ₀I/(2R). The wire's r is the perpendicular distance; the loop's R is the loop radius — and only the loop gets multiplied by N for a coil.",
    },
    {
        "section_type": "WARNING",
        "title": "Static-magnet induction",
        "body": "A magnet resting next to a loop induces nothing: Lenz requires a CHANGING flux. Motion toward/away or a growing current alters the flux; stillness does not.",
    },
    {
        "section_type": "WARNING",
        "title": "Wrong μ₀",
        "body": "μ₀ = 4π × 10⁻⁷ T·m/A, not 4π × 10⁻⁷ raw and not 9 × 10⁹. It is the vacuum's magnetic permeability, the partner of ε₀ in the wave speed c² = 1/(ε₀μ₀).",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Biot–Savart Slices (VERY HARD)",
        "body": (
            "A current element ds contributes dB perpendicular to both ds and r̂, "
            "scaled by sin θ and 1/r² — and the real field is the SUM over every "
            "element. Analogy: a candle is the whole lit wick, but its light at "
            "your eye is every point's share added together; each point "
            "contributes less as it's farther and more as it's aimed at you. "
            "Slicing + summing is the concept to bank."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Lenz's Law: Opposing the Change, Not the Field (HARD)",
        "body": (
            "Your instinct reads 'opposes' as opposing the field — but a decaying "
            "field is supported by the induced current. Analogy: a thermostat "
            "fights the change, not the temperature: in a cooling room it calls "
            "for heat. Four steps: changing? which way? oppose it? curl the hand. "
            "Static flux → no induced current, ever."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Superposing Fields From Two Wires",
        "body": (
            "Two wires, one point: B_total is the VECTOR SUM. Same-direction "
            "currents give opposed fields that fight (a zero point sits between "
            "same-direction, closer to the weaker wire); opposite currents give "
            "fields that add. Analogy: two people pushing opposite ways on a door "
            "versus two people pushing the same way."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "n vs N and the Two Lengths",
        "body": (
            "A solenoid has two 'lengths' hiding in it: the solenoid length L "
            "(the helix's extent) and the wire wound (each turn a 2πr loop, "
            "summed to d = N·2πr). n = N/L feeds the field formula; d buys the "
            "wire. Analogy: turns per meter is the thread pitch of a screw — "
            "tighter pitch (bigger n) means stronger field per meter."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Loop as a Bar Magnet",
        "body": (
            "Field lines pass cleanly through a loop's center, wrap outside, and "
            "close — the exact map of a short bar magnet. This one analogy lets "
            "you sand the solenoid's poles: current direction + right-hand curl "
            "names the face that acts north."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Biot–Savart: dB ∝ I, ∝ ds, ∝ sin θ, ∝ 1/r² — μ₀ = 4π × 10⁻⁷ T·m/A; the real field is the sum over all elements.\n"
            "• Straight wire: B = μ₀I/(2πr) — circles around the wire, ∝ I, ∝ 1/r.\n"
            "• Loop center: B = μ₀I/(2R); N-turn coil: μ₀NI/(2R) — a loop looks like a short bar magnet.\n"
            "• Solenoid: helix; interior field uniform and axial: B = μ₀nI, n = N/L; winding takes d = N·2πr.\n"
            "• Design chain: target B → n = B/(μ₀I) → N = nL → d = N·2πr.\n"
            "• Parallel currents: same direction attract, opposite repel (qualitative).\n"
            "• Lenz: induced current ⇔ changing flux; direction opposes the change — supporting the field when flux decreases."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Magnetic permeability of free space μ₀ — constant of the field laws: 4π × 10⁻⁷ T·m/A.\n"
            "• Turns per unit length n — n = N/L, the solenoid's winding density.\n"
            "• Solenoid — a long wire wound in a helix; uniform interior field.\n"
            "• Induced current — current in a closed loop caused by a CHANGING magnetic flux.\n"
            "• Lenz's law — the induced current opposes the change producing it.\n"
            "• Magnetic flux — the field through a surface; changing flux is what induction needs."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• dB = (μ₀/4π) I ds sin θ / r² — Biot–Savart element.\n"
            "• B = μ₀I/(2πr) — long straight wire.\n"
            "• B = μ₀I/(2R); B = μ₀NI/(2R) — loop center / N-turn coil.\n"
            "• B = μ₀nI, n = N/L — solenoid interior.\n"
            "• d = N·2πr — wire length to wind N turns of radius r.\n"
            "• Design chain: n = B/(μ₀I); N = nL."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Magnetic fields come from moving charge, sliced into elements by "
            "Biot–Savart: dB ∝ I, ∝ ds, ∝ sin θ, ∝ 1/r², with μ₀ = 4π × 10⁻⁷. "
            "Sum the slices: a straight wire gives B = μ₀I/(2πr), circling with "
            "the right hand, ∝ I and ∝ 1/r (10 A, 0.10 m → 2 × 10⁻⁵ T). Bend it "
            "into a loop: center B = μ₀I/(2R), N turns multiply — the loop is a "
            "short bar magnet. Coil it into a solenoid: uniform interior B = μ₀nI, "
            "n = N/L (400 turns/0.20 m, 2 A → 5 × 10⁻³ T); designing one means "
            "climbing n = B/(μ₀I) → N = nL → d = N·2πr. And when a loop's flux "
            "CHANGES, Lenz aims the induced current to fight the change — four "
            "steps: changing? which way? oppose it? curl the hand."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "Slicing the Wire: The Biot–Savart Law",
        "description": (
            "The four experimental observations behind Biot–Savart, the element "
            "formula dB = (μ₀/4π) I ds sin θ / r², and the straight-wire, "
            "loop/coil, and solenoid fields as the sums of slices."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "The Biot–Savart law as the source of all magnetic fields",
            "target_student": "First-year university student",
            "objective": "State the four observations, interpret the element formula, and compute wire, loop/coil, and solenoid fields by choosing the right geometry.",
            "hook": "Candlelight reaches your eyes from every point of the flame at once — no single point owns it. A wire's field is the same: slice it, add every element, and the whole is the sum.",
            "explanation_steps": [
                "The four observations: dB ∝ I, ∝ ds, ∝ sin θ, ∝ 1/r².",
                "μ₀ = 4π × 10⁻⁷ T·m/A, the vacuum's permeability.",
                "Element formula dB = (μ₀/4π) I ds sin θ / r², perpendicular to ds and r̂.",
                "Straight wire: the sum of slices → B = μ₀I/(2πr), ∝ I, ∝ 1/r.",
                "Loop center: B = μ₀I/(2R); N-turn coil: μ₀NI/(2R).",
                "Solenoid: uniform interior B = μ₀nI, n = N/L.",
                "Worked numbers: 10 A · 0.10 m → 2.0 × 10⁻⁵ T; 400 turns/0.20 m · 2 A → 5.0 × 10⁻³ T.",
            ],
            "common_mistake": "Applying the law to a whole wire at once; mixing N with n; confusing 1/r² with 1/r.",
            "check": "Double the distance from a wire and double the current — what happens to B?",
            "final_takeaway": "Every field is a sum of Biot–Savart slices: geometry picks the sum, and the wire, loop, and solenoid formulas are its three most famous answers.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "Nature Fights Back: Lenz's Law in Four Steps",
        "description": (
            "The two conditions for an induced current and the four-step "
            "direction recipe: is it changing, which way, oppose it, curl the "
            "right hand."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Direction of the induced current via Lenz's law",
            "target_student": "First-year university student",
            "objective": "State the closed-loop and changing-flux conditions and determine the induced-current direction for any changing flux scenario.",
            "hook": "Push a magnet toward a coil of wire and the coil fights you — repels. Pull it away and the coil holds on. Nothing touches anything: the coil generates its own current to resist you.",
            "explanation_steps": [
                "Two conditions: closed conducting loop AND changing flux — no change, no current.",
                "Step 1: is the flux changing? Static field → nothing happens.",
                "Step 2: which way — flux increasing or decreasing?",
                "Step 3: oppose the change — increasing → induced field against; decreasing → induced field with.",
                "Step 4: curl the right hand along the induced current, thumb = induced field.",
                "Worked demo: north pole approaching (north first) → loop repels, induced field southward, clockwise seen from the magnet.",
            ],
            "common_mistake": "Opposing the field rather than the change — a decaying field is SUPPORTED; a static magnet induces nothing at all.",
            "check": "A loop's field is increasing downward through it. Which way does the induced current circulate, seen from above?",
            "final_takeaway": "No change, no current; when flux changes the current opposes the change — push, repelled; pull, attracted. Nature resists, every time.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "List the four experimental observations established by Biot and Savart for the field contribution of a current element.",
        "options": [
            "dB ∝ I; dB ∝ ds; dB ∝ sin θ; dB ∝ 1/r²",
            "dB ∝ I²; dB ∝ ds²; dB ∝ cos θ; dB ∝ 1/r",
            "dB ∝ 1/I; dB ∝ r²; dB ∝ sin θ; dB ∝ ds",
            "dB ∝ I; dB ∝ 1/ds; dB ∝ θ; dB ∝ 1/r³",
        ],
        "correct_index": 0,
        "explanation": "The four observations: proportional to current I, to element length ds, to sin of the angle θ, and inversely to the square of the distance r².",
        "skill": "four Biot–Savart observations",
        "difficulty": 1,
        "competency_code": "magnetic-biot-savart",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What is μ₀, and what are its value and units?",
        "options": [
            "The magnetic permeability of free space; μ₀ = 4π × 10⁻⁷ T·m/A",
            "The Coulomb constant; μ₀ = 9 × 10⁹ N·m²/C²",
            "The electric permittivity; μ₀ = 8.85 × 10⁻¹² C²/(N·m²)",
            "A dimensionless constant; μ₀ = 1",
        ],
        "correct_index": 0,
        "explanation": "μ₀ = 4π × 10⁻⁷ T·m/A is the magnetic permeability of free space — the constant standing in front of every field-from-current formula.",
        "skill": "identify μ₀",
        "difficulty": 1,
        "competency_code": "magnetic-biot-savart",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Describe the field-line pattern around a long straight wire, and state the two proportionalities of B.",
        "options": [
            "Field lines CIRCLE the wire (right-hand thumb along current); B ∝ I and B ∝ 1/r",
            "Field lines radiate outward like a charge; B ∝ 1/I and B ∝ r²",
            "Field lines are straight and parallel to the wire; B is constant everywhere",
            "Field lines spiral along the wire; B ∝ r and B ∝ 1/I",
        ],
        "correct_index": 0,
        "explanation": "The right-hand rule wraps concentric circular field lines around the wire. Doubling the current doubles B; doubling the distance halves it (B ∝ I, B ∝ 1/r).",
        "skill": "wire field pattern and proportions",
        "difficulty": 1,
        "competency_code": "wire-field",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why is a current loop called 'a short bar magnet', and what does that analogy let you predict about a solenoid?",
        "options": [
            "Its field lines pass through the center and close outside, matching a short bar magnet — so a solenoid's poles can be named by its right-hand field direction",
            "A loop carries net magnetic charge like a bar magnet's poles",
            "The loop's field is uniform inside it, like iron between magnet poles",
            "The analogy only applies to straight wires, not loops",
        ],
        "correct_index": 0,
        "explanation": "The closed field-line pattern of a loop (through the center, wrapping outside) is the same map as a short bar magnet; curl your fingers along the current and the thumb names the field/pole direction.",
        "skill": "loop ↔ bar-magnet field pattern",
        "difficulty": 1,
        "competency_code": "loop-coil-field",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A long straight wire carries 10 A. Compute B at r = 0.10 m.",
        "options": [
            "B = (4π × 10⁻⁷)(10)/(2π)(0.10) = 2.0 × 10⁻⁵ T",
            "B = (4π × 10⁻⁷)(10)/(0.10)² = 4π × 10⁻⁵ T",
            "B = (4π × 10⁻⁷)(10)/(2)(0.10) = 6.3 × 10⁻⁵ T",
            "B = (4π × 10⁻⁷)(10)(0.10) = 1.3 × 10⁻⁶ T",
        ],
        "correct_index": 0,
        "explanation": "B = μ₀I/(2πr) = (4π × 10⁻⁷)(10)/(2π)(0.10) = 2.0 × 10⁻⁵ T. The 2πr in the denominator already encodes the circle geometry.",
        "skill": "straight-wire field computation",
        "difficulty": 2,
        "competency_code": "wire-field",
    },
    {
        "level": "APPLY",
        "prompt": "A circular loop of radius 5.0 cm carries 5.0 A. Find the field at its center.",
        "options": [
            "B = μ₀I/(2R) = (4π × 10⁻⁷)(5.0)/(2 × 0.050) ≈ 6.3 × 10⁻⁵ T",
            "B = μ₀I/(2πR) = (4π × 10⁻⁷)(5.0)/(2π × 0.050) ≈ 2.0 × 10⁻⁵ T",
            "B = μ₀I/(R) = (4π × 10⁻⁷)(5.0)/(0.050) ≈ 1.3 × 10⁻⁴ T",
            "B = μ₀IR² = (4π × 10⁻⁷)(5.0)(0.050)² ≈ 1.6 × 10⁻⁸ T",
        ],
        "correct_index": 0,
        "explanation": "Center of a loop: B = μ₀I/(2R) = (4π × 10⁻⁷)(5.0)/(0.10) ≈ 6.3 × 10⁻⁵ T. The straight-wire pattern (2πr in the denominator) is a different geometry.",
        "skill": "loop-center field",
        "difficulty": 2,
        "competency_code": "loop-coil-field",
    },
    {
        "level": "APPLY",
        "prompt": "A solenoid has 400 turns wound over 0.20 m and carries 2.0 A. Compute its interior field.",
        "options": [
            "n = 400/0.20 = 2000/m; B = (4π × 10⁻⁷)(2000)(2.0) ≈ 5.0 × 10⁻³ T",
            "n = 400; B = (4π × 10⁻⁷)(400)(2.0) ≈ 1.0 × 10⁻³ T",
            "n = 0.20/400; B = (4π × 10⁻⁷)(5 × 10⁻⁴)(2.0) ≈ 1.3 × 10⁻⁹ T",
            "B = (4π × 10⁻⁷)(400)/(0.20 × 2.0) ≈ 1.3 × 10⁻³ T",
        ],
        "correct_index": 0,
        "explanation": "n = N/L = 400/0.20 = 2000 turns/m, so B = μ₀nI = (4π × 10⁻⁷)(2000)(2.0) ≈ 5.0 × 10⁻³ T. Forgetting the N/L division gives wrong answer 2.",
        "skill": "solenoid field with n = N/L",
        "difficulty": 2,
        "competency_code": "solenoid-field",
    },
    {
        "level": "APPLY",
        "prompt": "An N = 50-turn coil, radius 0.10 m, carries 2.0 A. Find B at its center.",
        "options": [
            "B = μ₀NI/(2R) = (4π × 10⁻⁷)(50)(2.0)/(0.20) ≈ 6.3 × 10⁻⁴ T",
            "B = μ₀I/(2NR) = (4π × 10⁻⁷)(2.0)/(0.20 × 50) ≈ 2.5 × 10⁻⁷ T",
            "B = μ₀I/(2R) = (4π × 10⁻⁷)(2.0)/(0.20) ≈ 1.3 × 10⁻⁵ T",
            "B = μ₀NI/R = (4π × 10⁻⁷)(50)(2.0)/(0.10) ≈ 1.3 × 10⁻³ T",
        ],
        "correct_index": 0,
        "explanation": "B = μ₀NI/(2R) = (4π × 10⁻⁷)(50)(2.0)/(0.20) ≈ 6.3 × 10⁻⁴ T. Each turn adds its field, so N multiplies the single-loop value of 1.3 × 10⁻⁵ T.",
        "skill": "N-turn coil field",
        "difficulty": 2,
        "competency_code": "loop-coil-field",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Design a solenoid for a bacteria-magnetism experiment: target B = 2.0 × 10⁻⁴ T, winding length L = 0.10 m, current I = 1.0 A, wire radius r = 2.0 cm. Find n, N, and the wire length d.",
        "options": [
            "n = B/(μ₀I) ≈ 159/m; N = nL ≈ 16 turns; d = N·2πr ≈ 2.0 m",
            "n = μ₀I/B ≈ 6.3/m; N = 0.63; d = N·2πr ≈ 8 cm",
            "n = B·μ₀·I ≈ 2.5 × 10⁻¹⁰/m; N = 0.025; d ≈ 3 mm",
            "n = BL/(μ₀I) ≈ 16/m; N = n ≈ 1.6; d ≈ 0.2 m",
        ],
        "correct_index": 0,
        "explanation": "Climb the design chain: n = B/(μ₀I) = 2.0 × 10⁻⁴/(4π × 10⁻⁷ × 1.0) ≈ 159 turns/m; N = nL ≈ 16 turns; wire d = N·2πr = 16 × 2π × 0.020 ≈ 2.0 m.",
        "skill": "inverted solenoid design chain",
        "difficulty": 3,
        "competency_code": "solenoid-field",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two long parallel wires, 20 cm apart, carry 5.0 A and 8.0 A in the SAME direction. Where between them is the net field zero?",
        "options": [
            "d = 7.7 cm from the 5.0 A wire, where 5/d = 8/(0.20 − d)",
            "d = 12.3 cm from the 5.0 A wire, where the fields add",
            "At the midpoint, 10 cm from each",
            "No such point exists — same-direction fields can never cancel",
        ],
        "correct_index": 0,
        "explanation": "Same-direction currents give opposed fields between the wires. Set μ₀I₁/(2πd) = μ₀I₂/(2π(0.20−d)) → 5/d = 8/(0.20−d) → d = 7.7 cm from the weaker wire.",
        "skill": "two-wire field superposition",
        "difficulty": 3,
        "competency_code": "wire-field",
    },
    {
        "level": "TRANSFER",
        "prompt": "A closed loop sits in a magnetic field that begins to DECREASE smoothly. What happens — and which way does the induced field point?",
        "options": [
            "Induced current flows; the induced field points WITH the original field, resisting the decrease",
            "Induced current flows; the induced field points AGAINST the original field, opposing the field itself",
            "No induced current — a static magnet produces none",
            "Induced current flows only if the loop is a perfect conductor",
        ],
        "correct_index": 0,
        "explanation": "Decreasing flux satisfies Lenz's two conditions; opposing the CHANGE means the induced field SUPPORTS the original field, working to slow its fade. Answer 2 opposes the field, not the change.",
        "skill": "Lenz direction, decreasing-flux case",
        "difficulty": 3,
        "competency_code": "lenzs-law",
    },
    {
        "level": "TRANSFER",
        "prompt": "A closed conducting loop is held near a solenoid whose current is steadily INCREASING, so flux grows through the loop. Describe what appears in the loop and the direction rule that fixes its sense.",
        "options": [
            "An induced current flows; its field opposes the growth — pointing against the solenoid's field — found by asking change? which way? oppose it? then curling the right hand",
            "No current flows unless the loop touches the solenoid",
            "A steady current flows with the solenoid's field, aiding the growth",
            "A current flows only after the solenoid reaches full current",
        ],
        "correct_index": 0,
        "explanation": "Flux increasing → induced field points AGAINST the original; right-hand curl along the circulating induced current gives that sense. The two conditions (closed loop + changing flux) are both met, and Lenz aims the response against the change.",
        "skill": "Lenz transfer to a coupled circuit",
        "difficulty": 3,
        "competency_code": "lenzs-law",
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
        "code": "magnetic-fields",
        "title": "The Magnetic Field B",
        "taxonomy_level": "understand",
        "description": "Define B by the compass-north direction, describe field-line patterns, and convert between tesla and gauss.",
        "sort_order": 34,
    },
    {
        "code": "magnetic-biot-savart",
        "title": "The Biot–Savart Law",
        "taxonomy_level": "understand",
        "description": "State the four observations, interpret dB = (μ₀/4π) I ds sin θ / r², and identify μ₀ = 4π × 10⁻⁷ T·m/A.",
        "sort_order": 38,
    },
    {
        "code": "wire-field",
        "title": "Field of a Straight Current-Carrying Wire",
        "taxonomy_level": "apply",
        "description": "Compute B = μ₀I/(2πr) for a long straight wire, apply its proportionalities, and superpose fields from parallel wires.",
        "sort_order": 39,
    },
    {
        "code": "loop-coil-field",
        "title": "Fields of a Current Loop and N-Turn Coil",
        "taxonomy_level": "apply",
        "description": "Compute the center field B = μ₀I/(2R) of a loop and B = μ₀NI/(2R) of a coil, and use the short-bar-magnet field pattern.",
        "sort_order": 40,
    },
    {
        "code": "solenoid-field",
        "title": "Field of a Solenoid and Solenoid Design",
        "taxonomy_level": "apply",
        "description": "Compute the uniform interior field B = μ₀nI with n = N/L, and design a solenoid via n = B/(μ₀I), N = nL, d = N·2πr.",
        "sort_order": 41,
    },
    {
        "code": "lenzs-law",
        "title": "Lenz's Law",
        "taxonomy_level": "apply",
        "description": "State the closed-loop and changing-flux conditions and determine an induced current's direction by opposing the change.",
        "sort_order": 42,
    },
]

COMPETENCY_PREREQUISITES = [
    ("electric-current", "magnetic-biot-savart"),
    ("magnetic-fields", "magnetic-biot-savart"),
    ("magnetic-biot-savart", "wire-field"),
    ("magnetic-biot-savart", "loop-coil-field"),
    ("loop-coil-field", "solenoid-field"),
    ("magnetic-biot-savart", "lenzs-law"),
]

LESSON_COMPETENCIES = [
    {"code": "magnetic-biot-savart", "role": "teaches"},
    {"code": "wire-field", "role": "teaches"},
    {"code": "loop-coil-field", "role": "teaches"},
    {"code": "solenoid-field", "role": "teaches"},
    {"code": "lenzs-law", "role": "teaches"},
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

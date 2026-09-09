"""PHY211 — Physics, Module 4, Lecture 6: Electric Current, Resistance, Energy.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 6, Fall 2024 —
'Electric Current, Resistance, Ohm's Law, and Energy in Circuits').

The pivot from electrostatics to circuits. Imported by ``curriculum.content``
and seeded by ``curriculum.seed``.
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
    "code": "M4",
    "title": "Module 4 — Electric Current",
    "description": (
        "Chapter 5: current as flowing charge, the drift-speed picture "
        "(I = nev_dA), Ohm's law, resistance and resistivity, emf with internal "
        "resistance, and power in electric circuits."
    ),
    "sort_order": 4,
}

LESSON = {
    "code": "L6",
    "title": "Electric Current: The Energy Admin of Circuits",
    "description": (
        "Lecture 6 — the physics of current: how much charge flows, how SLOWLY "
        "the charges themselves move, why wires still deliver instantly, and how "
        "voltage, resistance, internal resistance, and power budget every circuit."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Define current I = Q/t (ampere = C/s) and distinguish conventional current from electron flow.",
        "Use the drift-speed picture J = I/A = nev_dA and explain why a lamp lights instantly though v_d is ~6 × 10⁻⁴ m/s.",
        "Apply Ohm's law V = IR and identify I as the current THROUGH the resistor, V the potential drop ACROSS it.",
        "Use R = ρL/A, explain resistivity vs resistance, and handle temperature: R_T = R₀(1 + αT).",
        "Model a real battery as emf in series with internal resistance: V = ℰ − Ir, and extract r from data.",
        "Compute electric power P = VI = V²/R = I²R and energy U = IVt, converting kWh ↔ joules.",
    ],
    "prerequisites": [
        "Electric potential and ΔV = −Ed (Lecture 4).",
        "Electric field and particle-motion reasoning (Lecture 3).",
        "Charge quantization and unit conversion (Lecture 1).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Current is charge on the move, but the surprise is how little of it you actually get "
            "by moving charge. In a typical wire the electrons crawl at fractions of a millimeter "
            "per second, yet a lamp lights the instant you flip the switch — because the wire was "
            "already FULL of charge, like a garden hose that is already full of water. This lecture "
            "quantifies that picture, then adds the three accounting tools every circuit needs: "
            "Ohm's law for the resistor, an internal resistance hiding inside every battery, and "
            "the power formulas that bill the energy."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Electric Current",
        "body": "I = Q / t   (unit: ampere = C/s)",
        "metadata": {
            "meaning": "How much charge passes a cross-section per second.",
            "when_used": "Every current calculation; extend to Q = N·e when counting charges.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Two Directions, One Convention",
        "body": "Conventional current flows + → − (the arrow in every diagram). In metals the actual movers are electrons, − → +, carrying the SAME amount of charge the other way. Same current number, opposite arrows.",
    },
    {
        "section_type": "FORMULA",
        "title": "Current as drift of charge",
        "body": "J = I / A = n·e·v_d    multiple by the wire:  I = n·e·v_d·A",
        "metadata": {
            "meaning": "n = number of free electrons per m³; e = 1.6 × 10⁻¹⁹ C; A = cross-section; v_d = drift speed (tiny!).",
            "when_used": "Converting between current and drift speed; the 'why is it instant?' question.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The slowness of drift speed",
        "body": (
            "A 1 A current in a copper wire of cross-section 1 mm²: v_d = I/(n e A) ≈ "
            "6 × 10⁻⁴ m/s — about 40 minutes to travel one meter. Yet the lamp lights "
            "instantly: the wire is already full of electrons, everywhere at once, all pushed "
            "into motion the moment the field is applied."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "The hose and the turnstile",
        "body": (
            "Two physical pictures: the garden hose already full of water (turn the tap, water "
            "comes out the end immediately — no need to wait for the tap end to arrive); and the "
            "stadium turnstile (each second, n fans per cubic meter pass the gate at speed v_d "
            "through area A). The gate IS the wire's cross-section; the fans are the cars "
            "(charge)."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Ohm's law",
        "body": "V = I·R   (unit: ohm = V/A)",
        "metadata": {
            "meaning": "For ohmic materials: proportional, V_A − V_B = I·R must be the DROP across the resistor.",
            "when_used": "The workhorse relation once drift physics is done; R is a geometry–material property.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Resistivity vs resistance",
        "body": "R = ρ·L / A   with  σ = 1/ρ   and  R_T = R₀(1 + αT)",
        "metadata": {
            "meaning": "ρ is the MATERIAL (Ω·m); R is the OBJECT (Ω) — shape transports material into size.",
            "when_used": "Resistance of a specific wire; temperature dependence of conductors.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Real Batteries Hide a Resistor",
        "body": (
            "A perfect battery keeps its voltage forever; the real internal chemistry surrenders "
            "some voltage the harder it is pushed. Model it as an idealized emf ℰ with a small "
            "resistor r inside, in series. The terminal voltage you measure is ℰ minus the drop "
            "across r: V = ℰ − Ir. Heavy load (large I) digs deeper into the hidden resistor — "
            "dim headlights at idle, all because r eats part of ℰ."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "emf and terminal voltage",
        "body": "V = ℰ − I·r   so   r = (ℰ − V) / I",
        "metadata": {
            "meaning": "ℰ = the no-load voltage; V = what the battery actually delivers under current I.",
            "when_used": "Any battery, flashlight to car, when load draws a current; r is the internal resistance.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The flashlight battery",
        "body": (
            "A 1.5 V flashlight battery drives 0.24 A while its terminals read 1.2 V. The 0.3 V "
            "gap is the internal drop: r = (ℰ − V)/I = 0.3/0.24 = 1.25 Ω. The battery looks like "
            "a 1.5 V source with a 1.25 Ω resistor glued inside."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Electric power and energy",
        "body": "P = VI = V²/R = I²R   and   U = I·V·t   (1 kWh = 3.6 × 10⁶ J)",
        "metadata": {
            "meaning": "Power is the energy-billing rate of the circuit; pick V²/R when voltage is fixed, I²R when current is fixed.",
            "when_used": "Heaters, bulbs, appliances, battery ratings; the kWh on your electricity bill.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The appliance power math",
        "body": (
            "A 120 V heater drawing 10 A: P = VI = 1,200 W (or I²R = 10² × 12 = 1,200 W, or "
            "V²/R = 120²/12 — same). Running 1 hour banks U = IVt = 1.2 kWh = 4.32 × 10⁶ J of "
            "heat."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — current from charge",
        "body": (
            "2.4 C of charge passes a point in 4 s: I = Q/t = 2.4/4 = 0.6 A. Counting electrons "
            "instead: N = Q/e = 1.5 × 10¹⁹ electrons. Amass the charge, divide by the time, "
            "count cars at the turnstile."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — drift speed in copper",
        "body": (
            "1 A through a 1 mm² copper wire. n ≈ 8.5 × 10²⁸ electrons/m³: "
            "v_d = I/(n e A) = 1/((8.5 × 10²⁸)(1.6 × 10⁻¹⁹)(10⁻⁶)) ≈ 7 × 10⁻⁵ m/s. Compare: "
            "electrons crawl millimeters-tens of minutes per meter; charge INSTANTLY everywhere."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — the flashlight's hidden resistor",
        "body": (
            "ℰ = 1.5 V, I = 0.24 A, terminals read 1.2 V. r = (ℰ − V)/I = 0.3/0.24 = 1.25 Ω. "
            "Loaded, the battery delivers 1.2 V; unloaded, all 1.5 V — the terminal gap is the "
            "internal drop Ir."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — resistance of a wire",
        "body": (
            "Copper (ρ = 1.72 × 10⁻⁸ Ω·m), L = 50 m, A = 1 mm²: R = ρL/A = (1.72 × 10⁻⁸)(50)/10⁻⁶ "
            "= 0.86 Ω. Heat it 100 °C with α = 3.9 × 10⁻³ /°C: R_T = R₀(1 + αΔT) = 0.86(1 + 0.39) "
            "≈ 1.20 Ω — resistance grows with temperature."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — power billing",
        "body": (
            "A 120 V heater at 10 A: P = VI = 1,200 W. One hour: U = IVt = 1200 Wh = 1.2 kWh = "
            "1.2 × 3.6 × 10⁶ J = 4.32 × 10⁶ J. The meter tracks kWh; the physics tracks joules."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Electrons flow the other way",
        "body": "Conventional current is + → −; electrons march − → + through the same wire. Same magnitude, opposite arrows — draw the conventional arrow and let the electrons do the opposite.",
    },
    {
        "section_type": "WARNING",
        "title": "Don't read v_d as the signal speed",
        "body": "v_d ≈ 6 × 10⁻⁴ m/s is the DRIFT speed. The push (the field) travels at light speed through the wire, which is why the lamp is instant while the charges crawl.",
    },
    {
        "section_type": "WARNING",
        "title": "V in Ohm's law is a DROP",
        "body": "V = IR means V_A − V_B, the potential drop across the resistor carried by current I. Not some absolute 'voltage of the resistor'."
    },
    {
        "section_type": "WARNING",
        "title": "Resistivity is not resistance",
        "body": "ρ is material-only (Ω·m); R = ρL/A is the object's response to its geometry. Double the length, double R; double the cross-section, halve R.",
    },
    {
        "section_type": "WARNING",
        "title": "The hidden r is AMONG the series",
        "body": "Every real battery is emf + r in series. Forget r and the terminal voltage comes out wrong exactly when the load is heaviest.",
    },
    {
        "section_type": "WARNING",
        "title": "Which power form?",
        "body": "P = VI always. P = V²/R steps on voltage being fixed; P = I²R on current being fixed. Pick by the variable the circuit holds constant.",
    },
    {
        "section_type": "WARNING",
        "title": "Amp is a rate, not a quantity",
        "body": "1 A is one coulomb PER SECOND. 'Amps stored in a battery' is a category error — batteries store charge (Ah), circuits carry current (A).",
    },
    {
        "section_type": "WARNING",
        "title": "kWh is energy, not power",
        "body": "kWh is a JOULE under a different name: 1 kWh = 3.6 × 10⁶ J. Watts are power (J/s); watt-hours are energy (J)."
    },
    {
        "section_type": "WARNING",
        "title": "Temperature ramps resistance",
        "body": "Conductors heat → resistance grows (R_T = R₀(1 + αT)); semiconductors go the OTHER way. The formula's sign expresses that with α."
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Turnstile at the Wire's Cross-Section",
        "body": (
            "I = nev_dA is the whole physics of current in one line. Picture the stadium "
            "turnstile: n fans per cubic meter moving at speed v_d, squeezed through an exit "
            "gate of area A — the fans per second ARE the current. The hose analogy fixes the "
            "conceptual bug: the lamp lights instantly because the wire was already packed "
            "with charge, not because anything moves fast. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "emf vs Terminal Voltage",
        "body": (
            "The battery isn't a perfect 1.5 V; it's a 1.5 V source saddled with internal "
            "resistance r. Under load, r eats Ir volts before the terminals, so V = ℰ − Ir. "
            "Same battery: 1.5 V on the shelf, 1.2 V pushing 0.24 A. Every 'why did the "
            "headlights dim?' puzzle is this one equation. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Choosing P = V²/R vs P = I²R",
        "body": (
            "Power formulas look interchangeable but the variable you DIDN'T pick becomes the "
            "constraint. Voltage fixed (wall outlet) → P = V²/R. Current fixed (series circuit) "
            "→ P = I²R. Ask which quantity the circuit holds still before substituting. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Resistivity is a Material, Resistance is a Shape",
        "body": (
            "Copper's ρ is the same in every wire; the wire's R changes with L and A. The "
            "formula R = ρL/A is a shape-transport that turns a material constant into a "
            "device property — and the temperature rule adds its own twist for conductors vs "
            "semiconductors. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Two Directions at Once (Conventional vs Electron Flow)",
        "body": (
            "Diagrams arrow + → −; actual metal carries electrons − → +. The charge moved is "
            "identical, the currents numerically equal — only the arrow flips. Mixing the two "
            "pictures mid-problem is the classic setup for a sign disaster. Difficulty: EASY."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• I = Q/t (A = C/s); electrons move − → + while conventional current flows + → −.\n"
            "• Drift picture: I = nev_dA; v_d ≈ 6 × 10⁻⁴ m/s but the wire is ALREADY full of charge — instant delivery.\n"
            "• Ohm's law V = IR; the drop ACROSS the resistor equals current times resistance.\n"
            "• R = ρL/A: ρ is the material, R is the object; R_T = R₀(1 + αT).\n"
            "• Batteries are emf + r in series: V = ℰ − Ir, r = (ℰ − V)/I.\n"
            "• P = VI = V²/R = I²R; U = IVt; 1 kWh = 3.6 × 10⁶ J."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Current (I) — charge flow rate, C/s (ampere).\n"
            "• Drift speed (v_d) — the slow net speed of charges under the field.\n"
            "• Ohm (Ω) — the resistance that lets 1 A through for 1 V of drop.\n"
            "• Resistivity (ρ) — material property (Ω·m); conductance σ = 1/ρ.\n"
            "• emf (ℰ) — the battery's no-load voltage; terminal V = ℰ − Ir underneath.\n"
            "• Internal resistance (r) — the hidden resistor every real battery carries.\n"
            "• Watt / kilowatt-hour — J/s of power; 3.6 × 10⁶ J of energy."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• I = Q/t — current; Q = Ne.\n"
            "• J = I/A = nev_d — current density; I = nev_dA.\n"
            "• V = IR — Ohm's law.\n"
            "• R = ρL/A — resistance from resistivity and shape.\n"
            "• R_T = R₀(1 + αT) — temperature dependence.\n"
            "• V = ℰ − Ir — terminal voltage with internal resistance.\n"
            "• P = VI = V²/R = I²R; U = IVt.\n"
            "• 1 kWh = 3.6 × 10⁶ J."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Current is the charge rate through a wire, carried by electrons that drift at "
            "fractions of millimeters per second — but the push travels at light speed through "
            "charge already everywhere in the wire. I = nev_dA is the whole drift picture in "
            "one line. Ohm's law V = IR ties the drop to the current, and R = ρL/A turns a "
            "material constant into an object property. Real batteries hide an internal "
            "resistor: V = ℰ − Ir, so heavy loads dig into the terminals. Power is the billing "
            "rate P = VI = V²/R = I²R, with U = IVt and 1 kWh = 3.6 × 10⁶ J. Question the "
            "geometry, question the hidden resistor, and the formula choice falls out of what "
            "the circuit holds fixed."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Turnstile Inside a Wire: Where Current Really Comes From",
        "description": (
            "Why a lamp lights instantly even though the charges themselves drifts at a "
            "fraction of a millimeter per second: the wire was already full of charge, and "
            "I = nev_dA is the turnstile counting it."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Drift speed and the current-density picture I = nev_dA; instantaneous vs slow",
            "target_student": "First-year university student",
            "objective": "Compute v_d from I, n, e, A and explain why delivery is instant despite v_d ≈ 6 × 10⁻⁴ m/s.",
            "hook": "Electrons drift at millimeters per MINUTE — yet flip the switch and the lamp is on in microseconds. How can the wire deliver what its charges barely carry?",
            "explanation_steps": [
                "Define current as charge per second through a cross-section.",
                "The stadium-turnstile picture: n fans/m³, speed v_d, gate area A ⇒ I = nev_dA.",
                "Worked number: 1 A in a 1 mm² copper wire ⇒ v_d ≈ 6 × 10⁻⁴ m/s (40 min per meter).",
                "Contrast drift speed with the field push, which travels at light speed.",
                "The garden-hose analogy: a hose already full of water delivers instantly.",
                "Resolve the paradox: full wire + instant push = instant light, slow charges.",
                "Sanity check: larger current ⇒ faster drift, but never 'fast'."
            ],
            "common_mistake": "Reading v_d as the signal speed; imaging charges sprinting around the circuit; believing the lamp waits for a tap-end 'first charge'.",
            "check": "Roughly how fast do electrons drift in a 1 A, 1 mm² copper wire, and why is the lamp still instant?",
            "final_takeaway": "The wire is packed with charge; the field pushes all of it at once. I = nev_dA counts the slow drift, but delivery is instant.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Hidden Resistor Inside Your Battery",
        "description": (
            "emf vs terminal voltage: why a 1.5 V battery delivers only 1.2 V under load, the "
            "internal-resistance model V = ℰ − Ir, and extracting r from data."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "emf, internal resistance, terminal voltage V = ℰ − Ir",
            "target_student": "First-year university student",
            "objective": "Explain why terminal voltage drops under load, model the battery as emf + r in series, and compute r = (ℰ − V)/I from data.",
            "hook": "Shelf voltage 1.5 V, headlight voltage 1.2 V. The battery didn't weaken — a resistor you never see is eating the difference.",
            "explanation_steps": [
                "Define emf ℰ: the battery's no-load, chemistry-measured voltage.",
                "Real battery = ideal source + hidden series resistor r.",
                "Terminal voltage V = ℰ − Ir: the bigger the load current, the deeper the internal drop.",
                "Worked example: flashlight 1.5 V, 0.24 A, terminals 1.2 V ⇒ r = 1.25 Ω.",
                "Visual: dimming headlights at idle; voltage sag is real data, not magic.",
                "When to distrust V = ℰ: heavy loads, weak cells, loaded measurements.",
                "Sanity check: r must come out positive; r > 0 for every real cell."
            ],
            "common_mistake": "Reading the loaded terminal voltage as the battery's emf; forgetting the internal drop on heavy loads; confusing r with the load resistance.",
            "check": "A 1.5 V battery delivering 0.24 A at 1.2 V terminals — find r. What does the terminal read with almost no load?",
            "final_takeaway": "Every battery hides a resistor: V = ℰ − Ir. Terminal voltage falls under load exactly by the internal drop.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "Define electric current, state its unit, and describe the direction of conventional current versus real electron flow in a metal wire.",
        "options": [
            "I = Q/t, ampere = C/s; conventional current flows + → −, while electrons flow − → + with the same magnitude",
            "I = Q·t, ampere = C·s; both conventional and electron flow are + → −",
            "I = Q/t, ampere = C/s; electrons and conventional current both flow − → +",
            "I = V/R, ampere = V/Ω; electrons flow + → −",
        ],
        "correct_index": 0,
        "explanation": "Current is charge rate I = Q/t in amperes (C/s). Diagrams use the conventional arrow + → −; the actual charge carriers in metals are electrons moving − → +.",
        "skill": "current definition and direction",
        "difficulty": 1,
        "competency_code": "electric-current",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Explaining the instantly-lit lamp: electrons drift at ~6×10⁻⁴ m/s, yet the light turns on in microseconds. Why?",
        "options": [
            "The wire is already full of charge; the field push travels near light speed and sets ALL the charge moving at once",
            "Electrons accelerate to near light speed inside the copper",
            "The lamp is actually powered by the electric potential alone with no moving charge",
            "Heat from earlier current lights the filament faster",
        ],
        "correct_index": 0,
        "explanation": "Drift speed is tiny, but the wire was packed with mobile charge. The electric field inside the wire establishes almost instantly, pushing the whole existing sea of electrons — delivery isn't limited by how fast any single charge travels.",
        "skill": "drift speed vs signal speed",
        "difficulty": 2,
        "competency_code": "drift-current",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "A flashlight battery is rated 1.5 V but its terminals read 1.2 V while it drives 0.24 A. What does the 0.3 V gap represent?",
        "options": [
            "The internal drop Ir across the battery's hidden internal resistance r = (ℰ − V)/I = 1.25 Ω",
            "A measurement error — terminals must always read ℰ",
            "The battery is producing +0.3 V of extra energy",
            "The load's own resistance contribution of 0.3 Ω",
        ],
        "correct_index": 0,
        "explanation": "Under load the battery is emf ℰ with internal resistance r; the terminal gap ℰ − V = Ir = 0.3 V is consumed inside the battery itself. r = 0.3/0.24 = 1.25 Ω.",
        "skill": "emf vs terminal voltage",
        "difficulty": 2,
        "competency_code": "emf-internal-resistance",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State Ohm's law and identify the exact two variables it connects.",
        "options": [
            "V = IR: the potential DROP across the resistor (V_A − V_B) and the current THROUGH it, for ohmic materials",
            "V = IR: the 'voltage owned by the resistor' and the current in any material regardless",
            "I = VR: the current and the battery's emf, always",
            "P = IV and the energy per charge, always independent of material",
        ],
        "correct_index": 0,
        "explanation": "V = IR is a statement about a resistor: current through it times its resistance equals the drop from one end to the other (V_A − V_B). The proportionality is only for ohmic materials.",
        "skill": "Ohm's law meaning",
        "difficulty": 1,
        "competency_code": "ohms-law",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "2.4 C of charge passes a point in 4 s. Find the current, and the number of electrons that crossed.",
        "options": [
            "I = 0.6 A; N = Q/e = 2.4/(1.6 × 10⁻¹⁹) = 1.5 × 10¹⁹ electrons",
            "I = 9.6 A; N = 1.5 × 10¹⁹ electrons",
            "I = 0.6 A; N = 2.4 × 10¹⁹ electrons",
            "I = 0.6 A; N = 1.5 × 10¹⁹ C per electron",
        ],
        "correct_index": 0,
        "explanation": "I = Q/t = 2.4/4 = 0.6 A. Each electron carries e = 1.6 × 10⁻¹⁹ C, so N = Q/e = 1.5 × 10¹⁹ carriers.",
        "skill": "current from charge",
        "difficulty": 1,
        "competency_code": "electric-current",
    },
    {
        "level": "APPLY",
        "prompt": "A 1 A current flows in a 1 mm² copper wire (n ≈ 8.5 × 10²⁸ electrons/m³). Compute the drift speed.",
        "options": [
            "v_d = I/(n e A) ≈ 7 × 10⁻⁵ m/s — orders of magnitude slower than a snail",
            "v_d = I·n·e·A ≈ 1.4 × 10⁴ m/s — near the field speed",
            "v_d = I·A/(n e) ≈ 7 × 10⁻⁵ m/s — same magnitude",
            "v_d = e·A/(n I) ≈ 10⁻⁴² m/s",
        ],
        "correct_index": 0,
        "explanation": "v_d = I/(n e A) = 1/((8.5 × 10²⁸)(1.6 × 10⁻¹⁹)(10⁻⁶)) ≈ 7 × 10⁻⁵ m/s. The wire is full of carriers; a whole-meter journey takes minutes, yet the push is instant.",
        "skill": "drift-speed computation",
        "difficulty": 2,
        "competency_code": "drift-current",
    },
    {
        "level": "APPLY",
        "prompt": "A 1.5 V flashlight battery drives 0.24 A while its terminals read 1.2 V. Find the internal resistance.",
        "options": [
            "r = (ℰ − V)/I = 0.3/0.24 = 1.25 Ω",
            "r = V/I = 5 Ω — the terminals fully account for the emf",
            "r = ℰ/I = 6.25 Ω",
            "r = (ℰ − V)·I = 0.072 Ω",
        ],
        "correct_index": 0,
        "explanation": "The 0.3 V gap is the internal drop Ir, so r = (ℰ − V)/I = 0.3/0.24 = 1.25 Ω. The battery behaves like a 1.5 V source in series with 1.25 Ω.",
        "skill": "extracting internal resistance",
        "difficulty": 2,
        "competency_code": "emf-internal-resistance",
    },
    {
        "level": "APPLY",
        "prompt": "A 50 m copper wire (ρ = 1.72 × 10⁻⁸ Ω·m) has cross-section 1 mm². Find R, then its value at 100 °C above room temperature (α = 3.9 × 10⁻³ /°C).",
        "options": [
            "R = 0.86 Ω; R_T = 0.86(1 + 0.39) ≈ 1.20 Ω",
            "R = 0.86 Ω; R_T = 0.86/(1 + 0.39) ≈ 0.62 Ω",
            "R = 86 Ω; R_T = 120 Ω",
            "R = 0.86 Ω; temperature does not affect conductors",
        ],
        "correct_index": 0,
        "explanation": "R = ρL/A = (1.72 × 10⁻⁸)(50)/(10⁻⁶) = 0.86 Ω. R_T = R₀(1 + αΔT) = 0.86(1 + 3.9 × 10⁻³ × 100) ≈ 0.86(1.39) ≈ 1.20 Ω — conductors grow more resistive when hot.",
        "skill": "resistance from resistivity + temperature",
        "difficulty": 2,
        "competency_code": "resistance-resistivity",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "A 120 V heater draws 10 A. Compute P and the energy delivered in 1 hour in both joules and kWh.",
        "options": [
            "P = VI = 1,200 W; U = IVt = 1.2 kWh = 4.32 × 10⁶ J",
            "P = VI = 1,200 W; U = 1.2 kWh = 1.2 × 10³ J",
            "P = V²/R = 1,200 W; U = 1.2 × 10⁶ J = 0.33 kWh",
            "P = 120 W; U = 120 Wh = 432,000 J",
        ],
        "correct_index": 0,
        "explanation": "P = VI = 120 × 10 = 1,200 W = 1.2 kW. In 1 h: U = IVt = 1.2 kWh = 1.2 × 3.6 × 10⁶ J = 4.32 × 10⁶ J. kWh is just a 3.6 × 10⁶ J wrapper.",
        "skill": "power and energy billing",
        "difficulty": 2,
        "competency_code": "electric-power",
    },
    {
        "level": "TRANSFER",
        "prompt": "A student claims 'R = V/I, so a higher voltage resistor is a higher resistance — measuring V²/R gives a different resistance.' Find every error.",
        "options": [
            "R is a geometry–material property (R = ρL/A); V/I just MEASURES it and V²/R by definition equals VI (power). Resistance never changes with applied voltage for ohmic materials",
            "R = V/I means resistance DOES change with voltage; V²/R is a second resistance",
            "Higher voltage always means higher resistance, so resistance is not a property",
            "V²/R is capacitance; R = V/I is resistance; they should be equal only in vacuum",
        ],
        "correct_index": 0,
        "explanation": "R is fixed by geometry and material for ohmic conductors; the measurement V/I returns that same constant. And V²/R = (V/R)·V = I·V = P — a power, not a different resistance.",
        "skill": "resistance as invariant property; formula taxonomy",
        "difficulty": 3,
        "competency_code": "ohms-law",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two wires of the same material carry the same current. Wire 2 has twice the length and twice the cross-section of Wire 1. Compare their resistances and the power dissipated in each.",
        "options": [
            "R₂ = R₁ because ρ(2L)/(2A) = ρL/A; for equal current, P₁ = P₂ (both I²R)",
            "R₂ = 2R₁ (length doubles it); P₂ = 2P₁",
            "R₂ = ½R₁ (area doubles it); P₂ = ½P₁",
            "R₂ = 4R₁; P₂ = 4P₁",
        ],
        "correct_index": 0,
        "explanation": "R = ρL/A scales linearly in length and inversely in area: doubling both leaves R unchanged. With equal current, P = I²R gives equal dissipation — a clean 'shape cancels' transfer.",
        "skill": "geometry scaling of resistance and power",
        "difficulty": 3,
        "competency_code": "resistance-resistivity",
    },
    {
        "level": "TRANSFER",
        "prompt": "A 12 V truck battery (ℰ = 12.6 V, r = 0.05 Ω) powers a starter drawing 80 A. Compute the terminal voltage and the power lost inside the battery.",
        "options": [
            "V = 12.6 − 80(0.05) = 8.6 V; P_internal = I²r = 80² × 0.05 = 320 W — a real load on the battery",
            "V = 12.6 V; P_internal = 0 — emf never sags",
            "V = 12.6 − 0.05/80 ≈ 12.6 V; P_internal ≈ 63 W",
            "V = 12.6 + 4 = 16.6 V; P_internal = 320 W",
        ],
        "correct_index": 0,
        "explanation": "Terminal V = ℰ − Ir = 12.6 − 80 × 0.05 = 8.6 V — the 4 V internal drop at kick-in explains dim headlights. Internal loss P = I²r = 6400 × 0.05 = 320 W, heat inside the cell.",
        "skill": "terminal sag and internal power under heavy load",
        "difficulty": 3,
        "competency_code": "emf-internal-resistance",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "electric-potential",
        "title": "Electric Potential",
        "taxonomy_level": "understand",
        "description": "Compute point-charge potential V = KQ/r, use ΔV = −Ed, and apply the high→low field rule.",
        "sort_order": 14,
    },
    {
        "code": "electric-current",
        "title": "Electric Current",
        "taxonomy_level": "understand",
        "description": "Define current I = Q/t (ampere), count charges via Q = Ne, and distinguish conventional current from electron flow.",
        "sort_order": 21,
    },
    {
        "code": "drift-current",
        "title": "Drift Velocity and Current Density",
        "taxonomy_level": "apply",
        "description": "Compute drift speed v_d = I/(neA) and apply the turnstile picture J = I/A = nev_d.",
        "sort_order": 22,
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
        "code": "emf-internal-resistance",
        "title": "Electromotive Force and Internal Resistance",
        "taxonomy_level": "apply",
        "description": "Model real batteries as emf in series with internal resistance: V = ℰ − Ir and r = (ℰ − V)/I.",
        "sort_order": 25,
    },
    {
        "code": "electric-power",
        "title": "Electric Power and Energy",
        "taxonomy_level": "apply",
        "description": "Compute P = VI = V²/R = I²R and energy U = IVt, converting kWh to joules.",
        "sort_order": 26,
    },
]

COMPETENCY_PREREQUISITES = [
    ("electric-potential", "electric-current"),
    ("electric-current", "drift-current"),
    ("electric-current", "ohms-law"),
    ("ohms-law", "resistance-resistivity"),
    ("ohms-law", "emf-internal-resistance"),
    ("ohms-law", "electric-power"),
]

LESSON_COMPETENCIES = [
    {"code": "electric-current", "role": "teaches"},
    {"code": "drift-current", "role": "teaches"},
    {"code": "ohms-law", "role": "teaches"},
    {"code": "resistance-resistivity", "role": "teaches"},
    {"code": "emf-internal-resistance", "role": "teaches"},
    {"code": "electric-power", "role": "teaches"},
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

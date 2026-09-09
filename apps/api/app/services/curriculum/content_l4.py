"""PHY211 — Physics, Module 2, Lecture 4: Electric Flux, Gauss's Law & Potential.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lectures 4, Fall 2024 — 'Electric
Flux, Gauss's Law, Electric Potential and Energy').

This is the single lesson of Module 2 (Chapters 2 and 3). Imported by
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
    "code": "M2",
    "title": "Module 2 — Electric Flux, Gauss's Law & Electric Potential",
    "description": (
        "Chapters 2–3: flux through surfaces, Gauss's law and enclosed charge, "
        "electric potential as scalar field, potential difference, and the "
        "energy bookkeeping of charges moving through potential."
    ),
    "sort_order": 2,
}

LESSON = {
    "code": "L4",
    "title": "Electric Flux, Gauss's Law, and Electric Potential",
    "description": (
        "Lecture 4 — the two complementary tools of electrostatics: Gauss's law, "
        "which counts enclosed charge through closed surfaces, and electric "
        "potential, the scalar field whose differences drive charges and store "
        "their energy."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Define electric flux Φ = EA cosθ, state its unit (N·m²/C), and identify when it is maximal and when it is zero.",
        "State Gauss's law Φ = q_in/ε₀ and explain why external charges contribute nothing to the net flux.",
        "Compute net flux for a given set of enclosed charges, reading the sign as inward or outward.",
        "Define electric potential V = KQ/r as a scalar, and describe its sign near negative charges.",
        "Use ΔV = V_B − V_A = −Ed in a uniform field and the rule that field lines run high → low potential.",
        "Compute the change in potential energy ΔU = qΔV for positive and NEGATIVE charges crossing a potential difference.",
        "Compute the work done by the field W = −ΔU and the final speed from ½mv² = |ΔU|, including the electron vs proton contrast.",
        "State the four properties of equipotential lines, including why no work is done moving along one.",
    ],
    "prerequisites": [
        "Electric field E = F/q₀ and E = KQ/r² with direction rules (Lecture 3).",
        "Charge signs and the elementary charge (Lecture 1).",
        "Vector and scalar addition; work–kinetic-energy ideas.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Two tools complete the electric-force story. Gauss's law asks what is hidden inside "
            "a closed surface and answers with count-only bookkeeping: enclosed charge, epsilon "
            "naught, done. Electric potential answers a different question — what energy does a "
            "charge gain or lose crossing a potential difference — and it turns charged-particle "
            "motion into a ledger of joules and volts."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Electric flux",
        "body": "Φ = E·A = EA cosθ   (unit: N·m²/C)",
        "metadata": {
            "meaning": "A measure of how many field lines penetrate the surface of area A.",
            "when_used": "Open or closed surfaces in a uniform field; θ is the angle between the field and the surface NORMAL.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "The normal-angle trap",
        "body": "θ is measured from the NORMAL, not the surface. A surface tilted 30° relative to the field is at θ = 60° to the normal — use cos 60°, not cos 30°. Flux is max at θ = 0 (surface face-on), zero at θ = 90° (surface parallel to the field).",
    },
    {
        "section_type": "EXAMPLE",
        "title": "Flux through a rectangle",
        "body": (
            "A 0.16 m × 0.38 m rectangle sits face-on in a uniform 580 N/C field: "
            "A = 0.16 × 0.38 = 0.0608 m², Φ = EA cos0° = (580)(0.0608) = 35.264 N·m²/C. "
            "Tilt the rectangle so its face is parallel to the field and the flux drops to zero."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Gauss's law",
        "body": "Φ_net = q_in / ε₀   with   ε₀ = 8.85 × 10⁻¹² C²/(N·m²)",
        "metadata": {
            "meaning": "Net flux through ANY closed surface depends only on the net charge enclosed.",
            "when_used": "Finding flux from enclosed charge (or charge from flux).",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Circle, add, divide",
        "body": "Enclose the charges, add them with signs, divide by ε₀. External charges contribute zero (their lines enter and leave in canceling pairs); shape and size of the surface are irrelevant; negative net flux means net INWARD.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "Gauss with ten charges",
        "body": (
            "Ten charges: +2 μC at positions 1, 3, 8, 9 and −2 μC at 2, 4, 5, 6, 7, 10. "
            "Surface S₁ encloses positions 1,2,3,4,5,7,10: (+2)+(−2)+(+2)+(−2)+(−2)+(−2)+(−2) "
            "= −6 μC ⇒ Φ = −6 × 10⁻⁶/ε₀ (inward). S₂ encloses 4,5,6,10: −8 μC ⇒ −8 × 10⁻⁶/ε₀. "
            "S₃ encloses 7,8,9,10: everything cancels ⇒ Φ = 0. No field lines drawn, no shapes "
            "considered — circle, add, divide."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Electric Potential: A Scalar Field",
        "body": (
            "The potential at a point is the work done to bring a unit positive charge there "
            "from infinity. It is a SCALAR — add signed numbers, no vectors. For a point charge "
            "V = KQ/r: positive near a positive charge, negative near a negative charge. "
            "Superposition is just arithmetic with signs."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Potential of a point charge",
        "body": "V = KQ / r   (scalar)",
        "metadata": {
            "meaning": "Signed potential at distance r from charge Q.",
            "when_used": "Adding potentials from several charges, or finding V at a point.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Signed scalar superposition",
        "body": (
            "q₁ = +6 μC is 0.3 m from point P; q₂ = −6 μC is 0.9 m from P. "
            "V = (9 × 10⁹)[6 × 10⁻⁶/0.3 + (−6 × 10⁻⁶)/0.9] = 9 × 10⁹ × 6 × 10⁻⁶ (3.333 − 1.111) "
            "= 1.2 × 10⁵ V. Sign matters, geometry matters, vectors do not."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Field, Potential, and Potential Difference",
        "body": (
            "Field lines run from high potential to low potential. In a uniform field E pointing "
            "from A to B, the potential drops with the field: ΔV = V_B − V_A = −Ed. The field "
            "always points 'downhill' in potential — which is why a positive charge, pushed "
            "along the field, loses potential energy."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Uniform-field potential difference",
        "body": "ΔV = V_B − V_A = −Ed",
        "metadata": {
            "meaning": "Moving distance d along (not against) the field lowers potential by E·d.",
            "when_used": "Parallel-plate and other uniform-field problems; the source of the electron TV-tube example.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Energy change across a potential difference",
        "body": "ΔU = qΔV   (" "W_field = −ΔU, ΔK = −ΔU" ")",
        "metadata": {
            "meaning": "The sign of q is the master switch: a negative charge climbing to higher V LOSES potential energy.",
            "when_used": "Every energy question about charges moving between potentials.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "The electron's backwards climb",
        "body": "Positive charges pay to climb to high V. Electrons flip the story: moving to higher V gives (−)(+) = −ΔU, so the electron gains kinetic energy — a marble sprinting uphill. Compute the signs; never 'feel' them.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "The TV-tube electron vs proton",
        "body": (
            "Electron accelerated from rest through 5000 V: ΔU = (−1.6 × 10⁻¹⁹)(5000) = "
            "−8 × 10⁻¹⁶ J; ½mₑv² = 8 × 10⁻¹⁶ ⇒ v = 4.19 × 10⁶ m/s. Proton through −5000 V: "
            "ΔU = (+e)(−5000) = −8 × 10⁻¹⁶ J — same energy payout; ½m_p v² ⇒ v = 9.79 × 10⁵ m/s. "
            "Same energy, different mass, different speed."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Equipotential Lines",
        "body": (
            "Equipotential lines connect points of equal potential. Four properties: (1) field "
            "lines point from high to low potential; (2) field lines are perpendicular to "
            "equipotentials; (3) there is no field component ALONG an equipotential; (4) no "
            "work is done moving a charge along one (ΔV = 0 ⇒ W = qΔV = 0)."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Potential energy of a charge pair",
        "body": "U = Kq₁q₂ / r",
        "metadata": {
            "meaning": "Signed energy of a pair — negative for an attractive pair (opposite signs).",
            "when_used": "Two-charge and multi-charge systems: U = Σ Kqᵢqⱼ/rᵢⱼ.",
        },
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — flux and tilt",
        "body": (
            "A flat surface of area 0.5 m² in a uniform 400 N/C field: face-on ⇒ Φ = "
            "(400)(0.5) = 200 N·m²/C; tilted 60° to the field ⇒ θ = 30° ⇒ Φ = 200 cos30° "
            "≈ 173.2 N·m²/C; parallel to the field (θ = 90°) ⇒ Φ = 0."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — Gauss computation",
        "body": (
            "A closed surface encloses +3 μC and −1 μC: q_in = +2 μC ⇒ Φ = 2 × 10⁻⁶/8.85 × 10⁻¹² "
            "≈ 2.26 × 10⁵ N·m²/C, outward (positive). One number, one sign, no geometry."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — point-charge potential",
        "body": (
            "V at 0.2 m from a +5 μC charge: V = KQ/r = (9 × 10⁹)(5 × 10⁻⁶)/0.2 = 2.25 × 10⁵ V. "
            "Move to 0.4 m and V halves — the potential decays as 1/r, not 1/r²."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — the energy ledger across 100 V",
        "body": (
            "Electron accelerated from rest through 100 V: ΔU = (−1.6 × 10⁻¹⁹)(100) = "
            "−1.6 × 10⁻¹⁷ J. ½mₑv² = 1.6 × 10⁻¹⁷ ⇒ v² = 3.2 × 10⁻¹⁷/9.1 × 10⁻³¹ = 3.5 × 10¹³ "
            "⇒ v ≈ 5.9 × 10⁶ m/s. From a hundred volts, a tube-era workhorse."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — system potential energy",
        "body": (
            "q₁ = +3 μC, q₂ = −5 μC separated by 0.4 m: U = Kq₁q₂/r = (9 × 10⁹)(3 × 10⁻⁶)"
            "(−5 × 10⁻⁶)/0.4 = −0.3375 J. Negative — an attractive pair that would prefer to "
            "fall together."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Measuring θ from the surface, not the normal",
        "body": "θ in Φ = EA cosθ is measured from the NORMAL. A surface 30° from the field uses cos 60°. This is the single most common flux error.",
    },
    {
        "section_type": "WARNING",
        "title": "Including EXTERNAL charges in q_in",
        "body": "A +50 μC monster beside your surface contributes nothing — its lines enter and leave in canceling pairs. Circle only what is actually inside.",
    },
    {
        "section_type": "WARNING",
        "title": "A bigger/rounder surface catches more flux",
        "body": "No. Gauss's law depends only on ENCLOSED charge. Any shape, any size: same q_in gives the same net flux.",
    },
    {
        "section_type": "WARNING",
        "title": "Zero flux = zero field",
        "body": "Zero net flux means zero net ENCLOSED charge, not a field-free surface. Lines can be busy entering and leaving while the ledger reads zero.",
    },
    {
        "section_type": "WARNING",
        "title": "Dropping the sign of the flux",
        "body": "Negative net flux means net INWARD. The sign carries physical meaning — report it.",
    },
    {
        "section_type": "WARNING",
        "title": "Positive-charge intuition for electrons",
        "body": "ΔU = qΔV multiplies TWO signs. An electron moving to higher V has ΔU < 0 and gains speed. Never decide the energy story without computing q × ΔV.",
    },
    {
        "section_type": "WARNING",
        "title": "Work = +ΔU",
        "body": "The field's work is the WITHDRAWAL from the potential account: W = −ΔU. Same sign as ΔU means double-counted.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Gauss's Law: The Bag That Counts Charge",
        "body": (
            "Close any surface into a bag and run a ledger on crossings: outgoing lines +1, "
            "incoming −1. Outside charges dip in and come back out — net zero, always, any "
            "shape. Only the charge inside starts lines that must exit (or enter), so Φ = q_in/ε₀. "
            "Analogy: a sealed bag; the lines crossing it tell you what's inside without "
            "peeking. Same enclosed charge, same flux — sphere, potato, or crumpled paper. "
            "Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Energy Ledger: ΔU = qΔV and the Negative q Flip",
        "body": (
            "Potential difference is an electrical height. ΔU = qΔV multiplies two signs, making "
            "the sign of the charge a master switch: positive charges pay to climb (ΔU > 0); "
            "electrons get PAID to climb (ΔU < 0). The field's work is the withdrawal W = −ΔU; "
            "from rest every joule lost becomes speed: ½mv² = |ΔU|. Analogy: a bank ledger — "
            "every joule leaving the potential account appears as kinetic 'cash'. Sign first, "
            "magnitude second, mass last. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Normal-Angle Trap in Flux",
        "body": (
            "θ in Φ = EA cosθ is the angle between the field and the surface NORMAL — not the "
            "surface itself. A square tilted 30° to the field is at θ = 60° to the normal. "
            "Anchor it with the extremes: face-on (θ = 0) is maximum flux; edge-on (θ = 90°) is "
            "zero. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Potential as a Scalar: Signs Add, Vectors Don't",
        "body": (
            "V = KQ/r carries the charge's sign and adds as plain arithmetic. String several "
            "charges together and the potential is a signed sum — no geometry beyond distances. "
            "This is both simpler than the field and easy to under-trust: students expect "
            "cancellation rules from vectors that simply do not apply. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Same Voltage, Different Speeds",
        "body": (
            "Same |ΔU| in a given tube, but ½mv² = |ΔU| divides by mass. Electron and proton "
            "through 5000 V: identical energy payout, speeds that differ by the mass factor "
            "(≈ 4.28 for this example). Voltage buys energy, never speed directly. "
            "Difficulty: MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Flux: Φ = EA cosθ, N·m²/C; θ from the NORMAL; max at 0°, zero at 90°.\n"
            "• Gauss: Φ = q_in/ε₀ for ANY closed surface; external charges contribute zero.\n"
            "• Negative flux = net inward; zero flux = zero net enclosed charge.\n"
            "• Potential V = KQ/r is scalar; negative near negative charges.\n"
            "• Uniform field: ΔV = V_B − V_A = −Ed; field runs high → low potential.\n"
            "• Energy: ΔU = qΔV — the sign of q is the master switch.\n"
            "• W_field = −ΔU; from rest ½mv² = |ΔU| — same voltage, same energy, lighter particle faster.\n"
            "• Equipotentials: field ⊥ them, no component along them, W = 0 along them."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Electric flux (Φ) — EA cosθ, a measure of field lines through a surface.\n"
            "• Gauss's law — Φ = q_in/ε₀ for any closed surface.\n"
            "• Electric potential (V) — work per unit positive charge from infinity; a scalar.\n"
            "• Potential difference (ΔV) — electrical height between two points, in volts.\n"
            "• Equipotential line — a locus of constant potential.\n"
            "• Potential energy of a pair — U = Kq₁q₂/r."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• Φ = EA cosθ — flux through an open surface.\n"
            "• Φ = q_in/ε₀ — Gauss's law.\n"
            "• V = KQ/r — point-charge potential.\n"
            "• ΔV = V_B − V_A = −Ed — uniform-field potential difference.\n"
            "• ΔU = qΔV — energy across a potential difference.\n"
            "• W_field = −ΔU — work by the field.\n"
            "• ½mv² = |ΔU| — speed gained from rest.\n"
            "• U = Kq₁q₂/r — pair potential energy."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Flux counts lines: EA cosθ, θ from the normal. Close a surface and the ledger says: "
            "outward +1, inward −1 — Gauss's law, Φ = q_in/ε₀, shape matters never, external "
            "charges never. Potential is the scalar V = KQ/r; in a uniform field ΔV = −Ed and "
            "field lines run downhill in V. Energy is one formula: ΔU = qΔV — and the electron "
            "'s negative sign flips the story: it gets paid to climb. Work is −ΔU, speed is "
            "½mv² = |ΔU|, and same voltage means same ENERGY — the lighter particle leaves "
            "faster. Equipotentials are perpendicular to field lines and cost nothing to walk "
            "along."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Charge Detector: Gauss's Law in One Bag",
        "description": (
            "Electric flux, the closed-surface ledger, why external charges contribute zero, "
            "and Gauss's law Φ = q_in/ε₀ with the three-surface worked example."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Gauss's law: flux through closed surfaces, q_in only, shape independence",
            "target_student": "First-year university student",
            "objective": "Compute net flux through any closed surface from its enclosed charges, reading the sign as inward/outward and ignoring all external charges.",
            "hook": "A sealed, opaque bag — yet by counting the field lines crossing its surface you can name the net charge hiding inside, down to the microcoulomb.",
            "explanation_steps": [
                "Flux as field lines through a surface, like rain through a window.",
                "Close the surface: inward crossing −1, outward crossing +1.",
                "Outside charge: line dips in, comes back out — net zero, always.",
                "Inside charge: lines must exit (or enter) — the ledger climbs.",
                "Gauss: Φ = q_in/ε₀; shape and size are irrelevant.",
                "The source problem: S₁ −6 μC/ε₀, S₂ −8 μC/ε₀, S₃ 0.",
                "Circle, add, divide — no field lines drawn.",
            ],
            "common_mistake": "Adding external charges to q_in; bigger/rounder-surface myth; zero flux read as zero field.",
            "check": "A closed surface encloses +6 μC and −2 μC; a +50 μC charge sits just outside. What is the net flux through the surface?",
            "final_takeaway": "Same enclosed charge ⇒ same net flux for any closed shape, with zero say from anything outside: Φ = q_in/ε₀.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Electron's Backwards Climb: qΔV and the Energy Ledger",
        "description": (
            "Energy bookkeeping for charges crossing potentials: ΔU = qΔV with the negative-q "
            "flip, W = −ΔU, and finding speeds from ½mv² = |ΔU|."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "ΔU = qΔV (negative q flips the story), W = −ΔU, ΔK = −ΔU",
            "target_student": "First-year university student",
            "objective": "Determine the sign of ΔU for positive and negative charges crossing a potential difference, compute the field's work, and find final speeds from rest.",
            "hook": "Positive charges fall toward low potential like marbles downhill. This electron climbs toward HIGH potential and comes out faster — one multiplication with a minus sign explains it, and old TV tubes were built on it.",
            "explanation_steps": [
                "ΔV as an electrical height difference between two points.",
                "Positive charge: climbing to high V costs energy; going with the field releases it.",
                "The master switch: ΔU = qΔV — the sign of q multiplies the sign of ΔV.",
                "Electron toward the + plate: (−)(+) = −ΔU, gains kinetic energy.",
                "The ledger: W_field = −ΔU; ΔK = −ΔU; from rest ½mv² = |ΔU|.",
                "Worked example: the 5000-V tube, electron vs proton.",
            ],
            "common_mistake": "Using positive-charge intuition for electrons; writing W = +ΔU; forgetting same |ΔU| gives different speeds for different masses.",
            "check": "An electron is accelerated from rest through 100 V. What is ΔU? What is its final speed? (mₑ = 9.1 × 10⁻³¹ kg)",
            "final_takeaway": "ΔU = qΔV decides everything — the electron's negative charge turns a climb into an energy payout, and every joule lost becomes speed: ½mv² = |ΔU|.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "Define electric flux and state its SI unit. When is flux through a surface zero?",
        "options": [
            "EA cosθ (θ from the normal); unit N·m²/C; zero when the surface is parallel to the field (θ = 90°)",
            "EA sinθ; unit N·m/C; zero when face-on to the field",
            "E/A; unit C·m/N; zero when the field is perpendicular",
            "E·A²; unit N·m³/C; never zero",
        ],
        "correct_index": 0,
        "explanation": "Flux = EA cosθ with the angle measured from the surface normal, in N·m²/C; it vanishes when the surface lies parallel to the field (θ = 90°).",
        "skill": "flux definition",
        "difficulty": 1,
        "competency_code": "electric-flux",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State Gauss's law in words. Does the net flux depend on the shape of the closed surface or on charges outside it?",
        "options": [
            "Net flux through any closed surface = net enclosed charge ÷ ε₀; independent of shape and of all external charges",
            "Net flux depends on the surface's area and shape; external charges add fully",
            "Net flux = (enclosed + nearby external charge) ÷ ε₀",
            "Net flux depends only on the largest charge near the surface",
        ],
        "correct_index": 0,
        "explanation": "Gauss's law fixes net flux by q_in/ε₀ alone or not — shape and all exterior charges are irrelevant, because external lines enter and leave in canceling pairs.",
        "skill": "Gauss statement",
        "difficulty": 1,
        "competency_code": "gauss-law",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Define electric potential. Is it a vector or a scalar, and what is its sign near a negative charge?",
        "options": [
            "Work to bring a unit positive charge from infinity to the point; scalar; negative near a negative charge",
            "Force per unit charge; vector; positive near a negative charge",
            "Charge per unit area; scalar; always positive",
            "Work to drag a unit negative charge; vector; zero everywhere",
        ],
        "correct_index": 0,
        "explanation": "Potential is work per unit positive charge from infinity — a scalar field. V = KQ/r makes it negative near a negative source.",
        "skill": "potential definition",
        "difficulty": 1,
        "competency_code": "electric-potential",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "In a uniform field pointing from A to B, which point is at higher potential, and what is ΔV = V_B − V_A in terms of E and d?",
        "options": [
            "A (field lines run high → low V); ΔV = −Ed",
            "B; ΔV = +Ed",
            "A; ΔV = +Ed",
            "Neither; ΔV = E/d",
        ],
        "correct_index": 0,
        "explanation": "Field lines point from high to low potential, so A is higher. Moving distance d along the field lowers potential: ΔV = V_B − V_A = −Ed.",
        "skill": "field–potential direction rule",
        "difficulty": 1,
        "competency_code": "electric-potential",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "A flat surface of area 0.5 m² sits in a uniform field of 400 N/C. Find the flux when it is (a) perpendicular to the field; (b) making 60° with the field; (c) parallel to the field.",
        "options": [
            "(a) 200 N·m²/C; (b) 60° to field ⇒ θ = 30° ⇒ ≈ 173.2 N·m²/C; (c) 0",
            "(a) 200 N·m²/C; (b) θ = 60° ⇒ 100 N·m²/C; (c) 0",
            "(a) 200 N·m²/C; (b) 200 N·m²/C; (c) 200 N·m²/C",
            "(a) 100 N·m²/C; (b) 86.6 N·m²/C; (c) 0",
        ],
        "correct_index": 0,
        "explanation": "(a) Φ = EA = 200. (b) Surface-to-field 60° ⇒ θ = 30° from the normal ⇒ 200 cos30° ≈ 173.2. (c) Parallel ⇒ θ = 90° ⇒ 0. The normal is the reference, not the surface.",
        "skill": "angle translation + flux computation",
        "difficulty": 2,
        "competency_code": "electric-flux",
    },
    {
        "level": "APPLY",
        "prompt": "A closed surface encloses +3 μC and −1 μC. Compute the net flux with ε₀ = 8.85 × 10⁻¹² C²/(N·m²).",
        "options": [
            "q_in = +2 μC; Φ ≈ 2.26 × 10⁵ N·m²/C, outward (positive)",
            "q_in = +2 μC; Φ ≈ 2.26 × 10⁵ N·m²/C, inward",
            "q_in = +4 μC; Φ ≈ 4.5 × 10⁵ N·m²/C, outward",
            "q_in = +2 μC; Φ ≈ 2.26 × 10⁻⁵ N·m²/C",
        ],
        "correct_index": 0,
        "explanation": "Circle what's inside: +3 − 1 = +2 μC. Φ = 2 × 10⁻⁶/8.85 × 10⁻¹² ≈ 2.26 × 10⁵ N·m²/C. Positive net flux means outward.",
        "skill": "Gauss computation",
        "difficulty": 2,
        "competency_code": "gauss-law",
    },
    {
        "level": "APPLY",
        "prompt": "q₁ = +6 μC is 0.3 m from point P; q₂ = −6 μC is 0.9 m from P. Find V at P.",
        "options": [
            "1.2 × 10⁵ V  (9 × 10⁹ × 6 × 10⁻⁶ × (3.333 − 1.111) = 1.2 × 10⁵)",
            "1.2 × 10⁵ V  (magnitudes added: 3.333 + 1.111)",
            "2.4 × 10⁵ V",
            "0 V (the charges cancel)",
        ],
        "correct_index": 0,
        "explanation": "V = K[q₁/r₁ + q₂/r₂] with signs: (0.3/...) = +K(6×10⁻⁶)/0.3 and −K(6×10⁻⁶)/0.9; the SIGNED sum reads 1.2 × 10⁵ V — the closer q₁ wins, the farther q₂ subtracts.",
        "skill": "signed scalar superposition",
        "difficulty": 2,
        "competency_code": "electric-potential",
    },
    {
        "level": "APPLY",
        "prompt": "A charge of +4 μC crosses ΔV = +12 V; then a charge of −2 μC makes the same trip. Find ΔU for each.",
        "options": [
            "+4 μC: +4.8 × 10⁻⁵ J; −2 μC: −2.4 × 10⁻⁵ J (ΔU = qΔV)",
            "+4 μC: +4.8 × 10⁻⁵ J; −2 μC: +2.4 × 10⁻⁵ J",
            "+4 μC: −4.8 × 10⁻⁵ J; −2 μC: −2.4 × 10⁻⁵ J",
            "Both: 4.8 × 10⁻⁵ J",
        ],
        "correct_index": 0,
        "explanation": "ΔU = qΔV multiplies the two signs: (+4 × 10⁻⁶)(12) = +4.8 × 10⁻⁵ J; (−2 × 10⁻⁶)(12) = −2.4 × 10⁻⁵ J. The negative charge GAINS kinetic energy on this climb.",
        "skill": "sign multiplication",
        "difficulty": 2,
        "competency_code": "potential-energy",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "A closed surface S encloses +5 μC. Two external charges, +10 μC and −10 μC, are brought close to S. (a) What is the flux? (b) The +5 μC moves outside and −3 μC is placed inside. Now what is the flux and what does its sign mean?",
        "options": [
            "(a) Φ = 5 × 10⁻⁶/ε₀ ≈ 5.65 × 10⁵ N·m²/C — the external pair changes nothing; (b) q_in = −3 μC ⇒ Φ ≈ −3.39 × 10⁵ N·m²/C — net INWARD",
            "(a) Φ ≈ 1.7 × 10⁶ N·m²/C — the external pair adds; (b) Φ ≈ −3.39 × 10⁵ inward",
            "(a) Φ = 5.65 × 10⁵ outward; (b) Φ = 5.65 × 10⁵ inward (sign unchanged)",
            "(a) Φ = 0 — the external charges cancel; (b) Φ = 0",
        ],
        "correct_index": 0,
        "explanation": "(a) Flux depends only on enclosed charge: +5 μC, so Φ = 5 × 10⁻⁶/ε₀; each external charge contributes zero individually. (b) New enclosed charge −3 μC ⇒ Φ = −3 × 10⁻⁶/ε₀, and the minus sign means net inward flux.",
        "skill": "Gauss with changing enclosures + sign interpretation",
        "difficulty": 3,
        "competency_code": "gauss-law",
    },
    {
        "level": "TRANSFER",
        "prompt": "The same charge +q is enclosed successively by a sphere, then an irregular potato-shaped surface, then a crumpled bag. Compare the net flux through the three surfaces.",
        "options": [
            "Identical in all three: Φ = q/ε₀ — Gauss depends only on enclosed charge, never on shape or size",
            "The sphere has the largest flux (most symmetric)",
            "The potato catches more lines; the bag the fewest",
            "Only the sphere obeys Gauss's law",
        ],
        "correct_index": 0,
        "explanation": "Gauss's law says net flux = q_in/ε₀ for ANY closed surface. Deforming the bag neither traps nor releases lines from the internal charge — all three give q/ε₀.",
        "skill": "shape-independence reasoning",
        "difficulty": 2,
        "competency_code": "gauss-law",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two charges +q and −q of equal magnitude are fixed in space. Describe the set of all points where the total potential is zero, using scalar superposition.",
        "options": [
            "V = Kq(1/r₊ − 1/r₋) = 0 ⇒ r₊ = r₋ — every point equidistant from both: the plane perpendicularly bisecting the segment (the field is NOT zero there)",
            "V = 0 only at the midpoint of the segment",
            "V = 0 nowhere because potentials always add",
            "V = 0 on every point of the segment joining them",
        ],
        "correct_index": 0,
        "explanation": "Scalar superposition: V = 0 ⇔ distances from the two charges are equal, which is exactly the perpendicular bisecting plane. Potential and field are different quantities — the field on that plane is not zero.",
        "skill": "scalar superposition transferred to a locus argument",
        "difficulty": 3,
        "competency_code": "electric-potential",
    },
    {
        "level": "TRANSFER",
        "prompt": "Through what potential difference must an electron, starting from rest, be accelerated to reach a speed of 1.9 × 10⁶ m/s? (mₑ = 9.1 × 10⁻³¹ kg)",
        "options": [
            "≈ 10.3 V (½m_e v² = 1.64 × 10⁻¹⁸ J = e|ΔV|)",
            "≈ 1.0 V",
            "≈ 103 V",
            "≈ 10 300 V",
        ],
        "correct_index": 0,
        "explanation": "KE needed = ½(9.1 × 10⁻³¹)(1.9 × 10⁶)² ≈ 1.64 × 10⁻¹⁸ J = |ΔU| = e|ΔV| ⇒ |ΔV| = 1.64 × 10⁻¹⁸/1.6 × 10⁻¹⁹ ≈ 10.3 V — the inverse of the TV-tube pattern.",
        "skill": "inverting the acceleration formula",
        "difficulty": 3,
        "competency_code": "potential-energy",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "electric-field",
        "title": "The Electric Field",
        "taxonomy_level": "understand",
        "description": "Define E = F/q₀, compute the point-charge field E = K|Q|/r², and apply the direction and superposition rules.",
        "sort_order": 8,
    },
    {
        "code": "electric-flux",
        "title": "Electric Flux",
        "taxonomy_level": "understand",
        "description": "Compute Φ = EA cosθ with the normal-angle rule and interpret its sign and zero cases.",
        "sort_order": 12,
    },
    {
        "code": "gauss-law",
        "title": "Gauss's Law",
        "taxonomy_level": "apply",
        "description": "Relate net flux through any closed surface to enclosed charge via Φ = q_in/ε₀, ignoring external charges and shape.",
        "sort_order": 13,
    },
    {
        "code": "electric-potential",
        "title": "Electric Potential",
        "taxonomy_level": "understand",
        "description": "Compute point-charge potential V = KQ/r, use ΔV = −Ed, and apply the high→low field rule.",
        "sort_order": 14,
    },
    {
        "code": "potential-energy",
        "title": "Electric Potential Energy",
        "taxonomy_level": "apply",
        "description": "Compute ΔU = qΔV with the negative-q flip, the field's work W = −ΔU, and speeds from ½mv² = |ΔU|.",
        "sort_order": 15,
    },
    {
        "code": "equipotentials",
        "title": "Equipotential Surfaces",
        "taxonomy_level": "understand",
        "description": "State and apply the properties of equipotential lines, including zero work along one.",
        "sort_order": 16,
    },
]

COMPETENCY_PREREQUISITES = [
    ("electric-field", "electric-flux"),
    ("electric-flux", "gauss-law"),
    ("electric-field", "electric-potential"),
    ("electric-potential", "potential-energy"),
    ("electric-potential", "equipotentials"),
]

LESSON_COMPETENCIES = [
    {"code": "electric-flux", "role": "teaches"},
    {"code": "gauss-law", "role": "teaches"},
    {"code": "electric-potential", "role": "teaches"},
    {"code": "potential-energy", "role": "teaches"},
    {"code": "equipotentials", "role": "teaches"},
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

"""PHY211 — Physics, Module 3, Lecture 5: Capacitance and Energy Storage.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 5, Fall 2024 —
'Capacitance, Dielectrics and Energy Storage').

The capstone lesson of the electrostatics arc. Imported by
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
    "code": "M3",
    "title": "Module 3 — Capacitance",
    "description": (
        "Chapter 4: the device that stores charge, its geometry (C = ε₀A/d), "
        "the energy it holds, how dielectrics multiply it, and how capacitors "
        "combine in series and parallel."
    ),
    "sort_order": 3,
}

LESSON = {
    "code": "L5",
    "title": "Capacitance: Geometry, Energy, Dielectrics, and Combinations",
    "description": (
        "Lecture 5 — the capacitor as the practical payoff of the electrostatics "
        "arc: capacitance as a charge-per-volt ratio set by geometry, the stored "
        "energy and energy density, dielectrics that multiply capacitance, and "
        "series/parallel combination rules."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Define capacitance C = Q/ΔV, state the farad, and explain why a bigger battery does NOT change C.",
        "Compute the parallel-plate capacitance C₀ = ε₀A/d and the field E₀ = ΔV₀/d (e.g. 12 V over 1 mm → 12,000 V/m).",
        "Compute stored energy in all three forms U = Q²/2C = ½QΔV = ½CΔV² and the energy density u = ½ε₀E².",
        "Narrate the dielectric chain: molecules polarize, E = E₀/k, ΔV = ΔV₀/k, Q = Q₀ (locked), C = kC₀.",
        "Use C = kε₀A/d = εA/d with k = ε/ε₀ and recall k is unitless with k ≥ 1 (k = 1 for air).",
        "Combine capacitors: parallel C_eq = ΣCᵢ; series 1/C_eq = Σ1/Cᵢ; n identical → nC and C/n.",
        "Explain why series shares charge (full Q on each) and is always smaller than the smallest member, while parallel shares voltage and adds.",
    ],
    "prerequisites": [
        "Gauss's law and the flux/enclosed-charge machinery (Lecture 4).",
        "Electric potential and ΔV = −Ed in a uniform field (Lecture 4).",
        "Sign handling with potential differences (Lecture 4).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A capacitor is two conductors that do NOT touch, built to store charge. Its deep "
            "lesson is that capacitance is a ratio — charge per volt — decided by geometry and "
            "material alone, never by how full it is. This lecture derives that ratio from "
            "Gauss's law, banks the three energy formulas, and shows how an ordinary insulator "
            "makes a capacitor better by fighting the field inside it."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Capacitance",
        "body": "C = Q / ΔV   (unit: farad = C/V)",
        "metadata": {
            "meaning": "Charge stored per volt across the plates — a RATIO, not a 'how much charge' number.",
            "when_used": "Every capacitor problem. Q and ΔV scale together; only geometry/material change C.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Bigger battery, same C",
        "body": "Double the voltage, the stored charge doubles, but Q/ΔV stays fixed. Only the area A, the gap d, or the material (k) can change capacitance.",
    },
    {
        "section_type": "FORMULA",
        "title": "Parallel-plate capacitance",
        "body": "C₀ = ε₀A / d",
        "metadata": {
            "meaning": "Bigger plates hold more charge per volt; a wider gap holds less (weaker field per volt).",
            "when_used": "Any parallel-plate capacitor; the base case before dielectric insertion.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The field inside the gap",
        "body": (
            "A 12 V battery across a plate gap of 1 mm: E₀ = ΔV₀/d = 12/10⁻³ = 12,000 V/m. "
            "The same voltage spread over a wider gap means a weaker field — the geometric "
            "origin of C ∝ 1/d."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Energy Stored and Energy Density",
        "body": (
            "Charging a capacitor moves charge against the already-building field, so the energy "
            "banked is the integral of V·dq — which collapses to three equivalent formulas. The "
            "Go-with-Q form (Q²/2C) is the right choice whenever the charge is fixed (battery "
            "disconnected); the Go-with-ΔV form (½CΔV²) when the voltage is fixed. The energy "
            "physically lives in the field of the gap, at density u = ½ε₀E²."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Stored energy (three forms)",
        "body": "U = Q²/2C = ½QΔV = ½C(ΔV)²",
        "metadata": {
            "meaning": "All three are the same quantity; pick the one whose fixed variable you know.",
            "when_used": "Energy of any charged capacitor.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Energy density in the field",
        "body": "u = ½ε₀E²",
        "metadata": {"meaning": "Joules per cubic meter of gap — energy lives in the field, not on the plates."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "a capacitor at 50 V",
        "body": (
            "A 12 μF capacitor charged to 50 V (Q = 600 μC). U = ½C(ΔV)² = ½(12 × 10⁻⁶)(2500) "
            "= 0.015 J; U = ½QΔV = ½(600 × 10⁻⁶)(50) = 0.015 J; U = Q²/2C = 0.015 J — three "
            "roads, one answer."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Dielectrics: The Insulator That Fights the Field",
        "body": (
            "Slide an insulating slab into a charged, battery-DISCONNECTED capacitor and the "
            "molecules polarize — each becomes a tiny dipole aligned with the field. The forest "
            "of dipoles creates an induced field E′ OPPOSITE to E₀, so the net field weakens: "
            "E = E₀/k. Follow the chain: same gap, weaker field ⇒ ΔV = ΔV₀/k; battery gone ⇒ "
            "Q = Q₀ locked; so C = Q/ΔV = kC₀. The dielectric multiplies capacitance because "
            "it makes the same charge cheaper in volts."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Dielectric capacitance",
        "body": "C = kC₀ = kε₀A/d = εA/d   with   k = ε/ε₀",
        "metadata": {
            "meaning": "k is unitless, always ≥ 1, k = 1 for air; ε = kε₀ is the material's permittivity.",
            "when_used": "Any capacitor with a dielectric; extracting k from measured Q and ΔV.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Dielectric chain in order",
        "body": "Polarize → induced field OPPOSES E₀ → E = E₀/k → ΔV = ΔV₀/k → Q locked = Q₀ → C = Q/ΔV = kC₀. k multiplies C and divides E and ΔV; it never touches the charge. This chain holds for a disconnected battery.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "Extracting k from data",
        "body": (
            "A = 0.028 m², d = 0.55 mm, 12 V battery, Q = 3.62 × 10⁻⁸ C. C = Q/ΔV = 3.02 nF. "
            "Solve C = kε₀A/d for k = Qd/(ΔV ε₀ A) = 6.7. Sanity check: with air this capacitor "
            "would be C₀ = ε₀A/d ≈ 0.45 nF; the ratio 3.02/0.45 = 6.7 — the dielectric raised "
            "capacitance by exactly its own constant."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Combinations: Parallel and Series",
        "body": (
            "Parallel: both capacitors see the SAME voltage; each stores its own charge; the "
            "total charge adds — C_eq = C₁ + C₂ + ⋯. Series: an isolated middle node between "
            "the capacitors must stay charge-neutral, forcing the FULL charge Q onto every "
            "capacitor; the voltages stack, so 1/C_eq = 1/C₁ + 1/C₂ + ⋯ and the equivalent is "
            "SMALLER than the smallest member. Two mnemonics that survive exams: series shares "
            "CHARGE, parallel shares VOLTAGE; and smaller capacitors in series take the bigger "
            "voltage (ΔVᵢ = Q/Cᵢ)."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Combination rules",
        "body": "Parallel: C_eq = C₁ + C₂ + ⋯    Series: 1/C_eq = 1/C₁ + 1/C₂ + ⋯",
        "metadata": {
            "meaning": "n identical capacitors: parallel → nC; series → C/n.",
            "when_used": "Reducing any capacitor network before computing Q or ΔV.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Series charge is not shared",
        "body": "Every capacitor in a series chain carries the FULL charge Q. The equal split myth is false; the isolated middle node has no way to acquire a net charge.",
    },
    {
        "section_type": "EXAMPLE",
        "title": "4 μF and 6 μF",
        "body": (
            "Parallel across 10 V: C_eq = 10 μF; the 4 μF holds 40 μC, the 6 μF holds 60 μC, "
            "total 100 μC. Series across 10 V: 1/C_eq = 1/4 + 1/6 = 5/12 ⇒ C_eq = 2.4 μF; "
            "Q = 24 μC on EACH; ΔV(4μF) = 6 V, ΔV(6μF) = 4 V (sum 10 ✓). The SMALLER capacitor "
            "takes the LARGER voltage."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — full characterization of a plate capacitor",
        "body": (
            "Plates of area 0.1 m², gap 0.2 mm of air, 9 V: C = ε₀A/d = (8.85 × 10⁻¹²)(0.1)/"
            "(2 × 10⁻⁴) ≈ 4.4 × 10⁻⁹ F; Q = CΔV ≈ 4.0 × 10⁻⁸ C; E = ΔV/d = 4.5 × 10⁴ V/m; "
            "U = ½C(ΔV)² ≈ 1.8 × 10⁻⁷ J."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — scaling prediction",
        "body": (
            "A capacitor has C = 20 pF. Double the area ⇒ 40 pF; additionally halve the gap ⇒ "
            "80 pF. Independent multipliers: C ∝ A and C ∝ 1/d — the source's Example 1 "
            "pattern, predictable before any numbers."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — three identical 12 μF capacitors",
        "body": (
            "Series: 1/C_eq = 3/12 = 1/4 ⇒ C_eq = 4 μF. Parallel: C_eq = 3 × 12 = 36 μF. Same "
            "parts, same pile on the table, ninefold difference from wiring alone."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — the dielectric that multiplies by 6.7",
        "body": (
            "A = 0.028 m², d = 0.55 mm, 12 V, Q = 3.62 × 10⁻⁸ C per plate. C = Q/ΔV = 3.02 nF; "
            "k = Qd/(ΔVε₀A) = 6.7. Air-gap value C₀ = 0.45 nF; ratio 6.7. The dielectric "
            "multiplied capacitance by exactly its own constant — physics checking itself."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — battery disconnected, dielectric k = 4",
        "body": (
            "Air capacitor 100 pF charged to 12 V, then DISCONNECTED. Insert k = 4: "
            "C′ = 400 pF; ΔV′ = 12/4 = 3 V; Q = (100 × 10⁻¹²)(12) = 1.2 nC, locked. Charge "
            "never moved; the bigger tank rating simply made the same water cheaper in volts."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "C as 'charge stored'",
        "body": "C is the RATIO Q/ΔV. A bigger battery stores more charge but leaves C unchanged — the ratio is fixed by geometry and material.",
    },
    {
        "section_type": "WARNING",
        "title": "Charge 'splits' in series",
        "body": "False — every capacitor in a series chain carries the FULL charge Q. The isolated middle node forces it; 24 μC on each, never 12.",
    },
    {
        "section_type": "WARNING",
        "title": "Equal voltages in series",
        "body": "Only identical capacitors share voltage equally. Unequal capacitors divide it in inverse proportion: ΔVᵢ = Q/Cᵢ — smaller C, bigger slice.",
    },
    {
        "section_type": "WARNING",
        "title": "The un-flipped reciprocal",
        "body": "1/C_eq = 1/2 means C_eq = 2, not 0.5. The LAST step of every series problem is flipping the reciprocal — and it's the step most often skipped.",
    },
    {
        "section_type": "WARNING",
        "title": "Dielectric adds charge",
        "body": "With a disconnected battery the charge is LOCKED. k multiplies C and divides E and ΔV; it never touches Q.",
    },
    {
        "section_type": "WARNING",
        "title": "Field gets stronger inside",
        "body": "Opposite. The polarized molecules CANCEL part of the field: E = E₀/k, always weaker.",
    },
    {
        "section_type": "WARNING",
        "title": "Units on k (or k < 1)",
        "body": "k is a unitless ratio ε/ε₀ with k ≥ 1 (k = 1 for air). A result below 1 is a sign error.",
    },
    {
        "section_type": "WARNING",
        "title": "Centimeter↔meter slips in areas",
        "body": "1 cm² = 10⁻⁴ m². Feed A in square meters and d in meters, or the capacitance is off by a factor of 10⁴.",
    },
    {
        "section_type": "WARNING",
        "title": "Which variable is frozen?",
        "body": "Battery disconnected ⇒ Q locked (use Q²/2C). Battery connected ⇒ ΔV locked. Ask 'what is frozen?' before choosing an energy form or predicting a dielectric change.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Series: More Parts, Less Capacitance",
        "body": (
            "The isolated wire between two series capacitors is charge-neutral and must stay "
            "that way — it forces the FULL charge Q onto each capacitor. Meanwhile the voltages "
            "stack, so the combination demands more volts per charge: worse exchange rate. "
            "Analogy: stacked gaps double the separation at fixed plate area — C = ε₀A/d halves. "
            "Parallel is glued plates (area doubles); series is stacked gaps (distance "
            "doubles). Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Dielectric Mechanism",
        "body": (
            "Insulating molecules have no free charges, but they polarize — nuclei and electron "
            "clouds pull apart into aligned dipoles whose induced field E′ opposes E₀. Net field "
            "E = E₀ − E′ = E₀/k. With the battery gone the charge is locked, so the same charge "
            "over less voltage means C = kC₀. Analogy: the dielectric doesn't feed the "
            "capacitor, it disarms the field. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Choosing Among the Three Energy Forms",
        "body": (
            "U = Q²/2C, U = ½QΔV, U = ½CΔV² are identical — but they disagree LOUDLY if you "
            "pick one whose 'fixed' variable is actually free. Q is fixed when the battery is "
            "disconnected (use Q²/2C); ΔV when it stays connected (use ½CΔV²). During dielectric "
            "insertion this choice flips the story. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Smaller Capacitor, Bigger Voltage (Series)",
        "body": (
            "Same charge Q everywhere in a series chain, and ΔV = Q/C — so the smallest "
            "capacitor demands the largest voltage. This inverse proportionality is the "
            "inverse of the parallel story (shared voltage, charge ∝ C) and is a favorite exam "
            "fact. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Energy Lives in the Field",
        "body": (
            "u = ½ε₀E² puts the energy in the gap's field, not on the plates. With a dielectric "
            "the density uses ε = kε₀. This picture is what makes capacitors feel like storage "
            "tanks with a measurable 'level' — and it sets up the RC circuits of the next "
            "module. Difficulty: MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• C = Q/ΔV — a ratio fixed by geometry/material; a bigger battery raises Q, never C.\n"
            "• Parallel plates: C₀ = ε₀A/d; E₀ = ΔV₀/d (12 V / 1 mm → 12,000 V/m).\n"
            "• Energy: U = Q²/2C = ½QΔV = ½CΔV²; density u = ½ε₀E².\n"
            "• Dielectric chain (battery off): E = E₀/k → ΔV = ΔV₀/k → Q = Q₀ → C = kC₀ = εA/d, k = ε/ε₀ ≥ 1.\n"
            "• Parallel: C_eq = ΣCᵢ, shared voltage. Series: 1/C_eq = Σ1/Cᵢ, shared charge (FULL Q).\n"
            "• Series is always smaller than the smallest member; smaller capacitors take bigger series voltages."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Capacitor — two conductors that do not touch, built to store charge.\n"
            "• Capacitance (C) — Q/ΔV, the charge stored per volt; unit farad.\n"
            "• Dielectric — an insulating material whose polarization weakens the field and raises C.\n"
            "• Dielectric constant (k) — ε/ε₀, unitless, ≥ 1 (air: 1).\n"
            "• Energy density (u) — energy per unit volume of the gap field, ½εε₀... ½εE².\n"
            "• Equivalent capacitance (C_eq) — the single capacitor that mimics a whole combination."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• C = Q/ΔV — definition (farad = C/V).\n"
            "• C₀ = ε₀A/d — parallel-plate capacitance.\n"
            "• E₀ = ΔV₀/d — field in the gap.\n"
            "• U = Q²/2C = ½QΔV = ½CΔV² — stored energy.\n"
            "• u = ½ε₀E² — energy density.\n"
            "• E = E₀/k; ΔV = ΔV₀/k; Q = Q₀; C = kC₀ — the dielectric chain.\n"
            "• C = kε₀A/d = εA/d with ε = kε₀ — dielectric capacitance.\n"
            "• C_eq = ΣCᵢ (parallel); 1/C_eq = Σ1/Cᵢ (series); n identical → nC, C/n."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Capacitance is charge per volt, set by A, d, and k — never by the battery size. "
            "The gap holds a field E₀ = ΔV₀/d and the energy lives in that field at "
            "u = ½ε₀E². Slide in a dielectric with the battery off: molecules polarize and "
            "fight the field, E drops by k, voltage drops by k, charge stays locked — so "
            "C = kC₀. Parallel shares VOLTAGE and adds charges; series shares the FULL CHARGE "
            "and adds voltages, coming out smaller than the smallest member. n identical: nC "
            "or C/n. Series shares charge, parallel shares voltage — never the reverse."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "More Parts, Less Capacitance? Series Capacitors Explained",
        "description": (
            "Why parallel capacitors add while series capacitors shrink below the smallest "
            "member: the isolated-middle-node argument, charge distribution, and voltage "
            "division."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Series vs parallel combinations; C_eq; why series is smaller than the smallest",
            "target_student": "First-year university student",
            "objective": "Compute C_eq for series and parallel chains (including n-identical cases) and explain WHY series comes out smaller, with full charge/voltage distribution.",
            "hook": "Two identical 6 μF capacitors in parallel make 12 μF. In series they make 3 μF — HALF of a single one. You just added a component and storage went DOWN.",
            "explanation_steps": [
                "Define C_eq as the single device: charge in per volt out.",
                "Parallel: common voltage, charges add ⇒ C_eq = ΣCᵢ.",
                "Series: the isolated middle node stays neutral, forcing FULL Q on every capacitor.",
                "Voltages stack ⇒ worse charge-per-volt ⇒ 1/C_eq = Σ1/Cᵢ.",
                "Stacked-gaps vs glued-plates picture of C ∝ A/d.",
                "Numbered example: 4 μF and 6 μF in both wirings with full distributions.",
                "Sanity check: series C_eq must be BELOW the smallest member.",
            ],
            "common_mistake": "Charge splitting in series; equal voltages assumed; the un-flipped reciprocal (1/C_eq reported as C_eq).",
            "check": "Three identical 12 μF capacitors: which wiring gives the bigger C_eq, and what are both answers?",
            "final_takeaway": "Series shares charge and adds voltages → reciprocal sum → smaller than the smallest. Parallel shares voltage and adds charges → plain sum.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Insulator That Multiplies Your Capacitor: Dielectrics",
        "description": (
            "The dielectric chain: molecular polarization, the induced opposing field, "
            "E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, and C = kC₀, with k-extraction from data."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Dielectric mechanism: polarization, induced opposing field, E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, C = kC₀",
            "target_student": "First-year university student",
            "objective": "Narrate the dielectric chain in order, compute the new C, ΔV, and E after insertion (battery disconnected), and extract k from measured data.",
            "hook": "Slide an ordinary piece of plastic — a non-conductor — between a charged capacitor's plates and the capacitance multiplies. By seven, for the lecture's mystery material.",
            "explanation_steps": [
                "Setup: air-gap capacitor, charged, battery disconnected — Q₀ locked on.",
                "Insert the dielectric: molecules polarize — stretch and align with the field.",
                "Each molecule a tiny dipole; together they make an induced field E′ opposite E₀.",
                "Net field E = E₀ − E′ = E₀/k — weakened, not eliminated.",
                "Consequence chain: ΔV = ΔV₀/k; Q = Q₀; C = kC₀.",
                "Constants: k unitless, ≥ 1, k = 1 for air; ε = kε₀; C = εA/d.",
                "Worked example: extracting k = 6.7 from the source's data.",
            ],
            "common_mistake": "Thinking Q increases; applying k to Q instead of C; believing the field gets stronger; assuming k has units or can be below 1.",
            "check": "Air capacitor, 100 pF, charged to 12 V, battery removed, insert k = 4. New C? New ΔV? What stayed fixed?",
            "final_takeaway": "The dielectric's molecules fight the field: E and ΔV drop by k, the locked charge stays, so C = Q/ΔV rises to kC₀ = εA/d.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "Define capacitance and state its unit. Does C change when the capacitor is connected to a larger battery?",
        "options": [
            "C = Q/ΔV, unit farad (C/V); NO — Q ∝ ΔV, so the ratio is fixed by geometry/material (A, d, k)",
            "C = Q·ΔV, unit farad (C·V); yes — a bigger battery increases C",
            "C = Q/ΔV, unit farad; yes — C doubles with the battery",
            "C = ΔV/Q, unit V/C; no — C is fixed",
        ],
        "correct_index": 0,
        "explanation": "C = Q/ΔV is a ratio. Raising the battery raises both Q and ΔV proportionally, leaving the ratio fixed; only A, d, or k can change C.",
        "skill": "ratio concept",
        "difficulty": 1,
        "competency_code": "plate-capacitance",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "In a series combination, which quantity is the same on every capacitor? In a parallel combination?",
        "options": [
            "Series: the full charge Q; parallel: the voltage ΔV",
            "Series: the voltage ΔV; parallel: the full charge Q",
            "Series: the charge is shared equally; parallel: the charge is shared",
            "Series: nothing is the same; parallel: the current",
        ],
        "correct_index": 0,
        "explanation": "The isolated node in series forces the FULL charge onto every capacitor; in parallel every capacitor clips the same two nodes, so each sees the whole voltage.",
        "skill": "combination signatures",
        "difficulty": 1,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why is the equivalent capacitance of a series combination always smaller than the smallest capacitor in it?",
        "options": [
            "Same Q on each forces voltages ΔVᵢ = Q/Cᵢ that ADD; the chain needs more total voltage for the same charge than any single member — a worse charge-per-volt ratio",
            "Series wires physically remove material from the capacitors",
            "The gaps stack until the field collapses",
            "It isn't — series is always between the largest and smallest",
        ],
        "correct_index": 0,
        "explanation": "With equal Q everywhere and stacked voltages, the combination demands more volts per coulomb than any member: 1/C_eq = Σ1/Cᵢ > 1/C_smallest, hence C_eq < C_smallest.",
        "skill": "series reasoning",
        "difficulty": 2,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State what happens to E, ΔV, Q, and C when a dielectric is inserted into a charged, DISCONNECTED capacitor.",
        "options": [
            "E → E₀/k; ΔV → ΔV₀/k; Q = Q₀ (unchanged, locked); C → kC₀ (increased)",
            "E → E₀/k; ΔV → ΔV₀/k; Q → kQ₀; C → C₀",
            "E → kE₀; ΔV → kΔV₀; Q → Q₀; C → kC₀",
            "Everything stays the same",
        ],
        "correct_index": 0,
        "explanation": "The dielectric weakens the field (E = E₀/k), which lowers the voltage; with the battery gone the charge is locked, so the ratio Q/ΔV rises to kC₀.",
        "skill": "dielectric chain",
        "difficulty": 2,
        "competency_code": "dielectric-effects",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "Capacitors of 3 μF and 6 μF are connected in parallel across 12 V. Find C_eq, the charge on each, and the total charge.",
        "options": [
            "C_eq = 9 μF; Q₁ = 36 μC, Q₂ = 72 μC; total 108 μC = C_eqΔV",
            "C_eq = 9 μF; Q₁ = 72 μC, Q₂ = 36 μC; total 108 μC",
            "C_eq = 2 μF; Q₁ = 24 μC, Q₂ = 24 μC; total 48 μC",
            "C_eq = 9 μF; Q₁ = 12 μC, Q₂ = 12 μC; total 24 μC",
        ],
        "correct_index": 0,
        "explanation": "Parallel C_eq = 3 + 6 = 9 μF. Each sees 12 V: Qᵢ = CᵢΔV gives 36 μC and 72 μC — bigger capacitor, more charge. Total 108 μC = C_eqΔV ✓.",
        "skill": "parallel distribution",
        "difficulty": 2,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "APPLY",
        "prompt": "The same 3 μF and 6 μF are reconnected in SERIES across 12 V. Find C_eq, the charge on each, and the voltage across each.",
        "options": [
            "C_eq = 2 μF; Q = 24 μC on EACH; ΔV(3μF) = 8 V, ΔV(6μF) = 4 V (sum 12 V ✓)",
            "C_eq = 2 μF; Q = 24 μC total shared 12/12; ΔV = 6 V each",
            "C_eq = 2 μF; Q₁ = 48 μC, Q₂ = 96 μC; voltages 8 V and 4 V",
            "C_eq = 9 μF; Q = 24 μC each; ΔV = 6 V each",
        ],
        "correct_index": 0,
        "explanation": "1/C_eq = 1/3 + 1/6 = 1/2 ⇒ C_eq = 2 μF. Q = C_eqΔV = 24 μC on EACH (series shares the full charge). ΔV₁ = 24/3 = 8 V, ΔV₂ = 24/6 = 4 V — smaller capacitor, larger voltage.",
        "skill": "series distribution",
        "difficulty": 2,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "APPLY",
        "prompt": "A parallel-plate capacitor has plates of area 0.1 m² separated by 0.2 mm of air at 9 V. Find C, the stored charge, and the field.",
        "options": [
            "C ≈ 4.4 nF; Q ≈ 4.0 × 10⁻⁸ C; E = 4.5 × 10⁴ V/m",
            "C ≈ 0.44 nF; Q ≈ 4.0 × 10⁻⁹ C; E = 45 V/m",
            "C ≈ 4.4 μF; Q ≈ 40 μC; E = 4.5 × 10³ V/m",
            "C ≈ 4.4 nF; Q ≈ 4.0 × 10⁻⁶ C; E = 4.5 × 10⁴ V/m",
        ],
        "correct_index": 0,
        "explanation": "C = ε₀A/d = (8.85 × 10⁻¹²)(0.1)/(2 × 10⁻⁴) ≈ 4.4 × 10⁻⁹ F. Q = CΔV ≈ 4.0 × 10⁻⁸ C. E = ΔV/d = 9/2 × 10⁻⁴ = 4.5 × 10⁴ V/m. Watch the millimeter conversion.",
        "skill": "full plate-capacitor characterization",
        "difficulty": 2,
        "competency_code": "plate-capacitance",
    },
    {
        "level": "APPLY",
        "prompt": "A 12 μF capacitor is charged to 50 V. Find the stored energy via all three formulas.",
        "options": [
            "Q = 600 μC; U = 0.015 J by ½CΔV², by ½QΔV, and by Q²/2C",
            "Q = 600 μC; U = 0.03 J by all three",
            "Q = 600 μC; U = 0.015 J by ½CΔV² but 0.03 J by Q²/2C",
            "Q = 60 μC; U = 1.5 × 10⁻³ J",
        ],
        "correct_index": 0,
        "explanation": "Q = (12 × 10⁻⁶)(50) = 600 μC. U = ½CΔV² = ½(12 × 10⁻⁶)(2500) = 0.015 J; ½QΔV = ½(600 × 10⁻⁶)(50) = 0.015 J; Q²/2C = (600 × 10⁻⁶)²/(2 × 12 × 10⁻⁶) = 0.015 J — all agree.",
        "skill": "energy forms",
        "difficulty": 2,
        "competency_code": "stored-energy",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "An air capacitor of 100 pF is charged to 12 V and disconnected. A dielectric with k = 4 fills the gap. Determine the new C, ΔV, and Q — then what happens to the stored energy.",
        "options": [
            "C′ = 400 pF; ΔV′ = 3 V; Q = 1.2 nC (locked); Q is fixed so use Q²/2C ⇒ U drops by the factor k (U′ = U₀/k)",
            "C′ = 400 pF; ΔV′ = 3 V; Q rises to 4.8 nC; energy unchanged",
            "C′ = 25 pF; ΔV′ = 48 V; Q = 1.2 nC; energy rises by k",
            "C′ = 400 pF; ΔV′ = 48 V; Q = 1.2 nC; energy unchanged",
        ],
        "correct_index": 0,
        "explanation": "C′ = kC₀ = 400 pF; ΔV′ = ΔV₀/k = 3 V; Q = C₀ΔV₀ = 1.2 nC stays locked. With Q fixed, U = Q²/2C: U₀ = 7.2 × 10⁻⁹ J, U′ = 1.8 × 10⁻⁹ J — U drops by the factor k.",
        "skill": "dielectric chain + energy-form selection under constraints",
        "difficulty": 3,
        "competency_code": "dielectric-effects",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two capacitors, 6 μF and 3 μF, in series across 12 V. A student claims: 'C_eq = 4.5 μF — the average — and each capacitor holds 6 V.' Identify every error and give the correct solution.",
        "options": [
            "C_eq is the reciprocal sum (2 μF, not an average); equal voltages hold only for identical capacitors; correct: Q = 24 μC on each, ΔV(6μF) = 4 V, ΔV(3μF) = 8 V",
            "C_eq = 4.5 μF is correct but voltages are 8 V and 4 V",
            "C_eq = 2 μF and each capacitor holds 6 V is correct",
            "C_eq = 9 μF; voltages 6 V each — series averages everything",
        ],
        "correct_index": 0,
        "explanation": "Two canonical series errors: C_eq is a reciprocal sum, 1/C_eq = 1/6 + 1/3 = 1/2 ⇒ 2 μF, never an average; and series voltages split in inverse proportion to capacitance — the smaller 3 μF takes the larger 8 V.",
        "skill": "diagnosing the two canonical series errors",
        "difficulty": 2,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "TRANSFER",
        "prompt": "You have two identical capacitors C. Compare C_eq in series (C/2) versus parallel (2C) and explain each with the gap-stacking / plate-gluing picture.",
        "options": [
            "Series C/2 (stacked gaps: separation 2d at area A); parallel 2C (glued plates: area 2A at gap d); ratio parallel:series = 4",
            "Series C/2 and parallel 2C both reduce to C; ratio 1",
            "Series 2C, parallel C/2 — wiring mirrored",
            "Series and parallel both give C — the geometry is identical",
        ],
        "correct_index": 0,
        "explanation": "Series: 1/C_eq = 2/C ⇒ C/2, the picture of stacked gaps (effective separation 2d). Parallel: C_eq = 2C, the picture of glued plates (area 2A). Same parts, wiring alone gives a fourfold swing.",
        "skill": "combination intuition + C ∝ A/d picture",
        "difficulty": 2,
        "competency_code": "combinations-capacitors",
    },
    {
        "level": "TRANSFER",
        "prompt": "A parallel-plate capacitor with a dielectric (k = 6.7) stores 3.62 × 10⁻⁸ C per plate at 12 V. Where does the stored energy physically reside, and what formula computes it per unit volume?",
        "options": [
            "In the field within the gap/dielectric at density u = ½εE² with ε = kε₀; independent of plate geometry",
            "On the plate surfaces, at density u = charge/area",
            "Only in the connecting wires",
            "In the dielectric molecules as chemical energy, at density u = kQ/2",
        ],
        "correct_index": 0,
        "explanation": "The energy lives in the electric field of the gap, density u = ½εE² (ε = kε₀ for a dielectric), a per-volume quantity that does not care about plate shape. Numerically E ≈ 2.18 × 10⁴ V/m ⇒ u ≈ 1.4 × 10⁻² J/m³.",
        "skill": "energy-density concept transferred to a real device",
        "difficulty": 3,
        "competency_code": "stored-energy",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
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
        "code": "plate-capacitance",
        "title": "Parallel-Plate Capacitance",
        "taxonomy_level": "apply",
        "description": "Compute C = Q/ΔV and C₀ = ε₀A/d, and explain why the ratio is fixed by geometry and material.",
        "sort_order": 17,
    },
    {
        "code": "stored-energy",
        "title": "Stored Energy of a Capacitor",
        "taxonomy_level": "apply",
        "description": "Compute stored energy in all three forms and the energy density u = ½εE².",
        "sort_order": 18,
    },
    {
        "code": "dielectric-effects",
        "title": "Dielectrics",
        "taxonomy_level": "apply",
        "description": "Apply the dielectric chain E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, C = kC₀ and extract k from data.",
        "sort_order": 19,
    },
    {
        "code": "combinations-capacitors",
        "title": "Capacitors in Series and Parallel",
        "taxonomy_level": "apply",
        "description": "Reduce capacitor networks via C_eq = ΣCᵢ (parallel) and 1/C_eq = Σ1/Cᵢ (series) with full charge/voltage distribution.",
        "sort_order": 20,
    },
]

COMPETENCY_PREREQUISITES = [
    ("gauss-law", "plate-capacitance"),
    ("electric-potential", "plate-capacitance"),
    ("plate-capacitance", "stored-energy"),
    ("plate-capacitance", "dielectric-effects"),
    ("plate-capacitance", "combinations-capacitors"),
]

LESSON_COMPETENCIES = [
    {"code": "plate-capacitance", "role": "teaches"},
    {"code": "stored-energy", "role": "teaches"},
    {"code": "dielectric-effects", "role": "teaches"},
    {"code": "combinations-capacitors", "role": "teaches"},
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

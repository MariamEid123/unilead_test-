"""PHY211 — Physics, Module 11, Lesson 13: Midterm Review Problem Clinic (Ch. 1–5).

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: 'Part 1' additional practice set for the PHY211 midterm —
79 multiple-choice problems spanning charge → Coulomb's law → field & flux →
potential → capacitance & dielectrics → current & drift → Ohm's law).

A consolidation lesson rather than new instruction: students PRACTICE across
the midterm syllabus, REMEDIATE weak topics, RETRY, then transfer to the
final-review material. Imported by ``curriculum.content`` and seeded by
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
    "code": "M11",
    "title": "Module 11 — Midterm Review Problem Clinic (Ch. 1–5)",
    "description": (
        "Consolidation of Chapters 1–5: charge & electron counting, Coulomb's "
        "law and zero-field/zero-force/zero-potential points, field lines & "
        "flux (Gauss's law), potential & potential energy, capacitor networks "
        "with the isolated-vs-connected question, and the microscopic current "
        "model down to Ohm's law and resistivity."
    ),
    "sort_order": 11,
}

LESSON = {
    "code": "L13",
    "title": "Midterm Review: Charge, Coulomb's Law, Field & Flux, Potential, Capacitance, Current & Resistance",
    "description": (
        "A practice-first consolidation of the midterm syllabus: charging and "
        "quantization, Coulomb scaling and silent (zero) points, field "
        "superposition and Gauss's law flux form, potential superposition, "
        "capacitor networks and the battery-vs-isolated invariant, drift "
        "velocity, and resistance from geometry."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Explain charging by friction in terms of electron transfer and apply charge conservation and Q = ne.",
        "Apply Coulomb's law including scaling with charge and distance, and locate zero-force points by superposition.",
        "Compute electric fields (E = F/q, E = K|Q|/r²) and flux (Φ = q_enc/ε₀) and interpret field-line pictures.",
        "Compute electric potential and potential energy and relate ΔV, E, and d in uniform fields.",
        "Reduce capacitor networks and predict dielectric and geometry changes for isolated vs battery-connected capacitors.",
        "Relate current to drift velocity (I = nqAv_d) and compute resistance from resistivity and geometry.",
    ],
    "prerequisites": [
        "Properties and quantization of charge, charge units, and the three charging methods (Lectures 1–2).",
        "Coulomb's law, the electric field, field lines, and flux/Gauss's law (Lectures 2–4).",
        "Electric potential, potential energy, capacitance, dielectrics, and capacitor combinations (Lectures 4–5).",
        "Electric current, drift velocity, Ohm's law, and resistance/resistivity (Lectures 6–7).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "This clinic re-runs the midterm concept map READY for exam speed: "
            "charging → Coulomb force → electric field (superposition) → field "
            "lines & flux → potential & potential energy → capacitors & energy → "
            "current & drift velocity → Ohm's law & resistivity. Each block "
            "feeds the next, so drill the chain once, end-to-end, and the "
            "discrete topics snap together."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Electric Charge and Charging by Friction",
        "body": (
            "Only ELECTRONS move when objects are charged by rubbing; total "
            "charge is conserved; net charge is quantized: |Q| = ne with "
            "e = 1.6 × 10⁻¹⁹ C. Rubbing fur on rubber moves electrons fur → "
            "rubber (rubber negative, fur positive); rubbing glass with silk "
            "moves electrons OFF the glass (glass positive). Protons never "
            "transfer by rubbing, and the two partners always end up equal and "
            "opposite."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The transfer question",
        "body": (
            "When an object becomes negative, ask 'which way did electrons "
            "move?' — never 'which protons got removed?'. The donor and "
            "receiver always finish with EQUAL and OPPOSITE net charges."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Coulomb's law and the factor trick",
        "body": "F = ke·q₁q₂/r²     and     F₂/F₁ = (q₁′q₂′/q₁q₂)·(r/r′)²",
        "metadata": {
            "meaning": "Magnitudes first, direction by signs (like repel, unlike attract); the pair exerts equal and opposite forces (Newton's third law).",
            "when_used": "Halving separation → force ×4; tripling both charges → ×9; tripling distance → ÷9. The factor form kills unit-conversion slips.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "The Electric Field: Vectors, Not Numbers",
        "body": (
            "E = F/q is force per unit positive test charge; for a point "
            "charge E = ke·|Q|/r² pointing AWAY from + and TOWARD −. Multiple "
            "fields add as VECTORS: sketch each arrow, then add. A charge q in "
            "a field feels F = qE — same direction as E for positive q, "
            "opposite for negative. Zero-field points occur where the arrows "
            "cancel: LIKE charges cancel BETWEEN them (closer to the smaller "
            "charge); UNLIKE charges cancel OUTSIDE, beyond the smaller charge."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Field Lines and Electric Flux (Gauss's Law)",
        "body": (
            "Φ = q_enclosed/ε₀ through ANY closed surface depends only on the "
            "NET enclosed charge — not on the surface's size or shape, and "
            "outside charges contribute zero net flux. Line density is field "
            "strength; lines begin on + and end on −; their count is "
            "proportional to charge; direction gives sign. Growing a balloon "
            "surface around a charge spreads the lines but does not change the "
            "count."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Potential and potential energy (scalars)",
        "body": "V = ke·Q/r     and     PE = ke·q₁q₂/r     and     ΔV = −Ed",
        "metadata": {
            "meaning": "V is potential energy per unit charge (J/C = V; also 1 V = 1 N/C·m); potentials ADD as signed numbers, energies too. In a uniform field, V drops by E·d along the field.",
            "when_used": "ZERO-POTENTIAL points differ from zero-FIELD points: V is a scalar sum, E is a vector sum. Between opposite charges V = 0 lies closer to the smaller charge; E = 0 there does not exist.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Capacitance and Capacitor Networks",
        "body": (
            "C = Q/ΔV = κε₀A/d depends ONLY on geometry and the dielectric — "
            "never on Q or V. Raising the battery voltage raises Q but leaves C "
            "alone. Rules (mirror images of the resistor rules): SERIES shares "
            "the same charge and 1/Cₛ = Σ1/Cᵢ (result SMALLER than the "
            "smallest); PARALLEL shares the same voltage and Cₚ = ΣCᵢ (result "
            "LARGER than the largest)."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The invariant question",
        "body": (
            "Stored energy: U = ½CV² = ½QV = Q²/2C. Before any what-if, ask: "
            "is the battery attached? ISOLATED (disconnected): Q is locked — "
            "pull plates apart (C↓) → V = Q/C ↑ and U = Q²/2C ↑; insert a "
            "dielectric (C↑) → V ↓, U ↓. CONNECTED: V is locked — C↓ → Q = CV "
            "↓ and U = ½CV² ↓; dielectric → Q ↑, U ↑."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Current and Drift Velocity",
        "body": (
            "I = ΔQ/Δt, and microscopically I = nqAv_d. Carriers are "
            "conduction electrons drifting fractions of a millimeter per "
            "second; a thicker wire (larger A) needs a SMALLER drift speed for "
            "the same current. I triples with n, q, A fixed → v_d triples; "
            "double the diameter → area ×4 → v_d ÷4."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Ohm's law and resistivity",
        "body": "V = IR     and     R = ρL/A",
        "metadata": {
            "meaning": "ρ is the MATERIAL's property; R is the specific OBJECT's; resistance grows with L, shrinks with A, and rises with temperature.",
            "when_used": "When a constraint links L and A (e.g., fixed volume AL = const), substitute the constraint into R = ρL/A BEFORE solving: stretch to 3× at constant volume → R ×9.",
        },
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — electron counting (source Q4)",
        "body": (
            "Q = −3.8 × 10⁻⁶ C: n = |Q|/e = (3.8 × 10⁻⁶)/(1.6 × 10⁻¹⁹) = "
            "2.4 × 10¹³ electrons, the minus sign meaning an excess. "
            "Answer: 2.4 × 10¹³."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — the zero-force point (source Q9)",
        "body": (
            "+2.00 C at x = 0 and +3.00 C at x = 3.00 m; a third charge feels "
            "no force where the fields cancel: 2/x² = 3/(3 − x)² → "
            "2(3 − x)² = 3x² → x² + 12x − 18 = 0 → x ≈ 1.35 m from the +2 C "
            "charge. Between two like charges, closer to the smaller one."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — potential in a uniform field (source Q30)",
        "body": (
            "E = 600 N/C along +x with V(x = 3.0 m) = 1000 V. V decreases "
            "along the field, so V(1.0) − V(3.0) = E·2.0 = 1200 V → "
            "V(1.0) = 2200 V."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — series capacitors share charge (source Q47)",
        "body": (
            "1.0 µF and 0.50 µF in series across 100 V: 1/Cₛ = 1 + 2 = 3 "
            "(µF)⁻¹ → Cₛ = 1/3 µF. The battery delivers Q = CₛV = 33 µC, and "
            "in series EVERY plate pair carries this same 33 µC — including "
            "the 1.0 µF capacitor."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — isolated vs connected (sources Q62 vs Q63)",
        "body": (
            "Plates pulled apart so d doubles → C halves. ISOLATED: Q fixed → "
            "U = Q²/2C doubles (ratio 2). BATTERY CONNECTED: V fixed → "
            "U = ½CV² halves (ratio ½). Identical motion, opposite energy "
            "changes — decided entirely by which quantity is locked."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 6 — resistance with a volume constraint (source Q77)",
        "body": (
            "Copper, volume 100 cm³ = 10⁻⁴ m³, R = 8.5 Ω, ρ = 1.7 × 10⁻⁵ Ω·m: "
            "since A = V/L, R = ρL²/V → L = √(RV/ρ) = √(8.5 × 10⁻⁴/1.7 × 10⁻⁵) "
            "≈ 7.1 m."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "'Protons were removed'",
        "body": "Protons are bound in the nucleus; only electrons transfer in friction charging. Ask which way the electrons moved.",
    },
    {
        "section_type": "WARNING",
        "title": "Doubling distance → force ×1/4, not ×1/2",
        "body": "Coulomb's law is inverse-square: use the factor form (r/r′)². Distance ×3 → force ÷9.",
    },
    {
        "section_type": "WARNING",
        "title": "Adding E-fields as plain numbers",
        "body": "E is a vector; directions decide add vs cancel. Sketch the arrows first — same-sign charges cancel between them, opposite charges double between them.",
    },
    {
        "section_type": "WARNING",
        "title": "V = 0 where E = 0? No.",
        "body": "V is a scalar sum, E is a vector sum — their zero points differ. Solve each condition separately (Q9 vs Q38).",
    },
    {
        "section_type": "WARNING",
        "title": "Raising the voltage raises the capacitance?",
        "body": "C = Q/V is fixed by geometry and dielectric; only Q rises. Ask what changed: V, Q, or the geometry itself.",
    },
    {
        "section_type": "WARNING",
        "title": "Resistor rules applied to capacitors",
        "body": "Capacitor rules are the mirror image: series takes reciprocals (SAME charge), parallel adds directly (SAME voltage).",
    },
    {
        "section_type": "WARNING",
        "title": "Diameter vs area in I = nqAv_d",
        "body": "A = πr² scales with radius squared — double the diameter → area ×4 → v_d ÷4.",
    },
    {
        "section_type": "WARNING",
        "title": "Unit-prefix slips (mC vs µC vs nC)",
        "body": "Powers of ten dominate the wrong options. Convert everything to SI (coulombs, meters) before computing.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Zero-field / zero-force points on a line",
        "body": (
            "Students hunt for a formula instead of equating two magnitudes and "
            "guessing the region. The net field is zero where the two "
            "contributions have EQUAL magnitude and OPPOSITE direction: same "
            "signs → between them (nearer the smaller); opposite signs → outside "
            "beyond the smaller. Analogy: two speakers of different loudness — "
            "find where they sound equally loud. Steps: pick the region → write "
            "ke|Q|/r² for each → set equal → square-root → solve → check the "
            "region. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Potential vs potential energy (and their signs)",
        "body": (
            "V = keQ/r is the environment (J per coulomb); PE = qV is the "
            "energy of a charge placed in it. The potential of a NEGATIVE "
            "charge is negative; PE is negative for opposite-sign (bound) "
            "pairs. Analogy: V is the hill's height, PE = qV is the energy of "
            "a particular ball on it — a negative ball rolls the other way. "
            "Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Isolated vs battery-connected capacitor",
        "body": (
            "The same action (pull plates apart, insert dielectric) produces "
            "opposite energy changes in the two cases. Battery = voltage-lock; "
            "disconnected = charge-lock. Rewrite everything from the invariant "
            "using U = ½CV² (V fixed) or U = Q²/2C (Q fixed). Analogy: a "
            "water container with the level locked or the amount locked — never "
            "both. Difficulty: VERY HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Series/parallel capacitor networks",
        "body": (
            "Resistor intuition interferes and the same-charge-in-series rule "
            "feels wrong. Collapse piece by piece: parallel group (same V) → "
            "add; series group (same Q) → reciprocals; repeat until one "
            "capacitor remains. Analogy: the narrowest pipe and the widest "
            "reservoir set the extremes — series < smallest, parallel > "
            "largest. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The microscopic current model (I = nqAv_d)",
        "body": (
            "Current feels instant, so the sluggish drift contradicts "
            "intuition. I = (carrier count) × (charge) × (speed) passing per "
            "second: I = nqAv_d. Analogy: a packed highway vs an empty one — "
            "the same cars per hour can mean crawling in eight lanes or "
            "speeding in one. Convert diameter → A = πr² before substituting. "
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
            "• Charging = electron transfer; partners get equal & opposite charge; |Q| = ne.\n"
            "• Coulomb: F ∝ q₁q₂/r²; equal-and-opposite pairs; direction by signs.\n"
            "• E = F/q; point-charge fields superpose as vectors; zero-E points: like charges between, unlike outside.\n"
            "• Flux Φ = q_enc/ε₀ — only the net enclosed charge matters.\n"
            "• V = keQ/r superposes as a scalar; PE = keq₁q₂/r; in uniform fields V changes by Ed.\n"
            "• C = Q/ΔV = κε₀A/d (geometry only). Series: same Q, 1/C adds; parallel: same V, C adds.\n"
            "• U = ½CV² = Q²/2C — pick the form matching the invariant. Isolated → Q fixed; connected → V fixed.\n"
            "• I = nqAv_d; thicker wire → slower drift. V = IR; R = ρL/A."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Quantization of charge — net charge = integer × e.\n"
            "• Electric field — force per unit positive charge (N/C).\n"
            "• Electric flux — field 'flow' through a closed surface; Φ = q_enc/ε₀.\n"
            "• Potential — potential energy per unit charge (J/C = V).\n"
            "• Capacitance — charge stored per volt (F = C/V).\n"
            "• Drift velocity — the slow average carrier speed carrying the current.\n"
            "• Resistivity — the material's intrinsic resistance property (Ω·m)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• F = keq₁q₂/r²; E = keQ/r²; V = keQ/r; PE = keq₁q₂/r.\n"
            "• Φ = q_enc/ε₀ — Gauss's law (flux form).\n"
            "• C = κε₀A/d; Q = CV; U = ½CV²; 1/Cₛ = Σ1/Cᵢ; Cₚ = ΣCᵢ.\n"
            "• I = nqAv_d; V = IR; R = ρL/A."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Electrons move when things rub; Q = ne. Coulomb: like repels, "
            "F ~ q₁q₂/r². Fields add as vectors, potentials as scalars. Flux = "
            "enclosed charge/ε₀. Capacitors: geometry sets C; series shares Q, "
            "parallel shares V; energy ½CV² — battery fixes V, isolation fixes "
            "Q. Current I = nqAv_d (bigger wire, slower drift). Resistance "
            "ρL/A, Ohm V = IR."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The Battery Paradox: Pull Capacitor Plates Apart and Energy Goes… Which Way?",
        "description": (
            "Isolated vs battery-connected capacitor behavior: the same 'pull "
            "the plates apart' motion doubles the stored energy in one case and "
            "halves it in the other, decided by which quantity is locked."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Isolated vs battery-connected capacitor behavior",
            "target_student": "First-year university student",
            "objective": "Predict changes in Q, V, C, and U when capacitor geometry changes, conditioned on whether the battery is connected.",
            "hook": "Two identical capacitors; pull the plates apart in both — one gains energy, one loses it. Same action, opposite result.",
            "explanation_steps": [
                "C = ε₀A/d sets capacitance from geometry alone.",
                "Two invariants: the battery locks V; disconnection locks Q.",
                "U = ½CV² vs U = Q²/2C — choose the form matching the invariant.",
                "Double d → C halves on both sides; energy halves (connected) or doubles (isolated).",
                "Insert a dielectric both ways: C ↑ → U ↓ (isolated), U ↑ (connected).",
            ],
            "common_mistake": "Applying the connected-case result to an isolated capacitor.",
            "check": "The battery is disconnected, then you insert a dielectric (κ = 2). Does the stored energy increase or decrease?",
            "final_takeaway": "Battery locks V; no battery locks Q. Everything else follows.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "Where Is Zero? Hunting the Silent Point Between Charges",
        "description": (
            "Zero-field and zero-potential points via superposition: the "
            "region logic for like vs unlike charges, the magnitude-equality "
            "equation, and why zero field and zero potential are two different "
            "questions."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Zero-field and zero-potential points via superposition",
            "target_student": "First-year university student",
            "objective": "Locate where the net field (or potential) of two point charges vanishes, for any sign combination.",
            "hook": "Two charges on a line, and somewhere between them total silence — a five-step ritual, not luck.",
            "explanation_steps": [
                "Fields are vectors: need equal magnitude AND opposite direction.",
                "Region rule: like charges cancel between them; unlike charges cancel outside.",
                "Set keQ₁/r₁² = keQ₂/r₂² and square-root.",
                "Contrast with V = 0 — a scalar sum with no direction condition.",
            ],
            "common_mistake": "Placing the zero point between unlike charges.",
            "check": "Charges +q and +9q, distance d apart: where is E = 0?",
            "final_takeaway": "Fields cancel head-to-head where magnitudes match; potentials cancel where signed scalars sum to zero — different points.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "A plastic straw becomes negatively charged after rubbing on wool. What moved, and what is the wool's final charge?",
        "options": [
            "Electrons moved from the WOOL to the STRAW; the wool is left with an equal POSITIVE charge",
            "Protons moved from the straw to the wool; the straw loses positive charge",
            "Electrons moved from the straw to the wool; the wool becomes negative too",
            "No transfer happens — negative charge is created out of nothing",
        ],
        "correct_index": 0,
        "explanation": "Friction transfers only electrons (mobile), never protons (nuclear). The wool loses electrons to the straw, so the straw is negative and the wool is equally positive — charge is conserved.",
        "skill": "friction charging and conservation",
        "difficulty": 1,
        "competency_code": "review-charging",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Two point charges are moved from 6 cm apart to 2 cm apart. By what factor does the electric force change, and why?",
        "options": [
            "Force ×9 — Coulomb's law is inverse-square: r dropped by 3, so (r/r′)² = 9",
            "Force ×3 — the force scales directly with distance",
            "Force ÷3 — a shorter distance means a smaller force",
            "Force ×1/9 — the force falls as the larger distance squared",
        ],
        "correct_index": 0,
        "explanation": "The factor form F₂/F₁ = (r/r′)² with r/r′ = 6/2 = 3 gives 9: distance ×3 → force ×9, because the separation enters squared and in the denominator.",
        "skill": "Coulomb scaling",
        "difficulty": 1,
        "competency_code": "review-coulomb",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Is it true that raising the voltage across a capacitor increases its capacitance, since C = Q/V?",
        "options": [
            "False — C is fixed by geometry and dielectric (C = κε₀A/d); raising V only raises the stored charge Q",
            "True — a bigger Q means a bigger C by definition",
            "True, but only while the battery is disconnected",
            "False — raising V lowers Q, so C falls",
        ],
        "correct_index": 0,
        "explanation": "C = Q/V defines capacitance but its value is set ONLY by geometry and dielectric. Doubling V doubles Q; C never moves.",
        "skill": "capacitance is geometry-bound",
        "difficulty": 1,
        "competency_code": "review-capacitance",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why do all capacitors in a series chain carry the same charge, even when their capacitances differ?",
        "options": [
            "Series means each plate charges the next by induction — the same charge flows through the whole chain",
            "Each capacitor in series is wired to its own power supply",
            "Series capacitors automatically share their charge equally",
            "Only the largest capacitor stores charge; the smaller ones stay empty",
        ],
        "correct_index": 0,
        "explanation": "In series there is one current path: the charge pushed onto the first plate's partner induces the same magnitude on the next, so every capacitor stores the SAME charge Q = CₛV regardless of its individual C.",
        "skill": "series charge sharing",
        "difficulty": 1,
        "competency_code": "review-capacitance",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "An object carries a charge of −4.8 × 10⁻⁶ C. How many excess electrons does it have?",
        "options": [
            "3.0 × 10¹³ electrons",
            "3.0 × 10¹⁰ electrons",
            "1.6 × 10¹⁹ electrons",
            "3.0 × 10¹⁹ electrons",
        ],
        "correct_index": 0,
        "explanation": "n = |Q|/e = (4.8 × 10⁻⁶)/(1.6 × 10⁻¹⁹) = 3.0 × 10¹³ electrons; the negative sign is an excess of electrons.",
        "skill": "electron counting",
        "difficulty": 2,
        "competency_code": "review-charging",
    },
    {
        "level": "APPLY",
        "prompt": "Charges +5.0 µC and −5.0 µC sit 3.0 cm apart. Find the force magnitude and its nature.",
        "options": [
            "F ≈ 250 N, ATTRACTIVE (opposite signs)",
            "F ≈ 250 N, repulsive",
            "F ≈ 500 N, attractive",
            "F ≈ 25 N, attractive",
        ],
        "correct_index": 0,
        "explanation": "F = ke·q₁q₂/r² = (8.99 × 10⁹)(25 × 10⁻¹²)/(0.03)² ≈ 250 N, and opposite signs attract.",
        "skill": "Coulomb's law with signs",
        "difficulty": 2,
        "competency_code": "review-coulomb",
    },
    {
        "level": "APPLY",
        "prompt": "A wire has cross-section 2.0 × 10⁻⁶ m², current 4.0 A, and carrier density 8.5 × 10²⁸ m⁻³. Find the drift velocity.",
        "options": [
            "v_d ≈ 1.5 × 10⁻⁴ m/s",
            "v_d ≈ 1.5 × 10⁻² m/s",
            "v_d ≈ 2.9 × 10⁻⁴ m/s",
            "v_d ≈ 8.5 × 10⁻³ m/s",
        ],
        "correct_index": 0,
        "explanation": "v_d = I/(nqA) = 4.0/[(8.5 × 10²⁸)(1.6 × 10⁻¹⁹)(2.0 × 10⁻⁶)] ≈ 1.5 × 10⁻⁴ m/s — characteristically slow.",
        "skill": "drift velocity computation",
        "difficulty": 2,
        "competency_code": "review-current-drift",
    },
    {
        "level": "APPLY",
        "prompt": "A 12-V battery charges a 4.7 µF capacitor. Find the stored charge and the stored energy.",
        "options": [
            "Q ≈ 56 µC and U ≈ 3.4 × 10⁻⁴ J",
            "Q ≈ 56 µC and U ≈ 6.8 × 10⁻⁴ J",
            "Q ≈ 2.6 µC and U ≈ 3.4 × 10⁻⁵ J",
            "Q ≈ 56 µC and U ≈ 3.4 × 10⁻² J",
        ],
        "correct_index": 0,
        "explanation": "Q = CV = (4.7 × 10⁻⁶)(12) ≈ 56 µC; U = ½CV² = ½(4.7 × 10⁻⁶)(144) ≈ 3.4 × 10⁻⁴ J.",
        "skill": "capacitor charge and energy",
        "difficulty": 2,
        "competency_code": "review-capacitance",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Using only 1-µF capacitors, design a 0.75-µF equivalent. Sketch your network.",
        "options": [
            "Two 1-µF in series (0.5 µF) in parallel with four 1-µF in series (0.25 µF) → 0.75 µF",
            "Three 1-µF in parallel (3 µF) in series with one 1-µF → 0.75 µF",
            "Two 1-µF in parallel (2 µF) in series with three 1-µF in parallel (3 µF) → 1.2 µF",
            "Six 1-µF in series → 0.75 µF",
        ],
        "correct_index": 0,
        "explanation": "0.75 = 0.5 ∥ 0.25: two in series give 0.5 µF, four in series give 0.25 µF, and joining those parallel groups adds to 0.75 µF.",
        "skill": "capacitor network design",
        "difficulty": 3,
        "competency_code": "review-capacitance",
    },
    {
        "level": "TRANSFER",
        "prompt": "Charges +q and +9q are separated by distance d. Find the point where the electric field is zero.",
        "options": [
            "d/4 from the +q charge",
            "d/8 from the +q charge",
            "d/2 from the +q charge",
            "d/3 from the +q charge",
        ],
        "correct_index": 0,
        "explanation": "Set 1/x² = 9/(d − x)² → 1/x = 3/(d − x) → d − x = 3x → x = d/4. Between like charges, nearer the smaller charge.",
        "skill": "zero-point to symbolic form",
        "difficulty": 3,
        "competency_code": "review-coulomb",
    },
    {
        "level": "TRANSFER",
        "prompt": "A wire is stretched uniformly to three times its original length at constant volume. By what factor does its resistance change?",
        "options": [
            "R ×9 — L triples and A divides by 3, so R = ρL/A scales as 3/(1/3) = 9",
            "R ×3 — only the length matters",
            "R ×1/9 — volume shrinks the resistance",
            "R ×27 — the volume constraint enters squared",
        ],
        "correct_index": 0,
        "explanation": "Constant volume links L and A: A = V₀/L, so R = ρL²/V₀ ∝ L². L ×3 → R ×9.",
        "skill": "resistivity with a constraint",
        "difficulty": 3,
        "competency_code": "review-resistance",
    },
    {
        "level": "TRANSFER",
        "prompt": "Charges +3 µC at x = 0 and −6 µC at x = 1.0 m: find the V = 0 point and explain why no E = 0 point lies between them.",
        "options": [
            "V = 0 at x ≈ 0.33 m (between, nearer the smaller charge); NO E = 0 between them because both fields point the same way (+ → −)",
            "V = 0 at x ≈ 0.67 m, and E = 0 at the same point",
            "V is never zero; E = 0 at x ≈ 0.33 m",
            "V = 0 at x ≈ 0.33 m and E = 0 there too",
        ],
        "correct_index": 0,
        "explanation": "Potentials cancel as signed scalars: 3/x = 6/(1 − x) → x = 1/3 m, closer to the weaker charge. But fields between opposite charges point the SAME way (from + toward −), so they add — no E = 0 exists between them.",
        "skill": "vector vs scalar zero conditions",
        "difficulty": 3,
        "competency_code": "review-potential",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "charge-quantization",
        "title": "Quantization of Charge",
        "taxonomy_level": "recall",
        "description": "State that charge is quantized (Q = ±Ne, e = 1.6 × 10⁻¹⁹ C) and use it to judge whether a charge is physically possible.",
        "sort_order": 1,
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
        "code": "review-charging",
        "title": "Midterm Review: Charging and Quantization",
        "taxonomy_level": "apply",
        "description": "Review electron-transfer charging, charge conservation, Q = ne electron counting, and the factor scaling of Coulomb's law.",
        "sort_order": 59,
    },
    {
        "code": "review-coulomb",
        "title": "Midterm Review: Coulomb's Law and Zero Points",
        "taxonomy_level": "apply",
        "description": "Review Coulomb forces with signs, superpose fields on a line, and locate zero-force and zero-field points by region logic.",
        "sort_order": 60,
    },
    {
        "code": "review-field-flux",
        "title": "Midterm Review: Field Superposition and Flux",
        "taxonomy_level": "apply",
        "description": "Review vector field superposition, field-line reading, and the Gauss's-law flux form Φ = q_enc/ε₀.",
        "sort_order": 61,
    },
    {
        "code": "review-potential",
        "title": "Midterm Review: Potential and Potential Energy",
        "taxonomy_level": "apply",
        "description": "Review scalar potential superposition, V = keQ/r, PE = qV, and ΔV = −Ed in uniform fields.",
        "sort_order": 62,
    },
    {
        "code": "review-capacitance",
        "title": "Midterm Review: Capacitance and Energy",
        "taxonomy_level": "apply",
        "description": "Review capacitor networks, stored energy, dielectrics, and the isolated-vs-battery-connected invariant.",
        "sort_order": 63,
    },
    {
        "code": "review-current-drift",
        "title": "Midterm Review: Current and Drift Velocity",
        "taxonomy_level": "apply",
        "description": "Review I = ΔQ/Δt and the microscopic I = nqAv_d with the bigger-wire-slower-drift rule.",
        "sort_order": 64,
    },
    {
        "code": "review-resistance",
        "title": "Midterm Review: Ohm's Law and Resistivity",
        "taxonomy_level": "apply",
        "description": "Review V = IR and R = ρL/A, including geometry constraints like constant-volume stretching.",
        "sort_order": 65,
    },
]

COMPETENCY_PREREQUISITES = [
    ("charge-quantization", "review-charging"),
    ("coulomb-force", "review-coulomb"),
    ("review-charging", "review-coulomb"),
    ("electric-field", "review-field-flux"),
    ("electric-flux", "review-field-flux"),
    ("gauss-law", "review-field-flux"),
    ("review-coulomb", "review-field-flux"),
    ("electric-potential", "review-potential"),
    ("potential-energy", "review-potential"),
    ("review-field-flux", "review-potential"),
    ("plate-capacitance", "review-capacitance"),
    ("stored-energy", "review-capacitance"),
    ("dielectric-effects", "review-capacitance"),
    ("combinations-capacitors", "review-capacitance"),
    ("review-potential", "review-capacitance"),
    ("electric-current", "review-current-drift"),
    ("drift-current", "review-current-drift"),
    ("review-capacitance", "review-current-drift"),
    ("ohms-law", "review-resistance"),
    ("resistance-resistivity", "review-resistance"),
    ("review-current-drift", "review-resistance"),
]

LESSON_COMPETENCIES = [
    {"code": "review-charging", "role": "teaches"},
    {"code": "review-coulomb", "role": "teaches"},
    {"code": "review-field-flux", "role": "teaches"},
    {"code": "review-potential", "role": "teaches"},
    {"code": "review-capacitance", "role": "teaches"},
    {"code": "review-current-drift", "role": "teaches"},
    {"code": "review-resistance", "role": "teaches"},
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

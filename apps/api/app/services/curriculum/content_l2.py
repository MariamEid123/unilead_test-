"""PHY211 — Physics, Module 1, Lecture 2: Electric Force — Coulomb's Law.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 2, Fall 2024 — 'Coulomb's
Law and the Superposition of Forces').

This bundle is imported by ``curriculum.content`` alongside the Lecture 1
bundle and seeded into the DB by ``curriculum.seed`` (bootstrap path) and
the CLI importer. Fields follow the same plain JSON-able Python conventions
as the Lecture 1 bundle.
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
    "code": "L2",
    "title": "Electric Force: Coulomb's Law and Superposition",
    "description": (
        "Lecture 2 — the inverse-square force law between point charges, the "
        "equal-and-opposite force pair, signed-direction bookkeeping for "
        "collinear charges, and the zero-force equilibrium position."
    ),
    "estimated_minutes": 80,
    "difficulty": "medium",
    "objectives": [
        "State Coulomb's law F = K|q₁||q₂|/r² in words and give K = 9 × 10⁹ N·m²/C² with the ε₀ relation K = 1/(4πε₀).",
        "Explain why charge signs must NOT be inserted into the magnitude formula; signs fix direction separately.",
        "Recognize that Fₐᵦ and F_ba form an equal-and-opposite action–reaction pair (F⃗₁₂ = −F⃗₂₁).",
        "Describe the inverse-square structure shared with gravity and the electric/gravity dominance ratio (≈ 2.3 × 10³⁹ for hydrogen).",
        "Apply the five-step superposition recipe to compute the net force on a charge from several collinear charges.",
        "Solve the zero-force-position problem: choose the region, balance |q₁|/d₁² = |q₂|/d₂², solve the quadratic, reject the out-of-segment root.",
        "Explain why the equilibrium position is independent of the test charge (K and q₃ cancel).",
    ],
    "prerequisites": [
        "Properties of electric charge and the quantization rule (Lecture 1).",
        "Charge units and the μC/nC/… prefix conversions (Lecture 1).",
        "Elementary vector addition on a line.",
        "Solving a quadratic equation.",
    ],
    "sort_order": 2,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Once a charge exists, the next question is what it does. The answer, laid down by "
            "Coulomb, is an inverse-square law: the force between two point charges grows with "
            "the product of their magnitudes and falls off as the square of the distance. The "
            "scale of that force makes electricity dominate the microscopic world — in the "
            "hydrogen atom it outranks gravity by a factor of roughly 10³⁹."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Coulomb's law (magnitude)",
        "body": "F = K|q₁||q₂| / r²   with   K = 9 × 10⁹ N·m²/C² = 1/(4πε₀)",
        "metadata": {
            "meaning": "Magnitude of the electric force between two point charges separated by distance r.",
            "when_used": "Any pair of point charges. Absolute values go in; signs determine direction afterward.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Magnitudes in, direction out",
        "body": "The formula answers ONLY 'how strong?'. Direction comes separately from the signs: like charges repel, unlike charges attract.",
    },
    {
        "section_type": "FORMULA",
        "title": "Permittivity of free space",
        "body": "ε₀ = 8.85 × 10⁻¹² C²/(N·m²)  and  K = 1/(4πε₀)",
        "metadata": {
            "meaning": "ε₀ describes how well empty space transmits the electric field; it builds the Coulomb constant.",
            "when_used": "Relating the two constants; Gauss's-law derivations in later lectures.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "The Force Pair Is Always Equal and Opposite",
        "body": (
            "F₁₂ means the force acting BY q₁ ON q₂; F₂₁ is the force by q₂ on q₁. In magnitude "
            "they are always equal — F₁₂ = F₂₁ — no matter how different the charges are. In "
            "direction F⃗₁₂ = −F⃗₂₁. A small charge never 'feels' a weaker force than the big one "
            "that pulls it: the interaction is a pair."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Action–reaction pair",
        "body": "The magnitude of the force on each member of a pair is identical; only the directions oppose. Charge size is irrelevant.",
    },
    {
        "section_type": "TEXT",
        "title": "Superposition: Many Charges, One Net Force",
        "body": (
            "When several charges act on one target, each neighbor acts independently, as if the "
            "others did not exist. The net force is the vector sum of the individual forces: "
            "F⃗₁ = F⃗₂₁ + F⃗₃₁ + ⋯. On a line this becomes a signed sum after fixing a positive "
            "direction. The discipline that prevents errors: magnitudes are computed separately, "
            "directions are decided separately, and only then are the signed values added."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Superposition of forces",
        "body": "F⃗₁ = F⃗₂₁ + F⃗₃₁ + F⃗₄₁ + ⋯  (vector sum)",
        "metadata": {"when_used": "Force on one charge due to several others."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Example — two attractions, opposite directions",
        "body": (
            "q₁ = +4 μC (left), q₂ = −6 μC (middle), q₃ = +8 μC (right), 2 m between each. "
            "Net force on q₂: q₁ pulls it toward the left with 0.054 N; q₃ pulls it toward the "
            "right with 0.108 N. Both forces are attractions, yet they point opposite ways — "
            "because the two positive charges sit on opposite sides of q₂. Net = 0.108 − 0.054 "
            "= 0.054 N in +x. Direction is signs PLUS geometry, never signs alone."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Inverse-Square Scaling",
        "body": (
            "Distance ×n forces strength ÷n². Double the distance ⇒ quarter the force; triple it "
            "⇒ one-ninth. The law cannot be read linearly: intuition that says 'twice as far, "
            "half as strong' is wrong by a factor of two."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Force scaling with distance",
        "body": "| Distance change | Force change |\n|---|---|\n| r → 2r | F → F/4 |\n| r → 3r | F → F/9 |\n| r → r/2 | F → 4F |",
        "metadata": {"note": "Only the distance is squared — each charge scales linearly."},
    },
    {
        "section_type": "TEXT",
        "title": "The Zero-Force (Equilibrium) Position",
        "body": (
            "Between two like charges the two forces pull opposite ways, so somewhere between "
            "them they cancel. The condition is |q₁|/d₁² = |q₂|/d₂². K and the test charge's "
            "magnitude cancel from both sides — the position is a property of the source charges "
            "alone. Solving gives a quadratic with two roots; ONLY the root inside the segment "
            "is physical. The surviving answer always sits closer to the smaller charge."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Equilibrium balance condition",
        "body": "|q₁|/d₁² = |q₂|/d₂²",
        "metadata": {
            "meaning": "Equal opposing force magnitudes on the test charge from the two sources.",
            "when_used": "Locating the zero-net-force point between two like charges.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Reject the out-of-segment root",
        "body": "Outside the segment both forces point the same way and can never cancel. The extra quadratic root is an artifact of squaring the distance difference.",
    },
    {
        "section_type": "TEXT",
        "title": "The Electric/Gravity Ratio in the Hydrogen Atom",
        "body": (
            "Both the electric and gravitational forces are inverse-square with the same r, so in "
            "their ratio the distances cancel. What remains is constants and masses: "
            "F_e/F_g ≈ 2.3 × 10³⁹. At atomic scales electricity governs the atom and gravity is "
            "irrelevant — a fact every student should quote, not compute, on an exam."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — Coulomb computation with mixed signs",
        "body": (
            "q₁ = +6 μC and q₂ = −3 μC are 0.2 m apart. Magnitudes: F = (9 × 10⁹)(6 × 10⁻⁶)"
            "(3 × 10⁻⁶)/(0.2)² = 4.05 N. Opposite signs ⇒ attraction. Each charge feels 4.05 N "
            "— the pair is equal and opposite."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — superposition on the middle charge",
        "body": (
            "Line: q₁ = +4 μC, q₂ = −6 μC, q₃ = +8 μC, 2 m between neighbors. Net force on q₁: "
            "q₂ attracts it toward the right (+x) with (9 × 10⁹)(4 × 10⁻⁶)(6 × 10⁻⁶)/2² = 0.054 N; "
            "q₃ repels it toward the left (−x) with (9 × 10⁹)(4 × 10⁻⁶)(8 × 10⁻⁶)/4² = 0.018 N. "
            "Net = 0.054 − 0.018 = 0.036 N in +x."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — superposition on the far charge",
        "body": (
            "Same line, target q₃: q₁ repels it rightward (+x, 0.018 N); q₂ attracts it leftward "
            "(−x, 0.108 N). Net = 0.018 − 0.108 = −0.09 N, i.e. 0.09 N in −x. Report both the "
            "magnitude and the direction."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — hydrogen atom dominance",
        "body": (
            "F_e = K e²/r² = 9 × 10⁹ × (1.6 × 10⁻¹⁹)²/r² ≈ 8.2 × 10⁻⁸ N; "
            "F_g = G mₑ m_p/r² ≈ 3.6 × 10⁻⁴⁷ N (same r). Ratio F_e/F_g ≈ 2.3 × 10³⁹. "
            "Same denominator, wildly different numerator — electricity wins."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — the silent spot",
        "body": (
            "q₁ = +4 μC at x = 2.0 m, q₂ = +8 μC at the origin, test charge between them. "
            "Balance: 4/(2 − x)² = 8/x². Cancel, cross-multiply: x² − 8x + 8 = 0. Roots: "
            "x = 6.82 m and x = 1.171 m. 6.82 lies outside the segment ⇒ reject. The silent spot "
            "is x = 1.171 m from the 8 μC charge — closer to the smaller 4 μC charge."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 6 — two protons in a nucleus",
        "body": (
            "Protons 5 × 10⁻¹⁵ m apart: F = (9 × 10⁹)(1.6 × 10⁻¹⁹)²/(5 × 10⁻¹⁵)² = 9.2 N — a "
            "macroscopic force from microscopic particles. Gravity is set aside because "
            "F_e ≫ F_g at these scales."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Signed charges in the magnitude formula",
        "body": "Coulomb's law takes absolute values. Plugging −3 μC × +5 μC yields a meaningless 'negative force'. Signs decide direction, never the formula.",
    },
    {
        "section_type": "WARNING",
        "title": "Unsquared distance",
        "body": "The distance is squared. Forgetting it turns an inverse-square law into a linear one — double the distance must give a QUARTER of the force.",
    },
    {
        "section_type": "WARNING",
        "title": "Adding magnitudes without directions",
        "body": "Opposite forces cancel partially. Example 5: 0.432 + 4.5 = 4.932 (wrong) vs. 0.432 − 4.5 = −4.068 (right). Add the signed values, not the magnitudes.",
    },
    {
        "section_type": "WARNING",
        "title": "Reading F₁₂ backwards",
        "body": "F₁₂ is the force BY q₁ ON q₂. Reverse the subscript and you reverse the direction — which makes the two forces look like they point the same way.",
    },
    {
        "section_type": "WARNING",
        "title": "The bigger charge feels the bigger force",
        "body": "False. F₁₂ = F₂₁ in magnitude always. The interaction pair is equal regardless of charge size.",
    },
    {
        "section_type": "WARNING",
        "title": "Keeping the out-of-segment root",
        "body": "In zero-force problems, only the root INSIDE the segment is physical. The other root solves the squared equation but violates the direction condition.",
    },
    {
        "section_type": "WARNING",
        "title": "The answer depends on the test charge",
        "body": "It does not — K and |q₃| cancel from both sides of the balance. The silent spot depends only on the two source charges.",
    },
    {
        "section_type": "WARNING",
        "title": "Prefix and exponent slips",
        "body": "3 μC = 3 × 10⁻⁶ C, never 3 × 10⁻³ C. Convert prefixes explicitly and handle the coefficients and the powers of ten separately.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Direction Bookkeeping with Magnitude-Only Substitution",
        "body": (
            "The formula demands absolute values, the final answer demands a direction — two steps "
            "students try to fuse. Do them in order: (1) magnitudes into the formula; (2) sign pair "
            "→ repulsion or attraction; (3) where the other charge sits; (4) push away / pull "
            "toward; (5) convert to ± along your axis. Analogy: a GPS gives distance, a compass "
            "gives heading — you don't ask the GPS for a heading. A 'negative force' from the "
            "formula is a computation error, never a direction. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Inverse-Square Scaling",
        "body": (
            "Intuition is linear — twice as far feels half as strong. The field spreads over a "
            "sphere whose area grows as r², so strength dilutes as 1/r². Analogy: a flashlight "
            "beam at double distance covers four times the area, so each patch gets a quarter of "
            "the brightness. Replace r → nr: the force becomes F/n². Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Superposition of Several Collinear Forces",
        "body": (
            "Three skills run in sequence — pairwise magnitudes, direction logic, signed addition — "
            "and a slip anywhere destroys the answer. To a first approximation, add magnitudes "
            "(4.5 + 0.432); the truth is the difference (4.068) because the forces oppose. Analogy: "
            "two people pulling a box from opposite sides — motion follows the difference, not the "
            "sum. The weak force still shifts the net; you can't ignore it. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Zero-Force (Equilibrium) Position",
        "body": (
            "Between two like charges one force pulls left and the other right; somewhere between "
            "them the weaker charge, standing closer, exactly matches the stronger one. Balance "
            "K|q₁||q₃|/(d − x)² = K|q₂||q₃|/x²; K and |q₃| cancel; solve the quadratic and keep "
            "only the root inside the segment. Analogy: a tug-of-war where the child is allowed "
            "to stand much closer to the midpoint — one placement moves nothing. The quiet spot "
            "always hugs the smaller charge. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Electric/Gravity Ratio in the Hydrogen Atom",
        "body": (
            "Two formulas, wildly different constants, 40 orders of magnitude of exponents. Same "
            "r in both ⇒ the r² cancels conceptually; only the constants and the tiny masses "
            "differ. F_e ≈ 8.2 × 10⁻⁸ N vs. F_g ≈ 3.6 × 10⁻⁴⁷ N; ratio ≈ 2.3 × 10³⁹ — gravity "
            "is irrelevant inside the atom. Difficulty: MEDIUM."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Coulomb's law: F = K|q₁||q₂|/r², an inverse-square law between point charges.\n"
            "• K = 9 × 10⁹ N·m²/C² = 1/(4πε₀); ε₀ = 8.85 × 10⁻¹² C²/(N·m²).\n"
            "• Magnitudes go in the formula; signs determine direction (like repels, unlike attracts).\n"
            "• F₁₂ = F₂₁ in magnitude; F⃗₁₂ = −F⃗₂₁ in direction — always.\n"
            "• Electric force beats gravity by ≈ 2.3 × 10³⁹ in the hydrogen atom.\n"
            "• Distance ×n ⇒ force ÷ n² (double ⇒ quarter).\n"
            "• Net force = vector sum; on a line, signed addition after fixing +x.\n"
            "• Zero net force sits BETWEEN like charges at |q₁|/d₁² = |q₂|/d₂², independent of the test charge; keep only the in-segment root."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Coulomb's law (inverse-square law) — F = K|q₁||q₂|/r², the force magnitude between two point charges.\n"
            "• F₁₂ — the force acting BY q₁ ON q₂.\n"
            "• Permittivity of free space (ε₀) — the constant K = 1/(4πε₀) is built on it.\n"
            "• Superposition — the net force on a charge is the vector sum of all individual forces acting on it.\n"
            "• Zero-force position — the point between two like charges where the opposing pulls cancel."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• F = K|q₁||q₂|/r² — pairwise force magnitude.\n"
            "• K = 9 × 10⁹ N·m²/C²; K = 1/(4πε₀); ε₀ = 8.85 × 10⁻¹² C²/(N·m²).\n"
            "• F⃗₁ = F⃗₂₁ + F⃗₃₁ + ⋯ — superposition of forces.\n"
            "• F⃗₁₂ = −F⃗₂₁ — the equal-and-opposite pair.\n"
            "• |q₁|/d₁² = |q₂|/d₂² — zero-force balance; then x = (−b ± √(b²−4ac))/2a."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Magnitudes in the formula, direction from the signs — like repels, unlike attracts. "
            "Each pair is equal and opposite, no exceptions. Double the distance, quarter the "
            "force. Many charges? Compute each pair, assign +/− along your axis, add. Want a zero "
            "net force? The charge must sit between two LIKE charges at |q₁|/d₁² = |q₂|/d₂² — "
            "solve the quadratic and keep only the root inside the segment, remembering the quiet "
            "spot hugs the smaller charge. At atomic scales electricity beats gravity by 10³⁹."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "One Charge, Many Forces: Adding Coulomb Forces Without Panic",
        "description": (
            "The five-step signed-addition recipe for superposition of electric forces from "
            "several collinear charges, including the add-the-magnitudes trap."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Superposition of electric forces from several collinear charges (signed-addition recipe)",
            "target_student": "First-year university student",
            "objective": "Compute the net force on one charge due to two or more collinear charges by computing pairwise magnitudes, assigning directions, and adding with signs — without ever adding raw magnitudes.",
            "hook": "Three charges on a ruler. The middle-right one is pushed right by one neighbor and pulled left by another. Which way does it actually move, and by how much?",
            "explanation_steps": [
                "Recap Coulomb for a single pair (magnitudes only).",
                "Introduce superposition: every neighbor acts independently.",
                "Build the recipe: fix +x → pairwise magnitudes → directions from signs + geometry → ± signs → add.",
                "Walk Example 5 with visible direction arrows (4.068 N in −x).",
                "Show the trap: 0.432 + 4.5 = 4.932 (wrong) vs. 0.432 − 4.5 = −4.068 (right).",
            ],
            "common_mistake": "Adding magnitudes (4.5 + 0.432); using signed charges inside the formula.",
            "check": "A +2 μC charge sits between a −6 μC charge on its left and a +8 μC charge on its right. Which forces point +x and which point −x?",
            "final_takeaway": "Magnitudes → directions → signs → sum. Never skip a step, never add raw magnitudes.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Silent Spot: Where a Charge Feels Nothing",
        "description": (
            "Finding the position of zero net force between two like charges: region choice, the "
            "balance equation, the quadratic, and rejecting the non-physical root."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Zero net force position between two like charges (balance, quadratic, root rejection)",
            "target_student": "First-year university student",
            "objective": "Set up and solve the zero-force-position problem: choose the correct region, balance the inverse-square expressions, solve the quadratic, and reject the non-physical root.",
            "hook": "Put a charge anywhere between two positive charges and it gets yanked. But there's exactly one spot — one silent spot — where it feels nothing, and it always hides closer to the smaller charge.",
            "explanation_steps": [
                "Why the spot must be BETWEEN the charges (opposing forces).",
                "Set up distances from both charges (x and d − x).",
                "Balance the two Coulomb magnitudes; watch K and the test charge cancel.",
                "Cross-multiply → quadratic → two roots.",
                "Physical reasoning: one root is outside the segment → reject it.",
                "The pattern: the answer is closer to the smaller charge.",
            ],
            "common_mistake": "Keeping the root x = 6.82 m; placing the charge outside the segment; assuming the answer depends on q₃.",
            "check": "Two positive charges, 9 μC and 4 μC, one meter apart. Is the silent spot closer to 9 μC or to 4 μC, and why?",
            "final_takeaway": "Between the charges, balance |q₁|/d₁² = |q₂|/d₂²; the test charge cancels; keep only the in-segment root; the spot hugs the smaller charge.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "State Coulomb's law in words, and explain why the charge signs must NOT be inserted into the formula F = K|q₁||q₂|/r².",
        "options": [
            "Force ∝ (product of charge magnitudes)/r²; signs never enter the formula — they fix direction (repulsion/attraction) separately",
            "Force ∝ (sum of charges)/r; signs are required inside the formula and flip the magnitude",
            "Force ∝ (product of charges)/r; signs are optional and only scale the answer",
            "Coulomb's law contains no distance at all; signs determine the force's magnitude",
        ],
        "correct_index": 0,
        "explanation": "The magnitude is proportional to the product of the charge MAGNITUDES, inversely proportional to r². Signs determine whether the force is repulsive or attractive — a separate decision, never inserted into the formula.",
        "skill": "formula structure",
        "difficulty": 1,
        "competency_code": "coulomb-force",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "A 20 μC charge and a 5 μC charge exert forces on each other. Which statement is true?",
        "options": [
            "The 20 μC charge exerts the larger force",
            "The 5 μC charge exerts the larger force",
            "The magnitudes are equal — F₁₂ = F₂₁ regardless of charge sizes",
            "The larger force always acts on the smaller charge",
        ],
        "correct_index": 2,
        "explanation": "The interaction is an equal-and-opposite pair: F⃗₁₂ = −F⃗₂₁. The magnitudes are always equal regardless of how different the charges are.",
        "skill": "action–reaction pair",
        "difficulty": 1,
        "competency_code": "coulomb-force",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "If the distance between two charges is halved, what happens to the force? If it is tripled?",
        "options": [
            "Halved → force ×4; tripled → force ×⅑ (F ∝ 1/r²)",
            "Halved → force ×2; tripled → force ×3",
            "Halved → force ×½; tripled → force ×3",
            "Halved → no change; tripled → force ×9",
        ],
        "correct_index": 0,
        "explanation": "The inverse-square structure means a factor n in the distance becomes 1/n² in the force: halving gives ×4, tripling gives ÷9.",
        "skill": "inverse-square scaling",
        "difficulty": 1,
        "competency_code": "coulomb-force",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why must a third charge be placed BETWEEN two like charges (rather than outside them) for the net force on it to be zero?",
        "options": [
            "Only between them do the two forces point in opposite directions; outside, both point the same way and can only add",
            "Outside the segment the forces are too weak to balance",
            "Between the charges Coulomb's law freezes; the forces disappear",
            "It can't — zero force is impossible anywhere for like charges",
        ],
        "correct_index": 0,
        "explanation": "Cancellation needs opposing forces. Between like charges one pull is left, the other right; outside the segment both pulls point the same direction and superposition can only add them.",
        "skill": "equilibrium region reasoning",
        "difficulty": 2,
        "competency_code": "zero-force-position",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "q₁ = +6 μC and q₂ = −3 μC are separated by 0.2 m. Find the magnitude of the force each exerts on the other and state its character.",
        "options": [
            "4.05 N, attraction; each charge feels 4.05 N",
            "4.05 N, repulsion; each charge feels 4.05 N",
            "8.1 N, attraction; the larger charge feels more",
            "0.405 N, attraction",
        ],
        "correct_index": 0,
        "explanation": "F = (9 × 10⁹)(6 × 10⁻⁶)(3 × 10⁻⁶)/(0.2)² = 4.05 N. Opposite signs ⇒ attraction, and each member of the pair feels the same 4.05 N.",
        "skill": "direct Coulomb computation",
        "difficulty": 2,
        "competency_code": "coulomb-force",
    },
    {
        "level": "APPLY",
        "prompt": "Line: q₁ = +4 μC, q₂ = −6 μC, q₃ = +8 μC, 2 m between neighbors. Calculate the net force on q₁ due to q₂ and q₃.",
        "options": [
            "0.036 N in +x (0.054 N rightward pull − 0.018 N leftward push)",
            "0.072 N in −x (forces added)",
            "0.036 N in −x",
            "0.054 N in +x (q₃ ignored)",
        ],
        "correct_index": 0,
        "explanation": "q₂ attracts q₁ rightward: (9 × 10⁹)(4 × 10⁻⁶)(6 × 10⁻⁶)/2² = 0.054 N (+x). q₃ repels q₁ leftward: (9 × 10⁹)(4 × 10⁻⁶)(8 × 10⁻⁶)/4² = 0.018 N (−x). Net = 0.054 − 0.018 = 0.036 N in +x.",
        "skill": "superposition with mixed interactions",
        "difficulty": 2,
        "competency_code": "force-superposition",
    },
    {
        "level": "APPLY",
        "prompt": "Same configuration: calculate the net force on q₃ due to q₁ and q₂.",
        "options": [
            "0.09 N in −x (0.018 N rightward push − 0.108 N leftward pull)",
            "0.09 N in +x",
            "0.126 N in +x (magnitudes added)",
            "0.108 N in −x (q₁ ignored)",
        ],
        "correct_index": 0,
        "explanation": "q₁ repels q₃ rightward (+x, 0.018 N); q₂ attracts q₃ leftward (−x, 0.108 N). Net = 0.018 − 0.108 = −0.09 N, reported as 0.09 N in −x.",
        "skill": "superposition with mixed interactions",
        "difficulty": 2,
        "competency_code": "force-superposition",
    },
    {
        "level": "APPLY",
        "prompt": "Two protons in a nucleus are separated by 5 × 10⁻¹⁵ m. Find the electric force between them.",
        "options": [
            "≈ 9.2 N (and gravity is negligible because F_e ≫ F_g at this scale)",
            "≈ 9.2 × 10⁻³ N",
            "≈ 0.92 N",
            "≈ 9.2 × 10⁶ N",
        ],
        "correct_index": 0,
        "explanation": "F = (9 × 10⁹)(1.6 × 10⁻¹⁹)²/(5 × 10⁻¹⁵)² = 9 × 10⁹ × 2.56 × 10⁻³⁸/2.5 × 10⁻²⁹ ≈ 9.2 N. Gravity is set aside: F_e ≫ F_g (≈10³⁹ for hydrogen).",
        "skill": "Coulomb computation + scale judgment",
        "difficulty": 2,
        "competency_code": "coulomb-force",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "q₁ = +2 μC at x = 0, q₂ = −3 μC at x = 0.4 m, q₃ = +6 μC at x = 1.0 m. Compute the net force on q₂ (magnitude and direction).",
        "options": [
            "0.1125 N in +x (0.45 N rightward − 0.3375 N leftward)",
            "0.7875 N in +x (magnitudes summed)",
            "0.1125 N in −x",
            "0.45 N in +x (q₁ ignored)",
        ],
        "correct_index": 0,
        "explanation": "q₁ attracts q₂ leftward: (9 × 10⁹)(2 × 10⁻⁶)(3 × 10⁻⁶)/0.4² = 0.3375 N (−x). q₃ attracts q₂ rightward: (9 × 10⁹)(3 × 10⁻⁶)(6 × 10⁻⁶)/0.6² = 0.45 N (+x). Net = 0.45 − 0.3375 = 0.1125 N in +x.",
        "skill": "superposition in a new geometry (target not at an end, unequal spacings)",
        "difficulty": 3,
        "competency_code": "force-superposition",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two positive charges, 9 μC and 4 μC, are fixed 1 m apart. A third charge is placed between them so the net force on it is zero. Find its distance from the 4 μC charge.",
        "options": [
            "0.4 m from the 4 μC charge (0.6 m from the 9 μC), and the result is independent of the third charge's magnitude and sign",
            "0.6 m from the 4 μC charge",
            "0.5 m from the 4 μC charge",
            "0.3 m from the 4 μC charge",
        ],
        "correct_index": 0,
        "explanation": "Balance 4/x² = 9/(1−x)² → 2/x = 3/(1−x) → 2(1−x) = 3x → x = 0.4 m from the 4 μC charge. K and the third charge cancel from both sides, so the position is fixed by the sources alone — and hugs the smaller charge.",
        "skill": "equilibrium procedure with symbolic cancellation",
        "difficulty": 3,
        "competency_code": "zero-force-position",
    },
    {
        "level": "TRANSFER",
        "prompt": "A student solves a zero-force problem and obtains roots x = 0.6 m and x = −1.4 m for charges spanning 0 < x < 2 m. Why must the negative root be rejected?",
        "options": [
            "At x = −1.4 m both forces point the same direction, so cancellation is impossible; the root is an artifact of squaring",
            "The negative root gives a force that is negative, which is physically impossible",
            "Only roots between the charges can be positive numbers",
            "The quadratic formula is only valid for positive roots",
        ],
        "correct_index": 0,
        "explanation": "The setup assumed the test charge lies between the charges so the forces oppose. Outside on the far side, both forces point the same way and can only add; squaring erases the sign of the distance difference and manufactures the impostor root.",
        "skill": "root-rejection reasoning",
        "difficulty": 3,
        "competency_code": "zero-force-position",
    },
    {
        "level": "TRANSFER",
        "prompt": "Charge q₁ = +5 μC experiences zero net force from charges q₂ and q₃ placed on either side of it. You now double both q₂ and q₃. Does q₁ still experience zero net force?",
        "options": [
            "Yes — each force scales by the same factor of 2, so the opposing magnitudes stay equal and the balance survives",
            "No — the doubling of both charges doubles the net force",
            "No — doubling changes the direction of the forces",
            "Yes — because Coulomb's law ignores charge magnitudes",
        ],
        "correct_index": 0,
        "explanation": "Each force depends linearly on each involved charge (F ∝ q). Doubling both source charges multiplies both opposing forces by 2, leaving them equal — the balance condition is preserved.",
        "skill": "proportional reasoning on the force law",
        "difficulty": 3,
        "competency_code": "force-superposition",
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
        "code": "force-superposition",
        "title": "Superposition of Electric Forces",
        "taxonomy_level": "apply",
        "description": "Compute the net force on a charge due to several collinear charges by signed vector addition.",
        "sort_order": 6,
    },
    {
        "code": "zero-force-position",
        "title": "Zero-Force Equilibrium Position",
        "taxonomy_level": "apply",
        "description": "Locate the point between two like charges where the net force is zero, keeping only the physical root.",
        "sort_order": 7,
    },
]

COMPETENCY_PREREQUISITES = [
    ("charge-properties", "coulomb-force"),
    ("charge-units", "coulomb-force"),
    ("coulomb-force", "force-superposition"),
    ("force-superposition", "zero-force-position"),
]

LESSON_COMPETENCIES = [
    {"code": "coulomb-force", "role": "teaches"},
    {"code": "force-superposition", "role": "teaches"},
    {"code": "zero-force-position", "role": "teaches"},
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

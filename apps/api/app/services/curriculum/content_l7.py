"""PHY211 — Physics, Module 5, Lecture 7: DC Circuits and RC Time Constants.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 7, Fall 2024 —
'DC Circuits: Series, Parallel, Network Reduction, Batteries in Parallel,
and RC Circuits').

The capstone of the circuits arc — and the end of the physics semester.
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
    "code": "M5",
    "title": "Module 5 — DC Circuits",
    "description": (
        "Chapter 6: series and parallel networks, the network-reduction procedure, "
        "batteries in parallel, and the RC time constant that bends DC into "
        "exponential behavior."
    ),
    "sort_order": 5,
}

LESSON = {
    "code": "L7",
    "title": "DC Circuits: Networks, Real Batteries, and the RC Time Constant",
    "description": (
        "Lecture 7 — combining resistors into single equivalents, running the "
        "network-reduction procedure, wiring batteries without reverse currents, "
        "and the RC circuit that charges and discharges exponentially against "
        "its own time constant."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Combine series resistors: same current, drops add, Req = ΣRᵢ.",
        "Combine parallel resistors: same voltage, currents add (I₁/I₂ = R₂/R₁), 1/Req = Σ1/Rᵢ, and Req is BELOW the smallest branch.",
        "Run the network-reduction procedure: merge series runs, then parallel groups, redraw, repeat — and verify with the drop-check ΣV = ℰ.",
        "Apply the two shortcuts: two parallel resistors R₁R₂/(R₁+R₂), and n identical resistors R/n.",
        "Model batteries in parallel: equal terminal voltage, shared current, matched internal-resistance rule, and the hidden reverse-current trap.",
        "Compute the RC time constant τ = RC (Ω·F = s) and the charge/current at any time: charging q = q₀(1 − e^(−t/τ)), discharging q = q₀e^(−t/τ).",
        "Recall the τ-markers: 63% charged (charging) and 37% remaining (discharging) at one time constant.",
    ],
    "prerequisites": [
        "Ohm's law V = IR (Lecture 6).",
        "emf and internal resistance V = ℰ − Ir (Lecture 6).",
        "Capacitance and stored charge C = Q/ΔV (Lecture 5).",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A circuit diagram is a wiring problem: resistors in series and parallel reduce to "
            "a single equivalent, the network-reduction procedure turns any tangle into one "
            "resistor, and then the battery's internal resistance and the RC time constant "
            "handle the rest. Two wires that LOOK parallel may hide a battery doing something "
            "unexpected, and a capacitor plus resistor DRAWS the time axis — exponential "
            "charging and discharging against τ = RC."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Series resistors",
        "body": "Req = R₁ + R₂ + ⋯    same I,   V_total = V₁ + V₂ + ⋯",
        "metadata": {
            "meaning": "One path: identical current; the drops slice the source voltage.",
            "when_used": "Chaining resistors end-to-end; V_drop across any element = I·Rᵢ.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The 169 Ω trick question",
        "body": (
            "Three resistors, 42 Ω, 17 Ω, 110 Ω, in series on a 9 V battery: Req = 169 Ω, "
            "I = 9/169 ≈ 53 mA — the same 53 mA through EVERY resistor. Drops: 42 × 0.053 = "
            "2.23 V, 17 × 0.053 = 0.90 V, 110 × 0.053 = 5.83 V. Sanity check: the drops ADD "
            "to exactly 9 V (2.23 + 0.90 + 5.83 = 8.96 ≈ 9 V ✓)."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Parallel resistors",
        "body": "1/Req = 1/R₁ + 1/R₂ + ⋯    same V,   I_total = I₁ + I₂ + ⋯,   I₁/I₂ = R₂/R₁",
        "metadata": {
            "meaning": "Same voltage across every branch; the currents split INVERSE to resistance.",
            "when_used": "Any multi-branch junction; the 'less resistance downhill' rule.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "The 16.34 Ω parallel",
        "body": (
            "65 Ω, 25 Ω, 170 Ω in parallel carrying 1.3 A: Req = 16.34 Ω — BELOW the smallest "
            "(25 Ω) branch. V across them all = 1.3 × 16.34 ≈ 21.2 V; branch currents "
            "21.2/65 = 0.33 A, 21.2/25 = 0.85 A, 21.2/170 = 0.12 A, which ADD to 1.3 A ✓. "
            "The smallest resistor carries the biggest share."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Req is always below the smallest branch",
        "body": "Adding a parallel branch can only EASE the path (more lanes). Two 6 Ω in parallel give 3 Ω — a single resistor smaller than both. Half the intuitive 'average' is a trap.",
    },
    {
        "section_type": "FORMULA",
        "title": "Two shortcuts",
        "body": "Exactly two in parallel: Req = R₁R₂/(R₁+R₂)    n identical: Req = R/n",
        "metadata": {
            "meaning": "Only for two; only for identical.",
            "when_used": "Speeding up any two-element parallel reduction; n-identical branch stacks.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Network Reduction — The Procedure",
        "body": (
            "1) Merge every pure series run (add). 2) Merge every pure parallel group "
            "(reciprocal sum, flip). 3) Redraw the smaller network. 4) Repeat until ONE "
            "resistor remains. 5) VERIFY by the drop-check: ΣV across series elements must "
            "equal the source ℰ. The redraw step is the one students skip and the one that "
            "keeps the arithmetic honest."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Mixed 35 Ω and 15 Ω ladder",
        "body": (
            "Two parallel pairs, each (35, 35) in parallel → 17.5 Ω each; those two 17.5 Ω "
            "resistors are then IN SERIES → 35 Ω total. Same two ingredients, wired twice, "
            "one answer: reduction is just applied series/parallel rules."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "RC time constant",
        "body": "τ = R·C   (Ω·F = seconds)",
        "metadata": {
            "meaning": "The circuit's own clock: one τ is 63% of the way to fully charged.",
            "when_used": "Every RC circuit; compare τ to your time axis before reading anything.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Charging and discharging",
        "body": "Charging: q(t) = q₀(1 − e^(−t/τ)),  I(t) = I₀e^(−t/τ)    Discharging: q(t) = q₀e^(−t/τ)",
        "metadata": {
            "meaning": "q₀ = Cℰ is the asymptotic charge, I₀ = ℰ/R the starting current.",
            "when_used": "Voltage across the capacitor, current through R, at any time t.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "ℰ = 12 V, R = 175 Ω, C = 55.7 μF",
        "body": (
            "τ = RC = (175)(55.7 × 10⁻⁶) = 9.75 ms; q₀ = Cℰ = 668 μC; I₀ = ℰ/R = 68 mA. After "
            "one τ: q ≈ 420 μC (63% charged) and I ≈ 25 mA (down to 37%). After 5τ the "
            "capacitor is within 1% of full — the exponential is effectively over, permanently."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The 63% / 37% markers",
        "body": "Charging: 1τ → 63% full, current at 37%. Discharging: 1τ → 37% remains. The τ-markers mirror each other: a capacitor never 'finishes' — it asymptotes.",
    },
    {
        "section_type": "TEXT",
        "title": "Batteries in Parallel",
        "body": (
            "Parallel batteries clamp each other to the SAME terminal voltage and share the "
            "load. If their emfs disagree, current flows between them, inside-out: a 'hidden "
            "reverse current' that drains a good battery warming a weak one. The safe wiring "
            "is matched emf AND matched internal resistance r — whereupon each battery "
            "supplies half the current, each drops the same r, and the pair behaves like a "
            "single emf with resistance r/2."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "The matched parallel pair",
        "body": (
            "Two 12 V batteries (r = 0.1 Ω each) in parallel feeding a 1.2 A load: each cell "
            "drives 0.6 A; each internal drop = 0.6 × 0.1 = 0.06 V; terminals read 11.94 V; "
            "equivalent battery = 12 V with r_eq = 0.05 Ω. No fighting, no reverse current — "
            "matched cells share work evenly."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — series verification by drop-check",
        "body": (
            "42 Ω, 17 Ω, 110 Ω in series on 9 V: Req = 169 Ω, I = 53 mA. Drops 2.23 V, 0.90 V, "
            "5.83 V — and they ADD to the source (8.96 ≈ 9 V ✓). Every series answer should be "
            "proof-read with ΣV = ℰ."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — parallel full distribution",
        "body": (
            "65 Ω, 25 Ω, 170 Ω in parallel carrying 1.3 A: 1/Req = 1/65 + 1/25 + 1/170 ⇒ "
            "Req = 16.34 Ω (below the smallest, 25 Ω ✓). V = 21.2 V shared; branch currents "
            "0.33 A, 0.85 A, 0.12 A — the inverse-resistance split means the LIGHTEST branch "
            "carries the HEAVIEST share. Sum back to 1.3 A ✓."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — two-step mixed reduction",
        "body": (
            "Divide the network into pure sub-networks: (35 ∥ 35) = 17.5 Ω twice, then the "
            "two 17.5 Ω appear IN SERIES ⇒ 35 Ω. Keep pure runs and pure groups separate on "
            "every pass; never cross-add."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — RC timing",
        "body": (
            "ℰ = 12 V, R = 175 Ω, C = 55.7 μF: τ = 9.75 ms, q₀ = 668 μC, I₀ = 68 mA. At "
            "t = τ: q ≈ 420 μC (63%), I ≈ 25 mA (37%). At t = 2τ: q = 668(1 − e⁻²) ≈ 578 μC "
            "(87%). The earlier times do the dramatic work."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — parallel batteries that don't fight",
        "body": (
            "Two matched 12 V cells, r = 0.1 Ω each, feeding 1.2 A: 0.6 A per cell, internal "
            "drop 0.06 V each, terminals 11.94 V, r_eq = r/2 = 0.05 Ω. Matched emf and "
            "matched r: no hidden reverse current, even split of the work."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Series shares current, not voltage",
        "body": "Same I through every element; the DROPS split in proportion to the resistances (Vᵢ = IRᵢ). The 169 Ω example shows the split — never copy a 'each resistor gets half the battery' habit.",
    },
    {
        "section_type": "WARNING",
        "title": "Parallel shares voltage, not current",
        "body": "Same V across every branch; the CURRENTS split INVERSE to resistance — the smallest resistor carries the biggest share. I₁/I₂ = R₂/R₁ is the anti-average.",
    },
    {
        "section_type": "WARNING",
        "title": "The un-flipped reciprocal again",
        "body": "1/Req = 5/12 means Req = 12/5 = 2.4 Ω, carelessly 0.42 Ω is wrong. Flip the LAST fraction and then sanity-check against the smallest branch.",
    },
    {
        "section_type": "WARNING",
        "title": "The two-shortcut limits",
        "body": "R₁R₂/(R₁+R₂) is valid ONLY for exactly two, and R/n only for n identical. Applying them beyond their boundary silently corrupts a reduction.",
    },
    {
        "section_type": "WARNING",
        "title": "Ω × F really is seconds",
        "body": "(V/A)(C/V) = C/A = s. τ = 9.75 ms, not 9.75 μs or 9.75 s — one decimal slip and every reading is off by 1000×.",
    },
    {
        "section_type": "WARNING",
        "title": "'Full' never quite happens",
        "body": "Setup: charge hard at first, asymptote at q₀. At τ it's 63%, not 100%; at 5τ ~99%. If your formula says q = q₀ at finite t, the exponential mechanics are wrong.",
    },
    {
        "section_type": "WARNING",
        "title": "Discharging is not charging mirrored",
        "body": "q = q₀e^(−t/τ) drops from q₀ TO 37% at one τ. Using the (1 − e^...) charging form here leaves 63% 'remaining' that was never there.",
    },
    {
        "section_type": "WARNING",
        "title": "Mismatched batteries in parallel",
        "body": "Different emf or different r lets a reverse current flow INSIDE the pair — a good battery current-heats a weak one. Only matched cells (equal emf AND equal r) share cleanly.",
    },
    {
        "section_type": "WARNING",
        "title": "Redraw, don't re-argue",
        "body": "The reduction's failure mode is mental algebra on a messy network. Redraw after each merge and the structure advertises the next step.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Network-Reduction Procedure",
        "body": (
            "Reduction is a LOOP, not a formula: merge series runs (add), merge parallel "
            "groups (reciprocal, flip), redraw, repeat. The redraw is the step students skip "
            "— and the reason they lose stoichiometry in combination networks. Closing the "
            "loop with the drop-check ΣV = ℰ is the proof that the ONE resistor you ended "
            "with really is the network. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The RC Time Constant",
        "body": (
            "RC is the circuit's clock, in SECONDS despite Ω and F. q = q₀(1 − e^(−t/τ)) "
            "means the capacitor charges hard at first and asymptotes toward q₀ = Cℰ — never "
            "reaching it. The same τ times the CURRENT: I₀ = ℰ/R decays to 37% each τ. "
            "'RC circuits are slow' is the scope error; τ vs your observation window decides "
            "everything. Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Batteries in Parallel: The Hidden Reverse Current",
        "body": (
            "Two parallel batteries are FORCED to the same terminal voltage. If their emfs "
            "disagree, the higher one pushes current BACKWARD through the lower cell — "
            "discharging the strong cell and heating the weak one, exactly the lecture's "
            "'mystery' of batteries that fight each other. Matched emf + matched r removes "
            "the fight: each cell halves the current, terminals read one voltage, r_eq = r/2. "
            "Difficulty: HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Voltage Division vs Current Division",
        "body": (
            "Series and parallel permute the same two variables: series SPLITS voltage and "
            "shares current; parallel splits current and shares voltage — and each split is "
            "inverse-proportional to R. I₁/I₂ = R₂/R₁ (parallel) vs V₁/V₂ = R₁/R₂ (series) "
            "is a mirror; cross them and every number inverts. Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Series-Same-Current Trap",
        "body": (
            "Common intuition: 'a big resistor in series leaves less current for the rest.' "
            "False — series is ONE path. I is identical through every element; the big "
            "resistor just takes a bigger DROP, and the drops re-add to ℰ. The 169 Ω example "
            "lives or dies on this. Difficulty: EASY."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Series: same I, drops add, Req = ΣRᵢ; verify with ΣV = ℰ.\n"
            "• Parallel: same V, currents add inverse to R (I₁/I₂ = R₂/R₁), 1/Req = Σ1/Rᵢ — Req below the smallest branch.\n"
            "• Shortcuts: two parallel R₁R₂/(R₁+R₂); n identical R/n.\n"
            "• Reduction = merge series runs, merge parallel groups, redraw, repeat.\n"
            "• Parallel batteries: matched emf AND matched r; mismatched = hidden reverse current.\n"
            "• RC: τ = RC (seconds); charging q = q₀(1 − e^(−t/τ)), discharging q = q₀e^(−t/τ).\n"
            "• τ-markers: 63% charged at 1τ (charging), 37% left at 1τ (discharging); ~99% at 5τ."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Equivalent resistance (Req) — one resistor mimicking a whole network.\n"
            "• Series network — a single path; equal I, additive drops.\n"
            "• Parallel network — shared nodes; equal V, additive currents.\n"
            "• Time constant (τ) — RC in seconds; the circuit's characteristic clock.\n"
            "• Charging asymptote (q₀) — Cℰ, approached but never reached.\n"
            "• Reverse current — the internal fighting current of mismatched parallel batteries."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• Req = R₁ + R₂ + ⋯ (series); Vᵢ = IRᵢ.\n"
            "• 1/Req = 1/R₁ + 1/R₂ + ⋯ (parallel); I₁/I₂ = R₂/R₁.\n"
            "• Two parallel: Req = R₁R₂/(R₁+R₂); n identical: Req = R/n.\n"
            "• τ = RC (Ω·F = s).\n"
            "• Charging: q = q₀(1 − e^(−t/τ)); I = I₀e^(−t/τ); q₀ = Cℰ, I₀ = ℰ/R.\n"
            "• Discharging: q = q₀e^(−t/τ).\n"
            "• Parallel matched batteries: r_eq = r/2, same ℰ."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Resistors in SERIES share ONE current and split the voltage (drops re-add to ℰ); "
            "resistors in PARALLEL share ONE voltage and split the current inverse-proportionally "
            "— Req always lands below the smallest branch. Reduce any network by merging series "
            "runs, then parallel groups, redrawing each time, until ONE resistor remains, and "
            "close with the drop-check. When capacitors enter, τ = RC sets the clock: charge "
            "builds to 63% by one τ and asymptotes at q₀ = Cℰ; discharge is the mirror, 37% "
            "remaining at one τ. Wire batteries in parallel ONLY when emf and internal "
            "resistance match — otherwise a hidden reverse current makes good cells heat weak "
            "ones. Series shares current; parallel shares voltage; the time constant is always "
            "in seconds."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "The RC Time Constant: Charging and Discharging",
        "description": (
            "τ = RC in seconds, the 63%/37% markers, and why a capacitor asymptotes toward "
            "q₀ = Cℰ instead of ever 'finishing'."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "RC time constant: τ = RC, charging q = q₀(1 − e^(−t/τ)), discharging q = q₀e^(−t/τ)",
            "target_student": "First-year university student",
            "objective": "Compute τ, q₀, and I₀; find charge and current at any time (including the τ-markers); distinguish charging from discharging forms.",
            "hook": "ℰ = 12 V, R = 175 Ω, C = 55.7 μF: the capacitor charges to 63% in 9.75 milliseconds — then spends forever chasing the last percent.",
            "explanation_steps": [
                "Define τ = RC and check the units: (V/A)(C/V) = C/A = s.",
                "Charging set-up: switch closes, capacitor starts empty, current starts at I₀ = ℰ/R.",
                "Why the charge asymptotes: as q builds, the remaining voltage falls — less push left.",
                "The equation q(t) = q₀(1 − e^(−t/τ)), q₀ = Cℰ; I(t) = I₀e^(−t/τ).",
                "The markers: 63% at 1τ, 87% at 2τ, ~99% at 5τ.",
                "Discharging: q = q₀e^(−t/τ) — 37% left at 1τ, the exact mirror of charging.",
                "Worked example with the lecture's values and time-axis sanity check.",
            ],
            "common_mistake": "Using the charging form while discharging; reading q₀ as instant; treating τ as µs/ms interchangeably; expecting 100% at finite t.",
            "check": "With ℰ = 12 V, R = 175 Ω, C = 55.7 μF, how much charge sits on the capacitor and what current flows after exactly one time constant?",
            "final_takeaway": "τ = RC is the circuit's clock in seconds: 63% charged / 37% current at 1τ while charging, 37% left at 1τ when discharging — exponential, asymptotic, never finished.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "Batteries in Parallel: The Hidden Reverse Current",
        "description": (
            "Why two parallel batteries fight each other when emfs or internal resistances "
            "mismatch — and how matching emf AND r makes them share work evenly."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Parallel battery banks: shared terminal voltage, current sharing, matched-emf/matched-r rule, reverse-current failure mode",
            "target_student": "First-year university student",
            "objective": "Explain why mismatched parallel batteries develop a hidden reverse current, and compute the behavior of a matched pair (shared current, r_eq = r/2).",
            "hook": "Two identical-looking 12 V batteries in parallel — yet the weaker one gets HOT. The stronger cell is heating it by driving current the WRONG way.",
            "explanation_steps": [
                "Parallel forces equal terminal voltage on both cells.",
                "If emfs differ, the higher-emf cell pushes current backward through the lower — the reverse current.",
                "Where the heat goes: reverse current inside the weak cell = internal I²r heating.",
                "The matched rule: equal emf AND equal internal resistance r.",
                "Matched pair under load: each cell drives half the current, equal internal drops, terms one voltage.",
                "The equivalent: same ℰ with r_eq = r/2.",
                "Worked example: two 12 V / 0.1 Ω cells supplying 1.2 A.",
            ],
            "common_mistake": "Assuming parallel batteries must split evenly; overlooking r; believing emf alone decides sharing; forgetting the reverse-current failure mode.",
            "check": "Two matched 12 V batteries (r = 0.1 Ω each) feed a 1.2 A load. How much current from each cell, what's the terminal voltage, and what is r_eq?",
            "final_takeaway": "Parallel batteries clamp to one voltage; mismatched emf or r breeds a hidden reverse current. Matched cells share evenly and act like one battery with r_eq = r/2.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "In a series circuit, which quantity is identical through every resistor, and which quantity is split?",
        "options": [
            "Identical current; the drops split proportionally to R (Vᵢ = IRᵢ), re-adding to ℰ",
            "Identical voltage; the current splits proportionally to 1/R",
            "Identical charge; the energy splits evenly",
            "Identical power; the resistance splits as 1/R",
        ],
        "correct_index": 0,
        "explanation": "Series is one path: the same I flows everywhere; each resistor takes a drop Vᵢ = IRᵢ and the drops re-add to the source voltage (drop-check).",
        "skill": "series signature",
        "difficulty": 1,
        "competency_code": "series-networks",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Why is the parallel equivalent resistance always below the smallest branch resistor?",
        "options": [
            "Each added branch is another LANE: more cross-section for the same push, so resistance can only drop below the smallest single branch",
            "Because metal wires have negative resistance",
            "Because voltage is shared equally, resistance must average to the middle",
            "It isn't — parallel Req always sits between the smallest and largest",
        ],
        "correct_index": 0,
        "explanation": "Parallel branches are parallel paths — more lanes for charge. The equivalent conductance adds and the resistance falls: Req = 1/(Σ1/Rᵢ) below every member.",
        "skill": "parallel Req bound",
        "difficulty": 2,
        "competency_code": "parallel-networks",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Two identical batteries are placed in parallel. When do they fight each other with a hidden reverse current, and when do they share cleanly?",
        "options": [
            "Fight when emf OR internal resistance r differs; share cleanly when BOTH match (each drives equal current, r_eq = r/2)",
            "They always fight regardless of matching",
            "They always share — batteries in parallel never interact",
            "Fight when emf matches; share when r differs",
        ],
        "correct_index": 0,
        "explanation": "Parallel forces a single terminal voltage; a higher emf pushes current backward through the lower cell (reverse current + heating). Matching emf AND r removes the fight: equal current each, r_eq = r/2.",
        "skill": "parallel battery bank conditions",
        "difficulty": 2,
        "competency_code": "emf-combinations",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Define the RC time constant, its unit, and the value of charge at t = τ while charging.",
        "options": [
            "τ = RC in seconds; at t = τ the capacitor holds 63% of q₀ = Cℰ — it asymptotes, never 'finishing'",
            "τ = R/C in farads; at τ it holds 50%",
            "τ = CR in hours; at τ it is 100% full",
            "τ = 1/(RC) in hertz; at τ it holds 37% while charging",
        ],
        "correct_index": 0,
        "explanation": "τ = RC: (V/A)(C/V) = C/A = s. One time constant is a 63%-of-the-way marker toward the asymptote q₀ = Cℰ; the exponential form q₀(1 − e^(−t/τ)) never reaches q₀.",
        "skill": "time constant meaning",
        "difficulty": 1,
        "competency_code": "rc-charging",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "Three resistors — 42 Ω, 17 Ω, 110 Ω — are in series on a 9 V battery. Find Req, the current, and the three drops.",
        "options": [
            "Req = 169 Ω; I ≈ 53 mA; drops 2.23 V, 0.90 V, 5.83 V (sum ≈ 9 V ✓)",
            "Req = 169 Ω; I ≈ 53 mA; drops 3 V each",
            "Req = 48 Ω; I ≈ 187 mA; drops 21.4/8.7/56 V",
            "Req = 169 Ω; I ≈ 53 mA; drops 4.5/4.5/0 V",
        ],
        "correct_index": 0,
        "explanation": "Req = 42 + 17 + 110 = 169 Ω; I = 9/169 ≈ 53 mA; Vᵢ = IRᵢ gives 2.23 V, 0.90 V, 5.83 V — the drop-check closes: they re-add to ℰ.",
        "skill": "series network + drop-check",
        "difficulty": 2,
        "competency_code": "series-networks",
    },
    {
        "level": "APPLY",
        "prompt": "Resistors of 65 Ω, 25 Ω, and 170 Ω in parallel carry a total of 1.3 A. Find Req, the shared voltage, and each branch current.",
        "options": [
            "Req = 16.34 Ω (below 25 Ω ✓); V ≈ 21.2 V; branches 0.33 A, 0.85 A, 0.12 A (sum 1.3 A ✓)",
            "Req = 86.7 Ω; V = 113 V; branches split evenly 0.43 A",
            "Req = 16.34 Ω; V = 1.3 V; branches 20/52/7.6 mA",
            "Req = 260 Ω; V = 338 V; branch currents 5.2/13.5/2 A",
        ],
        "correct_index": 0,
        "explanation": "1/Req = 1/65 + 1/25 + 1/170 ⇒ 16.34 Ω. V = I·Req = 21.2 V shared: I₁ = 21.2/65 = 0.33 A, I₂ = 21.2/25 = 0.85 A, I₃ = 21.2/170 = 0.12 A — inverse split, re-adding to 1.3 A.",
        "skill": "parallel network + current division",
        "difficulty": 2,
        "competency_code": "parallel-networks",
    },
    {
        "level": "APPLY",
        "prompt": "ℰ = 12 V, R = 175 Ω, C = 55.7 μF. Compute τ, the final charge q₀, and the initial current I₀.",
        "options": [
            "τ = 9.75 ms; q₀ = 668 μC; I₀ = 68 mA",
            "τ = 9.75 s; q₀ = 668 C; I₀ = 68 A",
            "τ = 975 μs; q₀ = 6.68 μC; I₀ = 680 mA",
            "τ = 9.75 ms; q₀ = 668 μC; I₀ = 12 A",
        ],
        "correct_index": 0,
        "explanation": "τ = RC = (175)(55.7 × 10⁻⁶) = 9.75 ms; q₀ = Cℰ = (55.7 × 10⁻⁶)(12) = 668 μC; I₀ = ℰ/R = 12/175 ≈ 68 mA.",
        "skill": "RC parameters",
        "difficulty": 2,
        "competency_code": "rc-charging",
    },
    {
        "level": "APPLY",
        "prompt": "A fully charged 100 μF capacitor (q₀ = 1.2 mC) discharges through 50 Ω. Find τ and the charge (a) at t = τ and (b) at t = 5τ.",
        "options": [
            "τ = RC = 5 ms; at τ q = q₀e⁻¹ ≈ 0.44 mC (37%); at 5τ q ≈ 8 μC (<1%)",
            "τ = 5 μs; at τ q = 0.44 μC; at 5τ q = 1.2 mC",
            "τ = 5 ms; at τ q = 0.76 mC (63%); at 5τ q = 1.2 mC",
            "τ = 500 s; at τ half is gone; at 5τ nothing remains",
        ],
        "correct_index": 0,
        "explanation": "τ = (50)(100 × 10⁻⁶) = 5 ms. Discharging uses q = q₀e^(−t/τ): at 1τ, q = 1.2e⁻¹ ≈ 0.44 mC (37% left); at 5τ, q ≈ 1.2e⁻⁵ ≈ 8 μC — effectively finished.",
        "skill": "RC discharging applications",
        "difficulty": 2,
        "competency_code": "rc-discharging",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Two 35 Ω resistors in parallel are placed IN SERIES with another identical parallel pair. Reduce the network and state the procedure you ran.",
        "options": [
            "(35 ∥ 35) = 17.5 Ω twice; the two 17.5 Ω are in series ⇒ Req = 35 Ω. My procedure: merge pure parallel groups, redraw, then merge the series run, redraw, verify by ΣV = ℰ",
            "(35 ∥ 35) = 70 Ω, then 70 + 70 = 140 Ω",
            "(35 + 35) = 70 Ω twice, then 70 ∥ 70 = 35 Ω",
            "(35 ∥ 35) = 17.5 Ω, and the two 17.5 Ω are in parallel again ⇒ 8.75 Ω",
        ],
        "correct_index": 0,
        "explanation": "Parallel pairs merge first (17.5 Ω each); the interconnecting wire puts those equivalents IN SERIES (35 Ω). The reduction loop — group, reduce, redraw, repeat — is exactly what keeps this order honest.",
        "skill": "two-step mixed reduction procedure",
        "difficulty": 2,
        "competency_code": "network-reduction",
    },
    {
        "level": "TRANSFER",
        "prompt": "Two 12 V batteries (r = 0.1 Ω each) in parallel feed a 1.2 A load. Compute each cell's current, the terminal voltage, and r_eq. What changes if one battery's r jumps to 0.5 Ω?",
        "options": [
            "Matched: 0.6 A each; terminals 11.94 V; r_eq = 0.05 Ω. With r₂ = 0.5 Ω the pair is mismatched — the fair split is lost and reverse-current heating begins",
            "Matched: 0.6 A each; terminals 12 V; r_eq = 0.1 Ω",
            "Matched: 1.2 A each; terminals 11.4 V; r_eq = 0.2 Ω",
            "Matched: 0.6 A each; terminals 11.94 V; r_eq = 0.2 Ω; mismatching changes nothing",
        ],
        "correct_index": 0,
        "explanation": "Matched cells split 1.2 A into 0.6 A each; drops 0.06 V per cell; terminals 11.94 V; r_eq = r/2 = 0.05 Ω. Mismatched r then splits current unevenly and invites the reverse-current failure — matching is the shield.",
        "skill": "parallel-battery matching and failure mode",
        "difficulty": 3,
        "competency_code": "emf-combinations",
    },
    {
        "level": "TRANSFER",
        "prompt": "A 9 V battery charges 40 μF through 250 Ω. After what time is the capacitor 63% charged, and what current flows at that instant? Then the battery is swapped for a short: how long until only 37% of the charge remains?",
        "options": [
            "τ = 10 ms (charging: 63% full, I = I₀e⁻¹ = (9/250)(0.368) ≈ 13 mA); then discharging: ANOTHER τ = 10 ms to fall to 37%",
            "τ = 10 s; 63% at 10 s at 3.6 A; discharge 37% after 5 s",
            "τ = 10 ms; charging 63% at 10 ms at 3.6 mA; discharge needs 50 ms (5τ)",
            "τ = 250 ms; 63% at 250 ms; discharge to 37% in 90 ms",
        ],
        "correct_index": 0,
        "explanation": "τ = RC = (250)(40 × 10⁻⁶) = 10 ms. Charging reaches 63% at one τ with I = I₀e⁻¹ ≈ 13 mA; the charging and discharging clocks are the SAME τ, so the drop to 37% takes another 10 ms.",
        "skill": "reusing τ across charge and discharge",
        "difficulty": 3,
        "competency_code": "rc-charging",
    },
    {
        "level": "TRANSFER",
        "prompt": "A student computes Req for 65 ∥ 25 ∥ 170 Ω by taking the average, 86.7 Ω. Identify the error and give the correct value plus its sanity bound.",
        "options": [
            "Parallel is a reciprocal sum, not an average: 1/Req = 1/65 + 1/25 + 1/170 ⇒ Req = 16.34 Ω, which satisfies the bound below the smallest (25 Ω) — 86.7 Ω fails it",
            "The average is right; Req = 86.7 Ω sits between the smallest and largest",
            "Reciprocal sum gives 65 Ω; the bound requires touching the biggest branch",
            "Average is right for parallel; only series uses reciprocals",
        ],
        "correct_index": 0,
        "explanation": "Reverting to the reciprocal-form is the fix and the bound is the proof: Req below 25 Ω or the parallel machinery is wrong. 86.7 Ω, the average, is a series-flavored instinct and fails the bound immediately.",
        "skill": "diagnosing the parallel average error",
        "difficulty": 2,
        "competency_code": "parallel-networks",
    },
]

# --- competencies ------------------------------------------------------------
COMPETENCIES = [
    {
        "code": "ohms-law",
        "title": "Ohm's Law",
        "taxonomy_level": "apply",
        "description": "Apply V = IR to resistors, treating V as the drop across and I as the current through, for ohmic materials.",
        "sort_order": 23,
    },
    {
        "code": "emf-internal-resistance",
        "title": "Electromotive Force and Internal Resistance",
        "taxonomy_level": "apply",
        "description": "Model real batteries as emf in series with internal resistance: V = ℰ − Ir and r = (ℰ − V)/I.",
        "sort_order": 25,
    },
    {
        "code": "plate-capacitance",
        "title": "Parallel-Plate Capacitance",
        "taxonomy_level": "apply",
        "description": "Compute C = Q/ΔV and C₀ = ε₀A/d, and explain why the ratio is fixed by geometry and material.",
        "sort_order": 17,
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
        "code": "network-reduction",
        "title": "Network Reduction",
        "taxonomy_level": "analyze",
        "description": "Reduce mixed-series-parallel networks by repeated merge/redraw passes and verify with the drop-check ΣV = ℰ.",
        "sort_order": 29,
    },
    {
        "code": "emf-combinations",
        "title": "Batteries in Series and Parallel",
        "taxonomy_level": "analyze",
        "description": "Combine real batteries, enforce the matched-emf/matched-r rule for parallel banks, and predict the reverse-current failure mode.",
        "sort_order": 30,
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
]

COMPETENCY_PREREQUISITES = [
    ("ohms-law", "series-networks"),
    ("ohms-law", "parallel-networks"),
    ("series-networks", "network-reduction"),
    ("parallel-networks", "network-reduction"),
    ("emf-internal-resistance", "emf-combinations"),
    ("network-reduction", "rc-charging"),
    ("plate-capacitance", "rc-charging"),
    ("rc-charging", "rc-discharging"),
]

LESSON_COMPETENCIES = [
    {"code": "series-networks", "role": "teaches"},
    {"code": "parallel-networks", "role": "teaches"},
    {"code": "network-reduction", "role": "teaches"},
    {"code": "emf-combinations", "role": "teaches"},
    {"code": "rc-charging", "role": "teaches"},
    {"code": "rc-discharging", "role": "teaches"},
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

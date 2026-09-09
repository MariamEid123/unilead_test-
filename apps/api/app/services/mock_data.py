"""
Static mock content for the PHY211 — Physics curriculum.

This is content, not state: it never changes at runtime. Mutable student
progress lives separately in services/student_state.py. This module is the
single source of truth for the *active* first-year curriculum graph; the
legacy robotics-simulation footing that keeps the reusable PID sim engine
available is fenced inside ``db/bootstrap.py`` and is not exposed here.
"""

COURSE_CODE = "PHY211"
COURSE_TITLE = "Physics"

# The initial competency set. Every new student starts at zero — no
# demonstrated competencies, no progress. Whatever they demonstrate is
# earned through the loop (diagnostic → learn → practice → review).
# The Compass services read + write this to the DB.
INITIAL_COMPETENCIES = [
    {
        "id": "charge-properties",
        "name": "Properties of Electric Charge",
        "status": "not_started",
        "progress": 0,
        "taxonomy_level": "understand",
        "description": "Describe the two types of charge, the attraction/repulsion rule, and the coulomb as the SI unit.",
    },
    {
        "id": "charge-quantization",
        "name": "Quantization of Charge",
        "status": "not_started",
        "progress": 0,
        "taxonomy_level": "recall",
        "description": "State that charge is quantized (Q = ±Ne, e = 1.6 × 10⁻¹⁹ C) and use quantization to judge whether a charge is physically possible.",
    },
    {
        "id": "charge-units",
        "name": "Charge Units and Electron Counting",
        "status": "not_started",
        "progress": 0,
        "taxonomy_level": "recall",
        "description": "Convert between coulombs and mC/μC/nC/pC and count the elementary charges in a given charge.",
    },
    {
        "id": "charge-transfer",
        "name": "Charge Transfer by Conduction",
        "status": "not_started",
        "progress": 0,
        "taxonomy_level": "apply",
        "description": "Compute final charges when conducting spheres touch, using q′ = q_t/r_t and q_i′ = q′ × r_i.",
    },
    {
        "id": "charging-methods",
        "name": "Charging Methods",
        "status": "not_started",
        "progress": 0,
        "taxonomy_level": "apply",
        "description": "Distinguish rubbing, induction, and conduction; predict the sign each method produces and the role of grounding.",
    },
]

# Directed prerequisite edges in the PHY211 competency graph:
# (pre, post) means ``pre`` must come before ``post``.
COMPETENCY_PREREQUISITES = [
    ("charge-properties", "charge-quantization"),
    ("charge-quantization", "charge-units"),
    ("charge-units", "charge-transfer"),
    ("charge-properties", "charging-methods"),
]

# Remediation content catalog. The adaptive controller matches a student's
# state to these rows by scoring competency / misconception selectors.
# Each row's selectors are the curriculum owner's single source of truth.
REMEDIATION_RESOURCES = [
    {
        "resource_code": "res-properties-interaction",
        "competency_code": "charge-properties",
        "kind": "lesson",
        "title": "The Interaction Rule",
        "body": "There are exactly two kinds of charge. Like charges repel, opposite charges attract, and the coulomb (C) is the SI unit of charge.",
        "sort_order": 0,
    },
    {
        "resource_code": "res-properties-e",
        "competency_code": "charge-properties",
        "kind": "lesson",
        "title": "The Elementary Charge",
        "body": "The electron is the smallest negative charge (q = −e) and the proton the smallest positive charge (q = +e), with e = 1.6 × 10⁻¹⁹ C.",
        "sort_order": 1,
    },
    {
        "resource_code": "res-properties-interaction-fix",
        "competency_code": "charge-properties",
        "misconception_tag": "charge_interaction_rule_misunderstood",
        "kind": "practice",
        "title": "Like Repels, Unlike Attracts",
        "body": "Same-sign pairs always repel and opposite-sign pairs always attract — that single rule predicts every interaction. An electron and a proton attract; two electrons repel.",
        "sort_order": 2,
    },
    {
        "resource_code": "res-quantization-packet",
        "competency_code": "charge-quantization",
        "kind": "lesson",
        "title": "Charge Comes in Packets",
        "body": "Charge is quantized: any charge is Q = ±Ne with N a whole number and e = 1.6 × 10⁻¹⁹ C. A charge divided by e must be an integer.",
        "sort_order": 3,
    },
    {
        "resource_code": "res-quantization-check",
        "competency_code": "charge-quantization",
        "misconception_tag": "quantization_misunderstood",
        "kind": "practice",
        "title": "Testing a Charge for Physical Plausibility",
        "body": "Divide the proposed charge by e. If the quotient is not a whole number, the charge cannot exist in nature. Example: 5.0 × 10⁻¹⁹ C ÷ (1.6 × 10⁻¹⁹ C) = 3.125 → impossible.",
        "sort_order": 4,
    },
    {
        "resource_code": "res-units-staircase",
        "competency_code": "charge-units",
        "kind": "lesson",
        "title": "The Prefix Staircase",
        "body": "mC = 10⁻³ C, μC = 10⁻⁶ C, nC = 10⁻⁹ C, pC = 10⁻¹² C. Every step down the staircase divides the charge — and the electron count — by 1000.",
        "sort_order": 5,
    },
    {
        "resource_code": "res-units-prefix-fix",
        "competency_code": "charge-units",
        "misconception_tag": "prefix_misconverted",
        "kind": "practice",
        "title": "Don't Slip a Prefix",
        "body": "Convert the prefix BEFORE dividing by e. 0.5 μC is 0.5 × 10⁻⁶ C = 5 × 10⁻⁷ C — a factor-of-a-thousand error lives in the prefix, not the mantissa.",
        "sort_order": 6,
    },
    {
        "resource_code": "res-units-counting",
        "competency_code": "charge-units",
        "kind": "worked_example",
        "title": "Counting Electrons",
        "body": "N = |Q|/e. For −64 μC: (64 × 10⁻⁶)/(1.6 × 10⁻¹⁹) = 4 × 10¹⁴ electrons. A count is never negative — both minus signs cancel.",
        "sort_order": 7,
    },
    {
        "resource_code": "res-transfer-qprimer",
        "competency_code": "charge-transfer",
        "kind": "lesson",
        "title": "When Conducting Spheres Touch",
        "body": "Contact charges the same sign as the charger. Equal spheres split the total equally; unequal spheres split in proportion to radius: q′ = q_t/r_t, then q_i′ = q′ × r_i.",
        "sort_order": 8,
    },
    {
        "resource_code": "res-transfer-conservation-fix",
        "competency_code": "charge-transfer",
        "misconception_tag": "charge_conservation_misunderstood",
        "kind": "practice",
        "title": "Charge Is Conserved",
        "body": "The total charge is the algebraic sum of all initial charges (minus signs matter). Final charges must add back to exactly that total — that's your built-in check.",
        "sort_order": 9,
    },
    {
        "resource_code": "res-transfer-ratio",
        "competency_code": "charge-transfer",
        "kind": "worked_example",
        "title": "The Radius Ratio",
        "body": "Final charges come out in the ratio of the radii: q₁′/q₂′ = r₁/r₂. A 2:1 radius pair after contact always ends 2:1 in charge, whatever the sizes.",
        "sort_order": 10,
    },
    {
        "resource_code": "res-methods-comparison",
        "competency_code": "charging-methods",
        "kind": "lesson",
        "title": "Three Ways to Charge",
        "body": "Rubbing: insulators, direct contact, electrons move. Induction: conductors, no contact, opposite sign, ground wire in the loop. Conduction: conductors, direct contact, same sign.",
        "sort_order": 11,
    },
    {
        "resource_code": "res-methods-grounding-fix",
        "competency_code": "charging-methods",
        "misconception_tag": "grounding_direction_misunderstood",
        "kind": "practice",
        "title": "Which Way Do Electrons Go?",
        "body": "A negative rod near a grounded sphere pushes electrons from the sphere into the ground — the sphere is left POSITIVE. Disconnect the ground while the rod is still near, then remove the rod.",
        "sort_order": 12,
    },
    {
        "resource_code": "res-methods-induction",
        "competency_code": "charging-methods",
        "kind": "worked_example",
        "title": "The Induction Procedure",
        "body": "Order matters: bring the rod near (never touch) → ground the sphere → disconnect the ground → remove the rod. The result is always the OPPOSITE sign of the charging object.",
        "sort_order": 13,
    },
]

INITIAL_OVERALL_PROGRESS = 0

DIAGNOSTIC_QUESTIONS = [
    {
        "id": "q1",
        "competency_id": "charge-properties",
        "prompt": "Which statement correctly describes how electric charges interact?",
        "options": [
            {"id": "a", "label": "Like charges attract; opposite charges repel"},
            {"id": "b", "label": "Like charges repel; opposite charges attract"},
            {"id": "c", "label": "Charges always attract one another"},
            {"id": "d", "label": "Charges never exert forces at a distance"},
        ],
    },
    {
        "id": "q2",
        "competency_id": "charge-quantization",
        "prompt": "Which of the following charges could exist in nature?",
        "options": [
            {"id": "a", "label": "+3e"},
            {"id": "b", "label": "+1.5e"},
            {"id": "c", "label": "−2.5e"},
            {"id": "d", "label": "0.5e"},
        ],
    },
    {
        "id": "q3",
        "competency_id": "charge-units",
        "prompt": "A charge of 0.5 μC equals how many coulombs?",
        "options": [
            {"id": "a", "label": "5 × 10⁻⁷ C"},
            {"id": "b", "label": "5 × 10⁻⁶ C"},
            {"id": "c", "label": "0.5 × 10⁻³ C"},
            {"id": "d", "label": "5 × 10⁻⁸ C"},
        ],
    },
    {
        "id": "q4",
        "competency_id": "charge-transfer",
        "prompt": "A charged metal sphere carrying 6 C touches an identical neutral sphere. After they are separated, the charge on each sphere is:",
        "options": [
            {"id": "a", "label": "6 C on the first and 0 C on the second"},
            {"id": "b", "label": "3 C on each"},
            {"id": "c", "label": "6 C on each"},
            {"id": "d", "label": "0 C on both"},
        ],
    },
    {
        "id": "q5",
        "competency_id": "charging-methods",
        "prompt": "A negatively charged rod is held near, but never touches, a grounded neutral metal sphere. The ground wire is disconnected first, then the rod is removed. The sphere ends up:",
        "options": [
            {"id": "a", "label": "neutral"},
            {"id": "b", "label": "negatively charged"},
            {"id": "c", "label": "positively charged"},
            {"id": "d", "label": "impossible to charge without touching"},
        ],
    },
]

LESSON_SECTIONS = {
    "charge-transfer": [
        {
            "id": "sec-1",
            "heading": "What is Charge Transfer?",
            "body": (
                "Charge transfer is the motion of free electrons between conductors that touch. "
                "The object that gave electrons away ends positive; the one that accepted them "
                "ends negative — conduction always leaves the touched object with the same sign "
                "as the charger."
            ),
        },
        {
            "id": "sec-2",
            "heading": "The Algebra of Sharing: q′ = q_t / r_t",
            "body": (
                "Equal spheres split the total charge equally, but unequal spheres share in "
                "proportion to their radii: compute q′ = q_t / r_t (total charge over total "
                "radius, algebraic sum — minus signs matter), then multiply by each radius, "
                "q_i′ = q′ × r_i. The final charges must sum back to q_t."
            ),
        },
        {
            "id": "sec-3",
            "heading": "Why Prediction Matters",
            "body": (
                "Computing the final charges before the spheres ever touch lets you predict the "
                "outcome of an experiment, check conservation, and catch sign errors — the same "
                "reasoning discipline used everywhere in physics."
            ),
        },
    ],
}

PRACTICE_TASKS = {
    "charge-transfer": {
        "id": "ct-001",
        "title": "Predict the Final Charges on Two Touching Spheres",
        "objective": "Practice predicting charge-sharing outcomes for conducting spheres before computing them.",
        "requirements": [
            "State whether the spheres gain the same sign as the charger",
            "Compute the final charge on each sphere (q′ = q_t/r_t, then q_i′ = q′ × r_i)",
            "Verify the final charges conserve the original total",
        ],
        "hints": [
            "The total charge is an algebraic sum — negative charges subtract",
            "Bigger spheres take bigger shares: the split follows the radii, not a coin flip",
        ],
    },
}

EVIDENCE_TEMPLATE = [
    {"id": "diagnostic", "label": "Diagnostic demonstrated understanding", "met": True},
    {"id": "reasoning", "label": "Reasoning demonstrated with AI Coach", "met": True},
    {"id": "practice", "label": "Practice task completed", "met": True},
    {"id": "transfer", "label": "Transfer not demonstrated yet", "met": False},
]
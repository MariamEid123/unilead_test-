"""MAT111 — Mathematics 1 (AIU first-year calculus course).

Structured curriculum bundles derived from the official MAT111 material:
problem sheets 1–10, the course formula sheet, Maclaurin-expansion notes and
the L'Hospital tutorial. Each bundle is one module + one lesson (the same
importer contract as the physics course) and is imported idempotently by
``curriculum.seed`` together with the PHY211 bundles.

Sheet map:
  Sheet 1  → L1  Derivatives of inverse trigonometric functions
  Sheet 2  → L2  Hyperbolic functions and their derivatives
  Sheet 3  → L3  Limits with L'Hospital's rule
  Sheet 4  → L4  Maclaurin expansions
  Sheets 5 → L5–L10  Integration: basic rules, inverse-trig/hyperbolic
             integrals, trigonometric powers, by parts, partial fractions,
             by substitution.

Fields are plain JSON-able Python, same conventions as the physics bundles.
"""

from __future__ import annotations

COURSE_CODE = "MAT111"
COURSE_TITLE = "Mathematics 1"
COURSE_CREDITS = 3
COURSE_DESCRIPTION = (
    "Mathematics 1 (MAT111) — first-year core course. Starts with "
    "differentiation of transcendental functions (inverse trig, hyperbolic), "
    "moves through limits and Maclaurin expansions, then the full toolkit of "
    "integration techniques. Built on the competency-graph and "
    "evidence-based learning model of the Arete platform."
)

DEPARTMENT_CODE = "MATH"
DEPARTMENT_NAME = "Mathematics"
FACULTY_CODE = "ENG"
FACULTY_NAME = "Faculty of Engineering"

MODULE_DERIVATION = {
    "code": "M1",
    "title": "Module 1 — Differentiation of Transcendental Functions",
    "description": (
        "Inverse trigonometric and hyperbolic functions: their derivatives "
        "and the identities that keep the calculus consistent."
    ),
    "sort_order": 1,
}

MODULE_APPLICATIONS = {
    "code": "M2",
    "title": "Module 2 — Applications of Differentiation",
    "description": (
        "Limits evaluated with L'Hospital's rule and Maclaurin expansions of "
        "elementary functions."
    ),
    "sort_order": 2,
}

MODULE_INTEGRATION = {
    "code": "M3",
    "title": "Module 3 — Integration",
    "description": (
        "The standard integration toolkit: basic rules, inverse-trig and "
        "hyperbolic integrals, powers of trig functions, by parts, partial "
        "fractions and substitution."
    ),
    "sort_order": 3,
}

# --- L1 ---------------------------------------------------------------

L1_OBJECTIVES = [
    "Write down the derivative rules for sin⁻¹u, cos⁻¹u, tan⁻¹u and sec⁻¹u.",
    "Differentiate composites using the chain rule with inverse-trig inner functions.",
    "Differentiate implicit and parametric equations and find the second derivative.",
]
L1_PREREQUISITES = [
    "The chain rule and the quotient rule.",
    "Implicit differentiation.",
]
L1_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Inverse trigonometric functions appear constantly in geometry and "
            "integration. Their derivatives are pure algebra: each one is built "
            "from a right-triangle relation plus the chain rule. Because sin⁻¹x "
            "only exists where |x| ≤ 1, every √(1 − u²) below comes with a domain "
            "requirement in mind."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Derivative rules for inverse trig functions",
        "body": (
            "d/dx sin⁻¹(u) = u′/√(1 − u²)      |u| < 1\n"
            "d/dx cos⁻¹(u) = −u′/√(1 − u²)     |u| < 1\n"
            "d/dx tan⁻¹(u) = u′/(1 + u²)\n"
            "d/dx cot⁻¹(u) = −u′/(1 + u²)\n"
            "d/dx sec⁻¹(u) = u′/(|u|√(u² − 1))   |u| > 1\n"
            "d/dx csc⁻¹(u) = −u′/(|u|√(u² − 1))  |u| > 1"
        ),
        "metadata": {
            "note": "The ± signs follow the same pairing as the ordinary trig functions: cosine, cotangent and cosecant derivatives carry a minus sign.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 1)",
        "body": (
            "Let y = tan⁻¹ x sin x + x/(x − 1). "
            "Using the product rule on the first term and the quotient rule on the second: "
            "y′ = [1/(1 + x²)]·sin x + tan⁻¹ x·cos x + [(x − 1) − x]/(x − 1)² "
            "= sin x/(1 + x²) + tan⁻¹ x cos x − 1/(x − 1)²."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Signs come in pairs",
        "body": (
            "tan⁻¹ and sec⁻¹ are positive; cos⁻¹, cot⁻¹ and csc⁻¹ are negative. "
            "If you know the positive one you know the negative one for free."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "Don't square the u prematurely",
        "body": (
            "The rule is d/dx(tan⁻¹ u) = u′/(1 + u²) — the u² is inside the "
            "denominator, and u′ is applied by the chain rule. For u = 3x², "
            "use u′ = 6x: d/dx tan⁻¹(3x²) = 6x/(1 + 9x⁴)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Six inverse-trig derivative rules, four of them with a sign. "
            "Everything else is the chain rule on the inner function u."
        ),
    },
]
L1_PRACTICE = [
    {
        "prompt": "d/dx sin⁻¹(u) = ?",
        "options": ["u′/√(1 − u²)", "−u′/√(1 − u²)", "u′/(1 + u²)", "u′/√(u² − 1)"],
        "correct_index": 0,
        "explanation": "sin⁻¹ has positive derivative u′/√(1 − u²), valid for |u| < 1.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "inverse-trig derivatives",
    },
    {
        "prompt": "d/dx tan⁻¹(3x²) = ?",
        "options": ["6x/(1 + 9x⁴)", "3x²/(1 + x⁶)", "6x/(1 + 3x⁴)", "2x/(1 + 9x²)"],
        "correct_index": 0,
        "explanation": "Chain rule: (1/(1 + u²))·u′ with u = 3x², u′ = 6x gives 6x/(1 + 9x⁴).",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "inverse-trig derivatives",
    },
    {
        "prompt": "d/dx sec⁻¹(u) = ?",
        "options": ["u′/(|u|√(u² − 1))", "u′/(u√(1 − u²))", "−u′/(|u|√(u² − 1))", "u′/√(1 − u²)"],
        "correct_index": 0,
        "explanation": "sec⁻¹ has positive derivative u′/(|u|√(u² − 1)), valid for |u| > 1.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "inverse-trig derivatives",
    },
]
L1_LINKS = [
    {"code": "inv-trig-deriv", "role": "teaches"},
    {"code": "chain-rule", "role": "requires"},
]

# --- L2 ---------------------------------------------------------------

L2_OBJECTIVES = [
    "Define sinh, cosh, tanh and the reciprocal hyperbolic functions from eˣ.",
    "Apply the key identities: cosh²x − sinh²x = 1 and the double-angle forms.",
    "Differentiate hyperbolic functions and their inverses.",
]
L2_PREREQUISITES = [
    "Exponential functions and the chain rule.",
    "Interpreting a derivative table.",
]
L2_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Hyperbolic functions are built from exponentials — they are not new "
            "transcendental functions, just convenient combinations. That is why "
            "their identities mirror the trig ones almost one-for-one, with the "
            "double-angle and half-angle formulas carrying a sign."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Definitions",
        "body": (
            "sinh x = (eˣ − e⁻ˣ)/2    cosh x = (eˣ + e⁻ˣ)/2\n"
            "tanh x = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)    coth x = (eˣ + e⁻ˣ)/(eˣ − e⁻ˣ)\n"
            "sech x = 2/(eˣ + e⁻ˣ)    csch x = 2/(eˣ − e⁻ˣ)"
        ),
        "metadata": {
            "meaning": "sinh is the odd combination, cosh the even one.",
            "when_used": "Any hyperbolic identity or derivative problem.",
        },
    },
    {
        "section_type": "TABLE",
        "title": "Key relations",
        "body": (
            "cosh²x − sinh²x = 1\n"
            "1 − tanh²x = sech²x    coth²x − 1 = csch²x\n"
            "sinh(2x) = 2 sinh x cosh x\n"
            "cosh(2x) = cosh²x + sinh²x = 1 + 2 sinh²x = 2 cosh²x − 1"
        ),
        "metadata": {"note": "The trig identity cos²x + sin²x = 1 becomes cosh²x − sinh²x = 1."},
    },
    {
        "section_type": "TABLE",
        "title": "Derivatives (Sheet 2)",
        "body": (
            "d/dx sinh(u) = cosh(u)·u′     d/dx cosh(u) = sinh(u)·u′\n"
            "d/dx tanh(u) = sech²(u)·u′     d/dx coth(u) = −csch²(u)·u′\n"
            "d/dx sech(u) = −sech(u)tanh(u)·u′   d/dx csch(u) = −csch(u)coth(u)·u′"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 2)",
        "body": (
            "Differentiate y = sin²(3x). Rewrite as y = (sin 3x)² and use the "
            "chain rule twice: y′ = 2 sin(3x)·cos(3x)·3 = 6 sin(3x) cos(3x) "
            "= 3 sin(6x)."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Every hyperbolic derivative comes from the exponential definition. "
            "The only things to memorise are the sign of each rule and the "
            "cosh²x − sinh²x = 1 family."
        ),
    },
]
L2_PRACTICE = [
    {
        "prompt": "cosh²x − sinh²x = ?",
        "options": ["1", "0", "2", "cosh(2x)"],
        "correct_index": 0,
        "explanation": "The central hyperbolic identity, mirroring cos²x + sin²x = 1 with a minus.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "hyperbolic identities",
    },
    {
        "prompt": "d/dx cosh(u) = ?",
        "options": ["sinh(u)·u′", "−sinh(u)·u′", "cosh(u)·u′", "sech²(u)·u′"],
        "correct_index": 0,
        "explanation": "Unlike d/dx cos(u) = −sin(u)·u′, the hyperbolic derivative keeps the plus sign.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "hyperbolic derivatives",
    },
    {
        "prompt": "d/dx tanh(4x) = ?",
        "options": ["4 sech²(4x)", "sech²(4x)", "4 sech²(4x) tanh(4x)", "4 tanh²(4x)"],
        "correct_index": 0,
        "explanation": "d/dx tanh(u) = sech²(u)·u′ with u = 4x, u′ = 4.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "hyperbolic derivatives",
    },
]
L2_LINKS = [
    {"code": "hyperbolic-deriv", "role": "teaches"},
    {"code": "chain-rule", "role": "requires"},
]

# --- L3 ---------------------------------------------------------------

L3_OBJECTIVES = [
    "State L'Hospital's rule for 0/0 and ∞/∞ forms.",
    "Recognise when a limit needs L'Hospital and apply it repeatedly.",
    "Evaluate first-year limits by combining the rule with Maclaurin series.",
]
L3_PREREQUISITES = [
    "Limits and continuity from school calculus.",
    "Differentiation of polynomials, exponentials, logs and trig functions.",
]
L3_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Many first-year limits look like 0/0: sin⁻¹(4x)/x, ln(1 + 2x)/x, "
            "(eˣ − 1)/x. L'Hospital gives a fast verdict — differentiate the "
            "numerator and denominator separately, then take the limit again. "
            "When a 0/0 survives, apply it again, and it interacts cleanly with "
            "the Maclaurin expansions from Sheet 4."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "L'Hospital's rule",
        "body": (
            "If lim f(x) = lim g(x) = 0 (or ±∞) as x → a, and lim f′(x)/g′(x) "
            "exists, then lim f(x)/g(x) = lim f′(x)/g′(x)."
        ),
        "metadata": {
            "meaning": "Replaces a 0/0 or ∞/∞ ratio by the ratio of derivatives.",
            "when_used": "Only after confirming the indeterminate form — never on e.g. 1/2.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 3)",
        "body": (
            "Evaluate lim[x→0] (sin⁻¹(4x) + ln(1 + 5x))/(x cos 3x). "
            "Both parts vanish at x = 0 (0/0). Differentiate: numerator "
            "4/√(1 − 16x²) + 5/(1 + 5x); denominator cos 3x − 3x sin 3x. "
            "At x = 0 the ratio is 4 + 5 = 9."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Check the form first",
        "body": (
            "Plug x = a into numerator and denominator. If you get 0/0, ∞/∞, "
            "0·∞, 1^∞ or ∞ − ∞ you may need L'Hospital (or a series). If you "
            "get an ordinary number, that IS the answer."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Confirm the indeterminate form, differentiate top and bottom "
            "separately, re-evaluate. Repeat until a real number appears."
        ),
    },
]
L3_PRACTICE = [
    {
        "prompt": "lim[x→0] (sin x)/x = ?",
        "options": ["1", "0", "∞", "undefined"],
        "correct_index": 0,
        "explanation": "0/0 form; L'Hospital: cos x/1 → 1 at x = 0.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "lhopital",
    },
    {
        "prompt": "lim[x→0] (eˣ − 1)/x = ?",
        "options": ["1", "0", "e", "undefined"],
        "correct_index": 0,
        "explanation": "0/0 form; L'Hospital: eˣ/1 → 1.",
        "level": "APPLY",
        "difficulty": 1,
        "skill": "lhopital",
    },
    {
        "prompt": "lim[x→0] (1 − cos x)/x² = ?",
        "options": ["1/2", "0", "1", "−1/2"],
        "correct_index": 0,
        "explanation": "0/0 twice: first derivative sin x/(2x), second cos x/2 → 1/2. Equivalently Maclaurin 1 − cos x ≈ x²/2.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "lhopital",
    },
    {
        "prompt": "When may you legitimately use L'Hospital's rule?",
        "options": [
            "The limit is of form 0/0 or ∞/∞",
            "Any time a limit looks hard",
            "Only when the denominator is a constant",
            "Only when x → ∞",
        ],
        "correct_index": 0,
        "explanation": "L'Hospital applies to indeterminate 0/0 and ∞/∞ forms (after verifying the form).",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "lhopital",
    },
]
L3_LINKS = [
    {"code": "limits-lhopital", "role": "teaches"},
    {"code": "chain-rule", "role": "requires"},
]

# --- L4 ---------------------------------------------------------------

L4_OBJECTIVES = [
    "Write the Maclaurin formula f(x) = Σ f⁽ⁿ⁾(0)xⁿ/n!.",
    "Expand eˣ, sin x, cos x, ln(1 + x) and (1 + x)ⁿ from memory.",
    "Multiply, divide and compose standard series to reach the required order.",
]
L4_PREREQUISITES = [
    "Taylor's theorem and derivatives to arbitrary high order.",
    "Limits (Sheet 3) and the informal notion 1/n! ≈ 0 for large n within range.",
]
L4_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A Maclaurin expansion approximates a smooth function near 0 as a "
            "power series. For the functions of this course the pattern is "
            "regular, so engineers substitute: sin(2x) → 2x − (8x³)/6 + …, "
            "e^{3x} → 1 + 3x + (9x²)/2 + …. Products and quotients are handled "
            "by multiplying the truncated series and keeping terms up to the "
            "target order."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Maclaurin series (standard, Sheet 4 / formula sheet)",
        "body": (
            "eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! + ⋯\n"
            "sin x = x − x³/3! + x⁵/5! − ⋯\n"
            "cos x = 1 − x²/2! + x⁴/4! − ⋯\n"
            "sinh x = x + x³/3! + x⁵/5! + ⋯\n"
            "cosh x = 1 + x²/2! + x⁴/4! + ⋯\n"
            "ln(1 + x) = x − x²/2 + x³/3 − x⁴/4 + ⋯\n"
            "(1 + x)ⁿ = 1 + nx + n(n−1)x²/2! + n(n−1)(n−2)x³/3! + ⋯"
        ),
        "metadata": {
            "meaning": "The five series most often substituted into one another.",
            "when_used": "Expansions of products, quotients, powers and limits.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 4)",
        "body": (
            "Expand f(x) = x e^{3x} up to x³: e^{3x} = 1 + 3x + 9x²/2 + 27x³/6, "
            "so x e^{3x} = x + 3x² + (9/2)x³ + (27/6)x⁴ — the x⁴ term is 4.5x⁴, "
            "already beyond the requested order."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Keep only terms up to the target order",
        "body": (
            "When you expand a product of two series, every term whose power "
            "exceeds the requested order is discarded. Count powers carefully — "
            "that is where most mistakes in Sheet 4 proof problems are born."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Maclaurin turns functions into polynomials. Substitute the standard "
            "series, truncate at the target order, and combine products/quotients "
            "by multiplying the polynomials."
        ),
    },
]
L4_PRACTICE = [
    {
        "prompt": "The Maclaurin series of cos x starts:",
        "options": ["1 − x²/2! + x⁴/4! − ⋯", "1 + x²/2! + x⁴/4! + ⋯", "x − x³/3! + x⁵/5! − ⋯", "1 − x + x² − x³ + ⋯"],
        "correct_index": 0,
        "explanation": "cos x is even and cos 0 = 1, so only even powers appear, alternating in sign.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "maclaurin",
    },
    {
        "prompt": "e^{3x} up to x² equals:",
        "options": ["1 + 3x + (9/2)x²", "1 + 3x + 3x²", "1 + x²/2", "1 + 3x + 9x²"],
        "correct_index": 0,
        "explanation": "Substitute u = 3x into eᵘ = 1 + u + u²/2: 1 + 3x + (9/2)x².",
        "level": "APPLY",
        "difficulty": 1,
        "skill": "maclaurin",
    },
    {
        "prompt": "Keeping terms up to x³, x·sin(2x) ≈ ?",
        "options": ["2x² − (8/6)x⁴", "2x − (8/6)x³", "2x² + (8/3)x⁴", "x + x³/6"],
        "correct_index": 0,
        "explanation": "sin(2x) ≈ 2x − (8x³)/6; multiplying by x gives 2x² − (8/6)x⁴.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "maclaurin",
    },
]
L4_LINKS = [
    {"code": "maclaurin", "role": "teaches"},
    {"code": "limits-lhopital", "role": "requires"},
]

# --- L5 ---------------------------------------------------------------

L5_OBJECTIVES = [
    "Recite the power rule, exponential rule and the basic trig integrals.",
    "Recognise u′/u type integrands and integrate to ln|u|.",
    "Integrate simple composites by inspection of the u′ factor.",
]
L5_PREREQUISITES = [
    "The derivative rules (Sheets 1–2) — integration is their inverse.",
    "Algebraic manipulation of powers and fractions.",
]
L5_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Integration is differentiation in reverse. Most basic integrals are "
            "read directly off the derivative table: if d/dx F = f then ∫f dx = "
            "F + c. The generalised rules (the u′-formulas) handle composites in "
            "one glance, exactly as the chain rule does for derivatives."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Standard general integrals (Sheet 5)",
        "body": (
            "∫uⁿu′dx = uⁿ⁺¹/(n+1) + c,  n ≠ −1\n"
            "∫(u′/u)dx = ln|u| + c\n"
            "∫eᵘu′dx = eᵘ + c\n"
            "∫sin(u)u′dx = −cos(u) + c      ∫cos(u)u′dx = sin(u) + c\n"
            "∫sec²(u)u′dx = tan(u) + c      ∫sec(u)tan(u)u′dx = sec(u) + c\n"
            "∫csc²(u)u′dx = −cot(u) + c     ∫csc(u)cot(u)u′dx = −csc(u) + c"
        ),
        "metadata": {"note": "Check any basic integral by differentiating the answer."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 5)",
        "body": (
            "∫ (2x)/(x² + 1) dx: notice u = x² + 1 has u′ = 2x, so the integrand "
            "is u′/u → ln|x² + 1| + c."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The u′-factor is the fingerprint",
        "body": (
            "A composite integrand almost always contains a piece equal to u′ "
            "(today) multiplied by something you know how to integrate. Locate "
            "u′ and the rest is a table lookup."
        ),
    },
    {
        "section_type": "WARNING",
        "title": "n = −1 is special",
        "body": (
            "∫u⁻¹u′dx is NOT u⁰/0; it is ln|u| + c. The power rule formula "
            "only holds for n ≠ −1."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Read the generalised formulas as 'derivative table in reverse with "
            "a u′ factor'. Half of every technique lesson is training you to "
            "spot that factor."
        ),
    },
]
L5_PRACTICE = [
    {
        "prompt": "∫xⁿdx (n ≠ −1) = ?",
        "options": ["xⁿ⁺¹/(n+1) + c", "xⁿ⁻¹/(n−1) + c", "nxⁿ⁻¹ + c", "ln|x| + c"],
        "correct_index": 0,
        "explanation": "Power rule for integration: increase the exponent by 1 and divide.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "basic integration",
    },
    {
        "prompt": "∫ (1/u)·u′ dx = ?",
        "options": ["ln|u| + c", "u²/2 + c", "1/u + c", "eᵘ + c"],
        "correct_index": 0,
        "explanation": "The u′/u form integrates to the natural log of |u|.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "basic integration",
    },
    {
        "prompt": "∫ 3x²·e^{x³} dx = ?",
        "options": ["e^{x³} + c", "e^{x³}/3 + c", "3e^{x³} + c", "x³e^{x³} + c"],
        "correct_index": 0,
        "explanation": "u = x³ has u′ = 3x², so the integrand is eᵘu′ → e^{x³} + c.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "basic integration",
    },
]
L5_LINKS = [
    {"code": "basic-integration", "role": "teaches"},
    {"code": "chain-rule", "role": "requires"},
]

# --- L6 ---------------------------------------------------------------

L6_OBJECTIVES = [
    "Recognise the five inverse-trig and inverse-hyperbolic integrations by shape.",
    "Scale a² correctly when pulling 1/a from the arctan/tanh form.",
    "Integrate sinh and cosh composites.",
]
L6_PREREQUISITES = [
    "Basic integration rules (Sheet 5).",
    "The inverse-trig derivative table (Sheet 1).",
]
L6_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Sheet 6 collects the integrals whose answers are inverse-trig and "
            "inverse-hyperbolic functions. They are recognisable by shape: "
            "1/(a² + u²), 1/√(a² − u²), 1/√(a² + u²), 1/(a² − u²), 1/√(u² − a²). "
            "The trick is deciding which a to factor out."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "The five shapes (Sheet 6)",
        "body": (
            "∫u′/(a² + u²)dx = (1/a)tan⁻¹(u/a) + c\n"
            "∫u′/(a² − u²)dx = (1/a)tanh⁻¹(u/a) + c\n"
            "∫u′/√(a² − u²)dx = sin⁻¹(u/a) + c\n"
            "∫u′/√(a² + u²)dx = sinh⁻¹(u/a) + c\n"
            "∫u′/√(u² − a²)dx = cosh⁻¹(u/a) + c"
        ),
        "metadata": {"note": "arcosh and artanh also admit log forms: tanh⁻¹x = ½ln((1+x)/(1−x))."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 6)",
        "body": (
            "∫ dx/(9 + 4x²): write 9 + 4x² = 9 + (2x)², so a = 3, u = 2x, "
            "u′ = 2. The formula gives (1/3)tan⁻¹(2x/3) + c (after balancing the "
            "missing 2 with a factor 1/2 → (1/2)·(1/3)tan⁻¹(2x/3) + c)."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Match the denominator to one of five shapes",
        "body": (
            "a² + u² → tan⁻¹; a² − u² → tanh⁻¹; √(a² − u²) → sin⁻¹; "
            "√(a² + u²) → sinh⁻¹; √(u² − a²) → cosh⁻¹. Identify a, then u, then "
            "make the missing u′ appear."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Five integrand shapes map to five inverse functions. Draw a, draw u, "
            "supply u′ by scaling constants, then read the answer off the table."
        ),
    },
]
L6_PRACTICE = [
    {
        "prompt": "∫ u′/√(a² − u²) dx = ?",
        "options": ["sin⁻¹(u/a) + c", "tan⁻¹(u/a) + c", "sinh⁻¹(u/a) + c", "cos⁻¹(u/a) + c"],
        "correct_index": 0,
        "explanation": "The ✓-denominator with a minus gives arcsin.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "inverse-trig/hyperbolic integrals",
    },
    {
        "prompt": "∫ dx/(1 + x²) = ?",
        "options": ["tan⁻¹x + c", "sin⁻¹x + c", "tanh⁻¹x + c", "ln|x| + c"],
        "correct_index": 0,
        "explanation": "a = 1, u = x: the basic 1/(1 + x²) integral is arctan.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "inverse-trig/hyperbolic integrals",
    },
    {
        "prompt": "∫ dx/√(4 − x²) = ?",
        "options": ["sin⁻¹(x/2) + c", "2 sin⁻¹(x/2) + c", "sin⁻¹(2x) + c", "tan⁻¹(x/2) + c"],
        "correct_index": 0,
        "explanation": "a = 2, u = x, u′ = 1: table gives sin⁻¹(x/2).",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "inverse-trig/hyperbolic integrals",
    },
]
L6_LINKS = [
    {"code": "inverse-integration", "role": "teaches"},
    {"code": "basic-integration", "role": "requires"},
]

# --- L7 ---------------------------------------------------------------

L7_OBJECTIVES = [
    "Decide the case: is a power of sin or cos odd, or are both even?",
    "Use the odd-power substitution sin²x = 1 − cos²x (or the symmetric one).",
    "Use the half-angle identities for all-even cases.",
]
L7_PREREQUISITES = [
    "Basic integration rules (Sheet 5).",
    "The trig identities from the formula sheet.",
]
L7_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Integrals like ∫sinᵐx cosⁿx dx are categorised by parity. If one "
            "power is odd, peel off one factor and the rest becomes a polynomial "
            "in the other function. If both powers are even, half-angle "
            "identities reduce the degree step by step."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "The two cases (Sheet 7)",
        "body": (
            "Case 1 — one of m, n odd (> 1): use sin²x = 1 − cos²x or "
            "cos²x = 1 − sin²x to convert everything to one variable.\n"
            "Case 2 — both m, n even: use sin²x = (1 − cos 2x)/2, "
            "cos²x = (1 + cos 2x)/2, and sin x cos x = sin(2x)/2."
        ),
        "metadata": {
            "note": "The same ideas extend to ∫tanᵐx secⁿx dx with tan²x = sec²x − 1.",
        },
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 7)",
        "body": (
            "∫sin³x dx = ∫sin²x·sin x dx = ∫(1 − cos²x) sin x dx. With "
            "u = cos x, du = −sin x dx: −∫(1 − u²) du = −u + u³/3 + c "
            "= −cos x + cos³x/3 + c."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Odd power → save one factor for du",
        "body": (
            "With an odd power you always have a spare sin x dx (or cos x dx) "
            "that becomes du. Everything that remains is even in the new "
            "variable, so you can use the Pythagorean identity to clear squares."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Parity decides the method: odd power → substitute 1 − cos² (or "
            "1 − sin²); even powers → halve the angles."
        ),
    },
]
L7_PRACTICE = [
    {
        "prompt": "For ∫sin³x cos²x dx the clean first step is:",
        "options": ["sin³x = sin x(1 − cos²x), let u = cos x", "sinus-half-angle on sin³x", "integration by parts straight away", "partial fractions"],
        "correct_index": 0,
        "explanation": "sin³ has an odd power; peel one sin x for du and rewrite sin²x = 1 − cos²x.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "trig powers",
    },
    {
        "prompt": "sin²x written for the 'both even' case equals:",
        "options": ["(1 − cos 2x)/2", "(1 + cos 2x)/2", "1 − cos²x", "sin(2x)/2"],
        "correct_index": 0,
        "explanation": "The half-angle identity sin²x = (1 − cos 2x)/2 linearises the square.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "trig powers",
    },
    {
        "prompt": "∫cos²x dx = ?",
        "options": ["x/2 + sin(2x)/4 + c", "x/2 − sin(2x)/4 + c", "x/2 + c", "sin²x + c"],
        "correct_index": 0,
        "explanation": "cos²x = (1 + cos 2x)/2 → x/2 + sin(2x)/4 (since ∫cos 2x = sin 2x /2, halved again).",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "trig powers",
    },
]
L7_LINKS = [
    {"code": "trig-powers", "role": "teaches"},
    {"code": "basic-integration", "role": "requires"},
]

# --- L8 ---------------------------------------------------------------

L8_OBJECTIVES = [
    "State ∫u dv = uv − ∫v du and choose u and dv by the ILATE order.",
    "Apply parts to products with polynomials, exponentials and logs.",
    "Handle cyclic products (e.sin, e.cos) by repeating parts.",
]
L8_PREREQUISITES = [
    "Basic integration rules (Sheet 5).",
    "Choosing functions by their derivative/integral behaviour.",
]
L8_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Integration by parts reverses the product rule: ∫u dv = uv − ∫v du. "
            "The art is the choice — pick u so that du is simpler (polynomials, "
            "logs, inverse trig), and dv so that v is just as simple (eˣ, "
            "sin, cos). The ILATE priority answers most choices."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Integration by parts",
        "body": "∫ u dv = u v − ∫ v du",
        "metadata": {
            "meaning": "Integral of a product = first × integral of second − integral of (derivative of first × that integral).",
            "when_used": "Products like x·eˣ, x·sin x, ln x, x·ln x.",
        },
    },
    {
        "section_type": "TABLE",
        "title": "ILATE priority",
        "body": (
            "I — Inverse trig (sin⁻¹, tan⁻¹) pick as u\n"
            "L — Logarithms (ln) pick as u\n"
            "A — Algebraic xⁿ pick as u\n"
            "T — Trig (sin, cos) pick as dv\n"
            "E — Exponential eˣ pick as dv"
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 8)",
        "body": (
            "∫ x eˣ dx: ILATE → u = x, dv = eˣdx, so du = dx, v = eˣ. "
            "Then ∫ = x eˣ − ∫eˣ dx = x eˣ − eˣ + c = eˣ(x − 1) + c."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Repeated parts for cyclic products",
        "body": (
            "∫ eˣ sin x dx needs parts twice; the second pass regenerates the "
            "original integral, which you then solve algebraically by "
            "transposition."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Apply ILATE, write u, dv, du, v, translate the formula, and check "
            "the new integral is simpler than the old."
        ),
    },
]
L8_PRACTICE = [
    {
        "prompt": "∫x eˣ dx = ?",
        "options": ["eˣ(x − 1) + c", "x eˣ + c", "x²/2 · eˣ + c", "eˣ/x + c"],
        "correct_index": 0,
        "explanation": "u = x, dv = eˣdx → xeˣ − ∫eˣdx = eˣ(x − 1) + c.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "by parts",
    },
    {
        "prompt": "By ILATE, for ∫x² ln x dx the parts choice is:",
        "options": ["u = ln x, dv = x²dx", "u = x², dv = ln x dx", "u = x², dv = x dx", "u = ln x, dv = 1 dx"],
        "correct_index": 0,
        "explanation": "Logarithms outrank algebraic powers, so ln x is u and x² dx is dv.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "by parts",
    },
    {
        "prompt": "∫u dv = ?",
        "options": ["uv − ∫v du", "uv + ∫v du", "∫v du − uv", "uv − ∫u du"],
        "correct_index": 0,
        "explanation": "Parts formula: first × integral of second minus the swapped integral.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "by parts",
    },
]
L8_LINKS = [
    {"code": "by-parts", "role": "teaches"},
    {"code": "basic-integration", "role": "requires"},
]

# --- L9 ---------------------------------------------------------------

L9_OBJECTIVES = [
    "Classify a rational integrand as proper or improper.",
    "Write the correct partial-fraction template for the denominator.",
    "Solve for the constants by the cover-up method or by equating coefficients.",
]
L9_PREREQUISITES = [
    "Polynomial long division to convert improper to proper fractions.",
    "The integration rules of Sheet 5.",
]
L9_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "A rational function becomes easy once it is split into a sum of "
            "simple fractions — each piece integrates to a log or an "
            "arctangent. The answer only depends on how the denominator "
            "factors: distinct linear factors, repeated ones, or an "
            "irreducible quadratic."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Partial-fraction templates (formula sheet)",
        "body": (
            "1) (px + q)/((x−a)(x−b)) → A/(x−a) + B/(x−b)\n"
            "2) (px + q)/(x−a)² → A/(x−a) + B/(x−a)²\n"
            "3) (px²+qx+r)/((x−a)(x−b)(x−c)) → A/(x−a) + B/(x−b) + C/(x−c)\n"
            "4) (px²+qx+r)/((x−a)²(x−b)) → A/(x−a) + B/(x−a)² + C/(x−b)\n"
            "5) (px²+qx+r)/((x−a)(x²+bx+c)) → A/(x−a) + (Bx+C)/(x²+bx+c)"
        ),
        "metadata": {"note": "Every linear factor (x−a)ᵏ contributes k terms with denominators up to (x−a)ᵏ."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 9)",
        "body": (
            "1/((x−1)(x−2)): write A/(x−1) + B/(x−2). Multiply through: "
            "1 = A(x−2) + B(x−1). Set x = 1 → A = −1; set x = 2 → B = 1. "
            "So the integral is −ln|x−1| + ln|x−2| + c."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "Improper first, factor second",
        "body": (
            "If the numerator's degree ≥ the denominator's, divide first. Then "
            "factor the denominator completely and match the template above."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Factor the denominator, write the template, solve A, B, C by "
            "selecting x to kill terms, integrate the logs."
        ),
    },
]
L9_PRACTICE = [
    {
        "prompt": "For 1/((x−a)(x−b)) the partial-fraction template is:",
        "options": ["A/(x−a) + B/(x−b)", "A/(x−a) + B/(x−a)²", "A/x + B/(x−b)", "(Ax+B)/(x−a)(x−b)"],
        "correct_index": 0,
        "explanation": "Distinct linear factors each get their own simple fraction.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "partial fractions",
    },
    {
        "prompt": "For (px+q)/(x−a)² the template is:",
        "options": ["A/(x−a) + B/(x−a)²", "A/(x−a) + B/(x−a) multiplied twice", "A/(x−a)² + B/(x−a)²", "A/(x−a)·(x−a)"],
        "correct_index": 0,
        "explanation": "A repeated factor (x−a)² needs one term per power.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "partial fractions",
    },
    {
        "prompt": "In 1/((x−1)(x−2)) = A/(x−1) + B/(x−2), the cover-up value of B is:",
        "options": ["1", "−1", "2", "1/2"],
        "correct_index": 0,
        "explanation": "Set x = 2: B = 1/(2−1) = 1.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "partial fractions",
    },
]
L9_LINKS = [
    {"code": "partial-fractions", "role": "teaches"},
    {"code": "basic-integration", "role": "requires"},
]

# --- L10 --------------------------------------------------------------

L10_OBJECTIVES = [
    "Use a linear substitution u = ax + b for integrands containing (ax+b)ⁿ.",
    "Pick the trig substitution that matches each radical shape.",
    "Back-substitute the answer into the original variable and simplify.",
]
L10_PREREQUISITES = [
    "Basic integration rules (Sheet 5).",
    "The integration forms of Sheet 6.",
]
L10_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Substitution converts an unrecognisable integral into one from the "
            "tables. A linear substitution removes (ax + b)ⁿ; a trigonometric "
            "substitution kills square roots like √(a² − u²) by turning them "
            "into perfect squares via the Pythagorean identities."
        ),
    },
    {
        "section_type": "TABLE",
        "title": "Trig substitution table (Sheet 10)",
        "body": (
            "√(a² − u²)  →  u = a sin θ   (θ ∈ [−π/2, π/2])\n"
            "√(a² + u²)  →  u = a tan θ   (θ ∈ (−π/2, π/2))\n"
            "√(u² − a²)  →  u = a sec θ   (θ ∈ [0, π/2) or [π, 3π/2))"
        ),
        "metadata": {"note": "The θ restrictions keep the substitution one-to-one so back-substitution is unambiguous."},
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked example (Sheet 10)",
        "body": (
            "∫ dx/√(9 − x²): with u = x, a = 3 the Sheet-6 form applies without "
            "a trig substitution → sin⁻¹(x/3) + c. The trig substitution only "
            "earns its keep when an extra x or linear factor sits beside the "
            "radical."
        ),
    },
    {
        "section_type": "KEY_POINT",
        "title": "The radical decides the substitution",
        "body": (
            "√(a² − u²) → sin; √(a² + u²) → tan; √(u² − a²) → sec. Draw the "
            "right triangle to read the final answer in x for free."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Summary",
        "body": (
            "Match the radical to the substitution, integrate in θ, then convert "
            "back with the triangle. Sheet 6's forms do the work before you "
            "reach the triangle when possible."
        ),
    },
]
L10_PRACTICE = [
    {
        "prompt": "For an integrand with √(a² − u²) the recommended substitution is:",
        "options": ["u = a sin θ", "u = a tan θ", "u = a sec θ", "u = a cosh θ"],
        "correct_index": 0,
        "explanation": "√(a² − u²) with u = a sin θ becomes √(a² cos² θ) = a cos θ.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "substitution",
    },
    {
        "prompt": "For an integrand with √(a² + u²) the recommended substitution is:",
        "options": ["u = a tan θ", "u = a sin θ", "u = a sec θ", "u = a sinh θ"],
        "correct_index": 0,
        "explanation": "√(a² + u²) with u = a tan θ becomes a sec θ.",
        "level": "UNDERSTAND",
        "difficulty": 1,
        "skill": "substitution",
    },
    {
        "prompt": "∫ (2x) e^{x²} dx is best done with:",
        "options": ["linear substitution u = x²", "trig substitution", "by parts with u = 2x", "partial fractions"],
        "correct_index": 0,
        "explanation": "u = x² has du = 2x dx; the integrand is eᵘ du → e^{x²} + c.",
        "level": "APPLY",
        "difficulty": 2,
        "skill": "substitution",
    },
]
L10_LINKS = [
    {"code": "substitution", "role": "teaches"},
    {"code": "inverse-integration", "role": "requires"},
]


def _bundle(
    *,
    module: dict,
    lesson: dict,
    contents: list,
    practice: list,
    links: list,
    competency_codes: list,
) -> dict:
    """Build one importer bundle (course + module + lesson) with a shared course shell."""
    return {
        "course": {
            "code": COURSE_CODE,
            "title": COURSE_TITLE,
            "credits": COURSE_CREDITS,
            "description": COURSE_DESCRIPTION,
            "department_code": DEPARTMENT_CODE,
            "department_name": DEPARTMENT_NAME,
            "faculty_code": FACULTY_CODE,
            "faculty_name": FACULTY_NAME,
            "module": module,
            "lesson": lesson,
            "lesson_contents": contents,
            "summary_contents": [
                {
                    "section_type": "SUMMARY",
                    "title": "Lesson review",
                    "body": next(
                        (s["body"] for s in contents if s["section_type"] == "SUMMARY"),
                        "",
                    ),
                }
            ],
            "resources": [],
            "competencies": [
                {
                    "code": code,
                    "title": _COMPETENCY_TITLES[code],
                    "description": _COMPETENCY_DESCRIPTIONS[code],
                    "taxonomy_level": _COMPETENCY_LEVELS[code],
                }
                for code in competency_codes
            ],
            "competency_prerequisites": [
                (pre, post) for pre, post in [
                    ("chain-rule", "inv-trig-deriv"),
                    ("chain-rule", "hyperbolic-deriv"),
                    ("limits-lhopital", "maclaurin"),
                    ("basic-integration", "inverse-integration"),
                    ("inverse-integration", "trig-powers"),
                    ("basic-integration", "by-parts"),
                    ("basic-integration", "partial-fractions"),
                    ("inverse-integration", "substitution"),
                ] if pre in competency_codes and post in competency_codes
            ],
            "lesson_competencies": links,
            "practice_items": practice,
        }
    }


_COMPETENCY_TITLES = {
    "chain-rule": "Chain rule for composite functions",
    "inv-trig-deriv": "Derivatives of inverse trigonometric functions",
    "hyperbolic-deriv": "Hyperbolic functions and their derivatives",
    "limits-lhopital": "Limits with L'Hospital's rule",
    "maclaurin": "Maclaurin expansions",
    "basic-integration": "Basic integration rules",
    "inverse-integration": "Integrals giving inverse trig/hyperbolic functions",
    "trig-powers": "Integrating powers and products of trigonometric functions",
    "by-parts": "Integration by parts",
    "partial-fractions": "Integration by partial fractions",
    "substitution": "Integration by substitution",
}

_COMPETENCY_DESCRIPTIONS = {
    "chain-rule": "Differentiate composites of any of the course's elementary functions.",
    "inv-trig-deriv": "Use the six inverse-trig derivative rules with the chain rule.",
    "hyperbolic-deriv": "Differentiate sinh, cosh, tanh and the inverse hyperbolic functions.",
    "limits-lhopital": "Evaluate 0/0 and ∞/∞ limits using L'Hospital's rule and series.",
    "maclaurin": "Expand and combine Maclaurin series up to a stated order.",
    "basic-integration": "Integrate elementary functions using the generalised rules of Sheet 5.",
    "inverse-integration": "Recognise and integrate the five inverse-trig/hyperbolic shapes.",
    "trig-powers": "Integrate sinᵐx cosⁿx (and tanᵐx secⁿx) by parity.",
    "by-parts": "Integrate products with the parts formula and ILATE ordering.",
    "partial-fractions": "Decompose rational functions and integrate the parts.",
    "substitution": "Choose and apply linear and trigonometric substitutions.",
}

_COMPETENCY_LEVELS = {
    "chain-rule": "apply",
    "inv-trig-deriv": "apply",
    "hyperbolic-deriv": "apply",
    "limits-lhopital": "apply",
    "maclaurin": "apply",
    "basic-integration": "understand",
    "inverse-integration": "apply",
    "trig-powers": "apply",
    "by-parts": "apply",
    "partial-fractions": "apply",
    "substitution": "apply",
}


def _lesson(
    *,
    code: str,
    title: str,
    description: str,
    minutes: int,
    difficulty: str,
    objectives: list,
    prerequisites: list,
    sort_order: int,
) -> dict:
    return {
        "code": code,
        "title": title,
        "description": description,
        "estimated_minutes": minutes,
        "difficulty": difficulty,
        "objectives": objectives,
        "prerequisites": prerequisites,
        "sort_order": sort_order,
    }


BUNDLES = [
    _bundle(
        module=MODULE_DERIVATION,
        lesson=_lesson(
            code="MA1",
            title="Derivatives of Inverse Trigonometric Functions",
            description=(
                "Sheet 1 — the six inverse-trig derivative rules with the chain "
                "rule, plus implicit and parametric first and second derivatives."
            ),
            minutes=80,
            difficulty="medium",
            objectives=L1_OBJECTIVES,
            prerequisites=L1_PREREQUISITES,
            sort_order=1,
        ),
        contents=L1_CONTENTS,
        practice=L1_PRACTICE,
        links=L1_LINKS,
        competency_codes=["inv-trig-deriv", "chain-rule"],
    ),
    _bundle(
        module=MODULE_DERIVATION,
        lesson=_lesson(
            code="MA2",
            title="Hyperbolic Functions and Their Derivatives",
            description=(
                "Sheet 2 — definitions from eˣ, the cosh²x − sinh²x = 1 family "
                "and every hyperbolic derivative rule."
            ),
            minutes=70,
            difficulty="medium",
            objectives=L2_OBJECTIVES,
            prerequisites=L2_PREREQUISITES,
            sort_order=2,
        ),
        contents=L2_CONTENTS,
        practice=L2_PRACTICE,
        links=L2_LINKS,
        competency_codes=["hyperbolic-deriv", "chain-rule"],
    ),
    _bundle(
        module=MODULE_APPLICATIONS,
        lesson=_lesson(
            code="MA3",
            title="Limits with L'Hospital's Rule",
            description=(
                "Sheet 3 — indeterminate forms and how L'Hospital's rule plus "
                "the Maclaurin series resolve them."
            ),
            minutes=75,
            difficulty="medium",
            objectives=L3_OBJECTIVES,
            prerequisites=L3_PREREQUISITES,
            sort_order=1,
        ),
        contents=L3_CONTENTS,
        practice=L3_PRACTICE,
        links=L3_LINKS,
        competency_codes=["limits-lhopital", "chain-rule"],
    ),
    _bundle(
        module=MODULE_APPLICATIONS,
        lesson=_lesson(
            code="MA4",
            title="Maclaurin Expansions",
            description=(
                "Sheet 4 — the standard series for eˣ, sin, cos, sinh, cosh, "
                "ln(1+x) and (1+x)ⁿ, and how to combine them."
            ),
            minutes=85,
            difficulty="hard",
            objectives=L4_OBJECTIVES,
            prerequisites=L4_PREREQUISITES,
            sort_order=2,
        ),
        contents=L4_CONTENTS,
        practice=L4_PRACTICE,
        links=L4_LINKS,
        competency_codes=["maclaurin", "limits-lhopital"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA5",
            title="Basic Rules of Integration",
            description=(
                "Sheet 5 — the generalised power, log and exponential rules and "
                "basic trig integrals read straight off the derivative table."
            ),
            minutes=70,
            difficulty="easy",
            objectives=L5_OBJECTIVES,
            prerequisites=L5_PREREQUISITES,
            sort_order=1,
        ),
        contents=L5_CONTENTS,
        practice=L5_PRACTICE,
        links=L5_LINKS,
        competency_codes=["basic-integration"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA6",
            title="Integrals Giving Inverse Trig and Hyperbolic Functions",
            description=(
                "Sheet 6 — the five integrand shapes that map to sin⁻¹, tan⁻¹, "
                "tanh⁻¹, sinh⁻¹ and cosh⁻¹."
            ),
            minutes=75,
            difficulty="medium",
            objectives=L6_OBJECTIVES,
            prerequisites=L6_PREREQUISITES,
            sort_order=2,
        ),
        contents=L6_CONTENTS,
        practice=L6_PRACTICE,
        links=L6_LINKS,
        competency_codes=["inverse-integration", "basic-integration"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA7",
            title="Integrating Powers and Products of Trigonometric Functions",
            description=(
                "Sheet 7 — the odd/even parity rules for ∫sinᵐx cosⁿx dx and "
                "their extension to tan and sec."
            ),
            minutes=75,
            difficulty="medium",
            objectives=L7_OBJECTIVES,
            prerequisites=L7_PREREQUISITES,
            sort_order=3,
        ),
        contents=L7_CONTENTS,
        practice=L7_PRACTICE,
        links=L7_LINKS,
        competency_codes=["trig-powers", "inverse-integration"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA8",
            title="Integration by Parts",
            description=(
                "Sheet 8 — ∫u dv = uv − ∫v du and the ILATE ordering that "
                "chooses u and dv."
            ),
            minutes=75,
            difficulty="medium",
            objectives=L8_OBJECTIVES,
            prerequisites=L8_PREREQUISITES,
            sort_order=4,
        ),
        contents=L8_CONTENTS,
        practice=L8_PRACTICE,
        links=L8_LINKS,
        competency_codes=["by-parts", "basic-integration"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA9",
            title="Integration by Partial Fractions",
            description=(
                "Sheet 9 — factoring denominators, writing the correct template "
                "and solving for the constants."
            ),
            minutes=80,
            difficulty="medium",
            objectives=L9_OBJECTIVES,
            prerequisites=L9_PREREQUISITES,
            sort_order=5,
        ),
        contents=L9_CONTENTS,
        practice=L9_PRACTICE,
        links=L9_LINKS,
        competency_codes=["partial-fractions", "basic-integration"],
    ),
    _bundle(
        module=MODULE_INTEGRATION,
        lesson=_lesson(
            code="MA10",
            title="Integration by Substitution",
            description=(
                "Sheet 10 — linear substitutions u = ax + b and the three "
                "trigonometric substitutions for radical integrands."
            ),
            minutes=75,
            difficulty="medium",
            objectives=L10_OBJECTIVES,
            prerequisites=L10_PREREQUISITES,
            sort_order=6,
        ),
        contents=L10_CONTENTS,
        practice=L10_PRACTICE,
        links=L10_LINKS,
        competency_codes=["substitution", "inverse-integration"],
    ),
]
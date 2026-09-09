"""PHY211 — Physics, Module 8, Lecture 10: Nature of Light and Ray Optics.

Structured curriculum bundle derived from the ARETE content-transformation
pipeline (source: Phy 211 Lecture Notes, Lecture 10, Fall 2024 —
'Nature of Light and Ray Optics', Chapter 9).

Introduces the geometric optics toolkit: the ray model, the law of
reflection, the index of refraction, Snell's law, apparent depth, total
internal reflection, and the prism/fiber applications. Imported by
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
    "code": "M8",
    "title": "Module 8 — Ray Optics",
    "description": (
        "Chapter 9: light as straight rays. The law of reflection, the index of "
        "refraction n = c/v, Snell's law, the apparent-depth illusion, total "
        "internal reflection, and the prism/fiber systems that exploit the "
        "critical angle."
    ),
    "sort_order": 8,
}

LESSON = {
    "code": "L10",
    "title": "Nature of Light and Ray Optics: Reflection, Refraction, Apparent Depth, and Total Internal Reflection",
    "description": (
        "Lecture 10 — the geometric picture that lets us 'see' light: rays travel "
        "straight until borders. Reflections obey θi = θr; refractions obey "
        "n₁sinθ₁ = n₂sinθ₂; inside a medium the speed and wavelength shrink by "
        "n while the frequency never changes; and past the critical angle, light "
        "gives up bending altogether — total internal reflection, the engine of "
        "prisms and optical fibers."
    ),
    "estimated_minutes": 90,
    "difficulty": "medium",
    "objectives": [
        "Explain the ray model of light and why geometric optics describes shadows, images, and direction without waves.",
        "State the law of reflection θi = θr with all angles measured from the normal.",
        "Define the index of refraction n = c/v and use n to find the speed and wavelength of light in a medium.",
        "Apply Snell's law n₁sinθ₁ = n₂sinθ₂ with angles from the normal.",
        "Interpret apparent depth d′ = n₂d/n₁ and the pool bottom looking shallower than it is.",
        "State the conditions for total internal reflection and compute the critical angle sinθ_C = n₂/n₁.",
        "Explain the 45° prism and the optical fiber as total-internal-reflection devices.",
        "Recognize that frequency (and color) never changes when light crosses a border.",
    ],
    "prerequisites": [
        "Properties of electric charge — matter of any kind interacts through its internal charges (Lecture 1).",
        "Field-lines intuition for how waves carry energy across space.",
        "Basic geometry: triangles and right-angle trigonometry.",
    ],
    "sort_order": 1,
}

# --- lesson content blocks ---------------------------------------------------
LESSON_CONTENTS = [
    {
        "section_type": "TEXT",
        "title": "The Big Picture",
        "body": (
            "Optics is the physics of seeing, and it is almost pure geometry. "
            "Light travels along straight lines — rays — until it meets a border. "
            "At a border it either bounces (reflection), bends (refraction), or, "
            "past a critical angle, refuses to leave (total internal reflection). "
            "This lecture banks those three decisions and the one quantity a "
            "border can never change: frequency."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "The Ray Model of Light",
        "body": (
            "Light is a wave — but for forming shadows, images, and direction, we "
            "draw it as RAYS: straight lines perpendicular to the wavefronts, "
            "pointing the way energy travels. Rays fan out from a point source "
            "and collect to a point again after ideal optics. The ray model is "
            "why we get sharp shadows: each ray obeys geometry, and the image is "
            "where the rays (or their extensions) meet."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Law of Reflection",
        "body": "θ₁ (incident) = θ₂ (reflected), both measured from the NORMAL",
        "metadata": {
            "meaning": "The incident ray, the normal, and the reflected ray lie in one plane; the angle in equals the angle out, each from the normal to the surface.",
            "when_used": "Every mirror problem. For a 30° incidence (from the normal), the reflected ray also leaves at 30° — and the ray's deviation double-counts angles.",
        },
    },
    {
        "section_type": "FORMULA",
        "title": "Index of Refraction",
        "body": "n = c / v      (v = speed of light inside the medium)",
        "metadata": {
            "meaning": "How much a material slows light: n = 1 in vacuum, n ≈ 1.33 water, n ≈ 1.5 glass. Inside the medium light moves slower: v = c/n.",
            "when_used": "Converting between vacuum and in-material speeds; every angle-and-velocity problem. n is always ≥ 1.",
        },
    },
    {
        "section_type": "KEY_POINT",
        "title": "Faster, slower, but never a new color",
        "body": (
            "Crossing into a medium, the SPEED drops (v = c/n) and the WAVELENGTH "
            "shrinks in step (λ_medium = λ_air/n) — but the FREQUENCY, which is "
            "the color, never changes. Frequency is the identity of light; the "
            "medium buys time and length from it without recolorizing it."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Snell's Law",
        "body": "n₁ sin θ₁ = n₂ sin θ₂",
        "metadata": {
            "meaning": "At a border, the product n·sinθ is the same on both sides; every angle from the NORMAL: heavier n ⇒ smaller θ (bends toward the normal).",
            "when_used": "Air-to-glass, water-to-air, any two-media border. Into denser medium θ shrinks; into rarer medium θ grows.",
        },
    },
    {
        "section_type": "TEXT",
        "title": "Apparent Depth: The Pool Looks Shallower",
        "body": (
            "Looking into water, rays bend toward the normal as they exit — the "
            "eye extends them back and meets them higher up. The pool floor "
            "appears raised: apparent depth d′ = n₂·d/n₁, with n₁ that of the "
            "medium the object sits in. A 4.0 m pool with n₁ = 4/3 gives "
            "d′ = 4.0 × (1/(4/3)) = 3.0 m — one meter disappears. The same trick "
            "makes the fish look nearer than it is, which is why spear fishermen "
            "aim below what they see."
        ),
    },
    {
        "section_type": "FORMULA",
        "title": "Total Internal Reflection and the Critical Angle",
        "body": "sin θ_C = n₂ / n₁   (requires n₁ > n₂)",
        "metadata": {
            "meaning": "Going from a denser medium out to a rarer one, past θ_C the refracted ray would demand sinθ₂ > 1 — impossible — so the light reflects entirely. Nothing leaves.",
            "when_used": "Glass→air, water→air, fiber core→cladding. Above θ_C: 100% reflection, perfectly efficient.",
        },
    },
    {
        "section_type": "EXPLANATION",
        "title": "Critical-angle table",
        "body": (
            "Glass (n = 1.5) → air: sinθ_C = 1/1.5 → θ_C ≈ 41.8°. Diamond "
            "(n ≈ 2.42) → air: sinθ_C = 1/2.42 → θ_C ≈ 24.4° — the tiny critical "
            "angle is why cut diamonds trap so much light and sparkle. Optical "
            "fiber core (n₁ = 1.6) → cladding (n₂ = 1.4): sinθ_C = 1.4/1.6 → "
            "θ_C ≈ 61.0° — steeper arrivals escape, gentle ones stay confined."
        ),
    },
    {
        "section_type": "TEXT",
        "title": "Why the critical angle matters: prisms and fibers",
        "body": (
            "A 45° prism reflects incident light it cannot refract — a 45°–45°–90° "
            "prism turns a beam a full 90° without any metal film, which is why "
            "binoculars and periscopes pack them (better than any mirror coating). "
            "An optical fiber threads the same trick down a glass core: light "
            "entering at a shallow angle hits the core–cladding border beyond "
            "θ_C each bounce and never escapes; signals ride hundreds of "
            "kilometers on repeated total internal reflections."
        ),
    },
]

WORKED_EXAMPLES = [
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 1 — Snell's law across a border",
        "body": (
            "Light in air (n₁ = 1) strikes water (n₂ = 1.33) at 45° from the "
            "normal. Snell: (1)sin 45° = (1.33)sin θ₂ → sin θ₂ = 0.7071/1.33 "
            "= 0.5317 → θ₂ ≈ 32.1°. Enters the denser medium, bends TOWARD the "
            "normal — no surprise, only the arithmetic."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 2 — speed and wavelength inside glass",
        "body": (
            "Red light (f fixed) at 600 nm in air enters glass with n = 1.5. New "
            "speed: v = c/n = (3 × 10⁸)/1.5 = 2 × 10⁸ m/s. New wavelength: "
            "λ_glass = λ_air/n = 600/1.5 = 400 nm. Frequency (the color) is "
            "unchanged — the picture of the light is identical on both sides, "
            "only its speed and wavelength adapted."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 3 — the shallower-looking pool",
        "body": (
            "A swimming pool is 4.0 m deep. Looking straight down from air "
            "(n₂ = 1) into water (n₁ = 4/3): d′ = n₂·d/n₁ = (1)(4.0)/(4/3) "
            "= 3.0 m. The bottom appears a full meter higher than it is — "
            "distance-to-fish illusions carry the same factor."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 4 — critical angle of glass",
        "body": (
            "Glass (n₁ = 1.5) to air (n₂ = 1.0): sinθ_C = n₂/n₁ = 1/1.5 = 0.6667 "
            "→ θ_C ≈ 41.8°. Every arrival between 41.8° and 90° stays inside — "
            "total internal reflection keeps rays trapped, driving fibers, prisms, "
            "and the diamond's sparkle."
        ),
    },
    {
        "section_type": "EXAMPLE",
        "title": "Worked Example 5 — an optical fiber end-to-end",
        "body": (
            "A fiber has core n₁ = 1.6, cladding n₂ = 1.4. Critical angle: "
            "sinθ_C = 1.4/1.6 = 0.875 → θ_C ≈ 61.0°. A ray launched at a shallow "
            "angle hits the core wall beyond 61°, reflects back inside, and "
            "repeats the bounce down the fiber — clamped by geometry at every "
            "turn. Steeper-than-61° arrivals break out; the launch cone must stay "
            "gentle."
        ),
    },
]

WARNINGS = [
    {
        "section_type": "WARNING",
        "title": "Angles from the normal",
        "body": "Reflection and Snell angles are always measured from the NORMAL, not the surface. 30° from the glass face is 60° from the normal — converting wrong yields mirror-image answers.",
    },
    {
        "section_type": "WARNING",
        "title": "Confirming θ_C's direction",
        "body": "Total internal reflection requires n₁ > n₂ — light must LEAVE a denser medium. A plank of glass to air at 60° (past 41.8°) reflects; a beam in AIR into glass at 60° just refracts. Check which side is incident before quoting θ_C.",
    },
    {
        "section_type": "WARNING",
        "title": "The sin θ_C subtraction",
        "body": "sin θ_C = n₂/n₁ is a RATIO with the smaller index on top, never a difference and never (n₂ − n₁)/n₁. Diamond's small 24.4° comes from the big denominator 2.42.",
    },
    {
        "section_type": "WARNING",
        "title": "Assuming the color changes",
        "body": "Crossing a border changes speed and wavelength, never frequency — the color is the frequency. A 600-nm red in air hopping into glass is the same red at 400 nm inside, not a different color.",
    },
    {
        "section_type": "WARNING",
        "title": "Apparent depth booster",
        "body": "The pool bottom LOOKS shallower than the real depth: d′ = n₂d/n₁ is always smaller than d when viewing from a rarer medium. When the object's medium is denser, its apparent depth is compressed — never enlarged.",
    },
    {
        "section_type": "WARNING",
        "title": "n used as 1/sin θ blindly",
        "body": "Diamonds sparkle not because n is 'more bendy' but because the CRITICAL ANGLE is small (24.4°), trapping light inside. Keep the chain: big n → small sinθ_C → more trapping.",
    },
    {
        "section_type": "WARNING",
        "title": "The fiber's two indices",
        "body": "A fiber works because the CORE index exceeds the CLADDING index (1.6 > 1.4). Swap them and light leaks at the first bounce — the cladding is what bounces, not the air.",
    },
    {
        "section_type": "WARNING",
        "title": "Rays are not marbles",
        "body": "The ray model is geometry, not a particle picture. Total internal reflection delivers ALL the light back (100%) — a metal mirror at best reflects ~95% — which is why prisms beat mirrors in instruments.",
    },
]

DIFFICULT_CONCEPTS = [
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Angles at a Border, Always From the Normal",
        "body": (
            "Every optical angle is measured from the normal (the perpendicular), "
            "because bending is rotation about the surface's orientation, not "
            "along it. Analogy: a car driving at 30° to the shore into deeper "
            "sand turns toward the normal; the angle to the shore is the "
            "complement. Normal-first, always. Difficulty: EASY–MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Invariant Frequency (a medium can't recolor light)",
        "body": (
            "Speed and wavelength adapt at the border; the frequency cannot. "
            "Why? The wave arriving must match the wave leaving at the boundary "
            "— like a train of steps crossing a moving walkway: each step "
            "arrives at a new rate, and the count per second is handed over "
            "unchanged, even though stride length and walking speed shift. "
            "Difficulty: MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Apparent Depth and Where Your Brain Puts Things",
        "body": (
            "No ray actually ends at the apparent position — your eye extends the "
            "refracted rays backward and meets them higher up. The bottom 'is' "
            "one meter higher because your brain post-processes the geometry. "
            "Analogy: a spoon in a glass looks bent at the surface — same "
            "backward-extension trick, applied to a straight rod. Difficulty: "
            "MEDIUM."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "Total Internal Reflection: When Snell Says Impossible",
        "body": (
            "Outward-bound light wants sinθ₂ = n₁sinθ₁/n₂; past the critical "
            "angle that exceeds 1 — no refracted ray exists, so everything "
            "reflects. Not 'a weak reflection': ALL the light, perfectly, which "
            "is why the effect, not the mirror, powers fiber and diamond optics. "
            "Difficulty: MEDIUM–HARD."
        ),
    },
    {
        "section_type": "DIFFICULT_CONCEPT",
        "title": "The Launch Cone of a Fiber",
        "body": (
            "A fiber's acceptance angle follows from two borders in series: air→"
            "core refraction picks the entering angle, and core→cladding Snell "
            "demands arrival beyond 61°. Newcomers launch steep rays that escape "
            "at the first bounce. Analogy: a bowling alley's gutters — the "
            "channel only keeps balls rolling gently enough to stay between "
            "them. Difficulty: HARD."
        ),
    },
]

# --- summary view blocks -----------------------------------------------------
SUMMARY_CONTENTS = [
    {
        "section_type": "SUMMARY",
        "title": "Key Takeaways",
        "body": (
            "• Ray model: light travels in straight rays; rays fan from sources, meet at images.\n"
            "• Law of reflection: θi = θr, both from the normal; incident, normal, reflected in one plane.\n"
            "• Index of refraction: n = c/v (n ≥ 1; vacuum 1, water ≈ 1.33, glass ≈ 1.5).\n"
            "• Speed and λ drop by n inside a medium; the FREQUENCY never changes when light crosses a border.\n"
            "• Snell: n₁sinθ₁ = n₂sinθ₂, angles from the normal; denser medium ⇒ bends toward the normal.\n"
            "• Apparent depth looks shallower: d′ = n₂d/n₁ (4.0 m pool → 3.0 m).\n"
            "• Total internal reflection (n₁ > n₂, θ > θ_C): sinθ_C = n₂/n₁ — glass 41.8°, diamond 24.4°, fiber 61.0°.\n"
            "• 45° prisms and optical fibers run on total internal reflection — 100% efficient, unlike mirrors."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Definitions",
        "body": (
            "• Ray — a straight line of light travel, perpendicular to the wavefronts.\n"
            "• Normal — the perpendicular to the surface; all angles are measured from it.\n"
            "• Index of refraction n — the ratio c/v of a medium.\n"
            "• Apparent depth — the raised, virtual position of an object seen through a denser medium: d′ = n₂d/n₁.\n"
            "• Total internal reflection — 100% reflection of light at a denser→rarer border past the critical angle.\n"
            "• Critical angle θ_C — the incidence whose refracted ray skims the surface: sinθ_C = n₂/n₁.\n"
            "• Cladding — the lower-index jacket that keeps a fiber's core light bouncing inside."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "Key Formulas",
        "body": (
            "• θi = θr — law of reflection.\n"
            "• n = c/v; v = c/n — index and speed.\n"
            "• λ_medium = λ_air/n; f constant — wavelength and frequency across a border.\n"
            "• n₁sinθ₁ = n₂sinθ₂ — Snell's law.\n"
            "• d′ = n₂d/n₁ — apparent depth.\n"
            "• sinθ_C = n₂/n₁ (n₁ > n₂) — critical angle for total internal reflection."
        ),
    },
    {
        "section_type": "SUMMARY",
        "title": "60-Second Review",
        "body": (
            "Light travels in rays, straight until a border. Reflection: "
            "θi = θr, from the normal. Bending: n = c/v slows light inside a "
            "medium — speed and wavelength shrink by n, frequency is the one "
            "thing a border cannot touch. Refraction: n₁sinθ₁ = n₂sinθ₂ means "
            "denser media pull the ray toward the normal. Looking into water, "
            "rays extend backward and lift the floor: d′ = n₂d/n₁ (4.0 m pool "
            "looks 3.0 m). Going the other way, outward light hits sinθ₂ > 1 "
            "and gives up: total internal reflection past θ_C = sin⁻¹(n₂/n₁) — "
            "41.8° glass, 24.4° diamond, 61.0° fiber core. Prisms and fibers "
            "exploit it; the angles never hide; the frequency never changes."
        ),
    },
]

# --- video lectures ----------------------------------------------------------
VIDEO_RESOURCES = [
    {
        "resource_type": "VIDEO",
        "title": "One Thing Light Never Changes at a Border",
        "description": (
            "The ray model, reflection, the index of refraction, and Snell's "
            "law — with the invariant frequency as the guiding fact across "
            "every interface."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Reflection and refraction across a single interface",
            "target_student": "First-year university student",
            "objective": "Apply the law of reflection and Snell's law with angles from the normal, and explain which quantities do (and do not) change at a border.",
            "hook": "The same grain of light leaves the sun as red, crosses a window, dives into a fish tank, and is still the very same red on arrival — frequency is the oldest identification card in the universe.",
            "explanation_steps": [
                "Ray model: straight lines, sharp shadows, geometric optics.",
                "θi = θr from the normal; incident, normal, reflected coplanar.",
                "n = c/v: water 1.33, glass 1.5 — speed inside is c/n.",
                "λ shrinks by n; f never changes — the invariant identity.",
                "Snell: n₁sinθ₁ = n₂sinθ₂, bends toward the denser medium.",
                "Worked numbers: air 45° → water 32.1°; 600 nm → 400 nm in glass.",
            ],
            "common_mistake": "Measuring angles from the surface; claiming the color changes; using n ratios instead of n·sinθ products.",
            "check": "Light hits glass at 30° from the normal. Where does the reflected ray go, and how far does the refracted ray bend?",
            "final_takeaway": "One product n·sinθ is conserved at a border, one frequency is conserved too — everything else (direction, speed, wavelength) adapts.",
        },
        "sort_order": 1,
    },
    {
        "resource_type": "VIDEO",
        "title": "The Perfect Mirror: Total Internal Reflection",
        "description": (
            "The three conditions for total internal reflection, critical-angle "
            "computation, apparent depth, and the prism/fiber systems that "
            "convert the effect into instruments."
        ),
        "duration_seconds": 510,
        "metadata": {
            "target_concept": "Total internal reflection and its applications",
            "target_student": "First-year university student",
            "objective": "Identify when light is trapped (n₁ > n₂, θ > θ_C), compute sinθ_C = n₂/n₁, and explain prisms and fibers from the effect.",
            "hook": "No mirror is a perfect mirror — every coating swallows a few percent. But light bouncing off a diamond's inner faces loses nothing at all: it is its own perfect mirror.",
            "explanation_steps": [
                "Outward ray from a denser medium demands sinθ₂ ≤ 1.",
                "sinθ_C = n₂/n₁: glass 41.8°, diamond 24.4°, core 1.6/clad 1.4 → 61.0°.",
                "Past θ_C: 100% reflection — nothing escapes.",
                "Apparent depth as the same geometry run forward: d′ = n₂d/n₁.",
                "45° prisms turn beams 90°; roof prisms flip images.",
                "Fiber: launch cone, core>cladding, bounce down the line.",
            ],
            "common_mistake": "Applying θ_C without n₁ > n₂; using difference rather than ratio; drawing the escaped refracted ray past the critical angle.",
            "check": "Diamond's critical angle is 24.4°, glass's is 41.8°. Which traps more light, and why does the answer make diamonds sparkle?",
            "final_takeaway": "Three conditions — denser medium, outward direction, shallow enough angle — and light becomes its own perfect mirror: prisms, fibers, and sparkle follow.",
        },
        "sort_order": 2,
    },
]

# --- practice items ----------------------------------------------------------
PRACTICE_ITEMS = [
    # LEVEL 1 — UNDERSTAND
    {
        "level": "UNDERSTAND",
        "prompt": "State the ray model of light: what are rays, how do they behave in a uniform medium, and why is the model enough for shadows and images?",
        "options": [
            "Rays are straight lines along which light travels; in a uniform medium they go straight until a surface, and their geometry locates shadows and images",
            "Rays curve continuously toward any nearby matter; shadows are set by wave frequency",
            "Rays exist only inside optical fibers; outside them light has no direction",
            "Rays move fastest in glass and slowest in vacuum",
        ],
        "correct_index": 0,
        "explanation": "The ray model draws light as straight rays perpendicular to wavefronts; geometric optics (direction, shadows, image position) needs nothing more than the straight-line rule.",
        "skill": "ray-model statement",
        "difficulty": 1,
        "competency_code": "ray-model",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "State the law of reflection, including how the angles are measured.",
        "options": [
            "θi = θr, with both angles measured from the normal; the incident ray, the normal, and the reflected ray lie in one plane",
            "θi = θr, with both angles measured from the surface itself",
            "θi + θr = 90°, from the surface",
            "The reflected ray always doubles the incident angle measured from the normal",
        ],
        "correct_index": 0,
        "explanation": "The law of reflection equates the angles from the normal and keeps the three rays coplanar — the geometric rule behind every mirror.",
        "skill": "law of reflection statement",
        "difficulty": 1,
        "competency_code": "reflection-law",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "Define the index of refraction n. Light in air at 3 × 10⁸ m/s enters a medium with n = 1.5 — what is its new speed?",
        "options": [
            "n = c/v; new speed v = c/n = 3 × 10⁸/1.5 = 2 × 10⁸ m/s",
            "n = v/c; new speed v = nc = 4.5 × 10⁸ m/s",
            "n = c²/v²; new speed v = c/1.5² ≈ 1.3 × 10⁸ m/s",
            "n = c/v with n measured only in vacuum; speed inside is unchanged",
        ],
        "correct_index": 0,
        "explanation": "n = c/v inverts to v = c/n: a medium of n = 1.5 slows light to two-thirds its vacuum speed, 2 × 10⁸ m/s.",
        "skill": "index of refraction and speed",
        "difficulty": 1,
        "competency_code": "refraction-snell",
    },
    {
        "level": "UNDERSTAND",
        "prompt": "What are the three requirements for total internal reflection, and what is unusual about the reflection it produces?",
        "options": [
            "Denser→rarer direction (n₁ > n₂), incidence beyond the critical angle, and a dielectric border; the reflection returns essentially 100% of the light",
            "Rarer→denser direction, any angle, and a metallic coating; the reflection is slightly weaker than a mirror",
            "Any direction as long as the angle is smaller than 45°",
            "A vacuum on the far side with θ < θ_C; the reflection is diffuse",
        ],
        "correct_index": 0,
        "explanation": "Total internal reflection needs n₁ > n₂, θ > θ_C (both governed by sinθ_C = n₂/n₁), and returns essentially 100% — the most efficient mirror there is.",
        "skill": "TIR conditions",
        "difficulty": 1,
        "competency_code": "total-internal-reflection",
    },
    # LEVEL 2 — APPLY
    {
        "level": "APPLY",
        "prompt": "Light in air (n = 1.00) strikes water (n = 1.33) at 45° from the normal. Find the refracted angle.",
        "options": [
            "θ₂ = sin⁻¹(sin 45°/1.33) = sin⁻¹(0.5317) ≈ 32.1° — bends toward the normal",
            "θ₂ = 45° — the angle is preserved in refraction",
            "θ₂ = sin⁻¹(1.33 sin 45°) — impossible, argument > 1",
            "θ₂ = 1.33 × 45° ≈ 59.9° — bends away from the normal",
        ],
        "correct_index": 0,
        "explanation": "Snell: (1)sin 45° = (1.33)sin θ₂ → sin θ₂ = 0.5317 → θ₂ ≈ 32.1°. Into a denser medium light bends toward the normal.",
        "skill": "Snell across a single interface",
        "difficulty": 2,
        "competency_code": "refraction-snell",
    },
    {
        "level": "APPLY",
        "prompt": "A 600 nm ray in air enters glass with n = 1.5. What are the wavelength and frequency behavior inside the glass?",
        "options": [
            "λ = 600/1.5 = 400 nm; frequency unchanged (f stays the same, so the color is identical)",
            "λ = 600 × 1.5 = 900 nm; frequency drops",
            "λ = 600 nm; frequency rises by 1.5 (color shifts blue)",
            "λ = 600 nm but the speed changes; frequency doubles at the border",
        ],
        "correct_index": 0,
        "explanation": "λ_medium = λ_air/n = 400 nm and the frequency — the color — is invariant. Speed and wavelength adapt by n; the frequency is handed over untouched.",
        "skill": "wavelength and frequency at a border",
        "difficulty": 2,
        "competency_code": "refraction-snell",
    },
    {
        "level": "APPLY",
        "prompt": "A swimming pool measures 4.0 m deep. Viewed from air straight down, how deep does the floor appear?",
        "options": [
            "d′ = (1)(4.0)/(4/3) = 3.0 m — the bottom looks a meter shallower",
            "d′ = (4/3)(4.0)/(1) ≈ 5.3 m — deeper than reality",
            "d′ = 4.0 m — apparent depth always equals true depth",
            "d′ = 4.0 × (4/3 + 1) ≈ 9.3 m — magnified",
        ],
        "correct_index": 0,
        "explanation": "d′ = n₂d/n₁ = (1)(4.0)/(4/3) = 3.0 m: the object's own medium (n₁ = 4/3) compresses the apparent depth, exactly the illusion spear fishermen must defeat.",
        "skill": "apparent depth computation",
        "difficulty": 2,
        "competency_code": "ray-apparent-depth",
    },
    {
        "level": "APPLY",
        "prompt": "Find the critical angle for a glass-to-air surface with n_glass = 1.5.",
        "options": [
            "sinθ_C = 1/1.5 = 0.6667 → θ_C ≈ 41.8°",
            "sinθ_C = 1.5 → impossible; glass cannot have total internal reflection",
            "sinθ_C = 1.5/1.0 → θ_C ≈ 90°",
            "sinθ_C = 0.5 → θ_C = 30°",
        ],
        "correct_index": 0,
        "explanation": "sinθ_C = n₂/n₁ = 1/1.5 = 0.6667 → θ_C ≈ 41.8°: outward light arriving more steeply than 41.8° stays trapped inside the glass.",
        "skill": "critical-angle computation",
        "difficulty": 2,
        "competency_code": "total-internal-reflection",
    },
    # LEVEL 3 — TRANSFER
    {
        "level": "TRANSFER",
        "prompt": "Design an optical fiber: core n₁ = 1.6 and cladding n₂ = 1.4. What is the critical angle, and which launches stay inside?",
        "options": [
            "θ_C = 61.0° (sin⁻¹(1.4/1.6)); rays arriving at the core wall beyond 61° stay confined; steeper arrivals escape",
            "θ_C = 28.7° (sin⁻¹(1.6/1.4) with reversed ratio); all launches escape",
            "θ_C = 41.8°; only normal-incidence rays are guided",
            "θ_C = 90°; no ray can ever leave the core",
        ],
        "correct_index": 0,
        "explanation": "The core/cladding ratio sets sinθ_C = 1.4/1.6 = 0.875 → 61.0°. Light must arrive at the wall beyond 61° — a launch cone that stays gentle — to keep bouncing. Reversing the ratio is the classic error.",
        "skill": "fiber acceptance design",
        "difficulty": 3,
        "competency_code": "prism-fiber",
    },
    {
        "level": "TRANSFER",
        "prompt": "A 45°–45°–90° prism turns a horizontal beam through 90° with no coated mirror. What effect does the prism rely on and why does it beat the mirror?",
        "options": [
            "Total internal reflection inside the glass: the beam hits the far face beyond 41.8° and returns essentially 100% of the light, unlike metal coatings that absorb several percent",
            "Gradient refraction: the beam bends gradually by 90° across the glass",
            "Apparent-depth shrinking: the prism 'raises' the beam path by geometry",
            "The mirror equation: the prism focuses the beam to the image point",
        ],
        "correct_index": 0,
        "explanation": "The hypotenuse face meets the beam at 45° > θ_C (41.8°), so the beam is wholly reflected — a perfect, coating-free turn that beats every metallic mirror's ~95%.",
        "skill": "45° prism as a TIR device",
        "difficulty": 3,
        "competency_code": "prism-fiber",
    },
    {
        "level": "TRANSFER",
        "prompt": "A coin sits 2.0 m below the surface of a pool (n₁ = 1.33). A well-stocked spear fisherman sees the coin and thrusts straight down. Where relative to the image should the spear actually be aimed?",
        "options": [
            "Below the apparent position — the coin is really at 2.0 m but appears at 1.5 m, so aim ~0.5 m deeper than where it looks",
            "At the apparent position — the image coincides with the object for straight-down viewing",
            "Above the apparent position — the coin is shallower than it looks",
            "Sideways of the image — refraction shifts only the azimuth",
        ],
        "correct_index": 0,
        "explanation": "Apparent depth is d′ = 1.5 m while the true depth is 2.0 m — the coin sits ~0.5 m deeper than it appears. Every object in a denser medium must be reached below its image.",
        "skill": "apparent-depth transfer to aiming",
        "difficulty": 3,
        "competency_code": "ray-apparent-depth",
    },
    {
        "level": "TRANSFER",
        "prompt": "White light hits an air–glass border. Inside the glass, why have the colors separated into a small fan, and which color bends most?",
        "options": [
            "n varies with wavelength — shorter wavelengths (violet) get larger n, so they refract most; the frequency of each color is unchanged by the glass",
            "The glass changes frequency so each color changes hue",
            "Total internal reflection splits the beam at the critical angle",
            "Reflection at the first face already separates colors",
        ],
        "correct_index": 0,
        "explanation": "Dispersion: each wavelength carries its own n, so Snell bends each differently — violet (short λ, big n) bends most, red least — while every component keeps its own frequency through the glass.",
        "skill": "dispersion via wavelength-dependent n",
        "difficulty": 3,
        "competency_code": "refraction-snell",
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
        "code": "ray-model",
        "title": "The Ray Model of Light",
        "taxonomy_level": "understand",
        "description": "State the ray model of light and explain how straight-ray geometry locates shadows and images.",
        "sort_order": 43,
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
        "code": "ray-apparent-depth",
        "title": "Apparent Depth",
        "taxonomy_level": "apply",
        "description": "Compute apparent depth d′ = n₂d/n₁ and apply the shallower-than-real illusion to aiming and image placement.",
        "sort_order": 46,
    },
    {
        "code": "total-internal-reflection",
        "title": "Total Internal Reflection",
        "taxonomy_level": "apply",
        "description": "State the n₁ > n₂ / θ > θ_C conditions and compute the critical angle sinθ_C = n₂/n₁.",
        "sort_order": 47,
    },
    {
        "code": "prism-fiber",
        "title": "Prisms and Optical Fibers",
        "taxonomy_level": "apply",
        "description": "Explain 45° prisms and optical fibers as total-internal-reflection devices with index ratios and acceptance cones.",
        "sort_order": 48,
    },
]

COMPETENCY_PREREQUISITES = [
    ("charge-properties", "ray-model"),
    ("ray-model", "reflection-law"),
    ("ray-model", "refraction-snell"),
    ("refraction-snell", "ray-apparent-depth"),
    ("refraction-snell", "total-internal-reflection"),
    ("total-internal-reflection", "prism-fiber"),
]

LESSON_COMPETENCIES = [
    {"code": "ray-model", "role": "teaches"},
    {"code": "reflection-law", "role": "teaches"},
    {"code": "refraction-snell", "role": "teaches"},
    {"code": "ray-apparent-depth", "role": "teaches"},
    {"code": "total-internal-reflection", "role": "teaches"},
    {"code": "prism-fiber", "role": "teaches"},
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

# ARETE — LECTURE 10 (FULL TRANSFORMATION)

---

# 1. SOURCE ANALYSIS

| Item | Value |
|---|---|
| Course | PHY 211 — Physics (Electricity, Magnetism & Optics) |
| Lecture | **Lecture 10** — Chapter 9 |
| Title | The Nature of Light and the Principles of Ray Optics |
| Instructor | Dr. Ashraf Mousa Abdelwahed — AIU, Fall 2024 |

**Main topics:**
1. The nature of light (optics, geometric optics, the ray model, dual nature, EM spectrum)
2. Wave basics: v = λf
3. Reflection of light (laws; specular vs. diffuse)
4. Refraction of light (refraction law, refractive index, Snell's law, boundary behavior of λ, f, v)
5. Apparent depth
6. Total internal reflection and the critical angle
7. Applications: prisms; fiber optics

**Subtopics:** definitions of optics and geometric optics; the ray; photons vs. electromagnetic (transverse) waves; EM spectrum (figure); wavelength and frequency definitions; angles of incidence/reflection; the two reflection rules; smooth vs. rough surfaces; angle of refraction; sin θ₁/sin θ₂ = v₁/v₂; speed higher in the less dense medium; angle of deviation β = θ₁ − θ₂; refractive index n = c/v (n = 1 air, n > 1 otherwise); relative index n₁₂ = n₂/n₁; Snell's law; v and λ change, f unchanged; λm = λair/nm; apparent depth d′ = d(n₂/n₁) for a directly-overhead observer; TIR progression (bend away → critical angle → full reflection); direction condition (high → low only); sin θ_C = n₂/n₁; 45°–90°–45° prisms (90°/180° beam turning; binoculars, periscopes, telescopes); optical fibers (core/cladding, zigzag path, endoscopy).

**Learning objectives (from content):** use the ray model; apply reflection and refraction laws; compute indices, critical angles, and apparent depths; decide when TIR occurs; explain prism and fiber applications.

**Important definitions:** optics; geometric optics; ray; wavelength; frequency; angles of incidence/reflection/refraction; angle of deviation; refractive index; relative refractive index; critical angle; total internal reflection; optical fiber (core, cladding); endoscope.

**Examples in source:** 4 (two-mirror geometry; index from angles; apparent depth of a coin; diamond TIR) + the prism computation (42° critical angle) in the applications section.

**Procedures:** reflection geometry (mirror-surface triangle / deviation method); Snell evaluation (identify media → assign angles from the normal → solve); TIR decision (check direction → compute θ_C → compare).

**Common misconceptions in source material:** angles from the surface rather than the normal; frequency changing between media; TIR in the wrong direction; apparent depth formula applied to oblique viewing.

**Difficult concepts:** angle reference convention; frequency invariance; bending direction reasoning; TIR asymmetry; two-mirror geometry.

**Prerequisites:** trigonometry (sine, sin⁻¹); basic wave vocabulary; the electromagnetic field concept (contextual, from Lectures 8–9); no direct dependence on earlier circuit/magnetism lectures — this opens the optics sequence.

**Concept map:**

```
Ray Optics (Ch. 9)
├── Nature of light
│   ├── Optics / Geometric optics / Ray
│   ├── Dual nature: photons ↔ EM transverse waves (EM spectrum)
│   └── v = λf (λ: crest-to-crest; f: cycles/sec)
├── Reflection
│   ├── Rule I: θi = θr · Rule II: coplanar (angles from the NORMAL)
│   ├── Specular (smooth) vs. Diffuse (rough — law still holds)
│   └── Multi-mirror geometry (triangle / deviation method)
├── Refraction
│   ├── sinθ1/sinθ2 = v1/v2 → Snell: n1 sinθ1 = n2 sinθ2
│   ├── n = c/v ≥ 1 · relative index n12 = n2/n1 · β = θ1 − θ2
│   └── Boundary: v, λ change (λm = λair/nm) · f NEVER changes
├── Apparent depth (observer directly above): d′ = d(n2/n1)
└── Total internal reflection
    ├── Only high-n → low-n · bend away → θC (refraction = 90°) → TIR
    ├── sin θC = n2/n1
    └── Applications: prisms (90°/180° turns, binoculars) · fibers (core/cladding, endoscopy)
```

**Dependencies:** first optics lecture — starts a new sequence (Chapters 9–10); prerequisites are mathematical (trigonometry) rather than from earlier lectures.

---

# 2. COURSE / MODULE / LESSON METADATA

| Field | Value |
|---|---|
| **COURSE** | PHY 211 — Physics II |
| **MODULE** | Ray Optics (Chapter 9) |
| **LESSON** | Lecture 10 — The Nature of Light and the Principles of Ray Optics |
| **TOPICS** | Nature of light; reflection; refraction & Snell's law; boundary behavior of wave quantities; apparent depth; total internal reflection; prisms; fiber optics |
| **PREREQUISITES** | Trigonometry (sine, inverse sine); basic wave vocabulary (crest, trough, cycle); EM-field concept (contextual) |
| **COMPETENCIES** | Use the ray model; apply both reflection laws; solve multi-mirror geometry; compute refractive indices and apply Snell's law; state which quantities change at a boundary; compute apparent depth (directly-overhead case); compute critical angles and decide when TIR occurs; explain prism and fiber-optic operation |
| **DIFFICULTY** | Overall: MEDIUM · Snell computations & apparent depth: MEDIUM · Boundary wave-quantity reasoning (f invariance) and TIR decision logic: HARD |
| **ESTIMATED STUDY TIME** | ~3 hours (lesson 70 min · worked examples 30 min · practice 45 min · videos 16 min · self-check & transfer 30 min) |

**ARETE flow placement:**
- **LEARN:** nature of light, reflection laws, refraction definitions.
- **PRACTICE:** Snell's law and critical-angle computations.
- **PROVE:** TIR decision problems (direction check → θ_C → comparison); boundary-quantity reasoning.
- **REMEDIATE/RETRY targets:** angle reference (normal, not surface); the n₂/n₁ ratio direction; frequency invariance.
- **TRANSFER:** fiber/prism design; layered media; multi-mirror geometry in new configurations.
- **MASTER:** design chains (choose a cladding index for a target θ_C) and multi-interface light paths.

---

# 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Define optics and geometric optics, and explain the ray model used to describe reflection and refraction.
2. State the dual nature of light (photon stream vs. transverse electromagnetic wave, part of the EM spectrum).
3. Apply v = λf with precise definitions of wavelength and frequency.
4. State and apply both laws of reflection, with angles measured from the normal; distinguish specular from diffuse reflection.
5. Solve two-mirror reflection geometry problems.
6. State the refraction law, define refractive index and relative refractive index, and apply Snell's law in both directions.
7. Explain which wave quantities change at a boundary and compute λ in a medium (λm = λair/nm).
8. Apply the apparent-depth relation d′ = d(n₂/n₁) for an observer directly above a submerged object.
9. Define the critical angle, compute it, and decide whether total internal reflection occurs for a given interface and incidence angle.
10. Describe how 45°–90°–45° prisms and optical fibers exploit total internal reflection.

---

# 4. WEB-READY LESSON

# Lecture 10 — The Nature of Light and the Principles of Ray Optics

## Prerequisites
The student should already understand:
- Trigonometry: sine of an angle and sin⁻¹.
- Basic wave vocabulary: crest, trough, cycle.
- The idea of an electromagnetic field (context from Lectures 8–9).

---

### 1. The Nature of Light

**Core Idea**
Optics is the physics branch that studies light — its nature, properties, and optical instruments. Geometric optics studies reflection and refraction by representing light as **rays**. Light itself has a **dual nature**: in some cases a stream of particles (photons), in others a transverse electromagnetic wave.

**Explanation**
To describe reflection and refraction, geometric optics replaces the full wave picture with a **ray**: *a straight line drawn along the direction of propagation of the wave, showing the path of the wave as it travels through space.* Every ray is emitted from a source of light — the ray model is a bookkeeping tool, not a claim about what light "is."

What light *is* depends on the experiment: it can be considered a stream of particles called **photons**, or **electromagnetic waves** — transverse waves, part of the **EM spectrum** (shown as a figure in the source; further details [SOURCE DOES NOT SPECIFY]). Light has a **dual nature**: sometimes wave-like, sometimes particle-like.

For any wave, including light:

**v = λf** — speed = wavelength × frequency, where **λ** is the distance between two successive crests or troughs, and **f** is the number of complete cycles per second.

**Example**
A wave with λ = 600 nm and f = 5.0 × 10¹⁴ Hz travels at v = λf = 3.0 × 10⁸ m/s — the speed of light in air.

**Key Point**
The ray is a model for tracing paths; light itself is both photon-stream and EM wave; every wave obeys v = λf.

### 2. Reflection of Light

**Core Idea**
Reflection is the rebounding back of light when it meets a reflecting surface, governed by two rules — and the angles are always measured **from the normal**.

**Explanation**
The **angle of incidence** is the angle between the incident ray and the **normal** to the surface; the **angle of reflection** likewise between the reflected ray and the normal. The two rules:

- **Rule I:** θ_i = θ_r (angle of incidence = angle of reflection).
- **Rule II:** the incident ray, the reflected ray, and the normal to the reflecting surface all lie in **one plane**.

Reflection comes in two types:
- **Specular reflection** — on a *smooth* surface (one clean reflected beam).
- **Diffuse reflection** — on a *rough* surface: the law of reflection *still holds* at every point, but the surface's local normals point in different directions, so the reflected rays scatter.

**Example**
Two mirrors at 120°; a ray strikes M₁ at 65° to the normal — after reflecting from both mirrors, it leaves M₂ at **55°** to the normal. (Full geometric solution: Worked Example 1.)

**Key Point**
θ_i = θ_r, all three lines coplanar, angles from the **normal** — and the law holds even on rough surfaces (diffuse reflection).

### 3. Refraction and the Refractive Index

**Core Idea**
Refraction is the change of direction of light as it passes from one medium to another. The bending is quantified by Snell's law using each medium's refractive index, n = c/v.

**Explanation**
The **angle of refraction** is between the refracted ray and the normal. The refraction law in speed form:

**sin θ₁ / sin θ₂ = v₁ / v₂** — with the key fact: the speed of light is **higher in the less dense medium**.

The **angle of deviation** is β = θ₁ − θ₂, the angle between the refracted ray and the extension of the incident ray.

**Refractive index:** the ratio of the speed of light in air (vacuum), c = 3 × 10⁸ m/s, to the speed in the medium:

**n = c/v** — unitless, with n ∝ 1/v: n = 1 for air and n > 1 for any other medium (e.g., n_water = c/v_water, n_glass = c/v_glass, n_oil = c/v_oil).

The **relative refractive index** between two media is the ratio of their indices: **n₁₂ = n₂/n₁**.

**Snell's law:**

**n₁ sin θ₁ = n₂ sin θ₂**

**Example**
A 550 nm beam in air strikes a slab at 40° and refracts at 26°: n₂ = (1 × sin 40°)/(sin 26°) = 1.47. (Worked Example 2.)

**Key Point**
n = c/v (≥ 1); Snell's law with angles from the normal; light travels faster in the less dense medium.

### 4. What Changes at a Boundary

**Core Idea**
When light passes from one medium to another, the **speed v and the wavelength λ change — the frequency f does not**.

**Explanation**
With f fixed and v different on each side, v₁ = λ₁f and v₂ = λ₂f give:

**n₁/n₂ = v₂/v₁ = λ₂/λ₁** — so n ∝ 1/λ, and inside a medium:

**λ_medium = λ_air / n_medium**

Entering a denser medium: v drops, λ shrinks by the same factor, f is untouched. Leaving back to air: both grow back. The unchanged frequency is the anchor of every boundary problem.

**Example**
600 nm light in air entering glass (n = 1.5): λ_glass = 600/1.5 = **400 nm**; the frequency stays 5.0 × 10¹⁴ Hz. (Worked Example 6.)

**Key Point**
f is the invariant; v and λ scale together (both ÷ n going in, × n coming out).

### 5. Apparent Depth

**Core Idea**
An object lying under water appears closer to the surface than it actually is.

**Explanation**
For a general (oblique) viewing angle, determining the apparent depth is difficult (the source's Figure a). The simple case (Figure b) is an observer **directly above** the submerged object, where the apparent depth d′ relates to the actual depth d by:

**d′ = d(n₂/n₁)**

with n₁ the medium of the object (water) and n₂ the medium of the observer (air). Since n₂ < n₁ looking into water, d′ < d: distances along the line of sight appear compressed.

**Example**
A coin at the bottom of a 3.00 m pool, viewed from directly above: d′ = 3.00 × (1/1.33) = **2.26 m**. (Worked Example 3.)

**Key Point**
Looking straight down into water, depths appear shrunk by the ratio of indices — the formula is for the directly-overhead case only.

### 6. Total Internal Reflection

**Core Idea**
Light going from a **higher**-index medium toward a **lower**-index one bends *away* from the normal. Beyond the critical angle, no light escapes at all — it is totally reflected back inside.

**Explanation**
The progression as the incidence angle grows (high n → low n):
1. The refracted ray bends **away from the normal**; as θ₁ increases, θ₂ increases faster.
2. At the **critical angle θ_C**, the refraction angle reaches exactly **90°** — the refracted ray points *along the surface*.
3. For incidence **exceeding** θ_C, there is no refracted light: all the incident light is reflected back into the original medium — **total internal reflection (TIR)**.

Applying Snell's law at the critical angle (n₁ sin θ_C = n₂ sin 90°):

**sin θ_C = n₂/n₁  →  θ_C = sin⁻¹(n₂/n₁)**

**TIR occurs only when light travels from higher index toward lower index.** It never occurs in reverse — e.g., from air into water, the refraction angle is always *smaller* than the incidence angle and can never reach 90°.

**Example**
Light inside diamond (n₁ = 2.42) strikes a diamond–air interface at 28°: θ_C = sin⁻¹(1/2.42) = 24.4°; 28° > 24.4° → totally reflected. With water instead (n₂ = 1.33): θ_C = 33.3°; 28° < 33.3° → refracted (partially). (Worked Example 4.)

**Key Point**
Check the direction first (high → low only), then compare the incidence angle to θ_C = sin⁻¹(n₂/n₁). At exactly θ_C, refraction is 90°; TIR is strictly *beyond* θ_C.

### 7. Applications: Prisms and Fiber Optics

**Core Idea**
Total internal reflection gives a perfectly efficient mirror — exploited by glass prisms to turn beams through 90° or 180°, and by optical fibers to "pipe" light from one place to another.

**Explanation**
**Prisms:** binoculars, periscopes, and telescopes use 45°–90°–45° glass prisms (n₁ = 1.5). A ray entering and striking the hypotenuse at θ₁ = 45°: the critical angle for glass–air is θ_C = sin⁻¹(1/1.5) = **42°**. Since 45° > 42°, the light is totally reflected at the hypotenuse, directed vertically upward — the beam is turned through **90°**. With two internal reflections, the same prism turns a beam through **180°** — the arrangement used inside binoculars.

**Fiber optics:** hair-thin threads of glass or plastic — **optical fibers** — pipe light from one place to another. A fiber consists of a cylindrical inner **core** that carries the light and an outer concentric shell, the **cladding**. The core is transparent glass or plastic with a **relatively high** index of refraction; the cladding is glass of a type with a **relatively low** index. Light enters one end of the core, strikes the core/cladding interface at an incidence angle **greater than the critical angle**, and is reflected back into the core — traveling along the fiber in a **zigzag path**.

**Medicine:** optical fiber cables have had extraordinary impact — in **endoscopy**, a device called an **endoscope** peers inside the body.

**Example**
The 45°–90°–45° prism calculation: θ_C = 42° < 45° → total internal reflection → the 90° turn, lossless. (Worked Example 5.)

**Key Point**
High-index core + low-index cladding (or glass + air at the prism hypotenuse) + incidence beyond θ_C = light trapped and piped wherever you route the fiber.

---

## Key Takeaways
1. Optics studies light; geometric optics studies reflection & refraction using **rays** — straight lines along the propagation direction.
2. Light has dual nature: photons in some cases, transverse EM waves (part of the EM spectrum) in others; v = λf always.
3. Reflection: θ_i = θ_r; incident ray, reflected ray, and normal coplanar; angles from the **normal**; the law holds even for diffuse reflection on rough surfaces.
4. Refraction: sin θ₁/sin θ₂ = v₁/v₂; Snell: n₁ sin θ₁ = n₂ sin θ₂; n = c/v ≥ 1; light is faster in the less dense medium.
5. At a boundary: **v and λ change (λm = λair/nm); f never changes**.
6. Apparent depth (looking straight down): d′ = d(n₂/n₁) — submerged objects look shallower.
7. TIR: only from higher n toward lower n, for incidence beyond θ_C = sin⁻¹(n₂/n₁); at θ_C the refracted ray skims the surface at 90°.
8. Applications: 45° prisms turn beams 90°/180° (θ_C = 42° < 45°) in binoculars/periscopes; fibers pipe light via core(high n)/cladding(low n) zigzag TIR — endoscopy in medicine.

## Self-Check (attempt before looking at answers)
1. What is a light ray, and which branch of optics uses it as its central tool?
2. In which situations does light behave like a wave, and in which like a particle?
3. Define wavelength and frequency precisely, as used in v = λf.
4. State both laws of reflection — and identify the reference line from which all angles are measured.
5. On which type of surface does diffuse reflection occur? Does the law of reflection still hold there?
6. Light passes from air into glass. State what happens to its speed, wavelength, frequency, and direction.
7. Why can the refractive index of a physical medium never be less than 1?
8. State the two conditions required for total internal reflection to occur.
9. What is the refracted ray doing at exactly the critical angle? Does TIR occur *at* θ_C or beyond it?
10. Describe the structure of an optical fiber: which part has the higher index, and why must it be that way?

---

# 5. FORMULAS

| # | Formula | Variables | When it is used | Interpretation & assumptions |
|---|---|---|---|---|
| 1 | v = λf | v: wave speed; λ: wavelength (crest-to-crest); f: frequency (cycles/s) | Any wave, incl. light | In air/vacuum: v = c = 3 × 10⁸ m/s |
| 2 | sin θ₁ / sin θ₂ = v₁ / v₂ | θ₁, θ₂: angles from the normal in each medium | Refraction (speed form) | v is higher in the less dense medium |
| 3 | β = θ₁ − θ₂ | β: angle of deviation | Refraction geometry | Between the refracted ray and the extension of the incident ray |
| 4 | n = c/v | c = 3 × 10⁸ m/s | Refractive index of a medium | Unitless; n = 1 (air), n > 1 elsewhere; n ∝ 1/v |
| 5 | n₁₂ = n₂/n₁ | n₁, n₂: indices of the two media | Relative refractive index | Ratio between the two media's indices |
| 6 | n₁ sin θ₁ = n₂ sin θ₂ | — | Snell's law | Angles from the normal; works in both directions |
| 7 | n₁/n₂ = v₂/v₁ = λ₂/λ₁ | — | Boundary behavior | f is invariant; v and λ scale together |
| 8 | λ_m = λ_air / n_m | — | Wavelength inside a medium | λ shrinks by n entering; restored leaving |
| 9 | d′ = d(n₂/n₁) | d: actual depth; n₁: object's medium; n₂: observer's medium | Apparent depth | **Observer directly above** the object only |
| 10 | sin θ_C = n₂/n₁ → θ_C = sin⁻¹(n₂/n₁) | n₁: higher index (light starts here); n₂: lower index | Critical angle | TIR only for high → low and θ > θ_C; at θ_C, refraction = 90° |

*(Reflection laws: θ_i = θ_r; coplanarity of incident ray, reflected ray, normal.)*

---

# 6. WORKED EXAMPLES

**WE 1 — Two mirrors at 120° (Source Example 1)**
Two mirrors make an angle of 120°; a ray is incident on M₁ at 65° to the normal. Find the angle the ray makes with the normal to M₂ after reflecting from both mirrors.
*(The source's printed solution is a figure; the following is the standard geometric reconstruction, cross-checked two ways.)*
1. After reflecting from M₁, the ray leaves at 65° to M₁'s normal → 90° − 65° = **25° to M₁'s surface**.
2. Triangle formed by the two hit points and the corner where the mirrors meet: corner angle = 120°, angle at the first hit = 25°.
3. Angle between the ray and M₂'s surface at the second hit = 180° − 120° − 25° = **35°**.
4. Angle to M₂'s normal = 90° − 35° = **55°**.
5. *Cross-check (deviation method):* total deviation after two reflections = 360° − 2(120°) = 120°; the first reflection deviates 180° − 2(65°) = 50°; the second must deviate 70°, which corresponds to θ₂ = (180° − 70°)/2 = **55°** ✓.

**WE 2 — Refractive index from angles (Source Example 2)**
A 550 nm beam travels in air, strikes a transparent slab at 40° to the normal, and refracts at 26°. Find the slab's index.
1. n₁ = 1 (air), θ₁ = 40°, θ₂ = 26°.
2. Snell: n₂ = n₁ sin θ₁ / sin θ₂.
3. **n₂ = (1 × sin 40°)/(sin 26°) = 0.643/0.438 = 1.47.**

**WE 3 — Apparent depth of a coin (Source Example 3)**
A swimmer at the surface of a 3.00 m pool sees a coin on the bottom directly below. How deep does it appear?
1. Observer directly above → d′ = d(n₂/n₁), with n₁ = 1.33 (water), n₂ = 1 (air).
2. d′ = 3.00 × (1/1.33).
3. **d′ = 2.26 m** — the coin looks ~0.74 m closer than it is.

**WE 4 — Total internal reflection at a diamond interface (Source Example 4)**
A beam propagates through diamond (n₁ = 2.42) and strikes a diamond–air interface at 28°.
(a) With air (n₂ = 1):
1. θ_C = sin⁻¹(n₂/n₁) = sin⁻¹(1/2.42) = sin⁻¹(0.413).
2. **θ_C = 24.4°.** Since 28° > 24.4° → **no refraction; total internal reflection.**
(b) With water (n₂ = 1.33) surrounding the diamond:
1. θ_C = sin⁻¹(1.33/2.42) = sin⁻¹(0.550).
2. **θ_C = 33.3°.** Since 28° < 33.3° → the beam is **refracted into the water** (partially refracted, partially reflected).

**WE 5 — The 45°–90°–45° prism (from the source's applications section)**
A ray enters a 45°–90°–45° glass prism (n₁ = 1.5) and strikes the hypotenuse at θ₁ = 45°. What happens?
1. Critical angle at the glass–air interface: θ_C = sin⁻¹(n₂/n₁) = sin⁻¹(1/1.5) = sin⁻¹(0.667).
2. **θ_C = 42°.**
3. 45° > 42° → total internal reflection at the hypotenuse — the beam is turned through **90°**.
4. With a second internal reflection, the same prism turns a beam through **180°** — the folding used in binoculars.

**WE 6 — Wavelength and frequency in a medium (pedagogical example — the source states the relations without a numerical application)**
Light of wavelength 600 nm in air enters glass (n = 1.5). Find λ in the glass and the frequency.
1. λ_glass = λ_air/n = 600 nm / 1.5 = **400 nm**.
2. f is unchanged across the boundary: f = c/λ_air = (3 × 10⁸)/(600 × 10⁻⁹) = **5.0 × 10¹⁴ Hz** — the same value in air and in glass.
3. Check inside the glass: v = c/n = 2.0 × 10⁸ m/s and v = λf = (400 × 10⁻⁹)(5.0 × 10¹⁴) = 2.0 × 10⁸ m/s ✓.

---

# 7. COMMON MISTAKES

| # | What students usually do | Why it's wrong | How to avoid it |
|---|---|---|---|
| 1 | Measure optical angles from the surface | Both reflection and refraction laws define angles from the **normal** | Draw the normal first, every single time |
| 2 | Say the frequency changes between media | f is the invariant — crests can't pile up or vanish at the boundary | Lock in: "f fixed; v and λ scale together" |
| 3 | Say the wavelength stays the same | λ must shrink with v (λ = v/f) in a denser medium: λm = λair/nm | Compute λm = λair/n whenever the light enters a medium |
| 4 | Reverse the critical-angle ratio (sin θ_C = n₁/n₂) | n₁ must be the **higher** index — the medium the light starts in | Derive it once from n₁ sin θ_C = n₂ sin 90°, never memorize blindly |
| 5 | Apply TIR when light goes air → water (low → high) | TIR requires high → low only; in reverse, θ₂ < θ₁ always and can never reach 90° | Check the direction *before* computing anything |
| 6 | Think TIR happens *at* the critical angle | At θ_C the refracted ray is at 90° (skim); TIR is strictly for θ > θ_C | Compare with "greater than," not "greater or equal" |
| 7 | Use the apparent-depth formula for oblique viewing | d′ = d(n₂/n₁) holds for the observer **directly above** (the source's simple case) | Check "directly overhead?" before applying |
| 8 | In two-mirror problems, measure angles between the ray and the mirror surface instead of using the triangle correctly | The geometry runs through the triangle: corner angle + surface angle at the first hit | Convert incidence to the surface angle (90° − θ), then use the triangle's 180° sum |
| 9 | Confuse the angle of deviation β with the angle of refraction | β = θ₁ − θ₂ is between the refracted ray and the *extension* of the incident ray | Label β separately on every refraction sketch |
| 10 | Use c as the light speed inside a medium | Inside a medium v = c/n — slower in denser media | Attach "c/n" to every speed question involving a medium |

---

# 8. LECTURE SUMMARY

# Lecture Summary — The Nature of Light and Ray Optics

## What You Need to Know
- The ray model and the dual nature of light, with v = λf.
- Both reflection laws (angles from the normal) and specular vs. diffuse reflection.
- Snell's law, refractive index, relative index, and the deviation angle.
- Which wave quantities change at a boundary — and the one that never does.
- The apparent-depth relation for the directly-overhead observer.
- The critical angle, the TIR direction condition, and the decision procedure.
- How prisms (90°/180° turns) and optical fibers (core + cladding) use TIR.

## Key Definitions
- **Optics** → the physics branch studying light, its nature, properties, and optical instruments.
- **Geometric optics** → the branch studying reflection and refraction using rays.
- **Ray** → a straight line along the direction of propagation, showing the wave's path.
- **Wavelength (λ)** → distance between two successive crests or troughs.
- **Frequency (f)** → number of complete cycles per second.
- **Angle of incidence/reflection/refraction** → angle between the corresponding ray and the normal.
- **Angle of deviation (β = θ₁ − θ₂)** → angle between the refracted ray and the extension of the incident ray.
- **Refractive index (n = c/v)** → ratio of light's speed in air/vacuum to its speed in the medium; unitless; n ≥ 1.
- **Relative refractive index (n₁₂ = n₂/n₁)** → ratio of two media's indices.
- **Critical angle (θ_C)** → the incidence angle (in the higher-index medium) giving a 90° refraction angle in the lower-index medium.
- **Total internal reflection** → all incident light reflected back when incidence exceeds θ_C going high → low.
- **Optical fiber** → core (high n) + cladding (low n); light zigzags by repeated TIR. **Endoscope** → medical fiber device to peer inside the body.

## Key Formulas
- v = λf → wave relation.
- sin θ₁/sin θ₂ = v₁/v₂; n₁ sin θ₁ = n₂ sin θ₂ → refraction (speed form; Snell).
- n = c/v; n₁₂ = n₂/n₁; β = θ₁ − θ₂ → index, relative index, deviation.
- n₁/n₂ = v₂/v₁ = λ₂/λ₁; λm = λair/nm → boundary behavior (f invariant).
- d′ = d(n₂/n₁) → apparent depth (directly overhead).
- sin θ_C = n₂/n₁ → critical angle (high → low only).

## Important Ideas
- The ray is a model; light itself is both photon-stream and transverse EM wave.
- Reflection law holds everywhere — even on rough surfaces (diffuse).
- Frequency is untouchable at boundaries; speed and wavelength pay the price.
- TIR is a *directional* phenomenon: it exists only escaping toward a lower index.
- TIR is a perfect mirror — which is why prisms and fibers beat coated mirrors for folding and piping light.

## Common Mistakes
Angles from the surface; frequency "changing"; wavelength "constant"; reversed θ_C ratio; TIR in the wrong direction; TIR "at" θ_C; apparent depth applied obliquely; two-mirror triangle mishandled; β confused with θ₂; c used inside media.

## Exam Focus
1. Snell's law with angles correctly referenced (both directions, including finding n from angles).
2. The boundary-quantity question: what changes, what doesn't — with λm = λair/nm computation.
3. The full TIR decision: direction check → θ_C computation → comparison (diamond-style problems, including the surrounding-medium variation).
4. Two-mirror geometry via the triangle method.
5. Apparent depth for the directly-overhead case.

## 60-Second Review
Light: dual nature — photons or transverse EM waves; rays trace its paths; v = λf. Reflection: θi = θr, coplanar, angles from the normal; rough surfaces still obey (diffuse). Refraction: n₁ sinθ₁ = n₂ sinθ₂; n = c/v ≥ 1; light faster in the less dense medium. At a boundary: v and λ change, f never; λm = λair/nm. Looking straight down into water: d′ = d(n₂/n₁) — things look shallower. TIR: high → low only; sinθ_C = n₂/n₁; beyond θ_C, 100% reflection. Prisms: 42° < 45° → 90°/180° turns. Fibers: high-n core, low-n cladding, zigzag light — endoscopes.

---

# 9. DIFFICULT CONCEPTS

### Difficult Concept: Angles Are Measured from the Normal
**Why students struggle:** The surface is the visible line; the normal is invisible and must be constructed.
**Simple explanation:** Both laws are *defined* relative to the perpendicular to the surface — the normal — not the surface itself.
**Intuitive analogy:** Latitude is measured from the equator, not the coastline — an agreed reference line, even if it isn't drawn on the ground.
**Step-by-step:** (1) Find the point where the ray meets the surface. (2) Draw the perpendicular to the surface there. (3) Measure every angle (θ_i, θ_r, θ₁, θ₂) between the ray and that perpendicular.
**Mini example:** A ray "50° to the surface" strikes a mirror: the angle of incidence is 90° − 50° = 40°.
**Misconception to avoid:** "The angle with the surface is the angle of incidence."
**Difficulty: MEDIUM**

### Difficult Concept: The Dual Nature of Light
**Why students struggle:** Students want one answer: "Is light a wave or a particle?"
**Simple explanation:** Light behaves as a wave in some situations and as a particle (photon stream) in others — the source's statement of dual nature.
**Intuitive analogy:** A colleague who is a strict accountant at work and a relaxed guitarist at home — neither description is wrong; the context selects the behavior.
**Step-by-step:** (1) For reflection/refraction path-tracing → use the ray model. (2) For boundary wave quantities (λ, f) → use the wave picture. (3) In particle-context experiments → photons. (4) Never force one picture onto all situations.
**Mini example:** Ray tracing in a prism (particle-like path) and wavelength shrinking inside it (wave behavior) coexist in the same problem.
**Misconception to avoid:** "Light was proven to be a wave, so the particle idea is obsolete" (or vice versa).
**Difficulty: EASY**

### Difficult Concept: The Unchanging Frequency at a Boundary
**Why students struggle:** Three quantities are in play; students guess which one stays fixed, and "denser medium" intuitions push them toward changing f.
**Simple explanation:** Wave crests cannot pile up or vanish at the boundary — arrivals per second must equal departures per second — so f is identical on both sides; with speed dropping, the wavelength must shrink to compensate.
**Intuitive analogy:** A border checkpoint: cars arrive at a rate and leave at the same rate; if the road beyond is slower, the cars just travel closer together — the flow rate (frequency) is preserved.
**Step-by-step:** (1) v = λf on each side. (2) f₁ = f₂ (crest bookkeeping at the boundary). (3) v₂ = c/n₂ < v₁ → λ₂ = v₂/f shrinks. (4) λ₂/λ₁ = v₂/v₁ = n₁/n₂ → λm = λair/nm.
**Mini example:** 600 nm air → glass (n = 1.5): λ becomes 400 nm; f stays 5.0 × 10¹⁴ Hz.
**Misconception to avoid:** "The frequency increases in a denser medium" (or "the wavelength is unchanged").
**Difficulty: HARD** → video provided

### Difficult Concept: Which Way Does the Light Bend?
**Why students struggle:** "Denser medium" and "toward/away from the normal" get paired wrongly under exam pressure.
**Simple explanation:** Light is faster in the less dense medium; entering a slower medium bends the ray toward the normal, and leaving it bends the ray away.
**Intuitive analogy:** A marching band wheeling from pavement onto sand: the side that hits the sand first slows, and the whole line pivots *toward* the slow side.
**Step-by-step:** (1) Identify n₁ and n₂. (2) n₂ > n₁ (slower ahead) → bends toward the normal (θ₂ < θ₁). (3) n₂ < n₁ (faster ahead) → bends away (θ₂ > θ₁). (4) Verify numerically with Snell.
**Mini example:** Air → glass at 30°: sin θ₂ = 0.5/1.5 → θ₂ = 19.5° — toward the normal. Glass → air at 20°: sin θ₂ = 1.5 × 0.342 → θ₂ ≈ 31° — away.
**Misconception to avoid:** "Denser medium bends light away from the normal."
**Difficulty: MEDIUM**

### Difficult Concept: Total Internal Reflection and the Critical Angle
**Why students struggle:** The condition is asymmetric (one direction only), the ratio in sin θ_C is easily reversed, and the boundary case (θ = θ_C) is subtly different from TIR itself.
**Simple explanation:** Escaping toward a lower index, the refraction angle grows faster than the incidence angle; it hits 90° at θ_C, and beyond that no refraction is mathematically possible — everything reflects.
**Intuitive analogy:** A snorkeler looking up at a steep angle sees the water surface turn into a perfect mirror — beyond a certain angle, the outside world simply disappears.
**Step-by-step:** (1) Confirm light goes high n → low n; otherwise stop (no TIR possible). (2) Compute sin θ_C = n₂/n₁. (3) Compare: θ < θ_C → refraction (plus partial reflection); θ = θ_C → refracted ray at 90°; θ > θ_C → total internal reflection.
**Mini example:** Diamond → air: θ_C = 24.4° — a mere 28° incidence traps the light completely.
**Misconception to avoid:** "TIR happens whenever the incidence angle is large," regardless of direction — and reversing the n-ratio.
**Difficulty: HARD** → video provided

### Difficult Concept: Apparent Depth
**Why students struggle:** The formula looks like it came from nowhere, and students apply it to any viewing angle.
**Simple explanation:** Refraction redirects the rays leaving the underwater object; your eye traces them back along straight lines, placing the object shallower than it is. The clean formula holds for the observer directly above.
**Intuitive analogy:** A straw in a glass of water looks broken at the surface — your eye assumes light always travels straight, but refraction bent it.
**Step-by-step:** (1) Confirm the observer is directly above. (2) Identify n₁ (object's medium) and n₂ (observer's medium). (3) d′ = d(n₂/n₁). (4) For water viewed from air: d′ = d/n_water < d.
**Mini example:** 3.00 m pool: the coin appears at 2.26 m — about 25% shallower.
**Misconception to avoid:** "The water actually makes the object smaller/closer in 3-D" — only the depth along the line of sight is affected, and only for the overhead case by this formula.
**Difficulty: MEDIUM**

---

# 10. VIDEO LESSON PLANS

---

**VIDEO 1**

**VIDEO TITLE:** "One Thing Light Never Changes at a Border"
**TARGET CONCEPT:** Boundary behavior of speed, wavelength, and frequency; connection to Snell's law and bending
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** State which quantities change when light crosses a boundary, compute λ inside a medium, and explain why the speed change bends the beam.
**HOOK:** Light crosses from air into glass — three properties are on the table: speed, wavelength, frequency. Two change instantly. One *cannot ever* change — and that single fact hands you easy points on every optics exam.
**EXPLANATION:** (1) v = λf with precise definitions. (2) The checkpoint argument: crests arriving = crests departing → f identical on both sides. (3) Speed drops in the denser medium (v = c/n) → λ must shrink: λm = λair/nm. (4) Why the beam bends: wavefronts hitting at an angle, one side slows first → pivot toward the normal (Snell). (5) Worked numbers.
**VISUALS:** Wavefronts crossing a boundary, crests visibly closer together in the dense medium; a "border checkpoint" animation with wave-crests passing through at a fixed rate; a marching band wheeling from pavement onto sand (cadence constant, steps shorten, line pivots); a table filling in v, λ, f for air vs. glass; Snell solved on screen.
**EXAMPLE:** 600 nm light, air → glass (n = 1.5): λ = 400 nm, f = 5.0 × 10¹⁴ Hz unchanged; entering at 30° → refracts at 19.5°.
**COMMON MISTAKE:** Saying frequency changes; saying wavelength is constant; using c as the speed inside a medium.
**CHECK FOR UNDERSTANDING:** "Light of 500 nm enters a medium with n = 2. What is the wavelength inside — and what is the frequency?"
**FINAL TAKEAWAY:** f is the invariant; v and λ scale together (÷n in, ×n out); the angled speed change is what bends the beam.

---

**VIDEO 2**

**VIDEO TITLE:** "The Perfect Mirror: Total Internal Reflection"
**TARGET CONCEPT:** Critical angle, the direction condition for TIR, and the prism/fiber applications
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Compute the critical angle, decide when TIR occurs for any interface, and explain prism and fiber-optic operation.
**HOOK:** There's a piece of glass that reflects 100% of the light hitting it — no coating, no silvering. It folds light paths inside binoculars, pipes light through hair-thin glass, and lets doctors see inside the body. It only works in one direction.
**EXPLANATION:** (1) High n → low n: refraction bends away from the normal; θ₂ grows faster than θ₁. (2) At θ_C, θ₂ = 90° (ray skims the surface). (3) Beyond θ_C, sin θ₂ would exceed 1 — impossible → all light reflects: TIR. (4) sin θ_C = n₂/n₁. (5) The asymmetry: air → water can never TIR. (6) Worked example (diamond, two surroundings). (7) Applications: 45° prism (θ_C = 42° < 45° → 90°/180° turns); fiber core/cladding zigzag; endoscopy.
**VISUALS:** Animated refraction diagram with θ₁ slider: the refracted ray sweeping toward 90°, then vanishing at θ_C with a "NO SOLUTION for sin θ₂ > 1" stamp; the water-surface-as-mirror snorkeling view; the prism geometry turning a beam 90°, then 180°; a cutaway optical fiber with a zigzag ray trapped between core and cladding; an endoscope silhouette.
**EXAMPLE:** Diamond (n₁ = 2.42) at 28°: θ_C = 24.4° → TIR; surrounded by water (n₂ = 1.33): θ_C = 33.3° → refracts.
**COMMON MISTAKE:** Reversing the n₂/n₁ ratio; applying TIR from air into water; thinking TIR occurs exactly at θ_C.
**CHECK FOR UNDERSTANDING:** "Light inside water (n = 1.33) heads toward air at 50° — does it escape?"
**FINAL TAKEAWAY:** TIR = high → low only, beyond θ_C = sin⁻¹(n₂/n₁); at θ_C the ray skims at 90°; beyond it, glass becomes a perfect mirror.

---

# 11. VIDEO SCRIPTS

---

## SCRIPT 1 — "One Thing Light Never Changes at a Border"

**[0:00–0:30] Hook**
When a beam of light crosses from air into glass, three of its properties are on the table: its speed, its wavelength, its frequency. Two of them change the instant it crosses. One of them cannot change — not ever, not at any border, not in any material. And that single unchangeable fact explains why light bends, why its wavelength shrinks, and it will hand you points on every optics exam you ever sit.

**[0:30–2:00] Concept introduction**
First, the toolkit. For any wave — including light — speed equals wavelength times frequency: v = λf. The wavelength is the distance between two successive crests. The frequency is the number of complete cycles per second. In air, light travels at v = c, three times ten to the eighth meters per second.

Now the border. Light slows down inside glass — the speed becomes c over n, where n is the refractive index. So v drops. The question is: what happens to λ and f? Here's the argument you'll never forget. Picture the boundary as a checkpoint. Wave crests arrive at the glass at some rate — f cycles per second. Ask yourself: can crests pile up at the border? No — that would require infinite amplitude. Can crests vanish? No — a wave can't just lose cycles. Arrivals must equal departures. The frequency on the glass side is *identical* to the frequency on the air side. Frequency is the invariant.

**[2:00–4:00] Visual explanation**
But if the speed dropped and the frequency can't change, something else must give — and it's the wavelength. From v = λf: λ equals v over f. The speed is smaller, the frequency is the same, so the wavelength shrinks by exactly the same factor that the speed did. Going from air into a medium with index n: wavelength inside equals wavelength in air, divided by n.

Numbers. Six hundred nanometers of light, air into glass with n = 1.5. Wavelength inside: six hundred divided by one point five — four hundred nanometers. Exactly two-thirds. The frequency? Still five times ten to the fourteenth hertz — untouched. And here's the check that proves it: inside the glass, v = c/n = two times ten to the eighth, and λf = four hundred nanometers times five times ten to the fourteenth — two times ten to the eighth. Consistent, everywhere.

Now, the bend. When the wavefront hits the boundary *at an angle*, one side of the wavefront enters the slow medium before the other side. The slow side drags; the fast side keeps moving — the whole wavefront pivots, like a marching band wheeling from pavement onto sand. Note the band analogy in your head: the cadence — the *frequency* — stays locked; the steps — the *wavelength* — get shorter; and the whole line *turns*. That turn is refraction, and its exact recipe is Snell's law: n₁ sine θ₁ equals n₂ sine θ₂.

**[4:00–6:00] Worked example**
Let's do it all in one problem. Light of wavelength six hundred nanometers in air hits glass, n = 1.5, at thirty degrees to the normal. Three questions. One: the wavelength inside. Six hundred over one point five — four hundred nanometers. Two: the frequency. Unchanged — and in air, f = c over λ: three times ten to the eighth, divided by six hundred times ten to the minus ninth — five times ten to the fourteenth hertz. Three: the refraction angle. Snell: one times sine thirty equals one point five times sine θ₂. Sine thirty is a half. Sine θ₂ = 0.5 over 1.5 = one third — θ₂ ≈ 19.5 degrees. Toward the normal, exactly as the marching band turned. Three quantities tracked, one law of bending — and the frequency never moved.

**[6:00–7:00] Common mistake**
The exam classics. One: "the frequency increases in a denser medium." Never — the checkpoint argument forbids it. Two: "the wavelength stays the same." No — it shrinks with the speed; λ inside = λ air over n. Three: using c as the speed inside glass. The speed inside is c over n. If you catch yourself pairing "denser" with "higher frequency," stop and replay the checkpoint.

**[7:00–8:00] Quick student challenge**
Two questions. Light of five hundred nanometers enters a medium with n = 2. Wavelength inside? … Five hundred over two — two hundred fifty nanometers. Frequency? … Unchanged — same as it was in air, six times ten to the fourteenth hertz. Second: the light now goes back *out* of the glass into air. What happens to the wavelength and speed? … Both grow back — multiplied by n — and the frequency? Still fixed. Always fixed.

**[8:00–8:30] Final recap**
One sentence to carry out of this video: at any border, frequency never changes; speed and wavelength scale together — divided by n going in, multiplied by n coming out. And when the border is met at an angle, that speed change pivots the beam — refraction, Snell's law. One invariant, two followers, one bend. That's the whole boundary story.

---

## SCRIPT 2 — "The Perfect Mirror: Total Internal Reflection"

**[0:00–0:30] Hook**
There is a piece of glass that reflects one hundred percent of the light that hits it — no mirror coating, no silvering, nothing. It's how binoculars fold a long light path into a short tube, how hair-thin glass threads pipe light around corners, and how doctors peer inside the human body without surgery. The trick is called total internal reflection — and it only works in one direction.

**[0:30–2:00] Concept introduction**
Set it up. Light is *inside* a medium with a high refractive index — water, n = 1.33 — heading toward a medium with a lower index — air, n = 1. Snell's law: n₁ sine θ₁ equals n₂ sine θ₂. Now watch the consequence of the indices being backwards from the usual story. Since n₂ is *smaller* than n₁, sine θ₂ must be *bigger* than sine θ₁. The refracted ray bends *away* from the normal.

Push the incidence angle up, and the refraction angle climbs even faster. At some special incidence angle, θ₂ reaches exactly ninety degrees — the refracted ray points *along the surface*, skimming it like a stone on a pond. That incidence angle is the critical angle, θ_C. And here's the punchline: push the incidence angle just one degree beyond θ_C. Snell's law now demands sine θ₂ bigger than one. Impossible — there is no solution. No refracted ray exists at all. Every last bit of light reflects back into the water. That is total internal reflection: a perfect mirror, made from nothing but an angle.

**[2:00–4:00] Visual explanation**
The formula. At the critical angle itself, Snell reads: n₁ sine θ_C equals n₂ sine ninety — and sine ninety is just one. So sine θ_C equals n₂ over n₁. Memorize it *by its structure*: the small index sits on top — the index of the medium you're *trying to escape into*. Numbers: water to air, sine θ_C = one over 1.33 — θ_C ≈ 48.8 degrees. Diamond to air: one over 2.42 — a mere 24.4 degrees. That tiny critical angle is why light rattles around inside a diamond so many times before finding an escape — the familiar reason it sparkles. *(That last framing is the everyday illustration; the physics is the 24.4°.)*

Now the asymmetry — the part everyone misses. Total internal reflection only exists going from *higher* index toward *lower*. Send the light the other way — air into water — and Snell makes θ₂ *smaller* than θ₁. The refracted angle starts shrinking and can never climb toward ninety. No critical angle exists in that direction. TIR is a one-way street. One more subtlety: *exactly at* θ_C, the refracted ray is at ninety degrees — skimming the surface. Total internal reflection is strictly *beyond* θ_C.

**[4:00–6:00] Worked example and applications**
The lecture's own example. A beam travels *inside* diamond, n = 2.42, and hits a diamond–air boundary at twenty-eight degrees. Critical angle: sine inverse of one over 2.42 — 24.4 degrees. Twenty-eight is bigger than 24.4 — no refraction; the beam is totally reflected back into the diamond. Now change the surroundings: dip the diamond in water, n = 1.33. Critical angle: sine inverse of 1.33 over 2.42 — 33.3 degrees. Twenty-eight is now *less* than 33.3 — the beam refracts out into the water, partially reflected, partially escaped. Same diamond, same angle — the second medium decides everything.

Applications. Take a glass prism with angles forty-five, ninety, forty-five — n = 1.5. A ray enters and hits the long side, the hypotenuse, at forty-five degrees. Critical angle for glass–air: sine inverse of one over 1.5 — forty-two degrees. Forty-five beats forty-two: total internal reflection — and the beam exits turned through exactly ninety degrees. Add a second reflection: one hundred eighty. That's how binoculars, periscopes, and telescopes fold long light paths into short instruments — with essentially lossless mirrors.

And the fiber. An optical fiber is a hair-thin thread with two layers: a core with a relatively high index, and a surrounding cladding with a relatively low index. Light enters the core and strikes the core–cladding boundary at an angle beyond the critical angle — reflected back in — again — again — a zigzag path, carrying the light wherever you route the fiber. In medicine, bundles of such fibers form an endoscope, letting doctors see inside the body. A perfect mirror, a zigzag, and a window into the human interior — all from one inequality: θ greater than θ_C.

**[6:00–7:00] Common mistake**
Three classics. One: reversing the ratio — sine θ_C is n₂ over n₁, with n₁ the *higher* index, the medium the light starts in. If your critical angle comes out bigger than you expected, check the ratio first. Two: applying TIR from air into water — wrong direction; impossible; the refraction angle only shrinks that way. Three: claiming TIR happens *at* the critical angle — at θ_C the refracted ray skims at ninety degrees; total reflection is strictly beyond.

**[7:00–8:00] Quick student challenge**
Try this. Light inside water, n = 1.33, heads toward the air above at fifty degrees to the normal. Does it escape? Compute: θ_C = sine inverse of one over 1.33 — 48.8 degrees. Fifty is greater than 48.8 — totally internally reflected. The water keeps it. Second: the same ray, but traveling from *air* into water at fifty degrees — total internal reflection? … Never. Wrong direction — TIR only exists escaping toward the lower index.

**[8:00–8:30] Final recap**
Total internal reflection in one breath: high index toward low index only; critical angle sine θ_C equals n₂ over n₁; at θ_C the refracted ray skims the surface at ninety degrees; beyond it, one hundred percent reflection — a perfect, coating-free mirror. Prisms use it to turn beams ninety and one hundred eighty degrees; fibers use it to pipe light through a high-index core inside a low-index cladding. One inequality, and glass becomes a mirror.

---

# 12. PRACTICE QUESTIONS

## LEVEL 1 — UNDERSTAND

1. Define optics and geometric optics, and state the concept geometric optics uses to represent light.
2. What is a ray?
3. State the dual nature of light.
4. From v = λf, define wavelength and frequency precisely (as the source defines them).
5. State the two laws of reflection, and identify the reference line for all angles.
6. Distinguish specular from diffuse reflection — which surface produces each, and does the reflection law hold on a rough surface?
7. Define the refractive index. Why is n = 1 for air and n > 1 for any other medium?
8. When light passes from one medium into another, which quantities change and which remains exactly the same?
9. Define the critical angle, and state the direction condition required for total internal reflection.
10. What is the relative refractive index between two media?

## LEVEL 2 — APPLY

11. A wave in air has f = 5.0 × 10¹⁴ Hz and λ = 600 nm. Compute v and compare with c.
12. Light in air strikes glass (n = 1.5) at 30° to the normal. Find the refraction angle.
13. Light travels from glass (n = 1.5) into air with an incidence angle of 20°. Find the refraction angle and state whether the ray bends toward or away from the normal.
14. The speed of light in a certain medium is 2.0 × 10⁸ m/s. Find its refractive index.
15. Light of wavelength 600 nm in air enters a medium with n = 1.5. Find the wavelength inside.
16. Find the critical angle for a glass (n = 1.5)–air interface.
17. A pool is 4.0 m deep; a coin lies on the bottom, viewed from directly above. How deep does it appear (n_water = 1.33)?
18. Two mirrors make a 90° angle; a ray strikes M₁ at 30° to the normal. Find the angle the ray makes with M₂'s normal after both reflections. Verify with the deviation method.
19. A beam in air strikes a slab at 50° to the normal and refracts at 31°. Find the slab's index.
20. Light in water (n = 1.33) strikes the water–air surface at 40° to the normal. Does total internal reflection occur? Justify.

## LEVEL 3 — TRANSFER

21. Light passes from medium A (n = 1.2) into medium B (n = 1.8). Compare the speeds and wavelengths in the two media, state what happens to the frequency, and state which way the ray bends.
22. Light travels from air into an oil layer (n = 1.45) floating on water (n = 1.33). At which interface(s) could total internal reflection ever occur, and what is the critical angle there?
23. An optical fiber has a core of n = 1.6 and a cladding of n = 1.4. Find the critical angle at the core–cladding interface.
24. A periscope designer tests a 45°–90°–45° prism made of a new material with n = 1.3 (instead of glass's 1.5). Light hits the hypotenuse at 45°. Will the prism still turn the beam by total internal reflection?
25. A coin lies at the bottom of a 4.0 cm layer of oil (n = 1.45), viewed from directly above. Find the apparent depth of the coin.
26. Light of wavelength 500 nm in air enters glass (n = 1.5) at 30° to the normal. Find (a) the wavelength inside the glass, (b) the refraction angle, and (c) the frequency.

**INSTRUCTOR ANSWER KEY (not for student display)**

1. Optics: the physics branch studying light, its nature, properties, and optical instruments. Geometric optics: the branch studying reflection and refraction; it uses the light ray. [EASY]
2. A straight line drawn along the direction of propagation of the wave, showing the wave's path through space. [EASY]
3. A stream of particles (photons) in some cases; transverse electromagnetic waves (part of the EM spectrum) in others. [EASY]
4. λ: distance between two successive crests or troughs; f: number of complete cycles in one second. [EASY]
5. Rule I: θ_i = θ_r; Rule II: incident ray, reflected ray, and normal coplanar; all angles from the normal. [EASY]
6. Specular = smooth surface; diffuse = rough surface; the law still holds, but the local surface normals vary, scattering the reflected light. [EASY]
7. n = c/v, the ratio of light's speed in air/vacuum to its speed in the medium; since v ≤ c in any medium, n ≥ 1, with equality only for air. [EASY]
8. Speed and wavelength change; frequency does not. [EASY]
9. θ_C: the incidence angle in the higher-index medium giving a 90° refraction angle in the lower-index medium; TIR requires light to travel from higher index toward lower index. [EASY]
10. The ratio of the two media's refractive indices: n₁₂ = n₂/n₁. [EASY]
11. v = λf = (600 × 10⁻⁹)(5.0 × 10¹⁴) = 3.0 × 10⁸ m/s = c ✓ (light in air). [EASY]
12. sin θ₂ = (1)(sin 30°)/1.5 = 0.333 → θ₂ ≈ 19.5°. [EASY]
13. sin θ₂ = 1.5 × sin 20° = 0.513 → θ₂ ≈ 30.9°; bends away from the normal (low index ahead). [MEDIUM — reversed Snell]
14. n = (3 × 10⁸)/(2.0 × 10⁸) = 1.5. [EASY]
15. λ = 600/1.5 = 400 nm. [EASY]
16. θ_C = sin⁻¹(1/1.5) = sin⁻¹(0.667) ≈ 41.8°. [EASY]
17. d′ = 4.0 × (1/1.33) ≈ 3.0 m. [EASY]
18. Ray leaves M₁ at 30° to the normal → 60° to M₁'s surface. Triangle: 90° + 60° + angle-at-M₂ = 180° → ray meets M₂ at 30° to its surface → 60° to the normal. Deviation check: total deviation = 360 − 2(90) = 180°; first = 180 − 2(30) = 120°; second = 60° → θ₂ = (180 − 60)/2 = 60° ✓. **Answer: 60°.** [MEDIUM — two-mirror geometry]
19. n₂ = sin 50°/sin 31° = 0.766/0.515 ≈ 1.49. [EASY]
20. θ_C = sin⁻¹(1/1.33) ≈ 48.8°; 40° < 48.8° → no TIR; the light refracts (partially) into the air. [MEDIUM — full TIR decision]
21. v_B = c/1.8 < v_A = c/1.2 (v_B = ⅔ v_A); λ_B = ⅔ λ_A (same scaling); f unchanged; bends toward the normal (into the denser, slower medium). [MEDIUM — boundary reasoning]
22. Air→oil: low→high — TIR impossible. Oil→water: high→low — TIR possible: θ_C = sin⁻¹(1.33/1.45) = sin⁻¹(0.917) ≈ 66.6°, so only for oil-side incidence beyond 66.6°. [HARD — layered media + direction check]
23. θ_C = sin⁻¹(1.4/1.6) = sin⁻¹(0.875) ≈ 61.0°. [MEDIUM]
24. θ_C = sin⁻¹(1/1.3) = sin⁻¹(0.769) ≈ 50.3°; 45° < 50.3° → no TIR; the prism fails to turn the beam. [MEDIUM — design check]
25. d′ = 4.0 × (1/1.45) ≈ 2.76 cm. [EASY]
26. (a) λ = 500/1.5 ≈ 333 nm; (b) θ₂ = 19.5°; (c) f = c/λ_air = (3 × 10⁸)/(500 × 10⁻⁹) = 6.0 × 10¹⁴ Hz — unchanged in the glass. [MEDIUM — three-part synthesis]

---

# 13. TRANSFER QUESTIONS

*New-context problems carrying Lecture 10 concepts into unfamiliar settings.*

**T1 — Underwater spotlight:** A diver's spotlight emits a beam from inside the water (n = 1.33) toward the surface, hitting it at 50° to the normal. Compute the critical angle for water–air first, then decide whether the beam escapes or undergoes total internal reflection.
→ *Key:* θ_C = sin⁻¹(1/1.33) ≈ 48.8°; 50° > 48.8° → TIR — the beam stays in the water. [MEDIUM]

**T2 — Budget periscope test:** A manufacturer offers 45°–90°–45° prisms in two materials: glass (n = 1.5) and a cheap plastic (n = 1.2). For each, determine whether light hitting the hypotenuse at 45° undergoes total internal reflection, and conclude which material works for a periscope.
→ *Key:* Glass: θ_C = 41.8° < 45° → works. Plastic: θ_C = sin⁻¹(1/1.2) = 56.4° > 45° → fails (light leaks out). [MEDIUM]

**T3 — Fiber design (inverted critical angle):** A fiber engineer wants the core–cladding critical angle to be exactly 45° using a core of n = 1.5. What cladding index is required?
→ *Key:* n₂ = n₁ sin θ_C = 1.5 × sin 45° = 1.5 × 0.707 ≈ 1.06 — a very low-index cladding; the design equation is Snell at the 90° condition, solved backwards. [HARD — design inversion]

**T4 — Gem identification:** An unknown gemstone has n = 2.0. Light inside it strikes the gem–air surface at 35°. Compute θ_C and decide what happens; compare the behavior with the diamond case (θ_C = 24.4°).
→ *Key:* θ_C = sin⁻¹(1/2.0) = 30°; 35° > 30° → TIR. The gem (θ_C = 30°) traps light over a narrower range of angles than diamond (24.4°), so diamond traps light more readily. [MEDIUM]

**T5 — Mirror maze geometry:** Two plane mirrors meet at 60°. A ray strikes M₁ at 40° to the normal. Find the angle to M₂'s normal after both reflections, using the triangle method, and verify with the deviation method.
→ *Key:* Ray leaves M₁ at 50° to its surface; triangle: 180° − 60° − 50° = 70° to M₂'s surface → 20° to the normal. Deviation check: total = 360 − 2(60) = 240°; first = 180 − 2(40) = 100°; second = 140° → θ₂ = (180 − 140)/2 = 20° ✓. [MEDIUM — geometry transfer to a new angle]

**T6 — Spearfishing reasoning:** A fish lies 6.0 m below the surface of a lake, viewed by a spearfisher directly above. Compute the apparent depth, then decide whether the fisher should aim above or below where the fish *appears* to be.
→ *Key:* d′ = 6.0/1.33 ≈ 4.5 m — the fish appears ~1.5 m shallower than it is, so the fisher must aim *below* the apparent position. (Aiming conclusion follows directly from d′ < d.) [MEDIUM]

---

# 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All Lecture 10 topics present: optics/geometric optics/ray definitions; dual nature + EM spectrum; v = λf with source definitions of λ and f; both reflection rules; specular/diffuse; refraction law (speed form); deviation angle; n = c/v (n_air, n_glass, n_oil examples); relative index; Snell; boundary behavior (f invariant, λm = λair/nm); apparent depth (incl. the "difficult oblique case" note); TIR full progression + direction condition + θ_C; prisms (42°, 90°/180°, binoculars/periscopes/telescopes); fiber optics (core/cladding, zigzag, endoscopy). |
| Mathematical formulas correct | ✅ | All 10 formulas match the source; all 4 source examples reproduce exactly (55° derived with two cross-checks; 1.47; 2.26 m; 24.4°/33.3°; 42°); all practice/transfer computations verified. |
| Technical terminology preserved | ✅ | Ray, geometric optics, photons, EM spectrum, specular/diffuse reflection, normal, refractive index, relative refractive index, angle of deviation, critical angle, total internal reflection, core, cladding, endoscopy/endoscope — all retained. |
| Explanations in original language | ✅ | No source paragraphs reproduced; only formulas and short standard definitions shared. |
| Understandable to a first-year student | ✅ | Checkpoint argument, marching band analogy, and snorkeler view scaffold the hardest ideas; all analogies flagged or standard. |
| Difficult concepts explicitly identified | ✅ | 6 concepts with full analysis and difficulty ratings in §9. |
| Common misconceptions identified | ✅ | 10 in §7; per-concept misconceptions in §9; in-video mistakes in §10–11. |
| Examples actually teach | ✅ | All 4 source examples + the prism computation retained with full reasoning; 1 clearly-flagged pedagogical example added (wavelength/frequency in a medium) to cover a source relation without a numerical application. |
| Practice progresses understand → apply → transfer | ✅ | L1 (10 conceptual) → L2 (10 computational) → L3 (6 synthesis) + 6 transfer tasks, all with verified keys. |
| No unsupported claims added | ✅ | Flagged items: EM-spectrum figure details [SOURCE DOES NOT SPECIFY]; Example 1's printed solution is a figure — 55° derived by standard geometry with two independent cross-checks; the checkpoint argument for frequency invariance is a pedagogical elaboration of the source's bare statement "f does not change"; diamond-sparkle framing, marching band analogy, and spearfishing aiming conclusion flagged as everyday illustrations/reasoning from the source's formulas. |
| No large verbatim reproduction | ✅ | Only formulas and short standard definitions overlap with the source. |
| Suitable for direct web integration | ✅ | Clean Markdown; student-facing self-check separated from instructor keys. |

**Source errata handled transparently (meaning preserved, typos not propagated):**
- No numerical errata in this lecture: all source computations verified (1.47; 2.26 m; 24.4°; 33.3°; 42°).
- Example 1's solution is a figure not captured in the extracted text; the 55° answer is reconstructed with the triangle method and independently confirmed by the deviation method.
- The EM-spectrum and refraction/figures sections carry no quantitative text; conceptual content preserved exactly as stated, with [SOURCE DOES NOT SPECIFY] where the figures contained details.
- The apparent-depth relation is explicitly tied to the directly-overhead case (the source's "simple" Figure b), with the oblique case noted as difficult per the source.


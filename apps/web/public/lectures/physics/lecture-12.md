# ARETE — LECTURE 12 (FULL TRANSFORMATION)

---

# 1. SOURCE ANALYSIS

| Item | Value |
|---|---|
| Course | PHY 211 — Physics (Electricity, Magnetism & Optics) |
| Lecture | **Lecture 12** — Chapter 10 (continuation) |
| Title | Lenses |
| Instructor | Dr. Ashraf Mousa Abdelwahed — AIU, Fall 2024 |

**Main topics:**
1. Thin lenses: types, definitions, converging vs. diverging
2. Focal points of converging and diverging lenses
3. Ray diagrams for thin lenses
4. Image cases for convex (converging) and concave (diverging) lenses
5. The lens equation (source name: "lens maker's equation") and magnification
6. Sign conventions for thin lenses
7. Defects of lenses: chromatic aberration and spherical aberration

**Subtopics:** spherical/cylindrical/spherical-cylindrical lens types; spherical lens definition (two spherical surfaces, or one spherical + one plane); converging lenses (+f, thicker at center) vs. diverging (−f, thicker at edges); the two focal points; three principal rays (parallel → through/appears-from F; through center → straight; through the other F → parallel); convex-lens image cases (p = ∞, p > 2f, p = 2f, 2f > p > f, p = f, p < f); concave lens always virtual/upright/reduced; 1/p + 1/q = 1/f; M = −q/p; sign convention; |M| readings; chromatic aberration (n varies with wavelength; violet refracted more than red; f greater for red than violet; edges act like a prism; blurred image; achromatic combination — convex + concave of different materials in contact); spherical aberration (far-from-axis rays focus differently from near-axis rays; remedy: variable aperture/barrier).

**Learning objectives (from content):** classify lenses; construct ray diagrams; locate and characterize images; solve the lens equation with signs; identify and remedy both aberrations.

**Important definitions:** spherical lens; converging/diverging lens; focal point; real/virtual image (carried from Chapter 10); chromatic aberration; achromatic combination; spherical aberration; variable aperture.

**Examples in source:** 1 (converging lens, f = 10.0 cm, three object positions: 30.0, 10.0, 5.00 cm).

**Procedures:** ray-diagram construction (three rays); equation evaluation (set f sign → solve q → compute M → read signs); aberration diagnosis (color-dependent vs. ray-height-dependent blur).

**Common misconceptions in source material:** real-image side for lenses; magnifier image "real"; aberrations as damage rather than inherent behavior.

**Difficult concepts:** the mirror↔lens sign flip; the p = f transition for lenses; why diverging lenses never form real images; chromatic mechanism.

**Prerequisites:** Lecture 11 (mirror equation, M = −q/p, sign reading, real/virtual); Lecture 10 (refraction, refractive index — lenses work by transmission, not reflection).

**Concept map:**

```
Lenses (Ch. 10, cont.)
├── Types: spherical · cylindrical · spherical-cylindrical [details: SOURCE DOES NOT SPECIFY]
│   └── Spherical lens = transparent refracting medium, 2 spherical surfaces
│       (or 1 spherical + 1 plane)
├── Classification
│   ├── Converging: f > 0 · thick center · two REAL focal points (one per side)
│   └── Diverging: f < 0 · thick edges · focal points virtual (rays appear to originate)
├── Ray diagrams (3 rays)
│   ├── ∥ axis → through F (or appears from F)
│   ├── Through center → STRAIGHT (undeviated)
│   └── Through other focal point → emerges ∥ axis
├── Image zones (converging): ∞→F · >2f R/I/small · =2f R/I/same ·
│   2f–f R/I/large (projector) · =f infinity · <f V/U/large (magnifier)
│   └── Diverging: always V/U/reduced
├── Equation (source: "lens maker's equation")
│   ├── 1/p + 1/q = 1/f ; M = −q/p
│   └── Signs: q+ real BEHIND lens (far side) · q− virtual on object side · f+ converging
└── Aberrations
    ├── Chromatic: n(λ) varies → violet bends more → f_red > f_violet → blur
    │   └── Fix: achromatic doublet (convex + concave, different materials)
    └── Spherical: marginal ≠ paraxial foci → Fix: variable aperture (barrier)
```

**Dependencies:** final lecture of the sequence — builds on L11's equation/sign machinery and L10's refraction physics.

---

# 2. COURSE / MODULE / LESSON METADATA

| Field | Value |
|---|---|
| **COURSE** | PHY 211 — Physics II |
| **MODULE** | Image Formation (Chapter 10) — continuation |
| **LESSON** | Lecture 12 — Lenses |
| **TOPICS** | Lens types; focal points; ray diagrams; image zones; the lens equation & sign conventions; chromatic & spherical aberration |
| **PREREQUISITES** | Lecture 11 (1/p + 1/q = 1/f, M = −q/p, sign reading); Lecture 10 (refraction, refractive index) |
| **COMPETENCIES** | Classify lenses by shape and f-sign; draw the three principal rays; solve the lens equation with correct signs; fully characterize images for every zone; distinguish and remedy chromatic vs. spherical aberration |
| **DIFFICULTY** | Overall: MEDIUM-HARD · Equation computations: MEDIUM · The mirror↔lens geometric sign flip and the zone/magnifier transition: HARD |
| **ESTIMATED STUDY TIME** | ~3 hours (lesson 60 min · worked examples 25 min · practice 45 min · videos 16 min · self-check & transfer 30 min) |

**ARETE flow placement:**
- **LEARN:** lens types, focal points, the three rays, aberration definitions.
- **PRACTICE:** lens-equation computations with sign reading.
- **PROVE:** full image characterization (side + type + orientation + size); aberration diagnosis.
- **REMEDIATE/RETRY targets:** real-image side for lenses; f-sign; "q < 0 = no image"; chromatic/spherical mix-up.
- **TRANSFER:** optical design (projector, magnifier, peephole); conjugate positions.
- **MASTER:** predict-then-verify across all six zones; connecting mirror and lens frameworks into one system.

---

# 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. List the three lens types and define a spherical lens.
2. Distinguish converging from diverging lenses by shape and by the sign of f.
3. Describe the focal points of converging lenses (two, one on each side, real) and of diverging lenses (virtual).
4. Draw the three principal rays for a thin lens and use them to locate images.
5. State the image character for every object zone of a converging lens — including the p = f transition and the magnifying-glass regime (p < f) — and for any position with a diverging lens.
6. Solve 1/p + 1/q = 1/f with the lens sign conventions, compute M = −q/p, and state on which side of the lens each image forms.
7. Explain chromatic aberration: its cause (wavelength-dependent index), its signature (f_red > f_violet), and its remedy (achromatic combination).
8. Explain spherical aberration: its cause (ray-height-dependent foci) and its remedy (variable aperture).

---

# 4. WEB-READY LESSON

# Lecture 12 — Lenses

## Prerequisites
The student should already understand:
- The mirror equation, M = −q/p, and sign reading (Lecture 11).
- Real vs. virtual images, and the Chapter-10 convention: real images form **behind** lenses; virtual images form **in front of** lenses.
- Refraction and refractive index (Lecture 10) — lenses work by *transmission*.

---

### 1. Types of Lenses

**Core Idea**
A **spherical lens** is a part of a transparent refracting medium bounded by two spherical surfaces, or by one spherical and one plane surface. Lenses come in three types: spherical, cylindrical, and spherical-cylindrical.

**Explanation**
The type list is the source's classification; details of the cylindrical and spherical-cylindrical types are [SOURCE DOES NOT SPECIFY] — the lecture's quantitative work concerns **spherical** lenses only.

The working classification is by behavior:
- **Converging lenses:** have **positive** focal lengths and are **thicker at the center than at the edges**.
- **Diverging lenses:** have **negative** focal lengths and are **thicker at the edges than at the center**.

**Example**
A biconvex lens (bulging outward on both sides) is thick in the middle → converging, f > 0. A biconcave lens (hollowed on both sides) is thick at the rim → diverging, f < 0.

**Key Point**
Shape predicts behavior: **thick middle = converging = f > 0; thick edge = diverging = f < 0.**

### 2. Focal Points of Lenses

**Core Idea**
A converging lens has **two real focal points**, one on each side, symmetric about the lens; a diverging lens's focal points are **virtual** — parallel rays only *appear* to originate from them.

**Explanation**
Parallel rays entering a converging lens refract and actually pass through a point F on the far side; by symmetry, rays entering from the other side converge to a focal point at the same distance on the opposite side. For a diverging lens, parallel rays refract *apart*; tracing them backward, they appear to diverge from a focal point on the **incoming** side — no light actually passes through it.

**Example**
Sunlight (parallel rays) through a converging lens of f = 10 cm burns a spot 10 cm *behind* the lens. Through a diverging lens, the rays spread — the apparent origin is 10 cm in front, and nothing burns anywhere.

**Key Point**
Converging: real F on both sides. Diverging: virtual F on the incoming side. Either way, f's sign is fixed by the lens type before any computation.

### 3. Ray Diagrams for Thin Lenses

**Core Idea**
Three rays with known fates locate any thin-lens image:

1. **Ray 1:** parallel to the principal axis → refracts **through** one of the focal points (converging) or **appears to come from** one (diverging).
2. **Ray 2:** through the **center of the lens** → continues in a **straight line** — undeviated.
3. **Ray 3:** through the **other focal point** → emerges **parallel to the principal axis**.

**Explanation**
Ray 2 is the lens's gift: the center of a thin lens acts like a thin window — the ray passes straight through. Where the refracted rays intersect, the image sits; when they diverge, their backward extensions meet at the virtual image on the object's side.

**Example**
An object beyond 2F of a converging lens: Ray 1 leaves the tip parallel and crosses F on the far side; Ray 2 goes straight through the center — they intersect below the axis between F and 2F: a real, inverted, reduced image *behind* the lens.

**Key Point**
Learn the three fates — and remember the center ray never bends. The intersection side tells you real (far side) vs. virtual (object side).

### 4. Image Zones of a Converging Lens

**Core Idea**
A converging lens (f > 0) produces six distinct behaviors depending on object position — including the projector regime (2f > p > f) and the magnifying-glass regime (p < f).

**Explanation**
*(The source presents these cases through labeled figures: p = ∞, p > 2f, p = 2f, 2f > p > f, p = f, p < f. The table below is reconstructed from the source's own equation — each row is derivable from 1/p + 1/q = 1/f — and matches the source's stated "If p > f: real, inverted" and "If p < f: virtual, upright.")*

| Object position | Image |
|---|---|
| p = ∞ | Real image at F (point-sized) |
| p > 2f | Real, inverted, **reduced** (between f and 2f) — the *camera* regime |
| p = 2f | Real, inverted, **same size** (q = 2f) |
| 2f > p > f | Real, inverted, **enlarged** (beyond 2f) — the *projector* regime |
| p = f | **Image at infinity** (emerging rays parallel) |
| p < f | **Virtual, upright, enlarged** — the *magnifying-glass* regime |

As with the concave mirror, crossing p = f flips everything: outside f, real and inverted; at f, escape to infinity; inside f, virtual, upright, magnified — now on the **object's side** of the lens.

**Example**
f = +10 cm: object at 30 cm (p > 2f = 20) → real, inverted, reduced; object at 5 cm (p < f) → virtual, upright, doubled. (Worked Example 1.)

**Key Point**
Same zone logic as the concave mirror — but real images form on the **far side**, and the p < f image is the magnifier you look *through*.

### 5. Images from a Diverging Lens

**Core Idea**
For **any** object position, a diverging lens (f < 0) produces a **virtual, upright, reduced** image on the object's side.

**Explanation**
Parallel-to-axis rays spread apart after the lens; every object's rays refract divergently; backward extensions always meet on the incoming side, between the lens and F — smaller than the object, upright, uncatchable on a screen. The equation confirms it universally: with f < 0 and p > 0, 1/q = 1/f − 1/p is always negative → q < 0 (virtual) and |M| = |q|/p < 1 (reduced).

**Example**
f = −10 cm, object at p = 15 cm: q = −6 cm, M = +0.4 — virtual, upright, reduced, on the object's side. (Worked Example 2.)

**Key Point**
Diverging lenses have exactly one answer: virtual, upright, reduced — for every object, every time.

### 6. The Lens Equation and Magnification

**Core Idea**
The same mathematical structure as the mirror equation locates lens images:

**1/p + 1/q = 1/f** *(the source labels this the "lens maker's equation"; many texts call it the thin-lens equation — the naming note is preserved, the formula is the source's)*

**M = −q/p** (and M = h′/h)

**Explanation**
The **lens sign conventions** (the source's Chapter-10 definitions plus its lens statements — the lens-specific table rows were not captured in the text extraction):

| Quantity | Positive | Negative |
|---|---|---|
| Object distance p | Real object (in front of the lens) | [virtual object] |
| Image distance q | **Real image — behind the lens** (far side, where transmitted light lands) | **Virtual image — in front of the lens** (object's side) |
| Focal length f | **Converging** lens | **Diverging** lens |
| Image height h′, M | Upright | Inverted |

Reading |M|: = 1 same size; > 1 enlarged; < 1 diminished. The mirror and lens equations are *identical in form* — only the geometric meaning of q's sign flips: mirrors reflect (real images on the *same* side as the object); lenses transmit (real images on the *opposite* side).

**Example**
Converging f = +10 cm, p = 30 cm: q = +15 cm — real, 15 cm **behind** the lens; M = −0.5 — inverted, half-size. (Worked Example 1a.)

**Key Point**
Solve, then translate: q's sign → real (far side) / virtual (object side); M's sign → orientation; |M| → size; f's sign → lens type.

### 7. Chromatic Aberration

**Core Idea**
A lens cannot focus all colors of white light at one point, because the material's index of refraction varies with wavelength — violet refracts more than red.

**Explanation**
The full causal chain from the source:
1. **n varies with wavelength.**
2. Violet rays are refracted **more** than red when white light passes through the lens — the lens's edges act like a **prism**, dispersing the white light.
3. The focal length is **greater for red light than for violet light**; other wavelengths focus at intermediate points.
4. The result: a **blurred image**.

**Remedy — the achromatic combination:** two lenses **in contact, made of different materials** — one **converging (convex)** and one **diverging (concave)** — engineered so their dispersions cancel, bringing the colors back to a common focus.

**Example**
White light through a simple converging lens: the violet image forms closest to the lens, the red image farther back; the intermediate colors strung between them are the blur. A marked achromatic doublet collapses them onto one another. *(Illustrative framing; the source states the mechanism qualitatively.)*

**Key Point**
Chromatic = **color**-dependent focus (n depends on λ); fix = achromatic doublet (different materials, convex + concave).

### 8. Spherical Aberration

**Core Idea**
A lens cannot focus all rays at one point because rays passing **far from the principal axis** come to different focal points than rays passing **near the axis**.

**Explanation**
Even for a single wavelength, the spherical shape misbehaves: marginal rays (through the lens's outer regions) focus at different points than paraxial rays (close to the axis). The remedy from the source: a **variable aperture** — a barrier that blocks the offending far-from-axis rays, letting only the well-behaved near-axis rays through.

**Example**
Stop a lens down to a small central aperture: the image sharpens (all transmitted rays are near-axis) at the cost of less light passing — the trade every camera iris makes. *(The light trade-off is the direct consequence of inserting a barrier.)*

**Key Point**
Spherical = **ray-height**-dependent focus; fix = aperture stop. One word separates the aberrations: chromatic ↔ color; spherical ↔ ray height.

---

## Key Takeaways
1. Spherical lens = transparent refracting medium bounded by two spherical surfaces (or one spherical + one plane); types: spherical, cylindrical, spherical-cylindrical.
2. Converging: **f > 0, thick center**, two real focal points (one per side). Diverging: **f < 0, thick edge**, virtual focal points.
3. Three rays: parallel → through/from F; **through the center → straight**; through the other F → parallel.
4. Converging zones: p = ∞ → F; p > 2f real/inverted/reduced (camera); p = 2f real/inverted/same; 2f > p > f real/inverted/enlarged (projector); p = f → infinity; **p < f virtual/upright/enlarged (magnifier)**.
5. Diverging lens: always virtual, upright, reduced — for every p.
6. 1/p + 1/q = 1/f and M = −q/p — identical to mirrors, with one geometric flip.
7. Lens signs: q > 0 = real = **behind** the lens; q < 0 = virtual = object's side; f > 0 converging.
8. Chromatic aberration: n varies with λ → violet bends more → f_red > f_violet → blur; remedy: **achromatic doublet** (convex + concave, different materials).
9. Spherical aberration: marginal vs. paraxial foci differ; remedy: **variable aperture** (barrier).

## Self-Check (attempt before looking at answers)
1. List the three lens types and define a spherical lens.
2. Which lens is thicker at the center — and what sign does its focal length carry?
3. How many focal points does a converging lens have, and where are they? What about a diverging lens?
4. State the fates of the three principal rays; which one passes through the lens unchanged?
5. A converging lens with the object beyond 2f: state the image's type, orientation, and size — and which side of the lens it forms on.
6. The object sits exactly at 2f: where is the image and what is M?
7. The object is inside f: what do you see when you look through the lens, and where is the image?
8. A diverging lens, any object position: what image always results?
9. For a lens, where do real and virtual images form — and how does this differ from mirrors?
10. Chromatic vs. spherical aberration: state the cause and the remedy of each in one line apiece.

---

# 5. FORMULAS

| # | Formula | Variables | When it is used | Interpretation & assumptions |
|---|---|---|---|---|
| 1 | 1/p + 1/q = 1/f | p: object distance; q: image distance; f: focal length | Thin-lens equation (source name: "lens maker's equation") | Thin-lens approximation; sign conventions below |
| 2 | M = −q/p | — | Magnification from positions | M > 0 upright; M < 0 inverted |
| 3 | M = h′/h | h, h′: object/image heights | Magnification from sizes | h′ + upright / − inverted |
| 4 | q > 0 ⇔ real, behind lens | — | Sign reading (lenses) | Transmitted light actually lands there |
| 5 | q < 0 ⇔ virtual, object side | — | Sign reading (lenses) | Backward extensions meet where no light is |
| 6 | f > 0 ⇔ converging; f < 0 ⇔ diverging | — | Input sign | Thick center = +; thick edge = − |
| 7 | \|M\| = 1 / > 1 / < 1 | — | Size reading | Same / enlarged / diminished |
| 8 | f_red > f_violet | — | Chromatic aberration signature | n(λ): violet refracted more; other colors intermediate |

---

# 6. WORKED EXAMPLES

**WE 1 — Converging lens, three positions (Source Example 2)**
A converging lens of f = 10.0 cm forms images of an object at various distances. Locate and describe the image for (a) p = 30.0 cm, (b) p = 10.0 cm, (c) p = 5.00 cm.
(a) p = 30.0 cm:
1. 1/q = 1/f − 1/p = 1/10 − 1/30 = 2/30 = 1/15.
2. **q = +15 cm** (+ve → real, 15 cm **behind** the lens, on the far side).
3. M = −q/p = −15/30 = **−0.5** → inverted, reduced.
4. **Real, inverted, diminished** — the p > 2f (camera) zone (2f = 20 cm); the image sits between f (10) and 2f (20) ✓.
(b) p = 10.0 cm (= f):
1. 1/q = 1/10 − 1/10 = 0 → **q = ∞: the image is at infinity** (emerging rays parallel).
(c) p = 5.00 cm:
1. 1/q = 1/10 − 1/5 = −1/10 → **q = −10 cm** (−ve → virtual, 10 cm **in front** of the lens, on the object's side).
2. M = −(−10)/5 = **+2** → upright, doubled.
3. **Virtual, upright, enlarged** — the magnifying-glass zone (p < f).

**WE 2 — Diverging lens (pedagogical example — the source's example covers only the converging case)**
A diverging lens has f = −10 cm; an object stands at p = 15 cm. Locate and describe the image.
1. 1/q = 1/f − 1/p = −1/10 − 1/15 = (−3 − 2)/30 = −1/6.
2. **q = −6 cm** → virtual, 6 cm in front of the lens (object's side).
3. M = −(−6)/15 = **+0.4** → upright, reduced.
4. Exactly the diverging table's universal answer: virtual, upright, reduced ✓.

**WE 3 — The magnifying glass (pedagogical example)**
A converging lens with f = +10 cm is used as a magnifier, the object at p = 8.0 cm. Find the image.
1. 1/q = 1/10 − 1/8 = (4 − 5)/40 = −1/40.
2. **q = −40 cm** → virtual, 40 cm in front of the lens.
3. M = −(−40)/8 = **+5** → upright, five times larger.
4. The closer the object sits to f (from inside), the farther and larger the virtual image — the lever every magnifier pulls.

**WE 4 — Object at 2f: the copier case (pedagogical example)**
Converging lens, f = +10 cm, object at p = 20 cm (= 2f). Find the image.
1. 1/q = 1/10 − 1/20 = 1/20 → **q = +20 cm** — the image forms at 2f on the far side, symmetric with the object.
2. M = −20/20 = **−1** → real, inverted, **same size**.
3. The 1:1 reproduction used by copy machines and 1:1 projectors — the lens version of the mirror's p = 2f case.

**WE 5 — Projection design (pedagogical example)**
A real image must appear on a screen 45 cm behind a lens, of an object 15 cm in front of it. Find f and M.
1. 1/f = 1/p + 1/q = 1/15 + 1/45 = (3 + 1)/45 = 4/45.
2. **f = +11.25 cm** (converging).
3. M = −45/15 = **−3** → real, inverted, tripled on the screen.
4. Zone check: 2f = 22.5 > 15 > 11.25 ✓ — the projector regime (2f > p > f, real, inverted, enlarged), consistent.

**WE 6 — Aberration diagnosis (pedagogical example, qualitative)**
A lens forms a sharp image of red light but a blurred image of white light. A second lens blurs even single-color light, worse at large aperture. Diagnose each.
1. Sharp in monochrome (red), blurred in white → the defect is **color-dependent** → **chromatic aberration**: the index varies with wavelength, violet refracts more, f_red > f_violet → colors focus at different points. Remedy: **achromatic combination** (convex + concave, different materials).
2. Blurred even for one color, worse with large aperture → the defect is **ray-height-dependent** → **spherical aberration**: marginal rays focus differently from near-axis rays. Remedy: **variable aperture** (barrier).

---

# 7. COMMON MISTAKES

| # | What students usually do | Why it's wrong | How to avoid it |
|---|---|---|---|
| 1 | Place the real image on the object's side of a lens (mirror habit) | Mirrors reflect (light stays on your side); lenses transmit — a real lens image forms **behind** the lens, where the transmitted light lands | Ask "did the light pass through, or bounce back?" before assigning the side |
| 2 | Use f > 0 for a diverging lens | f's sign encodes the lens type: converging (thick middle) +, diverging (thick edge) − | Attach the sign to the shape before computing |
| 3 | Put the virtual image behind the lens | Virtual lens images form **in front**, on the object's side — where the diverging rays appear to come from | Virtual = where the eye traces backward = the incoming side |
| 4 | Drop the minus in M = −q/p | The sign carries the upright/inverted information | Compute M fully: sign → orientation, magnitude → size |
| 5 | Read q < 0 as "no image" | A negative q is a perfectly good **virtual** image — the magnifier's image is virtual and is the whole point | Translate instantly: q− → virtual, object's side |
| 6 | Expect a diverging lens to form real images | With f < 0 and p > 0, 1/q is always negative — the image is always virtual | One answer for diverging lenses: V/U/R, every time |
| 7 | Draw Ray 2 (through the center) as bending | The center of a thin lens passes the ray **straight through** — undeviated | The center-ray is your cheapest, most reliable ray |
| 8 | Declare "no image" when p < f for a converging lens | Inside f is the magnifying-glass regime: virtual, upright, enlarged — the most useful image the lens makes | Zone table recall: outside f real/inverted; inside f virtual/upright |
| 9 | Mix up chromatic and spherical aberration | Chromatic depends on **color** (n varies with λ); spherical depends on **ray height** (marginal vs. paraxial) | Keyword link: chromatic ↔ color ↔ achromatic doublet; spherical ↔ ray height ↔ aperture |
| 10 | Treat aberrations as lens "damage" | They are inherent behaviors of simple spherical lenses — every simple lens has both | Frame them as design constraints with known fixes, not defects to "repair" |

---

# 8. LECTURE SUMMARY

# Lecture Summary — Lenses

## What You Need to Know
- Lens types and the converging/diverging classification (shape ↔ f-sign ↔ focal-point character).
- The three principal rays, especially the straight-through center ray.
- All six image zones of a converging lens, including the projector and magnifier regimes.
- The universal answer of diverging lenses.
- The lens equation with its sign conventions — and the one geometric flip relative to mirrors.
- Both aberrations: cause, signature, and remedy.

## Key Definitions
- **Spherical lens** → transparent refracting medium bounded by two spherical surfaces (or one spherical + one plane).
- **Converging lens** → +f, thicker at the center; two real focal points, one per side.
- **Diverging lens** → −f, thicker at the edges; virtual focal points on the incoming side.
- **Chromatic aberration** → the inability of a lens to converge/diverge all colors of white light in one focus; caused by wavelength-dependent n.
- **Achromatic combination** → two lenses in contact from different materials (one convex, one concave) correcting chromatic aberration.
- **Spherical aberration** → the inability of a lens to focus all rays at one point; marginal-ray foci differ from near-axis foci.
- **Variable aperture** → a barrier blocking far-from-axis rays, correcting spherical aberration.

## Key Formulas
- 1/p + 1/q = 1/f → thin-lens equation (source: "lens maker's equation").
- M = −q/p = h′/h → magnification.
- f_red > f_violet → the chromatic signature.
- Sign table: q+ real behind · q− virtual in front · f+ converging · M+ upright.

## Important Ideas
- The lens equation is the mirror equation wearing different geometry: mirrors bounce light (real images on the object's side); lenses transmit it (real images on the far side).
- One converging lens is camera, copier, projector, and magnifier — the object distance selects the job.
- Diverging lenses trade image size for a wide, always-upright virtual view.
- Every simple spherical lens misfocuses by color (chromatic) and by ray height (spherical) — both have standard optical fixes.

## Common Mistakes
Real image placed on the wrong side; f-sign errors; virtual image placed behind; dropped M minus; "q < 0 = no image"; expecting real images from diverging lenses; bent center ray; "no image" inside f; aberration mix-up; aberrations as damage.

## Exam Focus
1. Solving 1/p + 1/q = 1/f with signs and stating the image's **side** — the mirror/lens flip is the graded point.
2. Zone-table predictions for converging lenses (all six cases) and the universal diverging answer.
3. Design inversions: given M and q (projector-style), find f and p.
4. The magnifier regime: virtual, upright, enlarged, object's side.
5. Aberration diagnosis from symptoms (color-dependent vs. ray-height-dependent blur) with remedies.

## 60-Second Review
Spherical lens: two curved surfaces (or one + plane). Converging: thick middle, f > 0, real F both sides. Diverging: thick edge, f < 0, virtual F. Rays: ∥→F; center→straight; F→∥. Converging zones: ∞→F; >2f R/I/small; =2f R/I/same; 2f–f R/I/big; =f ∞; <f V/U/big (magnifier). Diverging: always V/U/small. Equation: 1/p + 1/q = 1/f; M = −q/p. Lens signs: q+ real BEHIND; q− virtual in front (object side); f+ converging. Chromatic: n(λ) varies, violet bends more, f_red > f_violet → fix: achromatic doublet. Spherical: marginal ≠ paraxial → fix: aperture stop.

---

# 9. DIFFICULT CONCEPTS

### Difficult Concept: The Mirror↔Lens Sign Flip
**Why students struggle:** The equation and M-formula are *identical* to the mirror's, so mirror habits auto-apply — and the geometric meaning of q's sign is opposite.
**Simple explanation:** Mirrors reflect — the light never crosses, so a real image forms on the object's side (q > 0, in front). Lenses transmit — the light passes through, so a real image forms on the far side (q > 0, behind). Virtual is wherever the light only *appears* to originate: behind a mirror, in front of a lens.
**Intuitive analogy:** A mirror is a wall that throws the ball back — the catch happens on your side. A lens is a window you throw the ball *through* — the catch happens in the neighbor's yard. Same throw, same physics, opposite yard.
**Step-by-step:** (1) Identify the element: mirror or lens. (2) Solve 1/p + 1/q = 1/f identically. (3) Read q: + → real — for a mirror, in front; for a lens, behind (far side). (4) − → virtual — mirror: behind; lens: in front (object's side). (5) M as always.
**Mini example:** f = +10, p = 30: q = +15 for BOTH a concave mirror and a converging lens — but the mirror's image is 15 cm in front (your side), the lens's is 15 cm behind (the far side).
**Misconception to avoid:** "Positive q means the same location in both chapters."
**Difficulty: HARD** → video provided

### Difficult Concept: The Zones of a Converging Lens and the Magnifier Regime
**Why students struggle:** Six cases to track; the p = f discontinuity; and the counterintuitive fact that the *same* lens flips from projector to magnifier.
**Simple explanation:** Outside f, transmitted rays converge behind the lens — real and inverted, growing as the object approaches. At f, they emerge parallel — image at infinity. Inside f, they diverge — extensions meet on the object's side: virtual, upright, enlarged: the magnifier.
**Intuitive analogy:** A phase change, exactly like the concave mirror's: smooth growth, then disappearance at the focal point, then reappearance in a flipped form. The projector and the magnifying glass are the same glass — object position is the only switch.
**Step-by-step:** (1) Mark F and 2F on both sides. (2) Compare p to 2f and f. (3) Read the zone: p > 2f camera; p = 2f copier; 2f > p > f projector; p = f nothing (infinity); p < f magnifier. (4) Verify with the equation.
**Mini example:** f = +10: p = 30 → real, inverted, half-size on the far side; p = 8 → virtual, upright, ×5 on your side.
**Misconception to avoid:** "No image when p < f" — there is one, and it's the most useful image in the table.
**Difficulty: HARD** → video provided

### Difficult Concept: Why a Diverging Lens Never Forms a Real Image
**Why students struggle:** Students accept the table as a fact to memorize without seeing why it's *forced*.
**Simple explanation:** With f < 0 and p > 0, the equation gives 1/q = negative − positive = always negative → q < 0 always: virtual, on the object's side, with |M| = |q|/p < 1 — reduced. The physics: a diverging lens spreads rays apart; they can never converge to a real point.
**Intuitive analogy:** A crowd leaving a stadium through a gate that only pushes people *apart*: no matter how they arrive, they exit spread out — they can never bunch up at a meeting point on the far side.
**Step-by-step:** (1) f < 0, p > 0. (2) 1/q = 1/f − 1/p = (−) − (+) < 0. (3) q < 0 → virtual, in front. (4) |q| < p (since 1/|q| = 1/|f| + 1/p > 1/p) → |M| < 1 → reduced. (5) Conclusion holds for every p.
**Mini example:** Any diverging-lens problem: check the answer is V/U/R — if it isn't, an error was made.
**Misconception to avoid:** "A strong enough diverging lens could still project an image" — it cannot, ever.
**Difficulty: MEDIUM**

### Difficult Concept: The Two Focal Points of a Converging Lens
**Why students struggle:** Mirrors have one focal point; the lens's second focal point (on the object's side) appears only in Ray 3 and feels redundant.
**Simple explanation:** Light can pass through a lens from either direction — and each direction gets its own real focal point, symmetric about the lens. Ray 3 exploits the incoming-side focal point: a ray through it emerges parallel.
**Intuitive analogy:** A door that works from both sides: each side has its own "meeting spot" at the same distance — symmetry, not duplication.
**Step-by-step:** (1) Place F on the far side (exit focal point). (2) Mirror it at the same distance on the incoming side. (3) Rays parallel on the way in → through the far F. (4) Rays through the near F → parallel on the way out. (5) Center rays pass straight.
**Mini example:** Ray-diagram completeness: all three rays should intersect (or their extensions meet) at the same image point — a built-in error check.
**Misconception to avoid:** "Ray 3 uses the same focal point as Ray 1" — it uses the *other* one.
**Difficulty: MEDIUM**

### Difficult Concept: Chromatic Aberration
**Why students struggle:** The causal chain has four links (n varies with λ → violet bends more → f differs by color → blur), and students break it in the middle.
**Simple explanation:** The lens's index of refraction depends (slightly) on the light's color — violet is bent more than red, so each color gets its own focal point: red's is farthest, violet's is nearest, the others strung between — that spread *is* the blur.
**Intuitive analogy:** A prism splits white light because each color bends a different amount; a lens's edges are curved prism surfaces — the same dispersion, too small to see as a rainbow but big enough to spread the focus.
**Step-by-step:** (1) White light enters. (2) n_violet > n_red → violet refracts more. (3) Stronger bending → shorter focal length: f_red > f_violet. (4) Each wavelength focuses at its own point → blurred image. (5) Fix: achromatic doublet — a convex and a concave lens of *different materials* in contact, whose dispersions cancel.
**Mini example:** Sharp red image + blurred white image = chromatic, by definition (the color dependence is the diagnostic).
**Misconception to avoid:** "Better glass removes chromatic aberration" — the fix needs *two different materials*, not better polish.
**Difficulty: MEDIUM**

### Difficult Concept: Spherical Aberration
**Why students struggle:** It sounds like a defect ("spherical" suggests the shape is wrong) and students conflate it with chromatic.
**Simple explanation:** Even one pure color through one perfect spherical lens focuses badly: rays through the lens's outer zones meet at different points than rays near the axis. Block the outer rays with an aperture, and the remaining near-axis rays share (almost) one focus.
**Intuitive analogy:** A radio antenna dish built as a simple sphere instead of the ideal curve: signals hitting the rim bounce to slightly wrong spots — covering the rim fixes the reception at the cost of signal strength.
**Step-by-step:** (1) Send monochromatic light through the full aperture. (2) Marginal rays (far from the axis) focus at point A; paraxial rays (near the axis) at point B ≠ A. (3) The spread of foci blurs the image. (4) Insert a barrier (variable aperture) to pass only near-axis rays. (5) Image sharpens; less light gets through.
**Mini example:** The diagnostic distinction: blur that persists even in pure monochromatic light is spherical, not chromatic.
**Misconception to avoid:** "Spherical aberration depends on the light's color" — it depends on the ray's *height off the axis*.
**Difficulty: EASY**

---

# 10. VIDEO LESSON PLANS

---

**VIDEO 1**

**VIDEO TITLE:** "The Great Flip: Reading Lens Signs After Mirrors"
**TARGET CONCEPT:** The geometric sign flip between mirrors and lenses in 1/p + 1/q = 1/f
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Determine on which side of a lens each image forms, and apply the full sign convention after learning the mirror version.
**HOOK:** Same equation. Same magnification formula. One line of algebra. Yet if you carry your mirror habits into lens problems, you'll draw the image on the wrong side of the room every single time.
**EXPLANATION:** (1) The toolkit is identical: 1/p + 1/q = 1/f; M = −q/p; f > 0 converging, f < 0 diverging. (2) The flip: mirrors reflect — light stays on your side — real image (q+) in front. Lenses transmit — light passes through — real image (q+) behind, on the far side. (3) Virtual images: behind a mirror, in front of a lens (object's side). (4) Side-by-side ray panels proving both. (5) Worked example (source Example 2). (6) Predict-then-verify with a diverging lens.
**VISUALS:** Two parallel animated panels — MIRROR: object left, reflected rays converging left of the mirror (q+, real, your side); LENS: object left, transmitted rays crossing inside the lens and converging right of it (q+, real, far side); then the virtual cases with dashed backward extensions meeting behind the mirror vs. in front of the lens; a screen icon moving to where light actually lands in each case; the source's three-part example solved live with the side of each image highlighted.
**EXAMPLE:** Converging f = +10 cm: p = 30 → q = +15 (real, BEHIND, M = −0.5); p = 5 → q = −10 (virtual, IN FRONT, M = +2).
**COMMON MISTAKE:** Placing the real lens image on the object's side; f-sign errors; "q < 0 = no image."
**CHECK FOR UNDERSTANDING:** "A diverging lens, f = −10 cm, object at 15 cm — predict the image's type, size, and *side* before computing."
**FINAL TAKEAWAY:** Mirrors bounce, lenses transmit. q+ = real = where the light actually goes: your side for mirrors, the far side for lenses. Everything else is unchanged.

---

**VIDEO 2**

**VIDEO TITLE:** "From Projector to Magnifying Glass: The Zones of a Converging Lens"
**TARGET CONCEPT:** The six image zones of a converging lens; the p = f transition and the magnifier regime
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** State the image character for every object zone of a converging lens and explain the flip at the focal point.
**HOOK:** The projector on your lecture hall's ceiling and the magnifying glass in your drawer are the *same piece of glass*. Same shape, same focal length. The only difference is where you put the object. Today we walk all six stops — from infinity to your eyeball.
**EXPLANATION:** (1) Setup: converging lens, two focal points (one per side), 2F landmarks on both sides; distant object → image at F. (2) p > 2f: real, inverted, reduced, between F and 2F — the camera. (3) p = 2f: real, inverted, same size, at 2F — the copier. (4) 2f > p > f: real, inverted, enlarged, beyond 2F — the projector. (5) p = f: parallel rays out, image at infinity. (6) p < f: rays diverge; extensions meet on the object's side — virtual, upright, enlarged: the magnifier. (7) The flip at f mirrors the concave-mirror story. (8) Worked example from the lecture.
**VISUALS:** An animated object sliding along the axis from far left toward the lens; the image tracking through all six zones — shrinking, crossing, growing beyond 2F, escaping to infinity at F (freeze-frame "rays parallel"), then flipping to virtual and huge on the object's side; zone flags at F and 2F; a six-row table filling in as the animation passes each stop; small icons (camera, copier, projector, magnifier) stamping each zone.
**EXAMPLE:** f = +10 cm: p = 30 → q = +15, M = −0.5 (camera zone); p = 10 → q = ∞; p = 5 → q = −10, M = +2 (magnifier zone).
**COMMON MISTAKE:** Expecting the magnifier's image on the far side (it's virtual, on the object's side); "no image" when p < f; forgetting diverging lenses never join this game.
**CHECK FOR UNDERSTANDING:** "Object exactly at 2f — predict position, size, orientation, and side. Then: object just inside f — what do you see through the lens?"
**FINAL TAKEAWAY:** Six stops, one switch: the object's position. Outside f — real and inverted (camera → copier → projector); at f — infinity; inside f — virtual, upright, huge. One lens, every job.

---

# 11. VIDEO SCRIPTS

---

## SCRIPT 1 — "The Great Flip: Reading Lens Signs After Mirrors"

**[0:00–0:30] Hook**
Same equation. Same magnification formula. One line of algebra — identical, letter for letter. And yet, if you carry your mirror habits into a lens problem, you will draw the image on the wrong side of the room. Every single time. Because between mirrors and lenses there is exactly one difference — a geometric flip — and today you're going to see it, prove it, and never get it wrong again.

**[0:30–2:00] Concept introduction**
The toolkit first — notice how familiar it is. One over p, plus one over q, equals one over f. Magnification: M equals minus q over p. Focal length: positive for a converging lens — thick in the middle; negative for a diverging lens — thick at the edges. Object distance p: positive for a real object in front of the lens. All identical to the mirror chapter.

Now the flip. Ask one question about any optical element: does the light *bounce*, or does it *pass through*? A mirror bounces. The light comes in from your side and goes back to your side — it never crosses. So when the reflected rays converge, they converge on *your* side, in front of the mirror. That's a real image: q positive, in front.

A lens transmits. The light enters from your side, passes *through* the glass, and exits on the far side. When the refracted rays converge, they converge *behind* the lens — in the neighbor's yard. That's a real image for a lens: q positive — same sign, same physics — but on the opposite side of the element.

And virtual? Wherever the light only *appears* to originate. For a mirror: behind it, where no light goes. For a lens: in front, on the object's side — where the diverging rays seem to come from as you look through the glass.

**[2:00–4:00] Visual explanation**
Two panels, side by side. Left panel, the mirror: object on the left, rays hit the mirror, reflect, and converge at a point on the left — your side. Screen there? Image. q positive. Right panel, the lens: same object on the left, same converging story — but the rays cross *inside* the lens and meet on the right. Screen there — behind the lens — image. q positive again, opposite side.

Now the virtual cases. Mirror: reflected rays spread apart; extend them backward, they meet behind the mirror. Lens: refracted rays spread apart after the glass; extend them backward, they meet in *front* — on the object's side. Look through a magnifying glass: the big upright image you see is floating on your side of the lens. That's q negative.

The screen test settles every dispute: real means light actually *lands* there. Mirror — it lands in front. Lens — it lands behind. The sign didn't change; the geometry did. Mirrors bounce; lenses transmit. That's the whole flip.

**[4:00–6:00] Worked example**
The lecture's own numbers. A converging lens, f = plus ten centimeters. Case one: object at thirty. One over q equals one over ten minus one over thirty — one fifteenth — q = plus fifteen. Positive: real. And where? *Behind* the lens, fifteen centimeters into the far side. M = minus fifteen over thirty — minus zero point five: inverted, half size. Real, inverted, diminished, behind — the camera zone.

Case two: object at ten — at the focus. One over q = zero. q at infinity; the emerging rays are parallel.

Case three: object at five — inside the focus. One over q = one over ten minus one over five — minus one over ten — q = *minus* ten. Negative: virtual — and on the *object's* side, ten centimeters in front of the lens. M = plus two: upright and doubled. That's the magnifying glass. Notice: same numbers as the mirror example from last lecture — q = plus fifteen, minus ten — but the *sides* are opposite. The equation is bilingual; the geometry has an accent.

**[6:00–7:00] Common mistake**
The classics. One: placing the real lens image on the object's side — mirror habit. Ask "bounce or pass through?" first. Two: positive f for a diverging lens. Thick middle gets plus; thick edge gets minus. Three: reading q negative as "no image." It's the magnifier's image — the most useful one in the chapter. Four: dropping the minus in M and losing the orientation.

**[7:00–8:00] Quick student challenge**
Predict before computing. A diverging lens: f = minus ten, object at fifteen. What will the image be — type, size, and side? … Diverging lenses only ever make virtual, upright, reduced images, on the object's side. Verify: one over q = minus one over ten minus one over fifteen — minus one sixth — q = minus six centimeters. Virtual, six centimeters in front. M = plus zero point four. Upright, two-fifths size. Prediction confirmed — including the side.

**[8:00–8:30] Final recap**
The flip in ten seconds: mirrors bounce — real images on your side, virtual behind. Lenses transmit — real images behind, on the far side; virtual in front, on the object's side. The equation never changed; only the address of "positive q" did. Bounce or transmit — ask it once, and every sign places itself.

---

## SCRIPT 2 — "From Projector to Magnifying Glass: The Zones of a Converging Lens"

**[0:00–0:30] Hook**
The projector on your lecture hall's ceiling. The magnifying glass in your desk drawer. Two instruments, opposite jobs — one throws a huge real image onto a screen, the other shows you a huge virtual image through the glass. And here's the secret: they are the *same piece of glass*. Same shape, same focal length. The only difference is where you put the object. Today we walk all six stops of a converging lens — from infinity to your eyeball — and find the exact position where one instrument becomes the other.

**[0:30–2:00] Concept introduction**
The setup. A converging lens — thick in the middle, f positive. It has *two* focal points, one on each side, symmetric about the glass; and twice as far out on each side, the 2F landmarks. Those landmarks cut the axis into zones, and each zone is a different instrument.

Start at infinity. A very distant object sends parallel rays; a converging lens bends them all through the far focal point. Image at F: real, inverted, and essentially a point. Now bring the object closer, and watch what happens stop by stop.

**[2:00–4:00] Visual explanation**
Stop one: object beyond 2F. The refracted rays converge between F and 2F on the far side — real, inverted, and *reduced*: a small upside-down image you can catch on a screen. That's your camera: the world far away, squeezed small onto the sensor. Stop two: object exactly at 2F. The image forms exactly at 2F on the far side — real, inverted, *the same size*. Object and image, mirror twins about the lens. That's the photocopier's 1:1 regime. Stop three: object between 2F and F. Now the image moves *beyond* 2F and grows — real, inverted, enlarged. This is the projector: a small slide just outside the focus, thrown huge onto a distant screen. The closer the object creeps to F, the farther and larger the image — without limit.

Stop four: object exactly at F. The refracted rays emerge *parallel* — they never meet. The image has fled to infinity. This is the vanishing point. And stop five — the payoff: object *inside* F. Now the rays *diverge* after the lens. Trace them backward: they meet on the object's side — a virtual, upright, *enlarged* image. Everything flipped — real became virtual, inverted became upright — and the lens became a magnifying glass. Same flip you saw at the focal point of a concave mirror; the lens just performs it on the far side.

And one player never joins this game: the diverging lens. Thick at the edges, f negative — it spreads rays for every object position. One answer, always: virtual, upright, reduced, on the object's side.

**[4:00–6:00] Worked example**
The lecture's numbers — f = plus ten. Landmarks: F at ten, 2F at twenty, on both sides. Object at thirty: beyond 2F — stop one. One over q = one over ten minus one over thirty — q = plus fifteen. Real, inverted, M = minus zero point five — and check: fifteen sits between F and 2F, exactly where stop one promises. The camera.

Object at ten: exactly at F — stop four. q at infinity; parallel rays out. Object at five: inside F — stop five. One over q = minus one over ten — q = minus ten: virtual, ten centimeters on the object's side. M = plus two: upright, doubled. The magnifier. One lens, three stops, three instruments: camera, collimator, magnifying glass. Same glass every time.

**[6:00–7:00] Common mistake**
Three traps. One: expecting the magnifier's image on the far side. It's virtual — it lives on the object's side, where the diverging rays appear to come from. You look *through* the lens at it; you can never project it. Two: declaring "no image" when the object is inside f. There absolutely is one — virtual, upright, enlarged. It's the reason this lens is in your drawer. Three: reading M = plus two as inverted. Plus means upright — the sign and the magnitude are two separate readings.

**[7:00–8:00] Quick student challenge**
Two predictions, no computing. Object exactly at 2F, f = ten: where is the image, what size, what orientation, which side? … At 2F on the *far* side — real, inverted, same size. Now the object slides just inside F. What do you see looking through the lens? … An enormous, upright, virtual image — on your side. Last one: which zone never produces a real image, in the entire lens chapter? … Inside f — and every position for a diverging lens.

**[8:00–8:30] Final recap**
Six stops, one switch — the object's position. Infinity: image at F. Beyond 2F: camera. At 2F: copier. Between 2F and F: projector. At F: infinity. Inside F: magnifying glass — virtual, upright, huge, on your side. The projector and the magnifying glass were never different instruments. They're the same lens, reading different zones. Position is the switch.

---

# 12. PRACTICE QUESTIONS

## LEVEL 1 — UNDERSTAND

1. List the three types of lenses and define a spherical lens.
2. Which lens is thicker at the center than the edges, and what sign does its focal length carry? Which is thicker at the edges?
3. How many focal points does a converging lens have and where? Where is the focal point of a diverging lens, in terms of the light?
4. State the fates of the three principal rays for a thin lens — which ray crosses the lens unchanged?
5. For a converging lens with the object beyond 2f: state the image's type, orientation, size, and the side of the lens on which it forms.
6. An object sits exactly at 2f: where does the image form, and what is M?
7. An object sits inside f of a converging lens: what image forms, on which side, and why is this called the magnifying-glass regime?
8. For a diverging lens at any object position: what image always results?
9. For a lens, where do real images form, and where do virtual images form? State the mirror contrast.
10. State the cause and the remedy of chromatic aberration; then of spherical aberration.

## LEVEL 2 — APPLY

11. A converging lens has f = +20 cm; the object is at p = 30 cm. Find q and M, and fully describe the image (including its side).
12. A converging lens has f = +12 cm; the object is at p = 8.0 cm. Find q and M, and fully describe the image.
13. A diverging lens has f = −12 cm; the object is at p = 24 cm. Find q and M, and fully describe the image.
14. A diverging lens has f = −10 cm; the object is at p = 15 cm. Find q and M.
15. A converging lens has f = +15 cm; the object sits at 2f. Find q and M, and describe the image.
16. An object at p = 40 cm from a lens forms a real image at q = +20 cm. Find f and M, and identify the lens type and zone.
17. An object 12 cm from a lens produces a virtual, upright image 36 cm from the lens (on the object's side). Find f and M, and verify the zone.
18. For a converging lens of focal length f, derive where the object must sit for M = −1, and apply it for f = 10 cm.
19. A converging lens (f = +6.0 cm) is used as a magnifier with the object at 4.0 cm. Find q and M.
20. A real image must form on a screen 60 cm behind a lens, of an object 15 cm in front. Find f and M.

## LEVEL 3 — TRANSFER

21. Camera-style design: a converging lens (f = +5.0 cm) images a distant object at p = 15 cm. Locate the image, find M, and confirm the zone that matches a camera's behavior (real, inverted, reduced).
22. Projector design: with a lens of f = +12 cm, a real image with M = −3 is required on a screen. Find the object and image positions.
23. An object 10 cm from a lens produces a virtual, upright image 30 cm from the lens. Find f and M, identify the lens and zone, and check consistency.
24. Lens-choice reasoning: for each application, choose the lens type and the required object-distance condition — (a) a projector throwing an enlarged real image; (b) a door peephole giving a wide, upright, small view; (c) a magnifying glass.
25. White light passes through a converging lens. Which color focuses closest to the lens, which farthest, and why? What is the remedy for the resulting blur?
26. A lens forms sharp images in red light but blurred images in white light; a different lens blurs even pure single-color light, worse at large aperture. Diagnose both lenses and prescribe the remedy for each.

**INSTRUCTOR ANSWER KEY (not for student display)**

1. Spherical, cylindrical, spherical-cylindrical. Spherical lens: a transparent refracting medium bounded by two spherical surfaces or by one spherical and one plane surface. [EASY]
2. Converging: thick center, f > 0. Diverging: thick edges, f < 0. [EASY]
3. Converging: two real focal points, one on each side, symmetric. Diverging: the refracted rays only *appear* to originate from a focal point on the incoming side. [EASY]
4. Parallel → through F (or appears from F); through the center → straight, undeviated; through the other focal point → emerges parallel. [EASY]
5. Real, inverted, reduced — between f and 2f on the far side (behind the lens). [EASY]
6. At q = 2f on the far side; M = −1 (real, inverted, same size). [EASY]
7. Virtual, upright, enlarged, on the object's side (in front of the lens) — because the refracted rays diverge and their extensions meet there; looking through the lens shows the magnified image. [EASY]
8. Virtual, upright, reduced — always. [EASY]
9. Lens: real behind (far side), virtual in front (object's side). Mirror: real in front, virtual behind — the geometric flip. [EASY]
10. Chromatic: n varies with wavelength (violet refracted more; f_red > f_violet) → remedy: achromatic combination (convex + concave, different materials in contact). Spherical: marginal rays focus differently from near-axis rays → remedy: variable aperture (barrier). [EASY]
11. 1/q = 1/20 − 1/30 = 1/60 → q = +60 cm; M = −2 → real, inverted, doubled, behind the lens. Zone: 2f = 40 > 30 > 20 ✓ (projector zone: real, inverted, enlarged). [EASY]
12. 1/q = 1/12 − 1/8 = −1/24 → q = −24 cm; M = +3 → virtual, upright, tripled, on the object's side (magnifier zone: p < f ✓). [EASY]
13. 1/q = −1/12 − 1/24 = −1/8 → q = −8 cm; M = +1/3 → virtual, upright, reduced, object's side ✓. [EASY]
14. 1/q = −1/10 − 1/15 = −1/6 → q = −6 cm; M = +0.4. [EASY]
15. p = 30 = 2f: 1/q = 1/15 − 1/30 = 1/30 → q = +30 cm; M = −1 → real, inverted, same size at 2f, behind the lens. [EASY]
16. 1/f = 1/40 + 1/20 = 3/40 → f = +13.3 cm (converging); M = −0.5. Zone: p = 40 > 2f ≈ 26.7 ✓ — real, inverted, reduced (camera zone). [MEDIUM — inverted reasoning]
17. q = −36: 1/f = 1/12 − 1/36 = 1/18 → f = +18 cm (converging); M = +3. Zone: p = 12 < f = 18 ✓ — magnifier zone, virtual/upright/enlarged, consistent. [MEDIUM]
18. M = −1 → q = p → 2/p = 1/f → p = 2f. With f = 10 cm: p = 20 cm, q = +20 cm. [MEDIUM — derivation]
19. 1/q = 1/6 − 1/4 = −1/12 → q = −12 cm; M = +3 → virtual, upright, tripled, object's side. [EASY]
20. 1/f = 1/15 + 1/60 = 5/60 = 1/12 → f = +12 cm; M = −60/15 = −4 → real, inverted, quadrupled on the screen. [EASY]
21. 1/q = 1/5 − 1/15 = 2/15 → q = +7.5 cm; M = −0.5 → real, inverted, half-size, behind. Zone: p = 15 > 2f = 10 ✓ — the camera regime (real, inverted, reduced), with the image between f (5) and 2f (10) ✓. [MEDIUM — design check]
22. M = −3 → q = 3p; 1/12 = 1/p + 1/3p = 4/3p → 3p = 48 → **p = 16 cm, q = +48 cm** (check: 1/16 + 1/48 = 4/48 = 1/12 ✓). Zone: 2f = 24 > 16 > 12 ✓ projector regime. [HARD — design chain]
23. q = −30: 1/f = 1/10 − 1/30 = 1/15 → f = +15 cm (converging); M = +3. Zone: p = 10 < f = 15 ✓ magnifier zone — virtual, upright, enlarged ✓. [MEDIUM]
24. (a) Converging with 2f > p > f. (b) Diverging (any p — always V/U/R, wide field). (c) Converging with p < f. [MEDIUM — design reasoning]
25. Violet focuses closest (refracted more, shortest f); red farthest (f_red > f_violet per the source); intermediate colors between them → blurred white-light image. Remedy: achromatic combination. [MEDIUM]
26. Lens 1: chromatic aberration (blur only in white light = color-dependent) → achromatic doublet. Lens 2: spherical aberration (blur even monochromatic, worse at large aperture = ray-height-dependent) → variable aperture. [MEDIUM — diagnostic reasoning]

---

# 13. TRANSFER QUESTIONS

*New-context problems carrying Lecture 12 concepts into unfamiliar settings.*

**T1 — Peephole design:** A door peephole must show an approaching person as an upright, small, wide-view image for *any* standing distance. Using the image tables (no computation), select the lens type and justify why the alternative would fail.
→ *Key:* Diverging lens — always virtual, upright, reduced for every p (one fixed behavior, wide apparent field). A converging lens flips character across zones: the visitor's image would invert or blow up depending on distance. [MEDIUM]

**T2 — Projector design (numbers):** A projector must throw an image with M = −4 onto a screen 80 cm behind the lens. Find the required focal length and the object (slide) position.
→ *Key:* q = +80, M = −4 → p = q/4 = 20 cm; 1/f = 1/20 + 1/80 = 5/80 = 1/16 → **f = +16 cm, slide at 20 cm**. Zone: 2f = 32 > 20 > 16 ✓ projector regime. [MEDIUM-HARD — design chain]

**T3 — Conjugate positions (lens version):** For a converging lens, compute the image for p = 3f and for p = 1.5f. What structural property of the equation do the two (object, image) pairs reveal?
→ *Key:* p = 3f: 1/q = 1/f − 1/3f = 2/3f → q = 1.5f, M = −0.5. p = 1.5f: 1/q = 1/f − 1/1.5f = 1/3f → q = 3f, M = −2. The pairs are reciprocal: the image location of one is the object location of the other — p and q are interchangeable in the equation (object and image can swap roles). [HARD — structural insight]

**T4 — Magnifier design:** A jeweler wants M = +4 with the gem held 6.0 cm from the lens. Find the required focal length, and verify the zone consistency.
→ *Key:* M = −q/p → +4 = −q/6 → q = −24 cm; 1/f = 1/6 − 1/24 = 3/24 = 1/8 → **f = +8 cm** (converging). Check: p = 6 < f = 8 ✓ — magnifier zone. [MEDIUM-HARD — design inversion]

**T5 — Aberration diagnosis from symptoms:** Two lenses are tested. Lens A: sharp in monochromatic laser light, blurred under white light. Lens B: blurred even in laser light, and the blur worsens when the aperture is opened. Identify each defect and prescribe each remedy.
→ *Key:* A = chromatic (color-dependent; n varies with λ, f_red > f_violet) → achromatic combination (convex + concave, different materials). B = spherical (ray-height-dependent; marginal vs. paraxial foci) → variable aperture. [MEDIUM]

**T6 — Identification without computation:** An image of a real object cannot be caught on a screen, is upright, and is *smaller* than the object. Identify the lens type by reasoning alone, and explain why a converging lens could not have produced this.
→ *Key:* Diverging. A converging lens produces virtual images only when p < f — and those are always *enlarged* (|M| > 1); a reduced virtual image can only come from a diverging lens (|M| < 1 always). [MEDIUM-HARD — elimination reasoning]

---

# 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All Lecture 12 topics present: three lens types + spherical lens definition; converging/diverging (shapes, f signs); focal points of both; three principal rays; convex-lens image cases (all six incl. p = ∞); "If p > f real, inverted / p < f virtual, upright" statements; concave lens (V/U/R); the equation + M = −q/p; sign conventions; |M| readings; chromatic aberration (full causal chain, f_red > f_violet, prism-like edges, remedy); spherical aberration (cause, remedy). |
| Mathematical formulas correct | ✅ | All formulas match the source; the source example reproduces exactly (+15/−0.5; ∞; −10/+2); all practice/transfer computations verified with zone-consistency checks. |
| Technical terminology preserved | ✅ | Spherical/cylindrical/spherical-cylindrical lenses; converging/diverging; chromatic/spherical aberration; achromatic combination; variable aperture; "lens maker's equation" (source's name) retained with a clarifying note. |
| Explanations in original language | ✅ | No source paragraphs reproduced; only formulas and short standard definitions shared. |
| Understandable to a first-year student | ✅ | Bounce-vs-transmit framing for the sign flip; instrument icons (camera/copier/projector/magnifier) for the zones; prism analogy for dispersion. |
| Difficult concepts explicitly identified | ✅ | 6 concepts with full analysis and difficulty ratings in §9. |
| Common misconceptions identified | ✅ | 10 in §7; per-concept misconceptions in §9; in-video mistakes in §10–11. |
| Examples actually teach | ✅ | The source example retained in full (all three parts); 5 clearly-flagged pedagogical examples added (diverging computation; magnifier; object at 2f; projection design; aberration diagnosis) to cover skills the source's single converging example doesn't exercise. |
| Practice progresses understand → apply → transfer | ✅ | L1 (10 conceptual) → L2 (10 computational) → L3 (6 synthesis) + 6 transfer tasks, all with verified keys. |
| No unsupported claims added | ✅ | Flagged items: cylindrical/spherical-cylindrical lens details [SOURCE DOES NOT SPECIFY]; the lens-specific sign-convention table rows were not captured in the extraction — reconstructed from the source's own Chapter-10 definitions table ("real: behind lenses; virtual: in front of lenses"), its converging/diverging f-statements, and Example 2's confirmations; the six-zone table is presented as reconstructed from the source's own equation and its two stated rules ("p > f real, inverted; p < f virtual, upright"), matching its figure labels; the "camera/copier/projector/magnifier" labels, aperture light trade-off note, and chromatic illustration are clearly-marked everyday framings. |
| No large verbatim reproduction | ✅ | Only formulas and short standard definitions overlap with the source. |
| Suitable for direct web integration | ✅ | Clean Markdown; student-facing self-check separated from instructor keys. |

**Source errata handled transparently (meaning preserved, typos not propagated):**
- "Focal point of converging **length**" → restored as "lens" (obvious typographical slip, consistent with the figure context).
- The source labels 1/p + 1/q = 1/f the "lens maker's equation"; the source's naming is preserved, with the standard-name note ("thin-lens equation") clearly flagged as clarification — no formula or meaning altered.
- The lens sign-convention table and the image-case figures carry labels only in the extracted text; their content is reconstructed from the source's own Chapter-10 definitions (Lecture 11's table), its explicit converging/diverging statements, and its worked example — flagged in §4 and §6.
- No numerical errata: the source's Example 2 computes consistently throughout.


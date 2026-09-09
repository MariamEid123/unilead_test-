# ARETE — LECTURE 8 (FULL TRANSFORMATION)

---

# 1. SOURCE ANALYSIS

| Item | Value |
|---|---|
| Course | PHY 211 — Physics (Electricity, Magnetism & Optics) |
| Lecture | **Lecture 8** — Chapter 7 |
| Title | Magnetic Fields |
| Instructor | Dr. Ashraf Mousa Abdelwahed — AIU, Fall 2024 |

**Main topics:**
1. Magnetic poles
2. Magnetic fields and field lines
3. Force on a charge moving in a magnetic field
4. Units of the magnetic field (tesla, gauss)
5. Notation for 3-D field diagrams (figures only in source)
6. Motion of a charged particle in a uniform magnetic field
7. Magnetic force on a current-carrying conductor

**Subtopics:** dipolar structure of magnets; pole–pole forces (attract/repel, inverse-square); naming of poles via Earth's field; no magnetic monopoles; field set up by moving charges and by magnets; compass definition of B's direction; field lines outside a magnet (N → S); Earth's magnetic field (figure); proportionality facts of the magnetic force (q, B, v, sin θ); maximum and zero conditions; direction reversal for negative charges; Right-Hand rule 1 or 2; 1 T = 1 Wb/m² = 1 N/(A·m); 1 T = 10⁴ gauss; centripetal action of the force; r = mv/(|q|B); ω = v/r; carrier-counting derivation of F = IL × B with I = nqAv.

**Learning objectives (from content):** describe poles and fields; compute force magnitudes with sin θ; determine force directions with the RHR; analyze circular motion of charges; derive and apply the force on a current-carrying wire.

**Important definitions:** magnetic pole; magnetic field direction (compass definition); tesla; gauss; centripetal acceleration; mobile charge carrier density (n).

**Examples in source:** 2 (TV electron force; proton orbit speed).

**Procedures:** force-magnitude evaluation (identify θ → substitute); direction determination (RHR → flip if q < 0); circular-motion analysis (set |q|vB = mv²/r).

**Common misconceptions in source material:** force along B; same force direction for + and − charges; field lines S → N outside.

**Difficult concepts:** 3-D direction of the cross product; charge-sign reversal; angle identification; perpendicular force → circular motion; the microscopic derivation of F = BIL.

**Prerequisites:** Lecture 7 (electric current I); vector cross products; uniform circular motion (centripetal force mv²/r); electric charge; basic trigonometry (sin θ).

**Concept map:**

```
Magnetic Fields (Ch. 7)
├── Structure of magnetism
│   ├── Every magnet: N & S poles; like repel, unlike attract
│   ├── Pole force ∝ 1/r²
│   └── No monopoles — cutting a magnet always yields N–S pairs
├── The magnetic field B
│   ├── Sources: moving charges, magnets
│   ├── Direction = where a compass north points
│   ├── Field lines outside magnet: N → S
│   └── Earth's magnetic field (figure in source)
├── Force on a moving charge
│   ├── F = q v × B ; |F| = |q|vB sin θ
│   ├── Zero: v ∥ B (θ = 0°, 180°) · Max: v ⊥ B
│   ├── Direction: RHR → flip for negative q
│   └── Units: 1 T = 1 N/(A·m) = 10⁴ G
├── Circular motion (v ⊥ B)
│   └── |q|vB = mv²/r → r = mv/(|q|B) ; ω = v/r
└── Force on a current-carrying wire
    └── F = (q v × B)·nAL with I = nqAv → F = I L × B ; |F| = BIL sin θ
```

**Dependencies:** builds directly on Lecture 7 (the current I); prerequisites from earlier chapters (charge, vectors, circular motion) are assumed.

---

# 2. COURSE / MODULE / LESSON METADATA

| Field | Value |
|---|---|
| **COURSE** | PHY 211 — Physics II |
| **MODULE** | Magnetic Fields & Forces (Chapter 7) |
| **LESSON** | Lecture 8 — Magnetic Fields |
| **TOPICS** | Poles; field concept & field lines; force on moving charges (magnitude + direction); tesla/gauss; circular motion of charges; force on current-carrying wires |
| **PREREQUISITES** | Lecture 7 (current); vector cross products; uniform circular motion; electric charge; trigonometry |
| **COMPETENCIES** | State the magnetic-force proportionality facts; compute F = \|q\|vB sin θ; determine force direction with the RHR (incl. sign of charge); convert tesla ↔ gauss; derive and use r = mv/(\|q\|B) and ω = v/r; derive F = BIL sin θ from the single-charge law and apply it |
| **DIFFICULTY** | Overall: MEDIUM · Force magnitudes & circular motion: MEDIUM · Direction reasoning (RHR + sign) and the wire derivation: HARD |
| **ESTIMATED STUDY TIME** | ~3.5 hours (lesson 75 min · worked examples 25 min · practice 50 min · videos 16 min · self-check & transfer 40 min) |

**ARETE flow placement:**
- **LEARN:** poles, field concept, force law.
- **PRACTICE:** magnitude computations with sin θ.
- **PROVE:** direction determination with the RHR (including electrons); the wire-force derivation.
- **REMEDIATE/RETRY targets:** forgetting the negative-charge flip; measuring θ from the wrong reference; expecting the force along B.
- **TRANSFER:** geometry-based direction problems; r and ω reasoning for changed parameters.
- **MASTER:** combined direction + computation problems (e.g., design a field for a desired orbit radius).

---

# 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Describe the pole structure of magnets (attraction/repulsion rules, inverse-square pole force) and explain why an isolated magnetic pole cannot exist.
2. Define the direction of the magnetic field operationally (compass north) and state how field lines run outside a magnet.
3. State the experimental proportionality facts of the magnetic force and package them in F = q**v** × **B**.
4. Compute the force magnitude |q|vB sin θ and identify the maximum and zero conditions.
5. Determine the force direction with the right-hand rule, reversing it for negative charges.
6. Convert between tesla and gauss.
7. Apply |q|vB = mv²/r to find the radius or speed of a charged particle circling in a uniform field, and compute ω = v/r.
8. Reproduce the derivation of F = I**L** × **B** from the single-charge force (carrier counting, I = nqAv) and apply F = BIL sin θ.

---

# 4. WEB-READY LESSON

# Lecture 8 — Magnetic Fields

## Prerequisites
The student should already understand:
- Electric current (Lecture 7).
- Vector cross products and right-handed coordinate systems.
- Uniform circular motion: centripetal force mv²/r.
- Electric charge (including the sign convention).
- Trigonometry: sine of an angle, sin 90° = 1, sin 0° = 0.

---

### 1. Magnetic Poles

**Core Idea**
Every magnet, whatever its shape, has exactly two poles — north and south — and poles interact like electric charges do: like poles repel, unlike poles attract.

**Explanation**
The specific rules: N–N or S–S repel; N–S attract. The force between two poles varies as the **inverse square of the distance** between them. The poles were *named* for how a magnet behaves in Earth's field: suspend a bar magnet so it can turn freely, and it rotates until its magnetic north pole points toward Earth's north geographic pole.

The deepest fact in this section: **a single magnetic pole has never been isolated** — no magnetic monopole exists. No matter how many times you cut a permanent magnet in two, every piece comes out with its own north *and* south pole. Magnetism is fundamentally dipolar.

**Example**
Cut a bar magnet in half: you don't get a separate N and a separate S — you get two smaller, complete magnets, each with both poles. Cut those again: same result, forever.

**Key Point**
Magnets always come as N–S pairs; like poles repel, unlike attract, and the pole force falls off as 1/r².

### 2. Magnetic Fields and Field Lines

**Core Idea**
Any moving electric charge — and any magnet — fills the space around it with a magnetic field **B**, whose direction at any point is the direction a compass needle's north pole points there.

**Explanation**
The reminder from electrostatics: a static electric charge is surrounded by an electric field. The magnetic analog: the region of space surrounding any **moving** electric charge also contains a magnetic field, and every magnet sets one up around itself.

The operational definition of direction: **the direction of B at any location is the direction in which the north pole of a compass needle points at that location.** This makes B measurable and mappable — a compass can literally trace the field lines. Outside a magnet, the lines run from the **north pole to the south pole**. Earth itself has a magnetic field (shown as a figure in the source; further details [SOURCE DOES NOT SPECIFY]).

**Example**
Sprinkle small compasses around a bar magnet: each needle aligns with the local field, and the needle tips collectively map the N → S pattern outside the magnet.

**Key Point**
Moving charge ⇒ magnetic field; B's direction is defined by where a compass north points; field lines outside a magnet: N → S.

### 3. Force on a Moving Charge — Magnitude

**Core Idea**
A charge q moving with speed v in a field B feels a force of magnitude **|q|vB sin θ** — proportional to the charge, the field, the speed, and the sine of the angle between v and B.

**Explanation**
The experimental facts:
- The magnitude F_B is proportional to the charge q, the field B, and the speed v.
- When the velocity is **parallel** to the field (θ = 0° or 180°), the force is **zero**.
- When the velocity makes any angle θ ≠ 0 with the field, the force acts in a direction **perpendicular to both** the velocity and the field.
- The force on a **positive** charge is opposite to the force on a **negative** charge moving in the same way.
- The magnitude is proportional to **sin θ**, where θ is the angle between v and B.

Packaged in one equation:

**F_B = |q| v B sin θ**

with the extremes:
- **Minimum:** F = 0 when v ∥ or antiparallel to B (θ = 0° or 180°).
- **Maximum:** F = |q|vB when v ⊥ B (θ = 90°).

**Example**
An electron at 8.0 × 10⁶ m/s in a 0.025 T field at 60° to its velocity: F = (1.6 × 10⁻¹⁹)(8.0 × 10⁶)(0.025) sin 60° = 2.8 × 10⁻¹⁴ N. (Worked Example 1.)

**Key Point**
F = |q|vB **sin θ** — zero when aligned with the field, maximum when perpendicular; θ is the angle between v and B, nothing else.

### 4. Force Direction — the Right-Hand Rule

**Core Idea**
The direction of the magnetic force comes from the vector equation **F_B = q v × B** and is found with the right-hand rule — then reversed if the charge is negative.

**Explanation**
All the facts of Section 3 are summarized in the single vector equation:

**F_B = q v × B** (F in N, q in C, v in m/s, B in T)

The cross product says the force is perpendicular to *both* v and B — a genuinely three-dimensional, "sideways" force. The direction is determined by **Right-Hand rule 1 or 2** (the source names both variants without specifying one — [SOURCE DOES NOT SPECIFY] which; any standard version gives the same answer).

The standard version: point the fingers of your right hand along **v** (for a positive charge), curl them toward **B**; the **thumb** gives the force. Because the law contains q, a **negative charge reverses the direction** — solve for a positive charge, then flip.

*Instructor note on diagram notation (standard convention supporting the source's "Notation notes" figures, whose details are not captured in the text):* a field pointing **out of the page** is drawn as a dot ⊙; a field **into the page** as a cross ⊗.

**Example**
v to the right, B into the page: right-hand rule gives the force **upward** for a proton — and **downward** for an electron, same motion.

**Key Point**
Direction = right-hand rule for **v × B**, then flip for negative charges. The force never points along v or along B.

### 5. Units of the Magnetic Field

**Core Idea**
The SI unit of B is the **tesla (T)**; the common non-SI unit is the **gauss (G)**, with 1 T = 10⁴ G.

**Explanation**
The tesla is built from the force law:

**1 T = 1 Wb/m² = 1 N/(C·m/s) = 1 N/(A·m)**

The gauss conversion:

**1 T = 10⁴ Gauss**

Everyday fields are tiny in tesla (the source's TV coil field is 0.025 T), which is why the gauss survives in practice. [Specific everyday field values: SOURCE DOES NOT SPECIFY.]

**Example**
0.025 T = 250 G; conversely, 500 G = 5.0 × 10⁻⁵ T.

**Key Point**
1 T = 1 N/(A·m); 1 T = 10⁴ G. Check units whenever a field is given in gauss.

### 6. Motion of a Charged Particle in a Uniform Magnetic Field

**Core Idea**
With v perpendicular to B, the magnetic force has constant magnitude and always points toward the center of the path — it is a centripetal force, and the particle moves in a circle.

**Explanation**
The force is always perpendicular to the velocity, so it changes the velocity's *direction* while leaving circular motion at constant speed — the magnetic force supplies the centripetal acceleration:

**|q| v B = mv²/r**

Solving for the radius:

**r = mv/(|q|B)**

The radius is proportional to the **linear momentum mv** and inversely proportional to the charge and the field. The **angular speed** of the particle is:

**ω = v/r** (in rad/s)

**Example**
A proton circling with r = 14 cm in a 0.35 T field moves at v = |q|rB/m = 4.7 × 10⁶ m/s. (Worked Example 2.)

**Key Point**
Perpendicular force ⇒ circular motion: r = mv/(|q|B). Fast or heavy particles make big circles; strong fields and large charges make small ones.

### 7. Magnetic Force on a Current-Carrying Conductor

**Core Idea**
A current is a collection of many moving charges, so a wire in a magnetic field feels the vector sum of all the individual magnetic forces — which collapses into **F = I L × B**.

**Explanation**
Build it in four steps:
1. Each charge carrier in the wire feels **q v × B** (v = drift velocity along the wire).
2. Count the carriers in a straight segment of length L and cross-section A: the segment's volume is AL, and with n carriers per unit volume, the number of carriers is **nAL**.
3. The total force is the sum: **F_B = (q v × B) nAL**.
4. Use the current relation **I = nqAv** — the scalars regroup (v and L are both along the wire), collapsing the swarm into:

**F_B = I L × B  with magnitude  F_B = B I L sin θ**

Here **L is a vector pointing in the direction of the current**, with magnitude equal to the segment length, and **θ is the angle between L (i.e., the current) and B**.

**Example**
A 0.50 m wire carrying 2.0 A perpendicular to a 0.10 T field: F = BIL = 0.10 × 2.0 × 0.50 = 0.10 N. (Worked Example 3.)

**Key Point**
Same law, macroscopic form: replace the single charge's q**v** with the wire's I**L**; θ is between the wire (current) and the field.

---

## Key Takeaways
1. Every magnet is a dipole — no isolated poles exist; cutting a magnet always yields smaller dipoles; pole forces follow 1/r².
2. Moving charges and magnets set up B; its direction is where a compass north points; field lines outside a magnet run N → S.
3. F = |q|vB sin θ — zero when v ∥ B, maximum |q|vB when v ⊥ B.
4. The force is perpendicular to *both* v and B; find its direction with the right-hand rule and **flip for negative charges**.
5. 1 T = 1 N/(A·m) = 10⁴ gauss.
6. v ⊥ B ⇒ uniform circular motion with r = mv/(|q|B) and ω = v/r — the field steers, it doesn't push along the path.
7. A current is a stream of charges: F = BIL sin θ, with L along the current and θ between the current and the field.
8. In every magnetic-force formula, the angle is between the *motion* (v or L) and B — identify it before substituting anything.

## Self-Check (attempt before looking at answers)
1. What happens if you cut a bar magnet exactly in half — do you isolate a single pole? What do you get?
2. How is the direction of B at a point defined experimentally, and what tool performs the measurement?
3. Outside a bar magnet, do the field lines run N → S or S → N?
4. A proton moves parallel to a magnetic field. What is the magnetic force on it — and what is it for an electron moving the same way?
5. Under what condition is the force on a moving charge maximum, and what is that maximum value?
6. An electron and a proton move with the same velocity in the same field (neither parallel to B). Compare their force magnitudes and their force directions.
7. What relation connects the current to the microscopic carrier picture (n, q, A, v)?
8. In F = BIL sin θ, what exactly does θ measure — and what happens to the force if the wire is parallel to B?
9. A proton circles in a fixed uniform field. If its speed doubles, what happens to the radius of its circle? What happens to ω = v/r?
10. Convert 0.30 T to gauss, and 500 G to tesla.

---

# 5. FORMULAS

| # | Formula | Variables | When it is used | Interpretation & assumptions |
|---|---|---|---|---|
| 1 | **F**_B = q**v** × **B** | q: charge (C); **v**: velocity (m/s); **B**: field (T) | Force on a moving point charge (direction) | Result perpendicular to both v and B; reverses for negative q |
| 2 | F_B = \|q\| v B sin θ | θ: angle between **v** and **B** | Force magnitude | F = 0 for θ = 0°, 180°; F_max = \|q\|vB for θ = 90° |
| 3 | 1 T = 1 Wb/m² = 1 N/(C·m/s) = 1 N/(A·m) | — | Unit definition of the tesla | Follows directly from the force law |
| 4 | 1 T = 10⁴ Gauss | — | Unit conversion | Check units when B is given in gauss |
| 5 | \|q\| v B = mv²/r | m: particle mass (kg); r: orbit radius (m) | Circular motion, v ⊥ B | Magnetic force = centripetal force |
| 6 | r = mv/(\|q\|B) | — | Orbit radius; also inverted for v or B | r ∝ momentum; r ∝ 1/(\|q\|B); assumes v ⊥ B |
| 7 | ω = v/r | ω: angular speed (rad/s) | Speed around the circle | Combining with #6 gives ω = \|q\|B/m (derived) |
| 8 | I = nqAv | n: carriers per unit volume; A: cross-section; v: drift speed | Connects current to carrier picture | Used in deriving the wire force |
| 9 | **F**_B = (**q**v** × B**)·nAL | L: segment length; AL: segment volume | Intermediate step: total force on a wire segment | nAL = number of carriers in the segment |
| 10 | **F**_B = I**L** × **B** | **L**: vector along the current, magnitude = segment length | Force on a straight current-carrying segment | Direction from the same right-hand rule |
| 11 | F_B = B I L sin θ | θ: angle between **L** (current) and **B** | Force magnitude on a wire | Zero if the wire is parallel to B; max = BIL if perpendicular |

---

# 6. WORKED EXAMPLES

**WE 1 — Force on a TV electron (Source Example 1)**
An electron in an old-style TV picture tube moves toward the front of the tube at 8.0 × 10⁶ m/s along the x-axis. Coils around the neck create a field of 0.025 T at 60° to the x-axis, lying in the xy-plane. Find the magnetic force.
1. Identify the angle: θ = 60° (the angle between v and B — both given relative to the x-axis, so the angle *between them* is 60°).
2. F = |q|vB sin θ = (1.6 × 10⁻¹⁹)(8.0 × 10⁶)(0.025)(sin 60°).
3. Multiply: (1.6 × 8.0 × 0.025) = 0.32 → 0.32 × 10⁻¹³ = 3.2 × 10⁻¹⁴; × 0.866:
4. **F = 2.8 × 10⁻¹⁴ N.**
5. Note: the formula gives the magnitude only; the direction requires the right-hand rule for v × B, then a flip because the charge is negative.

**WE 2 — Proton orbit speed (Source Example 2)**
A proton moves in a circular orbit of radius 14 cm in a uniform 0.35 T field perpendicular to its velocity. Find its speed. (m_p = 1.67 × 10⁻²⁷ kg.)
1. From r = mv/(|q|B), rearrange: v = |q|rB/m.
2. v = (1.6 × 10⁻¹⁹)(0.14)(0.35)/(1.67 × 10⁻²⁷).
3. Numerator: 0.0784 × 10⁻¹⁹ = 7.84 × 10⁻²¹.
4. **v = 7.84 × 10⁻²¹ / 1.67 × 10⁻²⁷ = 4.7 × 10⁶ m/s.**
5. Extension: ω = v/r = 4.7 × 10⁶/0.14 ≈ **3.4 × 10⁷ rad/s.**
*(Source erratum: the printed numerator shows 1.6 × 10⁻¹⁶ C; the printed answer, 4.7 × 10⁶ m/s, requires the proton charge 1.6 × 10⁻¹⁹ C, which is used here.)*

**WE 3 — Force on a current-carrying wire (pedagogical example — the source derives the formula but includes no numerical wire example)**
A straight 0.50 m wire carries 2.0 A perpendicular to a 0.10 T uniform field. Find the force.
1. θ = 90° (wire ⊥ field) → sin θ = 1.
2. F = BIL sin θ = 0.10 × 2.0 × 0.50 × 1.
3. **F = 0.10 N.**
4. If the wire were at 60° to the field instead: F = 0.10 × sin 60° ≈ 0.087 N. If parallel to the field: F = 0.

**WE 4 — Direction workout (pedagogical example)**
A proton moves due east; the magnetic field points due north. Find the force direction. Then repeat for an electron, and for the case "B into the page, proton moving to the right."
1. Proton east, B north: right-hand rule — fingers east, curl toward north → thumb points **up** (out of the ground). Force is upward.
2. Electron, same motion: flip → force **downward**, same magnitude (same |q|, v, B).
3. B into the page (⊗), proton moving right: v × B = **up the page** (for the positive proton).
Direction problems are solved in two steps: right-hand rule, then sign check.

---

# 7. COMMON MISTAKES

| # | What students usually do | Why it's wrong | How to avoid it |
|---|---|---|---|
| 1 | Assume the force points along **B** (like gravity along g) | The force is the cross product — perpendicular to *both* v and B | Tag every v × B problem with "perpendicular to both" |
| 2 | Apply the right-hand rule and forget the flip for electrons | F = q**v** × **B**: a negative q reverses the force | Solve for a positive charge, then reverse if q < 0 |
| 3 | Use the angle between v and the surface/normal instead of between v and B | θ is strictly the angle between the two vectors in the formula | Identify v and B first; θ is the smaller angle between them |
| 4 | Use F = \|q\|vB when v is not perpendicular to B | That is the *maximum* formula; the general case needs sin θ | Default to F = \|q\|vB sin θ; sin 90° = 1 recovers the maximum |
| 5 | Use the complement angle (e.g., 30° instead of 60°) | If a problem gives the angle from another reference, convert first | Draw v and B tail-to-tail and read the angle between them |
| 6 | Mix gauss and tesla | 1 G = 10⁻⁴ T — a factor of 10⁴ error | Convert to tesla before substituting into formulas |
| 7 | Invert r = mv/(\|q\|B) incorrectly | The radius grows with momentum and shrinks with field and charge | Remember the pattern: "fast/heavy = big circle; strong field/charge = small circle" |
| 8 | Expect the circling particle to speed up | The force is centripetal — it changes the *direction* of v, not its magnitude (uniform circular motion) | Perpendicular force ⇒ turning, not accelerating along the path |
| 9 | In F = BIL sin θ, measure θ between the wire and the normal (or the page) | θ is between the wire/current and **B** itself | Draw the wire and the field; read the angle between those two lines |
| 10 | Treat L as just a number | **L is a vector along the current** — its direction enters the cross product | Assign L the current's direction before applying the right-hand rule |

---

# 8. LECTURE SUMMARY

# Lecture Summary — Magnetic Fields

## What You Need to Know
- The dipolar structure of magnets, the pole interaction rules, and why monopoles can't be isolated.
- The operational definition of B's direction (compass north) and the N → S pattern of field lines outside a magnet.
- The complete force law on a moving charge: magnitude, direction, and the maximum/zero conditions.
- The right-hand rule, including the sign flip for negative charges.
- The tesla and its relation to the gauss.
- Circular motion of a charge perpendicular to B: r = mv/(|q|B), ω = v/r.
- The derivation of the force on a current-carrying wire from the carrier picture.

## Key Definitions
- **Magnetic pole** → the two (N and S) ends of every magnet; like poles repel, unlike attract; pole force ∝ 1/r².
- **Magnetic monopole** → an isolated single pole — never observed; cutting a magnet always yields N–S pairs.
- **Magnetic field B** → the region around moving charges and magnets; its direction = the direction a compass north pole points.
- **Tesla (T)** → SI unit of B: 1 T = 1 Wb/m² = 1 N/(C·m/s) = 1 N/(A·m).
- **Gauss (G)** → non-SI unit: 1 T = 10⁴ G.
- **Centripetal force** → the inward force (here \|q\|vB) that bends a perpendicular velocity into a circle.
- **L (in F = IL × B)** → a vector pointing along the current with magnitude equal to the segment's length.
- **n (carrier density)** → number of mobile charge carriers per unit volume; enters I = nqAv.

## Key Formulas
- F = q**v** × **B**; F = |q|vB sin θ → force on a moving charge.
- 1 T = 1 N/(A·m); 1 T = 10⁴ G → units.
- |q|vB = mv²/r → r = mv/(|q|B); ω = v/r → circular motion.
- I = nqAv; F = (**qv** × **B**)nAL → F = I**L** × **B**; F = BIL sin θ → force on a wire.

## Important Ideas
- Magnetism is intrinsically dipolar; there is no magnetic analog of an isolated charge.
- A magnetic field surrounds *moving* charge — motion is the essential ingredient.
- The magnetic force is sideways: perpendicular to both the motion and the field — never along either.
- Alignment kills the force (v ∥ B ⇒ F = 0); perpendicularity maximizes it.
- A perpendicular magnetic force turns motion into a circle without changing the speed.
- A current-carrying wire is a "river of charges" — summing the single-charge forces collapses into F = BIL sin θ.

## Common Mistakes
Force along B; missing the negative-charge flip; wrong angle reference; dropping sin θ; gauss/tesla confusion; inverted r-formula; expecting speed-up in the circle; θ measured from the wrong line for wires; L treated as directionless.

## Exam Focus
1. Computing F = |q|vB sin θ with the *correct* angle (including recognizing the zero-force case).
2. Direction problems: RHR + sign of charge, often with into/out-of-page notation.
3. r = mv/(|q|B) in all directions: find r, find v, find B — plus ω = v/r.
4. F = BIL sin θ with the angle between the wire and the field, and reproducing its derivation.

## 60-Second Review
Every magnet: two poles; like repel, unlike attract; force ∝ 1/r²; no monopoles. B surrounds moving charges and magnets; direction = compass north; lines outside: N → S. Force on a moving charge: F = |q|vB sin θ — zero if v ∥ B, max \|q\|vB if ⊥; direction by right-hand rule (v, curl to B, thumb = F), flip for negative charges. Units: 1 T = 1 N/(A·m) = 10⁴ G. v ⊥ B ⇒ circle: r = mv/(|q|B), ω = v/r — field steers, never pushes along. A wire is charges in motion: count nAL carriers, use I = nqAv, get F = BIL sin θ, θ between current and B.

---

# 9. DIFFICULT CONCEPTS

### Difficult Concept: The Right-Hand Rule and the Cross-Product Direction
**Why students struggle:** The result lives in 3-D, perpendicular to *two* given vectors at once; students have never used a rule where the answer is orthogonal to both inputs, and hand-based rules feel arbitrary.
**Simple explanation:** The magnetic force is always sideways — perpendicular to the velocity *and* to the field — and the right hand is just a physical device for finding that sideways direction.
**Intuitive analogy:** A car driving through a crosswind: the push on the car is neither forward (along v) nor along the wind's own line — it shoves the car sideways, perpendicular to both.
**Step-by-step:** (1) Point right-hand fingers along **v**. (2) Curl them toward **B**. (3) The thumb gives the force for a **positive** charge. (4) If q < 0, reverse the answer. (5) If **v** ∥ **B**, no curl is possible — force zero.
**Mini example:** v right, B into the page → F up (proton), F down (electron).
**Misconception to avoid:** "The force points along the field" and "the same direction for + and − charges."
**Difficulty: HARD** → video provided

### Difficult Concept: The Zero-Force Alignment (v ∥ B)
**Why students struggle:** Intuition says maximum alignment with the field should mean maximum effect — like gravity or electric forces.
**Simple explanation:** The sin θ factor kills the force exactly when the motion and the field line up: θ = 0° or 180° gives sin θ = 0.
**Intuitive analogy:** Trying to screw a screw with a screwdriver held *along* the screw axis... hmm — simpler: a rudder works only when water flows *across* it; flow straight along the blade and nothing turns.
**Step-by-step:** (1) Locate v and B. (2) Find the smaller angle between them. (3) F ∝ sin θ. (4) θ = 0° or 180° → F = 0; θ = 90° → F = |q|vB.
**Mini example:** A proton moving exactly along the field lines feels nothing, no matter how fast.
**Misconception to avoid:** "Moving through the strongest field region gives the biggest force regardless of direction."
**Difficulty: MEDIUM**

### Difficult Concept: Circular Motion from a Perpendicular Force
**Why students struggle:** Students expect forces to speed things up; here the force only turns them, and the radius formula mixes four quantities.
**Simple explanation:** A force always perpendicular to the velocity changes its direction, not its magnitude — the definition of uniform circular motion. Setting the sideways force equal to the required centripetal force gives r = mv/(|q|B).
**Intuitive analogy:** Swinging a ball on a string: the hand pulls inward constantly; the ball travels in a circle at unchanged speed.
**Step-by-step:** (1) v ⊥ B ⇒ |F| = |q|vB, constant. (2) F always ⊥ v ⇒ centripetal. (3) |q|vB = mv²/r. (4) Solve for whichever quantity is asked: r = mv/(|q|B), v = |q|rB/m, B = mv/(|q|r). (5) ω = v/r.
**Mini example:** Same proton, same field, double the speed → double the radius; the angular speed ω = v/r stays the same.
**Misconception to avoid:** "The magnetic force accelerates the particle" — it changes velocity's *direction*, not its magnitude.
**Difficulty: MEDIUM**

### Difficult Concept: From Single Charges to a Whole Wire (the F = BIL derivation)
**Why students struggle:** It is a microscopic-to-macroscopic leap: counting invisible carriers in an imagined box, then folding the count into the current relation — two unfamiliar ideas in one derivation.
**Simple explanation:** Each carrier feels q**v** × **B**; a piece of wire of volume AL holds nAL carriers; multiplying gives the total, and the current relation I = nqAv collapses everything into F = I**L** × **B**.
**Intuitive analogy:** Rain on a windshield: each drop stings a little; the total push on the glass is (force per drop) × (number of drops in the glass's area). The wire is the windshield; the carriers are the drops.
**Step-by-step:** (1) Take a straight segment, length L, cross-section A → volume AL. (2) Carriers inside: nAL. (3) Each feels q**v** × **B**. (4) Total: F = (q**v** × **B**)nAL. (5) Substitute I = nqAv (v and L both lie along the wire, so v × B and L × B point the same way). (6) F = I**L** × **B**, magnitude BIL sin θ.
**Mini example:** 0.50 m, 2.0 A, 0.10 T, perpendicular → F = 0.10 N.
**Misconception to avoid:** "The wire is neutral, so there's no force" — neutrality cancels the *net charge*, not the *motion* of the carriers; the magnetic force selects the moving charges.
**Difficulty: HARD** → video provided

### Difficult Concept: No Magnetic Monopoles
**Why students struggle:** Electricity is built from isolated charges, so students assume magnetism has isolated poles too.
**Simple explanation:** Every magnetic object, however divided, always shows both a north and a south pole; a single pole has never been isolated.
**Intuitive analogy:** A coin: cut it as finely as you like, every piece still has a head side and a tail side.
**Step-by-step:** (1) State the fact: every magnet has N and S. (2) Cut it: each piece has N and S. (3) Cut again: same. (4) Conclusion: poles cannot be separated — no monopole. (The source states the fact; a deeper explanation of *why* is [SOURCE DOES NOT SPECIFY].)
**Mini example:** Snap a magnetized needle in two → two complete compass needles, not a "north needle" and a "south needle."
**Misconception to avoid:** "Cutting a magnet separates the poles."
**Difficulty: EASY**

---

# 10. VIDEO LESSON PLANS

---

**VIDEO 1**

**VIDEO TITLE:** "The Sideways Force: Mastering the Right-Hand Rule"
**TARGET CONCEPT:** Direction and magnitude of the magnetic force F = qv × B
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Determine both magnitude and direction of the magnetic force on any moving charge, including negative charges.
**HOOK:** Old TVs steered electrons in flight with pure magnetism — never touching them. The surprise: the push is never forward, never along the field — always sideways.
**EXPLANATION:** (1) Magnitude F = |q|vB sin θ; zero when v ∥ B, max when ⊥. (2) Direction perpendicular to both v and B (cross product). (3) Right-hand rule: fingers along v, curl toward B, thumb = F for positive charge. (4) Negative charge → flip. (5) Page notation ⊙ / ⊗. (6) Worked example from the lecture.
**VISUALS:** 3-D arrows for v and B with a highlighted perpendicular force arrow; an animated right hand performing the rule; a "flip the arrow" animation when the charge sign changes; screen symbols ⊙ (out of page) and ⊗ (into page); the TV example as an electron beam curving to the screen.
**EXAMPLE:** Electron, v = 8.0 × 10⁶ m/s, B = 0.025 T at 60°: F = 2.8 × 10⁻¹⁴ N; direction by RHR, then reversed for the electron.
**COMMON MISTAKE:** Forgetting to flip for negative charges; using the angle between v and the surface instead of v and B.
**CHECK FOR UNDERSTANDING:** "A proton moves north; B points east. Which way is the force?"
**FINAL TAKEAWAY:** Magnetic force = cross product: perpendicular to both v and B, proportional to sin θ, reversed for negative charges.

---

**VIDEO 2**

**VIDEO TITLE:** "From One Charge to a Whole Wire: Where F = BIL Comes From"
**TARGET CONCEPT:** Derivation of the force on a current-carrying conductor from the single-charge law
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Reproduce and explain the derivation F = (qv × B)nAL → F = IL × B, and apply F = BIL sin θ.
**HOOK:** Inside every electric motor, a plain copper wire jumps in a magnetic field. But magnetic forces act on *moving charges* — and a wire is just metal sitting still. The resolution: a current is trillions of charges in motion, and we can *count* them.
**EXPLANATION:** (1) One carrier feels q**v** × **B**. (2) A segment of length L and cross-section A has volume AL → nAL carriers. (3) Total force = (qv × B) · nAL. (4) The current relation I = nqAv. (5) Since v and L are both along the wire, the scalars regroup → F = I**L** × **B**, magnitude BIL sin θ. (6) Worked numbers.
**VISUALS:** A wire drawn as a transparent tube with drifting carrier dots; a "counting box" of volume AL snapping into place, labeled N = nAL; each dot receiving a tiny force arrow; the arrows merging into one big arrow; the swarm fading into a single current arrow I along L; the regrouping shown algebraically step by step.
**EXAMPLE:** 0.50 m wire, 2.0 A, 0.10 T perpendicular → F = 0.10 N; tilted to 60° → × sin 60° ≈ 0.087 N; parallel to B → zero.
**COMMON MISTAKE:** Measuring θ between the wire and the normal/page instead of between the wire and B; treating L as a directionless length.
**CHECK FOR UNDERSTANDING:** "Double the current and halve the length — what happens to the force? And if the wire lies parallel to B?"
**FINAL TAKEAWAY:** A wire is a river of charges; count the carriers (nAL), fold in I = nqAv, and the single-charge law becomes F = BIL sin θ.

---

# 11. VIDEO SCRIPTS

---

## SCRIPT 1 — "The Sideways Force: Mastering the Right-Hand Rule"

**[0:00–0:30] Hook**
Old television sets did something remarkable: they fired electrons at the screen and steered them in flight — never touching them, using nothing but magnetic fields. Here's the strange part: the field never pushes the electrons *forward*, and never *along* the field. It pushes them sideways. Today you'll learn to predict that sideways push in any situation — in under a minute.

**[0:30–2:00] Concept introduction**
The rule is one vector equation: the magnetic force equals q times v cross B — charge times velocity cross magnetic field. Its magnitude is |q|, times v, times B, times the sine of the angle theta *between v and B*.

Three facts fall straight out of that. First: if the velocity is parallel to the field — theta zero or one-eighty — the sine vanishes, and the force is zero. Moving *along* the field? No push at all. Second: maximum force, |q|vB, when velocity and field are perpendicular. Third — and this is the one that trips everyone: the force is perpendicular to *both* v and B. It's a sideways force. Gravity pulls along g. Electric forces pull along the field. Magnetism doesn't. It's the cross product.

**[2:00–4:00] Visual explanation**
To find the direction, we use the right hand. Point your fingers along the velocity, v. Now curl them toward the magnetic field, B. Your thumb points along the force — for a *positive* charge.

Two quick tools. On paper, a dot in a circle means the field points out of the page toward you; a cross means it points into the page, away from you. Let's try one: velocity points right; the field points into the page. Fingers right… curl into the page… thumb points *up*. Force is up — for a positive charge.

Now, the electron. Same velocity, same field — electrons are *negative*. The law has q in it, and negative q flips the whole answer. So for the electron, the force points *down*. Every magnetic-force problem is two steps: do the right-hand rule for a positive charge, then flip if your charge is negative.

**[4:00–6:00] Worked example**
From the lecture: an electron in an old TV tube moves at 8.0 times ten to the sixth meters per second along the x-axis. Coils create a field of 0.025 tesla, at 60 degrees to the x-axis, in the x-y plane. Magnitude first: F = |q| v B sine theta — 1.6 times ten to the minus nineteen, times 8 times ten to the sixth, times 0.025, times sine of 60. Multiply it out: 2.8 times ten to the minus fourteen newtons. Tiny to us — enormous to an electron. Direction: right-hand rule with v along x and B at 60 degrees in the plane… and then flip it, because it's an electron.

**[6:00–7:00] Common mistake**
Four classic errors. One: doing the right hand with B first and v second — order matters in a cross product; it's q v cross B, velocity first. Two: forgetting the flip for negative charges — this alone fails half the exam versions. Three: using the wrong angle — theta is between v and B, not between v and the surface or the normal to anything. Four: expecting the force along the field. Never. Perpendicular to both.

**[7:00–8:00] Quick student challenge**
Try this: a proton moves due north. The magnetic field points due east. Which way does the force push? Right hand: fingers point north, curl toward the east… thumb points *down*, toward the ground. Now the same situation, but with an electron. Flip it: the force points *up*, away from the ground. If you got both, you own this rule.

**[8:00–8:30] Final recap**
The magnetic force: F = |q| v B sine theta. Perpendicular to both velocity and field. Zero when they're parallel. Right-hand rule: fingers along v, curl to B, thumb is F — and always flip for negative charges. Sideways, every time.

---

## SCRIPT 2 — "From One Charge to a Whole Wire: Where F = BIL Comes From"

**[0:00–0:30] Hook**
Inside every electric motor, a plain copper wire jumps when you switch on the current. But wait — magnetic forces act on *moving charges*. A wire is just… metal, sitting still. How does motionless metal feel a magnetic force? The answer: a current isn't still at all. It's trillions of charges marching in lockstep. And today we're going to *count* them.

**[0:30–2:00] Concept introduction**
Start with what we know: one charge moving with velocity v through a field B feels the force q times v cross B. That's Lecture 8's core law. Now zoom inside the wire. It's packed with mobile charge carriers — electrons — drifting along the wire with some speed v. Each one of them individually feels q v cross B.

So the total force on the wire is just that single-carrier force multiplied by *how many carriers are in the segment*. And here's the counting trick: imagine a box inside the wire — a straight segment of length L, with cross-sectional area A. The box's volume is A times L. If the carrier density is n — carriers per cubic meter — then the number of carriers in the box is n times A times L. Total force: q v cross B, times nAL. Simple counting.

**[2:00–4:00] Visual explanation**
Watch the wire on screen: a transparent tube, and the blue dots drifting through it — that's the current, seen from the inside. Now snap the counting box around a length L of the tube. Every dot inside the box — that's nAL of them — gets a tiny force arrow. All the little arrows add up to one big arrow: the total push on the wire.

Now the elegant part. Look at what we have: n, A, L, q, v — a swarm of microscopic numbers. Physics already has a name for part of this swarm: the *current*. Charge flowing past a point per second equals the carrier density times the charge times the drift speed times the area: I = n q A v. That's the bridge between the microscopic and the everyday.

Substitute it in. The n, the A, the q, the v — they regroup. And since the drift velocity v points *along the wire*, and L points along the wire too, v cross B and L cross B point the same way. Everything collapses into one clean statement: **F = I L cross B**. The current times a vector L pointing along the current, crossed with the field. Magnitude: B times I times L times sine theta — and theta is the angle between the *wire* and the *field*. A one-line law, hiding an army of charges.

**[4:00–6:00] Worked example**
Numbers. A straight wire, half a meter long, carrying 2 amperes, sitting perpendicular to a 0.10-tesla field. Theta is ninety degrees, sine theta is one. F = B I L: 0.10 times 2.0 times 0.50 — one tenth of a newton. Small, but real — scale up the current and the length, and this is exactly the force that spins a motor.

Now tilt the wire to sixty degrees with the field: multiply by sine sixty, about 0.87 — the force drops to roughly 0.087 newtons. And lay the wire *parallel* to the field: sine of zero — the force vanishes completely. Same wire, same current, same field — only the angle changed. That's the sin theta factor doing its job, exactly as it did for single charges.

**[6:00–7:00] Common mistake**
Watch for these. One: measuring theta between the wire and the *normal* to something, or between the wire and the page. Theta is between the wire — the current direction — and B. Draw both lines; read the angle between *them*. Two: treating L as just a number. L is a vector along the current; if a problem asks for *direction*, you need L pointing the way the current flows before you use the right-hand rule. Three: plugging in B in gauss. Convert to tesla first.

**[7:00–8:00] Quick student challenge**
Two quick ones. First: I double the current and halve the length of the wire. What happens to the force? … B, I, and L multiply — two times a half is one — the force is *unchanged*. Second: the wire lies exactly along the field lines. What's the force? … Zero — the current and the field are parallel, sine theta is zero. Bonus: which single change would double the force on a perpendicular wire? Double the current, double the length, or double the field — any one of them.

**[8:00–8:30] Final recap**
A current-carrying wire is a river of charges. Each charge feels q v cross B. Count them — n A L in a segment. Fold in the current relation I = n q A v. And the microscopic swarm collapses into the macroscopic law: F = B I L sine theta, with theta between the wire and the field. One law, two views — single charge or whole wire.

---

# 12. PRACTICE QUESTIONS

## LEVEL 1 — UNDERSTAND

1. State the two pole-interaction rules for magnets, and state how the pole force depends on distance.
2. What happens when a bar magnet is cut in half — and why does this make an isolated magnetic pole impossible?
3. How is the direction of B at a point defined, and with what instrument?
4. What surrounds any *moving* electric charge, in addition to its electric field?
5. When is the magnetic force on a moving charge exactly zero?
6. Under what condition is the force maximum, and what is that maximum value?
7. A positive and a negative charge move identically in the same field. Compare the magnitudes and directions of their forces.
8. Express the tesla in terms of the newton and the ampere, and give its relation to the gauss.
9. In uniform circular motion of a charged particle, what supplies the centripetal force, and what does it change about the particle's velocity?
10. In the microscopic picture of a current-carrying wire, what does n represent, and how many carriers sit in a segment of volume AL?

## LEVEL 2 — APPLY

11. A proton moves at 2.0 × 10⁵ m/s perpendicular to a 0.50 T field. Find the magnetic force.
12. A charge of +2.0 μC moves at 3.0 × 10⁴ m/s in a 0.040 T field, with its velocity at 30° to the field. Find the force.
13. A proton (m = 1.67 × 10⁻²⁷ kg) moves at 3.0 × 10⁶ m/s perpendicular to a 0.20 T field. Find the radius of its circular path.
14. A 0.50 m straight wire carries 2.0 A perpendicular to a 0.10 T field. Find the force on it.
15. A 1.5 m wire carrying 5.0 A sits at 60° to a 0.30 T field. Find the force on it.
16. An electron moving at 6.0 × 10⁶ m/s perpendicular to a field experiences a force of 4.8 × 10⁻¹⁴ N. Find B.
17. For the proton of Worked Example 2 (v = 4.7 × 10⁶ m/s, r = 0.14 m), compute the angular speed ω.
18. Convert: (a) 0.005 T to gauss; (b) 0.50 G to tesla.
19. An electron moves at 5.0 × 10⁶ m/s directly *along* a 0.20 T field. What force does it feel? Justify.
20. A proton circles in a 0.35 T field with radius 0.28 m (double the radius of Worked Example 2). Find its speed, and check the result against Example 2.

## LEVEL 3 — TRANSFER

21. Two particles carry equal charge magnitudes and move at the same speed in the same uniform field, both perpendicular to B. Particle A has four times the mass of particle B. Compare their orbit radii, and state the proportionality involved.
22. Starting from r = mv/(|q|B) and ω = v/r, derive an expression for ω that contains no v. Then answer: if the proton of Worked Example 2 doubles its speed, what happens to its radius and to its angular speed?
23. An electron moves along +x; the field points along +y. Determine the direction of the magnetic force. Repeat for a proton.
24. A 1.0 m wire carrying 4.0 A in a 0.20 T field experiences a force of 0.60 N. Find the angle between the wire and the field.
25. Design task: a proton moving at 4.7 × 10⁶ m/s must circle with radius 0.50 m. What magnetic field is required?
26. A horizontal wire carries current due east in a region where the magnetic field points due north (both horizontal). Find the direction of the force on the wire.

**INSTRUCTOR ANSWER KEY (not for student display)**

1. Like poles repel (N–N, S–S); unlike attract (N–S); force ∝ 1/r². [EASY]
2. Two complete magnets, each with N and S — every fragment remains a dipole; hence no monopole can be isolated. [EASY]
3. The direction in which the north pole of a compass needle points at that location; measured with a compass. [EASY]
4. A magnetic field. [EASY]
5. When the velocity is parallel (or antiparallel) to B: θ = 0° or 180° → sin θ = 0. [EASY]
6. When v ⊥ B (θ = 90°): F_max = |q|vB. [EASY]
7. Equal magnitudes (same |q|, v, B); exactly opposite directions. [EASY]
8. 1 T = 1 N/(A·m); 1 T = 10⁴ G. [EASY]
9. The magnetic force |q|vB supplies the centripetal force; it changes the *direction* of the velocity, not its magnitude. [EASY]
10. n = number of mobile charge carriers per unit volume; carriers in volume AL = nAL. [EASY]
11. F = (1.6 × 10⁻¹⁹)(2.0 × 10⁵)(0.50) = 1.6 × 10⁻¹⁴ N. [EASY]
12. F = (2.0 × 10⁻⁶)(3.0 × 10⁴)(0.040) sin 30° = 1.2 × 10⁻³ N. [MEDIUM — sin θ with the correct angle]
13. r = (1.67 × 10⁻²⁷ × 3.0 × 10⁶)/(1.6 × 10⁻¹⁹ × 0.20) = 0.157 m. [MEDIUM]
14. F = 0.10 × 2.0 × 0.50 = 0.10 N. [EASY]
15. F = 0.30 × 5.0 × 1.5 × sin 60° = 1.95 N ≈ 1.9 N. [MEDIUM]
16. B = F/(|q|v) = 4.8 × 10⁻¹⁴/(1.6 × 10⁻¹⁹ × 6.0 × 10⁶) = 0.050 T. [MEDIUM — inverted formula]
17. ω = v/r = 4.7 × 10⁶/0.14 ≈ 3.4 × 10⁷ rad/s. [EASY]
18. (a) 0.005 T = 50 G; (b) 0.50 G = 5.0 × 10⁻⁵ T. [EASY]
19. Zero — v is parallel to B, so sin θ = 0 regardless of the speed or field strength. [EASY — zero-force recognition]
20. v = |q|rB/m = (1.6 × 10⁻¹⁹)(0.28)(0.35)/(1.67 × 10⁻²⁷) ≈ 9.4 × 10⁶ m/s — exactly double Example 2's answer, since r ∝ v at fixed B. [MEDIUM — consistency reasoning]
21. r_A = 4 r_B; r ∝ mv with |q|, v, B fixed. [MEDIUM]
22. ω = v/r = v/(mv/|q|B) = |q|B/m — independent of v. Doubling v: r doubles, ω unchanged. [HARD — algebraic elimination]
23. v × B = x̂ × ŷ = +ẑ → force along +z (out of the ground) for the *proton*; the electron's force is along −z. [MEDIUM — RHR + sign flip]
24. sin θ = F/(BIL) = 0.60/(0.20 × 4.0 × 1.0) = 0.75 → θ ≈ 48.6°. [MEDIUM — inverted wire formula]
25. B = mv/(|q|r) = (1.67 × 10⁻²⁷ × 4.7 × 10⁶)/(1.6 × 10⁻¹⁹ × 0.50) ≈ 0.098 T. [MEDIUM — design inversion]
26. F = I**L** × **B**: east × north = up → the force is vertically **upward**. [MEDIUM — 3-D direction reasoning]

---

# 13. TRANSFER QUESTIONS

*New-context problems carrying Lecture 8 concepts into unfamiliar settings.*

**T1 — Mass-spectrometer reasoning (from the source's r-formula only):** Two singly charged particles enter the same uniform field at the same speed, both perpendicular to B. One traces a circle of twice the radius of the other. What can you conclude about their masses?
→ *Key:* r ∝ m (same |q|, v, B) → the larger circle belongs to the particle of twice the mass. [EASY-MEDIUM]

**T2 — TV steering sensitivity:** In Worked Example 1's TV tube, the coil field's angle to the electron's velocity is reduced from 60° to 30° (same magnitude 0.025 T, same speed). Find the new force, using the proportionality F ∝ sin θ.
→ *Key:* F' = 2.8 × 10⁻¹⁴ × (sin 30°/sin 60°) = 2.8 × 10⁻¹⁴ × 0.577 ≈ 1.6 × 10⁻¹⁴ N. [MEDIUM]

**T3 — Two-wire reasoning:** Two identical straight wires lie side by side in a uniform field **B**, carrying equal currents in *opposite* directions, both perpendicular to B. Compare the forces on the wires (magnitude and direction).
→ *Key:* Equal magnitudes (same B, I, L, θ); opposite directions — reversing **L** reverses **I L × B**. [MEDIUM — vector direction transfer]

**T4 — Cyclotron-style parameter shift:** For a fixed-speed proton in a uniform field, the field strength B is doubled. What happens to the orbit radius r and to the angular speed ω (use the derived relation ω = |q|B/m)?
→ *Key:* r = mv/(|q|B) halves; ω = |q|B/m doubles. [MEDIUM-HARD — two-formula synthesis]

**T5 — Page-notation geometry:** A field **B** points straight *into* the page (⊗). A proton moves to the *right* across the page. Determine the force direction. Then state the electron's force for the same motion.
→ *Key:* v × B = x̂ × (−ẑ) = +ŷ → force **up the page** for the proton; **down the page** for the electron. [MEDIUM — 3-D notation]

**T6 — Diagnostic reasoning:** A current-carrying wire sits in a uniform magnetic field and feels *zero* force. What can you conclude about its orientation (assuming I ≠ 0)? What would you check next?
→ *Key:* The wire (current direction) must be parallel or antiparallel to B (θ = 0° or 180°); then check whether I = 0 or the field is zero — but under the stated assumption, orientation is the conclusion. [MEDIUM — inverse reasoning]

---

# 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All Lecture 8 topics present: poles (rules, 1/r², naming via Earth, no monopoles, cutting), fields (sources, compass definition, field lines N→S, Earth's field), force on moving charges (all proportionality facts, max/min conditions, sign reversal), RHR 1 or 2, units (tesla definitions, gauss), notation figures, circular motion (r, ω), wire force (full derivation with nAL and I = nqAv). |
| Mathematical formulas correct | ✅ | All 11 formulas match the source; both source examples reproduce exactly (2.8 × 10⁻¹⁴ N; 4.7 × 10⁶ m/s); all new practice computations verified. |
| Technical terminology preserved | ✅ | Magnetic pole, monopole, magnetic field, tesla, gauss, centripetal acceleration, right-hand rule 1 or 2, mobile charge carriers, emf-free notation kept per source. |
| Explanations in original language | ✅ | No source paragraphs reproduced; only formulas and short standard definitions shared. |
| Understandable to a first-year student | ✅ | Layered structure; analogies flagged as pedagogical; 3-D reasoning scaffolded via notation section. |
| Difficult concepts explicitly identified | ✅ | 5 concepts with full analysis and difficulty ratings in §9. |
| Common misconceptions identified | ✅ | 10 in §7; per-concept misconceptions in §9; in-video mistakes in §10–11. |
| Examples actually teach | ✅ | Both source examples retained with full reasoning; 2 clearly-flagged pedagogical examples added (wire magnitude, direction workout) to cover skills the source's examples don't exercise. |
| Practice progresses understand → apply → transfer | ✅ | L1 (10 conceptual) → L2 (10 computational) → L3 (6 synthesis) + 6 transfer tasks, all with verified keys. |
| No unsupported claims added | ✅ | Flagged items: the source's "Notation notes" and "Earth's Magnetic Field" are figures whose details were not extracted — standard conventions presented as clearly-marked instructor notes; the source names "Right-Hand rule 1 or 2" without specifying a variant — [SOURCE DOES NOT SPECIFY]; ω = \|q\|B/m is presented as a *derived* consequence of the source's own formulas; constant-speed statement follows from the source's "uniform circular motion / centripetal acceleration" framing. |
| No large verbatim reproduction | ✅ | Only formulas and short definitions overlap with the source. |
| Suitable for direct web integration | ✅ | Clean Markdown; student-facing self-check separated from instructor keys. |

**Source errata handled transparently (meaning preserved, typos not propagated):**
- Worked Example 2 prints the proton charge as 1.6 × 10⁻¹⁶ C; the printed answer (4.7 × 10⁶ m/s) requires 1.6 × 10⁻¹⁹ C, which is used throughout.
- The garbled extraction of the vector equations (𝑭𝑩 = 𝒒?⃗? × ?⃗⃗? and 𝑭𝑩 = 𝑰?⃗? × ?⃗⃗?) is restored as **F**_B = q**v** × **B** and **F**_B = I**L** × **B**, exactly as the source's variable lists and magnitude formulas confirm.
- The source's "Notation notes" section contains figures only; the ⊙/⊗ convention is presented as a standard instructor note, flagged as such.


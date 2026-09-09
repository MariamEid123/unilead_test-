# ARETE — LECTURE 9 (FULL TRANSFORMATION)

---

# 1. SOURCE ANALYSIS

| Item | Value |
|---|---|
| Course | PHY 211 — Physics (Electricity, Magnetism & Optics) |
| Lecture | **Lecture 9** — Chapter 8 |
| Title | Sources of the Magnetic Fields |
| Instructor | Dr. Ashraf Mousa Abdelwahed — AIU, Fall 2024 |

**Main topics:**
1. The magnetic field produced by a current — the Biot–Savart law
2. Applications: field of a thin straight wire
3. Applications: field of a current loop / thin coil
4. Applications: field of a solenoid
5. Forces between currents (figures only)
6. Lenz's law

**Subtopics:** the experiments of Biot and Savart; the four experimental observations on dB; vector and magnitude forms of the law; μ₀ (magnetic permeability of free space); B ∝ I and B ∝ 1/r for a straight wire; loop center field; N-turn coil field; field-line resemblance of a loop to a short bar magnet; solenoid as a helix; uniform interior field; n = N/L; wire length d = N × 2πr; force between parallel wires and between loops (figures only); induced-current conditions and direction rule (Lenz).

**Learning objectives (from content):** state and interpret the Biot–Savart law; compute fields for wire, loop/coil, and solenoid; design solenoid windings; determine induced-current directions.

**Important definitions:** magnetic permeability of free space (μ₀); turns per unit length (n); solenoid; magnetic flux (used by the source, formally defined elsewhere — [SOURCE DOES NOT SPECIFY a definition in this lecture]); induced current.

**Examples in source:** 1 (solenoid design for a bacteria-magnetism experiment).

**Procedures:** field evaluation (choose geometry → select formula → substitute); solenoid design (target B → N → wire length via d = N·2πr); Lenz direction determination (change? → which way? → oppose → right-hand curl).

**Common misconceptions in source material:** treating the whole wire as one source; N confused with n; induced field "opposing the field" rather than the change.

**Difficult concepts:** differential vector contributions; sin θ and 1/r² factors; n vs N; wire length vs solenoid length; Lenz's two-condition logic.

**Prerequisites:** Lecture 8 (magnetic field B, tesla, cross products, right-hand rule, F = IL × B); Lecture 7 (current I).

**Concept map:**

```
Sources of the Magnetic Field (Ch. 8)
├── Biot–Savart law
│   ├── Four observations: ⟂ to ds & r̂ ; ∝ 1/r² ; ∝ I, ds ; ∝ sin θ
│   ├── dB = (μ₀/4π)(I ds × r̂)/r² ; μ₀ = 4π×10⁻⁷ T·m/A
│   └── Total B = sum of all element contributions
├── Applications (the law collapses for symmetric shapes)
│   ├── Straight wire → B = μ₀I/2πr (B ∝ I, ∝ 1/r)
│   ├── Loop center → B = μ₀I/2R ; N-turn coil → μ₀NI/2R
│   │   └── lines resemble a SHORT bar magnet
│   └── Solenoid (helix) → B = μ₀nI, n = N/L
│       ├── interior uniform, parallel to axis
│       ├── lines resemble a LONG bar magnet
│       └── winding wire length d = N × 2πr
├── Forces between currents (figures only) → [SOURCE DOES NOT SPECIFY]
└── Lenz's law
    └── Induced current ⇔ changing flux ; direction opposes the CHANGE
```

**Dependencies:** directly extends Lecture 8 (field concept, units, cross products); the flagged pedagogical note on parallel wires combines this lecture's B = μ₀I/2πr with Lecture 8's F = IL × B.

---

# 2. COURSE / MODULE / LESSON METADATA

| Field | Value |
|---|---|
| **COURSE** | PHY 211 — Physics II |
| **MODULE** | Sources of the Magnetic Field (Chapter 8) |
| **LESSON** | Lecture 9 — Sources of the Magnetic Fields |
| **TOPICS** | Biot–Savart law; fields of wire, loop/coil, solenoid; solenoid design; forces between currents (qualitative); Lenz's law |
| **PREREQUISITES** | Lecture 8 (B, tesla, cross products, RHR, F = IL×B); Lecture 7 (current) |
| **COMPETENCIES** | State the four Biot–Savart observations and the law; compute B for a straight wire, loop/coil center, and solenoid interior; design a solenoid (B → N → wire length); describe loop/solenoid field-line patterns; determine induced-current directions with Lenz's law |
| **DIFFICULTY** | Overall: HARD · Field computations: MEDIUM · Biot–Savart conceptual structure: VERY HARD · Lenz direction logic: HARD |
| **ESTIMATED STUDY TIME** | ~3 hours (lesson 60 min · worked examples 25 min · practice 45 min · videos 17 min · self-check & transfer 30 min) |

**ARETE flow placement:**
- **LEARN:** the four observations; the three field formulas; Lenz's statement.
- **PRACTICE:** direct field computations.
- **PROVE:** solenoid design problems (two-step: N then wire length); Lenz direction determinations.
- **REMEDIATE/RETRY targets:** N vs. n; sin θ; "opposes the change, not the field."
- **TRANSFER:** inverted design problems (given wire, find turns); Lenz in new geometries.
- **MASTER:** full design chains (target field → turns → wire) and multi-step Lenz reasoning.

---

# 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Describe the experiments of Biot and Savart and state what their law computes.
2. State the four experimental observations underlying the Biot–Savart law.
3. Write the law in vector and magnitude form, with the value and units of μ₀.
4. Compute the field of a long straight wire and describe its dependence on I and r.
5. Compute the field at the center of a single loop and of an N-turn coil.
6. Compute the interior field of a solenoid using n = N/L, and the wire length d = N × 2πr needed to wind one.
7. Describe the field-line patterns of loops and solenoids and their resemblance to bar magnets, and the uniformity of the solenoid's interior field.
8. State Lenz's law and determine the direction of an induced current for a changing flux.

---

# 4. WEB-READY LESSON

# Lecture 9 — Sources of the Magnetic Fields

## Prerequisites
The student should already understand:
- The magnetic field B, its units (tesla), and the compass definition (Lecture 8).
- Vector cross products and the right-hand rule.
- Electric current I (Lecture 7).
- The force law F = I**L** × **B** (Lecture 8).

---

### 1. The Biot–Savart Law

**Core Idea**
Biot and Savart studied the force exerted by an electric current on a nearby magnet and arrived at a mathematical expression giving the magnetic field at any point in space due to a current — built from the contributions of tiny pieces of the wire.

**Explanation**
The law is based on four experimental observations about the field **dB** at a point P, produced by a length element **ds** of a wire carrying a steady current I (ds points along the current):

1. **dB is perpendicular** both to ds and to the unit vector r̂ directed from ds toward P.
2. The magnitude of **dB** is **inversely proportional to r²**, where r is the distance from ds to P.
3. The magnitude of **dB** is **proportional to the current I** and to the magnitude ds of the length element.
4. The magnitude of **dB** is **proportional to sin θ**, where θ is the angle between ds and r̂.

These observations are summarized in the **Biot–Savart law**:

**dB = (μ₀/4π) (I ds × r̂)/r² → magnitude: dB = (μ₀/4π) (I ds sin θ)/r²**

where **μ₀ = 4π × 10⁻⁷ T·m/A** is the *magnetic permeability of free space*. The total field at P is the sum of all such contributions along the wire.

Two immediate readings: an element pointing *directly at* P has θ = 0 ⇒ contributes nothing; an element "broadside" to P (θ = 90°) contributes maximally.

**Example (conceptual)**
Two identical elements sit at the same distance from P, one pointing straight at P, one perpendicular to the line of sight: the first contributes zero, the second the maximum — the sin θ factor at work.

**Key Point**
Slice the wire into elements; each contributes ∝ I·ds·sin θ / r², perpendicular to the element and to the line of sight; add them all to get B.

### 2. The Field of a Long Straight Wire

**Core Idea**
Applying Biot–Savart to a thin straight current-carrying wire gives the field at distance r from it:

**B = μ₀I/(2πr)**

**Explanation**
The two proportionality facts from the source: **B ∝ I** (double the current, double the field) and **B ∝ 1/r** (double the distance, halve the field). Note that the field is *not* constant around a wire — it fades with distance.

**Example**
A 10 A current: at r = 0.10 m, B = (4π × 10⁻⁷ × 10)/(2π × 0.10) = 2.0 × 10⁻⁵ T = 0.20 gauss — tying this lecture back to Lecture 8's unit conversion. (Worked Example 2.)

**Key Point**
Wire: B = μ₀I/(2πr). Memorize the two proportionalities — most exam questions test them without full computation.

### 3. The Field at the Center of a Loop and a Coil

**Core Idea**
At the center of a circular current loop of radius R, every element contributes at distance R and at the best angle — the result collapses to **B = μ₀I/(2R)**. Stack N turns into a thin coil and each turn adds its field: **B = μ₀NI/(2R)**.

**Explanation**
The field-line pattern surrounding a current loop is **similar to the field lines surrounding a short bar magnet** — a loop behaves like a small magnet, an idea that becomes essential when reading solenoid field patterns.

**Example**
A single loop of R = 0.050 m carrying 2.0 A: B = (4π × 10⁻⁷ × 2)/(0.10) = 2.5 × 10⁻⁵ T at the center. Wind 100 turns instead: the field multiplies by 100 → 2.5 × 10⁻³ T. (Worked Example 3.)

**Key Point**
Loop center: B = μ₀I/(2R); N turns → ×N. Here R is the *loop's own radius* — not a distance from a wire.

### 4. The Solenoid

**Core Idea**
A solenoid is a long wire wound in the form of a helix. Inside, the contributions of all turns align along the axis, producing a **uniform** field: **B = μ₀nI**, where **n = N/L** is the number of turns per unit length.

**Explanation**
Three facts from the source:
- The interior field has a **constant value and is directed parallel to the axis** — uniform.
- The field lines of a solenoid resemble those of a **long bar magnet**.
- Construction arithmetic: winding N turns around a cylinder of radius r uses a wire of length

**d = N × 2πr**

since each turn wraps once around the circumference.

**Example**
The source's design problem: a solenoid must produce B = 0.002 T inside, is 0.25 m long, carries 2.5 A, and has radius 2 cm → N = LB/(μ₀I) = 159 turns, requiring d = 159 × 2π(0.02) ≈ 20 m of wire. (Worked Example 1.)

**Key Point**
Solenoid: B = μ₀nI with **n = N/L (turns per meter)** — and for design problems, wire length = N × 2πr.

### 5. Forces Between Currents

**Core Idea**
Currents exert magnetic forces on one another — introduced in the source with figures for (1) two parallel current-carrying wires and (2) two current loops.

**Explanation**
The source presents these two topics through figures only; their formulas and details are [SOURCE DOES NOT SPECIFY].

*Optional pedagogical note (beyond the source, built from Lecture 8 + this lecture):* two parallel wires carrying currents in the **same direction attract** each other; opposite directions **repel**. This follows directly from F = I**L** × **B** (Lecture 8) using the field of the other wire, B = μ₀I/2πr (this lecture).

**Key Point**
Both building blocks — the field of a wire and the force on a current-carrying wire — are already in your toolkit; the quantitative details of the force-between-currents formulas are not part of this lecture's source.

### 6. Lenz's Law

**Core Idea**
A closed conducting loop carries an induced current **if and only if** the magnetic flux through it is *changing* — and the induced current flows so that its own magnetic field **opposes the change** in the flux.

**Explanation (the source's statement, preserved)**
*"There is an induced current in a closed, conducting loop if and only if the magnetic flux through the loop is changing. The direction of the induced current is such that the induced magnetic field opposes the change in the flux."*

Two conditions are packed into that sentence:
1. **Change is mandatory** — a strong but *steady* flux induces nothing.
2. The opposition targets the **change**, not the field: if flux is *decreasing*, the induced field actually *supports* the original field, propping it up.

The source uses "magnetic flux" without defining it in this lecture [SOURCE DOES NOT SPECIFY a formal definition here]; an informal working gloss: *the amount of magnetic field passing through the loop*.

**Example (pedagogical illustration of the law)**
Push a bar magnet's north pole toward a loop: flux through the loop changes (increases) → current is induced, directed so the loop's near face becomes a **north** pole — repelling the approaching magnet. Pull it away: the flux decreases → the current reverses, the near face becomes **south** — attracting the retreating magnet. Motion is always resisted. (Worked Example 5.)

**Key Point**
No change → no current. The induced current always opposes the **change** in flux — not the field itself.

---

## Key Takeaways
1. Biot–Savart builds fields from tiny current elements: dB = (μ₀/4π) I ds sin θ / r², perpendicular to ds and r̂; total B = the sum over the whole wire.
2. μ₀ = 4π × 10⁻⁷ T·m/A (magnetic permeability of free space).
3. Straight wire: B = μ₀I/(2πr) — doubles with current, halves with distance.
4. Loop center: B = μ₀I/(2R); an N-turn thin coil multiplies it by N; a loop's field lines look like a short bar magnet's.
5. Solenoid interior: B = μ₀nI with n = N/L — uniform and parallel to the axis; field lines like a long bar magnet.
6. Winding a solenoid of N turns on radius r takes d = N × 2πr of wire.
7. Parallel same-direction currents attract each other (pedagogical note; formulas beyond source).
8. Lenz's law: induced current ⇔ changing flux; its direction opposes the **change** — supporting the original field when the flux decreases.

## Self-Check (attempt before looking at answers)
1. What experiments led to the Biot–Savart law, and what does the law let you compute?
2. List the four experimental observations behind the law, in your own words.
3. State the value and SI units of μ₀.
4. What is the direction of dB relative to ds and to r̂?
5. A wire element points directly at point P. What is its contribution to the field at P, and why?
6. For a long straight wire, state the two proportionalities of B.
7. At the center of a thin coil, what happens to B if the number of turns doubles (same I and R)?
8. What does n represent in B = μ₀nI? If a solenoid is stretched to twice its length (same N, same I), what happens to the interior field?
9. How much wire is needed to wind a solenoid of N turns on a cylinder of radius r?
10. A loop sits in a strong but perfectly steady magnetic field — is there an induced current? What changes when the field starts *decreasing*?

---

# 5. FORMULAS

| # | Formula | Variables | When it is used | Interpretation & assumptions |
|---|---|---|---|---|
| 1 | dB = (μ₀/4π)(I **ds** × r̂)/r² | **ds**: length element along current; r̂: unit vector from ds toward P; r: distance ds → P | Field contribution of one current element (direction) | Direction ⟂ to both ds and r̂ |
| 2 | dB = (μ₀/4π)(I ds sin θ)/r² | θ: angle between **ds** and r̂ | Contribution magnitude | θ = 0 → zero; θ = 90° → maximum; falls as 1/r² |
| 3 | μ₀ = 4π × 10⁻⁷ T·m/A | — | Constant in every formula | Magnetic permeability of free space |
| 4 | B = μ₀I/(2πr) | r: distance from the wire | Field of a long straight wire | B ∝ I, B ∝ 1/r |
| 5 | B = μ₀I/(2R) | R: the loop's own radius | Field at the center of a single loop | R is a property of the loop, not a distance from a wire |
| 6 | B = μ₀NI/(2R) | N: number of turns | Center of a thin coil | Each turn adds; N × the single-loop value |
| 7 | B = μ₀nI ; n = N/L | N: total turns; L: solenoid length | Interior of a long solenoid | Field uniform, parallel to axis; **n is turns per meter**, not the turn count |
| 8 | d = N × 2πr | d: wire length; r: solenoid radius | Winding/design problems | Each turn = one full circumference |

---

# 6. WORKED EXAMPLES

**WE 1 — Solenoid design (Source Example 1)**
A research student prepares a solenoid to study the effect of a magnetic field on a certain type of bacteria. Required interior field B = 0.002 T, solenoid length L = 0.25 m, current I = 2.5 A, radius r = 2 cm. Find the length of wire required.
1. Start from B = μ₀nI = μ₀(N/L)I and solve for N: N = LB/(μ₀I).
2. N = (0.25 × 0.002)/((4π × 10⁻⁷) × 2.5) = 5 × 10⁻⁴ / 3.14 × 10⁻⁶.
3. **N = 159 turns.**
4. Wire length: d = N × 2πr = 159 × 2π × 0.02 = 159 × 0.1257.
5. **d ≈ 20 m.**
Note the two-step structure: the field requirement fixes the *turn count*; the radius then fixes the *wire length* — two different roles.

**WE 2 — Field of a straight wire (pedagogical example — the source gives the formula without a numerical application)**
A long straight wire carries 10 A. Find B at 0.10 m, then at 0.20 m.
1. B = μ₀I/(2πr) = (4π × 10⁻⁷ × 10)/(2π × 0.10).
2. The π and one factor of 10⁻¹ cancel: **B = 2.0 × 10⁻⁵ T** (= 0.20 G).
3. At 0.20 m (double distance): B ∝ 1/r → **1.0 × 10⁻⁵ T** — halved, no recomputation needed.

**WE 3 — Loop and coil center (pedagogical example)**
A circular loop of R = 0.050 m carries 2.0 A. Find B at the center; then for a 100-turn coil of the same radius and current.
1. Single loop: B = μ₀I/(2R) = (4π × 10⁻⁷ × 2.0)/(0.10) = 8π × 10⁻⁶.
2. **B = 2.5 × 10⁻⁵ T.**
3. N = 100 turns: B = μ₀NI/(2R) = 100 × 2.5 × 10⁻⁵.
4. **B = 2.5 × 10⁻³ T.**
Note: no π appears in the loop formula — R is the loop's own radius, not a distance from a wire.

**WE 4 — Solenoid interior field (pedagogical example)**
A solenoid has 400 turns over a length of 0.20 m and carries 2.0 A. Find B inside.
1. n = N/L = 400/0.20 = **2000 turns/m**.
2. B = μ₀nI = 4π × 10⁻⁷ × 2000 × 2.0.
3. **B = 5.0 × 10⁻³ T** — uniform inside, parallel to the axis.

**WE 5 — Lenz's-law direction workout (pedagogical demonstration built on the source's statement of the law)**
A bar magnet's north pole moves toward a closed conducting loop, then away. Determine the induced current's effect each time.
1. *Approach:* flux through the loop (pointing away from the magnet) is **increasing** → a current is induced.
2. The induced field must **oppose the increase** → it points back toward the magnet.
3. By the right-hand curl, the current flows so the loop's near face is a **north pole** → the loop **repels** the approaching magnet.
4. *Retreat:* the flux is **decreasing** → the induced field flips to **support** the fading flux → near face becomes **south** → the loop **attracts** the retreating magnet.
5. Check against the law: in both cases the induced effect resists the *change* — never the magnet's mere presence.

---

# 7. COMMON MISTAKES

| # | What students usually do | Why it's wrong | How to avoid it |
|---|---|---|---|
| 1 | Treat the whole wire as a single source at one distance | Every piece of the wire is at a different distance and angle from the point; only the *sum* of element contributions gives B | Think "slice, contribute, sum" before touching any formula |
| 2 | Drop the sin θ factor in dB | An element pointing straight at P contributes nothing — sin θ encodes this | Ask "is this element broadside or head-on to the point?" |
| 3 | Use r instead of r² in the element contribution | The contribution falls off as inverse *square* distance | Attach "one over r squared" to every dB statement |
| 4 | Plug total turns N where n = N/L belongs (solenoid) | B = μ₀nI uses turns *per meter*; a long, loosely wound solenoid is weaker than a short, dense one | Convert to n (divide by L) *before* substituting |
| 5 | Confuse the loop formula (2R) with the wire formula (2πr) | In the loop formula R is the loop's own radius; in the wire formula r is the distance *from* the wire | Match formula to geometry first: circle-of-current → 2R; straight wire → 2πr |
| 6 | Use the solenoid's length L as the wire length | L is the solenoid's *axial* length; the wire wraps N circumferences: d = N × 2πr | Label the two lengths explicitly in every design problem |
| 7 | Assume B around a straight wire is constant | B ∝ 1/r — it fades with distance | Recite the two proportionalities for the wire |
| 8 | In Lenz problems, make the induced field oppose the *field* | The law targets the **change**: a decreasing flux is *supported*, not opposed, by the induced field | Always ask "increasing or decreasing?" before choosing the direction |
| 9 | Expect current from a strong static magnet inside a coil | No change in flux → no induced current, regardless of strength | "Change is mandatory" — check it first |
| 10 | Quote μ₀ wrong or with wrong units | μ₀ = 4π × 10⁻⁷ T·m/A exactly — errors cascade through every field formula | Memorize value *and* units together |

---

# 8. LECTURE SUMMARY

# Lecture Summary — Sources of the Magnetic Fields

## What You Need to Know
- The four experimental observations behind the Biot–Savart law and the law itself, in both forms, with μ₀.
- The three collapsed field formulas and when each applies: straight wire, loop/coil center, solenoid interior.
- Solenoid design arithmetic: turns from the field requirement, wire length from the turns.
- The field-line resemblances (loop ↔ short bar magnet; solenoid ↔ long bar magnet) and the solenoid's uniform interior field.
- Lenz's law: the two conditions and the direction rule.

## Key Definitions
- **Biot–Savart law** → the expression giving dB at a point due to a current element ds: (μ₀/4π) I ds sin θ / r².
- **Magnetic permeability of free space (μ₀)** → 4π × 10⁻⁷ T·m/A; the constant of the magnetic universe.
- **Solenoid** → a long wire wound in the form of a helix; produces a uniform interior field.
- **Turns per unit length (n = N/L)** → the winding density that sets the solenoid field.
- **Magnetic flux** → the amount of magnetic field passing through a loop (informal gloss; formally defined elsewhere — [SOURCE DOES NOT SPECIFY in this lecture]).
- **Induced current** → the current driven in a closed conducting loop by a *changing* flux.

## Key Formulas
- dB = (μ₀/4π) I ds sin θ / r² → element contribution (vector form: ds × r̂).
- B = μ₀I/(2πr) → long straight wire.
- B = μ₀I/(2R); B = μ₀NI/(2R) → loop center; thin coil center.
- B = μ₀nI, n = N/L → solenoid interior (uniform, axial).
- d = N × 2πr → wire needed to wind a solenoid.

## Important Ideas
- Every magnetic field built by a current is a *sum* of tiny element contributions — simple formulas emerge only for symmetric shapes.
- Density beats count: a solenoid's field depends on turns per meter, not turns alone.
- A current loop is a small magnet; a solenoid is a long one.
- Design problems run in chains: field → turns → wire.
- Nature resists change, not fields: Lenz's law in one line.

## Common Mistakes
Whole-wire treatment; missing sin θ; r vs r²; N vs n; loop/wire formula mix-up; solenoid length vs wire length; opposing the field instead of the change; static-magnet induction; wrong μ₀.

## Exam Focus
1. Choosing the correct formula by geometry (wire / loop / solenoid) — and justifying the choice.
2. B = μ₀nI problems in all directions: find B, find n, find I; stretching/compression reasoning.
3. Two-step solenoid design: N from the field, then d = N × 2πr.
4. Proportionality reasoning without full computation (B ∝ I, B ∝ 1/r; loop ∝ N, ∝ 1/R).
5. Lenz direction determinations, especially the decreasing-flux case (induced field *supports* the original).

## 60-Second Review
Biot–Savart: slice the current into elements; each gives dB = (μ₀/4π) I ds sin θ / r², perpendicular to ds and r̂; sum them. μ₀ = 4π × 10⁻⁷ T·m/A. Straight wire: B = μ₀I/2πr (∝I, ∝1/r). Loop center: μ₀I/2R; N-turn coil: μ₀NI/2R — a loop is a short bar magnet. Solenoid: B = μ₀nI, n = N/L — uniform inside, axial, like a long bar magnet; winding takes d = N·2πr. Parallel currents attract (pedagogical). Lenz: induced current only for *changing* flux; direction opposes the change — supporting the field when it fades.

---

# 9. DIFFICULT CONCEPTS

### Difficult Concept: The Biot–Savart Law
**Why students struggle:** It is a *differential* law — the answer comes from summing infinitely many tiny contributions, each with its own distance, angle, and perpendicular direction; students have never built a field this way.
**Simple explanation:** Treat every tiny piece of the current as a weak field source; the field anywhere is the sum of all the pieces' contributions.
**Intuitive analogy:** Candlelight in a dark room: each bit of flame adds a little brightness where you stand, fading with distance squared; the total brightness is all the bits combined.
**Step-by-step:** (1) Take element ds along the current. (2) Its distance and direction to point P give r and θ. (3) Contribution: dB = (μ₀/4π) I ds sin θ / r², perpendicular to ds and the line of sight. (4) Sum over all elements. (5) For symmetric shapes the sum collapses to a memorized formula (wire, loop, solenoid).
**Mini example:** An element pointing directly at P: θ = 0 ⇒ contributes nothing; the same element broadside to P contributes maximally.
**Misconception to avoid:** "Treat the whole wire as one source at one distance" — and forgetting sin θ or the r².
**Difficulty: VERY HARD** → video provided

### Difficult Concept: Lenz's Law
**Why students struggle:** Two coupled conditions (change + opposition), and "opposes the *change*" is subtly different from "opposes the *field*."
**Simple explanation:** The induced current flows so that its own magnetic field fights whatever change is happening to the flux.
**Intuitive analogy:** A stubborn friend: push them and they lean back; pull them and they lean toward you — always resisting the *motion*, not your existence.
**Step-by-step:** (1) Is the flux through the loop changing? No → stop, no current. (2) Increasing or decreasing, and in which direction? (3) The induced field points to oppose that specific change. (4) Curl the right hand around the loop with the thumb along the induced field — the fingers give the current direction.
**Mini example:** Push a magnet's north pole toward a loop → near face becomes north → repulsion; pull it away → near face becomes south → attraction.
**Misconception to avoid:** "The induced field opposes the external field" (it *supports* it when the flux is decreasing) and "any strong magnet near a coil induces current" (only *change* matters).
**Difficulty: HARD** → video provided

### Difficult Concept: Turns per Unit Length (n = N/L)
**Why students struggle:** N and n look like the same idea ("how many turns"), and problems hand over N while the formula wants n.
**Simple explanation:** The solenoid's field depends on winding *density* — turns packed per meter — not the raw count: a 100-turn solenoid 2 cm long is far stronger than a 100-turn solenoid 2 m long.
**Intuitive analogy:** Crowd noise: 100 people packed into one bus stop is loud; the same 100 people spread along a highway are barely audible. Density, not headcount.
**Step-by-step:** (1) Read off N and L. (2) Compute n = N/L (units: turns/m). (3) Substitute into B = μ₀nI. (4) For design problems, invert: N = LB/(μ₀I).
**Mini example:** 400 turns over 0.20 m → n = 2000 turns/m; stretch to 0.40 m at the same N → n = 1000 → B halves.
**Misconception to avoid:** "More turns always means more field" — only at fixed length.
**Difficulty: MEDIUM**

### Difficult Concept: Wire Length vs. Solenoid Length (d = N × 2πr)
**Why students struggle:** Two lengths live in every solenoid problem: the axial length L and the winding wire length d — students substitute one for the other.
**Simple explanation:** The wire doesn't run along the solenoid; it *wraps around* it N times, and each wrap is one full circumference 2πr.
**Intuitive analogy:** Ribbon around a pipe: the pipe might be 25 cm long, but the ribbon spirals around it dozens of times — the ribbon's length has nothing to do with the pipe's length.
**Step-by-step:** (1) Identify which length is asked: axial L or wire d. (2) If wire: count the turns N. (3) Each turn = 2πr. (4) d = N × 2πr.
**Mini example:** 159 turns on a 2 cm radius → d = 159 × 2π(0.02) ≈ 20 m: a 25-cm-long solenoid built from 20 m of wire.
**Misconception to avoid:** "The wire is roughly as long as the solenoid."
**Difficulty: MEDIUM**

### Difficult Concept: 2R vs. 2πr — Telling the Loop and Wire Formulas Apart
**Why students struggle:** The two formulas look almost identical (μ₀I over "two times something"), so students grab whichever comes to mind.
**Simple explanation:** They answer different questions: the wire formula gives the field at distance r *from* a long straight wire; the loop formula gives the field *at the center of* a circle of current of radius R.
**Intuitive analogy:** "How far is the station?" vs. "How big is the roundabout?" — both are distances, but one measures your separation from an object, the other measures the object's own size.
**Step-by-step:** (1) Picture the geometry. (2) Straight wire with a point off to the side → B = μ₀I/(2πr), r = distance to the wire. (3) Circle of current with the point at its middle → B = μ₀I/(2R), R = the loop's radius. (4) Multiple turns on the loop → multiply by N.
**Mini example:** 2 A at 0.05 m: from a straight wire, B = 8 × 10⁻⁶ T; at the center of a 0.05 m loop, B = 2.5 × 10⁻⁵ T — three times stronger, same numbers, different geometry.
**Misconception to avoid:** "Both formulas are the same thing with different letters."
**Difficulty: MEDIUM**

---

# 10. VIDEO LESSON PLANS

---

**VIDEO 1**

**VIDEO TITLE:** "Slicing the Wire: The Biot–Savart Law"
**TARGET CONCEPT:** Building magnetic fields from current-element contributions; the wire, loop, and solenoid formulas
**TARGET STUDENT:** First-year university student
**DURATION:** ~9 minutes
**LEARNING OBJECTIVE:** Explain the four proportionalities of the Biot–Savart law and apply the field formulas for a straight wire, a coil center, and a solenoid.
**HOOK:** A current-carrying wire is an invisible magnet — but what is its field at one specific point? You can't treat the whole wire at once. The trick: slice it.
**EXPLANATION:** (1) Each tiny element ds contributes dB = (μ₀/4π)I ds sin θ/r², perpendicular to ds and the line of sight. (2) The four facts (I, ds, sin θ, 1/r²). (3) Sum over the wire → B = μ₀I/2πr for a straight wire. (4) Loop: every element at distance R, best angle → μ₀NI/2R. (5) Stack loops into a solenoid: interior fields align → B = μ₀nI, uniform. (6) The winding formula d = N·2πr. (7) Worked design example from the lecture.
**VISUALS:** A wire chopped into glowing segments; arrows from each segment to point P shrinking with 1/r²; a "sin θ meter" showing zero contribution when ds points at P; a coil assembling turn-by-turn; a helix growing into a solenoid with parallel interior field arrows; the design example computed step by step on screen.
**EXAMPLE:** The bacteria-experiment solenoid: B = 0.002 T, L = 0.25 m, I = 2.5 A, r = 2 cm → N = 159 turns, wire = 20 m.
**COMMON MISTAKE:** Using N where n = N/L belongs; forgetting sin θ; r instead of r².
**CHECK FOR UNDERSTANDING:** "Double the current in a long wire and double your distance from it — what happens to B?"
**FINAL TAKEAWAY:** Slice, contribute, sum. The three formulas are Biot–Savart collapses for symmetric shapes: wire μ₀I/2πr, coil μ₀NI/2R, solenoid μ₀nI.

---

**VIDEO 2**

**VIDEO TITLE:** "Nature Fights Back: Lenz's Law in Four Steps"
**TARGET CONCEPT:** Direction of the induced current via Lenz's law
**TARGET STUDENT:** First-year university student
**DURATION:** ~7 minutes
**LEARNING OBJECTIVE:** Determine the direction of an induced current in a conducting loop for any changing flux.
**HOOK:** Whatever you do to a coil — push or pull — it fights back. Induced currents exist to resist *you*.
**EXPLANATION:** (1) The law's statement: induced current iff flux changes; direction opposes the change. (2) The two hidden conditions. (3) The four-step recipe: changing? which way? oppose the change; curl the right hand. (4) The classic magnet-and-loop demonstration (flagged as the standard pedagogical illustration). (5) Why a static magnet produces nothing.
**VISUALS:** A conducting loop with "flux arrows" passing through it, growing/shrinking; an induced-field arrow appearing to counter the change; a right hand curling around the loop with the thumb as induced B; an animated bar magnet (N marked) showing repulsion on approach and attraction on retreat; a "paused" magnet stamped "NO CURRENT."
**EXAMPLE:** Push a magnet's north pole toward the loop → near face becomes north → repulsion; pull it away → near face becomes south → attraction.
**COMMON MISTAKE:** "The induced field opposes the field" (it opposes the *change*); "any magnet nearby induces current."
**CHECK FOR UNDERSTANDING:** "The magnet sits motionless inside the loop — what is the induced current?"
**FINAL TAKEAWAY:** No change, no current; the induced current always opposes the change in flux — push it away when you push, hold it back when you pull.

---

# 11. VIDEO SCRIPTS

---

## SCRIPT 1 — "Slicing the Wire: The Biot–Savart Law"

**[0:00–0:30] Hook**
A wire carrying current is an invisible magnet — it twists compasses, it attracts other wires. But suppose I ask a harder question: what is the magnetic field at *this* exact point in space, right here? You can't treat the whole wire at once — every part of it is a different distance and a different angle from that point. The trick that unlocks everything: slice the wire into pieces so small that each piece is simple. That's the Biot–Savart law.

**[0:30–2:00] Concept introduction**
Take one tiny slice of the wire — call its length ds, pointing along the current. Biot and Savart's experiments on the force between a current and a nearby magnet led to four facts about the little field dB this slice creates at a point P. It's proportional to the current I — more current, more field. It's proportional to ds — a longer slice contributes more. It's proportional to the *sine* of theta, where theta is the angle between the slice and the line from the slice to your point. And it falls off as one over r *squared* — double the distance, quarter the contribution.

Put together: dB equals mu-zero over four pi, times I ds sine theta, over r squared. And the direction? Perpendicular to both the slice and the line of sight — that's the cross product ds cross r-hat. Mu-zero, four pi times ten to the minus seven tesla-meters per amp, is just the constant of the magnetic universe.

**[2:00–4:00] Visual explanation**
Here's my favorite way to see it. Think of candlelight. Every little bit of flame sends light toward you, and the brightness from each bit fades with the square of its distance from you. Brightness where you stand = all the bits added together. The wire is the candle: each slice glows a little "magnetic light" at your point, fading with distance squared, and the total field is the sum of every slice's contribution.

Notice what sine theta does. If a slice points *directly at* your point — theta zero, sine zero — that slice contributes *nothing*. Slices broadside to your point contribute the most. When you add up every slice of a long straight wire — that's the calculus — the answer collapses to something beautifully simple: B equals mu-zero I over two pi r. Double the current, double the field. Double your distance, half the field.

Now bend the wire into a loop of radius R and ask about the *center*. Every slice is at distance R, and every slice is broadside — maximum contribution, everywhere. Result: B = mu-zero I over 2R. Wind N turns together, and each turn adds its own: mu-zero N I over 2R. And remember from the lecture: the field lines around a current loop look exactly like those of a *short bar magnet*.

**[4:00–6:00] Worked example**
Stack many loops along an axis — a helix — and you've built a *solenoid*. Inside, all the contributions point along the axis and reinforce: B = mu-zero n I, where little n is turns *per meter* — N over L. Uniform, strong, controllable. That's why solenoids are everywhere. And one construction fact: each turn wraps once around the circumference, so winding N turns on radius r takes N times two pi r of wire.

A real design problem from the lecture: a research student needs a solenoid producing 0.002 tesla inside, 0.25 meters long, running 2.5 amps, wound on a 2-centimeter radius. How much wire? First, turns: N = L B over mu-zero I — 0.25 times 0.002, divided by four pi times ten to the minus seven times 2.5 — 159 turns. Each turn wraps once around the circumference, 2 pi r. Total wire: 159 times 2 pi times 0.02 — about twenty meters.

**[6:00–7:00] Common mistake**
Watch for these. One: forgetting sine theta — a slice pointing at your point contributes nothing. Two: r instead of r squared — it's an inverse-square contribution. Three — the most common on solenoid problems — plugging in the total turn count N where the turns-*per-length* n belongs. And four: assuming the field around a straight wire is constant — it drops off as one over r.

**[7:00–8:00] Quick student challenge**
Two quick ones. First: a long straight wire — I double the current and also double my distance from it. What happens to B? Field doubles from the current, then halves from the distance — *unchanged*. Second: at the center of a loop, I double the radius. B = mu-zero I over 2R — the field *halves*.

**[8:00–8:30] Final recap**
The recipe: slice the wire, let each slice contribute mu-zero over four pi, I ds sine theta, over r squared, perpendicular to the slice and the line of sight — and sum. The famous results are just that sum for symmetric shapes: wire — mu-zero I over 2 pi r. Loop — mu-zero N I over 2R. Solenoid — mu-zero n I. Slice, contribute, sum.

---

## SCRIPT 2 — "Nature Fights Back: Lenz's Law in Four Steps"

**[0:00–0:30] Hook**
Here's something almost alive about circuits: whatever you do to a coil of wire — push a magnet toward it, pull it away — the coil fights back. Push, and it repels. Pull, and it holds on. Not because anything is touching — because the coil *generates its own current* to resist you. That's Lenz's law, and today it becomes a four-step recipe you can't get wrong.

**[0:30–2:00] Concept introduction**
The law, stated precisely: there is an induced current in a closed, conducting loop *if and only if* the magnetic flux through the loop is changing. And the direction of that induced current is such that the magnetic field it creates *opposes the change* in the flux.

Flux, informally, is the amount of magnetic field passing through the loop — how many field lines poke through it. Two conditions hide in that sentence. First: *change is mandatory*. A strong but steady field induces nothing. Second: the induced current doesn't fight the field — it fights the *change* in the field. That distinction is where every exam point is won or lost.

**[2:00–4:00] Visual explanation**
The recipe — four steps. Step one: ask, is the flux through the loop changing? If no — stop. No current, no matter how strong the field. If yes — step two: which way is it changing? More flux or less, and pointing which direction through the loop? Step three: the induced magnetic field must *oppose that change*. Flux in some direction increasing? The induced field points back the other way. Flux *decreasing*? The induced field points the *same* way — propping it up. It always resists the change, not the field. Step four: curl your right hand around the loop with your thumb along the induced field — your fingers wrap in the current's direction.

**[4:00–6:00] Worked example**
The classic demo — and this goes beyond the one-line statement in the notes, so treat it as the standard illustration. Take a bar magnet, north pole facing a loop, and push it *toward* the loop. Flux pointing away from the magnet is *increasing* through the loop. Step three: the induced field must point back toward the magnet. Curl your right hand — the current flows so that the loop's near face is a *north pole*. North faces north — the loop repels the magnet. You're pushing; it pushes back.

Now reverse it: pull the magnet away. Flux decreasing — so the induced field flips, now *supporting* the fading flux. The loop's near face becomes a *south pole* — and it attracts the magnet, tugging it back. Push — repelled. Pull — held. Motion is always resisted.

**[6:00–7:00] Common mistake**
Three traps. Trap one: "the induced field opposes the external field." No — it opposes the *change*. When flux is decreasing, the induced field actually points the *same* way as the external field, holding it up. Trap two: "a strong magnet inside a coil creates current." Only if something is *changing*. A magnet sitting perfectly still: flux constant, current zero. Trap three: forgetting the loop must be closed — no closed conducting loop, no induced current.

**[7:00–8:00] Quick student challenge**
Two questions. First: a magnet hovers motionless inside a conducting loop — perfectly still. What's the induced current? … Zero. Flux constant. Second: same setup, but now you pull the magnet away — compared to when you pushed it in, which way does the induced current flow? … Reversed. Approaching and retreating are opposite changes, so the loop responds in opposite directions.

**[8:00–8:30] Final recap**
Lenz's law in one breath: no change, no current; when flux changes, the induced current flows to oppose that change. Four steps: is it changing, which way, oppose it, curl the right hand. Push — repelled. Pull — attracted. Nature resists you, every single time.

---

# 12. PRACTICE QUESTIONS

## LEVEL 1 — UNDERSTAND

1. What experiments led to the Biot–Savart law, and what does the law compute?
2. State the four experimental observations underlying the law.
3. Give the value and SI units of μ₀.
4. What is the direction of dB relative to ds and to r̂?
5. A wire element points directly at the point P. What is its contribution to B at P, and which factor is responsible?
6. For a long straight wire, state both proportionalities of B.
7. What do the field lines around a current loop resemble? Around a solenoid?
8. What does n represent in B = μ₀nI, and in what units is it measured?
9. Describe the magnetic field inside a long solenoid (magnitude and direction).
10. State Lenz's law in one sentence, making the distinction between opposing the *field* and opposing the *change*.

## LEVEL 2 — APPLY

11. A long straight wire carries 10 A. Find B at 0.10 m from it.
12. For the same wire, find B at 0.20 m — using proportionality, not a full recomputation.
13. What current in a long straight wire produces B = 4.0 × 10⁻⁵ T at a distance of 0.20 m?
14. A single circular loop of radius 0.10 m carries 5.0 A. Find B at its center.
15. A thin coil of 50 turns, radius 0.050 m, carries 2.0 A. Find B at its center.
16. A solenoid has 400 turns over 0.20 m and carries 2.0 A. Find B inside.
17. What turns-per-unit-length n is required to produce B = 6.0 × 10⁻³ T inside a solenoid carrying 3.0 A?
18. How much wire is needed to wind 500 turns on a cylinder of radius 3.0 cm?
19. A current element ds points along +x; the unit vector r̂ toward the point P points along +y. What is the direction of dB?
20. At the center of a circular loop, what angle does each current element make with r̂ (from the geometry of the circle), and what does that mean for its contribution?

## LEVEL 3 — TRANSFER

21. For a long straight wire, the current is doubled and the observation distance is also doubled. What happens to B? Justify with the proportionalities.
22. A loop's radius is doubled while the current is unchanged. What happens to the center field?
23. A solenoid is stretched to twice its length, keeping the same number of turns and the same current. What happens to the interior field, and why?
24. Compare solenoid A (n = 1000 turns/m, I = 2.0 A) with solenoid B (n = 500 turns/m, I = 4.0 A). Which produces the stronger interior field?
25. Design: an interior field of 0.010 T is required at I = 5.0 A. Find the required n, and the number of turns if the solenoid is 0.30 m long.
26. A closed loop sits in a magnetic field that begins to *decrease* smoothly. Is there an induced current? In which direction does its induced field point — with or against the original field? Justify with Lenz's law.

**INSTRUCTOR ANSWER KEY (not for student display)**

1. Experiments on the force exerted by an electric current on a nearby magnet; the law gives the magnetic field at a point in space due to a current (via element contributions). [EASY]
2. (i) dB ⟂ ds and ⟂ r̂; (ii) |dB| ∝ 1/r²; (iii) |dB| ∝ I and ds; (iv) |dB| ∝ sin θ (θ between ds and r̂). [EASY]
3. μ₀ = 4π × 10⁻⁷ T·m/A. [EASY]
4. Perpendicular to both — the direction of ds × r̂. [EASY]
5. Zero; sin θ = 0 (observation 4). [EASY]
6. B ∝ I; B ∝ 1/r. [EASY]
7. Loop → short bar magnet; solenoid → long bar magnet. [EASY]
8. Turns per unit length, n = N/L; units: turns/m (= m⁻¹). [EASY]
9. Uniform — constant magnitude, directed parallel to the solenoid's axis. [EASY]
10. Induced current exists iff the flux is changing; its direction makes the induced field oppose the *change* in flux (supporting the original field if the flux decreases). [MEDIUM]
11. B = (4π × 10⁻⁷ × 10)/(2π × 0.10) = 2.0 × 10⁻⁵ T. [EASY]
12. B ∝ 1/r → half of Q11: 1.0 × 10⁻⁵ T. [EASY]
13. I = B·2πr/μ₀ = (4.0 × 10⁻⁵ × 2π × 0.20)/(4π × 10⁻⁷) = 40 A. [MEDIUM — inverted formula]
14. B = μ₀I/(2R) = (4π × 10⁻⁷ × 5.0)/(0.20) = 3.1 × 10⁻⁵ T. [EASY]
15. B = μ₀NI/(2R) = (4π × 10⁻⁷ × 50 × 2.0)/(0.10) = 1.3 × 10⁻³ T. [MEDIUM]
16. n = 400/0.20 = 2000 /m; B = 4π × 10⁻⁷ × 2000 × 2.0 = 5.0 × 10⁻³ T. [MEDIUM — the N → n conversion]
17. n = B/(μ₀I) = 6.0 × 10⁻³/(4π × 10⁻⁷ × 3.0) ≈ 1.6 × 10³ turns/m. [MEDIUM — inverted]
18. d = N × 2πr = 500 × 2π × 0.030 ≈ 94 m. [EASY]
19. ds × r̂ = x̂ × ŷ = +ẑ → dB along +z (perpendicular to both). [MEDIUM — cross-product direction]
20. Each element (tangent to the circle) is perpendicular to r̂ (radial): θ = 90°, sin θ = 1 — every element contributes maximally at the center. *(Derivable directly from the geometry of a circle + observation 4.)* [MEDIUM]
21. Unchanged: ×2 from I, ×½ from r → B ∝ I/r. [MEDIUM]
22. Halves: B = μ₀I/(2R) ∝ 1/R. [EASY]
23. Halves: n = N/L halves when L doubles, so B = μ₀nI halves. [MEDIUM — the density idea]
24. Equal: B_A = μ₀(1000)(2.0) = μ₀(2000); B_B = μ₀(500)(4.0) = μ₀(2000). [MEDIUM]
25. n = 0.010/(4π × 10⁻⁷ × 5.0) ≈ 1.6 × 10³ turns/m; N = nL = 1.6 × 10³ × 0.30 ≈ 477 turns. [MEDIUM — design chain]
26. Yes — the flux is changing (decreasing); the induced field points *with* the original field, opposing the decrease. [HARD — the decreasing-flux case]

---

# 13. TRANSFER QUESTIONS

*New-context problems carrying Lecture 9 concepts into unfamiliar settings.*

**T1 — Design task (mirror of the source's bacteria experiment):** A research team needs an interior solenoid field of 0.005 T over a length of 0.30 m, running 2.0 A, on a 1.5 cm-radius former. Determine the required number of turns and the total wire length.
→ *Key:* N = LB/(μ₀I) = (0.30 × 0.005)/((4π × 10⁻⁷)(2.0)) ≈ 597 turns; d = 597 × 2π(0.015) ≈ 56 m. [MEDIUM-HARD — full design chain]

**T2 — Sensor reasoning by proportionality:** A probe measures B = 4.0 × 10⁻⁵ T at 2.0 cm from a long straight wire. Without recomputing from the formula, find B at 8.0 cm from the same wire.
→ *Key:* B ∝ 1/r: distance ×4 → field ÷4 → 1.0 × 10⁻⁵ T. [EASY]

**T3 — Loop scaling comparison:** Loop B has three times the radius of loop A; both carry the same current. Compare their center fields.
→ *Key:* B = μ₀I/(2R) ∝ 1/R → B_B = B_A/3. [EASY]

**T4 — Coil vs. single loop:** A 40-turn coil and a single loop share the same radius and current. Compare the fields at their centers.
→ *Key:* B_coil = 40 × B_loop (the N multiplier). [EASY]

**T5 — Coupled-circuit reasoning (Lenz transfer):** A closed conducting loop is held near a solenoid whose current is steadily *increasing*. Describe what appears in the loop, and state the direction rule that fixes its sense.
→ *Key:* The flux through the loop is increasing → an induced current appears, directed so its induced field *opposes the increase* (points against the solenoid's growing field through the loop). Only the law's statement is needed — the geometry is new. [MEDIUM]

**T6 — Reverse design (wire budget):** You have exactly 15 m of wire and must wind a solenoid on a 1.0 cm-radius cylinder. What is the maximum number of complete turns you can wind?
→ *Key:* Invert d = N·2πr → N = d/(2πr) = 15/(2π × 0.010) ≈ 238 complete turns. [MEDIUM — formula inversion]

---

# 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All Lecture 9 topics present: Biot–Savart (experiments, four observations, both forms, μ₀), straight wire (formula + proportionalities), loop center, N-turn coil, loop↔short bar magnet, solenoid (definition, uniform interior field, long bar magnet, B = μ₀nI, n = N/L, d = N·2πr), forces between currents (flagged), Lenz's law (exact statement preserved). |
| Mathematical formulas correct | ✅ | All 8 formulas match the source; the source example reproduces exactly (N = 159, d = 20 m); all practice/transfer computations verified. |
| Technical terminology preserved | ✅ | Biot–Savart law, magnetic permeability of free space, solenoid, turns per unit length, magnetic flux, induced current — all retained. |
| Explanations in original language | ✅ | No source paragraphs reproduced; only formulas and the one-line Lenz statement (a necessary standard statement) shared. |
| Understandable to a first-year student | ✅ | Slicing/candlelight and four-step Lenz recipe scaffold the two hardest ideas; analogies flagged as pedagogical. |
| Difficult concepts explicitly identified | ✅ | 5 concepts with full analysis and difficulty ratings in §9. |
| Common misconceptions identified | ✅ | 10 in §7; per-concept misconceptions in §9; in-video mistakes in §10–11. |
| Examples actually teach | ✅ | The source example retained with full reasoning; 4 clearly-flagged pedagogical examples added to cover skills the source's single example doesn't exercise (wire field, loop/coil, solenoid interior, Lenz direction). |
| Practice progresses understand → apply → transfer | ✅ | L1 (10 conceptual) → L2 (10 computational) → L3 (6 synthesis) + 6 transfer tasks, all with verified keys. |
| No unsupported claims added | ✅ | Flagged items: forces between currents — figures only in the source, formulas marked [SOURCE DOES NOT SPECIFY], with a clearly-labeled pedagogical note built from Lectures 7–8; "magnetic flux" used informally with [SOURCE DOES NOT SPECIFY] for its formal definition; the θ = 90° loop-center geometry and the magnet-loop Lenz demo are flagged as derivable/standard illustrations; the parallel-currents attraction note is explicitly labeled beyond-the-source. |
| No large verbatim reproduction | ✅ | Only formulas and the single standard statement of Lenz's law overlap with the source. |
| Suitable for direct web integration | ✅ | Clean Markdown; student-facing self-check separated from instructor keys. |

**Source errata handled transparently (meaning preserved, typos not propagated):**
- No numerical errata in this lecture: the solenoid example computes consistently (N = 159; d = 20 m).
- The Biot–Savart vector equation appears with extraction artifacts ("𝑑?⃗? × ?̂?"); restored as dB = (μ₀/4π)(I **ds** × r̂)/r² exactly as the source's own list of observations and magnitude formula confirm.
- "Forces between currents" and the associated figures carry no quantitative content in the extracted text — preserved as topic names with [SOURCE DOES NOT SPECIFY] on details.
- The source states Lenz's law for a "closed, conducting loop" — the closed-loop condition is retained everywhere (including the video script's trap #3).


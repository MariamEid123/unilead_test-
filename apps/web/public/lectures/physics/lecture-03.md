تمام — دي **Lecture 3** بالباكدج الكامل. (ملحوظة للتوثيق: بعض ترويسات صفحات المصدر مكتوب فيها Fall 2023 رغم أن الغلاف Fall 2024 — خطأ مطبعي في المصدر، المحتوى نفسه سليم. والأمثلة مرقّمة 7 و8 لأنها تكمل ترقيم Lecture 2.)

---

## 1. SOURCE ANALYSIS

**Source document:** Phy 211 Lecture Notes — Lecture 3, Fall 2024, AIU (Dr. Ashraf Mousa Abdelwahed), 8 pages.

| Item | Finding |
|---|---|
| Course | Phy 211 — Physics [full course title: SOURCE DOES NOT SPECIFY] |
| Chapter | Chapter 1 — Electric Force & Electric Field |
| Lecture | Lecture 3 (third lecture of the chapter) |
| Position | Builds directly on Coulomb's law (Lecture 2); prepares the ground for flux & Gauss's law and potential (Lecture 4) |
| Source notes | Page headers inconsistently show "Fall 2023"; cover shows Fall 2024 — cosmetic inconsistency only. Examples numbered 7 and 8, continuing Lecture 2's numbering. |

**Main topics**
1. The electric field E⃗ — definition, existence around any charged object, E = F/q₀
2. Field of a point charge: E = KQ/r²; direction rules (away from +, toward −)
3. Superposition of fields from several charges
4. Motion of a charged particle in a field: F = E|q| = ma, a = E|q|/m, a ∝ 1/m; electron vs. proton; charge accelerators
5. Electric field lines — four rules
6. The electric dipole: moment p⃗, torque τ, polarization, potential energy

**Important definitions:** electric field; field of a point charge; vector sum of fields; field lines (begin/end, tangent, no crossing, density ∝ charge); electric dipole; dipole moment; torque; polarization.

**Important formulas:** E = F/q₀ = KQ/r²; E_net = E₁ + E₂ + E₃ + ⋯; F = E|q| = ma; a = E|q|/m; p = q(2a); τ = pE sinθ; τ⃗ = p⃗ × E⃗; U = pE cosθ.

**Worked examples in source:** Example 7 (field of −3 µC at 30 cm), Example 8 (two-charge field at point P between them + electron acceleration at P).

**Procedures:** compute E from a single charge (magnitude → direction); superpose collinear fields with a sign convention; compute particle acceleration; derive dipole torque from force × normal distance.

**Prerequisites (inferred):** Lectures 1–2 (Coulomb's law, superposition with signs, prefixes); Newton's second law; basic trigonometry (sin/cos).

**Dependencies:** reuses Lecture 2's inverse-square machinery; its field concept is the foundation of Lecture 4 (flux Φ = E·A, Gauss's law, E = −ΔV/d) and the capacitor (E = ΔV/d).

**Difficult concepts identified:** the field concept itself (existence without a test charge); direction bookkeeping for negative charges; negative particles accelerating opposite to E; the no-crossing rule for field lines; dipole torque/polarization.

**Common misconceptions in the material:** field depends on the test charge; signed Q in the E formula; field points away from negative charges; dipole feels a net force in a uniform field; p⃗ directed from +q to −q.

---

## 2. COURSE / MODULE / LESSON METADATA

- **COURSE:** Phy 211 — Physics (full title [SOURCE DOES NOT SPECIFY]; Chapter 1: Electric Force & Electric Field)
- **MODULE:** Chapter 1 — Electric Force & Electric Field (Module 1: Foundations of Electrostatics)
- **LESSON:** Lecture 3 — Electric Field, Field Lines, and the Electric Dipole
- **TOPICS:** definition of E; point-charge field; superposition; charged-particle motion; field-line rules; dipole moment, torque, polarization, and energy
- **PREREQUISITES:** Lectures 1–2; Newton's second law; trigonometry (sin/cos)
- **COMPETENCIES:** compute field magnitudes and directions; superpose collinear fields; predict and compute particle acceleration; apply the four field-line rules; compute dipole moment, torque, and energy
- **DIFFICULTY:** Overall MEDIUM; two HARD sub-concepts: the field concept itself, and dipole torque/polarization
- **ESTIMATED STUDY TIME:** ~90 minutes (≈50 min lesson + ≈40 min practice)

**Position in the ARETE learning flow:** LEARN + PRACTICE. Gated on Lectures 1–2. Everything downstream (flux, Gauss's law, potential, capacitors) consumes this lesson's field concept — highest-leverage lesson in the module.

---

## 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Define the electric field and explain that it exists in the space around any charged object, whether or not another charge is present.
2. Apply E = F/q₀ and explain the role of the positive test charge q₀.
3. Compute the field of a point charge, E = KQ/r², and state its direction for positive and negative source charges.
4. Superpose fields from several collinear charges using a sign convention.
5. Predict the direction of a charged particle's acceleration (positive → along E; negative → opposite E) and compute it via a = E|q|/m.
6. Explain why aₑ ≫ a_p for an electron and proton in the same field, and connect this to charge accelerators.
7. State and apply all four rules of electric field lines.
8. Define the electric dipole and its moment p⃗ (direction from −q toward +q, magnitude p = q·2a).
9. Compute dipole torque τ = pE sinθ, explain polarization (alignment with the field), and evaluate U = pE cosθ.

---

## 4. WEB-READY LESSON

# Lecture 3 — Electric Field, Field Lines, and the Electric Dipole

## Prerequisites
The student should already understand:
- Coulomb's law and its magnitude-only discipline (Lecture 2)
- Superposition with signs on a line (Lecture 2)
- Charge signs and prefixes (Lecture 1)
- Newton's second law (F = ma) and basic sin/cos

---

### 1. What Is an Electric Field?

#### Core Idea
Every charged object modifies the space around it. That modified space is the electric field — and it is the field that pushes any other charge placed in it.

#### Explanation
The lecture's logic runs in three steps:

- A charged object creates a condition in the space around itself: **an electric field is said to exist in the region of space around a charged object.**
- The field does work: **it exerts an electric force on any other charged object within it.**
- We measure the field's strength by probing it with a small positive **test charge q₀** and dividing the measured force by that charge:

> **E = F / q₀**  (units: N/C)

Think of q₀ as a thermometer, not an ingredient: you dip it in to *read* the field, but the field was already there — and when you divide the force by q₀, the test charge itself cancels out. The field belongs to the source charge; the test charge merely reveals it.

#### Example
If a +2 µC test charge at some point feels a force of 0.6 N, the field at that point is E = 0.6/(2 × 10⁻⁶) = 3 × 10⁵ N/C — and any *other* charge placed there would feel a force scaled to its own charge: F = qE.

#### Key Point
The field is a property of the space around a source charge. E = F/q₀ is the reading, not the recipe: the field exists with or without a probe.

---

### 2. The Field of a Point Charge

#### Core Idea
Dividing Coulomb's force law by the test charge produces the field of a point charge: E = KQ/r², directed away from +Q and toward −Q.

#### Explanation
Take Coulomb's law between a source charge Q and a test charge q₀ and divide by q₀:

**E = (KQq₀/r²) / q₀ = KQ / r²**

The source states the same result from the force on q₂: E = F/|q₂| = K|q₁|/r² — the target charge cancels every time, confirming that the field belongs to the source alone.

Direction rules (memorize both):

- **Positive source charge:** field points **away** from it (radially outward).
- **Negative source charge:** field points **toward** it (radially inward).

As with Coulomb's law, use |Q| in the formula — magnitudes only — and assign direction separately.

#### Example
The source's Example 7: a −3 µC charge, 30 cm away. |E| = (9 × 10⁹)(3 × 10⁻⁶)/(0.3)² = 3 × 10⁵ N/C — pointing from the point P **toward** the negative charge. (Full solution below.)

#### Key Point
E = K|Q|/r² with the same inverse-square scaling as the force (double r → E/4). Negative charge ⇒ field points inward; positive ⇒ outward.

---

### 3. Superposition of Fields

#### Core Idea
When several charges are present, each creates its own field independently, and the total field at any point is their **vector sum**.

#### Explanation
Just as forces superpose, fields superpose:

> **E⃗_net = E⃗₁ + E⃗₂ + E⃗₃ + ⋯**

The procedure is identical to Lecture 2's force recipe, transferred to fields:

1. Fix a positive x-direction.
2. Compute each field's magnitude: E = K|q|/r² (magnitudes only).
3. Assign each field's direction: away from each positive source, toward each negative source.
4. Write each with a ± sign and add algebraically.

One new advantage over force problems: the point where you evaluate the field does not have to hold any charge at all — fields live everywhere in space, so "find E at point P" needs no target charge.

#### Example
The source's Example 8: between a −25 µC charge (2 cm to the left of P) and a +50 µC charge (8 cm to the right of P), both fields point in the −x direction and **add**: 5.625 × 10⁸ + 0.703 × 10⁸ = 6.328 × 10⁸ N/C in −x. (Full solution below.)

#### Key Point
Fields superpose exactly like forces: pairwise magnitudes → direction rules → signed addition. Between a negative charge on one side and a positive charge on the other, the fields reinforce.

---

### 4. Charged Particles in a Field: Acceleration

#### Core Idea
A charge q in a field E feels F = E|q| and accelerates with a = E|q|/m — positive charges along the field, negative charges against it, and lighter particles always accelerate more.

#### Explanation
A charged particle in an electric field experiences an electric force, and by Newton's second law that net force accelerates it:

> **F = E|q| = ma  →  a = E|q|/m**

Two direction rules and one proportionality:

- **Positive charge:** acceleration **in the direction of E**.
- **Negative charge:** acceleration **opposite to E**.
- **a ∝ 1/m** — at fixed E and q, the lighter the particle, the larger the acceleration.

Because mₑ ≪ m_p, an electron and a proton placed in the *same* field satisfy **aₑ ≫ aₐ**... — **aₑ ≫ a_p** — and the source notes that this very fact is exploited in **charge accelerators**.

#### Example
In Example 8b, an electron at point P (where E = 6.328 × 10⁸ N/C points in −x) accelerates at 1.11 × 10²⁰ m/s² **in the +x direction** — opposite the field, because it is negative.

#### Key Point
a = E|q|/m. Sign of the charge sets the direction (along E for +, against for −); mass sets the size. Electrons respond thousands of times more strongly than protons.

---

### 5. Picturing the Field: Electric Field Lines

#### Core Idea
Field lines are a drawing language for the invisible field — and four strict grammar rules govern them.

#### Explanation
The field can be represented by lines obeying:

1. **Lines begin on positive charges and terminate on negative charges.** They don't start or stop in empty space.
2. **Field lines cannot intersect** — even when charges are very close. (Reason: at a crossing point, the field would need two different directions at once, but E at any point has exactly one direction.)
3. **The direction of E at any point is the tangent to the field line** at that point.
4. **The number of lines leaving a positive charge (or entering a negative one) is proportional to the magnitude of the charge** — a bigger charge gets more lines, so line density visually encodes field strength.

#### Example
A +3 µC charge would be drawn with three times as many outward lines as a +1 µC charge; a dipole's lines run from the +q to the −q, arcing smoothly, never crossing.

#### Key Point
Four rules: start on +, end on −; never cross; tangent = direction; line count ∝ charge. Any proposed drawing violating one of these is physically wrong.

---

### 6. The Electric Dipole

#### Core Idea
Two equal-and-opposite charges separated by a fixed distance 2a form a dipole — in a uniform field it feels zero net force but a torque that twists it into alignment.

#### Explanation
**Definition:** an electric dipole consists of two charges of equal magnitude and opposite sign separated by a distance 2a (the pair is bound and cannot be separated, as the source states).

**Dipole moment:** the vector p⃗ points **from −q toward +q** along the line joining the charges, with magnitude:

> **p = q · 2a**  (units: C·m — derived from charge × distance)

**In a uniform field:** the +q feels a force along E; the −q feels an equal force opposite E. Net force = **zero** — but the two forces act along different lines, so they create a **torque**:

**τ = force × (normal distance between the two forces) = (qE)(2a sinθ) = pE sinθ**, or in vector form **τ⃗ = p⃗ × E⃗ (N·m)**, where θ is the angle between the dipole axis and the field.

**Polarization:** due to this torque, the dipole **tends to align with the field direction** — this alignment phenomenon is called *polarization*.

**Potential energy:** the source gives the dipole's energy as:

> **U = p⃗ · E⃗ = pE cosθ** (Joule) — *as stated in the source; use this course's convention in exams.* *(Pedagogical note: textbooks differ on sign conventions for dipole energy — always follow your course's formula sheet.)*

#### Example
*(Pedagogical example, built from the source's formulas — no numeric dipole example appears in the source.)* A dipole with q = 1 µC and 2a = 2 cm has p = 10⁻⁶ × 0.02 = 2 × 10⁻⁸ C·m. In a field of 5 × 10⁵ N/C at θ = 30°: τ = (2 × 10⁻⁸)(5 × 10⁵)(0.5) = 5 × 10⁻³ N·m, and U = pE cos30° ≈ 8.66 × 10⁻³ J.

#### Key Point
Dipole in a uniform field: net force zero, torque pE sinθ twisting it toward alignment (polarization). Moment p = q·2a points from − to +.

---

### Key Takeaways

- An electric field exists in the space around every charged object; it exerts forces on charges placed in it.
- E = F/q₀: the test charge reads the field; dividing by q₀ removes it — the field is the source's property.
- Point charge: E = K|Q|/r², same inverse-square scaling as Coulomb's law (double r → quarter E).
- Direction: away from positive sources, toward negative sources.
- Multiple charges: E_net is the vector sum — same sign-convention recipe as force superposition.
- Particle in a field: a = E|q|/m; positive charges accelerate along E, negative charges opposite E.
- Since mₑ ≪ m_p, electrons accelerate ~1800× more than protons in the same field — the principle behind charge accelerators.
- Field lines: begin on +, end on −, never cross, tangent gives E's direction, line count proportional to charge magnitude.
- Dipole: equal-and-opposite charges at fixed separation 2a; moment p = q·2a from −q toward +q.
- Dipole in a uniform field: zero net force, torque τ = pE sinθ aligning it with the field (polarization); energy U = pE cosθ.

### Self-Check (answers are not shown — attempt before checking)

1. Define the electric field in words, and write its defining formula with units.
2. Does the field at a point change if you place a bigger test charge there? Justify using E = F/q₀.
3. State the direction of the electric field (a) 1 m from a +6 µC charge; (b) 1 m from a −6 µC charge.
4. Distinguish E and F: which one exists without a second charge, and what are their units?
5. A uniform field points in +x. An electron is placed in it — which way does it accelerate, and why?
6. Why can two electric field lines never intersect? Argue from the meaning of E's direction at a point.
7. Two equal positive charges sit 10 cm apart. Without computing, where between them is the net field zero — and why?
8. State the magnitude and direction of the dipole moment of a dipole with charges ±2 µC separated by 3 cm.
9. A dipole sits in a uniform field at θ = 90°. What is its net force? Its torque (in terms of p and E)? Its energy according to this course's formula?

---

## 5. FORMULAS

### F1 — Definition of the electric field
**E = F / q₀**  (N/C)
- **F:** force on the positive test charge **q₀** placed at the point.
- **When used:** converting a measured force into a field value; conceptual definition.
- **Interpretation:** force per unit positive charge — the field's "strength reading."
- **Assumptions:** q₀ is small enough not to disturb the source; q₀ is positive by convention.

### F2 — Field of a point charge
**E = K|Q| / r²**  (N/C)
- **Q:** source charge (C); **r:** distance from the source (m); **K** = 9 × 10⁹ N·m²/C².
- **When used:** field of any single (point) charge.
- **Interpretation:** inverse-square in r; direction separate — away from +Q, toward −Q.
- **Assumptions:** point source charge; magnitudes only in the formula.

### F3 — Superposition of fields
**E⃗_net = E⃗₁ + E⃗₂ + E⃗₃ + ⋯**
- **When used:** several source charges.
- **Interpretation:** each source contributes independently; total is the vector sum (signed addition in 1-D).
- **Assumptions:** a fixed positive direction; each Eᵢ computed with its own rᵢ.

### F4 — Force and acceleration of a particle in a field
**F = E|q| = ma  →  a = E|q| / m**  (m/s²)
- **q:** particle's charge; **m:** particle's mass.
- **When used:** motion of a charged particle in a known field.
- **Interpretation:** positive charge → a along E; negative → opposite E; a ∝ 1/m.
- **Assumptions:** the field is the only force considered; |q| used for magnitude, sign handled by direction.

### F5 — Dipole moment
**p = q · 2a**  (C·m)
- **q:** magnitude of each dipole charge; **2a:** separation between them.
- **Direction of p⃗:** from −q toward +q along the dipole axis.
- **When used:** any dipole torque or energy calculation.

### F6 — Torque on a dipole
**τ = F × (2a sinθ) = (qE)(2a sinθ) = pE sinθ** ; **τ⃗ = p⃗ × E⃗** (N·m)
- **θ:** angle between the dipole axis (p⃗) and the field E⃗.
- **When used:** dipole in a (uniform) electric field.
- **Interpretation:** torque is maximum at θ = 90° and zero at θ = 0° (aligned) and 180°.
- **Assumptions:** net force zero (equal-and-opposite forces); torque from force × normal distance between the two force lines.

### F7 — Dipole potential energy
**U = p⃗ · E⃗ = pE cosθ**  (J)
- **When used:** energy of an aligned/misaligned dipole, as given in this course.
- **Interpretation (per the source's formula):** U = pE at θ = 0; U = 0 at θ = 90°.
- **Assumptions:** use the course's sign convention (see pedagogical note in the lesson).

---

## 6. WORKED EXAMPLES

### Worked Example 1 — Field of a single negative charge (Source: Example 7)
*Find the magnitude and direction of E due to a charge q = −3 µC at a point P, 30 cm from the charge.*

**Step 1 — Magnitude (use |q|):**
|E| = Ke|q|/r² = (9 × 10⁹)(3 × 10⁻⁶)/(0.3)²

**Step 2 — Compute:**
(9 × 10⁹)(3 × 10⁻⁶) = 2.7 × 10⁴ ; (0.3)² = 0.09

|E| = 2.7 × 10⁴/0.09 = **3 × 10⁵ N/C**

**Step 3 — Direction:** the charge is **negative**, so the field points **toward** it: at P, E is directed **from P toward the charge q**. ✓

---

### Worked Example 2 — Superposed fields + electron acceleration (Source: Example 8)
*Charges q₁ = −25 µC and q₂ = +50 µC are 10 cm apart. Point P lies between them, 2 cm to the right of q₁ (8 cm left of q₂).*
*a) Find E at P. b) An electron is placed at P — find its acceleration (direction and magnitude). (mₑ = 9.1 × 10⁻³¹ kg, qₑ = 1.6 × 10⁻¹⁹ C)*

**a) Step 1 — Axis:** +x to the right (q₁ at left, q₂ at right, P between).

**Step 2 — Field from q₁ (magnitudes):**
E₁ = K|q₁|/r² = (9 × 10⁹)(25 × 10⁻⁶)/(0.02)²
= 2.25 × 10⁵/4 × 10⁻⁴ = **5.625 × 10⁸ N/C**

**Step 3 — Direction of E₁:** q₁ is negative → field points toward q₁ → P is to q₁'s right → **−x direction**.

**Step 4 — Field from q₂:**
E₂ = (9 × 10⁹)(50 × 10⁻⁶)/(0.08)²
= 4.5 × 10⁵/6.4 × 10⁻³ = **0.703 × 10⁸ N/C**

**Step 5 — Direction of E₂:** q₂ is positive → field points away from q₂ → P is to q₂'s left → away from q₂ means pointing **−x**.

**Step 6 — Superpose (both are −x, so they add):**
E_p = −E₁ − E₂ = −5.625 × 10⁸ − 0.703 × 10⁸ = **−6.328 × 10⁸ N/C**

**Result (a):** magnitude **6.328 × 10⁸ N/C**, directed into the **−x** direction. *(Note the physics: between a negative charge on the left and a positive charge on the right, both fields point the same way — they reinforce.)*

**b) Step 7 — Acceleration magnitude:**
aₑ = E_p |qₑ|/mₑ = (6.328 × 10⁸)(1.6 × 10⁻¹⁹)/(9.1 × 10⁻³¹)

**Step 8 — Compute:**
(6.328 × 10⁸)(1.6 × 10⁻¹⁹) = 1.0125 × 10⁻¹⁰ ; ÷ 9.1 × 10⁻³¹ = **1.11 × 10²⁰ m/s²**

**Step 9 — Direction:** the electron is **negative**, so it accelerates **opposite to E**. E points −x → the electron accelerates in the **+x direction**. ✓

---

### Worked Example 3 — Dipole quantities *(pedagogical — constructed from the source's formulas; the source contains no numeric dipole example)*
*A dipole has charges q = ±1 µC separated by 2a = 2 cm. It sits in a uniform field E = 5 × 10⁵ N/C with its axis at θ = 30° to the field. Find p, the force on each charge, τ, and U.*

**Step 1 — Dipole moment:**
p = q · 2a = (1 × 10⁻⁶)(0.02) = **2 × 10⁻⁸ C·m** (direction: from −q toward +q)

**Step 2 — Force on each charge:**
F = qE = (1 × 10⁻⁶)(5 × 10⁵) = **0.5 N** — equal and opposite on the two charges (net force = 0).

**Step 3 — Torque:**
τ = pE sinθ = (2 × 10⁻⁸)(5 × 10⁵)(sin 30°) = (2 × 10⁻⁸)(5 × 10⁵)(0.5) = **5 × 10⁻³ N·m**

**Step 4 — Potential energy (course formula):**
U = pE cosθ = (2 × 10⁻⁸)(5 × 10⁵)(cos 30°) ≈ **8.66 × 10⁻³ J**

**Step 5 — Interpretation:** the torque twists the dipole toward θ = 0 (alignment with the field) — polarization.

---

## 7. COMMON MISTAKES

**Mistake 1 — Believing the field depends on the test charge.**
- *What students do:* think E changes when a bigger charge is placed at the point.
- *Why it's wrong:* E = F/q₀ — the force grows with q₀, but the ratio is fixed; the field belongs to the source.
- *How to avoid:* remember the thermometer analogy: the probe reads the field; it doesn't create it.

**Mistake 2 — Substituting a signed Q into E = KQ/r².**
- *What students do:* plug −3 µC into the formula and report a "negative field."
- *Why it's wrong:* the formula gives a magnitude; direction is assigned separately (toward/away).
- *How to avoid:* magnitudes in, direction after — the same discipline as Coulomb's law.

**Mistake 3 — Reversing the direction rule for negative charges.**
- *What students do:* draw the field of a negative charge pointing outward.
- *Why it's wrong:* field lines terminate on negative charges; E points **toward** a negative source.
- *How to avoid:* anchor with the dipole picture: lines leave +, enter −.

**Mistake 4 — Sending electrons along the field.**
- *What students do:* given E in +x, let an electron accelerate in +x.
- *Why it's wrong:* the electron's force is F = qE with q negative → force (and acceleration) opposite E.
- *How to avoid:* two-question check: "What's the charge's sign? Opposite sign ⇒ flip direction."

**Mistake 5 — Adding field magnitudes without directions.**
- *What students do:* in superposition problems, sum |E₁| + |E₂| regardless of orientation.
- *Why it's wrong:* fields are vectors; opposite directions cancel, same directions add (Example 8: both −x, so they add).
- *How to avoid:* draw both field directions at P *before* touching the calculator.

**Mistake 6 — Drawing crossing field lines.**
- *What students do:* sketch two field lines intersecting between charges.
- *Why it's wrong:* the tangent rule would give E two directions at one point — impossible.
- *How to avoid:* apply rule 2 as a hard constraint in every sketch.

**Mistake 7 — Claiming a dipole feels a net force in a uniform field.**
- *What students do:* compute F = qE on one charge and call it the dipole's force.
- *Why it's wrong:* the −q feels an equal, opposite force: net force zero — the effect is a **torque**.
- *How to avoid:* always ask "what does the *other* charge feel?" before answering for the dipole.

**Mistake 8 — Pointing p⃗ from +q toward −q.**
- *What students do:* reverse the dipole moment's direction.
- *Why it's wrong:* the convention is from **−q toward +q**; reversing it flips the torque's sense.
- *How to avoid:* "p points to the Positive charge" — from the minus to the plus.

**Mistake 9 — Confusing E and F (units and roles).**
- *What students do:* report a force in N/C or a field in newtons.
- *Why it's wrong:* E is N/C (force per charge, exists everywhere); F is N (acts on a specific charge).
- *How to avoid:* check units at the end of every answer.

---

## 8. LECTURE SUMMARY

# Lecture Summary

## What You Need to Know
- A charged object creates an electric field in the space around it; the field exerts forces on any charge placed in it.
- E = F/q₀ (N/C) — field = force per unit positive test charge; the test charge cancels, so the field belongs to the source.
- Point-charge field: E = K|Q|/r², inverse-square; direction away from +Q, toward −Q.
- Net field from several charges = vector sum (signed addition on a line).
- Particle in a field: a = E|q|/m; + charge accelerates along E, − charge opposite; a ∝ 1/m ⇒ aₑ ≫ aₐ → aₑ ≫ a_p (charge accelerators).
- Field lines: start on +, end on −; never cross; tangent = E direction; number of lines ∝ |charge|.
- Dipole = ±q separated by fixed 2a; moment p = q·2a from −q toward +q.
- Dipole in a uniform field: net force zero, torque τ = pE sinθ aligning it with the field — polarization; energy U = pE cosθ (course convention).

## Key Definitions
- **Electric field** → the condition of space around a charged object that exerts a force on any charge in it; measured as E = F/q₀.
- **Test charge q₀** → small positive charge used to probe the field; cancels from the measurement.
- **Electric field lines** → directed curves whose tangent gives E; begin on +, terminate on −; never intersect.
- **Electric dipole** → two equal, opposite charges at fixed separation 2a (cannot be separated).
- **Dipole moment p⃗** → vector from −q toward +q, magnitude p = q·2a.
- **Polarization** → the torque-driven alignment of a dipole with the field direction.

## Key Formulas
- **E = F/q₀** → definition (force per unit positive charge).
- **E = K|Q|/r²** → point-charge field magnitude.
- **E⃗_net = E⃗₁ + E⃗₂ + ⋯** → superposition.
- **a = E|q|/m** → particle acceleration in a field.
- **p = q·2a** → dipole moment magnitude.
- **τ = pE sinθ; τ⃗ = p⃗ × E⃗** → dipole torque.
- **U = pE cosθ** → dipole energy (source's convention).

## Important Ideas
- The field exists whether or not anything is there to feel it — the test charge is a probe, not a participant.
- Fields superpose exactly like forces; all of Lecture 2's sign-discipline transfers.
- Between a − charge and a + charge (negative on the left), the fields point the same way and reinforce.
- Electron vs. proton in the same field: same force magnitude (same |q|), wildly different accelerations (mass ratio ~1830).
- Zero net force does not mean nothing happens — the dipole still rotates.

## Common Mistakes
- Thinking the field depends on the test charge.
- Signed Q in E = KQ/r²; field drawn leaving a negative charge.
- Electrons accelerated along (instead of against) E.
- Adding field magnitudes without directions.
- Crossing field lines; p⃗ reversed; claiming net force on a dipole.

## Exam Focus
The concepts most likely to demand real understanding:
1. **Direction bookkeeping** — field directions from mixed-sign charges at points between/outside them, then signed superposition (Example 8 pattern).
2. **The sign flip for negative particles** — electron acceleration direction.
3. **The dipole's "zero force, nonzero torque"** paradox and τ = pE sinθ.
4. **Field-line rules** — especially justifying why lines cannot cross.

## 60-Second Review
A charge fills the space around it with an electric field. Probe it with a test charge: E = F/q₀ — the probe cancels, so the field is the source's property. Point charge: E = K|Q|/r², away from +, toward −, quarter-strength at double distance. Several charges: vector sum, signs along your axis. Drop a particle in: a = E|q|/m — positive along E, negative opposite, electrons outrun protons ~1800:1 (that's an accelerator). Field lines: leave +, enter −, never cross, tangent = E, count ∝ charge. Dipole (±q, separation 2a): p = q·2a from − to +; uniform field gives zero net force but torque pE sinθ that aligns it — polarization; energy pE cosθ.

---

## 9. DIFFICULT CONCEPTS

### Difficult Concept: The Field Concept Itself

**Why students struggle:** Coulomb's law looks like action at a distance — two charges "pull" each other with nothing in between. Accepting that the space itself carries a property (the field) that exists *without* any second charge requires a conceptual leap, not a formula.
**Simple explanation:** Don't ask "how does q₂ feel q₁?" Ask instead: "q₁ has modified the space around it; any charge that walks into that modified space gets pushed." The modification is the field.
**Intuitive analogy:** A temperature map of a room: every point has a temperature whether or not a thermometer is there. Dip a thermometer in (the test charge) and you *read* the value — the reading doesn't create the warmth.
**Step-by-step explanation:** (1) A source charge Q exists. (2) The space around it is now "charged territory": the field exists at every point. (3) Place a small positive q₀ at some point → it feels F. (4) Divide: E = F/q₀. (5) Remove q₀ → the field stays; a different charge placed there would feel a force scaled to itself (F = qE).
**Mini example:** At a point where E = 3 × 10⁵ N/C: a +2 µC charge feels 0.6 N; a +4 µC charge feels 1.2 N; no charge — no force, but E is still 3 × 10⁵ N/C.
**Misconception to avoid:** "The field needs a charge to act on." No — it needs a charge to *reveal* it.
**Difficulty:** HARD

### Difficult Concept: Field Direction Bookkeeping and Superposition

**Why students struggle:** Direction depends on *two* things — the source's sign (toward/away) *and* the source's position relative to the field point. Holding both at once under exam pressure produces flipped signs.
**Simple explanation:** Two questions per source: "What's its sign?" (toward −, away from +) and "Where is it relative to P?" — combine the answers into ± along your axis.
**Intuitive analogy:** Weather vanes around a fountain: each vane points according to the flow *at its own location*, not the fountain's center.
**Step-by-step explanation:** (1) Fix +x. (2) For each source: E = K|q|/r². (3) Sign rule: away from +, toward −. (4) Position rule: convert "away/toward" into ±x using geometry. (5) Add signed values. (6) Between a − on the left and a + on the right, both point −x → add.
**Mini example:** Example 8: E₁ (from −25 µC, left of P) → toward it → −x. E₂ (from +50 µC, right of P) → away from it → −x. Sum: 6.328 × 10⁸ N/C in −x.
**Misconception to avoid:** "The field at P between charges always partially cancels." Only when the two fields point opposite ways — between *like* charges, yes; between *unlike* charges, they add.
**Difficulty:** MEDIUM

### Difficult Concept: Negative Particles Accelerating Opposite to E

**Why students struggle:** E is *defined* with a positive test charge, so the field's direction "feels" like the direction of motion — but the force on a negative charge is antiparallel to E.
**Simple explanation:** The field's arrows show where a *positive* probe would go. An electron is the mirror image: it goes the other way, and being ~1830× lighter, it goes there much faster.
**Intuitive analogy:** Wind arrows on a map show where a leaf drifts; a helium balloon released in the same wind slides the opposite way.
**Step-by-step explanation:** (1) Identify E's direction. (2) Force: F = qE with the sign of q. (3) Positive q → F along E; negative q → F opposite E. (4) Acceleration follows F (Newton). (5) Magnitude: a = E|q|/m — mass matters independently.
**Mini example:** Example 8b: E in −x, electron → accelerates +x at 1.11 × 10²⁰ m/s²; a proton there would accelerate −x at only ~6 × 10¹⁶ m/s².
**Misconception to avoid:** "Electrons move along the field lines." They move *against* them (when free to accelerate).
**Difficulty:** MEDIUM

### Difficult Concept: The No-Crossing Rule for Field Lines

**Why students struggle:** Students accept the rule as memorized dogma without seeing why it's logically forced.
**Simple explanation:** A field line's tangent is E's direction. If two lines crossed, E at that single point would need two directions at once — and a charge placed there couldn't decide which way to go.
**Intuitive analogy:** Two one-way streets crossing at an intersection with contradictory signposts: traffic law forbids it; so does physics.
**Step-by-step explanation:** (1) Rule 3: tangent = direction of E. (2) E at a point is a single vector. (3) Two crossing lines ⇒ two tangents at one point ⇒ two directions for one E. (4) Contradiction ⇒ lines can never intersect, however close the charges.
**Mini example:** Two nearby equal positive charges: their outward line patterns bend around each other, merging smoothly — they never touch.
**Misconception to avoid:** "Close charges let their lines cross." No — the rule is absolute.
**Difficulty:** MEDIUM

### Difficult Concept: Dipole Torque — Zero Net Force, Real Rotation

**Why students struggle:** Newton's intuition says zero net force ⇒ no motion. The dipole violates that expectation: it rotates. The torque construction (force × normal distance, 2a sinθ) is also geometrically unfamiliar.
**Simple explanation:** Two equal, opposite forces that don't share a line of action form a couple: they can't translate the object, but they twist it. The twist grows with the misalignment angle.
**Intuitive analogy:** Both hands on a steering wheel, pushing with equal force in opposite directions: the car doesn't move, but the wheel turns. The more your hands are offset (bigger angle), the harder the twist.
**Step-by-step explanation:** (1) +q feels +qE along the field. (2) −q feels qE opposite. (3) Net force: qE − qE = 0. (4) Lines of action are separated by the normal distance 2a sinθ. (5) Each force contributes torque: τ = (qE)(2a sinθ) = pE sinθ. (6) The torque rotates p⃗ toward E⃗ — alignment = polarization. (7) At θ = 0: sinθ = 0 → no torque: the dipole rests aligned.
**Mini example:** Pedagogical example above: p = 2 × 10⁻⁸ C·m, E = 5 × 10⁵ N/C, θ = 30° → τ = 5 × 10⁻³ N·m; at θ = 90° the same dipole would feel τ = pE = 10⁻² N·m (maximum).
**Misconception to avoid:** "Equal and opposite forces always cancel everything." They cancel *translation* — not *rotation*.
**Difficulty:** HARD

### Difficult Concept: Dipole Potential Energy and the Angle θ

**Why students struggle:** Three angle-dependent quantities (τ ∝ sinθ, U ∝ cosθ) plus a convention-sensitive sign make θ bookkeeping easy to scramble.
**Simple explanation:** Two different functions of the same angle: torque is *biggest* when the dipole is perpendicular to the field (sin 90° = 1) and energy (course formula) is *smallest* there (cos 90° = 0). At alignment (θ = 0), the torque vanishes and U = pE.
**Intuitive analogy:** A weathervane: hardest to twist when it's broadside to the wind, calm when aligned.
**Step-by-step explanation:** (1) Identify θ: angle between the dipole axis and E. (2) Torque: τ = pE sinθ. (3) Energy: U = pE cosθ (course convention). (4) Evaluate at landmark angles: θ = 0 (τ = 0, U = pE); θ = 90° (τ = pE, U = 0). (5) Never mix the sin and cos between the two formulas.
**Mini example:** p = 2 × 10⁻⁸ C·m, E = 5 × 10⁵ N/C: at θ = 0 → τ = 0, U = 10⁻² J; at θ = 90° → τ = 10⁻² N·m, U = 0.
**Misconception to avoid:** Using cosθ in the torque formula or sinθ in the energy.
**Difficulty:** MEDIUM

---

## 10. VIDEO LESSON PLANS

*(Plans for the two HARD concepts.)*

### VIDEO 1

**VIDEO TITLE:** The Electric Field: Reading the Invisible

**TARGET CONCEPT:** The field concept — existence without a test charge; E = F/q₀; direction rules; superposition

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can explain what an electric field is, why it exists without a probe, compute E = F/q₀ and E = K|Q|/r², and assign directions correctly.

**HOOK:** "Coulomb told us *how hard* two charges push each other — but he left a question hanging: *how does a charge even know the other one is there?* Nothing touches. Nothing connects. This lecture's answer changed physics: the space itself is changed. Today you'll learn to read that change."

**EXPLANATION:**
1. The problem: action at a distance in Coulomb's law.
2. The answer: charge modifies space — the field exists at every point around a source.
3. The probe: small positive test charge q₀; measure F; divide by q₀ — the probe cancels.
4. The thermometer analogy hammered home.
5. Point-charge field: E = K|Q|/r²; direction rules; inverse-square link to Lecture 2.
6. Superposition: the same signed recipe, now without needing a target charge.

**VISUALS:**
- A charge alone in empty space, then a "heat map" of field values fading with distance.
- An animated thermometer/test charge dipping into points, reading F, then the division F/q₀ leaving E behind as the probe fades out.
- Direction arrows flipping when the source's sign flips (red ↔ blue).
- Example 7 on screen with the "toward the negative charge" arrow.

**EXAMPLE:** Example 7 (−3 µC at 30 cm → 3 × 10⁵ N/C toward the charge) plus a live probe demo with a bigger test charge showing E unchanged.

**COMMON MISTAKE:** Believing E depends on the test charge; signed Q in the formula.

**CHECK FOR UNDERSTANDING:** "A +4 µC test charge at point P feels 0.2 N. What is E at P — and what force would a +8 µC charge feel at the same point?"

**FINAL TAKEAWAY:** The field is the source's property, living in space; the test charge only reads it: E = F/q₀ = K|Q|/r².

---

### VIDEO 2

**VIDEO TITLE:** Zero Net Force, But It Still Spins: The Dipole

**TARGET CONCEPT:** Dipole moment, torque τ = pE sinθ, polarization, U = pE cosθ

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can explain why a dipole in a uniform field feels zero net force but a torque, compute p, τ, and U, and describe the alignment motion.

**HOOK:** "Here's a rule you've trusted since school: no net force, no motion. This little object breaks it. Two equal opposite charges, a uniform field — the forces cancel perfectly. And yet it spins. Let's find the missing ingredient."

**EXPLANATION:**
1. Build the dipole: ±q, separation 2a, bound together; moment p = q·2a from − to +.
2. Forces in a uniform field: +qE on one, −qE on the other → sum = zero.
3. The steering-wheel insight: equal, opposite, *offset* forces = a couple = pure rotation.
4. Geometry: normal distance between force lines = 2a sinθ → τ = pE sinθ.
5. Polarization: torque drives θ → 0; aligned dipole is calm (τ = 0).
6. Energy: U = pE cosθ (course convention); landmark values at θ = 0 and 90°.

**VISUALS:**
- Steering-wheel demo (two hands, equal opposite pushes, wheel turns).
- Dipole in a uniform field with offset force arrows; the gap between their lines of action highlighted as 2a sinθ, shrinking as the dipole rotates.
- A rotating θ-dial synced to live τ and U readouts (τ peaking at 90°, U peaking at 0°).
- The dipole animating into alignment and stopping.

**EXAMPLE:** The pedagogical example: q = 1 µC, 2a = 2 cm, E = 5 × 10⁵ N/C, θ = 30° → p = 2 × 10⁻⁸ C·m, τ = 5 × 10⁻³ N·m, U ≈ 8.66 × 10⁻³ J (clearly marked as constructed from the lecture's formulas).

**COMMON MISTAKE:** Reporting a net force for the dipole; pointing p⃗ from + to −; sin/cos swap between τ and U.

**CHECK FOR UNDERSTANDING:** "The same dipole sits at θ = 90°. Net force? Torque (in terms of p and E)? Energy (course formula)? Answer all three before the recap."

**FINAL TAKEAWAY:** Equal-and-opposite-but-offset forces give zero force and torque pE sinθ — the dipole rotates until it aligns with the field.

---

## 11. VIDEO SCRIPTS

### VIDEO SCRIPT 1 — The Electric Field: Reading the Invisible

**[0:00–0:30] Hook**
"Last time, Coulomb gave us a beautiful formula: two charges, a force, done. But he left something weird behind. Think about it — how does this charge *know* that charge is over there? Nothing touches. Nothing connects. No rope, no wire. And yet, push — instantly proportional to the charges, inverse-square in the distance. This lecture's answer to that mystery is one of the most useful ideas in all of physics: the space around a charge isn't empty. It's *changed*. And today you're going to learn to read that change."

**[0:30–2:00] Concept introduction**
"Here's the claim. Take a charge — any charge — and let it sit there. According to this picture, it fills the space around it with something called the **electric field**. The field exists at every point around the charge: near, far, everywhere. And its job is simple: if you ever place another charge in that region, the field grabs it and pushes it. So the force from Coulomb's law? In this new picture, it's a two-step process. Step one: the source charge creates a field. Step two: the field pushes whatever charge you drop into it. Now the obvious question: *how do we measure* something that's invisible and everywhere? That's where our probe comes in."

**[2:00–4:00] Visual explanation**
"Meet the test charge — a small positive charge we call q-naught. Here's the measurement: place q-naught at the point you care about. It feels a force F. Divide that force by the charge: **E equals F over q-naught**. Units: newtons per coulomb. That number — force per unit positive charge — is the field's strength at that point. Now the part everyone misses, so watch carefully: take the probe away. Does the field disappear? No! The field was there *before* the probe and it's there *after*. The test charge is like a thermometer. A thermometer reads a room's temperature — it doesn't *create* the warmth. Take the thermometer out, the room is still warm. Same here: q-naught *reads* the field; the field belongs to the source charge. And here's the beautiful confirmation: for a point source charge Q, Coulomb's law gives the force K-Q-q-naught over r-squared. Divide by q-naught — the probe cancels completely — and you get **E equals K-Q over r-squared**. The field depends on the source and the distance. Only. Direction rule: field points *away* from a positive charge, *toward* a negative charge. And notice the r-squared: the field inherits the inverse-square law — double the distance, the field drops to a quarter. Everything you practiced last lecture transfers."

**[4:00–6:00] Worked example**
"The lecture's own example. A charge of minus three microcoulombs, and a point P thirty centimeters away. Find the field. Magnitude first — and notice I write *absolute value*: E equals nine times ten to the nine, times three times ten to the minus six, divided by zero-point-three squared. Top: twenty-seven times ten to the three. Bottom: zero-point-zero-nine. E equals three times ten to the fifth newtons per coulomb. Direction: the source is *negative*, so the field points *toward* it — at P, the field arrow points from P straight at the charge. Now let me prove the probe-idea with numbers. Put a plus-two-microcoulomb test charge at P: it feels F equals q-E — two micro times three times ten to the five — zero point six newtons. Put a plus-four-microcoulomb there instead: one point two newtons. Different forces — but divide each by its own charge and you get the *same* three times ten to the five, every time. The field didn't care which probe I sent in. That's the whole point. And when several charges are present, each one contributes its own field, and the total is just the vector sum — the exact signed-recipe you already know from forces, except now you don't even need a charge sitting at P to ask the question."

**[6:00–7:00] Common mistake**
"Two mistakes dominate exams here. Mistake one: 'the field depends on what I put in it.' No. A bigger test charge feels a *bigger force* — but F over q gives the same E, always. The field is the source's property. Mistake two: shoving the sign into the formula. If you'd plugged minus-three microcoulombs into E equals K-Q-over-r-squared, you'd get a 'negative field' — meaningless. Magnitudes in; direction out — toward negative, away from positive. If your answer to 'find E' is a negative number, you've mixed the two jobs."

**[7:00–8:00] Quick student challenge**
"Your turn, two parts. Part one: a plus-four-microcoulomb test charge at point P feels a force of zero point two newtons. What is E at P? Part two: what force would a plus-eight-microcoulomb charge feel at that same point? Pause and do both. … Part one: E equals F over q — zero point two divided by four times ten to the minus six — five times ten to the fourth newtons per coulomb. Part two: F equals q-E — eight micro times five times ten to the fourth — zero point *four* newtons. Notice: the charge doubled, the force doubled, the field — never moved. If part two had asked for E, the answer would've been *identical* to part one."

**[8:00–8:30] Final recap**
"The electric field in thirty seconds. A charge modifies the space around it — that modification is real, it's everywhere around the source, and it exists whether or not anything is there to feel it. To *read* it: drop in a small positive test charge, measure the force, divide — E equals F over q-naught. For a point source: E equals K-Q over r-squared — away from plus, toward minus, quarter strength at double distance. Multiple charges: add the fields as vectors. The field is the property of the *source* — the probe just takes the reading."

---

### VIDEO SCRIPT 2 — Zero Net Force, But It Still Spins

**[0:00–0:30] Hook**
"Here's a rule you've trusted since your first physics class: no net force means no motion. I'm about to show you an object where the forces cancel *perfectly* — plus F here, minus F there, sum exactly zero — and the thing spins anyway. It's called an electric dipole, it's everywhere in physics and chemistry, and understanding it means upgrading your intuition about what forces can do. Thirty seconds in, and the rule you trusted gets an asterisk."

**[0:30–2:00] Concept introduction**
"First, the object. An electric dipole is two charges — equal magnitude, opposite sign, plus q and minus q — held a fixed distance apart. Call the separation two-a; the pair is bound and can't be pulled apart. To describe it, we define one vector: the **dipole moment**, p. Its magnitude is the charge times the separation: **p equals q times two-a**. Its direction: from the *negative* charge toward the *positive* charge, along the axis. Burn that direction in — from minus to plus — because half the errors on dipole problems are just a reversed arrow. Now put this dipole into a uniform electric field, E, and let the axis sit at some angle theta to the field. What happens? Plus q feels a force q-E along the field. Minus q feels a force q-E *against* the field. Equal magnitudes, opposite directions. Add them: zero. The dipole as a whole goes nowhere. And yet — look at it — the forces aren't acting along the same line. They're pulling on opposite ends of a rigid object."

**[2:00–4:00] Visual explanation**
"You already know this situation from real life: a steering wheel. Both hands push with equal force, in opposite directions. The car doesn't lurch forward or back — the forces cancel — but the wheel *turns*. Equal, opposite, and *offset* forces form what's called a couple: zero translation, pure rotation. For the dipole, the geometry gives us the torque directly. Torque is force times the *normal* distance between the two force lines — the perpendicular gap. Look at the picture: that gap is two-a times sine theta — it shrinks as the dipole rotates toward alignment. So: torque equals q-E times two-a sine theta. And since q times two-a is exactly p: **torque equals p-E sine theta**. Vector form: tau equals p cross E. Check the landmarks: theta equals ninety degrees — dipole broadside to the field — sine is one, torque is maximum: p-E. Theta equals zero — dipole aligned with the field — sine is zero, torque vanishes. And *that's* the motion: the torque swings the dipole toward alignment with the field. That alignment process has a name — **polarization** — the dipole polarizes, lining up with E. One more quantity: the source gives the dipole's potential energy as **U equals p-E cosine theta** — note it's *cosine* here, sine in the torque, and use your course's formula exactly as given."

**[4:00–6:00] Worked example**
"Numbers — the lecture gives the formulas, so let's build one example and run it end to end. Take q equal to one microcoulomb on each end, separation two centimeters, sitting in a field of five times ten to the fifth newtons per coulomb, at thirty degrees. Step one, the moment: p equals q times two-a — one times ten to the minus six, times zero point zero two — two times ten to the minus eight coulomb-meters. Step two, the force on each charge: q-E — one micro times five times ten to the five — zero point five newtons on each end, opposite directions. Net force: zero point five minus zero point five — zero, exactly as promised. Step three, torque: p-E sine theta — two times ten to the minus eight, times five times ten to the five, times sine thirty, which is zero point five — five times ten to the minus three newton-meters. Step four, energy: p-E cosine thirty — two times ten to the minus eight times five times ten to the five times zero point eight six six — about eight point seven times ten to the minus three joules. Every number came from two formulas: sine for the twist, cosine for the energy. Keep them straight and dipoles are free points."

**[6:00–7:00] Common mistake**
"Three errors to dodge. Error one — the big one: 'the forces are equal and opposite, so nothing happens.' Translation: yes, zero. Rotation: absolutely not. Never answer 'nothing' for a dipole in a uniform field — the correct answer is *torque*. Error two: pointing the moment from plus toward minus. It's the reverse: **from minus to plus**. Flip it and your torque comes out with the wrong sense — the dipole would seem to rotate *away* from alignment, which it never does. Error three: swapping the trig functions — cosine in the torque, sine in the energy. Anchor it: torque is *largest* at ninety degrees, so it carries the sine; energy is *largest* at alignment in this course's convention, so it carries the cosine. Maximum twist and maximum energy never live at the same angle — that asymmetry is your memory hook."

**[7:00–8:00] Quick student challenge**
"Same dipole — p equals two times ten to the minus eight coulomb-meters — same field, five times ten to the fifth — but now at theta equals ninety degrees. Three answers, fast: net force? Torque? Energy, course formula? Pause. … Net force: still zero — that never changes in a uniform field. Torque: p-E sine ninety — sine ninety is one — so torque equals p-E: two times ten to the minus eight times five times ten to the fifth — one times ten to the minus *two* newton-meters. The maximum possible twist for this dipole. Energy: p-E cosine ninety — cosine ninety is zero — energy equals zero. So at ninety degrees: maximum torque, zero energy. At zero degrees: zero torque, maximum energy. Two opposite corners of the same physics."

**[8:00–8:30] Final recap**
"The dipole in thirty seconds. Two equal opposite charges, separation two-a; moment p equals q-two-a pointing minus-to-plus. Uniform field: forces cancel — net force zero — but they act on opposite ends, so the dipole feels a torque: p-E sine theta. That torque rotates it toward alignment with the field — that's polarization. Aligned, the torque dies; the energy, in this course's formula, is p-E cosine theta. Zero net force doesn't mean nothing happens — it means nothing *translates*. The spin is the story."

---

## 12. PRACTICE QUESTIONS

*(Student-facing questions. Instructor keys are for platform use and must not be displayed with the question.)*

### LEVEL 1 — UNDERSTAND

**Q1.** Define the electric field in words and write its defining equation with the correct unit.
> *Instructor key — Answer:* The field exists in the region of space around a charged object and exerts a force on any charge placed in it; E = F/q₀ with q₀ a positive test charge; unit N/C. *Skill:* field definition. *Difficulty:* EASY.

**Q2.** State the direction of the electric field (a) surrounding an isolated positive charge; (b) surrounding an isolated negative charge.
> *Instructor key — Answer:* (a) radially away from the charge; (b) radially toward the charge. *Skill:* direction rules. *Difficulty:* EASY.

**Q3.** List the four rules that electric field lines must obey.
> *Instructor key — Answer:* (1) begin on + and terminate on − charges; (2) never intersect; (3) tangent at any point = direction of E there; (4) number of lines leaving/entering ∝ charge magnitude. *Skill:* field-line rules. *Difficulty:* EASY.

**Q4.** Why does an electron and a proton in the same electric field have aₑ ≫ a_p, even though the forces on them have equal magnitude?
> *Instructor key — Answer:* a = E|q|/m; both have |q| = e, but mₑ ≪ m_p (factor ~1830), so the electron's acceleration is ~1830× larger. (Source links this to charge accelerators.) *Skill:* a ∝ 1/m. *Difficulty:* EASY–MEDIUM.

**Q5.** In which direction is the dipole moment p⃗ of an electric dipole drawn, and what is its magnitude in terms of q and the separation?
> *Instructor key — Answer:* From −q toward +q along the axis; p = q·2a where 2a is the charge separation. *Skill:* dipole definition. *Difficulty:* EASY.

**Q6.** True or false, with a one-sentence justification: two electric field lines may cross if the two charges are extremely close together.
> *Instructor key — Answer:* False — at a crossing, E would have two directions at one point, contradicting the tangent rule; the no-crossing rule is absolute. *Skill:* field-line logic. *Difficulty:* MEDIUM.

### LEVEL 2 — APPLY

**Q7.** Calculate the magnitude and direction of the electric field at a point 0.5 m from a +2 µC charge.
> *Instructor key — Answer:* E = (9 × 10⁹)(2 × 10⁻⁶)/(0.5)² = 7.2 × 10⁴ N/C, directed away from the charge. *Skill:* point-charge field. *Difficulty:* EASY–MEDIUM.

**Q8.** An electron is placed at the point of Q7. Find the magnitude and direction of its acceleration. (mₑ = 9.1 × 10⁻³¹ kg)
> *Instructor key — Answer:* a = E|e|/mₑ = (7.2 × 10⁴)(1.6 × 10⁻¹⁹)/(9.1 × 10⁻³¹) ≈ 1.27 × 10¹⁶ m/s², directed opposite to E (toward the +2 µC charge). *Skill:* particle acceleration + sign flip. *Difficulty:* MEDIUM.

**Q9.** A dipole has charges ±3 µC separated by 4 cm. It is placed in a uniform field of 2 × 10⁵ N/C with its axis perpendicular to the field. Find p, the net force on the dipole, and the torque on it.
> *Instructor key — Answer:* p = (3 × 10⁻⁶)(0.04) = 1.2 × 10⁻⁷ C·m; net force = 0 (equal and opposite forces in a uniform field); τ = pE sin90° = (1.2 × 10⁻⁷)(2 × 10⁵) = 2.4 × 10⁻² N·m. *Skill:* dipole quantities. *Difficulty:* MEDIUM.

**Q10.** For the dipole of Q9 at 90°, evaluate the dipole's energy using the course formula.
> *Instructor key — Answer:* U = pE cos90° = 0. *Skill:* U = pE cosθ. *Difficulty:* EASY.

**Q11.** Two charges lie on the x-axis: q₁ = +5 µC at the origin and q₂ = −3 µC at x = 0.1 m. Find the net electric field (magnitude and direction) at point P, x = 0.3 m.
> *Instructor key — Answer:* E₁ = (9 × 10⁹)(5 × 10⁻⁶)/(0.3)² = 5 × 10⁵ N/C, away from +q₁ → +x. E₂ = (9 × 10⁹)(3 × 10⁻⁶)/(0.2)² = 6.75 × 10⁵ N/C, toward −q₂ (which is left of P) → −x. Net = 5 × 10⁵ − 6.75 × 10⁵ = −1.75 × 10⁵ → **1.75 × 10⁵ N/C in −x**. *Skill:* superposition outside the pair. *Difficulty:* MEDIUM–HARD.

---

## 13. TRANSFER QUESTIONS

### LEVEL 3 — TRANSFER

**Q12.** Two positive charges, +4 µC and +16 µC, are fixed 30 cm apart on a line. Using the direction rules for fields (not forces), find the point between them where the net electric field is zero.
> *Instructor key — Answer:* Between like charges the fields oppose; balance K·4/x² = K·16/(0.3−x)² → 2/x = 4/(0.3−x) → 2(0.3−x) = 4x → x = 0.1 m from the 4 µC charge (0.2 m from the 16 µC — closer to the smaller charge, mirroring Lecture 2's force result). *Skill:* transferring the equilibrium procedure from forces to fields. *Difficulty:* HARD.

**Q13.** In a certain region the electric field is 4 × 10⁴ N/C pointing in +x. An electron and a proton are released from rest there. (a) Compare the directions of their accelerations. (b) Compute the ratio aₑ/aₐ → aₑ/a_p. (c) State the application the source connects to this fact.
> *Instructor key — Answer:* (a) Electron accelerates −x (opposite E); proton +x (along E). (b) aₑ/a_p = m_p/mₑ = (1.67 × 10⁻²⁷)/(9.1 × 10⁻³¹) ≈ 1830. (c) Charge accelerators (exploiting aₑ ≫ a_p). *Skill:* sign flip + mass scaling + application. *Difficulty:* MEDIUM.

**Q14.** A dipole is released from rest at θ = 90° in a uniform field. Describe its subsequent motion in terms of torque and alignment, and state its torque and energy (course formula) at the moment of release and when it stops rotating.
> *Instructor key — Answer:* At release: τ = pE (maximum), U = pE cos90° = 0. The torque rotates p⃗ toward E⃗ (polarization); θ decreases, sinθ decreases, so the torque shrinks. It stops rotating at θ = 0: τ = 0, U = pE. Motion: pure rotation from broadside to aligned. *Skill:* qualitative dipole dynamics. *Difficulty:* MEDIUM–HARD.

**Q15.** Using rule 3 (tangent = direction of E) and the fact that E is a single vector at each point, prove that field lines can never intersect — in your own words, as you would explain it to a classmate.
> *Instructor key — Answer:* At an intersection point, two lines would each have their own tangent; by rule 3 each tangent is the direction of E; so E would have two different directions at one point — impossible for a single vector. Hence no intersections, regardless of charge proximity. *Skill:* reasoning from definitions. *Difficulty:* MEDIUM.

**Q16.** A student claims: "At the exact midpoint between two equal positive charges, the field is huge because both charges contribute." Evaluate the claim using superposition and the direction rules.
> *Instructor key — Answer:* False — at the midpoint, each charge produces equal-magnitude fields pointing in *opposite* directions (each away from its own charge), so E_net = 0. Magnitudes are large but the vector sum vanishes. (A positive test charge there would be in unstable equilibrium.) *Skill:* direction-based cancellation reasoning. *Difficulty:* MEDIUM.

---

## 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | Field definition and E = F/q₀, point-charge field with direction rules, superposition, particle motion incl. accelerators note, all four field-line rules, dipole (moment, torque, polarization, energy), Examples 7 and 8 all present. |
| Mathematical formulas correct | ✅ | All formulas and numeric results verified against the source (3 × 10⁵ N/C; 5.625 × 10⁸; 0.703 × 10⁸; 6.328 × 10⁸; 1.11 × 10²⁰ m/s²). Dipole energy presented **exactly as the source states it** (U = pE cosθ), with a clearly-marked pedagogical convention note. |
| Technical terminology preserved | ✅ | Electric field, test charge, field lines, tangent, electric dipole, dipole moment, torque, polarization, N/C, charge accelerators. |
| Explanations in original language | ✅ | Fully rewritten; only formulas and short standard definitions kept canonical. |
| Understandable to a first-year student | ✅ | Thermometer, temperature-map, weather-vane, steering-wheel analogies — all marked pedagogical. |
| Difficult concepts explicitly identified | ✅ | 6 concepts with ratings; 2 rated HARD (field concept, dipole torque) with full video plans and scripts. |
| Common misconceptions identified | ✅ | 9 mistakes with what/why/how, echoed in videos and difficult-concept entries. |
| Examples actually teach the concept | ✅ | Both source examples worked step-by-step; dipole numeric example clearly marked as constructed from the source's formulas. |
| Practice progresses understand → apply → transfer | ✅ | Level 1 (6), Level 2 (6), Level 3 (5) incl. force→field equilibrium transfer, electron/proton comparison, dipole dynamics. Self-check (9) without revealed answers. |
| No unsupported claims added | ✅ | Accelerator fact, formulas, and Example values from the source. Dipole example, analogies, and the convention note explicitly flagged. Header date discrepancy noted rather than "corrected." Course title marked [SOURCE DOES NOT SPECIFY]. |
| No large verbatim reproduction | ✅ | Structure and numbers preserved; wording fully rewritten. |
| Suitable for direct web integration | ✅ | Clean Markdown, metadata, flow position, instructor keys separated from student-facing content. |

**ARETE placement note:** Deploy as the third LEARN lesson of Module 1, gated on Lectures 1–2. Attach Video 1 to the field-concept topic and Video 2 to the dipole topic. Enable REMEDIATE on mistakes 1, 4, and 7 (test-charge misconception, electron direction flip, dipole net-force claim). Q11 and Q12 make strong PROVE-stage items; the field concept here is the direct prerequisite for Lecture 4's flux and E = −ΔV/d — flag it as high-stakes in the mastery map.

---

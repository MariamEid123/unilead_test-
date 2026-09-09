# ARETE — Content Transformation Output

---

## 1. SOURCE ANALYSIS

**Source document:** Phy 211 Lecture Notes — Lecture 1, Fall 2024, AIU (Dr. Ashraf Mousa Abdelwahed), 8 pages.

| Item | Finding |
|---|---|
| Course | Phy 211 — Physics [full course title: SOURCE DOES NOT SPECIFY] |
| Chapter | Chapter 1 — Electric Force & Electric Field |
| Lecture | Lecture 1 (first lecture of the chapter) |
| Scope note | Despite the chapter title, this lecture covers **only** electric charge, its properties, quantization, and the three charging methods. Coulomb-force and field calculations are not in this document. |

**Main topics**
1. The fundamental unit of electric charge (Millikan, 1909)
2. Properties of electric charge (types, attraction/repulsion, SI unit)
3. Quantization of charge: Q = ±Ne
4. Counting electrons in a given charge
5. Charge unit conversions (mC, μC, nC, pC)
6. Charging by rubbing (friction) — for insulators
7. Charging by induction — for conductors
8. Charging by conduction — for conductors; charge sharing between spheres

**Important definitions:** elementary charge *e*; quantization; repulsive vs. attractive force; the coulomb (C); rubbing, induction, conduction as charging methods. (The terms *conductor* and *insulator* are used but not formally defined in the source.)

**Important formulas:** e = 1.6 × 10⁻¹⁹ C; Q = ±Ne; N = Q/(±e); Q ∝ r; q′ = q_t / r_t; q_i′ = q′ × r_i; ratio relations q₁′/q₂′ = r₁/r₂.

**Worked examples in source:** Example 1 (−64 μC → number of electrons), Example 2 (−1 mC, −1 μC, −1 nC, −1 pC), Example 3 (three touching spheres, radii 3 m, 2 m, 1 m).

**Procedures:** the multi-step induction procedure (bring rod near → electrons shift → ground the far end → disconnect ground → remove rod); conduction charge-sharing procedure.

**Prerequisites (inferred):** atomic structure (electrons, protons); SI metric prefixes; basic algebra; qualitative idea of conductors vs. insulators.

**Dependencies:** None — this is Lecture 1 and the foundation for later material in Chapter 1 (electric force and field) [not included in this document].

**Source notes for transparency:**
- Learning objectives are not explicitly stated in the source; the ones below are inferred from the content.
- Example 3 contains a small typographical artifact ("10 + 20 − 10q"); the source's own arithmetic confirms the intended total is 10 + 20 − 10 = 20 C. This interpretation is used.
- Biographical dates for Millikan appear in the source; only the 1909 discovery is used here, as it is the academically relevant fact.

---

## 2. COURSE / MODULE / LESSON METADATA

- **COURSE:** Phy 211 — Physics (full title [SOURCE DOES NOT SPECIFY]; Chapter 1: Electric Force & Electric Field)
- **MODULE:** Chapter 1 — Electric Force & Electric Field (Module 1: Foundations of Electrostatics)
- **LESSON:** Lecture 1 — Electric Charge: Properties, Quantization, and Charging Methods
- **TOPICS:** nature of charge; charge quantization; electron counting; unit prefixes; charging by friction, induction, and conduction; charge sharing between conducting spheres
- **PREREQUISITES:** atomic structure (proton/electron); SI prefixes; algebra; qualitative conductor/insulator distinction
- **COMPETENCIES:** apply Q = ±Ne to count charge carriers; convert charge units; describe and distinguish the three charging methods; predict the sign produced by each method; compute final charges on touching conducting spheres
- **DIFFICULTY:** Overall EASY–MEDIUM (introductory), containing two HARD sub-concepts: charging by induction, and radius-proportional charge sharing
- **ESTIMATED STUDY TIME:** ~75 minutes (≈45 min lesson + ≈30 min practice)

**Position in the ARETE learning flow (LEARN → PRACTICE → PROVE → REMEDIATE → RETRY → TRANSFER → MASTER):**
This lesson is the **LEARN** entry point of the entire course and supports **PRACTICE** through worked examples and drill questions. It supplies the vocabulary and rules that every later stage of Chapter 1 (force, field) will assume, so it feeds directly into future TRANSFER tasks.

---

## 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. State the value of the fundamental unit of charge, e = 1.6 × 10⁻¹⁹ C, and explain what Millikan's 1909 discovery revealed about charge.
2. List the key properties of electric charge, including the two types, the attraction/repulsion rules, and the SI unit (coulomb).
3. Explain what "charge is quantized" means and apply Q = ±Ne.
4. Calculate the number of electrons (or protons) corresponding to a given total charge, handling signs correctly.
5. Convert fluently between coulombs, milli-, micro-, nano-, and picocoulombs.
6. Describe charging by rubbing, and predict the sign of each object for glass–silk and plastic–wool pairs.
7. Describe the full step-by-step induction procedure, including the role of grounding, and predict the sign of the induced charge.
8. Describe charging by conduction and predict the resulting sign.
9. Apply Q ∝ r, q′ = q_t/r_t, and q_i′ = q′ × r_i to find the final charge on conducting spheres after contact, including cases with negative charges.

---

## 4. WEB-READY LESSON

# Lecture 1 — Electric Charge: Properties, Quantization, and Charging Methods

*(The full formula table, step-by-step worked examples, and the common-mistakes gallery in the sections that follow are part of this lesson in ARETE.)*

## Prerequisites
The student should already understand:
- The basic structure of the atom (protons and electrons)
- SI prefixes and powers of ten
- Elementary algebra
- The qualitative difference between a conductor (charges move freely) and an insulator (charges stay put) *(pedagogical clarification — the terms are used in the source but not defined there)*

---

### 1. The Fundamental Unit of Charge

#### Core Idea
Electric charge is not continuous. It comes in identical, indivisible "packets," and every charge ever measured is a whole-number multiple of one tiny unit called the elementary charge, e.

#### Explanation
In 1909, Robert Millikan discovered that whenever an object becomes charged, the amount of charge it carries is always a multiple of one fundamental unit, denoted e (the "electron charge"):

> **e = 1.6 × 10⁻¹⁹ C**

The symbol for charge is q or Q, and the SI unit is the coulomb (C). To grasp how small e is: one full coulomb corresponds to about 6.25 × 10¹⁸ elementary units — a number you can verify yourself from the counting method in Topic 3.

#### Example
A charge of +3.2 × 10⁻¹⁹ C is physically meaningful: it equals exactly 2e. A charge of +2.4 × 10⁻¹⁹ C is not — it would be 1.5e, and half-packets don't exist.

#### Key Point
Charge is built from identical units of magnitude e = 1.6 × 10⁻¹⁹ C. There is no such thing as a fraction of an elementary charge.

---

### 2. Properties of Electric Charge

#### Core Idea
There are exactly two kinds of charge, they interact by simple rules, and charge is always measured in multiples of e.

#### Explanation
The six essential properties from the lecture:

1. **Two types exist:** positive (+) and negative (−).
2. **The electron is the smallest negative charge:** q_e = −e = −1.6 × 10⁻¹⁹ C.
3. **The proton is the smallest positive charge:** q_p = +e = +1.6 × 10⁻¹⁹ C.
4. **Interaction rule:** same-sign charges repel each other; opposite-sign charges attract each other.
   - **Repulsive force** = the push between similar (same-sign) charges.
   - **Attractive force** = the pull between opposite-sign charges.
5. **SI unit:** the coulomb (C).
6. **Quantization:** any total charge is an integer multiple of e:

   **Q = ±Ne** (Q = total charge, N = number of e's, e = fundamental charge)

   So the allowed values are Q = ±1e, ±2e, ±3e, … — nothing in between.

#### Example
Two protons (both +) push apart; a proton and an electron pull together. A dust grain with charge −5e carries five electrons' worth of negative charge — never −4.5e.

#### Key Point
Like repels, unlike attracts, and every charge in nature is Q = ±Ne with N a whole number.

---

### 3. Quantization in Action: Counting Electrons

#### Core Idea
Rearranging Q = ±Ne turns any charge into a count of elementary particles: N = Q/(±e).

#### Explanation
If an object carries a negative total charge Q, the excess electrons number

**N = Q / (−e)**

Both negatives cancel, so N — a count of objects — always comes out positive. Getting a *negative* number of electrons is a guaranteed sign of a sign-handling error.

#### Example
A sphere carries −64 μC. Convert, then divide:
N = (−64 × 10⁻⁶) / (−1.6 × 10⁻¹⁹) = 4 × 10¹⁴ electrons.
(The full step-by-step version is in the Worked Examples section.)

#### Key Point
Number of excess electrons = total charge ÷ elementary charge. Take magnitudes if the signs confuse you; a count is always positive.

---

### 4. Units of Charge: The Prefix Staircase

#### Core Idea
Charges in real problems are usually tiny fractions of a coulomb, so four prefixes do most of the work.

#### Explanation

| Unit | Symbol | Value |
|---|---|---|
| 1 millicoulomb | 1 mC | 10⁻³ C |
| 1 microcoulomb | 1 μC | 10⁻⁶ C |
| 1 nanocoulomb | 1 nC | 10⁻⁹ C |
| 1 picocoulomb | 1 pC | 10⁻¹² C |

Each step down the staircase divides the charge by 1000 — and therefore divides the electron count by 1000 too. That's why −1 mC contains 6.25 × 10¹⁵ electrons, −1 μC contains 6.25 × 10¹², and so on: the count slides in step with the unit.

#### Example
−1 pC is the smallest of the set, yet it still represents 6.25 × 10⁶ — over six million — electrons.

#### Key Point
m → μ → n → p steps down by three powers of ten each time. Misreading μ as milli is the classic unit blunder.

---

### 5. Charging Method I: Rubbing (Friction) — for Insulators

#### Core Idea
Rubbing two different materials together transfers electrons from one to the other, leaving one positive and the other negative.

#### Explanation
When a **glass rod is rubbed with silk**, electrons move from the rod to the silk. Losing electrons leaves the rod with a **net positive** charge; gaining them leaves the silk **net negative**.

When a **plastic rod is rubbed with wool**, electrons move the other way — from wool to plastic. The plastic becomes **net negative** and the wool becomes **net positive**.

In both cases the total charge is unchanged; it has only been redistributed between the two objects. Rubbing is the method used for charging **insulators**.

#### Example
After rubbing plastic with wool, the plastic rod (negative) can pick up tiny bits of paper, while the wool patch carries an equal positive charge.

#### Key Point
Friction moves *electrons only*. The object that loses electrons becomes positive; the one that gains them becomes negative.

---

### 6. Charging Method II: Induction — for Conductors

#### Core Idea
A conductor can be given a net charge **without any contact at all**: a nearby charged object rearranges the conductor's free charges, and a temporary ground connection lets electrons enter or leave.

#### Explanation
The full procedure (charging a neutral metal sphere positively):

1. Rub a plastic rod on wool so the rod is negative.
2. Bring the rod **near** (not touching) a neutral metal sphere mounted on an insulating stand.
3. The rod repels the sphere's free electrons to the **far end** and attracts the sphere's positive charge to the **near end**. The sphere is still neutral overall — its charge has merely been redistributed.
4. Connect the **far end to the Earth** with a wire. The repelled electrons flow down into the ground, while the positives remain held near the rod.
5. **Disconnect the ground wire first**, then remove the rod. The sphere is left with a **net positive** charge.

The sign rules that follow:

- To charge an object **positively** by induction → use a **negative** charging object.
- To charge an object **negatively** by induction → use a **positive** charging object.

In other words, **induction always leaves the target with the opposite sign of the charging object.**

#### Example
A negatively charged rod near a grounded sphere: electrons flee into the Earth, the ground wire is cut, the rod is removed — the sphere ends positive even though the rod never touched it and never gave it a single charge.

#### Key Point
Induction = no contact + opposite-sign result. The electrons that move travel between the sphere and the **ground**, never between the rod and the sphere.

---

### 7. Charging Method III: Conduction — for Conductors

#### Core Idea
Conduction charges by **direct contact**: part of the charge flows onto the neutral object, which ends up with the **same sign** as the charging object.

#### Explanation
When a charged object touches a neutral one, some of its charge flows over, leaving the previously neutral object partially charged. How much transfers depends on the **shapes** of the two bodies.

The sign rules (opposite of induction's):

- To charge an object **positively** by conduction → use a **positive** object.
- To charge an object **negatively** by conduction → use a **negative** object.

**Special case — identical spheres:** two identical metal spheres on insulating mounts share the charge **equally**.

**General case — spheres of different sizes:** the shared charge is proportional to the radius:

> **Q ∝ r**

Bigger sphere → bigger share. The machinery for computing this:

- Shared charge per unit radius after contact:
  **q′ = q_t / r_t = (q₁ + q₂ + q₃ + ⋯) / (r₁ + r₂ + r₃ + ⋯)**
- Final charge on the i-th sphere:
  **q_i′ = q′ × r_i**
- Ratios: q₁′/q₂′ = r₁/r₂, q₁′/q₃′ = r₁/r₃, q₂′/q₃′ = r₂/r₃

*(Pedagogical note, not in source: an intuitive picture is two connected water tanks — the "level" equalizes, but the bigger tank always holds more total water. A full explanation via electric potential comes later in the course.)*

#### Example
Spheres with radii 3 m, 2 m, and 1 m carrying 10 C, 20 C, and −10 C are all touched together. Total charge = 20 C, total radius = 6 m, so q′ = 20/6 C per meter. Final charges: 10 C, 6.667 C, and 3.333 C. (Full solution in the Worked Examples section.)

#### Key Point
Contact ⇒ same sign as the charger ⇒ and the split follows the radii, not a 50/50 coin flip. Only identical spheres end up equal.

---

### Key Takeaways

- Charge comes only in multiples of e = 1.6 × 10⁻¹⁹ C: Q = ±Ne.
- Electron: −e. Proton: +e. Like charges repel; opposite charges attract.
- Unit of charge is the coulomb; typical problem charges use mC (10⁻³), μC (10⁻⁶), nC (10⁻⁹), pC (10⁻¹²).
- To count electrons: divide the charge by e (magnitudes; a count is positive).
- Three charging methods: rubbing (insulators), induction (conductors, no contact), conduction (conductors, contact).
- Rubbing transfers electrons: glass→silk leaves glass positive; wool→plastic leaves plastic negative.
- Induction gives the **opposite** sign; grounding lets electrons escape to (or arrive from) the Earth; cut the ground before removing the rod.
- Conduction gives the **same** sign; identical spheres split equally; unequal spheres split in proportion to radius, Q ∝ r.
- For touching spheres: q′ = q_t/r_t, then q_i′ = q′ × r_i — and the final charges must add back to the initial total.

### Self-Check (answers are not shown — attempt these before checking)

1. Why can no object in the universe carry a charge of exactly 2.4 × 10⁻¹⁹ C?
2. A plastic rod is rubbed with wool. What sign does each object end up with, and which particles actually moved?
3. Calculate the number of excess electrons on an object carrying −3.2 μC.
4. In the induction procedure, why must the ground wire be disconnected **before** the rod is taken away?
5. Two conducting spheres with radii 4 m and 2 m touch and then separate. Which one holds more charge, and what is the ratio of their charges?
6. State the essential difference between induction and conduction in terms of physical contact, and the difference in the resulting sign of the charged object.
7. You want to charge a metal sphere **negatively** by induction. What sign of charging object do you need?
8. Convert 0.75 μC into nanocoulombs.
9. Using Q ∝ r, explain why two identical spheres always share charge equally after contact.

---

## 5. FORMULAS

### F1 — Elementary charge
**e = 1.6 × 10⁻¹⁹ C**
- **Meaning:** the smallest possible magnitude of charge; magnitude of the electron's and proton's charge.
- **When used:** every quantization or electron-counting problem.
- **Interpretation:** charge is "lumpy," not smooth.
- **Assumptions:** value used as given in this course (2 significant figures).

### F2 — Electron and proton charges
**q_e = −e = −1.6 × 10⁻¹⁹ C  |  q_p = +e = +1.6 × 10⁻¹⁹ C**
- **Meaning:** the smallest negative and smallest positive charges in nature.
- **When used:** reasoning about sign in any charging process.
- **Interpretation:** the magnitudes are identical; only the sign differs.

### F3 — Quantization of charge
**Q = ±Ne**
- **Q:** total charge (C) — **N:** a whole number of elementary charges (electrons or protons) — **e:** 1.6 × 10⁻¹⁹ C.
- **When used:** checking whether a charge is physically possible; counting charge carriers.
- **Interpretation:** allowed charges are ±1e, ±2e, ±3e, … — N must be an integer.
- **Assumptions:** N counts particles, so it can never be fractional or negative in a valid answer.

### F4 — Counting electrons
**N = Q / (±e)**
- **Meaning:** number of excess (or missing) electrons for a given charge.
- **When used:** whenever a charge is given and a particle count is requested.
- **Interpretation:** for a negative Q divide by −e; the two minus signs cancel, giving a positive N.
- **Assumptions:** the object's charge comes only from excess/deficit electrons.

### F5 — Unit conversions
**1 mC = 10⁻³ C, 1 μC = 10⁻⁶ C, 1 nC = 10⁻⁹ C, 1 pC = 10⁻¹² C**
- **When used:** before any calculation involving a prefixed charge.
- **Interpretation:** each prefix step changes both the charge and the electron count by a factor of 1000.

### F6 — Charge per unit radius after contact
**q′ = q_t / r_t = (q₁ + q₂ + q₃ + ⋯) / (r₁ + r₂ + r₃ + ⋯)**
- **q′:** charge per unit radius (C/m) shared by all spheres after contact — **q_t:** total (algebraic) charge — **r_t:** sum of radii — **q₁, q₂, q₃:** charges before contact — **r₁, r₂, r₃:** radii of spheres 1, 2, 3.
- **When used:** conducting spheres brought into contact with one another.
- **Interpretation:** after contact every sphere carries the same charge-per-radius; multiply by each radius to get its share.
- **Assumptions:** all objects are conducting spheres in simultaneous contact; negative charges enter the sum with a minus sign; charge-sharing proportional to radius (Q ∝ r) is the model used in this course.

### F7 — Final charge on each sphere
**q_i′ = q′ × r_i  (i = 1, 2, 3, …)**
- **Meaning:** the i-th sphere's charge after contact = shared value × its radius.
- **When used:** immediately after computing q′.
- **Interpretation:** bigger sphere → bigger final charge.
- **Assumptions:** same as F6.

### F8 — Ratio relations
**q₁′/q₂′ = r₁/r₂  (and likewise for any pair)**
- **When used:** quick comparisons without computing the totals.
- **Interpretation:** final charges stand in the same ratio as the radii.

### F9 — Proportionality
**Q ∝ r**
- **Meaning:** for spheres in contact, the charge retained is proportional to the radius.
- **Interpretation:** this generalizes "identical spheres share equally" (equal radii ⇒ equal shares).
- **Assumptions:** spherical conductors; the transfer proportion generally depends on the objects' shapes.

---

## 6. WORKED EXAMPLES

### Worked Example 1 — Counting electrons on a charged sphere
*A charged sphere carries −64 μC. How many electrons does it hold?*

**Step 1 — Convert to coulombs:**
Q = −64 μC = −64 × 10⁻⁶ C

**Step 2 — Set up the quantization relation:**
Q = −Ne

**Step 3 — Solve for N:**
N = Q / (−e) = (−64 × 10⁻⁶) / (−1.6 × 10⁻¹⁹)

**Step 4 — Compute (handle the powers of ten separately):**
64 / 1.6 = 40  and  10⁻⁶ / 10⁻¹⁹ = 10¹³

N = 40 × 10¹³ = **4 × 10¹⁴ electrons** *(the source writes this as 40 × 10¹³; both forms are identical)*

**Step 5 — Sanity check:** N is positive, as any count must be. ✓

---

### Worked Example 2 — Electron counts across the prefix staircase
*How many electrons are in −1 mC, −1 μC, −1 nC, and −1 pC?*

Each case uses N = Q/(−e), i.e., dividing the charge by 1.6 × 10⁻¹⁹:

| Charge | In coulombs | Calculation | Electrons |
|---|---|---|---|
| −1 mC | −1 × 10⁻³ C | (10⁻³)/(1.6 × 10⁻¹⁹) | 6.25 × 10¹⁵ |
| −1 μC | −1 × 10⁻⁶ C | (10⁻⁶)/(1.6 × 10⁻¹⁹) | 6.25 × 10¹² |
| −1 nC | −1 × 10⁻⁹ C | (10⁻⁹)/(1.6 × 10⁻¹⁹) | 6.25 × 10⁹ |
| −1 pC | −1 × 10⁻¹² C | (10⁻¹²)/(1.6 × 10⁻¹⁹) | 6.25 × 10⁶ |

**Observation (pedagogical):** every step down the prefix staircase removes three powers of ten from both the charge and the electron count. Even −1 pC still means millions of electrons — individual charges are astonishingly small.

---

### Worked Example 3 — Charge sharing among three spheres
*Three conducting spheres touch each other simultaneously. Sphere 1: radius 3 m, charge 10 C. Sphere 2: radius 2 m, charge 20 C. Sphere 3: radius 1 m, charge −10 C. Find each final charge.*

**Step 1 — Total charge before contact (algebraic sum — the −10 C subtracts!):**
q_t = q₁ + q₂ + q₃ = 10 + 20 − 10 = 20 C

**Step 2 — Total radius:**
r_t = r₁ + r₂ + r₃ = 3 + 2 + 1 = 6 m

**Step 3 — Shared charge per unit radius:**
q′ = q_t / r_t = 20 / 6 C/m ≈ 3.333 C/m

**Step 4 — Final charge on each sphere (q_i′ = q′ × r_i):**
- q₁′ = (20/6) × 3 = **10 C**
- q₂′ = (20/6) × 2 = **6.667 C**
- q₃′ = (20/6) × 1 = **3.333 C**

**Step 5 — Verification (pedagogical check, consistent with the source's formula):**
10 + 6.667 + 3.333 = 20 C = q_t ✓ — no charge was created or destroyed; it was only redistributed.
Ratio check: q₁′ : q₂′ : q₃′ = 10 : 6.667 : 3.333 = 3 : 2 : 1 = r₁ : r₂ : r₃ ✓

---

## 7. COMMON MISTAKES

**Mistake 1 — Treating charge as a continuous quantity.**
- *What students do:* accept any charge value, e.g. 2.4 × 10⁻¹⁹ C, as possible.
- *Why it's wrong:* charge is quantized — Q/e must be a whole number.
- *How to avoid:* always divide the proposed charge by 1.6 × 10⁻¹⁹ and confirm the result is an integer.

**Mistake 2 — Sign slips when counting electrons.**
- *What students do:* write N = (−64 × 10⁻⁶)/(1.6 × 10⁻¹⁹) and report a negative number of electrons.
- *Why it's wrong:* a count of particles cannot be negative; the charge's sign and the electron's sign must both be included.
- *How to avoid:* use N = |Q|/e for a quick magnitude, or divide by −e for negative charges and confirm N > 0.

**Mistake 3 — Prefix mix-ups.**
- *What students do:* read μC as 10⁻³ C, or nC as 10⁻⁶ C.
- *Why it's wrong:* μ = 10⁻⁶, n = 10⁻⁹, p = 10⁻¹², m = 10⁻³ — each is a distinct factor of 1000.
- *How to avoid:* memorize the staircase m → μ → n → p (each step ÷1000) and write the conversion explicitly before computing.

**Mistake 4 — Confusing induction with conduction.**
- *What students do:* describe induction as requiring contact, or conduction as working at a distance.
- *Why it's wrong:* induction is precisely the **no-contact** method; conduction requires **direct contact**.
- *How to avoid:* anchor the words: conduction = "conduct" = contact; induction = influence at a distance.

**Mistake 5 — Expecting the induced object to match the rod's sign.**
- *What students do:* predict that a negative rod leaves the sphere negative.
- *Why it's wrong:* the rod never transfers charge to the sphere; the sphere's electrons escape to ground, so the sphere ends with the **opposite** sign.
- *How to avoid:* remember the rule — induction: opposite sign; conduction: same sign.

**Mistake 6 — Wrong order of operations in induction.**
- *What students do:* remove the rod before disconnecting the ground wire.
- *Why it's wrong:* once the rod's influence is gone, the escaped electrons flow back from the ground and the sphere returns to neutral.
- *How to avoid:* fix the sequence in memory: **ground → drain → disconnect → remove rod.**

**Mistake 7 — Assuming a 50/50 split for unequal spheres.**
- *What students do:* split the total charge in half regardless of the spheres' sizes.
- *Why it's wrong:** the sharing depends on shape; for spheres it's proportional to radius (Q ∝ r). Only identical spheres split equally.
- *How to avoid:* never split without checking radii. Compute q′ = q_t/r_t first, then multiply by each radius.

**Mistake 8 — Mishandling negative charges in the total.**
- *What students do:* compute q_t = 10 + 20 + 10 (dropping the minus on −10 C) or forget a neutral sphere still contributes its radius.
- *Why it's wrong:** q_t is an algebraic sum; negative charges subtract. And even a neutral sphere (q = 0) takes a share of charge after contact because its radius counts in r_t.
- *How to avoid:* write the sum with signs explicitly, then verify that the final charges add back to q_t.

**Mistake 9 — Mixing up radius and diameter.**
- *What students do:* plug diameters into r_i.
- *Why it's wrong:* the proportionality Q ∝ r is stated for radii.
- *How to avoid:* check the given quantity's label before substituting.

---

## 8. LECTURE SUMMARY

# Lecture Summary

## What You Need to Know
- Charge exists in two kinds, positive and negative; like repels, unlike attracts.
- All charge is quantized: Q = ±Ne with e = 1.6 × 10⁻¹⁹ C.
- The electron carries −e; the proton carries +e; the SI unit of charge is the coulomb.
- Prefix conversions: mC = 10⁻³ C, μC = 10⁻⁶ C, nC = 10⁻⁹ C, pC = 10⁻¹² C.
- Three ways to charge an object: rubbing (insulators), induction (conductors, no contact), conduction (conductors, contact).
- Rubbing moves electrons: glass→silk (glass +, silk −); wool→plastic (plastic −, wool +).
- Induction leaves the object with the **opposite** sign of the charging object; grounding is the key step; disconnect ground before removing the rod.
- Conduction leaves the object with the **same** sign; spheres share charge in proportion to radius.

## Key Definitions
- **Elementary charge (e)** → the fundamental unit of charge, 1.6 × 10⁻¹⁹ C, discovered as the indivisible unit by Millikan (1909).
- **Quantization of charge** → every charge is an integer multiple of e: Q = ±Ne.
- **Repulsive force** → force between same-sign charges.
- **Attractive force** → force between opposite-sign charges.
- **Coulomb (C)** → the SI unit of electric charge.
- **Rubbing (friction)** → charging by transferring electrons between two rubbed materials; used for insulators.
- **Induction** → charging a conductor without contact, using a nearby charge to redistribute electrons and a ground connection to remove or supply them.
- **Conduction** → charging by direct contact; part of the charge flows onto the other object.

## Key Formulas
- **e = 1.6 × 10⁻¹⁹ C** → size of the fundamental charge unit.
- **Q = ±Ne** → quantization; total charge from a number of elementary charges.
- **N = Q/(±e)** → counting electrons (or protons) in a charge.
- **q′ = q_t/r_t = (q₁+q₂+q₃+⋯)/(r₁+r₂+r₃+⋯)** → shared charge per unit radius after spheres touch.
- **q_i′ = q′ × r_i** → final charge on each sphere after contact.
- **q₁′/q₂′ = r₁/r₂** → final charges are in the ratio of the radii.
- **Q ∝ r** → bigger spheres take bigger shares.

## Important Ideas
- Charge is never created or destroyed in these processes — only transferred or redistributed.
- Electrons are always the mobile particles in rubbing, induction, and conduction.
- The ground (Earth) acts as both a source and a sink for electrons during induction.
- Even "uncharged" spheres participate in contact sharing: their radius counts in r_t.

## Common Mistakes
- Accepting non-integer multiples of e as valid charges.
- Producing negative electron counts through sign errors.
- Confusing μ (10⁻⁶) with m (10⁻³).
- Mixing up induction (no contact, opposite sign) with conduction (contact, same sign).
- Removing the rod before cutting the ground wire in induction.
- Splitting charge 50/50 between unequal spheres.
- Dropping minus signs when summing total charge in sphere-sharing problems.

## Exam Focus
The concepts most likely to demand genuine understanding rather than memorization:
1. **The induction procedure** — being able to narrate the five steps and predict the sign at each stage (especially *why* grounding matters and *why* the order matters).
2. **Charge sharing with mixed signs** — computing q_t correctly when negative charges are present, then distributing q_t/r_t across unequal radii.
3. **Quantization as a physical constraint** — using Q/e ∈ ℤ to rule out impossible charge values.

## 60-Second Review
Charge comes in packets of e = 1.6 × 10⁻¹⁹ C — so any charge is Q = ±Ne, and counting electrons is just division. Likes repel, unlikes attract. To charge something: **rub** an insulator (electrons hop — glass goes +, plastic goes −), **induce** a conductor (bring a charged object near, ground the far side, cut the wire, remove the object — result is the opposite sign), or use **conduction** (touch — same sign). When conducting spheres touch, charge spreads proportionally to radius: q′ = (total charge)/(total radius), each sphere gets q′ × its radius, and the pieces must sum back to the total. Induction: opposite sign, no contact. Conduction: same sign, contact. Ground before you remove the rod — always.

---

## 9. DIFFICULT CONCEPTS

### Difficult Concept: Quantization of Charge

**Why students struggle:** Macroscopic charges look perfectly smooth and continuous, so "charge comes only in lumps" feels arbitrary. Students also forget to *use* quantization as a validity test.
**Simple explanation:** Charge behaves like eggs, not like milk. You can have 1 egg, 2 eggs, 12 eggs — never 1.5 eggs. Every charge in nature is a whole number of "charge eggs" of size e.
**Intuitive analogy:** Coins in a currency with a smallest denomination: any price must be a whole number of coins; you cannot pay half a coin.
**Step-by-step explanation:**
1. The elementary unit has magnitude e = 1.6 × 10⁻¹⁹ C.
2. An object's charge is Q = ±Ne with N a whole number.
3. To test any proposed charge, divide by e: the result must be an integer.
4. To count particles, divide the total charge by e and take the magnitude.
**Mini example:** Is −4.8 × 10⁻¹⁹ C possible? −4.8 × 10⁻¹⁹ / (−1.6 × 10⁻¹⁹) = 3 → yes, that's 3 excess electrons. Is −4.0 × 10⁻¹⁹ C possible? 4.0/1.6 = 2.5 → no, half-electrons don't exist.
**Misconception to avoid:** "Small enough charges can be any value." No — only integer multiples of e are physical.
**Difficulty:** MEDIUM

### Difficult Concept: Charging by Induction

**Why students struggle:** It's a multi-step, order-dependent process involving three bodies (rod, sphere, Earth) and two different charge motions (redistribution inside the sphere, then transfer to/from ground). The result — opposite sign — is counterintuitive.
**Simple explanation:** The charged rod never touches the sphere; it just "pushes" or "pulls" the sphere's free electrons around. The ground wire then gives those displaced electrons a one-way exit (or entrance). When you seal the exit and remove the rod, the sphere is stuck with whatever imbalance remains.
**Intuitive analogy:** A room full of people (electrons) and a "bouncer" (negative rod) standing at the door. People back away from the door. If you open an exit door on the far wall, some people leave the room entirely. Close the exit *before* the bouncer walks away, and the room ends up with fewer people — net "positive" — even though the bouncer never entered.
**Step-by-step explanation:**
1. Charge the rod (e.g., plastic rubbed with wool → negative).
2. Bring the rod near the neutral conductor (no contact).
3. Free electrons redistribute: repelled to the far side (for a negative rod), leaving the near side positive.
4. Ground the far side: repelled electrons drain into the Earth.
5. Disconnect the ground wire (rod still in place).
6. Remove the rod. The sphere keeps a net charge **opposite** to the rod's.
**Mini example:** Negative rod + grounded neutral sphere → electrons leave via the wire → sphere ends **positive**. To end **negative** instead, start with a **positive** rod (electrons then flow *from* the ground *onto* the sphere).
**Misconception to avoid:** "Charge moves from the rod to the sphere." It never does — the transfer happens between the sphere and the ground.
**Difficulty:** HARD

### Difficult Concept: Charge Sharing Proportional to Radius (Conduction)

**Why students struggle:** The intuition "they touch, so they split evenly" is strong and wrong for unequal spheres. The formula chain (sum charges with signs, sum radii, divide, multiply back) has several places to slip.
**Simple explanation:** When conducting spheres touch, they don't equalize their *charges* — they equalize their charge-to-radius ratio. Every meter of radius ends up carrying the same share, so the bigger sphere automatically walks away with more total charge.
**Intuitive analogy:** Two connected water tanks of different sizes: the water *level* equalizes, but the bigger tank always holds more total water. Level ↔ q′ (charge per meter of radius); tank size ↔ radius.
**Step-by-step explanation:**
1. Add up all charges algebraically: q_t = q₁ + q₂ + q₃ + ⋯ (minus signs matter).
2. Add up all radii: r_t = r₁ + r₂ + r₃ + ⋯
3. Compute the shared value: q′ = q_t / r_t (in C/m).
4. Each sphere's final charge: q_i′ = q′ × r_i.
5. Check: the final charges must sum back to q_t, and their ratios must match the radii ratios.
**Mini example:** Spheres of radius 4 m (12 C) and 2 m (0 C) touch. q_t = 12 C, r_t = 6 m, q′ = 2 C/m → final charges 8 C and 4 C. The big sphere takes twice the charge of the small one — exactly its radius ratio.
**Misconception to avoid:** "Contact means 50/50." Equal sharing only happens for identical spheres (equal radii).
**Difficulty:** HARD

### Difficult Concept: Sign Bookkeeping When Counting Electrons

**Why students struggle:** The double negative (negative charge divided by negative electron charge) plus unit prefixes creates multiple simultaneous demands.
**Simple explanation:** A count of particles is always a positive whole number. If your arithmetic produces "−6.25 × 10¹² electrons," something went wrong before the final step.
**Intuitive analogy:** "How many people left the room?" is never answered with "minus five people."
**Step-by-step explanation:** (1) Convert the prefixed unit to coulombs. (2) Write the charge with its sign. (3) Divide by −e if the charge is negative (or by +e for a positive charge, giving the number of electrons *removed*). (4) Confirm the result is positive.
**Mini example:** Q = −32 μC → N = (−32 × 10⁻⁶)/(−1.6 × 10⁻¹⁹) = 2 × 10¹⁴ electrons.
**Misconception to avoid:** "The sign of the answer tells you the particle type." No — the sign was consumed by the division; the answer is just a count.
**Difficulty:** MEDIUM

### Difficult Concept: Metric Prefixes for Charge

**Why students struggle:** Four prefixes spanning twelve orders of magnitude, with handwriting that makes μ and m look alike.
**Simple explanation:** Learn them as a staircase: each step down (m → μ → n → p) divides by 1000.
**Intuitive analogy:** Steps of a staircase, each 1000 times smaller than the last.
**Step-by-step explanation:** (1) Identify the prefix. (2) Replace it with its power of ten. (3) Combine powers of ten last, after handling the coefficients.
**Mini example:** 0.75 μC = 0.75 × 10⁻⁶ C = 7.5 × 10⁻⁷ C.
**Misconception to avoid:** μ does not mean 10⁻³ — that's m. Write the symbol carefully and say "micro" out loud when reading it.
**Difficulty:** EASY

---

## 10. VIDEO LESSON PLANS

*(Plans for the two HARD concepts.)*

### VIDEO 1

**VIDEO TITLE:** Charge Without Touching: How Induction Really Works

**TARGET CONCEPT:** Charging a conductor by induction (procedure, role of grounding, sign rule, order of operations)

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can narrate the five-step induction procedure, predict the sign of the induced charge (opposite to the charging object), and explain why the ground wire must be disconnected before the rod is removed.

**HOOK:** Open with the paradox — a negatively charged rod gives a neutral metal sphere a *positive* charge without ever touching it and without giving it any charge. "Sounds impossible — let's watch it happen step by step."

**EXPLANATION:**
1. Review the two interaction rules (like repels, unlike attracts) and the fact that conductors contain free electrons.
2. Establish that a charged object *near* a conductor can redistribute its electrons without any transfer across the gap.
3. Walk through the five steps with visuals: approach → polarization → ground the far end (electrons drain to Earth) → disconnect ground → remove rod.
4. Derive the sign rule: opposite sign, always.
5. Reverse the scenario: positive rod → electrons flow *from* ground *onto* the sphere → negative result.

**VISUALS:**
- Animated metal sphere on an insulating stand; electrons drawn as small blue dots that drift within the sphere.
- Negative rod (red "−" markers) approaching from the left; arrows showing electrons migrating right.
- Split-screen zoom on the far end when the ground wire appears; electron dots flowing down the wire into a stylized "Earth."
- A step counter (1–5) in the corner; sign badges (+/−) updating live on the sphere.
- Final freeze-frame comparing the rod's sign vs. the sphere's sign with a big "OPPOSITE" stamp.

**EXAMPLE:** Plastic rod rubbed with wool (negative — electrons moved from wool to plastic) brought near a neutral metal sphere on an insulating mount; full procedure; final result positive. Then the mirrored case with a positive rod producing a negative sphere.

**COMMON MISTAKE:** Believing the sphere ends up with the *same* sign as the rod, or that charge flows between the rod and the sphere.

**CHECK FOR UNDERSTANDING:** "You have a positively charged rod. Describe, in order, how to charge a neutral metal sphere negatively by induction — and state when exactly you disconnect the ground wire."

**FINAL TAKEAWAY:** Induction = charge without contact; the ground supplies or removes electrons; disconnect first, remove the rod second; the result is always the opposite sign.

---

### VIDEO 2

**VIDEO TITLE:** When Spheres Touch: Why the Big One Gets More Charge

**TARGET CONCEPT:** Charge sharing by conduction between conducting spheres; Q ∝ r; q′ = q_t/r_t; q_i′ = q′ × r_i

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can compute the final charge on each of several touching conducting spheres (including negative initial charges) and verify the result using charge conservation and radius ratios.

**HOOK:** Pose the intuition trap: "A big sphere with 12 C touches a small neutral sphere. Half and half, right? Wrong. By the end of this video you'll compute the exact split in under a minute."

**EXPLANATION:**
1. Conduction basics: contact required; resulting object takes the charger's sign; how much transfers depends on shape.
2. Identical spheres → equal split (the familiar special case).
3. General spheres → charge proportional to radius, Q ∝ r; introduce q′ as "charge per meter of radius."
4. Build the recipe: q_t (algebraic sum) → r_t → q′ = q_t/r_t → q_i′ = q′ × r_i.
5. Two built-in safety checks: final charges sum to q_t; charge ratios equal radius ratios.

**VISUALS:**
- Two spheres of clearly different sizes touching; charge units drawn as dots flowing until the "dots per meter of radius" are equal on both.
- A water-tank analogy animation (connected tanks, equal levels, unequal volumes).
- Formula build-up with each term color-coded to the matching part of the diagram.
- The worked example on screen with a running checklist: total charge ✓, total radius ✓, shared value ✓, per-sphere multiplication ✓, conservation check ✓.

**EXAMPLE:** The lecture's three-sphere problem: radii 3 m, 2 m, 1 m with charges 10 C, 20 C, −10 C → q_t = 20 C, r_t = 6 m, q′ = 20/6 C/m → final charges 10 C, 6.667 C, 3.333 C.

**COMMON MISTAKE:** Splitting the total charge 50/50 (or equally among all spheres) regardless of radius; forgetting that −10 C subtracts in the total.

**CHECK FOR UNDERSTANDING:** "Sphere A: radius 4 m, charge 12 C. Sphere B: radius 2 m, neutral. They touch. What is each final charge — and what's the ratio?"

**FINAL TAKEAWAY:** Spheres in contact equalize charge *per radius*, not total charge: q′ = q_t/r_t, then multiply by each sphere's radius — and the final charges must always add back to the original total.

---

## 11. VIDEO SCRIPTS

### VIDEO SCRIPT 1 — Charge Without Touching: How Induction Really Works

**[0:00–0:30] Hook**
"Here's a puzzle for you. This metal sphere is sitting on an insulating stand, and it is completely neutral — zero net charge. In my other hand, a rod I've charged negatively. Now, common sense says: if I want this sphere to become *positive*, I'd have to somehow put positive charge onto it, right? Watch closely — the rod is never going to touch the sphere. Not once. And the sphere still ends up positive. Charged by an object it never contacted, with a sign *opposite* to that object. This is charging by induction, and in the next eight minutes you'll be able to predict every single step."

**[0:30–2:00] Concept introduction**
"First, the two rules everything rests on. One: charges of the same sign push each other away; charges of opposite sign pull toward each other. Two: in a metal — a conductor — some electrons are free to move around. A neutral conductor has exactly equal amounts of positive and negative, so overall it's zero. But here's the key idea of the whole video: a charged object held *near* a conductor can shove those free electrons around without anything crossing the gap. No contact, no transfer — just rearrangement. Keep that phrase in mind: *redistribution, not transfer*."

**[2:00–4:00] Visual explanation**
"Let's run the full procedure. Step one: I bring my negative rod close to the sphere — close, but never touching. Every free electron in that sphere feels the rod's repulsion and drifts to the far side. The near side is left electron-poor, which means positive. Look at the sphere's badge: total charge still zero. It's just polarized — negative on the far side, positive on the near side.
Step two: I connect the far end of the sphere to the Earth with a wire. Now those crowded, repelled electrons have somewhere to go — and they go: down the wire, into the ground. Watch the blue dots leave.
Step three: they keep draining as long as the rod keeps pushing them.
Step four — and this order matters: while the rod is still in place, I disconnect the ground wire. The sphere has now *lost* electrons. Its total is no longer zero. It's positive, and the rod's attraction is holding that positive charge near it.
Step five: I take the rod away. The remaining positive charge spreads out over the sphere. Done. The sphere is positive, the rod is still negative, and they never touched.
Now run it in reverse: if the rod were *positive*, it would pull the sphere's electrons toward the near side — and electrons would come *up from the ground* through the wire to join them. Cut the wire, remove the rod, and the sphere is left negative. That's why the rule is: **induction always leaves the target with the opposite sign of the charging object.** Negative rod → positive sphere. Positive rod → negative sphere."

**[4:00–6:00] Worked example**
"Let's use the exact case from the lecture. I rub a plastic rod with wool. From friction, electrons transfer from the wool *to* the plastic — so the rod is negative, the wool is positive. Now I hold that rod near my neutral metal sphere on its insulating mount. Electrons in the sphere get pushed to the far end. I attach the ground wire to that far end. The repelled electrons flow into the Earth. I cut the wire — still with the rod in place — and then I remove the rod. Final answer: the sphere carries a net *positive* charge. Ask yourself at each step: which way are the electrons moving? Between the sphere and the ground — never between the rod and the sphere. The Earth is doing the heavy lifting: it's both a source and a sink of electrons."

**[6:00–7:00] Common mistake**
"Three mistakes I see constantly. Mistake one: 'the sphere gets the same sign as the rod.' No — think it through: the negative rod *expelled* electrons, so the sphere must be short of electrons, which means positive. Opposite sign, every time. Mistake two: 'charge flows from the rod into the sphere.' Impossible — they never touch. The only charge transfer happens through the ground wire. Mistake three, the sneaky one: the order of operations. If you remove the rod *before* disconnecting the ground wire, the sphere's electrons just flow back up from the Earth, and you end up with a neutral sphere and a wasted afternoon. The sequence is fixed: ground, drain, disconnect, *then* remove."

**[7:00–8:00] Quick student challenge**
"Your turn. You have a *positively* charged rod, a neutral metal sphere on an insulating stand, and a ground wire. Pause the video and describe, step by step, how to give that sphere a *negative* charge by induction. Which way do the electrons move, and at exactly what moment do you disconnect the wire? … Ready? Hold the positive rod near the sphere — the sphere's electrons are pulled toward it, and electrons flow *from the ground onto the sphere*. While the rod is still there, disconnect the wire. Then remove the rod. The sphere keeps its extra electrons: negative. If you said 'disconnect after removing the rod' — go back and watch the common-mistake minute again."

**[8:00–8:30] Final recap**
"Induction in one breath: charge without contact. A charged rod polarizes a conductor; a ground wire lets electrons escape to Earth — or arrive from it; you disconnect the ground first, remove the rod second; and the object always ends up with the *opposite* sign of the rod. Master this procedure — it returns in every electrostatics exam in some disguise."

---

### VIDEO SCRIPT 2 — When Spheres Touch: Why the Big One Gets More Charge

**[0:00–0:30] Hook**
"Quick intuition test. Big metal sphere, twelve coulombs of charge. Small neutral metal sphere. I touch them together and pull them apart. Question: does each one keep six? Half and half? Almost everyone says yes — and almost everyone is wrong. The big sphere walks away with *more* charge than the small one, every single time. Today you'll learn why size decides the split — and how to compute the exact answer in under a minute, even with three spheres and a negative charge thrown in."

**[0:30–2:00] Concept introduction**
"First, what conduction charging is: when a charged object physically touches another object, some of that charge flows across, and the touched object ends up with the *same* sign as the charger. How much flows? That depends on the shapes of the two objects — the lecture is explicit about that. Now, the famous special case: two *identical* metal spheres on insulating mounts share the charge equally. Makes sense — same size, same share. But here's the general rule for spheres, and it's the star of this video: **the charge each sphere keeps is proportional to its radius.** Q is proportional to r. Bigger sphere, bigger share. And here's the intuition that makes it stick: think of two water tanks connected by a pipe. The water *level* equalizes — but the big tank always ends up holding more total water. Spheres in contact equalize their charge *per meter of radius*, not their total charges."

**[2:00–4:00] Visual explanation**
"Here's the recipe, built from the diagram. Step one: total charge. Add up every sphere's charge *algebraically* — and if a sphere is negative, that's a minus sign in your sum. q_t = q₁ + q₂ + q₃ and so on. Step two: total radius. Add up all the radii: r_t = r₁ + r₂ + r₃. Step three: the shared value — I call it the charge-per-meter: q prime equals q_t over r_t. Units: coulombs per meter. This is the 'water level' — the same for every sphere after they've touched. Step four: each sphere's final charge is q prime times *its* radius: q_i prime = q′ × r_i. Multiply the level by the size. And notice the beautiful shortcut hiding in here: the ratio of any two final charges equals the ratio of their radii. q₁′ over q₂′ equals r₁ over r₂. Plus one free self-check: your final charges must add back up to the original total. Charge is never created or destroyed — only redistributed."

**[4:00–6:00] Worked example**
"The lecture's own problem. Three conducting spheres touch each other all at once. Sphere one: radius three meters, charge ten coulombs. Sphere two: radius two meters, twenty coulombs. Sphere three: radius one meter, *minus* ten coulombs. Find the final charge on each.
Step one, total charge: ten plus twenty minus ten — do not drop that minus! — equals twenty coulombs. Step two, total radius: three plus two plus one equals six meters. Step three, charge per meter: twenty over six — about three point three three coulombs per meter. Step four, multiply back: sphere one gets three point three three times three — ten coulombs. Sphere two: three point three three times two — six point six seven. Sphere three: three point three three times one — three point three three. Final step, the check: ten plus six point six seven plus three point three three — twenty coulombs. Exactly the total we started with. And the ratios? Ten to six point six seven to three point three three — that's three to two to one. Exactly the radii. Two independent confirmations that the answer is right."

**[6:00–7:00] Common mistake**
"The mistakes that cost real marks. Number one, the big one: assuming an equal split. Equal only happens for *identical* spheres. If the radii differ, the split follows the radii. Number two: dropping the minus sign on a negative charge when you compute q_t — that turns twenty coulombs into forty and destroys the whole answer. Number three: plugging in only one sphere's numbers, or forgetting that even a *neutral* sphere still contributes its radius to r_t — zero charge, yes, but its size still earns it a share. Number four: using diameters where the formula wants radii. And number five: never checking. The conservation check — do the final charges sum to q_t? — takes ten seconds and catches nearly every error."

**[7:00–8:00] Quick student challenge**
"Your turn. Sphere A: radius four meters, carrying twelve coulombs. Sphere B: radius two meters, completely neutral. They touch, then separate. Pause and predict each final charge *before* you compute. … Here we go: total charge twelve, total radius six, charge per meter: two. Sphere A: two times four — eight coulombs. Sphere B: two times two — four coulombs. Notice the ratio: eight to four is two to one, exactly the ratio of the radii. Not six and six — the big sphere takes twice what the small one gets. If your gut said 'six each,' don't feel bad — now your gut has the water-tank picture to correct it."

**[8:00–8:30] Final recap**
"Conduction sharing in thirty seconds. Spheres in contact don't equalize total charge — they equalize charge per radius. Add all charges with their signs. Add all radii. Divide: q′ = q_t over r_t. Multiply back by each radius: q_i′ = q′ × r_i. Verify the total. Bigger sphere, bigger share. That's it — now go practice."

---

## 12. PRACTICE QUESTIONS

*(Student-facing questions. The answer key below each is for instructor/platform use and must not be displayed with the question.)*

### LEVEL 1 — UNDERSTAND

**Q1.** What does it mean to say that electric charge is "quantized"? State the value of the fundamental unit of charge.
> *Instructor key — Answer:* Charge exists only in integer multiples of e; e = 1.6 × 10⁻¹⁹ C; Q = ±Ne. *Skill:* quantization concept. *Difficulty:* EASY.

**Q2.** Classify each pair as attractive or repulsive: (a) two electrons; (b) a proton and an electron; (c) two protons.
> *Instructor key — Answer:* (a) repulsive; (b) attractive; (c) repulsive. *Skill:* charge interaction rules. *Difficulty:* EASY.

**Q3.** Name the three charging methods covered in this lecture, and for each state whether direct contact is required and which type of material (conductor/insulator) it applies to in this lecture.
> *Instructor key — Answer:* Rubbing — contact, insulators; induction — no contact, conductors; conduction — contact, conductors. *Skill:* method classification. *Difficulty:* EASY.

**Q4.** A glass rod is rubbed with silk. What are the final signs of the rod and the silk, and which particles moved between them and in which direction?
> *Instructor key — Answer:* Rod positive, silk negative; electrons moved from rod to silk. *Reasoning:* friction transfers electrons; the loser of electrons becomes positive. *Skill:* friction charging. *Difficulty:* EASY.

**Q5.** Which charging method does this lecture assign to insulators?
> *Instructor key — Answer:* Rubbing (friction). *Skill:* method classification. *Difficulty:* EASY.

**Q6.** An object is claimed to carry a charge of −3.2 × 10⁻¹⁹ C; another, −4.0 × 10⁻¹⁹ C. Determine whether each is physically possible and justify.
> *Instructor key — Answer:* −3.2 × 10⁻¹⁹ C = −2e → possible (2 excess electrons). −4.0 × 10⁻¹⁹ C = −2.5e → impossible (N must be an integer). *Skill:* quantization as a validity test. *Difficulty:* MEDIUM.

### LEVEL 2 — APPLY

**Q7.** A conducting sphere carries −96 μC. How many excess electrons does it have?
> *Instructor key — Answer:* N = (−96 × 10⁻⁶)/(−1.6 × 10⁻¹⁹) = 6 × 10¹⁴ electrons. *Reasoning:* convert prefix, divide magnitudes, combine powers of ten. *Skill:* electron counting with prefix conversion. *Difficulty:* MEDIUM.

**Q8.** An object carries +4.8 μC. How many electrons were removed from it?
> *Instructor key — Answer:* 4.8 × 10⁻⁶ / 1.6 × 10⁻¹⁹ = 3 × 10¹³ electrons removed. *Reasoning:* positive charge = electron deficit; N = |Q|/e. *Skill:* electron counting, positive case. *Difficulty:* MEDIUM.

**Q9.** Two identical conducting spheres on insulating mounts carry 8 C and 4 C. They are touched together and separated. Find the final charge on each — first by the equal-sharing rule, then by the formula q′ = q_t/r_t, and confirm both agree.
> *Instructor key — Answer:* Equal sharing: (8 + 4)/2 = 6 C each. Formula: q_t = 12 C, r_t = 2r, q′ = 12/(2r) = 6/r C/m, each q_i′ = (6/r) × r = 6 C. Both methods agree. *Skill:* contact charge sharing; consistency of the two routes. *Difficulty:* MEDIUM.

**Q10.** A conducting sphere of radius 5 m carrying 15 C touches a neutral conducting sphere of radius 2.5 m. Find each final charge.
> *Instructor key — Answer:* q_t = 15 C, r_t = 7.5 m, q′ = 2 C/m → sphere 1: 2 × 5 = 10 C; sphere 2: 2 × 2.5 = 5 C. *Reasoning:* neutral sphere contributes radius but zero charge; multiply q′ by each radius. *Skill:* applying q′ = q_t/r_t with a neutral participant. *Difficulty:* MEDIUM.

**Q11.** You want to charge a neutral metal sphere **negatively** by induction. What sign must the charging object have, what must you connect during the process, and in what order must you disconnect and remove things?
> *Instructor key — Answer:* Positive charging object; ground wire connected to the sphere; electrons flow from Earth onto the sphere; disconnect the ground wire *while the object is still near*, then remove the object. *Skill:* induction procedure and sign rule. *Difficulty:* MEDIUM.

**Q12.** Convert: (a) 0.5 mC into μC; (b) 250 nC into μC; (c) how many electrons are in −1 μC?
> *Instructor key — Answers:* (a) 500 μC; (b) 0.25 μC; (c) 6.25 × 10¹² electrons. *Skill:* prefix conversions; electron counting. *Difficulty:* EASY–MEDIUM.

---

## 13. TRANSFER QUESTIONS

### LEVEL 3 — TRANSFER

**Q13.** Three conducting spheres are touched together simultaneously: sphere 1 has radius 1 m and charge 2 C; sphere 2 has radius 2 m and charge −4 C; sphere 3 has radius 3 m and is initially neutral. Find the final charge on each sphere and verify your answer two independent ways.
> *Instructor key — Answer:* q_t = 2 + (−4) + 0 = −2 C; r_t = 6 m; q′ = −2/6 = −1/3 C/m. Final: q₁′ = −1/3 C ≈ −0.333 C; q₂′ = −2/3 C ≈ −0.667 C; q₃′ = −1 C. Verification 1 (conservation): −1/3 − 2/3 − 1 = −2 C ✓. Verification 2 (ratios): 1/3 : 2/3 : 1 = 1 : 2 : 3 = radii ✓. *Reasoning:* the neutral sphere still takes a share via its radius; the negative total makes every final charge negative. *Skill:* full charge-sharing procedure with mixed signs and a neutral sphere. *Difficulty:* HARD.

**Q14.** You must give a neutral metal sphere (on an insulating stand) a **negative** charge, but no charged object is allowed to touch it — and you only have a **positively charged** rod and a ground wire. Describe the complete procedure, stating at every step which way electrons move.
> *Instructor key — Answer:* Bring the positive rod near (no contact) → the sphere's free electrons shift toward the near side (polarization). Connect the ground wire → electrons are drawn from the Earth onto the sphere (they are attracted by the rod's influence and flow up the wire). While the rod is still in place, disconnect the wire. Remove the rod → the sphere is left with excess electrons: net negative. *Reasoning:* induction with a positive charger yields a negative target; the Earth supplies the electrons. *Skill:* induction procedure transferred to a planning task. *Difficulty:* HARD.

**Q15.** A classmate claims that friction left a dust particle with a charge of −5.0 × 10⁻¹⁹ C. Using quantization, evaluate the claim. If it is impossible, state the two nearest *allowed* negative charges.
> *Instructor key — Answer:* 5.0 × 10⁻¹⁹ / 1.6 × 10⁻¹⁹ = 3.125 → not an integer → impossible. Nearest allowed: −3e = −4.8 × 10⁻¹⁹ C and −4e = −6.4 × 10⁻¹⁹ C. *Skill:* applying Q = ±Ne as a physical constraint in a novel context. *Difficulty:* MEDIUM.

**Q16.** A negatively charged rod is held near — but not touching — a small neutral conductor hanging from an insulating thread. Based on the mechanism of induction described in this lecture, describe the charge distribution inside the conductor and predict whether the rod attracts or repels it. Explain.
> *Instructor key — Answer:* The rod repels the conductor's free electrons to the far side and attracts its positive charge to the near side — the near face becomes positive and the far face negative. Because the opposite-sign charge is now closer to the rod than the same-sign charge, the net interaction is attraction. *(Note: the redistribution itself is exactly the lecture's induction mechanism; the "net attraction" conclusion is a pedagogical extension of that mechanism.)* *Skill:* transfer of the polarization mechanism to a prediction task. *Difficulty:* HARD.

**Q17.** The lecture states that two identical metal spheres with insulator mountings share charge equally when touched. Show mathematically that this rule is a special case of q_i′ = (q_t / r_t) × r_i, and use it to find the charge on each of two identical spheres after a sphere carrying Q touches a neutral identical sphere.
> *Instructor key — Answer:* With r₁ = r₂ = r: q_t = q₁ + q₂; r_t = 2r; q′ = (q₁ + q₂)/(2r); then q₁′ = q₂′ = q′ × r = (q₁ + q₂)/2 — equal halves. For charge Q touching a neutral identical sphere: q_t = Q, r_t = 2r, each ends with (Q/2r) × r = Q/2. *Skill:* deriving a stated special case from the general formula. *Difficulty:* MEDIUM.

---

## 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All properties of charge, all three charging methods, all formulas, all three examples, prefix table, induction sign rules, conduction sign rules, and Q ∝ r sharing model are present. |
| Mathematical formulas correct | ✅ | e = 1.6 × 10⁻¹⁹ C; Q = ±Ne; N = Q/(±e); q′ = q_t/r_t; q_i′ = q′ × r_i; ratio relations — all match the source. Example 3's source typo ("10 + 20 − 10q") resolved per the source's own arithmetic (sum = 20 C). |
| Technical terminology preserved | ✅ | Coulomb, quantization, elementary/electron charge, induction, conduction, rubbing (friction), repulsive/attractive force, insulator mounting, charge per unit radius. |
| Explanations in original language | ✅ | All prose rewritten; only short standard definitions and formulas retained in canonical form. |
| Understandable to a first-year student | ✅ | Reading level controlled; analogies (eggs/coins, bouncer in a room, water tanks) added and clearly marked as pedagogical. |
| Difficult concepts explicitly identified | ✅ | 5 concepts with difficulty ratings; 2 rated HARD and given full video plans and scripts. |
| Common misconceptions identified | ✅ | 9 mistakes with what/why/how; misconceptions embedded in difficult-concept entries and video scripts. |
| Examples actually teach the concept | ✅ | Each topic includes at least one example; worked examples include reasoning steps and verification checks. |
| Practice progresses understand → apply → transfer | ✅ | Level 1 (6), Level 2 (6), Level 3 (5), plus a 9-question self-check without revealed answers. |
| No unsupported claims added | ✅ | Pedagogical additions (charge-conservation check, water-tank analogy, potential-based note, net-attraction inference in Q16) are explicitly flagged as such. Course title marked [SOURCE DOES NOT SPECIFY] where absent. |
| No large verbatim reproduction | ✅ | Structure and formulas preserved; wording rewritten throughout. |
| Suitable for direct web integration | ✅ | Clean Markdown, self-contained lesson, metadata, estimated times, and platform-facing answer keys separated from student-facing questions. |

**Placement recommendation for ARETE:** Deploy as the first LEARN-stage lesson of Module 1; attach the two videos to the induction and conduction-sharing topics; enable REMEDIATE on mistakes 5, 6, and 7 (induction sign/order and 50/50 splitting), which are the highest-frequency failure modes for this material.
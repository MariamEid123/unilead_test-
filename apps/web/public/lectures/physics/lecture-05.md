تمام — دي **Lecture 5 (Capacitors)** بالباكدج الكامل — آخر محاضرة وعدتك بيها. وملاحظة مهمة في الآخر عن **Lecture 6** اللي موجودة كمان في ملفاتك.

---

## 1. SOURCE ANALYSIS

**Source document:** Phy 211 Lecture Notes — Lecture 5, Fall 2024, AIU (Dr. Ashraf Mousa Abdelwahed), 8 pages.

| Item | Finding |
|---|---|
| Course | Phy 211 — Physics [full course title: SOURCE DOES NOT SPECIFY] |
| Chapter | Chapter 4 — Capacitors |
| Lecture | Lecture 5 (final electrostatics lecture of the provided arc) |
| Position | Depends on Gauss's law, ε₀, potential difference, and E = ΔV/d (Lecture 4); bridges into DC circuits (Lecture 6 — Electric Current) |

**Main topics**
1. The capacitor ("condenser"): structure, charging, E₀ = ΔV₀/d
2. Capacitance: definition C = Q/ΔV, the farad; Q₀ ∝ ΔV₀
3. The parallel-plate formula from Gauss's law: C₀ = ε₀A/d; C ∝ A and C ∝ 1/d
4. Energy stored in a charged capacitor: U = Q²/2C = ½QΔV = ½C(ΔV)²
5. Energy density: u = ½εE²
6. Dielectrics: polarization mechanism, E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, C = kC₀ = εA/d
7. Combinations: parallel (C_eq = C₁ + C₂; n identical → nC) and series (1/C_eq = 1/C₁ + 1/C₂; n identical → C/n)

**Important definitions:** capacitor; capacitance (ratio of charge on either conductor to potential difference between them); farad; dielectric; dielectric constant k (unitless, k ≥ 1, k = 1 for air); permittivity of material ε = kε₀; relative permittivity k = ε/ε₀.

**Worked examples in source:** Example 1 (geometric changes → C ratios), Example 2 (C from Q and ΔV; new ΔV at larger Q), Example 3 (full characterization: C, Q, E), Example 4 (finding k from Q, ΔV, geometry).

**Procedures:** deriving C₀ = ε₀A/d via Gauss's law; the dielectric consequence chain (polarize → E drops → ΔV drops → C rises); computing C_eq for series and parallel; distributing Q or ΔV across combined capacitors.

**Prerequisites (inferred):** Lectures 1–4 — charge, field, Gauss's law (Φ = q_in/ε₀), potential difference, E = ΔV/d, ε₀.

**Dependencies:** the E = ΔV/d and ε₀ machinery from Lecture 4 is used throughout; this lesson's C = Q/ΔV and energy storage prepare the transition to current and circuits.

**Difficult concepts identified:** capacitance as a ratio; the Gauss's-law derivation; the three energy forms; why series capacitors share the same Q and yield smaller C_eq; the dielectric mechanism.

**Common misconceptions in the material:** capacitance = "stored charge"; charge splitting in series; equal voltages in series; the dielectric "adding" charge; k multiplying the wrong quantity.

**Source notes for transparency:**
- The dielectric analysis assumes the capacitor is **disconnected** from the battery (Q = Q₀ stays fixed); Example 4 instead describes a capacitor *built with* a dielectric while connected to a 12 V battery (Q given). Both scenarios are as presented in the source — the dynamic "insert dielectric while battery still connected" case is not analyzed. [SOURCE DOES NOT SPECIFY]
- No table of k values for named materials is given (only k = 1 for air and the example's k = 6.7). [SOURCE DOES NOT SPECIFY material names]
- All numeric results re-verified: 53 pF, 636 × 10⁻¹² C, 12000 V/m, 1 μF, 100 V, k = 6.7 — all confirmed. No arithmetic slips found in this file.

---

## 2. COURSE / MODULE / LESSON METADATA

- **COURSE:** Phy 211 — Physics (full title [SOURCE DOES NOT SPECIFY])
- **MODULE:** Chapter 4 — Capacitors (completion of the electrostatics arc: Modules 1–4 = Lectures 1–5)
- **LESSON:** Lecture 5 — Capacitors: Capacitance, Energy, Dielectrics, and Combinations
- **TOPICS:** capacitor structure; C = Q/ΔV; C = ε₀A/d; stored energy (three forms); energy density; dielectric mechanism and k; parallel and series combinations
- **PREREQUISITES:** Lectures 1–4 (charge; field; Gauss's law; potential difference; E = ΔV/d; ε₀)
- **COMPETENCIES:** compute capacitance from geometry; predict C changes from geometry changes; compute Q, ΔV, E, U for a capacitor; determine dielectric constants; combine capacitors in series and parallel and distribute charge/voltage
- **DIFFICULTY:** Overall MEDIUM (formula-driven with a few deep ideas); two HARD sub-concepts: the series-combination logic, and the dielectric mechanism
- **ESTIMATED STUDY TIME:** ~90 minutes (≈50 min lesson + ≈40 min practice)

**Position in the ARETE learning flow:** LEARN + PRACTICE. Gated on Lecture 4 (potential difference + Gauss's law). Serves as the capstone PROVE/TRANSFER opportunity for the whole electrostatics arc — every concept from Lectures 1–4 converges here — and the launchpad for DC circuits (Lecture 6).

---

## 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Describe a capacitor's structure and explain how it stores equal-and-opposite charges with a field E₀ = ΔV₀/d between the plates.
2. Define capacitance as C = Q/ΔV, state the farad, and explain why C is a fixed property of a given device's geometry and material.
3. Derive (or reconstruct) C₀ = ε₀A/d from Gauss's law and the uniform-field relation.
4. Predict quantitatively how doubling the area, halving the separation, or both, changes C.
5. Compute any of Q, C, ΔV given the other two.
6. Evaluate the energy stored using all three equivalent forms (Q²/2C, ½QΔV, ½CΔV²) and the energy density u = ½εE².
7. Explain the dielectric mechanism (polarization → induced opposing field) and trace the chain E = E₀/k → ΔV = ΔV₀/k → C = kC₀ with Q = Q₀.
8. Use C = kε₀A/d = εA/d and k = ε/ε₀ to find k from measured quantities.
9. Combine capacitors: parallel (C_eq = ΣCᵢ) and series (1/C_eq = Σ1/Cᵢ), including n identical cases, and distribute Q or ΔV across each capacitor.

---

## 4. WEB-READY LESSON

# Lecture 5 — Capacitors: Capacitance, Energy, Dielectrics, and Combinations

## Prerequisites
The student should already understand:
- Charge, field, and the field's direction rules (Lectures 1–3)
- Gauss's law: Φ = q_in/ε₀ (Lecture 4)
- Potential difference and E = ΔV/d in a uniform field (Lecture 4)
- ε₀ = 8.85 × 10⁻¹² C²/(N·m²)

---

### 1. What Is a Capacitor?

#### Core Idea
A capacitor is a charge-storage device: two metal conductors placed close together but **not touching**, carrying equal and opposite charges.

#### Explanation
The structure is almost disarmingly simple — two conductors separated by a small gap (the classic design: two parallel plates). Connect a potential difference ΔV₀ across them and the device "quickly becomes charged": +Q₀ accumulates on one plate, −Q₀ on the other. Between the plates appears a (nearly) uniform electric field obeying the Lecture 4 relation:

> **E₀ = ΔV₀ / d**

with d the plate separation. Everything in this lecture is the story of three linked quantities — Q₀, ΔV₀, and the geometry — and the constant that ties them together.

#### Example
A parallel-plate capacitor with a 12 V battery across a 1 mm gap creates E = 12/10⁻³ = 12,000 V/m between its plates (the source's own Example 3c).

#### Key Point
Two conductors, never touching: equal-and-opposite charges, a field in the gap, and a voltage across it — related by E = ΔV/d.

---

### 2. Capacitance: The Device's Charge-per-Volt Rating

#### Core Idea
Capacitance C is the ratio of the charge on either conductor to the potential difference between them — how much charge you get per volt.

#### Explanation
Experiment shows the plate charge Q₀ is **directly proportional** to the applied voltage ΔV₀:

> **Q₀ ∝ ΔV₀  →  Q₀ = C₀ΔV₀  →  C₀ = Q₀/ΔV₀**

Capacitance is defined as *the ratio of the magnitude of the charge on either conductor to the magnitude of the potential difference between the conductors.* Its unit:

> **Coulomb/Volt = F (farad)**

The crucial conceptual point: C is **not** the amount of charge stored — it's the exchange rate between charge and voltage. For a fixed device, C is fixed by its geometry and the material in the gap: double the battery voltage and Q doubles too, leaving C = Q/ΔV untouched. One farad is enormous; real devices live in μF (10⁻⁶), nF (10⁻⁹), and pF (10⁻¹²) territory.

#### Example
The source's Example 2a: conductors carrying ±10.0 μC at 10.0 V → C = 10 μC/10 V = **1 μF**. When the charge grows to ±100 μC (Example 2b), the voltage climbs to 100 V — but C is still 1 μF. The ratio never moved.

#### Key Point
C = Q/ΔV is a property of the *device*, not of the moment: charge and voltage scale together, and their ratio is the capacitance.

---

### 3. The Parallel-Plate Formula: C₀ = ε₀A/d

#### Core Idea
Gauss's law converts the plate geometry into a hard formula: capacitance grows with plate area and shrinks with separation.

#### Explanation
Reconstruct the source's derivation in three moves:

1. **Gauss's law** (Lecture 4) over a plate of area A with charge Q₀: Φ_E = E₀A = Q₀/ε₀ → E₀ = Q₀/(ε₀A).
2. **The uniform-field relation** (Lecture 4): E₀ = ΔV₀/d.
3. **Equate and match to Q₀ = C₀ΔV₀:**

   Q₀/(ε₀A) = ΔV₀/d  →  Q₀ = (ε₀A/d)·ΔV₀  →  **C₀ = ε₀A/d**

Two design knobs follow immediately:

> **C ∝ A (area of each plate)**  and  **C ∝ 1/d (distance between the plates)**

Bigger plates collect more charge for the same voltage; a wider gap weakens the field per volt and reduces the stored charge. Engineers "build" a capacitance exactly this way — choose A and d.

#### Example
The source's Example 1, in one line each:
- Double the area: C₂ = ε₀(2A)/d = **2C₁**
- Halve the separation: C₂ = ε₀A/(d/2) = **2C₁**
- Do both: C₂ = ε₀(2A)/(d/2) = **4C₁**

#### Key Point
C₀ = ε₀A/d. Area is the gas pedal; separation is the brake. Full worked versions below.

---

### 4. Energy Stored in a Charged Capacitor

#### Core Idea
The work done while charging — pushing positive and negative charges apart onto the plates — is stored as electric potential energy, with three equivalent expressions.

#### Explanation
Charging costs work: the battery must pile + charge onto one plate and − charge onto the other against their mutual attraction. That work appears as energy stored in the capacitor:

> **U = Q²/2C = ½QΔV = ½C(ΔV)²** (Joule)

All three forms describe the *same* stored energy — pick whichever matches the variables you know:

- Know Q and C → Q²/2C
- Know Q and ΔV → ½QΔV
- Know C and ΔV → ½C(ΔV)²

(They are mutually consistent through Q = CΔV — verified numerically in the worked examples.)

#### Example
A 53 pF capacitor at 12 V: U = ½C(ΔV)² = ½(53 × 10⁻¹²)(144) ≈ 3.8 × 10⁻⁹ J — and the same value comes out of Q²/2C and ½QΔV (full check below).

#### Key Point
Stored energy = the charging work; three interchangeable formulas; never forget the ½.

---

### 5. Energy Density: u = ½εE²

#### Core Idea
Dividing the stored energy by the volume it occupies (A·d) shows that the energy lives *in the field itself*.

#### Explanation
The energy density is the energy stored per unit volume:

> **u = U/Volume = U/(Ad) = ½C(ΔV)²/(Ad)**

Substituting C = εA/d and ΔV = Ed:

u = ½(εA/d)(Ed)²/(Ad) = **½ ε E²**  (J/m³)

A remarkable simplification: the geometry (A and d) vanishes completely — the density depends only on the field strength and the medium's permittivity ε (= kε₀). Wherever a field E exists in a medium ε, energy sits there at density ½εE².

#### Example
*(Pedagogical, from source formulas and Example 3c's numbers)*: the 12,000 V/m field in the air gap stores u = ½(8.85 × 10⁻¹²)(1.2 × 10⁴)² ≈ 6.4 × 10⁻⁴ J/m³.

#### Key Point
u = ½εE² — energy per unit volume of field; no A, no d, just field strength and permittivity.

---

### 6. Dielectrics: The Insulator That Boosts Capacitance

#### Core Idea
Slide an insulating material between the plates and the capacitance multiplies by k — because the material's polarized molecules partially cancel the internal field.

#### Explanation
**Definition:** a dielectric is an insulating material that, when placed between a capacitor's plates, increases the capacitance.

**The mechanism, step by step:**
1. With air in the gap: C₀ = Q₀/V₀ and E₀ = ΔV₀/d.
2. Insert the dielectric: its molecules **polarize** — they stretch/align with the field, each becoming a tiny dipole.
3. The polarized molecules jointly produce an **induced field E′ pointing opposite to E₀**.
4. The net field inside is reduced by the factor k:

> **E = E₀ − E′ = E₀/k**

**The consequence chain (battery disconnected):**
- The charge has nowhere to go → **Q = Q₀** (locked on the plates).
- Weaker field over the same gap d → **ΔV = ΔV₀/k**.
- Same charge, less voltage → the ratio improves:

> **C = Q/V = Q₀/(ΔV₀/k) = kC₀ — capacitance increases.**

**The constants:**
- k = **dielectric constant** — unitless, **k ≥ 1** (equal to 1 for air).
- ε = **kε₀** = electric permittivity of the material; k = ε/ε₀ = εᵣ (relative permittivity).
- The master formula becomes:

> **C = kε₀A/d = εA/d**

#### Example
The source's Example 4: plates 0.028 m², gap 0.55 mm, dielectric of unknown k, 12 V battery, plate charge 3.62 × 10⁻⁸ C → k = 6.7. (Full solution below.)

#### Key Point
Dielectric polarizes → induced field fights E₀ → E and ΔV shrink by k → with Q fixed, C = Q/ΔV grows to kC₀ = εA/d.

---

### 7. Capacitors in Parallel

#### Core Idea
Side-by-side connection: every capacitor sees the same voltage, their charges add, and the equivalent capacitance is the plain sum.

#### Explanation
Capacitors in parallel share both terminals, so:

> **ΔV = ΔV₁ = ΔV₂** (same voltage across each)
> **Q_total = Q₁ + Q₂** (charges add)
> **C_eq = C₁ + C₂** — total capacitance **increases**
> **Q_total = C_eq·ΔV**

For **n identical** capacitors C in parallel: **C_eq = nC.**

Intuition from the plate formula: parallel is like *gluing plates side by side* — same gap, more total area, more capacitance. *(Pedagogical picture — consistent with C = ε₀A/d.)*

#### Example
4 μF ∥ 6 μF at 10 V: C_eq = 10 μF; Q₁ = 40 μC, Q₂ = 60 μC (each gets Qᵢ = CᵢΔV — the bigger capacitor takes more charge at the common voltage); total 100 μC = C_eqΔV ✓.

#### Key Point
Parallel: one voltage, charges add, C_eq = ΣCᵢ — always *bigger* than any single one.

---

### 8. Capacitors in Series

#### Core Idea
End-to-end connection: the same charge sits on every capacitor, voltages add, and the equivalent capacitance comes out *smaller* than the smallest individual.

#### Explanation
In a series chain, the conductor between two capacitors is isolated from the world — so the two facing plates must remain neutral overall: whatever −Q appears on one, +Q appears on the other. The result:

> **ΔV = ΔV₁ + ΔV₂ + ⋯** (voltages add along the chain)
> **Q_total = Q₁ = Q₂ = ⋯ = Q** (the *same* charge on each — the full Q, not a share)
> **1/C_eq = 1/C₁ + 1/C₂ + ⋯** — total capacitance **decreases**
> **Q_total = C_eq·ΔV**

For **n identical** capacitors C in series: **C_eq = C/n.**

Intuition from the plate formula: series is like *stacking the gaps* — same plate area, added separation, less capacitance. *(Pedagogical picture — consistent with C = ε₀A/d.)*

#### Example
4 μF in series with 6 μF at 10 V: 1/C_eq = 1/4 + 1/6 = 5/12 → **C_eq = 2.4 μF** (smaller than both!). Q = C_eqΔV = 24 μC on *each* capacitor; ΔV₁ = Q/C₁ = 6 V, ΔV₂ = Q/C₂ = 4 V — sum 10 V ✓, and note the *smaller* capacitor took the *larger* voltage.

#### Key Point
Series: same Q everywhere, voltages add, reciprocal sum — C_eq comes out *below* the smallest member. Each capacitor carries the FULL charge, never a fraction.

---

### Key Takeaways

- A capacitor = two non-touching conductors storing ±Q with a field E = ΔV/d in the gap.
- Capacitance is the ratio C = Q/ΔV (farad) — a device property, not the stored amount; Q and ΔV scale together.
- Parallel plates: C₀ = ε₀A/d — C ∝ A, C ∝ 1/d.
- Geometric scaling: area ×2 → C ×2; gap ÷2 → C ×2; both together → C ×4.
- Stored energy: U = Q²/2C = ½QΔV = ½C(ΔV)² — three forms of the same quantity.
- Energy density: u = ½εE² — energy lives in the field, independent of geometry.
- A dielectric's polarized molecules induce a field opposing E₀: E = E₀/k, and with the battery off, ΔV = ΔV₀/k while Q = Q₀.
- Therefore C = kC₀ = kε₀A/d = εA/d, with k unitless, ≥ 1, k = 1 for air, ε = kε₀.
- Parallel: same ΔV, charges add, C_eq = C₁ + C₂ (n identical → nC) — capacitance grows.
- Series: same Q on each, voltages add, 1/C_eq = 1/C₁ + 1/C₂ (n identical → C/n) — capacitance shrinks below the smallest.
- In series, the smaller capacitor takes the larger share of the voltage (ΔVᵢ = Q/Cᵢ).

### Self-Check (answers are not shown — attempt before checking)

1. Define capacitance and state its unit. Does a capacitor's C change if you connect it to a bigger battery? Justify.
2. A parallel-plate capacitor's plates are each 0.01 m² with a 0.5 mm air gap. Compute C.
3. If a capacitor's area is tripled and its separation is also tripled, what happens to C? Show the ratio.
4. Why does inserting a dielectric reduce the internal field E, and what does that do to ΔV (battery disconnected)?
5. In the dielectric scenario of this lecture, which quantities stay fixed and which change: Q, ΔV, E, C?
6. Two capacitors, 3 μF and 6 μF, are connected in parallel across 12 V. Find C_eq and the charge on each.
7. The same two capacitors are reconnected in series across 12 V. Find C_eq, the charge on each, and the voltage across each. Which capacitor has the larger voltage?
8. Explain, using charge conservation at the isolated middle conductor, why every capacitor in a series chain carries the same Q.
9. A charged capacitor is disconnected from its battery; a dielectric (k = 3) fills the gap. By what factor does the stored energy U change? (Hint: which form of U has only fixed quantities in it?)
10. Three identical 12 μF capacitors: what is C_eq in series? In parallel? What is the ratio?

---

## 5. FORMULAS

### F1 — Capacitance (definition)
**C = Q/ΔV** (F)
- **Q:** magnitude of charge on either conductor; **ΔV:** potential difference between the conductors.
- **When used:** any capacitor, from measured Q and ΔV.
- **Interpretation:** charge per volt — the device's storage efficiency; fixed by geometry and material.
- **Assumptions:** Q₀ ∝ ΔV₀ (linearity), as stated in the source.

### F2 — Field between plates
**E₀ = ΔV₀/d** (V/m = N/C)
- **d:** plate separation.
- **When used:** converting plate voltage ↔ internal field.
- **Interpretation:** uniform field between charged parallel plates (Lecture 4 relation, reused here).

### F3 — Parallel-plate capacitance (from Gauss's law)
**C₀ = ε₀A/d** (F)
- **A:** area of each plate; **d:** separation; **ε₀** = 8.85 × 10⁻¹² C²/(N·m²).
- **When used:** designing or analyzing an air-gap parallel-plate capacitor.
- **Interpretation:** C ∝ A, C ∝ 1/d — geometry sets the storage rating.
- **Assumptions:** parallel plates; field uniform across A; derived via Φ_E = E₀A = Q₀/ε₀.

### F4 — Stored energy (three equivalent forms)
**U = Q²/2C = ½QΔV = ½C(ΔV)²** (J)
- **When used:** energy in any charged capacitor — choose the form matching your knowns.
- **Interpretation:** the charging work, stored as electric potential energy.
- **Assumptions:** all three forms describe the same state (linked by Q = CΔV).

### F5 — Energy density
**u = U/(Ad) = ½εE²** (J/m³)
- **ε:** permittivity of the gap material (= kε₀; ε₀ for air).
- **When used:** energy per unit volume of field region.
- **Interpretation:** energy resides in the field itself; independent of plate geometry.

### F6 — Dielectric relations (battery disconnected)
**E = E₀ − E′ = E₀/k ; ΔV = ΔV₀/k ; Q = Q₀ ; C = kC₀**
- **E′:** induced field of the polarized dielectric (opposes E₀); **k:** dielectric constant.
- **When used:** analyzing a dielectric inserted into a charged, isolated capacitor.
- **Interpretation:** polarization weakens the net field → voltage drops → the charge-to-voltage ratio improves.
- **Assumptions:** Q has nowhere to flow (source's scenario); k ≥ 1, unitless; k = 1 for air.

### F7 — Capacitance with dielectric
**C = kε₀A/d = εA/d** ; **ε = kε₀** ; **k = ε/ε₀ = εᵣ**
- **When used:** any dielectric-filled capacitor; finding k from measured quantities.
- **Interpretation:** the dielectric upgrades the "effective ε₀" of the gap by the factor k.

### F8 — Parallel combination
**ΔV = ΔV₁ = ΔV₂ ; Q_total = Q₁ + Q₂ ; C_eq = C₁ + C₂ ; n identical: C_eq = nC ; Q_total = C_eqΔV**
- **When used:** capacitors sharing both terminals.
- **Interpretation:** charges add at a common voltage — total storage increases.

### F9 — Series combination
**ΔV = ΔV₁ + ΔV₂ + ⋯ ; Q_total = Q₁ = Q₂ = ⋯ = Q ; 1/C_eq = 1/C₁ + 1/C₂ + ⋯ ; n identical: C_eq = C/n ; Q_total = C_eqΔV**
- **When used:** capacitors forming a single chain.
- **Interpretation:** same charge everywhere, voltages add — total storage decreases below the smallest member.
- **Assumptions:** the internal node is electrically isolated (charge conservation on the facing plates).

---

## 6. WORKED EXAMPLES

### Worked Example 1 — Geometry changes (Source: Example 1)
*A parallel-plate capacitor has area A and separation d. What happens to C if: (1) the area is doubled; (2) the separation is halved; (3) both?*

**Case 1 — Area doubled:**
C₂ = ε₀(2A)/d → C₂/C₁ = 2ε₀A/d ÷ ε₀A/d = 2 → **C₂ = 2C₁**

**Case 2 — Separation halved:**
C₂ = ε₀A/(½d) = 2ε₀A/d → **C₂ = 2C₁**

**Case 3 — Both:**
C₂ = ε₀(2A)/(½d) = 4ε₀A/d → **C₂ = 4C₁**

**Insight:** the two knobs are independent multipliers — area ratios multiply C up, separation ratios multiply C up inversely.

---

### Worked Example 2 — C from Q and ΔV (Source: Example 2)
*Two conductors carry +10.0 μC and −10.0 μC with 10.0 V between them.*
*(a) Find the capacitance. (b) If the charges grow to ±100 μC, what is the new ΔV?*

**Step 1 — (a) Definition:**
C = Q/ΔV = (10 × 10⁻⁶)/10 = **10⁻⁶ F = 1 μF**

**Step 2 — (b) Same device ⇒ same C; solve for ΔV:**
ΔV = Q/C = (100 × 10⁻⁶)/(1 × 10⁻⁶) = **100 V**

**Insight:** nothing about the capacitor changed — a tenfold charge demands a tenfold voltage. C stayed at 1 μF throughout.

---

### Worked Example 3 — Full capacitor characterization (Source: Example 3)
*Plates 20 cm × 3 cm, 1 mm air gap. (a) Find C. (b) Charge at 12 V? (c) Field between the plates?*

**Step 1 — Convert units:**
A = 0.20 m × 0.03 m = 6.0 × 10⁻³ m² ; d = 1 × 10⁻³ m

**Step 2 — (a) Capacitance:**
C = ε₀A/d = (8.85 × 10⁻¹²)(6 × 10⁻³)/(1 × 10⁻³) = 53 × 10⁻¹² F = **53 pF**

**Step 3 — (b) Charge:**
Q = CΔV = (53 × 10⁻¹²)(12) = **636 × 10⁻¹² C**

**Step 4 — (c) Field:**
E = ΔV/d = 12/(1 × 10⁻³) = **12,000 V/m (or N/C)**

---

### Worked Example 4 — Energy consistency check *(pedagogical — built from the source's formulas and Example 3's numbers)*
*For the capacitor above (53 pF, 12 V, 636 × 10⁻¹² C), verify that all three energy forms agree.*

**Form 1:** U = ½C(ΔV)² = ½(53 × 10⁻¹²)(144) = 3.8 × 10⁻⁹ J
**Form 2:** U = ½QΔV = ½(636 × 10⁻¹²)(12) = 3.8 × 10⁻⁹ J
**Form 3:** U = Q²/2C = (636 × 10⁻¹²)²/(2 × 53 × 10⁻¹²) = 3.8 × 10⁻⁹ J

All three agree ✓ — they are one quantity in three costumes.

---

### Worked Example 5 — Finding the dielectric constant (Source: Example 4)
*A parallel-plate capacitor: area 0.028 m², separation 0.55 mm, gap filled with a dielectric of constant k. Connected to a 12 V battery, each plate carries 3.62 × 10⁻⁸ C. Find k.*

**Step 1 — Extract the data:**
A = 0.028 m², d = 0.55 × 10⁻³ m, ΔV = 12 V, Q = 3.62 × 10⁻⁸ C

**Step 2 — Start from the dielectric formula:**
C = kε₀A/d, and C = Q/ΔV → Q/ΔV = kε₀A/d

**Step 3 — Solve for k:**
k = Qd/(ΔV·ε₀·A)

**Step 4 — Substitute (numerator first):**
Qd = (3.62 × 10⁻⁸)(0.55 × 10⁻³) = 1.99 × 10⁻¹¹

**Step 5 — Denominator:**
ΔV·ε₀·A = (12)(8.85 × 10⁻¹²)(0.028) = 2.97 × 10⁻¹²

**Step 6 — Divide:**
k = 1.99 × 10⁻¹¹/2.97 × 10⁻¹² = **6.7**

**Sanity check:** C = Q/ΔV = 3.02 nF; the air-only version would be C₀ = ε₀A/d ≈ 0.45 nF; ratio 3.02/0.45 ≈ 6.7 ✓ — the dielectric multiplied the capacitance by exactly k.

---

### Worked Example 6 — Series vs. parallel, same pair *(pedagogical — from the source's combination formulas)*
*Capacitors 4 μF and 6 μF at 10 V, first in parallel, then in series.*

**Parallel:**
- C_eq = 4 + 6 = **10 μF**
- Q_total = C_eqΔV = (10 μF)(10 V) = **100 μC**
- Each at the full 10 V: Q₁ = 40 μC, Q₂ = 60 μC (sum 100 ✓ — the bigger capacitor holds more charge at a common voltage)

**Series:**
- 1/C_eq = 1/4 + 1/6 = 5/12 → **C_eq = 2.4 μF** (below both!)
- Q = C_eqΔV = (2.4 μF)(10 V) = **24 μC on each** (the full Q — not 12 each)
- Voltages: ΔV₁ = Q/C₁ = 24/4 = 6 V ; ΔV₂ = Q/C₂ = 24/6 = 4 V (sum 10 ✓)
- The **smaller** capacitor (4 μF) took the **larger** voltage (6 V).

**Insight:** identical hardware, two wiring choices, answers differing by more than a factor of 4 — the wiring *is* part of the device.

---

## 7. COMMON MISTAKES

**Mistake 1 — Treating capacitance as "the charge stored."**
- *What students do:* say "this capacitor has 100 μC of capacitance."
- *Why it's wrong:* C is the *ratio* Q/ΔV — a fixed rating. The same 1 μF capacitor holds 10 μC at 10 V or 100 μC at 100 V.
- *How to avoid:* always attach units and ask "per volt?": capacitance is charge **per volt**.

**Mistake 2 — Thinking a bigger battery changes C.**
- *What students do:* believe charging harder increases the capacitance.
- *Why it's wrong:* Q ∝ ΔV — both grow together, so the ratio stays fixed by geometry and material.
- *How to avoid:* only A, d, and k can change C (for this device family).

**Mistake 3 — Unit conversion slips with area.**
- *What students do:* enter 20 cm × 3 cm as 0.2 × 0.03 "m²" — correct here — but then treat 20 cm² as 0.20 m².
- *Why it's wrong:* 1 cm² = 10⁻⁴ m²; lengths and areas convert with *different* powers of ten.
- *How to avoid:* convert each *length* to meters first, then multiply — never convert the squared number directly from memory.

**Mistake 4 — Assuming equal voltages in series.**
- *What students do:* split the source voltage equally among series capacitors of different sizes.
- *Why it's wrong:* in series the *charge* is equal; voltages divide as ΔVᵢ = Q/Cᵢ — the smaller capacitor takes more.
- *How to avoid:* compute Q = C_eqΔV once, then divide by each Cᵢ.

**Mistake 5 — Assuming the charge splits in series.**
- *What students do:* give each of two series capacitors "half the charge."
- *Why it's wrong:* the isolated middle conductor forces the facing plates to stay neutral — each capacitor carries the *full* Q.
- *How to avoid:* remember: series shares charge, parallel shares voltage — never the reverse.

**Mistake 6 — Reciprocal error in series C_eq.**
- *What students do:* compute 1/C_eq = 1/6 + 1/3 = 1/2 and report "C_eq = ½ μF."
- *Why it's wrong:* 1/2 is the value of 1/C_eq — you must invert it: C_eq = 2 μF.
- *How to avoid:* box the last step: "flip the final reciprocal." Sanity check: series C_eq must be *smaller than the smallest* member (but still bigger than zero — not smaller than that).

**Mistake 7 — Adding voltages in parallel or assuming equal charges there.**
- *What students do:* in parallel, split the total charge equally between unequal capacitors.
- *Why it's wrong:* parallel means a *common voltage*: Qᵢ = CᵢΔV, so the bigger capacitor takes more charge.
- *How to avoid:* in parallel, start from the shared ΔV; in series, start from the shared Q.

**Mistake 8 — Believing the dielectric "adds charge."**
- *What students do:* say inserting a dielectric increases Q.
- *Why it's wrong:* in the source's (disconnected) scenario the charge is locked: Q = Q₀. What shrinks is ΔV; C rises *because* the denominator fell.
- *How to avoid:* trace the chain in order: E → ΔV → C. The charge is the anchor that never moves.

**Mistake 9 — Applying k to the wrong quantity.**
- *What students do:* multiply Q by k, or divide C by k.
- *Why it's wrong:* k multiplies C (C = kC₀) and divides E and ΔV. It never touches Q (disconnected case).
- *How to avoid:* write the three relations together: E/k, ΔV/k, C×k, Q unchanged.

**Mistake 10 — Energy formula slips.**
- *What students do:* drop the ½ (U = QΔV), or use ½C(ΔV)² with Q's value.
- *Why it's wrong:* each form has a fixed structure; losing the ½ doubles the energy, mixing variables destroys it.
- *How to avoid:* match the form to your knowns *before* substituting, and keep the ½ visible in every line.

---

## 8. LECTURE SUMMARY

# Lecture Summary

## What You Need to Know
- A capacitor stores charge on two non-touching conductors; the field between parallel plates is E = ΔV/d.
- Capacitance C = Q/ΔV (farad) — a device rating fixed by geometry and material; Q and ΔV scale together.
- Parallel plates: C₀ = ε₀A/d — area up ⇒ C up; gap up ⇒ C down.
- Energy stored: U = Q²/2C = ½QΔV = ½C(ΔV)² — one quantity, three forms.
- Energy density: u = ½εE² — stored in the field, independent of geometry.
- Dielectric: polarizing molecules induce an opposing field → E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, C = kC₀ = εA/d; k ≥ 1, unitless, k = 1 for air; ε = kε₀.
- Parallel combination: same ΔV, charges add, C_eq = C₁ + C₂ (n identical → nC).
- Series combination: same Q, voltages add, 1/C_eq = 1/C₁ + 1/C₂ (n identical → C/n) — smaller than the smallest member.
- In series, the smaller capacitor carries the larger voltage; in parallel, the bigger capacitor carries more charge.

## Key Definitions
- **Capacitor ("condenser")** → device that stores electric charge: two metal conductors near each other, not touching.
- **Capacitance (C)** → magnitude of charge on either conductor ÷ magnitude of potential difference between them; unit farad (C/V).
- **Dielectric** → insulating material placed between the plates that increases the capacitance.
- **Dielectric constant (k)** → unitless multiplier of capacitance; k ≥ 1; k = 1 for air; k = ε/ε₀ = εᵣ.
- **Permittivity of material (ε)** → ε = kε₀; upgrades the gap's "field-ability" over vacuum.
- **Energy density (u)** → stored energy per unit volume: ½εE².

## Key Formulas
- **C = Q/ΔV** → definition (charge per volt).
- **C₀ = ε₀A/d** → parallel-plate capacitance (air).
- **E = ΔV/d** → field in the gap.
- **U = Q²/2C = ½QΔV = ½C(ΔV)²** → stored energy.
- **u = ½εE²** → energy density.
- **E = E₀/k; ΔV = ΔV₀/k; Q = Q₀; C = kC₀** → dielectric chain (disconnected).
- **C = kε₀A/d = εA/d** → capacitance with dielectric.
- **Parallel: C_eq = C₁ + C₂; n identical: nC** → same ΔV.
- **Series: 1/C_eq = 1/C₁ + 1/C₂; n identical: C/n** → same Q.

## Important Ideas
- Capacitance is an *exchange rate*, not an amount — the deepest idea of the lecture.
- The Gauss's-law derivation ties Lectures 4 and 5 into one story: field from charge (Gauss), voltage from field (E = ΔV/d), charge from voltage (C).
- The dielectric improves storage not by adding charge but by *weakening the field's opposition* — same charge, cheaper voltage.
- Series and parallel are mirror images: series shares Q and adds ΔV; parallel shares ΔV and adds Q.
- Series intuition: stacked gaps (bigger d ⇒ smaller C). Parallel intuition: glued plates (bigger A ⇒ bigger C). Both straight from ε₀A/d.

## Common Mistakes
- C conflated with stored charge; battery assumed to change C.
- cm²/mm conversion slips.
- Equal voltages or split charges in series; equal charges in parallel.
- Forgetting the final reciprocal flip in 1/C_eq.
- Dielectric assumed to change Q; k applied to the wrong quantity.
- Missing ½ in energy formulas.

## Exam Focus
The concepts most likely to demand real understanding:
1. **Series combination logic** — same Q on every capacitor, voltage division ΔVᵢ = Q/Cᵢ, C_eq below the smallest.
2. **The dielectric chain** — reproducing E → ΔV → C in order, with Q fixed.
3. **Geometric scaling of C** — the "double A, halve d" style questions (source Example 1 pattern).
4. **Energy-form selection** — choosing the correct U formula for the given data.

## 60-Second Review
A capacitor: two plates, ±Q, field E = ΔV/d in the gap. Its rating is C = Q/ΔV — charge per volt, fixed by geometry: C = ε₀A/d. Bigger plates or tighter gap ⇒ bigger C; double A *and* halve d ⇒ ×4. Stored energy: Q²/2C = ½QΔV = ½CΔV², density ½εE². Slide in a dielectric: molecules polarize, induced field fights back — E and ΔV drop by k, charge stays put, so C = kC₀ = εA/d. Combinations: parallel shares voltage, adds charge, C_eq = ΣC (n identical → nC); series shares charge, adds voltages, 1/C_eq = Σ1/C (n identical → C/n) — series always comes out smaller than its smallest member, and the little capacitor takes the big voltage.

---

## 9. DIFFICULT CONCEPTS

### Difficult Concept: Capacitance as a Ratio, Not an Amount

**Why students struggle:** The word "capacitance" sounds like "capacity" — how much it holds. But C is a *fixed ratio*: doubling the voltage doubles the stored charge while C never budges.
**Simple explanation:** C is the exchange rate between charge and voltage for this device. A big-C capacitor is one that accepts a lot of charge *without* the voltage climbing much.
**Intuitive analogy:** A wide tank vs. a narrow tank: both can hold the same "charge" of water, but the wide one's water level ("voltage") rises far less per liter. Wide tank = high capacitance. The tank's width doesn't change when you pour more water in.
**Step-by-step explanation:** (1) Device built: C fixed by A, d, material. (2) Apply ΔV: charge Q = CΔV flows on. (3) Apply 2ΔV: 2Q flows on. (4) Compute C = Q/ΔV either time — identical. (5) To change C, change A, d, or k — never the battery.
**Mini example:** 1 μF capacitor: 10 V → 10 μC; 100 V → 100 μC. C = 1 μF in both cases.
**Misconception to avoid:** "Charging a capacitor more increases its capacitance." No — only geometry or dielectric can.
**Difficulty:** MEDIUM

### Difficult Concept: From Gauss's Law to C = ε₀A/d

**Why students struggle:** It's a two-formula bridge (Gauss + uniform field) ending in a "match the pattern" step (Q₀ = C₀ΔV₀) — students lose the thread halfway.
**Simple explanation:** Charge makes field (Gauss); field over a distance makes voltage; voltage per charge is capacitance. Three links, one chain.
**Intuitive analogy:** An assembly line: raw material (Q₀) → processed into field (E₀ = Q₀/ε₀A) → packaged as voltage (ΔV₀ = E₀d) → the conversion rate of the whole line is C.
**Step-by-step explanation:** (1) Gauss: Φ = E₀A = Q₀/ε₀ → E₀ = Q₀/(ε₀A). (2) Uniform field: E₀ = ΔV₀/d. (3) Equate: Q₀/(ε₀A) = ΔV₀/d. (4) Rearrange: Q₀ = (ε₀A/d)ΔV₀. (5) Compare with the definition Q₀ = C₀ΔV₀ → C₀ = ε₀A/d. (6) Read the knobs: C ∝ A, C ∝ 1/d.
**Mini example:** A = 0.006 m², d = 10⁻³ m → C = 8.85 × 10⁻¹² × 6 = 53 pF (the source's Example 3).
**Misconception to avoid:** "C depends on Q or ΔV." The derivation explicitly cancels them — only geometry and ε₀ survive.
**Difficulty:** MEDIUM

### Difficult Concept: The Three Energy Forms

**Why students struggle:** Three algebraically different expressions for one quantity feel like three separate laws; students grab the wrong one or mangle the ½'s.
**Simple explanation:** It's one bank balance readable in three currencies — pick the currency you actually hold: (Q, C), (Q, ΔV), or (C, ΔV).
**Intuitive analogy:** A trip's cost in dollars, euros, or pounds: different symbols, same money, linked by fixed exchange rates (here, Q = CΔV).
**Step-by-step explanation:** (1) Inventory your knowns. (2) Pick the matching form. (3) Substitute with the ½ in place. (4) Cross-check with a second form when possible (as in Worked Example 4).
**Mini example:** 53 pF at 12 V holding 636 pC: all three forms give 3.8 × 10⁻⁹ J.
**Misconception to avoid:** "U = QΔV" (missing ½) — that's the work of moving the *last* bit of charge, not the average over the whole charging process.
**Difficulty:** MEDIUM

### Difficult Concept: Series — Same Q, Smaller C_eq

**Why students struggle:** Two instincts misfire at once: "components in a chain share the load" (they expect Q/2 on each) and "more parts = more capability" (they expect C_eq to grow). Reality is the opposite on both counts.
**Simple explanation:** The conductor between two series capacitors is electrically isolated — its net charge must stay zero. So whatever charge appears on one side of it, the opposite appears on the other: every capacitor ends up with the *full* Q. And since the voltages add, the combination demands more volts per charge — a *worse* exchange rate, i.e., smaller C.
**Intuitive analogy:** Two rooms connected by a sealed (uncharged) door. If 20 people crowd into the left room, the sealed door's two faces must show matching crowds on both sides — you can't pile people "into the door." Series water pipes: the same water passes every section; the pressure drops add.
And the geometry picture: series = stacking the gaps — same plate area, double the separation, half the capacitance (straight from ε₀A/d).
**Step-by-step explanation:** (1) Mark the isolated middle node: its total charge is conserved at zero. (2) Land +Q on the outer plate of C₁ → −Q induced on its facing plate. (3) Zero net on the node → +Q on C₂'s near plate → −Q on its far plate. (4) Every capacitor holds Q — the full amount. (5) Voltages: ΔVᵢ = Q/Cᵢ, and they add. (6) C_eq = Q/ΔV_total = Q/Σ(Q/Cᵢ) → 1/C_eq = Σ(1/Cᵢ). (7) Consequence: C_eq < smallest Cᵢ, and the smaller capacitor gets the bigger ΔVᵢ.
**Mini example:** 4 μF + 6 μF in series: C_eq = 2.4 μF — less than 4, less than 6. At Q = 24 μC: 6 V across the 4 μF, 4 V across the 6 μF.
**Misconception to avoid:** "Each series capacitor gets half the charge." Each gets ALL of it — voltage is what divides.
**Difficulty:** HARD

### Difficult Concept: The Dielectric Mechanism

**Why students struggle:** An *insulator* improving a charge-storage device is backwards-sounding. And the causal chain (polarize → field weakens → voltage drops → ratio improves) runs opposite to the "more stuff = more charge" instinct.
**Simple explanation:** The dielectric's molecules line up with the field and push back against it. The internal field weakens, so the same locked-on charge produces less voltage — and less voltage per charge *means* more capacitance.
**Intuitive analogy:** A spring mattress under a weight: the mattress compresses and pushes back, so the same weight sits at a lower height. Weaker net opposition, lower "height" (voltage), better rating. Or a crowd leaning into a wind: the people's pushback means the wind's net effect through the crowd is reduced.
**Step-by-step explanation:** (1) Charged capacitor, battery disconnected: Q₀ locked on the plates, field E₀. (2) Insert dielectric: its molecules polarize — stretch/align along the field. (3) The aligned molecules create an induced field E′ *opposing* E₀. (4) Net field: E = E₀ − E′ = E₀/k (weaker). (5) Same gap d ⇒ ΔV = Ed = ΔV₀/k (lower). (6) Q = Q₀ (unchanged — nowhere to go). (7) C = Q/ΔV = Q₀/(ΔV₀/k) = kC₀ (bigger). (8) Master formula: C = kε₀A/d = εA/d.
**Mini example:** Air capacitor 100 pF, disconnect, insert k = 4: C → 400 pF; ΔV drops to a quarter; Q unchanged.
**Misconception to avoid:** "The dielectric adds charge." In this scenario Q never moves — C rises because ΔV *fell*.
**Difficulty:** HARD

---

## 10. VIDEO LESSON PLANS

*(Plans for the two HARD concepts.)*

### VIDEO 1

**VIDEO TITLE:** More Parts, Less Capacitance? Series vs. Parallel, Finally Explained

**TARGET CONCEPT:** Capacitor combinations — why series forces the same Q on every capacitor, why voltages add, and why C_eq comes out *smaller* than the smallest (vs. parallel's plain sum)

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can compute C_eq for series and parallel combinations, distribute Q and ΔV correctly across each capacitor, and explain the isolated-middle-node argument for equal charges.

**HOOK:** "Two identical capacitors. Wire them side by side — you get double. Wire them end to end — you get HALF of one. You *added* a component and the value went DOWN. If that sounds like broken math, stay with me: in eight minutes you'll not only compute it, you'll be able to explain *why* to anyone."

**EXPLANATION:**
1. Reframe the question: C_eq is just "charge in per volt out" for the whole blob.
2. Parallel: everything shares two terminals → same ΔV → charges add → C_eq = ΣCᵢ.
3. Series: the spotlight on the isolated middle node — zero net charge, always.
4. The induction cascade: +Q on the outer plate forces −Q then +Q then −Q down the chain — every capacitor gets the FULL Q.
5. Voltages add: ΔV_total = Σ(Q/Cᵢ) → 1/C_eq = Σ(1/Cᵢ).
6. Geometry intuition: series = stacked gaps (d grows ⇒ C shrinks); parallel = glued plates (A grows ⇒ C grows).
7. Worked example with voltage division and the "smaller cap, bigger voltage" punchline.

**VISUALS:**
- Two-terminal "blob" framing: charge entering one terminal, leaving the other, voltage meter across the blob.
- The middle node circled and "sealed" with a padlock icon; charge conservation equation floating beside it (−Q + +Q = 0).
- Domino-style induction animation: +Q lands → −Q appears → +Q appears → −Q appears, labeled "the full Q everywhere."
- Side-by-side gap-stacking (series) and plate-gluing (parallel) animations, synced to C = ε₀A/d.
- Voltage bar charts over each capacitor summing to the source voltage.

**EXAMPLE:** 4 μF and 6 μF at 10 V, both wirings (parallel: 10 μF, 100 μC total; series: 2.4 μF, 24 μC each, 6 V + 4 V).

**COMMON MISTAKE:** Charge "splitting" in series; equal voltages assumed; the un-flipped reciprocal (1/C_eq reported as C_eq).

**CHECK FOR UNDERSTANDING:** "Three identical 12 μF capacitors: predict first — which wiring gives the bigger C_eq? Then compute both."

**FINAL TAKEAWAY:** Series shares charge and adds voltages → reciprocal sum → smaller than the smallest. Parallel shares voltage and adds charges → plain sum. Stacked gaps vs. glued plates.

---

### VIDEO 2

**VIDEO TITLE:** The Insulator That Multiplies Your Capacitor: Dielectrics

**TARGET CONCEPT:** Dielectric mechanism — polarization, induced opposing field, E = E₀/k, ΔV = ΔV₀/k, Q = Q₀, C = kC₀

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can narrate the dielectric chain in order, compute the new C, ΔV, and E after insertion (battery disconnected), and extract k from measured data.

**HOOK:** "Take a charged capacitor. Disconnect the battery. Now slide an ordinary piece of plastic — a *non-conductor*, something electricity can't pass through at all — between the plates. The capacitance multiplies. By seven, if it's the lecture's mystery material. How does something that blocks charge make a charge-storage device *better*? This is the strangest — and most useful — trick in this whole chapter."

**EXPLANATION:**
1. Setup: air-gap capacitor, charged, battery disconnected — Q₀ locked on.
2. Insert the dielectric: insulating, but its molecules polarize — stretch and align with the field.
3. Each molecule becomes a tiny dipole; together they generate an induced field E′ pointing *opposite* E₀.
4. Net field: E = E₀ − E′ = E₀/k — weakened, not eliminated.
5. Consequence chain: same gap, weaker field → ΔV = ΔV₀/k; charge locked → Q = Q₀; ratio → C = kC₀.
6. Constants: k unitless, ≥ 1, k = 1 for air; ε = kε₀; C = kε₀A/d = εA/d.
7. Worked example: extracting k = 6.7 from the source's data.

**VISUALS:**
- Capacitor with visible field lines; a dielectric slab sliding in.
- Molecules drawn as neutral circles that stretch into dipole ellipses, rotating into alignment.
- Induced-field arrows (E′) appearing opposite E₀; the two arrow stacks partially canceling, with the surviving net labeled E = E₀/k.
- A "locked charge" padlock on Q while ΔV's meter visibly drops.
- The mystery-material worked example with live numbers and a k-counter climbing to 6.7.

**EXAMPLE:** The source's Example 4: A = 0.028 m², d = 0.55 mm, 12 V battery, Q = 3.62 × 10⁻⁸ C → k = 6.7 (with the C = 3.02 nF vs. C₀ = 0.45 nF sanity check).

**COMMON MISTAKE:** Thinking Q increases; applying k to Q instead of C; believing the field gets stronger; assuming k has units or can be below 1.

**CHECK FOR UNDERSTANDING:** "Air capacitor, 100 pF, charged to 12 V, battery removed, insert k = 4. New C? New ΔV? What stayed fixed?"

**FINAL TAKEAWAY:** The dielectric's molecules fight the field: E and ΔV drop by k, the locked charge stays, so C = Q/ΔV rises to kC₀ = εA/d. An insulator that makes storage *better*.

---

## 11. VIDEO SCRIPTS

### VIDEO SCRIPT 1 — More Parts, Less Capacitance?

**[0:00–0:30] Hook**
"Here are two identical capacitors — six microfarads each. Connect them side by side, in parallel: the combination is twelve microfarads. Fine, that makes sense. Now connect them end to end, in series: three microfarads. Wait — that's HALF of a single one. I just added a second component, and my storage went DOWN? If your brain is quietly filing this under 'circuit voodoo,' this video is for you. By the end you'll compute it, predict it, and — the real test — explain *why* it has to be true."

**[0:30–2:00] Concept introduction**
"First, let's be crystal clear about what we're computing. When we ask for the equivalent capacitance C-e-q, we're treating the whole wired blob as ONE mystery device: I push charge plus-Q onto one terminal, charge minus-Q comes off the other, and a voltage delta-V appears across the blob. C-e-q is just Q over delta-V — charge in, per volt out. That's the only question. Now, parallel is the easy case, so let's kill it fast. In parallel, both capacitors are clipped to the *same two terminals* — whatever voltage the battery applies, each capacitor sees *all of it*. Same delta-V for everyone. And each stores its own charge, Q-one equals C-one delta-V, Q-two equals C-two delta-V. The battery had to supply both — total charge is the sum. Sum of charges at a common voltage: C-e-q equals C-one plus C-two. Bigger than either one. Parallel adds storage. Done. Now the strange one — series."

**[2:00–4:00] Visual explanation**
"Series: capacitor one, then a connecting wire, then capacitor two. And I want you to stare at that middle wire — the conductor *between* the two capacitors. Here's the thing about it: it's connected to nothing else. It's an island. Electrically isolated. And an isolated conductor keeps its total charge at zero — always; charge can't appear from nowhere. Now watch the dominoes fall. I push plus-Q onto the left terminal of capacitor one. That positive charge pulls negative charge onto the plate facing it — the right plate of capacitor one goes to minus-Q. But that right plate is part of our island! The island's total must stay zero — so if its left side just went minus-Q, its right side — the left plate of capacitor two — must go plus-Q. And THAT positive pulls minus-Q onto the far plate of capacitor two. Look at the pattern: plus-Q, minus-Q, plus-Q, minus-Q. Every single capacitor in the chain carries the exact same charge — the FULL Q. Not Q-over-two. Not 'its share.' The full amount. Series shares charge. That's rule one. Rule two: the voltages. Each capacitor builds its own voltage, Q over C — and walking from one end of the chain to the other, you climb each voltage in turn. They add. And if you're adding voltage for the same charge, the exchange rate — charge per volt — has gotten WORSE. That's why C-e-q comes out smaller. One over C-e-q equals one over C-one plus one over C-two — smaller than the smallest member, every time. Want a picture? Series is just stacking the gaps: same plate area, twice the separation — and C equals epsilon-A over d, so double the gap, half the capacitance. Parallel is gluing plates side by side: same gap, twice the area, double the C. The wiring *is* geometry."

**[4:00–6:00] Worked example**
"Numbers. Four microfarads and six microfarads — first in parallel across ten volts, then in series across ten volts. Parallel: C-e-q is four plus six — ten microfarads. Total charge: ten micro times ten volts — one hundred microcoulombs. Each capacitor sits at the full ten volts: the four-microfarad holds forty microcoulombs, the six holds sixty. The bigger one carries more — at a shared voltage, capacity rules. Now series. One over C-e-q: one quarter plus one sixth — three twelfths plus two twelfths — five twelfths. So C-e-q is twelve over five: two point four microfarads. Less than four. Less than six. Smaller than the smallest. Total charge from the source: two point four micro times ten volts — twenty-four microcoulombs. And here's the sentence that separates the exam-ready from the rest: EVERY capacitor holds twenty-four microcoulombs. The full Q. Now the voltages: the four-microfarad builds twenty-four over four — six volts. The six-microfarad: twenty-four over six — four volts. Six plus four is ten ✓. And notice the twist — the SMALLER capacitor took the LARGER voltage. Same charge, smaller capacity, bigger price in volts. Remember that; it's a favorite exam fact."

**[6:00–7:00] Common mistake**
"Three mistakes, all deadly. Mistake one: 'the charge splits in series.' No. Twenty-four microcoulombs on each — not twelve. The isolated middle node *forces* the full charge onto everyone. If you remember one image from this video, remember the padlocked island. Mistake two: 'series capacitors share the voltage equally.' Only when they're identical. Unequal capacitors divide the voltage in inverse proportion — smaller C, bigger slice. Mistake three, the arithmetic assassin: you compute one-over-C-e-q equals one-half — and you write down 'C-e-q equals half a microfarad.' No! One over C-e-q is one-half means C-e-q is TWO. The last step of every series problem is flipping that reciprocal — and it's the step most often skipped under exam pressure. Sanity check that catches it instantly: series C-e-q must be smaller than the smallest capacitor, but never absurdly small — half a microfarad from six and three? Suspicious. Two? Plausible."

**[7:00–8:00] Quick student challenge**
"Your turn — three identical twelve-microfarad capacitors. Before touching a calculator: which wiring gives the bigger C-e-q, and roughly what should the answers be? Pause and commit. … Series: one over C-e-q is three over twelve — a quarter — C-e-q is four microfarads. Parallel: three times twelve — thirty-six microfarads. The parallel answer is *nine times* the series answer — same parts, same pile on the table, just different wiring. If you'd guessed 'series gives thirty-six,' you're not alone — that's exactly the intuition this video exists to overwrite."

**[8:00–8:30] Final recap**
"Thirty seconds. Parallel: everyone shares the voltage, charges add, C-e-q is the plain sum — glued plates, more area, more storage. Series: an isolated middle node locks the FULL charge onto every capacitor, voltages stack, and one over C-e-q is the sum of reciprocals — stacked gaps, more separation, less storage, always below the smallest member. Series shares charge. Parallel shares voltage. Never the reverse."

---

### VIDEO SCRIPT 2 — The Insulator That Multiplies Your Capacitor

**[0:00–0:30] Hook**
"Watch this. I've got a charged capacitor — plates, charge, field, voltage, the works. I disconnect the battery. And now I slide an ordinary piece of plastic between the plates. Plastic — an insulator — something electric charge cannot pass through *at all*. And the capacitance… multiplies. If it's the mystery material from your lecture, it multiplies by almost seven. How does something that *blocks* electricity make an electricity-storage device *better*? Stick around — because this is the single strangest, most useful trick in the capacitor chapter."

**[0:30–2:00] Concept introduction**
"Setup first. A parallel-plate capacitor with air in the gap, charged up, and then — key detail — the battery is disconnected. That means the charge Q-zero on the plates is *locked*. It has nowhere to flow. The field between the plates is E-zero, the voltage across the gap is delta-V-zero. Frozen picture. Now the plastic. Yes, it's an insulator — no free charges drifting through it. But its *molecules* are a different story. Each molecule is neutral, but in an electric field, its positive nucleus and negative electron cloud get pulled in opposite directions — the molecule *stretches*. It becomes a tiny dipole, a microscopic plus-minus arrow, and it swings to line up with the field. Millions of molecules, all leaning the same way. And here's the punchline: a forest of aligned dipoles creates its own electric field — an *induced* field, E-prime — pointing exactly OPPOSITE to the field that stretched them. The dielectric fights back."

**[2:00–4:00] Visual explanation**
"So what does the field look like now? Original field E-zero, pushing right. Induced field E-prime, pushing left. The net field is the difference: E equals E-zero minus E-prime — weakened, but not erased. Your lecture writes that as E equals E-zero over k, where k is the dielectric constant — a number that's one for air and *at least* one for every real material. Follow the chain now, because each link is forced. Same gap d, weaker field → the voltage across the gap drops: delta-V equals E-d equals delta-V-zero over k. The charge? Locked — Q equals Q-zero; the battery's gone, the charge has nowhere to move. So pause and look at the scorecard: same charge, less voltage. And what is capacitance? Charge per volt. Same numerator, smaller denominator — the ratio IMPROVES. C equals Q over delta-V equals Q-zero over delta-V-zero-over-k — that's k times C-zero. The capacitance multiplied by k. That's the whole trick: the dielectric doesn't add charge — it makes the existing charge *cheaper in volts*. One formula collects everything: C equals k-epsilon-zero-A over d — or, defining the material's permittivity epsilon as k times epsilon-zero, C equals epsilon-A over d. k is unitless, bigger than or equal to one — and if a material ever seemed to give k less than one, you've made a sign error somewhere."

**[4:00–6:00] Worked example**
"Your lecture's own mystery material. A capacitor: plate area zero point zero two eight square meters, gap zero point five five millimeters, filled with a dielectric of unknown constant k. Connect a twelve-volt battery — each plate ends up with three point six two times ten to the minus eight coulombs. Find k. Path: the capacitor's actual capacitance is C equals Q over delta-V — three point six two times ten to the minus eight, divided by twelve — about three point zero two nanofarads. But the formula with a dielectric says C equals k epsilon-zero A over d. Set them equal and solve for k: k equals Q-d over delta-V epsilon-zero A. Numerator: three point six two times ten to the minus eight times zero point five five times ten to the minus three — one point nine nine times ten to the minus eleven. Denominator: twelve, times eight point eight five times ten to the minus twelve, times zero point zero two eight — two point nine seven times ten to the minus twelve. Divide: k equals six point seven. And a free sanity check: what would this capacitor be with *air*? Epsilon-zero A over d — about zero point four five nanofarads. The real one is three point zero two. Ratio: six point seven. The dielectric multiplied the capacitance by exactly its own constant. Physics checking itself — beautiful."

**[6:00–7:00] Common mistake**
"Four traps. Trap one, the big one: 'inserting the dielectric adds charge.' In our scenario — battery off — the charge is *locked*; Q never moves. What changes is the voltage. The capacitance rises because the *denominator* fell, not because the numerator grew. If you ever catch yourself multiplying Q by k, stop — k multiplies C and divides E and delta-V. It never touches the charge. Trap two: 'the field gets stronger inside.' Opposite — the polarized molecules are *canceling* part of it; E equals E-zero over k. Trap three: units on k. None. It's a pure ratio — epsilon over epsilon-zero. And it can't be below one: no material amplifies the field past what vacuum would do. Trap four: confusing the two scenarios. Everything above assumes the battery is disconnected. If the battery stays connected, the voltage is what's locked instead — a different story, and your lecture keeps it out of scope. When in doubt, ask first: what's frozen — the charge or the voltage?"

**[7:00–8:00] Quick student challenge**
"Your turn. Air capacitor, one hundred picofarads, charged to twelve volts. Battery removed. In comes a slab with k equals four. Three answers: new capacitance? New voltage? And what quantity never moved? Pause — all three. … Capacitance: k C-zero — four hundred picofarads. Voltage: delta-V-zero over k — twelve over four — three volts. The unmoved quantity: the charge — whatever was locked on the plates when you unplugged the battery, exactly one point two nanocoulombs, is still sitting there. Bigger tank rating, lower water level, same amount of water."

**[8:00–8:30] Final recap**
"The dielectric in thirty seconds. Its molecules polarize — stretch and align — and their induced field fights the original: E equals E-zero over k. Same gap, weaker field → voltage drops to delta-V-zero over k. Battery off → charge locked at Q-zero. Same charge over smaller volts → C equals k-C-zero — or epsilon-A over d, with epsilon equals k-epsilon-zero. The insulator doesn't feed the capacitor; it *disarms* the field. That's the trick — and it's why every real capacitor you'll ever open is stuffed with nothing-conductor."

---

## 12. PRACTICE QUESTIONS

*(Student-facing questions. Instructor keys are for platform use and must not be displayed with the question.)*

### LEVEL 1 — UNDERSTAND

**Q1.** Define capacitance and state its unit. Does C change when the capacitor is connected to a larger battery? Justify.
> *Instructor key — Answer:* C = Q/ΔV — magnitude of charge on either conductor over the potential difference between them; unit farad (C/V). No: Q ∝ ΔV, so the ratio is fixed by geometry and material; only A, d, or k can change C. *Skill:* ratio concept. *Difficulty:* EASY.

**Q2.** Why does doubling the plate area double C, while doubling the separation halve it? Answer using C = ε₀A/d.
> *Instructor key — Answer:* C ∝ A (more area collects more charge per volt at the same field) and C ∝ 1/d (a wider gap means a weaker field E = ΔV/d per volt, hence less charge). Doubling A → ×2; doubling d → ×½. *Skill:* geometric scaling. *Difficulty:* EASY.

**Q3.** State what happens to E, ΔV, Q, and C when a dielectric is inserted into a charged, *disconnected* capacitor.
> *Instructor key — Answer:* E → E₀/k (weakened); ΔV → ΔV₀/k; Q = Q₀ (unchanged — locked); C → kC₀ (increased). *Skill:* dielectric chain. *Difficulty:* MEDIUM.

**Q4.** In a series combination, which quantity is the same on every capacitor? In a parallel combination?
> *Instructor key — Answer:* Series: the charge Q (full, not shared). Parallel: the voltage ΔV. *Skill:* combination signatures. *Difficulty:* EASY.

**Q5.** True or false, with justification: a dielectric constant k can be less than 1, and it carries units.
> *Instructor key — Answer:* False on both: k is unitless (a ratio ε/ε₀) and k ≥ 1, with k = 1 for air. *Skill:* constant properties. *Difficulty:* EASY.

**Q6.** Why is the equivalent capacitance of a series combination always smaller than the smallest capacitor in it?
> *Instructor key — Answer:* Same Q on each forces voltages ΔVᵢ = Q/Cᵢ that add; the combination needs MORE total voltage for the same charge than any single member would — a worse charge-per-volt ratio: 1/C_eq = Σ1/Cᵢ > 1/C_smallest. *Skill:* series reasoning. *Difficulty:* MEDIUM.

### LEVEL 2 — APPLY

**Q7.** A parallel-plate capacitor has plates of area 0.1 m² separated by 0.2 mm of air. Find C, the charge at 9 V, the field between the plates, and the stored energy.
> *Instructor key — Answer:* C = ε₀A/d = (8.85 × 10⁻¹²)(0.1)/(2 × 10⁻⁴) = 4.4 × 10⁻⁹ F ≈ 4.4 nF; Q = CΔV ≈ 4.0 × 10⁻⁸ C; E = ΔV/d = 4.5 × 10⁴ V/m; U = ½C(ΔV)² ≈ 1.8 × 10⁻⁷ J. *Skill:* full characterization. *Difficulty:* MEDIUM.

**Q8.** A capacitor has C = 20 pF. Predict the new C after (a) the area is doubled; (b) additionally the separation is halved.
> *Instructor key — Answer:* (a) 40 pF; (b) 80 pF (×2 from area, ×2 from gap — independent multipliers, the source's Example 1 pattern). *Skill:* scaling. *Difficulty:* EASY–MEDIUM.

**Q9.** Capacitors of 3 μF and 6 μF are connected in parallel across 12 V. Find C_eq, the charge on each, and the total charge.
> *Instructor key — Answer:* C_eq = 9 μF; Q₁ = 36 μC, Q₂ = 72 μC (Qᵢ = CᵢΔV — bigger takes more); total 108 μC = C_eqΔV ✓. *Skill:* parallel distribution. *Difficulty:* MEDIUM.

**Q10.** The same 3 μF and 6 μF are reconnected in series across 12 V. Find C_eq, the charge on each, and the voltage across each.
> *Instructor key — Answer:* 1/C_eq = 1/3 + 1/6 = 1/2 → C_eq = 2 μF; Q = C_eqΔV = 24 μC on EACH; ΔV₁ = 24/3 = 8 V, ΔV₂ = 24/6 = 4 V (sum 12 ✓; smaller cap → larger voltage). *Skill:* series distribution. *Difficulty:* MEDIUM.

**Q11.** A dielectric-filled capacitor (k = 5) has plate area 0.02 m² and gap 0.1 mm. Find its capacitance.
> *Instructor key — Answer:* C = kε₀A/d = (5)(8.85 × 10⁻¹²)(0.02)/(10⁻⁴) = 8.85 × 10⁻⁹ F ≈ 8.9 nF. *Skill:* dielectric formula. *Difficulty:* MEDIUM.

**Q12.** A 12 μF capacitor is charged to 50 V. Find the stored energy via all three formulas and confirm they agree.
> *Instructor key — Answer:* Q = 600 μC. U = ½C(ΔV)² = ½(12 × 10⁻⁶)(2500) = 0.015 J; U = ½QΔV = ½(600 × 10⁻⁶)(50) = 0.015 J; U = Q²/2C = (600 × 10⁻⁶)²/(2 × 12 × 10⁻⁶) = 0.015 J ✓. *Skill:* energy forms. *Difficulty:* MEDIUM.

---

## 13. TRANSFER QUESTIONS

### LEVEL 3 — TRANSFER

**Q13.** You have two identical capacitors C. Compare C_eq in series (C/2) versus parallel (2C), and state the ratio. Explain each result with the gap-stacking / plate-gluing picture of C = ε₀A/d.
> *Instructor key — Answer:* Series: 1/C_eq = 2/C → C_eq = C/2 (stacked gaps: effective separation 2d at area A → C = ε₀A/2d). Parallel: C_eq = 2C (glued plates: area 2A at gap d). Ratio parallel:series = 4 — same parts, wiring alone changes the answer fourfold. *Skill:* combination intuition + formula. *Difficulty:* MEDIUM.

**Q14.** An air capacitor of 100 pF is charged to 12 V and disconnected. A dielectric with k = 4 fills the gap. Determine the new C, ΔV, and Q — then, using the appropriate energy form, determine what happens to the stored energy U.
> *Instructor key — Answer:* C′ = kC₀ = 400 pF; ΔV′ = ΔV₀/k = 3 V; Q = C₀ΔV₀ = 1.2 nC (locked). Energy: use Q²/2C (Q is the fixed quantity): U₀ = Q²/2C₀ = 7.2 × 10⁻⁹ J; U′ = Q²/2C′ = 1.8 × 10⁻⁹ J → **U drops by the factor k** (U′ = U₀/k). *(The U conclusion is derived directly from the source's formulas — the source does not state it explicitly.)* *Skill:* dielectric chain + energy-form selection under constraints. *Difficulty:* HARD.

**Q15.** You need a 106 pF capacitance. You already have the source's Example 3 capacitor (53 pF, d = 1 mm, air). Two options: (a) halve the gap; (b) keep the gap and fill with a dielectric. What does each option require?
> *Instructor key — Answer:* (a) C = ε₀A/(d/2) = 2 × 53 = 106 pF — a purely geometric doubling. (b) Need k = C/C₀ = 106/53 = 2 — a material with dielectric constant 2 (k ≥ 1 always achievable in principle). Two independent routes to the same target — engineering choice between mechanics (moving plates) and materials. *Skill:* design transfer of both knobs. *Difficulty:* MEDIUM.

**Q16.** Two identical capacitors are wired in series across a 10 V source. Using only the source's relations (ΔV = ΔV₁ + ΔV₂ and Q the same on each), prove that each capacitor sees exactly 5 V — and explain why this "voltage splitting" property makes series chains useful for high-voltage applications.
> *Instructor key — Answer:* Q same and C₁ = C₂ ⇒ ΔV₁ = Q/C = ΔV₂; with ΔV₁ + ΔV₂ = 10 V ⇒ each = 5 V. Each device endures only half the total voltage — a chain of n identical capacitors divides the total n ways, letting assemblies withstand voltages no single capacitor could. *(The "high-voltage usefulness" framing is a pedagogical extension of the source's relations.)* *Skill:* derivation + application reasoning. *Difficulty:* MEDIUM–HARD.

**Q17.** Two capacitors, 6 μF and 3 μF, in series across 12 V. A student claims: "C_eq = 4.5 μF — the average — and each capacitor holds 6 V." Identify every error and give the correct full solution.
> *Instructor key — Answer:* Errors: (1) C_eq is not an average — it's the reciprocal sum: 1/C_eq = 1/6 + 1/3 = 1/2 → C_eq = 2 μF; (2) equal voltages hold only for *identical* capacitors. Correct: Q = C_eqΔV = 24 μC on each; ΔV(6μF) = 4 V, ΔV(3μF) = 8 V — the smaller capacitor takes double the voltage. *Skill:* diagnosing the two canonical series errors. *Difficulty:* MEDIUM.

**Q18.** A parallel-plate capacitor with a dielectric (k = 6.7, the source's Example 4 material) stores 3.62 × 10⁻⁸ C per plate at 12 V. Using energy density reasoning, where does the stored energy physically reside, and what formula would you use to compute it per unit volume?
> *Instructor key — Answer:* In the field within the dielectric (the gap region), at density u = ½εE² with ε = kε₀ — energy per unit volume of the gap, independent of plate geometry. (Numerically: E = ΔV/d = 12/0.55 × 10⁻³ ≈ 2.18 × 10⁴ V/m; u = ½(6.7)(8.85 × 10⁻¹²)(2.18 × 10⁴)² ≈ 1.4 × 10⁻² J/m³.) *Skill:* energy-density concept transferred to a real device. *Difficulty:* MEDIUM.

---

## 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | Capacitor structure, C = Q/ΔV + farad, the Gauss-law derivation, C ∝ A & C ∝ 1/d, all three energy forms, energy density, the full dielectric chain (E′, E = E₀/k, ΔV₀/k, Q = Q₀, kC₀, ε = kε₀, εᵣ, k = 1 for air), parallel and series rules incl. n-identical cases, and all four source examples. |
| Mathematical formulas correct | ✅ | All formulas preserved exactly; every numeric result re-derived and matched (2C₁, 2C₁, 4C₁; 1 μF; 100 V; 53 pF; 636 × 10⁻¹² C; 12,000 V/m; k = 6.7). |
| Technical terminology preserved | ✅ | Capacitor/condenser, capacitance, farad, dielectric, dielectric constant, relative permittivity, permittivity of material, energy density, equivalent capacitance. |
| Explanations in original language | ✅ | Fully rewritten; exchange-rate, tank-width, assembly-line, spring-mattress, padlocked-island analogies all marked pedagogical. |
| Understandable to a first-year student | ✅ | Recipes and chains made explicit; every worked example step-by-step with sanity checks. |
| Difficult concepts explicitly identified | ✅ | 5 concepts with ratings; 2 rated HARD (series logic, dielectric mechanism) with full video plans and scripts. |
| Common misconceptions identified | ✅ | 10 mistakes with what/why/how, echoed in the difficult-concept entries and both video scripts. |
| Examples actually teach the concept | ✅ | All source examples worked in full; pedagogical additions (energy consistency check, series/parallel comparison) clearly labeled and built from source formulas. |
| Practice progresses understand → apply → transfer | ✅ | Level 1 (6), Level 2 (6), Level 3 (6) incl. design trade-offs, constrained energy reasoning, error diagnosis; 10-question self-check without revealed answers. |
| No unsupported claims added | ✅ | Battery-connected insertion dynamics and material k tables marked [SOURCE DOES NOT SPECIFY]; derived conclusions (U′ = U₀/k, voltage-division framing) explicitly flagged as derived/ pedagogical. |
| No large verbatim reproduction | ✅ | Structure, formulas, and numbers preserved; wording fully rewritten. |
| Suitable for direct web integration | ✅ | Clean Markdown; metadata; learning-flow position; instructor keys separated from student-facing content. |

**ARETE placement note:** Deploy as the capstone LEARN+PRACTICE lesson of the electrostatics arc (Lectures 1–5), gated on Lecture 4. Attach Video 1 to the combinations topic and Video 2 to the dielectric topic. Enable REMEDIATE on mistakes 5, 6, and 8 (charge-splitting in series, un-flipped reciprocal, dielectric-adds-charge) — the three highest-frequency failure modes. Q14, Q16, and Q17 are strong PROVE-stage items; this lesson's mastery unlocks the DC-circuits module that follows.


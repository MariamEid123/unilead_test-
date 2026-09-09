تمام — هنبدأ **محاضرة محاضرة** بالتفصيل الكامل. دي **المحاضرة 7** بالهيكل الكامل (14 قسم). قولي "كمّل" بعد كده وهعمل **المحاضرة 8** بنفس الشكل، وهكذا لحد 12.

---

# ARETE — LECTURE 7 (FULL TRANSFORMATION)

---

# 1. SOURCE ANALYSIS

| Item | Value |
|---|---|
| Course | PHY 211 — Physics (Electricity, Magnetism & Optics) |
| Lecture | **Lecture 7** — Chapter 6 |
| Title | Direct Current "DC" Circuits |
| Instructor | Dr. Ashraf Mousa Abdelwahed — AIU, Fall 2024 |

**Main topics:**
1. Resistors in series
2. Resistors in parallel
3. Series–parallel combination networks
4. EMF & terminal voltage (internal resistance)
5. EMFs in series & in parallel
6. RC circuits — charging
7. RC circuits — discharging

**Subtopics:** same-current/same-voltage reasoning; Req rules; n identical resistors; voltage & current divider ratios; two-resistor parallel shortcut; open-circuit emf; V = ℰ − Ir; battery stacking (aiding & opposing); battery lifetime and current sharing; matched internal resistance requirement; q(t), VC(t), I(t) for charge/discharge; τ = RC; 63% / 37% factors; q₀ = ℰC; I₀ = ℰ/R; stored energy U = qV_C/2.

**Learning objectives (from content):** reduce networks; compute branch quantities; distinguish emf/terminal voltage; explain battery combination rules; analyze RC transients numerically.

**Important definitions:** equivalent resistance; emf (open-circuit terminal PD); terminal voltage; internal resistance; time constant.

**Examples in source:** 6 (network reduction; series battery; parallel battery; car-battery terminal voltage; RC charge + energy; RC constants).

**Procedures:** stepwise network reduction; RC transient evaluation (compute τ → t/τ → exponent → plug into equation).

**Common misconceptions in source material:** parallel Req "bigger"; battery always supplies emf; linear charging; any two batteries can be paralleled.

**Difficult concepts:** parallel resistance smaller than smallest; terminal voltage sag; reverse-current danger in mismatched parallel batteries; exponential RC behavior; 63/37 assignment.

**Prerequisites (from earlier course chapters — not in these PDFs):** Ohm's law (V = IR); electric current; emf; capacitance (q = CV); capacitor energy; exponentials & natural log; SI prefixes (μ, m, k).

**Concept map:**

```
DC Circuits (Ch. 6)
├── Resistive networks
│   ├── Series → same I, V divides, Req = ΣR (> any R)
│   ├── Parallel → same V, I divides, 1/Req = Σ(1/R) (< smallest R)
│   └── Mixed → collapse stepwise, redraw each time
├── Real sources
│   ├── emf vs terminal voltage → V = ℰ − Ir ; I = ℰ/(R + r)
│   └── EMF combinations
│       ├── Series → voltages add (with sign), internal r adds
│       └── Parallel → same V, shared I, lasts longer, r drops
│           └── requires matched internal resistances (reverse-current risk)
└── RC transients (τ = RC, q₀ = ℰC, I₀ = ℰ/R)
    ├── Charging → q, VC rise to 63% at τ ; I decays to 37% at τ
    ├── Discharging → q, VC, I all fall to 37% at τ
    └── Energy at time t → U = q·VC / 2
```

---

# 2. COURSE / MODULE / LESSON METADATA

| Field | Value |
|---|---|
| **COURSE** | PHY 211 — Physics II |
| **MODULE** | DC & Transient Circuits (Chapter 6) |
| **LESSON** | Lecture 7 — Direct Current (DC) Circuits |
| **TOPICS** | Series/parallel networks; emf & internal resistance; battery combinations; RC charging & discharging |
| **PREREQUISITES** | Ohm's law; current; emf; capacitance q = CV; capacitor energy; exponentials/logs |
| **COMPETENCIES** | Reduce any series–parallel network; use divider ratios; compute terminal voltage; choose battery arrangement; evaluate q(t), VC(t), I(t), τ, and stored energy in RC circuits |
| **DIFFICULTY** | Overall: MEDIUM · Network reduction & battery combinations: MEDIUM · RC transients: HARD |
| **ESTIMATED STUDY TIME** | ~4 hours (lesson 90 min · worked examples 30 min · practice 60 min · videos 18 min · self-check & transfer 45 min) |

**ARETE flow placement:**
- **LEARN:** series/parallel rules, emf & terminal voltage.
- **PRACTICE:** divider problems, network reduction.
- **PROVE:** RC transient computation with correct 63/37 assignment.
- **REMEDIATE/RETRY targets:** "add reciprocals then forget to invert"; terminal voltage sign; linear-charging intuition.
- **TRANSFER:** design tasks (choose battery arrangement; choose R for a target τ).
- **MASTER:** mixed networks with internal resistance + RC timing in one problem.

---

# 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Explain why the same current flows through series resistors and why the same voltage appears across parallel resistors.
2. Compute Req for series, parallel, and mixed networks, and use it to find the battery current.
3. Apply the divider relations (V₁/V₂ = R₁/R₂; I₁/I₂ = R₂/R₁) and the special cases for n identical resistors.
4. Distinguish emf from terminal voltage and compute V = ℰ − Ir and I = ℰ/(R + r) for a real battery.
5. State what series and parallel battery arrangements are each used for, and explain the matched-internal-resistance requirement for parallel EMFs.
6. Write the charging and discharging equations for q(t), V_C(t), and I(t) in an RC circuit.
7. Compute τ, q₀ = ℰC, I₀ = ℰ/R, and evaluate any quantity at a given time t.
8. Interpret the 63% and 37% factors correctly and compute the energy stored in a partially charged capacitor.

---

# 4. WEB-READY LESSON

# Lecture 7 — Direct Current (DC) Circuits

## Prerequisites
The student should already understand:
- Ohm's law (V = IR) and the meaning of electric current.
- The concepts of emf and capacitance, and the relations q = CV and (capacitor energy) U = qV/2.
- Exponential functions e⁻ˣ and the natural logarithm.
- SI prefixes: μ = 10⁻⁶, m = 10⁻³, k = 10³.

---

### 1. Resistors in Series

**Core Idea**
Components connected end-to-end form one path. The same current passes through every element, and the source voltage divides among them in proportion to resistance.

**Explanation**
Charge can neither accumulate nor vanish anywhere in a single loop, so the identical current I flows through R₁, R₂, and R₃. Each resistor drops V₁ = IR₁, V₂ = IR₂, V₃ = IR₃, and the source supplies the whole sum:

ℰ = V₁ + V₂ + V₃ = I(R₁ + R₂ + R₃)

Define the **equivalent resistance** as the single resistor that draws the same current I from the same emf — comparing ℰ = I·Req with the line above gives:

**Req = R₁ + R₂ + R₃ → Req is larger than every resistor in the chain.**

Two divider ratios follow immediately: voltages split in proportion to resistance (V₁/V₂ = R₁/R₂), and the fraction of the emf across R₁ is V₁/ℰ = R₁/Req. For **n identical resistors R**: Req = nR.

**Example**
42 Ω + 17 Ω + 110 Ω in series on a 9 V battery → Req = 169 Ω, I = 53 mA, and the voltages 2.23 V, 0.90 V, 5.83 V add back to 9 V. (Full solution: Worked Example 2.)

**Key Point**
Series = one current, divided voltage, and Req bigger than any single resistor.

### 2. Resistors in Parallel

**Core Idea**
Resistors connected across the same two nodes all experience the same voltage, while the total current splits among the branches.

**Explanation**
Each branch sees the full emf, so I₁ = ℰ/R₁, I₂ = ℰ/R₂, I₃ = ℰ/R₃. The total current leaving the source is the sum:

I = I₁ + I₂ + I₃ = ℰ(1/R₁ + 1/R₂ + 1/R₃)

Matching this against I = ℰ/Req:

**1/Req = 1/R₁ + 1/R₂ + 1/R₃ → Req is smaller than every branch resistor.**

The result makes physical sense: each extra branch is an extra path for current, so the combination conducts *better* than any single branch. Two working shortcuts: for exactly two resistors, Req = R₁R₂/(R₁ + R₂); for **n identical resistors R**, Req = R/n.

Currents divide *inversely* to resistance: I₁/I₂ = R₂/R₁, and the fraction of the total current in branch 1 is I₁/I = Req/R₁.

**Example**
65 Ω, 25 Ω, 170 Ω in parallel carrying 1.3 A total: 1/Req = 0.0612 Ω⁻¹ → Req = 16.34 Ω — below 25 Ω, the smallest branch. (Worked Example 3.)

**Key Point**
Parallel = one voltage, divided current, and Req smaller than the smallest branch. Add the **reciprocals**, then invert the total.

### 3. Reducing Combination Networks

**Core Idea**
Any series–parallel network collapses step by step: merge series runs, merge parallel groups, redraw, repeat.

**Explanation / Procedure**
1. Find resistors in one unbroken path (same current) → add them.
2. Find resistors across the same two nodes (same voltage) → combine reciprocally.
3. Redraw the simplified circuit and repeat until a single Req sits between the terminals.

**Example**
35 Ω and 82 Ω in series → 117 Ω; that pair in parallel with 45 Ω → (117 × 45)/162 = 32.5 Ω. (Worked Example 1.)

**Key Point**
Never attack the whole network at once — collapse one identifiable group at a time, redrawing after each step.

### 4. EMF and Terminal Voltage

**Core Idea**
A real battery contains internal resistance r. With no current flowing (open circuit) the terminal voltage equals the emf; under load, the terminals deliver less.

**Explanation**
The emf ℰ is the open-circuit potential difference between the source's terminals. When current I flows, the internal resistance drops Ir *inside* the battery, so the measurable terminal voltage is:

**V = ℰ − I r**

Connect a load R across the terminals: the loop gives ℰ − Ir = IR, hence:

**ℰ = I(R + r)  →  I = ℰ / (R + r)**

The load only ever sees V = IR — never the full emf. The heavier the current, the larger the internal drop and the more the battery "sags."

**Example**
A 12.0 V car battery with r = 0.010 Ω: at 10 A the terminals read 11.9 V; at 100 A only 11 V. (Worked Example 4.)

**Key Point**
Emf = the ideal no-load value; terminal voltage = what the circuit actually gets: V = ℰ − Ir, always below ℰ when current flows.

### 5. EMFs in Series

**Core Idea**
Stacking batteries in series adds their voltages (with orientation signs) and adds their internal resistances — the arrangement used to *increase voltage*.

**Explanation**
Potential differences add along the chain. Two 3 V cells aligned give V_ac = (V_a − V_b) + (V_b − V_c) = 6 V, so V_a > V_c and current flows a → c through the external resistance. If they oppose (12 V against 6 V, as in the source's second figure): V_ac = −12 + 6 = −6 V, so V_a < V_c and the current flows c → a, its direction set by the larger source. For batteries in series, the **total internal resistance increases**.

**Example**
A 12 V and a 6 V battery in series, opposing: the net 6 V drives the current — from the 12 V battery's side out through the circuit.

**Key Point**
Series: voltages add (mind the signs), internal resistances add — purpose: higher voltage.

### 6. EMFs in Parallel

**Core Idea**
Parallel batteries keep the single-cell voltage but share the current: the combination lasts longer, wastes less internally, and has *lower* total internal resistance — used to *increase the current obtained from the source*.

**Explanation**
The voltage is the same as one battery. The arrangement lasts about **twice as long** as a single cell because each source produces only a fraction of the total current, and the loss due to internal resistance is smaller than for a single cell (more energy delivered). For batteries in parallel, the **total internal resistance decreases**.

**Critical constraint from the source:** the internal resistances of the batteries must be the **same** — otherwise the battery with *less* internal resistance could be damaged due to **reverse current**.

**Example**
Two matched 3 V cells in parallel supply a load: the load still sees 3 V, but each cell carries only part of the current, and the pair's combined internal resistance is lower than either cell's alone.

**Key Point**
Parallel: same voltage, shared current, longer life, lower internal r — but only with **matched internal resistances**.

### 7. RC Circuits — Charging a Capacitor

**Core Idea**
Battery ℰ, resistor R, capacitor C in series. Close the switch: charge builds exponentially toward q₀ = ℰC, the capacitor voltage rises toward ℰ, and the current decays from I₀ = ℰ/R to zero. The timescale is τ = RC.

**Explanation**
At t = 0 the capacitor is empty (V_C = 0), so nothing yet opposes the battery and the current is at its maximum, I₀ = ℰ/R. As charge accumulates, V_C grows and pushes back against ℰ; the effective driving voltage shrinks, so the current shrinks, so charging slows — self-limiting exponential behavior:

- **q(t) = q₀(1 − e^(−t/τ)) = ℰC(1 − e^(−t/RC))**, with maximum charge **q₀ = ℰC**
- **V_C(t) = q/C = ℰ(1 − e^(−t/τ))**
- **I(t) = I₀ e^(−t/τ) = (ℰ/R) e^(−t/τ)**, with I₀ = ℰ/R

**Time constant τ = RC.** At t = τ: q = q₀(1 − e⁻¹) = q₀(1 − 0.37) = **0.63 q₀**, V_C = **0.63 ℰ**, while the current has fallen to **0.37 I₀**. Where the numbers come from: e⁻¹ ≈ 0.37; rising quantities reach 1 − 0.37 = 0.63 of maximum, decaying ones fall to 0.37.

**Example**
ℰ = 12 V, R = 175 Ω, C = 55.7 μF → τ = 9.75 ms, q₀ = 6.68 × 10⁻⁴ C, I₀ = 0.068 A. (Worked Example 6; charge & energy at a specific time: Worked Example 5.)

**Key Point**
Everything is exponential, never linear. One τ means 63% of the way up for q and V_C, down to 37% for I.

### 8. RC Circuits — Discharging a Capacitor

**Core Idea**
Remove the battery and close the switch: the fully charged capacitor (q₀ = ℰC) dumps its charge through R. Charge, voltage, and current all decay exponentially with the same τ = RC.

**Explanation**
- **q(t) = q₀ e^(−t/τ) = ℰC e^(−t/RC)** — starts at q₀, ends at zero
- **V_C(t) = ℰ e^(−t/τ)** — starts at ℰ, ends at zero
- **I(t) = (ℰ/R) e^(−t/τ)** — starts at I₀ = ℰ/R, decays to zero

At t = τ, each of these has fallen to **0.37** of its starting value. The discharge curves are the mirror images of the charging curves, run by the same clock.

**Example**
A capacitor holding q₀ = ℰC discharges through R: after one τ, 37% of the charge remains; after three τ (≈ 1 − e⁻³), only ~5% — effectively empty.

**Key Point**
Same τ = RC governs both directions. On discharge, "37% remains at one τ" replaces "63% reached at one τ."

### 9. Energy Stored at Time t

**Core Idea**
The energy in the capacitor at any moment is **U = q·V_C / 2**, where both q and V_C are the time-dependent values.

**Explanation**
Substitute the charging expressions: at time t, q = ℰC(1 − e^(−t/τ)) and V_C = ℰ(1 − e^(−t/τ)); half their product gives the stored energy. Since both factors grow, the energy grows faster than either — the capacitor fills with energy as it fills with charge.

**Example**
At t = 4.2 ms in the ℰ = 6 V, R = 150 Ω, C = 23 μF circuit: q = 97 μC and V_C = 4.22 V → U = (97 × 10⁻⁶ × 4.22)/2 = 2.05 × 10⁻⁴ J. (Worked Example 5.)

**Key Point**
U = qV_C/2 with the *instantaneous* q and V_C — at full charge this becomes U = q₀ℰ/2.

---

## Key Takeaways
1. Series: same current; Req = ΣR > any R; n identical → nR.
2. Parallel: same voltage; 1/Req = Σ(1/R) < smallest R; two resistors → product/sum; n identical → R/n.
3. Dividers: voltage shares ∝ R in series; current shares ∝ 1/R in parallel.
4. Terminal voltage V = ℰ − Ir is always below the emf under load; heavy loads sag the battery.
5. Series batteries: voltages add (signs matter), internal r adds. Parallel batteries: same voltage, shared current, longer life, lower r — but internal resistances must match, or the lower-r battery risks reverse-current damage.
6. Charging: q = ℰC(1 − e^(−t/τ)), V_C = ℰ(1 − e^(−t/τ)), I = (ℰ/R)e^(−t/τ).
7. Discharging: q = ℰC·e^(−t/τ), V_C = ℰ·e^(−t/τ), I = (ℰ/R)e^(−t/τ).
8. One clock for everything: τ = RC; at t = τ, rising quantities hit 63%, falling ones hit 37%. Energy at any instant: U = qV_C/2.

## Self-Check (attempt before looking at answers)
1. Which single quantity is identical for all resistors in series? In parallel — which quantity is identical?
2. A 10 Ω and a 40 Ω resistor are in parallel. Compute Req. Is it above or below 10 Ω — and does that match your rule?
3. A battery of emf 9.0 V and internal resistance 0.05 Ω delivers 2.0 A. What is its terminal voltage?
4. Why does the terminal voltage in question 3 fall further if the current doubles?
5. What does a series battery arrangement give you that a parallel arrangement does not — and vice versa?
6. What condition must parallel batteries satisfy, and what can happen to which battery if it is violated?
7. What are the SI units of the product RC? Show the combination.
8. During charging at t = τ: what fraction of q₀ has the capacitor reached? What fraction of V_C? What fraction of I₀ does the current still carry?
9. During discharging at t = τ: what fraction of the charge remains?
10. An RC circuit reaches 63% of full charge in 2.0 ms. What is τ? Roughly when is it 95% charged?

---

# 5. FORMULAS

| # | Formula | Variables | When it is used | Interpretation & assumptions |
|---|---|---|---|---|
| 1 | Req = R₁ + R₂ + … + Rₙ | Rᵢ: individual resistances (Ω) | Single current path | Req exceeds every Rᵢ; n identical → nR |
| 2 | 1/Req = 1/R₁ + 1/R₂ + … + 1/Rₙ | same | Same two nodes, same voltage | Req below every Rᵢ; n identical → R/n |
| 3 | Req = R₁R₂/(R₁ + R₂) | two resistors only | Quick two-branch parallel | Special case of #2 |
| 4 | V₁/V₂ = R₁/R₂ | Vᵢ: voltage across Rᵢ | Series voltage division | From V = IR with common I |
| 5 | V₁/ℰ = R₁/Req | ℰ: source emf | Fraction of emf on R₁ | Series only |
| 6 | I₁/I₂ = R₂/R₁ | Iᵢ: branch currents | Parallel current division | More current takes the smaller-R path |
| 7 | I₁/I = Req/R₁ | I: total current | Fraction of total in branch 1 | Parallel only |
| 8 | V = ℰ − Ir | ℰ: emf; r: internal resistance; I: current | Battery under load | Open circuit (I = 0) → V = ℰ |
| 9 | I = ℰ/(R + r) | R: external load | Real battery + load | From ℰ = IR + Ir |
| 10 | q(t) = ℰC(1 − e^(−t/τ)) | q₀ = ℰC: max charge; t: time | RC **charging**, capacitor initially empty | t = τ → 0.63 q₀; t → ∞ → q₀ |
| 11 | V_C(t) = ℰ(1 − e^(−t/τ)) | V_C = q/C | RC charging | t = τ → 0.63 ℰ; starts at 0 |
| 12 | I(t) = (ℰ/R) e^(−t/τ) | I₀ = ℰ/R | RC charging **and** discharging | t = τ → 0.37 I₀; starts at I₀ |
| 13 | q(t) = ℰC · e^(−t/τ) | q₀ = ℰC | RC **discharging**, initially full | t = τ → 0.37 q₀ |
| 14 | V_C(t) = ℰ · e^(−t/τ) | — | RC discharging | t = τ → 0.37 ℰ |
| 15 | τ = RC | R in Ω, C in F → τ in s | All RC timing | The circuit's characteristic clock; Ω·F = s |
| 16 | U = q·V_C / 2 | q, V_C: instantaneous values | Capacitor energy at time t | At full charge → U = q₀ℰ/2 |

---

# 6. WORKED EXAMPLES

**WE 1 — Series–parallel reduction (Source Example 1)**
Find the equivalent resistance between A and B for R₁ = 35 Ω in series with R₂ = 82 Ω, the pair then in parallel with R₃ = 45 Ω.
1. Series pair: R₁₂ = 35 + 82 = **117 Ω**.
2. Parallel with R₃: 1/Req = 1/117 + 1/45 → Req = (117 × 45)/(117 + 45) = 5265/162.
3. **Req = 32.5 Ω** — smaller than 45 Ω (parallel rule) even though the series part grew.

**WE 2 — Series circuit (Source Example 2)**
A 9.0 V battery drives 42 Ω, 17 Ω, 110 Ω in series. Find (a) the battery current, (b) the voltage across each resistor.
1. Req = 42 + 17 + 110 = **169 Ω**.
2. I = ℰ/Req = 9/169 = 0.053 A = **53 mA**.
3. V₁ = IR₁ = 0.053 × 42 = **2.226 V**; V₂ = 0.053 × 17 = **0.901 V**; V₃ = 0.053 × 110 = **5.83 V**.
4. Check: 2.226 + 0.901 + 5.83 ≈ 9.0 V ✓ (small rounding gap from using 0.053).

**WE 3 — Parallel circuit (Source Example 3)**
Three resistors 65 Ω, 25 Ω, 170 Ω in parallel; the total current through them is 1.3 A. Find (a) the emf, (b) each branch current.
1. 1/Req = 1/65 + 1/25 + 1/170 = 0.01538 + 0.04 + 0.00588 = 0.0612 Ω⁻¹.
2. Req = 1/0.0612 = **16.34 Ω** (below 25 Ω — the smallest branch ✓).
3. ℰ = I·Req = 1.3 × 16.34 = **21.2 V**.
4. I₁ = 21.2/65 = **0.33 A**; I₂ = 21.2/25 = **0.85 A**; I₃ = 21.2/170 = **0.12 A**.
5. Check: 0.33 + 0.85 + 0.12 = 1.30 A ✓. Note the smallest resistor (25 Ω) carries the largest branch current.

**WE 4 — Terminal voltage (Source Example 4)**
Car battery: ℰ = 12.0 V, r = 0.010 Ω. Find the terminal voltage when the current drawn is (a) 10.0 A, (b) 100.0 A.
- (a) V = ℰ − Ir = 12 − (10)(0.01) = **11.9 V**
- (b) V = 12 − (100)(0.01) = **11 V**
Ten times the current → ten times the internal drop. Real batteries sag under heavy load.

**WE 5 — RC charging: charge and energy (Source Example 5)**
ℰ = 6 V, R = 150 Ω, C = 23 μF; the switch closes at t = 0. Find the charge at t = 4.2 ms and the capacitor's stored energy at that instant.
1. τ = RC = 150 × 23 × 10⁻⁶ = **3.45 × 10⁻³ s** (3.45 ms).
2. t/τ = 4.2/3.45 = **1.22**.
3. q₀ = ℰC = 6 × 23 × 10⁻⁶ = 1.38 × 10⁻⁴ C (138 μC).
4. q = q₀(1 − e^(−1.22)) = 138 μC × (1 − 0.296) ≈ **97 × 10⁻⁶ C**.
5. V_C at that instant = ℰ(1 − e^(−t/τ)) = 6 × 0.704 = **4.22 V**.
6. U = q·V_C/2 = (97 × 10⁻⁶ × 4.22)/2 ≈ **2.05 × 10⁻⁴ J**.
7. Cross-check with U = q²/2C: (97 × 10⁻⁶)² / (2 × 23 × 10⁻⁶) = 2.05 × 10⁻⁴ J ✓.

**WE 6 — RC constants (Source Example 6)**
ℰ = 12 V, R = 175 Ω, C = 55.7 μF. Find (a) the time constant, (b) the maximum charge, (c) the initial current.
1. τ = RC = 175 × 55.7 × 10⁻⁶ = **9.75 × 10⁻³ s = 9.75 ms**.
2. q₀ = ℰC = 12 × 55.7 × 10⁻⁶ = **6.68 × 10⁻⁴ C**.
3. I₀ = ℰ/R = 12/175 = **0.068 A**.
Meaning: after 9.75 ms (one τ), the capacitor holds 63% of 668 μC (~420 μC) and the current has fallen to 37% of 68 mA.

---

# 7. COMMON MISTAKES

| # | What students usually do | Why it's wrong | How to avoid it |
|---|---|---|---|
| 1 | Add parallel resistances directly (Req = R₁ + R₂) | Parallel branches share voltage, not current — the reciprocal rule applies | In parallel, sum the **1/R** values, **then invert**; sanity-check that Req < smallest branch |
| 2 | Compute 1/Req and report it as the answer | The sum of reciprocals is not Req itself | Always finish with "flip the total" — and check units (Ω, not Ω⁻¹) |
| 3 | Assume parallel Req lies between the branch values | Extra branches = extra paths = better conduction | Apply the "smaller than smallest" test after every parallel merge |
| 4 | Use V = ℰ (not ℰ − Ir) for a loaded battery | The internal drop Ir is invisible in the diagram but real | Ask "is current flowing?" If yes → V = ℰ − Ir |
| 5 | Think parallel batteries add their voltages | Parallel EMFs keep the voltage of a single cell; only current capability and lifetime improve | Series adds voltage; parallel adds endurance — keep the two purposes separate |
| 6 | Parallel any two batteries regardless of internal resistance | Mismatched internal resistances drive a reverse current that can damage the lower-r battery (per the source) | Check "matched internal resistances?" before paralleling |
| 7 | Treat RC charging as linear ("half the time → half the charge") | The rate slows as the capacitor fills — the behavior is exponential | Always use e^(−t/τ); "one τ = 63% up / 37% down" |
| 8 | Attach 63% to the current during charging | Rising quantities (q, V_C) reach 63%; the decaying current falls to 37% | Ask "is this quantity rising or falling?" before assigning the factor |
| 9 | Plug C in μF directly into τ = RC | τ = RC requires SI units — 1 Ω × 1 μF = 10⁻⁶ s, not 1 s | Convert to farads first (μF → × 10⁻⁶), then multiply |
| 10 | Use the charge equation q = ℰC(1 − e^(−t/τ)) during discharge | That form *rises*; discharge decays from q₀ with a pure exponential | Check the direction: filling → (1 − e^…); emptying → (e^…) |

---

# 8. LECTURE SUMMARY

# Lecture Summary — DC Circuits

## What You Need to Know
- How to collapse series, parallel, and mixed networks to one Req and extract every current and voltage.
- The difference between emf and terminal voltage, and how internal resistance sags a real battery under load.
- What series vs. parallel battery arrangements are for, and the matched-internal-resistance rule.
- The complete exponential behavior of charging and discharging RC circuits, all timed by τ = RC.

## Key Definitions
- **Equivalent resistance (Req)** → the single resistor that draws the same current from the same source.
- **Emf (ℰ)** → the terminal potential difference when no current flows (open circuit).
- **Terminal voltage (V)** → the potential difference across the battery's terminals under load; V = ℰ − Ir.
- **Internal resistance (r)** → the hidden resistance inside a real battery.
- **Time constant (τ = RC)** → the time for a charging quantity to reach 0.63 of its maximum (or a decaying quantity to fall to 0.37).
- **Maximum charge (q₀ = ℰC)** → the final charge on a fully charged capacitor.
- **Initial current (I₀ = ℰ/R)** → the largest current in an RC circuit, at the instant the switch closes.

## Key Formulas
- Req = ΣRᵢ (series); 1/Req = Σ(1/Rᵢ) (parallel) → network reduction.
- V₁/V₂ = R₁/R₂; I₁/I₂ = R₂/R₁ → divider relations.
- V = ℰ − Ir; I = ℰ/(R + r) → real-battery behavior.
- q = ℰC(1 − e^(−t/τ)); V_C = ℰ(1 − e^(−t/τ)); I = (ℰ/R)e^(−t/τ) → charging.
- q = ℰC e^(−t/τ); V_C = ℰ e^(−t/τ) → discharging.
- τ = RC; q₀ = ℰC; I₀ = ℰ/R; U = qV_C/2 → constants and energy.

## Important Ideas
- Series trades voltage for shared current; parallel trades current for shared voltage — Req moves *opposite* ways in the two cases.
- A real battery is an ideal emf in series with a small hidden resistor.
- The exponential is self-limiting feedback: the fuller the capacitor, the slower it charges.
- One clock (τ = RC) runs every RC process, charging or discharging.

## Common Mistakes
Parallel Req mis-added or "between" values; the missing final inversion; V = ℰ under load; parallel batteries treated as voltage-adders; unmatched batteries paralleled; linear charging; 63/37 swapped; μF unit slips; charging formula used for discharge.

## Exam Focus
1. Mixed-network reduction with sign-checked branch quantities.
2. Terminal voltage under a specified load (including reversed reasoning: given V, find I or r).
3. Reading the RC equations: what 63%, 37%, and τ physically mean, applied to the correct quantity.
4. Evaluating q, V_C, I, and U at a specific time t — including the exponent arithmetic.

## 60-Second Review
Series: one current, voltages add, Req grows (nR for n equal). Parallel: one voltage, currents add, Req shrinks below the smallest (R/n for n equal). Real battery: V = ℰ − Ir. Series batteries: voltages add, r adds. Parallel batteries: same V, shared current, lasts longer, r drops — matched r required or the low-r battery suffers reverse current. RC: τ = RC, q₀ = ℰC, I₀ = ℰ/R. Charging: q and V_C rise to 63% at one τ; I falls to 37%. Discharging: everything falls to 37% at one τ. Energy at time t: U = qV_C/2.

---

# 9. DIFFICULT CONCEPTS

### Difficult Concept: Parallel Resistance Is Smaller Than Any Branch
**Why students struggle:** Intuition says "more resistors = more resistance."
**Simple explanation:** Parallel branches are extra roads for the current — more roads, less total obstruction.
**Intuitive analogy:** A highway with more open lanes is easier to drive, even if each lane is narrow.
**Step-by-step:** (1) Every branch gets the full voltage ℰ. (2) Each draws Iᵢ = ℰ/Rᵢ. (3) The total current exceeds any single branch current. (4) Req = ℰ/I must be smaller than every Rᵢ.
**Mini example:** 6 Ω ∥ 6 Ω: 1/Req = 1/6 + 1/6 = 1/3 → Req = 3 Ω.
**Misconception to avoid:** "Req sits between the smallest and largest branch." It is *below the smallest*.
**Difficulty: MEDIUM**

### Difficult Concept: Terminal Voltage vs. Emf
**Why students struggle:** The internal resistance is invisible on the circuit diagram.
**Simple explanation:** The battery spends part of its own emf pushing current through its internal resistance.
**Intuitive analogy:** A pump with a partly clogged outlet: rated pressure only appears when nothing flows.
**Step-by-step:** (1) Open circuit → no internal drop → V = ℰ. (2) Current I flows → internal drop Ir. (3) V = ℰ − Ir at the terminals. (4) Bigger I → bigger sag.
**Mini example:** 12 V, r = 0.01 Ω, I = 100 A → V = 11 V.
**Misconception to avoid:** "A 12 V battery always delivers 12 V." Only when I ≈ 0.
**Difficulty: MEDIUM**

### Difficult Concept: Batteries in Parallel and the Reverse-Current Danger
**Why students struggle:** Parallel looks harmless — same voltage, more current — so the matching requirement feels arbitrary; and it's counterintuitive that the *stronger* (lower-r) battery is the one at risk.
**Simple explanation:** Parallel sources must share the load fairly; if their internal resistances differ, the sharing breaks down and a reverse current can be forced through the lower-r battery, damaging it.
**Intuitive analogy:** Two people carrying a couch: if one carries almost everything, the strong one gets hurt — the sharing, not the couch, is the problem.
**Step-by-step:** (1) Parallel EMFs → same terminal voltage as one cell. (2) Each source supplies part of the total current → lasts ~twice as long. (3) Internal losses drop, total internal resistance decreases. (4) If the internal resistances are unequal, current redistributes unevenly — the source says the battery with less internal resistance could be damaged by reverse current. (5) Rule: parallel only matched batteries.
**Mini example:** A fresh cell and an aged cell (different r) in parallel: uneven sharing → circulating/reverse current → the low-r cell suffers.
**Misconception to avoid:** "Any two batteries of the same voltage can be paralleled safely."
**Difficulty: HARD** → video provided

### Difficult Concept: RC Charging and the Time Constant
**Why students struggle:** Exponentials are new; the self-limiting feedback (current shrinks as the capacitor fills) is unfamiliar; 0.63 and 0.37 look arbitrary.
**Simple explanation:** The capacitor's own rising voltage opposes the battery, so charging continuously decelerates — producing e^(−t/RC).
**Intuitive analogy:** Filling a tank through a hose whose flow drops as the tank fills: fast at first, ever slower, never instantly full.
**Step-by-step:** (1) t = 0: V_C = 0, I = ℰ/R (maximum). (2) Charge builds → V_C rises. (3) The effective drive (ℰ − V_C) shrinks → I shrinks → charging slows. (4) q(t) = ℰC(1 − e^(−t/τ)). (5) At t = τ: q and V_C at 63%; I at 37%.
**Mini example:** R = 175 Ω, C = 55.7 μF → τ = 9.75 ms; at one τ, q ≈ 0.63 × 668 μC.
**Misconception to avoid:** "The capacitor fills at a constant rate" — and attaching 63% to a decaying quantity.
**Difficulty: HARD** → video provided

### Difficult Concept: Discharge Symmetry (37%)
**Why students struggle:** Students re-derive everything from scratch instead of seeing discharge as the mirror of charge.
**Simple explanation:** Same clock, opposite direction: whatever was rising now falls; the (1 − e^…) shape becomes a pure e^… decay.
**Intuitive analogy:** A bathtub draining through the same pipe that filled it — same pipe physics, reversed flow.
**Step-by-step:** (1) Start at q₀ = ℰC instead of 0. (2) Battery gone: only the capacitor drives current. (3) q = q₀ e^(−t/τ); V_C = ℰ e^(−t/τ); I = (ℰ/R) e^(−t/τ). (4) At one τ: 37% of each remains.
**Mini example:** After one τ of discharge, 37% of the charge remains; after 3τ, ~5%.
**Misconception to avoid:** Using the charging formula (1 − e^…) during discharge.
**Difficulty: MEDIUM**

---

# 10. VIDEO LESSON PLANS

---

**VIDEO 1**

**VIDEO TITLE:** "Why 63%? The RC Time Constant Demystified"
**TARGET CONCEPT:** Exponential charging/discharging of an RC circuit and the meaning of τ = RC
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Predict q, V_C, and I in an RC circuit at t = τ and explain why charging is exponential, not linear.
**HOOK:** A charging device races to about sixty-something percent, then crawls — why does nature refuse to fill anything at a constant rate?
**EXPLANATION:** (1) Circuit: ℰ, R, C, switch. (2) At t = 0 the empty capacitor acts like a plain wire → I starts at I₀ = ℰ/R. (3) As charge accumulates, V_C grows and opposes the battery → current shrinks → charging decelerates. (4) q(t) = ℰC(1 − e^(−t/τ)). (5) Evaluate at t = τ: e⁻¹ = 0.37 ⇒ 63% of q₀, current at 37%. (6) Discharge as the mirror (37% left). (7) Worked numbers from the lecture's Example 6.
**VISUALS:** Animated circuit with plates filling; live-drawn q(t) curve with a vertical "τ" marker at the 63% level; mirrored I(t) decay; unit clock showing Ω × F = s; discharge curves overlaid in a second color; the 3τ ≈ 95% mark.
**EXAMPLE:** ℰ = 12 V, R = 175 Ω, C = 55.7 μF: τ = 9.75 ms, q₀ = 668 μC, I₀ = 68 mA; at one τ: q ≈ 420 μC, I ≈ 25 mA (0.37 × 68 mA).
**COMMON MISTAKE:** Linear charging; attaching 63% to the current; forgetting μF → F conversion.
**CHECK FOR UNDERSTANDING:** "After three time constants, is the capacitor closer to 50%, 95%, or 100% full?"
**FINAL TAKEAWAY:** τ = RC is the circuit's internal clock — everything exponential: up to 63% or down to 37% at exactly one τ.

---

**VIDEO 2**

**VIDEO TITLE:** "Batteries in Parallel: The Hidden Reverse Current"
**TARGET CONCEPT:** Parallel EMF arrangements — current sharing, endurance, and the matched-internal-resistance rule
**TARGET STUDENT:** First-year university student
**DURATION:** ~8 minutes
**LEARNING OBJECTIVE:** Explain what parallel batteries do (and don't) provide, and justify the matched-internal-resistance requirement.
**HOOK:** Two batteries side by side: more voltage? No. More life? Yes — but only if they match. Mismatch them and one battery starts destroying itself.
**EXPLANATION:** (1) Series vs. parallel purposes. (2) Parallel: same voltage as one cell; each source supplies part of the current → lasts ~twice as long. (3) Total internal resistance decreases → less internal loss → more energy delivered. (4) The catch: internal resistances must match, else a reverse current can damage the *lower-r* battery. (5) Everyday illustration (clearly flagged as pedagogical): never mix fresh and old batteries in a device.
**VISUALS:** Two batteries drawn as ideal ℰ + internal r, connected in parallel to a load R; current arrows splitting at the node; a "lifetime bar" doubling; internal resistors merging (r/2) for matched cells; a mismatched pair with a highlighted circulating reverse-current loop through the low-r battery.
**EXAMPLE:** Two matched 3 V cells in parallel feeding a load: load sees 3 V; each cell carries half the current; combined internal resistance lower than one cell alone. Then the mismatched case: one aged cell (higher r) — the fresh, low-r cell ends up carrying a reverse current and is the one at risk.
**COMMON MISTAKE:** Thinking parallel batteries add voltage; paralleling batteries with different internal resistances.
**CHECK FOR UNDERSTANDING:** "You need 3 V from 1.5 V cells — series or parallel? You need longer runtime at 1.5 V — which?"
**FINAL TAKEAWAY:** Series stacks voltage; parallel shares current and extends life with lower internal resistance — but only between matched batteries.

---

# 11. VIDEO SCRIPTS

---

## SCRIPT 1 — "Why 63%? The RC Time Constant Demystified"

**[0:00–0:30] Hook**
Ever notice how a charging device races to about sixty percent… and then crawls the rest of the way? That's not the battery being lazy — it's one of nature's most stubborn patterns: the exponential. Today, with one battery, one resistor, and one capacitor, I'll show you exactly why an RC circuit hits sixty-three percent at one particular moment — and where that strange number actually comes from.

**[0:30–2:00] Concept introduction**
Here's the circuit: a battery of emf ℰ, a resistor R, a capacitor C, and a switch. The moment we close the switch, here's the key insight: the capacitor is completely empty, so at that instant it behaves like a plain piece of wire. Nothing is blocking the current yet. So the starting current is the biggest it will ever be: I₀ equals ℰ over R.

But as charge piles onto the plates, a voltage builds across the capacitor — and that voltage pushes *back* against the battery. The effective driving voltage is ℰ minus V_C. Every moment, V_C is a little bigger, so the current is a little smaller, so the charging is a little slower. That feedback — "the fuller it gets, the slower it fills" — is exactly what produces an exponential, not a straight line.

**[2:00–4:00] Visual explanation**
Watch the graph as I draw it. The charge curve shoots up early, then flattens as it approaches its ceiling, q₀ = ℰC. The formula: q of t equals q₀ times one minus e to the minus t over τ. Check the endpoints. At t = 0, the exponential is 1, so q is zero — correct. As t goes to infinity, the exponential vanishes, so q equals q₀ — full.

Now, τ — the *time constant* — equals R times C. It's the circuit's own internal clock, and the units even prove it: ohms times farads gives seconds. Here's the famous moment: set t equal to τ. The exponential becomes e to the minus one — about 0.37. So the charge is q₀ times one minus 0.37 — that's 0.63 q₀. Sixty-three percent isn't magic; it's just one minus zero-point-three-seven.

Meanwhile the current follows the mirror-image curve: I of t equals ℰ over R, times e to the minus t over τ. At t = τ, the current is down to 37 percent of its starting value. One clock, two behaviors: rising things reach 63%, falling things drop to 37%.

And discharge? Pure mirror. Remove the battery, close the switch, and the capacitor empties through the same resistor: q equals q₀ times e to the minus t over τ. At one τ, 37 percent of the charge is still there. Same clock, opposite direction.

**[4:00–6:00] Worked example**
Real numbers from the lecture. ℰ = 12 volts, R = 175 ohms, C = 55.7 microfarads. Time constant: 175 times 55.7 times ten to the minus six — about 9.75 milliseconds. Maximum charge: q₀ = ℰC — about 668 microcoulombs. Initial current: ℰ over R — about 68 milliamps.

So after roughly ten milliseconds — one time constant — the capacitor holds 63% of 668 microcoulombs, about 420. And the current has fallen to 37% of 68 milliamps — about 25. After three time constants, the charge is at one minus e to the minus three — about 95%. That's why engineers treat three-to-five time constants as "done."

**[6:00–7:00] Common mistake**
Now, the mistakes I see constantly. One: assuming the capacitor fills linearly — "half the time, half the charge." No. The rate itself decays. Two: swapping the numbers. Ask one question about any quantity: is it *rising* or *falling*? Rising — charge and voltage — 63 percent at one τ. Falling — current — 37 percent. On discharge, everything falls: 37 percent *remains*. Three: units. If C is in microfarads, multiply by ten to the minus six before computing τ — otherwise your time constant is a million times too big.

**[7:00–8:00] Quick student challenge**
Your turn. A circuit has a time constant of 2 seconds. How long until the capacitor reaches 86.5 percent of full charge? Think: 86.5 percent means one minus e to the minus t-over-τ equals 0.865 — so t over τ must be 2. Answer: four seconds — two time constants. Second question: I double the capacitance — faster or slower? Slower — τ doubles.

**[8:00–8:30] Final recap**
Remember this: τ = RC is the circuit's clock. Everything is exponential — never linear. Rising quantities hit 63% at one τ; falling ones hit 37%. Full charge is ℰC; initial current is ℰ over R; discharge is the mirror of charge. Master those five facts, and every RC problem is just bookkeeping.

---

## SCRIPT 2 — "Batteries in Parallel: The Hidden Reverse Current"

**[0:00–0:30] Hook**
Put two batteries side by side and connect plus to plus, minus to minus. What do you get? Most students say "double the voltage." Wrong — you get the *same* voltage. What you actually get is longer life and more deliverable current. But there's a catch, and it's a dangerous one: if the two batteries don't match inside, one of them starts destroying itself. Today, the hidden physics of parallel batteries.

**[0:30–2:00] Concept introduction**
First, straighten out the two arrangements. Series — batteries stacked end to end — is for *voltage*: potential differences add along the chain. Two 3-volt cells in series give 6 volts across the outside terminals. But series also stacks the internal resistances — the total r goes *up*.

Parallel is the other tool. Connect the batteries side by side and the terminal voltage stays that of a single cell. What changes is the *current*: the load's current is shared between the sources. Each battery produces only a fraction of the total — and because each works less hard, the pair lasts about twice as long as one cell alone. There's a second bonus: the internal resistances combine in parallel too, so the total internal resistance goes *down*. Less resistance inside means less energy wasted inside — more of the battery's energy actually reaches your circuit.

**[2:00–4:00] Visual explanation**
Let me draw it. Each real battery is an ideal emf ℰ plus a small internal resistor r. Two of them in parallel, feeding a load R. Watch the current arrows: the load pulls a total current I, and it splits — half from each battery at the node. Now look at the two internal resistors: they're in parallel, so together they behave like r over 2 for two matched cells. Lower internal resistance, smaller internal voltage drop, less lost energy.

Compare side by side: series gives you two ℰ and two r — more voltage, more internal loss. Parallel gives you one ℰ and half the r — same voltage, better delivery, double the endurance. Different tools for different jobs.

**[4:00–6:00] The catch, and an example**
Here's the catch from the lecture notes, and it's the part everyone forgets: the internal resistances of parallel batteries have to be the *same*. Why? If they're not equal, the current sharing breaks down — the load redistributes unevenly, and a *reverse current* can be driven through one of the batteries. And notice which one: the source says the battery with *less* internal resistance is the one that could be damaged. The stronger battery ends up suffering — it's carrying a current pattern it was never meant to handle.

Example. Two 3-volt cells in parallel feeding a small motor: matched internal resistances — each supplies half the motor's current, everything is fair, the motor sees 3 volts for twice as long. Now swap one cell for an aged one with a different internal resistance. The sharing collapses — one cell dominates, and a circulating reverse current flows through the low-resistance cell, damaging it. This is why you never mix fresh and old batteries in the same device — the fresh, low-r one is the one that gets hurt. *(That everyday rule is the standard illustration of the lecture's stated principle.)*

**[6:00–7:00] Common mistake**
Three classics. One: "parallel batteries double the voltage." No — voltage stays at the single-cell value; only current capability and lifetime improve. Two: paralleling batteries with different internal resistances and assuming it's fine — the mismatched pair is exactly the reverse-current scenario. Three: forgetting that *series* is the arrangement that raises internal resistance — if you need voltage, accept the extra internal r; if you need endurance, go parallel with matched cells.

**[7:00–8:00] Quick student challenge**
Two questions. You have 1.5-volt cells and you need 3 volts for your circuit — series or parallel? … Series: two cells stack to 3 volts. You have a 1.5-volt circuit that must run as long as possible — series or parallel? … Parallel: same voltage, shared current, double the life. And the bonus: you have two batteries with different internal resistances — can you parallel them? … No — the lower-resistance one risks reverse-current damage.

**[8:00–8:30] Final recap**
Series: voltages add, internal resistances add — a voltage tool. Parallel: voltage unchanged, current shared, life doubled, internal resistance halved — an endurance tool, but *only* for matched batteries. Same voltage, shared work, matched insides — that's parallel batteries in one breath.

---

# 12. PRACTICE QUESTIONS

## LEVEL 1 — UNDERSTAND

1. In a series circuit, which quantity is identical through every resistor — and why must it be?
2. In a parallel circuit, which quantity is identical across every branch — and why?
3. A 10 Ω resistor is placed in parallel with a 1000 Ω resistor. Is Req greater than 1000 Ω, between 10 and 1000 Ω, or less than 10 Ω? Explain without computing.
4. When a battery drives a large current, why does the voltage at its terminals fall below the emf?
5. A car battery reads 11 V at its terminals while a starter draws 100 A, but 11.9 V when only 10 A flows. Explain the difference in one sentence.
6. What is the physical meaning of τ = RC, and show that its units are seconds.
7. During charging at t = τ, what fraction of q₀ has the capacitor reached? What fraction of V_C? What fraction of I₀ remains?
8. During discharging at t = τ, what fraction of the charge remains — and why does this number differ from the charging case?
9. Why does a parallel battery arrangement last about twice as long as a single cell?
10. What condition must parallel batteries satisfy, and what happens to which battery when it is violated?

## LEVEL 2 — APPLY

11. A 12 V ideal battery drives three series resistors: 20 Ω, 30 Ω, 70 Ω. Find the current and the voltage across each resistor; verify with a sum check.
12. Two resistors, 6 Ω and 3 Ω, are in parallel across an ideal 12 V battery. Find Req, each branch current, and the total current.
13. Reduce the network: 50 Ω in series with 50 Ω, that combination in parallel with 25 Ω.
14. A battery has ℰ = 9.0 V and r = 0.10 Ω, connected to a 4.40 Ω load. Find the current and the terminal voltage.
15. A 4 Ω and a 12 Ω resistor are in parallel and carry a total current of 4.0 A. Find the voltage across them and each branch current. Verify with the divider ratio I₁/I₂ = R₂/R₁.
16. Find the equivalent resistance of (a) five 10 Ω resistors in series; (b) five 10 Ω resistors in parallel.
17. A series pair (6 Ω and 3 Ω) runs on a 12 V battery. Find the voltage across each resistor and verify the ratio V₁/V₂ = R₁/R₂.
18. A real battery has ℰ = 12 V and r = 0.020 Ω. At what current does the terminal voltage equal exactly 11.5 V?
19. An RC circuit has ℰ = 10 V, R = 2.0 kΩ, C = 50 μF. Find τ, q₀, and I₀; then find the charge at t = τ and at t = 0.2 s.
20. A capacitor discharges from q₀ = 100 μC with τ = 2.0 ms. Find the charge remaining at t = 4.0 ms.

## LEVEL 3 — TRANSFER

21. A real battery (ℰ = 12 V, r = 0.05 Ω) drives two resistors, 6 Ω and 3 Ω, connected in *parallel* across its terminals. Find the terminal voltage and the current through the 3 Ω resistor. (Hint: the parallel pair is the load R in I = ℰ/(R + r).)
22. The RC circuit of Worked Example 6 (R = 175 Ω, C = 55.7 μF) must reach 90% of full charge. Using 1 − e^(−t/τ) = 0.90, find the number of time constants required and the corresponding time.
23. A timing circuit needs τ = 0.5 s using a 100 μF capacitor. Choose R. Then state what fraction of full charge is reached at t = 1.0 s.
24. You have two 1.5 V cells, each with r = 0.5 Ω. Compute the terminal voltage and total internal resistance when they are connected (a) in series and (b) in parallel.
25. A 12 V battery drives R₁ = 40 Ω in series with an unknown R₂. The voltage across R₂ must be 4.0 V. Use the divider relation to find R₂, then verify with a full calculation.
26. A capacitor discharges through a resistor. At what time (in units of τ) has it fallen to exactly 10% of its starting charge?

**INSTRUCTOR ANSWER KEY (not for student display)**

1. Current — charge is conserved; it cannot accumulate anywhere in a single path. [EASY]
2. Voltage — both branches connect the same two nodes; a given pair of nodes has one potential difference. [EASY]
3. Less than 10 Ω — extra branches are extra paths; Req is smaller than the smallest branch. [EASY]
4. Part of the emf is dropped across the internal resistance: V = ℰ − Ir, and Ir grows with I. [EASY]
5. The internal drop Ir is ten times larger at 100 A (1 V) than at 10 A (0.1 V). [EASY]
6. τ is the characteristic response time — the time to reach 63% (charging) or fall to 37%; Ω × F = (V/A)(C/V) = C/A = s. [MEDIUM]
7. q = 0.63 q₀; V_C = 0.63 ℰ; I = 0.37 I₀. [EASY]
8. 0.37 q₀ remains — on discharge the quantity *decays* from q₀, so e⁻¹ ≈ 0.37 applies directly, rather than 1 − e⁻¹. [MEDIUM]
9. Each source supplies only a fraction of the total current, so each is drained more slowly; also less internal-resistance loss → more energy delivered. [EASY]
10. Identical internal resistances; otherwise the lower-r battery can be damaged by reverse current. [EASY]
11. Req = 120 Ω; I = 0.10 A; V = 2.0 V, 3.0 V, 7.0 V; sum = 12 V ✓. [EASY]
12. Req = 2 Ω; I(6Ω) = 2.0 A; I(3Ω) = 4.0 A; total = 6.0 A. [EASY]
13. Series pair = 100 Ω; 100 ∥ 25 = (100 × 25)/125 = 20 Ω. [EASY]
14. I = 9/(4.40 + 0.10) = 2.0 A; V = 9 − 2(0.10) = 8.8 V. [EASY]
15. Req = 3 Ω; V = 4 × 3 = 12 V; I(4Ω) = 3 A, I(12Ω) = 1 A; check I₁/I₂ = 3 = 12/4 ✓. [MEDIUM]
16. (a) 50 Ω; (b) 10/5 = 2 Ω. [EASY]
17. Req = 9 Ω; I = 1.33 A; V₁ = 8.0 V, V₂ = 4.0 V; ratio 2 = 6/3 ✓. [EASY]
18. 11.5 = 12 − 0.02I → I = 25 A. [MEDIUM — reversed terminal-voltage reasoning]
19. τ = 0.10 s; q₀ = 500 μC; I₀ = 5 mA; q(τ) = 500(1 − e⁻¹) ≈ 316 μC; q(0.2 s = 2τ) = 500(1 − e⁻²) ≈ 432 μC. [MEDIUM]
20. t = 2τ → q = 100·e⁻² ≈ 13.5 μC. [MEDIUM]
21. R = 6 ∥ 3 = 2 Ω; I = 12/2.05 = 5.85 A; V = 12 − 5.85(0.05) ≈ 11.71 V; I(3Ω) = 11.71/3 ≈ 3.9 A. [MEDIUM-HARD — parallel load inside a real-battery loop]
22. e^(−t/τ) = 0.10 → t = τ ln 10 ≈ 2.30τ; time = 2.30 × 9.75 ms ≈ 22.5 ms. [HARD — inverting the exponential]
23. R = τ/C = 0.5/100 × 10⁻⁶ = 5 kΩ; at t = 1.0 s = 2τ → 1 − e⁻² ≈ 86%. [MEDIUM]
24. (a) Series: ℰ = 3.0 V, r_total = 1.0 Ω. (b) Parallel: ℰ = 1.5 V, r_total = 0.25 Ω. [MEDIUM]
25. V₂/ℰ = R₂/(R₁ + R₂): 4/12 = R₂/(40 + R₂) → R₂ = 20 Ω. Verify: Req = 60 Ω, I = 0.2 A, V₂ = 0.2 × 20 = 4.0 V ✓. [MEDIUM — divider used as a design equation]
26. q₀ e^(−t/τ) = 0.1 q₀ → t = τ ln 10 ≈ 2.3τ. [MEDIUM]

---

# 13. TRANSFER QUESTIONS

*New-context problems carrying Lecture 7 concepts into unfamiliar settings.*

**T1 — Component-bin design:** You have exactly two 12 Ω resistors and must present (a) 6 Ω, then (b) 24 Ω to a circuit. Specify each connection and justify with the combination rules.
→ *Key:* (a) Parallel: 12/2 = 6 Ω; (b) Series: 24 Ω. Tests: structural command of both rules. [EASY]

**T2 — Vehicle electrical reasoning:** During engine start, a starter motor draws about 100 A from a 12.0 V battery with r = 0.010 Ω (Worked Example 4's values). Compute the terminal voltage during cranking, and explain why lights connected to the same battery dim momentarily. *(The dimming explanation follows directly from V = ℰ − Ir; the everyday framing is pedagogical.)*
→ *Key:* V = 12 − 100(0.010) = 11 V; every load connected to the terminals shares this sagged voltage. [MEDIUM]

**T3 — Timing design:** A timing circuit must reach 63% of full charge in 0.5 s and uses a 100 μF capacitor. Choose R. How long until the circuit is ~95% charged?
→ *Key:* 63% at one τ → τ = 0.5 s → R = 0.5/100 μF = 5 kΩ; 95% ≈ 3τ = 1.5 s. [MEDIUM]

**T4 — Energy-storage device:** Using the components of Worked Example 6 (ℰ = 12 V, C = 55.7 μF), compute the maximum energy the capacitor can store, then the energy stored at exactly one time constant. 
→ *Key:* U_max = q₀ℰ/2 = (6.68 × 10⁻⁴)(12)/2 ≈ 4.01 × 10⁻³ J. At t = τ: q = 0.63q₀ and V_C = 0.63ℰ → U = ½(0.63q₀)(0.63ℰ) = 0.199·q₀ℰ/... precisely U = 0.5 × (0.63)² × q₀ℰ ≈ 1.59 × 10⁻³ J. *(The (0.63)² relation is a direct substitution into the source's U = qV_C/2.)* [HARD — layered substitution]

**T5 — Mixed-battery hazard analysis:** A technician parallels a fresh 12 V battery (low internal resistance) with an aged 12 V battery (high internal resistance) to "boost" a system. Using the source's rule, identify which battery is at risk, what the mechanism is, and the design requirement that was violated.
→ *Key:* The fresh, low-r battery risks damage by reverse current; violated requirement: matched internal resistances. [MEDIUM — conceptual rule application]

**T6 — Derivation practice:** Starting from V₁ = IR₁ and V₂ = IR₂ for a series pair, prove the divider relation V₁/V₂ = R₁/R₂, then use it to explain why the largest resistor in a series chain always drops the largest share of the emf.
→ *Key:* V₁/V₂ = IR₁/IR₂ = R₁/R₂; the common I cancels; hence Vᵢ/ℰ = Rᵢ/Req grows with Rᵢ. [MEDIUM — first exposure to ratio reasoning]

---

# 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | All Lecture 7 topics present: series, parallel, mixed reduction, emf/terminal voltage, EMF series (aiding + opposing) & parallel (lifetime, current sharing, matched-r rule), RC charging (q, V_C, I, τ, 63/37), RC discharging (all three quantities), stored energy. |
| Mathematical formulas correct | ✅ | All 16 formulas match the source; all 6 worked examples reproduce the source's numerical results (WE5 energy cross-checked two ways: qV_C/2 and q²/2C). |
| Technical terminology preserved | ✅ | emf, terminal voltage, internal resistance, equivalent resistance, time constant, reverse current — all retained. |
| Explanations in original language | ✅ | No source paragraphs reproduced; only formulas and short standard definitions overlap. |
| Understandable to a first-year student | ✅ | Layered structure (core idea → explanation → example → key point); analogies clearly pedagogical. |
| Difficult concepts explicitly identified | ✅ | 5 concepts with full analysis and difficulty ratings in §9. |
| Common misconceptions identified | ✅ | 10 in §7; per-concept misconceptions in §9; in-video mistakes in §10–11. |
| Examples actually teach | ✅ | All 6 source examples retained with full reasoning steps; procedures taught before application. |
| Practice progresses understand → apply → transfer | ✅ | L1 (10 conceptual) → L2 (10 computational) → L3 (6 synthesis) + 6 transfer tasks, all with verified keys. |
| No unsupported claims added | ✅ | Pedagogical additions explicitly flagged (mixing old/new batteries illustration, "engine start" framing, (0.63)² energy substitution). No gaps requiring [SOURCE DOES NOT SPECIFY] in this lecture — all content fully specified in the source. |
| No large verbatim reproduction | ✅ | Only formulas and short definitions shared with the source. |
| Suitable for direct web integration | ✅ | Clean Markdown; student-facing self-check separated from instructor keys. |

**Source errata handled transparently (meaning preserved, typos not propagated):**
- The source's series derivation prints "R₁" twice where "R₂" is intended (e.g., "Req = R₁ + R₁ + R₃", "V₂ = IR₁") — corrected to R₂, consistent with the source's own worked example (35 + 82 = 117).
- Examples 2 and 3 label the second resistor as "R₁" — corrected to R₂ per the values given.
- Source's Example 5 energy line is garbled in layout ("q × ℰ(1 − e…)/2"); presented cleanly as U = qV_C/2 with V_C = ℰ(1 − e^(−t/τ)), reproducing the source's stated result 2.05 × 10⁻⁴ J.

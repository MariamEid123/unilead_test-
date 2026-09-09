تمام — دي **Lecture 6 (Electric Current)** بالباكدج الكامل — وبها تكتمل السلسلة كلها (Lectures 1–6). (تنبيهات توثيقية: فيه ٣ أخطاء مطبعية صغيرة في المصدر — هتلاقيها مشروحة في القسم الأول، المحتوى العلمي نفسه سليم وكل الأرقام اتفحصت.)

---

## 1. SOURCE ANALYSIS

**Source document:** Phy 211 Lecture Notes — Lecture 6, Fall 2024, AIU (Dr. Ashraf Mousa Abdelwahed), 11 pages.

| Item | Finding |
|---|---|
| Course | Phy 211 — Physics [full course title: SOURCE DOES NOT SPECIFY] |
| Chapter | Chapter 5 — Electric Current |
| Lecture | Lecture 6 (opens the DC-circuits part of the course) |
| Position | Builds on potential difference and the electric field (Lectures 3–4); independent of capacitors (Lecture 5), though the same ΔV language carries over |

**Main topics**
1. Free electrons in metals: thermal liberation, random motion, zero net current
2. Drift under an applied field → drift velocity → electric current
3. Electric current I: definition, I = Q/t, the ampere; electron flow vs. conventional current
4. Drift velocity, mobility μ, relaxation time τ; v_d = μE
5. Current density J = I/A
6. The micro-relation: n = N/V, I = nev_dA, J = nev_d
7. Ohm's law: V = IR, resistance, the ohm; potential drop along a conductor
8. emf and internal resistance: E = V + Ir; terminal voltage V = E − Ir
9. Resistivity ρ = RA/L and R = ρL/A; conductivity σ = 1/ρ (Siemens)
10. Temperature dependence: ρ_T = ρ_0(1 + αT), R_T = R_0(1 + αT)
11. Electric energy ΔU = IVt and power P = VI = V²/R = I²R
12. The kilowatt-hour and electric bills

**Important definitions:** free electrons; electric current; conventional current; drift velocity; mobility; relaxation time; current density; charge density (concentration) n; resistance; emf; internal resistance; terminal voltage; resistivity; conductivity; temperature coefficient α; the kWh.

**Worked examples in source:** Example 1 (Q and electron count from I and t), Example 2 (flashlight bulb: R, then new I at lower voltage), Example 3 (copper wire: diameter from R, then voltage drop), Example 4 (headlight resistance from P and V), Example 5 (heater power + monthly cost), Example 6 (bulb: I, R, and half-resistance replacement), Example 7 (reading-lamp hourly cost).

**Prerequisites (inferred):** Lectures 1–4 — charge and the electron (L1), the electric field (L3), potential difference and energy of a charge crossing ΔV (L4); basic algebra; energy and power concepts.

**Dependencies:** this is the first circuits lecture — everything later in circuits (resistor networks, etc., beyond the provided set [SOURCE DOES NOT SPECIFY]) builds on V = IR and power formulas introduced here.

**Difficult concepts identified:** electron flow vs. conventional current; drift velocity (slow electrons despite instant effects); I = nev_dA; emf vs. terminal voltage; resistance vs. resistivity; choosing among the three power formulas.

**Source notes for transparency (three cosmetic typos, content unaffected):**
1. The battery bullet is printed twice as "If the battery is **not** connected…" — the second instance clearly means "**connected** to a load" (V = E − Ir). Presented here with the intended meaning.
2. Example 3 writes "d = 2√(A/π) = √(A/π)" (dropped factor of 2 mid-line) — the final answer d = 2.1 × 10⁻³ m is correct for d = 2√(A/π).
3. Example 3b ends "1.2 d" — clearly "1.2 V."
4. Example 1's electron count rounds 3.75 × 10²¹ to 3.8 × 10²¹ — both shown below.
All other numbers re-verified: 5 Ω, 0.24 A, 3.4 × 10⁻⁶ m², 1.2 V, 3.6 Ω, 3600 W, 324 kWh, $34.02, 0.79 A, 120 Ω, 150 W, 276 Wh, $0.021 — all confirmed.

---

## 2. COURSE / MODULE / LESSON METADATA

- **COURSE:** Phy 211 — Physics (full title [SOURCE DOES NOT SPECIFY])
- **MODULE:** Chapter 5 — Electric Current (Module 2: DC Circuits — begins here)
- **LESSON:** Lecture 6 — Electric Current, Resistance, and Electric Power
- **TOPICS:** current & its definition; electron vs. conventional flow; drift velocity, mobility, relaxation time; current density; I = nev_dA; Ohm's law; emf & internal resistance; resistivity & conductivity; temperature dependence; power & energy; kWh & billing
- **PREREQUISITES:** Lectures 1–4 (charge/electron; field; potential difference; energy of charge through ΔV)
- **COMPETENCIES:** compute Q, N, I; relate I to drift velocity, density, and area; apply V = IR; distinguish emf from terminal voltage and find r; compute R from geometry (ρ, L, A) and its temperature scaling; compute power and energy in all forms; perform kWh cost calculations
- **DIFFICULTY:** Overall MEDIUM (long list of topics, each individually simple); two HARD sub-concepts: drift velocity & the I = nev_dA picture, and emf/internal resistance
- **ESTIMATED STUDY TIME:** ~100 minutes (≈60 min lesson + ≈40 min practice — the most example-dense lecture of the set)

**Position in the ARETE learning flow:** LEARN + PRACTICE. Gated on Lecture 4 (potential difference). Serves as the entry gate for the DC-circuits module and as a TRANSFER destination for the whole electrostatics arc (fields and potentials from Lectures 3–4 become the *engine* that drives current).

---

## 3. LEARNING OBJECTIVES

By the end of this lecture, the student should be able to:

1. Explain how free electrons arise in metals and why their random thermal motion produces zero net current.
2. Define electric current, compute I = Q/t (and Q = It), and count the electrons corresponding to a transported charge (Q = Ne).
3. Distinguish electron flow direction (− to + terminal) from conventional current direction (+ to −).
4. Define drift velocity, mobility, and relaxation time, and use v_d = μE and μ = eτ/m.
5. Define current density (J = I/A) and charge concentration (n = N/V), and derive/apply I = nev_dA and J = nev_d.
6. State and apply Ohm's law (V = IR), including the potential-drop relations V_A − V_B = IR and V_B − V_A = −IR.
7. Distinguish emf from terminal voltage, and compute internal resistance via E = V + Ir and r = (E − V)/I.
8. Distinguish resistance from resistivity; apply R = ρL/A, σ = 1/ρ, and predict how L and A changes affect R.
9. Apply the temperature model R_T = R_0(1 + αT) (and ρ_T = ρ_0(1 + αT)).
10. Compute electric energy (ΔU = IVt) and power in all three forms (VI, V²/R, I²R), choosing the correct form for the situation.
11. Convert between joules and kilowatt-hours and compute the operating cost of an appliance.

---

## 4. WEB-READY LESSON

# Lecture 6 — Electric Current, Resistance, and Electric Power

## Prerequisites
The student should already understand:
- Charge, the electron's charge e = 1.6 × 10⁻¹⁹ C, and Q = Ne (Lecture 1)
- The electric field and its effect on charges (Lecture 3)
- Potential difference ΔV and the energy change of a charge crossing it (Lecture 4)

---

### 1. From Free Electrons to Current

#### Core Idea
A metal's thermal energy liberates its outer electrons; they wander randomly (no current) — until an applied field lines them up into a slow, collective drift.

#### Explanation
In an uncharged metallic conductor at rest, the **thermal internal energy** of the material is enough to liberate the outer electrons of its atoms. These are the **free electrons** — free to move throughout the material.

Left alone, they move **randomly** in all directions. At any point inside the metal, just as many electrons wander one way as the other: the **net flow of charge at any point is zero — zero current**.

Now apply an **electric field / potential difference** across the conductor. Every free electron still jitters thermally, but superimposed on that jitter is a small, one-directional motion toward the positive terminal. That average directed velocity is the **drift velocity**, and this organized motion of charge is what we call **electric current**.

#### Example
A copper wire sitting in a drawer: free electrons by the trillion, all moving — and delivering exactly nothing, because their motion is perfectly disordered. Connect it to a battery: same electrons, now with a bias — current flows.

#### Key Point
Random motion ⇒ zero net charge flow. Field-imposed drift ⇒ current. The electrons were always there; the battery only *organizes* them.

---

### 2. Electric Current: Definition, Direction, and Counting

#### Core Idea
Current is the net charge passing through a cross-section of the conductor per unit time — and its "official" direction is opposite to the electron flow.

#### Explanation
The definition:

> **I = Q/t** (in general: I = ΔQ/Δt or I = dQ/dt) — unit: **C/s = A (Ampere)**

Two direction conventions coexist, and you must keep them straight:

- **Electrons** physically move from the **− terminal to the + terminal** of the source.
- **Conventional current** is defined as the current due to flow of **positive charge: from the + terminal to the − terminal**.

The conventional direction is the one used in all circuit analysis — arrows on diagrams, signs in equations. It's a historical convention that stuck, and it changes nothing physical.

For counting the charge carriers, reuse Lecture 1's quantization:

> **Q = Ne** (number of electrons × e)

so a current moving Q coulombs always corresponds to Q/e electrons.

#### Example
The source's Example 1: I = 2.5 A for 4 minutes (= 240 s). Q = It = 600 C, and N = Q/e = 600/1.6 × 10⁻¹⁹ ≈ **3.8 × 10²¹ electrons** (unrounded: 3.75 × 10²¹). One "ordinary" current ≈ trillions of trillions of electrons per second.

#### Key Point
I = Q/t in amperes; electrons go − to +, conventional current goes + to −; N = Q/e counts the carriers.

---

### 3. Drift Velocity, Mobility, and Relaxation Time

#### Core Idea
Drift velocity is the electrons' tiny average velocity toward the + terminal under an applied field; it is proportional to the field, with the mobility as the proportionality constant.

#### Explanation
Definitions, each building on the previous:

- **Drift velocity v_d:** the average velocity with which free electrons drift toward the + terminal when a field E is applied.
- **Mobility μ:** the drift velocity per unit electric field: **μ = v_d/E**, giving

> **v_d = μE**

with the microscopic model:

> **μ = eτ/m** (unit: m²·V⁻¹·s⁻¹)

- **Relaxation time τ:** the average time between two successive collisions of an electron with the lattice.

The picture: an electron accelerates under the field between collisions, collides, restarts. The steady average of this stop-and-go motion is the drift — and the longer the free time between collisions (bigger τ) or the lighter the particle (smaller m), the more effectively the field can organize the motion (bigger μ).

#### Example
*(Pedagogical, from the source's formulas)* If τ ≈ 10⁻¹⁴ s for a typical metal: μ = eτ/mₑ = (1.6 × 10⁻¹⁹)(10⁻¹⁴)/(9.1 × 10⁻³¹) ≈ 1.8 × 10⁻³ m²/V·s — and in a field of 0.01 V/m, v_d = μE ≈ 2 × 10⁻⁵ m/s. That's a fifth of a millimeter per second.

#### Key Point
v_d = μE with μ = eτ/m — drift is tiny, collision-limited, and proportional to the applied field.

---

### 4. Current Density and the Microscopic Relation: I = nev_dA

#### Core Idea
Current depends on three microscopic factors — how many carriers, how fast they drift, how much wire they flow through: I = nev_dA.

#### Explanation
**Current density** packs the "intensity" of current per unit area:

> **J = I/A** (unit: A·m⁻²)

**Charge density (concentration) n** counts the carriers per unit volume:

> **n = N/V = N/(AL)**

(for a wire segment of length L and cross-section A).

Now count the current directly from the picture. In one second, every electron advances v_d meters. The electrons that cross a given cross-section in that second are exactly those within a cylinder of length v_d behind it — volume A·v_d, containing n·A·v_d electrons, each carrying charge e:

> **I = n e v_d A**  and, dividing by A: **J = n e v_d**

The proportionality structure the source highlights: **I ∝ v_d, I ∝ n, I ∝ A.** Want more current? More carriers (n), faster drift (v_d), or a fatter pipe (A).

#### Example
*(Pedagogical, using typical metal values)* A wire of A = 1 mm² = 10⁻⁶ m², n = 10²⁸ m⁻³, carrying I = 1 A:
v_d = I/(neA) = 1/(10²⁸ × 1.6 × 10⁻¹⁹ × 10⁻⁶) ≈ **6 × 10⁻⁴ m/s** — less than a millimeter per second, for a perfectly ordinary one-amp current.

#### Key Point
I = nev_dA: carriers × charge × speed × area. Drift speeds are astonishingly small — the strength of current comes from the *enormous* n, not from fast electrons.

---

### 5. Ohm's Law and Resistance

#### Core Idea
The current through a conductor is directly proportional to the potential difference applied across its ends; the constant of proportionality is the resistance.

#### Explanation
The law:

> **V ∝ I → V = IR**, with **R = V/I** (unit: V/A = **Ω, "Ohm"**)

R measures the conductor's opposition to current flow. Along a conductor carrying current I from point A to point B, the potential drops in the direction of the current:

> **V_A − V_B = IR**  (going with the current: potential falls)
> **V_B − V_A = −IR** (going against it: potential rises)

Think of it as electrical "friction along a slope": current runs downhill from high potential to low, and R sets how steeply the potential must fall to push a given current.

#### Example
The source's Example 2a: a flashlight bulb drawing 300 mA from 1.5 V has R = V/I = 1.5/0.3 = **5 Ω**. In Example 2b the battery drops to 1.2 V — resistance unchanged (a device property) — so the current becomes I = V/R = 1.2/5 = **0.24 A**.

#### Key Point
V = IR — one law, three uses: find the current, the voltage, or the resistance. The drop along a current-carrying conductor is IR in the direction of flow.

---

### 6. emf, Internal Resistance, and Terminal Voltage

#### Core Idea
A real battery has an internal resistance; when current flows, part of the battery's emf is consumed inside — so the voltage you measure at the terminals is less than the emf.

#### Explanation
The battery's total "push" is its **emf, E**. But a real battery is not an ideal source: it has an **internal resistance r**. When a current I flows, Ohm's law applies *inside the battery too* — an amount Ir is dropped across r:

> **(emf) E = V + Ir**  →  **V = E − Ir**  →  **r = (E − V)/I**

where **V is the terminal voltage** — what the outside world actually receives. Two limiting cases:

- **Battery not connected to a load:** I = 0 → **V = E** (the terminal voltage equals the emf).
- **Battery connected and delivering current I:** **V = E − Ir** — the terminal voltage sags below the emf, and the more current is drawn, the more it sags.

The "missing" voltage Ir is consumed inside the battery itself.

#### Example
*(Pedagogical, built from the source's own Example 2 numbers and the formula above)* A flashlight battery with emf 1.5 V delivers I = 0.24 A while its terminal voltage reads 1.2 V. Then r = (E − V)/I = (1.5 − 1.2)/0.24 = **1.25 Ω**. Check: the bulb's 5 Ω across 1.2 V draws exactly 0.24 A ✓.

#### Key Point
E = V + Ir. Open circuit: V = E. Under load: V = E − Ir. The gap between emf and terminal voltage is the price of the battery's own internal resistance.

---

### 7. Resistivity and Conductivity: What R Is Made Of

#### Core Idea
Resistance depends on the wire's geometry; resistivity is the material's internal property — constant for the material at fixed temperature, independent of shape and size.

#### Explanation
The definition of **resistivity**:

> **ρ = RA/L** (unit: **Ω·m**)

inverted into the working formula:

> **R = ρL/A → R ∝ L and R ∝ 1/A**

A is the conductor's cross-sectional area; L its length. The crucial conceptual split:

- **Resistance R** — belongs to a *specific object*: double its length or fatten it, and R changes.
- **Resistivity ρ** — belongs to the *material*: it is constant for the conductor at constant temperature and **does not change with A or L**. Copper is copper, whatever shape you bend it into.

**Conductivity σ** is the reciprocal of resistivity — a material's willingness to conduct:

> **σ = 1/ρ = L/RA** (unit: Ω⁻¹·m⁻¹ or **S·m⁻¹, "Siemens"**)

#### Example
The source's Example 3a: a 20 m copper wire (ρ = 1.7 × 10⁻⁸ Ω·m) with R = 0.1 Ω. A = ρL/R = 3.4 × 10⁻⁶ m²; with A = πr², d = 2√(A/π) ≈ **2.1 mm**. And 3b: at I = 12 A, the wire's own drop is V = IR = **1.2 V**.

#### Key Point
R = ρL/A — length is the gas pedal (more wire, more resistance), area is the brake (fatter wire, less resistance). ρ belongs to the material; R to the object.

---

### 8. Resistance vs. Temperature

#### Core Idea
Resistivity (and hence resistance) grows linearly with temperature: ρ_T = ρ_0(1 + αT).

#### Explanation
The linear model from the source:

> **ρ_T = ρ_0(1 + αT)**  and  **R_T = R_0(1 + αT)**

with:

- **α:** the coefficient of increase in resistivity with temperature (unit: °C⁻¹ or K⁻¹)
- **ρ_0 / R_0:** the values at **zero temperature** (the model's reference)
- **ρ_T / R_T:** the values at temperature T

Graphically, plotting R against T gives a straight line through R₀ at T = 0 with **slope = R₀α**.

*(Pedagogical note: this is the model as given in the source — a linear law referenced to 0 °C. Use the course's formula exactly as stated in exams.)*

#### Example
*(Pedagogical)* With R₀ = 20 Ω and α = 5 × 10⁻³ /°C, at T = 100 °C: R = 20(1 + 0.5) = **30 Ω** — a 50% increase from heating.

#### Key Point
Hotter metal ⇒ more lattice jitter ⇒ more collisions ⇒ more resistance: R_T = R_0(1 + αT), slope R₀α.

---

### 9. Electric Energy and Power

#### Core Idea
A charge crossing a potential difference gains/loses energy ΔU = VΔQ; per unit time this is power — expressible in three equivalent ways.

#### Explanation
When a small charge ΔQ moves across a potential difference V, its electrical potential energy changes by:

> **ΔU = V·ΔQ** (Joule) → for a steady current: **ΔU = IVt**

**Power** is the rate of energy delivery:

> **P = ΔU/t = V·ΔQ/t = V·I** (unit: **Watt = J/s**)

and substituting Ohm's law (V = IR) in both directions gives the other two forms:

> **P = V(V/R) = V²/R**  and  **P = (IR)·I = I²R**

Three forms, one physics — but they answer *different questions* (see the difficult-concepts section): V²/R rules at fixed voltage; I²R rules at fixed current.

#### Example
The source's Example 4: a 40 W headlight designed for 12 V → R = V²/P = 144/40 = **3.6 Ω**. Example 6: a 75 W bulb at 95 V draws I = P/V = 0.79 A and has R = V/I ≈ 120 Ω.

#### Key Point
P = VI = V²/R = I²R; energy = power × time. At fixed V, lower resistance means *more* power — the brightest bulb is the "easiest" one for current to pass through.

---

### 10. The Kilowatt-Hour and Electric Bills

#### Core Idea
Electric bills charge for energy, not power — measured in kilowatt-hours: 1 kWh = 3.6 × 10⁶ J.

#### Explanation
For household energy, the practical unit is the **kilowatt-hour**:

> **Energy = Power × time**
> **1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J**

Cost calculation is always three steps:
1. Power in kW × hours of use = energy in kWh
2. Multiply by the rate per kWh
3. Interpret.

#### Example
The source's Example 5: a heater drawing 15 A on 240 V: P = IV = 3600 W = 3.6 kW. Running 3 h/day for 30 days: 90 hours → 3.6 × 90 = 324 kWh. At $0.105/kWh: **$34.02** per month. And Example 7: a 120 V, 2.3 A lamp for one hour: U = IVt = 276 Wh = 0.276 kWh → at $0.075/kWh, **$0.021** — about two cents of light.

#### Key Point
1 kWh = 3.6 MJ. Billing = (kW) × (hours) × (rate). A watt is a *rate*; a kWh is an *amount*.

---

### Key Takeaways

- Thermal energy liberates free electrons in metals; their random motion gives zero net current.
- Under an applied field, electrons drift toward the + terminal: that organized drift IS the current.
- I = Q/t (ampere = C/s); electrons flow − to +; conventional current flows + to −.
- Count electrons via N = Q/e — an ordinary ampere means ~10¹⁹–10²¹ electrons per second.
- Drift velocity: v_d = μE, with mobility μ = eτ/m and τ the mean time between collisions.
- I = nev_dA and J = nev_d: current = carriers × charge × drift speed × area. Drift speeds are sub-millimeter per second; the power of current comes from huge n.
- Ohm's law: V = IR; potential falls by IR in the direction of current flow.
- A real battery has internal resistance: E = V + Ir; open circuit V = E; under load V = E − Ir; r = (E − V)/I.
- R = ρL/A: length ↑ R, area ↓ R. Resistivity ρ (Ω·m) is the material's own property — geometry-independent; conductivity σ = 1/ρ (S/m).
- Temperature: R_T = R₀(1 + αT), slope R₀α — hotter conductors resist more.
- Power: P = VI = V²/R = I²R; energy U = IVt; 1 kWh = 3.6 × 10⁶ J — the billing unit of energy.

### Self-Check (answers are not shown — attempt before checking)

1. Why does an isolated metal wire carry no current even though its free electrons are moving?
2. A current of 0.5 A flows for 2 minutes. Find Q and the number of electrons transported.
3. In which direction do electrons move in a circuit, and in which direction is the conventional current defined? Which one do circuit diagrams use?
4. What is drift velocity, and why is it so small compared to the electrons' thermal speeds?
5. A wire carries the same current after being replaced by one with double the cross-sectional area. What happens to the drift velocity? (Use I = nev_dA.)
6. State Ohm's law. What happens to the current if the potential difference across a fixed resistor is doubled?
7. A battery's emf is 9 V. What voltage do its terminals show when no load is connected? Under a 2 A load with r = 0.3 Ω?
8. Distinguish resistance from resistivity: which changes when you cut a wire in half?
9. A 60 W bulb and a 100 W bulb are both rated 120 V. Which has the smaller resistance, and by what factor?
10. Why does an electric bill charge in kWh rather than in watts — and how many joules is one kWh?
11. Using R_T = R₀(1 + αT), at what temperature does a conductor's resistance double, in terms of α?

---

## 5. FORMULAS

### F1 — Electric current
**I = Q/t** (A); more generally I = ΔQ/Δt or dQ/dt
- **Q:** net charge through a cross-section; **t:** time.
- **When used:** any steady-current computation.
- **Interpretation:** charge flow rate; 1 A = 1 C/s.

### F2 — Charge counting
**Q = It = Ne**
- **N:** number of electrons; **e** = 1.6 × 10⁻¹⁹ C.
- **When used:** converting transported charge to electron counts.
- **Assumptions:** electrons are the carriers (metals).

### F3 — Drift velocity and mobility
**v_d = μE ; μ = v_d/E = eτ/m** (m²·V⁻¹·s⁻¹)
- **τ:** relaxation time — average time between two successive collisions; **m:** electron mass.
- **When used:** relating field to drift; comparing materials.
- **Interpretation:** drift ∝ field; longer collision-free time or lighter particle ⇒ higher mobility.

### F4 — Current density
**J = I/A** (A·m⁻²)
- **A:** cross-sectional area.
- **Interpretation:** current intensity per unit area — a local, wire-independent measure.

### F5 — Carrier concentration
**n = N/V = N/(AL)**
- **When used:** counting carriers per volume in a wire segment of area A and length L.

### F6 — The microscopic current law
**I = n e v_d A ; J = n e v_d**
- **When used:** connecting current to the microscopic picture; estimating drift speeds.
- **Interpretation:** I ∝ n, ∝ v_d, ∝ A — the three levers of current.

### F7 — Ohm's law
**V = IR ; R = V/I** (Ω)
- **When used:** any resistive element at fixed conditions.
- **Interpretation:** current ∝ voltage; R is the opposition. Along a conductor: V_A − V_B = IR (drop with the current).

### F8 — emf and internal resistance
**E = V + Ir ; V = E − Ir ; r = (E − V)/I**
- **E:** emf; **V:** terminal voltage; **r:** internal resistance; **I:** current drawn.
- **When used:** real batteries under load.
- **Interpretation:** I = 0 ⇒ V = E; the terminal sags by Ir when current flows.

### F9 — Resistance from geometry
**R = ρL/A ; ρ = RA/L** (Ω·m) ; **σ = 1/ρ = L/RA** (S·m⁻¹)
- **L:** length; **A:** cross-sectional area; **ρ:** resistivity (material property, constant at fixed temperature); **σ:** conductivity.
- **Interpretation:** R ∝ L, R ∝ 1/A; ρ and σ belong to the material, not the object.

### F10 — Temperature dependence
**ρ_T = ρ_0(1 + αT) ; R_T = R_0(1 + αT)**
- **α:** temperature coefficient (°C⁻¹ or K⁻¹); subscript 0: value at zero temperature.
- **Interpretation:** linear growth with T; graph slope = R₀α.

### F11 — Energy and power
**ΔU = VΔQ = IVt** (J) ; **P = VI = V²/R = I²R** (W)
- **When used:** energy delivered by a potential difference; power dissipated by any element.
- **Interpretation:** three power forms are equivalent via V = IR — choose by what's held fixed.

### F12 — Billing unit
**Energy = Power × time ; 1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J**
- **When used:** household/commercial energy accounting.

---

## 6. WORKED EXAMPLES

### Worked Example 1 — From current to electron count (Source: Example 1)
*A steady current of 2.5 A flows in a wire for 4 minutes. (a) How much charge passes any point? (b) How many electrons is that?*

**Step 1 — Convert the time:**
t = 4 min = 4 × 60 = 240 s

**Step 2 — Charge:**
Q = It = 2.5 × 240 = **600 C**

**Step 3 — Electrons (quantization from Lecture 1):**
N = Q/e = 600/(1.6 × 10⁻¹⁹) = 3.75 × 10²¹ ≈ **3.8 × 10²¹ electrons** *(source's rounded value)*

---

### Worked Example 2 — Ohm's law with a changing battery (Source: Example 2)
*A flashlight bulb draws 300 mA from a 1.5 V battery. (a) Find the bulb's resistance. (b) The battery voltage drops to 1.2 V — what is the new current?*

**Step 1 — (a) Ohm's law:**
R = V/I = 1.5/(300 × 10⁻³) = **5 Ω**

**Step 2 — (b) The bulb's resistance doesn't change — it's a property of the bulb:**
I = V/R = 1.2/5 = **0.24 A**

---

### Worked Example 3 — Designing a copper wire (Source: Example 3)
*ρ(copper) = 1.7 × 10⁻⁸ Ω·m. (a) Find the diameter of a 20 m wire whose resistance is 0.1 Ω. (b) Find the voltage drop across it at I = 12 A.*

**Step 1 — (a) Solve R = ρL/A for A:**
A = ρL/R = (1.7 × 10⁻⁸)(20)/(0.1) = **3.4 × 10⁻⁶ m²**

**Step 2 — Convert area to diameter (A = πr²):**
r = √(A/π) = √(1.082 × 10⁻⁶) ≈ 1.04 × 10⁻³ m
d = 2r ≈ **2.1 × 10⁻³ m = 2.1 mm** ✓ *(source's answer; the mid-line typo drops the factor 2 but the final value is correct)*

**Step 3 — (b) Voltage drop along the wire:**
V = IR = 12 × 0.1 = **1.2 V**

---

### Worked Example 4 — Resistance from power rating (Source: Example 4)
*Find the resistance of a 40 W automobile headlight designed for 12 V.*

**Step 1 — Choose the power form with known V and P:**
P = V²/R → R = V²/P

**Step 2 — Substitute:**
R = 12²/40 = 144/40 = **3.6 Ω**

---

### Worked Example 5 — Power and monthly cost (Source: Example 5)
*An electric heater draws 15.0 A on a 240 V line. Find its power and its monthly cost (30 days, 3 h/day, $0.105/kWh).*

**Step 1 — Power:**
P = IV = 15 × 240 = 3600 W = 3.6 kW

**Step 2 — Usage hours:**
(3 h/day)(30 days) = 90 hours

**Step 3 — Energy:**
3.6 kW × 90 h = 324 kWh

**Step 4 — Cost:**
324 × 0.105 = **$34.02 per month**

---

### Worked Example 6 — Bulb analysis and replacement (Source: Example 6)
*A 75 W bulb operates on 95 V. (a) Current? (b) Resistance? (c) Replaced by a bulb with half that resistance — is its power greater or less, and by what factor?*

**Step 1 — (a) From P = VI:**
I = P/V = 75/95 = **0.79 A**

**Step 2 — (b) Ohm's law:**
R = V/I = 95/0.79 ≈ **120 Ω**

**Step 3 — (c) New bulb, same 95 V, R′ = 60 Ω:**
P′ = V²/R′ = 95²/60 = 9025/60 ≈ **150 W — greater** (the fixed-voltage regime: less resistance ⇒ more power)

**Step 4 — Factor:**
150/75 = **2** — halving the resistance doubled the power.

---

### Worked Example 7 — Hourly cost of a lamp (Source: Example 7)
*A reading lamp carries 2.3 A at 120 V; energy costs $0.075/kWh. Find the cost of one hour of use.*

**Step 1 — Energy in watt-hours:**
U = IVt = 2.3 × 120 × 1 = 276 Wh = 0.276 kWh

**Step 2 — Cost:**
0.276 × 0.075 = **$0.021** (about two cents)

---

## 7. COMMON MISTAKES

**Mistake 1 — Reversing the current direction conventions.**
- *What students do:* draw electron flow (+ to −) or conventional current (− to +).
- *Why it's wrong:* electrons physically move − to +; conventional current is defined + to − and is what all circuit rules use.
- *How to avoid:* fix the pair in memory: "electrons Exit the negative terminal; conventional current Exits the positive."

**Mistake 2 — Thinking the electrons' motion speed is the current's "speed."**
- *What students do:* believe flipping a switch waits for electrons to travel from the switch to the lamp.
- *Why it's wrong:* drift speeds are ~10⁻⁴–10⁻³ m/s; the field organizes the *entire* electron population of the wire essentially at once.
- *How to avoid:* separate the carriers (slow) from the organization (fast): it's a push that propagates, not a package that travels.

**Mistake 3 — Confusing resistance with resistivity.**
- *What students do:* claim "copper has a resistance of 1.7 × 10⁻⁸ Ω."
- *Why it's wrong:* that number is resistivity ρ (Ω·m) — a material property. Resistance R belongs to a specific object and depends on L and A.
- *How to avoid:* attach the units mentally: Ω·m = material; Ω = object.

**Mistake 4 — Treating emf as the voltage under load.**
- *What students do:* plug the battery's labeled emf into V = IR for a loaded circuit.
- *Why it's wrong:* under load, the terminal voltage is V = E − Ir, strictly less than E.
- *How to avoid:* open circuit ⇒ V = E; anything drawing current ⇒ subtract Ir first.

**Mistake 5 — Using P = I²R when the voltage is the fixed quantity.**
- *What students do:* hear "higher resistance, more power" and apply I²R blindly at fixed V.
- *Why it's wrong:* at fixed V, P = V²/R — higher R means LESS power (the 60 Ω bulb of Example 6 drew more than the 120 Ω one).
- *How to avoid:* first ask what's held fixed — the source (voltage) or the current — then pick the formula.

**Mistake 6 — Diameter/radius slips in wire problems.**
- *What students do:* plug the diameter into A = πr², or forget to double r at the end.
- *How to avoid:* write A = πr², solve for r, then d = 2r — never skip the last doubling (Example 3 needed it).

**Mistake 7 — Unit sloppiness: mA, minutes, kWh.**
- *What students do:* enter 300 for 300 mA; use 4 instead of 240 s for "4 minutes"; treat kWh as a power unit.
- *Why it's wrong:* current needs amperes, time needs seconds, and kWh is *energy* (power × time).
- *How to avoid:* convert everything to SI before computing; convert to kWh only at the billing step.

**Mistake 8 — Misreading the temperature formula's reference.**
- *What students do:* apply R_T = R_0(1 + αT) with R₀ taken at room temperature.
- *Why it's wrong:* in this course's model, R₀ is the value at **zero temperature** — the reference of the given law.
- *How to avoid:* read the subscript literally: 0 ⇒ T = 0; use the source's convention in exams.

**Mistake 9 — Believing electrons are consumed by appliances.**
- *What students do:* imagine the lamp "uses up" the electrons delivered by the wire.
- *Why it's wrong:* the same electrons circulate; appliances consume *energy* (charge crossing a potential difference), not charge carriers.
- *How to avoid:* trace the energy, not the electrons: ΔU = VΔQ.

**Mistake 10 — Mixing up current direction with potential-drop signs.**
- *What students do:* write V_B − V_B = +IR when moving against the current.
- *Why it's wrong:* potential falls along the current: V_A − V_B = +IR going with it, −IR against.
- *How to avoid:* "downhill with the current": walking with I, you lose IR.

---

## 8. LECTURE SUMMARY

# Lecture Summary

## What You Need to Know
- Thermal energy frees outer electrons in metals; random motion ⇒ zero net current; an applied field creates a drift (v_d) toward the + terminal ⇒ current.
- I = Q/t (A = C/s); electrons flow − to +; conventional current + to −; N = Q/e counts carriers.
- v_d = μE; μ = v_d/E = eτ/m (τ = mean time between collisions).
- J = I/A; n = N/V; **I = nev_dA**, J = nev_d — drift is sub-mm/s; huge n carries the current.
- Ohm's law: V = IR; potential drops IR along the current direction.
- Real battery: E = V + Ir; open circuit V = E; under load V = E − Ir; r = (E − V)/I.
- R = ρL/A (R ∝ L, ∝ 1/A); ρ (Ω·m) is geometry-independent; σ = 1/ρ (S/m).
- R_T = R₀(1 + αT) — resistance grows linearly with temperature.
- ΔU = IVt; P = VI = V²/R = I²R; 1 kWh = 3.6 × 10⁶ J; cost = kWh × rate.

## Key Definitions
- **Free electrons** → outer electrons liberated by the metal's thermal energy, mobile throughout the material.
- **Electric current (I)** → net charge through a cross-section per unit time; ampere.
- **Conventional current** → current defined as positive-charge flow, + terminal to − terminal.
- **Drift velocity (v_d)** → average electron velocity toward the + terminal under an applied field.
- **Mobility (μ)** → drift velocity per unit field; μ = eτ/m.
- **Relaxation time (τ)** → average time between two successive electron collisions.
- **Current density (J)** → current per unit cross-sectional area.
- **Charge density (n)** → number of carriers per unit volume (concentration).
- **Resistance (R)** → a conductor's opposition to current; V = IR; ohm.
- **emf (E)** → the battery's total driving voltage.
- **Internal resistance (r)** → the battery's own resistance; consumes Ir when current flows.
- **Terminal voltage (V)** → the voltage actually delivered: E − Ir.
- **Resistivity (ρ)** → RA/L — the material's intrinsic resistance property, Ω·m.
- **Conductivity (σ)** → 1/ρ, Siemens per meter.
- **Kilowatt-hour** → 3.6 × 10⁶ J — the billed unit of energy.

## Key Formulas
- **I = Q/t; Q = Ne** → current and carrier counting.
- **v_d = μE; μ = eτ/m** → drift and mobility.
- **I = nev_dA; J = I/A = nev_d** → the microscopic current law.
- **V = IR; V_A − V_B = IR** → Ohm's law and potential drops.
- **E = V + Ir; V = E − Ir** → emf, internal resistance, terminal voltage.
- **R = ρL/A; σ = 1/ρ** → geometry ↔ material.
- **R_T = R₀(1 + αT)** → temperature scaling.
- **P = VI = V²/R = I²R; ΔU = IVt** → power and energy.
- **1 kWh = 3.6 × 10⁶ J** → billing.

## Important Ideas
- Current is organized motion, not fast motion — drift is tiny, n is astronomical.
- The conventional direction is a bookkeeping convention; physics runs on the formulas either way.
- A real battery is an ideal emf *in series with its own internal resistance* — the terminal voltage is what's left after the battery pays its own toll.
- ρ belongs to materials; R belongs to objects — the single most useful conceptual split in the lecture.
- Fixed V vs. fixed I flips the meaning of "more resistance": at fixed V, more R means less power; at fixed I, more R means more.
- Bills charge for *energy* (kWh = power × time), never for current or power alone.

## Common Mistakes
- Direction conventions reversed; drift speed mistaken for signal speed.
- emf used as the loaded terminal voltage.
- Resistance/resistivity conflation.
- Wrong power form for the constraint (I²R vs. V²/R).
- Diameter/radius and unit-conversion slips.
- kWh treated as power; temperature reference misread.

## Exam Focus
The concepts most likely to demand real understanding:
1. **I = nev_dA reasoning** — predicting how v_d responds to changes in I, A, or n.
2. **emf vs. terminal voltage** — computing r from (E, V, I) data and interpreting the sag.
3. **Fixed-V vs. fixed-I power logic** — the "which bulb is brighter" class of questions.
4. **R = ρL/A scaling** — geometry change problems (including the stretch-the-wire transfer).

## 60-Second Review
Thermal energy frees metal electrons; random motion = no current; a field drifts them toward + at v_d = μE (μ = eτ/m) — that's current: I = Q/t, electrons − to +, conventional + to −. Count with N = Q/e. Microscopically I = nev_dA — sub-millimeter drift, ~10²⁸ carriers per m³. Ohm: V = IR, potential falls IR along the current. Real battery: E = V + Ir — open: V = E; loaded: V = E − Ir. Wire: R = ρL/A (length up, area down); ρ is the material's own number, σ = 1/ρ; heat raises R by R₀(1 + αT). Power: P = VI = V²/R = I²R — fixed V: less R, more P; fixed I: more R, more P. Energy = Pt; 1 kWh = 3.6 MJ; cost = kWh × rate.

---

## 9. DIFFICULT CONCEPTS

### Difficult Concept: Conventional Current vs. Electron Flow

**Why students struggle:** Two arrows, opposite directions, both called "current" — and textbooks casually switch between them.
**Simple explanation:** The physical carriers move − to +. Before anyone knew that, physicists defined current as positive-charge flow, + to −. The definition stuck; every circuit law and diagram arrow uses it.
**Intuitive analogy:** Theater tickets: the audience (electrons) files *into* the hall while the empty seats file *out* — describing "seat flow" gives you a perfectly consistent arrow pointing exactly opposite the people's motion, and seat-accounting works flawlessly.
**Step-by-step explanation:** (1) Identify the carriers: in metals, electrons (negative). (2) They drift toward the + terminal: physical direction. (3) Define the conventional current: the direction positive carriers *would* move: + to −. (4) Use conventional direction in all diagrams, Ohm's-law drops, and circuit rules. (5) When counting carriers (N = Q/e), the answer is a count — direction doesn't enter.
**Mini example:** A battery drives 0.5 A through a bulb: electrons exit the − terminal through the wire; every drawing shows I exiting the + terminal. Both statements describe the same event.
**Misconception to avoid:** "Conventional current is wrong." It's a *convention*, not a claim — and it keeps every formula in the course consistent.
**Difficulty:** MEDIUM

### Difficult Concept: Drift Velocity — Slow Electrons, Instant Current

**Why students struggle:** "Current flows" evokes something racing through the wire; learning that electrons drift a fraction of a millimeter per second feels like a contradiction with reality (the lamp lights instantly).
**Simple explanation:** The current is not a courier carrying energy from the battery — it's the *simultaneous organization* of electrons already present everywhere in the wire. When the field appears, every free electron in the circuit begins drifting at once.
**Intuitive analogy:** A garden hose already full of water: open the tap and water leaves the nozzle immediately — not because new molecules raced down the hose, but because the whole column is pushed together. Or a packed crowd doing "the wave": each person moves centimeters; the wave crosses the stadium in seconds.
**Step-by-step explanation:** (1) The wire is already packed with free electrons (n ~ 10²⁸ per m³). (2) Apply a field via the switch: the field exists throughout the conductor. (3) Every electron begins drifting at v_d = μE — tiny, because collisions interrupt the acceleration every τ seconds. (4) Charge through any cross-section per second: I = n(e)(v_d)(A) — the *population*, not the speed, does the work. (5) The lamp lights because electrons at the lamp itself start moving immediately.
**Mini example:** *(Pedagogical)* 1 A in a 1 mm² copper wire: v_d ≈ 6 × 10⁻⁴ m/s — an electron would need ~40 minutes to cross one meter; the light still turns on the instant you flip the switch.
**Misconception to avoid:** "Electricity travels at the electrons' speed." The carriers crawl; the *organization* of the carriers is what propagates.
**Difficulty:** HARD

### Difficult Concept: The Microscopic Law I = nev_dA

**Why students struggle:** It's the first formula uniting a *count of invisible particles* with a *measurable macroscopic current* — and the cylinder-counting derivation is unfamiliar geometry.
**Simple explanation:** Hold a frame across the wire and count what crosses in one second: only electrons within v_d meters of the frame can make it — a cylinder of volume A·v_d, holding n·A·v_d electrons, each of charge e.
**Intuitive analogy:** A turnstile at a stadium: in one second, only the people within one "walking-second" of the gate can pass. Wider gate (A), denser crowd (n), faster walkers (v_d) — more people per second.
**Step-by-step explanation:** (1) Fix a cross-section of area A. (2) In 1 s, an electron moving at v_d sweeps a distance v_d. (3) All electrons inside the cylinder A·v_d behind the section cross it. (4) Their number: n·A·v_d. (5) Their charge: n·e·v_d·A = I. (6) Divide by A for the local version: J = nev_d.
**Mini example:** *(Pedagogical)* Triple the wire's diameter at the same current: A grows ×9, so v_d must fall to 1/9 — fatter pipe, lazier drift.
**Misconception to avoid:** "Current is proportional to electron speed alone." It's speed × density × area — a slow dense crowd out-delivers a fast sparse one.
**Difficulty:** HARD

### Difficult Concept: emf vs. Terminal Voltage (Internal Resistance)

**Why students struggle:** The battery is treated as a perfect, fixed source for years; introducing a hidden resistor *inside* it — and a voltage that depends on how much current you draw — breaks that mental model.
**Simple explanation:** The battery promises E volts but has to push its own current through its own internal resistance first — paying an Ir toll before delivering anything. What remains at the terminals is V = E − Ir.
**Intuitive analogy:** A water pump rated at a fixed pressure, connected through a narrow internal pipe: the more water you draw, the more pressure is lost inside the pump's own piping, and the less reaches your faucet. Zero flow (tap closed) ⇒ full rated pressure at the outlet.
**Step-by-step explanation:** (1) Model the battery: ideal emf E in series with internal resistance r. (2) Current I flows through both. (3) The internal drop: Ir. (4) Terminal voltage: V = E − Ir. (5) No load: I = 0 ⇒ V = E (the label value). (6) Given (E, V, I): r = (E − V)/I.
**Mini example:** *(Pedagogical, from the source's Example 2 numbers)* emf 1.5 V, terminal 1.2 V at 0.24 A → r = 0.3/0.24 = 1.25 Ω. Drawing twice the current would drop the terminal further — the sag grows with the load.
**Misconception to avoid:** "The battery's label is what it delivers." Only when nothing is connected; under load, subtract the internal toll first.
**Difficulty:** HARD

### Difficult Concept: Resistance vs. Resistivity

**Why students struggle:** Two near-identical words, one algebraic relation (ρ = RA/L), and a habit of solving for whichever symbol looks isolated.
**Simple explanation:** Resistivity is the material's personality (Ω·m); resistance is the personality *expressed through a shape* (Ω). Same copper, different wire shapes — same ρ, wildly different R.
**Intuitive analogy:** Travel time through a city: the city's traffic density (resistivity) is fixed, but your trip time (resistance) depends on route length (L) and road width (A). Lengthen the route: more time. Widen the road: less time. Neither changes how congested the city itself is.
**Step-by-step explanation:** (1) Ask: material or object? (2) Material ⇒ ρ, Ω·m, independent of A and L at fixed temperature. (3) Object ⇒ R = ρL/A, changes with geometry. (4) Scaling rules: R ∝ L (series more wire), R ∝ 1/A (parallel more lanes). (5) Conductivity: σ = 1/ρ — the material's friendliness.
**Mini example:** Doubling a wire's length doubles R; folding it double (half L, same A... or doubling A by laying two side by side) halves R — ρ never moved.
**Misconception to avoid:** "Cutting the wire changes copper's resistivity." It changes the *object's* resistance only.
**Difficulty:** MEDIUM

### Difficult Concept: Choosing Among P = VI, V²/R, I²R

**Why students struggle:** Three equivalent formulas that *disagree* if used carelessly — because they hide assumptions about what's held constant.
**Simple explanation:** All three are Ohm's law in disguise. The question "does more resistance mean more power?" has two opposite answers: fixed V ⇒ V²/4R... no — P = V²/R says less; fixed I ⇒ P = I²R says more. The formula choice must match the constraint.
**Intuitive analogy:** Waterfall power: the drop height (V) and the flow (I) trade off through the channel's narrowness (R). Hold the height fixed and widen the channel — more flow, more power. Hold the flow fixed and narrow the channel — you need more height, delivered elsewhere, and more power burns *in the channel*.
**Step-by-step explanation:** (1) Identify the constraint: a fixed source voltage (most household cases) or a fixed current. (2) Fixed V ⇒ use P = V²/R: R and P move oppositely. (3) Fixed I ⇒ use P = I²R: R and P move together. (4) If neither is fixed, use P = VI directly with measured values. (5) For energy: U = Pt.
**Mini example:** The source's Example 6c: at fixed 95 V, halving R (120 → 60 Ω) *doubled* the power (75 → 150 W). Same bulbs at fixed current would show the opposite.
**Misconception to avoid:** "Higher resistance always dissipates more power." Only at fixed current; at fixed voltage it's exactly backwards.
**Difficulty:** MEDIUM

---

## 10. VIDEO LESSON PLANS

*(Plans for the HARD concepts: drift velocity + I = nev_dA — combined into one video, since they form a single storyline — and emf/internal resistance.)*

### VIDEO 1

**VIDEO TITLE:** Slow Electrons, Instant Light: The Drift Velocity Paradox

**TARGET CONCEPT:** Drift velocity (v_d = μE), the microscopic law I = nev_dA, and why tiny drift speeds still produce instant, powerful currents

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can explain why current flows the instant a switch closes despite sub-millimeter-per-second drift, derive I = nev_dA by cylinder counting, and predict how v_d responds to changes in I, A, or n.

**HOOK:** "Flip a switch — the lamp is on before your finger finishes moving. So the electrons must be sprinting down that wire, right? Wrong. They're drifting at less than a millimeter per second — a snail would beat them to the lamp. And yet the light is instant. Today we resolve the paradox, and in doing so, you'll meet the single most important microscopic equation in this chapter."

**EXPLANATION:**
1. The setup: metals are packed with free electrons (thermal energy liberates them); random motion ⇒ zero current.
2. The switch closes: the field exists throughout the wire — every electron starts drifting at once.
3. Why the drift is so slow: collisions every τ seconds; v_d = μE, μ = eτ/m.
4. The garden-hose/wave resolution of the paradox: nothing travels; everything is pushed.
5. Cylinder counting → I = nev_dA; the three levers (n, v_d, A).
6. A live estimate with typical numbers (marked pedagogical) → sub-mm/s for 1 A.

**VISUALS:**
- Wire cross-section packed with electron dots jittering randomly (thermal) with a "net flow: ZERO" meter.
- Switch closes: a field shading sweeps the whole wire; every dot gains a small rightward bias — the "net flow" meter jumps instantly.
- Slow-motion zoom: one electron accelerating, colliding, restarting — τ timer popping.
- Garden-hose animation: full pipe, tap opens, outlet flows immediately.
- The cylinder: a highlighted slice of wire; everything within v_d of the cross-section crosses in 1 s; the slice labeled with n·A·v_d electrons.
- A "v_d-o-meter" showing 6 × 10⁻⁴ m/s next to a snail icon.

**EXAMPLE:** *(Pedagogical, typical metal values, clearly marked)* 1 A through a 1 mm² wire with n = 10²⁸ m⁻³ → v_d ≈ 6 × 10⁻⁴ m/s; then predict v_d when the wire is replaced by one with double diameter at the same current (÷ 4).

**COMMON MISTAKE:** Believing the signal travels at v_d; believing electrons are consumed by the appliance; forgetting A in mm² must convert to m².

**CHECK FOR UNDERSTANDING:** "Same current, wire replaced by one with double the cross-sectional area: does the drift velocity rise, fall, or stay? By what factor?"

**FINAL TAKEAWAY:** Current = a whole population nudged at once: I = nev_dA. The carriers crawl; the current is instant because the push is instant.

---

### VIDEO 2

**VIDEO TITLE:** Where Did My Volts Go? emf, Internal Resistance, and the Sagging Battery

**TARGET CONCEPT:** emf vs. terminal voltage; E = V + Ir; computing r; the load-dependence of terminal voltage

**TARGET STUDENT:** First-year university student

**DURATION:** ~8:30

**LEARNING OBJECTIVE:** The student can model a real battery as emf + internal resistance, explain why the terminal voltage equals E only at zero current, and compute r from (E, V, I) data.

**HOOK:** "A fresh battery says nine volts on the label. My multimeter agrees — nine volts. Then I connect it to a real load, and the terminals read eight point four. Where did zero point six volts go? Nobody cut the wire. Nobody inserted a resistor. The volts vanished *inside the battery* — and by the end of this video you'll be able to compute exactly where."

**EXPLANATION:**
1. The ideal battery myth: a perfect, unchanging source.
2. The real model: an ideal emf E in series with the battery's own internal resistance r.
3. Current through the battery pays a toll: Ir dropped inside before anything reaches the terminals.
4. The master equation: E = V + Ir → V = E − Ir.
5. The open-circuit case: I = 0 ⇒ V = E — the label is true only when nothing is connected.
6. Extraction: r = (E − V)/I from measured data.
7. Why heavy loads sag harder: bigger I, bigger Ir toll.

**VISUALS:**
- A battery cut open: an ideal "E" battery icon with a small resistor "r" drawn inside the casing.
- A voltage budget bar: E splits into V (delivered, green) + Ir (internal toll, red) — the red slice grows as I grows.
- A live scenario: multimeter reading 9.0 V open, sagging to 8.4 V under load, with the 0.6 V animating into the internal resistor and dissolving as heat.
- A V-vs-I graph: a straight line starting at (0, E) with slope −r.

**EXAMPLE:** *(Pedagogical, built from the lecture's own Example 2 numbers)* Flashlight battery, emf 1.5 V, delivering 0.24 A with the terminal reading 1.2 V → r = (1.5 − 1.2)/0.24 = 1.25 Ω; cross-check with the bulb's 5 Ω drawing 0.24 A at 1.2 V ✓.

**COMMON MISTAKE:** Using E (the label) as the circuit voltage under load; treating r as an external component; forgetting that V = E only at I = 0.

**CHECK FOR UNDERSTANDING:** "A 12 V (emf) battery with r = 0.1 Ω delivers 30 A to a starter motor. What voltage do the terminals show — and where did the rest go?"

**FINAL TAKEAWAY:** A real battery pays a toll before it delivers: E = V + Ir. Open circuit: V = E. Under load: V = E − Ir — and the heavier the load, the deeper the sag.

---

## 11. VIDEO SCRIPTS

### VIDEO SCRIPT 1 — Slow Electrons, Instant Light

**[0:00–0:30] Hook**
"Flip a light switch. The lamp is on before your finger finishes moving. So obviously the electrons are sprinting down that wire, right? Here's the truth: they're drifting at less than a millimeter per second. A snail — an actual garden snail — would beat them to the lamp by a mile. And the light still comes on instantly. That's not a contradiction — it's the most misunderstood fact in all of electricity, and untangling it will hand you the key equation of this entire chapter. Let's go."

**[0:30–2:00] Concept introduction**
"Start with what a metal wire actually is. The atoms are locked in a lattice, but their outer electrons — the loose ones — have been knocked free by the metal's own thermal energy. We call them free electrons, and a copper wire is *packed* with them: on the order of ten to the twenty-eight per cubic meter. Now watch what they're doing. Constant, frantic, random motion — every direction, equally. And here's the punchline of randomness: at any point in the wire, just as many electrons are wandering left as right. Net flow of charge: zero. A wire sitting in a drawer is a stampede going nowhere. Current requires *organization* — and that's what the switch provides. Close it, and a potential difference appears across the wire — an electric field, everywhere in the conductor, essentially at once. Every single free electron, along the entire length, feels a force toward the positive terminal. Random jitter plus a tiny collective bias toward plus — that bias is the drift velocity. That's what current is: not fast electrons — *organized* electrons."

**[2:00–4:00] Visual explanation**
"Now the speed question — why so slow? Watch one electron in slow motion. The field accelerates it. But it lives in a crowded lattice: within about ten-to-the-minus-fourteen seconds it slams into something and stops. Then the field accelerates it again. Crash, restart, crash, restart. The *average* of this stop-and-go is the drift velocity — and because each free run is so short, that average is minuscule. Your lecture captures it in two formulas: drift velocity equals mobility times field, v-d equals mu-E; and the mobility itself is e-tau over m, where tau is the average time between collisions. Shorter collision-free time, or a heavier particle — less mobility, lazier drift. So how does a millimeter-per-second crawl produce an instant lamp? The garden hose. Your hose is already full of water. Open the tap, and water leaves the nozzle immediately — not because new molecules raced down the hose, but because the entire column is pushed together. The wire is the same: it's already full of electrons. The switch doesn't *send* anything from the battery to the lamp — it nudges the electrons already at the lamp. And now, the counting equation. Imagine a frame fixed across the wire. In one second, which electrons cross it? Only those close enough to reach it: everything within v-d meters of the frame. That's a cylinder — area A, length v-d, volume A-v-d. Electrons inside: n times A times v-d. Each carries charge e. Multiply it out: current equals n, e, v-d, A. Four factors — how many carriers, what charge, how fast they drift, how fat the pipe."

**[4:00–6:00] Worked example**
"Let's put real numbers on it — typical metal values, so treat these as an illustration. Take one ampere through a wire of one square millimeter — that's ten to the minus six square meters. Carrier density, ten to the twenty-eighth per cubic meter. Drift velocity: v-d equals I over n-e-A. Denominator: ten to the twenty-eight, times one point six times ten to the minus nineteen, times ten to the minus six. The powers stack: ten to the twenty-eight, minus nineteen, minus six — ten to the three. Times the one point six: sixteen hundred. So v-d is one over sixteen hundred — about six times ten to the minus four meters per second. Look at that number. Six tenths of a millimeter per second. An electron crossing a one-meter wire would need about half an hour. And that's carrying a perfectly ordinary, perfectly useful ampere. The lesson is right there in the formula: the current is strong not because the electrons are fast, but because there are *so many of them*. Speed times population — and the population is astronomical. Now a prediction test. Same current, but a fatter wire — double the diameter. Area goes up by four. One ampere spread over four times the area: the drift velocity drops to a quarter. Same current, lazier electrons, fatter pipe. If you can make that prediction with the formula alone, you own this equation."

**[6:00–7:00] Common mistake**
"Three mistakes to dodge. Mistake one, the big one: 'electricity travels at the drift speed.' No — the *carriers* crawl; the *push* — the field organizing the whole population at once — is what propagates. Never again say the switch waits for electrons to arrive from the battery. Mistake two: 'the lamp uses up the electrons.' Nothing is consumed. The same electrons circulate forever; what the lamp takes is *energy* — charge falling through a potential difference. Mistake three, the arithmetic trap: the area must be in square *meters*. One square millimeter is ten to the minus six — miss that conversion and your drift velocity is off by a factor of a million, which is exactly the kind of error that makes students trust the wrong answer because it 'looks reasonable.'"

**[7:00–8:00] Quick student challenge**
"Your turn. A wire carries a steady current. The wire is replaced with one made of a material with *half* the carrier density — same size, same current. Question: what happens to the drift velocity, and by what factor? Pause and reason it through with I equals n-e-v-d-A. … Current fixed: the product of n and v-d must stay constant. Halve n, and v-d must *double* — fewer carriers means each must work harder... drift faster... to deliver the same current. Same logic as before, run in reverse. If you got that — and you can explain *why* in one sentence — you're ready for anything this chapter throws at this equation."

**[8:00–8:30] Final recap**
"Thirty seconds. A metal is packed with free electrons in random motion — zero net flow. Close the switch: the field organizes all of them at once into a drift of v-d equals mu-E — tiny, because collisions interrupt everything every tau seconds. Count what crosses a frame in one second — everything in the cylinder A-v-d — and you get the master equation: I equals n-e-v-d-A. The carriers crawl; the current is instant; the strength comes from the crowd. Slow electrons, instant light — no paradox left."

---

### VIDEO SCRIPT 2 — Where Did My Volts Go?

**[0:00–0:30] Hook**
"Fresh battery. The label says nine volts. I put a multimeter on the terminals: nine volts — the label tells the truth. Now I connect the battery to a real circuit, and measure again: eight point four volts. Point six volts — gone. Nobody cut the wire. Nobody snuck a resistor into my circuit. So where did they go? Spoiler: they never left. They're being spent *inside the battery itself* — and once you see the model, you'll be able to compute the missing volts, and the hidden resistance causing them, in under a minute."

**[0:30–2:00] Concept introduction**
"Here's the myth we've been quietly using: a battery is a perfect source — it holds its terminals at its rated voltage, always, no matter what. Here's the reality. Every real battery has two parts living inside its casing. First, the ideal part — the emf, capital E — the battery's true driving voltage, what the label promises. Second, the unglamorous part: the battery's own internal resistance — lowercase r. The chemicals and internals of a battery aren't perfect conductors; pushing current *through the battery itself* costs something. So picture the model: an ideal E-volt source, in series with a small resistor r, both hidden inside the casing. When no current flows — nothing connected — there's no toll to pay, and the terminals sit at exactly E volts. That's why the meter reads the label. But the moment a load draws a current I, that current has to pass through the internal resistance — and Ohm's law does not care whose resistor it is. The drop across r is I-times-r, paid *before* the outside world sees a single volt. What's left at the terminals: E minus I-r. That's your terminal voltage, capital V."

**[2:00–4:00] Visual explanation**
"Watch the voltage budget. The full bar is the emf, E. Every volt of it gets spent somewhere. The green slice is what the terminals deliver — V. The red slice is the internal toll — I-r. With a light load, tiny current, the red slice is a sliver: the terminals sit just under E. Now crank the load — a motor starting, a heater warming up. Current climbs. The red slice eats the budget: the terminal voltage visibly sags. That's the entire phenomenon of a 'weak battery' — not a smaller promise, a bigger toll. Write it as the master equation: E equals V plus I-r. Rearranged: V equals E minus I-r. And the extraction formula — this is the exam move — r equals E-minus-V over I. Given the emf, the measured terminal voltage, and the current, you can compute the hidden resistance directly. Two landmark cases to memorize. Open circuit — nothing connected, I equals zero: the equation collapses to V equals E. The label is true *only* here. Heavy load — big I: the toll grows, and the sag deepens. Plot terminal voltage against current and you get a straight line: starting at E when I is zero, sloping downward — and the slope's magnitude is r. One graph, one hidden number, readable at a glance."

**[4:00–6:00] Worked example**
"Numbers, straight from your own lecture — a flashlight. A battery with emf one point five volts drives a bulb. With the circuit running, the terminal voltage measures one point two volts, and the current is zero point two four amps — those exact values come from the lecture's Example 2, where the five-ohm bulb draws zero point two four amps at one point two volts. Now the question the lecture's formulas were built for: what's the battery's internal resistance? Extraction formula: r equals E-minus-V, over I. E-minus-V: one point five minus one point two — zero point three volts of internal toll. Divide by the current, zero point two four: r equals one point two five ohms. Done. And let's close the loop with a consistency check — this is the habit that catches errors: the terminal voltage should equal the current through the bulb times the bulb's resistance. Zero point two four times five ohms — one point two volts. Matches the measured terminal voltage exactly. The model isn't a story; it's bookkeeping that balances. One more piece of interpretation, free of charge: those zero point three 'missing' volts are being *dissipated inside the battery* — power equals I-squared-r, about seventy milliwatts of warmth in your hand. That's why heavy-duty batteries get warm, and why dead batteries read fine on a multimeter yet fail under load: high internal resistance, huge toll, collapsed terminal."

**[6:00–7:00] Common mistake**
"Three traps. Trap one, the classic: plugging the *label* — the emf — into V equals I-R for the outside circuit while current is flowing. Under load, the circuit sees E minus I-r, always less than E. Open circuit only: V equals E. Trap two: hunting for the internal resistance out in the wires. It's not a component you can clip out — it lives inside the casing, in series with the ideal source. Trap three: reading a battery's health from its open-circuit voltage alone. A battery can read a perfect twelve volts with a multimeter and still fail the moment a load appears — because the multimeter draws essentially zero current, paying zero toll. The emf survived; the internal resistance grew. If you want a battery's real story, measure the terminal voltage *while it's working*."

**[7:00–8:00] Quick student challenge**
"Your turn — a real-world one. A car battery: emf twelve volts, internal resistance zero point one ohms. The starter motor draws thirty amps on a cold morning. Question one: what voltage do the battery terminals actually show during cranking? Question two: where did the rest go? Pause — both answers. … Terminal voltage: E minus I-r — twelve, minus thirty times zero point one — twelve minus three — *nine volts*. The starter, expecting twelve, gets nine — that's the sluggish crank of a cold, tired battery. The missing three volts: dissipated inside the battery at P equals I-squared-r — nine hundred times zero point one — ninety watts of heat warming the battery's own internals. If you nailed both, and you can explain *why* the sag grows with the current, you've fully internalized the model."

**[8:00–8:30] Final recap**
"Thirty seconds. A real battery is an ideal emf in series with its own internal resistance. Current through the battery pays an internal toll of I-r before anything reaches the terminals. Terminal voltage: V equals E minus I-r. Open circuit — I equals zero — the terminal equals the emf: the label is true only for an idle battery. Under load, the label sags by exactly the toll. And from measurements: r equals E-minus-V over I. The volts were never stolen — they were spent at home. That's where your volts went."

---

## 12. PRACTICE QUESTIONS

*(Student-facing questions. Instructor keys are for platform use and must not be displayed with the question.)*

### LEVEL 1 — UNDERSTAND

**Q1.** Why does an isolated metal wire carry no current, even though its free electrons are in constant motion?
> *Instructor key — Answer:* The motion is random and isotropic — equal flow in every direction, so the *net* charge transport through any cross-section is zero. Current requires an applied field/potential difference to bias the motion (drift). *Skill:* random-vs-drift concept. *Difficulty:* EASY.

**Q2.** In which physical direction do electrons move in a circuit, and how is conventional current defined? Which direction do circuit diagrams use?
> *Instructor key — Answer:* Electrons: − terminal → + terminal. Conventional current: + terminal → − terminal (defined as positive-charge flow). Diagrams and all circuit rules use the conventional direction. *Skill:* conventions. *Difficulty:* EASY.

**Q3.** Define mobility and relaxation time, and state the relation between them.
> *Instructor key — Answer:* Mobility μ = v_d/E (drift velocity per unit field), μ = eτ/m; relaxation time τ = average time between two successive collisions. *Skill:* definitions. *Difficulty:* EASY.

**Q4.** Distinguish resistance from resistivity. Which of the two changes if a wire is cut in half lengthwise?
> *Instructor key — Answer:* Resistivity ρ (Ω·m) is a material property, independent of geometry (at fixed temperature); resistance R = ρL/A belongs to a specific object. Cutting the wire in half changes its R (halves it) but not ρ. *Skill:* R vs. ρ. *Difficulty:* EASY–MEDIUM.

**Q5.** State the two limiting cases of terminal voltage for a battery with emf E and internal resistance r.
> *Instructor key — Answer:* Open circuit (I = 0): V = E. Connected and delivering I: V = E − Ir. *Skill:* emf/terminal cases. *Difficulty:* EASY.

**Q6.** Is the kilowatt-hour a unit of power or of energy? How many joules is one kWh?
> *Instructor key — Answer:* Energy: 1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J. *Skill:* units. *Difficulty:* EASY.

### LEVEL 2 — APPLY

**Q7.** A current of 0.8 A flows for 5 minutes. Find the total charge transported and the corresponding number of electrons.
> *Instructor key — Answer:* t = 300 s; Q = It = 240 C; N = Q/e = 240/1.6 × 10⁻¹⁹ = 1.5 × 10²¹ electrons. *Skill:* I = Q/t + N = Q/e. *Difficulty:* EASY–MEDIUM.

**Q8.** A 60 W bulb is rated for 120 V. Find its resistance and its operating current.
> *Instructor key — Answer:* R = V²/P = 14400/60 = 240 Ω; I = P/V = 0.5 A. *Skill:* power forms. *Difficulty:* MEDIUM.

**Q9.** An aluminum wire has ρ = 2.8 × 10⁻⁸ Ω·m, length 10 m, cross-section 2 × 10⁻⁶ m². Find its resistance, the voltage drop at I = 12 A, and the power it dissipates.
> *Instructor key — Answer:* R = ρL/A = (2.8 × 10⁻⁸)(10)/(2 × 10⁻⁶) = 0.14 Ω; V = IR = 1.68 V; P = I²R = 144 × 0.14 ≈ 20.2 W. *Skill:* R = ρL/A + drop + dissipation. *Difficulty:* MEDIUM.

**Q10.** A heater draws 10 A on a 220 V line and runs 4 hours/day for 30 days. Find the monthly energy in kWh and the cost at $0.12/kWh.
> *Instructor key — Answer:* P = IV = 2200 W = 2.2 kW; hours = 120; energy = 264 kWh; cost = 264 × 0.12 = $31.68. *Skill:* billing. *Difficulty:* MEDIUM.

**Q11.** A conductor has R₀ = 20 Ω (at the model's zero-temperature reference) and α = 5 × 10⁻³ /°C. Find its resistance at 100 °C.
> *Instructor key — Answer:* R_T = R₀(1 + αT) = 20(1 + 0.5) = 30 Ω. *Skill:* temperature model. *Difficulty:* EASY–MEDIUM.

**Q12.** A battery with emf 9 V shows a terminal voltage of 8.1 V while delivering 0.9 A. Find r and the resistance of the load.
> *Instructor key — Answer:* r = (E − V)/I = 0.9/0.9 = 1 Ω; R_load = V/I = 8.1/0.9 = 9 Ω. Check: E = I(R + r) = 0.9 × 10 = 9 V ✓. *Skill:* internal resistance extraction. *Difficulty:* MEDIUM.

---

## 13. TRANSFER QUESTIONS

### LEVEL 3 — TRANSFER

**Q13.** A wire of resistance R is stretched uniformly to twice its length (volume constant). What is its new resistance? Justify using R = ρL/A and volume conservation.
> *Instructor key — Answer:* Volume AL constant: L → 2L forces A → A/2. R′ = ρ(2L)/(A/2) = 4ρL/A = **4R** — both levers (length up, area down) push resistance in the same direction. *Skill:* geometric transfer of R = ρL/A. *Difficulty:* MEDIUM–HARD.

**Q14.** Two bulbs are rated 60 W and 100 W, both at 120 V. (a) Which has the smaller resistance? (b) Compute both resistances. (c) A student concludes "the 100 W bulb must resist more to make more power." Evaluate this claim.
> *Instructor key — Answer:* (a) The 100 W bulb. (b) R = V²/P: 60 W → 240 Ω; 100 W → 144 Ω. (c) False — at *fixed voltage* (P = V²/R), more power means *less* resistance; the claim wrongly applies the fixed-current regime (P = I²R). *Skill:* power-form selection + misconception repair. *Difficulty:* MEDIUM–HARD.

**Q15.** A 12 V-emf battery with internal resistance 0.1 Ω supplies a starter motor drawing 30 A. (a) Find the terminal voltage during cranking. (b) Find the power dissipated *inside* the battery. (c) Explain why a battery can read full voltage on a multimeter yet still fail to start a car.
> *Instructor key — Answer:* (a) V = E − Ir = 12 − 3 = 9 V. (b) P_r = I²r = 900 × 0.1 = 90 W. (c) The multimeter draws ~zero current ⇒ pays ~zero internal toll ⇒ reads E; under a heavy load, a large (aged) r eats the budget: terminal collapses. *Skill:* emf model transferred to diagnosis. *Difficulty:* HARD.

**Q16.** Using R_T = R₀(1 + αT), at what temperature does a conductor's resistance double? Express your answer in terms of α, then evaluate for α = 4 × 10⁻³ /°C.
> *Instructor key — Answer:* Doubling: 2R₀ = R₀(1 + αT) ⇒ αT = 1 ⇒ **T = 1/α**; for α = 4 × 10⁻³: T = 250 °C. *Skill:* inverting the linear model. *Difficulty:* MEDIUM.

**Q17.** A laptop charger delivers 65 W and is used 6 h/day for 30 days. At $0.10/kWh, find the monthly cost. Then explain why the *power* rating alone cannot determine the bill.
> *Instructor key — Answer:* Energy = 65 W × 180 h = 11.7 kWh → $1.17. Power is a *rate*; cost depends on rate × usage time × price — a 1500 W heater used 1 h can cost less than a 65 W charger left on all month. *Skill:* energy accounting + rate-vs-amount reasoning. *Difficulty:* MEDIUM.

**Q18.** The same current I flows through two wires of identical dimensions but different carrier concentrations: n₁ = 2n₂. Compare their drift velocities and their current densities. Justify with I = nev_dA and J = I/A.
> *Instructor key — Answer:* Same I and same A ⇒ same J = I/A. But I = nev_dA: with n₁ = 2n₂, v_d1 = v_d2/2 — the denser wire drifts *half as fast* to deliver the same current. Current density depends on the wire, drift on the material's carrier population. *Skill:* microscopic law in comparative reasoning. *Difficulty:* MEDIUM–HARD.

---

## 14. CONTENT QUALITY REPORT

| Check | Status | Notes |
|---|---|---|
| No important source concept removed | ✅ | Free electrons/random motion, drift velocity, mobility & relaxation time, conventional vs. electron current, I = Q/t + Q = Ne, current density, I = nev_dA + J = nev_d, Ohm's law + potential-drop signs, emf/internal resistance + both load cases, resistivity/conductivity + geometric scaling, temperature law with slope R₀α, all three power forms, ΔU = IVt, kWh, and all seven source examples. |
| Mathematical formulas correct | ✅ | All formulas preserved exactly as given; all numeric results re-derived and matched (600 C, 3.8 × 10²¹, 5 Ω, 0.24 A, 3.4 × 10⁻⁶ m², 2.1 mm, 1.2 V, 3.6 Ω, 3600 W, 324 kWh, $34.02, 0.79 A, 120 Ω, 150 W, 276 Wh, $0.021). |
| Technical terminology preserved | ✅ | Free electrons, drift velocity, mobility, relaxation time, current density, conventional current, emf, internal resistance, terminal voltage, resistivity, conductivity, Siemens, temperature coefficient, kilowatt-hour. |
| Explanations in original language | ✅ | Fully rewritten; hose/wave, turnstile, theater-ticket, pump, city-traffic analogies all marked pedagogical. |
| Understandable to a first-year student | ✅ | Microscopic picture built stepwise; every example includes conversion and verification steps. |
| Difficult concepts explicitly identified | ✅ | 6 concepts with ratings; 2 rated HARD (drift velocity/I = nev_dA, emf & internal resistance) with full video plans and scripts. |
| Common misconceptions identified | ✅ | 10 mistakes with what/why/how, echoed in difficult-concept entries and both scripts. |
| Examples actually teach the concept | ✅ | All 7 source examples worked step-by-step; pedagogical additions (drift estimate, internal-resistance bridge from Example 2) clearly marked and built from source formulas/numbers. |
| Practice progresses understand → apply → transfer | ✅ | Level 1 (6), Level 2 (6), Level 3 (6) incl. stretched-wire, battery diagnosis, bulb comparison, model inversion; 11-question self-check without revealed answers. |
| No unsupported claims added | ✅ | Pedagogical numeric examples (drift estimates, starter-motor case, stretched wire) explicitly flagged; circuit topics beyond the source (resistor networks) not introduced; source typos transparently documented; course title marked [SOURCE DOES NOT SPECIFY]. |
| No large verbatim reproduction | ✅ | Structure, formulas, and numbers preserved; wording fully rewritten. |
| Suitable for direct web integration | ✅ | Clean Markdown; metadata; flow position; instructor keys separated from student-facing content. |

**ARETE placement note:** Deploy as the opening LEARN+PRACTICE lesson of the DC-circuits module, gated on Lecture 4 (potential difference). Attach Video 1 to the drift-velocity topic and Video 2 to the emf/internal-resistance topic. Enable REMEDIATE on mistakes 4, 5, and 6 (emf-as-loaded-voltage, wrong power form, diameter/unit slips) — the three highest-frequency failure modes. Q13–Q15 are strong PROVE-stage items; Q15 (battery diagnosis) is the single best TRANSFER item of the lecture — it forces the emf model into a real-world judgment.


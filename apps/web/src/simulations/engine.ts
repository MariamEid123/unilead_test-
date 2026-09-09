// Real-physics simulation core for the Physics 2 course.
//
// The Coulomb pair below integrates the equations of motion with RK4 using
// the true Coulomb force F = k_e |q1 q2| / r^2. Distances, forces, velocities
// and kinetic energy are computed in real SI units; the only non-physical
// knobs are the demonstration's release distance and the (adjustable) masses
// of the test spheres, which exist to make the motion match a human-watchable
// timescale without faking the force law.

export const COULOMB_K = 8.9875e9; // N·m²/C²

// Closest approach allowed. Real point charges have no such floor, but two
// oppositely-charged spheres that touch would transfer charge and neutralize,
// which stops the interaction — that is exactly what we report.
export const MIN_SEPARATION = 0.015; // m

export interface CoulombParams {
  q1C: number; // Coulomb, signed
  q2C: number; // Coulomb, signed
  r0M: number; // initial separation (m)
  mKG: number; // each sphere's mass (kg)
}

export interface CoulombFrame {
  t: number; // simulated time (s)
  x1: number; // position of charge 1 (m)
  x2: number; // position of charge 2 (m)
  v1: number; // velocity of charge 1 (m/s, signed)
  v2: number; // velocity of charge 2 (m/s, signed)
  r: number; // separation (m)
  fN: number; // force magnitude (N)
  keJ: number; // total kinetic energy (J)
  peJ: number; // electric potential energy k q1 q2 / r (J, signed)
  contacted: boolean;
}

export function coulombForce(newtonsPer: { q1C: number; q2C: number; rM: number }): number {
  const r = Math.max(Math.abs(newtonsPer.rM), 1e-6);
  return (COULOMB_K * Math.abs(newtonsPer.q1C * newtonsPer.q2C)) / (r * r);
}

// Derivative of [x1, v1, x2, v2] under Coulomb acceleration.
function derivatives(
  params: CoulombParams,
  x1: number,
  v1: number,
  x2: number,
  v2: number
): [number, number, number, number] {
  const r = Math.max(x2 - x1, MIN_SEPARATION);
  const f = coulombForce({ q1C: params.q1C, q2C: params.q2C, rM: r });
  // Like signs repel (spheres push apart), opposite signs attract.
  const apart = params.q1C * params.q2C > 0 ? 1 : -1;
  const a = f / params.mKG;
  return [v1, -apart * a, v2, apart * a];
}

export class CoulombPair {
  private p: CoulombParams;
  private _x1: number;
  private _v1: number;
  private _x2: number;
  private _v2: number;
  private _t: number;
  private _contacted: boolean;

  constructor(params: CoulombParams) {
    this.p = { ...params };
    this._x1 = -params.r0M / 2;
    this._v1 = 0;
    this._x2 = params.r0M / 2;
    this._v2 = 0;
    this._t = 0;
    this._contacted = false;
  }

  get params(): CoulombParams {
    return { ...this.p };
  }

  setParams(params: CoulombParams) {
    this.p = { ...params };
    this.reset();
  }

  reset() {
    this._x1 = -this.p.r0M / 2;
    this._v1 = 0;
    this._x2 = this.p.r0M / 2;
    this._v2 = 0;
    this._t = 0;
    this._contacted = false;
  }

  // Advance by dtSim seconds using fixed-size RK4 substeps so the 1/r²
  // singularity is approached with bounded per-step error.
  step(dtSim: number) {
    if (this._contacted) return;
    const SUB = 64;
    const h = dtSim / SUB;
    for (let i = 0; i < SUB; i += 1) {
      if (this.p.q1C * this.p.q2C < 0 && this._x2 - this._x1 <= MIN_SEPARATION) {
        this._contacted = true;
        this._v1 = 0;
        this._v2 = 0;
        return;
      }
      const [k1x1, k1v1, k1x2, k1v2] = derivatives(this.p, this._x1, this._v1, this._x2, this._v2);
      const [k2x1, k2v1, k2x2, k2v2] = derivatives(
        this.p,
        this._x1 + (h / 2) * k1x1,
        this._v1 + (h / 2) * k1v1,
        this._x2 + (h / 2) * k1x2,
        this._v2 + (h / 2) * k1v2
      );
      const [k3x1, k3v1, k3x2, k3v2] = derivatives(
        this.p,
        this._x1 + (h / 2) * k2x1,
        this._v1 + (h / 2) * k2v1,
        this._x2 + (h / 2) * k2x2,
        this._v2 + (h / 2) * k2v2
      );
      const [k4x1, k4v1, k4x2, k4v2] = derivatives(
        this.p,
        this._x1 + h * k3x1,
        this._v1 + h * k3v1,
        this._x2 + h * k3x2,
        this._v2 + h * k3v2
      );

      this._x1 += (h / 6) * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1);
      this._v1 += (h / 6) * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1);
      this._x2 += (h / 6) * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2);
      this._v2 += (h / 6) * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2);
      this._t += h;
    }
  }

  frame(): CoulombFrame {
    const r = Math.max(this._x2 - this._x1, MIN_SEPARATION);
    const f = coulombForce({ q1C: this.p.q1C, q2C: this.p.q2C, rM: r });
    return {
      t: this._t,
      x1: this._x1,
      x2: this._x2,
      v1: this._v1,
      v2: this._v2,
      r,
      fN: this._contacted ? 0 : f,
      keJ: 0.5 * this.p.mKG * (this._v1 * this._v1 + this._v2 * this._v2),
      peJ: (COULOMB_K * this.p.q1C * this.p.q2C) / r,
      contacted: this._contacted,
    };
  }

  // Fractional drift of total mechanical energy versus the release point —
  // a first-principles check that the integration conserves energy.
  conservationDrift(frame: CoulombFrame): number {
    const r0 = Math.max(this.p.r0M, MIN_SEPARATION);
    const pe0 = (COULOMB_K * this.p.q1C * this.p.q2C) / r0;
    const total = frame.keJ + frame.peJ;
    if (Math.abs(pe0) < 1e-12) return 0;
    return Math.abs(total - pe0) / Math.abs(pe0);
  }
}

// Simple helper for graph traces: keeps a capped series of samples.
export class Trace<T> {
  private buf: T[] = [];
  private cap: number;

  constructor(cap: number) {
    this.cap = cap;
  }

  push(value: T) {
    this.buf.push(value);
    if (this.buf.length > this.cap) this.buf.shift();
  }

  clear() {
    this.buf = [];
  }

  empty() {
    return this.buf.length === 0;
  }

  get(): T[] {
    return this.buf;
  }
}
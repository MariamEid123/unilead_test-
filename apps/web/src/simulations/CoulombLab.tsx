import { useEffect, useMemo, useRef, useState } from 'react';
import Button from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import { CoulombPair, type CoulombFrame, MIN_SEPARATION } from './engine';
import './CoulombLab.css';

// Wall-clock → simulation-time mapping. The physics is real; this only slows
// the replay so the motion stays readable on screen.
const TIME_SCALE = 0.05; // 1 wall second = 0.05 simulated seconds

const WORLD_HALF = 0.15; // m — how much of the rail the camera shows
const VIEW_W = 720;
const VIEW_H = 300;
const PX_PER_M = (VIEW_W - 90) / (WORLD_HALF * 2);

interface Preset {
  id: string;
  label: string;
  q1: number; // µC (signed)
  q2: number; // µC (signed)
}

const PRESETS: Preset[] = [
  { id: 'repel-equal', label: 'Repel (+,+)', q1: 2, q2: 2 },
  { id: 'repel-strong', label: 'Repel (+,+) strong', q1: 5, q2: 5 },
  { id: 'attract', label: 'Attract (+,-)', q1: 2, q2: -2 },
  { id: 'one-strong', label: 'One strong, one weak', q1: 6, q2: 1 },
];

function Slider({
  label,
  value,
  display,
  min,
  max,
  step,
  unit,
  onChange,
}: {
  label: string;
  value: number;
  display: string;
  min: number;
  max: number;
  step: number;
  unit: string;
  onChange: (v: number) => void;
}) {
  return (
    <label className="coulomb__slider">
      <span className="coulomb__slider-label">
        <strong>{label}</strong>
        <span className="coulomb__slider-value">
          {display} {unit}
        </span>
      </span>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
      />
    </label>
  );
}

function fmt(v: number, digits: number): string {
  if (!Number.isFinite(v)) return '—';
  return v.toFixed(digits);
}

export default function CoulombLab() {
  const [q1uC, setQ1uC] = useState(2);
  const [q2Mag, setQ2Mag] = useState(2);
  const [q2Neg, setQ2Neg] = useState(false);
  const [distCm, setDistCm] = useState(5);
  const [massG, setMassG] = useState(200);
  const [playing, setPlaying] = useState(false);

  const q2uC = q2Neg ? -q2Mag : q2Mag;

  const pairRef = useRef<CoulombPair | null>(null);
  const [frame, setFrame] = useState<CoulombFrame | null>(null);
  const [vTrace, setVTrace] = useState<{ t: number; v: number }[]>([]);

  if (pairRef.current === null) {
    pairRef.current = new CoulombPair({
      q1C: q1uC * 1e-6,
      q2C: q2uC * 1e-6,
      r0M: distCm * 0.01,
      mKG: massG * 1e-3,
    });
  }

  function resetTo(q1: number, q2: number, d: number, m: number) {
    setPlaying(false);
    setVTrace([]);
    const pair = new CoulombPair({
      q1C: q1 * 1e-6,
      q2C: q2 * 1e-6,
      r0M: d * 0.01,
      mKG: m * 1e-3,
    });
    pairRef.current = pair;
    setFrame(pair.frame());
  }

  function applyPreset(p: Preset) {
    setQ1uC(p.q1);
    setQ2Mag(Math.abs(p.q2));
    setQ2Neg(p.q2 < 0);
    setDistCm(5);
    setMassG(200);
    resetTo(p.q1, p.q2, 5, 200);
  }

  // Rebuild the pair whenever a parameter changes (classic "restart the
  // experiment" behaviour — the initial conditions are re-applied).
  useEffect(() => {
    resetTo(q1uC, q2uC, distCm, massG);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [q1uC, q2uC, distCm, massG]);

  useEffect(() => {
    if (!playing) return;
    let raf = 0;
    let last = performance.now();
    let skipped = 0;

    const loop = (now: number) => {
      const dtWall = Math.min((now - last) / 1000, 0.05);
      last = now;
      const pair = pairRef.current;
      if (pair && !pair.frame().contacted) {
        pair.step(dtWall * TIME_SCALE);
        const f = pair.frame();
        setFrame(f);
        if (skipped % 4 === 0) {
          setVTrace((prev) => [...prev.slice(-299), { t: f.t, v: Math.hypot(f.v1, f.v2) }]);
        }
        skipped += 1;
      } else {
        setPlaying(false);
      }
      raf = requestAnimationFrame(loop);
    };

    raf = requestAnimationFrame(loop);
    return () => cancelAnimationFrame(raf);
  }, [playing]);

  const paramsOpacity = playing ? 0.5 : 1;
  const f = frame;
  const drift = f && pairRef.current ? pairRef.current.conservationDrift(f) : null;

  const layout = (fr: CoulombFrame) => {
    const cx = VIEW_W / 2;
    return { p1x: cx + fr.x1 * PX_PER_M, p2x: cx + fr.x2 * PX_PER_M };
  };

  // --- F(r) theoretical curve + live dot ---
  const fGraph = useMemo(() => {
    const k = 8.9875e9;
    const q = Math.abs(q1uC * q2uC) * 1e-12;
    const rStart = Math.max(distCm * 0.01, MIN_SEPARATION);
    const rMax = 0.16;
    const fStart = (k * q) / (rStart * rStart);
    const yMax = Math.max(fStart * 1.6, 1);
    const x = (r: number) => 4 + ((r - MIN_SEPARATION) / (rMax - MIN_SEPARATION)) * 232;
    const y = (fN: number) => 174 - Math.min(fN / yMax, 1) * 150;
    const points: { x: number; y: number }[] = [];
    const N = 90;
    for (let i = 0; i <= N; i += 1) {
      const r = MIN_SEPARATION + ((rMax - MIN_SEPARATION) * i) / N;
      const fN = (k * q) / (r * r);
      points.push({ x: x(r), y: y(fN) });
    }
    const tickR = [0.03, 0.06, 0.09, 0.12, 0.15];
    return { points, x, y, yMax, tickR };
  }, [q1uC, q2uC, distCm]);

  const liveDot = f ? { r: Math.min(f.r, 0.16 + 1e-6), f: f.fN } : null;

  // --- v(t) graph ---
  const vGraph = useMemo(() => {
    if (vTrace.length < 2) return { line: '', maxT: 1, maxV: 1 };
    const maxT = Math.max(...vTrace.map((s) => s.t), 1);
    const maxV = Math.max(...vTrace.map((s) => s.v), 1);
    const pts = vTrace.map((s) => ({
      x: 4 + (s.t / maxT) * 232,
      y: 174 - Math.min(s.v / maxV, 1) * 150,
    }));
    const line = pts.map((p, i) => `${i === 0 ? 'M' : 'L'}${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(' ');
    return { line, maxT, maxV };
  }, [vTrace]);

  const sameSign = q1uC * q2uC > 0;

  return (
    <div className="coulomb">
      <div className="coulomb__presets" role="group" aria-label="Experiment presets">
        {PRESETS.map((p) => {
          const active = q1uC === p.q1 && q2uC === p.q2 && distCm === 5 && massG === 200;
          return (
            <Button key={p.id} size="sm" variant={active ? 'secondary' : 'ghost'} onClick={() => applyPreset(p)}>
              {p.label}
            </Button>
          );
        })}
      </div>

      <div className="coulomb__grid">
        <section className="coulomb__stage-card" aria-label="Charge dynamics stage">
          <div className="coulomb__stage-head">
            <span className="coulomb__stage-title">Free-body dynamics</span>
            <div className="coulomb__stage-actions">
              <Button size="sm" variant={playing ? 'secondary' : 'primary'} onClick={() => setPlaying((p) => !p)}>
                {playing ? 'Pause' : 'Release'}
              </Button>
              <Button size="sm" variant="ghost" onClick={() => resetTo(q1uC, q2uC, distCm, massG)}>
                Reset
              </Button>
            </div>
          </div>

          <svg className="coulomb__stage" viewBox={`0 0 ${VIEW_W} ${VIEW_H}`} role="img" aria-label="Two charges moving under the Coulomb force">
            <defs>
              <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
                <polygon points="0 0, 8 3, 0 6" fill="currentColor" />
              </marker>
            </defs>

            {/* rail */}
            <line x1="30" y1="150" x2={VIEW_W - 30} y2="150" stroke="currentColor" strokeOpacity="0.18" strokeWidth="2" />

            {/* ruler ticks every 2 cm */}
            {Array.from({ length: 15 }, (_, i) => -14 + i * 2).map((cm) => {
              const px = VIEW_W / 2 + (cm * 0.01) * PX_PER_M;
              const major = cm % 4 === 0;
              return (
                <g key={cm}>
                  <line x1={px} y1={major ? 143 : 146} x2={px} y2="154" stroke="currentColor" strokeOpacity="0.35" strokeWidth={major ? 1.4 : 1} />
                  {major && (
                    <text x={px} y="136" textAnchor="middle" fontSize="9" fill="currentColor" fillOpacity="0.45">
                      {cm === 0 ? '0' : `${cm}`}
                    </text>
                  )}
                </g>
              );
            })}
            <text x={VIEW_W / 2} y="168" textAnchor="middle" fontSize="9" fill="currentColor" fillOpacity="0.45">cm</text>

            {f && (() => {
              const { p1x, p2x } = layout(f);
              const dir = sameSign ? 1 : -1;
              const arrow = Math.max(18, Math.min(70, 20 + (f.fN / (f.fN + 8)) * 55));
              const d1 = dir * arrow;
              const d2 = -dir * arrow;
              return (
                <g>
                  {/* force label near midrail */}
                  <text x={(p1x + p2x) / 2} y="120" textAnchor="middle" fontSize="11" fontWeight="700" fill={q1uC > 0 ? 'var(--color-on-tint)' : 'currentColor'}>
                    |F| = {fmt(f.fN, 2)} N
                  </text>
                  <text x={(p1x + p2x) / 2} y="134" textAnchor="middle" fontSize="10" fill="currentColor" fillOpacity="0.55">
                    r = {fmt(f.r * 100, 1)} cm
                  </text>

                  {/* force arrows */}
                  <g stroke="var(--color-accent)" strokeWidth="2.6" fill="none">
                    <line x1={p1x} y1="112" x2={p1x - d1} y2="112" markerEnd="url(#arrowhead)" />
                    <line x1={p2x} y1="112" x2={p2x - d2} y2="112" markerEnd="url(#arrowhead)" />
                  </g>

                  {/* charges */}
                  <g>
                    <circle cx={p1x} cy="150" r="16" fill={q1uC >= 0 ? 'var(--color-primary)' : 'var(--color-navy)'} />
                    <text x={p1x} y="154" textAnchor="middle" fontSize="14" fontWeight="700" fill="#fff">{q1uC >= 0 ? '+' : '−'}</text>
                    <text x={p1x} y="184" textAnchor="middle" fontSize="10" fill="currentColor" fillOpacity="0.6">{fmt(q1uC, 1)} µC</text>
                  </g>
                  <g>
                    <circle cx={p2x} cy="150" r="16" fill={q2uC >= 0 ? 'var(--color-primary)' : 'var(--color-navy)'} />
                    <text x={p2x} y="154" textAnchor="middle" fontSize="14" fontWeight="700" fill="#fff">{q2uC >= 0 ? '+' : '−'}</text>
                    <text x={p2x} y="184" textAnchor="middle" fontSize="10" fill="currentColor" fillOpacity="0.6">{fmt(q2uC, 1)} µC</text>
                  </g>

                  {f.contacted && (
                    <text x={VIEW_W / 2} y="240" textAnchor="middle" fontSize="13" fontWeight="700" fill="var(--color-danger)">
                      Contact! The spheres touched and neutralized — the interaction stopped.
                    </text>
                  )}
                </g>
              );
            })()}

            {!f && (
              <text x={VIEW_W / 2} y="156" textAnchor="middle" fontSize="12" fill="currentColor" fillOpacity="0.4">Press Release to run the experiment</text>
            )}
          </svg>

          {f && (
            <div className="coulomb__metrics">
              {[
                { label: 'Separation', value: `${fmt(f.r * 100, 2)} cm` },
                { label: 'Force', value: `${fmt(f.fN, 3)} N` },
                { label: 'Speed', value: `${fmt(Math.hypot(f.v1, f.v2), 2)} m/s` },
                { label: 'Kinetic energy', value: `${fmt(f.keJ, 4)} J` },
                { label: 'Sim time', value: `${fmt(f.t, 3)} s` },
              ].map((m) => (
                <div className="coulomb__metric" key={m.label}>
                  <span>{m.label}</span>
                  <strong>{m.value}</strong>
                </div>
              ))}
              {drift !== null && (
                <div className="coulomb__metric">
                  <span>Energy check</span>
                  <Badge tone={drift < 0.001 ? 'success' : 'warning'}>
                    {drift < 0.001 ? 'conserved ✓' : 'drift'}
                  </Badge>
                </div>
              )}
            </div>
          )}
        </section>

        <section className="coulomb__controls" aria-label="Experiment parameters" style={{ opacity: paramsOpacity }}>
          <span className="coulomb__controls-title">Parameters</span>
          <Slider label="Charge 1" value={q1uC} display={q1uC.toFixed(1)} min={0.5} max={10} step={0.5} unit="µC" onChange={setQ1uC} />
          <Slider label="Charge 2 (magnitude)" value={q2Mag} display={q2Mag.toFixed(1)} min={0.5} max={10} step={0.5} unit="µC" onChange={setQ2Mag} />
          <div className="coulomb__sign-toggle">
            <span className="coulomb__sign-label">Charge 2 sign</span>
            <div className="coulomb__sign-buttons">
              <Button size="sm" variant={!q2Neg ? 'secondary' : 'ghost'} onClick={() => setQ2Neg(false)} disabled={playing}>
                Positive (+)
              </Button>
              <Button size="sm" variant={q2Neg ? 'secondary' : 'ghost'} onClick={() => setQ2Neg(true)} disabled={playing}>
                Negative (−)
              </Button>
            </div>
          </div>
          <Slider label="Separation at release" value={distCm} display={distCm.toFixed(1)} min={2} max={20} step={0.5} unit="cm" onChange={setDistCm} />
          <Slider label="Sphere mass" value={massG} display={String(massG)} min={10} max={500} step={5} unit="g" onChange={setMassG} />
          <p className="coulomb__params-note muted">
            Changing a parameter restarts the experiment with the new initial conditions. The force law is
            always F&nbsp;=&nbsp;k·|q₁q₂|/r² with k&nbsp;=&nbsp;8.99×10⁹ N·m²/C².
          </p>
        </section>
      </div>

      {f && (
        <div className="coulomb__graphs">
          <section className="coulomb__graph-card" aria-label="Force versus separation graph">
            <span className="coulomb__stage-title">Force vs separation — the true 1/r² curve</span>
            <svg viewBox="0 0 240 190" className="coulomb__graph" role="img" aria-label="Force versus separation">
              <g stroke="currentColor" strokeOpacity="0.15" strokeWidth="1">
                {[0.5, 1, 1.5].map((f) => <line key={f} x1="4" y1={174 - (f / 1.5) * 150} x2="236" y2={174 - (f / 1.5) * 150} />)}
                {fGraph.tickR.map((r) => <line key={r} x1={fGraph.x(r)} y1="174" x2={fGraph.x(r)} y2="190" />)}
              </g>
              <polyline
                points={fGraph.points.map((p) => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(' ')}
                fill="none"
                stroke="var(--color-accent)"
                strokeWidth="2"
              />
              {liveDot && (
                <g>
                  <line x1={fGraph.x(liveDot.r)} y1="174" x2={fGraph.x(liveDot.r)} y2={fGraph.y(0)} stroke="var(--color-primary)" strokeDasharray="3 3" strokeWidth="1.4" />
                  <circle cx={fGraph.x(liveDot.r)} cy={fGraph.y(liveDot.f)} r="4" fill="var(--color-primary)" />
                </g>
              )}
              <text x="4" y="14" fontSize="9" fill="currentColor" fillOpacity="0.6">F (N, clipped at {fmt(fGraph.yMax, 1)})</text>
              <text x="120" y="188" textAnchor="middle" fontSize="9" fill="currentColor" fillOpacity="0.6">r (m) →</text>
              {fGraph.tickR.map((r) => (
                <text key={r} x={fGraph.x(r)} y="186" textAnchor="middle" fontSize="8" fill="currentColor" fillOpacity="0.6">{r.toFixed(2)}</text>
              ))}
            </svg>
            <p className="coulomb__graph-note muted">
              The orange curve is the exact theoretical F = k·q₁q₂/r² for your charges; the live dot rides the
              curve because the dynamics integrate the same law.
            </p>
          </section>

          <section className="coulomb__graph-card" aria-label="Speed over time graph">
            <span className="coulomb__stage-title">Speed vs time</span>
            {vGraph.line ? (
              <svg viewBox="0 0 240 190" className="coulomb__graph" role="img" aria-label="Speed against time">
                <g stroke="currentColor" strokeOpacity="0.15" strokeWidth="1">
                  {[0.5, 1, 1.5].map((s) => <line key={s} x1="4" y1={174 - (s / 1.5) * 150} x2="236" y2={174 - (s / 1.5) * 150} />)}
                </g>
                <path d={vGraph.line} fill="none" stroke="var(--color-primary)" strokeWidth="2" />
                {f && (
                  <circle
                    cx={4 + Math.min(f.t / vGraph.maxT, 1) * 232}
                    cy={174 - Math.min(Math.hypot(f.v1, f.v2) / vGraph.maxV, 1) * 150}
                    r="4"
                    fill="var(--color-primary)"
                  />
                )}
                <text x="4" y="14" fontSize="9" fill="currentColor" fillOpacity="0.6">|v| (m/s)</text>
                <text x="120" y="188" textAnchor="middle" fontSize="9" fill="currentColor" fillOpacity="0.6">t (s) →</text>
              </svg>
            ) : (
              <p className="muted">Run the experiment to trace speed over time.</p>
            )}
            <p className="coulomb__graph-note muted">
              {sameSign
                ? 'Like charges decelerate as they separate (1/r² fades) — speed keeps growing, but more and more slowly.'
                : 'Opposite charges accelerate toward each other; the force and speed climb without bound until contact.'}
            </p>
          </section>
        </div>
      )}

      <section className="coulomb__analysis" aria-label="What to look for">
        <span className="coulomb__stage-title">Check your understanding</span>
        <ul className="coulomb__analysis-list">
          {[
            {
              q: 'How does the force change when you double both charges (2 µC → 4 µC) at the same separation?',
              a: 'Each charge doubles, so the product q₁q₂ quadruples — the force becomes 4× larger. Compare the presets and read the |F| readout at equal distances.',
            },
            {
              q: 'At the same charges, how does the force change when the spheres move from 6 cm to 3 cm apart?',
              a: 'Separation halves, so 1/r² quadruples — the force is 4× stronger. This steep climb as r shrinks is the inverse-square law; watch the F–r curve.',
            },
            {
              q: 'Why do opposite charges keep speeding up, while like charges barely accelerate once far apart?',
              a: 'For like charges the force shrinks as 1/r² as they separate, so acceleration collapses. For opposite charges r keeps falling, 1/r² keeps growing, and so does the force — right up to contact.',
            },
            {
              q: 'What does the energy-check badge tell you?',
              a: 'It compares KE + electric PE against the PE at release. It stays ≈ constant because the simulation integrates the true equations of motion with RK4 — the badge reports the numerical drift, not a made-up result.',
            },
          ].map((item, i) => (
            <li key={i}>
              <p className="coulomb__analysis-q"><strong>{item.q}</strong></p>
              <details className="coulomb__analysis-reveal">
                <summary>Reveal reasoning</summary>
                <p className="muted">{item.a}</p>
              </details>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
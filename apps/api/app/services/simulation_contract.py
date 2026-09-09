"""Sprint 7A/7B/7C — the deterministic PID simulation contract.

This module is the *single agreed contract* between the UI, the coach, and
the evidence pipeline:

* **Task presets (7A)** — each ``task_id`` maps to one competency with fixed,
  deterministic plant/solver parameters. Same task + same gains ⇒ identical
  telemetry, every run, on every machine.
* **PID simulation (7B)** — a discrete PID controller driving a second-order
  plant (RK4), provided by the AI Education simulation core. Compass never
  re-implements the integrator; it pins the operational constants here.
* **Telemetry & metrics (7C)** — the closed-loop trace is reduced to the
  exact rubric metric keys the Mastery Engine evaluates
  (``overshoot``, ``settling_time``, ``rise_time``, ``steady_state_error``,
  ``stable``), so a simulation run is directly comparable to an assessment
  attempt.

Proven (deterministic) gain sets for the ``pid-001`` plant
(``wn=8.0, zeta=0.3``, step to 1.0, dt=0.01, 4s horizon) against the MEC271
mastery rubric (OS ≤ 10 %, ST ≤ 2.0 s, SSE ≤ 0.01, stable):
``SIM_FAILING_GAINS`` fails, ``SIM_PASSING_GAINS`` passes.

The rubric itself is pinned below (``RUBRIC_CRITERIA``) and seeded into the
DB by the legacy simulation footing in ``db/bootstrap`` — the module is the
only source of truth for *passing*; it also pre-computes known gain
combinations so tests and the demo reflect a real, stable curriculum.
"""

from __future__ import annotations

from dataclasses import dataclass

# MEC271 mastery rubric metric keys (must match the DB rubric metric_field).
METRIC_KEYS = ("overshoot", "settling_time", "rise_time", "steady_state_error", "stable")

# The MEC271 PID mastery rubric — retained as the historical instrument the
# reusable simulation engine resolves. The bootstrap legacy footing seeds
# exactly these criteria into the DB.
RUBRIC_CRITERIA = [
    {"metric_field": "overshoot", "operator": "<=", "threshold": 10.0, "mandatory": True},
    {"metric_field": "settling_time", "operator": "<=", "threshold": 2.0, "mandatory": True},
    {
        "metric_field": "steady_state_error",
        "operator": "<=",
        "threshold": 0.01,
        "mandatory": True,
    },
    {"metric_field": "stable", "operator": "is_true", "threshold": None, "mandatory": True},
]


@dataclass(frozen=True)
class PIDTask:
    """All parameters of one deterministic PID simulation task (7A)."""

    task_id: str
    competency_code: str
    plant_natural_frequency: float
    plant_damping_ratio: float
    setpoint: float
    dt: float
    duration: float


# The pid-001 arm tune (MEC271 → pid-tuning). Plant is deliberately
# under-damped so students must trade Kp/Ki/Kd instead of fluking a pass.
SIMULATION_TASKS: dict[str, PIDTask] = {
    "pid-001": PIDTask(
        task_id="pid-001",
        competency_code="pid-tuning",
        plant_natural_frequency=8.0,
        plant_damping_ratio=0.3,
        setpoint=1.0,
        dt=0.01,
        duration=4.0,
    ),
}


def get_task(task_id: str) -> PIDTask:
    """Resolve a task id to its preset (raises KeyError when unknown)."""
    return SIMULATION_TASKS[task_id]


def simulate_gains(task_id: str, *, kp: float, ki: float, kd: float) -> dict:
    """Run the deterministic closed-loop step response (7B) → 7C metrics.

    Returns a plain dict with exactly ``METRIC_KEYS``. Deterministic: same
    task + same gains ⇒ bit-identical values. Never raises for numeric
    inputs; unstable/divergent gains simply report their trace's metrics.
    """
    from ai_education.domain.evidence import PIDParameters
    from ai_education.simulation.engine import PIDSimulationEngine
    from ai_education.simulation.plant import SecondOrderPlant

    task = get_task(task_id)
    plant = SecondOrderPlant(
        natural_frequency=task.plant_natural_frequency,
        damping_ratio=task.plant_damping_ratio,
    )
    engine = PIDSimulationEngine()
    telemetry = engine.simulate_step(
        PIDParameters(kp=kp, ki=ki, kd=kd),
        plant=plant,
        setpoint=task.setpoint,
        dt=task.dt,
        duration=task.duration,
    )
    return metrics_from_telemetry(telemetry)


def metrics_from_telemetry(telemetry) -> dict:
    """Translate a StepResponseTelemetry into rubric-aligned metric keys (7C)."""

    return {
        "overshoot": telemetry.overshoot_pct,
        "settling_time": telemetry.settling_time_sec,
        "rise_time": telemetry.rise_time_sec,
        "steady_state_error": telemetry.steady_state_error,
        "stable": telemetry.is_stable,
    }


# Deterministic reference gain sets for tests and the demo script.
SIM_FAILING_GAINS: dict[str, float] = {"kp": 2.0, "ki": 0.5, "kd": 0.1}
SIM_PASSING_GAINS: dict[str, float] = {"kp": 5.0, "ki": 4.0, "kd": 1.0}

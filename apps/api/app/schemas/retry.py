"""Schemas for the Sprint 4E retry endpoint.

The retry is a *fresh assessment attempt* — the client supplies the metrics
of the new run (the same deterministic, objective metrics the rubric reads:
overshoot, settling_time, steady_state_error, stable). The endpoint then
records a new EvidenceRecord and lets the Mastery Engine decide the level.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RetryRequest(BaseModel):
    """Objective metrics of the retry run for one competency.

    These mirror the rubric metric fields so the deterministic evaluator can
    read them directly (``evaluate_criterion(metric_field, metrics)``).
    """

    overshoot: float = Field(..., ge=0.0, le=100.0, description="Percent overshoot.")
    settling_time: float = Field(..., ge=0.0, le=60.0, description="Settling time (seconds).")
    steady_state_error: float = Field(
        ..., ge=0.0, le=1.0, description="Steady-state error (absolute)."
    )
    stable: bool = Field(True, description="Whether the response is stable.")
    rise_time: float | None = Field(
        default=None, ge=0.0, le=60.0, description="Rise time (seconds)."
    )
    kp: float | None = Field(default=None, description="Kp used in this attempt (context).")
    ki: float | None = Field(default=None, description="Ki used in this attempt (context).")
    kd: float | None = Field(default=None, description="Kd used in this attempt (context).")

    def metric_dict(self) -> dict:
        """Metrics exactly as the rubric expects (omits context-only fields)."""
        return {
            "overshoot": self.overshoot,
            "settling_time": self.settling_time,
            "steady_state_error": self.steady_state_error,
            "stable": self.stable,
        }


class RetryResponse(BaseModel):
    """Outcome of one retry submission."""

    attempt_number: int = Field(..., description="New attempt number for this assessment.")
    attempt_id: int = Field(..., description="PK of the new AssessmentAttempt.")
    evidence_id: int = Field(..., description="PK of the new (immutable) EvidenceRecord.")
    passed: bool = Field(..., description="All rubric criteria passed this attempt.")
    passed_count: int = Field(..., description="How many rubric criteria passed.")
    total: int = Field(..., description="Total rubric criteria.")
    level: str = Field(..., description="Resolved mastery level from the engine.")
    reason_codes: list[str] = Field(
        default_factory=list, description="Failed criteria / reason codes (empty when passed)."
    )
    remediation_plan_id: int | None = Field(
        default=None, description="Open remediation plan created, if mastery not achieved."
    )


class RetryReviewRequest(BaseModel):
    """Instructor reviews a student's retry (also routed via Mastery Engine)."""

    competency_code: str = Field(
        ..., max_length=64, description="Durable competency code (e.g. pid-tuning)."
    )
    overshoot: float = Field(..., ge=0.0, le=100.0)
    settling_time: float = Field(..., ge=0.0, le=60.0)
    steady_state_error: float = Field(..., ge=0.0, le=1.0)
    stable: bool = Field(True)

    def metric_dict(self) -> dict:
        return {
            "overshoot": self.overshoot,
            "settling_time": self.settling_time,
            "steady_state_error": self.steady_state_error,
            "stable": self.stable,
        }

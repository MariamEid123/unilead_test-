"""Schemas for the Sprint 5 Student Model + adaptive endpoints.

These mirror the deterministic dicts produced by the services; FastAPI
validates them before they reach the client so the API contract stays tight.
All numbers are computed (never guessed by an LLM), so the schema carries
the confidence contract verbatim.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class CompetencyProfile(BaseModel):
    """One competency's derived state in the Sprint 5 Student Model."""

    competency_code: str
    competency_title: str
    competency_id: int
    mastery_level: str = Field(..., description="NOT_DEMONSTRATED / DEVELOPING / DEMONSTRATED.")
    confidence: float = Field(
        ...,
        description=(
            "Recency-weighted pass ratio over evidence, newest first: "
            "Σ λ^i·pass_i / Σ λ^i with λ=0.75. In [0,1], 0 when no evidence."
        ),
    )
    attempt_count: int
    evidence_count: int
    weak_criteria: list[str] = Field(
        ..., description="Rubric metrics that failed in the most recent non-passing evidence."
    )
    misconceptions: list[str] = Field(
        ..., description="Misconception tags by frequency, most common first."
    )
    remediation_open_count: int
    remediation_completed_count: int
    open_plan_id: int | None = None
    prerequisite_codes: list[str] = Field(
        ..., description="Competency codes that must come before this one."
    )
    prerequisites_satisfied: bool
    last_evidence_at: str | None = None
    # Sprint 8B — every mastery claim is stamped with the evidence lineage
    # that supports it: the EvidenceRecord ids behind the claim, a count of
    # the sources that produced them, and the ids whose verdict reached
    # DEMONSTRATED.
    evidence_ids: list[int] = Field(
        default_factory=list,
        description="EvidenceRecord ids for (student, competency), oldest first.",
    )
    evidence_sources: dict[str, int] = Field(
        default_factory=dict,
        description="Evidence source_type -> count for this competency.",
    )
    proven_evidence_ids: list[int] = Field(
        default_factory=list,
        description="EvidenceRecord ids whose deterministic verdict is DEMONSTRATED.",
    )


class EvidenceLineageRecord(BaseModel):
    """One immutable EvidenceRecord as told by the narrative (Sprint 8A)."""

    evidence_id: int
    source_type: str
    source_ref_id: int | None = None
    verdict_level: str = Field(..., description="Level this evidence alone achieves.")
    passed_criteria: list[str] = Field(..., description="Mandatory rubric criteria passed.")
    created_at: str | None = None


class CompetencyNarrative(BaseModel):
    """The evidence story for one competency (Sprint 8A)."""

    proven_criteria: list[str] = Field(
        ..., description="Mandatory rubric criteria the latest evidence passed."
    )
    unproven_criteria: list[str] = Field(
        ..., description="Mandatory rubric criteria still failing — the current gap."
    )
    misconception_tags: list[str] = Field(..., description="Deterministic misconception tags.")
    evidence_lineage: list[EvidenceLineageRecord] = Field(
        ..., description="One entry per EvidenceRecord, oldest first."
    )


class EvidenceNarrative(BaseModel):
    """The Sprint 8A Evidence Narrative read model for one student + course."""

    student_id: str
    course_code: str | None = None
    total_evidence: int = Field(..., description="Total EvidenceRecord rows for the student.")
    evidence_counts_by_source: dict[str, int] = Field(
        ..., description="source_type -> evidence count."
    )
    competencies: dict[str, CompetencyNarrative]


class StudentModelResponse(BaseModel):
    """The full derived model for one student in one course."""

    student_id: str
    course_code: str
    course_title: str
    generated_at: str = Field(..., description="RFC3339 UTC timestamp.")
    total_competencies: int
    attempted_count: int
    demonstrated_count: int
    overall_confidence: float
    competencies: dict[str, CompetencyProfile]
    # Sprint 8A — the evidence narrative derived from evidence_records only.
    evidence_narrative: EvidenceNarrative


class NextStepResource(BaseModel):
    """One remediation-catalog resource matched to the student's state."""

    resource_code: str
    title: str
    kind: str
    body: str
    score: int


class NextStep(BaseModel):
    """One prioritized adaptive intervention."""

    priority: int = Field(..., description="1 = highest. Consistent with the 5C ladder.")
    action: str = Field(
        ...,
        description=(
            "complete_remediation / unlock_prerequisite / practice / revalidate / advance / start."
        ),
    )
    reason: str
    competency_code: str
    competency_title: str
    plan_id: int | None = None
    confidence: float | None = None
    missing_prerequisites: list[str] = []
    weak_criteria: list[str] = []
    misconceptions: list[str] = []
    resources: list[NextStepResource] = []


class LearningPathStep(BaseModel):
    """One competency on the ordered path to a target."""

    competency_code: str
    competency_title: str
    mastery_level: str
    confidence: float
    evidence_count: int
    status: str = Field(..., description="ready / locked / in_progress / not_started.")
    locked: bool
    blocked_by: list[str]


class EarliestNextStep(BaseModel):
    """The first not-yet-demonstrated competency on a learning path (8D)."""

    competency_code: str
    competency_title: str
    status: str = Field(..., description="ready / locked / in_progress / not_started.")
    blocked_by: list[str] = Field(
        ..., description="Prerequisite codes not yet demonstrated (none when not locked)."
    )
    evidence_count: int
    confidence: float
    reason: str = Field(..., description="blocked_by_prerequisites / not_demonstrated.")


class LearningPathResponse(BaseModel):
    """The ordered prerequisite-aware path to a target competency."""

    course_code: str | None
    target: str
    status: str = Field(..., description="ready / blocked / in_progress / not_started.")
    total_steps: int
    blockers: list[str]
    path: list[LearningPathStep]
    # Sprint 8D — every next step must be explainable from the evidence.
    earliest_next_step: EarliestNextStep | None


class ReadinessBlocked(BaseModel):
    """Why one competency blocks transfer."""

    competency_code: str
    reason: str


class TransferReadinessResponse(BaseModel):
    """Gate result for transferring/advancing from a course."""

    course_code: str | None
    ready: bool
    progress: str = Field(..., description='"demonstrated/total", e.g. "3/5".')
    required_competencies: list[str]
    blocked_competencies: list[ReadinessBlocked]
    confidence_threshold: float

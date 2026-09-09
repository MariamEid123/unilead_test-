"""PID simulation router — runs a real simulation for the current student.

The run routes through the deterministic evidence pipeline (attempt ->
rubric -> evidence -> mastery -> plan) inside ``simulation_service``.
"""

import logging

from fastapi import APIRouter, Depends

from ..auth.dependencies import get_current_student
from ..db.models import Student
from ..schemas.simulation import SimulationRequest, SimulationResult
from ..services import simulation_service

router = APIRouter(prefix="/api/simulation", tags=["simulation"])
_log = logging.getLogger("arete.simulation")


@router.post("", response_model=SimulationResult)
def run_simulation(
    request: SimulationRequest,
    current_student: Student = Depends(get_current_student),
) -> dict:
    """Run a PID simulation with the given gains and record the evidence
    for the current student.
    """
    _log.info(
        "simulation for student=%s kp=%.3f ki=%.3f kd=%.3f",
        current_student.student_id,
        request.kp,
        request.ki,
        request.kd,
    )
    return simulation_service.run_simulation(request, current_student.student_id)

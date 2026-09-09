"""Safe code executor for the ARETE coding lab.

The lab RUN / SUBMIT buttons must genuinely execute the student's program —
never fake a result. This module runs Python 3 in a small sandbox aimed at
**didactic safety**, not full OS isolation:

  * a throwaway working directory per run (no writes land in the repo),
  * ``python -I`` (isolated mode = no user site-packages, no ``PYTHONPATH``),
  * a minimal subprocess environment (no secrets, no project state),
  * hard caps on source length, stdin length, wall-clock time and output,
  * the process group is force-killed on timeout.

Boundaries are intentionally documented: on a shared/multi-tenant host the
executor must sit behind a container / VM per run — the platform documents
this for production (see ``docs/``). For the local demo this layer is an
appropriate, honest execution boundary and never pretends a run succeeded.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass

MAX_SOURCE_CHARS = 40_000
MAX_STDIN_CHARS = 2_048
MAX_OUTPUT_CHARS = 16_000
TIMEOUT_SECONDS = 4.0
WINDOWS = os.name == "nt"


@dataclass
class ExecResult:
    """Outcome of one sandboxed execution."""

    status: str  # ok | compile_error | runtime_error | timeout | rejected | internal_error
    stdout: str = ""
    stderr: str = ""
    exit_code: int | None = None
    duration_ms: int = 0
    detail: str = ""


def _truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + "\n… [output truncated]"


def execute_python(source: str, stdin: str = "") -> ExecResult:
    """Run ``source`` as a Python program, feeding ``stdin`` to ``input()``.

    Returns an ``ExecResult``. A syntax problem is reported as
    ``compile_error``; anything that raises while being executed as
    ``runtime_error``; hitting the wall-clock limit as ``timeout``.
    """
    if not source or not source.strip():
        return ExecResult(status="rejected", detail="Your program is empty — write some code first.")
    if len(source) > MAX_SOURCE_CHARS:
        return ExecResult(status="rejected", detail="Source code too large.")
    if len(stdin) > MAX_STDIN_CHARS:
        return ExecResult(status="rejected", detail="Input too large.")

    try:
        temp_dir = tempfile.TemporaryDirectory(prefix="arete-lab-")
    except OSError as exc:
        return ExecResult(status="internal_error", detail=str(exc))

    with temp_dir:
        work_dir = pathlib.Path(temp_dir.name)
        script_path = work_dir / "main.py"
        script_path.write_text(source, encoding="utf-8")

        cmd = [sys.executable, "-I", "-B", "-u", str(script_path)]
        run_env = {
            "PATH": os.environ.get("PATH", ""),
            "TEMP": temp_dir.name,
            "TMP": temp_dir.name,
            "SystemRoot": os.environ.get("SystemRoot", r"C:\Windows"),
            "SystemDrive": os.environ.get("SystemDrive", "C:"),
            "PYTHONUTF8": "1",
        }
        if not WINDOWS:
            run_env["HOME"] = temp_dir.name

        start = time.perf_counter()
        try:
            proc = subprocess.run(
                cmd,
                input=stdin,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                cwd=temp_dir.name,
                env=run_env,
            )
            duration_ms = int((time.perf_counter() - start) * 1000)
        except subprocess.TimeoutExpired:
            return ExecResult(
                status="timeout",
                duration_ms=int((time.perf_counter() - start) * 1000),
                detail=f"Your program ran for more than {TIMEOUT_SECONDS:.0f}s and was stopped. "
                "Check for an infinite loop (a loop whose condition never becomes false).",
            )
        except OSError as exc:
            return ExecResult(status="internal_error", duration_ms=0, detail=str(exc))

    stdout = _truncate(proc.stdout or "")
    stderr = _truncate(proc.stderr or "")
    status = _classify_status(proc.returncode, stdout, stderr)
    return ExecResult(
        status=status,
        stdout=stdout,
        stderr=stderr,
        exit_code=proc.returncode,
        duration_ms=duration_ms,
    )


def _classify_status(exit_code: int, stdout: str, stderr: str) -> str:
    if exit_code != 0:
        lowered = stderr.lower()
        if "syntaxerror" in lowered or "indentationerror" in lowered:
            return "compile_error"
        if "traceback" in lowered:
            return "runtime_error"
        return "runtime_error"
    return "ok"


def runtime_label() -> str:
    """Human label of the interpreter the lab executes against."""
    if hasattr(sys, "implementation"):
        return f"Python {sys.implementation.name} {sys.version_info.major}.{sys.version_info.minor}"
    return f"Python {sys.version.split()[0]}"
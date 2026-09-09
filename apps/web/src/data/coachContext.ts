// Adaptive context pack for the AI Coach.
//
// On every coach interaction the UI assembles the learning context the coach
// is working with — focus, earliest_next_step, competency, evidence and
// misconception — from REAL student data (never invented). The pack is sent
// with each turn so the wire protocol carries it explicitly; the engine's
// authoritative facts remain the backend CoachContext.

import type {
  Competency,
  CoachContextPack,
  CompetencyStatus,
  DiagnosticResult,
  Student,
} from '../types';
import { getContinueLesson } from '../components/home/continueAction';

const STATUS_LABELS: Record<CompetencyStatus, string> = {
  NOT_STARTED: 'Not started',
  NEEDS_PRACTICE: 'Needs practice',
  DEVELOPING: 'In progress',
  DEMONSTRATED: 'Demonstrated',
};

// The competency the student should focus on right now: weakest first.
export function pickFocusCompetency(student: Student | null): Competency | null {
  if (!student) return null;
  const priority: CompetencyStatus[] = ['NEEDS_PRACTICE', 'DEVELOPING'];
  return (
    student.competencies.find((c) => priority.includes(c.status)) ??
    student.competencies[0] ??
    null
  );
}

function buildNextStep(student: Student | null): string | null {
  const lesson = getContinueLesson(student);
  if (!lesson) return null;
  if (lesson.nextLessonTitle) {
    return `${lesson.courseTitle} — ${lesson.nextLessonTitle}`;
  }
  return lesson.courseTitle;
}

function buildEvidenceLines(
  student: Student | null,
  competency: Competency | null,
  diagnosticResults: DiagnosticResult[] | null
): string[] {
  const lines: string[] = [];
  if (competency) {
    lines.push(
      `${competency.name}: ${STATUS_LABELS[competency.status] ?? competency.status} (${competency.progress}% mastery)`
    );
  }
  const active = student?.courseProgress.find((p) => p.courseId === student.course.id);
  if (active) {
    const done = active.completedLectures ?? 0;
    const total = active.totalLectures ?? 0;
    lines.push(`${done} of ${total} lessons completed in ${active.courseTitle}`);
  }
  const diag = diagnosticResults?.find((r) => r.competencyId === competency?.id);
  if (diag) {
    lines.push(`Diagnostic accuracy: ${diag.accuracy}%`);
    for (const misconception of diag.misconceptions ?? []) {
      lines.push(`Misconception detected: ${misconception.replace(/_/g, ' ')}`);
    }
  }
  return lines;
}

function buildMisconception(
  competency: Competency | null,
  diagnosticResults: DiagnosticResult[] | null
): string | null {
  const prior = diagnosticResults?.find((r) => r.competencyId === competency?.id);
  const raw = prior?.misconceptions?.[0] ?? null;
  if (raw) return raw;
  if (competency?.status === 'NEEDS_PRACTICE') return `recent attempts in ${competency.name}`;
  return null;
}

export function buildCoachContext(
  student: Student | null,
  diagnosticResults: DiagnosticResult[] | null
): CoachContextPack {
  const competency = pickFocusCompetency(student);
  return {
    focus: competency?.name ?? 'your learning path',
    earliestNextStep: buildNextStep(student),
    competency: competency
      ? {
          id: competency.id,
          name: competency.name,
          status: competency.status,
          progress: competency.progress,
        }
      : {
          id: student?.course.id ?? '',
          name: student?.course.title ?? 'Your courses',
          status: 'NOT_STARTED',
          progress: 0,
        },
    evidence: buildEvidenceLines(student, competency, diagnosticResults),
    misconception: buildMisconception(competency, diagnosticResults),
  };
}
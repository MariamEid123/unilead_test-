import type { JourneyFlags, Student } from '../../types';
import { getActiveCourseProgress } from '../../data/courses';

export const JOURNEY_STAGES = [
  { number: '01', label: 'Diagnostic', description: 'Find your starting point.', href: '/my-learning/diagnostic' },
  { number: '02', label: 'Courses', description: 'Choose a course and build the core idea.', href: '/courses' },
  { number: '03', label: 'Coach', description: 'Work through the hard part.', href: '/my-learning/ai-coach' },
  { number: '04', label: 'Practice', description: 'Apply it with feedback.', href: '/my-learning/practice' },
  { number: '05', label: 'Apply', description: 'Test it in a new context.', href: '/apply-review/simulation' },
  { number: '06', label: 'Demonstrate', description: 'Show what you can do.', href: '/apply-review/review' },
] as const;

export type JourneyStageStatus = 'completed' | 'current' | 'upcoming';

export interface JourneyStage {
  number: string;
  label: string;
  description: string;
  href: string;
  status: JourneyStageStatus;
}

// Derives each learning stage's state from the student's *real* progress
// (backend lesson/practice activity) combined with the in-session journey
// flags. `current` is always the first stage that isn't done yet.
export function buildJourneyStages(
  student: Student | null,
  journey: JourneyFlags
): JourneyStage[] {
  const active = getActiveCourseProgress(student);
  const lessonsDone = (active?.completedLectures ?? 0) > 0;
  const quizzesDone = (active?.completedQuizzes ?? 0) > 0;

  const done = [
    journey.hasCompletedDiagnostic || lessonsDone || quizzesDone,
    lessonsDone,
    journey.hasCompletedPractice,
    journey.hasCompletedPractice || quizzesDone,
    journey.hasCompletedSimulation,
    journey.hasCompletedReview,
  ];

  const currentIndex = done.findIndex((isDone) => !isDone);

  return JOURNEY_STAGES.map((step, index) => ({
    ...step,
    status: (
      done[index] ? 'completed' : index === currentIndex ? 'current' : 'upcoming'
    ) as JourneyStageStatus,
  }));
}
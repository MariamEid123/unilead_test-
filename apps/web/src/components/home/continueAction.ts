import type { CourseProgress, JourneyFlags, Student } from '../../types';
import { getActiveCourseProgress, getCatalogMatch, getLecturesForCourse } from '../../data/courses';
import { buildJourneyStages } from './journeyStages';

export interface ContinueAction {
  href: string;
  message: string;
}

export interface ContinueLesson {
  active: CourseProgress;
  courseId: string;
  courseTitle: string;
  percentage: number;
  /** The most relevant next lesson to study (first incomplete), if known. */
  nextLessonTitle: string | null;
  /** Where "Continue" should take the student. */
  href: string;
}

// Resolves the student's real learning context: their active course and the
// next lesson they have not yet completed. Matches lesson codes exactly the
// way CourseDetail does, so it stays consistent with the rest of the app.
export function getContinueLesson(student: Student | null): ContinueLesson | null {
  const active = getActiveCourseProgress(student);
  if (!active || !active.courseId) return null;

  const course = getCatalogMatch(active);
  const courseId = course?.id ?? active.courseId;
  const done = new Set(active.completedLessons ?? []);
  const lectures = getLecturesForCourse(courseId);
  const next = lectures.find((lecture) => lecture.code && !done.has(lecture.code));
  const last = active.completedLessons?.slice(-1)[0] ?? null;
  const lastLecture = last ? lectures.find((lecture) => lecture.code === last) : undefined;

  return {
    active,
    courseId,
    courseTitle: course?.title ?? active.courseTitle,
    percentage: Math.max(0, Math.min(100, Math.round(active.progressPercentage ?? 0))),
    nextLessonTitle: next?.title ?? null,
    href: next
      ? `/courses/${courseId}/lectures/${next.code}`
      : lastLecture
        ? `/courses/${courseId}/lectures/${lastLecture.code}`
        : `/courses/${courseId}`,
  };
}

// Derives where the student should go next and a short personalized message,
// entirely from real student data. Used by the Hero and the Continue card so
// the whole dashboard agrees on a single "next action".
export function getContinueAction(student: Student | null, journey: JourneyFlags): ContinueAction {
  if (!student) {
    return {
      href: '/courses',
      message: 'Your learning journey starts here. Let\u2019s find the best place to begin.',
    };
  }

  const lesson = getContinueLesson(student);
  if (lesson) {
    return {
      href: lesson.href,
      message:
        lesson.percentage > 0
          ? 'You\u2019re making progress. Let\u2019s continue where you left off.'
          : 'Your course is ready. Let\u2019s get started.',
    };
  }

  // Otherwise route to the next learning stage in the journey.
  const stages = buildJourneyStages(student, journey);
  const currentStage = stages.find((stage) => stage.status === 'current');
  if (currentStage) {
    return {
      href: currentStage.href,
      message: `Next up: ${currentStage.label}. Let\u2019s keep your momentum going.`,
    };
  }

  // Everything is complete.
  return {
    href: '/progress',
    message: 'Great work! You\u2019re one step closer to mastering your skills.',
  };
}
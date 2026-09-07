import type { CourseProgress, Student } from '../types';

export interface CourseCatalogItem {
  id: string;
  title: string;
  description: string;
  subject: string;
  lectures: number;
  quizzes: number;
  assignments: number;
  accent: 'physics' | 'math';
}

export interface CourseLecture {
  id: string;
  number: number;
  title: string;
  completed?: boolean;
}

export interface CourseTopic {
  id: string;
  name: string;
  category?: string;
}

export const COURSE_TOPICS: Record<string, CourseTopic[]> = {
  'math-zero-foundations': [
    { id: 'algebra', name: 'Algebra' },
    { id: 'functions', name: 'Functions' },
    { id: 'quadratic-equations', name: 'Quadratic Equations' },
    { id: 'trigonometry', name: 'Trigonometry' },
    { id: 'numbers-operations', name: 'Numbers and Operations' },
    { id: 'equations', name: 'Patterns and Equations' },
  ],
  'physics-fundamentals': [
    { id: 'motion-kinematics', name: 'Motion and Kinematics' },
    { id: 'forces-energy', name: 'Forces and Energy' },
    { id: 'newtons-laws', name: "Newton's Laws" },
    { id: 'work-power', name: 'Work and Power' },
    { id: 'vectors-scalars', name: 'Vectors and Scalars' },
  ],
};

export function getTopicsForCourse(courseId: string): CourseTopic[] {
  return COURSE_TOPICS[courseId] ?? [];
}

export const COURSE_CATALOG: CourseCatalogItem[] = [
  {
    id: 'physics-fundamentals',
    title: 'Physics Fundamentals',
    description: 'Explore the fundamental concepts of physics through structured lessons and practical learning.',
    subject: 'Physics',
    lectures: 24,
    quizzes: 8,
    assignments: 4,
    accent: 'physics',
  },
  {
    id: 'math-zero-foundations',
    title: 'Math Zero: Foundations',
    description: 'Build your mathematical foundation step by step through simple lessons and practice.',
    subject: 'Mathematics',
    lectures: 18,
    quizzes: 6,
    assignments: 3,
    accent: 'math',
  },
];

export function getCourseById(courseId: string) {
  return COURSE_CATALOG.find((course) => course.id === courseId);
}

export function getCourseProgress(
  student: Student | null | undefined,
  course: CourseCatalogItem
): CourseProgress | undefined {
  if (!student?.courseProgress) return undefined;
  return student.courseProgress.find(
    (p) =>
      p.courseId === course.id ||
      p.courseTitle.toLowerCase() === course.title.toLowerCase() ||
      (p.courseId === 'physics' && course.id === 'physics-fundamentals') ||
      (p.courseId === 'math-zero' && course.id === 'math-zero-foundations')
  );
}

export function getCoursePercentage(
  student: Student | null | undefined,
  course: CourseCatalogItem
): number {
  const progress = getCourseProgress(student, course);
  return Math.max(0, Math.min(100, Math.round(progress?.progressPercentage ?? 0)));
}

const COURSE_LECTURES: Record<string, CourseLecture[]> = {
  'physics-fundamentals': [
    { id: 'introduction-to-physics', number: 1, title: 'Introduction to Physics' },
    { id: 'motion-and-speed', number: 2, title: 'Motion and Speed' },
    { id: 'newtons-laws', number: 3, title: "Newton's Laws" },
  ],
  'math-zero-foundations': [
    { id: 'numbers-and-operations', number: 1, title: 'Numbers and Operations' },
    { id: 'patterns-and-equations', number: 2, title: 'Patterns and Equations' },
    { id: 'fractions-and-proportions', number: 3, title: 'Fractions and Proportions' },
  ],
};

export function getLecturesForCourse(courseId: string) {
  return COURSE_LECTURES[courseId] ?? [];
}

export function getLectureById(courseId: string, lectureId: string) {
  return getLecturesForCourse(courseId).find((lecture) => lecture.id === lectureId);
}
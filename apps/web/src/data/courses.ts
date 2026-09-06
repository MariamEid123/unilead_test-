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
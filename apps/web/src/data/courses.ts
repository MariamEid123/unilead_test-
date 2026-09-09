import type { CourseProgress, Student } from '../types';

export interface CourseCatalogItem {
  id: string;
  code?: string;
  title: string;
  description: string;
  subject: string;
  lectures: number;
  quizzes: number;
  assignments: number;
  accent: 'physics' | 'math' | 'code';
  image?: string;
}

export interface CourseLecture {
  id: string;
  code?: string;
  number: number;
  title: string;
  completed?: boolean;
  pdf?: string;
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
    code: 'PHY211',
    title: 'Physics Fundamentals',
    description: 'Explore the fundamental concepts of physics through structured lessons and practical learning.',
    subject: 'Physics',
    lectures: 24,
    quizzes: 8,
    assignments: 4,
    accent: 'physics',
    image: '/courses/physics.svg',
  },
  {
    id: 'math-1',
    code: 'MAT111',
    title: 'Mathematics 1',
    description: 'First-year Mathematics 1: differentiation of transcendental functions, limits and Maclaurin expansions, and the full integration toolkit.',
    subject: 'Mathematics',
    lectures: 10,
    quizzes: 0,
    assignments: 0,
    accent: 'math',
    image: '/courses/math.svg',
  },
  {
    id: 'structured-programming',
    code: 'CSE014',
    title: 'Structured Programming',
    description: 'First-year Structured Programming (Introductory Java): programs, expressions, selection, loops, arrays, strings, static methods and recursion.',
    subject: 'Programming',
    lectures: 12,
    quizzes: 0,
    assignments: 0,
    accent: 'code',
    image: '/courses/code.svg',
  },
  {
    id: 'information-technology',
    code: 'IT001',
    title: 'Information Technology Essentials',
    description: 'First-year IT foundation: computer systems and hardware, networks and security, and the data & productivity tools used every day.',
    subject: 'Information Technology',
    lectures: 3,
    quizzes: 0,
    assignments: 0,
    accent: 'code',
    image: '/courses/code.svg',
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
    image: '/courses/math.svg',
  },
];

export function getCourseById(courseId: string) {
  return COURSE_CATALOG.find((course) => course.id === courseId);
}

export function getCourseByCode(code: string) {
  return COURSE_CATALOG.find((course) => course.code === code);
}

export function courseImage(course: { image?: string; accent?: 'physics' | 'math' | 'code'; subject?: string }): string {
  if (course.image) return course.image;
  if (course.accent === 'physics') return '/courses/physics.svg';
  if (course.accent === 'code') return '/courses/code.svg';
  if (course.accent === 'math' || course.subject?.toLowerCase().includes('math')) return '/courses/math.svg';
  return '/courses/physics.svg';
}

export function getCourseProgress(
  student: Student | null | undefined,
  course: CourseCatalogItem
): CourseProgress | undefined {
  if (!student?.courseProgress) return undefined;
  return student.courseProgress.find(
    (p) =>
      p.courseId === course.code ||
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

export function getActiveCourseProgress(student: Student | null | undefined): CourseProgress | null {
  if (!student?.courseProgress?.length) return null;

  const direct = student.courseProgress.find(
    (p) =>
      (student.course.code && p.courseId === student.course.code) ||
      (student.course.id && p.courseId === student.course.id) ||
      (student.course.title && p.courseTitle.toLowerCase() === student.course.title.toLowerCase())
  );
  if (direct) return direct;

  const withProgress = student.courseProgress.filter((p) => (p.progressPercentage ?? 0) > 0);
  const pool = (withProgress.length ? withProgress : [...student.courseProgress]).sort(
    (a, b) => (b.progressPercentage ?? 0) - (a.progressPercentage ?? 0)
  );
  return pool[0] ?? null;
}

export function getCatalogMatch(progress: CourseProgress): CourseCatalogItem | null {
  return (
    getCourseByCode(progress.courseId) ??
    COURSE_CATALOG.find((course) => course.title === progress.courseTitle) ??
    COURSE_CATALOG.find((course) => course.id === progress.courseId) ??
    null
  );
}

const COURSE_LECTURES: Record<string, CourseLecture[]> = {
  'physics-fundamentals': [
    { id: 'electric-charge', code: 'L1', number: 1, title: 'Electric Charge and Its Properties', pdf: '/lectures/physics/lecture-01.pdf' },
    { id: 'charge-quantization', code: 'L1', number: 2, title: 'Charge Quantization and Charging Methods', pdf: '/lectures/physics/lecture-01.pdf' },
    { id: 'coulombs-law', code: 'L2', number: 3, title: "Coulomb's Law", pdf: '/lectures/physics/lecture-02.pdf' },
    { id: 'force-superposition', code: 'L2', number: 4, title: 'Superposition of Electric Forces', pdf: '/lectures/physics/lecture-02.pdf' },
    { id: 'electric-field', code: 'L3', number: 5, title: 'The Electric Field', pdf: '/lectures/physics/lecture-03.pdf' },
    { id: 'field-lines-dipoles', code: 'L3', number: 6, title: 'Field Lines, Motion in a Field and Dipoles', pdf: '/lectures/physics/lecture-03.pdf' },
    { id: 'electric-flux', code: 'L4', number: 7, title: 'Electric Flux', pdf: '/lectures/physics/lecture-04.pdf' },
    { id: 'gausss-law', code: 'L4', number: 8, title: "Gauss's Law", pdf: '/lectures/physics/lecture-04.pdf' },
    { id: 'capacitors-capacitance', code: 'L5', number: 9, title: 'Capacitors and Capacitance', pdf: '/lectures/physics/lecture-05.pdf' },
    { id: 'capacitor-energy', code: 'L5', number: 10, title: 'Energy Storage and Dielectrics', pdf: '/lectures/physics/lecture-05.pdf' },
    { id: 'electric-current', code: 'L6', number: 11, title: 'Electric Current and Drift Velocity', pdf: '/lectures/physics/lecture-06.pdf' },
    { id: 'current-density', code: 'L6', number: 12, title: 'Current Density and Charge Carriers', pdf: '/lectures/physics/lecture-06.pdf' },
    { id: 'resistors-series-parallel', code: 'L7', number: 13, title: 'Resistors: Series and Parallel', pdf: '/lectures/physics/lecture-07.pdf' },
    { id: 'emf-rc-circuits', code: 'L7', number: 14, title: 'EMF, Terminal Voltage and RC Circuits', pdf: '/lectures/physics/lecture-07.pdf' },
    { id: 'magnetic-poles-fields', code: 'L8', number: 15, title: 'Magnetic Poles and Fields', pdf: '/lectures/physics/lecture-08.pdf' },
    { id: 'force-on-moving-charge', code: 'L8', number: 16, title: 'Force on a Charge Moving in a Magnetic Field', pdf: '/lectures/physics/lecture-08.pdf' },
    { id: 'biot-savart-law', code: 'L9', number: 17, title: 'The Biot-Savart Law', pdf: '/lectures/physics/lecture-09.pdf' },
    { id: 'wires-loops-solenoids', code: 'L9', number: 18, title: 'Wires, Loops and Solenoids', pdf: '/lectures/physics/lecture-09.pdf' },
    { id: 'light-and-reflection', code: 'L10', number: 19, title: 'The Nature of Light and Reflection', pdf: '/lectures/physics/lecture-10.pdf' },
    { id: 'refraction-tir', code: 'L10', number: 20, title: 'Refraction and Total Internal Reflection', pdf: '/lectures/physics/lecture-10.pdf' },
    { id: 'image-formation-mirrors', code: 'L11', number: 21, title: 'Image Formation and Plane Mirrors', pdf: '/lectures/physics/lecture-11.pdf' },
    { id: 'spherical-mirrors', code: 'L11', number: 22, title: 'Spherical Mirrors and Ray Diagrams', pdf: '/lectures/physics/lecture-11.pdf' },
    { id: 'thin-lenses', code: 'L12', number: 23, title: 'Thin Lenses and Ray Diagrams', pdf: '/lectures/physics/lecture-12.pdf' },
    { id: 'lens-equation', code: 'L12', number: 24, title: 'The Lens Equation and Magnification', pdf: '/lectures/physics/lecture-12.pdf' },
  ],
  'math-zero-foundations': [
    { id: 'numbers-and-operations', number: 1, title: 'Numbers and Operations' },
    { id: 'patterns-and-equations', number: 2, title: 'Patterns and Equations' },
    { id: 'fractions-and-proportions', number: 3, title: 'Fractions and Proportions' },
  ],
  'information-technology': [
    { id: 'IT1', code: 'IT1', number: 1, title: 'Computers, Hardware and Operating Systems' },
    { id: 'IT2', code: 'IT2', number: 2, title: 'Networks, the Internet and Security' },
    { id: 'IT3', code: 'IT3', number: 3, title: 'Data and Productivity Tools' },
  ],
};

export function getLecturesForCourse(courseId: string) {
  return COURSE_LECTURES[courseId] ?? [];
}

export function getLectureById(courseId: string, lectureId: string) {
  return getLecturesForCourse(courseId).find((lecture) => lecture.id === lectureId);
}

export function getLectureByCode(courseId: string, code: string) {
  return getLecturesForCourse(courseId).find((lecture) => lecture.code === code);
}

export function resolveLecture(courseId: string, lectureIdOrCode: string) {
  return getLectureById(courseId, lectureIdOrCode) ?? getLectureByCode(courseId, lectureIdOrCode);
}
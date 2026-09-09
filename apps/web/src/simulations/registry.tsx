// Registry of interactive Physics 2 simulations. Each entry is a real,
// self-contained experiment; lessons reference sims by lesson id so the
// lecture pages can surface the right practical activity.
import type { ComponentType } from 'react';
import CoulombLab from './CoulombLab';

export interface SimMeta {
  id: string;
  title: string;
  courseCode: string;
  objective: string;
  // Static course  lecture ids this experiment supports (see data/courses.ts).
  lessonIds: string[];
  Component: ComponentType;
}

export const SIMULATIONS: SimMeta[] = [
  {
    id: 'coulombs-law',
    title: "Coulomb's Law in Motion",
    courseCode: 'PHY211',
    objective:
      'Release two point charges and watch the true F = k·|q₁q₂|/r² move them. Adjust charge, separation and mass, read live force/speed/kinetic energy, and confirm the 1/r² force–separation curve.',
    lessonIds: ['coulombs-law', 'force-superposition'],
    Component: CoulombLab,
  },
];

export function simulationById(id: string): SimMeta | undefined {
  return SIMULATIONS.find((s) => s.id === id);
}

export function simulationForLesson(lessonId: string | undefined): SimMeta | undefined {
  if (!lessonId) return undefined;
  return SIMULATIONS.find((s) => s.lessonIds.includes(lessonId));
}

export function simulationsForCourse(courseCode: string): SimMeta[] {
  return SIMULATIONS.filter((s) => s.courseCode === courseCode);
}
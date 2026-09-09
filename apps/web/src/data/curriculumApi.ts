import { apiGet, apiPost } from './apiClient';

export interface CourseListItem {
  id: number;
  code: string;
  title: string;
  description: string;
  credits: number;
  module_count: number;
  lesson_count: number;
}

export interface LessonCard {
  code: string;
  title: string;
  description: string;
  difficulty: string;
  estimated_minutes: number | null;
  sort_order: number;
  section_count: number;
  video_count: number;
  practice_count: number;
}

export interface ModuleCard {
  code: string;
  title: string;
  description: string;
  sort_order: number;
  lessons: LessonCard[];
}

export interface CourseDetail {
  id: number;
  code: string;
  title: string;
  description: string;
  credits: number;
  modules: ModuleCard[];
}

export interface CompetencyLink {
  code: string;
  title: string;
  role: string;
}

export interface LessonDetail {
  code: string;
  title: string;
  description: string;
  difficulty: string;
  estimated_minutes: number | null;
  objectives: string[];
  prerequisites: string[];
  course_code: string;
  course_title: string;
  module_code: string;
  module_title: string;
  competencies: CompetencyLink[];
  section_count: number;
  video_count: number;
  practice_count: number;
}

export interface ContentSection {
  section_type: string;
  title: string | null;
  body: string;
  sort_order: number;
  metadata: Record<string, unknown>;
}

export interface VideoResource {
  title: string;
  description: string;
  external_url: string | null;
  duration_seconds: number | null;
  sort_order: number;
  metadata: Record<string, unknown>;
}

export interface PracticeItemView {
  id: number;
  level: string;
  prompt: string;
  options: string[];
  skill: string | null;
  difficulty: number;
  sort_order: number;
}

export interface PracticeGradeResult {
  item_id: number;
  correct: boolean;
  correct_index: number;
  explanation: string;
}

export interface CourseLessonMaterials {
  lesson_code: string;
  lesson_title: string;
  module_code: string;
  module_title: string;
  resources: VideoResource[];
}

export interface CourseProgress {
  course_id: string;
  course_title: string;
  progress_percentage: number | null;
  completed_lectures: number | null;
  total_lectures: number | null;
  completed_quizzes: number | null;
  total_quizzes: number | null;
  completed_assignments: number | null;
  total_assignments: number | null;
}

export interface ProgressResponse {
  overall_progress: number;
  competencies: { name: string; status: string }[];
  recommended_next_activity: string;
  course_code: string;
  course_title: string;
  courses: CourseProgress[];
  last_active_course: string | null;
  last_lecture: string | null;
}

export function fetchCourses() {
  return apiGet<CourseListItem[]>('/curriculum/courses');
}

export function fetchCourseDetail(code: string) {
  return apiGet<CourseDetail>(`/curriculum/courses/${encodeURIComponent(code)}`);
}

export function fetchLessonDetail(code: string) {
  return apiGet<LessonDetail>(`/curriculum/lessons/${encodeURIComponent(code)}`);
}

export function fetchLectureSections(code: string) {
  return apiGet<ContentSection[]>(`/curriculum/lessons/${encodeURIComponent(code)}/lecture`);
}

export function fetchSummarySections(code: string) {
  return apiGet<ContentSection[]>(`/curriculum/lessons/${encodeURIComponent(code)}/summary`);
}

export function fetchVideoResources(code: string) {
  return apiGet<VideoResource[]>(`/curriculum/lessons/${encodeURIComponent(code)}/videos`);
}

export function fetchCourseMaterials(code: string) {
  return apiGet<CourseLessonMaterials[]>(`/curriculum/courses/${encodeURIComponent(code)}/materials`);
}

export function fetchPracticeItems(code: string) {
  return apiGet<PracticeItemView[]>(`/curriculum/lessons/${encodeURIComponent(code)}/practice`);
}

export function fetchProgress() {
  return apiGet<ProgressResponse>('/progress');
}

export async function completeLesson(code: string) {
  return apiPost<ProgressResponse>(`/curriculum/lessons/${encodeURIComponent(code)}/complete`, {});
}

export async function gradePractice(lessonCode: string, itemId: number, selectedIndex: number) {
  return apiPost<PracticeGradeResult>(`/curriculum/lessons/${encodeURIComponent(lessonCode)}/practice/grade`, {
    item_id: itemId,
    selected_index: selectedIndex,
  });
}

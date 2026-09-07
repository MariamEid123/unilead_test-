// API layer for the app.
//
// This file is the ONLY place that knows the backend exists — every page
// imports from here exactly as it did when this was pure mock data, so
// nothing above this layer had to change when the FastAPI backend was
// added. Pages still never compute mastery/progress themselves; they just
// display what this layer returns.
//
// Field-name translation (backend is snake_case, frontend types are
// camelCase) happens once, right here.

import { apiGet, apiPost, setAuthToken, clearAuthToken } from './apiClient';
import type {
  Student,
  DiagnosticQuestion,
  DiagnosticAnswer,
  DiagnosticResult,
  LessonSection,
  PracticeTask,
  OnboardingAnswers,
  SimulationResult,
  ReviewData,
  CompetencyStatus,
  Competency,
  CourseProgress,
  CoachMode,
  CoachResponse,
  RemediationPlan,
  TransferScenario,
  TransferEvaluation,
  InstructorStudentSummary,
  InstructorCompetencyAggregate,
  InstructorClassSummary,
  InstructorStudentDetail,
  EvidenceEvent,
  AuthSession,
  SignUpRequest,
  LoginRequest,
  MeResponse,
  SignUpResult,
  VerifyEmailRequest,
} from '../types';

function toFrontendStatus(status: string): CompetencyStatus {
  return status.toUpperCase() as CompetencyStatus;
}

// ---- Student / competencies -------------------------------------------

interface ApiCompetency {
  id: string;
  name: string;
  status: string;
  progress: number;
}

interface ApiProgress {
  overall_progress: number;
  courses: ApiCourseProgress[];
  last_active_course: string | null;
  last_lecture: string | null;
}

interface ApiCourseProgress {
  course_id: string;
  course_title: string;
  progress_percentage?: number;
  completed_lectures?: number;
  total_lectures?: number;
  completed_quizzes?: number;
  total_quizzes?: number;
  completed_assignments?: number;
  total_assignments?: number;
}

function mapCompetency(c: ApiCompetency): Competency {
  return { id: c.id, name: c.name, status: toFrontendStatus(c.status), progress: c.progress };
}

function toAvailableNumber(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) && value >= 0 ? value : null;
}

function mapCourseProgress(course: ApiCourseProgress): CourseProgress {
  return {
    courseId: course.course_id,
    courseTitle: course.course_title,
    progressPercentage: toAvailableNumber(course.progress_percentage),
    completedLectures: toAvailableNumber(course.completed_lectures),
    totalLectures: toAvailableNumber(course.total_lectures),
    completedQuizzes: toAvailableNumber(course.completed_quizzes),
    totalQuizzes: toAvailableNumber(course.total_quizzes),
    completedAssignments: toAvailableNumber(course.completed_assignments),
    totalAssignments: toAvailableNumber(course.total_assignments),
  };
}

export async function getStudent(): Promise<Student> {
  const [competencies, progress, me] = await Promise.all([
    apiGet<ApiCompetency[]>('/competencies'),
    apiGet<ApiProgress>('/progress'),
    getMe(),
  ]);

  const activeCourse = progress.last_active_course
    ? progress.courses.find((course) => course.course_id === progress.last_active_course)
    : undefined;

  return {
    id: me.studentId,
    name: me.name,
    email: me.email,
    course: {
      // No active course means no learning activity has been recorded. Do not
      // invent a Physics default in the frontend.
      id: activeCourse?.course_id ?? '',
      code: activeCourse?.course_id?.toUpperCase() ?? '',
      title: activeCourse?.course_title ?? '',
    },
    overallProgress: progress.overall_progress,
    courseProgress: progress.courses.map(mapCourseProgress),
    competencies: competencies.map(mapCompetency),
  };
}

// ---- Onboarding ---------------------------------------------------------

export async function submitOnboarding(answers: OnboardingAnswers): Promise<{ success: true }> {
  return apiPost('/onboarding', {
    learning_challenge: answers.learningChallenge,
    preferred_method: answers.preferredMethod,
    obstacle: answers.obstacle,
    goal: answers.goal,
  });
}

// ---- Diagnostic -----------------------------------------------------------

interface ApiDiagnosticQuestion {
  id: string;
  competency_id: string;
  prompt: string;
  options: { id: string; label: string }[];
}

interface ApiDiagnosticResult {
  competency_id: string;
  competency_name: string;
  status: string;
  misconceptions: string[];
  accuracy: number;
}

export async function getDiagnosticQuestions(): Promise<DiagnosticQuestion[]> {
  const questions = await apiGet<ApiDiagnosticQuestion[]>('/diagnostic/questions');
  return questions.map((q) => ({
    id: q.id,
    competencyId: q.competency_id,
    prompt: q.prompt,
    options: q.options,
  }));
}

export async function submitDiagnostic(answers: DiagnosticAnswer[]): Promise<DiagnosticResult[]> {
  const results = await apiPost<ApiDiagnosticResult[]>('/diagnostic', {
    answers: answers.map((a) => ({ question_id: a.questionId, option_id: a.optionId })),
  });
  return results.map((r) => ({
    competencyId: r.competency_id,
    competencyName: r.competency_name,
    status: toFrontendStatus(r.status),
    misconceptions: r.misconceptions ?? [],
    accuracy: r.accuracy ?? 0,
  }));
}

// ---- Learning / Practice content ------------------------------------------

export async function getLesson(competencyId: string): Promise<LessonSection[]> {
  return apiGet(`/learning/${competencyId}`);
}

export async function getPracticeTask(competencyId: string): Promise<PracticeTask> {
  return apiGet(`/practice/${competencyId}`);
}

// Marks a practice attempt as submitted. There's no backend endpoint for
// this yet (nothing downstream reads the result), so it resolves locally —
// keeping the same signature Practice.tsx already calls.
export async function submitPractice(_taskId: string): Promise<{ submitted: true }> {
  return { submitted: true };
}

// ---- Simulation -------------------------------------------------------------

interface ApiSimulationResult {
  stable: boolean;
  overshoot: number;
  settling_time: number;
  rise_time: number;
  steady_state_error: number;
  kp: number;
  ki: number;
  kd: number;
  requirements_met: boolean;
  result: 'PASS' | 'FAIL';
  attempt: number;
  competency_id: string;
  misconception: string | null;
}

export interface RunSimulationParams {
  kp: number;
  ki: number;
  kd: number;
  competencyId?: string;
  taskId?: string;
}

export async function runSimulation(params: RunSimulationParams): Promise<SimulationResult> {
  const r = await apiPost<ApiSimulationResult>('/simulation', {
    kp: params.kp,
    ki: params.ki,
    kd: params.kd,
    competency_id: params.competencyId ?? 'pid-tuning',
    task_id: params.taskId ?? 'pid-001',
  });
  return {
    stable: r.stable,
    overshoot: r.overshoot,
    settlingTime: r.settling_time,
    riseTime: r.rise_time,
    steadyStateError: r.steady_state_error,
    kp: r.kp,
    ki: r.ki,
    kd: r.kd,
    requirementsMet: r.requirements_met,
    result: r.result,
    attempt: r.attempt,
    competencyId: r.competency_id,
    misconception: r.misconception,
  };
}

// ---- Review / Evidence -----------------------------------------------------

interface ApiReviewResponse {
  competency_id: string;
  competency_name: string;
  status: string;
  progress: number;
  overall_progress: number;
  evidence: { id: string; label: string; met: boolean }[];
}

// Views the current evidence without changing anything server-side.
export async function getReview(competencyId: string): Promise<ReviewData> {
  const r = await apiPost<ApiReviewResponse>('/review', {
    competency_id: competencyId,
    finalize: false,
  });
  return {
    competencyId: r.competency_id,
    competencyName: r.competency_name,
    status: toFrontendStatus(r.status),
    evidence: r.evidence,
  };
}

// Finalizes the review: the backend folds the evidence back into the
// student's progress (this is the one place mastery numbers actually
// change), and we merge the result into the passed-in student object.
export async function completeReview(student: Student): Promise<Student> {
  const active =
    student.competencies.find((c) => c.status === 'DEVELOPING') ?? student.competencies[0]!;

  const r = await apiPost<ApiReviewResponse>('/review', {
    competency_id: active.id,
    finalize: true,
  });

  return {
    ...student,
    overallProgress: r.overall_progress,
    competencies: student.competencies.map((c) =>
      c.id === r.competency_id ? { ...c, status: toFrontendStatus(r.status), progress: r.progress } : c
    ),
  };
}

// ---- AI Coach ---------------------------------------------------------------

interface ApiCoachResponse {
  message: string;
  active_mode: CoachMode;
  target_competency_id: string | null;
  scaffolding_level: 'LOW' | 'MEDIUM' | 'HIGH' | null;
  suggested_actions: string[];
  turn_index: number;
  total_turns: number;
  finished: boolean;
}

export interface SendCoachMessageParams {
  message: string;
  mode?: CoachMode;
  competencyId?: string;
}

export async function sendCoachMessage(params: SendCoachMessageParams): Promise<CoachResponse> {
  const r = await apiPost<ApiCoachResponse>('/coach', {
    message: params.message,
    mode: params.mode ?? null,
    competency_id: params.competencyId ?? null,
  });
  return {
    message: r.message,
    activeMode: r.active_mode,
    targetCompetencyId: r.target_competency_id,
    scaffoldingLevel: r.scaffolding_level,
    suggestedActions: r.suggested_actions ?? [],
    turnIndex: r.turn_index,
    totalTurns: r.total_turns,
    finished: r.finished,
  };
}

// ---- Remediation ------------------------------------------------------------

interface ApiRemediationPlan {
  competency_id: string;
  detected_misconception: string | null;
  recommended_action: string;
  conceptual_focus: string;
  guided_question: string;
  remediation_steps: string[];
  consecutive_failures: number;
  total_attempts: number;
  summary_text: string;
}

export async function getRemediationPlan(competencyId: string): Promise<RemediationPlan> {
  const r = await apiGet<ApiRemediationPlan>(`/remediation/${competencyId}`);
  return {
    competencyId: r.competency_id,
    detectedMisconception: r.detected_misconception,
    recommendedAction: r.recommended_action,
    conceptualFocus: r.conceptual_focus,
    guidedQuestion: r.guided_question,
    remediationSteps: r.remediation_steps ?? [],
    consecutiveFailures: r.consecutive_failures,
    totalAttempts: r.total_attempts,
    summaryText: r.summary_text,
  };
}

// ---- Transfer ---------------------------------------------------------------

interface ApiTransferScenario {
  competency_id: string;
  scenario_id: string;
  title: string;
  domain: string;
  prompt: string;
  error_signal_meaning: string;
  control_output_meaning: string;
  system_inertia: string;
  conceptual_challenge: string;
}

interface ApiTransferEvaluation {
  competency_id: string;
  scenario_id: string;
  passed: boolean;
  matched_terms: string[];
  matched_count: number;
  min_required: number;
  feedback: string;
}

export async function getTransferScenario(
  competencyId: string,
  scenarioId?: string
): Promise<TransferScenario> {
  const qs = scenarioId ? `?scenario_id=${encodeURIComponent(scenarioId)}` : '';
  const r = await apiGet<ApiTransferScenario>(`/transfer/${competencyId}${qs}`);
  return {
    competencyId: r.competency_id,
    scenarioId: r.scenario_id,
    title: r.title,
    domain: r.domain,
    prompt: r.prompt,
    errorSignalMeaning: r.error_signal_meaning,
    controlOutputMeaning: r.control_output_meaning,
    systemInertia: r.system_inertia,
    conceptualChallenge: r.conceptual_challenge,
  };
}

export async function submitTransferResponse(
  competencyId: string,
  responseText: string,
  scenarioId: string
): Promise<TransferEvaluation> {
  const r = await apiPost<ApiTransferEvaluation>(`/transfer/${competencyId}`, {
    response_text: responseText,
    scenario_id: scenarioId,
  });
  return {
    competencyId: r.competency_id,
    scenarioId: r.scenario_id,
    passed: r.passed,
    matchedTerms: r.matched_terms ?? [],
    matchedCount: r.matched_count,
    minRequired: r.min_required,
    feedback: r.feedback,
  };
}

// ---- Instructor (NEW) -----------------------------------------------------

interface ApiInstructorStudentSummary {
  student_id: string;
  display_name: string;
  course_code: string;
  course_title: string;
  overall_progress: number;
  competencies: ApiCompetency[];
}

interface ApiInstructorCompetencyAggregate {
  competency_id: string;
  competency_name: string;
  demonstrated: number;
  developing: number;
  needs_practice: number;
  not_started: number;
}

interface ApiInstructorClassSummary {
  total_students: number;
  average_overall_progress: number;
  students_demonstrated_all: number;
  students_with_failures: number;
}

interface ApiEvidenceEvent {
  timestamp: string;
  event_type: string;
  competency_id: string | null;
  title: string;
  detail: string;
  result: 'PASS' | 'FAIL' | 'INFO';
}

interface ApiInstructorStudentDetail extends ApiInstructorStudentSummary {
  evidence_timeline: ApiEvidenceEvent[];
}

function mapInstructorStudent(s: ApiInstructorStudentSummary): InstructorStudentSummary {
  return {
    studentId: s.student_id,
    displayName: s.display_name,
    courseCode: s.course_code,
    courseTitle: s.course_title,
    overallProgress: s.overall_progress,
    competencies: (s.competencies ?? []).map(mapCompetency),
  };
}

function mapEvidenceEvent(e: ApiEvidenceEvent): EvidenceEvent {
  return {
    timestamp: e.timestamp,
    eventType: e.event_type,
    competencyId: e.competency_id,
    title: e.title,
    detail: e.detail,
    result: e.result,
  };
}

export async function getInstructorClassSummary(): Promise<InstructorClassSummary> {
  const r = await apiGet<ApiInstructorClassSummary>('/instructor/summary');
  return {
    totalStudents: r.total_students,
    averageOverallProgress: r.average_overall_progress,
    studentsDemonstratedAll: r.students_demonstrated_all,
    studentsWithFailures: r.students_with_failures,
  };
}

export async function getInstructorCompetencyAggregate(): Promise<InstructorCompetencyAggregate[]> {
  const r = await apiGet<ApiInstructorCompetencyAggregate[]>('/instructor/aggregate');
  return r.map((c) => ({
    competencyId: c.competency_id,
    competencyName: c.competency_name,
    demonstrated: c.demonstrated,
    developing: c.developing,
    needsPractice: c.needs_practice,
    notStarted: c.not_started,
  }));
}

export async function getInstructorStudents(): Promise<InstructorStudentSummary[]> {
  const r = await apiGet<ApiInstructorStudentSummary[]>('/instructor/students');
  return r.map(mapInstructorStudent);
}

export async function getInstructorStudentDetail(
  studentId: string
): Promise<InstructorStudentDetail> {
  const r = await apiGet<ApiInstructorStudentDetail>(`/instructor/students/${studentId}`);
  return {
    ...mapInstructorStudent(r),
    evidenceTimeline: (r.evidence_timeline ?? []).map(mapEvidenceEvent),
  };
}

// ---- Evidence Timeline (NEW) -----------------------------------------------

export async function getMyEvidenceTimeline(): Promise<EvidenceEvent[]> {
  const r = await apiGet<ApiEvidenceEvent[]>('/evidence/me/timeline');
  return r.map(mapEvidenceEvent);
}

export async function getEvidenceTimeline(studentId: string): Promise<EvidenceEvent[]> {
  const r = await apiGet<ApiEvidenceEvent[]>(`/evidence/${studentId}/timeline`);
  return r.map(mapEvidenceEvent);
}

// ---- Auth (NEW) ------------------------------------------------------------
//
// signup/login/me — JWT-based auth. The token is stored in localStorage
// (see apiClient.ts) and automatically attached to every subsequent
// request via the Authorization header.

interface ApiAuthResponse {
  access_token: string;
  token_type: string;
  user_id: number;
  email: string;
  username: string;
  name: string;
  student_id: string;
  role: string;
}

function mapAuthResponse(r: ApiAuthResponse): AuthSession {
  // Persist the token immediately so subsequent requests are authenticated.
  setAuthToken(r.access_token);
  return {
    accessToken: r.access_token,
    tokenType: r.token_type as 'bearer',
    userId: r.user_id,
    email: r.email,
    username: r.username,
    name: r.name,
    studentId: r.student_id,
    role: (r.role === 'instructor' ? 'instructor' : 'student'),
  };
}

interface ApiSignUpResponse {
  verification_required: boolean;
  email: string;
  message: string;
  resend_after_seconds: number;
}

function mapSignUpResponse(r: ApiSignUpResponse): SignUpResult {
  return {
    verificationRequired: r.verification_required,
    email: r.email,
    message: r.message,
    resendAfterSeconds: r.resend_after_seconds,
  };
}

// Signup no longer returns a JWT — the backend emails a 6-digit code that
// must be verified (POST /api/auth/verify-email) before a token is issued.
export async function signUp(req: SignUpRequest): Promise<SignUpResult> {
  const r = await apiPost<ApiSignUpResponse>('/auth/signup', {
    name: req.name,
    username: req.username,
    email: req.email,
    password: req.password,
  });
  return mapSignUpResponse(r);
}

export async function designPreviewLogin(): Promise<AuthSession> {
  const r = await apiPost<ApiAuthResponse>('/auth/design-preview', {});
  return mapAuthResponse(r);
}

export async function verifyEmail(req: VerifyEmailRequest): Promise<AuthSession> {
  const r = await apiPost<ApiAuthResponse>('/auth/verify-email', {
    email: req.email,
    code: req.code,
  });
  return mapAuthResponse(r);
}

interface ApiResendResponse {
  email: string;
  message: string;
  resend_after_seconds: number;
}

export async function resendVerificationCode(email: string): Promise<{
  email: string;
  resendAfterSeconds: number;
}> {
  const r = await apiPost<ApiResendResponse>('/auth/resend-verification', { email });
  return { email: r.email, resendAfterSeconds: r.resend_after_seconds };
}

export async function forgotPassword(email: string): Promise<{ message: string }> {
  return apiPost<{ message: string }>('/auth/forgot-password', { email });
}

export async function resetPassword(req: {
  email: string;
  code: string;
  newPassword: string;
}): Promise<{ message: string }> {
  return apiPost<{ message: string }>('/auth/reset-password', {
    email: req.email,
    code: req.code,
    new_password: req.newPassword,
  });
}

export async function login(req: LoginRequest): Promise<AuthSession> {
  const r = await apiPost<ApiAuthResponse>('/auth/login', {
    email: req.email,
    password: req.password,
  });
  return mapAuthResponse(r);
}

export async function getMe(): Promise<MeResponse> {
  const r = await apiGet<ApiMeResponse>('/auth/me');
  return {
    userId: r.user_id,
    email: r.email,
    username: r.username,
    name: r.name,
    studentId: r.student_id,
    studentDisplayName: r.student_display_name,
    role: (r.role === 'instructor' ? 'instructor' : 'student'),
  };
}

interface ApiMeResponse {
  user_id: number;
  email: string;
  username: string;
  name: string;
  student_id: string;
  student_display_name: string;
  role: string;
}

export function logout(): void {
  clearAuthToken();
}

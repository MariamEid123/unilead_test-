// Core domain types for the competency-based learning MVP.
// These mirror the "Data Contract" the real Education API will eventually return.

export type CompetencyStatus =
  | 'NOT_STARTED'
  | 'NEEDS_PRACTICE'
  | 'DEVELOPING'
  | 'DEMONSTRATED';

export interface Competency {
  id: string;
  name: string;
  status: CompetencyStatus;
  progress: number; // 0-100, derived from evidence — UI never invents this
}

export interface Course {
  id: string;
  code: string; // e.g. PHY211
  title: string; // e.g. Physics (First Year)
}

export interface CourseProgress {
  courseId: string;
  courseTitle: string;
  progressPercentage: number | null;
  completedLectures: number | null;
  totalLectures: number | null;
  completedQuizzes: number | null;
  totalQuizzes: number | null;
  completedAssignments: number | null;
  totalAssignments: number | null;
  completedLessons: string[];
}

export interface Student {
  id: string;
  name: string;
  email: string;
  course: Course;
  overallProgress: number; // 0-100
  courseProgress: CourseProgress[];
  competencies: Competency[];
}

export interface OnboardingAnswers {
  learningChallenge: string;
  preferredMethod: string;
  obstacle: string;
  goal: string;
}

export interface DiagnosticQuestion {
  id: string;
  competencyId: string;
  prompt: string;
  options: { id: string; label: string }[];
}

export interface DiagnosticAnswer {
  questionId: string;
  optionId: string;
}

export interface DiagnosticResult {
  competencyId: string;
  competencyName: string;
  status: CompetencyStatus;
  // NEW (wired): misconceptions detected from incorrect answers on this
  // competency's diagnostic question.
  misconceptions: string[];
  // NEW (wired): raw correctness on this competency's question (0..1).
  accuracy: number;
}

export interface Recommendation {
  id: string;
  title: string;
  reason: string;
  href: string;
  actionLabel: string;
}

export interface LessonSection {
  id: string;
  heading: string;
  body: string;
}

export interface PracticeTask {
  id: string;
  title: string;
  objective: string;
  requirements: string[];
  hints: string[];
}

export interface SimulationResult {
  stable: boolean;
  overshoot: number; // percent
  settlingTime: number; // seconds
  riseTime: number; // seconds
  steadyStateError: number;
  // NEW (wired): which gains produced this run + evidence outcome.
  kp: number;
  ki: number;
  kd: number;
  requirementsMet: boolean;
  result: 'PASS' | 'FAIL';
  attempt: number;
  competencyId: string;
  misconception: string | null;
}

export interface EvidenceItem {
  id: string;
  label: string;
  met: boolean;
}

export interface ReviewData {
  competencyId: string;
  competencyName: string;
  status: CompetencyStatus;
  evidence: EvidenceItem[];
}

// The six AI Coach modes — mirrors ai_education.domain.enums.CoachMode.
export type CoachMode =
  | 'LEARN'
  | 'HINT'
  | 'PRACTICE'
  | 'REFLECT'
  | 'REMEDIATE'
  | 'TRANSFER';

export interface CoachMessage {
  id: string;
  sender: 'coach' | 'student';
  text: string;
  // NEW (wired): which mode produced this coach message.
  mode?: CoachMode;
}

// The adaptive learning context the UI assembles from real student data and
// sends to the coach engine on EVERY interaction. The engine treats it as
// corroborative — the authoritative facts live in the backend's CoachContext.
export interface CoachContextPack {
  focus: string;
  earliestNextStep: string | null;
  competency: {
    id: string;
    name: string;
    status: CompetencyStatus;
    progress: number;
  };
  evidence: string[];
  misconception: string | null;
}

// NEW (wired): the response shape from POST /api/coach.
export interface CoachResponse {
  message: string;
  activeMode: CoachMode;
  targetCompetencyId: string | null;
  scaffoldingLevel: 'LOW' | 'MEDIUM' | 'HIGH' | null;
  suggestedActions: string[];
  turnIndex: number;
  totalTurns: number;
  finished: boolean;
}

// NEW (wired): the response shape from GET /api/remediation/{id}.
export interface RemediationPlan {
  competencyId: string;
  detectedMisconception: string | null;
  recommendedAction: string;
  conceptualFocus: string;
  guidedQuestion: string;
  remediationSteps: string[];
  consecutiveFailures: number;
  totalAttempts: number;
  summaryText: string;
}

// NEW (wired): the response shape from GET /api/transfer/{id}.
export interface TransferScenario {
  competencyId: string;
  scenarioId: string;
  title: string;
  domain: string;
  prompt: string;
  errorSignalMeaning: string;
  controlOutputMeaning: string;
  systemInertia: string;
  conceptualChallenge: string;
}

// NEW (wired): the response shape from POST /api/transfer/{id}.
export interface TransferEvaluation {
  competencyId: string;
  scenarioId: string;
  passed: boolean;
  matchedTerms: string[];
  matchedCount: number;
  minRequired: number;
  feedback: string;
}

// Tracks how far the student has progressed through the core learning loop.
// The UI reads these flags to decide what to recommend next — it never
// invents progression logic of its own.
export interface JourneyFlags {
  hasCompletedOnboarding: boolean;
  hasCompletedDiagnostic: boolean;
  hasCompletedLearning: boolean;
  hasCompletedPractice: boolean;
  hasCompletedSimulation: boolean;
  hasCompletedReview: boolean;
}

// Async state wrapper every page uses for its data fetch.
export type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'error'; message: string }
  | { status: 'success'; data: T };

// ---- Instructor types (NEW) ------------------------------------------------

export interface InstructorStudentSummary {
  studentId: string;
  displayName: string;
  courseCode: string;
  courseTitle: string;
  overallProgress: number;
  competencies: Competency[];
}

export interface InstructorCompetencyAggregate {
  competencyId: string;
  competencyName: string;
  demonstrated: number;
  developing: number;
  needsPractice: number;
  notStarted: number;
}

export interface InstructorClassSummary {
  totalStudents: number;
  averageOverallProgress: number;
  studentsDemonstratedAll: number;
  studentsWithFailures: number;
}

export interface EvidenceEvent {
  timestamp: string;
  eventType:
    | 'diagnostic_submitted'
    | 'simulation_run'
    | 'remediation_completed'
    | 'transfer_evaluated'
    | 'coach_turn'
    | string;
  competencyId: string | null;
  title: string;
  detail: string;
  result: 'PASS' | 'FAIL' | 'INFO';
}

export interface InstructorStudentDetail extends InstructorStudentSummary {
  evidenceTimeline: EvidenceEvent[];
}

// ---- Auth types (NEW) ------------------------------------------------------

export interface AuthSession {
  accessToken: string;
  tokenType: 'bearer';
  userId: number;
  email: string;
  username: string;
  name: string;
  studentId: string;
  role: 'student' | 'instructor';
}

export interface SignUpRequest {
  name: string;
  username: string;
  email: string;
  password: string;
}

export interface SignUpResult {
  verificationRequired: boolean;
  email: string;
  message: string;
  resendAfterSeconds: number;
}

export interface VerifyEmailRequest {
  email: string;
  code: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface MeResponse {
  userId: number;
  email: string;
  username: string;
  name: string;
  studentId: string;
  studentDisplayName: string;
  role: 'student' | 'instructor';
}

// ---- Code Lab types (NEW) -------------------------------------------------
// Wire shapes from the /api/lab endpoints (lab router + schemas/lab.py).
// The backend grades against real sandboxed execution; answers, tests and
// solution indexes never leave the server (the manifest view strips them).

export interface LabRuntime {
  language: string;
  available: boolean;
  label: string;
}

export interface LabLesson {
  code: string;
  title: string;
}

export type LabChallengeType = 'complete_code' | 'debug' | 'output_prediction' | 'challenge';
export type LabDifficulty = 'easy' | 'medium' | 'hard';

export interface LabChallengeView {
  id: string;
  lessonCode: string;
  type: LabChallengeType;
  topic: string;
  difficulty: LabDifficulty;
  title: string;
  prompt: string;
  starterCode: string | null;
  codeText: string | null;
  options: string[] | null;
  lessonTitle: string;
}

export interface LabManifest {
  courseCode: string;
  courseTitle: string;
  runtime: string;
  runtimeLabel: string;
  lessons: LabLesson[];
  challenges: LabChallengeView[];
}

export interface LabRunResult {
  status: 'ok' | 'compile_error' | 'runtime_error' | 'timeout' | 'rejected' | 'internal_error';
  stdout: string;
  stderr: string;
  exitCode: number | null;
  durationMs: number;
  detail: string;
}

export interface LabTestReport {
  passed: boolean;
  input: string;
  expected: string;
  got: string;
  note: string | null;
}

export type LabVerdict =
  | 'passed'
  | 'failed'
  | 'compile_error'
  | 'timeout'
  | 'rejected'
  | 'correct'
  | 'wrong';

export interface LabSubmitResult {
  verdict: LabVerdict;
  testsPassed: number;
  testsTotal: number;
  reports: LabTestReport[];
  compileError: string | null;
  correctIndex: number | null;
  explanation: string;
  feedback: string;
  newlyPassed: boolean;
}

export interface LabHintResult {
  challengeId: string;
  level: 'general' | 'specific' | 'solution';
  text: string;
  hintsUsed: number;
  remaining: number;
}

export interface LabAssistResult {
  depth: 'hint' | 'explain' | 'deeper' | 'solution';
  text: string;
  suggestions: string[];
}

export interface LabRecentAttempt {
  challengeId: string;
  title: string;
  type: LabChallengeType;
  difficulty: LabDifficulty;
  correct: boolean;
  passedTests: number;
  totalTests: number;
  at: string;
}

export interface LabProgress {
  totalChallenges: number;
  attempted: number;
  passed: number;
  attempts: number;
  accuracyPct: number;
  currentDifficulty: LabDifficulty;
  streakDays: number;
  progressPct: number;
  weakTopics: string[];
  recent: LabRecentAttempt[];
}

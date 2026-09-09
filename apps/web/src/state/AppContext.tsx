// oxlint-disable react/only-export-components -- context module intentionally exports a provider + hook pair
import type { ReactNode } from 'react';
import { createContext, useContext, useEffect, useMemo, useState } from 'react';
import type { Student, DiagnosticResult, OnboardingAnswers, JourneyFlags, AuthSession } from '../types';
import { getMe } from '../data/mockApi';

interface AppState {
  student: Student | null;
  setStudent: (s: Student) => void;
  onboardingAnswers: OnboardingAnswers | null;
  setOnboardingAnswers: (a: OnboardingAnswers) => void;
  diagnosticResults: DiagnosticResult[] | null;
  setDiagnosticResults: (r: DiagnosticResult[]) => void;

  // NEW: auth session — stored in localStorage so refresh keeps you logged in
  session: AuthSession | null;
  setSession: (s: AuthSession | null) => void;

  // Theme — light/dark; persisted and applied via `.dark` class + color-scheme.
  theme: 'light' | 'dark';
  toggleTheme: () => void;

  // Journey progress — read by Home to decide what to recommend next.
  journey: JourneyFlags;
  markLearningComplete: () => void;
  markPracticeComplete: () => void;
  markSimulationComplete: () => void;
  markReviewComplete: () => void;
}

const AppContext = createContext<AppState | undefined>(undefined);

const SESSION_KEY = 'Areta_session';
const THEME_KEY = 'Areta_theme';

function loadTheme(): 'light' | 'dark' {
  try {
    const stored = localStorage.getItem(THEME_KEY);
    if (stored === 'light' || stored === 'dark') return stored;
  } catch {
    // ignore storage failures
  }
  return window.matchMedia?.('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

function loadSession(): AuthSession | null {
  try {
    const raw = localStorage.getItem(SESSION_KEY);
    if (!raw) return null;
    return JSON.parse(raw) as AuthSession;
  } catch {
    return null;
  }
}

function saveSession(s: AuthSession | null) {
  if (s) {
    localStorage.setItem(SESSION_KEY, JSON.stringify(s));
  } else {
    localStorage.removeItem(SESSION_KEY);
  }
}

export function AppProvider({ children }: { children: ReactNode }) {
  const [student, setStudent] = useState<Student | null>(null);
  const [onboardingAnswers, setOnboardingAnswers] = useState<OnboardingAnswers | null>(null);
  const [diagnosticResults, setDiagnosticResults] = useState<DiagnosticResult[] | null>(null);
  const [session, setSessionState] = useState<AuthSession | null>(loadSession);

  // Validate the stored session against the backend on mount.
  // If the token is expired or invalid, clear it silently.
  useEffect(() => {
    if (!session) return;
    let cancelled = false;
    (async () => {
      try {
        const me = await getMe();
        if (cancelled) return;
        // Update session with fresh data from server (especially role).
        const updated: AuthSession = {
          ...session,
          name: me.name,
          email: me.email,
          username: me.username,
          studentId: me.studentId,
          role: me.role as AuthSession['role'] ?? session.role,
        };
        setSessionState(updated);
        saveSession(updated);
      } catch {
        if (!cancelled) {
          // Token is invalid/expired — clear session.
          setSessionState(null);
          saveSession(null);
        }
      }
    })();
    return () => { cancelled = true; };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const [hasCompletedLearning, setHasCompletedLearning] = useState(false);
  const [hasCompletedPractice, setHasCompletedPractice] = useState(false);
  const [hasCompletedSimulation, setHasCompletedSimulation] = useState(false);
  const [hasCompletedReview, setHasCompletedReview] = useState(false);

  const [theme, setTheme] = useState<'light' | 'dark'>(loadTheme);

  // Apply the theme to <html> (cascades to every var) and keep the browser
  // chrome (scrollbars, form controls) in sync.
  useEffect(() => {
    const root = document.documentElement;
    root.classList.toggle('dark', theme === 'dark');
    root.style.colorScheme = theme;
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch {
      // ignore storage failures
    }
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#0B1120' : '#2E313A');
  }, [theme]);

  const toggleTheme = () => setTheme((t) => (t === 'dark' ? 'light' : 'dark'));

  const setSession = (s: AuthSession | null) => {
    setSessionState(s);
    saveSession(s);
  };

  const value = useMemo<AppState>(
    () => ({
      student,
      setStudent,
      onboardingAnswers,
      setOnboardingAnswers,
      diagnosticResults,
      setDiagnosticResults,
      session,
      setSession,
      theme,
      toggleTheme,
      journey: {
        hasCompletedOnboarding: onboardingAnswers !== null,
        hasCompletedDiagnostic: diagnosticResults !== null,
        hasCompletedLearning,
        hasCompletedPractice,
        hasCompletedSimulation,
        hasCompletedReview,
      },
      markLearningComplete: () => setHasCompletedLearning(true),
      markPracticeComplete: () => setHasCompletedPractice(true),
      markSimulationComplete: () => setHasCompletedSimulation(true),
      markReviewComplete: () => setHasCompletedReview(true),
    }),
    [
      student,
      onboardingAnswers,
      diagnosticResults,
      session,
      theme,
      hasCompletedLearning,
      hasCompletedPractice,
      hasCompletedSimulation,
      hasCompletedReview,
    ]
  );

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useApp() {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useApp must be used within AppProvider');
  return ctx;
}

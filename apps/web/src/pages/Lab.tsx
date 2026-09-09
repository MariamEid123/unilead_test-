import { useEffect, useMemo, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import ProgressBar from '../components/ui/ProgressBar';
import { LoadingState, ErrorState, EmptyState } from '../components/ui/StateViews';
import {
  getLabManifest,
  getLabProgress,
  runLabCode,
  submitLabSolution,
  getLabHint,
  askLabCoach,
} from '../data/mockApi';
import { getCourseById } from '../data/courses';
import type {
  LabChallengeView,
  LabManifest,
  LabRunResult,
  LabSubmitResult,
  LabHintResult,
  LabAssistResult,
  LabProgress,
  LabDifficulty,
  LabChallengeType,
} from '../types';
import './Lab.css';

const TYPE_LABELS: Record<LabChallengeType, string> = {
  complete_code: 'Complete',
  debug: 'Debug',
  output_prediction: 'Predict',
  challenge: 'Challenge',
};

const DIFFICULTY_TONE: Record<LabDifficulty, 'success' | 'warning' | 'danger'> = {
  easy: 'success',
  medium: 'warning',
  hard: 'danger',
};

const DEPTH_LABELS: Record<LabAssistResult['depth'], string> = {
  hint: 'Hint',
  explain: 'Explain',
  deeper: 'Deeper',
  solution: 'Solution',
};

const DEPTH_ORDER: LabAssistResult['depth'][] = ['hint', 'explain', 'deeper', 'solution'];

interface CodeEditorProps {
  value: string;
  onChange: (value: string) => void;
  highlightLine: number | null;
  disabled?: boolean;
}

// Small dependency-free code editor: a monospace textarea with a synced line
// gutter, Tab-key indentation, and a highlighted "problem line" that the lab
// derives from real compiler/runtime errors.
function CodeEditor({ value, onChange, highlightLine, disabled }: CodeEditorProps) {
  const gutterRef = useRef<HTMLDivElement>(null);
  const textRef = useRef<HTMLTextAreaElement>(null);

  const lines = useMemo(() => value.split('\n'), [value]);
  const pad = String(lines.length).length;

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === 'Tab') {
      e.preventDefault();
      const el = e.currentTarget;
      const start = el.selectionStart ?? 0;
      const end = el.selectionEnd ?? 0;
      const next = `${value.slice(0, start)}  ${value.slice(end)}`;
      onChange(next);
      requestAnimationFrame(() => {
        el.selectionStart = el.selectionEnd = start + 2;
      });
    }
  }

  function syncScroll() {
    if (gutterRef.current && textRef.current) {
      gutterRef.current.scrollTop = textRef.current.scrollTop;
    }
  }

  return (
    <div className="lab__editor">
      <div
        ref={gutterRef}
        className="lab__gutter"
        role="presentation"
        aria-hidden="true"
      >
        {lines.map((_, i) => (
          <span
            key={i}
            className={`lab__gutter-line ${i + 1 === highlightLine ? 'lab__gutter-line--error' : ''}`}
          >
            {String(i + 1).padStart(pad, '0')}
          </span>
        ))}
      </div>
      <textarea
        ref={textRef}
        className="lab__textarea"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onScroll={syncScroll}
        onKeyDown={handleKeyDown}
        spellCheck={false}
        autoCapitalize="off"
        autoCorrect="off"
        disabled={disabled}
        wrap="off"
      />
    </div>
  );
}

// Pulls the first "line N" out of a Python traceback/compile message so the
// editor can point at it in the gutter. Returns null when nothing matches.
function errorLineFrom(message: string | undefined | null): number | null {
  if (!message) return null;
  const match = message.match(/line\s+(\d+)/i);
  return match ? Number(match[1]) : null;
}

export default function Lab() {
  const navigate = useNavigate();
  const { courseId } = useParams();
  const course = courseId ? getCourseById(courseId) : undefined;
  const isCse014 = course?.code === 'CSE014';

  const [manifest, setManifest] = useState<LabManifest | null>(null);
  const [progress, setProgress] = useState<LabProgress | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);

  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [codeByChallenge, setCodeByChallenge] = useState<Record<string, string>>({});
  const [stdin, setStdin] = useState('');
  const [solved, setSolved] = useState<Set<string>>(new Set());

  const [runResult, setRunResult] = useState<LabRunResult | null>(null);
  const [submitResult, setSubmitResult] = useState<LabSubmitResult | null>(null);
  const [mcqIndex, setMcqIndex] = useState<number | null>(null);
  const [hints, setHints] = useState<LabHintResult[]>([]);
  const [coach, setCoach] = useState<LabAssistResult | null>(null);
  const [busy, setBusy] = useState<'run' | 'submit' | 'hint' | 'coach' | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoadError(null);
    Promise.all([getLabManifest(), getLabProgress()])
      .then(([m, p]) => {
        if (cancelled) return;
        setManifest(m);
        setProgress(p);
        setSelectedId((prev) => prev ?? m.challenges[0]?.id ?? null);
      })
      .catch((err) => {
        if (!cancelled) setLoadError(err instanceof Error ? err.message : 'Could not load the lab.');
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const challenge: LabChallengeView | undefined = useMemo(
    () => manifest?.challenges.find((c) => c.id === selectedId),
    [manifest, selectedId]
  );

  const grouped = useMemo(() => {
    if (!manifest) return [];
    return manifest.lessons
      .map((lesson) => ({
        lesson,
        challenges: manifest.challenges.filter((c) => c.lessonCode === lesson.code),
      }))
      .filter((g) => g.challenges.length > 0);
  }, [manifest]);

  const code = challenge ? (codeByChallenge[challenge.id] ?? challenge.starterCode ?? '') : '';
  const isMcq = challenge?.type === 'output_prediction';

  // Live "problem line" for the editor gutter, taken from the newest real
  // error the student has produced (run-time traceback first, then compile).
  const errorSource = runResult?.stderr?.trim()
    ? runResult.stderr
    : submitResult?.compileError ?? null;
  const highlightLine = errorLineFrom(errorSource);

  useEffect(() => {
    setRunResult(null);
    setSubmitResult(null);
    setMcqIndex(null);
    setHints([]);
    setCoach(null);
    setStdin('');
  }, [selectedId]);

  function updateCode(id: string, value: string) {
    setCodeByChallenge((prev) => ({ ...prev, [id]: value }));
  }

  async function refreshProgress() {
    try {
      setProgress(await getLabProgress());
    } catch {
      // Non-fatal: the lab stays usable, stats just lag a refresh.
    }
  }

  async function handleRun() {
    if (!challenge || busy) return;
    setBusy('run');
    setSubmitResult(null);
    try {
      setRunResult(await runLabCode(code, stdin));
    } catch (err) {
      setRunResult({
        status: 'internal_error',
        stdout: '',
        stderr: '',
        exitCode: null,
        durationMs: 0,
        detail: err instanceof Error ? err.message : 'The run failed unexpectedly.',
      });
    } finally {
      setBusy(null);
    }
  }

  async function handleSubmit() {
    if (!challenge || busy) return;
    setBusy('submit');
    try {
      const source = isMcq ? null : code;
      const selectedIndex = isMcq ? mcqIndex : null;
      const result = await submitLabSolution(challenge.id, source, selectedIndex);
      setSubmitResult(result);
      if (result.verdict === 'passed' || result.verdict === 'correct') {
        setSolved((prev) => new Set(prev).add(challenge.id));
        void refreshProgress();
      }
    } catch (err) {
      setSubmitResult({
        verdict: 'rejected',
        testsPassed: 0,
        testsTotal: 0,
        reports: [],
        compileError: null,
        correctIndex: null,
        explanation: '',
        feedback: err instanceof Error ? err.message : 'Submission failed unexpectedly.',
        newlyPassed: false,
      });
    } finally {
      setBusy(null);
    }
  }

  async function handleHint() {
    if (!challenge || busy) return;
    setBusy('hint');
    try {
      const used = Math.min(hints.length, 3);
      const hint = await getLabHint(
        challenge.id,
        used === 0 ? 'general' : used === 1 ? 'specific' : 'solution',
        used
      );
      setHints((prev) => [...prev, hint]);
    } catch (err) {
      const broken: LabHintResult = {
        challengeId: challenge.id,
        level: 'general',
        text: err instanceof Error ? err.message : 'Could not fetch a hint.',
        hintsUsed: hints.length,
        remaining: 0,
      };
      setHints((prev) => [...prev, broken]);
    } finally {
      setBusy(null);
    }
  }

  async function handleCoach(question: string, depth: LabAssistResult['depth']) {
    if (!challenge || !question.trim() || busy) return;
    setBusy('coach');
    try {
      setCoach(
        await askLabCoach({
          question: question.trim(),
          code,
          error: errorSource ?? '',
          depth,
          challengeId: challenge.id,
        })
      );
    } catch (err) {
      setCoach({
        depth,
        text: err instanceof Error ? err.message : 'The coach could not respond right now.',
        suggestions: [],
      });
    } finally {
      setBusy(null);
    }
  }

  const verdictTone = submitResult
    ? ['passed', 'correct'].includes(submitResult.verdict)
      ? 'success'
      : submitResult.verdict === 'rejected'
        ? 'neutral'
        : 'danger'
    : 'neutral';

  if (loadError) {
    return (
      <div className="page-narrow">
        <ErrorState
          message={loadError}
          onRetry={() => {
            setLoadError(null);
            setManifest(null);
            setProgress(null);
            window.location.reload();
          }}
        />
      </div>
    );
  }

  if (!manifest) {
    return (
      <div className="page-narrow">
        <LoadingState message="Loading the lab…" />
      </div>
    );
  }

  if (!isCse014) {
    return (
      <div className="page-narrow">
        <button className="lab__back" type="button" onClick={() => navigate(courseId ? `/courses/${courseId}` : '/courses')}>
          ← Back to {course?.title ?? 'Courses'}
        </button>
        <EmptyState
          icon="🧪"
          title="No lab for this course yet"
          message="The interactive code lab currently ships with Structured Programming (CSE014). Head there to write and run real Python against graded challenges."
          action={<Button onClick={() => navigate('/courses')}>Browse courses</Button>}
        />
      </div>
    );
  }

  return (
    <div className="page lab">
      <button className="lab__back" type="button" onClick={() => navigate(courseId ? `/courses/${courseId}` : '/courses')}>
        ← Back to {course?.title ?? 'Courses'}
      </button>
      <div className="lab__eyebrow">{course?.title ?? 'Structured Programming'}</div>
      <div className="lab__title-row">
        <h1 className="lab__title">Coding Lab</h1>
        <Badge tone="accent">{manifest.runtimeLabel}</Badge>
      </div>
      <p className="muted lab__subtitle">
        Write Python, press <strong>Run</strong> to execute it for real in a sandbox, then{' '}
        <strong>Submit</strong> to have it graded against hidden tests. Stuck? Ask for a hint —
        the Coach explains in your own code&apos;s context.
      </p>

      {progress && (
        <Card padding="md" className="lab__progress-card">
          <div className="lab__progress-strip">
            <div className="lab__progress-stat">
              <strong>{progress.attempted}</strong>
              <span>of {progress.totalChallenges} started</span>
            </div>
            <div className="lab__progress-stat">
              <strong>{progress.passed}</strong>
              <span>passed</span>
            </div>
            <div className="lab__progress-stat">
              <strong>{progress.accuracyPct}%</strong>
              <span>accuracy</span>
            </div>
            <div className="lab__progress-stat">
              <strong>{progress.streakDays}d</strong>
              <span>daily streak</span>
            </div>
            <div className="lab__progress-stat">
              <strong>{progress.currentDifficulty}</strong>
              <span>current level</span>
            </div>
            <div className="lab__progress-bar">
              <ProgressBar value={progress.progressPct} label="Lab progress" />
            </div>
          </div>
        </Card>
      )}

      <div className="lab__layout">
        <aside className="lab__sidebar" aria-label="Challenges by lesson">
          {grouped.map((group) => {
            const solvedCount = group.challenges.filter((c) => solved.has(c.id)).length;
            return (
              <div className="lab__lesson" key={group.lesson.code}>
                <div className="lab__lesson-head">
                  <span className="lab__lesson-code">{group.lesson.code}</span>
                  <span className="lab__lesson-title">{group.lesson.title}</span>
                  {solvedCount > 0 && (
                    <span className="lab__lesson-count">
                      {solvedCount}/{group.challenges.length}
                    </span>
                  )}
                </div>
                <ul className="lab__challenge-list">
                  {group.challenges.map((c) => (
                    <li key={c.id}>
                      <button
                        type="button"
                        className={`lab__challenge ${selectedId === c.id ? 'lab__challenge--active' : ''}`}
                        onClick={() => setSelectedId(c.id)}
                      >
                        <span className="lab__challenge-check" aria-hidden="true">
                          {solved.has(c.id) ? '✓' : ''}
                        </span>
                        <span className="lab__challenge-text">
                          <strong>{TYPE_LABELS[c.type]}</strong>
                          <span>{c.title}</span>
                        </span>
                        <Badge tone={DIFFICULTY_TONE[c.difficulty]}>{c.difficulty}</Badge>
                      </button>
                    </li>
                  ))}
                </ul>
              </div>
            );
          })}
          {progress && progress.weakTopics.length > 0 && (
            <div className="lab__weak">
              <span className="lab__weak-label">Focus on</span>
              <div className="lab__weak-tags">
                {progress.weakTopics.slice(0, 3).map((t) => (
                  <Badge key={t} tone="warning">{t}</Badge>
                ))}
              </div>
            </div>
          )}
        </aside>

        <main className="lab__workspace">
          {!challenge ? (
            <EmptyState icon="🧪" title="No challenges yet" message="This course has no published lab challenges." />
          ) : (
            <>
              <Card padding="lg" className="lab__brief">
                <div className="lab__brief-top">
                  <span className="lab__brief-eyebrow">
                    {challenge.lessonCode} · {challenge.topic}
                  </span>
                  <div className="lab__brief-badges">
                    <Badge tone="primary">{TYPE_LABELS[challenge.type]}</Badge>
                    <Badge tone={DIFFICULTY_TONE[challenge.difficulty]}>{challenge.difficulty}</Badge>
                    {solved.has(challenge.id) && <Badge tone="success">Solved</Badge>}
                  </div>
                </div>
                <h2 className="lab__brief-title">{challenge.title}</h2>
                <p className="lab__brief-prompt">{challenge.prompt}</p>
                {challenge.type === 'output_prediction' && challenge.codeText && (
                  <pre className="lab__code-preview">{challenge.codeText}</pre>
                )}
              </Card>

              {challenge.type === 'output_prediction' ? (
                <Card padding="lg" className="lab__mcq">
                  <h3 className="lab__section-title">What will this program print?</h3>
                  <div className="lab__options" role="radio" aria-label="Answer choices">
                    {challenge.options?.map((option, i) => {
                      const selected = mcqIndex === i;
                      const showCorrect = submitResult != null;
                      const isAnswer = submitResult?.correctIndex === i;
                      return (
                        <label
                          key={i}
                          className={`lab__option ${
                            showCorrect && isAnswer
                              ? 'lab__option--correct'
                              : showCorrect && selected
                                ? 'lab__option--wrong'
                                : selected
                                  ? 'lab__option--selected'
                                  : ''
                          }`}
                        >
                          <input
                            type="radio"
                            name="mcq"
                            checked={selected}
                            disabled={submitResult != null}
                            onChange={() => setMcqIndex(i)}
                          />
                          <span className="lab__option-text">
                            <span className="lab__option-key">{String.fromCharCode(65 + i)}</span>
                            <span className="lab__option-code">{option}</span>
                            {showCorrect && isAnswer && <span className="lab__option-tag">correct</span>}
                            {showCorrect && selected && !isAnswer && <span className="lab__option-tag">you picked this</span>}
                          </span>
                        </label>
                      );
                    })}
                  </div>
                  <Button onClick={handleSubmit} disabled={mcqIndex === null || busy !== null} loading={busy === 'submit'}>
                    Submit Answer
                  </Button>
                </Card>
              ) : (
                <Card padding="lg" className="lab__editor-card">
                  <div className="lab__editor-head">
                    <span className="lab__section-title">Your code</span>
                    <span className="lab__editor-meta muted">Python 3 · sandboxed</span>
                  </div>
                  <CodeEditor
                    value={code}
                    onChange={(v) => updateCode(challenge.id, v)}
                    highlightLine={highlightLine}
                    disabled={busy !== null}
                  />
                  {highlightLine !== null && (
                    <p className="lab__error-line-note muted">
                      The error points at line {highlightLine}. Read it carefully and fix that line, then re-run.
                    </p>
                  )}
                  <details className="lab__stdin">
                    <summary>Program input (stdin) — for experimenting with input()</summary>
                    <textarea
                      className="lab__stdin-input"
                      value={stdin}
                      onChange={(e) => setStdin(e.target.value)}
                      rows={3}
                      placeholder={'Ahmed\n19'}
                      disabled={busy !== null}
                    />
                  </details>
                  <div className="lab__actions">
                    <Button variant="secondary" onClick={handleRun} disabled={busy !== null} loading={busy === 'run'}>
                      Run code
                    </Button>
                    <Button onClick={handleSubmit} disabled={busy !== null} loading={busy === 'submit'}>
                      Submit for grading
                    </Button>
                    <Button variant="ghost" onClick={handleHint} disabled={busy !== null} loading={busy === 'hint'}>
                      Hint {hints.length > 0 ? hints.length + 1 : ''} of 3
                    </Button>
                  </div>
                </Card>
              )}

              {runResult && (
                <Card padding="md" className="lab__console">
                  <div className="lab__console-head">
                    <span className="lab__section-title">Run output</span>
                    <span className="muted">{runResult.durationMs} ms</span>
                  </div>
                  {runResult.status === 'ok' ? (
                    <pre className={`lab__mono ${runResult.stdout ? '' : 'lab__mono--empty'}`}>
                      {runResult.stdout || 'No output — your program printed nothing.'}
                    </pre>
                  ) : (
                    <>
                      {runResult.stderr && <pre className="lab__mono lab__mono--error">{runResult.stderr}</pre>}
                      <p className="lab__console-note">
                        {runResult.status === 'compile_error' && 'Compile error — Python could not parse your program.'}
                        {runResult.status === 'runtime_error' && 'Runtime error — the program crashed while running.'}
                        {runResult.status === 'timeout' && 'Timed out — the program did not finish within the limit.'}
                        {runResult.status === 'rejected' && 'Request rejected by the sandbox.'}
                        {runResult.status === 'internal_error' && (runResult.detail || 'The sandbox could not run your program.')}
                      </p>
                    </>
                  )}
                </Card>
              )}

              {submitResult && (
                <Card padding="md" className="lab__submit">
                  <div className="lab__submit-head">
                    <Badge tone={verdictTone}>{submitResult.verdict.toUpperCase()}</Badge>
                    {challenge.type !== 'output_prediction' && (
                      <span className="muted">
                        {submitResult.testsPassed}/{submitResult.testsTotal} tests passing
                      </span>
                    )}
                    {submitResult.newlyPassed && <Badge tone="success">First pass — recorded</Badge>}
                  </div>
                  {submitResult.feedback && <p className="lab__submit-feedback">{submitResult.feedback}</p>}

                  {submitResult.reports.length > 0 && (
                    <div className="lab__reports">
                      {submitResult.reports.map((report, i) => (
                        <div key={i} className={`lab__report ${report.passed ? 'lab__report--pass' : 'lab__report--fail'}`}>
                          <div className="lab__report-head">
                            <span>Test {i + 1}</span>
                            <span>{report.passed ? '✓ passed' : '✗ mismatch'}</span>
                          </div>
                          {!report.passed && (
                            <div className="lab__report-cols">
                              <div><span>Input</span><pre>{report.input}</pre></div>
                              <div><span>Expected</span><pre>{report.expected}</pre></div>
                              <div><span>Got</span><pre>{report.got}</pre></div>
                            </div>
                          )}
                          {report.note && <p className="muted">{report.note}</p>}
                        </div>
                      ))}
                    </div>
                  )}

                  {submitResult.explanation && <p className="lab__submit-explanation">{submitResult.explanation}</p>}
                  {submitResult.compileError && <pre className="lab__mono lab__mono--error">{submitResult.compileError}</pre>}
                </Card>
              )}

              {hints.length > 0 && (
                <Card padding="md" className="lab__hints">
                  <span className="lab__section-title">Hints revealed</span>
                  <ol className="lab__hints-list">
                    {hints.map((hint, i) => (
                      <li key={i} className={`lab__hint lab__hint--${hint.level}`}>
                        <Badge tone={hint.level === 'general' ? 'neutral' : hint.level === 'specific' ? 'warning' : 'danger'}>
                          {hint.level}
                        </Badge>
                        <span>{hint.text}</span>
                      </li>
                    ))}
                  </ol>
                </Card>
              )}

              <Card padding="lg" className="lab__coach">
                <span className="lab__section-title">Coach — your code, explained</span>
                <div className="lab__coach-body">
                  <div className="lab__coach-depth" role="group" aria-label="Coach depth">
                    {DEPTH_ORDER.map((depth) => (
                      <Button
                        key={depth}
                        size="sm"
                        variant={coach?.depth === depth ? 'secondary' : 'ghost'}
                        onClick={() => handleCoach(prefillQuestion(), depth)}
                        disabled={busy !== null || !challenge}
                      >
                        {DEPTH_LABELS[depth]}
                      </Button>
                    ))}
                  </div>
                  {coach && (
                    <div className={`lab__coach-response lab__coach-response--${coach.depth}`}>
                      <span className="muted">{DEPTH_LABELS[coach.depth]}</span>
                      <p>{coach.text}</p>
                      {coach.suggestions.length > 0 && (
                        <ul className="lab__coach-suggestions">
                          {coach.suggestions.map((s, i) => (
                            <li key={i}>{s}</li>
                          ))}
                        </ul>
                      )}
                    </div>
                  )}
                </div>
              </Card>
            </>
          )}
        </main>
      </div>
    </div>
  );

  function prefillQuestion(): string {
    if (challenge?.type === 'output_prediction') {
      return 'Walk me through what this program does, in order.';
    }
    const err = errorSource;
    return err
      ? `My code fails with this error:\n${err.slice(0, 400)}\nWhat went wrong?`
      : `I'm stuck on "${challenge?.title ?? 'this challenge'}". What should I try first?`;
  }
}
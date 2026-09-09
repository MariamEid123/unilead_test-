import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import ProgressBar from '../components/ui/ProgressBar';
import CompetencyCard from '../components/domain/CompetencyCard';
import { LoadingState, ErrorState } from '../components/ui/StateViews';
import { getStudent } from '../data/mockApi';
import { COURSE_CATALOG } from '../data/courses';
import { useApp } from '../state/AppContext';
import type { AsyncState, CourseProgress, Student } from '../types';
import './ProgressOverview.css';

function subjectLabel(progress: CourseProgress) {
  return COURSE_CATALOG.find(
    (course) => course.id === progress.courseId || course.title === progress.courseTitle
  )?.subject ?? progress.courseTitle;
}

function activityLabel(completed: number | null, total: number | null) {
  return completed !== null && total !== null ? `${completed}/${total}` : 'Not available yet';
}

export default function ProgressOverview() {
  const navigate = useNavigate();
  const { student, setStudent, journey } = useApp();
  const [state, setState] = useState<AsyncState<Student>>({ status: 'loading' });

  async function load() {
    setState({ status: 'loading' });
    try {
      const s = student ?? (await getStudent());
      if (!student) setStudent(s);
      setState({ status: 'success', data: s });
    } catch (err) {
      setState({
        status: 'error',
        message: err instanceof Error ? err.message : 'Could not load your progress.',
      });
    }
  }

  useEffect(() => {
    load();
    // Reload whenever the persisted student changes (e.g. after completing Review),
    // so progress reflects the latest evidence-driven update.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [student]);

  if (state.status === 'loading' || state.status === 'idle') {
    return (
      <div className="page">
        <LoadingState message="Loading your progress…" />
      </div>
    );
  }

  if (state.status === 'error') {
    return (
      <div className="page">
        <ErrorState message={state.message} onRetry={load} />
      </div>
    );
  }

  const s = state.data;
  const journeySteps = [
    { label: 'Find your starting point', done: journey.hasCompletedDiagnostic, href: '/my-learning/diagnostic' },
    { label: 'Choose a course', done: journey.hasCompletedLearning, href: '/courses' },
    { label: 'Practice with feedback', done: journey.hasCompletedPractice, href: '/my-learning/practice' },
    { label: 'Run the simulation', done: journey.hasCompletedSimulation, href: '/apply-review/simulation' },
    { label: 'Review your evidence', done: journey.hasCompletedReview, href: '/apply-review/review' },
  ];
  const nextStep = journeySteps.find((step) => !step.done) ?? null;
  return (
    <div className="page">
      <button className="progress-overview__back" type="button" onClick={() => navigate('/home')}>← Back</button>
      <div className="progress-overview__header">
        <h1 className="progress-overview__title">Your Progress</h1>
        <p className="muted">Progress is reported separately for each subject.</p>
      </div>

      <section className="progress-overview__subjects" aria-labelledby="subject-progress-title">
        <h2 id="subject-progress-title" className="progress-overview__subheading">Subject progress</h2>
        {s.courseProgress.length === 0 ? (
          <Card padding="lg"><p className="muted">No subject activity is available yet.</p></Card>
        ) : (
          <div className="grid grid-2 progress-overview__grid">
            {s.courseProgress.map((progress) => (
              <Card padding="lg" key={progress.courseId} className="progress-overview__subject-card">
                <span className="progress-overview__kicker">{subjectLabel(progress)}</span>
                <h3>{progress.courseTitle}</h3>
                <strong className="progress-overview__percentage">{progress.progressPercentage ?? 0}% Complete</strong>
                <ProgressBar value={progress.progressPercentage ?? 0} label={`${subjectLabel(progress)} progress`} tone="primary" size="md" />
                <dl className="progress-overview__activity-breakdown">
                  <div><dt>Lectures</dt><dd>{activityLabel(progress.completedLectures, progress.totalLectures)}</dd></div>
                  <div><dt>Quizzes</dt><dd>{activityLabel(progress.completedQuizzes, progress.totalQuizzes)}</dd></div>
                  <div><dt>Assignments</dt><dd>{activityLabel(progress.completedAssignments, progress.totalAssignments)}</dd></div>
                </dl>
              </Card>
            ))}
          </div>
        )}
      </section>

      <div className="progress-overview__dashboard-grid">
        <Card padding="lg" className="progress-overview__journey">
          <div className="progress-overview__section-heading"><div><span className="progress-overview__kicker">Your path</span><h2>Learning journey</h2></div><span className="muted">{journeySteps.filter((step) => step.done).length}/{journeySteps.length}</span></div>
          <ol className="progress-overview__journey-list">
            {journeySteps.map((step, index) => { const current = !step.done && journeySteps.slice(0, index).every((item) => item.done); return <li key={step.label} className={step.done ? 'is-done' : current ? 'is-current' : 'is-upcoming'}><button type="button" onClick={() => navigate(step.href)}><span className="progress-overview__journey-symbol" aria-hidden="true">{step.done ? '✓' : current ? '→' : '○'}</span><span>{step.label}</span></button></li>; })}
          </ol>
        </Card>
        <Card padding="lg" className="progress-overview__next">
          <span className="progress-overview__kicker">Your next step</span>
          {nextStep ? <><h2>{nextStep.label}</h2><p>Follow the path one step at a time. Your next activity is ready.</p><Button onClick={() => navigate(nextStep.href)}>Continue →</Button></> : <><h2>You are all caught up.</h2><p>Review your skills or return home to choose another activity.</p><Button onClick={() => navigate('/home')}>Back to Home →</Button></>}
        </Card>
      </div>

      <h2 className="progress-overview__subheading">Competencies</h2>
      <div className="grid grid-2 progress-overview__grid">
        {s.competencies.map((c) => (
          <CompetencyCard key={c.id} competency={c} />
        ))}
      </div>
    </div>
  );
}

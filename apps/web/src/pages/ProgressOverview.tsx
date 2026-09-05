import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import ProgressBar from '../components/ui/ProgressBar';
import CompetencyCard from '../components/domain/CompetencyCard';
import { LoadingState, ErrorState } from '../components/ui/StateViews';
import { getStudent } from '../data/mockApi';
import { useApp } from '../state/AppContext';
import type { AsyncState, Student } from '../types';
import './ProgressOverview.css';

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
  const completedActivities = [
    journey.hasCompletedLearning && 'Learning',
    journey.hasCompletedPractice && 'Practice',
    journey.hasCompletedSimulation && 'Simulation',
    journey.hasCompletedReview && 'Review',
  ].filter(Boolean) as string[];
  const journeySteps = [
    { label: 'Find your starting point', done: journey.hasCompletedDiagnostic, href: '/my-learning/diagnostic' },
    { label: 'Learn the core idea', done: journey.hasCompletedLearning, href: '/my-learning/learning' },
    { label: 'Practice with feedback', done: journey.hasCompletedPractice, href: '/my-learning/practice' },
    { label: 'Run the simulation', done: journey.hasCompletedSimulation, href: '/apply-review/simulation' },
    { label: 'Review your evidence', done: journey.hasCompletedReview, href: '/apply-review/review' },
  ];
  const nextStep = journeySteps.find((step) => !step.done) ?? null;
  const isComplete = s.overallProgress >= 100;

  return (
    <div className="page">
      <button className="progress-overview__back" type="button" onClick={() => navigate('/home')}>← Back</button>
      <div className="progress-overview__header">
        <h1 className="progress-overview__title">Your Progress</h1>
        <p className="muted">{s.course.code} — {s.course.title}</p>
      </div>

      {isComplete ? (
        <Card padding="lg" className="progress-overview__complete">
          <div className="progress-overview__complete-icon" aria-hidden="true">✓</div>
          <div><h2>Learning journey completed</h2><p className="muted">You completed the activities in this learning path.</p></div>
          <Button onClick={() => navigate('/home')}>Back to Home →</Button>
        </Card>
      ) : (
        <Card padding="lg" className="progress-overview__summary">
          <div className="progress-overview__summary-top"><div><span className="progress-overview__summary-label">Overall learning progress</span><strong className="progress-overview__percentage">{s.overallProgress}%</strong></div><span className="muted">Keep going</span></div>
          <ProgressBar value={s.overallProgress} label="Overall Course Progress" tone="primary" size="md" />
        </Card>
      )}

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

      {completedActivities.length > 0 && <Card padding="lg" className="progress-overview__activities"><div className="progress-overview__section-heading"><div><span className="progress-overview__kicker">What you have done</span><h2>Completed activities</h2></div></div><div className="progress-overview__activity-list">{completedActivities.map((activity) => <span key={activity} className="progress-overview__activity">✓ {activity}</span>)}</div></Card>}

      <h2 className="progress-overview__subheading">Competencies</h2>
      <div className="grid grid-2 progress-overview__grid">
        {s.competencies.map((c) => (
          <CompetencyCard key={c.id} competency={c} />
        ))}
      </div>

      <div className="progress-overview__cta">
        <Button variant="secondary" onClick={() => navigate('/progress/competency-profile')}>
          View Full Competency Profile
        </Button>
      </div>
    </div>
  );
}

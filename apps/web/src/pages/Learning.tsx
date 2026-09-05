import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Sidebar from '../components/layout/Sidebar';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { LoadingState, ErrorState } from '../components/ui/StateViews';
import { useApp } from '../state/AppContext';
import { getLesson, getStudent } from '../data/mockApi';
import type { AsyncState, LessonSection, Student } from '../types';
import './Learning.css';

export default function Learning() {
  const navigate = useNavigate();
  const { student, setStudent, markLearningComplete } = useApp();
  const [state, setState] = useState<AsyncState<{ student: Student; sections: LessonSection[] }>>({
    status: 'loading',
  });

  async function load() {
    setState({ status: 'loading' });
    try {
      const s = student ?? (await getStudent());
      const activeCompetency = s.competencies.find((c) => c.status === 'DEVELOPING') ?? s.competencies[0]!;
      const sections = await getLesson(activeCompetency.id);
      if (!student) setStudent(s);
      setState({ status: 'success', data: { student: s, sections } });
    } catch (err) {
      setState({
        status: 'error',
        message: err instanceof Error ? err.message : 'Could not load this lesson.',
      });
    }
  }

  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (state.status === 'loading' || state.status === 'idle') {
    return (
      <div className="page">
        <LoadingState message="Loading your lesson…" />
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

  const { student: s, sections } = state.data;
  const activeCompetency = s.competencies.find((c) => c.status === 'DEVELOPING') ?? s.competencies[0]!;

  return (
    <div className="page learning">
      <button className="learning__back" type="button" onClick={() => navigate('/my-learning')}>← Back</button>
      <div className="learning__eyebrow">{s.course.code}</div>
      <h1 className="learning__title">{activeCompetency.name}</h1>
      <div className="learning__path" aria-label="Learning path">
        <span className="learning__path-step learning__path-step--done">Learn</span>
        <span className="learning__path-arrow">→</span>
        <span className="learning__path-step learning__path-step--active">Understand</span>
        <span className="learning__path-arrow">→</span>
        <span className="learning__path-step">Try</span>
        <span className="learning__path-arrow">→</span>
        <span className="learning__path-step">Practice</span>
        <span className="learning__path-arrow">→</span>
        <span className="learning__path-step">Apply</span>
      </div>

      <div className="learning__layout">
        <Sidebar
          courseLabel={`${s.course.code} — ${s.course.title}`}
          competencies={s.competencies}
          activeCompetencyId={activeCompetency.id}
        />

        <div className="learning__content">
          <Card padding="lg" id="lesson-content">
            <div className="learning__lesson-intro">
              <span className="learning__lesson-label">Current lesson</span>
              <span className="learning__lesson-next">Next: Practice this skill</span>
            </div>
            {sections.map((sec) => (
              <div key={sec.id} className="learning__section">
                <h2 className="learning__section-heading">{sec.heading}</h2>
                <p className="learning__section-body muted">{sec.body}</p>
              </div>
            ))}
          </Card>

          <section className="learning__materials" aria-labelledby="materials-title">
            <div className="learning__materials-header">
              <div>
                <span className="learning__lesson-label">Use when you need another explanation</span>
                <h2 id="materials-title">Learning materials</h2>
              </div>
              <span className="muted learning__materials-count">3 resources</span>
            </div>
            <div className="learning__materials-grid">
              {[
                { type: 'Reading', title: `${activeCompetency.name}: the essentials`, detail: 'A short explanation of the core idea.', time: '8 min' },
                { type: 'Slides', title: 'Key ideas at a glance', detail: 'Review the concepts before you try them.', time: '5 min' },
                { type: 'Resource', title: 'Worked example', detail: 'See the reasoning step by step.', time: '6 min' },
              ].map((material) => (
                <article className="learning__material" key={material.type}>
                  <span className="learning__material-type">{material.type}</span>
                  <h3>{material.title}</h3>
                  <p className="muted">{material.detail}</p>
                  <div className="learning__material-footer">
                    <span className="muted">{material.time}</span>
                    <button type="button" className="learning__material-action" onClick={() => document.getElementById('lesson-content')?.scrollIntoView({ behavior: 'smooth' })}>View lesson</button>
                  </div>
                </article>
              ))}
            </div>
          </section>

          <div className="learning__actions">
            <Button variant="secondary" onClick={() => navigate('/my-learning/ai-coach')}>
              Ask AI Coach
            </Button>
            <Button
              onClick={() => {
                markLearningComplete();
                navigate('/my-learning/practice');
              }}
            >
              Next: Practice →
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

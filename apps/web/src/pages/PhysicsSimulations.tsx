import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import { getCourseById } from '../data/courses';
import { SIMULATIONS, simulationById } from '../simulations/registry';
import './Simulation.css';

// Physics 2 interactive simulation surface. Honest physics: the sims integrate
// the real equations of motion (see simulations/engine.ts) — nothing here is
// decorative or pre-baked.
export default function PhysicsSimulations({ courseId }: { courseId: string }) {
  const navigate = useNavigate();
  const course = getCourseById(courseId);
  const sims = SIMULATIONS;
  const [activeId, setActiveId] = useState(sims[0]?.id ?? null);
  const active = activeId ? simulationById(activeId) : undefined;
  const ActiveComponent = active?.Component;

  return (
    <div className="page-narrow simulation">
      <button className="simulation__back" type="button" onClick={() => navigate(courseId ? `/courses/${courseId}` : '/courses')}>
        ← Back to {course?.title ?? 'Courses'}
      </button>
      <div className="simulation__eyebrow">{course?.title ?? 'Physics Fundamentals'}</div>
      <h1 className="simulation__title">Physics 2 Simulation Lab</h1>
      <p className="muted simulation__subtitle">
        These experiments run real physics — the equations of motion are integrated numerically
        from Coulomb&apos;s law as your parameters change. Choose an experiment to get started.
      </p>

      <div className="physics-sims__picker" role="tablist" aria-label="Experiments">
        {sims.map((sim) => (
          <Card
            key={sim.id}
            interactive
            className={`physics-sims__card ${activeId === sim.id ? 'physics-sims__card--active' : ''}`}
            onClick={() => setActiveId(sim.id)}
            role="tab"
            aria-selected={activeId === sim.id}
          >
            <div className="physics-sims__card-top">
              <h3>{sim.title}</h3>
              <Badge tone="accent">interactive</Badge>
            </div>
            <p className="muted">{sim.objective}</p>
          </Card>
        ))}
      </div>

      {ActiveComponent && active ? (
        <>
          <div className="physics-sims__heading">
            <h2>{active.title}</h2>
            <Button variant="ghost" size="sm" onClick={() => navigate(`/courses/${courseId}`)}>
              Return to course
            </Button>
          </div>
          <ActiveComponent key={active.id} />
        </>
      ) : (
        <Card padding="lg">
          <p className="muted">No experiment selected.</p>
        </Card>
      )}
    </div>
  );
}
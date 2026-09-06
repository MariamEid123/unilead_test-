import { forwardRef } from 'react';
import { useNavigate } from 'react-router-dom';
import './JourneySection.css';

const STEPS = [
  { number: '01', label: 'Diagnostic', description: 'Find your starting point.', href: '/my-learning/diagnostic' },
  { number: '02', label: 'Courses', description: 'Choose a course and build the core idea.', href: '/courses' },
  { number: '03', label: 'Coach', description: 'Work through the hard part.', href: '/my-learning/ai-coach' },
  { number: '04', label: 'Practice', description: 'Apply it with feedback.', href: '/my-learning/practice' },
  { number: '05', label: 'Apply', description: 'Test it in a new context.', href: '/apply-review/simulation' },
  { number: '06', label: 'Demonstrate', description: 'Show what you can do.', href: '/apply-review/review' },
];

const JourneySection = forwardRef<HTMLElement, { activeStep?: number }>(function JourneySection({ activeStep = 1 }, ref) {
  const navigate = useNavigate();

  return (
    <section className="journey" id="how-it-works" ref={ref}>
      <div className="journey__inner">
        <h2 className="journey__title">Your Learning Journey</h2>
        <p className="journey__subtitle muted">
          Six steps. One goal: demonstrated competency.
        </p>

        <ol className="journey__timeline">
          {STEPS.map((step) => (
            <li key={step.number} className="journey__step">
              <button
                type="button"
                className={`journey__marker ${step.number === '06' ? 'journey__marker--final' : ''} ${Number(step.number) === activeStep ? 'journey__marker--active' : ''}`}
                onClick={() => navigate(step.href)}
                aria-label={`Go to ${step.label}`}
                aria-current={Number(step.number) === activeStep ? 'step' : undefined}
              >{step.number}</button>
              <div className="journey__step-body">
                <h3 className="journey__step-label">{step.label}</h3>
                <p className="muted journey__step-description">{step.description}</p>
              </div>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
});

export default JourneySection;

import { useNavigate } from 'react-router-dom';
import { useApp } from '../../state/AppContext';
import { buildJourneyStages, JOURNEY_STAGES } from './journeyStages';
import './JourneySection.css';

export default function JourneySection() {
  const navigate = useNavigate();
  const { student, journey } = useApp();

  const stages = buildJourneyStages(student, journey);
  const currentIndex = stages.findIndex((step) => step.status === 'current');
  const fillPercent = currentIndex === -1 ? 100 : (currentIndex / (JOURNEY_STAGES.length - 1)) * 100;

  return (
    <section className="journey" id="how-it-works">
      <div className="journey__inner">
        <div className="journey__heading">
          <h2 className="journey__title">Your Learning Journey</h2>
          <p className="journey__subtitle">See where you are and what comes next.</p>
        </div>

        <div className="journey__track">
          <span
            className="journey__line-fill"
            style={{ ['--fill' as string]: `${fillPercent}%`, ['--fill-w' as string]: `${fillPercent * 0.8}%` }}
            aria-hidden="true"
          />
          <ol className="journey__timeline">
            {stages.map((step) => (
              <li key={step.number} className={`journey__step journey__step--${step.status}`}>
                <button
                  type="button"
                  className={`journey__marker journey__marker--${step.status}`}
                  onClick={() => navigate(step.href)}
                  aria-label={`Go to ${step.label} (${step.status})`}
                  aria-current={step.status === 'current' ? 'step' : undefined}
                >
                  {step.status === 'completed' ? (
                    <svg viewBox="0 0 24 24" className="journey__check" aria-hidden="true">
                      <path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                  ) : (
                    step.number
                  )}
                </button>
                <div className="journey__step-body">
                  <h3 className="journey__step-label">{step.label}</h3>
                  <p className="journey__step-description">{step.description}</p>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </div>
    </section>
  );
}
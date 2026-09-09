import { useNavigate } from 'react-router-dom';
import Card from '../ui/Card';
import Button from '../ui/Button';
import './CoachCta.css';

export default function CoachCta() {
  const navigate = useNavigate();

  return (
    <section className="coach-cta" aria-labelledby="coach-cta-title">
      <div className="coach-cta__inner">
        <Card padding="lg" className="coach-cta__panel">
          <div className="coach-cta__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 3c3 0 5.5 2.2 5.5 5 0 1.2-.35 2.3-1 3.2.1 2.6-1.1 4.9-3 6.2a6.5 6.5 0 0 1-3 1.1" />
              <path d="M8.5 19.5h1.5M9 22h1.5" />
              <path d="M3 11a9 9 0 0 1 18 0" transform="none" />
              <path d="M5.5 15.5A14 14 0 0 1 3 13" transform="none" />
            </svg>
          </div>
          <div className="coach-cta__body">
            <h2 id="coach-cta-title" className="coach-cta__title">Need help understanding something?</h2>
            <p className="coach-cta__text">
              Your AI Coach is ready to explain, guide, and help you move forward.
            </p>
          </div>
          <Button variant="accent" size="lg" onClick={() => navigate('/my-learning/ai-coach')}>
            Ask Your AI Coach →
          </Button>
        </Card>
      </div>
    </section>
  );
}
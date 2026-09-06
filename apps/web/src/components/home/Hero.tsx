import { useNavigate } from 'react-router-dom';
import Button from '../ui/Button';
import './Hero.css';

interface HeroProps {
  primaryHref: string;
  primaryLabel: string;
  onExploreClick: () => void;
}

export default function Hero({ primaryHref, primaryLabel, onExploreClick }: HeroProps) {
  const navigate = useNavigate();

  return (
    <section className="hero">
      <div className="hero__inner">
        <div className="hero__copy">
          <h1 className="hero__headline">Learn. Practice. Prove Your Skills.</h1>
          <p className="hero__subtext">
            Understand it. Practice it. Prove it.
          </p>
          <div className="hero__actions">
            <Button variant="accent" size="lg" onClick={() => navigate(primaryHref)}>
              {primaryLabel} →
            </Button>
            <Button variant="ghost" size="lg" onClick={onExploreClick}>
              Explore How It Works
            </Button>
          </div>
        </div>

        <div className="hero__art">
          <img
            className="hero__logo-image"
            src="/unilead-logo.svg"
            alt="Areta — Learn, Practice, Lead"
          />
        </div>
      </div>
    </section>
  );
}

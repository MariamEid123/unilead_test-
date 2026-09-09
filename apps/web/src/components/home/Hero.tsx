import { useNavigate } from 'react-router-dom';
import Button from '../ui/Button';
import './Hero.css';

interface HeroProps {
  name?: string;
  message: string;
  primaryHref: string;
}

function timeGreeting() {
  const hour = new Date().getHours();
  if (hour < 5) return 'Good evening';
  if (hour < 12) return 'Good morning';
  if (hour < 18) return 'Good afternoon';
  return 'Good evening';
}

export default function Hero({ name, message, primaryHref }: HeroProps) {
  const navigate = useNavigate();
  const firstName = name ? name.trim().split(/\s+/)[0] : '';
  const greeting = `${timeGreeting()}${firstName ? `, ${firstName}` : ''} 👋`;

  return (
    <section className="hero">
      <div className="hero__inner">
        <div className="hero__copy">
          <span className="hero__greeting">{greeting}</span>
          <h1 className="hero__headline">
            {message}
          </h1>
          <div className="hero__actions">
            <Button variant="accent" size="lg" onClick={() => navigate(primaryHref)}>
              Continue Learning →
            </Button>
          </div>
        </div>

        <div className="hero__art">
          <img
            className="hero__logo-image"
            src="/logo.jpg"
            alt="Areta — Learn, Practice, Lead"
          />
        </div>
      </div>
    </section>
  );
}
import { useNavigate } from 'react-router-dom';
import Button from '../components/ui/Button';
import PageHeader from '../components/ui/PageHeader';
import './Plans.css';

const PLANS = [
  {
    name: 'Rush ARETE',
    description: 'Start your learning journey.',
    detail: 'First month free.',
    features: ['Access to available courses', 'Lectures', 'AI Learning Assistant', 'Basic quizzes'],
    action: 'Start for Free',
    featured: true,
  },
  {
    name: 'Plus',
    description: 'More room to grow as your learning expands.',
    detail: 'Coming Soon',
    features: [],
    action: 'Coming Soon',
    featured: false,
  },
  {
    name: 'Pro',
    description: 'A future experience for ambitious learners.',
    detail: 'Coming Soon',
    features: [],
    action: 'Coming Soon',
    featured: false,
  },
];

export default function Plans() {
  const navigate = useNavigate();

  return (
    <div className="page plans">
      <PageHeader
        eyebrow="Plans"
        title="Choose your learning path"
        subtitle="Start with the essentials today. More ways to learn are on the way."
      />

      <section className="plans__grid" aria-label="ARETE plans">
        {PLANS.map((plan) => (
          <article className={`plan-card ${plan.featured ? 'plan-card--featured' : ''}`} key={plan.name}>
            {plan.featured && <span className="plan-card__badge">Available now</span>}
            <div className="plan-card__heading">
              <h2>{plan.name}</h2>
              <p>{plan.description}</p>
            </div>
            <div className="plan-card__detail">{plan.detail}</div>
            <ul className="plan-card__features">
              {plan.features.map((feature) => (
                <li key={feature}><span aria-hidden="true">✓</span>{feature}</li>
              ))}
            </ul>
            <Button
              fullWidth
              variant={plan.featured ? 'primary' : 'secondary'}
              disabled={!plan.featured}
              onClick={plan.featured ? () => navigate('/courses') : undefined}
            >
              {plan.action}
            </Button>
          </article>
        ))}
      </section>
    </div>
  );
}
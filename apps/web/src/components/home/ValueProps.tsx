import { Link } from 'react-router-dom';
import './ValueProps.css';

const ITEMS = [
  {
    id: 'courses',
    title: 'Courses',
    description: 'Build strong foundations through focused, step-by-step learning.',
    href: '/courses',
  },
  {
    id: 'coach',
    title: 'AI Coach',
    description: 'Get explanations, hints, and support whenever you need them.',
    href: '/my-learning/ai-coach',
  },
  {
    id: 'practice',
    title: 'Practice & Apply',
    description: 'Turn what you learn into real skills through hands-on practice.',
    href: '/my-learning/practice',
  },
];

function ItemIcon({ name }: { name: string }) {
  switch (name) {
    case 'courses':
      return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
      );
    case 'coach':
      return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
          <path d="M9 10h6M9 14h4" />
        </svg>
      );
    default:
      return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="9" />
          <path d="M9 12l2 2 4-4" />
        </svg>
      );
  }
}

export default function ValueProps() {
  return (
    <section className="value-props">
      <div className="value-props__inner">
        <div className="value-props__heading">
          <h2 className="value-props__title">Your Path to Real Mastery</h2>
          <p className="value-props__subtitle">
            Learn the concepts. Practice the skills. Prove what you can do.
          </p>
        </div>

        <div className="value-props__grid">
          {ITEMS.map((item) => (
            <Link key={item.id} to={item.href} className="value-props__card">
              <div className="value-props__icon" aria-hidden="true">
                <ItemIcon name={item.id} />
              </div>
              <h3 className="value-props__card-title">{item.title}</h3>
              <p className="value-props__card-description">{item.description}</p>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}
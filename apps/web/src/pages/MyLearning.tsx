import PageHeader from '../components/ui/PageHeader';
import HubGrid from '../components/domain/HubGrid';

export default function MyLearning() {
  return (
    <div className="page">
      <PageHeader
        eyebrow="My Learning"
        title="Learn, get coached, and practice"
        subtitle="Move through your competencies at your own pace."
      />
      <HubGrid
        tiles={[
          {
            icon: '🧭',
            title: 'Diagnostic',
            description: 'Find out what you already know and where to start.',
            href: '/my-learning/diagnostic',
          },
          {
            icon: '📚',
            title: 'Courses',
            description: 'Choose a course and open its lectures.',
            href: '/courses',
          },
          {
            icon: '💬',
            title: 'AI Coach',
            description: 'Talk through your reasoning with a guided coach.',
            href: '/my-learning/ai-coach',
          },
          {
            icon: '✏️',
            title: 'Practice',
            description: 'Apply what you learned to a real task.',
            href: '/my-learning/practice',
          },
        ]}
      />
    </div>
  );
}

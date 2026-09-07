import { useNavigate } from 'react-router-dom';
import Card from '../ui/Card';
import Button from '../ui/Button';
import ProgressBar from '../ui/ProgressBar';
import { LoadingState, ErrorState } from '../ui/StateViews';
import type { AsyncState, Recommendation, Student } from '../../types';
import './PersonalizedSection.css';

interface PersonalizedSectionProps {
  state: AsyncState<{ student: Student; recommendation: Recommendation }>;
  onRetry: () => void;
}

export default function PersonalizedSection({ state, onRetry }: PersonalizedSectionProps) {
  return (
    <section className="personalized personalized--next-action">
      <div className="personalized__inner">
        <h2 className="personalized__title">Your Next Action</h2>

        {(state.status === 'loading' || state.status === 'idle') && (
          <Card padding="lg">
            <LoadingState message="Loading your progress…" />
          </Card>
        )}

        {state.status === 'error' && (
          <Card padding="lg">
            <ErrorState message={state.message} onRetry={onRetry} />
          </Card>
        )}

        {state.status === 'success' && (
          <PersonalizedContent student={state.data.student} recommendation={state.data.recommendation} />
        )}
      </div>
    </section>
  );
}

function PersonalizedContent({
  student,
  recommendation,
}: {
  student: Student;
  recommendation: Recommendation;
}) {
  const navigate = useNavigate();
  const activeCourseProgress = student.courseProgress.find(
    (progress) => progress.courseId === student.course.id
  );
  const progressPercentage = activeCourseProgress?.progressPercentage ?? null;

  return (
    <Card padding="lg" className="personalized__card">
      <div className="personalized__top">
        <div>
          <span className="personalized__course-code">Welcome back, {student.name}</span>
          <h3 className="personalized__course-title">{recommendation.title}</h3>
        </div>
        <div className="personalized__progress-figure">
          <span className="personalized__progress-number">
            {progressPercentage === null ? 'Not available yet' : `${progressPercentage}%`}
          </span>
          <span className="muted personalized__progress-label">Progress</span>
        </div>
      </div>

      {progressPercentage !== null && (
        <ProgressBar value={progressPercentage} showPercent={false} tone="primary" />
      )}

      <div className="personalized__grid">
        <div className="personalized__field">
          <span className="personalized__field-label">Available courses</span>
          <span className="personalized__field-value">Physics Fundamentals · Math Zero: Foundations</span>
        </div>
        <div className="personalized__field">
          <span className="personalized__field-label">Next step</span>
          <span className="personalized__field-value">{recommendation.title}</span>
        </div>
      </div>

      <p className="personalized__reason">
        <span className="personalized__reason-label">Why now: </span>
        {recommendation.reason}
      </p>

      <Button size="lg" onClick={() => navigate(recommendation.href)}>
        {recommendation.actionLabel} →
      </Button>
    </Card>
  );
}

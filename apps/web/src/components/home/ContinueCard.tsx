import { useNavigate } from 'react-router-dom';
import Card from '../ui/Card';
import Button from '../ui/Button';
import ProgressBar from '../ui/ProgressBar';
import { useApp } from '../../state/AppContext';
import { getContinueLesson } from './continueAction';
import './ContinueCard.css';

export default function ContinueCard() {
  const navigate = useNavigate();
  const { student } = useApp();

  const lesson = getContinueLesson(student);
  const needsCourse = !lesson;

  const href = needsCourse ? '/courses' : lesson.href;
  const buttonLabel = needsCourse ? 'Choose a Course →' : 'Continue →';

  return (
    <section className="continue-card" aria-labelledby="continue-card-title">
      <div className="continue-card__inner">
        <Card padding="lg" className="continue-card__panel">
          <div className="continue-card__context">
            <div className="continue-card__header">
              <div>
                <span className="continue-card__kicker">Continue Learning</span>
                <h2 id="continue-card-title" className="continue-card__title">
                  {needsCourse ? 'Start your first course' : lesson.courseTitle}
                </h2>
              </div>
              {!needsCourse && (
                <div className="continue-card__percent">
                  <strong>{lesson.percentage}%</strong>
                  <span>complete</span>
                </div>
              )}
            </div>

            {!needsCourse && (
              <>
                <div className="continue-card__row">
                  <div className="continue-card__label">Current Topic</div>
                  <div className="continue-card__value">{lesson.nextLessonTitle ?? 'Getting started'}</div>
                </div>

                <div className="continue-card__progress">
                  <ProgressBar value={lesson.percentage} showPercent={false} tone="primary" size="md" />
                </div>
              </>
            )}
          </div>

          <div className="continue-card__footer">
            <Button size="lg" onClick={() => navigate(href)}>
              {buttonLabel}
            </Button>
          </div>
        </Card>
      </div>
    </section>
  );
}
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '../ui/Button';
import ProgressBar from '../ui/ProgressBar';
import { COURSE_CATALOG, getCoursePercentage } from '../../data/courses';
import { useApp } from '../../state/AppContext';
import { getStudent } from '../../data/mockApi';
import './CourseSection.css';

export default function CourseSection() {
  const navigate = useNavigate();
  const { student, setStudent } = useApp();

  useEffect(() => {
    if (!student) {
      getStudent().then(setStudent).catch(() => {});
    }
  }, [student, setStudent]);

  return (
    <section className="home-courses" aria-labelledby="home-courses-title">
      <div className="home-courses__inner">
        <div className="home-courses__heading">
          <span className="home-courses__eyebrow">Build your foundations</span>
          <h2 id="home-courses-title">Explore Courses</h2>
          <p className="muted">Start with a focused course and keep your learning moving forward.</p>
        </div>

        <div className="home-courses__grid">
          {COURSE_CATALOG.map((course) => {
            const percentage = getCoursePercentage(student, course);
            const actionLabel = percentage > 0 ? 'Continue Course' : 'Explore Course';

            return (
              <article className="home-course-card" key={course.id}>
                <div className={`home-course-card__cover home-course-card__cover--${course.accent}`} aria-hidden="true">
                  <span>{course.subject}</span>
                  <strong>{course.accent === 'physics' ? 'F' : '0'}</strong>
                </div>
                <div className="home-course-card__body">
                  <div className="home-course-card__meta">
                    <span>{course.subject}</span>
                    <span>{course.lectures} lectures</span>
                  </div>
                  <h3>{course.title}</h3>
                  <p>{course.description}</p>

                  <div className="home-course-card__progress-block" aria-label={`${course.subject} progress: ${percentage}%`}>
                    <div className="home-course-card__progress-header">
                      <span className="home-course-card__progress-subject">{course.subject}</span>
                      <strong className="home-course-card__percentage">{percentage}% Complete</strong>
                    </div>
                    <ProgressBar value={percentage} showPercent={false} size="sm" tone="primary" />
                  </div>

                  <Button size="sm" onClick={() => navigate(`/courses/${course.id}`)}>
                    {actionLabel}
                  </Button>
                </div>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}
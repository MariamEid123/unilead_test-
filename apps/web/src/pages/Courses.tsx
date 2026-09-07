import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import PageHeader from '../components/ui/PageHeader';
import ProgressBar from '../components/ui/ProgressBar';
import { useApp } from '../state/AppContext';
import { COURSE_CATALOG, getCoursePercentage } from '../data/courses';
import { getStudent } from '../data/mockApi';
import './Courses.css';

export default function Courses() {
  const { student, setStudent } = useApp();

  useEffect(() => {
    if (!student) {
      getStudent().then(setStudent).catch(() => {});
    }
  }, [student, setStudent]);

  return (
    <div className="page courses">
      <PageHeader
        eyebrow="Courses"
        title="Choose what to learn next"
        subtitle="Build strong foundations with focused courses designed for steady progress."
      />

      <section className="courses__grid" aria-label="Available courses">
        {COURSE_CATALOG.map((course) => {
          const percentage = getCoursePercentage(student, course);
          const actionLabel = percentage > 0 ? 'Continue learning' : 'Explore course';

          return (
            <article className="course-card" key={course.id}>
              <div className={`course-card__cover course-card__cover--${course.accent}`} aria-hidden="true">
                <span className="course-card__cover-label">{course.subject}</span>
                <span className="course-card__cover-mark">{course.accent === 'physics' ? 'F' : '0'}</span>
              </div>
              <div className="course-card__body">
                <div className="course-card__meta">
                  <span>{course.subject}</span>
                  <span>{course.lectures} lectures</span>
                </div>
                <h2 className="course-card__title">{course.title}</h2>
                <p className="course-card__description">{course.description}</p>

                <div className="course-card__progress-block" aria-label={`${course.subject} progress: ${percentage}%`}>
                  <div className="course-card__progress-header">
                    <span className="course-card__progress-subject">{course.subject}</span>
                    <strong className="course-card__percentage">{percentage}% Complete</strong>
                  </div>
                  <ProgressBar value={percentage} showPercent={false} size="sm" tone="primary" />
                </div>

                <Link className="course-card__action" to={`/courses/${course.id}`}>
                  {actionLabel}<span aria-hidden="true"> &rarr;</span>
                </Link>
              </div>
            </article>
          );
        })}
      </section>
    </div>
  );
}

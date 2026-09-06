import { Link } from 'react-router-dom';
import PageHeader from '../components/ui/PageHeader';
import ProgressBar from '../components/ui/ProgressBar';
import { useApp } from '../state/AppContext';
import { COURSE_CATALOG } from '../data/courses';
import './Courses.css';

export default function Courses() {
  const { student } = useApp();

  return (
    <div className="page courses">
      <PageHeader
        eyebrow="Courses"
        title="Choose what to learn next"
        subtitle="Build strong foundations with focused courses designed for steady progress."
      />

      <section className="courses__grid" aria-label="Available courses">
        {COURSE_CATALOG.map((course) => {
          const progress = student?.course.title === course.title ? student.overallProgress : undefined;
          const actionLabel = progress && progress > 0 ? 'Continue learning' : 'Explore course';

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
                {progress !== undefined && (
                  <ProgressBar value={progress} label="Your progress" size="sm" />
                )}
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
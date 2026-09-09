import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import PageHeader from '../components/ui/PageHeader';
import ProgressBar from '../components/ui/ProgressBar';
import { useApp } from '../state/AppContext';
import { getCourseByCode, getCoursePercentage, courseImage } from '../data/courses';
import { fetchCourses, type CourseListItem } from '../data/curriculumApi';
import { getStudent } from '../data/mockApi';
import { LoadingState, ErrorState } from '../components/ui/StateViews';
import './Courses.css';

export default function Courses() {
  const { student, setStudent } = useApp();
  const [catalog, setCatalog] = useState<CourseListItem[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!student) {
      getStudent().then(setStudent).catch(() => {});
    }
    fetchCourses()
      .then((items) => setCatalog(items.filter((c) => c.lesson_count > 0)))
      .catch((err) => setError(err instanceof Error ? err.message : 'Could not load the course catalog.'));
  }, [student, setStudent]);

  return (
    <div className="page courses">
      <PageHeader
        eyebrow="Courses"
        title="Choose what to learn next"
        subtitle="Build strong foundations with focused courses designed for steady progress."
      />

      {!catalog && !error && <LoadingState message="Loading courses…" />}
      {error && <ErrorState message={error} onRetry={() => setCatalog(null)} />}
      {catalog && catalog.length === 0 && (
        <p className="muted">No courses are published yet.</p>
      )}
      {catalog && catalog.length > 0 && (
        <section className="courses__grid" aria-label="Available courses">
          {catalog.map((apiCourse) => {
            const staticCourse = getCourseByCode(apiCourse.code);
            const course = staticCourse ?? {
              id: apiCourse.code.toLowerCase(),
              title: apiCourse.title,
              description: apiCourse.description,
              subject: apiCourse.code.toUpperCase(),
              lectures: apiCourse.lesson_count,
              quizzes: 0,
              assignments: 0,
              accent: 'physics' as const,
            };
            const percentage = getCoursePercentage(student, course);
            const actionLabel = percentage > 0 ? 'Continue learning' : 'Explore course';

            return (
              <article className="course-card" key={apiCourse.code}>
                <img
                  className="course-card__photo"
                  src={courseImage(course)}
                  alt={`${course.subject} subject cover`}
                />
                <div className="course-card__body">
                  <div className="course-card__meta">
                    <span>{course.subject}</span>
                    <span>{apiCourse.lesson_count} lessons</span>
                  </div>
                  <h2 className="course-card__title">{apiCourse.title}</h2>
                  <p className="course-card__description">{apiCourse.description}</p>

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
      )}
    </div>
  );
}
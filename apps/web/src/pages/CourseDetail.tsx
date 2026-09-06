import { Link, useNavigate, useParams } from 'react-router-dom';
import Button from '../components/ui/Button';
import ProgressBar from '../components/ui/ProgressBar';
import { getCourseById, getLecturesForCourse } from '../data/courses';
import { useApp } from '../state/AppContext';
import NotFound from './NotFound';
import './Courses.css';

type CourseSection = 'overview' | 'lectures' | 'quizzes' | 'assignments' | 'simulation' | 'review';

const SECTION_ITEMS: { id: CourseSection; label: string }[] = [
  { id: 'overview', label: 'Overview' },
  { id: 'lectures', label: 'Lectures' },
  { id: 'quizzes', label: 'Quizzes' },
  { id: 'assignments', label: 'Assignments' },
  { id: 'simulation', label: 'Simulation' },
  { id: 'review', label: 'Review' },
];

const QUIZ_TITLES: Record<string, string[]> = {
  'physics-fundamentals': ['Motion check-in', 'Forces and energy review', 'Physics checkpoint'],
  'math-zero-foundations': ['Number sense check-in', 'Equations review', 'Foundations checkpoint'],
};
const ASSIGNMENT_TITLES: Record<string, string[]> = {
  'physics-fundamentals': ['Motion practice set', 'Forces and energy application', 'Physics reflection'],
  'math-zero-foundations': ['Number practice set', 'Equation application', 'Foundations reflection'],
};

export default function CourseDetail() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { student } = useApp();
  const { section } = useParams();
  const activeSection: CourseSection = section && SECTION_ITEMS.some((item) => item.id === section)
    ? section as CourseSection
    : 'overview';
  const course = courseId ? getCourseById(courseId) : undefined;

  if (!course) return <NotFound />;

  const progress = student?.course.title === course.title ? student.overallProgress : undefined;
  const lectures = getLecturesForCourse(course.id);
  const firstLecture = lectures[0];

  return (
    <div className="page course-detail">
      <Link className="course-detail__back" to="/courses">&larr; All courses</Link>
      <div className={`course-detail__hero course-detail__hero--${course.accent}`}>
        <span className="course-detail__subject">{course.subject}</span>
        <h1>{course.title}</h1>
        <p>{course.description}</p>
      </div>

      <div className="course-detail__workspace">
        <nav className="course-detail__nav" aria-label="Course sections">
          <span className="course-detail__nav-label">Course contents</span>
          {SECTION_ITEMS.map((section) => (
            <button
              key={section.id}
              className={`course-detail__nav-item ${activeSection === section.id ? 'course-detail__nav-item--active' : ''}`}
              type="button"
              aria-current={activeSection === section.id ? 'page' : undefined}
              onClick={() => navigate(section.id === 'overview' ? `/courses/${course.id}` : `/courses/${course.id}/${section.id}`)}
            >
              {section.label}
            </button>
          ))}
        </nav>

        <main className="course-detail__main">
          {activeSection === 'overview' && (
            <section aria-labelledby="course-overview-title">
              <span className="course-detail__eyebrow">Course overview</span>
              <h2 id="course-overview-title">A clear path from the basics to confidence</h2>
              <p className="muted">{course.description}</p>
              <div className="course-detail__stats" aria-label="Course contents summary">
                <div><strong>{course.lectures}</strong><span>Lectures</span></div>
                <div><strong>{course.quizzes}</strong><span>Quizzes</span></div>
                <div><strong>{course.assignments}</strong><span>Assignments</span></div>
              </div>
              {progress !== undefined && <ProgressBar value={progress} label="Your progress" />}
              <Button
                onClick={() => {
                  if (firstLecture) {
                    navigate(`/courses/${course.id}/lectures/${firstLecture.id}`);
                  }
                }}
                disabled={!firstLecture}
              >
                {progress && progress > 0 ? 'Continue learning' : 'Start learning'}
              </Button>
            </section>
          )}

          {activeSection !== 'overview' && (
            <section aria-labelledby={`${activeSection}-title`}>
              <span className="course-detail__eyebrow">Course contents</span>
              <h2 id={`${activeSection}-title`}>
                {SECTION_ITEMS.find((section) => section.id === activeSection)?.label}
              </h2>
              <p className="muted course-detail__section-intro">
                {activeSection === 'lectures' && `Browse the lessons in ${course.title}.`}
                {activeSection === 'quizzes' && `Review the knowledge checks for ${course.title}.`}
                {activeSection === 'assignments' && `See the practice work for ${course.title}.`}
                {activeSection === 'simulation' && `Run a simulation for ${course.title}.`}
                {activeSection === 'review' && `Review your learning evidence for ${course.title}.`}
              </p>
              <div className="course-detail__list">
                {activeSection === 'lectures' && lectures.map((lecture) => (
                  <div className="course-detail__list-item" key={lecture.id}>
                    <span className="course-detail__list-number">{String(lecture.number).padStart(2, '0')}</span>
                    <span className="course-detail__list-title">
                      <strong>Lecture {String(lecture.number).padStart(2, '0')}</strong>
                      <span>{lecture.title}</span>
                    </span>
                    <Link className="course-detail__list-action" to={`/courses/${course.id}/lectures/${lecture.id}`}>
                      Open lecture<span aria-hidden="true"> &rarr;</span>
                    </Link>
                  </div>
                ))}
                {activeSection !== 'lectures' && (activeSection === 'quizzes' ? QUIZ_TITLES[course.id] : activeSection === 'assignments' ? ASSIGNMENT_TITLES[course.id] : []).map((title, index) => (
                  <div className="course-detail__list-item" key={title}>
                    <span className="course-detail__list-number">{String(index + 1).padStart(2, '0')}</span>
                    <span>{title}</span>
                    <span className="course-detail__list-status">Coming soon</span>
                  </div>
                ))}
                {activeSection === 'simulation' && (
                  <div className="course-detail__section-action">
                    <Button onClick={() => navigate(`/courses/${course.id}/simulation`)}>Open {course.title} Simulation</Button>
                  </div>
                )}
                {activeSection === 'review' && (
                  <div className="course-detail__section-action">
                    <Button onClick={() => navigate(`/courses/${course.id}/review`)}>Open {course.title} Review</Button>
                  </div>
                )}
              </div>
            </section>
          )}
        </main>
      </div>
    </div>
  );
}
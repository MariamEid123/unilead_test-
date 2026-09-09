import { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import Button from '../components/ui/Button';
import ProgressBar from '../components/ui/ProgressBar';
import { LoadingState, ErrorState, EmptyState } from '../components/ui/StateViews';
import { getCourseById } from '../data/courses';
import {
  fetchCourseDetail,
  fetchCourseMaterials,
  type CourseDetail as ApiCourseDetail,
  type CourseLessonMaterials,
} from '../data/curriculumApi';
import { useApp } from '../state/AppContext';
import NotFound from './NotFound';
import './Courses.css';

type CourseSection = 'overview' | 'lectures' | 'materials' | 'quizzes' | 'assignments' | 'simulation' | 'review' | 'lab';

const SECTION_ITEMS: { id: CourseSection; label: string }[] = [
  { id: 'overview', label: 'Overview' },
  { id: 'lectures', label: 'Lectures' },
  { id: 'materials', label: 'Materials' },
  { id: 'quizzes', label: 'Quizzes' },
  { id: 'assignments', label: 'Assignments' },
  { id: 'simulation', label: 'Simulation' },
  { id: 'review', label: 'Review' },
  { id: 'lab', label: 'Lab' },
];

function formatActivity(completed: number | null | undefined, total: number | null | undefined) {
  return completed !== null && completed !== undefined && total !== null && total !== undefined
    ? `${completed}/${total}`
    : 'Not available yet';
}

function formatDuration(seconds: number): string {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  if (m === 0) return `${s}s`;
  if (s === 0) return `${m} min`;
  return `${m} min ${s}s`;
}

export default function CourseDetail() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { student } = useApp();
  const { section } = useParams();
  const activeSection: CourseSection = section && SECTION_ITEMS.some((item) => item.id === section)
    ? section as CourseSection
    : 'overview';

  const [detail, setDetail] = useState<ApiCourseDetail | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [materials, setMaterials] = useState<CourseLessonMaterials[] | null>(null);
  const [materialsError, setMaterialsError] = useState<string | null>(null);

  const course = courseId ? getCourseById(courseId) : undefined;
  const courseCode = course?.code;

  useEffect(() => {
    if (!courseCode) return;
    setDetail(null);
    setError(null);
    fetchCourseDetail(courseCode)
      .then(setDetail)
      .catch((err) => setError(err instanceof Error ? err.message : 'Could not load the course.'));
  }, [courseCode]);

  useEffect(() => {
    if (!courseCode || activeSection !== 'materials') return;
    setMaterials(null);
    setMaterialsError(null);
    fetchCourseMaterials(courseCode)
      .then(setMaterials)
      .catch((err) => setMaterialsError(err instanceof Error ? err.message : 'Could not load the materials.'));
  }, [courseCode, activeSection]);

  if (!course) return <NotFound />;

  const progress = student?.courseProgress.find(
    (item) => item.courseId === course.code || item.courseId === course.id
  );
  const allLessons = detail ? detail.modules.flatMap((m) => m.lessons) : [];
  const firstLecture = allLessons[0];
  const completedCodes = new Set(progress?.completedLessons ?? []);
  const isLoaded = courseCode !== undefined;
  const totalLectures = detail ? detail.modules.reduce((n, m) => n + m.lessons.length, 0) : progress?.totalLectures;

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
              onClick={() => navigate(section.id === 'overview' ? `/courses/${courseId}` : `/courses/${courseId}/${section.id}`)}
            >
              {section.label}
            </button>
          ))}
        </nav>

        <main className="course-detail__main">
          {!isLoaded ? (
            <LoadingState message="Loading course content…" />
          ) : error ? (
            <ErrorState message={error} onRetry={() => undefined} />
          ) : activeSection === 'overview' && (
            <section aria-labelledby="course-overview-title">
              <span className="course-detail__eyebrow">Course overview</span>
              <h2 id="course-overview-title">A clear path from the basics to confidence</h2>
              <p className="muted">{course.description}</p>
              <div className="course-detail__stats" aria-label="Course contents summary">
                <div><strong>{formatActivity(progress?.completedLectures, totalLectures)}</strong><span>Lectures</span></div>
                <div><strong>{formatActivity(progress?.completedQuizzes, progress?.totalQuizzes)}</strong><span>Quizzes</span></div>
                <div><strong>{formatActivity(progress?.completedAssignments, progress?.totalAssignments)}</strong><span>Assignments</span></div>
              </div>
              {progress?.progressPercentage !== null && progress?.progressPercentage !== undefined && <ProgressBar value={progress.progressPercentage} label="Your progress" />}
              <Button
                onClick={() => {
                  if (firstLecture) {
                    navigate(`/courses/${courseId}/lectures/${firstLecture.code}`);
                  }
                }}
                disabled={!firstLecture}
              >
                {progress?.progressPercentage && progress.progressPercentage > 0 ? 'Continue learning' : 'Start learning'}
              </Button>
            </section>
          )}

          {isLoaded && activeSection !== 'overview' && (
            <section aria-labelledby={`${activeSection}-title`}>
              <span className="course-detail__eyebrow">Course contents</span>
              <h2 id={`${activeSection}-title`}>
                {SECTION_ITEMS.find((section) => section.id === activeSection)?.label}
              </h2>
              <p className="muted course-detail__section-intro">
                {activeSection === 'lectures' && `Browse the lessons in ${course.title}, grouped by module.`}
                {activeSection === 'materials' && `Curated videos and reading, packed by lesson for ${course.title}.`}
                {activeSection === 'quizzes' && `Review the knowledge checks for ${course.title}.`}
                {activeSection === 'assignments' && `See the practice work for ${course.title}.`}
                {activeSection === 'simulation' && `Run a simulation for ${course.title}.`}
                {activeSection === 'review' && `Review your learning evidence for ${course.title}.`}
                {activeSection === 'lab' && `Write, run and get graded on real Python challenges for ${course.title}.`}
              </p>
              <div className="course-detail__list">
                {activeSection === 'lectures' && detail && detail.modules.map((module) => (
                  <div className="course-detail__module" key={module.code}>
                    <h3 className="course-detail__module-title">{module.title}</h3>
                    {module.lessons.map((lesson) => {
                      const complete = completedCodes.has(lesson.code);
                      return (
                        <div className="course-detail__list-item" key={lesson.code}>
                          <span className={`course-detail__list-number ${complete ? 'course-detail__list-number--done' : ''}`}>{complete ? '✓' : String(lesson.sort_order + 1).padStart(2, '0')}</span>
                          <span className="course-detail__list-title">
                            <strong>Lesson {lesson.code}</strong>
                            <span>{lesson.title}</span>
                          </span>
                          <span className="course-detail__list-meta">
                            {lesson.section_count > 0 ? `${lesson.section_count} blocks` : null}
                            {lesson.practice_count > 0 ? ` · ${lesson.practice_count} questions` : null}
                            {lesson.video_count > 0 ? ` · ${lesson.video_count} videos` : null}
                          </span>
                          <Link className="course-detail__list-action" to={`/courses/${courseId}/lectures/${lesson.code}`}>
                            {complete ? 'Review' : 'Open lesson'}<span aria-hidden="true"> &rarr;</span>
                          </Link>
                        </div>
                      );
                    })}
                  </div>
                ))}
                {activeSection === 'lectures' && detail && detail.modules.length === 0 && (
                  <p className="muted">No lessons are published for this course yet.</p>
                )}
                {activeSection === 'quizzes' && (
                  <EmptyState
                    icon="🧠"
                    title="Knowledge checks land soon"
                    message="This course doesn't publish quizzes yet — your proof of understanding happens in the simulation and review steps."
                    action={
                      <Button onClick={() => navigate(`/courses/${courseId}/simulation`)}>
                        Go to the Simulation
                      </Button>
                    }
                  />
                )}
                {activeSection === 'assignments' && (
                  <EmptyState
                    icon="✍️"
                    title="Practice is your assignment"
                    message="There are no long-form assignments in this course yet. Put the concepts to work by running the simulation and reviewing your evidence."
                    action={
                      <Button onClick={() => navigate(`/courses/${courseId}/simulation`)}>
                        Open the Practice Simulation
                      </Button>
                    }
                  />
                )}
                {activeSection === 'simulation' && (
                  <div className="course-detail__section-action">
                    <Button onClick={() => navigate(`/courses/${courseId}/simulation`)}>Open {course.title} Simulation</Button>
                  </div>
                )}
                {activeSection === 'review' && (
                  <div className="course-detail__section-action">
                    <Button onClick={() => navigate(`/courses/${courseId}/review`)}>Open {course.title} Review</Button>
                  </div>
                )}
                {activeSection === 'lab' &&
                  (course.code === 'CSE014' ? (
                    <div className="course-detail__section-action">
                      <Button onClick={() => navigate(`/courses/${courseId}/lab`)}>Open {course.title} Lab</Button>
                      <p className="muted course-detail__lab-note">
                        The lab runs real Python in a sandbox and grades your submissions against hidden tests.
                      </p>
                    </div>
                  ) : (
                    <EmptyState
                      icon="🧪"
                      title="No lab for this course yet"
                      message="The interactive code lab currently ships with Structured Programming (CSE014)."
                      action={<Button onClick={() => navigate(`/courses/${courseId}`)}>Back to Overview</Button>}
                    />
                  ))}
                {activeSection === 'materials' &&
                  (materialsError ? (
                    <ErrorState message={materialsError} onRetry={() => undefined} />
                  ) : !materials ? (
                    <p className="muted">Loading materials…</p>
                  ) : materials.length === 0 ? (
                    <EmptyState
                      icon="📚"
                      title="No materials published yet"
                      message="Nothing is curated for this course yet — check back soon."
                      action={<Button onClick={() => navigate(`/courses/${courseId}`)}>Back to Overview</Button>}
                    />
                  ) : (
                    materials.map((group) => (
                      <div className="course-detail__module" key={group.lesson_code}>
                        <h3 className="course-detail__module-title">
                          {group.lesson_title} <span className="muted">({group.lesson_code})</span>
                        </h3>
                        {group.resources.map((resource) => (
                          <div className="course-detail__list-item" key={resource.title}>
                            <span className="course-detail__list-number">▶</span>
                            <span className="course-detail__list-title">
                              <strong>{resource.title}</strong>
                              <span>{resource.description}</span>
                            </span>
                            <span className="course-detail__list-meta">
                              {resource.duration_seconds ? formatDuration(resource.duration_seconds) : null}
                              {resource.external_url ? ' · external link' : null}
                            </span>
                            {resource.external_url && (
                              <a
                                className="course-detail__list-action"
                                href={resource.external_url}
                                target="_blank"
                                rel="noreferrer"
                              >
                                Open<span aria-hidden="true"> ↗</span>
                              </a>
                            )}
                          </div>
                        ))}
                      </div>
                    ))
                  ))}
                {activeSection !== 'lectures' &&
                  activeSection !== 'materials' &&
                  activeSection !== 'quizzes' &&
                  activeSection !== 'assignments' &&
                  activeSection !== 'simulation' &&
                  activeSection !== 'review' &&
                  activeSection !== 'lab' && (
                    <EmptyState
                      icon="🧭"
                      title="Nothing here yet"
                      message="This part of the course isn't published. Head back to the overview to keep going."
                      action={<Button onClick={() => navigate(`/courses/${courseId}`)}>Back to Overview</Button>}
                    />
                  )}
              </div>
            </section>
          )}
        </main>
      </div>
    </div>
  );
}
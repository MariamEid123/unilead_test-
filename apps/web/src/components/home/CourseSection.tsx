import { useNavigate } from 'react-router-dom';
import Button from '../ui/Button';
import { COURSE_CATALOG } from '../../data/courses';
import './CourseSection.css';

export default function CourseSection() {
  const navigate = useNavigate();

  return (
    <section className="home-courses" aria-labelledby="home-courses-title">
      <div className="home-courses__inner">
        <div className="home-courses__heading">
          <span className="home-courses__eyebrow">Build your foundations</span>
          <h2 id="home-courses-title">Explore Courses</h2>
          <p className="muted">Start with a focused course and keep your learning moving forward.</p>
        </div>

        <div className="home-courses__grid">
          {COURSE_CATALOG.map((course) => (
            <article className="home-course-card" key={course.id}>
              <div className={`home-course-card__cover home-course-card__cover--${course.accent}`} aria-hidden="true">
                <span>{course.subject}</span>
                <strong>{course.accent === 'physics' ? 'F' : '0'}</strong>
              </div>
              <div className="home-course-card__body">
                <div className="home-course-card__meta">{course.lectures} lectures</div>
                <h3>{course.title}</h3>
                <p>{course.description}</p>
                <Button size="sm" onClick={() => navigate(`/courses/${course.id}`)}>
                  Explore Course
                </Button>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
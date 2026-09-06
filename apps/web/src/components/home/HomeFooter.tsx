import './HomeFooter.css';
import { useApp } from '../../state/AppContext';
import { COURSE_CATALOG } from '../../data/courses';

export default function HomeFooter() {
  const { student } = useApp();
  const hasSupportedCourse = student && COURSE_CATALOG.some((course) => course.title === student.course.title);
  const courseLabel = hasSupportedCourse ? student.course.title : 'Your learning workspace';

  return (
    <footer className="home-footer">
      <div className="home-footer__inner">
        <span className="home-footer__brand"><img src="/unilead-mark.svg" alt="" /> Areta</span>
        <span className="muted home-footer__meta">{courseLabel}</span>
      </div>
    </footer>
  );
}

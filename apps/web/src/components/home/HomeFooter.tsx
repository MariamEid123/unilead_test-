import './HomeFooter.css';
import { useApp } from '../../state/AppContext';

export default function HomeFooter() {
  const { student } = useApp();
  const courseLabel = student ? `${student.course.code} — ${student.course.title}` : 'Your learning workspace';

  return (
    <footer className="home-footer">
      <div className="home-footer__inner">
        <span className="home-footer__brand"><img src="/unilead-mark.svg" alt="" /> UniLead</span>
        <span className="muted home-footer__meta">{courseLabel}</span>
      </div>
    </footer>
  );
}

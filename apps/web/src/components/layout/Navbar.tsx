import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useApp } from '../../state/AppContext';
import { logout } from '../../data/mockApi';
import './Navbar.css';

export default function Navbar() {
  const location = useLocation();
  const navigate = useNavigate();
  const { student, session, setSession, setStudent } = useApp();

  const isActive = (prefix: string) => location.pathname.startsWith(prefix);

  const initials = session?.name
    ? session.name
        .split(' ')
        .map((n) => n[0])
        .slice(0, 2)
        .join('')
        .toUpperCase()
    : student?.name
    ? student.name
        .split(' ')
        .map((n) => n[0])
        .slice(0, 2)
        .join('')
        .toUpperCase()
    : 'S';

  function handleLogout() {
    logout();
    setSession(null);
    setStudent(null as never); // clear student too
    navigate('/login');
  }

  return (
    <header className="navbar">
      <div className="navbar__inner">
        <Link to="/home" className="navbar__brand">
          <img className="navbar__brand-mark" src="/unilead-mark.svg" alt="" />
          Areta
        </Link>

        <nav className="navbar__links">
          <Link
            to="/home"
            className={`navbar__link ${location.pathname === '/home' ? 'navbar__link--active' : ''}`}
          >
            Home
          </Link>

          <Link className={`navbar__link ${isActive('/courses') ? 'navbar__link--active' : ''}`} to="/courses">
            Courses
          </Link>

          <Link className={`navbar__link ${isActive('/plans') ? 'navbar__link--active' : ''}`} to="/plans">
            Plans
          </Link>

          <Link className={`navbar__link ${isActive('/progress') ? 'navbar__link--active' : ''}`} to="/progress">
            Progress
          </Link>

          {session?.role === 'instructor' && (
            <Link className={`navbar__link ${isActive('/instructor') ? 'navbar__link--active' : ''}`} to="/instructor">
              Instructor
            </Link>
          )}
        </nav>

        <div className="navbar__auth">
          {session && (
            <button className="navbar__logout" onClick={handleLogout} aria-label="Log out">
              Log out
            </button>
          )}
          <button className="navbar__avatar" onClick={() => navigate('/profile')} aria-label="View profile">
            {initials}
          </button>
        </div>
      </div>
    </header>
  );
}

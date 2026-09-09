import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useApp } from '../../state/AppContext';
import { logout } from '../../data/mockApi';
import './Navbar.css';

export default function Navbar() {
  const location = useLocation();
  const navigate = useNavigate();
  const { student, session, setSession, setStudent, theme, toggleTheme } = useApp();

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
          <img className="navbar__brand-mark" src="/logo.jpg" alt="" />
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
          <button
            type="button"
            className="navbar__theme"
            onClick={toggleTheme}
            aria-label={theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
            title={theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
          >
            {theme === 'dark' ? (
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <circle cx="12" cy="12" r="4" />
                <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41" />
              </svg>
            ) : (
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
              </svg>
            )}
          </button>
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

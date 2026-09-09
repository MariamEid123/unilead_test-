import { useState } from 'react';
import type { FormEvent } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import { useApp } from '../state/AppContext';
import { login, getStudent } from '../data/mockApi';
import { ApiError } from '../data/apiClient';
import './SignUp.css';

export default function Login() {
  const navigate = useNavigate();
  const location = useLocation();
  const { setStudent, setSession } = useApp();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<{ email?: string; password?: string; form?: string }>({});
  const [loading, setLoading] = useState(false);
  const successMessage = (location.state as { message?: string } | null)?.message;
  const sessionMessage = sessionStorage.getItem('Areta_auth_message');
  if (sessionMessage) sessionStorage.removeItem('Areta_auth_message');

  function validate() {
    const next: typeof errors = {};
    if (!email.trim()) next.email = 'Please enter your email.';
    else if (!/^\S+@\S+\.\S+$/.test(email)) next.email = 'Enter a valid email address.';
    if (!password) next.password = 'Please enter your password.';
    setErrors(next);
    return Object.keys(next).length === 0;
  }

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!validate()) return;
    setLoading(true);
    setErrors({});
    try {
      const session = await login({ email: email.trim(), password });
      setSession(session);

      // Only student-role accounts carry a Student record — employers and
      // staff roles (instructors, admins) have no student progress to load,
      // so asking for it returns 403 "Student access required" and would
      // block them from ever logging in. Route them straight to their panel.
      const isInstructor = session.role === 'instructor';
      if (!isInstructor) {
        const student = await getStudent();
        setStudent({ ...student, name: session.name, email: session.email });
      }
      const requestedFrom = (location.state as { from?: string } | null)?.from;
      const destination =
        isInstructor ? '/instructor' : requestedFrom ?? '/home';
      navigate(destination, { replace: true });
    } catch (err) {
      // 403 from login = correct password but the email isn't verified yet.
      // Send them to the verification screen (a code is already in their inbox).
      if (err instanceof ApiError && err.status === 403) {
        navigate(`/verify-email?email=${encodeURIComponent(email.trim())}`);
        return;
      }
      setErrors({
        form: err instanceof Error ? err.message : 'Could not log in. Please try again.',
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="signup">
      <div className="signup__panel">
        <div className="signup__brand">
          <img className="signup__brand-mark" src="/logo.jpg" alt="" />
        </div>
        <h2 className="signup__headline">Welcome back.</h2>
        <p className="signup__subtext muted">
          Pick up where you left off — your progress is saved across sessions.
        </p>
      </div>

      <div className="signup__form-side">
        <Card padding="lg" className="signup__card">
          <h1 className="signup__title">Log in</h1>
          <p className="muted signup__lede">Continue your competency journey.</p>

          {errors.form && <div className="signup__error">{errors.form}</div>}
          {(successMessage || sessionMessage) && <div className="signup__success">{successMessage || sessionMessage}</div>}

          <form onSubmit={handleSubmit} className="signup__form" noValidate>
            <Input
              label="Email"
              type="email"
              placeholder="you@university.edu"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              error={errors.email}
            />
            <Input
              label="Password"
              type="password"
              placeholder="Your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              error={errors.password}
            />
            <p className="muted signup__alt" style={{ margin: '-8px 0 0', textAlign: 'right' }}>
              <Link to="/forgot-password">Forgot password?</Link>
            </p>
            <Button type="submit" fullWidth size="lg" loading={loading}>
              Log In
            </Button>
          </form>

          <p className="muted signup__alt">
            New here? <Link to="/signup">Create an account</Link>
          </p>
        </Card>
      </div>
    </div>
  );
}

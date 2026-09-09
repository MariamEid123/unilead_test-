import { useState } from 'react';
import type { FormEvent } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import { forgotPassword } from '../data/mockApi';
import './SignUp.css';

export default function ForgotPassword() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [errors, setErrors] = useState<{ email?: string; form?: string }>({});
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    const trimmedEmail = email.trim();
    if (!trimmedEmail) {
      setErrors({ email: 'Please enter your email.' });
      return;
    }
    if (!/^\S+@\S+\.\S+$/.test(trimmedEmail)) {
      setErrors({ email: 'Enter a valid email address.' });
      return;
    }
    setErrors({});
    setLoading(true);
    try {
      await forgotPassword(trimmedEmail);
      navigate(`/reset-password?email=${encodeURIComponent(trimmedEmail)}`);
    } catch (error) {
      setErrors({ form: error instanceof Error ? error.message : 'Could not send the reset code.' });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="signup">
      <div className="signup__panel">
        <div className="signup__brand"><img className="signup__brand-mark" src="/logo.jpg" alt="" /> Areta</div>
        <h2 className="signup__headline">Find your way back.</h2>
        <p className="signup__subtext muted">We will send a short-lived code to reset your password securely.</p>
      </div>
      <div className="signup__form-side">
        <Card padding="lg" className="signup__card">
          <h1 className="signup__title">Forgot password?</h1>
          <p className="muted signup__lede">Enter your account email and we will send a reset code.</p>
          {errors.form && <div className="signup__error">{errors.form}</div>}
          <form onSubmit={handleSubmit} className="signup__form" noValidate>
            <Input label="Email" type="email" placeholder="you@university.edu" value={email} onChange={(e) => setEmail(e.target.value)} error={errors.email} />
            <Button type="submit" fullWidth size="lg" loading={loading}>Send Reset Code</Button>
          </form>
          <p className="muted signup__alt"><Link to="/login">Back to log in</Link></p>
        </Card>
      </div>
    </div>
  );
}
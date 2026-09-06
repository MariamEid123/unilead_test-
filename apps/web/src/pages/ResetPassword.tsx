import { useEffect, useState } from 'react';
import type { FormEvent } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import Card from '../components/ui/Card';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import { forgotPassword, resetPassword } from '../data/mockApi';
import { ApiError } from '../data/apiClient';
import './SignUp.css';

const RESEND_COOLDOWN_SECONDS = 60;

export default function ResetPassword() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const emailParam = searchParams.get('email') ?? '';
  const [email, setEmail] = useState(emailParam);
  const [code, setCode] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState<{ email?: string; code?: string; password?: string; confirmPassword?: string; form?: string }>({});
  const [info, setInfo] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [resending, setResending] = useState(false);
  const [resendCountdown, setResendCountdown] = useState(emailParam ? RESEND_COOLDOWN_SECONDS : 0);

  useEffect(() => {
    if (resendCountdown <= 0) return;
    const timer = setInterval(() => setResendCountdown((value) => value - 1), 1000);
    return () => clearInterval(timer);
  }, [resendCountdown]);

  function validate() {
    const next: typeof errors = {};
    if (!email.trim()) next.email = 'Please enter your email.';
    else if (!/^\S+@\S+\.\S+$/.test(email)) next.email = 'Enter a valid email address.';
    if (!code.trim()) next.code = 'Please enter the reset code.';
    if (password.length < 8) next.password = 'Password must be at least 8 characters.';
    else {
      const missing: string[] = [];
      if (!/[A-Z]/.test(password)) missing.push('an uppercase letter');
      if (!/[a-z]/.test(password)) missing.push('a lowercase letter');
      if (!/\d/.test(password)) missing.push('a digit');
      if (!/[!@#$%^&*()_+\-=[\]{}|;:,.<>?]/.test(password)) missing.push('a special character');
      if (missing.length) next.password = `Password must contain ${missing.join(', ')}.`;
    }
    if (password !== confirmPassword) next.confirmPassword = 'Passwords do not match.';
    setErrors(next);
    return Object.keys(next).length === 0;
  }

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!validate()) return;
    setLoading(true);
    setErrors({});
    setInfo(null);
    try {
      await resetPassword({ email: email.trim(), code: code.trim(), newPassword: password });
      navigate('/login', { state: { message: 'Password updated — log in with your new password.' } });
    } catch (error) {
      if (error instanceof ApiError && error.status === 400) {
        setErrors({ code: error.message.replace(/^Request failed \(\d+\):\s*/, '') });
      } else if (error instanceof ApiError && error.status === 403) {
        navigate(`/verify-email?email=${encodeURIComponent(email.trim())}`);
      } else {
        setErrors({ form: error instanceof Error ? error.message : 'Could not reset your password.' });
      }
    } finally {
      setLoading(false);
    }
  }

  async function handleResend() {
    setErrors({});
    setResending(true);
    try {
      await forgotPassword(email.trim());
      setCode('');
      setResendCountdown(RESEND_COOLDOWN_SECONDS);
      setInfo('A new reset code was sent if an account exists for this email.');
    } catch (error) {
      setErrors({ form: error instanceof Error ? error.message : 'Could not resend the reset code.' });
    } finally {
      setResending(false);
    }
  }

  return (
    <div className="signup">
      <div className="signup__panel">
        <div className="signup__brand"><img className="signup__brand-mark" src="/unilead-mark.svg" alt="" /> Areta</div>
        <h2 className="signup__headline">A fresh start.</h2>
        <p className="signup__subtext muted">Choose a strong password and get back to your learning journey.</p>
      </div>
      <div className="signup__form-side">
        <Card padding="lg" className="signup__card">
          <h1 className="signup__title">Reset your password</h1>
          <p className="muted signup__lede">Enter the code from your email, then choose a new password.</p>
          {errors.form && <div className="signup__error">{errors.form}</div>}
          {info && <div className="signup__success">{info}</div>}
          <form onSubmit={handleSubmit} className="signup__form" noValidate>
            <Input label="Email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} error={errors.email} />
            <Input label="Reset code" placeholder="6-digit code" inputMode="numeric" autoComplete="one-time-code" value={code} onChange={(e) => setCode(e.target.value)} error={errors.code} />
            <Input label="New password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} error={errors.password} />
            <Input label="Confirm new password" type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} error={errors.confirmPassword} />
            <Button type="submit" fullWidth size="lg" loading={loading}>Update Password</Button>
          </form>
          <p className="muted signup__alt">
            {resendCountdown <= 0 ? <>Didn't get it? <button type="button" className="signup__link-button" onClick={handleResend} disabled={resending}>{resending ? 'Sending…' : 'Resend the code'}</button></> : <>Resend available in {resendCountdown}s</>}
          </p>
          <p className="muted signup__alt"><Link to="/login">Back to log in</Link></p>
        </Card>
      </div>
    </div>
  );
}
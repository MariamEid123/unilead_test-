import { Navigate, Route, Routes, useLocation } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import { ProtectedRoute, InstructorRoute, PublicOnlyRoute } from './components/auth/ProtectedRoute';
import NotFound from './pages/NotFound';

import SignUp from './pages/SignUp';
import Login from './pages/Login';
import VerifyEmail from './pages/VerifyEmail';
import ForgotPassword from './pages/ForgotPassword';
import ResetPassword from './pages/ResetPassword';
import DesignPreview from './pages/DesignPreview';
import Onboarding from './pages/Onboarding';
import Home from './pages/Home';
import MyLearning from './pages/MyLearning';
import Courses from './pages/Courses';
import Plans from './pages/Plans';
import CourseDetail from './pages/CourseDetail';
import Lecture from './pages/Lecture';
import Diagnostic from './pages/Diagnostic';
import DiagnosticResults from './pages/DiagnosticResults';
import AICoach from './pages/AICoach';
import Practice from './pages/Practice';
import Assignment from './pages/Assignment';
import Remediation from './pages/Remediation';
import ApplyReview from './pages/ApplyReview';
import Simulation from './pages/Simulation';
import Lab from './pages/Lab';
import Review from './pages/Review';
import Transfer from './pages/Transfer';
import EvidenceTimeline from './pages/EvidenceTimeline';
import ProgressOverview from './pages/ProgressOverview';
import Profile from './pages/Profile';
import InstructorDashboard from './pages/InstructorDashboard';
import InstructorStudentDetail from './pages/InstructorStudentDetail';

// Routes that render full-bleed, without the main Navbar (auth/onboarding flow).
const NO_NAVBAR_ROUTES = ['/', '/signup', '/login', '/verify-email', '/forgot-password', '/reset-password', '/design-preview', '/onboarding'];

function Layout({ children }: { children: React.ReactNode }) {
  const location = useLocation();
  const showNavbar = !NO_NAVBAR_ROUTES.includes(location.pathname);

  return (
    <>
      {showNavbar && <Navbar />}
      {children}
    </>
  );
}

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Navigate to="/design-preview" replace />} />
        <Route path="/design-preview" element={<DesignPreview />} />
        <Route path="/signup" element={<PublicOnlyRoute><SignUp /></PublicOnlyRoute>} />
        <Route path="/login" element={<PublicOnlyRoute><Login /></PublicOnlyRoute>} />
        <Route path="/verify-email" element={<PublicOnlyRoute><VerifyEmail /></PublicOnlyRoute>} />
        <Route path="/forgot-password" element={<PublicOnlyRoute><ForgotPassword /></PublicOnlyRoute>} />
        <Route path="/reset-password" element={<PublicOnlyRoute><ResetPassword /></PublicOnlyRoute>} />
        <Route path="/onboarding" element={<ProtectedRoute><Onboarding /></ProtectedRoute>} />

        {/* Protected routes — require authentication */}
        <Route path="/home" element={<ProtectedRoute><Home /></ProtectedRoute>} />

        <Route path="/my-learning" element={<ProtectedRoute><MyLearning /></ProtectedRoute>} />
        <Route path="/courses" element={<ProtectedRoute><Courses /></ProtectedRoute>} />
        <Route path="/plans" element={<ProtectedRoute><Plans /></ProtectedRoute>} />
        <Route path="/courses/:courseId" element={<ProtectedRoute><CourseDetail /></ProtectedRoute>} />
        <Route path="/courses/:courseId/lectures/:lectureId" element={<ProtectedRoute><Lecture /></ProtectedRoute>} />
        <Route path="/courses/:courseId/:section" element={<ProtectedRoute><CourseDetail /></ProtectedRoute>} />
        <Route path="/courses/:courseId/simulation" element={<ProtectedRoute><Simulation /></ProtectedRoute>} />
        <Route path="/courses/:courseId/lab" element={<ProtectedRoute><Lab /></ProtectedRoute>} />
        <Route path="/courses/:courseId/review" element={<ProtectedRoute><Review /></ProtectedRoute>} />
        <Route path="/my-learning/diagnostic" element={<ProtectedRoute><Diagnostic /></ProtectedRoute>} />
        <Route path="/my-learning/diagnostic-results" element={<ProtectedRoute><DiagnosticResults /></ProtectedRoute>} />
        <Route path="/my-learning/ai-coach" element={<ProtectedRoute><AICoach /></ProtectedRoute>} />
        <Route path="/my-learning/practice" element={<ProtectedRoute><Practice /></ProtectedRoute>} />
        <Route path="/my-learning/assignment" element={<ProtectedRoute><Assignment /></ProtectedRoute>} />
        <Route path="/my-learning/remediation" element={<ProtectedRoute><Remediation /></ProtectedRoute>} />

        <Route path="/apply-review" element={<ProtectedRoute><ApplyReview /></ProtectedRoute>} />
        <Route path="/apply-review/simulation" element={<ProtectedRoute><Simulation /></ProtectedRoute>} />
        <Route path="/apply-review/transfer" element={<ProtectedRoute><Transfer /></ProtectedRoute>} />
        <Route path="/apply-review/evidence-timeline" element={<ProtectedRoute><EvidenceTimeline /></ProtectedRoute>} />
        <Route path="/apply-review/review" element={<ProtectedRoute><Review /></ProtectedRoute>} />

<Route path="/progress" element={<ProtectedRoute><ProgressOverview /></ProtectedRoute>} />
        <Route path="/progress/overview" element={<ProtectedRoute><ProgressOverview /></ProtectedRoute>} />
        <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />

        {/* Instructor-only views — require auth + instructor role */}
        <Route path="/instructor" element={<InstructorRoute><InstructorDashboard /></InstructorRoute>} />
        <Route path="/instructor/students/:studentId" element={<InstructorRoute><InstructorStudentDetail /></InstructorRoute>} />

        <Route path="*" element={<NotFound />} />
      </Routes>
    </Layout>
  );
}

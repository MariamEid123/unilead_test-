import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import ProgressBar from '../components/ui/ProgressBar';
import { LoadingState, ErrorState } from '../components/ui/StateViews';
import { useApp } from '../state/AppContext';
import { getStudent, completeReview } from '../data/mockApi';
import {
  COURSE_CATALOG,
  getCourseById,
  getCourseProgress,
  getCoursePercentage,
  getTopicsForCourse,
  getLecturesForCourse,
} from '../data/courses';
import type { CourseProgress } from '../types';
import './Review.css';

function getTopicLists(
  courseId: string,
  percentage: number,
  completedLectures: number
): { doingWell: string[]; needsPractice: string[] } {
  const topics = getTopicsForCourse(courseId);
  const total = topics.length;

  if (total === 0) {
    return {
      doingWell: ['Course foundations started'],
      needsPractice: ['Upcoming course topics'],
    };
  }

  // Determine number of demonstrated topics based on actual percentage and completed lectures
  const countWell = Math.max(
    completedLectures > 0 ? 1 : 0,
    Math.min(total, Math.round((percentage / 100) * total))
  );

  if (percentage === 0 && completedLectures === 0) {
    return {
      doingWell: ['Ready to begin — complete your first activity to see your strengths!'],
      needsPractice: topics.map((t) => t.name),
    };
  }

  const doingWell = topics.slice(0, countWell).map((t) => t.name);
  const needsPractice = topics.slice(countWell).map((t) => t.name);

  return {
    doingWell: doingWell.length > 0 ? doingWell : ['Foundations in progress'],
    needsPractice: needsPractice.length > 0 ? needsPractice : ['All topics completed! Keep practicing to stay sharp.'],
  };
}

function getRecommendedStep(
  subject: string,
  courseId: string,
  progress: CourseProgress | undefined,
  catalogLectures: number,
  catalogQuizzes: number,
  catalogAssignments: number
): { text: string; actionLabel: string; href: string } {
  const compLec = progress?.completedLectures ?? 0;
  const totLec = progress?.totalLectures ?? catalogLectures;
  const compQuiz = progress?.completedQuizzes ?? 0;
  const totQuiz = progress?.totalQuizzes ?? catalogQuizzes;
  const compAssign = progress?.completedAssignments ?? 0;
  const totAssign = progress?.totalAssignments ?? catalogAssignments;

  if (compQuiz < totQuiz && compLec > 0) {
    return {
      text: `Complete your remaining ${subject} quiz.`,
      actionLabel: `Open ${subject} Quizzes →`,
      href: `/courses/${courseId}/quizzes`,
    };
  }

  if (compLec < totLec) {
    const lectures = getLecturesForCourse(courseId);
    const nextLecture = lectures[compLec] ?? lectures[0];
    return {
      text: nextLecture
        ? `Watch your next lecture: ${nextLecture.title}.`
        : `Start your next ${subject} lecture.`,
      actionLabel: `Open Lecture →`,
      href: nextLecture ? `/courses/${courseId}/lectures/${nextLecture.id}` : `/courses/${courseId}/lectures`,
    };
  }

  if (compAssign < totAssign) {
    return {
      text: `Submit your next ${subject} practice assignment.`,
      actionLabel: `Open Assignments →`,
      href: `/courses/${courseId}/assignments`,
    };
  }

  return {
    text: `You are all caught up on ${subject}! Review your skills or explore another course.`,
    actionLabel: `Explore Courses →`,
    href: `/courses`,
  };
}

function getPercentageMeaning(percentage: number, subject: string): string {
  if (percentage === 0) {
    return `You haven't completed any activities in ${subject} yet. Completing your first lecture, quiz, or assignment will start raising your percentage toward 100%.`;
  }
  if (percentage >= 100) {
    return `Great job! You have completed 100% of all lectures, quizzes, and assignments for ${subject}.`;
  }
  return `Your ${percentage}% progress shows how much of this course you've completed so far. Each lecture you finish, quiz you take, and assignment you submit brings you closer to 100%.`;
}

export default function Review() {
  const navigate = useNavigate();
  const { courseId } = useParams();
  const { student, setStudent, markReviewComplete } = useApp();
  const [loading, setLoading] = useState(!student);
  const [error, setError] = useState<string | null>(null);
  const [continuing, setContinuing] = useState(false);

  // Resolve the active course: from URL parameter or fallback to student's course or first catalog item
  const defaultCourse = COURSE_CATALOG[0]!;
  const course = courseId ? getCourseById(courseId) : undefined;
  const activeCourse =
    course ??
    (student?.course?.id
      ? COURSE_CATALOG.find((c) => c.id === student.course.id || c.title === student.course.title)
      : undefined) ??
    defaultCourse;

  const subject = activeCourse.subject;

  useEffect(() => {
    if (!student) {
      setLoading(true);
      getStudent()
        .then((s) => {
          setStudent(s);
          setLoading(false);
        })
        .catch((err) => {
          setError(err instanceof Error ? err.message : 'Could not load your course data.');
          setLoading(false);
        });
    }
  }, [student, setStudent]);

  async function handleContinue() {
    setContinuing(true);
    try {
      const s = student ?? (await getStudent());
      const updated = await completeReview(s);
      setStudent(updated);
      markReviewComplete();
      navigate('/progress/overview');
    } catch {
      markReviewComplete();
      navigate('/progress/overview');
    } finally {
      setContinuing(false);
    }
  }

  if (loading) {
    return (
      <div className="page review">
        <LoadingState message="Preparing your review…" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="page review">
        <ErrorState
          message={error}
          onRetry={() => {
            setError(null);
            setLoading(true);
            getStudent().then(setStudent).catch(() => setError('Could not load course data.')).finally(() => setLoading(false));
          }}
        />
      </div>
    );
  }

  const progress = getCourseProgress(student, activeCourse);
  const percentage = getCoursePercentage(student, activeCourse);

  const completedLectures = progress?.completedLectures ?? 0;
  const totalLectures = progress?.totalLectures ?? activeCourse.lectures;
  const completedQuizzes = progress?.completedQuizzes ?? 0;
  const totalQuizzes = progress?.totalQuizzes ?? activeCourse.quizzes;
  const completedAssignments = progress?.completedAssignments ?? 0;
  const totalAssignments = progress?.totalAssignments ?? activeCourse.assignments;

  const { doingWell, needsPractice } = getTopicLists(activeCourse.id, percentage, completedLectures);
  const recommendation = getRecommendedStep(
    subject,
    activeCourse.id,
    progress,
    activeCourse.lectures,
    activeCourse.quizzes,
    activeCourse.assignments
  );
  const percentageMeaning = getPercentageMeaning(percentage, subject);

  return (
    <div className="page review">
      <button
        className="review__back"
        type="button"
        onClick={() => navigate(courseId ? `/courses/${activeCourse.id}` : '/courses')}
      >
        ← Back to {activeCourse.title}
      </button>

      <header className="review__header">
        <span className="review__eyebrow">{subject}</span>
        <h1 className="review__title">{subject} Review</h1>
        <p className="muted review__subtitle">
          A clear summary of how you're doing, what you've completed, and what to focus on next.
        </p>
      </header>

      {/* 1. Your Progress */}
      <Card padding="lg" className="review__progress-card">
        <div className="review__card-header">
          <h2>Your Progress</h2>
        </div>
        <div className="review__progress-hero">
          <span className="review__progress-number">{percentage}%</span>
          <div className="review__progress-bar-wrap">
            <ProgressBar value={percentage} showPercent={false} size="md" tone="primary" />
          </div>
        </div>
        <p className="review__progress-explanation">{percentageMeaning}</p>
      </Card>

      {/* 2. You're Doing Well & Needs More Practice */}
      <div className="review__topics-grid">
        <Card padding="lg" className="review__topic-box review__topic-box--well">
          <div className="review__card-header">
            <span className="review__badge review__badge--success" aria-hidden="true">✓</span>
            <h2>You're Doing Well</h2>
          </div>
          <p className="muted review__box-subtext">Topics where you have shown strong understanding:</p>
          <ul className="review__topic-list">
            {doingWell.map((topic) => (
              <li key={topic} className="review__topic-item review__topic-item--well">
                <span className="review__topic-icon" aria-hidden="true">✓</span>
                <span>{topic}</span>
              </li>
            ))}
          </ul>
        </Card>

        <Card padding="lg" className="review__topic-box review__topic-box--practice">
          <div className="review__card-header">
            <span className="review__badge review__badge--warning" aria-hidden="true">!</span>
            <h2>Needs More Practice</h2>
          </div>
          <p className="muted review__box-subtext">Topics to review to continue building confidence:</p>
          <ul className="review__topic-list">
            {needsPractice.map((topic) => (
              <li key={topic} className="review__topic-item review__topic-item--practice">
                <span className="review__topic-icon" aria-hidden="true">○</span>
                <span>{topic}</span>
              </li>
            ))}
          </ul>
        </Card>
      </div>

      {/* 3. Your Activity */}
      <Card padding="lg" className="review__activity-card">
        <div className="review__card-header">
          <h2>Your Activity</h2>
        </div>
        <p className="muted review__box-subtext">Your completed activities across this course:</p>
        <div className="review__activity-grid">
          <div className="review__activity-item">
            <span className="review__activity-label">Lectures</span>
            <strong className="review__activity-val">{completedLectures}/{totalLectures}</strong>
          </div>
          <div className="review__activity-item">
            <span className="review__activity-label">Quizzes</span>
            <strong className="review__activity-val">{completedQuizzes}/{totalQuizzes}</strong>
          </div>
          <div className="review__activity-item">
            <span className="review__activity-label">Assignments</span>
            <strong className="review__activity-val">{completedAssignments}/{totalAssignments}</strong>
          </div>
        </div>
      </Card>

      {/* 4. Recommended Next Step */}
      <Card padding="lg" className="review__recommendation-card">
        <div className="review__card-header">
          <span className="review__badge review__badge--accent" aria-hidden="true">→</span>
          <h2>Recommended Next Step</h2>
        </div>
        <p className="review__recommendation-text">{recommendation.text}</p>
        <div className="review__recommendation-action">
          <Button onClick={() => navigate(recommendation.href)}>
            {recommendation.actionLabel}
          </Button>
        </div>
      </Card>

      {/* Navigation and Save Actions */}
      <div className="review__footer-actions">
        <Button variant="secondary" onClick={() => navigate(courseId ? `/courses/${activeCourse.id}` : '/courses')}>
          ← Back to Course
        </Button>
        <Button onClick={handleContinue} loading={continuing}>
          Save & View Full Progress →
        </Button>
      </div>
    </div>
  );
}

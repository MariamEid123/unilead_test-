import { useEffect, useRef, useState } from 'react';
import Hero from '../components/home/Hero';
import ValueProps from '../components/home/ValueProps';
import JourneySection from '../components/home/JourneySection';
import Differentiators from '../components/home/Differentiators';
import PersonalizedSection from '../components/home/PersonalizedSection';
import CourseSection from '../components/home/CourseSection';
import FinalCta from '../components/home/FinalCta';
import HomeFooter from '../components/home/HomeFooter';
import { useApp } from '../state/AppContext';
import { getStudent } from '../data/mockApi';
import { COURSE_CATALOG } from '../data/courses';
import type { AsyncState, Recommendation, Student } from '../types';

const COURSES_HREF = '/courses';

function getRecommendation(student: Student): Recommendation {
  const activeCourse = COURSE_CATALOG.find(
    (course) => course.id === student.course.id || course.title === student.course.title
  );

  if (!activeCourse) {
    return {
      id: 'rec-start-learning',
      title: 'Start your learning journey',
      reason: 'Choose Mathematics or Physics to begin.',
      href: COURSES_HREF,
      actionLabel: 'Choose a subject',
    };
  }

  const actionSubject = activeCourse.subject === 'Mathematics' ? 'Math' : activeCourse.subject;
  return {
    id: `rec-continue-${activeCourse.id}`,
    title: `Continue ${activeCourse.subject}`,
    reason: `Pick up where you left off in ${activeCourse.subject}.`,
    href: `/courses/${activeCourse.id}`,
    actionLabel: `Continue ${actionSubject}`,
  };
}

export default function Home() {
  const { student, setStudent, journey } = useApp();
  const [state, setState] = useState<AsyncState<{ student: Student; recommendation: Recommendation }>>({
    status: 'loading',
  });
  const journeySectionRef = useRef<HTMLElement>(null);

  async function load() {
    setState({ status: 'loading' });
    try {
      // Re-read progress on Home so a subject change made elsewhere is shown
      // immediately instead of using a stale context value.
      const s = await getStudent();
      if (JSON.stringify(student) !== JSON.stringify(s)) setStudent(s);
      const rec = getRecommendation(s);
      setState({ status: 'success', data: { student: s, recommendation: rec } });
    } catch (err) {
      setState({ status: 'error', message: err instanceof Error ? err.message : 'Failed to load your dashboard.' });
    }
  }

  useEffect(() => {
    load();
    // Reload whenever journey progress changes, so the recommendation stays current.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [journey]);

  const primaryHref = state.status === 'success' ? state.data.recommendation.href : COURSES_HREF;
  const primaryLabel = state.status === 'success' ? state.data.recommendation.actionLabel : 'Choose a subject';
  const activeStep = journey.hasCompletedReview
    ? 6
    : journey.hasCompletedSimulation
      ? 6
      : journey.hasCompletedPractice
        ? 5
        : journey.hasCompletedLearning
          ? 4
          : journey.hasCompletedDiagnostic
            ? 2
            : 1;

  function scrollToJourney() {
    journeySectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  return (
    <div className="home">
      <Hero primaryHref={primaryHref} primaryLabel={primaryLabel} onExploreClick={scrollToJourney} />
      <ValueProps />
      <JourneySection ref={journeySectionRef} activeStep={activeStep} />
      <Differentiators />
      <PersonalizedSection state={state} onRetry={load} />
      <CourseSection />
      <FinalCta href={primaryHref} label={primaryLabel} />
      <HomeFooter />
    </div>
  );
}

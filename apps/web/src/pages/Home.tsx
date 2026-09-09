import { useEffect } from 'react';
import Hero from '../components/home/Hero';
import ContinueCard from '../components/home/ContinueCard';
import ValueProps from '../components/home/ValueProps';
import JourneySection from '../components/home/JourneySection';
import CoachCta from '../components/home/CoachCta';
import HomeFooter from '../components/home/HomeFooter';
import { useApp } from '../state/AppContext';
import { getStudent } from '../data/mockApi';
import { getContinueAction } from '../components/home/continueAction';

export default function Home() {
  const { student, setStudent, journey } = useApp();

  useEffect(() => {
    let cancelled = false;
    getStudent()
      .then((s) => {
        if (!cancelled) setStudent(s);
      })
      .catch(() => {
        // Fall back to whatever the student context already holds. The
        // Continue card and journey render their own states from real data.
      });
    return () => {
      cancelled = true;
    };
    // Reload whenever journey progress changes, so the hero message stays current.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [journey]);

  const action = getContinueAction(student, journey);

  return (
    <div className="home">
      <Hero name={student?.name} message={action.message} primaryHref={action.href} />
      <ContinueCard />
      <ValueProps />
      <JourneySection />
      <CoachCta />
      <HomeFooter />
    </div>
  );
}
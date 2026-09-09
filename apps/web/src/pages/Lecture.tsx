import { useCallback, useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { getCourseById, resolveLecture } from '../data/courses';
import {
  completeLesson,
  fetchCourseDetail,
  fetchLectureSections,
  fetchLessonDetail,
  fetchPracticeItems,
  fetchSummarySections,
  fetchVideoResources,
  gradePractice,
  type ContentSection,
  type CourseDetail,
  type LessonDetail,
  type PracticeItemView,
  type VideoResource,
} from '../data/curriculumApi';
import { getStudent } from '../data/mockApi';
import { useApp } from '../state/AppContext';
import { simulationForLesson } from '../simulations/registry';
import { renderMarkdown } from '../utils/markdown';
import { LoadingState, ErrorState, EmptyState } from '../components/ui/StateViews';
import NotFound from './NotFound';
import './Lecture.css';

type LectureTab = 'lecture' | 'summary' | 'practice' | 'videos';

const TAB_LABELS: { id: LectureTab; label: string; hint: string }[] = [
  { id: 'lecture', label: 'Lecture', hint: 'Work through the material' },
  { id: 'summary', label: 'Summary', hint: 'See the big picture in one place' },
  { id: 'practice', label: 'Practice', hint: 'Check your understanding' },
  { id: 'videos', label: 'Videos', hint: 'Watch short targeted explanations' },
];

interface GradedItem extends PracticeItemView {
  correct: boolean | null;
  correctIndex: number | null;
  explanation: string | null;
}

function FormulaBlock({ section }: { section: ContentSection }) {
  const meaning = section.metadata?.meaning as string | undefined;
  const whenUsed = section.metadata?.when_used as string | undefined;
  return (
    <div className="lecture-block lecture-block--formula">
      {section.title && <div className="lecture-block__title">{section.title}</div>}
      <div
        className="lecture-block__formula"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
      />
      {(meaning || whenUsed) && (
        <dl className="lecture-block__meta">
          {meaning && <div><dt>What it means</dt><dd>{meaning}</dd></div>}
          {whenUsed && <div><dt>When to use it</dt><dd>{whenUsed}</dd></div>}
        </dl>
      )}
    </div>
  );
}

function TableBlock({ section }: { section: ContentSection }) {
  const note = section.metadata?.note as string | undefined;
  return (
    <div className="lecture-block lecture-block--table">
      {section.title && <div className="lecture-block__title">{section.title}</div>}
      <div
        className="lecture-block__table"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
      />
      {note && <p className="lecture-block__note">{note}</p>}
    </div>
  );
}

function TextBlock({ section }: { section: ContentSection }) {
  return (
    <div className="lecture-block">
      {section.title && <div className="lecture-block__title">{section.title}</div>}
      <div
        className="lecture-block__prose"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
      />
    </div>
  );
}

function SectionBlock({ section }: { section: ContentSection }) {
  switch (section.section_type) {
    case 'FORMULA':
      return <FormulaBlock section={section} />;
    case 'TABLE':
      return <TableBlock section={section} />;
    case 'EXAMPLE':
      return (
        <div className="lecture-block lecture-block--example">
          <div className="lecture-block__label">Example</div>
          {section.title && <div className="lecture-block__title">{section.title}</div>}
          <div
            className="lecture-block__prose"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
          />
        </div>
      );
    case 'KEY_POINT':
      return (
        <div className="lecture-block lecture-block--keypoint">
          <div className="lecture-block__label">Key point</div>
          {section.title && <div className="lecture-block__title">{section.title}</div>}
          <div
            className="lecture-block__prose"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
          />
        </div>
      );
    case 'WARNING':
      return (
        <div className="lecture-block lecture-block--warning">
          <div className="lecture-block__label">Common mistake</div>
          {section.title && <div className="lecture-block__title">{section.title}</div>}
          <div
            className="lecture-block__prose"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
          />
        </div>
      );
    case 'DIFFICULT_CONCEPT':
      return (
        <div className="lecture-block lecture-block--difficult">
          <div className="lecture-block__label">Tricky idea</div>
          {section.title && <div className="lecture-block__title">{section.title}</div>}
          <div
            className="lecture-block__prose"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(section.body) }}
          />
        </div>
      );
    default:
      return <TextBlock section={section} />;
  }
}

function PracticeItemCard({ item, onGrade }: {
  item: GradedItem;
  onGrade: (itemId: number, selectedIndex: number) => void;
}) {
  const [selected, setSelected] = useState<number | null>(null);
  const graded = item.correct !== null;
  const chooserClass = graded && item.correctIndex !== null
    ? (selected === item.correctIndex ? 'lecture-practice__option--correct' : 'lecture-practice__option--wrong')
    : '';

  return (
    <div className="lecture-practice__item">
      <p className="lecture-practice__prompt">{item.prompt}</p>
      <div className="lecture-practice__options" role="radiogroup" aria-label={`Options for: ${item.prompt}`}>
        {item.options.map((option, index) => (
          <button
            key={`${item.id}-${index}`}
            type="button"
            role="radio"
            aria-checked={selected === index}
            className={`lecture-practice__option ${selected === index ? 'lecture-practice__option--selected' : ''} ${chooserClass}`}
            onClick={() => {
              setSelected(index);
              if (!graded) onGrade(item.id, index);
            }}
            disabled={graded}
          >
            <span className="lecture-practice__option-letter">{String.fromCharCode(65 + index)}</span>
            <span>{option}</span>
          </button>
        ))}
      </div>
      {graded && (
        <div className={`lecture-practice__feedback ${item.correct ? 'lecture-practice__feedback--correct' : 'lecture-practice__feedback--wrong'}`}>
          {item.correct ? 'Correct' : 'Not quite'} — {item.explanation}
        </div>
      )}
    </div>
  );
}

export default function Lecture() {
  const { courseId, lectureId } = useParams();
  const navigate = useNavigate();
  const { student, setStudent } = useApp();
  const course = courseId ? getCourseById(courseId) : undefined;
  const lecture = courseId && lectureId ? resolveLecture(courseId, lectureId) : undefined;
  const lessonCode = lecture?.code ?? (/^[A-Za-z]{1,2}\d{1,2}$/.test(lectureId ?? '') ? lectureId : undefined);

  const [activeTab, setActiveTab] = useState<LectureTab>('lecture');
  const [detail, setDetail] = useState<LessonDetail | null>(null);
  const [sections, setSections] = useState<ContentSection[] | null>(null);
  const [summary, setSummary] = useState<ContentSection[] | null>(null);
  const [practice, setPractice] = useState<GradedItem[] | null>(null);
  const [videos, setVideos] = useState<VideoResource[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [courseDetail, setCourseDetail] = useState<CourseDetail | null>(null);
  const [completing, setCompleting] = useState(false);

  const completed = Boolean(student && lessonCode && student.courseProgress
    .some((p) => (p.courseId === course?.code || p.courseId === course?.id) && p.completedLessons.includes(lessonCode)));
  const orderedLessons = courseDetail
    ? courseDetail.modules.flatMap((m) => m.lessons).map((l) => l.code)
    : [];
  const currentIndex = lessonCode ? orderedLessons.indexOf(lessonCode) : -1;
  const prevLesson = currentIndex > 0 ? orderedLessons[currentIndex - 1] : undefined;
  const nextLesson = currentIndex !== -1 && currentIndex < orderedLessons.length - 1 ? orderedLessons[currentIndex + 1] : undefined;

  const loadLecture = useCallback(async () => {
    if (!lessonCode) return;
    setError(null);
    try {
      const [d, s] = await Promise.all([
        fetchLessonDetail(lessonCode),
        fetchLectureSections(lessonCode),
      ]);
      setDetail(d);
      setSections(s);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load lecture content.');
    }
  }, [lessonCode]);

  const loadSummary = useCallback(async () => {
    if (!lessonCode) return;
    setError(null);
    try {
      setSummary(await fetchSummarySections(lessonCode));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load summary.');
    }
  }, [lessonCode]);

  const loadPractice = useCallback(async () => {
    if (!lessonCode) return;
    setError(null);
    try {
      const items = await fetchPracticeItems(lessonCode);
      setPractice(items.map((item) => ({
        ...item,
        correct: null,
        correctIndex: null,
        explanation: null,
      })));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load practice questions.');
    }
  }, [lessonCode]);

  const loadVideos = useCallback(async () => {
    if (!lessonCode) return;
    setError(null);
    try {
      setVideos(await fetchVideoResources(lessonCode));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load videos.');
    }
  }, [lessonCode]);

  useEffect(() => {
    setDetail(null);
    setSections(null);
    setSummary(null);
    setPractice(null);
    setVideos(null);
    setError(null);
    setActiveTab('lecture');
  }, [lessonCode]);

  useEffect(() => {
    if (activeTab === 'lecture') void loadLecture();
    if (activeTab === 'summary') void loadSummary();
    if (activeTab === 'practice') void loadPractice();
    if (activeTab === 'videos') void loadVideos();
  }, [activeTab, loadLecture, loadSummary, loadPractice, loadVideos]);

  useEffect(() => {
    if (!course?.code) return;
    let cancelled = false;
    fetchCourseDetail(course.code)
      .then((c) => { if (!cancelled) setCourseDetail(c); })
      .catch(() => { if (!cancelled) setCourseDetail(null); });
    return () => { cancelled = true; };
  }, [course?.code]);

  const handleComplete = useCallback(async () => {
    if (!lessonCode || !student) return;
    setCompleting(true);
    try {
      await completeLesson(lessonCode);
      const fresh = await getStudent();
      setStudent(fresh);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Could not mark this lesson complete.');
    } finally {
      setCompleting(false);
    }
  }, [lessonCode, student, setStudent]);

  const goPrev = useCallback(() => {
    if (prevLesson && courseId) navigate(`/courses/${courseId}/lectures/${prevLesson}`);
  }, [prevLesson, courseId, navigate]);

  const goNext = useCallback(() => {
    if (nextLesson && courseId) navigate(`/courses/${courseId}/lectures/${nextLesson}`);
  }, [nextLesson, courseId, navigate]);

  const handleGrade = useCallback(async (itemId: number, selectedIndex: number) => {
    if (!lessonCode) return;
    try {
      const result = await gradePractice(lessonCode, itemId, selectedIndex);
      setPractice((prev) => prev?.map((item) => (
        item.id === itemId
          ? { ...item, correct: result.correct, correctIndex: result.correct === false ? selectedIndex : result.correct_index, explanation: result.explanation }
          : item
      )) ?? null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to submit answer.');
    }
  }, [lessonCode]);

  if (!course || !lessonCode) return <NotFound />;

  const relatedSim = simulationForLesson(lecture?.id ?? lectureId);

  const score = practice ? practice.filter((item) => item.correct).length : null;
  const sectionsByType = (
    sections
      ? [...sections].sort((a, b) => {
          const order = ['FORMULA', 'EXAMPLE', 'KEY_POINT', 'DIFFICULT_CONCEPT', 'WARNING', 'TABLE', 'TEXT', 'SUMMARY'];
          const ia = order.indexOf(a.section_type);
          const ib = order.indexOf(b.section_type);
          if (ia !== ib) return ia - ib;
          return a.sort_order - b.sort_order;
        })
      : []
  );

  // Resolve a stable lesson number for heading display: prefer the static
  // course catalogue number, else derive it from the course tree order.
  const lessonNumber = lecture?.number ?? (currentIndex >= 0 ? currentIndex + 1 : undefined);
  const lessonTitle = detail?.title ?? lecture?.title;

  return (
    <div className="page lecture-page">
      <Link className="course-detail__back" to={`/courses/${course?.id ?? ''}`}>
        &larr; Back to course
      </Link>

      <div className="lecture-page__heading">
        <span className="course-detail__eyebrow">
          {lessonNumber !== undefined ? `Lesson ${String(lessonNumber).padStart(2, '0')}` : detail?.code} · {course?.title}
        </span>
        <h1>{lessonTitle}</h1>
        {detail?.description && <p className="muted lecture-page__subtitle">{detail.description}</p>}
        {detail && (
          <ul className="lecture-page__meta">
            {detail.estimated_minutes ? <li>~{detail.estimated_minutes} min</li> : null}
            <li className={`lecture-page__difficulty lecture-page__difficulty--${detail.difficulty.toLowerCase()}`}>{detail.difficulty}</li>
            <li>{detail.section_count} reading blocks</li>
            <li>{detail.practice_count} practice questions</li>
            <li>{detail.video_count} videos</li>
          </ul>
        )}
      </div>

      <div className="lecture-page__tabs" role="tablist" aria-label="Lecture views">
        {TAB_LABELS.map((tab) => (
          <button
            key={tab.id}
            type="button"
            role="tab"
            aria-selected={activeTab === tab.id}
            className={`lecture-page__tab ${activeTab === tab.id ? 'lecture-page__tab--active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            <span>{tab.label}</span>
            <span className="lecture-page__tab-hint">{tab.hint}</span>
          </button>
        ))}
      </div>

      {error && <ErrorState message={error} onRetry={activeTab === 'lecture' ? loadLecture : activeTab === 'summary' ? loadSummary : activeTab === 'practice' ? loadPractice : loadVideos} />}

      {activeTab === 'lecture' ? (
        <div className="lecture-view" aria-label="Lecture content">
          {!sections && !error && <LoadingState message="Loading lecture content…" />}
          {detail && detail.objectives.length > 0 && (
            <section className="lecture-view__box" aria-labelledby="lecture-objectives-title">
              <h2 id="lecture-objectives-title">What you'll learn</h2>
              <ul>{detail.objectives.map((objective) => <li key={objective}>{objective}</li>)}</ul>
            </section>
          )}
          {detail && detail.prerequisites.length > 0 && (
            <section className="lecture-view__box" aria-labelledby="lecture-prereqs-title">
              <h2 id="lecture-prereqs-title">You'll need</h2>
              <ul>{detail.prerequisites.map((prereq) => <li key={prereq}>{prereq}</li>)}</ul>
            </section>
          )}
          {relatedSim && (
            <section className={`lecture-view__box lecture-view__box--sim ${relatedSim.id}`} aria-labelledby="lecture-sim-title">
              <span className="lecture-view__box-tag">Practical lab</span>
              <h2 id="lecture-sim-title">{relatedSim.title}</h2>
              <p>{relatedSim.objective}</p>
              <button
                type="button"
                className="lecture-page__complete-button"
                onClick={() => navigate(`/courses/${course.id}/simulation`)}
              >
                Open the simulation <span aria-hidden="true">&rarr;</span>
              </button>
            </section>
          )}
          {sections && sectionsByType.length > 0 && (
            <section className="lecture-view__blocks" aria-label="Lecture sections">
              {sectionsByType.map((section, idx) => <SectionBlock key={`${section.section_type}-${idx}`} section={section} />)}
            </section>
          )}
          {sections && sectionsByType.length === 0 && <EmptyState title="No content yet" message="The lecture has no reading blocks connected yet." />}
        </div>
      ) : activeTab === 'summary' ? (
        <div className="lecture-view" aria-label="Lecture summary">
          {!summary && !error && <LoadingState message="Loading summary…" />}
          {summary && summary.length > 0 && (
            <div className="lecture-view__blocks">
              {summary.map((section, idx) => <SectionBlock key={`${section.section_type}-${idx}`} section={section} />)}
            </div>
          )}
          {summary && summary.length === 0 && <EmptyState title="No summary yet" message="The summary for this lecture has not been connected yet." />}
        </div>
      ) : activeTab === 'practice' ? (
        <div className="lecture-practice" aria-label="Practice questions">
          {!practice && !error && <LoadingState message="Loading practice questions…" />}
          {practice && (
            <>
              <div className="lecture-practice__header">
                <h2>Practice</h2>
                {score !== null && <span className="lecture-practice__score">{score}/{practice.length} correct</span>}
              </div>
              {['UNDERSTAND', 'APPLY', 'TRANSFER'].map((level) => {
                const group = practice.filter((item) => item.level === level);
                if (group.length === 0) return null;
                return (
                  <section className="lecture-practice__group" key={level} aria-label={`${level} questions`}>
                    <div className="lecture-practice__group-heading">
                      <h3>{level === 'TRANSFER' ? 'Build deeper understanding' : level === 'APPLY' ? 'Apply it' : 'Check you understand'}</h3>
                      <span className="lecture-practice__group-level">{level}</span>
                    </div>
                    {group.map((item) => <PracticeItemCard key={item.id} item={item} onGrade={handleGrade} />)}
                  </section>
                );
              })}
              {practice.length === 0 && <EmptyState title="No practice yet" message="Practice questions for this lecture are not connected yet." />}
            </>
          )}
        </div>
      ) : (
        <div className="lecture-videos" aria-label="Video explanations">
          {!videos && !error && <LoadingState message="Loading videos…" />}
          {videos && videos.length > 0 && (
            <div className="lecture-videos__grid">
              {videos.map((video) => {
                const targetConcept = video.metadata?.target_concept != null ? String(video.metadata.target_concept) : null;
                const hook = video.metadata?.hook != null ? String(video.metadata.hook) : null;
                const objective = video.metadata?.objective != null ? String(video.metadata.objective) : null;
                const commonMistake = video.metadata?.common_mistake != null ? String(video.metadata.common_mistake) : null;
                const finalTakeaway = video.metadata?.final_takeaway != null ? String(video.metadata.final_takeaway) : null;
                return (
                <article className="lecture-videos__card" key={`${video.title}-${video.sort_order}`}>
                  <div className="lecture-videos__card-heading">
                    <h2>{video.title}</h2>
                    {video.duration_seconds ? <span className="lecture-videos__duration">{Math.ceil(video.duration_seconds / 60)} min</span> : null}
                  </div>
                  {video.description && <p className="muted">{video.description}</p>}
                  {(targetConcept || hook || objective) && (
                    <div className="lecture-videos__script">
                      {targetConcept && <div><span>Explains:</span> {targetConcept}</div>}
                      {hook && <div><span>Hook:</span> {hook}</div>}
                      {objective && <div><span>Goal:</span> {objective}</div>}
                    </div>
                  )}
                  {commonMistake && (
                    <div className="lecture-videos__mistake"><span>Common mistake addressed:</span> {commonMistake}</div>
                  )}
                  {finalTakeaway && (
                    <div className="lecture-videos__takeaway"><span>Takeaway:</span> {finalTakeaway}</div>
                  )}
                  {video.external_url && (
                    <a className="lecture-videos__link" href={video.external_url} target="_blank" rel="noopener noreferrer">Watch video</a>
                  )}
                </article>
                );
              })}
            </div>
          )}
          {videos && videos.length === 0 && <EmptyState title="No videos yet" message="Video explanations for this lecture are not connected yet." />}
        </div>
      )}

      <div className="lecture-page__footer">
        <div className="lecture-page__complete">
          {completed ? (
            <span className="lecture-page__complete-done" aria-label="Lesson complete">✓ Completed</span>
          ) : (
            <button type="button" className="lecture-page__complete-button" onClick={() => void handleComplete()} disabled={completing}>
              {completing ? 'Marking complete…' : 'Mark lesson complete'}
            </button>
          )}
        </div>
        {(prevLesson || nextLesson) && (
          <nav className="lecture-page__pager" aria-label="Lesson navigation">
            {prevLesson ? (
              <button type="button" className="lecture-page__pager-link" onClick={goPrev}>&larr; Previous lesson</button>
            ) : <span />}
            {nextLesson ? (
              <button type="button" className="lecture-page__pager-link lecture-page__pager-link--next" onClick={goNext}>Next lesson &rarr;</button>
            ) : <span />}
          </nav>
        )}
      </div>
    </div>
  );
}
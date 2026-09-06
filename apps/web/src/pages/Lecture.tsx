import { useState } from 'react';
import type { FormEvent } from 'react';
import { Link, useParams } from 'react-router-dom';
import { getCourseById, getLectureById } from '../data/courses';
import NotFound from './NotFound';
import './Courses.css';

type LectureView = 'lecture' | 'ai';

export default function Lecture() {
  const { courseId, lectureId } = useParams();
  const course = courseId ? getCourseById(courseId) : undefined;
  const lecture = courseId && lectureId ? getLectureById(courseId, lectureId) : undefined;
  const [activeView, setActiveView] = useState<LectureView>('lecture');
  const [message, setMessage] = useState('');

  if (!course || !lecture) return <NotFound />;

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setMessage('');
  }

  return (
    <div className="page lecture-page">
      <Link className="course-detail__back" to={`/courses/${course.id}/lectures`}>&larr; Back to Lectures</Link>
      <div className="lecture-page__heading">
        <span className="course-detail__eyebrow">Lecture {String(lecture.number).padStart(2, '0')} · {course.title}</span>
        <h1>{lecture.title}</h1>
      </div>

      <div className="lecture-page__tabs" role="tablist" aria-label="Lecture views">
        <button className={activeView === 'lecture' ? 'lecture-page__tab lecture-page__tab--active' : 'lecture-page__tab'} type="button" role="tab" aria-selected={activeView === 'lecture'} onClick={() => setActiveView('lecture')}>
          Lecture
        </button>
        <button className={activeView === 'ai' ? 'lecture-page__tab lecture-page__tab--active' : 'lecture-page__tab'} type="button" role="tab" aria-selected={activeView === 'ai'} onClick={() => setActiveView('ai')}>
          Ask AI
        </button>
      </div>

      <div className="lecture-page__layout">
        <section className={`lecture-page__viewer ${activeView === 'lecture' ? 'lecture-page__panel--visible' : ''}`} aria-label="Lecture PDF viewer">
          <div className="lecture-page__viewer-toolbar">
            <span>Lecture PDF</span>
            <span className="lecture-page__viewer-status">Viewer ready for lecture material</span>
          </div>
          <div className="lecture-page__document">
            <div className="lecture-page__document-icon" aria-hidden="true">PDF</div>
            <h2>{lecture.title}</h2>
            <p className="muted">The lecture PDF will appear here when course material is connected.</p>
          </div>
        </section>

        <aside className={`lecture-page__assistant ${activeView === 'ai' ? 'lecture-page__panel--visible' : ''}`} aria-label="ARETE AI Learning Assistant">
          <div className="lecture-page__assistant-heading">
            <span className="course-detail__eyebrow">Learning assistant</span>
            <h2>Ask ARETE</h2>
            <p className="muted">Ask anything about this lecture.</p>
          </div>
          <div className="lecture-page__chat" aria-live="polite">
            <p className="lecture-page__chat-empty">Your questions about this lecture will appear here.</p>
          </div>
          <form className="lecture-page__input-row" onSubmit={handleSubmit}>
            <label className="visually-hidden" htmlFor="lecture-question">Ask a question about this lecture</label>
            <input id="lecture-question" value={message} onChange={(event) => setMessage(event.target.value)} placeholder="Ask about this lecture" />
            <button type="submit" disabled={!message.trim()}>Send</button>
          </form>
          <p className="lecture-page__assistant-note">AI answers will be connected to this lecture's material in a future update.</p>
        </aside>
      </div>
    </div>
  );
}
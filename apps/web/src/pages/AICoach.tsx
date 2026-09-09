import { useEffect, useRef, useState } from 'react';
import type { FormEvent } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import { LoadingState, ErrorState, EmptyState } from '../components/ui/StateViews';
import { useApp } from '../state/AppContext';
import { getStudent, sendCoachMessage } from '../data/mockApi';
import { buildCoachContext, pickFocusCompetency } from '../data/coachContext';
import type { CoachMessage, CoachResponse, CoachContextPack, Student } from '../types';
import './AICoach.css';

let idCounter = 0;
function nextId() {
  idCounter += 1;
  return `msg-${idCounter}`;
}

// Navigation state from the Remediation page — opens the coach already
// focused on what needs fixing. Never carries an engine mode: the engine
// decides how to coach entirely on its own.
interface CoachPageState {
  intent?: 'remediate';
  competencyId?: string;
  misconception?: string | null;
}

// The seed message starts the conversation; the ENGINE words the coach's
// reply from the student's real adaptive context. No mode is ever chosen
// here — that is backend-only behaviour.
function openingMessage(intent?: string): string {
  if (intent === 'remediate') {
    return "Let's fix the weak spots, one step at a time. Where should I start?";
  }
  return "I'm ready to learn. Where should I focus?";
}

// The engine's suggested actions are curriculum facts; we render them in
// human language by swapping internal competency identifiers for their titles.
function humanizeActions(actions: string[], student: Student | null): string[] {
  const map = (student?.competencies ?? []).map((c) => ({ code: c.id, name: c.name }));
  if (map.length === 0) return actions;
  return actions.map((action) =>
    map.reduce((acc, { code, name }) => acc.split(code).join(name), action)
  );
}

export default function AICoach() {
  const navigate = useNavigate();
  const location = useLocation();
  const pageState = (location.state as CoachPageState | null) ?? null;
  const { student, setStudent, diagnosticResults } = useApp();

  const [messages, setMessages] = useState<CoachMessage[]>([]);
  const [input, setInput] = useState('');
  const [thinking, setThinking] = useState(false);
  const [started, setStarted] = useState(false);
  const [loadError, setLoadError] = useState('');
  const [contextPack, setContextPack] = useState<CoachContextPack | null>(null);
  const [suggestedActions, setSuggestedActions] = useState<string[]>([]);
  const [finished, setFinished] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  const activeCompetency = pickFocusCompetency(student);
  const isRemediation = pageState?.intent === 'remediate';

  const misconceptionRaw =
    (isRemediation && pageState?.misconception) || contextPack?.misconception || null;
  const misconceptionText =
    misconceptionRaw && misconceptionRaw.includes('_')
      ? `I noticed something in your recent attempts — let's revisit ${misconceptionRaw.replace(/_/g, ' ').toLowerCase()}, right?`
      : null;

  const humanizedActions = humanizeActions(suggestedActions, student);

  async function startConversation() {
    setStarted(true);
    setLoadError('');
    setThinking(true);
    try {
      let s = student;
      if (!s) {
        s = await getStudent();
        setStudent(s);
      }
      const pack = buildCoachContext(s, diagnosticResults);
      setContextPack(pack);
      const focused = pickFocusCompetency(s);
      const reply = await sendCoachMessage({
        message: openingMessage(pageState?.intent),
        competencyId: pageState?.competencyId ?? focused?.id,
        context: pack,
      });
      applyReply(reply);
    } catch (err) {
      setLoadError(err instanceof Error ? err.message : 'The AI Coach is unavailable right now.');
    } finally {
      setThinking(false);
    }
  }

  function applyReply(reply: CoachResponse) {
    setSuggestedActions(reply.suggestedActions);
    setFinished(reply.finished);
    setMessages((prev) => [
      ...prev,
      { id: nextId(), sender: 'coach', text: reply.message },
    ]);
  }

  useEffect(() => {
    if (!started) startConversation();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, thinking]);

  async function sendText(text: string) {
    if (!text || thinking || finished) return;
    setMessages((prev) => [...prev, { id: nextId(), sender: 'student', text }]);
    setInput('');
    setThinking(true);
    try {
      const reply = await sendCoachMessage({
        message: text,
        competencyId: activeCompetency?.id ?? pageState?.competencyId,
        context: contextPack ?? undefined,
      });
      applyReply(reply);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          id: nextId(),
          sender: 'coach',
          text: `I couldn't respond just now — ${err instanceof Error ? err.message : 'please try again.'}`,
        },
      ]);
    } finally {
      setThinking(false);
    }
  }

  function handleSend(e: FormEvent) {
    e.preventDefault();
    sendText(input.trim());
  }

  if (started && !loadError && student && student.competencies.length === 0) {
    return (
      <div className="page-narrow ai-coach">
        <Card padding="lg" className="ai-coach__panel">
          <div className="ai-coach__header">
            <img className="ai-coach__avatar" src="/logo.jpg" alt="" />
            <h1 className="ai-coach__title">AI Coach</h1>
          </div>
          <EmptyState
            icon="🧭"
            title="Let's find your starting point"
            message="There's nothing to coach you on yet. A short diagnostic will map your strengths and focus areas, and the coach will pick up from there."
            action={
              <Button size="lg" onClick={() => navigate('/my-learning/diagnostic')}>
                Start the Diagnostic
              </Button>
            }
          />
        </Card>
      </div>
    );
  }

  return (
    <div className="page-narrow ai-coach">
      {/* Adaptive context — shown in plain language, driven by real data. */}
      <div className="ai-coach__intro">
        <span className="ai-coach__intro-eyebrow">
          {isRemediation ? 'Your focus right now' : 'What we\u2019re working on'}
        </span>
        <h1 className="ai-coach__intro-title">
          {isRemediation
            ? 'Let\u2019s fix that together.'
            : contextPack?.focus ?? 'Your learning path'}
        </h1>
        {contextPack?.earliestNextStep && (
          <p className="ai-coach__intro-line">Up next: {contextPack.earliestNextStep}.</p>
        )}
        {misconceptionText && <p className="ai-coach__intro-note">{misconceptionText}</p>}
      </div>

      <Card padding="lg" className="ai-coach__panel">
        <div className="ai-coach__header">
          <img className="ai-coach__avatar" src="/logo.jpg" alt="" />
          <h1 className="ai-coach__title">Coach</h1>
          {finished && <Badge tone="accent">Demonstrated</Badge>}
        </div>

        {loadError ? (
          <ErrorState message={loadError} onRetry={startConversation} />
        ) : (started && thinking && messages.length === 0) ? (
          <LoadingState message="Your coach is getting ready…" />
        ) : (
          <>
            <div className="ai-coach__messages">
              {messages.map((m) => (
                <div key={m.id} className={`ai-coach__bubble ai-coach__bubble--${m.sender}`}>
                  <span className="ai-coach__bubble-sender">
                    {m.sender === 'coach' ? 'Coach' : 'You'}
                  </span>
                  <p>{m.text}</p>
                </div>
              ))}
              {thinking && (
                <div className="ai-coach__bubble ai-coach__bubble--coach ai-coach__bubble--thinking">
                  <span className="ai-coach__bubble-sender">Coach</span>
                  <span className="ai-coach__typing" aria-hidden="true">
                    <i />
                    <i />
                    <i />
                  </span>
                </div>
              )}
              <div ref={bottomRef} />
            </div>

            {humanizedActions.length > 0 && !finished && (
              <div className="ai-coach__suggestions">
                <span className="ai-coach__suggestions-label">Coach suggests:</span>
                <div className="ai-coach__chips">
                  {humanizedActions.map((action, i) => (
                    <button
                      key={i}
                      type="button"
                      className="ai-coach__chip"
                      disabled={thinking}
                      onClick={() => sendText(action)}
                    >
                      {action}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {finished ? (
              <div className="ai-coach__finished">
                <p className="muted">{'You\u2019ve worked through this area together. Ready to prove it?'}</p>
                <Button onClick={() => navigate('/apply-review/review')}>
                  Continue to Review
                </Button>
              </div>
            ) : (
              <form className="ai-coach__input-row" onSubmit={handleSend}>
                <input
                  className="ai-coach__input"
                  type="text"
                  placeholder="Tell the Coach how you're thinking…"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  disabled={thinking}
                  aria-label="Message to AI Coach"
                />
                <Button type="submit" disabled={!input.trim() || thinking}>
                  Send
                </Button>
              </form>
            )}
          </>
        )}
      </Card>
    </div>
  );
}
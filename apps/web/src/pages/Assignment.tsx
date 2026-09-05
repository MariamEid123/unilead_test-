import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { useApp } from '../state/AppContext';
import { getStudent } from '../data/mockApi';
import type { Student } from '../types';
import './Assignment.css';

export default function Assignment() {
  const navigate = useNavigate();
  const { student, setStudent } = useApp();
  const [loadedStudent, setLoadedStudent] = useState<Student | null>(student);
  const [response, setResponse] = useState('');
  const [submitted, setSubmitted] = useState(false);
  useEffect(() => {
    if (student) return;
    void getStudent().then((value) => {
      setLoadedStudent(value);
      setStudent(value);
    }).catch(() => undefined);
  }, [setStudent, student]);

  const currentStudent = student ?? loadedStudent;
  const competency = currentStudent?.competencies.find((item) => item.status === 'DEVELOPING') ?? currentStudent?.competencies[0];
  const topic = competency?.name ?? 'your current topic';

  return (
    <div className="page-narrow assignment">
      <button className="assignment__back" type="button" onClick={() => navigate('/my-learning/practice')}>← Back</button>
      <div className="assignment__eyebrow">Apply what you learned</div>
      <h1 className="assignment__title">Assignment: {topic}</h1>
      <p className="muted assignment__subtitle">
        Use the idea from your lesson and simulation to explain your reasoning in a real situation.
      </p>

      {submitted ? (
        <Card padding="lg" className="assignment__success">
          <div className="assignment__success-icon" aria-hidden="true">✓</div>
          <h2>Assignment submitted successfully.</h2>
          <p className="muted">Your response is saved for this learning session. Continue to the next activity.</p>
          <Button onClick={() => navigate('/progress')}>View Progress</Button>
        </Card>
      ) : (
        <>
          <Card padding="lg" className="assignment__brief">
            <div className="assignment__meta"><span>Assignment 01</span><span>10 min</span></div>
            <h2>Show how you would apply the concept.</h2>
            <p className="muted">Describe the decision you would make, the evidence you would watch, and how you would know it worked.</p>
            <ul>
              <li>Use at least two ideas from the lesson.</li>
              <li>Refer to what you observed in the simulation.</li>
              <li>Explain your reasoning in your own words.</li>
            </ul>
          </Card>
          <Card padding="lg" className="assignment__response">
            <label htmlFor="assignment-response">Your response</label>
            <textarea id="assignment-response" rows={8} value={response} onChange={(event) => setResponse(event.target.value)} placeholder="Write your approach and what you would look for..." />
            <div className="assignment__actions">
              <Button variant="ghost" onClick={() => navigate('/my-learning/practice')}>Back to Practice</Button>
              <Button onClick={() => setSubmitted(true)} disabled={!response.trim()}>Submit Assignment</Button>
            </div>
          </Card>
        </>
      )}
    </div>
  );
}

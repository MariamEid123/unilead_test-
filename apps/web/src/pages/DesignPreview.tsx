import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { designPreviewLogin } from '../data/mockApi';
import { useApp } from '../state/AppContext';

let previewLoginPromise: ReturnType<typeof designPreviewLogin> | null = null;

function loadPreviewSession() {
  previewLoginPromise ??= designPreviewLogin();
  return previewLoginPromise;
}

export default function DesignPreview() {
  const navigate = useNavigate();
  const { setSession } = useApp();

  useEffect(() => {
    void loadPreviewSession().then((session) => {
      setSession(session);
      window.location.replace('/home');
    }).catch(() => {
      navigate('/login', { replace: true });
    });
  }, [navigate, setSession]);

  return <div aria-busy="true" />;
}
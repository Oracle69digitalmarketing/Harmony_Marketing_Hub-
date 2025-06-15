import { useState } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function Campaigns() {
  const [subject, setSubject] = useState('');
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [preview, setPreview] = useState(false);
  const [gptTopic, setGptTopic] = useState('');
  const token = localStorage.getItem('token');

  const generateGPT = async () => {
    const res = await axios.post(`${API}/copywriter`, {
      type: 'email',
      topic: gptTopic,
      tone: 'friendly',
      audience: 'customers',
      cta: 'Get Started'
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setBody(res.data.generated);
  };

  const submitDraft = async () => {
    await axios.post(`${API}/campaigns`, { title, subject, body }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert("Campaign saved!");
    setTitle('');
    setSubject('');
    setBody('');
    setPreview(false);
  };

  return (
    <div>
      <h2>📬 Email Campaign Builder</h2>

      <div style={styles.gpt}>
        <input
          value={gptTopic}
          onChange={(e) => setGptTopic(e.target.value)}
          placeholder="Need help? Enter a product/topic"
        />
        <button onClick={generateGPT}>Generate with AI</button>
      </div>

      <form onSubmit={(e) => e.preventDefault()} style={styles.form}>
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Campaign title" required />
        <input value={subject} onChange={(e) => setSubject(e.target.value)} placeholder="Email subject" required />
        <textarea
          rows="10"
          value={body}
          onChange={(e) => setBody(e.target.value)}
          placeholder="Email body..."
          required
        />
        <div style={styles.actions}>
          <button type="button" onClick={() => setPreview(!preview)}>
            {preview ? "Edit" : "Preview"}
          </button>
          <button type="button" onClick={submitDraft}>Save Campaign</button>
        </div>
      </form>

      {preview && (
        <div style={styles.preview}>
          <h4>📧 Preview</h4>
          <strong>Subject:</strong> {subject}<br /><br />
          <div dangerouslySetInnerHTML={{ __html: body.replace(/\n/g, '<br/>') }} />
        </div>
      )}
    </div>
  );
}

const styles = {
  gpt: {
    display: 'flex',
    gap: '1rem',
    marginBottom: '1.5rem'
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    maxWidth: '600px',
    marginBottom: '2rem'
  },
  actions: {
    display: 'flex',
    gap: '1rem'
  },
  preview: {
    padding: '1rem',
    backgroundColor: '#f0f0f0',
    borderRadius: '6px',
    maxWidth: '600px'
  }
};

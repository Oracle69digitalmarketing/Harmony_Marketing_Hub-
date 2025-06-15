import { useState } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function Copywriter() {
  const [type, setType] = useState('caption');
  const [topic, setTopic] = useState('');
  const [tone, setTone] = useState('friendly');
  const [audience, setAudience] = useState('');
  const [cta, setCta] = useState('Learn more');
  const [output, setOutput] = useState('');
  const token = localStorage.getItem('token');

  const generate = async (e) => {
    e.preventDefault();
    const res = await axios.post(`${API}/copywriter`, {
      type, topic, tone, audience, cta
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setOutput(res.data.generated);
  };

  return (
    <div>
      <h2>✍️ GPT Copywriting Assistant</h2>
      <form onSubmit={generate} style={styles.form}>
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option value="caption">Caption</option>
          <option value="email">Email</option>
          <option value="ad">Ad</option>
        </select>
        <input value={topic} onChange={(e) => setTopic(e.target.value)} placeholder="What's the topic?" required />
        <input value={tone} onChange={(e) => setTone(e.target.value)} placeholder="Tone (e.g., urgent)" />
        <input value={audience} onChange={(e) => setAudience(e.target.value)} placeholder="Audience (e.g., busy moms)" />
        <input value={cta} onChange={(e) => setCta(e.target.value)} placeholder="Call to Action" />
        <button type="submit">Generate</button>
      </form>

      {output && (
        <div style={styles.output}>
          <h4>Generated Copy</h4>
          <pre>{output}</pre>
        </div>
      )}
    </div>
  );
}

const styles = {
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.8rem',
    maxWidth: '400px',
    marginBottom: '2rem'
  },
  output: {
    background: '#f0f0f0',
    padding: '1rem',
    borderRadius: '6px'
  }
};

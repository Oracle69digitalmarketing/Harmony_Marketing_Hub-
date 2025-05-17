import { useState } from 'react';
import axios from 'axios';

export default function Copywriter() {
  const [form, setForm] = useState({
    content_type: '',
    tone: '',
    message: '',
    target_audience: '',
    cta: ''
  });
  const [generated, setGenerated] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleGenerate = async () => {
    const token = localStorage.getItem('token');
    const res = await axios.post('/api/generate-copy', form, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setGenerated(res.data.copy);
  };

  return (
    <div>
      <h2>GPT Copywriting Assistant</h2>
      <input name="content_type" placeholder="e.g., Facebook Ad" onChange={handleChange} />
      <input name="tone" placeholder="e.g., Friendly, Professional" onChange={handleChange} />
      <textarea name="message" placeholder="Main message or offer" onChange={handleChange} />
      <input name="target_audience" placeholder="Who is this for?" onChange={handleChange} />
      <input name="cta" placeholder="Call-to-action (e.g., Buy Now)" onChange={handleChange} />
      <button onClick={handleGenerate}>Generate Copy</button>
      <pre>{generated}</pre>
    </div>
  );
}
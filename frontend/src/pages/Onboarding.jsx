import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Onboarding() {
  const [form, setForm] = useState({
    business_name: '',
    industry: '',
    target_audience: '',
    main_services: ''
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const token = localStorage.getItem('token');
    await axios.put('/api/profile', form, {
      headers: { Authorization: `Bearer ${token}` }
    });
    navigate('/dashboard');
  };

  return (
    <div>
      <h2>Business Setup</h2>
      <input name="business_name" placeholder="Business Name" onChange={handleChange} />
      <input name="industry" placeholder="Industry" onChange={handleChange} />
      <input name="target_audience" placeholder="Target Audience" onChange={handleChange} />
      <input name="main_services" placeholder="Main Services (comma separated)" onChange={handleChange} />
      <button onClick={handleSubmit}>Finish Setup</button>
    </div>
  );
}
import { useState, useEffect } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function Clients() {
  const [clients, setClients] = useState([]);
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  const token = localStorage.getItem('token');

  useEffect(() => {
    fetchClients();
  }, []);

  const fetchClients = async () => {
    const res = await axios.get(`${API}/clients`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setClients(res.data);
  };

  const addClient = async (e) => {
    e.preventDefault();
    await axios.post(`${API}/clients`, { name, phone, email }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setName('');
    setPhone('');
    setEmail('');
    fetchClients();
  };

  return (
    <div>
      <h2>👥 Clients</h2>
      <form onSubmit={addClient} style={styles.form}>
        <input value={name} onChange={e => setName(e.target.value)} placeholder="Client name" required />
        <input value={phone}

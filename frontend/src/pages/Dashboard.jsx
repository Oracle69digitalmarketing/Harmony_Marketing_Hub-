import { useEffect, useState } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get(`${API}/dashboard`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setSummary(res.data);
      } catch (err) {
        console.error("Failed to load dashboard", err);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) return <p>Loading dashboard...</p>;

  return (
    <div style={styles.wrapper}>
      <h2>📊 Welcome to your Dashboard</h2>

      <section style={styles.cardRow}>
        <div style={styles.card}>
          <h3>Clients</h3>
          <p>{summary.clients}</p>
        </div>
        <div style={styles.card}>
          <h3>Open Jobs</h3>
          <p>{summary.open_jobs}</p>
        </div>
        <div style={styles.card}>
          <h3>Completed</h3>
          <p>{summary.completed_jobs}</p>
        </div>
      </section>

      <section style={styles.aiBlock}>
        <h3>🧠 AI Insight</h3>
        <p>{summary.ai_message || "Your AI assistant will soon deliver growth tips here."}</p>
      </section>
    </div>
  );
}

const styles = {
  wrapper: { padding: '1rem' },
  cardRow: {
    display: 'flex',
    gap: '1rem',
    marginTop: '1.5rem',
    marginBottom: '2rem',
  },
  card: {
    background: '#f9f9f9',
    padding: '1rem',
    borderRadius: '8px',
    flex: 1,
    boxShadow: '0 0 5px rgba(0,0,0,0.1)',
    textAlign: 'center',
  },
  aiBlock: {
    background: '#e3f2fd',
    padding: '1rem',
    borderRadius: '6px',
  }
};

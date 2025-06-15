import { useEffect, useState } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function GrowthPlanner() {
  const [data, setData] = useState(null);
  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchGrowth = async () => {
      const res = await axios.get(`${API}/growth`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setData(res.data);
    };
    fetchGrowth();
  }, []);

  if (!data) return <p>Loading planner...</p>;

  return (
    <div style={styles.container}>
      <h2>📈 AI Growth Planner</h2>
      <div style={styles.kpiRow}>
        <KPI label="Clients" value={data.client_count} />
        <KPI label="Completed Jobs" value={data.completed_jobs} />
        <KPI label="Avg Lead Time" value={data.avg_lead_time} />
        <KPI label="Forecasted Orders" value={data.predicted_orders} />
      </div>
      <div style={styles.recommendation}>
        <h4>🧠 Smart Tip:</h4>
        <p>{data.recommendation}</p>
      </div>
    </div>
  );
}

function KPI({ label, value }) {
  return (
    <div style={styles.kpi}>
      <h4>{label}</h4>
      <p style={{ fontSize: '1.4rem', fontWeight: 'bold' }}>{value}</p>
    </div>
  );
}

const styles = {
  container: { padding: '1rem' },
  kpiRow: {
    display: 'flex',
    gap: '1rem',
    marginBottom: '1.5rem'
  },
  kpi: {
    background: '#f3f3f3',
    padding: '1rem',
    borderRadius: '8px',
    flex: 1,
    textAlign: 'center'
  },
  recommendation: {
    background: '#e3f2fd',
    padding: '1rem',
    borderRadius: '8px'
  }
};

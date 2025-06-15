import { Link } from 'react-router-dom';

export default function HomePage() {
  return (
    <div style={styles.container}>
      <h1>Harmony Marketing Hub</h1>
      <p>Welcome to your AI-powered business growth assistant.</p>
      <Link to="/login" style={styles.button}>Login to Dashboard</Link>
    </div>
  );
}

const styles = {
  container: {
    padding: '4rem',
    textAlign: 'center',
    fontFamily: 'Segoe UI, sans-serif',
  },
  button: {
    marginTop: '2rem',
    display: 'inline-block',
    padding: '0.75rem 1.5rem',
    backgroundColor: '#0070f3',
    color: '#fff',
    borderRadius: '6px',
    textDecoration: 'none',
    fontWeight: 'bold',
  }
};

import { Link } from 'react-router-dom';

export default function HomePage() {
  return (
    <div style={styles.container}>
      <h1>Harmony Marketing Hub</h1>
      <p>Your AI-powered business growth assistant.</p>
      <div style={styles.actions}>
        <Link to="/login" style={styles.login}>Login</Link>
        <Link to="/register" style={styles.register}>Register</Link>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: '4rem',
    textAlign: 'center',
    fontFamily: 'Segoe UI, sans-serif',
  },
  actions: {
    display: 'flex',
    gap: '1rem',
    justifyContent: 'center',
    marginTop: '2rem',
  },
  login: {
    padding: '0.75rem 1.5rem',
    backgroundColor: '#0070f3',
    color: '#fff',
    borderRadius: '6px',
    textDecoration: 'none',
    fontWeight: 'bold',
  },
  register: {
    padding: '0.75rem 1.5rem',
    backgroundColor: '#28a745',
    color: '#fff',
    borderRadius: '6px',
    textDecoration: 'none',
    fontWeight: 'bold',
  },
};

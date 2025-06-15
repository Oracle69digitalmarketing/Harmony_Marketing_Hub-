import { Link, useNavigate } from 'react-router-dom';

export default function Sidebar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <aside style={styles.sidebar}>
      <h3 style={styles.title}>Harmony Hub</h3>
      <nav style={styles.nav}>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/clients">Clients</Link>
        <Link to="/campaigns">Campaigns</Link>
        <Link to="/copywriter">Copywriter</Link>
        <Link to="/portfolio">Portfolio</Link>
        <Link to="/growth-planner">AI Planner</Link>
        <button onClick={logout} style={styles.logout}>Logout</button>
      </nav>
    </aside>
  );
}

const styles = {
  sidebar: {
    width: '200px',
    background: '#1d1f2f',
    color: '#fff',
    height: '100vh',
    padding: '20px',
    boxSizing: 'border-box',
  },
  title: {
    marginBottom: '2rem',
    fontSize: '1.2rem',
  },
  nav: {
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
  },
  logout: {
    marginTop: '2rem',
    background: '#c00',
    color: '#fff',
    border: 'none',
    padding: '0.5rem 1rem',
    cursor: 'pointer',
    borderRadius: '4px',
  },
};

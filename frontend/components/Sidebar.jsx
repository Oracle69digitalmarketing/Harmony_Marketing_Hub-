import { Link, useNavigate } from 'react-router-dom';
import './Sidebar.css';

export default function Sidebar() {
  const navigate = useNavigate();
  const logout = () => {
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <div className="sidebar">
      <h3>Harmony Hub</h3>
      <nav>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/portfolio">Portfolio</Link>
        <Link to="/clients">Clients</Link>
        <Link to="/campaigns">Email Campaigns</Link>
        <Link to="/copywriter">Copywriter</Link>
        <Link to="/growth-planner">AI Planner</Link>
        <button className="logout" onClick={logout}>Logout</button>
      </nav>
    </div>
  );
}

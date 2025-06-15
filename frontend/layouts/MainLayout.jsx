import Sidebar from '../components/Sidebar';

export default function MainLayout({ children }) {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <div style={{ marginLeft: '200px', padding: '20px', width: '100%' }}>
        {children}
      </div>
    </div>
  );
}

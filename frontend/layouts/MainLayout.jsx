import Sidebar from '../components/Sidebar';

export default function MainLayout({ children }) {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <main style={{ flexGrow: 1, padding: '2rem' }}>{children}</main>
    </div>
  );
}

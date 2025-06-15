export default function HomePage() {
  return (
    <main style={styles.main}>
      <h1 style={styles.title}>Harmony Marketing Hub</h1>
      <p style={styles.subtitle}>
        Welcome to your AI-powered business growth platform.
      </p>
      <div style={styles.section}>
        <p>🚀 You’re live on Vercel with a clean Vite + React setup.</p>
        <p>✅ Start building features in <code>src/pages/</code> and <code>src/components/</code>.</p>
      </div>
    </main>
  );
}

const styles = {
  main: {
    fontFamily: 'Segoe UI, Roboto, sans-serif',
    padding: '4rem 2rem',
    maxWidth: '720px',
    margin: '0 auto',
    textAlign: 'center',
  },
  title: {
    fontSize: '2.5rem',
    color: '#1d1f2f',
    marginBottom: '1rem',
  },
  subtitle: {
    fontSize: '1.25rem',
    color: '#555',
  },
  section: {
    marginTop: '2rem',
    backgroundColor: '#f5f5f5',
    padding: '1.5rem',
    borderRadius: '8px',
    textAlign: 'left',
  },
};

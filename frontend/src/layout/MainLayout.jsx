export default function MainLayout({ children }) {
  return (
    <div className="min-h-screen p-4 bg-gray-50 text-gray-800">
      <header className="mb-4 font-bold text-xl">Harmony Dashboard</header>
      <main>{children}</main>
    </div>
  );
}

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import RequireAuth from "./utils/RequireAuth";
import MainLayout from "./layout/MainLayout";

// Pages
import HomePage from "./pages/HomePage";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Calendar from "./pages/ContentCalendar";
import Optimizer from "./pages/Optimizer";
import Insights from "./pages/Insights";
import Team from "./pages/Team";
import HealthDashboard from "./pages/HealthDashboard";
import SendNow from "./pages/SendNow";
import GrowthPlanner from "./pages/GrowthPlanner"; // ✅ Make sure this path is correct
import Billing from "./pages/Billing";

function App() {
  return (
    <Router>
      <Routes>
        {/* Public routes */}
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected routes */}
        <Route
          path="/dashboard"
          element={
            <RequireAuth>
              <MainLayout>
                <Dashboard />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/calendar"
          element={
            <RequireAuth>
              <MainLayout>
                <Calendar />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/optimizer"
          element={
            <RequireAuth>
              <MainLayout>
                <Optimizer />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/insights"
          element={
            <RequireAuth>
              <MainLayout>
                <Insights />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/team"
          element={
            <RequireAuth>
              <MainLayout>
                <Team />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/health"
          element={
            <RequireAuth>
              <MainLayout>
                <HealthDashboard />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/send"
          element={
            <RequireAuth>
              <MainLayout>
                <SendNow />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/billing"
          element={
            <RequireAuth>
              <MainLayout>
                <Billing />
              </MainLayout>
            </RequireAuth>
          }
        />
        <Route
          path="/growth-planner"
          element={
            <RequireAuth>
              <MainLayout>
                <GrowthPlanner />
              </MainLayout>
            </RequireAuth>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;

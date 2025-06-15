import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Dashboard from './pages/Dashboard';
import Onboarding from './pages/Onboarding';
import Copywriter from './pages/Copywriter';
import Clients from './pages/Clients';
import Portfolio from './pages/Portfolio';
import EmailCampaigns from './pages/EmailCampaigns';
import GrowthPlanner from './pages/GrowthPlanner';
import MainLayout from './layouts/MainLayout';
import RequireAuth from './utils/RequireAuth';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/onboarding" element={<Onboarding />} />

        <Route path="/dashboard" element={<RequireAuth><MainLayout><Dashboard /></MainLayout></RequireAuth>} />
        <Route path="/portfolio" element={<RequireAuth><MainLayout><Portfolio /></MainLayout></RequireAuth>} />
        <Route path="/clients" element={<RequireAuth><MainLayout><Clients /></MainLayout></RequireAuth>} />
        <Route path="/campaigns" element={<RequireAuth><MainLayout><EmailCampaigns /></MainLayout></RequireAuth>} />
        <Route path="/copywriter" element={<RequireAuth><MainLayout><Copywriter /></MainLayout></RequireAuth>} />
        <Route path="/growth-planner" element={<RequireAuth><MainLayout><GrowthPlanner /></MainLayout></RequireAuth>} />
      </Routes>
    </BrowserRouter>
  );
}

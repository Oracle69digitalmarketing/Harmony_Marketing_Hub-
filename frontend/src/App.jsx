import { Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './pages/HomePage';
import NotFound from './pages/NotFound';
import Dashboard from './pages/Dashboard';
import Clients from './pages/Clients';
import Campaigns from './pages/Campaigns';
import Copywriter from './pages/Copywriter';
import Portfolio from './pages/Portfolio';
import GrowthPlanner from './pages/GrowthPlanner';
import Login from './pages/Login';
import Register from './pages/Register';

import RequireAuth from './utils/RequireAuth';
import MainLayout from './layouts/MainLayout';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      <Route
        path="/dashboard"
        element={
          <RequireAuth>
            <MainLayout><Dashboard /></MainLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/clients"
        element={
          <RequireAuth>
            <MainLayout><Clients /></MainLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/campaigns"
        element={
          <RequireAuth>
            <MainLayout><Campaigns /></MainLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/copywriter"
        element={
          <RequireAuth>
            <MainLayout><Copywriter /></MainLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/portfolio"
        element={
          <RequireAuth>
            <MainLayout><Portfolio /></MainLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/growth-planner"
        element={
          <RequireAuth>
            <MainLayout><GrowthPlanner /></MainLayout>
          </RequireAuth>
        }
      />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

<Route
  path="/clients"
  element={
    <RequireAuth>
      <MainLayout><Clients /></MainLayout>
    </RequireAuth>
  }
/>

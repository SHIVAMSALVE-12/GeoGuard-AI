import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import HomePage from "./pages/Home/HomePage";
import AssessmentPage from "./pages/Assessment/AssessmentPage";
import DashboardPage from "./pages/Dashboard/DashboardPage";
import AboutPage from "./pages/About/AboutPage";

export default function App() {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>

          <Route
            path="/"
            element={<HomePage />}
          />

          <Route
            path="/assessment"
            element={<AssessmentPage />}
          />

          <Route
            path="/dashboard"
            element={<DashboardPage />}
          />
           
          <Route
            path="/about"
            element={<AboutPage />}
          />

          <Route
            path="*"
            element={<Navigate to="/" replace />}
          />
          
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
}
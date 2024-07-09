import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import TopMenu from './components/TopMenu';
import SignupFormPage from './pages/auth/SignupFormPage';
import SignInFormPage from './pages/auth/SignInFormPage';
import AccountPage from './pages/AccountPage';
import CarListPage from './pages/CarListPage';
import ManagerPanelPage from './pages/ManagerPanelPage';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './routes/ProtectedRoute';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <TopMenu />
          <Routes>
            <Route path="/signup" element={<SignupFormPage />} />
            <Route path="/signin" element={<SignInFormPage />} />
            <Route path="/account" element={<AccountPage />} />
            <Route path="/" element={<CarListPage />} />

            <Route element={<ProtectedRoute allowedRoles={['manager']} />}>
              <Route path="/manager" element={<ManagerPanelPage />} />
            </Route>

            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;

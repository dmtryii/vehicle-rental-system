import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const TopMenu = () => {
  const navigate = useNavigate();
  const { authState, logout } = useAuth();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Vehicle Rental System
        </Typography>
        <Box>

          <Button color="inherit" onClick={() => navigate('/')}>
            Cars
          </Button>

          {authState.user && authState.user.roles.some(role => role.name === 'manager') && (
            <Button color="inherit" onClick={() => navigate('/manager')}>
              Manager panel
            </Button>
          )}

          <Button color="inherit" onClick={() => navigate('/account')}>
            Account
          </Button>

          {!authState.user ? (
            <Button color="inherit" onClick={() => navigate('/signin')}>
              Sign In
            </Button>
          ) : (
            <Button color="inherit" onClick={() => {
              navigate('/signin');
              logout();
            }}> 
            Log out
            </Button>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default TopMenu;
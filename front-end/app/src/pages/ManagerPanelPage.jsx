import React from 'react';
import { Container, Typography } from '@mui/material';

const ManagerPanel = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Manager Panel
      </Typography>
      <Typography variant="body1">
        This is a restricted area. Only users with the manager role can access this page.
      </Typography>
    </Container>
  );
};

export default ManagerPanel;
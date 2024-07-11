import React from 'react';
import { Card, CardContent, CardMedia, Typography, Box } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

const AddNewCarCard = ({ action }) => (
  <Card onClick={action} style={{ cursor: 'pointer', height: '100%' }}>
    <CardMedia
      component="div"
      style={{ 
        height: '140px', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        backgroundColor: '#f0f0f0' }}
    >
      <AddIcon style={{ fontSize: 40, color: '#000' }} />
    </CardMedia>
    <CardContent style={{ flex: 1 }}>
      <Box display="flex" justifyContent="center">
        <Typography variant="h5" component="div">
          Add New Car
        </Typography>
      </Box>
    </CardContent>
  </Card>
);

export default AddNewCarCard;
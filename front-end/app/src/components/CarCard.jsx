import React from 'react';
import { Card, CardContent, CardMedia, Typography, IconButton, Box } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import { useAuth } from '../context/AuthContext';


const CarCard = ({ car, onDelete, onEdit }) => {

  const { authState } = useAuth();

  return (
      <Card>
        <CardMedia
          component="img"
          height="140"
          image={car.picture_url}
          alt={`${car.manufacturer.name} ${car.name}`}
        />
        <CardContent>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Typography gutterBottom variant="h5" component="div">
            {car.manufacturer.name} {car.name}
          </Typography>
  
          {authState.user && authState.user.roles.some(role => role.name === 'manager') && (
            <Box>
              <IconButton onClick={() => {onEdit(car)}}>
                <EditIcon />
              </IconButton>
              <IconButton onClick={() => {onDelete(car.id)}}>
                <DeleteIcon />
              </IconButton>
            </Box>
          )}

        </Box>
        <Typography variant="body2" color="text.secondary">
          Year: {car.years}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Price: ${car.price}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Status: {car.status}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          License Plate: {car.license_plate}
        </Typography>
      </CardContent>
      </Card>
  );
} 

export default CarCard;
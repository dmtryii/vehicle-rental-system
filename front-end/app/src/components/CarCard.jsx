import React from 'react';
import { Card, CardContent, CardMedia, Typography } from '@mui/material';

const CarCard = ({ car }) => (
    <Card>
      <CardMedia
        component="img"
        height="140"
        image={`https://via.placeholder.com/300x140.png?text=${car.manufacturer.name}+${car.name}`}
        alt={`${car.manufacturer.name} ${car.name}`}
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {car.manufacturer.name} {car.name}
        </Typography>
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

export default CarCard;
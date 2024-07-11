import React, { useEffect, useState } from 'react';
import { Grid, Container } from '@mui/material';
import axios from 'axios';
import CarCard from '../components/CarCard';
import AddNewCarCard from '../components/AddNewCarCard';
import { useAuth } from '../context/AuthContext';
import CarForm from './CarForm';

const CarListPage = () => {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [formOpen, setFormOpen] = useState(false);
  const [selectedCar, setSelectedCar] = useState(null);
  const { authState } = useAuth();

  useEffect(() => {
    const fetchCars = async () => {
      try {
        const response = await axios.get('http://localhost:5004/vehicles/');
        setCars(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchCars();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  const handleDelete = async (carId) => {
    const confirmed = window.confirm("Are you sure you want to delete this car?");
    if (confirmed) {
      try {
        await axios.delete(`http://localhost:5004/vehicles/${carId}`);
        setCars(cars.filter((car) => car.id !== carId));
      } catch (err) {
        console.error('Failed to delete car:', err);
        setError(err);
      }
    }
  };

  const handleOpenForm = (car = null) => {
    setSelectedCar(car);
    setFormOpen(true);
  };

  const handleCloseForm = () => {
    setFormOpen(false);
    setSelectedCar(null);
  };

  const refreshCars = async () => {
    const response = await axios.get('http://localhost:5004/vehicles/');
    setCars(response.data);
  };

  return (
    <Container>
      <CarForm
        open={formOpen} 
        handleClose={handleCloseForm} 
        refreshCars={refreshCars} 
        car={selectedCar} />
      <Grid container spacing={4} mt={2}>

        {authState.user && authState.user.roles.some(role => role.name === 'manager') && (
          <Grid item xs={12} sm={6} md={4}>
            <AddNewCarCard action={() => {
              handleOpenForm();
            }} />
          </Grid>
        )}

        {cars.map((car) => (
          <Grid item key={car.id} xs={12} sm={6} md={4}>
            <CarCard
               car={car} 
               onDelete={handleDelete} 
               onEdit={() => handleOpenForm(car)} />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default CarListPage;
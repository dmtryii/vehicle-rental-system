import React, { useState, useEffect } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, Button, TextField, MenuItem } from '@mui/material';
import axios from 'axios';

const CarForm = ({ open, handleClose, refreshCars, car }) => {
  const [formData, setFormData] = useState({
    name: '',
    price: '',
    years: '',
    license_plate: '',
    picture_url: '',
    manufacturer_id: ''
  });

  const [manufacturers, setManufacturers] = useState([]);

  useEffect(() => {
    const fetchManufacturers = async () => {
      try {
        const response = await axios.get('http://localhost:5004/vehicles/manufacturers');
        setManufacturers(response.data);
      } catch (err) {
        console.error('Failed to fetch manufacturers:', err);
      }
    };

    fetchManufacturers();
  }, []);

  useEffect(() => {
    if (car) {
      setFormData(car);
    }
  }, [car]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (car) {
        await axios.put(`http://localhost:5004/vehicles/${car.id}`, formData);
      } else {
        await axios.post('http://localhost:5004/vehicles/', formData);
      }
      handleClose();
      refreshCars();
    } catch (err) {
      console.error('Failed to save car:', err);
    }
  };

  return (
    <Dialog open={open} onClose={handleClose}>
      <DialogTitle>{car ? 'Edit Car' : 'Add New Car'}</DialogTitle>
      <DialogContent>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Price"
            name="price"
            value={formData.price}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Years"
            name="years"
            value={formData.years}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="License Plate"
            name="license_plate"
            value={formData.license_plate}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Picture Url"
            name="picture_url"
            value={formData.picture_url}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            select
            label="Manufacturer"
            name="manufacturer_id"
            value={formData.manufacturer_id}
            onChange={handleChange}
            fullWidth
            margin="normal"
          >
            {manufacturers.map((manufacturer) => (
              <MenuItem key={manufacturer.id} value={manufacturer.id}>
                {manufacturer.name}
              </MenuItem>
            ))}
          </TextField>
          <DialogActions>
            <Button onClick={handleClose} color="secondary">
              Cancel
            </Button>
            <Button type="submit" variant="contained" color="primary">
              {car ? 'Save Changes' : 'Add Car'}
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default CarForm;
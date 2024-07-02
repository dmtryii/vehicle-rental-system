
from enum import Enum
from sqlalchemy_serializer import SerializerMixin

from app.extensions import db


class Status(Enum):
    AVAILABLE = 'AVAILABLE'
    RENTED_OUT = 'RENTED_OUT'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'

    def __str__(self):
        return self.value


class Manufacturer(db.Model, SerializerMixin):
    __tablename__ = 'manufacturers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String, nullable=False)
    cars = db.relationship('Vehicle', back_populates='manufacturer', cascade='all, delete-orphan')


class Vehicle(db.Model, SerializerMixin):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    years = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'), nullable=False)
    manufacturer = db.relationship('Manufacturer', back_populates='vehicles')
    
    rentals = db.relationship('Rental', back_populates='vehicle', cascade='all, delete-orphan')

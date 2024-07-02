
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

from app.extensions import db


class Rental(db.Model, SerializerMixin):
    __tablename__ = 'rentals'
        
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    vehicle = db.relationship('Vehicle', back_populates='rentals')
        
    user_id = db.Column(db.Integer, db.ForeignKey('base_users.id'), nullable=False)
    user = db.relationship('BaseUser', back_populates='rentals')

    additional_services = db.relationship('AdditionalService', secondary='rental_services', back_populates='rentals')


class AdditionalService(db.Model, SerializerMixin):
    __tablename__ = 'additional_services'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    rentals = db.relationship('Rental', secondary='rental_services', back_populates='additional_services')


rental_services = db.Table('rental_services',
    db.Column('rental_id', db.Integer, db.ForeignKey('rentals.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('additional_services.id'), primary_key=True)
)


class Discount(db.Model, SerializerMixin):
    __tablename__ = 'discounts'
        
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    
    users = db.relationship('BaseUser', secondary='user_discounts', back_populates='discounts')


user_discounts = db.Table('user_discounts',
    db.Column('user_id', db.Integer, db.ForeignKey('base_users.id'), primary_key=True),
    db.Column('discount_id', db.Integer, db.ForeignKey('discounts.id'), primary_key=True)
)


from typing import List, Optional
from app.exceptions.base_exception import EmptyFieldException, EntityAllreadyPresentException, EntityNotFoundException, ImpossibleFieldValueError
from app.helpers.enums import Status
from app.models.vehicles import Manufacturer, Vehicle
from app.extensions import db


def get_all_vehicle() -> List[Vehicle]:
    return Vehicle.query.all()


def get_all_manufacturers() -> List[Manufacturer]:
    return Manufacturer.query.all()


def create_manufacturer(name: str, country: str) -> Manufacturer:
    if not name:
        raise EmptyFieldException(message='Missing manufacturer name')
    
    if not country:
        raise EmptyFieldException(message='Missing manufacturer country')
    
    present_manufacturer = Manufacturer.query.filter_by(name=name).first()
    
    if present_manufacturer:
        raise EntityAllreadyPresentException(message='Manufacturer with that name is already present')       
    
    new_manufacturer = Manufacturer(
        name=name,
        country=country
    )

    db.session.add(new_manufacturer)
    db.session.commit()
    
    return new_manufacturer


def create_vehicle(name: str, price: float, years: int, 
                   license_plate: str, manufacturer_id: int,
                   picture_url: str = '',
                   description: str = '') -> Vehicle:
    if not name:
        raise EmptyFieldException(message='Missing vehicle name')
    
    if float(price) < 0:
        raise ImpossibleFieldValueError(message='The price cannot acquire a negative value')
    
    present_vehicle = Vehicle.query.filter_by(license_plate=license_plate).first()
    
    if present_vehicle:
        raise EntityAllreadyPresentException(message='Vehicle with such license plate is already present')  
    
    manufacturer = Manufacturer.query.filter_by(id=manufacturer_id).first()
    
    if not manufacturer:
        raise EntityNotFoundException(message=f'Manufacturer not found by id - {manufacturer_id}')
        
    new_vehicle = Vehicle(
        name=name,
        price=price,
        status=Status.AVAILABLE,
        years=years,
        license_plate=license_plate,
        manufacturer=manufacturer,
        picture_url=picture_url,
        description=description
    )
    
    db.session.add(new_vehicle)
    db.session.commit()
    
    return new_vehicle


def update_vehicle(id: int, name: Optional[str] = None, price: Optional[float] = None, 
                   status: Optional[Status] = None, years: Optional[int] = None, 
                   license_plate: Optional[str] = None, manufacturer_id: Optional[int] = None,
                   picture_url: Optional[str] = None, description: Optional[str] = None) -> Vehicle:

    current_vehicle = Vehicle.query.filter_by(id=id).first()

    if not current_vehicle:
        raise EntityNotFoundException(message=f'Vehicle not found by id - {id}')

    if name is not None:
        current_vehicle.name = name

    if price is not None:
        if float(price) < 0:
            raise ImpossibleFieldValueError(message='The price cannot acquire a negative value')
        current_vehicle.price = price
        
    if status is not None:
        current_vehicle.status = status
    
    if years is not None:
        current_vehicle.years = years

    if license_plate is not None:
        present_vehicle = Vehicle.query.filter_by(license_plate=license_plate).first()
        if present_vehicle and present_vehicle.id != id:
            raise EntityAllreadyPresentException(message='Vehicle with such license plate is already present') 
        current_vehicle.license_plate = license_plate

    if manufacturer_id is not None:
        manufacturer = Manufacturer.query.filter_by(id=manufacturer_id).first()
        if not manufacturer:
            raise EntityNotFoundException(message=f'Manufacturer not found by id - {manufacturer_id}')
        current_vehicle.manufacturer = manufacturer

    if picture_url is not None:
        current_vehicle.picture_url = picture_url
    
    if description is not None:
        current_vehicle.description = description
    
    db.session.commit()
    
    return current_vehicle


def delete_vehicle(id: int) -> None:
    current_vehicle = Vehicle.query.filter_by(id=id).first()
    db.session.delete(current_vehicle)
    db.session.commit()
    
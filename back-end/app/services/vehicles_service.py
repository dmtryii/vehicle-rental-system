
from app.exceptions.base_exception import EmptyFieldException, EntityAllreadyPresentException, EntityNotFoundException, ImpossibleFieldValueError
from app.helpers.enums import Status
from app.models.vehicles import Manufacturer, Vehicle
from app.extensions import db


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
        description=description
    )
    
    db.session.add(new_vehicle)
    db.session.commit()
    
    return new_vehicle

from flask import jsonify, request

from app.controllers.vehicles import bp
from app.services import vehicles_service


@bp.route('/')
def get_all_vehicles():
    vehicles = vehicles_service.get_all_vehicle()
    json_respone = [vehicle.to_dict() for vehicle in vehicles]
    return jsonify(json_respone), 200


@bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    vehicle = vehicles_service.create_vehicle(
        name=data.get('name'),
        price=data.get('price'),
        years=data.get('years'),
        license_plate=data.get('license_plate'),
        manufacturer_id=data.get('manufacturer_id'),
        description=data.get('description'),
    )
    return jsonify(vehicle.to_dict()), 201


@bp.route('/manufacturers', methods=['POST'])
def create_manufacturer():
    data = request.get_json()
    manufacturer = vehicles_service.create_manufacturer(
        name=data.get('name'),
        country=data.get('country')
    )
    return jsonify(manufacturer.to_dict()), 201

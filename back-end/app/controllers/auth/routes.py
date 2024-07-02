from flask import jsonify, request

from app.controllers.auth import bp
from app.services import auth_service

@bp.route('/singin', methods=['POST'])
def singin():
    data = request.get_json()    
    access_token = auth_service.singin(
        username=data.get('username'),
        password=data.get('password')
    )
    return jsonify(access_token=access_token), 200


@bp.route('/singup', methods=['POST'])
def singup():
    data = request.get_json()
    access_token = auth_service.singup(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        gender=data.get('gender'),
        birthday=data.get('birthday')
    )
    return jsonify(access_token=access_token), 201


from flask import jsonify
from flask_jwt_extended import jwt_required
from app.services import users_services
from app.controllers.users import bp


@bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = users_services.get_all()
    json_users= list(map(lambda x: x.to_dict(), users))
    return jsonify({'users': json_users}), 200

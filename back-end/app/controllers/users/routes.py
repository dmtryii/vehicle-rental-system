
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services import users_services
from app.controllers.users import bp


@bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = users_services.get_all()
    json_users= list(map(lambda x: x.to_dict(), users))
    return jsonify({'users': json_users}), 200


@bp.route("/identity", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    current_user = users_services.get_by_id(current_user_id)
    return jsonify(current_user=current_user.to_dict()), 200

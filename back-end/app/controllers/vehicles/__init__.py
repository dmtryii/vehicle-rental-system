from flask import Blueprint

bp = Blueprint('vehicles', __name__)

from app.controllers.vehicles import routes
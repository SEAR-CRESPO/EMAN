from flask import Blueprint
from controllers.ubicacionControllers import ubicacionControllers

ubicacion_bp = Blueprint("ubicacion",__name__)

@ubicacion_bp.route('/', methods= ["get"])
def home():
    data = ubicacionControllers.read()
    return data

@ubicacion_bp.route('/', methods= ["post"])
def add():
    data = ubicacionControllers.add()
    
    return data

@ubicacion_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = ubicacionControllers.delete(uuid)
    return data
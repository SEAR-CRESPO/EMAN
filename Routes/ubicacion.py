from flask import Blueprint
from controllers.ubicacionControllers import ubicacionController

ubicacion_bp = Blueprint("ubicacion",__name__)

@ubicacion_bp.route('/', methods= ["get"])
def home():
    data = ubicacionController.read()
    return data

@ubicacion_bp.route('/', methods= ["post"])
def add():
    
    return 
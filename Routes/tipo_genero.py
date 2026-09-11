from flask import Blueprint
from controllers.tipo_generoControllers import tipo_generoControllers

tipo_genero_bp = Blueprint("tipo_genero",__name__)

@tipo_genero_bp.route('/', methods= ["get"])
def home():
    data = tipo_generoControllers.read()
    return data

@tipo_genero_bp.route('/', methods= ["post"])
def add():
    data = tipo_generoControllers.add()
    
    return data


@tipo_genero_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = tipo_generoControllers.delete(uuid)
    return data
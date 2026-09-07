from flask import Blueprint
from controllers.tipo_generoControllers import tipo_generoController

tipo_genero_bp = Blueprint("tipo_genero",__name__)

@tipo_genero_bp.route('/', methods= ["get"])
def home():
    data = tipo_generoController.read()
    return data

@tipo_genero_bp.route('/', methods= ["post"])
def add():
    
    return 
from flask import Blueprint
from Controllers.tipo_generoController import tipo_generoController

tipo_genero_bp = Blueprint("tipo_genero",__name__)

@tipo_genero_bp.route('/', methods= ["get"])
def home():
    data = tipo_generoController.read()
    return data

@tipo_genero_bp.route('/', methods= ["post"])
def add():
    
    return 
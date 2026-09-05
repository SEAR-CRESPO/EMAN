from flask import Blueprint
from Controllers.administradorController import administradorController

administrador_bp = Blueprint("administrador",__name__)

@administrador_bp.route('/', methods= ["get"])
def home():
    data = administradorController.read()
    return data

@administrador_bp.route('/', methods= ["post"])
def add():

    return 
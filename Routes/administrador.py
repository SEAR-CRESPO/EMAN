from flask import Blueprint
from controllers.administradorControllers import administradorControllers

administrador_bp = Blueprint("administrador",__name__)

@administrador_bp.route('/', methods= ["get"])
def home():
    data = administradorControllers.read()
    return data

@administrador_bp.route('/', methods= ["post"])
def add():
    data = administradorControllers.add()
    return data

@administrador_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = administradorControllers.delete(uuid)
    return data
from flask import Blueprint
from controllers.clienteControllers import clienteControllers

cliente_bp = Blueprint("cliente",__name__)

@cliente_bp.route('/', methods= ["get"])
def home():
    data = clienteControllers.read()
    return data

@cliente_bp.route('/', methods= ["post"])
def add():
    data = clienteControllers.add()
    
    return data

@cliente_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = clienteControllers.delete(uuid)
    return data
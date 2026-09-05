from flask import Blueprint
from controllers.clienteController import clienteController

cliente_bp = Blueprint("cliente",__name__)

@cliente_bp.route('/', methods= ["get"])
def home():
    data = clienteController.read()
    return data

@cliente_bp.route('/', methods= ["post"])
def add():
    
    return 
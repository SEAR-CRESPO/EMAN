from flask import Blueprint
from controllers.compraControllers import compraControllers

compra_bp = Blueprint("compra",__name__)

@compra_bp.route('/', methods= ["get"])
def home():
    data = compraControllers.read()
    return data

@compra_bp.route('/', methods= ["post"])
def add():
    data = compraControllers.add()
    
    return data

@compra_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = compraControllers.delete(uuid)
    return data
from flask import Blueprint
from controllers.carrito_compraControllers import carrito_compraControllers

carrito_compra_bp = Blueprint("carrito_compra",__name__)

@carrito_compra_bp.route('/', methods= ["get"])
def home():
    data = carrito_compraControllers.read()
    return data

@carrito_compra_bp.route('/', methods= ["post"])
def add():
    data = carrito_compraControllers.add()
    
    return data

@carrito_compra_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = carrito_compraControllers.delete(uuid)
    return data
from flask import Blueprint
from controllers.pagoControllers import pagoControllers

pago_bp = Blueprint("pago",__name__)

@pago_bp.route('/', methods= ["get"])
def home():
    data = pagoControllers.read()
    return data

@pago_bp.route('/', methods= ["post"])
def add():
    data = pagoControllers.add()
    
    return data

@pago_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = pagoControllers.delete(uuid)
    return data
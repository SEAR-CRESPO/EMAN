from flask import Blueprint
from controllers.pagoControllers import pagoController

pago_bp = Blueprint("pago",__name__)

@pago_bp.route('/', methods= ["get"])
def home():
    data = pagoController.read()
    return data

@pago_bp.route('/', methods= ["post"])
def add():
    
    return 
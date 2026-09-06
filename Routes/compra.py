from flask import Blueprint
from controllers.compraControllers import compraController

compra_bp = Blueprint("compra",__name__)

@compra_bp.route('/', methods= ["get"])
def home():
    data = compraController.read()
    return data

@compra_bp.route('/', methods= ["post"])
def add():
    
    return 
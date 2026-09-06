from flask import Blueprint
from controllers.productoControllers import productoControllers

producto_bp = Blueprint("producto",__name__)

@producto_bp.route('/', methods= ["get"])
def home():
    data = productoControllers.read()
    return data

@producto_bp.route('/', methods= ["post"])
def add():
    
    return 
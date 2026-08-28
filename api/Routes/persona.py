from flask import Blueprint
from controllers.persona import persona

producto_bp = Blueprint("persona",__name__)

@producto_bd.route('/' methods= ["get"])
def home():
    data  = productoControllers.read()
    return data

@producto_bd.route('/' methods= ["post"])
def add():
    
    return 
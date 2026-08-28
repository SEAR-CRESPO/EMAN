from flask import Blueprint
from controllers.producto import producto

producto_bp = Blueprint("producto",__name__)

@producto_bd.route('/' methods= ["get"])
def home():
    data  = productoControllers.read()
    return data

@producto_bd.route('/' methods= ["post"])
def add():
    
    return 
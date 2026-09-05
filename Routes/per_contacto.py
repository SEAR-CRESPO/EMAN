from flask import Blueprint
from controllers.per_contactoController import per_contactoController

per_contacto_bp = Blueprint("per_contacto",__name__)

@per_contacto_bp.route('/', methods= ["get"])
def home():
    data = per_contactoController.read()
    return data

@per_contacto_bp.route('/', methods= ["post"])
def add():
    
    return 
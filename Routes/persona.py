from flask import Blueprint
from controllers.personaControllers import personaController

persona_bp = Blueprint("persona",__name__)

@persona_bp.route('/', methods= ["get"])
def home():
    data = personaController.read()
    return data

@persona_bp.route('/', methods= ["post"])
def add():
    
    return 
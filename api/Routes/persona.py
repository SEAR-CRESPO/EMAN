from flask import Blueprint
from Controllers.personaController import personaController

persona_bp = Blueprint("persona",__name__)

@persona_bp.route('/', methods= ["get"])
def home():
    data = personaController.read()
    return data

@persona_bp.route('/', methods= ["post"])
def add():
    
    return 
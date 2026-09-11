from flask import Blueprint
from controllers.personaControllers import personaControllers

persona_bp = Blueprint("persona",__name__)

@persona_bp.route('/', methods= ["get"])
def home():
    data = personaControllers.read()
    return data

@persona_bp.route('/', methods= ["post"])
def add():
    data = personaControllers.add()
    
    return data

@persona_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = personaControllers.delete(uuid)
    return data
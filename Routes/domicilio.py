from flask import Blueprint
from controllers.domicilioControllers import domicilioControllers

domicilio_bp = Blueprint("domicilio",__name__)

@domicilio_bp.route('/', methods= ["get"])
def home():
    data = domicilioControllers.read()
    return data

@domicilio_bp.route('/', methods= ["post"])
def add():
    data = domicilioControllers.add()
    
    return data

@domicilio_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = domicilioControllers.delete(uuid)
    return data
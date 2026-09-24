from flask import Blueprint
from controllers.dom_contactoControllers import dom_contactoControllers

dom_contacto_bp = Blueprint("dom_contacto",__name__)

@dom_contacto_bp.route('/', methods= ["get"])
def home():
    data = dom_contactoControllers.read()
    return data

@dom_contacto_bp.route('/', methods= ["post"])
def add():
    data = dom_contactoControllers.add()
    
    return data

@dom_contacto_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = dom_contactoControllers.delete(uuid)
    return data
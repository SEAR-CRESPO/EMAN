from flask import Blueprint
from controllers.per_contactoControllers import per_contactoControllers

per_contacto_bp = Blueprint("per_contacto",__name__)

@per_contacto_bp.route('/', methods= ["get"])
def home():
    data = per_contactoControllers.read()
    return data

@per_contacto_bp.route('/', methods= ["post"])
def add():
    data = per_contactoControllers.add()
    
    return data

@per_contacto_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = per_contactoControllers.delete(uuid)
    return data
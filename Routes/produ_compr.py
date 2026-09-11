from flask import Blueprint
from controllers.produ_comprControllers import produ_comprControllers

produ_compr_bp = Blueprint("produ_compr",__name__)

@produ_compr_bp.route('/', methods= ["get"])
def home():
    data = produ_comprControllers.read()
    return data

@produ_compr_bp.route('/', methods= ["post"])
def add():
    data = produ_comprControllers.add()
    
    return data

@produ_compr_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = produ_comprControllers.delete(uuid)
    return data
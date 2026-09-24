from flask import Blueprint
from controllers.produc_carriControllers import produc_carriControllers

produc_carri_bp = Blueprint("produc_carri",__name__)

@produc_carri_bp.route('/', methods= ["get"])
def home():
    data = produc_carriControllers.read()
    return data

@produc_carri_bp.route('/', methods= ["post"])
def add():
    data = produc_carriControllers.add()
    
    return data


@produc_carri_bp.route('/<uuid>', methods= ["delete"])
def delete(uuid):
    data = produc_carriControllers.delete(uuid)
    return data
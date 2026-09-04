from flask import Blueprint
from Controllers.domicilioController import domicilioController

domicilio_bp = Blueprint("domicilio",__name__)

@domicilio_bp.route('/', methods= ["get"])
def home():
    data = domicilioController.read()
    return data

@domicilio_bp.route('/', methods= ["post"])
def add():
    
    return 
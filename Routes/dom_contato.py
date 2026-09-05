from flask import Blueprint
from controllers.dom_contatoController import dom_contaroController

dom_contato_bp = Blueprint("dom_contato",__name__)

@dom_contato_bp.route('/', methods= ["get"])
def home():
    data = dom_contatoController.read()
    return data

@dom_contato_bp.route('/', methods= ["post"])
def add():
    
    return 
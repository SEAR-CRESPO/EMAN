from flask import Blueprint
from controllers.proct_compreController import proct_compreController

proct_compre_bp = Blueprint("proct_compre",__name__)

@proct_compre_bp.route('/', methods= ["get"])
def home():
    data = proct_compreController.read()
    return data

@proct_compre_bp.route('/', methods= ["post"])
def add():
    
    return 
from flask import jsonify, request 
from models.dom_contato import dom_contacto

class dom_contatoControllers:
    data = dom_contacto.read()
    return jsonify({"mensaje":data}), 200
from flask import jsonify, request 
from models.dom_contato import dom_contacto

class dom_contatoControllers:
    data = dom_contacto.read()
    return jsonify({"mensaje":data}), 200

 def add():
     
    data = request.get_jsonify(Silent=True)
    
    
if not data:
    return jsonify({"error": "No se proporcionaron datos"}), 400


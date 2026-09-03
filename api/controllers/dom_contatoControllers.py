from flask import jsonify, request 
from models.dom_contato import dom_contacto

class dom_contatoControllers:
    def read():
        data = dom_contacto.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CON_ID", "CON_UUID", "CON_TIPO_CONTACTO", "CON_VALOR", "CON_DOM_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = dom_contacto.add(data)
        return x

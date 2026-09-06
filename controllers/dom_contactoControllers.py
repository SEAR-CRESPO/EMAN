from flask import jsonify, request
from services.dom_contactoService import dom_contatoService

class dom_contactoControllers:
    @staticmethod
    def read():
        data = dom_contatoService.read()
        return jsonify({"mensaje": data}), 200

    @staticmethod
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CON_ID", "CON_UUID", "CON_TIPO_CONTACTO", "CON_VALOR", "CON_DOM_ID"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = dom_contatoService.add(data)
        return x
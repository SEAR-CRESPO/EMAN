from flask import jsonify, request
from services.administradorService import administradorService

class administradorController:
    def read():
        data = administradorService.read()
        return jsonify({"mensaje": data}), 200

    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["ADM_ID", "ADM_UUID", "ADM_PER_ID"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = administradorService.add(data)
        return x
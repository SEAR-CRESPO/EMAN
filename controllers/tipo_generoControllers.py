from flask import jsonify, request 
from services.tipo_generoService import tipo_generoService

class tipo_generoControllers:
    def read():
        data = tipo_generoService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["GEN_ID", "GEN_UUID", "GEN_GENERO", "GEN_PRO_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = tipo_generoService.add(data)
        return x

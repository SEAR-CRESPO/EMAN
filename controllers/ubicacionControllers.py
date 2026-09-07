from flask import jsonify, request 
from services.ubicacionService import ubicacionService

class ubicacionControllers:
    def read():
        data = ubicacionService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["UBI_ID", "UBI_UUID", "UBI_CIUDAD", "UBI_BARRIO", "UBI_DIRECCION", "UBI_DOM_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = ubicacionService.add(data)
        return x

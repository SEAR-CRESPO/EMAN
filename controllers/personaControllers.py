from flask import jsonify, request
from services.personaService import personaService 

class personaControllers:
    def read():
        data = personaService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PER_ID", "PER_UUID", "PER_CONTRASENA", "PER_NUMERO_DOCUMENTO", "PER_PRIMER_NOMBRE", "PER_SEGUNDO_NOMBRE", "PER_PRIMER_APELLIDO", "PER_SEGUNDO_APELLIDO"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = personaService.add(data)
        return x

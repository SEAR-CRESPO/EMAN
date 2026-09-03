from flask import jsonify, request 
from models.domicilio import domicilio

class domiciolioControllers:
    def read():
        data = domicilio.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["DOM_ID", "DOM_UUID", "DOM_CODIGO", "DOM_COM_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = domicilio.add(data)
        return x

from flask import jsonify, request 
from models.produc_carri import produc_carri

class produc_carriControllers:
    def read():
        data = produc_carri.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PROC_ID", "PROC_UUID", "PROC_CANTIDAD", "PROC_PRO_ID", "PROC_COMC_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = produc_carri.add(data)
        return x

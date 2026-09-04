from flask import jsonify, request 
from models.proct_compr import proct_compr

class proct_comprControllers:
    def read():
        data = proct_compr.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PRCO_ID", "PRCO_UUID", "PRCO_CANTIDAD", "PRCO_COM_ID", "PRCO_PRO_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = proct_compr.add(data)
        return x

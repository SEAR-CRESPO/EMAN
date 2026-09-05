from flask import jsonify, request
from models.producto import producto

class productoControllers:
    def read():
        data = producto.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CODIGO", "NOMBRE", "TALLA", "MARCA", "DESCRIPCION", "COLOR"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = producto.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 200

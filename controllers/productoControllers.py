from flask import jsonify, request
from services.productoService import productoService

class productoControllers:
    def read():
        data = productoService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CODIGO", "NOMBRE", "TALLA", "MARCA", "DESCRIPCION", "COLOR", "PRECIO"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = productoService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201

    def delete(uuid):
        x = productoService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x

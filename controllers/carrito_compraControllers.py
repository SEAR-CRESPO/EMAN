from flask import jsonify, request
from services.carrito_compraService import carrito_compraService

class carrito_compraControllers:
    def read():
        data = carrito_compraService.read()
        return jsonify({"mensaje": data}), 200

    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["COMC_ID", "COMC_UUID", "COMC_CODIGO", "COMC_CODIGO", "COMC_TOTAL_COMPRA", "COMC_FECHA"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = carrito_compraService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = carrito_compraService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
             return jsonify({"mensaje": "El cuerpo esta vacio o es invalido"}), 400
    
        required = ["COMC_UUID", "COMC_CODIGO", "COMC_TOTAL_COMPRA", "COMC_FECHA"]
    
        missed = [x for x in required if x not in data]
    
        if len(missed) > 0:
            return jsonify({"mensaje": f"Faltan datos parametros: {missed}"}), 400
    
        data["uuid"] = uuid
        print(data)
        x = carrito_compraService.update(data)
        if x["codigo_respuesta"] == 1:
             return jsonify({"mensaje": "recurso no encontrado"}), 400
        else:
             return jsonify(x), 200
            
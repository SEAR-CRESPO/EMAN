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
        return x
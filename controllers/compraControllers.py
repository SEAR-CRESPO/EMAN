from flask import jsonify, request
from services.compraService import compraService

class compraControllers:
    def read():
        data = compraService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["COM_ID", "COM_UUID", "COM_NUMERO_COMPRA", "COM_METODO_ENTREGA", "COM_FECHA_COMPRA", "COM_ADM_ID", "COM_CLI_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = compraService.add(data)
        return x

from flask import jsonify, request
from services.pagoService import pagoService

class pagoControllers:
    def read():
        data = pagoService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PAG_ID", "PAG_UUID", "PAG_NUMERO_PAGO", "PAG_VALOR", "PAG_METODO", "PAG_ESTADO", "PAG_FECHA", "PAG_COM_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = pagoService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = pagoService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x

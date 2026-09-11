from flask import jsonify, request
from services.clienteService import clienteService

class clienteControllers:
    def read():
        data = clienteService.read()
        return jsonify({"mensaje": data}), 200

    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CLI_ID", "CLI_UUID", "CLI_CODIGO", "CLI_NOMBRE", "CLI_APELLIDO", "CLI_EMAIL", "CLI_TELEFONO"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = clienteService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = clienteService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x
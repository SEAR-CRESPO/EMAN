from flask import jsonify, request
from services.administradorService import administradorService

class administradorControllers:
    def read():
        data = administradorService.read()
        return jsonify({"mensaje": data}), 200

    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["ADM_ID", "ADM_UUID", "ADM_PER_ID"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = administradorService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    
    def delete(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o es invalido"}), 400

        required = ["ADM_UUID"]

        missed = [x for x in required if x not in data]

        if len(missed) > 0:
            return jsonify({"mensaje": f"Faltan datos parametros: {missed}"}), 400

        data["uuid"] = uuid
        print(data)
        x = administradorService.update(data)
        if x["codigo_respuesta"] == 1:
            return jsonify({"mensaje": "recurso no encontrado"}), 400
        else:
            return jsonify(x), 200
        
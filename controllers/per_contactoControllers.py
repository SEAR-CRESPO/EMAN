from flask import jsonify, request
from services.per_contactoService import per_contactoService

class per_contactoControllers:
    def read():
        data = per_contactoService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CON_ID", "CON_UUID", "CON_TIPO_CONTACTO", "CON_VALOR", "CON_PER_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = per_contactoService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = per_contactoService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x

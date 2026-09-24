from flask import jsonify, request
from services.dom_contactoService import dom_contatoService

class dom_contactoControllers:
    @staticmethod
    def read():
        data = dom_contatoService.read()
        return jsonify({"mensaje": data}), 200

    @staticmethod
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["CON_ID", "CON_UUID", "CON_TIPO_CONTACTO", "CON_VALOR", "CON_DOM_ID"]
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = dom_contatoService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = dom_contatoService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x
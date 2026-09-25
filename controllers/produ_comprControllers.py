from flask import jsonify, request 
from services import carrito_compraService
from services.produ_comprService import produ_comprService

class produ_comprControllers:
    def read():
        data = produ_comprService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PRCO_ID", "PRCO_UUID", "PRCO_CANTIDAD", "PRCO_COM_ID", "PRCO_PRO_ID"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = produ_comprService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = produ_comprService.delate(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x


    
    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
             return jsonify({"mensaje": "El cuerpo esta vacio o es invalido"}), 400
    
        required = ["PRCO_ID", "PRCO_UUID", "PRCO_CANTIDAD", "PRCO_COM_ID", "PRCO_PRO_ID"]
    
        missed = [x for x in required if x not in data]
    
        if len(missed) > 0:
            return jsonify({"mensaje": f"Faltan datos parametros: {missed}"}), 400
    
        data["uuid"] = uuid
        print(data)
        x = produ_comprService.update(data)
        if x["codigo_respuesta"] == 1:
             return jsonify({"mensaje": "recurso no encontrado"}), 400
        else:
             return jsonify(x), 200

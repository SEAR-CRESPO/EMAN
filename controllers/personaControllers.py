from flask import jsonify, request
from services.carrito_compraService import carrito_compraService
from services.personaService import personaService 

class personaControllers:
    def read():
        data = personaService.read()
        return jsonify({"mensaje": data}), 200
    
    def add():
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        required = ["PER_CONTRASENA", "PER_NUMERO_DOCUMENTO", "PER_PRIMER_NOMBRE", "PER_SEGUNDO_NOMBRE", "PER_PRIMER_APELLIDO", "PER_SEGUNDO_APELLIDO"]
        
        falt = [x for x in required if x not in data]
        
        if len(falt) > 0:
            return jsonify({"error": "Faltan datos", "faltantes": falt}), 400
        
        x = personaService.add(data)
        return jsonify({"mensaje": "se registro", "data": x}), 201


    def delete(uuid):
        x = personaService.delete(uuid)
        if x == 404:
            return jsonify({"Mensaje":"No se encontro el registro"}), x
        else:
            return jsonify({"Mensaje":"Se elimino correctamente"}), x


    
    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
             return jsonify({"mensaje": "El cuerpo esta vacio o es invalido"}), 400
    
        required = ["PER_CONTRASENA", "PER_NUMERO_DOCUMENTO", "PER_PRIMER_NOMBRE", "PER_SEGUNDO_NOMBRE", "PER_PRIMER_APELLIDO", "PER_SEGUNDO_APELLIDO"]
    
        missed = [x for x in required if x not in data]
    
        if len(missed) > 0:
            return jsonify({"mensaje": f"Faltan datos parametros: {missed}"}), 400
    
        data["uuid"] = uuid
        print(data)
        x = personaService.update(data)
        if x["codigo_respuesta"] == 1:
             return jsonify({"mensaje": "recurso no encontrado"}), 400
        else:
             return jsonify(x), 200

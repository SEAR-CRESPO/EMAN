from flask import jsonify, request 
from models.ubicacion import ubicacion 

class ubicacionControllers:
    data = ubicacion.read()
    return jsonify({"mensaje":data}), 200
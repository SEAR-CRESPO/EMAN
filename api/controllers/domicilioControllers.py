from flask import jsonify, request 
from models.domicilio import domicilio

class domiciolioControllers:
    data = domicilio.read()
    return jsonify({"mensaje":data}), 200
from flask import jsonify, request 
from models.produc_carri import produc_carri

class produc_carriControllers:
    data = produc_carri.read()
    return jsonify({"mensaje":data}), 200
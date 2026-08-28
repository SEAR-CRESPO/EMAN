from flask import jsonify, request
from models.producto import producto

class productoControllers:

    def read():
        data = producto.read()
        return jsonify({"mensaje":data}), 200
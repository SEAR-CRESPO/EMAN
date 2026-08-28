from flask import jsonify, request
from models.pago import pago

class pagoControllers:
    data = pago.read()
    return jsonify({"mensaje":data}), 200
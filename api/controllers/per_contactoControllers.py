from flask import jsonify, request
from models.per_contacto import per_contacto

class per_contactoControllers:
    data = per_contacto.read()
    return jsonify({"mesaje":data}), 200
from flask import jsonify, request 
from models.tipo_genero import tipo_genero


class tipo_generoControllers:
    data = tipo_genero.read()
    return jsonify({"mensaje"}), 200
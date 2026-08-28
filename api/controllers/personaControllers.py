from flask import jsonify, request
from models.persona import persona 


class personaControllers:
    data = persona.read()
    return jsonify({"mesanje":data}), 200
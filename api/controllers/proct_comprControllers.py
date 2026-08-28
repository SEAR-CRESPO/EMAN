from flask import jsonify, request 
from models.proct_compr import proct_compr

class proct_comprtControllers:

    def read():
        data = proct_compr.read()
        return jsonify({"mensaje":data}), 200
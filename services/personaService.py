import uuid
from flask import current_app
from models.persona import persona

class personaService:
    def add(data):
        uuid_per = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_persona

            (PER_UUID, PER_CONTRASENA, PER_NUMERO_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE, PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_per, data["CONTRASENA"], data["NUMERO_DOCUMENTO"], data["PRIMER_NOMBRE"], data["SEGUNDO_NOMBRE"], data["PRIMER_APELLIDO"], data["SEGUNDO_APELLIDO"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_per, "CONTRASENA": data["CONTRASENA"],
                "NUMERO_DOCUMENTO": data["NUMERO_DOCUMENTO"], "PRIMER_NOMBRE":data ["PRIMER_NOMBRE"],
                "SEGUNDO_NOMBRE": data["SEGUNDO_NOMBRE"], "PRIMER_APELLIDO": data["PRIMER_APELLIDO"],
                "SEGUNDO_APELLIDO": data["SEGUNDO_APELLIDO"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_persona"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [persona(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7]).to_dict() for w in data]

        return x
    
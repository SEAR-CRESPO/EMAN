import uuid
from flask import current_app
from models.tipo_genero import tipo_genero

class tipo_generoService:
    def add(data):
        uuid_gen = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_tipo_genero

            (GEN_UUID, GEN_GENERO, GEN_PRO_ID) VALUES
            (%s, %s, %s)"""
        c.execute(query, (uuid_gen, data["GENERO"], data["PRO_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_gen, "GENERO": data["GENERO"],
                "PRO_ID": data["PRO_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_tipo_genero"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [tipo_genero(w[0],w[1],w[2],w[3]).to_dict() for w in data]

        return x
    
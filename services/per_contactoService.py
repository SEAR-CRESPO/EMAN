import uuid
from flask import current_app
from models.per_contacto import per_contacto

class per_contactoService:
    def add(data):
        uuid_con = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_per_contacto

            (CON_UUID, CON_TIPO_CONTACTO, CON_VALOR, CON_PER_ID) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_con, data["TIPO_CONTACTO"], data["VALOR"], data["PER_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_con, "TIPO_CONTACTO": data["TIPO_CONTACTO"],
                "VALOR": data["VALOR"], "PER_ID":data ["PER_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_per_contacto"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [per_contacto(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
    
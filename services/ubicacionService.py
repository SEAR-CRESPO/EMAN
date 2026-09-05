import uuid
from flask import current_app
from models.ubicacion import ubicacion

class ubicacionService:
    def add(data):
        uuid_ubi = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_ubicacion

            (UBI_UUID, UBI_CIUDAD, UBI_BARRIO, UBI_DIRECCION, UBI_DOM_ID) VALUES
            (%s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_ubi, data["CIUDAD"], data["BARRIO"], data["DIRECCION"], data["DOM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_ubi,
                "CIUDAD": data["CIUDAD"],
                "BARRIO": data["BARRIO"], "DIRECCION":data ["DIRECCION"],
                "DOM_ID": data["DOM_ID"] }
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_ubicacion"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [ubicacion(w[0],w[1],w[2],w[3],w[4],w[5]).to_dict() for w in data]

        return x
    
import uuid
from flask import current_app
from models.domicilio import domicilio

class domicilioService:
    def add(data):
        uuid_dom = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_domicilio

            (DOM_UUID, DOM_CODIGO, DOM_COM_ID,) VALUES
            (%s, %s, %s)"""
        c.execute(query, (uuid_dom, data["CODIGO"], data["COM_ID"] ))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_dom, "CODIGO": data["CODIGO"],
                "COM_ID": data["COM_ID"]}
        return data

     # marca la posicion %s
    def update(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_domicilio WHERE DOM_UUID = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_domicilio"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [domicilio(w[0],w[1],w[2],w[3]).to_dict() for w in data]

        return x
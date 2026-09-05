import uuid
from flask import current_app
from models.compra import compra

class compraService:
    def add(data):
        uuid_com = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_compra

            (COM_UUID,COM_NUMERO_COMPRA,COM_METODO_ENTREGA,COM_FECHA_COMPRA,COM_ADM_ID,COM_CLI_ID) VALUES
            (%s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_com, data["NUMERO_COMPRA"], data["METODO_ENTREGA"], data["FECHA_COMPRA"], data["ADM_ID"], data["CLI_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_com,
                "NUMERO_COMPRA": data["NUMERO_COMPRA"],
                "METODO_ENTREGA": data["METODO_ENTREGA"], "FECHA_COMPRA":data ["FECHA_COMPRA"],
                "ADM_ID": data["ADM_ID"], "CLI_ID": data["CLI_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_compra"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [compra(w[0],w[1],w[2],w[3],w[4],w[5],w[6]).to_dict() for w in data]

        return x
    
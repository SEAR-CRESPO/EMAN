import uuid
from flask import current_app
from models.pago import pago

class productoService:
    def add(data):
        uuid_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_pago

            (PAG_UUID, PAG_NUMERO_PAGO, PAG_VALOR, PAG_METODO, PAG_ESTADO, PAG_FECHA, PAG_COM_ID) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_pag, data["NUMERO_PAGO"], data["VALOR"], data["METODO"], data["ESTADO"], data["FECHA"], data["COM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_pag, "NUMERO_PAGO": data["NUMERO_PAGO"],
                "VALOR": data["VALOR"], "METODO":data ["METODO"],
                "ESTADO": data["ESTADO"], "FECHA": data["FECHA"],
                "COM_ID": data["COM_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_pago"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [pago(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7]).to_dict() for w in data]

        return x
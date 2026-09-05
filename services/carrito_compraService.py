import uuid
from flask import current_app
from models.carrito_compra import carrito_compra

class carrito_compraService:
    def add(data):
        uuid_comc = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_carrito_compra

            (COMC_UUID,COMC_CODIGO,COMC_TOTAL_COMPRA,COMC_FECHA) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_comc, data["CODIGO"], data["TOTAL_COMPRA"], data["FECHA"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_comc, "CODIGO": data["CODIGO"],
                "TOTAL_COMPRA": data["TOTAL_COMPRA"], "FECHA":data ["FECHA"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_carrito_compra"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [carrito_compra(w[0],w[1],w[2],w[3],w[4],).to_dict() for w in data]

        return x
import uuid
from flask import current_app
from models.carrito_compra import carrito_compra

class carrito_compraService:
    def add(data):
        uuid_comc = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_carrito_compra

            (comc_uuid,comc_codigo,comc_total_compra,comc_fecha) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_comc, data["COMC_CODIGO"], data["COMC_TOTAL_COMPRA"], data["COMC_FECHA"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_comc, "CODIGO": data["COMC_CODIGO"],
                "TOTAL_COMPRA": data["COMC_TOTAL_COMPRA"], "FECHA":data ["COMC_FECHA"]}
        return data

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_carrito_compra WHERE comc_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
        

    def update():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_carrito_compra"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [carrito_compra(w[0],w[1],w[2],w[3],w[4],).to_dict() for w in data]

        return x
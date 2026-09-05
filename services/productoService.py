import uuid
from flask import current_app
from models.producto import producto

class productoService:
    def add(data):
        uuid_pro = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_producto

            (PRO_UUID, PRO_CODIGO, PRO_NOMBRE, PRO_TALLA, PRO_MARCA, PRO_DESCRIPCION, PRO_COLOR) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_pro, data["CODIGO"], data["NOMBRE"], data["TALLA"], data["MARCA"], data["DESCRIPCION"], data["COLOR"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_pro, "CODIGO": data["CODIGO"],
                "NOMBRE": data["NOMBRE"], "TALLA":data ["TALLA"],
                "MARCA": data["MARCA"], "DESCRIPCION": data["DESCRIPCION"],
                "COLOR": data["COLOR"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_producto"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [producto(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7]).to_dict() for w in data]

        return x
    
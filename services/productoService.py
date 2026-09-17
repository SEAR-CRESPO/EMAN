import uuid
from flask import current_app
from models.producto import producto

class productoService:
    def add(data):
        uuid_pro = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_producto

            (pro_uuid, pro_codigo, pro_nombre, pro_talla, pro_marca, pro_descripcion, pro_color, pro_precio) VALUES
            (%s, %s, %s, %s, %s, %s, %s,%s)"""
        c.execute(query, (uuid_pro, data["PRO_CODIGO"], data["PRO_NOMBRE"], data["PRO_TALLA"], data["PRO_MARCA"], data["PRO_DESCRIPCION"], data["PRO_COLOR"], data["PRO_PRECIO"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_pro, "CODIGO": data["PRO_CODIGO"],
                "NOMBRE": data["PRO_NOMBRE"], "TALLA":data ["PRO_TALLA"],
                "MARCA": data["PRO_MARCA"], "DESCRIPCION": data["PRO_DESCRIPCION"],
                "COLOR": data["PRO_COLOR"],"PRECIO": data["PRO_PRECIO"]}
        return data

    def update():
        pass

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_producto WHERE pro_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM  t_producto"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [ producto(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7], w[8]).to_dict() for w in data]

        return x
    
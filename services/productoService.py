import uuid
from flask import current_app
from models.producto import producto

class productoService:
    def add(self, CODIGO, NOMBRE, TALLA, MARCA, DESCRIPCION, COLOR):
        uuid_pro = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO PRODUCTO
            (PRO_UUID, PRO_CODIGO, PRO_NOMBRE, PRO_TALLA, PRO_MARCA, PRO_DESCRIPCION, PRO_COLOR) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_pro, CODIGO, NOMBRE, TALLA, MARCA, DESCRIPCION, COLOR))
        current_app.mysql.connection.commit()
        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_pro, "CODIGO": CODIGO,
                "NOMBRE": NOMBRE, "TALLA": TALLA,
                "MARCA": MARCA, "DESCRIPCION": DESCRIPCION,
                "COLOR": COLOR}
        return data
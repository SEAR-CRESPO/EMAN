import uuid
from flask import current_app
from models.dom_contacto import dom_contacto

class dom_contatoService:
    def add(data):
        uuid_con = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_dom_contato

            (CON_UUID, CON_TIPO_CONTACTO, CON_VALOR, CON_DOM_ID) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_con, data["CON_TIPO_CONTACTO"], data["CON_VALOR"], data["CON_DOM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_con, "CON_TIPO_CONTACTO": data["CON_TIPO_CONTACTO"],
                "CON_VALOR": data["CON_VALOR"], "CON_DOM_ID":data ["CON_DOM_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_dom_contato"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [dom_contacto(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
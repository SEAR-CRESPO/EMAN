import uuid
from flask import current_app
from models.dom_contacto import dom_contacto

class dom_contatoService:
    def add(data):
        uuid_con = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_dom_contacto

            (con_uuid, con_tipo_contacto, con_valor, con_dom_id) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_con, data["CON_TIPO_CONTACTO"], data["CON_VALOR"], data["CON_DOM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_con, "TIPO_CONTACTO": data["CON_TIPO_CONTACTO"],
                "VALOR": data["CON_VALOR"], "DOM_ID":data ["CON_DOM_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_dom_contacto
            SET con_uuid = %s, con_tipo_contacto = %s, con_valor = %s
            WHERE con_uuid = %s"""
            c.execute(query, (Info["CON_UUID"], Info["CON_TIPO_CONTACTO"], Info["CON_VALOR"], Info["CON_UUID"]))
    
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["CON_UUID"], "TIPO_CONTACTO": Info["CON_TIPO_CONTACTO"], "VALOR": Info["CON_VALOR"]}
            print(data)
            return data 

     # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_dom_contacto WHERE con_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
    

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_dom_contacto"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [dom_contacto(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
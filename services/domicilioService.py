import uuid
from flask import current_app
from models.domicilio import domicilio

class domicilioService:
    def add(data):
        uuid_dom = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_domicilio

            (dom_uuid, dom_codigo, dom_con_id,) VALUES
            (%s, %s, %s)"""
        c.execute(query, (uuid_dom, data["DOM_CODIGO"], data["DOM_COM_ID"] ))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_dom, "CODIGO": data["DOM_CODIGO"],
                "COM_ID": data["DOM_COM_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_domicilio
            SET dom_uuid = %s, dom_codigo = %s, dom_con_id = %s
            WHERE dom_uuid = %s"""
            c.execute(query, (Info["DOM_UUID"], Info["DOM_CODIGO"], Info["DOM_COM_ID"], Info["DOM_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["DOM_UUID"], "CODIGO": Info["DOM_CODIGO"], "COM_ID": Info["DOM_COM_ID"]}
            print(data)
            return data 

     # marca la posicion %s
    def delete(uuid):
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
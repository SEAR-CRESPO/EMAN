import uuid
from flask import current_app
from models.produ_compr import produ_compr

class produ_comprService:
    def add(data):
        uuid_prco = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_produ_compr

            (prco_uuid, prco_cantidad, prco_com_id, prco_pro_id) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_prco, data["PRCO_CANTIDAD"], data["PRCO_COM_ID"], data["PRCO_PRO_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_prco, "PRCO_CANTIDAD": data["PRCO_CANTIDAD"],
                "COM_ID": data["PRCO_COM_ID"], "PRO_ID":data ["PRCO_PRO_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_produ_compr
            SET prco_uuid = %s, prco_cantidad = %s, prco_com_id = %s, prco_pro_id = %s
            WHERE prco_uuid = %s"""
            c.execute(query, (Info["PRCO_UUID"], Info["PRCO_CANTIDAD"], Info["PRCO_COM_ID"], Info["PRCO_PRO_ID"], Info["PRCO_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["PRCO_UUID"], "CANTIDAD": Info["PRCO_CANTIDAD"], "COM_ID": Info["PRCO_COM_ID"], "PRO_ID": Info["PRCO_PRO_ID"]}
            print(data)
            return data 

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_produ_compr WHERE prco_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_produ_compr"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [produ_compr(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
    
import uuid
from flask import current_app
from models.produc_carri import produc_carri

class produc_carriService:
    def add(data):
        uuid_proc = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_produc_carri

            (proc_uuid, proc_cantidad, proc_pro_id, proc_comc_id) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_proc, data["PROC_CANTIDAD"], data["PROC_PRO_ID"], data["PROC_COMC_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_proc, "CANTIDAD": data["PROC_CANTIDAD"],
                "PRO_ID": data["PROC_PRO_ID"], "COMC_ID":data ["PROC_COMC_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_produc_carri
            SET proc_uuid = %s, proc_cantidad = %s, proc_pro_id = %s, proc_comc_id = %s
            WHERE proc_uuid = %s"""
            c.execute(query, (Info["PROC_UUID"], Info["PROC_CANTIDAD"], Info["PROC_PRO_ID"], Info["PROC_COMC_ID"], Info["PROC_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["PROC_UUID"], "CANTIDAD": Info["PROC_CANTIDAD"], "PRO_ID": Info["PROC_PRO_ID"], "COMC_ID": Info["PROC_COMC_ID"]}
            print(data)
            return data 

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_produc_carri WHERE proc_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_produc_carri"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [produc_carri(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
    
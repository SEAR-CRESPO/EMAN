import uuid
from flask import current_app
from models.produc_carri import produc_carri

class produc_carriService:
    def add(data):
        uuid_proc = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_produc_carri

            (PROC_UUID, PROC_CANTIDAD, PROC_PRO_ID, PROC_COMC_ID) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_proc, data["CANTIDAD"], data["PRO_ID"], data["COMC_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_proc, "CANTIDAD": data["CANTIDAD"],
                "PRO_ID": data["PRO_ID"], "COMC_ID":data ["COMC_ID"]}
        return data

    def update():
        pass

    def delate():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT FROM * t_produc_carri"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [produc_carri(w[0],w[1],w[2],w[3],w[4]).to_dict() for w in data]

        return x
    
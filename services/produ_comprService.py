import uuid
from flask import current_app
from models.produ_compr import produ_compr

class produ_comprService:
    def add(data):
        uuid_prco = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_produ_compr

            (PRCO_UUID, PRCO_CANTIDAD, PRCO_COM_ID, PRCO_PRO_ID) VALUES
            (%s, %s, %s, %s)"""
        c.execute(query, (uuid_prco, data["CANTIDAD"], data["COM_ID"], data["PRO_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_prco, "CANTIDAD": data["CANTIDAD"],
                "COM_ID": data["COM_ID"], "PRO_ID":data ["PRO_ID"]}
        return data

    def update():
        pass

    # marca la posicion %s
    def update(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_produ_compr WHERE PRCO_UUID = %s"
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
    
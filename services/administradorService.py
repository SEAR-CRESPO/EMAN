import uuid
from flask import current_app
from models.administrador import administrador 

class administradorService:
    def add(data):
        uuid_adm = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_administrador

            (ADMI_UUID, ADMI_PER_ID) VALUES
            (%s, %s)"""
        c.execute(query, (uuid_adm, data["PER_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_adm, "PER_ID": data["PER_ID"]}
        return data

    
    # marca la posicion %s
    def update(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_administrador WHERE ADM_UUID = %s"
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
        query = "SELECT * FROM t_administrador"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [administrador(w[0],w[1],w[2]).to_dict() for w in data]

        return x
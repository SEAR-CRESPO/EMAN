import uuid
from flask import current_app
from models.administrador import administrador 

class administradorService:
    def add(data):
        uuid_adm = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_administrador

            (admi_uuid, adm_per_id) VALUES
            (%s, %s)"""
        c.execute(query, (uuid_adm, data["ADM_PER_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_adm, "PER_ID": data["ADM_PER_ID"]}
        return data

    
    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_administrador WHERE adm_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
    

    def update():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_administrador"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [administrador(w[0],w[1],w[2]).to_dict() for w in data]

        return x
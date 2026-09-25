import uuid
from flask import current_app
from models.ubicacion import ubicacion

class ubicacionService:
    def add(data):
        uuid_ubi = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_ubicacion
            (ubi_uuid, ubi_ciudad, ubi_barrio, ubi_direccion, ubi_dom_id) VALUES
            (%s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_ubi, data["UBI_CIUDAD"], data["UBI_BARRIO"], data["UBI_DIRECCION"], data["UBI_DOM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_ubi,
                "CIUDAD": data["UBI_CIUDAD"],
                "BARRIO": data["UBI_BARRIO"], "DIRECCION":data ["UBI_DIRECCION"],
                "DOM_ID": data["UBI_DOM_ID"] }
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_ubicacion
            SET ubi_uuid = %s, ubi_ciudad = %s, ubi_barrio = %s, ubi_direccion = %s, ubi_dom_id = %s
            WHERE ubi_uuid = %s"""
            c.execute(query, (Info["UBI_UUID"], Info["UBI_CIUDAD"], Info["UBI_BARRIO"], Info["UBI_DIRECCION"], Info["UBI_DOM_ID"], Info["UBI_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["UBI_UUID"], "CIUDAD": Info["UBI_CIUDAD"], "BARRIO": Info["UBI_BARRIO"], "DIRECCION": Info["UBI_DIRECCION"], "DOM_ID": Info["UBI_DOM_ID"]}
            print(data)
            return data 

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_ubicacion WHERE ubi_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_ubicacion"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [ubicacion(w[0],w[1],w[2],w[3],w[4],w[5]).to_dict() for w in data]

        return x
    
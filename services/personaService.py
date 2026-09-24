import uuid
from flask import current_app
from models.persona import persona

class personaService:
    def add(data):
        uuid_per = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        print(data)
        query = """INSERT INTO t_persona

            (per_uuid, per_contraseña, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_per, data["PER_CONTRASENA"], data["PER_NUMERO_DOCUMENTO"], data["PER_PRIMER_NOMBRE"], data["PER_SEGUNDO_NOMBRE"],
                           data["PER_PRIMER_APELLIDO"], data["PER_SEGUNDO_APELLIDO"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_per, "CONTRASENA": data["PER_CONTRASENA"],
                "NUMERO_DOCUMENTO": data["PER_NUMERO_DOCUMENTO"], "PRIMER_NOMBRE":data["PER_PRIMER_NOMBRE"],
                "SEGUNDO_NOMBRE": data["PER_SEGUNDO_NOMBRE"], "PRIMER_APELLIDO": data["PER_PRIMER_APELLIDO"],
                "SEGUNDO_APELLIDO": data["PER_SEGUNDO_APELLIDO"]}
        return data

     # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_persona WHERE PER_UUID = %s"
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
        query = "SELECT * FROM t_persona"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [persona(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7]).to_dict() for w in data]

        return x
    
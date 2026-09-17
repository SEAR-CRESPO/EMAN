import uuid
from flask import current_app
from models.tipo_genero import tipo_genero

class tipo_generoService:
    def add(data):
        uuid_gen = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_tipo_genero

            (gen_uuid, gen_genero, gen_pro_id) VALUES
            (%s, %s, %s)"""
        c.execute(query, (uuid_gen, data["GEN_GENERO"], data["GEN_PRO_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_gen, "GENERO": data["GEN_GENERO"],
                "PRO_ID": data["GENPRO_ID"]}
        return data

    def update():
        pass

    # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_tipo_genero WHERE gen_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_tipo_genero"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [tipo_genero(w[0],w[1],w[2],w[3]).to_dict() for w in data]

        return x
    
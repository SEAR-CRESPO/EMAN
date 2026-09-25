import uuid
from flask import current_app
from models.cliente import cliente

class clienteService:
    def add(data):
        uuid_cli = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_cliente

            (cli_uuid, cli_per_id) VALUES
            (%s, %s)"""
        c.execute(query, (uuid_cli, data["CLI_PER_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_cli, "PER_ID": data["CLI_PER_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_cliente
            SET cli_uuid = %s, cli_per_id = %s
            WHERE cli_uuid = %s"""
            c.execute(query, (Info["CLI_UUID"], Info["CLI_PER_ID"], Info["CLI_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["CLI_UUID"], "PER_ID": Info["CLI_PER_ID"]}
            print(data)
            return data 
    

     # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_cliente WHERE cli_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_cliente"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [cliente(w[0],w[1],w[2]).to_dict() for w in data]

        return x
import uuid
from flask import current_app
from models.cliente import cliente

class clienteService:
    def add(data):
        uuid_cli = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_cliente

            (CLI_UUID, CLI_PER_ID) VALUES
            (%s, %s)"""
        c.execute(query, (uuid_cli, data["PER_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_cli, "PER_ID": data["PER_ID"]}
        return data

    def update():
        pass
    

     # marca la posicion %s
    def update(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_cliente WHERE CLI_UUID = %s"
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
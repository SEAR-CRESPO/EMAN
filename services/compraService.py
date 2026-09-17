import uuid
from flask import current_app
from models.compra import compra

class compraService:
    def add(data):
        uuid_com = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_compra

            (com_uuid,com_numero_compra,com_metodo_entrega,com_fecha_compra,com_adm_id,com_cli_id) VALUES
            (%s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_com, data["COM_NUMERO_COMPRA"], data["COM_METODO_ENTREGA"], data["COM_FECHA_COMPRA"], data["COM_ADM_ID"], data["CON_ CLI_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_com,
                "NUMERO_COMPRA": data[" COM_NUMERO_COMPRA"],
                "METODO_ENTREGA": data["COM_METODO_ENTREGA"], "FECHA_COMPRA":data ["COM_FECHA_COMPRA"],
                "ADM_ID": data["COM_ADM_ID"], "COM_CLI_ID": data["COM_CLI_ID"]}
        return data

    def update():
        pass

     # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_compra WHERE com_uuid = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_compra"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [compra(w[0],w[1],w[2],w[3],w[4],w[5],w[6]).to_dict() for w in data]

        return x
    
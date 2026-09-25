import uuid
from flask import current_app
from models.pago import pago

class pagoService:
    def add(data):
        uuid_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()

        query = """INSERT INTO t_pago

            (pag_uuid, pag_numero_pago, pag_valor, pag_metodo, pag_estado, paga_fecha, pag_con_id) VALUES
            (%s, %s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_pag, data["PAG_NUMERO_PAGO"], data["PAG_VALOR"], data["PAG_METODO"], data["PAG_ESTADO"], data["PAG_FECHA"], data["PAG_COM_ID"]))

        current_app.mysql.connection.commit()

        ID = c.lastrowid
        data = {"ID": ID, "UUID": uuid_pag, "NUMERO_PAGO": data["PAG_NUMERO_PAGO"],
                "VALOR": data["PAG_VALOR"], "METODO":data ["PAG_METODO"],
                "ESTADO": data["PAG_ESTADO"], "FECHA": data["PAG_FECHA"],
                "COM_ID": data["PAG_COM_ID"]}
        return data

    def update(Info):
            c = current_app.mysql.connection.cursor()
            query = """
            UPDATE t_pago
            SET pag_uuid = %s, pag_numero_pago = %s, pag_valor = %s
            WHERE pag_uuid = %s"""
            c.execute(query, (Info["PAG_UUID"], Info["PAG_NUMERO_PAGO"], Info["PAG_VALOR"], Info["PAG_UUID"]))

            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                c.close()
                return {"mensaje": "no se encotro ese recurso o no se modifican datos"}
    
            c.close()
            data = {"UUID": Info["PAG_UUID"], "NUMERO_PAGO": Info["PAG_NUMERO_PAGO"], "VALOR": Info["PAG_VALOR"]}
            print(data)
            return data 

     # marca la posicion %s
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_pago WHERE PAG_UUID = %s"
        c.execute(query,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_pago"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [pago(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7]).to_dict() for w in data]

        return x
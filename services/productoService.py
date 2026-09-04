from models.producto import producto

# operaciones CRUD-> create, read, update, delete

class productoService:
    def add(brand,NOMBRE,TALLA,MARCA, DESCRIPCION, COLOR):
        uuid_producto = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO producto (PRO_UUID, PRO_CODIGO, PRO_NOMBRE, PRO_TALLA, PRO_MARCA, PRO_DESCRIPCION, PRO_COLOR) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        c.execute(query, (uuid_producto, brand, NOMBRE, TALLA, MARCA, DESCRIPCION, COLOR))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {"id": id,"uuid":uuid_producto,"brand":brand,"NOMBRE":NOMBRE,"TALLA":TALLA,"MARCA":MARCA,"DESCRIPCION":DESCRIPCION,"COLOR":COLOR}
    
        return data

    def update(PRO_ID, PRO_UUID, PRO_CODIGO, PRO_NOMBRE, PRO_TALLA, PRO_MARCA, PRO_DESCRIPCION, PRO_COLOR):
        pass

    def delete():
        pass

    def read():
        pass


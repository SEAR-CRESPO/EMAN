class producto:
    def __init__(self, PRO_ID, PRO_UUID, PRO_CODIGO, PRO_NOMBRE, PRO_TALLA, PRO_MARCA, PRO_DESCRIPCION, PRO_COLOR):
        self.PRO_ID        = PRO_ID
        self.PRO_UUID      = PRO_UUID
        self.PRO_CODIGO    = PRO_CODIGO
        self.NOMBRE        = PRO_NOMBRE
        self.TALLA         = PRO_TALLA
        self.PRO_MARCA     = PRO_MARCA
        self.PRO_DESCRIPCION = PRO_DESCRIPCION
        self.PRO_COLOR       = PRO_COLOR


    def to_dict(self):
        return{
            'PRO_ID'          : self.PRO_UUID,
            'PRO_UUID'        : self.PRO_UUID,
            'PRO_CODIGO'      : self.PRO_CODIGO,
            'PRO_NOMBRE'      : self.PRO_NOMBRE,
            'PRO_TALLA'       : self.PRO_TALLA,
            'PRO_MARCA'       : self.PRO_MARCA,
            'PRO_DESCRIPCION' : self.PRO_DESCRIPCION,
            'PRO_COLOR'       : self.PRO_COLOR
        }
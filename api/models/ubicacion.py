class ubicacion:
    def __init__(self, UBI_ID, UBI_UUID, UBI_CIUDAD, UBI_BARRIO, UBI_DIRECCION, UBI_DOM_ID):
        self.UBI_ID        = UBI_ID
        self.UBI_UUID      = UBI_UUID
        self.UBI_CIUDAD    = UBI_CIUDAD
        self.UBI_BARRIO    = UBI_BARRIO
        self.UBI_DIRECCION = UBI_DIRECCION
        self.UBI_DOM_ID    = UBI_DOM_ID



    def to_dict(self):
        return{
            'UBI_ID'       : self.UBI_ID,
            'UBI_UUID'     : self.UBI_UUID,
            'UBI_CIUDAD'   : self.UBI_CIUDAD,
            'UBI_BARRIO'   : self.UBI_BARRIO,
            'UBI_DIRECCION': self.UBI_DIRECCION,
            'UBI_DOM_ID'   : self.UBI_DOM_ID

        }

        
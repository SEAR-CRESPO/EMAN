class tipo_genero:
    def __init__(self, GEN_ID, GEN_UUID, GEN_GENERO, GEN_PRO_ID):
        self.GEN_ID     = GEN_ID
        self.GEN_UUID   = GEN_UUID
        self.GEN_GENERO = GEN_GENERO
        self.GEN_PRO_ID = GEN_PRO_ID



    def to_dict(self):
        return{
            'GEN_ID'     : self.GEN_ID,
            'GEN_UUID'   : self.GEN_UUID,
            'GEN_GENERO' : self.GEN_GENERO,
            'GEN_PRO_ID' : self.GEN_PRO_ID
        }
class carrit_compra:
    def __init__(self, COMC_ID, COMC_UUID, COMC_CODIGO, COMC_TOTAL_COMPRA, COMC_FECHA):
        self.COMC_ID           = COMC_ID
        self.COMC_UUID         = COMC_UUID
        self.COMC_CODIGO       = COMC_CODIGO
        self.COMC_TOTAL_COMPRA = COMC_TOTAL_COMPRA
        self.COMC_FECHA        = COMC_FECHA


    def to_dict(self):
        return{
            'COMC_ID'          : self.COMC_ID,
            'COMC_UUID'        : self.COMC_UUID,
            'COMC_CODIGO'      : self.COMC_CODIGO,
            'COMC_TOTAL_COMPRA': self.COMC_TOTAL_COMPRA,
            'COMC_FECHA'       : self.COMC_FECHA
        }
        
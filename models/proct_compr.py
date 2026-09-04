class produ_compr:
    def __init__(self, PRCO_ID, PRCO_UUID, PRCO_CANTIDAD, PRCO_COM_ID, PRCO_PRO_ID):
        self.PRCO_ID          = PRCO_ID
        self.PRCO_UUID        = PRCO_UUID
        self.PRCO_CANTIDAD    = PRCO_CANTIDAD
        self.PRCO_COM_ID      = PRCO_COM_ID
        self.PRCO_PRO_ID      = PRCO_PRO_ID



    def to_dict(self):
        return{
            'PRCO_ID'      : self.PRCO_ID,
            'PRCO_UUID'    : self.PRCO_UUID,
            'PRCO_CANTIDAD': self.PRCO_CANTIDAD,
            'PRCO_COM_ID'  : self.PRCO_COM_ID,
            'PRCO_PRO_ID'  : self.PRCO_PRO_ID
        }

        
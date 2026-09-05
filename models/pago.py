class pago:
    def __init__(self, PAG_ID, PAG_UUID, PAG_NUMERO_PAGO, PAG_VALOR, PAG_METODO, PAG_ESTADO, PAG_FECHA, PAG_COM_ID):
        self.PAG_ID          = PAG_ID
        self.PAG_UUID        = PAG_UUID
        self.PAG_NUMERO_PAGO = PAG_NUMERO_PAGO
        self.PAG_VALOR       = PAG_VALOR
        self.PAG_METODO      = PAG_METODO
        self.PAG_ESTADO      = PAG_ESTADO
        self.PAG_FECHA       = PAG_FECHA
        self.PAG_COM_ID      = PAG_COM_ID



    def to_dict(self):
        return{
            'PAG_ID'          : self.PAG_ID,
            'PAG_UUID'        : self.PAG_UUID,
            'PAG_NUMERO_PAGO' : self.PAG_NUMERO_PAGO,
            'PAG_VALOR'       : self.PAG_VALOR,
            'PAG_METODO'      : self.PAG_METODO,
            'PAG_ESTADO'      : self.PAG_ESTADO,
            'PAG_FECHA'       : self.PAG_FECHA,
            'PAG_COM_ID'      : self.PAG_COM_ID
        }
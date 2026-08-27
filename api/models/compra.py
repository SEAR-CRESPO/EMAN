class compra:
    def __init__(self, COM_ID, COM_UUID, COM_NUMERO_COMPRA, COM_METODO_ENTREGA, COM_FECHA_COMPRA, COM_ADM_ID, COM_CLI_ID):
        self.COM_ID             = COM_ID
        self.COM_UUID           = COM_UUID
        self.COM_NUMERO_COMPRA  = COM_NUMERO_COMPRA
        self.COM_METODO_ENTREGA = COM_METODO_ENTREGA
        self.COM_FECHA_COMPRA   = COM_FECHA_COMPRA
        self.COM_ADM_ID         = COM_ADM_ID
        self.COM_CLI_ID         = COM_CLI_ID



    def to_dict(self):
        return{
            'COM_ID'             : self.COM_ID,
            'COM_UUID'           : self.COM_UUID,
            'COM_NUMERO_COMPRA'  : self.COM_NUMERO_COMPRA,
            'COM_METODO_ENTREGA' : self.COM_METODO_ENTREGA,
            'COM_FECHA_COMPRA'   : self.COM_FECHA_COMPRA,
            'COM_ADM_ID'         : self.COM_ADM_ID,
            'COM_CLI_ID'         : self.COM_CLI_ID
        }
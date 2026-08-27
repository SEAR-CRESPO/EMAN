class domicilio:
    def __init__(self, DOM_ID, DOM_UUID, DOM_CODIGO, DOM_COM_ID):
        self.DOM_ID     = DOM_ID
        self.DOM_UUID   = DOM_UUID
        self.DOM_CODIGO = DOM_CODIGO
        self.DOM_COM_ID = DOM_COM_ID   


    def to_dict(self):
        return{
            'DOM_ID'    : self.DOM_ID,
            'DOM_UUID'  : self.DOM_UUID,
            'DOM_CODIGO': self.DOM_CODIGO,
            'DOM_COM_ID': self.DOM_COM_ID
        }
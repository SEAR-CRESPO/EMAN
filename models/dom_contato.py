class dom_contacto:
    def __init__(self, CON_ID, CON_UUID, CON_TIPO_CONTACTO, CON_VALOR, CON_DOM_ID):
        self.CON_ID            = CON_ID
        self.CON_UUID          = CON_UUID
        self.CON_TIPO_CONTACTO = CON_TIPO_CONTACTO
        self.CON_VALOR         = CON_VALOR
        self.CON_CON_DOM_ID    = CON_DOM_ID



    def to_dict(self):
        return{
            'CON_ID'            : self.CON_ID,
            'CON_UUID'          : self.CON_UUID,
            'CON_TIPO_CONTACTO' : self.CON_TIPO_CONTACTO,
            'CON_VALOR'         : self.CON_VALOR,
            'CON_CON_DOM_ID'    : self.CON_CON_DOM_ID
              
        }
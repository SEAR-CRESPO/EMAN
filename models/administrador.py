class administrador:
    def __init__(self, ADM_ID, ADM_UUID, ADM_PER_ID):
        self.ADM_ID     = ADM_ID
        self.ADM_UUID   = ADM_UUID
        self.ADM_PER_ID = ADM_PER_ID

    def to_dict(self):
        return{
            'ADM_ID'     : self.ADM_ID,
            'ADM_UUID'   : self.ADM_UUID,
            'ADM_PER_ID' : self.ADM_PER_ID
        }